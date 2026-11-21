"""Curated 180-citation Automated E-Commerce baseline (15 per chapter across Q1-Q12) mined strictly from verified Automated E-Commerce YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'321',
     '3pl',
     'ads',
     'amazon',
     'aov',
     'authorized',
     'automated',
     'automation',
     'avalara',
     'avoiding',
     'brand',
     'bundle',
     'business',
     'capital',
     'cash',
     'center',
     'certification',
     'chargeback',
     'churn',
     'client',
     'clients',
     'commerce',
     'contribution',
     'conversion',
     'cost',
     'cpsc',
     'creative',
     'cro',
     'customer',
     'customs',
     'cycle',
     'dealer',
     'dimensional',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'321',
     '3pl',
     'ads',
     'amazon',
     'aov',
     'authorized',
     'automated',
     'automation',
     'avalara',
     'avoiding',
     'brand',
     'budget',
     'bundle',
     'buyer',
     'capital',
     'cash',
     'center',
     'certification',
     'chargeback',
     'churn',
     'commerce',
     'contract',
     'contribution',
     'conversion',
     'cost',
     'cpsc',
     'creative',
     'cro',
     'customer',
     'customs',
     'cycle',
     'dealer',
     'decision',
     'dimensional',
     'escrow',
     'fee',
     'fees',
     'invoice',
     'pay',
     'payment',
     'pays',
     'retainer'},
 3: {'321',
     '3pl',
     'ads',
     'amazon',
     'aov',
     'authorized',
     'automated',
     'automation',
     'avalara',
     'avoiding',
     'brand',
     'bundle',
     'capital',
     'cash',
     'cashflow',
     'center',
     'certification',
     'chargeback',
     'churn',
     'commerce',
     'commission',
     'contribution',
     'conversion',
     'cost',
     'costs',
     'cpsc',
     'creative',
     'cro',
     'customer',
     'customs',
     'cycle',
     'dealer',
     'dimensional',
     'economics',
     'margin',
     'margins',
     'price',
     'pricing',
     'profit',
     'roi',
     'unit'},
 4: {'321',
     '3pl',
     'ads',
     'amazon',
     'aov',
     'authorized',
     'automated',
     'automation',
     'avalara',
     'avoiding',
     'brand',
     'budget',
     'bundle',
     'capital',
     'cash',
     'center',
     'certification',
     'chargeback',
     'churn',
     'commerce',
     'contribution',
     'conversion',
     'cost',
     'cpsc',
     'creative',
     'cro',
     'customer',
     'customs',
     'cycle',
     'dealer',
     'dimensional',
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
 5: {'321',
     '3pl',
     'ads',
     'amazon',
     'aov',
     'audit',
     'authorized',
     'automated',
     'automation',
     'avalara',
     'avoid',
     'avoiding',
     'brand',
     'bundle',
     'capital',
     'cash',
     'center',
     'certification',
     'chargeback',
     'churn',
     'clawback',
     'commerce',
     'contribution',
     'conversion',
     'cost',
     'cpsc',
     'creative',
     'cro',
     'customer',
     'customs',
     'cycle',
     'dealer',
     'dimensional',
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
 6: {'321',
     '3pl',
     'ads',
     'amazon',
     'aov',
     'authorized',
     'automated',
     'automation',
     'avalara',
     'avoiding',
     'brand',
     'bundle',
     'capital',
     'cash',
     'center',
     'certification',
     'chargeback',
     'churn',
     'client',
     'commerce',
     'contribution',
     'conversion',
     'cost',
     'cpsc',
     'creative',
     'cro',
     'customer',
     'customs',
     'cycle',
     'data',
     'deal',
     'dealer',
     'dimensional',
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
 7: {'321',
     '3pl',
     'ads',
     'amazon',
     'aov',
     'authorized',
     'automated',
     'automation',
     'avalara',
     'avoiding',
     'brand',
     'bundle',
     'capital',
     'cash',
     'center',
     'certification',
     'chargeback',
     'checklist',
     'churn',
     'commerce',
     'contribution',
     'conversion',
     'cost',
     'cpsc',
     'creative',
     'cro',
     'customer',
     'customs',
     'cycle',
     'dealer',
     'delivery',
     'dimensional',
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
 8: {'321',
     '3pl',
     'ads',
     'amazon',
     'aov',
     'api',
     'authorized',
     'automated',
     'automation',
     'avalara',
     'avoiding',
     'brand',
     'bundle',
     'capital',
     'cash',
     'center',
     'certification',
     'chargeback',
     'churn',
     'commerce',
     'contribution',
     'conversion',
     'cost',
     'cpsc',
     'creative',
     'crm',
     'cro',
     'customer',
     'customs',
     'cycle',
     'data',
     'database',
     'dealer',
     'dimensional',
     'platform',
     'portal',
     'scraper',
     'search',
     'software',
     'tool',
     'tools',
     'tracking'},
 9: {'321',
     '3pl',
     'ads',
     'agreement',
     'amazon',
     'aov',
     'authorized',
     'automated',
     'automation',
     'avalara',
     'avoiding',
     'brand',
     'bundle',
     'capital',
     'cash',
     'center',
     'certification',
     'chargeback',
     'churn',
     'commerce',
     'compliance',
     'contract',
     'contribution',
     'conversion',
     'cost',
     'cpsc',
     'creative',
     'cro',
     'customer',
     'customs',
     'cycle',
     'dealer',
     'dimensional',
     'disclosure',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'321',
      '3pl',
      'ads',
      'agent',
      'ai',
      'amazon',
      'aov',
      'authorized',
      'automate',
      'automated',
      'automation',
      'avalara',
      'avoiding',
      'brand',
      'bundle',
      'capital',
      'cash',
      'center',
      'certification',
      'chargeback',
      'churn',
      'commerce',
      'contribution',
      'conversion',
      'cost',
      'cpsc',
      'creative',
      'cro',
      'customer',
      'customs',
      'cycle',
      'dashboard',
      'dealer',
      'dimensional',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'321',
      '3pl',
      'ads',
      'amazon',
      'aov',
      'authorized',
      'automated',
      'automation',
      'avalara',
      'avoiding',
      'brand',
      'bundle',
      'capital',
      'cash',
      'center',
      'certification',
      'chargeback',
      'churn',
      'commerce',
      'contractor',
      'contribution',
      'conversion',
      'cost',
      'cpsc',
      'creative',
      'cro',
      'customer',
      'customs',
      'cycle',
      'dealer',
      'dimensional',
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
 12: {'321',
      '3pl',
      'action',
      'ads',
      'amazon',
      'aov',
      'authorized',
      'automated',
      'automation',
      'avalara',
      'avoiding',
      'brand',
      'bundle',
      'capital',
      'cash',
      'center',
      'certification',
      'chargeback',
      'churn',
      'commerce',
      'contribution',
      'conversion',
      'cost',
      'cpsc',
      'creative',
      'cro',
      'customer',
      'customs',
      'cycle',
      'day',
      'days',
      'dealer',
      'dimensional',
      'launch',
      'milestone',
      'month',
      'plan',
      'roadmap',
      'sprint',
      'start',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Noah Haynes',
      'channel': 'Noah Haynes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:52](https://www.youtube.com/watch?v=SjGeVqhkKPw&t=172s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, let's say you found a big growing market. That brings us to the second "
              'system, your business model. And this is where you need to understand unit '
              'economics. The first is your AOV, or average order value, which is how much '
              'your average customer spends per order.',
      'timestamp': 172,
      'timestamp_label': '[00:02:52]',
      'timestamp_seconds': 172,
      'tip': "So, let's say you found a big growing market. That brings us to the second "
             'system, your business model. And this is where you need to understand unit '
             'economics. The first is your AOV, or average order value, which is how much your '
             'average customer spends per order.',
      'title': 'Scaling an Ecommerce Brand Is Hard Until You Understand These 3 Systems (Noah '
               'Haynes)',
      'url': 'https://www.youtube.com/watch?v=SjGeVqhkKPw&t=172s',
      'video_id': 'SjGeVqhkKPw'},
     {'author': 'Ecommerce Paradise | High Ticket Dropshipping',
      'channel': 'Ecommerce Paradise | High Ticket Dropshipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:19](https://www.youtube.com/watch?v=EaAeDMJIPLQ&t=259s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s going to make you, you know, way more money. So the biggest difference "
              'between this business model and other drop shipping business models really is '
              'that authorized dealer agreement you have with the brand.',
      'timestamp': 259,
      'timestamp_label': '[00:04:19]',
      'timestamp_seconds': 259,
      'tip': "'s going to make you, you know, way more money. So the biggest difference "
             'between this business model and other drop shipping business models really is '
             'that authorized dealer agreement you have with the brand.',
      'title': 'What Is High Ticket Dropshipping? Complete Beginner Guide (2026) (Ecommerce '
               'Paradise | High Ticket Dropshipping)',
      'url': 'https://www.youtube.com/watch?v=EaAeDMJIPLQ&t=259s',
      'video_id': 'EaAeDMJIPLQ'},
     {'author': 'Kurtis Hanni',
      'channel': 'Kurtis Hanni',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=0WBeNhRVKHY&t=118s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And every business cycle is different. Sometimes in service businesses, you '
              "have arrangements that are pay when paid, meaning you don't have to pay the "
              'contractor or the person doing the work until you have p been paid by your '
              'customer.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': 'And every business cycle is different. Sometimes in service businesses, you have '
             "arrangements that are pay when paid, meaning you don't have to pay the "
             'contractor or the person doing the work until you have p been paid by your '
             'customer.',
      'title': 'You’re Not Broke, Your Cash Is Just Stuck (Cash Conversion Cycle Explained) '
               '(Kurtis Hanni)',
      'url': 'https://www.youtube.com/watch?v=0WBeNhRVKHY&t=118s',
      'video_id': '0WBeNhRVKHY'},
     {'author': 'InstructorTom',
      'channel': 'InstructorTom',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:23](https://www.youtube.com/watch?v=Ju1MGgf9RUw&t=443s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Could at least see the value of doing so and if we were too hard on our '
              'customers and making them pay in a very short time we may lose customers at '
              'least we can measure the effects of the cash conversion cycle thanks for '
              'watching.',
      'timestamp': 443,
      'timestamp_label': '[00:07:23]',
      'timestamp_seconds': 443,
      'tip': 'Could at least see the value of doing so and if we were too hard on our '
             'customers and making them pay in a very short time we may lose customers at '
             'least we can measure the effects of the cash conversion cycle thanks for '
             'watching.',
      'title': 'Video   Cash Conversion Cycle (InstructorTom)',
      'url': 'https://www.youtube.com/watch?v=Ju1MGgf9RUw&t=443s',
      'video_id': 'Ju1MGgf9RUw'},
     {'author': 'Peak Flow Media',
      'channel': 'Peak Flow Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:52](https://www.youtube.com/watch?v=YmrOjrklnxM&t=112s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Model also known as high toet e-commerce and what this business model entails '
              'is finding products from the United States and becoming a no inventory '
              'authorized.',
      'timestamp': 112,
      'timestamp_label': '[00:01:52]',
      'timestamp_seconds': 112,
      'tip': 'Model also known as high toet e-commerce and what this business model entails is '
             'finding products from the United States and becoming a no inventory authorized.',
      'title': 'What is High Ticket Dropshipping and Common FAQs (Peak Flow Media)',
      'url': 'https://www.youtube.com/watch?v=YmrOjrklnxM&t=112s',
      'video_id': 'YmrOjrklnxM'},
     {'author': 'Eric Andrews',
      'channel': 'Eric Andrews',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:59](https://www.youtube.com/watch?v=gG33a-ErNRQ&t=779s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Product launches and so the customer lifetime value is now 3.1 orders so our '
              'contribution margin to CAC ratio is 2.1 and LTV to CAC ratio is 6.7.',
      'timestamp': 779,
      'timestamp_label': '[00:12:59]',
      'timestamp_seconds': 779,
      'tip': 'Product launches and so the customer lifetime value is now 3.1 orders so our '
             'contribution margin to CAC ratio is 2.1 and LTV to CAC ratio is 6.7.',
      'title': 'Unit Economics Benchmarks for eCommerce | From Idea to Exit (Eric Andrews)',
      'url': 'https://www.youtube.com/watch?v=gG33a-ErNRQ&t=779s',
      'video_id': 'gG33a-ErNRQ'},
     {'author': 'Joe Verschoor',
      'channel': 'Joe Verschoor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:48](https://www.youtube.com/watch?v=uxvzRhKmdXU&t=588s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '100% of my clients have seen a sale within the first 2 weeks of launching. '
              "That's just what's been observed. And in fact, I had a client get her first "
              'sale before even running ads a couple weeks ago for 33 plus thousand dollars on '
              'a single order.',
      'timestamp': 588,
      'timestamp_label': '[00:09:48]',
      'timestamp_seconds': 588,
      'tip': '100% of my clients have seen a sale within the first 2 weeks of launching. '
             "That's just what's been observed. And in fact, I had a client get her first sale "
             'before even running ads a couple weeks ago for 33 plus thousand dollars on a '
             'single order.',
      'title': 'How to Choose a High Ticket Dropshipping Niche in 2026 (Joe Verschoor)',
      'url': 'https://www.youtube.com/watch?v=uxvzRhKmdXU&t=588s',
      'video_id': 'uxvzRhKmdXU'},
     {'author': 'Arthur Glinkin',
      'channel': 'Arthur Glinkin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=1Cr_iHc8p4s&t=38s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, real quick, my name's Arthur. I'm a certified pro adviser inside of "
              "QuickBooks Online. I'm also the owner of SMG Bookkeeping, an accounting and "
              'bookkeeping firm that works specifically with e-commerce clients to help '
              'streamline their accounting on the back end.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': "So, real quick, my name's Arthur. I'm a certified pro adviser inside of "
             "QuickBooks Online. I'm also the owner of SMG Bookkeeping, an accounting and "
             'bookkeeping firm that works specifically with e-commerce clients to help '
             'streamline their accounting on the back end.',
      'title': 'Ecommerce Sales Tax MADE EASY (TaxJar Setup) (Arthur Glinkin)',
      'url': 'https://www.youtube.com/watch?v=1Cr_iHc8p4s&t=38s',
      'video_id': '1Cr_iHc8p4s'},
     {'author': 'Enterprise Industry Network',
      'channel': 'Enterprise Industry Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:47](https://www.youtube.com/watch?v=axmEedpIF1E&t=47s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They do not want to buy the business and then immediately inject more cash just '
              'to fund payroll, inventory, or receivables gaps. That is where the adjustment '
              'comes in. During the deal process, buyer and seller usually agree on a target '
              'working capital amount.',
      'timestamp': 47,
      'timestamp_label': '[00:00:47]',
      'timestamp_seconds': 47,
      'tip': 'They do not want to buy the business and then immediately inject more cash just '
             'to fund payroll, inventory, or receivables gaps. That is where the adjustment '
             'comes in. During the deal process, buyer and seller usually agree on a target '
             'working capital amount.',
      'title': 'Working Capital Adjustments in a Business Sale | EIN Business Brokers | '
               'Enterprise Industry Network (Enterprise Industry Network)',
      'url': 'https://www.youtube.com/watch?v=axmEedpIF1E&t=47s',
      'video_id': 'axmEedpIF1E'},
     {'author': 'Report Pundit',
      'channel': 'Report Pundit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=bX6lGJtCxao&t=88s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Inventory on hand in report pundit. Add columns like cost and current value and '
              'schedule to email or Google Sheets. So the team starts the day with stock '
              'reality. Grade products A or B or C by their share of revenue in your selected '
              'window.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'Inventory on hand in report pundit. Add columns like cost and current value and '
             'schedule to email or Google Sheets. So the team starts the day with stock '
             'reality. Grade products A or B or C by their share of revenue in your selected '
             'window.',
      'title': 'Shopify Inventory Tracking Guide: ABC Analysis, Bundles & Stock Alerts (Report '
               'Pundit)',
      'url': 'https://www.youtube.com/watch?v=bX6lGJtCxao&t=88s',
      'video_id': 'bX6lGJtCxao'},
     {'author': 'Emiel Dingemans | eCommerce Retention Marketing',
      'channel': 'Emiel Dingemans | eCommerce Retention Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=6OklvvWTGmw&t=15s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In this video I walk you to the exact flows we use at magically to generate '
              'consistent automated revenue for our clients including seven eight and nine.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'In this video I walk you to the exact flows we use at magically to generate '
             'consistent automated revenue for our clients including seven eight and nine.',
      'title': 'Klaviyo Flows Tutorial For Beginners (2025 Full Course for Shopify) (Emiel '
               'Dingemans | eCommerce Retention Marketing)',
      'url': 'https://www.youtube.com/watch?v=6OklvvWTGmw&t=15s',
      'video_id': '6OklvvWTGmw'},
     {'author': 'CTLGlobalSolutions',
      'channel': 'CTLGlobalSolutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:01](https://www.youtube.com/watch?v=i9PB8pM9lZ4&t=61s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Clients can call their account managers directly. Many of them are set up on '
              "Teams. It's really important to us that the account management team is an "
              'extension of the client and that the client feels that they are part of their '
              'team as well.',
      'timestamp': 61,
      'timestamp_label': '[00:01:01]',
      'timestamp_seconds': 61,
      'tip': 'Clients can call their account managers directly. Many of them are set up on '
             "Teams. It's really important to us that the account management team is an "
             'extension of the client and that the client feels that they are part of their '
             'team as well.',
      'title': '3PL Fulfillment Built for Scaling Brands | CTL (CTLGlobalSolutions)',
      'url': 'https://www.youtube.com/watch?v=i9PB8pM9lZ4&t=61s',
      'video_id': 'i9PB8pM9lZ4'},
     {'author': 'CartonCloud',
      'channel': 'CartonCloud',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:19](https://www.youtube.com/watch?v=EYQU96qv5rk&t=19s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Become a proper three pearl operation that was our overall objective at the '
              'same time our business was evolving so suddenly we had 40 clients.',
      'timestamp': 19,
      'timestamp_label': '[00:00:19]',
      'timestamp_seconds': 19,
      'tip': 'Become a proper three pearl operation that was our overall objective at the same '
             'time our business was evolving so suddenly we had 40 clients.',
      'title': '3PL warehouse B2C x CartonCloud case study (CartonCloud)',
      'url': 'https://www.youtube.com/watch?v=EYQU96qv5rk&t=19s',
      'video_id': 'EYQU96qv5rk'},
     {'author': 'WatchMeDropship',
      'channel': 'WatchMeDropship',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:35](https://www.youtube.com/watch?v=xJp0s6G8Hew&t=1715s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Want to focus like I said on the make the model the brand and and what it is in '
              'combination with that not just golf simulator.',
      'timestamp': 1715,
      'timestamp_label': '[00:28:35]',
      'timestamp_seconds': 1715,
      'tip': 'Want to focus like I said on the make the model the brand and and what it is in '
             'combination with that not just golf simulator.',
      'title': 'High Ticket Product Research & USA Based Wholesale Dropshipping Suppliers '
               '(WatchMeDropship)',
      'url': 'https://www.youtube.com/watch?v=xJp0s6G8Hew&t=1715s',
      'video_id': 'xJp0s6G8Hew'},
     {'author': 'Kai Cromwell - eCommerce SEO',
      'channel': 'Kai Cromwell - eCommerce SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=61mBGqDsSo4&t=111s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re just like drop shipping from other brands, you're going to crush because "
              "people's vices are typically lifetime vices. So, you will have that client for "
              'years to come.',
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': "'re just like drop shipping from other brands, you're going to crush because "
             "people's vices are typically lifetime vices. So, you will have that client for "
             'years to come.',
      'title': '5 Best High Ticket SEO Dropshipping Niches for 2025 (Kai Cromwell - eCommerce '
               'SEO)',
      'url': 'https://www.youtube.com/watch?v=61mBGqDsSo4&t=111s',
      'video_id': '61mBGqDsSo4'}],
 2: [{'author': 'Marketing Business Network',
      'channel': 'Marketing Business Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=C5Ut79jWwHA&t=134s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Likewise, keeping too little stock can leave customers waiting and cost the '
              'company sales. Some businesses collect customer money before they pay '
              'suppliers, producing a negative cash conversion cycle. That describes payment '
              'timing, not a loss.',
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': 'Likewise, keeping too little stock can leave customers waiting and cost the '
             'company sales. Some businesses collect customer money before they pay suppliers, '
             'producing a negative cash conversion cycle. That describes payment timing, not a '
             'loss.',
      'title': 'What is the Cash Conversion Cycle? (Marketing Business Network)',
      'url': 'https://www.youtube.com/watch?v=C5Ut79jWwHA&t=134s',
      'video_id': 'C5Ut79jWwHA'},
     {'author': 'Adam Callinan',
      'channel': 'Adam Callinan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:35](https://www.youtube.com/watch?v=VCXWZQgbKXw&t=575s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Think of cost of goods sold, shipping and fulfillment to the customer, credit '
              'card fees, Shopify fees, Amazon fees, all the stuff that you pay when you sell '
              'a product.',
      'timestamp': 575,
      'timestamp_label': '[00:09:35]',
      'timestamp_seconds': 575,
      'tip': 'Think of cost of goods sold, shipping and fulfillment to the customer, credit '
             'card fees, Shopify fees, Amazon fees, all the stuff that you pay when you sell a '
             'product.',
      'title': 'The Only Video You Need to Scale Your Ecommerce Brand to 8 Figures (Adam '
               'Callinan)',
      'url': 'https://www.youtube.com/watch?v=VCXWZQgbKXw&t=575s',
      'video_id': 'VCXWZQgbKXw'},
     {'author': 'RRA Group | Freight Forwarding & Logistics',
      'channel': 'RRA Group | Freight Forwarding & Logistics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=007vdtJ5XrY&t=87s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That landed cost per unit is what to compare with the selling price. So: start '
              'with the invoice, add freight, insurance and fees, get duties and taxes '
              'estimated by a customs broker, and mark your estimates. Next: why freight '
              'quotes expire.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': 'That landed cost per unit is what to compare with the selling price. So: start '
             'with the invoice, add freight, insurance and fees, get duties and taxes '
             'estimated by a customs broker, and mark your estimates. Next: why freight quotes '
             'expire.',
      'title': 'Build a Landed-Cost Estimate: A Canadian Import Example (RRA Group | Freight '
               'Forwarding & Logistics)',
      'url': 'https://www.youtube.com/watch?v=007vdtJ5XrY&t=87s',
      'video_id': '007vdtJ5XrY'},
     {'author': 'ZIK Analytics',
      'channel': 'ZIK Analytics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:02](https://www.youtube.com/watch?v=7GY4PPBU0GY&t=362s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In this case, the buyer is responsible for paying the return shipping cost. '
              'Once the item is received, you can issue the refund. While this method is '
              "common, it can lead to a negative customer experience and may harm your brand's "
              'reputation.',
      'timestamp': 362,
      'timestamp_label': '[00:06:02]',
      'timestamp_seconds': 362,
      'tip': 'In this case, the buyer is responsible for paying the return shipping cost. Once '
             'the item is received, you can issue the refund. While this method is common, it '
             "can lead to a negative customer experience and may harm your brand's reputation.",
      'title': 'How To Handle Returns & Refunds on Shopify | 2026 Shipping Tutorial (ZIK '
               'Analytics)',
      'url': 'https://www.youtube.com/watch?v=7GY4PPBU0GY&t=362s',
      'video_id': '7GY4PPBU0GY'},
     {'author': 'Acuity Ecommerce Accounting',
      'channel': 'Acuity Ecommerce Accounting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:26](https://www.youtube.com/watch?v=8zfPSv7hAWM&t=746s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you have just a little bit of volume you'll be a smaller fee if you have a "
              "lot of volume you'll pay higher fees so you'll have to check out the pricing.",
      'timestamp': 746,
      'timestamp_label': '[00:12:26]',
      'timestamp_seconds': 746,
      'tip': "If you have just a little bit of volume you'll be a smaller fee if you have a "
             "lot of volume you'll pay higher fees so you'll have to check out the pricing.",
      'title': 'Avalara TaxJar Taxify | Sales Tax Solutions for Ecommerce Sellers (Acuity '
               'Ecommerce Accounting)',
      'url': 'https://www.youtube.com/watch?v=8zfPSv7hAWM&t=746s',
      'video_id': '8zfPSv7hAWM'},
     {'author': 'CFOmarketIQ',
      'channel': 'CFOmarketIQ',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:22](https://www.youtube.com/watch?v=nUu4s78pX8E&t=142s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Customer pricing, and whether your contracts let you pass any of it through. '
              "And then there's cash, because you pay the duty when the goods come in, long "
              'before you sell them. So a tariff change can squeeze your cash a quarter before '
              'it ever shows up in the P&L.',
      'timestamp': 142,
      'timestamp_label': '[00:02:22]',
      'timestamp_seconds': 142,
      'tip': 'Customer pricing, and whether your contracts let you pass any of it through. And '
             "then there's cash, because you pay the duty when the goods come in, long before "
             'you sell them. So a tariff change can squeeze your cash a quarter before it ever '
             'shows up in the P&L.',
      'title': 'Tariff news and your landed cost (CFOmarketIQ)',
      'url': 'https://www.youtube.com/watch?v=nUu4s78pX8E&t=142s',
      'video_id': 'nUu4s78pX8E'},
     {'author': 'Shipping Solutions',
      'channel': 'Shipping Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:46](https://www.youtube.com/watch?v=4868R7AGDp0&t=346s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Click on the plus sign to see the detail for each country. For Canada, if my '
              'goods qualify for the USMCA, then I only pay the cost of the goods plus freight '
              'and a small merchandise processing fee and harbor maintenance fee.',
      'timestamp': 346,
      'timestamp_label': '[00:05:46]',
      'timestamp_seconds': 346,
      'tip': 'Click on the plus sign to see the detail for each country. For Canada, if my '
             'goods qualify for the USMCA, then I only pay the cost of the goods plus freight '
             'and a small merchandise processing fee and harbor maintenance fee.',
      'title': 'Landed Cost Calculator: Compare Tariffs, Duties & Fees from Multiple Countries '
               '(Shipping Solutions)',
      'url': 'https://www.youtube.com/watch?v=4868R7AGDp0&t=346s',
      'video_id': '4868R7AGDp0'},
     {'author': 'Learn With Shopify',
      'channel': 'Learn With Shopify',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:14](https://www.youtube.com/watch?v=088tKYu7kKY&t=434s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Pick and pack rates per order makes 3pls cost prohibitive by pick and pack rate '
              'i mean the fee the 3pl charges you for each item that they.',
      'timestamp': 434,
      'timestamp_label': '[00:07:14]',
      'timestamp_seconds': 434,
      'tip': 'Pick and pack rates per order makes 3pls cost prohibitive by pick and pack rate '
             'i mean the fee the 3pl charges you for each item that they.',
      'title': 'Ecommerce Shipping and Fulfillment: A Complete Guide (Learn With Shopify)',
      'url': 'https://www.youtube.com/watch?v=088tKYu7kKY&t=434s',
      'video_id': '088tKYu7kKY'},
     {'author': "Jim's Ecommerce Tutorials",
      'channel': "Jim's Ecommerce Tutorials",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=HPTGnp51Iks&t=120s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Next, review the exchange amount and any payment difference. Depending on the '
              'products involved, the customer may need to pay more, receive a partial refund, '
              'or have a balance adjusted.',
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': 'Next, review the exchange amount and any payment difference. Depending on the '
             'products involved, the customer may need to pay more, receive a partial refund, '
             'or have a balance adjusted.',
      'title': "How To Process Shopify Returns And Exchanges (Easy Guide) (Jim's Ecommerce "
               'Tutorials)',
      'url': 'https://www.youtube.com/watch?v=HPTGnp51Iks&t=120s',
      'video_id': 'HPTGnp51Iks'},
     {'author': 'Novutech',
      'channel': 'Novutech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:53](https://www.youtube.com/watch?v=kjk-aLs-t1g&t=1673s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um everything is is down there. So this webop as well because it's the test web "
              'shop it also gives me the option to pay by bank deposits which is uh makes it '
              'easy for us to actually not having to fill out all the payment details.',
      'timestamp': 1673,
      'timestamp_label': '[00:27:53]',
      'timestamp_seconds': 1673,
      'tip': "Um everything is is down there. So this webop as well because it's the test web "
             'shop it also gives me the option to pay by bank deposits which is uh makes it '
             'easy for us to actually not having to fill out all the payment details.',
      'title': 'Shopify orders in NetSuite with 3PL fulfillment (Novutech)',
      'url': 'https://www.youtube.com/watch?v=kjk-aLs-t1g&t=1673s',
      'video_id': 'kjk-aLs-t1g'},
     {'author': 'Carbon Box Media',
      'channel': 'Carbon Box Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:54](https://www.youtube.com/watch?v=wFXlLgdV31A&t=714s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '500 or $1,000 for the platform and an agency fee or you do it in house, the '
              'email will always always be 10x to us or whatever you pay, whatever you pay.',
      'timestamp': 714,
      'timestamp_label': '[00:11:54]',
      'timestamp_seconds': 714,
      'tip': '500 or $1,000 for the platform and an agency fee or you do it in house, the '
             'email will always always be 10x to us or whatever you pay, whatever you pay.',
      'title': 'How to 3x Your Email Revenue (Shopify Brand Case Study) | Lifecycle Talks '
               '(Carbon Box Media)',
      'url': 'https://www.youtube.com/watch?v=wFXlLgdV31A&t=714s',
      'video_id': 'wFXlLgdV31A'},
     {'author': 'A Simple Model',
      'channel': 'A Simple Model',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:10](https://www.youtube.com/watch?v=8qsUvwoLJHw&t=370s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Result in a working capital adjustment of 2.5 million dollars in the buyer's "
              'favor because you have a working capital peg of 4 million dollars and a january '
              'balance of networking capital equal to 1.5 million.',
      'timestamp': 370,
      'timestamp_label': '[00:06:10]',
      'timestamp_seconds': 370,
      'tip': "Result in a working capital adjustment of 2.5 million dollars in the buyer's "
             'favor because you have a working capital peg of 4 million dollars and a january '
             'balance of networking capital equal to 1.5 million.',
      'title': 'The Working Capital Peg for a Seasonal Business (A Simple Model)',
      'url': 'https://www.youtube.com/watch?v=8qsUvwoLJHw&t=370s',
      'video_id': '8qsUvwoLJHw'},
     {'author': 'Carles Fos',
      'channel': 'Carles Fos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:20](https://www.youtube.com/watch?v=6joO-M0xN0k&t=320s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Marcas es que simplemente cogen estos productos y hacen una campaña de Google '
              'Shopping en Google ads y esto está mal por qué Porque esos datos que vamos a.',
      'timestamp': 320,
      'timestamp_label': '[00:05:20]',
      'timestamp_seconds': 320,
      'tip': 'Marcas es que simplemente cogen estos productos y hacen una campaña de Google '
             'Shopping en Google ads y esto está mal por qué Porque esos datos que vamos a.',
      'title': '🚀 Optimiza Tu Feed en Google Merchant Center | Guía Completa para Más Ventas 💰 '
               '(Carles Fos)',
      'url': 'https://www.youtube.com/watch?v=6joO-M0xN0k&t=320s',
      'video_id': '6joO-M0xN0k'},
     {'author': 'Zero To Sale',
      'channel': 'Zero To Sale',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=Cy4Xvc1vYac&t=22s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Amazon हमारी इनवॉइस के अंदर क्या चीजें देखता है। हमारी इनवॉइस के अंदर ऐसी कौन '
              'सी चीजें होनी चाहिए कि Amazon उसको एक्सेप्ट करें। ठीक है?',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'Amazon हमारी इनवॉइस के अंदर क्या चीजें देखता है। हमारी इनवॉइस के अंदर ऐसी कौन सी '
             'चीजें होनी चाहिए कि Amazon उसको एक्सेप्ट करें। ठीक है?',
      'title': 'Amazon Wholesale FBA invoice requirements explained (Zero To Sale)',
      'url': 'https://www.youtube.com/watch?v=Cy4Xvc1vYac&t=22s',
      'video_id': 'Cy4Xvc1vYac'},
     {'author': 'Prediko AI Inventory Management',
      'channel': 'Prediko AI Inventory Management',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=9Gx9hcJhdbo&t=21s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And after that, we're going to begin the onboarding. Um, in the meantime, I'll "
              'just give a quick introduction. I manage customer success in Predico for our UK '
              'and AMIA region. And joining me today is Isaiah who manages customer success '
              'for our US region.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "And after that, we're going to begin the onboarding. Um, in the meantime, I'll "
             'just give a quick introduction. I manage customer success in Predico for our UK '
             'and AMIA region. And joining me today is Isaiah who manages customer success for '
             'our US region.',
      'title': 'How to Set Up Prediko: Shopify Inventory Forecasting, Purchase Orders & AI '
               'Planning (Onboarding) (Prediko AI Inventory Management)',
      'url': 'https://www.youtube.com/watch?v=9Gx9hcJhdbo&t=21s',
      'video_id': '9Gx9hcJhdbo'}],
 3: [{'author': 'Mark Builds Brands Highlights',
      'channel': 'Mark Builds Brands Highlights',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:01](https://www.youtube.com/watch?v=eTADhJ3N_oo&t=181s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Gross profit per unit, all right? Basically, the the product price what you're "
              'selling it for minus the total product cost, which is going to be these two '
              'cells right here. Next, gross margin percentage.',
      'timestamp': 181,
      'timestamp_label': '[00:03:01]',
      'timestamp_seconds': 181,
      'tip': "Gross profit per unit, all right? Basically, the the product price what you're "
             'selling it for minus the total product cost, which is going to be these two '
             'cells right here. Next, gross margin percentage.',
      'title': 'unit economics for ecom explained (boring as hell, but prints $$$) (Mark '
               'Builds Brands Highlights)',
      'url': 'https://www.youtube.com/watch?v=eTADhJ3N_oo&t=181s',
      'video_id': 'eTADhJ3N_oo'},
     {'author': 'Intel by CandiMentor',
      'channel': 'Intel by CandiMentor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=CvHvBnjwlJg&t=30s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Freight, insurance, customs charges, and receiving expenses can all increase '
              'what each unit truly costs you. Purchase price tells you what the supplier '
              'charges. Landed cost tells you what the product costs after it has traveled '
              'through the entire inbound supply chain.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'Freight, insurance, customs charges, and receiving expenses can all increase '
             'what each unit truly costs you. Purchase price tells you what the supplier '
             'charges. Landed cost tells you what the product costs after it has traveled '
             'through the entire inbound supply chain.',
      'title': 'Landed Cost Calculation Explained (Intel by CandiMentor)',
      'url': 'https://www.youtube.com/watch?v=CvHvBnjwlJg&t=30s',
      'video_id': 'CvHvBnjwlJg'},
     {'author': 'Marcus Lam | High Ticket Dropshipping (AI)',
      'channel': 'Marcus Lam | High Ticket Dropshipping (AI)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:19](https://www.youtube.com/watch?v=ic0HLQbBhQA&t=679s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I have a video that explains what map pricing is. Minimum advertising price '
              'that prevents people from going price war with you. You will have the dealer '
              'cost. You will have your market price.',
      'timestamp': 679,
      'timestamp_label': '[00:11:19]',
      'timestamp_seconds': 679,
      'tip': 'I have a video that explains what map pricing is. Minimum advertising price that '
             'prevents people from going price war with you. You will have the dealer cost. '
             'You will have your market price.',
      'title': 'What is an Authorized Dealer? High Ticket Dropshipping (Marcus Lam | High '
               'Ticket Dropshipping (AI))',
      'url': 'https://www.youtube.com/watch?v=ic0HLQbBhQA&t=679s',
      'video_id': 'ic0HLQbBhQA'},
     {'author': 'SKUio',
      'channel': 'SKUio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=DFZ8XDRkuCE&t=20s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The duty rates are illustrative too, so confirm real rates with your customs '
              'broker. Brands like this often price a piece on its factory cost. The duty '
              "shows up weeks later, on the customs broker's bill. Until then, every margin "
              'report looks better than the truth.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'The duty rates are illustrative too, so confirm real rates with your customs '
             'broker. Brands like this often price a piece on its factory cost. The duty shows '
             "up weeks later, on the customs broker's bill. Until then, every margin report "
             'looks better than the truth.',
      'title': 'Jewelry Landed Cost: Duty, Sets and True Margin, from PO to Sale (SKUio)',
      'url': 'https://www.youtube.com/watch?v=DFZ8XDRkuCE&t=20s',
      'video_id': 'DFZ8XDRkuCE'},
     {'author': 'Asonjf',
      'channel': 'Asonjf',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:13](https://www.youtube.com/watch?v=r79NEO4JF2M&t=613s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '20%, but it can even lower to 15%. All right, guys, you guys will see your '
              'margins will actually increase based on the ticket price of your product. So, '
              'the higher the ticket price, likely the higher the profit you will actually '
              'receive as a dealer.',
      'timestamp': 613,
      'timestamp_label': '[00:10:13]',
      'timestamp_seconds': 613,
      'tip': '20%, but it can even lower to 15%. All right, guys, you guys will see your '
             'margins will actually increase based on the ticket price of your product. So, '
             'the higher the ticket price, likely the higher the profit you will actually '
             'receive as a dealer.',
      'title': 'How To Find Winning High Ticket Products (Asonjf)',
      'url': 'https://www.youtube.com/watch?v=r79NEO4JF2M&t=613s',
      'video_id': 'r79NEO4JF2M'},
     {'author': 'Tarun Brar - eCom Email Marketing',
      'channel': 'Tarun Brar - eCom Email Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:41](https://www.youtube.com/watch?v=coevagBV6wU&t=221s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '3x means it costs around $33 to find that customer, which means your gross '
              'profit after your acquisition cost is $26. If that customer just comes back for '
              'one more purchase, your gross profit increases exponentially.',
      'timestamp': 221,
      'timestamp_label': '[00:03:41]',
      'timestamp_seconds': 221,
      'tip': '3x means it costs around $33 to find that customer, which means your gross '
             'profit after your acquisition cost is $26. If that customer just comes back for '
             'one more purchase, your gross profit increases exponentially.',
      'title': 'Klaviyo Tutorial: How to Setup the Post-Purchase Flow 2025 (Step by Step) '
               '(Tarun Brar - eCom Email Marketing)',
      'url': 'https://www.youtube.com/watch?v=coevagBV6wU&t=221s',
      'video_id': 'coevagBV6wU'},
     {'author': 'Eric Andrews',
      'channel': 'Eric Andrews',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:57](https://www.youtube.com/watch?v=8xfPvprL5qE&t=237s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Get access to it okay so at a high level here is how we would break down unit '
              'economics for an e-commerce business so you have your net.',
      'timestamp': 237,
      'timestamp_label': '[00:03:57]',
      'timestamp_seconds': 237,
      'tip': 'Get access to it okay so at a high level here is how we would break down unit '
             'economics for an e-commerce business so you have your net.',
      'title': 'How to Calculate eCommerce Contribution Margins (Eric Andrews)',
      'url': 'https://www.youtube.com/watch?v=8xfPvprL5qE&t=237s',
      'video_id': '8xfPvprL5qE'},
     {'author': 'Natan',
      'channel': 'Natan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:48](https://www.youtube.com/watch?v=YHmvKbjg81E&t=408s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Facebook and Instagram ads, and trying to figure out how to keep any profit was '
              'really difficult because after the product cost, which was like $15 for this '
              '$30 item, and $6 in shipping, and then whatever other fees, I got left with '
              'like five or $6 per item.',
      'timestamp': 408,
      'timestamp_label': '[00:06:48]',
      'timestamp_seconds': 408,
      'tip': 'Facebook and Instagram ads, and trying to figure out how to keep any profit was '
             'really difficult because after the product cost, which was like $15 for this $30 '
             'item, and $6 in shipping, and then whatever other fees, I got left with like '
             'five or $6 per item.',
      'title': 'how i did $8.3m in sales with high ticket dropshipping (Natan)',
      'url': 'https://www.youtube.com/watch?v=YHmvKbjg81E&t=408s',
      'video_id': 'YHmvKbjg81E'},
     {'author': 'Eric Andrews Clips',
      'channel': 'Eric Andrews Clips',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:39](https://www.youtube.com/watch?v=LKEn47f67vQ&t=99s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Pure profit because there'll generally be little or no marketing associated "
              'with them so being profitable on the first order is ideal and some businesses '
              'are very profitable on the first order and those are exceptional e-commerce '
              'businesses.',
      'timestamp': 99,
      'timestamp_label': '[00:01:39]',
      'timestamp_seconds': 99,
      'tip': "Pure profit because there'll generally be little or no marketing associated with "
             'them so being profitable on the first order is ideal and some businesses are '
             'very profitable on the first order and those are exceptional e-commerce '
             'businesses.',
      'title': 'Contribution Margin: CAC Ratio for eCommerce | Unit Economics (Eric Andrews '
               'Clips)',
      'url': 'https://www.youtube.com/watch?v=LKEn47f67vQ&t=99s',
      'video_id': 'LKEn47f67vQ'},
     {'author': 'Dropship Circle - High Ticket Dropshipping',
      'channel': 'Dropship Circle - High Ticket Dropshipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:25](https://www.youtube.com/watch?v=WAF10Ijm6RE&t=625s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s the, the price the customer pays, right? So the good thing is, is this meets "
              "that criteria. It's 900 pounds to 5,000 pound plus. So we've got a big tick "
              'there. Profit per sale, 300 to 1,500. So evergreen means, is it seasonal or is '
              'it sold all year round.',
      'timestamp': 625,
      'timestamp_label': '[00:10:25]',
      'timestamp_seconds': 625,
      'tip': "'s the, the price the customer pays, right? So the good thing is, is this meets "
             "that criteria. It's 900 pounds to 5,000 pound plus. So we've got a big tick "
             'there. Profit per sale, 300 to 1,500. So evergreen means, is it seasonal or is '
             'it sold all year round.',
      'title': 'The Top 5 High-Ticket Dropshipping Products to Sell in 2025 for Maximum Profit '
               '(Dropship Circle - High Ticket Dropshipping)',
      'url': 'https://www.youtube.com/watch?v=WAF10Ijm6RE&t=625s',
      'video_id': 'WAF10Ijm6RE'},
     {'author': 'Peak Flow Media',
      'channel': 'Peak Flow Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:52](https://www.youtube.com/watch?v=wy_uAK2tMS0&t=112s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's called high ticket drop shipping where you are finding luxury products, "
              'products that are $1,000 and above. So, the reason why we do that is because '
              'the profit margins per one unit is a lot more. You can make 300 to 1,000 plus '
              'profit in one sale.',
      'timestamp': 112,
      'timestamp_label': '[00:01:52]',
      'timestamp_seconds': 112,
      'tip': "It's called high ticket drop shipping where you are finding luxury products, "
             'products that are $1,000 and above. So, the reason why we do that is because the '
             'profit margins per one unit is a lot more. You can make 300 to 1,000 plus profit '
             'in one sale.',
      'title': 'High-Ticket Dropshipping Explained (Peak Flow Media)',
      'url': 'https://www.youtube.com/watch?v=wy_uAK2tMS0&t=112s',
      'video_id': 'wy_uAK2tMS0'},
     {'author': 'Brent Freeman  - The CBB Group',
      'channel': 'Brent Freeman  - The CBB Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:19](https://www.youtube.com/watch?v=KSfESWIcDGI&t=379s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Price uh to satisfy that requirement and keep the business running so what kind '
              'of businesses require working capital well in general.',
      'timestamp': 379,
      'timestamp_label': '[00:06:19]',
      'timestamp_seconds': 379,
      'tip': 'Price uh to satisfy that requirement and keep the business running so what kind '
             'of businesses require working capital well in general.',
      'title': 'Working Capital Adjustment in a Business Sale. How it Can Change the Final '
               'Purchase Price! (Brent Freeman  - The CBB Group)',
      'url': 'https://www.youtube.com/watch?v=KSfESWIcDGI&t=379s',
      'video_id': 'KSfESWIcDGI'},
     {'author': 'Theo Clarke Podcast',
      'channel': 'Theo Clarke Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:08](https://www.youtube.com/watch?v=8V2vAoy6GNA&t=968s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Processing holds that will eat into your profit margins that's why I'm excited "
              'to introduce you to commerci of our sponsor today they handle everything from.',
      'timestamp': 968,
      'timestamp_label': '[00:16:08]',
      'timestamp_seconds': 968,
      'tip': "Processing holds that will eat into your profit margins that's why I'm excited "
             'to introduce you to commerci of our sponsor today they handle everything from.',
      'title': 'How To Dropship High-Ticket Products Using US Suppliers | Brook Hiddink | '
               'Ep.19 (Theo Clarke Podcast)',
      'url': 'https://www.youtube.com/watch?v=8V2vAoy6GNA&t=968s',
      'video_id': '8V2vAoy6GNA'},
     {'author': 'Derek Stroh',
      'channel': 'Derek Stroh',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:12](https://www.youtube.com/watch?v=cerX0RFHJ0c&t=132s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, not only is it going to help with increasing your customer satisfaction and '
              "increasing LTV, it's also going to help to reduce potential returns, which is "
              'again profit.',
      'timestamp': 132,
      'timestamp_label': '[00:02:12]',
      'timestamp_seconds': 132,
      'tip': 'So, not only is it going to help with increasing your customer satisfaction and '
             "increasing LTV, it's also going to help to reduce potential returns, which is "
             'again profit.',
      'title': 'Klaviyo Post Purchase Thank You Flow Strategies (Derek Stroh)',
      'url': 'https://www.youtube.com/watch?v=cerX0RFHJ0c&t=132s',
      'video_id': 'cerX0RFHJ0c'},
     {'author': 'Avalara',
      'channel': 'Avalara',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:29](https://www.youtube.com/watch?v=QiT660QtcXA&t=29s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But that doesn't mean you can just start a store on Amazon Marketplace and call "
              'it a day. First, you need to know if your marketplace is collecting sales tax '
              'for you. Some marketplaces, including Amazon, Walmart and Etsy, are required to '
              'collect sales tax on your behalf.',
      'timestamp': 29,
      'timestamp_label': '[00:00:29]',
      'timestamp_seconds': 29,
      'tip': "But that doesn't mean you can just start a store on Amazon Marketplace and call "
             'it a day. First, you need to know if your marketplace is collecting sales tax '
             'for you. Some marketplaces, including Amazon, Walmart and Etsy, are required to '
             'collect sales tax on your behalf.',
      'title': 'Tax 101: Does my online marketplace collect sales tax for me? (Avalara)',
      'url': 'https://www.youtube.com/watch?v=QiT660QtcXA&t=29s',
      'video_id': 'QiT660QtcXA'}],
 4: [{'author': 'ICandT',
      'channel': 'ICandT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:20](https://www.youtube.com/watch?v=ebKN15qGOxo&t=140s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'One tool, every cost fully auditable. Any quote in any currency, the full '
              'tariff and duty stack. Customs fees done right, hidden costs priced in, '
              'offshore versus US head-to-head, working capital impact, tooling payback, and '
              'always current tariff data.',
      'timestamp': 140,
      'timestamp_label': '[00:02:20]',
      'timestamp_seconds': 140,
      'tip': 'One tool, every cost fully auditable. Any quote in any currency, the full tariff '
             'and duty stack. Customs fees done right, hidden costs priced in, offshore versus '
             'US head-to-head, working capital impact, tooling payback, and always current '
             'tariff data.',
      'title': 'World Class Free Landed Cost Program that auto-updates currencies, duties, '
               'tariffs, etc. (ICandT)',
      'url': 'https://www.youtube.com/watch?v=ebKN15qGOxo&t=140s',
      'video_id': 'ebKN15qGOxo'},
     {'author': 'WallStreetMojo',
      'channel': 'WallStreetMojo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:52](https://www.youtube.com/watch?v=Sw24t4Xzk0I&t=952s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Be honest likewise other examples where negative cash conversion cycle could be '
              "like amazon so if you look at amazon's cash conversion cycle again it's the "
              "same it's around I think minus 24 25 days.",
      'timestamp': 952,
      'timestamp_label': '[00:15:52]',
      'timestamp_seconds': 952,
      'tip': 'Be honest likewise other examples where negative cash conversion cycle could be '
             "like amazon so if you look at amazon's cash conversion cycle again it's the same "
             "it's around I think minus 24 25 days.",
      'title': 'Cash Conversion Cycle - Meaning, Formula, Calculation & Interpretations '
               '(WallStreetMojo)',
      'url': 'https://www.youtube.com/watch?v=Sw24t4Xzk0I&t=952s',
      'video_id': 'Sw24t4Xzk0I'},
     {'author': 'New York SBDC',
      'channel': 'New York SBDC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:36:57](https://www.youtube.com/watch?v=LBisYGOUrx0&t=2217s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We also provide assistance as John mentioned classifying goods with the '
              'harmonized target schedule and utilize all the tools available from the US '
              'Department of Commerce. Um sorry and also there are tools from customs that are '
              'very useful.',
      'timestamp': 2217,
      'timestamp_label': '[00:36:57]',
      'timestamp_seconds': 2217,
      'tip': 'We also provide assistance as John mentioned classifying goods with the '
             'harmonized target schedule and utilize all the tools available from the US '
             'Department of Commerce. Um sorry and also there are tools from customs that are '
             'very useful.',
      'title': 'Calculating Landed Cost for Exported and Imported Goods (New York SBDC)',
      'url': 'https://www.youtube.com/watch?v=LBisYGOUrx0&t=2217s',
      'video_id': 'LBisYGOUrx0'},
     {'author': 'Macha',
      'channel': 'Macha',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:30](https://www.youtube.com/watch?v=eusN-cV9bSQ&t=270s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And the price grows with success. Each automated interaction carries its own '
              'fee on top of the ticket, so a better month costs more. We use the same '
              'scorecard as in our best AI customer service software video.',
      'timestamp': 270,
      'timestamp_label': '[00:04:30]',
      'timestamp_seconds': 270,
      'tip': 'And the price grows with success. Each automated interaction carries its own fee '
             'on top of the ticket, so a better month costs more. We use the same scorecard as '
             'in our best AI customer service software video.',
      'title': 'Gorgias AI Agent review (2026): AI Agent 3.0, price and setup, scored (Macha)',
      'url': 'https://www.youtube.com/watch?v=eusN-cV9bSQ&t=270s',
      'video_id': 'eusN-cV9bSQ'},
     {'author': 'Anton Kraly - Drop Ship Lifestyle',
      'channel': 'Anton Kraly - Drop Ship Lifestyle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:41](https://www.youtube.com/watch?v=D6kFUv6fy_4&t=401s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The reality is you don't need to buy things up front. You just need a budget "
              'for ads and a Shopify setup. Myth number two is that all suppliers are going to '
              'reject beginners and new store owners.',
      'timestamp': 401,
      'timestamp_label': '[00:06:41]',
      'timestamp_seconds': 401,
      'tip': "The reality is you don't need to buy things up front. You just need a budget for "
             'ads and a Shopify setup. Myth number two is that all suppliers are going to '
             'reject beginners and new store owners.',
      'title': 'What Is High-Ticket Dropshipping? (Anton Kraly - Drop Ship Lifestyle)',
      'url': 'https://www.youtube.com/watch?v=D6kFUv6fy_4&t=401s',
      'video_id': 'D6kFUv6fy_4'},
     {'author': 'Shipping Solutions',
      'channel': 'Shipping Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:59](https://www.youtube.com/watch?v=IrCCfr1mSvg&t=179s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'HTS code right, because that determines the duty rate you’ll pay. Then build '
              'the full landed cost—that means rolling in the purchase price, transportation, '
              'insurance, customs duties, taxes, import processing charges, and any add-ons '
              'like anti-dumping duties.',
      'timestamp': 179,
      'timestamp_label': '[00:02:59]',
      'timestamp_seconds': 179,
      'tip': 'HTS code right, because that determines the duty rate you’ll pay. Then build the '
             'full landed cost—that means rolling in the purchase price, transportation, '
             'insurance, customs duties, taxes, import processing charges, and any add-ons '
             'like anti-dumping duties.',
      'title': 'Duties, Tariffs and Taxes: Understanding the Costs of International Trade '
               '(Shipping Solutions)',
      'url': 'https://www.youtube.com/watch?v=IrCCfr1mSvg&t=179s',
      'video_id': 'IrCCfr1mSvg'},
     {'author': 'Trade Counsel',
      'channel': 'Trade Counsel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=-WXoF_u08g0&t=163s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's the $2,400 from the start. Paying it takes some setup. You need an "
              'importer number, which for most businesses is simply their federal tax ID. You '
              'need a customs bond, a guarantee from an insurance company that customs will be '
              "paid what it's owed, penalties included.",
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': "That's the $2,400 from the start. Paying it takes some setup. You need an "
             'importer number, which for most businesses is simply their federal tax ID. You '
             'need a customs bond, a guarantee from an insurance company that customs will be '
             "paid what it's owed, penalties included.",
      'title': "What Importers Get Wrong About US Customs (And It's Expensive) | Expert's "
               'Guide for Beginner (Trade Counsel)',
      'url': 'https://www.youtube.com/watch?v=-WXoF_u08g0&t=163s',
      'video_id': '-WXoF_u08g0'},
     {'author': 'Crescent Kao',
      'channel': 'Crescent Kao',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=qeqvFEGP-7g&t=134s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Amazon will resolve the claim through a concession to the customer and will not '
              'request reimbursement from you or your insurer if you provide proof of.',
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': 'Amazon will resolve the claim through a concession to the customer and will not '
             'request reimbursement from you or your insurer if you provide proof of.',
      'title': 'Amazon FBA Product Liability Insurance for Beginners Explained 2024 UPDATE! '
               '(Crescent Kao)',
      'url': 'https://www.youtube.com/watch?v=qeqvFEGP-7g&t=134s',
      'video_id': 'qeqvFEGP-7g'},
     {'author': 'Insurance Assurance',
      'channel': 'Insurance Assurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=XxorvB6ExNs&t=32s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'E-commerce business from your living room this guide is for you to get the '
              'insurance from the best rated insurance company check out the link in the.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': 'E-commerce business from your living room this guide is for you to get the '
             'insurance from the best rated insurance company check out the link in the.',
      'title': 'Product Liability Insurance Coverage and Cost | What is Product Liability? '
               'Small Business Insurance (Insurance Assurance)',
      'url': 'https://www.youtube.com/watch?v=XxorvB6ExNs&t=32s',
      'video_id': 'XxorvB6ExNs'},
     {'author': 'GroPulse',
      'channel': 'GroPulse',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=El6hMZ1_77w&t=56s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Stocky, built right into Shopify, can handle automated reordering like a champ. '
              'Katana MRP is perfect for syncing your production, and OrderHive uses AI to '
              'predict demand spikes before they hit. All these tools install in one click, '
              'saving you hours every week.',
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': 'Stocky, built right into Shopify, can handle automated reordering like a champ. '
             'Katana MRP is perfect for syncing your production, and OrderHive uses AI to '
             'predict demand spikes before they hit. All these tools install in one click, '
             'saving you hours every week.',
      'title': 'Shopify Inventory Management Complete Setup Guide (GroPulse)',
      'url': 'https://www.youtube.com/watch?v=El6hMZ1_77w&t=56s',
      'video_id': 'El6hMZ1_77w'},
     {'author': 'BIS Benefits - Best In Serving',
      'channel': 'BIS Benefits - Best In Serving',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:48](https://www.youtube.com/watch?v=A0rgATB8PiM&t=288s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And so, um, what I would encourage the audience to kind of hear is insurance '
              'tends to stack and you get what you need just to check the box at the beginning '
              "in survival mode. 't afford to not have someone care or be dorks like us and "
              'and know the right questions to ask.',
      'timestamp': 288,
      'timestamp_label': '[00:04:48]',
      'timestamp_seconds': 288,
      'tip': 'And so, um, what I would encourage the audience to kind of hear is insurance '
             'tends to stack and you get what you need just to check the box at the beginning '
             "in survival mode. 't afford to not have someone care or be dorks like us and and "
             'know the right questions to ask.',
      'title': 'What is Product Liability Insurance? (BIS Benefits - Best In Serving)',
      'url': 'https://www.youtube.com/watch?v=A0rgATB8PiM&t=288s',
      'video_id': 'A0rgATB8PiM'},
     {'author': 'Avalara',
      'channel': 'Avalara',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:49](https://www.youtube.com/watch?v=A7FAFArV6JM&t=109s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Background Avalara ave attacks is easy on your end too it comes ready to '
              'connect with s AP Commerce cloud using a pre-built.',
      'timestamp': 109,
      'timestamp_label': '[00:01:49]',
      'timestamp_seconds': 109,
      'tip': 'Background Avalara ave attacks is easy on your end too it comes ready to connect '
             'with s AP Commerce cloud using a pre-built.',
      'title': 'SAP Commerce Cloud + Avalara (Avalara)',
      'url': 'https://www.youtube.com/watch?v=A7FAFArV6JM&t=109s',
      'video_id': 'A7FAFArV6JM'},
     {'author': 'MarketingSherpa',
      'channel': 'MarketingSherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:10](https://www.youtube.com/watch?v=u0WQ5ZC6KME&t=250s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The other excellent lisa a lot of great points thank you so much for joining us '
              "in the media center and don't forget you can view all of our videos online at "
              'www.marketingsherpa.com irc.',
      'timestamp': 250,
      'timestamp_label': '[00:04:10]',
      'timestamp_seconds': 250,
      'tip': 'The other excellent lisa a lot of great points thank you so much for joining us '
             "in the media center and don't forget you can view all of our videos online at "
             'www.marketingsherpa.com irc.',
      'title': 'E-commerce Marketing: Evaluating what omnichannel really means '
               '(MarketingSherpa)',
      'url': 'https://www.youtube.com/watch?v=u0WQ5ZC6KME&t=250s',
      'video_id': 'u0WQ5ZC6KME'},
     {'author': 'Gavin Hewitson',
      'channel': 'Gavin Hewitson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:34](https://www.youtube.com/watch?v=Cu4iN3jgMwI&t=94s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, this store is integrated with Woo Commerce. So, it's triggered off of a "
              'Woo Commerce metric, but in some cases may be triggered off of a Shopify placed '
              "order metric, but we're triggering this flow off of the placed order metric.",
      'timestamp': 94,
      'timestamp_label': '[00:01:34]',
      'timestamp_seconds': 94,
      'tip': "Now, this store is integrated with Woo Commerce. So, it's triggered off of a Woo "
             'Commerce metric, but in some cases may be triggered off of a Shopify placed '
             "order metric, but we're triggering this flow off of the placed order metric.",
      'title': 'Klaviyo Post Purchase Flow Tutorial | Shopify Thank You Flow Setup (Gavin '
               'Hewitson)',
      'url': 'https://www.youtube.com/watch?v=Cu4iN3jgMwI&t=94s',
      'video_id': 'Cu4iN3jgMwI'},
     {'author': 'Marcus Lam | High Ticket Dropshipping (AI)',
      'channel': 'Marcus Lam | High Ticket Dropshipping (AI)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=7B1m62WaDkw&t=15s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I think real close it'll be over over a grand nice yeah that was uh free "
              "because I wasn't even I'm not even running ads to.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "I think real close it'll be over over a grand nice yeah that was uh free because "
             "I wasn't even I'm not even running ads to.",
      'title': 'Niching Down and Finding Better Suppliers | High Ticket Dropshipping (Case '
               'Study) (Marcus Lam | High Ticket Dropshipping (AI))',
      'url': 'https://www.youtube.com/watch?v=7B1m62WaDkw&t=15s',
      'video_id': '7B1m62WaDkw'}],
 5: [{'author': 'One Minute Finance',
      'channel': 'One Minute Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=7yuWFm95LDw&t=103s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The cash conversion cycle, or the CCC, measures exactly how long this trap '
              'lasts, from the exact moment cash leaves to pay suppliers, all the way to when '
              'it finally returns from your customers.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': 'The cash conversion cycle, or the CCC, measures exactly how long this trap '
             'lasts, from the exact moment cash leaves to pay suppliers, all the way to when '
             'it finally returns from your customers.',
      'title': 'The Cash Conversion Cycle (CCC) Explained | Formula, Working Capital & Cash '
               'Flow Mastery (One Minute Finance)',
      'url': 'https://www.youtube.com/watch?v=7yuWFm95LDw&t=103s',
      'video_id': '7yuWFm95LDw'},
     {'author': 'Mergers & Inquisitions / Breaking Into Wall Street',
      'channel': 'Mergers & Inquisitions / Breaking Into Wall Street',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:38](https://www.youtube.com/watch?v=rNjMWAOJHwM&t=518s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That depend heavily on inventory in these cases the trends in the cash '
              'conversion cycle could indicate when a company might need to raise capital or.',
      'timestamp': 518,
      'timestamp_label': '[00:08:38]',
      'timestamp_seconds': 518,
      'tip': 'That depend heavily on inventory in these cases the trends in the cash '
             'conversion cycle could indicate when a company might need to raise capital or.',
      'title': 'The Cash Conversion Cycle (CCC): The King of the Cash Flow Statement? (Mergers '
               '& Inquisitions / Breaking Into Wall Street)',
      'url': 'https://www.youtube.com/watch?v=rNjMWAOJHwM&t=518s',
      'video_id': 'rNjMWAOJHwM'},
     {'author': 'Daniel Boufford',
      'channel': 'Daniel Boufford',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:23](https://www.youtube.com/watch?v=jYFh4ucNZuw&t=143s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um but if uh if there's a problem on Amazon and they say a customer says it's "
              "inauthentic or any number of things can happen, they'll they'll request an "
              'invoice and they may or may not accept the invoice from the distributor.',
      'timestamp': 143,
      'timestamp_label': '[00:02:23]',
      'timestamp_seconds': 143,
      'tip': "Um but if uh if there's a problem on Amazon and they say a customer says it's "
             "inauthentic or any number of things can happen, they'll they'll request an "
             'invoice and they may or may not accept the invoice from the distributor.',
      'title': 'The Truth About Distributors vs Brand Direct (Amazon Wholesale) (Daniel '
               'Boufford)',
      'url': 'https://www.youtube.com/watch?v=jYFh4ucNZuw&t=143s',
      'video_id': 'jYFh4ucNZuw'},
     {'author': 'Coffeezilla',
      'channel': 'Coffeezilla',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:23](https://www.youtube.com/watch?v=fPLMdewUMQw&t=383s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Do it for the amazon automated store guys again do you notice do you notice you '
              'take all the risk.',
      'timestamp': 383,
      'timestamp_label': '[00:06:23]',
      'timestamp_seconds': 383,
      'tip': 'Do it for the amazon automated store guys again do you notice do you notice you '
             'take all the risk.',
      'title': 'Exposing the Walmart "Automation" SCAM (Coffeezilla)',
      'url': 'https://www.youtube.com/watch?v=fPLMdewUMQw&t=383s',
      'video_id': 'fPLMdewUMQw'},
     {'author': 'Sertac Altun',
      'channel': 'Sertac Altun',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:31](https://www.youtube.com/watch?v=B-HQodfgIG4&t=211s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This is what inversion is and let's get into that. What kind of brands are we "
              "avoiding on Amazon? It's going to be brands that look like this. This is what's "
              "going to guarantee our failure, right? There's no proof of concept for "
              'resellers, so we should avoid these products.',
      'timestamp': 211,
      'timestamp_label': '[00:03:31]',
      'timestamp_seconds': 211,
      'tip': "This is what inversion is and let's get into that. What kind of brands are we "
             "avoiding on Amazon? It's going to be brands that look like this. This is what's "
             "going to guarantee our failure, right? There's no proof of concept for "
             'resellers, so we should avoid these products.',
      'title': 'Amazon FBA Wholesale Brand direct for Beginners: The Easiest Way to Start in '
               '2027 (Sertac Altun)',
      'url': 'https://www.youtube.com/watch?v=B-HQodfgIG4&t=211s',
      'video_id': 'B-HQodfgIG4'},
     {'author': 'LedgerGurus: Ecommerce Accounting Experts',
      'channel': 'LedgerGurus: Ecommerce Accounting Experts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=-DhtTN5_Rh4&t=55s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And then lastly, I'm going to give a detailed review of pros and cons of some "
              'of our favorite slash most used softwares out there for sales tax automation. '
              "I'm going to talk about TaxJar, Avalara, Sovos, and Taxify. Why is sales tax so "
              'complicated for e-commerce sellers?',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': "And then lastly, I'm going to give a detailed review of pros and cons of some of "
             "our favorite slash most used softwares out there for sales tax automation. I'm "
             'going to talk about TaxJar, Avalara, Sovos, and Taxify. Why is sales tax so '
             'complicated for e-commerce sellers?',
      'title': 'Avalara? TaxJar? Taxify? BEST SALES TAX APP for Ecommerce (LedgerGurus: '
               'Ecommerce Accounting Experts)',
      'url': 'https://www.youtube.com/watch?v=-DhtTN5_Rh4&t=55s',
      'video_id': '-DhtTN5_Rh4'},
     {'author': 'Third-Party Profits',
      'channel': 'Third-Party Profits',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:35](https://www.youtube.com/watch?v=1lcG6ji-5ls&t=95s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ve been around, the more likely they are to be an authorized distributor of "
              "the brand. So, we're going to put 20 to 50 years and 50 plus years. Those are "
              'the two toggles that recommend. The second thing that recommend to do is to '
              'select a region.',
      'timestamp': 95,
      'timestamp_label': '[00:01:35]',
      'timestamp_seconds': 95,
      'tip': "'ve been around, the more likely they are to be an authorized distributor of the "
             "brand. So, we're going to put 20 to 50 years and 50 plus years. Those are the "
             'two toggles that recommend. The second thing that recommend to do is to select a '
             'region.',
      'title': 'How to Find Amazon Wholesale Suppliers That Actually Make You Money | '
               'Third-Party Profits Tutorial (Third-Party Profits)',
      'url': 'https://www.youtube.com/watch?v=1lcG6ji-5ls&t=95s',
      'video_id': '1lcG6ji-5ls'},
     {'author': 'Anatoliy Labinskiy | E-com business encyclopedia',
      'channel': 'Anatoliy Labinskiy | E-com business encyclopedia',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:50](https://www.youtube.com/watch?v=XED26wvEepA&t=170s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your payment providers avoid the holds than just save couple of bucks on there '
              'or win the dispute with the client and again if you want to know more more.',
      'timestamp': 170,
      'timestamp_label': '[00:02:50]',
      'timestamp_seconds': 170,
      'tip': 'Your payment providers avoid the holds than just save couple of bucks on there '
             'or win the dispute with the client and again if you want to know more more.',
      'title': 'How to Deal with Shopify Chargebacks, Refunds, and Returns | Dropshipping '
               'Beginner Mistakes in Ecom (Anatoliy Labinskiy | E-com business encyclopedia)',
      'url': 'https://www.youtube.com/watch?v=XED26wvEepA&t=170s',
      'video_id': 'XED26wvEepA'},
     {'author': 'KeyCommerce',
      'channel': 'KeyCommerce',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=S1NhYxaPnic&t=65s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Say you have a store that sells handmade rugs, minimalist design, short product '
              'names that look great on your site, something like The Midnight Oasis. We see '
              'this all the time when we audit stores at our agency, and it works perfectly as '
              'a brand product name.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': 'Say you have a store that sells handmade rugs, minimalist design, short product '
             'names that look great on your site, something like The Midnight Oasis. We see '
             'this all the time when we audit stores at our agency, and it works perfectly as '
             'a brand product name.',
      'title': 'How To Optimize Your Product Feed & Data In Google Merchant Center '
               '(KeyCommerce)',
      'url': 'https://www.youtube.com/watch?v=S1NhYxaPnic&t=65s',
      'video_id': 'S1NhYxaPnic'},
     {'author': 'Thomas | Amazon Wholesale',
      'channel': 'Thomas | Amazon Wholesale',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:52](https://www.youtube.com/watch?v=48JkrcvKaVs&t=112s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Get their cataloges running through scan unlimited it um which is like a '
              "catalog scanner to find profitable products and then you'll be good to go and "
              "that's exactly how you find authorized Distributors for Brands such as aani new "
              'to sell on Amazon.',
      'timestamp': 112,
      'timestamp_label': '[00:01:52]',
      'timestamp_seconds': 112,
      'tip': 'Get their cataloges running through scan unlimited it um which is like a catalog '
             "scanner to find profitable products and then you'll be good to go and that's "
             'exactly how you find authorized Distributors for Brands such as aani new to sell '
             'on Amazon.',
      'title': 'This is how you find brands authorized distributors to buy and sell their '
               'products on Amazon (Thomas | Amazon Wholesale)',
      'url': 'https://www.youtube.com/watch?v=48JkrcvKaVs&t=112s',
      'video_id': '48JkrcvKaVs'},
     {'author': 'Joe Verschoor',
      'channel': 'Joe Verschoor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:08](https://www.youtube.com/watch?v=5jY7d_1m1t0&t=248s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "MAP is not enforced, then it's kind of up to you what you charge for your "
              'products above your dealer cost to to your supplier. Um, so MAP versus no MAP, '
              "that's obviously a factor.",
      'timestamp': 248,
      'timestamp_label': '[00:04:08]',
      'timestamp_seconds': 248,
      'tip': "MAP is not enforced, then it's kind of up to you what you charge for your "
             'products above your dealer cost to to your supplier. Um, so MAP versus no MAP, '
             "that's obviously a factor.",
      'title': 'How Much Money Can You Actually Make High Ticket Dropshipping? [2027] (Joe '
               'Verschoor)',
      'url': 'https://www.youtube.com/watch?v=5jY7d_1m1t0&t=248s',
      'video_id': '5jY7d_1m1t0'},
     {'author': 'Racklify',
      'channel': 'Racklify',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=NXZLkZ_Gfuk&t=90s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Offerings on your site to do this you're going to have to ship these items to "
              'the customer in that set this is going to allow you to take full advantage of '
              'your.',
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': "Offerings on your site to do this you're going to have to ship these items to "
             'the customer in that set this is going to allow you to take full advantage of '
             'your.',
      'title': 'Dimensional Weight: How You Are Overpaying For Shipping Selling On Amazon & '
               'Shopify (Racklify)',
      'url': 'https://www.youtube.com/watch?v=NXZLkZ_Gfuk&t=90s',
      'video_id': 'NXZLkZ_Gfuk'},
     {'author': 'ShipBob',
      'channel': 'ShipBob',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:55](https://www.youtube.com/watch?v=zldfAGyfsfA&t=175s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Pack your orders in your custom branded packaging and offer the unbo boxing '
              'experience you want your customers to have to learn more about e-commerce '
              "fulfillment or how you can get started with ship Bob's fulfillment Solutions "
              'visit ship bob.com.',
      'timestamp': 175,
      'timestamp_label': '[00:02:55]',
      'timestamp_seconds': 175,
      'tip': 'Pack your orders in your custom branded packaging and offer the unbo boxing '
             'experience you want your customers to have to learn more about e-commerce '
             "fulfillment or how you can get started with ship Bob's fulfillment Solutions "
             'visit ship bob.com.',
      'title': 'How Ecommerce Fulfillment Works | Behind-The-Scenes of Order Fulfillment '
               '(ShipBob)',
      'url': 'https://www.youtube.com/watch?v=zldfAGyfsfA&t=175s',
      'video_id': 'zldfAGyfsfA'},
     {'author': 'Brook Hiddink',
      'channel': 'Brook Hiddink',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:38](https://www.youtube.com/watch?v=cBdVAQxml6U&t=158s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You actually have picked one look let's say I'm doing restaurants you can go I "
              'am starting a computer Graphics store in the B to B restaurant niche please '
              'tell me tell me 15 to 20 products that cost over two five two thousand five '
              'hundred dollars at a restaurant.',
      'timestamp': 158,
      'timestamp_label': '[00:02:38]',
      'timestamp_seconds': 158,
      'tip': "You actually have picked one look let's say I'm doing restaurants you can go I "
             'am starting a computer Graphics store in the B to B restaurant niche please tell '
             'me tell me 15 to 20 products that cost over two five two thousand five hundred '
             'dollars at a restaurant.',
      'title': 'B2B High Ticket Dropshipping Explained (Brook Hiddink)',
      'url': 'https://www.youtube.com/watch?v=cBdVAQxml6U&t=158s',
      'video_id': 'cBdVAQxml6U'},
     {'author': 'Strictly Commerce',
      'channel': 'Strictly Commerce',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:18](https://www.youtube.com/watch?v=fOjBryou0Do&t=198s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Items night call two pack oh really that list two pack Pepto Bismol two pack uh '
              'Pepto Bismol 4 o DayQuil 8 O nqu 8 t packs regular and super temps so uh we '
              "just brought those in and we're bringing more items in okay do you guys do you "
              'guys buy direct.',
      'timestamp': 198,
      'timestamp_label': '[00:03:18]',
      'timestamp_seconds': 198,
      'tip': 'Items night call two pack oh really that list two pack Pepto Bismol two pack uh '
             'Pepto Bismol 4 o DayQuil 8 O nqu 8 t packs regular and super temps so uh we just '
             "brought those in and we're bringing more items in okay do you guys do you guys "
             'buy direct.',
      'title': 'Talking to Wholesale Distributors for Amazon FBA (LIVE Call) | Road to $1M '
               '(Strictly Commerce)',
      'url': 'https://www.youtube.com/watch?v=fOjBryou0Do&t=198s',
      'video_id': 'fOjBryou0Do'}],
 6: [{'author': 'Eric Andrews',
      'channel': 'Eric Andrews',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=t2H3gJHuw6k&t=56s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, first let's walk through the economics of this brand outside of Black "
              'Friday, and then walk through these promos side by side. So, this brand is has '
              'a conversion rate of 1. Obviously, your customer acquisition cost is a function '
              'of your conversion rate.',
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': "So, first let's walk through the economics of this brand outside of Black "
             'Friday, and then walk through these promos side by side. So, this brand is has a '
             'conversion rate of 1. Obviously, your customer acquisition cost is a function of '
             'your conversion rate.',
      'title': '50% Off vs. BOGO: Unit Economics Case Study (How We Lost $500K) (Eric Andrews)',
      'url': 'https://www.youtube.com/watch?v=t2H3gJHuw6k&t=56s',
      'video_id': 't2H3gJHuw6k'},
     {'author': 'Abdul Rauf Ali',
      'channel': 'Abdul Rauf Ali',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:37](https://www.youtube.com/watch?v=V0LAr3jchLs&t=97s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Number four, does the landing page close? Your feed is the blueprint. If your '
              "blueprint is wrong, you don't fix the building by repainting the walls. So "
              'before we do any optimization in the Google Merchant Center, first we need to '
              'look at the ads account search terms data.',
      'timestamp': 97,
      'timestamp_label': '[00:01:37]',
      'timestamp_seconds': 97,
      'tip': 'Number four, does the landing page close? Your feed is the blueprint. If your '
             "blueprint is wrong, you don't fix the building by repainting the walls. So "
             'before we do any optimization in the Google Merchant Center, first we need to '
             'look at the ads account search terms data.',
      'title': 'Google Shopping Feed Optimization for Performance Max, 3 Fixes to improve ROAS '
               '& Merchant centre (Abdul Rauf Ali)',
      'url': 'https://www.youtube.com/watch?v=V0LAr3jchLs&t=97s',
      'video_id': 'V0LAr3jchLs'},
     {'author': 'Wise Explainer',
      'channel': 'Wise Explainer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=X3G7DDq6KD8&t=88s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Smaller stores may find the cost higher than simpler solutions, but the time '
              'savings, automation, and professional customer experience often justify the '
              'investment.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'Smaller stores may find the cost higher than simpler solutions, but the time '
             'savings, automation, and professional customer experience often justify the '
             'investment.',
      'title': 'Loop Returns Dropshipping Honest Review - Watch Before Using (Wise Explainer)',
      'url': 'https://www.youtube.com/watch?v=X3G7DDq6KD8&t=88s',
      'video_id': 'X3G7DDq6KD8'},
     {'author': 'Shopify Mastery',
      'channel': 'Shopify Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:10](https://www.youtube.com/watch?v=EjZsqaOIDsc&t=190s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That means that any customer who wants to find it can. This is also what '
              'payment processors like Shopify Payments, Stripe, and PayPal look for when a '
              'customer files a dispute. Having a clear, published policy is your first line '
              'of defense in a chargeback situation.',
      'timestamp': 190,
      'timestamp_label': '[00:03:10]',
      'timestamp_seconds': 190,
      'tip': 'That means that any customer who wants to find it can. This is also what payment '
             'processors like Shopify Payments, Stripe, and PayPal look for when a customer '
             'files a dispute. Having a clear, published policy is your first line of defense '
             'in a chargeback situation.',
      'title': 'How to Handle Shopify Dropshipping Returns, Refunds, and Return Policies. '
               '(Shopify Mastery)',
      'url': 'https://www.youtube.com/watch?v=EjZsqaOIDsc&t=190s',
      'video_id': 'EjZsqaOIDsc'},
     {'author': 'Pedro Bermudez',
      'channel': 'Pedro Bermudez',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=nm9aWWMYnEg&t=57s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'One, three ways to find brands with nobody sitting between you and them. The '
              'first one you can do tonight right on your phone. Two, the 30-second filter '
              'that tells you whether a brand is worth your time or a wasted week.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': 'One, three ways to find brands with nobody sitting between you and them. The '
             'first one you can do tonight right on your phone. Two, the 30-second filter that '
             'tells you whether a brand is worth your time or a wasted week.',
      'title': 'How to Find Amazon Wholesale and Brand Suppliers That Actually Make You Money '
               'Faster (Pedro Bermudez)',
      'url': 'https://www.youtube.com/watch?v=nm9aWWMYnEg&t=57s',
      'video_id': 'nm9aWWMYnEg'},
     {'author': 'KeyCommerce',
      'channel': 'KeyCommerce',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:43](https://www.youtube.com/watch?v=jmjy6G9akyM&t=343s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Under this, you can choose your audience, and here you have two options. The '
              "first is new customers. These are shoppers who haven't interacted with your "
              'brand before. Just be aware, this audience type is exclusively for shopping '
              'ads, not free listings.',
      'timestamp': 343,
      'timestamp_label': '[00:05:43]',
      'timestamp_seconds': 343,
      'tip': 'Under this, you can choose your audience, and here you have two options. The '
             "first is new customers. These are shoppers who haven't interacted with your "
             'brand before. Just be aware, this audience type is exclusively for shopping ads, '
             'not free listings.',
      'title': 'How to Run Promotions in Merchant Center for Google Shopping (KeyCommerce)',
      'url': 'https://www.youtube.com/watch?v=jmjy6G9akyM&t=343s',
      'video_id': 'jmjy6G9akyM'},
     {'author': 'Marcus Lam | High Ticket Dropshipping (AI)',
      'channel': 'Marcus Lam | High Ticket Dropshipping (AI)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:59](https://www.youtube.com/watch?v=g_OL9gG7q_I&t=299s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you look hard enough, you could actually go to the bottom. I believe they '
              "should have some form of dealer program. I'm going to search dealer program. "
              "I'm actually going to go to Google. I'll search dealer program with the brand "
              'name.',
      'timestamp': 299,
      'timestamp_label': '[00:04:59]',
      'timestamp_seconds': 299,
      'tip': 'If you look hard enough, you could actually go to the bottom. I believe they '
             "should have some form of dealer program. I'm going to search dealer program. I'm "
             "actually going to go to Google. I'll search dealer program with the brand name.",
      'title': 'How to Find USA Suppliers for High Ticket Dropshipping (Marcus Lam | High '
               'Ticket Dropshipping (AI))',
      'url': 'https://www.youtube.com/watch?v=g_OL9gG7q_I&t=299s',
      'video_id': 'g_OL9gG7q_I'},
     {'author': 'Trevor Zheng | High Ticket Dropshipping',
      'channel': 'Trevor Zheng | High Ticket Dropshipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:26](https://www.youtube.com/watch?v=v64Z-O_YyTY&t=446s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Them Brands here search that up onto Google and find our contact us information '
              'and contact them to become a dealer and another way is to look at.',
      'timestamp': 446,
      'timestamp_label': '[00:07:26]',
      'timestamp_seconds': 446,
      'tip': 'Them Brands here search that up onto Google and find our contact us information '
             'and contact them to become a dealer and another way is to look at.',
      'title': 'How To ACTUALLY Find Shopify Dropshipping Suppliers (USA High Ticket '
               'Suppliers) (Trevor Zheng | High Ticket Dropshipping)',
      'url': 'https://www.youtube.com/watch?v=v64Z-O_YyTY&t=446s',
      'video_id': 'v64Z-O_YyTY'},
     {'author': 'Theo Clough | Email Marketing',
      'channel': 'Theo Clough | Email Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:18](https://www.youtube.com/watch?v=AZHCdf0AuwM&t=198s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You cannot do the same with your followers. The next thing is the cost doesn't "
              'change. So, in Q4, your Facebook ads are going to increase in cost because more '
              'people are advertising. With email, the cost never increases unless you add '
              'more people onto the list.',
      'timestamp': 198,
      'timestamp_label': '[00:03:18]',
      'timestamp_seconds': 198,
      'tip': "You cannot do the same with your followers. The next thing is the cost doesn't "
             'change. So, in Q4, your Facebook ads are going to increase in cost because more '
             'people are advertising. With email, the cost never increases unless you add more '
             'people onto the list.',
      'title': 'Klaviyo Email Marketing For Beginners In (2026 Q4 Tutorial) (Theo Clough | '
               'Email Marketing)',
      'url': 'https://www.youtube.com/watch?v=AZHCdf0AuwM&t=198s',
      'video_id': 'AZHCdf0AuwM'},
     {'author': 'Ecom Chris',
      'channel': 'Ecom Chris',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:53](https://www.youtube.com/watch?v=d9kULGtUBD4&t=413s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Like actual search terms based on data. So without guessing and of course '
              "without keyword stuffing, right? That's that's the worst because that leads to "
              "turning titles into unreadable garbage. We don't want it either, right? It just "
              "doesn't make sense.",
      'timestamp': 413,
      'timestamp_label': '[00:06:53]',
      'timestamp_seconds': 413,
      'tip': 'Like actual search terms based on data. So without guessing and of course '
             "without keyword stuffing, right? That's that's the worst because that leads to "
             "turning titles into unreadable garbage. We don't want it either, right? It just "
             "doesn't make sense.",
      'title': 'Ultimate Guide to Google Shopping Feed Optimization: Increase CTR, Conversions '
               '& ROAS (Ecom Chris)',
      'url': 'https://www.youtube.com/watch?v=d9kULGtUBD4&t=413s',
      'video_id': 'd9kULGtUBD4'},
     {'author': 'SKUio',
      'channel': 'SKUio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=BAGqaHYyMlA&t=20s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The page sets out how estimated duty works, card by card. The first card '
              'explains what happens in your books. Step one, goods are received. Their '
              'estimated duty goes into stock cost, and is held in an accrued customs duty '
              'account.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'The page sets out how estimated duty works, card by card. The first card '
             'explains what happens in your books. Step one, goods are received. Their '
             'estimated duty goes into stock cost, and is held in an accrued customs duty '
             'account.',
      'title': 'How to Capitalize Estimated Import Duty Into Landed Cost and Reconcile Broker '
               'Bills | SKU.io (SKUio)',
      'url': 'https://www.youtube.com/watch?v=BAGqaHYyMlA&t=20s',
      'video_id': 'BAGqaHYyMlA'},
     {'author': 'William Rivera',
      'channel': 'William Rivera',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=KImeudrcJTU&t=15s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Suppliers every single time I need another one and in this video I'm going to "
              'show you a method that costs $0 for you to find your first profitable.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Suppliers every single time I need another one and in this video I'm going to "
             'show you a method that costs $0 for you to find your first profitable.',
      'title': 'How To Find Amazon Wholesale Suppliers In 5 Minutes (William Rivera)',
      'url': 'https://www.youtube.com/watch?v=KImeudrcJTU&t=15s',
      'video_id': 'KImeudrcJTU'},
     {'author': 'Tech Help Daily',
      'channel': 'Tech Help Daily',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=I8fM406sSsA&t=25s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now click inventory just below. Once products exist, this page lists every '
              'variant that tracks quantity at each location with its numbers side by side. To '
              'find one, type a product name or SKU in search and filter, like t-shirt.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': 'Now click inventory just below. Once products exist, this page lists every '
             'variant that tracks quantity at each location with its numbers side by side. To '
             'find one, type a product name or SKU in search and filter, like t-shirt.',
      'title': 'Shopify Inventory Management Tutorial for Beginners (2026 Step-by-Step Guide '
               'to Managing Stock) (Tech Help Daily)',
      'url': 'https://www.youtube.com/watch?v=I8fM406sSsA&t=25s',
      'video_id': 'I8fM406sSsA'},
     {'author': 'Prediko AI Inventory Management',
      'channel': 'Prediko AI Inventory Management',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:27](https://www.youtube.com/watch?v=IWUFOfiPmUI&t=207s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um, this call is mostly going to go over how to get started with Predico, what '
              'is kind of those first steps that you would want to take and then how to make '
              "the most of your data and the insights we're providing. If there are questions, "
              'we have the Q&A open.',
      'timestamp': 207,
      'timestamp_label': '[00:03:27]',
      'timestamp_seconds': 207,
      'tip': 'Um, this call is mostly going to go over how to get started with Predico, what '
             'is kind of those first steps that you would want to take and then how to make '
             "the most of your data and the insights we're providing. If there are questions, "
             'we have the Q&A open.',
      'title': 'How to Set Up Prediko: Shopify Inventory Forecasting, Purchase Orders & AI '
               'Planning (Onboarding) (Prediko AI Inventory Management)',
      'url': 'https://www.youtube.com/watch?v=IWUFOfiPmUI&t=207s',
      'video_id': 'IWUFOfiPmUI'},
     {'author': 'Build Assets Online',
      'channel': 'Build Assets Online',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:35](https://www.youtube.com/watch?v=ocjVuvj0QJg&t=275s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That was helpful if you want to learn how to build an online asset portfolio '
              'worth a million dollars or more we will show you how to do it build '
              "assetsonline.com playbook go check out the class and we'll see in the next one.",
      'timestamp': 275,
      'timestamp_label': '[00:04:35]',
      'timestamp_seconds': 275,
      'tip': 'That was helpful if you want to learn how to build an online asset portfolio '
             'worth a million dollars or more we will show you how to do it build '
             "assetsonline.com playbook go check out the class and we'll see in the next one.",
      'title': 'High Ticket Dropshipping Suppliers with No Price Lists - What to Do (Build '
               'Assets Online)',
      'url': 'https://www.youtube.com/watch?v=ocjVuvj0QJg&t=275s',
      'video_id': 'ocjVuvj0QJg'}],
 7: [{'author': 'ShipSage',
      'channel': 'ShipSage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=eRxb-KV0R4E&t=63s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Shopify, TikTok Shop, Etsy, and Amazon, your stock is synced across all your '
              'stores. No more overselling a size you ran out of. Step 3: the order comes in. '
              "Your customer checks out, and the order drops straight into ShipSage's OMS. "
              "That's our own order management system.",
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': 'Shopify, TikTok Shop, Etsy, and Amazon, your stock is synced across all your '
             'stores. No more overselling a size you ran out of. Step 3: the order comes in. '
             "Your customer checks out, and the order drops straight into ShipSage's OMS. "
             "That's our own order management system.",
      'title': 'How Shopify & TikTok Shop Clothing Brands Ship Thousands of Orders Daily | '
               'Inside an Apparel 3PL (ShipSage)',
      'url': 'https://www.youtube.com/watch?v=eRxb-KV0R4E&t=63s',
      'video_id': 'eRxb-KV0R4E'},
     {'author': 'Einstein Fulfillment',
      'channel': 'Einstein Fulfillment',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=7Xr-2wI5LJo&t=35s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Whether it's Shopify, Amazon, Woo Commerce, or a customuilt system, we'll make "
              'sure that your orders flow smoothly, your inventory stays sync, and reports are '
              'sent to you in real time. Step three, product inbound and warehouse prep.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': "Whether it's Shopify, Amazon, Woo Commerce, or a customuilt system, we'll make "
             'sure that your orders flow smoothly, your inventory stays sync, and reports are '
             'sent to you in real time. Step three, product inbound and warehouse prep.',
      'title': 'How a 3PL Onboards New Clients (Einstein Fulfillment)',
      'url': 'https://www.youtube.com/watch?v=7Xr-2wI5LJo&t=35s',
      'video_id': '7Xr-2wI5LJo'},
     {'author': 'Growth Manifesto Podcast',
      'channel': 'Growth Manifesto Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:32:21](https://www.youtube.com/watch?v=7v_KO8bj_G0&t=1941s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'As what are the key things that an e-commerce brand has to figure out to to '
              'step from 100 to 500 or from you say for I say for example 100 to 300 and then '
              "from 300 to 750, right? Cuz they're some pretty big steps, right?",
      'timestamp': 1941,
      'timestamp_label': '[00:32:21]',
      'timestamp_seconds': 1941,
      'tip': 'As what are the key things that an e-commerce brand has to figure out to to step '
             'from 100 to 500 or from you say for I say for example 100 to 300 and then from '
             "300 to 750, right? Cuz they're some pretty big steps, right?",
      'title': 'How to scale an eCommerce brand to $1M/mo | Paul Waddy (Growth Manifesto '
               'Podcast)',
      'url': 'https://www.youtube.com/watch?v=7v_KO8bj_G0&t=1941s',
      'video_id': '7v_KO8bj_G0'},
     {'author': 'Ecommerce Paradise | High Ticket Dropshipping',
      'channel': 'Ecommerce Paradise | High Ticket Dropshipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:19](https://www.youtube.com/watch?v=hHXf1_WdANY&t=679s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm interested in becoming an authorized dealer for your brand name. We drive "
              'traffic through Google Shopping and SEO and are looking for quality US brands '
              'to feature in our catalog.',
      'timestamp': 679,
      'timestamp_label': '[00:11:19]',
      'timestamp_seconds': 679,
      'tip': "I'm interested in becoming an authorized dealer for your brand name. We drive "
             'traffic through Google Shopping and SEO and are looking for quality US brands to '
             'feature in our catalog.',
      'title': 'How to Find USA High-Ticket Dropshipping Suppliers in 2026 (Ecommerce Paradise '
               '| High Ticket Dropshipping)',
      'url': 'https://www.youtube.com/watch?v=hHXf1_WdANY&t=679s',
      'video_id': 'hHXf1_WdANY'},
     {'author': 'Monopoly',
      'channel': 'Monopoly',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:48](https://www.youtube.com/watch?v=SeloMfYsYk0&t=48s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Products manufactured overseas travel by ocean freight, clear customs at '
              'American ports, and move by rail or truck to a 3PL warehouse. When shipments '
              'arrive, warehouse teams unload pallets, inspect products, verify cargo '
              'quantities, and digitally record incoming inventory.',
      'timestamp': 48,
      'timestamp_label': '[00:00:48]',
      'timestamp_seconds': 48,
      'tip': 'Products manufactured overseas travel by ocean freight, clear customs at '
             'American ports, and move by rail or truck to a 3PL warehouse. When shipments '
             'arrive, warehouse teams unload pallets, inspect products, verify cargo '
             'quantities, and digitally record incoming inventory.',
      'title': 'What Is 3PL Logistics? The Hidden System Powering E-Commerce #3plservices '
               '#fulfillment (Monopoly)',
      'url': 'https://www.youtube.com/watch?v=SeloMfYsYk0&t=48s',
      'video_id': 'SeloMfYsYk0'},
     {'author': 'Tutorial Stack',
      'channel': 'Tutorial Stack',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:00](https://www.youtube.com/watch?v=YnEcCYA-UDs&t=180s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, this is the part where you want to communicate with the customer. Keep the '
              'customer informed throughout the refund or return process. Send them a '
              'confirmation email with details of the refund or return and any next steps.',
      'timestamp': 180,
      'timestamp_label': '[00:03:00]',
      'timestamp_seconds': 180,
      'tip': 'So, this is the part where you want to communicate with the customer. Keep the '
             'customer informed throughout the refund or return process. Send them a '
             'confirmation email with details of the refund or return and any next steps.',
      'title': 'How to Handle Shopify Refunds and Returns (Step-by-Step) (Tutorial Stack)',
      'url': 'https://www.youtube.com/watch?v=YnEcCYA-UDs&t=180s',
      'video_id': 'YnEcCYA-UDs'},
     {'author': 'Tarun Brar - eCom Email Marketing',
      'channel': 'Tarun Brar - eCom Email Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=JT1uQ-EOyhM&t=20s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Most brands are doing SMS completely wrong. So, in this video, I'm going to "
              'show you guys how to build a profitable and customer-f first SMS marketing '
              'system that drives consistent revenue for your ecom brand.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Most brands are doing SMS completely wrong. So, in this video, I'm going to show "
             'you guys how to build a profitable and customer-f first SMS marketing system '
             'that drives consistent revenue for your ecom brand.',
      'title': 'Klaviyo SMS Marketing Tutorial: Step-by-Step for Beginners (Tarun Brar - eCom '
               'Email Marketing)',
      'url': 'https://www.youtube.com/watch?v=JT1uQ-EOyhM&t=20s',
      'video_id': 'JT1uQ-EOyhM'},
     {'author': 'Perseuss LLC',
      'channel': 'Perseuss LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:46](https://www.youtube.com/watch?v=VD9O6JRw54A&t=106s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, the typical 3PL magic consists of three steps. Number one, order drops in '
              'from Shopify, Okay? The products for that order live somewhere among these '
              'shelves. That means someone needs to first grab it and pick it. The second step '
              'of the magic is packing.',
      'timestamp': 106,
      'timestamp_label': '[00:01:46]',
      'timestamp_seconds': 106,
      'tip': 'So, the typical 3PL magic consists of three steps. Number one, order drops in '
             'from Shopify, Okay? The products for that order live somewhere among these '
             'shelves. That means someone needs to first grab it and pick it. The second step '
             'of the magic is packing.',
      'title': '3PL Explained: Real Warehouse Walkthrough (For Shopify Brands) (Perseuss LLC)',
      'url': 'https://www.youtube.com/watch?v=VD9O6JRw54A&t=106s',
      'video_id': 'VD9O6JRw54A'},
     {'author': 'ISF Expedite',
      'channel': 'ISF Expedite',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=3iYfv5mrDBE&t=72s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Step from determining freight costs to factoring and customs duties and taxes '
              'each component plays a crucial role in the final landed cost of your imported.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': 'Step from determining freight costs to factoring and customs duties and taxes '
             'each component plays a crucial role in the final landed cost of your imported.',
      'title': 'Calculating Landed Costs for Imported Goods (ISF Expedite)',
      'url': 'https://www.youtube.com/watch?v=3iYfv5mrDBE&t=72s',
      'video_id': '3iYfv5mrDBE'},
     {'author': 'Guides by Dan',
      'channel': 'Guides by Dan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:15](https://www.youtube.com/watch?v=V0kR_J_Vdkw&t=135s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And there you have it, a simple step-by-step guide to setting up your Shopify '
              'refunds and returns. Remember, a well-managed return and refund process not '
              'only helps in maintaining customer trust, but also in running a smooth online '
              'store operation.',
      'timestamp': 135,
      'timestamp_label': '[00:02:15]',
      'timestamp_seconds': 135,
      'tip': 'And there you have it, a simple step-by-step guide to setting up your Shopify '
             'refunds and returns. Remember, a well-managed return and refund process not only '
             'helps in maintaining customer trust, but also in running a smooth online store '
             'operation.',
      'title': 'How To Handle Shopify Refunds And Returns 2025 For Beginners (Guides by Dan)',
      'url': 'https://www.youtube.com/watch?v=V0kR_J_Vdkw&t=135s',
      'video_id': 'V0kR_J_Vdkw'},
     {'author': 'SAL Accounting CPA',
      'channel': 'SAL Accounting CPA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:31](https://www.youtube.com/watch?v=HbiniE5ODzI&t=451s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, as you can see on my screen right now, there's all the steps that you have "
              'to follow in tax jar where if you go down to step four, it would you can let it '
              'know where you want to when to collect sales tax.',
      'timestamp': 451,
      'timestamp_label': '[00:07:31]',
      'timestamp_seconds': 451,
      'tip': "So, as you can see on my screen right now, there's all the steps that you have "
             'to follow in tax jar where if you go down to step four, it would you can let it '
             'know where you want to when to collect sales tax.',
      'title': 'Numeral vs TaxJar vs Avalara - Best US Sales Tax Platform for Canadians (SAL '
               'Accounting CPA)',
      'url': 'https://www.youtube.com/watch?v=HbiniE5ODzI&t=451s',
      'video_id': 'HbiniE5ODzI'},
     {'author': 'Invoice Finance News',
      'channel': 'Invoice Finance News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:21](https://www.youtube.com/watch?v=Ooq0PnAEf5s&t=261s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A low number means cash flow is good and the danger of running out of money is '
              'minimized the formula for CCC also highlights the possible areas where '
              'improvements can be made good analytics just as much as Big Ideas can keep a '
              'company profitable.',
      'timestamp': 261,
      'timestamp_label': '[00:04:21]',
      'timestamp_seconds': 261,
      'tip': 'A low number means cash flow is good and the danger of running out of money is '
             'minimized the formula for CCC also highlights the possible areas where '
             'improvements can be made good analytics just as much as Big Ideas can keep a '
             'company profitable.',
      'title': 'What is the Cash Conversion Cycle? (Invoice Finance News)',
      'url': 'https://www.youtube.com/watch?v=Ooq0PnAEf5s&t=261s',
      'video_id': 'Ooq0PnAEf5s'},
     {'author': 'A Simple Model',
      'channel': 'A Simple Model',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:25](https://www.youtube.com/watch?v=DbHq5BHo_XA&t=205s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "In the next video we're going to look at this process in detail by exploring an "
              'example that involves heavy seasonality and comparing it to an example that '
              "does not but otherwise that's all for now thanks for watching.",
      'timestamp': 205,
      'timestamp_label': '[00:03:25]',
      'timestamp_seconds': 205,
      'tip': "In the next video we're going to look at this process in detail by exploring an "
             'example that involves heavy seasonality and comparing it to an example that does '
             "not but otherwise that's all for now thanks for watching.",
      'title': 'The Definition of Working Capital in the Working Capital Peg (A Simple Model)',
      'url': 'https://www.youtube.com/watch?v=DbHq5BHo_XA&t=205s',
      'video_id': 'DbHq5BHo_XA'},
     {'author': 'Flying Start Online',
      'channel': 'Flying Start Online',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:10](https://www.youtube.com/watch?v=rhATJAycfEU&t=610s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Way we have processed your order and it's going to take X amount of days to "
              "reach you once it does I'll be happy to process a.",
      'timestamp': 610,
      'timestamp_label': '[00:10:10]',
      'timestamp_seconds': 610,
      'tip': "Way we have processed your order and it's going to take X amount of days to "
             "reach you once it does I'll be happy to process a.",
      'title': 'DEALING WITH SHOPIFY REFUNDS & CHARGEBACKS (Day 27/30) #Bizathon3 (Flying '
               'Start Online)',
      'url': 'https://www.youtube.com/watch?v=rhATJAycfEU&t=610s',
      'video_id': 'rhATJAycfEU'},
     {'author': 'Tutorials by Manizha & Ryan',
      'channel': 'Tutorials by Manizha & Ryan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:50](https://www.youtube.com/watch?v=B2xFNVqbu7c&t=470s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Share with me or if I left something out then leave that in the comment box '
              'down below I would love to know what you guys have to say and I will catch you '
              'guys guys in the next video.',
      'timestamp': 470,
      'timestamp_label': '[00:07:50]',
      'timestamp_seconds': 470,
      'tip': 'Share with me or if I left something out then leave that in the comment box down '
             'below I would love to know what you guys have to say and I will catch you guys '
             'guys in the next video.',
      'title': 'How To Handle Shopify Refunds And Returns 2026 (For Beginners) (Tutorials by '
               'Manizha & Ryan)',
      'url': 'https://www.youtube.com/watch?v=B2xFNVqbu7c&t=470s',
      'video_id': 'B2xFNVqbu7c'}],
 8: [{'author': 'Understanding Accounting',
      'channel': 'Understanding Accounting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:20](https://www.youtube.com/watch?v=OoegPOU-YCE&t=1520s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This relationship alone establishes neither cash reserves nor overall '
              'liquidity. Calculate credit purchases, collection days, inventory days, payment '
              'days, and the cash conversion cycle. Annual credit sales are 788,400 dollars '
              'and cost of goods sold is 481,800 dollars.',
      'timestamp': 1520,
      'timestamp_label': '[00:25:20]',
      'timestamp_seconds': 1520,
      'tip': 'This relationship alone establishes neither cash reserves nor overall liquidity. '
             'Calculate credit purchases, collection days, inventory days, payment days, and '
             'the cash conversion cycle. Annual credit sales are 788,400 dollars and cost of '
             'goods sold is 481,800 dollars.',
      'title': 'Inventory Estimates and the Cash Conversion Cycle | ACC 300 Lecture 20 '
               '(Understanding Accounting)',
      'url': 'https://www.youtube.com/watch?v=OoegPOU-YCE&t=1520s',
      'video_id': 'OoegPOU-YCE'},
     {'author': 'Davie Fogarty Mentors',
      'channel': 'Davie Fogarty Mentors',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:57](https://www.youtube.com/watch?v=A-7pTamjBIw&t=837s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The homepage turns into a lookbook rather than a store. Instead, feature your '
              'key products front and center. Add a banner that communicates your main offer, '
              "such as free shipping, a seasonal sale, a bundle deal, or even if you're a "
              'brand new brand.',
      'timestamp': 837,
      'timestamp_label': '[00:13:57]',
      'timestamp_seconds': 837,
      'tip': 'The homepage turns into a lookbook rather than a store. Instead, feature your '
             'key products front and center. Add a banner that communicates your main offer, '
             "such as free shipping, a seasonal sale, a bundle deal, or even if you're a brand "
             'new brand.',
      'title': 'How To 4X Your Shopify Conversion Rate (Complete CRO Guide) (Davie Fogarty '
               'Mentors)',
      'url': 'https://www.youtube.com/watch?v=A-7pTamjBIw&t=837s',
      'video_id': 'A-7pTamjBIw'},
     {'author': 'Ecom Chris',
      'channel': 'Ecom Chris',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:03](https://www.youtube.com/watch?v=XQTEnn-3t0E&t=1023s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you have a great product feed and you start to run ads, but your tracking '
              'kind of sucks. You already you feed the algorithm bad input data on your '
              'conversions and how things are going, right?',
      'timestamp': 1023,
      'timestamp_label': '[00:17:03]',
      'timestamp_seconds': 1023,
      'tip': 'If you have a great product feed and you start to run ads, but your tracking '
             'kind of sucks. You already you feed the algorithm bad input data on your '
             'conversions and how things are going, right?',
      'title': 'Your Google Merchant Center Feed Is Losing You Sales! (Ecom Chris)',
      'url': 'https://www.youtube.com/watch?v=XQTEnn-3t0E&t=1023s',
      'video_id': 'XQTEnn-3t0E'},
     {'author': 'WorkflowLife',
      'channel': 'WorkflowLife',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:35](https://www.youtube.com/watch?v=etEhM2kyodk&t=455s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Where do you think AI can realistically help 3PL operations today? Imagine I '
              'know that the tools we have and actually has an AI capabilities, but what is '
              'right tool to go in and use the AI? And where do you see the 3PL operation '
              'using AI?',
      'timestamp': 455,
      'timestamp_label': '[00:07:35]',
      'timestamp_seconds': 455,
      'tip': 'Where do you think AI can realistically help 3PL operations today? Imagine I '
             'know that the tools we have and actually has an AI capabilities, but what is '
             'right tool to go in and use the AI? And where do you see the 3PL operation using '
             'AI?',
      'title': 'What Happens After You Click Buy? | Inside 3PL with Radial (WorkflowLife)',
      'url': 'https://www.youtube.com/watch?v=etEhM2kyodk&t=455s',
      'video_id': 'etEhM2kyodk'},
     {'author': 'Brad Sherman | OperationAMZ',
      'channel': 'Brad Sherman | OperationAMZ',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:54](https://www.youtube.com/watch?v=G9hSjTySxP0&t=954s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '"Can you tell me more about your e-commerce strategy? What does Amazon platform '
              'look like for you?" Or something along the lines of, "Can you tell me more '
              'about your e-commerce strategy?',
      'timestamp': 954,
      'timestamp_label': '[00:15:54]',
      'timestamp_seconds': 954,
      'tip': '"Can you tell me more about your e-commerce strategy? What does Amazon platform '
             'look like for you?" Or something along the lines of, "Can you tell me more about '
             'your e-commerce strategy?',
      'title': 'How to Contact Amazon FBA Wholesale Suppliers in 30 minutes (Brad Sherman | '
               'OperationAMZ)',
      'url': 'https://www.youtube.com/watch?v=G9hSjTySxP0&t=954s',
      'video_id': 'G9hSjTySxP0'},
     {'author': 'Max Crakanthorp',
      'channel': 'Max Crakanthorp',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=FZOo2bNTrzo&t=21s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Google Merchant Center step-by-step live in the account, so your products stay '
              'approved, show up more often, and send better data into Google Ads. For those '
              "of you who don't know me, I'm Max, the founder of Kraken Digital.",
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'Google Merchant Center step-by-step live in the account, so your products stay '
             'approved, show up more often, and send better data into Google Ads. For those of '
             "you who don't know me, I'm Max, the founder of Kraken Digital.",
      'title': 'Set Up Google Merchant Center The Right Way (Full Course) (Max Crakanthorp)',
      'url': 'https://www.youtube.com/watch?v=FZOo2bNTrzo&t=21s',
      'video_id': 'FZOo2bNTrzo'},
     {'author': 'NET not GROSS',
      'channel': 'NET not GROSS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:55](https://www.youtube.com/watch?v=El3a3K2N_sY&t=175s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The model underneath was the same old one: someone runs a store on Amazon or '
              'Walmart with your money. The AI was what changed in the advertising. In another '
              'file, the AI the company described was a repricing tool — software that adjusts '
              'prices.',
      'timestamp': 175,
      'timestamp_label': '[00:02:55]',
      'timestamp_seconds': 175,
      'tip': 'The model underneath was the same old one: someone runs a store on Amazon or '
             'Walmart with your money. The AI was what changed in the advertising. In another '
             'file, the AI the company described was a repricing tool — software that adjusts '
             'prices.',
      'title': 'Done-For-You AI Store: We Read the FTC Files (NET not GROSS)',
      'url': 'https://www.youtube.com/watch?v=El3a3K2N_sY&t=175s',
      'video_id': 'El3a3K2N_sY'},
     {'author': 'Kai Cromwell - eCommerce SEO',
      'channel': 'Kai Cromwell - eCommerce SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:42](https://www.youtube.com/watch?v=W6w0BjjlBs4&t=162s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Would apply to a product page within your shoply store or whatever e-commerce '
              "platform you're operating on be intentional with your keywords and place.",
      'timestamp': 162,
      'timestamp_label': '[00:02:42]',
      'timestamp_seconds': 162,
      'tip': 'Would apply to a product page within your shoply store or whatever e-commerce '
             "platform you're operating on be intentional with your keywords and place.",
      'title': 'How to Increase Organic Revenue with Google Merchant Center Optimization (Full '
               'Guide) (Kai Cromwell - eCommerce SEO)',
      'url': 'https://www.youtube.com/watch?v=W6w0BjjlBs4&t=162s',
      'video_id': 'W6w0BjjlBs4'},
     {'author': 'Jyll Saskin Gales | Google Ads Coach',
      'channel': 'Jyll Saskin Gales | Google Ads Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:00](https://www.youtube.com/watch?v=Q-KrwvAVhR4&t=180s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And I think it is so overlooked, not intentionally, but just because a lot of '
              "us are so in the platform working with Google Ads that we're thinking, right, I "
              'need to work on getting my uh performance up. Why uh is this campaign not '
              'working really well?',
      'timestamp': 180,
      'timestamp_label': '[00:03:00]',
      'timestamp_seconds': 180,
      'tip': 'And I think it is so overlooked, not intentionally, but just because a lot of us '
             "are so in the platform working with Google Ads that we're thinking, right, I "
             'need to work on getting my uh performance up. Why uh is this campaign not '
             'working really well?',
      'title': 'How to Optimize Product Category in Google Merchant Center | Inside Google Ads '
               'course | Casey Gill (Jyll Saskin Gales | Google Ads Coach)',
      'url': 'https://www.youtube.com/watch?v=Q-KrwvAVhR4&t=180s',
      'video_id': 'Q-KrwvAVhR4'},
     {'author': 'PreProduct',
      'channel': 'PreProduct',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=ZXDpWj-RfOQ&t=103s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And then also in Shopify orders admin, we need to apply a fulfillment status of '
              "hold so your 3PL warehouse software doesn't try to fulfill an item which "
              "doesn't actually exist in stock yet. So, let's set up the integration. Jump "
              "into pre-products and we'll go integrations.",
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': 'And then also in Shopify orders admin, we need to apply a fulfillment status of '
             "hold so your 3PL warehouse software doesn't try to fulfill an item which doesn't "
             "actually exist in stock yet. So, let's set up the integration. Jump into "
             "pre-products and we'll go integrations.",
      'title': 'Loop Returns Pre-order Integration for Shopify (PreProduct)',
      'url': 'https://www.youtube.com/watch?v=ZXDpWj-RfOQ&t=103s',
      'video_id': 'ZXDpWj-RfOQ'},
     {'author': 'Grow My Ads',
      'channel': 'Grow My Ads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:58](https://www.youtube.com/watch?v=hY8ZBC3A4uQ&t=298s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s going to be like, you know, 32 oz black spillproof water tumbler Oala or "
              'Bowala or however that gets thrown on there. But if someone searches for a '
              "brand search for Aala, they'll put Owala tumbler.",
      'timestamp': 298,
      'timestamp_label': '[00:04:58]',
      'timestamp_seconds': 298,
      'tip': "'s going to be like, you know, 32 oz black spillproof water tumbler Oala or "
             'Bowala or however that gets thrown on there. But if someone searches for a brand '
             "search for Aala, they'll put Owala tumbler.",
      'title': 'Google Shopping Feed Optimizations for 10X Growth (2026 Updated) (Grow My Ads)',
      'url': 'https://www.youtube.com/watch?v=hY8ZBC3A4uQ&t=298s',
      'video_id': 'hY8ZBC3A4uQ'},
     {'author': 'Wixpa Google Shopping Feed',
      'channel': 'Wixpa Google Shopping Feed',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:45](https://www.youtube.com/watch?v=RHJvGN_6sf0&t=285s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Google Merchant Center is actively receiving your Shopify product data. Before '
              "you celebrate, there's something extremely important you need to know. A "
              'perfect product feed does not guarantee product approval.',
      'timestamp': 285,
      'timestamp_label': '[00:04:45]',
      'timestamp_seconds': 285,
      'tip': 'Google Merchant Center is actively receiving your Shopify product data. Before '
             "you celebrate, there's something extremely important you need to know. A perfect "
             'product feed does not guarantee product approval.',
      'title': 'Shopify Google Merchant Center Product Feed Setup (2026) | Complete Beginner '
               'Guide #shopify #google (Wixpa Google Shopping Feed)',
      'url': 'https://www.youtube.com/watch?v=RHJvGN_6sf0&t=285s',
      'video_id': 'RHJvGN_6sf0'},
     {'author': 'KeyCommerce',
      'channel': 'KeyCommerce',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=UcU7Ishu1lY&t=111s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your products in merant Center clicking on one brings us to its product Details '
              'page where we can review the data Google is working with for what we want to '
              'do.',
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': 'Your products in merant Center clicking on one brings us to its product Details '
             'page where we can review the data Google is working with for what we want to do.',
      'title': 'How To Optimize Your Product Feed & Data In Google Merchant Center '
               '(KeyCommerce)',
      'url': 'https://www.youtube.com/watch?v=UcU7Ishu1lY&t=111s',
      'video_id': 'UcU7Ishu1lY'},
     {'author': 'Laurence Gartside',
      'channel': 'Laurence Gartside',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:03](https://www.youtube.com/watch?v=z3z_GomovEI&t=243s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Subtracting a few numbers but the Simplicity of the formula hides many pitfalls '
              'and nuances choices that we need to make when Gathering the data and '
              "calculating the various components that's where the real work lies.",
      'timestamp': 243,
      'timestamp_label': '[00:04:03]',
      'timestamp_seconds': 243,
      'tip': 'Subtracting a few numbers but the Simplicity of the formula hides many pitfalls '
             'and nuances choices that we need to make when Gathering the data and calculating '
             "the various components that's where the real work lies.",
      'title': 'The Cash Conversion Cycle formula and how to use it (Laurence Gartside)',
      'url': 'https://www.youtube.com/watch?v=z3z_GomovEI&t=243s',
      'video_id': 'z3z_GomovEI'},
     {'author': 'DigiSkills 3.0',
      'channel': 'DigiSkills 3.0',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:16](https://www.youtube.com/watch?v=wy6f7PCtG90&t=16s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'बहुत सारे ऑर्डर्स पर आपको कुछ डिस्प्यूट्स भी फेस करना पड़ सकते हैं। कुछ ऐसा भी '
              'सिनेरियो हो सकता है कि आपने जो प्रोडक्ट शिप की है शिपमेंट के दौरान.',
      'timestamp': 16,
      'timestamp_label': '[00:00:16]',
      'timestamp_seconds': 16,
      'tip': 'बहुत सारे ऑर्डर्स पर आपको कुछ डिस्प्यूट्स भी फेस करना पड़ सकते हैं। कुछ ऐसा भी '
             'सिनेरियो हो सकता है कि आपने जो प्रोडक्ट शिप की है शिपमेंट के दौरान.',
      'title': 'Professional Refund Protocols & Chargebacks Protection | Shopify | Lec 112 | '
               'DigiSkills 3.0 (DigiSkills 3.0)',
      'url': 'https://www.youtube.com/watch?v=wy6f7PCtG90&t=16s',
      'video_id': 'wy6f7PCtG90'}],
 9: [{'author': 'LedgerGurus: Ecommerce Accounting Experts',
      'channel': 'LedgerGurus: Ecommerce Accounting Experts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:55](https://www.youtube.com/watch?v=F-Y1cubdesE&t=355s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's somewhere between the factory and the customer. The longer that cycle is, "
              'the longer your cash is tied up. Everybody gets excited about going '
              'multi-channel. They sign a new relationship with a big wholesaler. They have '
              'net 60 day terms.',
      'timestamp': 355,
      'timestamp_label': '[00:05:55]',
      'timestamp_seconds': 355,
      'tip': "It's somewhere between the factory and the customer. The longer that cycle is, "
             'the longer your cash is tied up. Everybody gets excited about going '
             'multi-channel. They sign a new relationship with a big wholesaler. They have net '
             '60 day terms.',
      'title': 'Cash Conversion Cycle: The Metric EVERY Ecommerce Owner Should Understand '
               '(LedgerGurus: Ecommerce Accounting Experts)',
      'url': 'https://www.youtube.com/watch?v=F-Y1cubdesE&t=355s',
      'video_id': 'F-Y1cubdesE'},
     {'author': 'Understanding Accounting',
      'channel': 'Understanding Accounting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:49:14](https://www.youtube.com/watch?v=GtIbksKcl3Q&t=2954s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'From the operating cycle to the cash conversion cycle. A company acquires '
              'inventory, holds it until sale, and collects payment from the customer. A cash '
              'sale brings in payment at the time of sale.',
      'timestamp': 2954,
      'timestamp_label': '[00:49:14]',
      'timestamp_seconds': 2954,
      'tip': 'From the operating cycle to the cash conversion cycle. A company acquires '
             'inventory, holds it until sale, and collects payment from the customer. A cash '
             'sale brings in payment at the time of sale.',
      'title': 'Inventory Estimates and the Cash Conversion Cycle | ACC 300 Chapter 18 Reading '
               '(Understanding Accounting)',
      'url': 'https://www.youtube.com/watch?v=GtIbksKcl3Q&t=2954s',
      'video_id': 'GtIbksKcl3Q'},
     {'author': 'Vexrulon',
      'channel': 'Vexrulon',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:03](https://www.youtube.com/watch?v=bufdu58UUfo&t=183s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's like, how do I spend some of that extra cash to solidify the brand of me? "
              'So, this is not direct response ads. This is like kind of the big aspirational '
              'moments, these brand moments like we just did this launch this, you know, two '
              'weekends ago.',
      'timestamp': 183,
      'timestamp_label': '[00:03:03]',
      'timestamp_seconds': 183,
      'tip': "It's like, how do I spend some of that extra cash to solidify the brand of me? "
             'So, this is not direct response ads. This is like kind of the big aspirational '
             'moments, these brand moments like we just did this launch this, you know, two '
             'weekends ago.',
      'title': "Alex Hormozi's Guide to Scaling an E-Commerce Brand (Vexrulon)",
      'url': 'https://www.youtube.com/watch?v=bufdu58UUfo&t=183s',
      'video_id': 'bufdu58UUfo'},
     {'author': 'TaxJar',
      'channel': 'TaxJar',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:42](https://www.youtube.com/watch?v=M_AJmScLLXE&t=222s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This sale was made on Amazon into New York. Since New York has a marketplace '
              'facilitator law, Amazon collects the sales tax on this transaction on your '
              'behalf and remits it to the state.',
      'timestamp': 222,
      'timestamp_label': '[00:03:42]',
      'timestamp_seconds': 222,
      'tip': 'This sale was made on Amazon into New York. Since New York has a marketplace '
             'facilitator law, Amazon collects the sales tax on this transaction on your '
             'behalf and remits it to the state.',
      'title': 'TaxJar demo: How to automate sales tax compliance in 2026 (TaxJar)',
      'url': 'https://www.youtube.com/watch?v=M_AJmScLLXE&t=222s',
      'video_id': 'M_AJmScLLXE'},
     {'author': 'Chase Chappell',
      'channel': 'Chase Chappell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:02](https://www.youtube.com/watch?v=daDsoHXE52A&t=542s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And this is very important because we want people to recognize our brand '
              'because it can help increase conversion rates whenever ads are consistent and '
              'synergistic between each of our creatives.',
      'timestamp': 542,
      'timestamp_label': '[00:09:02]',
      'timestamp_seconds': 542,
      'tip': 'And this is very important because we want people to recognize our brand because '
             'it can help increase conversion rates whenever ads are consistent and '
             'synergistic between each of our creatives.',
      'title': 'How To Increase Conversion Rates on Shopify (2026 Guide) (Chase Chappell)',
      'url': 'https://www.youtube.com/watch?v=daDsoHXE52A&t=542s',
      'video_id': 'daDsoHXE52A'},
     {'author': 'PPC Incubator',
      'channel': 'PPC Incubator',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:17](https://www.youtube.com/watch?v=79VrN9FhpT8&t=257s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now that we see all the information, so all the custom labels populated for our '
              'products, we just need to go on our Google Ads account and for example, I will '
              'open the low brand rows and listing groups.',
      'timestamp': 257,
      'timestamp_label': '[00:04:17]',
      'timestamp_seconds': 257,
      'tip': 'Now that we see all the information, so all the custom labels populated for our '
             'products, we just need to go on our Google Ads account and for example, I will '
             'open the low brand rows and listing groups.',
      'title': 'Google Merchant Center - Optimizing Your Feed: Custom Labels with Google '
               'Sheets & Attribute Rules (PPC Incubator)',
      'url': 'https://www.youtube.com/watch?v=79VrN9FhpT8&t=257s',
      'video_id': '79VrN9FhpT8'},
     {'author': 'LedgerGurus: Ecommerce Accounting Experts',
      'channel': 'LedgerGurus: Ecommerce Accounting Experts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:25](https://www.youtube.com/watch?v=pqXEldKeguY&t=1225s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s called a voluntary disclosure agreement. We, we can help you waive any kind "
              'of penalties by working through us, who in turn will be working with the state '
              'to remediate things.',
      'timestamp': 1225,
      'timestamp_label': '[00:20:25]',
      'timestamp_seconds': 1225,
      'tip': "'s called a voluntary disclosure agreement. We, we can help you waive any kind "
             'of penalties by working through us, who in turn will be working with the state '
             'to remediate things.',
      'title': 'Sales Tax 101 with Avalara (LedgerGurus: Ecommerce Accounting Experts)',
      'url': 'https://www.youtube.com/watch?v=pqXEldKeguY&t=1225s',
      'video_id': 'pqXEldKeguY'},
     {'author': 'Davie Fogarty',
      'channel': 'Davie Fogarty',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:51](https://www.youtube.com/watch?v=313GvO3pScc&t=1431s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Realistically, as I said before, you've got a few ways to create the product. "
              'Typically, first-time founders, they will actually outreach to their supplier '
              "to create the product with the supplier. This is good because it's very "
              'cost-effective.',
      'timestamp': 1431,
      'timestamp_label': '[00:23:51]',
      'timestamp_seconds': 1431,
      'tip': "Realistically, as I said before, you've got a few ways to create the product. "
             'Typically, first-time founders, they will actually outreach to their supplier to '
             "create the product with the supplier. This is good because it's very "
             'cost-effective.',
      'title': 'Complete E-commerce Operations Guide (Advanced Tutorial) (Davie Fogarty)',
      'url': 'https://www.youtube.com/watch?v=313GvO3pScc&t=1431s',
      'video_id': '313GvO3pScc'},
     {'author': 'Fazil Automates',
      'channel': 'Fazil Automates',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=4OmfNbuCmDQ&t=79s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Here's the job in plain terms. Every time a paid order lands, this needs to "
              'happen automatically. The customer gets created in my system, my inventory '
              'updates, the order becomes a sales order and an invoice in my accounting and it '
              'gets tracked with the team notifier.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': "Here's the job in plain terms. Every time a paid order lands, this needs to "
             'happen automatically. The customer gets created in my system, my inventory '
             'updates, the order becomes a sales order and an invoice in my accounting and it '
             'gets tracked with the team notifier.',
      'title': 'I Automated My Entire Shopify Store With Claude (No Code) (Fazil Automates)',
      'url': 'https://www.youtube.com/watch?v=4OmfNbuCmDQ&t=79s',
      'video_id': '4OmfNbuCmDQ'},
     {'author': 'Tyler',
      'channel': 'Tyler',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:13](https://www.youtube.com/watch?v=SgxDnkPR36U&t=73s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Since e-commerce sellers have been required to collect and remit state sales '
              'tax the confusion around setting up taxes on e-commerce.',
      'timestamp': 73,
      'timestamp_label': '[00:01:13]',
      'timestamp_seconds': 73,
      'tip': 'Since e-commerce sellers have been required to collect and remit state sales tax '
             'the confusion around setting up taxes on e-commerce.',
      'title': 'Online Sales Tax: A Guide to Economic Nexus & Ecommerce (Tyler)',
      'url': 'https://www.youtube.com/watch?v=SgxDnkPR36U&t=73s',
      'video_id': 'SgxDnkPR36U'},
     {'author': 'Max Crakanthorp',
      'channel': 'Max Crakanthorp',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:15](https://www.youtube.com/watch?v=H4yH9xs030Q&t=855s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's something you kind of need to um you need to buy it for your own brand if "
              'you run a brand, right? Now, if you have a GTIN, put it in. It will give you an '
              'advantage in Merchant Center.',
      'timestamp': 855,
      'timestamp_label': '[00:14:15]',
      'timestamp_seconds': 855,
      'tip': "It's something you kind of need to um you need to buy it for your own brand if "
             'you run a brand, right? Now, if you have a GTIN, put it in. It will give you an '
             'advantage in Merchant Center.',
      'title': 'Live Optimizing A Product In Google Merchant Center (A - Z Guide) (Max '
               'Crakanthorp)',
      'url': 'https://www.youtube.com/watch?v=H4yH9xs030Q&t=855s',
      'video_id': 'H4yH9xs030Q'},
     {'author': 'I Am David Scheuer',
      'channel': 'I Am David Scheuer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:39](https://www.youtube.com/watch?v=HqGwAnGaUf8&t=459s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Here in the comment section you can write something like this um we are looking '
              'at the products your brand offers and would like to set up a wholesale account.',
      'timestamp': 459,
      'timestamp_label': '[00:07:39]',
      'timestamp_seconds': 459,
      'tip': 'Here in the comment section you can write something like this um we are looking '
             'at the products your brand offers and would like to set up a wholesale account.',
      'title': 'How to contact brands and distributors for your Amazon wholesale business! (I '
               'Am David Scheuer)',
      'url': 'https://www.youtube.com/watch?v=HqGwAnGaUf8&t=459s',
      'video_id': 'HqGwAnGaUf8'},
     {'author': 'Brandon Amoroso',
      'channel': 'Brandon Amoroso',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:11](https://www.youtube.com/watch?v=Pwv-LlhTPwo&t=431s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your billing you can import data as well and then your automations you can also '
              "build out more rules so let's say we want to do one ticket is created if the "
              'ticket status or rather the shopify last order.',
      'timestamp': 431,
      'timestamp_label': '[00:07:11]',
      'timestamp_seconds': 431,
      'tip': 'Your billing you can import data as well and then your automations you can also '
             "build out more rules so let's say we want to do one ticket is created if the "
             'ticket status or rather the shopify last order.',
      'title': "Gorgias Overview & Demo | Shopify's #1 Customer Service App (Brandon Amoroso)",
      'url': 'https://www.youtube.com/watch?v=Pwv-LlhTPwo&t=431s',
      'video_id': 'Pwv-LlhTPwo'},
     {'author': 'Grow My Ads',
      'channel': 'Grow My Ads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:40](https://www.youtube.com/watch?v=-w0GraOv2B0&t=520s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That out lots of great value in that video on feed optimizations Beyond just '
              "using these attribute rules so again that's somewhere on the screen or will be "
              "in the description below if not no worries we'll see you on the next video.",
      'timestamp': 520,
      'timestamp_label': '[00:08:40]',
      'timestamp_seconds': 520,
      'tip': 'That out lots of great value in that video on feed optimizations Beyond just '
             "using these attribute rules so again that's somewhere on the screen or will be "
             "in the description below if not no worries we'll see you on the next video.",
      'title': 'How to Optimize Google Ads Shopping Feeds with Feed Attribute Rules '
               '[Step-by-Step Tutorial] (Grow My Ads)',
      'url': 'https://www.youtube.com/watch?v=-w0GraOv2B0&t=520s',
      'video_id': '-w0GraOv2B0'},
     {'author': 'Marcus Lam | High Ticket Dropshipping (AI)',
      'channel': 'Marcus Lam | High Ticket Dropshipping (AI)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:46](https://www.youtube.com/watch?v=b7IMdD7nvhg&t=586s)',
      'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                   'e-commerce operations, contribution-margin underwriting, and automated '
                   'retention (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Also something not a lot of people think about is their store sellable at the '
              "Oney year mark it's an asset yeah I appreciate that thank you stuff for the "
              "goal so okay yeah perfect uh so that's about it Trevor we're going to end the "
              'recording.',
      'timestamp': 586,
      'timestamp_label': '[00:09:46]',
      'timestamp_seconds': 586,
      'tip': 'Also something not a lot of people think about is their store sellable at the '
             "Oney year mark it's an asset yeah I appreciate that thank you stuff for the goal "
             "so okay yeah perfect uh so that's about it Trevor we're going to end the "
             'recording.',
      'title': '9 to 5 Employee Learns Margins After Shipping | High Ticket Dropshipping (Case '
               'Study) (Marcus Lam | High Ticket Dropshipping (AI))',
      'url': 'https://www.youtube.com/watch?v=b7IMdD7nvhg&t=586s',
      'video_id': 'b7IMdD7nvhg'}],
 10: [{'author': 'Leading Social',
       'channel': 'Leading Social',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:26](https://www.youtube.com/watch?v=KpmUvCBEKK4&t=26s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I look at before we scale any e-commerce brand. Number one is contribution '
               "margin. So that's not your revenue, that's not your rorowaz. Contribution "
               'margin is revenue minus cost of goods, shipping, payment fees, and marketing. '
               "That's going to be your real fuel.",
       'timestamp': 26,
       'timestamp_label': '[00:00:26]',
       'timestamp_seconds': 26,
       'tip': 'I look at before we scale any e-commerce brand. Number one is contribution '
              "margin. So that's not your revenue, that's not your rorowaz. Contribution "
              'margin is revenue minus cost of goods, shipping, payment fees, and marketing. '
              "That's going to be your real fuel.",
       'title': '5 Financial Metrics You Must Know Before Scaling an Ecommerce Brand (Beyond '
                'ROAS) (Leading Social)',
       'url': 'https://www.youtube.com/watch?v=KpmUvCBEKK4&t=26s',
       'video_id': 'KpmUvCBEKK4'},
      {'author': 'Dropshipping Deep Dive',
       'channel': 'Dropshipping Deep Dive',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:33](https://www.youtube.com/watch?v=1L4TNDjsICQ&t=813s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Three days is not a window. So the speed of your customer conversation '
               'directly determines whether the supplier shares the cost or you eat all of it. '
               'And that changes your workflow. When a customer reports damage, you need '
               'photos the same day, not eventually.',
       'timestamp': 813,
       'timestamp_label': '[00:13:33]',
       'timestamp_seconds': 813,
       'tip': 'Three days is not a window. So the speed of your customer conversation directly '
              'determines whether the supplier shares the cost or you eat all of it. And that '
              'changes your workflow. When a customer reports damage, you need photos the same '
              'day, not eventually.',
       'title': 'Returns Without the Bleed: Refunds, Exchanges, and the Supplier Reality '
                '(Dropshipping Deep Dive)',
       'url': 'https://www.youtube.com/watch?v=1L4TNDjsICQ&t=813s',
       'video_id': '1L4TNDjsICQ'},
      {'author': 'Macha',
       'channel': 'Macha',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:23](https://www.youtube.com/watch?v=7Ac3MIM55Yc&t=83s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'It replies on email, live chat, SMS, Instagram, Facebook Messenger and '
               'WhatsApp. You need a Shopify store connected to Gorgias to use it. Gorgias '
               'says it automates up to 60% of customer conversations. Gorgias automation is '
               'the scripted side, with no AI writing the reply.',
       'timestamp': 83,
       'timestamp_label': '[00:01:23]',
       'timestamp_seconds': 83,
       'tip': 'It replies on email, live chat, SMS, Instagram, Facebook Messenger and '
              'WhatsApp. You need a Shopify store connected to Gorgias to use it. Gorgias says '
              'it automates up to 60% of customer conversations. Gorgias automation is the '
              'scripted side, with no AI writing the reply.',
       'title': 'Gorgias AI explained (2026): AI Agent, automation and cost (Macha)',
       'url': 'https://www.youtube.com/watch?v=7Ac3MIM55Yc&t=83s',
       'video_id': '7Ac3MIM55Yc'},
      {'author': 'GuidePixel',
       'channel': 'GuidePixel',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:11](https://www.youtube.com/watch?v=3VDc8PoFZa8&t=71s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Inform the customer of any changes made by using the communication tools '
               'within Loop Returns. You can choose to send an automated email update or '
               'contact the customer directly. To track the updated return, you can revisit '
               'the returns dashboard for future reference.',
       'timestamp': 71,
       'timestamp_label': '[00:01:11]',
       'timestamp_seconds': 71,
       'tip': 'Inform the customer of any changes made by using the communication tools within '
              'Loop Returns. You can choose to send an automated email update or contact the '
              'customer directly. To track the updated return, you can revisit the returns '
              'dashboard for future reference.',
       'title': 'How to update Shopify returns with Loop Returns - Step By Step (GuidePixel)',
       'url': 'https://www.youtube.com/watch?v=3VDc8PoFZa8&t=71s',
       'video_id': '3VDc8PoFZa8'},
      {'author': 'TUTOR BASE',
       'channel': 'TUTOR BASE',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:39](https://www.youtube.com/watch?v=qaQ0aFPTDKA&t=99s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "After selecting the appropriate template, it's time to personalize your flow. "
               'Give your automation a distinct and memorable name. This could be something '
               "like post purchase journey core or any name that resonates with your brand's "
               'voice and strategy.',
       'timestamp': 99,
       'timestamp_label': '[00:01:39]',
       'timestamp_seconds': 99,
       'tip': "After selecting the appropriate template, it's time to personalize your flow. "
              'Give your automation a distinct and memorable name. This could be something '
              "like post purchase journey core or any name that resonates with your brand's "
              'voice and strategy.',
       'title': 'How to Set Up Post Purchase Flow in Klaviyo 2026 (Quick Guide) (TUTOR BASE)',
       'url': 'https://www.youtube.com/watch?v=qaQ0aFPTDKA&t=99s',
       'video_id': 'qaQ0aFPTDKA'},
      {'author': 'Asonjf',
       'channel': 'Asonjf',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:28:43](https://www.youtube.com/watch?v=91zki-xXArY&t=1723s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Right yeah basically that's only yeah and and how much is it actually going to "
               'cost to automate your customer service department so to automate uh there are.',
       'timestamp': 1723,
       'timestamp_label': '[00:28:43]',
       'timestamp_seconds': 1723,
       'tip': "Right yeah basically that's only yeah and and how much is it actually going to "
              'cost to automate your customer service department so to automate uh there are.',
       'title': '$200,000 A Month Dropshipping High Ticket Products - Case Study (Asonjf)',
       'url': 'https://www.youtube.com/watch?v=91zki-xXArY&t=1723s',
       'video_id': '91zki-xXArY'},
      {'author': 'ShipSage',
       'channel': 'ShipSage',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:23](https://www.youtube.com/watch?v=CVklpdSeqOA&t=23s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So basically, what they do is they are ecommerce sellers selling on multiple '
               'channels: Amazon, Shopify. And basically, they outgrew their own warehouse. '
               "They spend a lot of time managing their warehouse, and now they're kind of "
               'facing a question: How do they scale, right?',
       'timestamp': 23,
       'timestamp_label': '[00:00:23]',
       'timestamp_seconds': 23,
       'tip': 'So basically, what they do is they are ecommerce sellers selling on multiple '
              'channels: Amazon, Shopify. And basically, they outgrew their own warehouse. '
              "They spend a lot of time managing their warehouse, and now they're kind of "
              'facing a question: How do they scale, right?',
       'title': 'E-Commerce Fulfillment | When You Outgrow Your Warehouse | 3PL Updates in US '
                '| ShipSage (ShipSage)',
       'url': 'https://www.youtube.com/watch?v=CVklpdSeqOA&t=23s',
       'video_id': 'CVklpdSeqOA'},
      {'author': 'Returndotai',
       'channel': 'Returndotai',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:23](https://www.youtube.com/watch?v=JzyBmddGOms&t=83s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'With everything verified and approved, the return is ready to move forward. '
               'Fast, accurate, and fully automated. Configure your store in minutes. Define '
               'return policies, set return windows and conditions that fit your brand.',
       'timestamp': 83,
       'timestamp_label': '[00:01:23]',
       'timestamp_seconds': 83,
       'tip': 'With everything verified and approved, the return is ready to move forward. '
              'Fast, accurate, and fully automated. Configure your store in minutes. Define '
              'return policies, set return windows and conditions that fit your brand.',
       'title': 'Shopify Returns Management App Demo | Automate Returns & Exchanges in 2 '
                'Minutes (Returndotai)',
       'url': 'https://www.youtube.com/watch?v=JzyBmddGOms&t=83s',
       'video_id': 'JzyBmddGOms'},
      {'author': 'Frankly eCommerce',
       'channel': 'Frankly eCommerce',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:26:01](https://www.youtube.com/watch?v=CCtunt0iWMU&t=1561s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And so we want to and that's we don't want to punish people. We just want to "
               "say, hey, if you enjoy this and you're faster at it, let's get you doing it "
               "more. And so, you know, we're trying trying to leverage speed and then have "
               'have a better idea.',
       'timestamp': 1561,
       'timestamp_label': '[00:26:01]',
       'timestamp_seconds': 1561,
       'tip': "And so we want to and that's we don't want to punish people. We just want to "
              "say, hey, if you enjoy this and you're faster at it, let's get you doing it "
              "more. And so, you know, we're trying trying to leverage speed and then have "
              'have a better idea.',
       'title': 'Scaling Creative Brands Through Operations (Frankly eCommerce)',
       'url': 'https://www.youtube.com/watch?v=CCtunt0iWMU&t=1561s',
       'video_id': 'CCtunt0iWMU'},
      {'author': 'Macha',
       'channel': 'Macha',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:20](https://www.youtube.com/watch?v=iqOjQraqwcM&t=80s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You keep paying for your Gorgias help desk whichever agent you pick, so we '
               "only price the AI part. We don't add the scores into one total. A brand "
               'watching price weighs them differently from one with nobody free to build the '
               'agent.',
       'timestamp': 80,
       'timestamp_label': '[00:01:20]',
       'timestamp_seconds': 80,
       'tip': 'You keep paying for your Gorgias help desk whichever agent you pick, so we only '
              "price the AI part. We don't add the scores into one total. A brand watching "
              'price weighs them differently from one with nobody free to build the agent.',
       'title': 'Best AI agent for Gorgias and Shopify support (2026) (Macha)',
       'url': 'https://www.youtube.com/watch?v=iqOjQraqwcM&t=80s',
       'video_id': 'iqOjQraqwcM'},
      {'author': 'Dean Alma',
       'channel': 'Dean Alma',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:31](https://www.youtube.com/watch?v=GYROU1C9Mks&t=91s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Sample the product and send it out for promo videos or to ship it to another '
               'customer and then just reuse it refunds are issued manually via the Shopify '
               "dashboard in the order section okay so that's how you can actually do shipment "
               'refunds and returns.',
       'timestamp': 91,
       'timestamp_label': '[00:01:31]',
       'timestamp_seconds': 91,
       'tip': 'Sample the product and send it out for promo videos or to ship it to another '
              'customer and then just reuse it refunds are issued manually via the Shopify '
              "dashboard in the order section okay so that's how you can actually do shipment "
              'refunds and returns.',
       'title': 'How to Deal With Refunds & Returns (Shopify Dropshipping) (Dean Alma)',
       'url': 'https://www.youtube.com/watch?v=GYROU1C9Mks&t=91s',
       'video_id': 'GYROU1C9Mks'},
      {'author': 'Amol Walunj',
       'channel': 'Amol Walunj',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=QZz9_VSA1lA&t=15s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Here's how a Savano's agent handles that across Shopify and Gorgeous >>  >> "
               'inside the policies you set.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': "Here's how a Savano's agent handles that across Shopify and Gorgeous >>  >> "
              'inside the policies you set.',
       'title': 'How to Automate Gorgias Customer Support with Cevanos AI | Live Demo (Amol '
                'Walunj)',
       'url': 'https://www.youtube.com/watch?v=QZz9_VSA1lA&t=15s',
       'video_id': 'QZz9_VSA1lA'},
      {'author': 'ShipWise',
       'channel': 'ShipWise',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:14](https://www.youtube.com/watch?v=PTU-PzhQg_4&t=254s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Over again it gets tiring and so if we can free up that for the staff because '
               'again that allows us to scale and the scalability of shipwise is literally '
               "there's no ceiling to that piece we were looking for a partner and we found "
               'that partner in ship wise.',
       'timestamp': 254,
       'timestamp_label': '[00:04:14]',
       'timestamp_seconds': 254,
       'tip': 'Over again it gets tiring and so if we can free up that for the staff because '
              'again that allows us to scale and the scalability of shipwise is literally '
              "there's no ceiling to that piece we were looking for a partner and we found "
              'that partner in ship wise.',
       'title': 'How this 3PL doubled their daily throughput | SKU Distribution | Case Study '
                '(ShipWise)',
       'url': 'https://www.youtube.com/watch?v=PTU-PzhQg_4&t=254s',
       'video_id': 'PTU-PzhQg_4'},
      {'author': 'Tim Sutton | Google Ads | Launchpresso',
       'channel': 'Tim Sutton | Google Ads | Launchpresso',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:27](https://www.youtube.com/watch?v=APb0cOGKROE&t=87s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "For today's example, I'm going to show you how to do that using my example "
               'store, CheapCampingGear. And coming across to my Google Merchant Center '
               'account that is associated with that test store. If you come across to '
               "products on the left, you'll see all your products.",
       'timestamp': 87,
       'timestamp_label': '[00:01:27]',
       'timestamp_seconds': 87,
       'tip': "For today's example, I'm going to show you how to do that using my example "
              'store, CheapCampingGear. And coming across to my Google Merchant Center account '
              'that is associated with that test store. If you come across to products on the '
              "left, you'll see all your products.",
       'title': 'How to Master Google Merchant Center Custom Labels in 5 Minutes! (Tim Sutton '
                '| Google Ads | Launchpresso)',
       'url': 'https://www.youtube.com/watch?v=APb0cOGKROE&t=87s',
       'video_id': 'APb0cOGKROE'},
      {'author': 'LedgerGurus: Ecommerce Accounting Experts',
       'channel': 'LedgerGurus: Ecommerce Accounting Experts',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:25:50](https://www.youtube.com/watch?v=1L7s6llWlRo&t=1550s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Again feel free to let us know if you have any questions or any comments any '
               "feedbacks about these three different softwares I'd love to hear what you "
               'think as well thank you so much and have a great day bye.',
       'timestamp': 1550,
       'timestamp_label': '[00:25:50]',
       'timestamp_seconds': 1550,
       'tip': 'Again feel free to let us know if you have any questions or any comments any '
              "feedbacks about these three different softwares I'd love to hear what you think "
              'as well thank you so much and have a great day bye.',
       'title': '2020 Sales Tax Apps for Online Sellers | Avalara, Taxjar, and Taxify '
                '(LedgerGurus: Ecommerce Accounting Experts)',
       'url': 'https://www.youtube.com/watch?v=1L7s6llWlRo&t=1550s',
       'video_id': '1L7s6llWlRo'}],
 11: [{'author': 'Marcus Lam | High Ticket Dropshipping (AI)',
       'channel': 'Marcus Lam | High Ticket Dropshipping (AI)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:16](https://www.youtube.com/watch?v=r2ydHddjtIw&t=136s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re wrong, but that business model is very very outdated and it's logistically "
               'very hard to scale. Any e-commerce owner that has a drop shipping store will '
               'tell you that, you know, you want to go into branding, but building brand '
               'requires so much capital upfront.',
       'timestamp': 136,
       'timestamp_label': '[00:02:16]',
       'timestamp_seconds': 136,
       'tip': "'re wrong, but that business model is very very outdated and it's logistically "
              'very hard to scale. Any e-commerce owner that has a drop shipping store will '
              'tell you that, you know, you want to go into branding, but building brand '
              'requires so much capital upfront.',
       'title': 'How to Dropship as an Authorized Dealer in 2026 | High Ticket Dropshipping '
                '(Marcus Lam | High Ticket Dropshipping (AI))',
       'url': 'https://www.youtube.com/watch?v=r2ydHddjtIw&t=136s',
       'video_id': 'r2ydHddjtIw'},
      {'author': 'Sales Tax at Scale',
       'channel': 'Sales Tax at Scale',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:52](https://www.youtube.com/watch?v=5Dtw2cworM0&t=532s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'What sets them apart is their customer service and their personal approach. '
               'So, here is how I would decide. Choose Avalara if you are a large enterprise '
               'with global operations, an in-house tax team, and the budget to match.',
       'timestamp': 532,
       'timestamp_label': '[00:08:52]',
       'timestamp_seconds': 532,
       'tip': 'What sets them apart is their customer service and their personal approach. So, '
              'here is how I would decide. Choose Avalara if you are a large enterprise with '
              'global operations, an in-house tax team, and the budget to match.',
       'title': 'Avalara? TaxJar? TaxCloud? The Honest Comparison for Ecommerce (Sales Tax at '
                'Scale)',
       'url': 'https://www.youtube.com/watch?v=5Dtw2cworM0&t=532s',
       'video_id': '5Dtw2cworM0'},
      {'author': 'Nick Theriot',
       'channel': 'Nick Theriot',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:25](https://www.youtube.com/watch?v=iacAWRoEwXI&t=85s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Google Ads or email agency. From my experience, we've seen mostly people hire "
               'out Google agencies and email agencies at this stage and continue to run their '
               'own Facebook ads. This is actually going to help us scale further through '
               'channel expansion.',
       'timestamp': 85,
       'timestamp_label': '[00:01:25]',
       'timestamp_seconds': 85,
       'tip': "Google Ads or email agency. From my experience, we've seen mostly people hire "
              'out Google agencies and email agencies at this stage and continue to run their '
              'own Facebook ads. This is actually going to help us scale further through '
              'channel expansion.',
       'title': 'Every Level of Scaling an ECOM Brand ($0, $30k, $100k, $1m, $10m) (Nick '
                'Theriot)',
       'url': 'https://www.youtube.com/watch?v=iacAWRoEwXI&t=85s',
       'video_id': 'iacAWRoEwXI'},
      {'author': 'ZEOS',
       'channel': 'ZEOS',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=xEx0Lhv0wec&t=21s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Here we unpack all things e-commerce, logistics, innovation, and Europe '
               'tailored to fashion and lifestyle. In this episode, we talk about your own '
               'e-commerce store and how you can scale your online TTC operations across '
               'Europe.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'Here we unpack all things e-commerce, logistics, innovation, and Europe '
              'tailored to fashion and lifestyle. In this episode, we talk about your own '
              'e-commerce store and how you can scale your online TTC operations across '
              'Europe.',
       'title': 'Scaling Own.Com in Europe | Business Casual with Luis Ribeiro (ZEOS)',
       'url': 'https://www.youtube.com/watch?v=xEx0Lhv0wec&t=21s',
       'video_id': 'xEx0Lhv0wec'},
      {'author': 'Witners Shipping',
       'channel': 'Witners Shipping',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:48](https://www.youtube.com/watch?v=8I51jDAoe-E&t=228s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Add them up, then divide by the number of units to get a landed cost per unit. '
               'W I T E E R S has in-house licensed UAE customs brokers handling imports, '
               'exports, and free zone movements with air, ocean, and road freight through one '
               'accountable team.',
       'timestamp': 228,
       'timestamp_label': '[00:03:48]',
       'timestamp_seconds': 228,
       'tip': 'Add them up, then divide by the number of units to get a landed cost per unit. '
              'W I T E E R S has in-house licensed UAE customs brokers handling imports, '
              'exports, and free zone movements with air, ocean, and road freight through one '
              'accountable team.',
       'title': 'How to Work Out Landed Cost for a Shipment Into Dubai (Witners Shipping)',
       'url': 'https://www.youtube.com/watch?v=8I51jDAoe-E&t=228s',
       'video_id': '8I51jDAoe-E'},
      {'author': 'MoreMozi',
       'channel': 'MoreMozi',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:28](https://www.youtube.com/watch?v=raqfsvgSW0o&t=208s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Okay, so let's go to the other one. Spend more paid ads, make more make more "
               'content, right? Um if you want to really get the brand where it wants to be, I '
               "would you'll probably get in the neighborhood of somewhere of like this is me "
               'just like shooting from the hip here.',
       'timestamp': 208,
       'timestamp_label': '[00:03:28]',
       'timestamp_seconds': 208,
       'tip': "Okay, so let's go to the other one. Spend more paid ads, make more make more "
              'content, right? Um if you want to really get the brand where it wants to be, I '
              "would you'll probably get in the neighborhood of somewhere of like this is me "
              'just like shooting from the hip here.',
       'title': 'Helping an E-Commerce Brand Doing $5M/Year Scale (MoreMozi)',
       'url': 'https://www.youtube.com/watch?v=raqfsvgSW0o&t=208s',
       'video_id': 'raqfsvgSW0o'},
      {'author': 'EICOM Institute',
       'channel': 'EICOM Institute',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:22:23](https://www.youtube.com/watch?v=TZ1BQdO4bl4&t=1343s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Creative and content management we need to uh if you you we want to hyper '
               'personalize we need to create content and to create content that scale you.',
       'timestamp': 1343,
       'timestamp_label': '[00:22:23]',
       'timestamp_seconds': 1343,
       'tip': 'Creative and content management we need to uh if you you we want to hyper '
              'personalize we need to create content and to create content that scale you.',
       'title': 'Scaling Omnichannel Personalization | Commerce Chats (EICOM Institute)',
       'url': 'https://www.youtube.com/watch?v=TZ1BQdO4bl4&t=1343s',
       'video_id': 'TZ1BQdO4bl4'},
      {'author': 'Amazon Seller School',
       'channel': 'Amazon Seller School',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:49](https://www.youtube.com/watch?v=x2RzKux5lK0&t=49s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Automation company and they started contacting him claiming to be a Russian '
               "Shadow team and we're showing him his home address social security number.",
       'timestamp': 49,
       'timestamp_label': '[00:00:49]',
       'timestamp_seconds': 49,
       'tip': 'Automation company and they started contacting him claiming to be a Russian '
              "Shadow team and we're showing him his home address social security number.",
       'title': 'FTC Sues Amazon Automation Company for Passive Income Scams & Death Threats '
                '(Amazon Seller School)',
       'url': 'https://www.youtube.com/watch?v=x2RzKux5lK0&t=49s',
       'video_id': 'x2RzKux5lK0'},
      {'author': 'Cherry Bekaert',
       'channel': 'Cherry Bekaert',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:50](https://www.youtube.com/watch?v=rUvJ4UwGqiA&t=50s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Amazon warehouse or a 3pl but what about economic nexus well this is the new '
               'kid on the block economic nexus came around in june 2018.',
       'timestamp': 50,
       'timestamp_label': '[00:00:50]',
       'timestamp_seconds': 50,
       'tip': 'Amazon warehouse or a 3pl but what about economic nexus well this is the new '
              'kid on the block economic nexus came around in june 2018.',
       'title': 'Sales & Use Tax: eCommerce Nexus (Cherry Bekaert)',
       'url': 'https://www.youtube.com/watch?v=rUvJ4UwGqiA&t=50s',
       'video_id': 'rUvJ4UwGqiA'},
      {'author': 'Ryan McKenzie',
       'channel': 'Ryan McKenzie',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:57](https://www.youtube.com/watch?v=jmsERJHMp_0&t=237s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The third option is to leverage human resources. What I mean by that is hire a '
               'team internally. This is not the solution for 98 percent of us. If my company, '
               "we have this massive tax team now it's, it's massive.",
       'timestamp': 237,
       'timestamp_label': '[00:03:57]',
       'timestamp_seconds': 237,
       'tip': 'The third option is to leverage human resources. What I mean by that is hire a '
              'team internally. This is not the solution for 98 percent of us. If my company, '
              "we have this massive tax team now it's, it's massive.",
       'title': "Don't Get Crushed by Ecom Sales Tax! Learn the Wayfair Secret to Survival "
                '(Ryan McKenzie)',
       'url': 'https://www.youtube.com/watch?v=jmsERJHMp_0&t=237s',
       'video_id': 'jmsERJHMp_0'},
      {'author': 'Prediko AI Inventory Management',
       'channel': 'Prediko AI Inventory Management',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:26:02](https://www.youtube.com/watch?v=P-gBTGovRRs&t=1562s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Q&A panel for questions now. Feel free to post yours if you have any. And um '
               "join joining me today uh sorry I didn't do the introductions earlier. Joining "
               'me today is Isaiah, our customer success manager for a US region.',
       'timestamp': 1562,
       'timestamp_label': '[00:26:02]',
       'timestamp_seconds': 1562,
       'tip': 'Q&A panel for questions now. Feel free to post yours if you have any. And um '
              "join joining me today uh sorry I didn't do the introductions earlier. Joining "
              'me today is Isaiah, our customer success manager for a US region.',
       'title': 'How to Set Up Prediko: Shopify Inventory Forecasting, Purchase Orders & Raw '
                'Materials (Onboarding) (Prediko AI Inventory Management)',
       'url': 'https://www.youtube.com/watch?v=P-gBTGovRRs&t=1562s',
       'video_id': 'P-gBTGovRRs'},
      {'author': 'Justin Lalonde',
       'channel': 'Justin Lalonde',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=la7VuqSuHHE&t=15s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Some reason a big pool of our clients are within the fashion space which led '
               'us to become experts at marketing for these types of e-commerce brands after '
               'a.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Some reason a big pool of our clients are within the fashion space which led us '
              'to become experts at marketing for these types of e-commerce brands after a.',
       'title': 'How I Would Scale A Fashion Ecom Brand! (Justin Lalonde)',
       'url': 'https://www.youtube.com/watch?v=la7VuqSuHHE&t=15s',
       'video_id': 'la7VuqSuHHE'},
      {'author': 'US Customs Clearing',
       'channel': 'US Customs Clearing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:13](https://www.youtube.com/watch?v=DLfvskykJiY&t=253s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Budgeting pricing and ensuring profitability in import operations remember to '
               'factor in all the components we discussed gather reliable information and '
               'optimize your processes for successful importing.',
       'timestamp': 253,
       'timestamp_label': '[00:04:13]',
       'timestamp_seconds': 253,
       'tip': 'Budgeting pricing and ensuring profitability in import operations remember to '
              'factor in all the components we discussed gather reliable information and '
              'optimize your processes for successful importing.',
       'title': 'How Do I Calculate The Landed Cost Of Imported Goods Into The USA? (US '
                'Customs Clearing)',
       'url': 'https://www.youtube.com/watch?v=DLfvskykJiY&t=253s',
       'video_id': 'DLfvskykJiY'},
      {'author': 'Eric Andrews Clips',
       'channel': 'Eric Andrews Clips',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:03](https://www.youtube.com/watch?v=tj2W9oEqeQo&t=123s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Total orders and you can see that 64. and again you finally take the '
               'Fulfillment you add up all the Fulfillment expenses and then you divide it by '
               'the total orders and the average would be 74. so on average you make 100 of '
               'contribution margin per order.',
       'timestamp': 123,
       'timestamp_label': '[00:02:03]',
       'timestamp_seconds': 123,
       'tip': 'Total orders and you can see that 64. and again you finally take the '
              'Fulfillment you add up all the Fulfillment expenses and then you divide it by '
              'the total orders and the average would be 74. so on average you make 100 of '
              'contribution margin per order.',
       'title': 'Master Contribution Margins for eCommerce (Eric Andrews Clips)',
       'url': 'https://www.youtube.com/watch?v=tj2W9oEqeQo&t=123s',
       'video_id': 'tj2W9oEqeQo'},
      {'author': 'Marketing Business Network',
       'channel': 'Marketing Business Network',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:10](https://www.youtube.com/watch?v=C5Ut79jWwHA&t=130s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Missed deadlines may damage relationships or bring charges. Likewise, keeping '
               'too little stock can leave customers waiting and cost the company sales. Some '
               'businesses collect customer money before they pay suppliers, producing a '
               'negative cash conversion cycle.',
       'timestamp': 130,
       'timestamp_label': '[00:02:10]',
       'timestamp_seconds': 130,
       'tip': 'Missed deadlines may damage relationships or bring charges. Likewise, keeping '
              'too little stock can leave customers waiting and cost the company sales. Some '
              'businesses collect customer money before they pay suppliers, producing a '
              'negative cash conversion cycle.',
       'title': 'What is the Cash Conversion Cycle? (Marketing Business Network)',
       'url': 'https://www.youtube.com/watch?v=C5Ut79jWwHA&t=130s',
       'video_id': 'C5Ut79jWwHA'}],
 12: [{'author': 'LedgerGurus: Ecommerce Accounting Experts',
       'channel': 'LedgerGurus: Ecommerce Accounting Experts',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:02](https://www.youtube.com/watch?v=e5r7-KT6mQ0&t=62s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Shipping costs can vary based on the product item, size, weight, or bundle of '
               'products. Payment processing fees can vary based on the credit card that the '
               'customer uses. Finally, advertising costs can vary by the month, week, day, '
               'and even time of day.',
       'timestamp': 62,
       'timestamp_label': '[00:01:02]',
       'timestamp_seconds': 62,
       'tip': 'Shipping costs can vary based on the product item, size, weight, or bundle of '
              'products. Payment processing fees can vary based on the credit card that the '
              'customer uses. Finally, advertising costs can vary by the month, week, day, and '
              'even time of day.',
       'title': 'Ecommerce Contribution Margin Explained (LedgerGurus: Ecommerce Accounting '
                'Experts)',
       'url': 'https://www.youtube.com/watch?v=e5r7-KT6mQ0&t=62s',
       'video_id': 'e5r7-KT6mQ0'},
      {'author': 'Luke Kermode, CFA',
       'channel': 'Luke Kermode, CFA',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:03](https://www.youtube.com/watch?v=1gBvyu9ADGo&t=303s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "The Day sales outstanding so we've got the operating cycle so how do we bridge "
               'to the um cash conversion cycle well if you remember from the formula we need '
               'to deduct the days payable.',
       'timestamp': 303,
       'timestamp_label': '[00:05:03]',
       'timestamp_seconds': 303,
       'tip': "The Day sales outstanding so we've got the operating cycle so how do we bridge "
              'to the um cash conversion cycle well if you remember from the formula we need '
              'to deduct the days payable.',
       'title': 'Cash Conversion Cycle Explained | CFA Level 1 Corporate Issuers (Luke '
                'Kermode, CFA)',
       'url': 'https://www.youtube.com/watch?v=1gBvyu9ADGo&t=303s',
       'video_id': '1gBvyu9ADGo'},
      {'author': 'built with ali',
       'channel': 'built with ali',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:18](https://www.youtube.com/watch?v=Mf4bZiQ2-Fc&t=198s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s called an authorized dealer or an authorized retailer. And basically, they "
               "will ship on your behalf directly to the customer. That's why it's drop "
               "shipping. And they'll usually do that within the US from US-based warehouses "
               'within the same business day.',
       'timestamp': 198,
       'timestamp_label': '[00:03:18]',
       'timestamp_seconds': 198,
       'tip': "'s called an authorized dealer or an authorized retailer. And basically, they "
              "will ship on your behalf directly to the customer. That's why it's drop "
              "shipping. And they'll usually do that within the US from US-based warehouses "
              'within the same business day.',
       'title': 'how i find dropshipping products that sell for $6,135.12 each (the opposite '
                'of what gurus tell you) (built with ali)',
       'url': 'https://www.youtube.com/watch?v=Mf4bZiQ2-Fc&t=198s',
       'video_id': 'Mf4bZiQ2-Fc'},
      {'author': 'Macha',
       'channel': 'Macha',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:50](https://www.youtube.com/watch?v=VsY0GsB1UI0&t=410s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Most teams have their first category live within a week. Setup is included in '
               'every plan, with no setup fee. Plans start at two hundred and ninety-nine '
               'dollars a month for seven hundred and fifty tickets, about forty cents a '
               'ticket.',
       'timestamp': 410,
       'timestamp_label': '[00:06:50]',
       'timestamp_seconds': 410,
       'tip': 'Most teams have their first category live within a week. Setup is included in '
              'every plan, with no setup fee. Plans start at two hundred and ninety-nine '
              'dollars a month for seven hundred and fifty tickets, about forty cents a '
              'ticket.',
       'title': 'AI for "where is my order" tickets in Gorgias (Macha)',
       'url': 'https://www.youtube.com/watch?v=VsY0GsB1UI0&t=410s',
       'video_id': 'VsY0GsB1UI0'},
      {'author': 'Stord',
       'channel': 'Stord',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:28](https://www.youtube.com/watch?v=eZY2MYqExrQ&t=88s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'One that can endure the tumultuous environment of rapid growth e-commerce '
               'businesses. We have the ability to rapidly launch nationwide fulfillment for '
               'brands in days when providers or tariffs change. We can reduce parcel costs '
               'when carriers levy new GRI.',
       'timestamp': 88,
       'timestamp_label': '[00:01:28]',
       'timestamp_seconds': 88,
       'tip': 'One that can endure the tumultuous environment of rapid growth e-commerce '
              'businesses. We have the ability to rapidly launch nationwide fulfillment for '
              'brands in days when providers or tariffs change. We can reduce parcel costs '
              'when carriers levy new GRI.',
       'title': 'A Message On New Tariffs And De Minimis (Section 321) (Stord)',
       'url': 'https://www.youtube.com/watch?v=eZY2MYqExrQ&t=88s',
       'video_id': 'eZY2MYqExrQ'},
      {'author': 'Avalara',
       'channel': 'Avalara',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:11](https://www.youtube.com/watch?v=RRnAKNi_DBU&t=71s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Nexus and states where you might need to start collecting and remitting sales '
               'tax. AvaTax not only calculates U. Simply select all countries that you sell '
               'into and AvaTax will calculate those taxes as well as customs duties and '
               'tariffs. Two Is the customer taxable?',
       'timestamp': 71,
       'timestamp_label': '[00:01:11]',
       'timestamp_seconds': 71,
       'tip': 'Nexus and states where you might need to start collecting and remitting sales '
              'tax. AvaTax not only calculates U. Simply select all countries that you sell '
              'into and AvaTax will calculate those taxes as well as customs duties and '
              'tariffs. Two Is the customer taxable?',
       'title': 'Avalara AvaTax Demo (Avalara)',
       'url': 'https://www.youtube.com/watch?v=RRnAKNi_DBU&t=71s',
       'video_id': 'RRnAKNi_DBU'},
      {'author': 'Marvin',
       'channel': 'Marvin',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=fHLUiiiopmw&t=15s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "FBA business now I've helped over 600 people start and grow their own Amazon "
               'FBA business many of them going from zero to over 100K per month in under one.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': "FBA business now I've helped over 600 people start and grow their own Amazon "
              'FBA business many of them going from zero to over 100K per month in under one.',
       'title': 'Amazon Wholesale || How To Find Wholesale Suppliers For Amazon FBA (Marvin)',
       'url': 'https://www.youtube.com/watch?v=fHLUiiiopmw&t=15s',
       'video_id': 'fHLUiiiopmw'},
      {'author': 'Milan Raviji│Klaviyo & Email Marketing',
       'channel': 'Milan Raviji│Klaviyo & Email Marketing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:55](https://www.youtube.com/watch?v=6xiaPZPDBCQ&t=355s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Now the targeting here, we only chose this for products where the churn was '
               'extremely high on month one. And that was their anal glands timing analogy '
               'products. And you can just set the flow to trigger after x amount of days of '
               'them receiving their box.',
       'timestamp': 355,
       'timestamp_label': '[00:05:55]',
       'timestamp_seconds': 355,
       'tip': 'Now the targeting here, we only chose this for products where the churn was '
              'extremely high on month one. And that was their anal glands timing analogy '
              'products. And you can just set the flow to trigger after x amount of days of '
              'them receiving their box.',
       'title': 'Recharge Subscription Flows Tutorial For 2026 (Full Strategy) (Milan '
                'Raviji│Klaviyo & Email Marketing)',
       'url': 'https://www.youtube.com/watch?v=6xiaPZPDBCQ&t=355s',
       'video_id': '6xiaPZPDBCQ'},
      {'author': 'FlexSync: Shopify Stock & Order Sync',
       'channel': 'FlexSync: Shopify Stock & Order Sync',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:09](https://www.youtube.com/watch?v=oYy3k8xOKpA&t=249s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Track every SKU, set reorder points, count regularly, and keep one source of '
               'truth. Flex Sync has a free plan for up to 500 SKUs, and paid plans come with '
               'a 14-day free trial. Find Flex Sync on the Shopify app store and start '
               'managing your inventory from Google Sheets.',
       'timestamp': 249,
       'timestamp_label': '[00:04:09]',
       'timestamp_seconds': 249,
       'tip': 'Track every SKU, set reorder points, count regularly, and keep one source of '
              'truth. Flex Sync has a free plan for up to 500 SKUs, and paid plans come with a '
              '14-day free trial. Find Flex Sync on the Shopify app store and start managing '
              'your inventory from Google Sheets.',
       'title': 'The Ultimate Shopify Inventory Management Guide | Stop Losing Sales! '
                '(FlexSync: Shopify Stock & Order Sync)',
       'url': 'https://www.youtube.com/watch?v=oYy3k8xOKpA&t=249s',
       'video_id': 'oYy3k8xOKpA'},
      {'author': 'Avalara',
       'channel': 'Avalara',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:36](https://www.youtube.com/watch?v=EtT3YoVfP0c&t=996s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'How do I then track, you know, the the where of tomorrow of next week of next '
               'month of next year. But we always start with where do we need to be collecting '
               'today? I want to jump in there real quick because we have talked about '
               'tracking the sales and the number of sales.',
       'timestamp': 996,
       'timestamp_label': '[00:16:36]',
       'timestamp_seconds': 996,
       'tip': 'How do I then track, you know, the the where of tomorrow of next week of next '
              'month of next year. But we always start with where do we need to be collecting '
              'today? I want to jump in there real quick because we have talked about tracking '
              'the sales and the number of sales.',
       'title': 'Webinar: Ecommerce Sales Tax Basics for Growing Sellers (Avalara)',
       'url': 'https://www.youtube.com/watch?v=EtT3YoVfP0c&t=996s',
       'video_id': 'EtT3YoVfP0c'},
      {'author': 'Smart Capital',
       'channel': 'Smart Capital',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:27](https://www.youtube.com/watch?v=8R8um_CLrWI&t=147s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But the mechanics are real, and they are the same mechanics working sellers '
               'use every day. In the next few minutes, you will learn the exact order volume '
               'number where self-fulfillment starts costing you more than a 3PL.',
       'timestamp': 147,
       'timestamp_label': '[00:02:27]',
       'timestamp_seconds': 147,
       'tip': 'But the mechanics are real, and they are the same mechanics working sellers use '
              'every day. In the next few minutes, you will learn the exact order volume '
              'number where self-fulfillment starts costing you more than a 3PL.',
       'title': 'How to Automate E-Commerce Fulfillment: Best US 3PL Partners for 2-Day '
                'Shipping 2026 (Smart Capital)',
       'url': 'https://www.youtube.com/watch?v=8R8um_CLrWI&t=147s',
       'video_id': '8R8um_CLrWI'},
      {'author': 'Sunrise Integration',
       'channel': 'Sunrise Integration',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:52](https://www.youtube.com/watch?v=daoVeRnScfo&t=472s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Your Shopify store is now ready to start accepting customer returns and if you '
               'need help configuring your Shopify store please contact our eCommerce experts '
               'at Sunrise integration.',
       'timestamp': 472,
       'timestamp_label': '[00:07:52]',
       'timestamp_seconds': 472,
       'tip': 'Your Shopify store is now ready to start accepting customer returns and if you '
              'need help configuring your Shopify store please contact our eCommerce experts '
              'at Sunrise integration.',
       'title': 'How To Use Shopify Self-Serve Returns - Shopify Tutorial (Sunrise '
                'Integration)',
       'url': 'https://www.youtube.com/watch?v=daoVeRnScfo&t=472s',
       'video_id': 'daoVeRnScfo'},
      {'author': 'Klaviyo',
       'channel': 'Klaviyo',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:24](https://www.youtube.com/watch?v=zfCLuKMRGEE&t=84s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'During major marketing moments for your brand, like a holiday sale, product '
               'launch, or a large site wide promotion, send the same message through both '
               'email and SMS to reinforce the importance of the event.',
       'timestamp': 84,
       'timestamp_label': '[00:01:24]',
       'timestamp_seconds': 84,
       'tip': 'During major marketing moments for your brand, like a holiday sale, product '
              'launch, or a large site wide promotion, send the same message through both '
              'email and SMS to reinforce the importance of the event.',
       'title': 'Klaviyo SMS & Email Integration: Boost Conversions & Engagement | Klaviyo '
                'Academy (Klaviyo)',
       'url': 'https://www.youtube.com/watch?v=zfCLuKMRGEE&t=84s',
       'video_id': 'zfCLuKMRGEE'},
      {'author': 'Justin Lalonde',
       'channel': 'Justin Lalonde',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:08](https://www.youtube.com/watch?v=rBcV_0ROMHM&t=428s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Not worse comes to worse we'll just leave you with a free action plan to "
               'implement on your own so make sure you check out other videos on the channel '
               "for some more useful ecommerce marketing tips and I'll see you guys in the "
               'next video peace.',
       'timestamp': 428,
       'timestamp_label': '[00:07:08]',
       'timestamp_seconds': 428,
       'tip': "Not worse comes to worse we'll just leave you with a free action plan to "
              'implement on your own so make sure you check out other videos on the channel '
              "for some more useful ecommerce marketing tips and I'll see you guys in the next "
              'video peace.',
       'title': 'The BITTER Truth About Scaling An Ecommerce Business! - DO THIS INSTEAD! '
                '(Justin Lalonde)',
       'url': 'https://www.youtube.com/watch?v=rBcV_0ROMHM&t=428s',
       'video_id': 'rBcV_0ROMHM'},
      {'author': 'Understanding Accounting',
       'channel': 'Understanding Accounting',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:24:44](https://www.youtube.com/watch?v=OoegPOU-YCE&t=1484s)',
       'relevance': 'Attributed practitioner commentary on lean 3PL-backed & authorized-dealer '
                    'e-commerce operations, contribution-margin underwriting, and automated '
                    'retention (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Subtract the unrounded payment period to obtain about 55. 74 days, roughly a '
               '56-day financing gap. Payroll, capital spending, debt service, and taxes still '
               'require separate cash forecasts.',
       'timestamp': 1484,
       'timestamp_label': '[00:24:44]',
       'timestamp_seconds': 1484,
       'tip': 'Subtract the unrounded payment period to obtain about 55. 74 days, roughly a '
              '56-day financing gap. Payroll, capital spending, debt service, and taxes still '
              'require separate cash forecasts.',
       'title': 'Inventory Estimates and the Cash Conversion Cycle | ACC 300 Lecture 20 '
                '(Understanding Accounting)',
       'url': 'https://www.youtube.com/watch?v=OoegPOU-YCE&t=1484s',
       'video_id': 'OoegPOU-YCE'}]}
