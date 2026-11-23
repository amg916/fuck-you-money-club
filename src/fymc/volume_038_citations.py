"""Curated 180-citation Contingent Corporate Bill-Audit & Tax-Credit Recovery baseline (15 per chapter across Q1-Q12) mined strictly from verified Contingent Corporate Bill-Audit & Tax-Credit Recovery YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'179d',
     '230',
     '250k',
     '8850',
     'access',
     'agreement',
     'allocation',
     'api',
     'appeal',
     'area',
     'assessment',
     'ats',
     'audit',
     'auditing',
     'authorization',
     'automated',
     'bill',
     'board',
     'building',
     'business',
     'call',
     'cam',
     'caps',
     'carrier',
     'case',
     'certification',
     'cfos',
     'charge',
     'circuit',
     'circular',
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
 2: {'179d',
     '230',
     '250k',
     '8850',
     'access',
     'agreement',
     'allocation',
     'api',
     'appeal',
     'area',
     'assessment',
     'ats',
     'audit',
     'auditing',
     'authorization',
     'automated',
     'bill',
     'board',
     'budget',
     'building',
     'business',
     'buyer',
     'call',
     'cam',
     'caps',
     'carrier',
     'case',
     'certification',
     'cfos',
     'charge',
     'circuit',
     'circular',
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
 3: {'179d',
     '230',
     '250k',
     '8850',
     'access',
     'agreement',
     'allocation',
     'api',
     'appeal',
     'area',
     'assessment',
     'ats',
     'audit',
     'auditing',
     'authorization',
     'automated',
     'bill',
     'board',
     'building',
     'business',
     'call',
     'cam',
     'caps',
     'carrier',
     'case',
     'cash',
     'cashflow',
     'certification',
     'cfos',
     'charge',
     'circuit',
     'circular',
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
 4: {'179d',
     '230',
     '250k',
     '8850',
     'access',
     'agreement',
     'allocation',
     'api',
     'appeal',
     'area',
     'assessment',
     'ats',
     'audit',
     'auditing',
     'authorization',
     'automated',
     'bill',
     'board',
     'budget',
     'building',
     'business',
     'call',
     'cam',
     'capital',
     'caps',
     'carrier',
     'case',
     'certification',
     'cfos',
     'charge',
     'circuit',
     'circular',
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
 5: {'179d',
     '230',
     '250k',
     '8850',
     'access',
     'agreement',
     'allocation',
     'api',
     'appeal',
     'area',
     'assessment',
     'ats',
     'audit',
     'auditing',
     'authorization',
     'automated',
     'avoid',
     'bill',
     'board',
     'building',
     'business',
     'call',
     'cam',
     'caps',
     'carrier',
     'case',
     'certification',
     'cfos',
     'charge',
     'circuit',
     'circular',
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
 6: {'179d',
     '230',
     '250k',
     '8850',
     'access',
     'agreement',
     'allocation',
     'api',
     'appeal',
     'area',
     'assessment',
     'ats',
     'audit',
     'auditing',
     'authorization',
     'automated',
     'bill',
     'board',
     'building',
     'business',
     'call',
     'cam',
     'caps',
     'carrier',
     'case',
     'certification',
     'cfos',
     'charge',
     'circuit',
     'circular',
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
 7: {'179d',
     '230',
     '250k',
     '8850',
     'access',
     'agreement',
     'allocation',
     'api',
     'appeal',
     'area',
     'assessment',
     'ats',
     'audit',
     'auditing',
     'authorization',
     'automated',
     'bill',
     'board',
     'building',
     'business',
     'call',
     'cam',
     'caps',
     'carrier',
     'case',
     'certification',
     'cfos',
     'charge',
     'checklist',
     'circuit',
     'circular',
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
 8: {'179d',
     '230',
     '250k',
     '8850',
     'access',
     'agreement',
     'allocation',
     'api',
     'appeal',
     'area',
     'assessment',
     'ats',
     'audit',
     'auditing',
     'authorization',
     'automated',
     'bill',
     'board',
     'building',
     'business',
     'call',
     'cam',
     'caps',
     'carrier',
     'case',
     'certification',
     'cfos',
     'charge',
     'circuit',
     'circular',
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
 9: {'179d',
     '230',
     '250k',
     '8850',
     'access',
     'agreement',
     'allocation',
     'api',
     'appeal',
     'area',
     'assessment',
     'ats',
     'audit',
     'auditing',
     'authorization',
     'automated',
     'bill',
     'board',
     'building',
     'business',
     'call',
     'cam',
     'caps',
     'carrier',
     'case',
     'certification',
     'cfos',
     'charge',
     'circuit',
     'circular',
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
 10: {'179d',
      '230',
      '250k',
      '8850',
      'access',
      'agent',
      'agreement',
      'ai',
      'allocation',
      'api',
      'appeal',
      'area',
      'assessment',
      'ats',
      'audit',
      'auditing',
      'authorization',
      'automate',
      'automated',
      'automation',
      'bill',
      'board',
      'building',
      'business',
      'call',
      'cam',
      'caps',
      'carrier',
      'case',
      'certification',
      'cfos',
      'charge',
      'circuit',
      'circular',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'179d',
      '230',
      '250k',
      '8850',
      'access',
      'agreement',
      'allocation',
      'api',
      'appeal',
      'area',
      'assessment',
      'ats',
      'audit',
      'auditing',
      'authorization',
      'automated',
      'bill',
      'board',
      'building',
      'business',
      'call',
      'cam',
      'caps',
      'carrier',
      'case',
      'certification',
      'cfos',
      'charge',
      'circuit',
      'circular',
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
 12: {'179d',
      '230',
      '250k',
      '8850',
      'access',
      'action',
      'agreement',
      'allocation',
      'api',
      'appeal',
      'area',
      'assessment',
      'ats',
      'audit',
      'auditing',
      'authorization',
      'automated',
      'bill',
      'board',
      'building',
      'business',
      'call',
      'cam',
      'caps',
      'carrier',
      'case',
      'certification',
      'cfos',
      'charge',
      'circuit',
      'circular',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Zog Inc',
      'channel': 'Zog Inc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:16](https://www.youtube.com/watch?v=u-o74Ze2VNs&t=916s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Where in fact, we do 98% of the work. What we do is we'll have a fact-finding "
              'call with the client. We have letters of authorization, and then we literally '
              "work off of online access. The client Once we have those, so that's 20-30 "
              "minute client's completely done.",
      'timestamp': 916,
      'timestamp_label': '[00:15:16]',
      'timestamp_seconds': 916,
      'tip': "Where in fact, we do 98% of the work. What we do is we'll have a fact-finding "
             'call with the client. We have letters of authorization, and then we literally '
             "work off of online access. The client Once we have those, so that's 20-30 minute "
             "client's completely done.",
      'title': 'Zog Partner Webinar featuring Rob Sullivan from Schooley Mitchell (Zog Inc)',
      'url': 'https://www.youtube.com/watch?v=u-o74Ze2VNs&t=916s',
      'video_id': 'u-o74Ze2VNs'},
     {'author': 'Shannon & Snyder CPAs',
      'channel': 'Shannon & Snyder CPAs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:48](https://www.youtube.com/watch?v=xZLoFvHJUec&t=228s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Actually was getting compared to the market in that area yeah he was using a '
              'rental value that was fair for the area but we.',
      'timestamp': 228,
      'timestamp_label': '[00:03:48]',
      'timestamp_seconds': 228,
      'tip': 'Actually was getting compared to the market in that area yeah he was using a '
             'rental value that was fair for the area but we.',
      'title': 'Commercial Property Tax Appeal Process in California (Shannon & Snyder CPAs)',
      'url': 'https://www.youtube.com/watch?v=xZLoFvHJUec&t=228s',
      'video_id': 'xZLoFvHJUec'},
     {'author': 'Rich Smith',
      'channel': 'Rich Smith',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:28](https://www.youtube.com/watch?v=jW2x9diynM0&t=268s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And that's where most owners miss it. They call in December with that end of "
              "the year tax panic in their voice. They've already installed the systems, no "
              'energy model, no allocation letter, no time left to run a third party analysis.',
      'timestamp': 268,
      'timestamp_label': '[00:04:28]',
      'timestamp_seconds': 268,
      'tip': "And that's where most owners miss it. They call in December with that end of the "
             "year tax panic in their voice. They've already installed the systems, no energy "
             'model, no allocation letter, no time left to run a third party analysis.',
      'title': '$500K Tax Deduction You Might Be Missing (179D Explained) (Rich Smith)',
      'url': 'https://www.youtube.com/watch?v=jW2x9diynM0&t=268s',
      'video_id': 'jW2x9diynM0'},
     {'author': 'RiverForest Connections',
      'channel': 'RiverForest Connections',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:22](https://www.youtube.com/watch?v=VvAP-sQig0I&t=82s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're not looking to switch and you also sign our service agreement which "
              'covers our business terms two we then do the analysis this is where we.',
      'timestamp': 82,
      'timestamp_label': '[00:01:22]',
      'timestamp_seconds': 82,
      'tip': "You're not looking to switch and you also sign our service agreement which "
             'covers our business terms two we then do the analysis this is where we.',
      'title': 'Schooley Mitchell Animated Video Mar 2023 Update Full (RiverForest '
               'Connections)',
      'url': 'https://www.youtube.com/watch?v=VvAP-sQig0I&t=82s',
      'video_id': 'VvAP-sQig0I'},
     {'author': 'Route Consultant',
      'channel': 'Route Consultant',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:23](https://www.youtube.com/watch?v=39UxCZgtvHU&t=743s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So maybe there's construction, uh, maybe there's something that's impacting "
              "your service area that's gonna be, you know, a while. Maybe they're building a "
              "hospital, and there's just a lot of chaos, and it's just taking a lot, but it's "
              'not gonna be forever.',
      'timestamp': 743,
      'timestamp_label': '[00:12:23]',
      'timestamp_seconds': 743,
      'tip': "So maybe there's construction, uh, maybe there's something that's impacting your "
             "service area that's gonna be, you know, a while. Maybe they're building a "
             "hospital, and there's just a lot of chaos, and it's just taking a lot, but it's "
             'not gonna be forever.',
      'title': 'FedEx P&D Contract Negotiation Tips (Route Consultant)',
      'url': 'https://www.youtube.com/watch?v=39UxCZgtvHU&t=743s',
      'video_id': '39UxCZgtvHU'},
     {'author': 'Mitchell Tax Law - Texas Tax Attorneys',
      'channel': 'Mitchell Tax Law - Texas Tax Attorneys',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=-ANQF-t6DyU&t=91s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Place the energy efficient property in service the designer does not include '
              'the allocated amount as income nor does the designer reduce future deductions '
              'by the amount of the allocation the requirements for this are set out in notice '
              '200840.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': 'Place the energy efficient property in service the designer does not include the '
             'allocated amount as income nor does the designer reduce future deductions by the '
             'amount of the allocation the requirements for this are set out in notice 200840.',
      'title': 'Understanding the 179D Deduction for Building Designers (Mitchell Tax Law - '
               'Texas Tax Attorneys)',
      'url': 'https://www.youtube.com/watch?v=-ANQF-t6DyU&t=91s',
      'video_id': '-ANQF-t6DyU'},
     {'author': 'Refund Retriever',
      'channel': 'Refund Retriever',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:37](https://www.youtube.com/watch?v=JeLyjRF9HEk&t=37s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Once we see the denial, our system populates another list and our in-house '
              'phone dispute agents call FedEx customer service to have the refunds processed. '
              'It is a time consuming process but our client are seeing more refunds each '
              'week.',
      'timestamp': 37,
      'timestamp_label': '[00:00:37]',
      'timestamp_seconds': 37,
      'tip': 'Once we see the denial, our system populates another list and our in-house phone '
             'dispute agents call FedEx customer service to have the refunds processed. It is '
             'a time consuming process but our client are seeing more refunds each week.',
      'title': 'FedEx Late Package Refund Denied? (Refund Retriever)',
      'url': 'https://www.youtube.com/watch?v=JeLyjRF9HEk&t=37s',
      'video_id': 'JeLyjRF9HEk'},
     {'author': 'Cherry Bekaert',
      'channel': 'Cherry Bekaert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:27](https://www.youtube.com/watch?v=JZ5NlVOVnnw&t=747s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Information about the building so such as the address and the place and service '
              'state of the EBP property and this section also requires potential energy.',
      'timestamp': 747,
      'timestamp_label': '[00:12:27]',
      'timestamp_seconds': 747,
      'tip': 'Information about the building so such as the address and the place and service '
             'state of the EBP property and this section also requires potential energy.',
      'title': "Form 7205: A&E Firms' Guide to Claiming Section 179D (Cherry Bekaert)",
      'url': 'https://www.youtube.com/watch?v=JZ5NlVOVnnw&t=747s',
      'video_id': 'JZ5NlVOVnnw'},
     {'author': 'Garrett Schmitt',
      'channel': 'Garrett Schmitt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:19](https://www.youtube.com/watch?v=UEDbkKJ-9Xk&t=379s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's different from fee for service. So these are outcomes that would not have "
              "happened under the traditional fee for service model. And I know we've got some "
              'great stories here today.',
      'timestamp': 379,
      'timestamp_label': '[00:06:19]',
      'timestamp_seconds': 379,
      'tip': "It's different from fee for service. So these are outcomes that would not have "
             "happened under the traditional fee for service model. And I know we've got some "
             'great stories here today.',
      'title': 'Profiling ACO Success: What Drives High Performance in the Medicare Shared '
               'Savings Program (Garrett Schmitt)',
      'url': 'https://www.youtube.com/watch?v=UEDbkKJ-9Xk&t=379s',
      'video_id': 'UEDbkKJ-9Xk'},
     {'author': 'Paramount Property Tax Appeal',
      'channel': 'Paramount Property Tax Appeal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:45](https://www.youtube.com/watch?v=fOMz56wkRgs&t=105s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Permanent financing so that's some of the stuff stayed the market uh look "
              'forward to hearing more from us but if you have any questions give us a call '
              'here at 858-225-1200 and ask for wes nichols.',
      'timestamp': 105,
      'timestamp_label': '[00:01:45]',
      'timestamp_seconds': 105,
      'tip': "Permanent financing so that's some of the stuff stayed the market uh look "
             'forward to hearing more from us but if you have any questions give us a call '
             'here at 858-225-1200 and ask for wes nichols.',
      'title': 'State of the Market: What Rising Cap Rates Mean for Property Tax Appeals '
               '(Paramount Property Tax Appeal)',
      'url': 'https://www.youtube.com/watch?v=fOMz56wkRgs&t=105s',
      'video_id': 'fOMz56wkRgs'},
     {'author': 'Hall CPA | Tax Smart Real Estate Investors',
      'channel': 'Hall CPA | Tax Smart Real Estate Investors',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=6eVkkFsis9g&t=59s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Improvements building and land that means that when we're done with a cost "
              "segregation study we're gonna have value allocated to five seven fifteen and.",
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': "Improvements building and land that means that when we're done with a cost "
             "segregation study we're gonna have value allocated to five seven fifteen and.",
      'title': 'Cost Segregation Studies Explained (Hall CPA | Tax Smart Real Estate '
               'Investors)',
      'url': 'https://www.youtube.com/watch?v=6eVkkFsis9g&t=59s',
      'video_id': '6eVkkFsis9g'},
     {'author': 'FedEx Europe',
      'channel': 'FedEx Europe',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:24](https://www.youtube.com/watch?v=yIHtr7s1k6o&t=84s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Include the country of origin - this is where the products were originally '
              'manufactured and may be different from the country the shipment is being sent '
              'from. Write down the true value of the shipment. This should be the market '
              'price of the goods, along with the currency.',
      'timestamp': 84,
      'timestamp_label': '[00:01:24]',
      'timestamp_seconds': 84,
      'tip': 'Include the country of origin - this is where the products were originally '
             'manufactured and may be different from the country the shipment is being sent '
             'from. Write down the true value of the shipment. This should be the market price '
             'of the goods, along with the currency.',
      'title': 'FedEx I How to Ship Learning Center | How to complete a commercial invoice for '
               'shipping (FedEx Europe)',
      'url': 'https://www.youtube.com/watch?v=yIHtr7s1k6o&t=84s',
      'video_id': 'yIHtr7s1k6o'},
     {'author': 'FedEx',
      'channel': 'FedEx',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:21](https://www.youtube.com/watch?v=jPerYiSDCp0&t=81s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We'll cover a hundred dollars in declared value for each shipment at no "
              'additional charge, and eligible shipments using select services are backed by '
              'the FedEx money back guarantee.',
      'timestamp': 81,
      'timestamp_label': '[00:01:21]',
      'timestamp_seconds': 81,
      'tip': "We'll cover a hundred dollars in declared value for each shipment at no "
             'additional charge, and eligible shipments using select services are backed by '
             'the FedEx money back guarantee.',
      'title': 'What is FedEx One Rate and how does flat rate shipping work? (FedEx)',
      'url': 'https://www.youtube.com/watch?v=jPerYiSDCp0&t=81s',
      'video_id': 'jPerYiSDCp0'},
     {'author': 'David Fiene',
      'channel': 'David Fiene',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:30](https://www.youtube.com/watch?v=dg087iZZfsQ&t=390s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you get some value out of this video be awesome if you hit that thumbs up '
              'okay until next time thank you for watching this video.',
      'timestamp': 390,
      'timestamp_label': '[00:06:30]',
      'timestamp_seconds': 390,
      'tip': 'If you get some value out of this video be awesome if you hit that thumbs up '
             'okay until next time thank you for watching this video.',
      'title': 'Work Opportunity Tax Credit   What You need to Know (David Fiene)',
      'url': 'https://www.youtube.com/watch?v=dg087iZZfsQ&t=390s',
      'video_id': 'dg087iZZfsQ'},
     {'author': 'Power Futures Lab',
      'channel': 'Power Futures Lab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:59](https://www.youtube.com/watch?v=EAW0K0M906s&t=119s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Africa we have a very diverse set of students in the course and interact with '
              "each other and share experiences on what works and what doesn't work "
              "effectively they're able to contribute to the proper running of the energy "
              'sector in the continent.',
      'timestamp': 119,
      'timestamp_label': '[00:01:59]',
      'timestamp_seconds': 119,
      'tip': 'Africa we have a very diverse set of students in the course and interact with '
             "each other and share experiences on what works and what doesn't work effectively "
             "they're able to contribute to the proper running of the energy sector in the "
             'continent.',
      'title': 'Financial Modelling for Utility Tariff Setting (Power Futures Lab)',
      'url': 'https://www.youtube.com/watch?v=EAW0K0M906s&t=119s',
      'video_id': 'EAW0K0M906s'}],
 2: [{'author': 'FedEx Europe',
      'channel': 'FedEx Europe',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=KB4Xoe9MLWk&t=75s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If your carrier takes care of customs clearance and the initial payment of '
              'duties and taxes, all you have to do is pay the bill when it comes. A fee for '
              'doing the work on your behalf will appear on the same invoice as the duties and '
              'taxes for your shipment.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': 'If your carrier takes care of customs clearance and the initial payment of '
             'duties and taxes, all you have to do is pay the bill when it comes. A fee for '
             'doing the work on your behalf will appear on the same invoice as the duties and '
             'taxes for your shipment.',
      'title': 'Extra shipping charges explained | Fees, duties and surcharges (FedEx Europe)',
      'url': 'https://www.youtube.com/watch?v=KB4Xoe9MLWk&t=75s',
      'video_id': 'KB4Xoe9MLWk'},
     {'author': 'Refund Retriever',
      'channel': 'Refund Retriever',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:24](https://www.youtube.com/watch?v=aXk57leOw6I&t=24s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A minimum charge is when a customer agrees to pay the greater amount of the net '
              'charge based on discounts or a set minimum price. FedEx will set the minimum '
              'charge for all services in the contract. These minimums are negotiable in your '
              'FedEx agreement.',
      'timestamp': 24,
      'timestamp_label': '[00:00:24]',
      'timestamp_seconds': 24,
      'tip': 'A minimum charge is when a customer agrees to pay the greater amount of the net '
             'charge based on discounts or a set minimum price. FedEx will set the minimum '
             'charge for all services in the contract. These minimums are negotiable in your '
             'FedEx agreement.',
      'title': 'FedEx Agreements | Part 3 - How Do Minimum Charges and Surcharges Work? '
               '(Refund Retriever)',
      'url': 'https://www.youtube.com/watch?v=aXk57leOw6I&t=24s',
      'video_id': 'aXk57leOw6I'},
     {'author': 'Share a Refund',
      'channel': 'Share a Refund',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:59](https://www.youtube.com/watch?v=PheSsrwvW9c&t=179s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You paid via credit card store with the carrier and that payment has already '
              'been transacted on the open invoice typically a sign of.',
      'timestamp': 179,
      'timestamp_label': '[00:02:59]',
      'timestamp_seconds': 179,
      'tip': 'You paid via credit card store with the carrier and that payment has already '
             'been transacted on the open invoice typically a sign of.',
      'title': 'One way to qualify a good parcel audit (Share a Refund)',
      'url': 'https://www.youtube.com/watch?v=PheSsrwvW9c&t=179s',
      'video_id': 'PheSsrwvW9c'},
     {'author': 'Cross the River, Find the Treasure',
      'channel': 'Cross the River, Find the Treasure',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:13](https://www.youtube.com/watch?v=k5BObDc9AxE&t=73s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You have the contract transmission letters that thank you for choosing your '
              'company letters uh we have filed you appeal letters invoice forms invoice '
              'letters past due notices updates for life and we also have included a '
              'persuasion tactic and a copyrighting sales ebooks.',
      'timestamp': 73,
      'timestamp_label': '[00:01:13]',
      'timestamp_seconds': 73,
      'tip': 'You have the contract transmission letters that thank you for choosing your '
             'company letters uh we have filed you appeal letters invoice forms invoice '
             'letters past due notices updates for life and we also have included a persuasion '
             'tactic and a copyrighting sales ebooks.',
      'title': 'DIY Real Estate Appraisal For Property Tax Appeals For Residential or Business '
               'Consulting (Cross the River, Find the Treasure)',
      'url': 'https://www.youtube.com/watch?v=k5BObDc9AxE&t=73s',
      'video_id': 'k5BObDc9AxE'},
     {'author': 'Vincent DiMaio',
      'channel': 'Vincent DiMaio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=E0kxjgPAax0&t=15s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'With the customer and the statute of limitations severely restricts the time to '
              "identify and declare these errors so whether you're a small business or a.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'With the customer and the statute of limitations severely restricts the time to '
             "identify and declare these errors so whether you're a small business or a.",
      'title': 'National Utilities Refund "NUR" Utility Bill Audit (Vincent DiMaio)',
      'url': 'https://www.youtube.com/watch?v=E0kxjgPAax0&t=15s',
      'video_id': 'E0kxjgPAax0'},
     {'author': 'Ryan Sumerlan',
      'channel': 'Ryan Sumerlan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:51](https://www.youtube.com/watch?v=h6W5k5owNiU&t=171s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The rates utility companies want you to pay or you can call us or go online to '
              'summerlin.com to get started paying the rates you were legally obliged to pay '
              "remember we don't get paid unless we save you money and it's a lot less than "
              'you expect.',
      'timestamp': 171,
      'timestamp_label': '[00:02:51]',
      'timestamp_seconds': 171,
      'tip': 'The rates utility companies want you to pay or you can call us or go online to '
             'summerlin.com to get started paying the rates you were legally obliged to pay '
             "remember we don't get paid unless we save you money and it's a lot less than you "
             'expect.',
      'title': 'Utility Bill Audit Secrets (Ryan Sumerlan)',
      'url': 'https://www.youtube.com/watch?v=h6W5k5owNiU&t=171s',
      'video_id': 'h6W5k5owNiU'},
     {'author': 'Save Paulding',
      'channel': 'Save Paulding',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:30](https://www.youtube.com/watch?v=oIIj8lWBYVY&t=1050s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Percent and sell them the bill and then they have to pay more when they lose or '
              'get a little bit back it kind of confuses everybody you know some of us from '
              'Alabama we like simple arithmetic all right this is a Carroll County forum '
              'here.',
      'timestamp': 1050,
      'timestamp_label': '[00:17:30]',
      'timestamp_seconds': 1050,
      'tip': 'Percent and sell them the bill and then they have to pay more when they lose or '
             'get a little bit back it kind of confuses everybody you know some of us from '
             'Alabama we like simple arithmetic all right this is a Carroll County forum here.',
      'title': 'Property Tax Appeal Class 06-19-2014 (Save Paulding)',
      'url': 'https://www.youtube.com/watch?v=oIIj8lWBYVY&t=1050s',
      'video_id': 'oIIj8lWBYVY'},
     {'author': 'Rich Smith',
      'channel': 'Rich Smith',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:09](https://www.youtube.com/watch?v=6593ENbIrIY&t=549s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You take a typical 5,000 ft commercial building like the one I've been talking "
              "about let's say the purchase price is 800,000 and uh you do a down payment of.",
      'timestamp': 549,
      'timestamp_label': '[00:09:09]',
      'timestamp_seconds': 549,
      'tip': "You take a typical 5,000 ft commercial building like the one I've been talking "
             "about let's say the purchase price is 800,000 and uh you do a down payment of.",
      'title': '179D & 45L Tax Incentives Explained: How to Save Thousands on Energy-Efficient '
               'Buildings (Rich Smith)',
      'url': 'https://www.youtube.com/watch?v=6593ENbIrIY&t=549s',
      'video_id': '6593ENbIrIY'},
     {'author': 'FedEx APAC',
      'channel': 'FedEx APAC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=wFYAxOSZzMg&t=92s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now let's talk about customs-related fees which are often undetermined during "
              'booking due to varying customs clearance processes For example a storage fee '
              'may apply when shipments remain uncleared by customs beyond the allowed time.',
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': "Now let's talk about customs-related fees which are often undetermined during "
             'booking due to varying customs clearance processes For example a storage fee may '
             'apply when shipments remain uncleared by customs beyond the allowed time.',
      'title': 'Understanding shipping surcharges (FedEx APAC)',
      'url': 'https://www.youtube.com/watch?v=wFYAxOSZzMg&t=92s',
      'video_id': 'wFYAxOSZzMg'},
     {'author': 'Toby Mathis Esq | Tax Planning & Asset Protection',
      'channel': 'Toby Mathis Esq | Tax Planning & Asset Protection',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:31](https://www.youtube.com/watch?v=3G2c1STMThk&t=151s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Have you seen those come up much Jeff? I know they're out there, I know the "
              "court case you're talking about that had the decision that you could use it in "
              'certain circumstances.',
      'timestamp': 151,
      'timestamp_label': '[00:02:31]',
      'timestamp_seconds': 151,
      'tip': "Have you seen those come up much Jeff? I know they're out there, I know the "
             "court case you're talking about that had the decision that you could use it in "
             'certain circumstances.',
      'title': 'Cost Segregation Study - Bonus Accelerated Depreciation (BIG Tax Cuts Job Act '
               'CHANGES) (Toby Mathis Esq | Tax Planning & Asset Protection)',
      'url': 'https://www.youtube.com/watch?v=3G2c1STMThk&t=151s',
      'video_id': '3G2c1STMThk'},
     {'author': 'Route Consultant',
      'channel': 'Route Consultant',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=-AnzYDP3LQw&t=126s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Options that you'll get for the contract so miso one has a higher percentage of "
              'your compensation tied to fixed charges which are things like the service '
              'charge.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': "Options that you'll get for the contract so miso one has a higher percentage of "
             'your compensation tied to fixed charges which are things like the service '
             'charge.',
      'title': 'Negotiation + Renegotiation Scenarios + Timeframes (Route Consultant)',
      'url': 'https://www.youtube.com/watch?v=-AnzYDP3LQw&t=126s',
      'video_id': '-AnzYDP3LQw'},
     {'author': 'Refund Retriever',
      'channel': 'Refund Retriever',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:41](https://www.youtube.com/watch?v=iizNycveRfc&t=161s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Most companies have no idea how much you're actually paying. Refund Retriever, "
              'we can help you identify every oversize charge on your invoice, quantify the '
              'real cost your business, and help negotiate better terms with FedEx.',
      'timestamp': 161,
      'timestamp_label': '[00:02:41]',
      'timestamp_seconds': 161,
      'tip': "Most companies have no idea how much you're actually paying. Refund Retriever, "
             'we can help you identify every oversize charge on your invoice, quantify the '
             'real cost your business, and help negotiate better terms with FedEx.',
      'title': 'FedEx Oversize Accessorial Fees 2026 (Refund Retriever)',
      'url': 'https://www.youtube.com/watch?v=iizNycveRfc&t=161s',
      'video_id': 'iizNycveRfc'},
     {'author': 'eTruckBiz',
      'channel': 'eTruckBiz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:40:37](https://www.youtube.com/watch?v=wO3DQr14wiU&t=2437s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s behaviors you've had people preach to you that pay per day and if they get "
              "done at 2 o'clock and and everything things great they go home it won't work in "
              'network 2.',
      'timestamp': 2437,
      'timestamp_label': '[00:40:37]',
      'timestamp_seconds': 2437,
      'tip': "'s behaviors you've had people preach to you that pay per day and if they get "
             "done at 2 o'clock and and everything things great they go home it won't work in "
             'network 2.',
      'title': 'CSA Negotiation Insights for FedEx Network 2.0: New Contract Charges CSPs '
               'Should Know About (eTruckBiz)',
      'url': 'https://www.youtube.com/watch?v=wO3DQr14wiU&t=2437s',
      'video_id': 'wO3DQr14wiU'},
     {'author': 'Refund Retriever',
      'channel': 'Refund Retriever',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:22](https://www.youtube.com/watch?v=TzPaNZCC4js&t=202s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Contact the experts at refund retriever to analyze your current excess oriole '
              'fee spend we can help lower your future shipping costs with a full contract '
              'analysis give us a call at 844 one eight zero eight five or check out our '
              'website refund retriever com thanks a lot.',
      'timestamp': 202,
      'timestamp_label': '[00:03:22]',
      'timestamp_seconds': 202,
      'tip': 'Contact the experts at refund retriever to analyze your current excess oriole '
             'fee spend we can help lower your future shipping costs with a full contract '
             'analysis give us a call at 844 one eight zero eight five or check out our '
             'website refund retriever com thanks a lot.',
      'title': 'FedEx Additional Handling Surcharge: What to know (Refund Retriever)',
      'url': 'https://www.youtube.com/watch?v=TzPaNZCC4js&t=202s',
      'video_id': 'TzPaNZCC4js'},
     {'author': 'SC DEW',
      'channel': 'SC DEW',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:44](https://www.youtube.com/watch?v=ujWX1IZPyFc&t=464s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Calculated tax credit to their cpa or licensed tax preparer for more '
              'information pertaining to the work opportunity tax credit contact the south '
              'carolina department of employment and workforce work opportunity tax credit '
              'staff at wotc at dew.sc.gov.',
      'timestamp': 464,
      'timestamp_label': '[00:07:44]',
      'timestamp_seconds': 464,
      'tip': 'Calculated tax credit to their cpa or licensed tax preparer for more information '
             'pertaining to the work opportunity tax credit contact the south carolina '
             'department of employment and workforce work opportunity tax credit staff at wotc '
             'at dew.sc.gov.',
      'title': 'Work Opportunity Tax Credit (WOTC) (SC DEW)',
      'url': 'https://www.youtube.com/watch?v=ujWX1IZPyFc&t=464s',
      'video_id': 'ujWX1IZPyFc'}],
 3: [{'author': 'LateShipment',
      'channel': 'LateShipment',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=WvGPHvucRD0&t=35s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Leading the list is late shipment. Top rated parcel audit software auditing 50 '
              'plus carrier billing error types across,200 plus carriers in 40 plus countries, '
              'reducing shipping costs by up to 20% with claims backtracked up to 45 days and '
              'no monthly fee.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'Leading the list is late shipment. Top rated parcel audit software auditing 50 '
             'plus carrier billing error types across,200 plus carriers in 40 plus countries, '
             'reducing shipping costs by up to 20% with claims backtracked up to 45 days and '
             'no monthly fee.',
      'title': 'Top 10 Parcel Audit Software Solutions for E-Commerce (LateShipment)',
      'url': 'https://www.youtube.com/watch?v=WvGPHvucRD0&t=35s',
      'video_id': 'WvGPHvucRD0'},
     {'author': 'I Love Winnipeg Real Estate',
      'channel': 'I Love Winnipeg Real Estate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=hvDoePHFWi4&t=88s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'To cam costs the idea behind common area maintenance charges is that tenants '
              'contribute to the cost.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'To cam costs the idea behind common area maintenance charges is that tenants '
             'contribute to the cost.',
      'title': 'Handling Annual CAM Reconciliation at a Commercial Property (I Love Winnipeg '
               'Real Estate)',
      'url': 'https://www.youtube.com/watch?v=hvDoePHFWi4&t=88s',
      'video_id': 'hvDoePHFWi4'},
     {'author': 'Cerasis , now part of GlobalTranz',
      'channel': 'Cerasis , now part of GlobalTranz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:19](https://www.youtube.com/watch?v=GnXmnbxCZ-A&t=199s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Of the person auditing the invoices multiplied by the number of hours spent '
              'auditing it would cost more to audit than leaving invoices alone this is part.',
      'timestamp': 199,
      'timestamp_label': '[00:03:19]',
      'timestamp_seconds': 199,
      'tip': 'Of the person auditing the invoices multiplied by the number of hours spent '
             'auditing it would cost more to audit than leaving invoices alone this is part.',
      'title': 'Reducing Parcel Shipping Costs with Parcel Audits (Cerasis , now part of '
               'GlobalTranz)',
      'url': 'https://www.youtube.com/watch?v=GnXmnbxCZ-A&t=199s',
      'video_id': 'GnXmnbxCZ-A'},
     {'author': 'Commercial Property Advisors',
      'channel': 'Commercial Property Advisors',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=lJFBf789ODI&t=15s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Question to you is it possible to to have a 10 unit apartment building that '
              'maybe you purchased for a million dollars in your cash flows a couple of.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Question to you is it possible to to have a 10 unit apartment building that '
             'maybe you purchased for a million dollars in your cash flows a couple of.',
      'title': 'Cost Segregation Made Simple (Commercial Property Advisors)',
      'url': 'https://www.youtube.com/watch?v=lJFBf789ODI&t=15s',
      'video_id': 'lJFBf789ODI'},
     {'author': 'Mark Perlberg, CPA',
      'channel': 'Mark Perlberg, CPA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:24](https://www.youtube.com/watch?v=3bjz5YCldWA&t=984s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, you rent out your office building to your company. We do a cost segregation '
              'study. We create massive losses and that offsets the profits from your business '
              'and drives down your taxes. Let me give you an example here. We actually had a '
              'dentist that did this recently.',
      'timestamp': 984,
      'timestamp_label': '[00:16:24]',
      'timestamp_seconds': 984,
      'tip': 'So, you rent out your office building to your company. We do a cost segregation '
             'study. We create massive losses and that offsets the profits from your business '
             'and drives down your taxes. Let me give you an example here. We actually had a '
             'dentist that did this recently.',
      'title': 'What is Cost Segregation, and When do I do a Cost Segregation Study? (Mark '
               'Perlberg, CPA)',
      'url': 'https://www.youtube.com/watch?v=3bjz5YCldWA&t=984s',
      'video_id': '3bjz5YCldWA'},
     {'author': 'BizCpas Accountants & Advisors',
      'channel': 'BizCpas Accountants & Advisors',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:52](https://www.youtube.com/watch?v=mKOnV6RitlA&t=172s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And fourth is to make sure you accelerate the depreciation and realize the '
              "benefits and the tax benefits which is cash flow. So in this case study, we're "
              'going to take a 700,000 luxury home with the total cost base of 700K.',
      'timestamp': 172,
      'timestamp_label': '[00:02:52]',
      'timestamp_seconds': 172,
      'tip': 'And fourth is to make sure you accelerate the depreciation and realize the '
             "benefits and the tax benefits which is cash flow. So in this case study, we're "
             'going to take a 700,000 luxury home with the total cost base of 700K.',
      'title': 'Cost Segregation Analysis Explained: How Real Estate Investors Save $45,000+ '
               'in Taxes Legally (BizCpas Accountants & Advisors)',
      'url': 'https://www.youtube.com/watch?v=mKOnV6RitlA&t=172s',
      'video_id': 'mKOnV6RitlA'},
     {'author': 'Engineered Tax Services',
      'channel': 'Engineered Tax Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:47](https://www.youtube.com/watch?v=XTuAPOFbamo&t=107s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'While this can reduce the time and cost, it may introduce some margin of error, '
              'it does require proper sampling techniques to remain credible. Number four is a '
              'square foot or rule of thumb allocation.',
      'timestamp': 107,
      'timestamp_label': '[00:01:47]',
      'timestamp_seconds': 107,
      'tip': 'While this can reduce the time and cost, it may introduce some margin of error, '
             'it does require proper sampling techniques to remain credible. Number four is a '
             'square foot or rule of thumb allocation.',
      'title': 'Are There Different Types of Cost Segregation Studies? (Engineered Tax '
               'Services)',
      'url': 'https://www.youtube.com/watch?v=XTuAPOFbamo&t=107s',
      'video_id': 'XTuAPOFbamo'},
     {'author': 'Tax Modern',
      'channel': 'Tax Modern',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:52](https://www.youtube.com/watch?v=hjpQzDqWetI&t=1012s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Pretty much everyone is going to be cash, not acural for rental properties. '
              'Then what we have here are just other answers, other statements for some of the '
              'other questions. The description of the trader business is just rental real '
              'estate.',
      'timestamp': 1012,
      'timestamp_label': '[00:16:52]',
      'timestamp_seconds': 1012,
      'tip': 'Pretty much everyone is going to be cash, not acural for rental properties. Then '
             'what we have here are just other answers, other statements for some of the other '
             'questions. The description of the trader business is just rental real estate.',
      'title': 'How to use Form 3115 for a Cost Segregation Study - Complete Tutorial (Tax '
               'Modern)',
      'url': 'https://www.youtube.com/watch?v=hjpQzDqWetI&t=1012s',
      'video_id': 'hjpQzDqWetI'},
     {'author': 'Asset Wise Institute',
      'channel': 'Asset Wise Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=e9edFqL1urU&t=85s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Only the building and some property components are depreciated. So, even in a '
              'normal purchase, you do not simply depreciate the full purchase price. You have '
              'to separate land from building. After a 1031 exchange, here is another layer.',
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': 'Only the building and some property components are depreciated. So, even in a '
             'normal purchase, you do not simply depreciate the full purchase price. You have '
             'to separate land from building. After a 1031 exchange, here is another layer.',
      'title': 'Cost Segregation After a 1031 Exchange: Depreciation & Timing Rules — I1031 M6 '
               'V2 (Asset Wise Institute)',
      'url': 'https://www.youtube.com/watch?v=e9edFqL1urU&t=85s',
      'video_id': 'e9edFqL1urU'},
     {'author': 'URDesigns Inc.',
      'channel': 'URDesigns Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=B_c8H2j_zZA&t=78s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Understanding of because it's not part of their core business that's where we "
              "come in we're independent consultants and we analyze these cost areas for the.",
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': "Understanding of because it's not part of their core business that's where we "
             "come in we're independent consultants and we analyze these cost areas for the.",
      'title': 'Schooley Mitchell: INTRODUCTION (URDesigns Inc.)',
      'url': 'https://www.youtube.com/watch?v=B_c8H2j_zZA&t=78s',
      'video_id': 'B_c8H2j_zZA'},
     {'author': 'LYFE Accounting',
      'channel': 'LYFE Accounting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=w16nUKkydYc&t=62s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'More depreciation means less income reported on your tax return, and less '
              'income on your tax return means lower taxes. Now, remember, depreciation is a '
              'non-cash expense that you can take that does not cost you any money out of your '
              'pocket.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': 'More depreciation means less income reported on your tax return, and less income '
             'on your tax return means lower taxes. Now, remember, depreciation is a non-cash '
             'expense that you can take that does not cost you any money out of your pocket.',
      'title': 'CPA Explains The #1 Real Estate Tax Deduction: Cost Segregation Explained '
               '(LYFE Accounting)',
      'url': 'https://www.youtube.com/watch?v=w16nUKkydYc&t=62s',
      'video_id': 'w16nUKkydYc'},
     {'author': 'PorterKinney',
      'channel': 'PorterKinney',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=G6l9WU9XBgI&t=31s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s what a cost segregation does. A cost segregation breaks out the different "
              'assets of a property into shorter lifespan than just 39-year property. So, by '
              'default, the IRS just says, "All right, you bought this building. We\'re going '
              'to make you depreciate it over 39 years.',
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': "'s what a cost segregation does. A cost segregation breaks out the different "
             'assets of a property into shorter lifespan than just 39-year property. So, by '
             'default, the IRS just says, "All right, you bought this building. We\'re going '
             'to make you depreciate it over 39 years.',
      'title': 'It’s Not Too Late to Do a Cost Segregation Study (PorterKinney)',
      'url': 'https://www.youtube.com/watch?v=G6l9WU9XBgI&t=31s',
      'video_id': 'G6l9WU9XBgI'},
     {'author': 'Cherry Bekaert',
      'channel': 'Cherry Bekaert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:48](https://www.youtube.com/watch?v=IYUnmXCy8I0&t=1068s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Are you an eligible small business looking to retroactively deduct your '
              "previously capitalized 174 costs? Yes, no, or I'm not sure if I'm an eligible "
              'small business.',
      'timestamp': 1068,
      'timestamp_label': '[00:17:48]',
      'timestamp_seconds': 1068,
      'tip': 'Are you an eligible small business looking to retroactively deduct your '
             "previously capitalized 174 costs? Yes, no, or I'm not sure if I'm an eligible "
             'small business.',
      'title': 'R&D Tax Credit Landscape: Q1 2026 Updates & Key Considerations (Cherry '
               'Bekaert)',
      'url': 'https://www.youtube.com/watch?v=IYUnmXCy8I0&t=1068s',
      'video_id': 'IYUnmXCy8I0'},
     {'author': 'WPPIEnergy',
      'channel': 'WPPIEnergy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:20](https://www.youtube.com/watch?v=BVDlaBB19aQ&t=200s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're saving money I mean the savings down the road is just unbelievable your "
              "replacement costs are less your expenses are down and you're doing something "
              'for the environment thank you very much gentlemen have a great.',
      'timestamp': 200,
      'timestamp_label': '[00:03:20]',
      'timestamp_seconds': 200,
      'tip': "You're saving money I mean the savings down the road is just unbelievable your "
             "replacement costs are less your expenses are down and you're doing something for "
             'the environment thank you very much gentlemen have a great.',
      'title': 'Shared Savings Program (WPPIEnergy)',
      'url': 'https://www.youtube.com/watch?v=BVDlaBB19aQ&t=200s',
      'video_id': 'BVDlaBB19aQ'},
     {'author': 'CostSegRx',
      'channel': 'CostSegRx',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:56](https://www.youtube.com/watch?v=IFbN2m1Gw3Y&t=116s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And you can see that there's plenty of depreciation moving forward. You have "
              '$14,711 in trailing depreciation with cost segregation versus without cost '
              'segregation of $17,307. Contact us today at costsegRX.',
      'timestamp': 116,
      'timestamp_label': '[00:01:56]',
      'timestamp_seconds': 116,
      'tip': "And you can see that there's plenty of depreciation moving forward. You have "
             '$14,711 in trailing depreciation with cost segregation versus without cost '
             'segregation of $17,307. Contact us today at costsegRX.',
      'title': 'Cost Segregation Example: $750K Commercial Property Tax Savings (2026) '
               '(CostSegRx)',
      'url': 'https://www.youtube.com/watch?v=IFbN2m1Gw3Y&t=116s',
      'video_id': 'IFbN2m1Gw3Y'}],
 4: [{'author': 'USA Senior Laws Guide',
      'channel': 'USA Senior Laws Guide',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:23](https://www.youtube.com/watch?v=LopTSxbolHY&t=563s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Look for words like notice of valuation, appeal process, or board of '
              "equalization. If you cannot find it online, call the county assessor's office "
              'directly and ask. Step two is to gather your evidence.',
      'timestamp': 563,
      'timestamp_label': '[00:09:23]',
      'timestamp_seconds': 563,
      'tip': 'Look for words like notice of valuation, appeal process, or board of '
             "equalization. If you cannot find it online, call the county assessor's office "
             'directly and ask. Step two is to gather your evidence.',
      'title': 'How to Appeal Your 2026 Property Tax Assessment — The Step by Step Process '
               'Most Seniors Never Use (USA Senior Laws Guide)',
      'url': 'https://www.youtube.com/watch?v=LopTSxbolHY&t=563s',
      'video_id': 'LopTSxbolHY'},
     {'author': 'George Ghazarian, CPA',
      'channel': 'George Ghazarian, CPA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:29](https://www.youtube.com/watch?v=Exr84oxoKzc&t=149s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The building needs to show a measurable energy savings over a baseline '
              'standard. This is basically uh determined by a third party engineer using IRS '
              'approved software to determine this. Step two, you need an allocation letter.',
      'timestamp': 149,
      'timestamp_label': '[00:02:29]',
      'timestamp_seconds': 149,
      'tip': 'The building needs to show a measurable energy savings over a baseline standard. '
             'This is basically uh determined by a third party engineer using IRS approved '
             'software to determine this. Step two, you need an allocation letter.',
      'title': 'The Energy Deduction Commercial Contractors Keep Missing (George Ghazarian, '
               'CPA)',
      'url': 'https://www.youtube.com/watch?v=Exr84oxoKzc&t=149s',
      'video_id': 'Exr84oxoKzc'},
     {'author': 'Cross the River, Find the Treasure',
      'channel': 'Cross the River, Find the Treasure',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:21](https://www.youtube.com/watch?v=nA_VWYA00vA&t=201s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Hence the income method is used when a business gets hit by a lack of earnings '
              "they get a reduction in property taxes and if they don't appeal the previous "
              "year's assessment is going to take hold and nothing changes if they don't "
              'appeal.',
      'timestamp': 201,
      'timestamp_label': '[00:03:21]',
      'timestamp_seconds': 201,
      'tip': 'Hence the income method is used when a business gets hit by a lack of earnings '
             "they get a reduction in property taxes and if they don't appeal the previous "
             "year's assessment is going to take hold and nothing changes if they don't "
             'appeal.',
      'title': 'Property Tax Appeal: Give Accurate Do-It-Yourself Real Estate Appraisal for '
               'Residential & Businesses (Cross the River, Find the Treasure)',
      'url': 'https://www.youtube.com/watch?v=nA_VWYA00vA&t=201s',
      'video_id': 'nA_VWYA00vA'},
     {'author': 'MTC Recovery Consultants',
      'channel': 'MTC Recovery Consultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=bNqu0vah45U&t=72s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Automatically receive thousands or even hundreds of thousands of dollars in '
              'credits from your carrier all you have to do is call one eight seven seven six.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': 'Automatically receive thousands or even hundreds of thousands of dollars in '
             'credits from your carrier all you have to do is call one eight seven seven six.',
      'title': 'Parcel Auditing to Lower FedEx, UPS, DHL, and Purolator Bills (MTC Recovery '
               'Consultants)',
      'url': 'https://www.youtube.com/watch?v=bNqu0vah45U&t=72s',
      'video_id': 'bNqu0vah45U'},
     {'author': 'Cherry Bekaert',
      'channel': 'Cherry Bekaert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:46](https://www.youtube.com/watch?v=zU4xMPqHWY0&t=346s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Case um because of the way that the tax code requires us to to perform this '
              'energy analysis we take a look at the building as it stands today or the.',
      'timestamp': 346,
      'timestamp_label': '[00:05:46]',
      'timestamp_seconds': 346,
      'tip': 'Case um because of the way that the tax code requires us to to perform this '
             'energy analysis we take a look at the building as it stands today or the.',
      'title': '179D Energy-Efficient Commercial Buildings Deduction for Not-for-Profits '
               '(Cherry Bekaert)',
      'url': 'https://www.youtube.com/watch?v=zU4xMPqHWY0&t=346s',
      'video_id': 'zU4xMPqHWY0'},
     {'author': 'Coastline Equity',
      'channel': 'Coastline Equity',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=u1Y-WxOKXpc&t=78s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Triple nets differs from cams and that the charges often in the lease include '
              "things like taxes and insurance which aren't part of the common area "
              'maintenance.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'Triple nets differs from cams and that the charges often in the lease include '
             "things like taxes and insurance which aren't part of the common area "
             'maintenance.',
      'title': 'CAM Reconciliations | The Real Estate Advisors - Episode 2 (Coastline Equity)',
      'url': 'https://www.youtube.com/watch?v=u1Y-WxOKXpc&t=78s',
      'video_id': 'u1Y-WxOKXpc'},
     {'author': 'Advisory Board',
      'channel': 'Advisory Board',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:47](https://www.youtube.com/watch?v=hGtjN7H07Bo&t=167s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But as you might expect, the devil’s in the details. And the Medicare Shared '
              'Savings Program is complex. Advisory Board’s collection of best practices, '
              'research, tools, and expert insight.',
      'timestamp': 167,
      'timestamp_label': '[00:02:47]',
      'timestamp_seconds': 167,
      'tip': 'But as you might expect, the devil’s in the details. And the Medicare Shared '
             'Savings Program is complex. Advisory Board’s collection of best practices, '
             'research, tools, and expert insight.',
      'title': 'What is the Medicare Shared Savings Program? (Advisory Board)',
      'url': 'https://www.youtube.com/watch?v=hGtjN7H07Bo&t=167s',
      'video_id': 'hGtjN7H07Bo'},
     {'author': 'Toby Mathis Esq | Tax Planning & Asset Protection',
      'channel': 'Toby Mathis Esq | Tax Planning & Asset Protection',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:59](https://www.youtube.com/watch?v=beMOZDrXOJ8&t=359s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, if the business owner has a different entity and has the real estate, then '
              'maybe. But yes, you need to own the real estate to be able to take the '
              'deduction.',
      'timestamp': 359,
      'timestamp_label': '[00:05:59]',
      'timestamp_seconds': 359,
      'tip': 'Now, if the business owner has a different entity and has the real estate, then '
             'maybe. But yes, you need to own the real estate to be able to take the '
             'deduction.',
      'title': 'How To Do A Cost Segregation Study: When It Saves You Money And When It '
               'Doesn’t (Toby Mathis Esq | Tax Planning & Asset Protection)',
      'url': 'https://www.youtube.com/watch?v=beMOZDrXOJ8&t=359s',
      'video_id': 'beMOZDrXOJ8'},
     {'author': 'Clint Coons Esq. | Real Estate Asset Protection',
      'channel': 'Clint Coons Esq. | Real Estate Asset Protection',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:44](https://www.youtube.com/watch?v=fV7tusLGp3E&t=44s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Okay, so quick level setup here. What do we make sure we're talking about the "
              'same thing. You see cost segregation or cost seg is a study usually done by '
              'engineers or a tax preparer that breaks down your building into pieces.',
      'timestamp': 44,
      'timestamp_label': '[00:00:44]',
      'timestamp_seconds': 44,
      'tip': "Okay, so quick level setup here. What do we make sure we're talking about the "
             'same thing. You see cost segregation or cost seg is a study usually done by '
             'engineers or a tax preparer that breaks down your building into pieces.',
      'title': 'Why Cost Segregation Can Be A BAD Idea (Clint Coons Esq. | Real Estate Asset '
               'Protection)',
      'url': 'https://www.youtube.com/watch?v=fV7tusLGp3E&t=44s',
      'video_id': 'fV7tusLGp3E'},
     {'author': 'Mock Theta Studies',
      'channel': 'Mock Theta Studies',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:33](https://www.youtube.com/watch?v=Kf0-irBt3DU&t=573s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Capacity charge is derived on the basis of AFC and that constitutes of return '
              'on equity, interest on loan capital, depreciation, interest on working capital '
              'and O and M expenses.',
      'timestamp': 573,
      'timestamp_label': '[00:09:33]',
      'timestamp_seconds': 573,
      'tip': 'Capacity charge is derived on the basis of AFC and that constitutes of return on '
             'equity, interest on loan capital, depreciation, interest on working capital and '
             'O and M expenses.',
      'title': 'Tariff Calculation for Power/Energy/Electricity (Mock Theta Studies)',
      'url': 'https://www.youtube.com/watch?v=Kf0-irBt3DU&t=573s',
      'video_id': 'Kf0-irBt3DU'},
     {'author': 'RE BackOffice',
      'channel': 'RE BackOffice',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:14](https://www.youtube.com/watch?v=5wJlP07wwrM&t=554s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Overwhelming it's essential for maintaining a fair balance between landlords "
              'and tenants the right tools and processes can make it easier and more efficient '
              'for everyone involved.',
      'timestamp': 554,
      'timestamp_label': '[00:09:14]',
      'timestamp_seconds': 554,
      'tip': "Overwhelming it's essential for maintaining a fair balance between landlords and "
             'tenants the right tools and processes can make it easier and more efficient for '
             'everyone involved.',
      'title': 'CAM Reconciliation: A Comprehensive Overview (RE BackOffice)',
      'url': 'https://www.youtube.com/watch?v=5wJlP07wwrM&t=554s',
      'video_id': '5wJlP07wwrM'},
     {'author': 'simpleQuE - ISO Certification Consulting',
      'channel': 'simpleQuE - ISO Certification Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:59](https://www.youtube.com/watch?v=Sf10tIpwF74&t=179s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Conducted so what I've seen as a certification body auditor for contingency "
              'planning from a good bad and ugly standpoint from.',
      'timestamp': 179,
      'timestamp_label': '[00:02:59]',
      'timestamp_seconds': 179,
      'tip': "Conducted so what I've seen as a certification body auditor for contingency "
             'planning from a good bad and ugly standpoint from.',
      'title': 'IATF 16949 Audits - The Good, Bad & Ugly: 6.1.2.3 Contingency Planning '
               '(simpleQuE - ISO Certification Consulting)',
      'url': 'https://www.youtube.com/watch?v=Sf10tIpwF74&t=179s',
      'video_id': 'Sf10tIpwF74'},
     {'author': 'Paramount Property Tax Appeal',
      'channel': 'Paramount Property Tax Appeal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:12](https://www.youtube.com/watch?v=lvlw6rQ6uBQ&t=132s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You know office and retail have been fluctuating however when uh retail and '
              'office buildings rents and will typically soften because a business.',
      'timestamp': 132,
      'timestamp_label': '[00:02:12]',
      'timestamp_seconds': 132,
      'tip': 'You know office and retail have been fluctuating however when uh retail and '
             'office buildings rents and will typically soften because a business.',
      'title': 'Inflation, Cap Rates, and Your Property Taxes: What You Need to Know '
               '(Paramount Property Tax Appeal)',
      'url': 'https://www.youtube.com/watch?v=lvlw6rQ6uBQ&t=132s',
      'video_id': 'lvlw6rQ6uBQ'},
     {'author': 'Refund Retriever',
      'channel': 'Refund Retriever',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:33](https://www.youtube.com/watch?v=VpvZiUp02QU&t=213s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Negotiating the best UPS and FedEx contracts contact refund retriever our '
              'proprietary software will reveal the shipping intelligence you need with '
              'Logistics experts in your company give us a call 800-441-8085 or check out our '
              'website refund retriever.com thanks a lot.',
      'timestamp': 213,
      'timestamp_label': '[00:03:33]',
      'timestamp_seconds': 213,
      'tip': 'Negotiating the best UPS and FedEx contracts contact refund retriever our '
             'proprietary software will reveal the shipping intelligence you need with '
             'Logistics experts in your company give us a call 800-441-8085 or check out our '
             'website refund retriever.com thanks a lot.',
      'title': 'UPS & FedEx Contracts Negotiation Tips (Refund Retriever)',
      'url': 'https://www.youtube.com/watch?v=VpvZiUp02QU&t=213s',
      'video_id': 'VpvZiUp02QU'},
     {'author': 'Buffalo Tax Strategies',
      'channel': 'Buffalo Tax Strategies',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:37](https://www.youtube.com/watch?v=AUiM2KAknsw&t=277s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Take advantage of again if one of your employees falls into one of these '
              "targeted groups so I hope that's how that helps thank you so much for joining "
              'us talk to you soon.',
      'timestamp': 277,
      'timestamp_label': '[00:04:37]',
      'timestamp_seconds': 277,
      'tip': 'Take advantage of again if one of your employees falls into one of these '
             "targeted groups so I hope that's how that helps thank you so much for joining us "
             'talk to you soon.',
      'title': 'TAX TIP For Employers - The Work Opportunity Tax Credit (WOTC) (Buffalo Tax '
               'Strategies)',
      'url': 'https://www.youtube.com/watch?v=AUiM2KAknsw&t=277s',
      'video_id': 'AUiM2KAknsw'}],
 5: [{'author': 'Experidium',
      'channel': 'Experidium',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=8-Sguow2LDM&t=163s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'At the end, you get a findings report. 38% of audited spend identified and '
              'evidenced. Every invoice audited, every overcharge evidenced. One approval '
              "before a dispute goes out. If you'd like to see it on your own carrier "
              'invoices, book a 20inut call.',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': 'At the end, you get a findings report. 38% of audited spend identified and '
             'evidenced. Every invoice audited, every overcharge evidenced. One approval '
             "before a dispute goes out. If you'd like to see it on your own carrier invoices, "
             'book a 20inut call.',
      'title': 'Freight Audit & Recovery Agent: Claude Checks Every Carrier Invoice '
               '(Experidium)',
      'url': 'https://www.youtube.com/watch?v=8-Sguow2LDM&t=163s',
      'video_id': '8-Sguow2LDM'},
     {'author': 'Pacific Regional Environment Programme (SPREP)',
      'channel': 'Pacific Regional Environment Programme (SPREP)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:16](https://www.youtube.com/watch?v=jUiK_mA7U40&t=136s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Outline the audit's goals, the types of materials to be assessed, the timeline, "
              'and the specific data to collect. Ensure that health, safety, and risk '
              'management protocols are in place, including assessing risks and implementing '
              'mitigation measures.',
      'timestamp': 136,
      'timestamp_label': '[00:02:16]',
      'timestamp_seconds': 136,
      'tip': "Outline the audit's goals, the types of materials to be assessed, the timeline, "
             'and the specific data to collect. Ensure that health, safety, and risk '
             'management protocols are in place, including assessing risks and implementing '
             'mitigation measures.',
      'title': 'The Waste Audit Process: step by step guide (Pacific Regional Environment '
               'Programme (SPREP))',
      'url': 'https://www.youtube.com/watch?v=jUiK_mA7U40&t=136s',
      'video_id': 'jUiK_mA7U40'},
     {'author': 'Waste Consultants',
      'channel': 'Waste Consultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:20](https://www.youtube.com/watch?v=zV8cq0gJWOA&t=260s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Thorough utility audit but you can absolutely reap the benefits with one '
              'utility audits can massively benefit your bottom line and can ease any residual '
              'fears you may have about building mistakes and price spikes.',
      'timestamp': 260,
      'timestamp_label': '[00:04:20]',
      'timestamp_seconds': 260,
      'tip': 'Thorough utility audit but you can absolutely reap the benefits with one utility '
             'audits can massively benefit your bottom line and can ease any residual fears '
             'you may have about building mistakes and price spikes.',
      'title': 'What is a Utility Audit? (Waste Consultants)',
      'url': 'https://www.youtube.com/watch?v=zV8cq0gJWOA&t=260s',
      'video_id': 'zV8cq0gJWOA'},
     {'author': 'Greg Walker',
      'channel': 'Greg Walker',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=sM254iPKhSo&t=20s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Consulting Group's risk-free workers compensation audit service. Because our "
              'goal is to save you money, not to charge you upfront. That means we provide the '
              'service on a contingency basis. We only get paid if we save you money.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Consulting Group's risk-free workers compensation audit service. Because our "
             'goal is to save you money, not to charge you upfront. That means we provide the '
             'service on a contingency basis. We only get paid if we save you money.',
      'title': 'Workers Compensation Audit Explained (Greg Walker)',
      'url': 'https://www.youtube.com/watch?v=sM254iPKhSo&t=20s',
      'video_id': 'sM254iPKhSo'},
     {'author': 'Good Citizens Society',
      'channel': 'Good Citizens Society',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:27](https://www.youtube.com/watch?v=72KTU2Th6eY&t=387s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Won't charge you a fee you don't want to take any chance of anybody making "
              'mistakes and submitting the wrong dimensions on a package we submit with.',
      'timestamp': 387,
      'timestamp_label': '[00:06:27]',
      'timestamp_seconds': 387,
      'tip': "Won't charge you a fee you don't want to take any chance of anybody making "
             'mistakes and submitting the wrong dimensions on a package we submit with.',
      'title': 'Negotiating a UPS or Fedex Contract - Small Business Shipping University - '
               'Episode 2 (Good Citizens Society)',
      'url': 'https://www.youtube.com/watch?v=72KTU2Th6eY&t=387s',
      'video_id': '72KTU2Th6eY'},
     {'author': 'Jason D. Knott',
      'channel': 'Jason D. Knott',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:44](https://www.youtube.com/watch?v=RmnPUe0eO7s&t=344s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "9062 is that conditional uh that conditional certification that you've already "
              "been pre-approved but in this case we're going to assume he.",
      'timestamp': 344,
      'timestamp_label': '[00:05:44]',
      'timestamp_seconds': 344,
      'tip': "9062 is that conditional uh that conditional certification that you've already "
             "been pre-approved but in this case we're going to assume he.",
      'title': 'Work Opportunity Tax Credits - IRS Form 8850 & DOL Form 9061 (Jason D. Knott)',
      'url': 'https://www.youtube.com/watch?v=RmnPUe0eO7s&t=344s',
      'video_id': 'RmnPUe0eO7s'},
     {'author': 'Waster - Waster Pty Ltd - Recycling Facts & Info',
      'channel': 'Waster - Waster Pty Ltd - Recycling Facts & Info',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=pJwMVLhMfWI&t=35s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We will look a bit more at the dirty work how do we know how much recyclable '
              'material is actually in your bin and if your business is making real progress '
              "in recycling more and sending less material to landfill let's talk about a "
              'waste audit.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'We will look a bit more at the dirty work how do we know how much recyclable '
             'material is actually in your bin and if your business is making real progress in '
             "recycling more and sending less material to landfill let's talk about a waste "
             'audit.',
      'title': 'What Is A Waste Audit ⚖️And How Can It Boost Recycling? (Waster - Waster Pty '
               'Ltd - Recycling Facts & Info)',
      'url': 'https://www.youtube.com/watch?v=pJwMVLhMfWI&t=35s',
      'video_id': 'pJwMVLhMfWI'},
     {'author': 'Flexport',
      'channel': 'Flexport',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:05](https://www.youtube.com/watch?v=xtorVFI9g4c&t=1205s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll look at your entries, they'll look at your products to see if there there "
              'is risk that warrants further review such as an audit. CVP form 29, if they '
              "know there is an issue or customs doesn't agree with you, they may issue a "
              'notice of action and assess additional duties.',
      'timestamp': 1205,
      'timestamp_label': '[00:20:05]',
      'timestamp_seconds': 1205,
      'tip': "'ll look at your entries, they'll look at your products to see if there there is "
             'risk that warrants further review such as an audit. CVP form 29, if they know '
             "there is an issue or customs doesn't agree with you, they may issue a notice of "
             'action and assess additional duties.',
      'title': 'Audits & Drawback: What Every Importer Needs to Know Right Now (Flexport)',
      'url': 'https://www.youtube.com/watch?v=xtorVFI9g4c&t=1205s',
      'video_id': 'xtorVFI9g4c'},
     {'author': 'Shipware',
      'channel': 'Shipware',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=6WEh56BpnbM&t=15s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm joined with Josh Taylor and Audi K Teddy they're going to walk through five "
              'mistakes to avoid in your UPS and FedEx negotiations Josh Taylor is our senior.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "I'm joined with Josh Taylor and Audi K Teddy they're going to walk through five "
             'mistakes to avoid in your UPS and FedEx negotiations Josh Taylor is our senior.',
      'title': "Don't Flub Your UPS/FedEx Negotiations: 5 Mistakes to Avoid | May 29, 2024 | "
               'Shipware Webinar (Shipware)',
      'url': 'https://www.youtube.com/watch?v=6WEh56BpnbM&t=15s',
      'video_id': '6WEh56BpnbM'},
     {'author': 'Vert Energy Group',
      'channel': 'Vert Energy Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:29](https://www.youtube.com/watch?v=bQpXnGBfNJY&t=269s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Savings beings to be realized to request a free utility bill analysis or for '
              'more information visit us at Vert Energy group.com or contact us with the '
              'information on the screen.',
      'timestamp': 269,
      'timestamp_label': '[00:04:29]',
      'timestamp_seconds': 269,
      'tip': 'Savings beings to be realized to request a free utility bill analysis or for '
             'more information visit us at Vert Energy group.com or contact us with the '
             'information on the screen.',
      'title': 'Utility Bill Audit - Introduction (Vert Energy Group)',
      'url': 'https://www.youtube.com/watch?v=bQpXnGBfNJY&t=269s',
      'video_id': 'bQpXnGBfNJY'},
     {'author': 'Fredrikson',
      'channel': 'Fredrikson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:50:00](https://www.youtube.com/watch?v=VMuMGmjYplc&t=3000s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That time and then they look at all of the payments during that 90-day episode '
              "and if you're if your costs exceed that you're at risk to pay back CMS and if.",
      'timestamp': 3000,
      'timestamp_label': '[00:50:00]',
      'timestamp_seconds': 3000,
      'tip': 'That time and then they look at all of the payments during that 90-day episode '
             "and if you're if your costs exceed that you're at risk to pay back CMS and if.",
      'title': 'Co-Management/Gainsharing/Shared Savings Arrangements and CMS’s Episode-Based '
               'Payment Initiatives (Fredrikson)',
      'url': 'https://www.youtube.com/watch?v=VMuMGmjYplc&t=3000s',
      'video_id': 'VMuMGmjYplc'},
     {'author': 'Cherry Bekaert',
      'channel': 'Cherry Bekaert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=0wGT1LCIPkY&t=55s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I got Bill harson and Andre Khan so um Bill why don't you say hello here hi "
              'everybody thank you so much for having me uh Brooks looking forward to our '
              'conversation today and where are you sitting today Bill uh I support our Austin '
              'office down here in Texas all.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': "I got Bill harson and Andre Khan so um Bill why don't you say hello here hi "
             'everybody thank you so much for having me uh Brooks looking forward to our '
             'conversation today and where are you sitting today Bill uh I support our Austin '
             'office down here in Texas all.',
      'title': 'Energy Savings Revolution – Section 179D for Commercial Buildings (Cherry '
               'Bekaert)',
      'url': 'https://www.youtube.com/watch?v=0wGT1LCIPkY&t=55s',
      'video_id': '0wGT1LCIPkY'},
     {'author': 'Mingle Health',
      'channel': 'Mingle Health',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:38](https://www.youtube.com/watch?v=BVWc_qDwmOo&t=878s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Calculations they've also provided some clarity on methodology for capping the "
              "aco's risk score growth and Regional risk score growth uh they've provided.",
      'timestamp': 878,
      'timestamp_label': '[00:14:38]',
      'timestamp_seconds': 878,
      'tip': "Calculations they've also provided some clarity on methodology for capping the "
             "aco's risk score growth and Regional risk score growth uh they've provided.",
      'title': 'Medicare Shared Savings Program (MSSP) Changes in 2025 (Mingle Health)',
      'url': 'https://www.youtube.com/watch?v=BVWc_qDwmOo&t=878s',
      'video_id': 'BVWc_qDwmOo'},
     {'author': 'Refund Retriever',
      'channel': 'Refund Retriever',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=v9AT9Omrd5c&t=79s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "However, there's not going to be an additional handling charge associated with "
              'any of these when the large package charge is applied. So, how can you minimize '
              'or avoid UPS large package charges and save money? Re-evaluate your packaging.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': "However, there's not going to be an additional handling charge associated with "
             'any of these when the large package charge is applied. So, how can you minimize '
             'or avoid UPS large package charges and save money? Re-evaluate your packaging.',
      'title': 'UPS Large Package Surcharge for 2025 (Refund Retriever)',
      'url': 'https://www.youtube.com/watch?v=v9AT9Omrd5c&t=79s',
      'video_id': 'v9AT9Omrd5c'},
     {'author': 'Scarbrough Global',
      'channel': 'Scarbrough Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:37](https://www.youtube.com/watch?v=iflfyKDuJzY&t=277s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Which component needs to be focused on to make the highest financial impact and '
              "we'll move through here on to the next kind of elements and I see I think I see "
              "a question I'm not not too sure is there anything on your side of Anor we okay.",
      'timestamp': 277,
      'timestamp_label': '[00:04:37]',
      'timestamp_seconds': 277,
      'tip': 'Which component needs to be focused on to make the highest financial impact and '
             "we'll move through here on to the next kind of elements and I see I think I see "
             "a question I'm not not too sure is there anything on your side of Anor we okay.",
      'title': 'How to negotiate contracts with UPS and FedEx intelligently (Scarbrough '
               'Global)',
      'url': 'https://www.youtube.com/watch?v=iflfyKDuJzY&t=277s',
      'video_id': 'iflfyKDuJzY'}],
 6: [{'author': 'Barracuda B2B',
      'channel': 'Barracuda B2B',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:25](https://www.youtube.com/watch?v=vnkFP_2Jzng&t=1045s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That doesn't exist in our business model. Our sole intention and purpose is to "
              "find the best deal for the client that's going to make their process better and "
              'more efficient.',
      'timestamp': 1045,
      'timestamp_label': '[00:17:25]',
      'timestamp_seconds': 1045,
      'tip': "That doesn't exist in our business model. Our sole intention and purpose is to "
             "find the best deal for the client that's going to make their process better and "
             'more efficient.',
      'title': "The Manufacturers' Efficiency Webinar Series: Dumpster Diving --  Find Savings "
               'in Waste Expenses (Barracuda B2B)',
      'url': 'https://www.youtube.com/watch?v=vnkFP_2Jzng&t=1045s',
      'video_id': 'vnkFP_2Jzng'},
     {'author': 'UtilityBillAudits',
      'channel': 'UtilityBillAudits',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=5A8gPPLuUaY&t=21s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'As for refunds, if you think these large utility firms are simply going to hand '
              "you a check for overages you've paid, think again. Let our utility bill "
              'auditing specialists help identify these over-payments and find your company '
              'monthly savings on your utility bills.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'As for refunds, if you think these large utility firms are simply going to hand '
             "you a check for overages you've paid, think again. Let our utility bill auditing "
             'specialists help identify these over-payments and find your company monthly '
             'savings on your utility bills.',
      'title': 'Utility Bill Audit Service | Get Overages Refunded Using Our Free Utility Bill '
               'Analysis (UtilityBillAudits)',
      'url': 'https://www.youtube.com/watch?v=5A8gPPLuUaY&t=21s',
      'video_id': '5A8gPPLuUaY'},
     {'author': 'Engineered Tax Services',
      'channel': 'Engineered Tax Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:51:15](https://www.youtube.com/watch?v=qEFJIGNNOkw&t=3075s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You can certainly use that for your existing clients. Uh but it's a it's a "
              'phenomenal tool to use for new potential clients as well. Uh and might be a '
              'great lead-in uh for you to win business. Um okay, one more question. Andy '
              'says, "Can you talk about audit protection?',
      'timestamp': 3075,
      'timestamp_label': '[00:51:15]',
      'timestamp_seconds': 3075,
      'tip': "You can certainly use that for your existing clients. Uh but it's a it's a "
             'phenomenal tool to use for new potential clients as well. Uh and might be a '
             'great lead-in uh for you to win business. Um okay, one more question. Andy says, '
             '"Can you talk about audit protection?',
      'title': 'Webinar: Cost Segregation Deep Dive & Referral Process - August 27 (Engineered '
               'Tax Services)',
      'url': 'https://www.youtube.com/watch?v=qEFJIGNNOkw&t=3075s',
      'video_id': 'qEFJIGNNOkw'},
     {'author': 'Workforce Texoma',
      'channel': 'Workforce Texoma',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:35](https://www.youtube.com/watch?v=gkdhTjVa4lQ&t=215s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Work opportunity tax credit forms with you to the interview the irs form 8850 '
              'you can find that at irs.gov the eta form 9061 you can find that at dol eta.gov '
              'for more information about work opportunity tax credit individuals may call '
              '1-800-829-1.',
      'timestamp': 215,
      'timestamp_label': '[00:03:35]',
      'timestamp_seconds': 215,
      'tip': 'Work opportunity tax credit forms with you to the interview the irs form 8850 '
             'you can find that at irs.gov the eta form 9061 you can find that at dol eta.gov '
             'for more information about work opportunity tax credit individuals may call '
             '1-800-829-1.',
      'title': 'Work Opportunity Tax Credit – Employee (Workforce Texoma)',
      'url': 'https://www.youtube.com/watch?v=gkdhTjVa4lQ&t=215s',
      'video_id': 'gkdhTjVa4lQ'},
     {'author': 'Workforce3One',
      'channel': 'Workforce3One',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=w5ydUbSH5TI&t=104s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can find out all the details on eligibility requirements at doleta. There '
              'are some people who don’t qualify: relatives and dependents of the employer '
              'who’s hiring, or majority owners of the business.',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': 'You can find out all the details on eligibility requirements at doleta. There '
             'are some people who don’t qualify: relatives and dependents of the employer '
             'who’s hiring, or majority owners of the business.',
      'title': 'Work Opportunity Tax Credit: A Tutorial for Employers (Workforce3One)',
      'url': 'https://www.youtube.com/watch?v=w5ydUbSH5TI&t=104s',
      'video_id': 'w5ydUbSH5TI'},
     {'author': 'iDrive Logistics',
      'channel': 'iDrive Logistics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:35](https://www.youtube.com/watch?v=H64bWcLI0O8&t=875s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I find it particularly perplexing to see that there's punitive pricing now "
              'attacking those very packages and it could lead to some really unintended '
              'consequences for UPS and for FedEx and any other carrier that chooses to pursue '
              'this methodology.',
      'timestamp': 875,
      'timestamp_label': '[00:14:35]',
      'timestamp_seconds': 875,
      'tip': "I find it particularly perplexing to see that there's punitive pricing now "
             'attacking those very packages and it could lead to some really unintended '
             'consequences for UPS and for FedEx and any other carrier that chooses to pursue '
             'this methodology.',
      'title': 'UPS Additional Handling 2025: How a 5‑Cubic‑Foot Rule Can Add 190\u202f% to '
               'Your Parcel Costs (iDrive Logistics)',
      'url': 'https://www.youtube.com/watch?v=H64bWcLI0O8&t=875s',
      'video_id': 'H64bWcLI0O8'},
     {'author': 'Advise RE',
      'channel': 'Advise RE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=8ZzVeQLb80E&t=28s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You just bought a property for a million dollars and you realize after doing a '
              'land building allocation, you always have to do that. Very Very first thing you '
              "do when you're buying this property is figure out what portion of it is land, "
              'what portion of it is building.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': 'You just bought a property for a million dollars and you realize after doing a '
             'land building allocation, you always have to do that. Very Very first thing you '
             "do when you're buying this property is figure out what portion of it is land, "
             'what portion of it is building.',
      'title': 'When a Cost Segregation Study Is Actually Worth It 💡 (Advise RE)',
      'url': 'https://www.youtube.com/watch?v=8ZzVeQLb80E&t=28s',
      'video_id': '8ZzVeQLb80E'},
     {'author': 'Ashokan Water Meter & Backflow',
      'channel': 'Ashokan Water Meter & Backflow',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:24](https://www.youtube.com/watch?v=PRQE0XuoBbg&t=24s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You back the money you may be owed and if we find nothing a miss our services '
              "are completely free that's a Shen water audit Services what.",
      'timestamp': 24,
      'timestamp_label': '[00:00:24]',
      'timestamp_seconds': 24,
      'tip': 'You back the money you may be owed and if we find nothing a miss our services '
             "are completely free that's a Shen water audit Services what.",
      'title': 'Utility Water Bill Audit (Ashokan Water Meter & Backflow)',
      'url': 'https://www.youtube.com/watch?v=PRQE0XuoBbg&t=24s',
      'video_id': 'PRQE0XuoBbg'},
     {'author': 'PM Business Advisors',
      'channel': 'PM Business Advisors',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:39](https://www.youtube.com/watch?v=ePf76grjr8U&t=99s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The check in hand and then the best part about the entire project is all these '
              "projects are done on a 100 contingent basis where there's no risk to the client "
              'so if you want to find out more about reverse sales and use tax audits reach '
              'out to us today thanks.',
      'timestamp': 99,
      'timestamp_label': '[00:01:39]',
      'timestamp_seconds': 99,
      'tip': 'The check in hand and then the best part about the entire project is all these '
             "projects are done on a 100 contingent basis where there's no risk to the client "
             'so if you want to find out more about reverse sales and use tax audits reach out '
             'to us today thanks.',
      'title': 'Sales and Use Tax Reverse Audit (PM Business Advisors)',
      'url': 'https://www.youtube.com/watch?v=ePf76grjr8U&t=99s',
      'video_id': 'ePf76grjr8U'},
     {'author': 'Amware Fulfillment',
      'channel': 'Amware Fulfillment',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:59](https://www.youtube.com/watch?v=d3jQIelSHJM&t=659s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'From a sourcing project was carrier diversification that would have been '
              'unheard of prior to that so the industry is focusing on it has been focusing '
              'on.',
      'timestamp': 659,
      'timestamp_label': '[00:10:59]',
      'timestamp_seconds': 659,
      'tip': 'From a sourcing project was carrier diversification that would have been unheard '
             'of prior to that so the industry is focusing on it has been focusing on.',
      'title': 'Making Sense of Parcel Costs with Joe Wilkinson at Intelligent Audit (Amware '
               'Fulfillment)',
      'url': 'https://www.youtube.com/watch?v=d3jQIelSHJM&t=659s',
      'video_id': 'd3jQIelSHJM'},
     {'author': 'CostSegRx',
      'channel': 'CostSegRx',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=Ha5KYCa_Yjk&t=50s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Your first year depreciation is 49,806. And below that, you'll see that I've "
              'worked up a revised fixed asset schedule showing the building basis, the '
              'distributive trades and services, the land improvements, the land, and the '
              'total.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': "Your first year depreciation is 49,806. And below that, you'll see that I've "
             'worked up a revised fixed asset schedule showing the building basis, the '
             'distributive trades and services, the land improvements, the land, and the '
             'total.',
      'title': 'Cost Segregation Example: $350K Rental Property Tax Savings (2026) (CostSegRx)',
      'url': 'https://www.youtube.com/watch?v=Ha5KYCa_Yjk&t=50s',
      'video_id': 'Ha5KYCa_Yjk'},
     {'author': 'Aaron Hall FAQs',
      'channel': 'Aaron Hall FAQs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:35](https://www.youtube.com/watch?v=VeB6ri8vEm8&t=395s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Minneapolis Minnesota generally representing business owners feel free to uh '
              'look in the description below to find out related information.',
      'timestamp': 395,
      'timestamp_label': '[00:06:35]',
      'timestamp_seconds': 395,
      'tip': 'Minneapolis Minnesota generally representing business owners feel free to uh '
             'look in the description below to find out related information.',
      'title': 'What Should You Know Before Hiring a Contingency Fee Lawyer? (Aaron Hall FAQs)',
      'url': 'https://www.youtube.com/watch?v=VeB6ri8vEm8&t=395s',
      'video_id': 'VeB6ri8vEm8'},
     {'author': 'Refund Retriever',
      'channel': 'Refund Retriever',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:36](https://www.youtube.com/watch?v=Tu2F34LOK0g&t=156s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Trying to get the guaranteed discount levels as high as possible and having '
              'less of your overall discount apply to the shipping volume so stay tuned for '
              'part two of our UPS Agreement blog and video series if you have any questions '
              'about your UPS contracts give us a call.',
      'timestamp': 156,
      'timestamp_label': '[00:02:36]',
      'timestamp_seconds': 156,
      'tip': 'Trying to get the guaranteed discount levels as high as possible and having less '
             'of your overall discount apply to the shipping volume so stay tuned for part two '
             'of our UPS Agreement blog and video series if you have any questions about your '
             'UPS contracts give us a call.',
      'title': 'UPS Shipper Agreement Negotiation: Understanding then Optimizing – Part 1 '
               '(Refund Retriever)',
      'url': 'https://www.youtube.com/watch?v=Tu2F34LOK0g&t=156s',
      'video_id': 'Tu2F34LOK0g'},
     {'author': 'Schooley Mitchell',
      'channel': 'Schooley Mitchell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=-6BHCV0JL-A&t=87s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If an employee wants to provide their own ppe their employer must be able to '
              'ensure that they are following the proper protocols in regards to cleaning '
              'reuse and disposal and and that the ppe is properly suited for its intended '
              'purposes.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': 'If an employee wants to provide their own ppe their employer must be able to '
             'ensure that they are following the proper protocols in regards to cleaning reuse '
             'and disposal and and that the ppe is properly suited for its intended purposes.',
      'title': 'Growing Your Business with Denis Tan Episode #8 (Schooley Mitchell)',
      'url': 'https://www.youtube.com/watch?v=-6BHCV0JL-A&t=87s',
      'video_id': '-6BHCV0JL-A'},
     {'author': 'Cherry Bekaert',
      'channel': 'Cherry Bekaert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:02](https://www.youtube.com/watch?v=S7Qlojol4pE&t=482s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In our filings as opposed to blindly just kind of paying it and seeing what '
              "happens so that that was a huge help honestly that is music to my ears I'm sure "
              'it is but yes.',
      'timestamp': 482,
      'timestamp_label': '[00:08:02]',
      'timestamp_seconds': 482,
      'tip': 'In our filings as opposed to blindly just kind of paying it and seeing what '
             "happens so that that was a huge help honestly that is music to my ears I'm sure "
             'it is but yes.',
      'title': 'Sales Tax Reverse Audit Service Client Interview (Cherry Bekaert)',
      'url': 'https://www.youtube.com/watch?v=S7Qlojol4pE&t=482s',
      'video_id': 'S7Qlojol4pE'}],
 7: [{'author': 'Refund Retriever',
      'channel': 'Refund Retriever',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=-UrxqsNpEm0&t=108s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'UPS states that a Residential surcharge will apply (in addition to all '
              'applicable Area Surcharges) to any delivery to, or a UPS On-Call Pickup request '
              'from, a location that is a home, including a business operating out of a home.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': 'UPS states that a Residential surcharge will apply (in addition to all '
             'applicable Area Surcharges) to any delivery to, or a UPS On-Call Pickup request '
             'from, a location that is a home, including a business operating out of a home.',
      'title': 'Residential Surcharge Contract Negotiation Considerations (Refund Retriever)',
      'url': 'https://www.youtube.com/watch?v=-UrxqsNpEm0&t=108s',
      'video_id': '-UrxqsNpEm0'},
     {'author': 'UPS',
      'channel': 'UPS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:59](https://www.youtube.com/watch?v=dp5xVhpuf64&t=119s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sure that you enter the correct billable weight when creating your shipment in '
              'order to avoid the shipping charge correction audit fee from being applied '
              'follow the steps mentioned in this video to avoid unnecessary fees on your '
              'parcels.',
      'timestamp': 119,
      'timestamp_label': '[00:01:59]',
      'timestamp_seconds': 119,
      'tip': 'Sure that you enter the correct billable weight when creating your shipment in '
             'order to avoid the shipping charge correction audit fee from being applied '
             'follow the steps mentioned in this video to avoid unnecessary fees on your '
             'parcels.',
      'title': 'How to Calculate Billable Weight on UPS Small Parcels | UPS (UPS)',
      'url': 'https://www.youtube.com/watch?v=dp5xVhpuf64&t=119s',
      'video_id': 'dp5xVhpuf64'},
     {'author': 'AirDNA',
      'channel': 'AirDNA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=nj5gSNmRQuU&t=68s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This means you get larger tax deductions sooner and lower your tax bill much '
              'faster. The process typically includes three steps. First, a review of all '
              'purchase documentation and receipts to identify what qualifies.',
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': 'This means you get larger tax deductions sooner and lower your tax bill much '
             'faster. The process typically includes three steps. First, a review of all '
             'purchase documentation and receipts to identify what qualifies.',
      'title': 'Cost Segregation for Airbnb Hosts: The Tax Strategy That Saves Thousands '
               '(AirDNA)',
      'url': 'https://www.youtube.com/watch?v=nj5gSNmRQuU&t=68s',
      'video_id': 'nj5gSNmRQuU'},
     {'author': 'Refund Retriever',
      'channel': 'Refund Retriever',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=P3sA9eO0D-k&t=40s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This will take you to step 2. Step 2 is where you will provide us with access '
              'to your UPS and/or FedEx Online Billing Centers as well as your billing '
              'address. The billing center is where we download and process all of your '
              'refunds. Our functionality is similar to mint.',
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': 'This will take you to step 2. Step 2 is where you will provide us with access to '
             'your UPS and/or FedEx Online Billing Centers as well as your billing address. '
             'The billing center is where we download and process all of your refunds. Our '
             'functionality is similar to mint.',
      'title': 'How to get started with Refund Retriever FedEx UPS auditing (Refund Retriever)',
      'url': 'https://www.youtube.com/watch?v=P3sA9eO0D-k&t=40s',
      'video_id': 'P3sA9eO0D-k'},
     {'author': 'Watchdog Advisory',
      'channel': 'Watchdog Advisory',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:59](https://www.youtube.com/watch?v=5eTaFaKQdHY&t=119s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Savings then there's no fee with just the three minutes set up the process is "
              'quick simple and requires no work on our clients part our process is so simple '
              'that we can be on languor invoices tomorrow all we need is your agreement to '
              'get started.',
      'timestamp': 119,
      'timestamp_label': '[00:01:59]',
      'timestamp_seconds': 119,
      'tip': "Savings then there's no fee with just the three minutes set up the process is "
             'quick simple and requires no work on our clients part our process is so simple '
             'that we can be on languor invoices tomorrow all we need is your agreement to get '
             'started.',
      'title': 'Parcel Shipping Audit (Watchdog Advisory)',
      'url': 'https://www.youtube.com/watch?v=5eTaFaKQdHY&t=119s',
      'video_id': '5eTaFaKQdHY'},
     {'author': 'IATF 16949 Auditing',
      'channel': 'IATF 16949 Auditing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:15](https://www.youtube.com/watch?v=4-TMYIb48FA&t=435s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Even in a remote audit these concerns should be clearly brought to the '
              'attention of the relevant process owner and finally based upon the information '
              'collected auditors should always follow audit trails to other relevant.',
      'timestamp': 435,
      'timestamp_label': '[00:07:15]',
      'timestamp_seconds': 435,
      'tip': 'Even in a remote audit these concerns should be clearly brought to the attention '
             'of the relevant process owner and finally based upon the information collected '
             'auditors should always follow audit trails to other relevant.',
      'title': 'IATF 16949 Audits | Auditing The Contingency Planning Process Part 1 | IAOB | '
               'SMMT (IATF 16949 Auditing)',
      'url': 'https://www.youtube.com/watch?v=4-TMYIb48FA&t=435s',
      'video_id': '4-TMYIb48FA'},
     {'author': 'Nolan Feeny',
      'channel': 'Nolan Feeny',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=lKGpIaNHgRw&t=87s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Patient and streamline the healthcare process providers are encouraged to '
              'invest in areas that provide a patient high quality and efficient services '
              'next.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': 'Patient and streamline the healthcare process providers are encouraged to invest '
             'in areas that provide a patient high quality and efficient services next.',
      'title': 'Medicare Shared Savings Program (Nolan Feeny)',
      'url': 'https://www.youtube.com/watch?v=lKGpIaNHgRw&t=87s',
      'video_id': 'lKGpIaNHgRw'},
     {'author': 'FedEx',
      'channel': 'FedEx',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=OpAC2Ev8SH0&t=79s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '165 inches FedEx Ground, and FedEx Home Delivery Maximum. You may also want to '
              'calculate the dimensional weight or DIM weight. Many carriers will compare the '
              'actual weight of the package with the dimensional weight and charge the higher '
              'of the two.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': '165 inches FedEx Ground, and FedEx Home Delivery Maximum. You may also want to '
             'calculate the dimensional weight or DIM weight. Many carriers will compare the '
             'actual weight of the package with the dimensional weight and charge the higher '
             'of the two.',
      'title': 'How to Measure a Box for Shipping | The Official FedEx Guide (FedEx)',
      'url': 'https://www.youtube.com/watch?v=OpAC2Ev8SH0&t=79s',
      'video_id': 'OpAC2Ev8SH0'},
     {'author': 'Macronet Services',
      'channel': 'Macronet Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=QMubvpeApZk&t=60s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Uh very quickly within the industry and mostly because of our heritage we've "
              'spent the last 20 years on the carrier side both on the design and delivery '
              'but.',
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': "Uh very quickly within the industry and mostly because of our heritage we've "
             'spent the last 20 years on the carrier side both on the design and delivery but.',
      'title': 'What is TEM or Telecom Expense Management? (Macronet Services)',
      'url': 'https://www.youtube.com/watch?v=QMubvpeApZk&t=60s',
      'video_id': 'QMubvpeApZk'},
     {'author': 'Health Affairs',
      'channel': 'Health Affairs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:23](https://www.youtube.com/watch?v=Zzb5OKFwcbg&t=863s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So the dispersed convener ACOs scored no better on quality on overall quality '
              'metrics than the local ACOs or the non-convener ACOs. So they they may have '
              "been delivering better care but didn't show up uh in sort of those aggregate "
              'quality measures.',
      'timestamp': 863,
      'timestamp_label': '[00:14:23]',
      'timestamp_seconds': 863,
      'tip': 'So the dispersed convener ACOs scored no better on quality on overall quality '
             'metrics than the local ACOs or the non-convener ACOs. So they they may have been '
             "delivering better care but didn't show up uh in sort of those aggregate quality "
             'measures.',
      'title': 'How ACO Conveners Are Changing the Medicare Shared Savings Program (MSSP) '
               'Behind the Scenes (Health Affairs)',
      'url': 'https://www.youtube.com/watch?v=Zzb5OKFwcbg&t=863s',
      'video_id': 'Zzb5OKFwcbg'},
     {'author': 'Reyann Davis',
      'channel': 'Reyann Davis',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:32](https://www.youtube.com/watch?v=EotsrYaUjUs&t=812s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Patient population as part of your ACO because remember they're assigned to "
              'your ACO based on their plurality of PCP care it also gives you an opportunity '
              'um to address quality measures and ICD tin.',
      'timestamp': 812,
      'timestamp_label': '[00:13:32]',
      'timestamp_seconds': 812,
      'tip': "Patient population as part of your ACO because remember they're assigned to your "
             'ACO based on their plurality of PCP care it also gives you an opportunity um to '
             'address quality measures and ICD tin.',
      'title': 'What is a Medicare Shared Savings Program ACO and participation options? '
               '(Reyann Davis)',
      'url': 'https://www.youtube.com/watch?v=EotsrYaUjUs&t=812s',
      'video_id': 'EotsrYaUjUs'},
     {'author': 'MPAY Inc.',
      'channel': 'MPAY Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:26](https://www.youtube.com/watch?v=ZAJF8uhnR3Q&t=26s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Take advantage of these tax credits because the application process can be '
              "time-consuming and complicated that's why we created the pay entry hire watse.",
      'timestamp': 26,
      'timestamp_label': '[00:00:26]',
      'timestamp_seconds': 26,
      'tip': 'Take advantage of these tax credits because the application process can be '
             "time-consuming and complicated that's why we created the pay entry hire watse.",
      'title': 'WOTC Work Opportunity Tax Credit (MPAY Inc.)',
      'url': 'https://www.youtube.com/watch?v=ZAJF8uhnR3Q&t=26s',
      'video_id': 'ZAJF8uhnR3Q'},
     {'author': 'Cherry Bekaert',
      'channel': 'Cherry Bekaert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=nR3lgfqRNqg&t=22s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And this installment will focus on the transition from 174 to 174A, new '
              'documentation requirements to the form 6765, um key elections that are '
              'clarified under refrac 2025-28 as well as audit train trends and court cases. '
              'This session also qualifies for one hour of CPE.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'And this installment will focus on the transition from 174 to 174A, new '
             'documentation requirements to the form 6765, um key elections that are clarified '
             'under refrac 2025-28 as well as audit train trends and court cases. This session '
             'also qualifies for one hour of CPE.',
      'title': 'R&D Tax Credit Updates: Section 174A Explained (Cherry Bekaert)',
      'url': 'https://www.youtube.com/watch?v=nR3lgfqRNqg&t=22s',
      'video_id': 'nR3lgfqRNqg'},
     {'author': 'SPCNVideos',
      'channel': 'SPCNVideos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:52](https://www.youtube.com/watch?v=dDY5xxNu_f8&t=172s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "En met tellson's of contracts and deurbel you know what a small package "
              'koorpartij snow and what they do what you do kansas today voor via nelsons of '
              'your gps een expert and see for yourself how I can say you free de 20 percent '
              'of your existing small fish goldrush.',
      'timestamp': 172,
      'timestamp_label': '[00:02:52]',
      'timestamp_seconds': 172,
      'tip': "En met tellson's of contracts and deurbel you know what a small package "
             'koorpartij snow and what they do what you do kansas today voor via nelsons of '
             'your gps een expert and see for yourself how I can say you free de 20 percent of '
             'your existing small fish goldrush.',
      'title': 'Five most common mistakes companies make when negotiating their UPS agreement '
               '(SPCNVideos)',
      'url': 'https://www.youtube.com/watch?v=dDY5xxNu_f8&t=172s',
      'video_id': 'dDY5xxNu_f8'},
     {'author': 'Refund Retriever',
      'channel': 'Refund Retriever',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:42](https://www.youtube.com/watch?v=JAnVvaSg0TA&t=282s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Take your time quantify any proposal that's presented to you shipping costs can "
              'easily turn from a liability to a competitive advantage with very little work '
              'so if you have any questions about refund retriever or your contracts give us a '
              'call.',
      'timestamp': 282,
      'timestamp_label': '[00:04:42]',
      'timestamp_seconds': 282,
      'tip': "Take your time quantify any proposal that's presented to you shipping costs can "
             'easily turn from a liability to a competitive advantage with very little work so '
             'if you have any questions about refund retriever or your contracts give us a '
             'call.',
      'title': 'Carrier Contract Negotiation: Basic Strategy (Refund Retriever)',
      'url': 'https://www.youtube.com/watch?v=JAnVvaSg0TA&t=282s',
      'video_id': 'JAnVvaSg0TA'}],
 8: [{'author': 'Commercial Real Estate Escalations Made Simple',
      'channel': 'Commercial Real Estate Escalations Made Simple',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:12](https://www.youtube.com/watch?v=mgDY9HBbVA8&t=372s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The database more does more than just crunch numbers. It's designed to build "
              'trust. It guarantees accuracy because all calculations are automated and tied '
              'directly to the lease data. That builds credibility with owners.',
      'timestamp': 372,
      'timestamp_label': '[00:06:12]',
      'timestamp_seconds': 372,
      'tip': "The database more does more than just crunch numbers. It's designed to build "
             'trust. It guarantees accuracy because all calculations are automated and tied '
             'directly to the lease data. That builds credibility with owners.',
      'title': 'CAM Reconciliation Case Study – How My Database Fixes the Most Common Lease '
               'Mistake (Commercial Real Estate Escalations Made Simple)',
      'url': 'https://www.youtube.com/watch?v=mgDY9HBbVA8&t=372s',
      'video_id': 'mgDY9HBbVA8'},
     {'author': 'Scarbrough Global',
      'channel': 'Scarbrough Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:35:16](https://www.youtube.com/watch?v=jEjymzbOEFQ&t=2116s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They do what will happen after that usually like I said within two business '
              "days once that once it's all spun up they'll get access to the platform and.",
      'timestamp': 2116,
      'timestamp_label': '[00:35:16]',
      'timestamp_seconds': 2116,
      'tip': 'They do what will happen after that usually like I said within two business days '
             "once that once it's all spun up they'll get access to the platform and.",
      'title': 'What is Parcel Audit and Contact Engineering? Full Version (Scarbrough Global)',
      'url': 'https://www.youtube.com/watch?v=jEjymzbOEFQ&t=2116s',
      'video_id': 'jEjymzbOEFQ'},
     {'author': 'Engineered Tax Services',
      'channel': 'Engineered Tax Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:42](https://www.youtube.com/watch?v=sXpa52KOvog&t=1902s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's something I use 20 times a day as I'm talking with clients, and there's a "
              'version of this on our website as well. So, as an affiliate, just remember you '
              'have all these tools and you have all of the views and access to things within '
              'our portal.',
      'timestamp': 1902,
      'timestamp_label': '[00:31:42]',
      'timestamp_seconds': 1902,
      'tip': "It's something I use 20 times a day as I'm talking with clients, and there's a "
             'version of this on our website as well. So, as an affiliate, just remember you '
             'have all these tools and you have all of the views and access to things within '
             'our portal.',
      'title': 'Webinar: Cost Segregation for Real Estate Professionals (Engineered Tax '
               'Services)',
      'url': 'https://www.youtube.com/watch?v=sXpa52KOvog&t=1902s',
      'video_id': 'sXpa52KOvog'},
     {'author': 'Scarbrough Global',
      'channel': 'Scarbrough Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=NKDaSW7CKiQ&t=21s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, kind of call it our 3D approach. The data pieces is the audit, so that's uh "
              "an ongoing parcel audit that's attached to UPS and FedEx online billing. So, "
              'this really has no impact to the way that folks um ship or operate.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "So, kind of call it our 3D approach. The data pieces is the audit, so that's uh "
             "an ongoing parcel audit that's attached to UPS and FedEx online billing. So, "
             'this really has no impact to the way that folks um ship or operate.',
      'title': 'How does the Parcel Audit work? (Scarbrough Global)',
      'url': 'https://www.youtube.com/watch?v=NKDaSW7CKiQ&t=21s',
      'video_id': 'NKDaSW7CKiQ'},
     {'author': "Brady's Corner",
      'channel': "Brady's Corner",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=t695zwyQZ7M&t=20s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Systems in commercial buildings HVAC interior lighting building envelope by '
              'taking advantage of 179 D your business may be qualified to receive up to $1 '
              '80.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'Systems in commercial buildings HVAC interior lighting building envelope by '
             'taking advantage of 179 D your business may be qualified to receive up to $1 80.',
      'title': "179D Energy Efficient Building Deduction (Brady's Corner)",
      'url': 'https://www.youtube.com/watch?v=t695zwyQZ7M&t=20s',
      'video_id': 't695zwyQZ7M'},
     {'author': 'LouisvilleMetroTV',
      'channel': 'LouisvilleMetroTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:44](https://www.youtube.com/watch?v=F5ky8tV3ZNs&t=44s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t really know how you can improve. Did you guys like clean out the "
              'refrigerators in the whole building? Now, we have more of a reason to do it '
              'because of the Office of Sustainability having some other projects to include '
              "this data in. So, we're excited to partner.",
      'timestamp': 44,
      'timestamp_label': '[00:00:44]',
      'timestamp_seconds': 44,
      'tip': "'t really know how you can improve. Did you guys like clean out the "
             'refrigerators in the whole building? Now, we have more of a reason to do it '
             'because of the Office of Sustainability having some other projects to include '
             "this data in. So, we're excited to partner.",
      'title': "What's a waste audit? (LouisvilleMetroTV)",
      'url': 'https://www.youtube.com/watch?v=F5ky8tV3ZNs&t=44s',
      'video_id': 'F5ky8tV3ZNs'},
     {'author': 'Refund Retriever',
      'channel': 'Refund Retriever',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=C_7KIASDpS8&t=63s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This should give your carrier rep a hint that a contract negotiation will take '
              'place. Know your own data Remember, FedEx and UPS have full access to your '
              'shipping reports and data.',
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': 'This should give your carrier rep a hint that a contract negotiation will take '
             'place. Know your own data Remember, FedEx and UPS have full access to your '
             'shipping reports and data.',
      'title': 'Tips for Carrier Contract Negotiation (PART 1) (Refund Retriever)',
      'url': 'https://www.youtube.com/watch?v=C_7KIASDpS8&t=63s',
      'video_id': 'C_7KIASDpS8'},
     {'author': 'Deloitte US',
      'channel': 'Deloitte US',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=uODSKRdc1bI&t=25s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Us to identify and apply for potentially available wattsy credits we can use '
              'our tool t4 wattsy along with your current HR applicant tracking systems to.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': 'Us to identify and apply for potentially available wattsy credits we can use our '
             'tool t4 wattsy along with your current HR applicant tracking systems to.',
      'title': 'Work Opportunity Tax Credit (WOTC) Services (Deloitte US)',
      'url': 'https://www.youtube.com/watch?v=uODSKRdc1bI&t=25s',
      'video_id': 'uODSKRdc1bI'},
     {'author': 'Oncor',
      'channel': 'Oncor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=yHlhF0nEJ14&t=15s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Office building, or a data center than someone's home. So, Encore is here to "
              'explain some of the terms  and processes that we.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Office building, or a data center than someone's home. So, Encore is here to "
             'explain some of the terms  and processes that we.',
      'title': 'Understanding Demand Ratchet Charges for Businesses (Oncor)',
      'url': 'https://www.youtube.com/watch?v=yHlhF0nEJ14&t=15s',
      'video_id': 'yHlhF0nEJ14'},
     {'author': 'Busch Systems',
      'channel': 'Busch Systems',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:59:30](https://www.youtube.com/watch?v=5sOj1M92UC4&t=3570s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Savannah and Burke James were saying a key part for a good waste audit is '
              'knowing your local environment so even if even if for some reason your data is.',
      'timestamp': 3570,
      'timestamp_label': '[00:59:30]',
      'timestamp_seconds': 3570,
      'tip': 'Savannah and Burke James were saying a key part for a good waste audit is '
             'knowing your local environment so even if even if for some reason your data is.',
      'title': 'How To Do A Waste Audit (Busch Systems)',
      'url': 'https://www.youtube.com/watch?v=5sOj1M92UC4&t=3570s',
      'video_id': '5sOj1M92UC4'},
     {'author': 'COPE Health Solutions',
      'channel': 'COPE Health Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:59](https://www.youtube.com/watch?v=PDcTn9Sq3mg&t=1499s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Operating models in order to run a value-based system you need the '
              'infrastructure the data the analytics the care management the outreach and the.',
      'timestamp': 1499,
      'timestamp_label': '[00:24:59]',
      'timestamp_seconds': 1499,
      'tip': 'Operating models in order to run a value-based system you need the '
             'infrastructure the data the analytics the care management the outreach and the.',
      'title': 'Updates to Medicare Direct and Medicare Shared Savings Programs (COPE Health '
               'Solutions)',
      'url': 'https://www.youtube.com/watch?v=PDcTn9Sq3mg&t=1499s',
      'video_id': 'PDcTn9Sq3mg'},
     {'author': 'Veteran Career Center',
      'channel': 'Veteran Career Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=kAARyRvMAkI&t=71s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Qualifications there are some aspects that are better to have covered here are '
              'the reasons why you should submit data for the wotc.',
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': 'Qualifications there are some aspects that are better to have covered here are '
             'the reasons why you should submit data for the wotc.',
      'title': 'Pre-screen WOTC tax credit (Veteran Career Center)',
      'url': 'https://www.youtube.com/watch?v=kAARyRvMAkI&t=71s',
      'video_id': 'kAARyRvMAkI'},
     {'author': 'WKRN News 2',
      'channel': 'WKRN News 2',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=FI_QPEhBhEE&t=21s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'SO WHAT DOES THAT MEAN FOR MANUFACTURING WORKERS. THIS IS KELLY MILAN TRACKING '
              'THE ECONOMY AND SHARES MORE. TENNESSEE RANKS AMONG THE TOP 10 STATES AND AUTO '
              'PART EXPORTS WITH NEARLY 350,000 JOBS TIED TO MANUFACTURING.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'SO WHAT DOES THAT MEAN FOR MANUFACTURING WORKERS. THIS IS KELLY MILAN TRACKING '
             'THE ECONOMY AND SHARES MORE. TENNESSEE RANKS AMONG THE TOP 10 STATES AND AUTO '
             'PART EXPORTS WITH NEARLY 350,000 JOBS TIED TO MANUFACTURING.',
      'title': 'Tariffs disrupting manufacturing sector (WKRN News 2)',
      'url': 'https://www.youtube.com/watch?v=FI_QPEhBhEE&t=21s',
      'video_id': 'FI_QPEhBhEE'},
     {'author': 'Watchdog Advisory',
      'channel': 'Watchdog Advisory',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:02](https://www.youtube.com/watch?v=Joo1fuo4HkY&t=122s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Valuable to you and we certainly appreciate that we vow not to take up your '
              "time any documentation that we need that you don't have readily available will "
              'obtain from your providers and of course all information is held in the '
              'strictest confidence.',
      'timestamp': 122,
      'timestamp_label': '[00:02:02]',
      'timestamp_seconds': 122,
      'tip': 'Valuable to you and we certainly appreciate that we vow not to take up your time '
             "any documentation that we need that you don't have readily available will obtain "
             'from your providers and of course all information is held in the strictest '
             'confidence.',
      'title': 'Workers Comp Premium Recovery Audit (Watchdog Advisory)',
      'url': 'https://www.youtube.com/watch?v=Joo1fuo4HkY&t=122s',
      'video_id': 'Joo1fuo4HkY'},
     {'author': 'Refund Retriever',
      'channel': 'Refund Retriever',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:11](https://www.youtube.com/watch?v=j2T9_igpwQU&t=131s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Your rates to other similar size Ripper's and get you a better FedEx or UPS "
              'agreement so if you have any questions about your FedEx UPS agreement contact '
              'us at refund retriever 800 four four one eight zero eight five or email me '
              'brian at refund retriever.',
      'timestamp': 131,
      'timestamp_label': '[00:02:11]',
      'timestamp_seconds': 131,
      'tip': "Your rates to other similar size Ripper's and get you a better FedEx or UPS "
             'agreement so if you have any questions about your FedEx UPS agreement contact us '
             'at refund retriever 800 four four one eight zero eight five or email me brian at '
             'refund retriever.',
      'title': 'Parcel Contract Negotiation - 5 Tips (Refund Retriever)',
      'url': 'https://www.youtube.com/watch?v=j2T9_igpwQU&t=131s',
      'video_id': 'j2T9_igpwQU'}],
 9: [{'author': 'Refund Retriever',
      'channel': 'Refund Retriever',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:06](https://www.youtube.com/watch?v=tMWkXFE9a10&t=186s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re probably costing you more than you think. At Reef Retriever, we understand "
              'these contracts and can help shippers understand these contract terms and '
              'negotiate better deals, including minimum charge reductions. Give us a call at '
              '800441-8085 or visit refund retriever.',
      'timestamp': 186,
      'timestamp_label': '[00:03:06]',
      'timestamp_seconds': 186,
      'tip': "'re probably costing you more than you think. At Reef Retriever, we understand "
             'these contracts and can help shippers understand these contract terms and '
             'negotiate better deals, including minimum charge reductions. Give us a call at '
             '800441-8085 or visit refund retriever.',
      'title': 'FedEx Minimum Charges Explained - Contract Negotiation Preparation (Refund '
               'Retriever)',
      'url': 'https://www.youtube.com/watch?v=tMWkXFE9a10&t=186s',
      'video_id': 'tMWkXFE9a10'},
     {'author': 'McDivitt Law Firm',
      'channel': 'McDivitt Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:07](https://www.youtube.com/watch?v=61zkacizavY&t=247s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're not getting a bill for that phone call or that email. The third thing to "
              'understand about a contingency fee lawyer is at the end of the case, how that '
              'lawyer is paid and how you get your money.',
      'timestamp': 247,
      'timestamp_label': '[00:04:07]',
      'timestamp_seconds': 247,
      'tip': "You're not getting a bill for that phone call or that email. The third thing to "
             'understand about a contingency fee lawyer is at the end of the case, how that '
             'lawyer is paid and how you get your money.',
      'title': '3 Rules You Need to Know About Contingency Fees (No Win, No Pay!) (McDivitt '
               'Law Firm)',
      'url': 'https://www.youtube.com/watch?v=61zkacizavY&t=247s',
      'video_id': '61zkacizavY'},
     {'author': 'Mingle Health',
      'channel': 'Mingle Health',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:51](https://www.youtube.com/watch?v=rPy0GAiwUUc&t=1011s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'November 1st, uh, and then access the current state of the rules in the '
              'electronic code of federal regul regulations. Thank you for joining us today. '
              'Use the links here on the right to ask questions, correct my answers, '
              'contribute your experience and comments.',
      'timestamp': 1011,
      'timestamp_label': '[00:16:51]',
      'timestamp_seconds': 1011,
      'tip': 'November 1st, uh, and then access the current state of the rules in the '
             'electronic code of federal regul regulations. Thank you for joining us today. '
             'Use the links here on the right to ask questions, correct my answers, contribute '
             'your experience and comments.',
      'title': '2026 Proposed Rule: Medicare Shared Savings Program (MSSP) Proposals for 2026 '
               '| Ask Dr. Mingle (Mingle Health)',
      'url': 'https://www.youtube.com/watch?v=rPy0GAiwUUc&t=1011s',
      'video_id': 'rPy0GAiwUUc'},
     {'author': 'VA OSDBU (On Demand)',
      'channel': 'VA OSDBU (On Demand)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=onLA9L1sYIc&t=90s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Local organizations such as tax professional organizations, small business '
              'organizations, community organizations, as well as local state and federal '
              'government agencies to do tax education and outreach. For a little over four '
              'years cause I started, in March 2020.',
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': 'Local organizations such as tax professional organizations, small business '
             'organizations, community organizations, as well as local state and federal '
             'government agencies to do tax education and outreach. For a little over four '
             'years cause I started, in March 2020.',
      'title': 'Understanding the Work Opportunity Tax Credit (VA OSDBU (On Demand))',
      'url': 'https://www.youtube.com/watch?v=onLA9L1sYIc&t=90s',
      'video_id': 'onLA9L1sYIc'},
     {'author': 'Brach Eichler LLC',
      'channel': 'Brach Eichler LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:12](https://www.youtube.com/watch?v=F3SJ8TZqOns&t=132s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is intended to provide general information, not legal advice. Please '
              'contact the authors if you need specific legal advice. Brach Eichler LLC is a '
              'full service law firm based in Roseland, New Jersey with over eighty attorneys.',
      'timestamp': 132,
      'timestamp_label': '[00:02:12]',
      'timestamp_seconds': 132,
      'tip': 'This is intended to provide general information, not legal advice. Please '
             'contact the authors if you need specific legal advice. Brach Eichler LLC is a '
             'full service law firm based in Roseland, New Jersey with over eighty attorneys.',
      'title': 'NOW is the Time to Consider a Commercial Property Tax Appeal! (Brach Eichler '
               'LLC)',
      'url': 'https://www.youtube.com/watch?v=F3SJ8TZqOns&t=132s',
      'video_id': 'F3SJ8TZqOns'},
     {'author': 'Carr, Riggs & Ingram',
      'channel': 'Carr, Riggs & Ingram',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=HpOuVeLrWBs&t=55s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Typically state audits are going to be pro state and so the agents are not '
              'going to be considering pro taxpayer provisions of the law having a reverse.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'Typically state audits are going to be pro state and so the agents are not going '
             'to be considering pro taxpayer provisions of the law having a reverse.',
      'title': '4 Trigger Events That Might Help You "Find" Money Using a Reverse Audit (Carr, '
               'Riggs & Ingram)',
      'url': 'https://www.youtube.com/watch?v=HpOuVeLrWBs&t=55s',
      'video_id': 'HpOuVeLrWBs'},
     {'author': 'Quality Builders',
      'channel': 'Quality Builders',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:08](https://www.youtube.com/watch?v=tHXC3Ph5z0Q&t=1208s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They're applying the law incorrectly so there's a big difference um in terms of "
              'the alderman most of the Alman offices are trying to teach like a DIY.',
      'timestamp': 1208,
      'timestamp_label': '[00:20:08]',
      'timestamp_seconds': 1208,
      'tip': "They're applying the law incorrectly so there's a big difference um in terms of "
             'the alderman most of the Alman offices are trying to teach like a DIY.',
      'title': 'Q&A with a expert in Property Tax Law -  Chicago Property Tax Appeal (Quality '
               'Builders)',
      'url': 'https://www.youtube.com/watch?v=tHXC3Ph5z0Q&t=1208s',
      'video_id': 'tHXC3Ph5z0Q'},
     {'author': 'Jeb Smith',
      'channel': 'Jeb Smith',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:39](https://www.youtube.com/watch?v=HDpLh9uRXMo&t=639s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Actually do an inspection it just means that you can't use that inspection "
              'Andor in this case the appraisal to back out of the contract you have to use.',
      'timestamp': 639,
      'timestamp_label': '[00:10:39]',
      'timestamp_seconds': 639,
      'tip': "Actually do an inspection it just means that you can't use that inspection Andor "
             'in this case the appraisal to back out of the contract you have to use.',
      'title': 'How Contingencies Work When Buying A House (Jeb Smith)',
      'url': 'https://www.youtube.com/watch?v=HDpLh9uRXMo&t=639s',
      'video_id': 'HDpLh9uRXMo'},
     {'author': 'Karlton Dennis',
      'channel': 'Karlton Dennis',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:03](https://www.youtube.com/watch?v=NOA2tGOp9G8&t=123s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'CPA or a qualified tax advisor. This can be an enrolled agent or a CTEC, and '
              "then you're going to have an engineering firm or someone who has a license in "
              'engineering. These are the two people that are required by law to perform a '
              'cost segregation study.',
      'timestamp': 123,
      'timestamp_label': '[00:02:03]',
      'timestamp_seconds': 123,
      'tip': 'CPA or a qualified tax advisor. This can be an enrolled agent or a CTEC, and '
             "then you're going to have an engineering firm or someone who has a license in "
             'engineering. These are the two people that are required by law to perform a cost '
             'segregation study.',
      'title': 'Inside My Real Cost Segregation Study (What Actually Happened) (Karlton '
               'Dennis)',
      'url': 'https://www.youtube.com/watch?v=NOA2tGOp9G8&t=123s',
      'video_id': 'NOA2tGOp9G8'},
     {'author': 'Accounting Instruction, Help, & How To (Financial & Managerial)',
      'channel': 'Accounting Instruction, Help, & How To (Financial & Managerial)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:56](https://www.youtube.com/watch?v=INmKlA5mo2U&t=176s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Small business job protection act of 1996 the amount of the tax credit under '
              'the wotc equals a percentage of qualified wages paid in a given year to an '
              'employee certified by the dla as being a member of one of the groups specified '
              'in the law.',
      'timestamp': 176,
      'timestamp_label': '[00:02:56]',
      'timestamp_seconds': 176,
      'tip': 'Small business job protection act of 1996 the amount of the tax credit under the '
             'wotc equals a percentage of qualified wages paid in a given year to an employee '
             'certified by the dla as being a member of one of the groups specified in the '
             'law.',
      'title': 'IRS provides relief for certain employers claiming the Work Opportunity Tax '
               'Credit (Accounting Instruction, Help, & How To (Financial & Managerial))',
      'url': 'https://www.youtube.com/watch?v=INmKlA5mo2U&t=176s',
      'video_id': 'INmKlA5mo2U'},
     {'author': 'Route Consultant',
      'channel': 'Route Consultant',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=fd7XjYGTb8c&t=39s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "When you're at the end of your contract year and are negotiating a new contract "
              'new buyers may also negotiate a contract before they purchase a business if '
              'the.',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': "When you're at the end of your contract year and are negotiating a new contract "
             'new buyers may also negotiate a contract before they purchase a business if the.',
      'title': 'How Negotiations Work for FedEx Ground Contractors (Route Consultant)',
      'url': 'https://www.youtube.com/watch?v=fd7XjYGTb8c&t=39s',
      'video_id': 'fd7XjYGTb8c'},
     {'author': 'Share a Refund',
      'channel': 'Share a Refund',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:39](https://www.youtube.com/watch?v=eTB0fyueR5A&t=519s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Economical legal or supply chain recommendation made to any specific listener '
              'and receipt is not to be constituted as advice nor to constitute any such '
              'person a client or a customer do not copy or distribute in whole or in part '
              'thank.',
      'timestamp': 519,
      'timestamp_label': '[00:08:39]',
      'timestamp_seconds': 519,
      'tip': 'Economical legal or supply chain recommendation made to any specific listener '
             'and receipt is not to be constituted as advice nor to constitute any such person '
             'a client or a customer do not copy or distribute in whole or in part thank.',
      'title': 'Workflow of a good parcel audit (Share a Refund)',
      'url': 'https://www.youtube.com/watch?v=eTB0fyueR5A&t=519s',
      'video_id': 'eTB0fyueR5A'},
     {'author': 'Regenerative Shift',
      'channel': 'Regenerative Shift',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:33:58](https://www.youtube.com/watch?v=qYAmJlpkzAw&t=2038s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Baseline is LEDs whereas the 2007 assumes the Baseline is fluorescent and hence '
              "that's H why you see the uh 50 56% more efficient Baseline we go to the next.",
      'timestamp': 2038,
      'timestamp_label': '[00:33:58]',
      'timestamp_seconds': 2038,
      'tip': 'Baseline is LEDs whereas the 2007 assumes the Baseline is fluorescent and hence '
             "that's H why you see the uh 50 56% more efficient Baseline we go to the next.",
      'title': 'Inflation Reduction Act - 179D Energy Efficient Commercial Building Deduction '
               '- Webinar (Regenerative Shift)',
      'url': 'https://www.youtube.com/watch?v=qYAmJlpkzAw&t=2038s',
      'video_id': 'qYAmJlpkzAw'},
     {'author': 'Engineered Tax Services',
      'channel': 'Engineered Tax Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:22](https://www.youtube.com/watch?v=1NYU-FDekUs&t=202s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're curious about claiming the 179 deduction as there's a lot at stake if "
              "you'd like more information or to chat with a professional we'd be happy to "
              'help just head over to www.engineeredtaxservices.com.',
      'timestamp': 202,
      'timestamp_label': '[00:03:22]',
      'timestamp_seconds': 202,
      'tip': "You're curious about claiming the 179 deduction as there's a lot at stake if "
             "you'd like more information or to chat with a professional we'd be happy to help "
             'just head over to www.engineeredtaxservices.com.',
      'title': '179d Energy-Efficient Commercial Building Tax Deduction Updates (Engineered '
               'Tax Services)',
      'url': 'https://www.youtube.com/watch?v=1NYU-FDekUs&t=202s',
      'video_id': '1NYU-FDekUs'},
     {'author': 'Refund Retriever',
      'channel': 'Refund Retriever',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:44](https://www.youtube.com/watch?v=XPU680Aw1bg&t=224s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                   'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                   'commercial utility/waste/telecom tariff recoveries, property-tax '
                   'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '4418 85 thanks a lot thank you for joining us on the shippers toolbox if you '
              'have any questions visit our website refund retriever.com feel free to reach '
              'out to us 800 44188 for anything related to your FedEx or UPS and voices have a '
              'great day.',
      'timestamp': 224,
      'timestamp_label': '[00:03:44]',
      'timestamp_seconds': 224,
      'tip': '4418 85 thanks a lot thank you for joining us on the shippers toolbox if you '
             'have any questions visit our website refund retriever.com feel free to reach out '
             'to us 800 44188 for anything related to your FedEx or UPS and voices have a '
             'great day.',
      'title': 'UPS Additional Handling Charge: What you need to know (Refund Retriever)',
      'url': 'https://www.youtube.com/watch?v=XPU680Aw1bg&t=224s',
      'video_id': 'XPU680Aw1bg'}],
 10: [{'author': 'Shipware',
       'channel': 'Shipware',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:03](https://www.youtube.com/watch?v=rjelY0C_iQg&t=483s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Agreement put that information together and get to your carrier and say look '
               "I've learned that 30 of my shipments aren't getting the full discount I need "
               'to get a concession on my minimum charge.',
       'timestamp': 483,
       'timestamp_label': '[00:08:03]',
       'timestamp_seconds': 483,
       'tip': 'Agreement put that information together and get to your carrier and say look '
              "I've learned that 30 of my shipments aren't getting the full discount I need to "
              'get a concession on my minimum charge.',
       'title': 'UPS & FedEx Minimum Charges: What Do They Mean to Shippers? (Shipware)',
       'url': 'https://www.youtube.com/watch?v=rjelY0C_iQg&t=483s',
       'video_id': 'rjelY0C_iQg'},
      {'author': 'Daniel Burke',
       'channel': 'Daniel Burke',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:52](https://www.youtube.com/watch?v=4pb6YRGZx4s&t=1072s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "We'll also talk to you about how to think about building basic bill review "
               "skills internally versus bringing in a specialist on contingency. It's "
               'important if you do the audit, great.',
       'timestamp': 1072,
       'timestamp_label': '[00:17:52]',
       'timestamp_seconds': 1072,
       'tip': "We'll also talk to you about how to think about building basic bill review "
              "skills internally versus bringing in a specialist on contingency. It's "
              'important if you do the audit, great.',
       'title': 'Energy Decision #09 - Utility Bill Audits and Error Recovery | Energy Answers '
                'by TEG (Daniel Burke)',
       'url': 'https://www.youtube.com/watch?v=4pb6YRGZx4s&t=1072s',
       'video_id': '4pb6YRGZx4s'},
      {'author': 'Commercial Real Estate Escalations Made Simple',
       'channel': 'Commercial Real Estate Escalations Made Simple',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:30](https://www.youtube.com/watch?v=CWHu33HRBVY&t=150s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Check the link below to visit our website or visit us on LinkedIn. Next, we'll "
               'dive into gross up clauses and how they affect your CAM bill when a building '
               "isn't fully leased.",
       'timestamp': 150,
       'timestamp_label': '[00:02:30]',
       'timestamp_seconds': 150,
       'tip': "Check the link below to visit our website or visit us on LinkedIn. Next, we'll "
              'dive into gross up clauses and how they affect your CAM bill when a building '
              "isn't fully leased.",
       'title': 'CAM Reconciliations Explained (Commercial Real Estate Escalations Made '
                'Simple)',
       'url': 'https://www.youtube.com/watch?v=CWHu33HRBVY&t=150s',
       'video_id': 'CWHu33HRBVY'},
      {'author': 'Auditel, Inc. Telecom Expense Management',
       'channel': 'Auditel, Inc. Telecom Expense Management',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:32](https://www.youtube.com/watch?v=gIcFGhjFIKI&t=152s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Ahead of the competition we hope that after some consideration you'll agree "
               "that a telecom audit is definitely a worthwhile project and that you'll give "
               'us a call eight hundred four seven three five six five five thanks for your '
               'time thanks for watching.',
       'timestamp': 152,
       'timestamp_label': '[00:02:32]',
       'timestamp_seconds': 152,
       'tip': "Ahead of the competition we hope that after some consideration you'll agree "
              "that a telecom audit is definitely a worthwhile project and that you'll give us "
              'a call eight hundred four seven three five six five five thanks for your time '
              'thanks for watching.',
       'title': 'Technology Expense Management Why Have Telecom Bill Audit? Part 2 (Auditel, '
                'Inc. Telecom Expense Management)',
       'url': 'https://www.youtube.com/watch?v=gIcFGhjFIKI&t=152s',
       'video_id': 'gIcFGhjFIKI'},
      {'author': 'LJM',
       'channel': 'LJM',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:51:04](https://www.youtube.com/watch?v=56winzXYmPA&t=3064s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s one of the things that's sometimes ignored through AI where you know you "
               "read read about things and so forth and it's it's it sounds sexy like hey look "
               'just throw it through AI but at the re you know and like building an RFP is '
               'fantastic right?',
       'timestamp': 3064,
       'timestamp_label': '[00:51:04]',
       'timestamp_seconds': 3064,
       'tip': "'s one of the things that's sometimes ignored through AI where you know you "
              "read read about things and so forth and it's it's it sounds sexy like hey look "
              'just throw it through AI but at the re you know and like building an RFP is '
              'fantastic right?',
       'title': 'How to Negotiate Shipping Carrier Contracts for 2026 (LJM)',
       'url': 'https://www.youtube.com/watch?v=56winzXYmPA&t=3064s',
       'video_id': '56winzXYmPA'},
      {'author': 'UtilityBillAudits',
       'channel': 'UtilityBillAudits',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:20](https://www.youtube.com/watch?v=V-4ioYMhiuo&t=260s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Expect so for more information visit UB Engineering online at UB audit.com or '
               'call us at 80176 0699 to speak to a utility audit specialist who can answer '
               'any of your questions.',
       'timestamp': 260,
       'timestamp_label': '[00:04:20]',
       'timestamp_seconds': 260,
       'tip': 'Expect so for more information visit UB Engineering online at UB audit.com or '
              'call us at 80176 0699 to speak to a utility audit specialist who can answer any '
              'of your questions.',
       'title': 'Utility Bill Audit (UtilityBillAudits)',
       'url': 'https://www.youtube.com/watch?v=V-4ioYMhiuo&t=260s',
       'video_id': 'V-4ioYMhiuo'},
      {'author': 'Sales Tax Sisters',
       'channel': 'Sales Tax Sisters',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:19](https://www.youtube.com/watch?v=LibBgjGxja4&t=199s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And when you say desk audits you send it up to like audit headquarters and the '
               'person will call you up and say.',
       'timestamp': 199,
       'timestamp_label': '[00:03:19]',
       'timestamp_seconds': 199,
       'tip': 'And when you say desk audits you send it up to like audit headquarters and the '
              'person will call you up and say.',
       'title': 'Sales and Use tax refund requests- Manage your expectations (Sales Tax '
                'Sisters)',
       'url': 'https://www.youtube.com/watch?v=LibBgjGxja4&t=199s',
       'video_id': 'LibBgjGxja4'},
      {'author': 'Cerasis , now part of GlobalTranz',
       'channel': 'Cerasis , now part of GlobalTranz',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:41](https://www.youtube.com/watch?v=nGN0KikmdVk&t=41s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Therefore it is important shippers understand the top misconceptions of parcel '
               "auditing and how parcel audits can add up to big savings so let's talk parcel "
               'audit misconceptions.',
       'timestamp': 41,
       'timestamp_label': '[00:00:41]',
       'timestamp_seconds': 41,
       'tip': 'Therefore it is important shippers understand the top misconceptions of parcel '
              "auditing and how parcel audits can add up to big savings so let's talk parcel "
              'audit misconceptions.',
       'title': '7 Misconceptions of Parcel Audits (Cerasis , now part of GlobalTranz)',
       'url': 'https://www.youtube.com/watch?v=nGN0KikmdVk&t=41s',
       'video_id': 'nGN0KikmdVk'},
      {'author': 'Puleo Energy',
       'channel': 'Puleo Energy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:53](https://www.youtube.com/watch?v=a4dO2n1QfzQ&t=473s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'More than willing to uh walk through the agreement with you as well so thank '
               'you very much for your time and looking forward to speaking with you soon.',
       'timestamp': 473,
       'timestamp_label': '[00:07:53]',
       'timestamp_seconds': 473,
       'tip': 'More than willing to uh walk through the agreement with you as well so thank '
              'you very much for your time and looking forward to speaking with you soon.',
       'title': 'Overview: Utility Bill Audit (Puleo Energy)',
       'url': 'https://www.youtube.com/watch?v=a4dO2n1QfzQ&t=473s',
       'video_id': 'a4dO2n1QfzQ'},
      {'author': 'Eric Nelson',
       'channel': 'Eric Nelson',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:35](https://www.youtube.com/watch?v=APAYRO4lrsk&t=335s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Service how do we reach you well you can always call us 408 241 8700 and we '
               'have a website sscpa.com great thanks very much for being here I appreciate it '
               'all right thank you foreign.',
       'timestamp': 335,
       'timestamp_label': '[00:05:35]',
       'timestamp_seconds': 335,
       'tip': 'Service how do we reach you well you can always call us 408 241 8700 and we '
              'have a website sscpa.com great thanks very much for being here I appreciate it '
              'all right thank you foreign.',
       'title': 'Commercial Property Tax Appeals in CA - How to get it done! (Eric Nelson)',
       'url': 'https://www.youtube.com/watch?v=APAYRO4lrsk&t=335s',
       'video_id': 'APAYRO4lrsk'},
      {'author': 'Veritas Insurance Services & Risk Management',
       'channel': 'Veritas Insurance Services & Risk Management',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:23](https://www.youtube.com/watch?v=9kzq5Jf3Bpk&t=23s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "What it is it's a work opportunity tax credit is what watsi stands for um "
               "right now it's going to give a huge opportunity for business owners to be.",
       'timestamp': 23,
       'timestamp_label': '[00:00:23]',
       'timestamp_seconds': 23,
       'tip': "What it is it's a work opportunity tax credit is what watsi stands for um right "
              "now it's going to give a huge opportunity for business owners to be.",
       'title': 'Work Opportunity Tax Credit (WOTC) Explained (Veritas Insurance Services & '
                'Risk Management)',
       'url': 'https://www.youtube.com/watch?v=9kzq5Jf3Bpk&t=23s',
       'video_id': '9kzq5Jf3Bpk'},
      {'author': 'Professional Workshops Inc.',
       'channel': 'Professional Workshops Inc.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:02](https://www.youtube.com/watch?v=loBLG0SW_90&t=122s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A useful reminder catchall section for a bunch of things that we need to do in '
               "the audit that sort of aren't specifically called for in a section in "
               'Professional Standards but are called for perhaps in many sections so thanks '
               'for listening.',
       'timestamp': 122,
       'timestamp_label': '[00:02:02]',
       'timestamp_seconds': 122,
       'tip': 'A useful reminder catchall section for a bunch of things that we need to do in '
              "the audit that sort of aren't specifically called for in a section in "
              'Professional Standards but are called for perhaps in many sections so thanks '
              'for listening.',
       'title': 'Contingencies (Professional Workshops Inc.)',
       'url': 'https://www.youtube.com/watch?v=loBLG0SW_90&t=122s',
       'video_id': 'loBLG0SW_90'},
      {'author': 'CT Logistics',
       'channel': 'CT Logistics',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:34](https://www.youtube.com/watch?v=35fjaKeQp-I&t=214s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Services capabilities and ro is on our services year after year after year to '
               'our clients all right great information thank you so much for being with us '
               "today thank you I've been speaking with Alan minor of CT logistics thanks for "
               'watching.',
       'timestamp': 214,
       'timestamp_label': '[00:03:34]',
       'timestamp_seconds': 214,
       'tip': 'Services capabilities and ro is on our services year after year after year to '
              'our clients all right great information thank you so much for being with us '
              "today thank you I've been speaking with Alan minor of CT logistics thanks for "
              'watching.',
       'title': 'CT Logistics Freight Bill Audit and Payment (CT Logistics)',
       'url': 'https://www.youtube.com/watch?v=35fjaKeQp-I&t=214s',
       'video_id': '35fjaKeQp-I'},
      {'author': 'C2 Realty Group',
       'channel': 'C2 Realty Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:42](https://www.youtube.com/watch?v=dCExXUUA6zA&t=162s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "22428 you can expect a taxable income of 9,38 now if you're a real estate "
               'professional by the guidelines of the IRS you can take this $9,000 loss and '
               'apply to your other income giving you a paper loss and reducing your overall '
               'tax liability.',
       'timestamp': 162,
       'timestamp_label': '[00:02:42]',
       'timestamp_seconds': 162,
       'tip': "22428 you can expect a taxable income of 9,38 now if you're a real estate "
              'professional by the guidelines of the IRS you can take this $9,000 loss and '
              'apply to your other income giving you a paper loss and reducing your overall '
              'tax liability.',
       'title': 'Real Estate Cost Segregation Example (C2 Realty Group)',
       'url': 'https://www.youtube.com/watch?v=dCExXUUA6zA&t=162s',
       'video_id': 'dCExXUUA6zA'},
      {'author': 'Refund Retriever',
       'channel': 'Refund Retriever',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:52](https://www.youtube.com/watch?v=EsbQUsT8hWs&t=532s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Our website refund retriever com feel free to reach out to us eight hundred '
               'four four one eight zero eight five four anything related to your FedEx or UPS '
               'invoices have a great day.',
       'timestamp': 532,
       'timestamp_label': '[00:08:52]',
       'timestamp_seconds': 532,
       'tip': 'Our website refund retriever com feel free to reach out to us eight hundred '
              'four four one eight zero eight five four anything related to your FedEx or UPS '
              'invoices have a great day.',
       'title': 'FedEx and UPS Shipping Contract Negotiations - Your Checklist (Refund '
                'Retriever)',
       'url': 'https://www.youtube.com/watch?v=EsbQUsT8hWs&t=532s',
       'video_id': 'EsbQUsT8hWs'}],
 11: [{'author': 'Official ReadyATS',
       'channel': 'Official ReadyATS',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:02](https://www.youtube.com/watch?v=KqRldQ_XlyA&t=542s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So what features does it have that would appeal to a busy restaurant manager '
               'trying to hire quickly? It hits the key pressure points. Things like uh easy '
               'job posting. It pushes your openings out to places like glass door. Really '
               'strong candidate management tools.',
       'timestamp': 542,
       'timestamp_label': '[00:09:02]',
       'timestamp_seconds': 542,
       'tip': 'So what features does it have that would appeal to a busy restaurant manager '
              'trying to hire quickly? It hits the key pressure points. Things like uh easy '
              'job posting. It pushes your openings out to places like glass door. Really '
              'strong candidate management tools.',
       'title': "ATS Podcast #2: Don't Leave Money on the Table: The $9,600 Hiring Secret "
                'Restaurants Are Missing (Official ReadyATS)',
       'url': 'https://www.youtube.com/watch?v=KqRldQ_XlyA&t=542s',
       'video_id': 'KqRldQ_XlyA'},
      {'author': 'Workstream',
       'channel': 'Workstream',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:20:45](https://www.youtube.com/watch?v=3hIbQPQR66Y&t=1245s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So this just goes to the misconception again that WOTC is really available for '
               'hiring like veterans and ex-felons which is not the case. WOTC credits are '
               'only available upon hire though no ongoing credits if you continue to employ '
               'the person in subsequent years.',
       'timestamp': 1245,
       'timestamp_label': '[00:20:45]',
       'timestamp_seconds': 1245,
       'tip': 'So this just goes to the misconception again that WOTC is really available for '
              'hiring like veterans and ex-felons which is not the case. WOTC credits are only '
              'available upon hire though no ongoing credits if you continue to employ the '
              'person in subsequent years.',
       'title': 'How To Claim Up To $9,600 In Tax Credits Per Hire - A Work Opportunity Tax '
                'Credit Webinar (Workstream)',
       'url': 'https://www.youtube.com/watch?v=3hIbQPQR66Y&t=1245s',
       'video_id': '3hIbQPQR66Y'},
      {'author': 'GavTax Advisory Services',
       'channel': 'GavTax Advisory Services',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:43](https://www.youtube.com/watch?v=jNwzCbQub20&t=403s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Houston and Texas to integrate these strategies into their business models. '
               'Our team models after tax returns, coordinates cost segregation studies, '
               'manages depreciation schedules, and helps ensure your documentation can stand '
               'up under audit.',
       'timestamp': 403,
       'timestamp_label': '[00:06:43]',
       'timestamp_seconds': 403,
       'tip': 'Houston and Texas to integrate these strategies into their business models. Our '
              'team models after tax returns, coordinates cost segregation studies, manages '
              'depreciation schedules, and helps ensure your documentation can stand up under '
              'audit.',
       'title': 'Bonus Depreciation & Cost Segregation Explained (2025–26): Save THOUSANDS in '
                'Real Estate Taxes! 💸 (GavTax Advisory Services)',
       'url': 'https://www.youtube.com/watch?v=jNwzCbQub20&t=403s',
       'video_id': 'jNwzCbQub20'},
      {'author': 'Refund Retriever',
       'channel': 'Refund Retriever',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:34](https://www.youtube.com/watch?v=wDr_1xPxOXA&t=94s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Quantify each proposed agreement In a successful parcel negotiation process, '
               'you will receive multiple pricing proposals from each carrier. It is essential '
               'to thoroughly examine every proposal to determine the real impact on your '
               'operations and spending.',
       'timestamp': 94,
       'timestamp_label': '[00:01:34]',
       'timestamp_seconds': 94,
       'tip': 'Quantify each proposed agreement In a successful parcel negotiation process, '
              'you will receive multiple pricing proposals from each carrier. It is essential '
              'to thoroughly examine every proposal to determine the real impact on your '
              'operations and spending.',
       'title': 'Tips for Carrier Contract Negotiation (PART 2) (Refund Retriever)',
       'url': 'https://www.youtube.com/watch?v=wDr_1xPxOXA&t=94s',
       'video_id': 'wDr_1xPxOXA'},
      {'author': 'Eide Bailly',
       'channel': 'Eide Bailly',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:35](https://www.youtube.com/watch?v=OfVPZqJ7nxY&t=155s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Bailey's team of construction specialists can help you every step of the way "
               "to claim if you've recently constructed 50,000 square foot building are a "
               "governmental facility please contact ID Bailey and we'd be happy to help you "
               'claim the 179 deduction.',
       'timestamp': 155,
       'timestamp_label': '[00:02:35]',
       'timestamp_seconds': 155,
       'tip': "Bailey's team of construction specialists can help you every step of the way to "
              "claim if you've recently constructed 50,000 square foot building are a "
              "governmental facility please contact ID Bailey and we'd be happy to help you "
              'claim the 179 deduction.',
       'title': 'Energy Efficiency Deduction: Taking Advantage of Section 179D (Eide Bailly)',
       'url': 'https://www.youtube.com/watch?v=OfVPZqJ7nxY&t=155s',
       'video_id': 'OfVPZqJ7nxY'},
      {'author': 'Compete Consulting Group',
       'channel': 'Compete Consulting Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:12](https://www.youtube.com/watch?v=RCPFFZVF7qs&t=132s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Group you'll be able to keep your money right where it belongs with you call "
               'the team at compete Consulting Group and claim back your refunds today one '
               'eight seven seven four two one four nine nine four or email info at compete '
               'consulting dotnet.',
       'timestamp': 132,
       'timestamp_label': '[00:02:12]',
       'timestamp_seconds': 132,
       'tip': "Group you'll be able to keep your money right where it belongs with you call "
              'the team at compete Consulting Group and claim back your refunds today one '
              'eight seven seven four two one four nine nine four or email info at compete '
              'consulting dotnet.',
       'title': 'Understanding Shipping Invoicing | Invoice Auditing Service | Compete '
                'Consulting Group (Compete Consulting Group)',
       'url': 'https://www.youtube.com/watch?v=RCPFFZVF7qs&t=132s',
       'video_id': 'RCPFFZVF7qs'},
      {'author': 'Cross the River, Find the Treasure',
       'channel': 'Cross the River, Find the Treasure',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:58](https://www.youtube.com/watch?v=7CfK4x3Fijc&t=58s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The method for establishing the valuation of a business is based on an income '
               'approach businesses are valued by the income they earn.',
       'timestamp': 58,
       'timestamp_label': '[00:00:58]',
       'timestamp_seconds': 58,
       'tip': 'The method for establishing the valuation of a business is based on an income '
              'approach businesses are valued by the income they earn.',
       'title': 'Commercial Business Property Tax Appeal (Cross the River, Find the Treasure)',
       'url': 'https://www.youtube.com/watch?v=7CfK4x3Fijc&t=58s',
       'video_id': '7CfK4x3Fijc'},
      {'author': 'Gift CPAs',
       'channel': 'Gift CPAs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:46](https://www.youtube.com/watch?v=RzWkA9XcT7g&t=46s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Hiring for many other state agencies you have a list of people that you can '
               'hire from in this scenario you do the hiring and then finally the US economy '
               'benefits.',
       'timestamp': 46,
       'timestamp_label': '[00:00:46]',
       'timestamp_seconds': 46,
       'tip': 'Hiring for many other state agencies you have a list of people that you can '
              'hire from in this scenario you do the hiring and then finally the US economy '
              'benefits.',
       'title': 'Work Opportunity Tax Credit Presentation (Gift CPAs)',
       'url': 'https://www.youtube.com/watch?v=RzWkA9XcT7g&t=46s',
       'video_id': 'RzWkA9XcT7g'},
      {'author': 'DCI Solutions - Cost & Tax Credit Specialists',
       'channel': 'DCI Solutions - Cost & Tax Credit Specialists',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=THfq9yETSTo&t=20s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': '2,400 to $9,600 for hiring that particular employee. It typically works best '
               'if you have at least 50 new hires, and if you do, you might be looking at '
               '25,000 or more dollars in federal tax savings. So, you have to hire people '
               'that are eligible.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': '2,400 to $9,600 for hiring that particular employee. It typically works best if '
              'you have at least 50 new hires, and if you do, you might be looking at 25,000 '
              'or more dollars in federal tax savings. So, you have to hire people that are '
              'eligible.',
       'title': 'Reducing Costs Using the WOTC Tax Credit (DCI Solutions - Cost & Tax Credit '
                'Specialists)',
       'url': 'https://www.youtube.com/watch?v=THfq9yETSTo&t=20s',
       'video_id': 'THfq9yETSTo'},
      {'author': 'Linked Accounting, LLP',
       'channel': 'Linked Accounting, LLP',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:34](https://www.youtube.com/watch?v=yEWXbR-V5qs&t=34s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Circumstances our solution is simple during the hiring process a questionnaire '
               'is completed by the new hire within 30 days of their higher date.',
       'timestamp': 34,
       'timestamp_label': '[00:00:34]',
       'timestamp_seconds': 34,
       'tip': 'Circumstances our solution is simple during the hiring process a questionnaire '
              'is completed by the new hire within 30 days of their higher date.',
       'title': 'The Work Opportunity Tax Credit (Linked Accounting, LLP)',
       'url': 'https://www.youtube.com/watch?v=yEWXbR-V5qs&t=34s',
       'video_id': 'yEWXbR-V5qs'},
      {'author': 'Biz-Reps',
       'channel': 'Biz-Reps',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:09](https://www.youtube.com/watch?v=sY8onoIne8Q&t=489s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Click through the description in this video to schedule an appointment with my '
               'team so that we can show you what you need to do to take advantage incentives '
               "thank you we'll see you next time.",
       'timestamp': 489,
       'timestamp_label': '[00:08:09]',
       'timestamp_seconds': 489,
       'tip': 'Click through the description in this video to schedule an appointment with my '
              'team so that we can show you what you need to do to take advantage incentives '
              "thank you we'll see you next time.",
       'title': 'How to Get the 179D Commercial Buildings Energy-Efficiency Tax Deduction '
                '(Biz-Reps)',
       'url': 'https://www.youtube.com/watch?v=sY8onoIne8Q&t=489s',
       'video_id': 'sY8onoIne8Q'},
      {'author': 'Steve Payerle',
       'channel': 'Steve Payerle',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:56](https://www.youtube.com/watch?v=7JAkJdSWJd4&t=296s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Businesses that are uncertain about their Tech costs or you know want sure '
               "they're maximizing their it Investments um you know reach out to us uh "
               "together between my team and Jim's team we can navigate you to Greater "
               'efficiencies and savings.',
       'timestamp': 296,
       'timestamp_label': '[00:04:56]',
       'timestamp_seconds': 296,
       'tip': 'Businesses that are uncertain about their Tech costs or you know want sure '
              "they're maximizing their it Investments um you know reach out to us uh together "
              "between my team and Jim's team we can navigate you to Greater efficiencies and "
              'savings.',
       'title': 'Next Level Technologies and Schooley Mitchell (Steve Payerle)',
       'url': 'https://www.youtube.com/watch?v=7JAkJdSWJd4&t=296s',
       'video_id': '7JAkJdSWJd4'},
      {'author': 'AtlantaxSystems',
       'channel': 'AtlantaxSystems',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:56](https://www.youtube.com/watch?v=v9ZkvElAVE4&t=116s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Resources that came with our team of dedicated tax professionals and services '
               'has delivered upon the strength of a responsive personal service unmatched in '
               "our industry she found out that Atlant tax is large enough to serve it's small "
               'enough to care.',
       'timestamp': 116,
       'timestamp_label': '[00:01:56]',
       'timestamp_seconds': 116,
       'tip': 'Resources that came with our team of dedicated tax professionals and services '
              'has delivered upon the strength of a responsive personal service unmatched in '
              "our industry she found out that Atlant tax is large enough to serve it's small "
              'enough to care.',
       'title': 'Atlantax Systems - Outsourcing Sales and Use Tax Compliance - Tax Rating - '
                'Reverse Audits (AtlantaxSystems)',
       'url': 'https://www.youtube.com/watch?v=v9ZkvElAVE4&t=116s',
       'video_id': 'v9ZkvElAVE4'},
      {'author': 'Accounting Instruction, Help, & How To (Financial & Managerial)',
       'channel': 'Accounting Instruction, Help, & How To (Financial & Managerial)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:15](https://www.youtube.com/watch?v=WLD-qzEGnIg&t=375s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Qualified employees so there's links to some of this information here if you "
               "want to check it out in more detail there'll be a link to this in the "
               'description.',
       'timestamp': 375,
       'timestamp_label': '[00:06:15]',
       'timestamp_seconds': 375,
       'tip': "Qualified employees so there's links to some of this information here if you "
              "want to check it out in more detail there'll be a link to this in the "
              'description.',
       'title': 'Help wanted? Businesses that are hiring should know about the work '
                'opportunity tax credit (Accounting Instruction, Help, & How To (Financial & '
                'Managerial))',
       'url': 'https://www.youtube.com/watch?v=WLD-qzEGnIg&t=375s',
       'video_id': 'WLD-qzEGnIg'},
      {'author': 'LateShipment',
       'channel': 'LateShipment',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:00](https://www.youtube.com/watch?v=WvGPHvucRD0&t=120s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Intelligent audit is eighth. Best known for pairing invoice auditing with '
               "contract optimization, so you're not just recovering refunds, but building "
               'stronger carrier agreements over time.',
       'timestamp': 120,
       'timestamp_label': '[00:02:00]',
       'timestamp_seconds': 120,
       'tip': 'Intelligent audit is eighth. Best known for pairing invoice auditing with '
              "contract optimization, so you're not just recovering refunds, but building "
              'stronger carrier agreements over time.',
       'title': 'Top 10 Parcel Audit Software Solutions for E-Commerce (LateShipment)',
       'url': 'https://www.youtube.com/watch?v=WvGPHvucRD0&t=120s',
       'video_id': 'WvGPHvucRD0'}],
 12: [{'author': 'Fenton Tax Help',
       'channel': 'Fenton Tax Help',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:32](https://www.youtube.com/watch?v=3iHBB7snmho&t=512s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Submit form 8850 within 28 days of the new hire start date. Three, receive '
               'certification. Your state agency reviews the application and confirms if the '
               'employee qualifies. File form 5884 with your tax return. If you miss that '
               '28-day deadline, you lose the credit.',
       'timestamp': 512,
       'timestamp_label': '[00:08:32]',
       'timestamp_seconds': 512,
       'tip': 'Submit form 8850 within 28 days of the new hire start date. Three, receive '
              'certification. Your state agency reviews the application and confirms if the '
              'employee qualifies. File form 5884 with your tax return. If you miss that '
              '28-day deadline, you lose the credit.',
       'title': 'The Work Opportunity Tax Credit Is Ending  Here is H (Fenton Tax Help)',
       'url': 'https://www.youtube.com/watch?v=3iHBB7snmho&t=512s',
       'video_id': '3iHBB7snmho'},
      {'author': 'Refund Retriever',
       'channel': 'Refund Retriever',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:59](https://www.youtube.com/watch?v=vOX4irOA_Tk&t=359s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Parcel audit or whatever people call it these days because there's so many "
               'different names you know give us a call eight hundred four four one eight zero '
               'eight five or shoot me an email Brian at refund retriever hope you guys have a '
               'great day thanks for listening.',
       'timestamp': 359,
       'timestamp_label': '[00:05:59]',
       'timestamp_seconds': 359,
       'tip': "Parcel audit or whatever people call it these days because there's so many "
              'different names you know give us a call eight hundred four four one eight zero '
              'eight five or shoot me an email Brian at refund retriever hope you guys have a '
              'great day thanks for listening.',
       'title': 'Importance of Small Parcel Auditing (Refund Retriever)',
       'url': 'https://www.youtube.com/watch?v=vOX4irOA_Tk&t=359s',
       'video_id': 'vOX4irOA_Tk'},
      {'author': 'Ergon Energy',
       'channel': 'Ergon Energy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:20](https://www.youtube.com/watch?v=ArxvRqneZ_c&t=80s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The highest reading over the month will be used to calculate the monthly '
               'demand charge. So, the more appliances you run during the same half hour block '
               "between 4pm and 9pm each day, the higher your demand charge will be. That's "
               'where you can make a difference.',
       'timestamp': 80,
       'timestamp_label': '[00:01:20]',
       'timestamp_seconds': 80,
       'tip': 'The highest reading over the month will be used to calculate the monthly demand '
              'charge. So, the more appliances you run during the same half hour block between '
              "4pm and 9pm each day, the higher your demand charge will be. That's where you "
              'can make a difference.',
       'title': 'Demand tariffs explained (Ergon Energy)',
       'url': 'https://www.youtube.com/watch?v=ArxvRqneZ_c&t=80s',
       'video_id': 'ArxvRqneZ_c'},
      {'author': 'OEO Energy Solutions',
       'channel': 'OEO Energy Solutions',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:26](https://www.youtube.com/watch?v=vxnBn-sUk98&t=86s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Everything on the invoices I've seen us cut bills by 40% and we can come in "
               "and really save the day on the audit that's the other reason why we try to get "
               'all.',
       'timestamp': 86,
       'timestamp_label': '[00:01:26]',
       'timestamp_seconds': 86,
       'tip': "Everything on the invoices I've seen us cut bills by 40% and we can come in and "
              "really save the day on the audit that's the other reason why we try to get all.",
       'title': 'FREE Utility Bill Audit — Are You Being Overcharged? (OEO Energy Solutions)',
       'url': 'https://www.youtube.com/watch?v=vxnBn-sUk98&t=86s',
       'video_id': 'vxnBn-sUk98'},
      {'author': 'Everything Architecture',
       'channel': 'Everything Architecture',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:44](https://www.youtube.com/watch?v=4v8s8Jhhtt0&t=104s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'During a waste audit, you literally need to collect every bin, every waste bin '
               'in your uh facility. Weigh it to understand how much of each type we have to '
               "start with. So, where we understand it's going at the moment.",
       'timestamp': 104,
       'timestamp_label': '[00:01:44]',
       'timestamp_seconds': 104,
       'tip': 'During a waste audit, you literally need to collect every bin, every waste bin '
              'in your uh facility. Weigh it to understand how much of each type we have to '
              "start with. So, where we understand it's going at the moment.",
       'title': 'How a Waste Audit Can Help Your Business (Everything Architecture)',
       'url': 'https://www.youtube.com/watch?v=4v8s8Jhhtt0&t=104s',
       'video_id': '4v8s8Jhhtt0'},
      {'author': 'IATF 16949 Auditing',
       'channel': 'IATF 16949 Auditing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:06](https://www.youtube.com/watch?v=tVupXEamHUk&t=66s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So first of all, let me um explain that the contingency plan is managed at '
               'both level plant level and corporate level. So the corporate level is the one '
               'that is then uh directly having contact with the customer in case of '
               'disruption.',
       'timestamp': 66,
       'timestamp_label': '[00:01:06]',
       'timestamp_seconds': 66,
       'tip': 'So first of all, let me um explain that the contingency plan is managed at both '
              'level plant level and corporate level. So the corporate level is the one that '
              'is then uh directly having contact with the customer in case of disruption.',
       'title': 'Auditing Contingency Planning (IATF 16949 Auditing)',
       'url': 'https://www.youtube.com/watch?v=tVupXEamHUk&t=66s',
       'video_id': 'tVupXEamHUk'},
      {'author': 'LawFull',
       'channel': 'LawFull',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:58](https://www.youtube.com/watch?v=IpoCPaop2Ds&t=358s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Why you should appeal as a group it's because at the end of the day what the "
               "cook what the county is going to look at is they're going to try to come up "
               'with.',
       'timestamp': 358,
       'timestamp_label': '[00:05:58]',
       'timestamp_seconds': 358,
       'tip': "Why you should appeal as a group it's because at the end of the day what the "
              "cook what the county is going to look at is they're going to try to come up "
              'with.',
       'title': 'Commercial property tax appeals (LawFull)',
       'url': 'https://www.youtube.com/watch?v=IpoCPaop2Ds&t=358s',
       'video_id': 'IpoCPaop2Ds'},
      {'author': 'TGG Accounting',
       'channel': 'TGG Accounting',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=DBpv31eMcBA&t=15s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "One tip a week that's going to help drive profitability into your business and "
               'this week we are going to talk about one of the myriad of different.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': "One tip a week that's going to help drive profitability into your business and "
              'this week we are going to talk about one of the myriad of different.',
       'title': 'What You Need to Know About the Work Opportunity Tax Credit (TGG Accounting)',
       'url': 'https://www.youtube.com/watch?v=DBpv31eMcBA&t=15s',
       'video_id': 'DBpv31eMcBA'},
      {'author': 'S3 Stores',
       'channel': 'S3 Stores',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:42](https://www.youtube.com/watch?v=q9kvSNRcgfs&t=102s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'FedEx would just uh take many large empty boxes and ship them by UPS 3day '
               'select like from all different locations, UPS locations. And in this case '
               'within 3 days uh the work of UPS will be paralyzed.',
       'timestamp': 102,
       'timestamp_label': '[00:01:42]',
       'timestamp_seconds': 102,
       'tip': 'FedEx would just uh take many large empty boxes and ship them by UPS 3day '
              'select like from all different locations, UPS locations. And in this case '
              'within 3 days uh the work of UPS will be paralyzed.',
       'title': 'How UPS and FedEx Dimensional Weight Works? (S3 Stores)',
       'url': 'https://www.youtube.com/watch?v=q9kvSNRcgfs&t=102s',
       'video_id': 'q9kvSNRcgfs'},
      {'author': 'Rob Freeman | Insuring The Built Environment',
       'channel': 'Rob Freeman | Insuring The Built Environment',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:19](https://www.youtube.com/watch?v=5s_6i2zdXo8&t=319s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Have questions about your insurance or anything related to Green buildings '
               'feel free to schedule an appointment with me the link below this video or you '
               'can just go to Rob freeman.com thanks for watching and have a great day.',
       'timestamp': 319,
       'timestamp_label': '[00:05:19]',
       'timestamp_seconds': 319,
       'tip': 'Have questions about your insurance or anything related to Green buildings feel '
              'free to schedule an appointment with me the link below this video or you can '
              'just go to Rob freeman.com thanks for watching and have a great day.',
       'title': 'How Does Section 179d (aka the "Green Building Tax Deduction") Work? (Rob '
                'Freeman | Insuring The Built Environment)',
       'url': 'https://www.youtube.com/watch?v=5s_6i2zdXo8&t=319s',
       'video_id': '5s_6i2zdXo8'},
      {'author': 'The TLC Companies',
       'channel': 'The TLC Companies',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:16](https://www.youtube.com/watch?v=kuYWnLG5-A4&t=256s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Could be a tax corporate tax reduction when they call it a pass-through it '
               "could actually go on to your owner's personal returns so in your helpful in "
               'here um this is actually through the Department of Labor 20 of eligible '
               'employees might be eligible for this credit.',
       'timestamp': 256,
       'timestamp_label': '[00:04:16]',
       'timestamp_seconds': 256,
       'tip': 'Could be a tax corporate tax reduction when they call it a pass-through it '
              "could actually go on to your owner's personal returns so in your helpful in "
              'here um this is actually through the Department of Labor 20 of eligible '
              'employees might be eligible for this credit.',
       'title': 'Work Opportunity Tax Credit - Webinar with WOTC.com (The TLC Companies)',
       'url': 'https://www.youtube.com/watch?v=kuYWnLG5-A4&t=256s',
       'video_id': 'kuYWnLG5-A4'},
      {'author': 'The Wealthy Accountant',
       'channel': 'The Wealthy Accountant',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:06](https://www.youtube.com/watch?v=XhVfWjlDk3w&t=306s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Actually by the month so you will actually have to make an adjustment by the '
               'month versus the year and that will be uh.',
       'timestamp': 306,
       'timestamp_label': '[00:05:06]',
       'timestamp_seconds': 306,
       'tip': 'Actually by the month so you will actually have to make an adjustment by the '
              'month versus the year and that will be uh.',
       'title': 'Cost Segregation: Form 3115 and Depreciation Adjustments (The Wealthy '
                'Accountant)',
       'url': 'https://www.youtube.com/watch?v=XhVfWjlDk3w&t=306s',
       'video_id': 'XhVfWjlDk3w'},
      {'author': 'MP: Wired for HR',
       'channel': 'MP: Wired for HR',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:53](https://www.youtube.com/watch?v=tAf8rI1hwtc&t=1013s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Within the last month this isn't a program where you're going to be able to go "
               'back like say with ertc or something and retroactively claim the credits for '
               'people that you hired you know over the last couple years this is really a '
               'moving forward type tax credit program.',
       'timestamp': 1013,
       'timestamp_label': '[00:16:53]',
       'timestamp_seconds': 1013,
       'tip': "Within the last month this isn't a program where you're going to be able to go "
              'back like say with ertc or something and retroactively claim the credits for '
              'people that you hired you know over the last couple years this is really a '
              'moving forward type tax credit program.',
       'title': 'Work Opportunity Tax Credit (WOTC): Eligibility, Proven Strategies, and Best '
                'Practices (MP: Wired for HR)',
       'url': 'https://www.youtube.com/watch?v=tAf8rI1hwtc&t=1013s',
       'video_id': 'tAf8rI1hwtc'},
      {'author': 'Lojistic',
       'channel': 'Lojistic',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:07](https://www.youtube.com/watch?v=5yyeqQ4VAFU&t=127s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Your money of course that's easier said than done keep in mind that the cruit "
               "logistic is more than happy to help we do it for a living and we think we're "
               "super good at it in the meantime Odyssey use it it'll for sure help you send "
               'cost.',
       'timestamp': 127,
       'timestamp_label': '[00:02:07]',
       'timestamp_seconds': 127,
       'tip': "Your money of course that's easier said than done keep in mind that the cruit "
              "logistic is more than happy to help we do it for a living and we think we're "
              "super good at it in the meantime Odyssey use it it'll for sure help you send "
              'cost.',
       'title': 'Audisee Tutorial (Lojistic)',
       'url': 'https://www.youtube.com/watch?v=5yyeqQ4VAFU&t=127s',
       'video_id': '5yyeqQ4VAFU'},
      {'author': 'USA Senior Laws Guide',
       'channel': 'USA Senior Laws Guide',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=LopTSxbolHY&t=20s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–50%` contingency '
                    'corporate expense auditing across `FedEx`/`UPS` parcel refund APIs, '
                    'commercial utility/waste/telecom tariff recoveries, property-tax '
                    'assessment appeals, and `WOTC`/specialty tax-credit splits (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'It is called a property tax appeal. It is your legal right as a homeowner. The '
               'county does not advertise it. Your assessor will not call you to remind you, '
               'and the deadlines to file are short, often only 30 to 60 days from the date '
               'you receive your assessment notice.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'It is called a property tax appeal. It is your legal right as a homeowner. The '
              'county does not advertise it. Your assessor will not call you to remind you, '
              'and the deadlines to file are short, often only 30 to 60 days from the date you '
              'receive your assessment notice.',
       'title': 'How to Appeal Your 2026 Property Tax Assessment — The Step by Step Process '
                'Most Seniors Never Use (USA Senior Laws Guide)',
       'url': 'https://www.youtube.com/watch?v=LopTSxbolHY&t=20s',
       'video_id': 'LopTSxbolHY'}]}
