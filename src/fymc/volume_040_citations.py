"""Curated 180-citation Self-Funded Health, PBM & Workers' Comp Arbitrage baseline (15 per chapter across Q1-Q12) mined strictly from verified Self-Funded Health, PBM & Workers' Comp Arbitrage YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'202',
     '2021',
     '400k',
     '500',
     '500k',
     '5500',
     'act',
     'administrator',
     'advisor',
     'advisory',
     'agency',
     'aggregate',
     'analytics',
     'appropriations',
     'architecture',
     'audit',
     'auditing',
     'balance',
     'based',
     'beating',
     'become',
     'benefit',
     'benefits',
     'billing',
     'book',
     'bor',
     'broker',
     'brokers',
     'buca',
     'building',
     'business',
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
 2: {'202',
     '2021',
     '400k',
     '500',
     '500k',
     '5500',
     'act',
     'administrator',
     'advisor',
     'advisory',
     'agency',
     'aggregate',
     'analytics',
     'appropriations',
     'architecture',
     'audit',
     'auditing',
     'balance',
     'based',
     'beating',
     'become',
     'benefit',
     'benefits',
     'billing',
     'book',
     'bor',
     'broker',
     'brokers',
     'buca',
     'budget',
     'building',
     'buyer',
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
 3: {'202',
     '2021',
     '400k',
     '500',
     '500k',
     '5500',
     'act',
     'administrator',
     'advisor',
     'advisory',
     'agency',
     'aggregate',
     'analytics',
     'appropriations',
     'architecture',
     'audit',
     'auditing',
     'balance',
     'based',
     'beating',
     'become',
     'benefit',
     'benefits',
     'billing',
     'book',
     'bor',
     'broker',
     'brokers',
     'buca',
     'building',
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
 4: {'202',
     '2021',
     '400k',
     '500',
     '500k',
     '5500',
     'act',
     'administrator',
     'advisor',
     'advisory',
     'agency',
     'aggregate',
     'analytics',
     'appropriations',
     'architecture',
     'audit',
     'auditing',
     'balance',
     'based',
     'beating',
     'become',
     'benefit',
     'benefits',
     'billing',
     'book',
     'bor',
     'broker',
     'brokers',
     'buca',
     'budget',
     'building',
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
 5: {'202',
     '2021',
     '400k',
     '500',
     '500k',
     '5500',
     'act',
     'administrator',
     'advisor',
     'advisory',
     'agency',
     'aggregate',
     'analytics',
     'appropriations',
     'architecture',
     'audit',
     'auditing',
     'avoid',
     'balance',
     'based',
     'beating',
     'become',
     'benefit',
     'benefits',
     'billing',
     'book',
     'bor',
     'broker',
     'brokers',
     'buca',
     'building',
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
 6: {'202',
     '2021',
     '400k',
     '500',
     '500k',
     '5500',
     'act',
     'administrator',
     'advisor',
     'advisory',
     'agency',
     'aggregate',
     'analytics',
     'appropriations',
     'architecture',
     'audit',
     'auditing',
     'balance',
     'based',
     'beating',
     'become',
     'benefit',
     'benefits',
     'billing',
     'book',
     'bor',
     'broker',
     'brokers',
     'buca',
     'building',
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
 7: {'202',
     '2021',
     '400k',
     '500',
     '500k',
     '5500',
     'act',
     'administrator',
     'advisor',
     'advisory',
     'agency',
     'aggregate',
     'analytics',
     'appropriations',
     'architecture',
     'audit',
     'auditing',
     'balance',
     'based',
     'beating',
     'become',
     'benefit',
     'benefits',
     'billing',
     'book',
     'bor',
     'broker',
     'brokers',
     'buca',
     'building',
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
 8: {'202',
     '2021',
     '400k',
     '500',
     '500k',
     '5500',
     'act',
     'administrator',
     'advisor',
     'advisory',
     'agency',
     'aggregate',
     'analytics',
     'api',
     'appropriations',
     'architecture',
     'audit',
     'auditing',
     'balance',
     'based',
     'beating',
     'become',
     'benefit',
     'benefits',
     'billing',
     'book',
     'bor',
     'broker',
     'brokers',
     'buca',
     'building',
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
 9: {'202',
     '2021',
     '400k',
     '500',
     '500k',
     '5500',
     'act',
     'administrator',
     'advisor',
     'advisory',
     'agency',
     'aggregate',
     'agreement',
     'analytics',
     'appropriations',
     'architecture',
     'audit',
     'auditing',
     'balance',
     'based',
     'beating',
     'become',
     'benefit',
     'benefits',
     'billing',
     'book',
     'bor',
     'broker',
     'brokers',
     'buca',
     'building',
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
 10: {'202',
      '2021',
      '400k',
      '500',
      '500k',
      '5500',
      'act',
      'administrator',
      'advisor',
      'advisory',
      'agency',
      'agent',
      'aggregate',
      'ai',
      'analytics',
      'appropriations',
      'architecture',
      'audit',
      'auditing',
      'automate',
      'automation',
      'balance',
      'based',
      'beating',
      'become',
      'benefit',
      'benefits',
      'billing',
      'book',
      'bor',
      'broker',
      'brokers',
      'buca',
      'building',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'202',
      '2021',
      '400k',
      '500',
      '500k',
      '5500',
      'act',
      'administrator',
      'advisor',
      'advisory',
      'agency',
      'aggregate',
      'analytics',
      'appropriations',
      'architecture',
      'audit',
      'auditing',
      'balance',
      'based',
      'beating',
      'become',
      'benefit',
      'benefits',
      'billing',
      'book',
      'bor',
      'broker',
      'brokers',
      'buca',
      'building',
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
 12: {'202',
      '2021',
      '400k',
      '500',
      '500k',
      '5500',
      'act',
      'action',
      'administrator',
      'advisor',
      'advisory',
      'agency',
      'aggregate',
      'analytics',
      'appropriations',
      'architecture',
      'audit',
      'auditing',
      'balance',
      'based',
      'beating',
      'become',
      'benefit',
      'benefits',
      'billing',
      'book',
      'bor',
      'broker',
      'brokers',
      'buca',
      'building',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Benefits Blake',
      'channel': 'Benefits Blake',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:18](https://www.youtube.com/watch?v=wUzyX8bEvt0&t=618s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The consolidated appropriations act of 2026 again mandates that pharmacy '
              'benefit managers make rebate arrangement records available for plan audit no '
              'later than August 2028. You also want to own your data.',
      'timestamp': 618,
      'timestamp_label': '[00:10:18]',
      'timestamp_seconds': 618,
      'tip': 'The consolidated appropriations act of 2026 again mandates that pharmacy benefit '
             'managers make rebate arrangement records available for plan audit no later than '
             'August 2028. You also want to own your data.',
      'title': 'Best-in-Class Transparent PBMs: What the Contract Has to Say (Benefits Blake)',
      'url': 'https://www.youtube.com/watch?v=wUzyX8bEvt0&t=618s',
      'video_id': 'wUzyX8bEvt0'},
     {'author': 'BenefitsAlly | Home of the 3x3x3 Challenge',
      'channel': 'BenefitsAlly | Home of the 3x3x3 Challenge',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=xXX6dBL4p3A&t=134s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Outfox goes live in just 30 days with no complex integrations required. Brokers '
              'using Outfox will have faster launches, measurable cost savings, and a stronger '
              'client satisfaction, helping you grow and retain your book of business.',
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': 'Outfox goes live in just 30 days with no complex integrations required. Brokers '
             'using Outfox will have faster launches, measurable cost savings, and a stronger '
             'client satisfaction, helping you grow and retain your book of business.',
      'title': 'Outfox Health - 3x3x3 Challenge With Beth Ann Lopez (BenefitsAlly | Home of '
               'the 3x3x3 Challenge)',
      'url': 'https://www.youtube.com/watch?v=xXX6dBL4p3A&t=134s',
      'video_id': 'xXX6dBL4p3A'},
     {'author': 'Imagine360',
      'channel': 'Imagine360',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=U6ZwMY7UtFU&t=21s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "They're demanding better they want more value there's more options on the "
              'market for them reference based pricing is becoming far more dominant in the.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "They're demanding better they want more value there's more options on the market "
             'for them reference based pricing is becoming far more dominant in the.',
      'title': 'Marty Makary, MD Explains How Reference-Based Pricing Is Transforming '
               'Employer-Sponsored Healthcare (Imagine360)',
      'url': 'https://www.youtube.com/watch?v=U6ZwMY7UtFU&t=21s',
      'video_id': 'U6ZwMY7UtFU'},
     {'author': 'PA Pharmacists',
      'channel': 'PA Pharmacists',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=l81CzyzPR6M&t=83s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Based on the changes in the marketplace what business can afford to stay in '
              'business when they are paid below their cost the funny thing is PBMs are quick '
              'to lower prices when the market drops but lag grossly behind when they '
              'increase.',
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': 'Based on the changes in the marketplace what business can afford to stay in '
             'business when they are paid below their cost the funny thing is PBMs are quick '
             'to lower prices when the market drops but lag grossly behind when they increase.',
      'title': 'Maximum Allowable Cost pricing or MAC pricing on pharmacies (PA Pharmacists)',
      'url': 'https://www.youtube.com/watch?v=l81CzyzPR6M&t=83s',
      'video_id': 'l81CzyzPR6M'},
     {'author': 'American Trust Administrators | Level Funding',
      'channel': 'American Trust Administrators | Level Funding',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:41](https://www.youtube.com/watch?v=E2z3UzEl2Ds&t=221s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Level funding is a more mature product or needs a more mature broker than a '
              'fully insured program does. And the benefit to that is that you can now provide '
              'surpluses when the plan runs well to your clients. Main Street, right there in '
              'River City.',
      'timestamp': 221,
      'timestamp_label': '[00:03:41]',
      'timestamp_seconds': 221,
      'tip': 'Level funding is a more mature product or needs a more mature broker than a '
             'fully insured program does. And the benefit to that is that you can now provide '
             'surpluses when the plan runs well to your clients. Main Street, right there in '
             'River City.',
      'title': 'How to Prepare Your First Level Funded Case (American Trust Administrators | '
               'Level Funding)',
      'url': 'https://www.youtube.com/watch?v=E2z3UzEl2Ds&t=221s',
      'video_id': 'E2z3UzEl2Ds'},
     {'author': 'Self-Funded',
      'channel': 'Self-Funded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:26](https://www.youtube.com/watch?v=A__ZFq9k8Ds&t=1526s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "But when you're when you're dealing with a service that has such a high "
              'intensity of of labor meaning you have to have a really beefed up service '
              'model.',
      'timestamp': 1526,
      'timestamp_label': '[00:25:26]',
      'timestamp_seconds': 1526,
      'tip': "But when you're when you're dealing with a service that has such a high "
             'intensity of of labor meaning you have to have a really beefed up service model.',
      'title': 'Unlocking Cost Savings with Reference Based Pricing (RBP) - ClaimDOC - Omar '
               'Arif (Self-Funded)',
      'url': 'https://www.youtube.com/watch?v=A__ZFq9k8Ds&t=1526s',
      'video_id': 'A__ZFq9k8Ds'},
     {'author': 'Ross & Yerger',
      'channel': 'Ross & Yerger',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:54](https://www.youtube.com/watch?v=zzL4UNZNaFo&t=174s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Stop-loss renewals on an annual basis and that's a very volatile market based "
              "on your claims experience lastly and where there's a lot of traction these.",
      'timestamp': 174,
      'timestamp_label': '[00:02:54]',
      'timestamp_seconds': 174,
      'tip': "Stop-loss renewals on an annual basis and that's a very volatile market based on "
             "your claims experience lastly and where there's a lot of traction these.",
      'title': 'What is a medical captive and how would it work for my business? (Ross & '
               'Yerger)',
      'url': 'https://www.youtube.com/watch?v=zzL4UNZNaFo&t=174s',
      'video_id': 'zzL4UNZNaFo'},
     {'author': 'RapidSync',
      'channel': 'RapidSync',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:04](https://www.youtube.com/watch?v=pzqZsKtSynY&t=364s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I mean, seriously, what other investment in your business gives you that kind '
              "of guaranteed return? And what's great is that the benefits just keep stacking "
              'up. A culture of safety does way more than just lower your XOD. It makes your '
              'restaurant a better place to work.',
      'timestamp': 364,
      'timestamp_label': '[00:06:04]',
      'timestamp_seconds': 364,
      'tip': 'I mean, seriously, what other investment in your business gives you that kind of '
             "guaranteed return? And what's great is that the benefits just keep stacking up. "
             'A culture of safety does way more than just lower your XOD. It makes your '
             'restaurant a better place to work.',
      'title': "Workers' Comp for Restaurants: Class Codes, Injury Risks & How to Control Your "
               'Premium (RapidSync)',
      'url': 'https://www.youtube.com/watch?v=pzqZsKtSynY&t=364s',
      'video_id': 'pzqZsKtSynY'},
     {'author': 'Ethica Pharmacy Advisors',
      'channel': 'Ethica Pharmacy Advisors',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=z2vuJMYnjZE&t=63s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Completely independent and transparent pharmacy benefit consulting firm. I '
              'wanted to make  sure that if a plan sponsor was working with Ethica.',
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': 'Completely independent and transparent pharmacy benefit consulting firm. I '
             'wanted to make  sure that if a plan sponsor was working with Ethica.',
      'title': 'PBM Audits: Why Independence Matters (Ethica Pharmacy Advisors)',
      'url': 'https://www.youtube.com/watch?v=z2vuJMYnjZE&t=63s',
      'video_id': 'z2vuJMYnjZE'},
     {'author': 'The Coyle Group - Business Insurance',
      'channel': 'The Coyle Group - Business Insurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=njIghi8P9jQ&t=65s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "There by luck you need a process and that's why we've designed the compcontrol "
              '360 process to help mid-market business owners like.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': "There by luck you need a process and that's why we've designed the compcontrol "
             '360 process to help mid-market business owners like.',
      'title': 'What is a Workers Comp Minimum Experience Modifier (The Coyle Group - Business '
               'Insurance)',
      'url': 'https://www.youtube.com/watch?v=njIghi8P9jQ&t=65s',
      'video_id': 'njIghi8P9jQ'},
     {'author': 'BeneSmart - A Modern Approach to Benefits',
      'channel': 'BeneSmart - A Modern Approach to Benefits',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:31](https://www.youtube.com/watch?v=UOjbo9Dprhw&t=1051s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Evaluated some new to Market Partners take some time to do that this year see '
              "if your company's really in the best position possible with your health plan "
              'you never know level funded solution could be right for your business.',
      'timestamp': 1051,
      'timestamp_label': '[00:17:31]',
      'timestamp_seconds': 1051,
      'tip': 'Evaluated some new to Market Partners take some time to do that this year see if '
             "your company's really in the best position possible with your health plan you "
             'never know level funded solution could be right for your business.',
      'title': 'Unlocking Savings with Level Funded Health Insurance | Purchasing Strategies '
               'for HR, CFOs, and CEOs (BeneSmart - A Modern Approach to Benefits)',
      'url': 'https://www.youtube.com/watch?v=UOjbo9Dprhw&t=1051s',
      'video_id': 'UOjbo9Dprhw'},
     {'author': 'Stillwell Risk Partners',
      'channel': 'Stillwell Risk Partners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:04](https://www.youtube.com/watch?v=tUclSqTs7E8&t=304s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Control of what your workers compensation costs are so again my name is Ryan '
              "I'm the owner here at Stillwater's Partners we specialize in workers "
              'compensation um and what we do is we help our clients take control of the risk.',
      'timestamp': 304,
      'timestamp_label': '[00:05:04]',
      'timestamp_seconds': 304,
      'tip': "Control of what your workers compensation costs are so again my name is Ryan I'm "
             "the owner here at Stillwater's Partners we specialize in workers compensation um "
             'and what we do is we help our clients take control of the risk.',
      'title': 'What is the Workers Comp Experience Modification Rate - and why should you '
               'care? (Stillwell Risk Partners)',
      'url': 'https://www.youtube.com/watch?v=tUclSqTs7E8&t=304s',
      'video_id': 'tUclSqTs7E8'},
     {'author': 'Leavitt Group',
      'channel': 'Leavitt Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:24](https://www.youtube.com/watch?v=9yOM92q1AWQ&t=84s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Predictable in the long run and we've not been able to do that in the "
              "traditional Insurance Market by participating in a captive we're really able to "
              'pull together with like-minded employers and purchase insurance in a different '
              'way through a captive.',
      'timestamp': 84,
      'timestamp_label': '[00:01:24]',
      'timestamp_seconds': 84,
      'tip': "Predictable in the long run and we've not been able to do that in the "
             "traditional Insurance Market by participating in a captive we're really able to "
             'pull together with like-minded employers and purchase insurance in a different '
             'way through a captive.',
      'title': 'Explore the Power of Medical Stop-Loss Insurance Captives (Leavitt Group)',
      'url': 'https://www.youtube.com/watch?v=9yOM92q1AWQ&t=84s',
      'video_id': '9yOM92q1AWQ'},
     {'author': 'Evolved Benefits',
      'channel': 'Evolved Benefits',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:54](https://www.youtube.com/watch?v=H0MJJJNfYdo&t=174s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Your profession that's exactly why you're in this business so you can help "
              'people and on the back and you get compensated for doing so um I get asked this '
              'question a lot hope this answered that question for you and of course I look '
              'forward to talking to you very soon.',
      'timestamp': 174,
      'timestamp_label': '[00:02:54]',
      'timestamp_seconds': 174,
      'tip': "Your profession that's exactly why you're in this business so you can help "
             'people and on the back and you get compensated for doing so um I get asked this '
             'question a lot hope this answered that question for you and of course I look '
             'forward to talking to you very soon.',
      'title': 'What Are The Commissions With A MEC Plan? (Evolved Benefits)',
      'url': 'https://www.youtube.com/watch?v=H0MJJJNfYdo&t=174s',
      'video_id': 'H0MJJJNfYdo'},
     {'author': 'American Trust Administrators | Level Funding',
      'channel': 'American Trust Administrators | Level Funding',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:38](https://www.youtube.com/watch?v=TKRoJd6Glxw&t=398s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Lot of communication between the older guys and the new guys when they come '
              'into the space I hope this helps you be a little bit more wise in your business '
              'helping mainst street fight for their future instead of funding Wall Street '
              "we'll see you in a bit.",
      'timestamp': 398,
      'timestamp_label': '[00:06:38]',
      'timestamp_seconds': 398,
      'tip': 'Lot of communication between the older guys and the new guys when they come into '
             'the space I hope this helps you be a little bit more wise in your business '
             'helping mainst street fight for their future instead of funding Wall Street '
             "we'll see you in a bit.",
      'title': 'Biggest Pitfalls of Level-Funded Health Plans (And How to Avoid Them) '
               '(American Trust Administrators | Level Funding)',
      'url': 'https://www.youtube.com/watch?v=TKRoJd6Glxw&t=398s',
      'video_id': 'TKRoJd6Glxw'}],
 2: [{'author': 'Benefits Blake',
      'channel': 'Benefits Blake',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:51](https://www.youtube.com/watch?v=m68BBrL5G18&t=291s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "ProPublica did some reporting on this back in 2019. And I'm going to date stamp "
              'that hard because it was before the new Consolidated Appropriations Act of 2021 '
              'disclosure laws took effect.',
      'timestamp': 291,
      'timestamp_label': '[00:04:51]',
      'timestamp_seconds': 291,
      'tip': "ProPublica did some reporting on this back in 2019. And I'm going to date stamp "
             'that hard because it was before the new Consolidated Appropriations Act of 2021 '
             'disclosure laws took effect.',
      'title': 'Why You Should Fire Your Benefits Broker (From a Broker) (Benefits Blake)',
      'url': 'https://www.youtube.com/watch?v=m68BBrL5G18&t=291s',
      'video_id': 'm68BBrL5G18'},
     {'author': 'P & C Insurance Helpline',
      'channel': 'P & C Insurance Helpline',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:53](https://www.youtube.com/watch?v=tzjptJxgOQg&t=113s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'t allow multiple brokers to come and get quotes for the same customer. The "
              'reason is like no, they wanted to offer or they wanted to honor the particular '
              'broker and it is time tedious process.',
      'timestamp': 113,
      'timestamp_label': '[00:01:53]',
      'timestamp_seconds': 113,
      'tip': "'t allow multiple brokers to come and get quotes for the same customer. The "
             'reason is like no, they wanted to offer or they wanted to honor the particular '
             'broker and it is time tedious process.',
      'title': 'Broker of Record(BOR) Letter (P & C Insurance Helpline)',
      'url': 'https://www.youtube.com/watch?v=tzjptJxgOQg&t=113s',
      'video_id': 'tzjptJxgOQg'},
     {'author': 'Tyler Dutchover',
      'channel': 'Tyler Dutchover',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=b2StkpG4yOY&t=88s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'This means that your company and the administrator that actually helps pay for '
              "you pays that first 75,000 of an individual's medical bills for the year.",
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'This means that your company and the administrator that actually helps pay for '
             "you pays that first 75,000 of an individual's medical bills for the year.",
      'title': 'What is Stop Loss Insurance? Explained in plain English (Tyler Dutchover)',
      'url': 'https://www.youtube.com/watch?v=b2StkpG4yOY&t=88s',
      'video_id': 'b2StkpG4yOY'},
     {'author': 'American Trust Administrators | Level Funding',
      'channel': 'American Trust Administrators | Level Funding',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:25](https://www.youtube.com/watch?v=QBs9tuVEIhw&t=325s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You're going to still going to have the fixed cost side of things. On the level "
              'funded side, this fixed cost is admin, broker fees, PPO fees, telemedicine, and '
              'then the majority generally is the stop-loss fee or the stop-loss coverage.',
      'timestamp': 325,
      'timestamp_label': '[00:05:25]',
      'timestamp_seconds': 325,
      'tip': "You're going to still going to have the fixed cost side of things. On the level "
             'funded side, this fixed cost is admin, broker fees, PPO fees, telemedicine, and '
             'then the majority generally is the stop-loss fee or the stop-loss coverage.',
      'title': 'Fully Insured vs Level-Funded: Which Is Better Long-Term for Small Businesses? '
               '(American Trust Administrators | Level Funding)',
      'url': 'https://www.youtube.com/watch?v=QBs9tuVEIhw&t=325s',
      'video_id': 'QBs9tuVEIhw'},
     {'author': 'The Benefits Group',
      'channel': 'The Benefits Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:06](https://www.youtube.com/watch?v=7-gc1zHvZbc&t=66s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "We're paying the claims and then a large claim comes through. Stop loss will "
              "advance money to that claims account. So there's two parts of the stop loss "
              "payment. There's a lot more, but we're going to stick with specific and "
              'aggregate protection.',
      'timestamp': 66,
      'timestamp_label': '[00:01:06]',
      'timestamp_seconds': 66,
      'tip': "We're paying the claims and then a large claim comes through. Stop loss will "
             "advance money to that claims account. So there's two parts of the stop loss "
             "payment. There's a lot more, but we're going to stick with specific and "
             'aggregate protection.',
      'title': 'Video Series #9   Stop Loss - Who Pays the Million-Dollar Claim (The Benefits '
               'Group)',
      'url': 'https://www.youtube.com/watch?v=7-gc1zHvZbc&t=66s',
      'video_id': '7-gc1zHvZbc'},
     {'author': 'Blue Ocean Benefits & Consulting',
      'channel': 'Blue Ocean Benefits & Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:18](https://www.youtube.com/watch?v=D23XjGg7o_g&t=438s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Going to pay and a self-funded one has this variable claim amount so fixed '
              'costs variable costs uh so watch some more of our videos for more of the '
              "details I'm Matt Roy with uh blue ocean uh benefits in Consulting and America "
              "America's insurance guy.",
      'timestamp': 438,
      'timestamp_label': '[00:07:18]',
      'timestamp_seconds': 438,
      'tip': 'Going to pay and a self-funded one has this variable claim amount so fixed costs '
             "variable costs uh so watch some more of our videos for more of the details I'm "
             "Matt Roy with uh blue ocean uh benefits in Consulting and America America's "
             'insurance guy.',
      'title': 'Basics of Self-Funded & Level-Funded Group Plans (Blue Ocean Benefits & '
               'Consulting)',
      'url': 'https://www.youtube.com/watch?v=D23XjGg7o_g&t=438s',
      'video_id': 'D23XjGg7o_g'},
     {'author': 'PBM Insider',
      'channel': 'PBM Insider',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=o57C9bK5ouI&t=54s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'A reimbursement amount that the PM PBM is willing to pay the pharmacy for the '
              'drug and a professional dispensing fee to cover things like the pharmacy staff, '
              'light bill, technology, counseling of patients, etc.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'A reimbursement amount that the PM PBM is willing to pay the pharmacy for the '
             'drug and a professional dispensing fee to cover things like the pharmacy staff, '
             'light bill, technology, counseling of patients, etc.',
      'title': 'The PBM Insider - What is Spread Pricing? (PBM Insider)',
      'url': 'https://www.youtube.com/watch?v=o57C9bK5ouI&t=54s',
      'video_id': 'o57C9bK5ouI'},
     {'author': 'Frier Levitt',
      'channel': 'Frier Levitt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:27](https://www.youtube.com/watch?v=67He43cmPRc&t=567s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And that's usually typical of a desktop audit. We'll also see invoice "
              'reconciliation audits and it is becoming a much more common ask um and part of '
              'audits um to be asking pharmacies for their inventory and their purchase '
              'records along with their dispensing information.',
      'timestamp': 567,
      'timestamp_label': '[00:09:27]',
      'timestamp_seconds': 567,
      'tip': "And that's usually typical of a desktop audit. We'll also see invoice "
             'reconciliation audits and it is becoming a much more common ask um and part of '
             'audits um to be asking pharmacies for their inventory and their purchase records '
             'along with their dispensing information.',
      'title': 'PBM Audits & Network Compliance in 2026 What Pharmacies Need to Know Now '
               '(Frier Levitt)',
      'url': 'https://www.youtube.com/watch?v=67He43cmPRc&t=567s',
      'video_id': '67He43cmPRc'},
     {'author': 'Tyler Dutchover',
      'channel': 'Tyler Dutchover',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:14](https://www.youtube.com/watch?v=m5BLhBDIZZ4&t=74s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re going to call them Mediocre Corp. They do accounting or manufacturing or "
              'some combination of the two. Under the fully insured model, that means that '
              "they're going to pay 500,000 during the year for their employees insurance.",
      'timestamp': 74,
      'timestamp_label': '[00:01:14]',
      'timestamp_seconds': 74,
      'tip': "'re going to call them Mediocre Corp. They do accounting or manufacturing or "
             'some combination of the two. Under the fully insured model, that means that '
             "they're going to pay 500,000 during the year for their employees insurance.",
      'title': 'Fully Insured vs Level Funded: Health Insurance Explained (Tyler Dutchover)',
      'url': 'https://www.youtube.com/watch?v=m5BLhBDIZZ4&t=74s',
      'video_id': 'm5BLhBDIZZ4'},
     {'author': 'Frier Levitt',
      'channel': 'Frier Levitt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:09](https://www.youtube.com/watch?v=hKqVi489zow&t=909s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "PBM um in making a certain decision against a pharmacy. 't emphasize enough "
              "that it's always good and in the best interest of a pharmacy to certainly um "
              'appeal audit findings regardless of the dollar amount.',
      'timestamp': 909,
      'timestamp_label': '[00:15:09]',
      'timestamp_seconds': 909,
      'tip': "PBM um in making a certain decision against a pharmacy. 't emphasize enough that "
             "it's always good and in the best interest of a pharmacy to certainly um appeal "
             'audit findings regardless of the dollar amount.',
      'title': 'PBM Audits & Network Compliance 2026: Critical Strategies for New Jersey '
               'Pharmacies (Frier Levitt)',
      'url': 'https://www.youtube.com/watch?v=hKqVi489zow&t=909s',
      'video_id': 'hKqVi489zow'},
     {'author': 'Heads Up Adviser',
      'channel': 'Heads Up Adviser',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=7cqcZyKB5aw&t=85s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'That group standpoint the value proposition of being in captive with another '
              'laser contract despite their size is is very valuable and they may they may '
              'stay put in that captive for forever and ever it just kind of depends on the '
              'group you know.',
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': 'That group standpoint the value proposition of being in captive with another '
             'laser contract despite their size is is very valuable and they may they may stay '
             'put in that captive for forever and ever it just kind of depends on the group '
             'you know.',
      'title': 'CAPTIVE VS TRADITIONAL STOP LOSS (Heads Up Adviser)',
      'url': 'https://www.youtube.com/watch?v=7cqcZyKB5aw&t=85s',
      'video_id': '7cqcZyKB5aw'},
     {'author': 'Bentley Tolk',
      'channel': 'Bentley Tolk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:41](https://www.youtube.com/watch?v=vgI5Fn4rQYY&t=221s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'ORISA as they administer ESOP investments but the plan is only followed to the '
              "extent it's consistent with Orisa and there's an abuse of discretion standard "
              "regarding the ESOP fiduciary's decision to invest in employer securities.",
      'timestamp': 221,
      'timestamp_label': '[00:03:41]',
      'timestamp_seconds': 221,
      'tip': 'ORISA as they administer ESOP investments but the plan is only followed to the '
             "extent it's consistent with Orisa and there's an abuse of discretion standard "
             "regarding the ESOP fiduciary's decision to invest in employer securities.",
      'title': 'ERISA Litigation 7: ERISA Pleading Requirements (6th Circuit) (Bentley Tolk)',
      'url': 'https://www.youtube.com/watch?v=vgI5Fn4rQYY&t=221s',
      'video_id': 'vgI5Fn4rQYY'},
     {'author': 'Self Insured Reporting',
      'channel': 'Self Insured Reporting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=HuaDk3XBOrc&t=79s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Provides a max to the amount of claims an employer will pay during a given '
              'period this provides protection for larger claims in total than the employer '
              'expected for the plan year if you like this content please consider '
              'subscribing.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': 'Provides a max to the amount of claims an employer will pay during a given '
             'period this provides protection for larger claims in total than the employer '
             'expected for the plan year if you like this content please consider subscribing.',
      'title': 'What is STOP-LOSS INSURANCE? | In less than 3 Minutes (Self Insured Reporting)',
      'url': 'https://www.youtube.com/watch?v=HuaDk3XBOrc&t=79s',
      'video_id': 'HuaDk3XBOrc'},
     {'author': 'Self-Funded',
      'channel': 'Self-Funded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:45](https://www.youtube.com/watch?v=J8culIBQaww&t=105s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Paying you know they're paying and also the paper involved which is the carrier "
              "they're paying the carrier for the right to issue policies under their name and "
              'then the mgu themselves take a percentage of the premium as their way to pay '
              'the bills.',
      'timestamp': 105,
      'timestamp_label': '[00:01:45]',
      'timestamp_seconds': 105,
      'tip': "Paying you know they're paying and also the paper involved which is the carrier "
             "they're paying the carrier for the right to issue policies under their name and "
             'then the mgu themselves take a percentage of the premium as their way to pay the '
             'bills.',
      'title': 'What is a Stop Loss MGU? (Self-Funded)',
      'url': 'https://www.youtube.com/watch?v=J8culIBQaww&t=105s',
      'video_id': 'J8culIBQaww'},
     {'author': 'AHealthcareZ - Healthcare Finance Explained',
      'channel': 'AHealthcareZ - Healthcare Finance Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:07](https://www.youtube.com/watch?v=xcu6bvj22fc&t=247s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Navigate the employees then they oftentimes end up getting lost and that's my "
              "summary for direct contracting certainly there's more about this I'd love to "
              'hear your opinion as well and thank you for watching ehealthcareyz.',
      'timestamp': 247,
      'timestamp_label': '[00:04:07]',
      'timestamp_seconds': 247,
      'tip': "Navigate the employees then they oftentimes end up getting lost and that's my "
             "summary for direct contracting certainly there's more about this I'd love to "
             'hear your opinion as well and thank you for watching ehealthcareyz.',
      'title': 'Healthcare Direct Contracting Explained (AHealthcareZ - Healthcare Finance '
               'Explained)',
      'url': 'https://www.youtube.com/watch?v=xcu6bvj22fc&t=247s',
      'video_id': 'xcu6bvj22fc'}],
 3: [{'author': 'The General Agency',
      'channel': 'The General Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:05](https://www.youtube.com/watch?v=FPcS3pupwwA&t=305s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'It could be anywhere from 15, 30%, 50 or 70, but this one actually ended up '
              "pretty high at 202. So, keep that in mind when you're looking at "
              'reference-based pricing products and if you need help, of course you can always '
              'call us here at the General Agency.',
      'timestamp': 305,
      'timestamp_label': '[00:05:05]',
      'timestamp_seconds': 305,
      'tip': 'It could be anywhere from 15, 30%, 50 or 70, but this one actually ended up '
             "pretty high at 202. So, keep that in mind when you're looking at reference-based "
             'pricing products and if you need help, of course you can always call us here at '
             'the General Agency.',
      'title': 'PPO vs RBP (reference-based pricing) (The General Agency)',
      'url': 'https://www.youtube.com/watch?v=FPcS3pupwwA&t=305s',
      'video_id': 'FPcS3pupwwA'},
     {'author': 'STAT',
      'channel': 'STAT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:17](https://www.youtube.com/watch?v=27INQuNycLA&t=197s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And if drugmakers have to offer rebates to PBMs to push their drugs up higher '
              'on the formulary, sometimes they have to raise the list price of their drugs to '
              'help cover the rebates. So let’s bring it all back. Drugs cost a lot of money '
              'to make, health insurance costs money.',
      'timestamp': 197,
      'timestamp_label': '[00:03:17]',
      'timestamp_seconds': 197,
      'tip': 'And if drugmakers have to offer rebates to PBMs to push their drugs up higher on '
             'the formulary, sometimes they have to raise the list price of their drugs to '
             'help cover the rebates. So let’s bring it all back. Drugs cost a lot of money to '
             'make, health insurance costs money.',
      'title': 'How pharmacy benefit managers influence drug pricing (STAT)',
      'url': 'https://www.youtube.com/watch?v=27INQuNycLA&t=197s',
      'video_id': '27INQuNycLA'},
     {'author': 'Holloway Benefit Concepts',
      'channel': 'Holloway Benefit Concepts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=2dsXkvZasDU&t=36s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s where all the cost really come from. In the Reference Based Pricing world "
              "you're getting away from all that so your claims dollars are not nearly as "
              "high, you're not paying as much in claims and your actual cost when people go "
              'to the hospital is much lower.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': "'s where all the cost really come from. In the Reference Based Pricing world "
             "you're getting away from all that so your claims dollars are not nearly as high, "
             "you're not paying as much in claims and your actual cost when people go to the "
             'hospital is much lower.',
      'title': 'What is Reference Based Pricing? | Employee Benefits 101 | Holloway Benefit '
               'Concepts (2020) (Holloway Benefit Concepts)',
      'url': 'https://www.youtube.com/watch?v=2dsXkvZasDU&t=36s',
      'video_id': '2dsXkvZasDU'},
     {'author': 'McGohan Brabender',
      'channel': 'McGohan Brabender',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=i5hi-x9Pdxw&t=146s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Control over health care costs can manage claims costs through tailored '
              'clinical or Wellness programs and guide employees towards fair price providers '
              "to help improve their health while also improving cost savings it's a win-win "
              'for both you and your employer.',
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': 'Control over health care costs can manage claims costs through tailored clinical '
             'or Wellness programs and guide employees towards fair price providers to help '
             "improve their health while also improving cost savings it's a win-win for both "
             'you and your employer.',
      'title': 'Understanding Your Self-Funded Health Plan | McGohan Brabender (McGohan '
               'Brabender)',
      'url': 'https://www.youtube.com/watch?v=i5hi-x9Pdxw&t=146s',
      'video_id': 'i5hi-x9Pdxw'},
     {'author': 'The Difference Card',
      'channel': 'The Difference Card',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:23](https://www.youtube.com/watch?v=iT4htd_Aqag&t=23s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your company you pay a monthly premium to access your benefits that monthly '
              'premium includes costs for claims profit pooling costs which is the average.',
      'timestamp': 23,
      'timestamp_label': '[00:00:23]',
      'timestamp_seconds': 23,
      'tip': 'Your company you pay a monthly premium to access your benefits that monthly '
             'premium includes costs for claims profit pooling costs which is the average.',
      'title': 'Self Funded vs Fully Insured Health Plans (The Difference Card)',
      'url': 'https://www.youtube.com/watch?v=iT4htd_Aqag&t=23s',
      'video_id': 'iT4htd_Aqag'},
     {'author': 'BeneSmart - A Modern Approach to Benefits',
      'channel': 'BeneSmart - A Modern Approach to Benefits',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:18](https://www.youtube.com/watch?v=WXjUaMhMjcQ&t=258s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "With fully insured plans, your cost is locked. You're just hoping for a low "
              "renewal. With level funded, there's a small chance that you'll get a refund, "
              'but again, those refunds are usually shared. And the game is still rigged with '
              'spread pricing and bakedin margins.',
      'timestamp': 258,
      'timestamp_label': '[00:04:18]',
      'timestamp_seconds': 258,
      'tip': "With fully insured plans, your cost is locked. You're just hoping for a low "
             "renewal. With level funded, there's a small chance that you'll get a refund, but "
             'again, those refunds are usually shared. And the game is still rigged with '
             'spread pricing and bakedin margins.',
      'title': 'Fully Insured vs Level-Funded vs Captives: What Most Employers Get Wrong '
               '(BeneSmart - A Modern Approach to Benefits)',
      'url': 'https://www.youtube.com/watch?v=WXjUaMhMjcQ&t=258s',
      'video_id': 'WXjUaMhMjcQ'},
     {'author': 'SmithRx',
      'channel': 'SmithRx',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:46](https://www.youtube.com/watch?v=3cUGL3xTK7E&t=166s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Transparency, straightforward pricing, and consumer choice. With clear pricing '
              'and more options, modern PBMs help employers better manage health care costs '
              'while giving employees better access to the medications they need. Smith RX, '
              'radically transparent pharmacy benefits.',
      'timestamp': 166,
      'timestamp_label': '[00:02:46]',
      'timestamp_seconds': 166,
      'tip': 'Transparency, straightforward pricing, and consumer choice. With clear pricing '
             'and more options, modern PBMs help employers better manage health care costs '
             'while giving employees better access to the medications they need. Smith RX, '
             'radically transparent pharmacy benefits.',
      'title': 'What is a PBM? (Long) (SmithRx)',
      'url': 'https://www.youtube.com/watch?v=3cUGL3xTK7E&t=166s',
      'video_id': '3cUGL3xTK7E'},
     {'author': 'American Ambulance Association',
      'channel': 'American Ambulance Association',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:41](https://www.youtube.com/watch?v=I33Yc7nNN_c&t=1781s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "That's an immediate two thousand dollars that you could save right so this is "
              'part of finding the right care the cost and quality of health care believe it '
              'or not health care the more a doctor does a procedure the less it costs the '
              "employer and it's counterintuitive.",
      'timestamp': 1781,
      'timestamp_label': '[00:29:41]',
      'timestamp_seconds': 1781,
      'tip': "That's an immediate two thousand dollars that you could save right so this is "
             'part of finding the right care the cost and quality of health care believe it or '
             'not health care the more a doctor does a procedure the less it costs the '
             "employer and it's counterintuitive.",
      'title': 'Employee Benefits Captive Insurance for EMS (American Ambulance Association)',
      'url': 'https://www.youtube.com/watch?v=I33Yc7nNN_c&t=1781s',
      'video_id': 'I33Yc7nNN_c'},
     {'author': 'ELAP Services',
      'channel': 'ELAP Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:11](https://www.youtube.com/watch?v=UcjjCTQMOV4&t=131s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Space and they need to be anchored to something and that's exactly what "
              "reference-based pricing does in the market and that's what e-lap and imagine "
              "health does and that's where you guys have been great leaders so thank you for "
              "what you're doing in healthcare.",
      'timestamp': 131,
      'timestamp_label': '[00:02:11]',
      'timestamp_seconds': 131,
      'tip': "Space and they need to be anchored to something and that's exactly what "
             "reference-based pricing does in the market and that's what e-lap and imagine "
             "health does and that's where you guys have been great leaders so thank you for "
             "what you're doing in healthcare.",
      'title': 'Reference-based pricing, Marty Makary, MD, & Healthcare Cost Transparency '
               '(ELAP Services)',
      'url': 'https://www.youtube.com/watch?v=UcjjCTQMOV4&t=131s',
      'video_id': 'UcjjCTQMOV4'},
     {'author': 'Remodel Benefits',
      'channel': 'Remodel Benefits',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:25](https://www.youtube.com/watch?v=vCzjI43ZWVI&t=325s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Scenario this is what inherently creates some issues within a reference-based '
              'pricing environment but again lesson number one here is that the savings is '
              'legit and this is why the savings are legit in a reference-based pricing '
              'environment it is literally just math.',
      'timestamp': 325,
      'timestamp_label': '[00:05:25]',
      'timestamp_seconds': 325,
      'tip': 'Scenario this is what inherently creates some issues within a reference-based '
             'pricing environment but again lesson number one here is that the savings is '
             'legit and this is why the savings are legit in a reference-based pricing '
             'environment it is literally just math.',
      'title': 'Reference Based Pricing - Lesson 1 (Remodel Benefits)',
      'url': 'https://www.youtube.com/watch?v=vCzjI43ZWVI&t=325s',
      'video_id': 'vCzjI43ZWVI'},
     {'author': 'AHealthcareZ - Healthcare Finance Explained',
      'channel': 'AHealthcareZ - Healthcare Finance Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:46](https://www.youtube.com/watch?v=yFJFnewKqw4&t=466s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '2012 the PBMs were not passing it through, right? So So back when the PBMs '
              'could keep the rebates, the rebates were a major contributor to their profit '
              'margin. Now they also had administrative fees back then. They only contributed '
              'in 5% to their overall profit margin.',
      'timestamp': 466,
      'timestamp_label': '[00:07:46]',
      'timestamp_seconds': 466,
      'tip': '2012 the PBMs were not passing it through, right? So So back when the PBMs could '
             'keep the rebates, the rebates were a major contributor to their profit margin. '
             'Now they also had administrative fees back then. They only contributed in 5% to '
             'their overall profit margin.',
      'title': 'PBM Deception on Rebate Pass-Through (AHealthcareZ - Healthcare Finance '
               'Explained)',
      'url': 'https://www.youtube.com/watch?v=yFJFnewKqw4&t=466s',
      'video_id': 'yFJFnewKqw4'},
     {'author': 'Workers Comp New York',
      'channel': 'Workers Comp New York',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:14](https://www.youtube.com/watch?v=HEoc6bRfx9U&t=1094s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Can you file a workers's compensation claim and a third party lawsuit "
              "simultaneously? So, that's what we were just talking about. Not only can you do "
              'it, you should do it. You can collect workers compensation benefits and sue a '
              'third party at the same time.',
      'timestamp': 1094,
      'timestamp_label': '[00:18:14]',
      'timestamp_seconds': 1094,
      'tip': "Can you file a workers's compensation claim and a third party lawsuit "
             "simultaneously? So, that's what we were just talking about. Not only can you do "
             'it, you should do it. You can collect workers compensation benefits and sue a '
             'third party at the same time.',
      'title': 'A 3rd Party Lawsuit Can DOUBLE (or TRIPLE) Your Workers Comp Payout! (Workers '
               'Comp New York)',
      'url': 'https://www.youtube.com/watch?v=HEoc6bRfx9U&t=1094s',
      'video_id': 'HEoc6bRfx9U'},
     {'author': 'The Coyle Group - Business Insurance',
      'channel': 'The Coyle Group - Business Insurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:48](https://www.youtube.com/watch?v=7sfUUlxeHHk&t=588s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Costly mistakes and get the right coverage at the right price you get peace of '
              "mind you're looking for and you're avoiding problems down the road thanks for "
              'watching and before you go here are other videos that may find interesting on '
              'workers comp insurance thanks.',
      'timestamp': 588,
      'timestamp_label': '[00:09:48]',
      'timestamp_seconds': 588,
      'tip': 'Costly mistakes and get the right coverage at the right price you get peace of '
             "mind you're looking for and you're avoiding problems down the road thanks for "
             'watching and before you go here are other videos that may find interesting on '
             'workers comp insurance thanks.',
      'title': 'Workers Comp Class Codes, What Are They For? 2026 (The Coyle Group - Business '
               'Insurance)',
      'url': 'https://www.youtube.com/watch?v=7sfUUlxeHHk&t=588s',
      'video_id': '7sfUUlxeHHk'},
     {'author': 'AHealthcareZ - Healthcare Finance Explained',
      'channel': 'AHealthcareZ - Healthcare Finance Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:10](https://www.youtube.com/watch?v=-xH2R8NZ4pU&t=1090s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Ain't what's paid so arguably the pbms are negotiating a discount off of a "
              "fictitious price to begin with so that's the basics of how pbms make money "
              'thank you for watching.',
      'timestamp': 1090,
      'timestamp_label': '[00:18:10]',
      'timestamp_seconds': 1090,
      'tip': "Ain't what's paid so arguably the pbms are negotiating a discount off of a "
             "fictitious price to begin with so that's the basics of how pbms make money thank "
             'you for watching.',
      'title': 'How Prescription Drug Coverage Works: Formulary Tiers, PBM, Rebates, '
               'Spread-Pricing Explained (AHealthcareZ - Healthcare Finance Explained)',
      'url': 'https://www.youtube.com/watch?v=-xH2R8NZ4pU&t=1090s',
      'video_id': '-xH2R8NZ4pU'},
     {'author': 'Self-Funded',
      'channel': 'Self-Funded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:22](https://www.youtube.com/watch?v=6st-3ujjXM4&t=202s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You'll have really rough health outcomes that means that when that renewal "
              "comes it's not just you going at it exactly you've got some leverage in the "
              "market to say let's negotiate our costs you're not sharing your costs you just "
              'have more leverage.',
      'timestamp': 202,
      'timestamp_label': '[00:03:22]',
      'timestamp_seconds': 202,
      'tip': "You'll have really rough health outcomes that means that when that renewal comes "
             "it's not just you going at it exactly you've got some leverage in the market to "
             "say let's negotiate our costs you're not sharing your costs you just have more "
             'leverage.',
      'title': 'Captive Insurance Risk Layers Explained (Self-Funded)',
      'url': 'https://www.youtube.com/watch?v=6st-3ujjXM4&t=202s',
      'video_id': '6st-3ujjXM4'}],
 4: [{'author': 'Berger Montague',
      'channel': 'Berger Montague',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:42](https://www.youtube.com/watch?v=WBl8smrz_3E&t=222s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Thank you and as stated before we will be creating further videos exploring the '
              'ramifications of the consolidated appropriations act thanks for your '
              'participation today again follow us on linkedin at one vision analytics or our '
              'website at www.',
      'timestamp': 222,
      'timestamp_label': '[00:03:42]',
      'timestamp_seconds': 222,
      'tip': 'Thank you and as stated before we will be creating further videos exploring the '
             'ramifications of the consolidated appropriations act thanks for your '
             'participation today again follow us on linkedin at one vision analytics or our '
             'website at www.',
      'title': 'Impact of the CAA of 2021 on Gag Clauses (Berger Montague)',
      'url': 'https://www.youtube.com/watch?v=WBl8smrz_3E&t=222s',
      'video_id': 'WBl8smrz_3E'},
     {'author': 'BWI Aviation Insurance',
      'channel': 'BWI Aviation Insurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=LDwFFXhIu_U&t=52s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Active Aviation insurance policy and you would like to change Brokers signing a '
              'Bor in this instance keeps your current insurance policy in place but changes.',
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': 'Active Aviation insurance policy and you would like to change Brokers signing a '
             'Bor in this instance keeps your current insurance policy in place but changes.',
      'title': 'Broker of Record Letters Explained | Aviation Insurance (BWI Aviation '
               'Insurance)',
      'url': 'https://www.youtube.com/watch?v=LDwFFXhIu_U&t=52s',
      'video_id': 'LDwFFXhIu_U'},
     {'author': 'Insurance Brokers of Arizona',
      'channel': 'Insurance Brokers of Arizona',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=TZ9e1Sq1WJw&t=39s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Premium is partially based on your total compensation to your employees during '
              'that policy period if you fail to comply with the audit the the insurance '
              'company.',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': 'Premium is partially based on your total compensation to your employees during '
             'that policy period if you fail to comply with the audit the the insurance '
             'company.',
      'title': 'Can I Refuse My Workers Comp Audit? (Insurance Brokers of Arizona)',
      'url': 'https://www.youtube.com/watch?v=TZ9e1Sq1WJw&t=39s',
      'video_id': 'TZ9e1Sq1WJw'},
     {'author': 'MNJ Insurance Solutions, Inc.',
      'channel': 'MNJ Insurance Solutions, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=ymSHX3jpZho&t=120s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Consider but these are just a few suggestions we recommend please contact M&J '
              "Insurance Solutions if you're interested in learning more about our services "
              'and or an analysis of your current benefit offerings and we look forward to '
              'talking with you soon.',
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': 'Consider but these are just a few suggestions we recommend please contact M&J '
             "Insurance Solutions if you're interested in learning more about our services and "
             'or an analysis of your current benefit offerings and we look forward to talking '
             'with you soon.',
      'title': '7 Things to Consider When Choosing an Employee Benefits Broker (MNJ Insurance '
               'Solutions, Inc.)',
      'url': 'https://www.youtube.com/watch?v=ymSHX3jpZho&t=120s',
      'video_id': 'ymSHX3jpZho'},
     {'author': 'Chris The Insurance Guy',
      'channel': 'Chris The Insurance Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:10](https://www.youtube.com/watch?v=l8vsYOmqKB4&t=430s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, these big commissions up front, but the renewals are dropped off '
              "significantly. They go down to like 3% renewal commission. This is why I'm a "
              'big believer in building up a PNC book first to build your foundation and base.',
      'timestamp': 430,
      'timestamp_label': '[00:07:10]',
      'timestamp_seconds': 430,
      'tip': 'So, these big commissions up front, but the renewals are dropped off '
             "significantly. They go down to like 3% renewal commission. This is why I'm a big "
             'believer in building up a PNC book first to build your foundation and base.',
      'title': 'Insurance License Exam: Which License Should I Get in 2026? (Chris The '
               'Insurance Guy)',
      'url': 'https://www.youtube.com/watch?v=l8vsYOmqKB4&t=430s',
      'video_id': 'l8vsYOmqKB4'},
     {'author': 'Conner Strong & Buckelew',
      'channel': 'Conner Strong & Buckelew',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:19](https://www.youtube.com/watch?v=f50x6TivjJ4&t=199s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "In the end you'll get all of the control that comes with self-insurance without "
              'the unexpected roadblocks that could slow you down learn more about captives at '
              'connerstrong.com and choose the path for employee benefits that actually '
              'benefits everyone.',
      'timestamp': 199,
      'timestamp_label': '[00:03:19]',
      'timestamp_seconds': 199,
      'tip': "In the end you'll get all of the control that comes with self-insurance without "
             'the unexpected roadblocks that could slow you down learn more about captives at '
             'connerstrong.com and choose the path for employee benefits that actually '
             'benefits everyone.',
      'title': 'Benefit Captives Explained (Conner Strong & Buckelew)',
      'url': 'https://www.youtube.com/watch?v=f50x6TivjJ4&t=199s',
      'video_id': 'f50x6TivjJ4'},
     {'author': 'synergy.',
      'channel': 'synergy.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:57](https://www.youtube.com/watch?v=6-UxSZMCtMg&t=1017s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The claims administrator which is going to be your bigger insurance company '
              'that is still involved in all of these situations.',
      'timestamp': 1017,
      'timestamp_label': '[00:16:57]',
      'timestamp_seconds': 1017,
      'tip': 'The claims administrator which is going to be your bigger insurance company that '
             'is still involved in all of these situations.',
      'title': 'Effective Techniques for ERISA Lien Negotiation (synergy.)',
      'url': 'https://www.youtube.com/watch?v=6-UxSZMCtMg&t=1017s',
      'video_id': '6-UxSZMCtMg'},
     {'author': 'Matthiesen, Wickert & Lehrer, S.C.',
      'channel': 'Matthiesen, Wickert & Lehrer, S.C.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:22](https://www.youtube.com/watch?v=M-sP3O4XgCs&t=322s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Employee benefit plan but does not regulate insurance and then self-funded '
              'plans generally speaking the preemption is going to apply so long as the law '
              'relates to the employee benefit.',
      'timestamp': 322,
      'timestamp_label': '[00:05:22]',
      'timestamp_seconds': 322,
      'tip': 'Employee benefit plan but does not regulate insurance and then self-funded plans '
             'generally speaking the preemption is going to apply so long as the law relates '
             'to the employee benefit.',
      'title': 'Fully Insured and Non ERISA Plans  Advanced Topics in Preemption and Anti '
               'Subrogation Exceptions (Matthiesen, Wickert & Lehrer, S.C.)',
      'url': 'https://www.youtube.com/watch?v=M-sP3O4XgCs&t=322s',
      'video_id': 'M-sP3O4XgCs'},
     {'author': 'Owen-Dunn',
      'channel': 'Owen-Dunn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:52](https://www.youtube.com/watch?v=lkhC7NvgCI4&t=112s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your group captive insurance company would collectively agree to cover all '
              'member claims up to a set limit typically 350 to 500 thousand dollars to.',
      'timestamp': 112,
      'timestamp_label': '[00:01:52]',
      'timestamp_seconds': 112,
      'tip': 'Your group captive insurance company would collectively agree to cover all '
             'member claims up to a set limit typically 350 to 500 thousand dollars to.',
      'title': 'Member Owned Group Captive Insurance Overview (Owen-Dunn)',
      'url': 'https://www.youtube.com/watch?v=lkhC7NvgCI4&t=112s',
      'video_id': 'lkhC7NvgCI4'},
     {'author': 'PeopleKeep',
      'channel': 'PeopleKeep',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=87JIyLFot-o&t=78s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Expenses must meet the following criteria to be eligible for reimbursement by '
              'your insurance carrier: * It must be an eligible expense as defined in your '
              'benefit plan document. The loss must meet the definition of a loss outlined in '
              'your policy.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'Expenses must meet the following criteria to be eligible for reimbursement by '
             'your insurance carrier: * It must be an eligible expense as defined in your '
             'benefit plan document. The loss must meet the definition of a loss outlined in '
             'your policy.',
      'title': 'What is stop-loss insurance? (PeopleKeep)',
      'url': 'https://www.youtube.com/watch?v=87JIyLFot-o&t=78s',
      'video_id': '87JIyLFot-o'},
     {'author': 'eQuoteMD',
      'channel': 'eQuoteMD',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:38](https://www.youtube.com/watch?v=IeLvLNXVKEo&t=218s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You currently have a medical malpractice insurance policy again I'm tim ryan "
              'here to answer your medical malpractice insurance questions please feel free to '
              'leave a question in the comment section below love to help you out in any way '
              'that I can have a great day.',
      'timestamp': 218,
      'timestamp_label': '[00:03:38]',
      'timestamp_seconds': 218,
      'tip': "You currently have a medical malpractice insurance policy again I'm tim ryan "
             'here to answer your medical malpractice insurance questions please feel free to '
             'leave a question in the comment section below love to help you out in any way '
             'that I can have a great day.',
      'title': 'Broker of Record Letter (BOR) in Medical Malpractice Insurance (eQuoteMD)',
      'url': 'https://www.youtube.com/watch?v=IeLvLNXVKEo&t=218s',
      'video_id': 'IeLvLNXVKEo'},
     {'author': 'American Trust Administrators | Level Funding',
      'channel': 'American Trust Administrators | Level Funding',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:17](https://www.youtube.com/watch?v=8scqEaAolto&t=377s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm selling to my cousin, whatever. Realize fully insurance is probably a "
              "better option. But when they're building something for the long term, 100% "
              'surplus is my true belief, deeply held, is the best way for them to go for '
              'today, tomorrow, and all of the years to come.',
      'timestamp': 377,
      'timestamp_label': '[00:06:17]',
      'timestamp_seconds': 377,
      'tip': "I'm selling to my cousin, whatever. Realize fully insurance is probably a better "
             "option. But when they're building something for the long term, 100% surplus is "
             'my true belief, deeply held, is the best way for them to go for today, tomorrow, '
             'and all of the years to come.',
      'title': 'Fully Insured vs Level-Funded: Which Is Better Long-Term for Small Businesses? '
               '(American Trust Administrators | Level Funding)',
      'url': 'https://www.youtube.com/watch?v=8scqEaAolto&t=377s',
      'video_id': '8scqEaAolto'},
     {'author': 'Vital Vista',
      'channel': 'Vital Vista',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=38sp-qkKLok&t=134s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "There's a TPA working behind the scenes to make your insurance claiming process "
              'as smooth and efficient as possible easing your burden when you need it most '
              'thank you for tuning in to vital Vista until next time stay informed stay '
              'healthy.',
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': "There's a TPA working behind the scenes to make your insurance claiming process "
             'as smooth and efficient as possible easing your burden when you need it most '
             'thank you for tuning in to vital Vista until next time stay informed stay '
             'healthy.',
      'title': 'The role of Third Party Administration in Hospitals | Vital Vista (Vital '
               'Vista)',
      'url': 'https://www.youtube.com/watch?v=38sp-qkKLok&t=134s',
      'video_id': '38sp-qkKLok'},
     {'author': "Amaxx | Workers' Comp for Employers",
      'channel': "Amaxx | Workers' Comp for Employers",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:30](https://www.youtube.com/watch?v=z2GYx81GGEM&t=390s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "On my name is Michael stack I'm the CEO of a max and remember your work today "
              "and workers compensation can have a dramatic impact on your company's bottom "
              "line just as we showed here but it will have a dramatic impact on someone's "
              'life so be great.',
      'timestamp': 390,
      'timestamp_label': '[00:06:30]',
      'timestamp_seconds': 390,
      'tip': "On my name is Michael stack I'm the CEO of a max and remember your work today "
             "and workers compensation can have a dramatic impact on your company's bottom "
             "line just as we showed here but it will have a dramatic impact on someone's life "
             'so be great.',
      'title': "How to Calculate Your Minimum Experience Modification Factor (Amaxx | Workers' "
               'Comp for Employers)',
      'url': 'https://www.youtube.com/watch?v=z2GYx81GGEM&t=390s',
      'video_id': 'z2GYx81GGEM'},
     {'author': 'Self-Funded',
      'channel': 'Self-Funded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:51](https://www.youtube.com/watch?v=4cndcrJWUGg&t=411s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Series of many videos talking about all the ins and outs and provisions '
              'enhancements and strategies around stop-loss but before we get into the really '
              'cool stuff you got to know the basics so thanks for watching have any questions '
              'let me know see you next time.',
      'timestamp': 411,
      'timestamp_label': '[00:06:51]',
      'timestamp_seconds': 411,
      'tip': 'Series of many videos talking about all the ins and outs and provisions '
             'enhancements and strategies around stop-loss but before we get into the really '
             'cool stuff you got to know the basics so thanks for watching have any questions '
             'let me know see you next time.',
      'title': 'Episode 1. Stop Loss Insurance Explained (Self-Funded)',
      'url': 'https://www.youtube.com/watch?v=4cndcrJWUGg&t=411s',
      'video_id': '4cndcrJWUGg'}],
 5: [{'author': 'Micro-Dyn',
      'channel': 'Micro-Dyn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:14](https://www.youtube.com/watch?v=Hz5wBrKavxY&t=74s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "But if providers don't agree, patients may receive a balance bill, meaning they "
              'have to pay the difference. Traditional pricing depends on contracts and '
              'networks. RBP depends on benchmarks and flexibility, but also introduces risks '
              'like billing disputes.',
      'timestamp': 74,
      'timestamp_label': '[00:01:14]',
      'timestamp_seconds': 74,
      'tip': "But if providers don't agree, patients may receive a balance bill, meaning they "
             'have to pay the difference. Traditional pricing depends on contracts and '
             'networks. RBP depends on benchmarks and flexibility, but also introduces risks '
             'like billing disputes.',
      'title': 'Reference-Based Pricing vs. Commercial Claims Pricing: What You NEED to Know '
               '(Micro-Dyn)',
      'url': 'https://www.youtube.com/watch?v=Hz5wBrKavxY&t=74s',
      'video_id': 'Hz5wBrKavxY'},
     {'author': 'AHealthcareZ - Healthcare Finance Explained',
      'channel': 'AHealthcareZ - Healthcare Finance Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:49](https://www.youtube.com/watch?v=wshiRRBh4Gs&t=469s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And older groups are left holding the bag, right? And so, what that does is '
              'that sort of cream as mo- many brokers, if you talk to them, they will tell you '
              'that the fully insured marketplace has essentially pump become a high-risk '
              'pool.',
      'timestamp': 469,
      'timestamp_label': '[00:07:49]',
      'timestamp_seconds': 469,
      'tip': 'And older groups are left holding the bag, right? And so, what that does is that '
             'sort of cream as mo- many brokers, if you talk to them, they will tell you that '
             'the fully insured marketplace has essentially pump become a high-risk pool.',
      'title': 'Level-Funded Health Plans Explained (AHealthcareZ - Healthcare Finance '
               'Explained)',
      'url': 'https://www.youtube.com/watch?v=wshiRRBh4Gs&t=469s',
      'video_id': 'wshiRRBh4Gs'},
     {'author': 'PeopleKeep',
      'channel': 'PeopleKeep',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=o5eOH2AXJAs&t=139s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'A self-funded plan without the hassle or financial risk A stand-alone health '
              'reimbursement arrangement (HRA) provides the benefits of a self-insured health '
              'plan without the potential risks.',
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': 'A self-funded plan without the hassle or financial risk A stand-alone health '
             'reimbursement arrangement (HRA) provides the benefits of a self-insured health '
             'plan without the potential risks.',
      'title': 'Level funded vs. self funded health plans (PeopleKeep)',
      'url': 'https://www.youtube.com/watch?v=o5eOH2AXJAs&t=139s',
      'video_id': 'o5eOH2AXJAs'},
     {'author': 'The Coyle Group - Business Insurance',
      'channel': 'The Coyle Group - Business Insurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:00](https://www.youtube.com/watch?v=Nfw1Tq_wDio&t=420s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Fit for you and your business now let's talk about some common mistakes made by "
              'employers and how to avoid them the most common mistake made by employers '
              'large.',
      'timestamp': 420,
      'timestamp_label': '[00:07:00]',
      'timestamp_seconds': 420,
      'tip': "Fit for you and your business now let's talk about some common mistakes made by "
             'employers and how to avoid them the most common mistake made by employers large.',
      'title': 'Workers Comp ERM or E-Mod Explained (The Coyle Group - Business Insurance)',
      'url': 'https://www.youtube.com/watch?v=Nfw1Tq_wDio&t=420s',
      'video_id': 'Nfw1Tq_wDio'},
     {'author': 'Maximize Asset Protection',
      'channel': 'Maximize Asset Protection',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:56](https://www.youtube.com/watch?v=hqPZ5l67B4A&t=1256s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Risk lies I made a foolish mistake $64,000 just United Healthcare took it and I '
              "don't think we had to claim one not one so it's uh life's lesson so it's It's "
              'Tricky out there for these business.',
      'timestamp': 1256,
      'timestamp_label': '[00:20:56]',
      'timestamp_seconds': 1256,
      'tip': 'Risk lies I made a foolish mistake $64,000 just United Healthcare took it and I '
             "don't think we had to claim one not one so it's uh life's lesson so it's It's "
             'Tricky out there for these business.',
      'title': 'Group Health Insurance Explained: Fully Funded vs. Self-Funded vs. Level '
               'Funded Plans (Maximize Asset Protection)',
      'url': 'https://www.youtube.com/watch?v=hqPZ5l67B4A&t=1256s',
      'video_id': 'hqPZ5l67B4A'},
     {'author': 'Insurance for Entrepreneurs',
      'channel': 'Insurance for Entrepreneurs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=abb1Gjc-5z4&t=59s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, most business owners think their workers comp premium is based on the '
              'insurance company they choose or how good of a deal they can negotiate. But '
              "that's not really how this works. At its core, workers compensation is just a "
              'math problem.',
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': 'Now, most business owners think their workers comp premium is based on the '
             'insurance company they choose or how good of a deal they can negotiate. But '
             "that's not really how this works. At its core, workers compensation is just a "
             'math problem.',
      'title': 'How Workers Compensation Class Codes Impact Premium (Insurance for '
               'Entrepreneurs)',
      'url': 'https://www.youtube.com/watch?v=abb1Gjc-5z4&t=59s',
      'video_id': 'abb1Gjc-5z4'},
     {'author': 'Complete Captive',
      'channel': 'Complete Captive',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:08](https://www.youtube.com/watch?v=PERxwpJ2Rnk&t=608s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "This was helpful next week we're going to talk about something that's near and "
              "dear to me fortuitous risks and risk financing we'll talk next week bye now.",
      'timestamp': 608,
      'timestamp_label': '[00:10:08]',
      'timestamp_seconds': 608,
      'tip': "This was helpful next week we're going to talk about something that's near and "
             "dear to me fortuitous risks and risk financing we'll talk next week bye now.",
      'title': 'Stop Loss Underwriting - Individual vs Block Underwriting (Complete Captive)',
      'url': 'https://www.youtube.com/watch?v=PERxwpJ2Rnk&t=608s',
      'video_id': 'PERxwpJ2Rnk'},
     {'author': 'Multnomah Group, Inc.',
      'channel': 'Multnomah Group, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:03](https://www.youtube.com/watch?v=_QhwEj0_Hrg&t=123s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Concerns brought by participants but having no avenue through which a planned '
              "sponsor can alleviate these concerns or risks makes it unlikely that they'll "
              'continue to want to provide any meaningful retirement benefits to participants.',
      'timestamp': 123,
      'timestamp_label': '[00:02:03]',
      'timestamp_seconds': 123,
      'tip': 'Concerns brought by participants but having no avenue through which a planned '
             "sponsor can alleviate these concerns or risks makes it unlikely that they'll "
             'continue to want to provide any meaningful retirement benefits to participants.',
      'title': 'The Current Landscape of Class Action ERISA Cases (Multnomah Group, Inc.)',
      'url': 'https://www.youtube.com/watch?v=_QhwEj0_Hrg&t=123s',
      'video_id': '_QhwEj0_Hrg'},
     {'author': 'Underwrite University',
      'channel': 'Underwrite University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:58](https://www.youtube.com/watch?v=DHZSiVqJxkY&t=178s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Risk I understand and now stop-loss reinsurance helps insurers handle total '
              "losses ensuring stability even in difficult years that's right it's essential "
              "for managing weather-driven risks in agriculture ensuring insurers aren't "
              'overwhelmed in Bad seasons.',
      'timestamp': 178,
      'timestamp_label': '[00:02:58]',
      'timestamp_seconds': 178,
      'tip': 'Risk I understand and now stop-loss reinsurance helps insurers handle total '
             "losses ensuring stability even in difficult years that's right it's essential "
             "for managing weather-driven risks in agriculture ensuring insurers aren't "
             'overwhelmed in Bad seasons.',
      'title': 'Stop Loss Reinsurance Introductory Course | Learn the Basics of Stop Loss '
               'Reinsurance (Underwrite University)',
      'url': 'https://www.youtube.com/watch?v=DHZSiVqJxkY&t=178s',
      'video_id': 'DHZSiVqJxkY'},
     {'author': 'American Trust Administrators | Level Funding',
      'channel': 'American Trust Administrators | Level Funding',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:55](https://www.youtube.com/watch?v=D3AuT-Ki3nw&t=295s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Side nine times out of 10 and we're never going to catch it up and that's your "
              'problem Mr hospital administrator is a very slick way to use law and.',
      'timestamp': 295,
      'timestamp_label': '[00:04:55]',
      'timestamp_seconds': 295,
      'tip': "Side nine times out of 10 and we're never going to catch it up and that's your "
             'problem Mr hospital administrator is a very slick way to use law and.',
      'title': 'Reference Based Pricing vs PPO: The TRUTH About Fair Pricing, Charge Masters, '
               'and Level-Funded Plans (American Trust Administrators | Level Funding)',
      'url': 'https://www.youtube.com/watch?v=D3AuT-Ki3nw&t=295s',
      'video_id': 'D3AuT-Ki3nw'},
     {'author': 'Security Health Plan',
      'channel': 'Security Health Plan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:44](https://www.youtube.com/watch?v=8FR_2qIAL34&t=284s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Age and health of the employees enrolling in the plan so a healthier workforce '
              'means a lower monthly cost less overall risk for the employer and a greater '
              'possibility for refunds at the end of the run out period.',
      'timestamp': 284,
      'timestamp_label': '[00:04:44]',
      'timestamp_seconds': 284,
      'tip': 'Age and health of the employees enrolling in the plan so a healthier workforce '
             'means a lower monthly cost less overall risk for the employer and a greater '
             'possibility for refunds at the end of the run out period.',
      'title': 'Webinar: Level-Funded Health Plans: A Smart Choice for Employers (Security '
               'Health Plan)',
      'url': 'https://www.youtube.com/watch?v=8FR_2qIAL34&t=284s',
      'video_id': '8FR_2qIAL34'},
     {'author': 'Frier Levitt',
      'channel': 'Frier Levitt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:38](https://www.youtube.com/watch?v=JTumBwWl7Mw&t=1658s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Are available to the pharmacies so and we we have we need to and we have been '
              'and we need to make sure the pharmacies you know do not lose uh any any more '
              'money uh on audit.',
      'timestamp': 1658,
      'timestamp_label': '[00:27:38]',
      'timestamp_seconds': 1658,
      'tip': 'Are available to the pharmacies so and we we have we need to and we have been '
             'and we need to make sure the pharmacies you know do not lose uh any any more '
             'money uh on audit.',
      'title': 'Navigating PBM Audits: Ensuring Pharmacy Compliance and Mitigating Risks '
               '(Frier Levitt)',
      'url': 'https://www.youtube.com/watch?v=JTumBwWl7Mw&t=1658s',
      'video_id': 'JTumBwWl7Mw'},
     {'author': 'Self-Funded',
      'channel': 'Self-Funded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:02](https://www.youtube.com/watch?v=AM2DB13I88c&t=362s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Make sure if you have your administrator filing the claims that they've got "
              'some sort of feed or some sort of process established with.',
      'timestamp': 362,
      'timestamp_label': '[00:06:02]',
      'timestamp_seconds': 362,
      'tip': "Make sure if you have your administrator filing the claims that they've got some "
             'sort of feed or some sort of process established with.',
      'title': 'Episode 20.  Filing Stop Loss Claims (Self-Funded)',
      'url': 'https://www.youtube.com/watch?v=AM2DB13I88c&t=362s',
      'video_id': 'AM2DB13I88c'},
     {'author': 'Medilink Global',
      'channel': 'Medilink Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=Tvw5ziI8ANo&t=111s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Conventional practices which are inefficient and inconvenient to differentiate '
              'your propositions from your competitors to create better opportunity to upsell '
              'and cross-sell your products thank you for watching our video contact us for '
              'more information now.',
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': 'Conventional practices which are inefficient and inconvenient to differentiate '
             'your propositions from your competitors to create better opportunity to upsell '
             'and cross-sell your products thank you for watching our video contact us for '
             'more information now.',
      'title': 'Everything About Third-Party Administrator (TPA) (Medilink Global)',
      'url': 'https://www.youtube.com/watch?v=Tvw5ziI8ANo&t=111s',
      'video_id': 'Tvw5ziI8ANo'},
     {'author': 'Self-Funded',
      'channel': 'Self-Funded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:01](https://www.youtube.com/watch?v=Dy4S9Ie5mEM&t=361s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Hope I hope that helps again hope that stimulated some questions maybe I didn't "
              'explain something thoroughly enough you let me know in the comments below '
              'always good to see you thanks for watching see you next.',
      'timestamp': 361,
      'timestamp_label': '[00:06:01]',
      'timestamp_seconds': 361,
      'tip': "Hope I hope that helps again hope that stimulated some questions maybe I didn't "
             'explain something thoroughly enough you let me know in the comments below always '
             'good to see you thanks for watching see you next.',
      'title': 'Episode 2. Stop Loss Aggregate Corridor Explained (Self-Funded)',
      'url': 'https://www.youtube.com/watch?v=Dy4S9Ie5mEM&t=361s',
      'video_id': 'Dy4S9Ie5mEM'}],
 6: [{'author': 'Vault of Profit',
      'channel': 'Vault of Profit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:11](https://www.youtube.com/watch?v=351RCg-LQ6I&t=971s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Can you aggregate at least 5 million covered employee lives before you attempt '
              'to negotiate your first commercial rebate contract? Do you have the multistate '
              'legal architecture to survive aggressive state transparency laws and federal '
              'anti-kickback scrutiny?',
      'timestamp': 971,
      'timestamp_label': '[00:16:11]',
      'timestamp_seconds': 971,
      'tip': 'Can you aggregate at least 5 million covered employee lives before you attempt '
             'to negotiate your first commercial rebate contract? Do you have the multistate '
             'legal architecture to survive aggressive state transparency laws and federal '
             'anti-kickback scrutiny?',
      'title': 'The Economics of Owning a Pharmacy Benefit Manager PBM (Vault of Profit)',
      'url': 'https://www.youtube.com/watch?v=351RCg-LQ6I&t=971s',
      'video_id': '351RCg-LQ6I'},
     {'author': 'JS Benefits Group',
      'channel': 'JS Benefits Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=6P2sMVFtCtk&t=85s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So before you simply accept your next renewal, take a second look. I'm Jennifer "
              "Shafer with JS Benefits Group. Let's find out what your benefit strategy could "
              'be doing differently.',
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': "So before you simply accept your next renewal, take a second look. I'm Jennifer "
             "Shafer with JS Benefits Group. Let's find out what your benefit strategy could "
             'be doing differently.',
      'title': 'Your Health Insurance Renewal Is Coming  5 Things Employers Should Review '
               '1080p caption (JS Benefits Group)',
      'url': 'https://www.youtube.com/watch?v=6P2sMVFtCtk&t=85s',
      'video_id': '6P2sMVFtCtk'},
     {'author': 'UCPath Center',
      'channel': 'UCPath Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:54](https://www.youtube.com/watch?v=3Mo211tpO_Y&t=894s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Accolid serves as your first point of contact for help with health benefits '
              'questions. You can find the link to the providers in the UC Select and Blue '
              'Shield PPO networks on the ualthplans.',
      'timestamp': 894,
      'timestamp_label': '[00:14:54]',
      'timestamp_seconds': 894,
      'tip': 'Accolid serves as your first point of contact for help with health benefits '
             'questions. You can find the link to the providers in the UC Select and Blue '
             'Shield PPO networks on the ualthplans.',
      'title': 'New Employee Benefits Orientation (NEBO) 2026 for Safe Harbor Employees '
               '(UCPath Center)',
      'url': 'https://www.youtube.com/watch?v=3Mo211tpO_Y&t=894s',
      'video_id': '3Mo211tpO_Y'},
     {'author': 'The Dental Startup Journey with Maritza Duran',
      'channel': 'The Dental Startup Journey with Maritza Duran',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=uSNmcAr95UQ&t=83s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Are some of the benefits and disadvantages of this type of enrollment i'll "
              "start with the positives one benefit that you'll find when you.",
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': "Are some of the benefits and disadvantages of this type of enrollment i'll start "
             "with the positives one benefit that you'll find when you.",
      'title': 'The TRUTH Behind Contracting With Third Party Administrators (TPAs) On Your '
               'Dental Practice (The Dental Startup Journey with Maritza Duran)',
      'url': 'https://www.youtube.com/watch?v=uSNmcAr95UQ&t=83s',
      'video_id': 'uSNmcAr95UQ'},
     {'author': 'Self Insured Reporting',
      'channel': 'Self Insured Reporting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:49](https://www.youtube.com/watch?v=Ci7LnsZjk2g&t=169s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Accurate what we find is that once you take the burden of actually creating the '
              'reports off of the employee benefit broker.',
      'timestamp': 169,
      'timestamp_label': '[00:02:49]',
      'timestamp_seconds': 169,
      'tip': 'Accurate what we find is that once you take the burden of actually creating the '
             'reports off of the employee benefit broker.',
      'title': 'Who is Self Insured Reporting? (Self Insured Reporting)',
      'url': 'https://www.youtube.com/watch?v=Ci7LnsZjk2g&t=169s',
      'video_id': 'Ci7LnsZjk2g'},
     {'author': 'Hint Health',
      'channel': 'Hint Health',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:51](https://www.youtube.com/watch?v=5ztwBEIpJjs&t=1011s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'First study we did not have the detail to really back up the idea that uh '
              "there's less specialist visits but I will say based on the DP doctors that.",
      'timestamp': 1011,
      'timestamp_label': '[00:16:51]',
      'timestamp_seconds': 1011,
      'tip': 'First study we did not have the detail to really back up the idea that uh '
             "there's less specialist visits but I will say based on the DP doctors that.",
      'title': 'Direct Primary Care & Employee Benefits: Cutting Costs, Boosting Value, and '
               'Enhancing Care (Hint Health)',
      'url': 'https://www.youtube.com/watch?v=5ztwBEIpJjs&t=1011s',
      'video_id': '5ztwBEIpJjs'},
     {'author': 'Workers Comp New York',
      'channel': 'Workers Comp New York',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=xRwoIXOTi1E&t=21s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Most of the time, we're going to get a call or an email from an insurance "
              "company saying something along the lines of, “Please find out if your client's "
              "interested and if your client is interested in settling, what's their demand?",
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "Most of the time, we're going to get a call or an email from an insurance "
             "company saying something along the lines of, “Please find out if your client's "
             "interested and if your client is interested in settling, what's their demand?",
      'title': 'Workers Comp Settlement Tips Your Lawyer Won’t Tell You! (Workers Comp New '
               'York)',
      'url': 'https://www.youtube.com/watch?v=xRwoIXOTi1E&t=21s',
      'video_id': 'xRwoIXOTi1E'},
     {'author': 'Self-Funded',
      'channel': 'Self-Funded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:09](https://www.youtube.com/watch?v=DrOopjZtatU&t=1389s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um the AI will automatically assign uh ICD10 codes um CPT codes. It will put in '
              "whatever data you tell it to put in. Um and so you don't have to like manually "
              'search and enter each each thing. We call it click fatigue in the hospital.',
      'timestamp': 1389,
      'timestamp_label': '[00:23:09]',
      'timestamp_seconds': 1389,
      'tip': 'Um the AI will automatically assign uh ICD10 codes um CPT codes. It will put in '
             "whatever data you tell it to put in. Um and so you don't have to like manually "
             'search and enter each each thing. We call it click fatigue in the hospital.',
      'title': 'Why Direct Primary Care Is The Only Way Forward | The Physician Burnout Crisis '
               '(Self-Funded)',
      'url': 'https://www.youtube.com/watch?v=DrOopjZtatU&t=1389s',
      'video_id': 'DrOopjZtatU'},
     {'author': 'AHealthcareZ - Healthcare Finance Explained',
      'channel': 'AHealthcareZ - Healthcare Finance Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:28](https://www.youtube.com/watch?v=vT0NNXYjQ_Y&t=568s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Benefits professional need to explain this to people outside of employee '
              "benefits and so knowing this chart cold is super important for you and that's "
              'what I wanted to leave you with today thank you for watching a healthcare z.',
      'timestamp': 568,
      'timestamp_label': '[00:09:28]',
      'timestamp_seconds': 568,
      'tip': 'Benefits professional need to explain this to people outside of employee '
             "benefits and so knowing this chart cold is super important for you and that's "
             'what I wanted to leave you with today thank you for watching a healthcare z.',
      'title': 'Pharmacy Benefit Managers (PBMs) Explained - Learn How the Money Flows '
               '(AHealthcareZ - Healthcare Finance Explained)',
      'url': 'https://www.youtube.com/watch?v=vT0NNXYjQ_Y&t=568s',
      'video_id': 'vT0NNXYjQ_Y'},
     {'author': 'OneVision',
      'channel': 'OneVision',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:33](https://www.youtube.com/watch?v=ks-F1VjDtk4&t=1353s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Fiduciary process this is nothing to be afraid of you're going to have partners "
              'that are going to help you with the burden associated with the caa but the '
              'first thing you as a fiduciary need to do is to establish that fiduciary '
              'committee.',
      'timestamp': 1353,
      'timestamp_label': '[00:22:33]',
      'timestamp_seconds': 1353,
      'tip': "Fiduciary process this is nothing to be afraid of you're going to have partners "
             'that are going to help you with the burden associated with the caa but the first '
             'thing you as a fiduciary need to do is to establish that fiduciary committee.',
      'title': 'FrontPath  CAA Overview (OneVision)',
      'url': 'https://www.youtube.com/watch?v=ks-F1VjDtk4&t=1353s',
      'video_id': 'ks-F1VjDtk4'},
     {'author': 'Christopher Martens',
      'channel': 'Christopher Martens',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:42](https://www.youtube.com/watch?v=M8zhsS8szwY&t=942s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Client move into a captive and then they're calling all their friends right and "
              "they're in the same industry so the other thing that I'm seeing too is I'm.",
      'timestamp': 942,
      'timestamp_label': '[00:15:42]',
      'timestamp_seconds': 942,
      'tip': "Client move into a captive and then they're calling all their friends right and "
             "they're in the same industry so the other thing that I'm seeing too is I'm.",
      'title': 'Medical Stop Loss Group Captives (Christopher Martens)',
      'url': 'https://www.youtube.com/watch?v=M8zhsS8szwY&t=942s',
      'video_id': 'M8zhsS8szwY'},
     {'author': 'TheSpringGroup',
      'channel': 'TheSpringGroup',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:21](https://www.youtube.com/watch?v=L4bWq8jE_JE&t=201s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Addressed with an actuarial study but first and foremost you must take that '
              'initial step to think about medical stop-loss because that in our view is one '
              'of the only ways you can create a sustainable healthcare solution for your '
              'employees.',
      'timestamp': 201,
      'timestamp_label': '[00:03:21]',
      'timestamp_seconds': 201,
      'tip': 'Addressed with an actuarial study but first and foremost you must take that '
             'initial step to think about medical stop-loss because that in our view is one of '
             'the only ways you can create a sustainable healthcare solution for your '
             'employees.',
      'title': 'Medical Stop Loss in Captives (TheSpringGroup)',
      'url': 'https://www.youtube.com/watch?v=L4bWq8jE_JE&t=201s',
      'video_id': 'L4bWq8jE_JE'},
     {'author': 'Mattingly House',
      'channel': 'Mattingly House',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:45](https://www.youtube.com/watch?v=5rIKr0wfdwo&t=225s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'List of medications that this company will approve for you so part of the PBM '
              'strategy is again developing this formulary and in the uh efforts of developing '
              'this form.',
      'timestamp': 225,
      'timestamp_label': '[00:03:45]',
      'timestamp_seconds': 225,
      'tip': 'List of medications that this company will approve for you so part of the PBM '
             'strategy is again developing this formulary and in the uh efforts of developing '
             'this form.',
      'title': 'PBM Drug Rebates (Mattingly House)',
      'url': 'https://www.youtube.com/watch?v=5rIKr0wfdwo&t=225s',
      'video_id': '5rIKr0wfdwo'},
     {'author': 'Self Insured Reporting',
      'channel': 'Self Insured Reporting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:30](https://www.youtube.com/watch?v=5PxkF9WUCd0&t=630s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'A handful of different things that you can do to actually control those but the '
              'first step is understanding this dynamic of how the dollars even work.',
      'timestamp': 630,
      'timestamp_label': '[00:10:30]',
      'timestamp_seconds': 630,
      'tip': 'A handful of different things that you can do to actually control those but the '
             'first step is understanding this dynamic of how the dollars even work.',
      'title': 'Fully Insured VS Self Insured (Self Insured Reporting)',
      'url': 'https://www.youtube.com/watch?v=5PxkF9WUCd0&t=630s',
      'video_id': '5PxkF9WUCd0'},
     {'author': 'AHealthcareZ - Healthcare Finance Explained',
      'channel': 'AHealthcareZ - Healthcare Finance Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:11](https://www.youtube.com/watch?v=UQkzQUPP8JE&t=551s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "As you're looking at the report and I think you'll find a lot more actionable "
              'intelligence out of those reports than you currently do and thank you for '
              'watching a healthcare z.',
      'timestamp': 551,
      'timestamp_label': '[00:09:11]',
      'timestamp_seconds': 551,
      'tip': "As you're looking at the report and I think you'll find a lot more actionable "
             'intelligence out of those reports than you currently do and thank you for '
             'watching a healthcare z.',
      'title': 'How to Read Healthcare Reports: Analyze Employer Claims Data (AHealthcareZ - '
               'Healthcare Finance Explained)',
      'url': 'https://www.youtube.com/watch?v=UQkzQUPP8JE&t=551s',
      'video_id': 'UQkzQUPP8JE'}],
 7: [{'author': 'Medical Lien Management, Inc.',
      'channel': 'Medical Lien Management, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:50](https://www.youtube.com/watch?v=k60NAIUrnWA&t=770s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "It's the beginning of a conversation, not the end of one. What are the tactical "
              'steps? Step one, verify timelines and authority. Is the audit within the legal '
              'look back period for your state. Does this third party auditor even have the '
              'authority to demand this money?',
      'timestamp': 770,
      'timestamp_label': '[00:12:50]',
      'timestamp_seconds': 770,
      'tip': "It's the beginning of a conversation, not the end of one. What are the tactical "
             'steps? Step one, verify timelines and authority. Is the audit within the legal '
             'look back period for your state. Does this third party auditor even have the '
             'authority to demand this money?',
      'title': 'Workers Comp Unwrapped 403; Retroactive Denials & Overpayment Audits: When '
               'Paid Claims Get Pulled... (Medical Lien Management, Inc.)',
      'url': 'https://www.youtube.com/watch?v=k60NAIUrnWA&t=770s',
      'video_id': 'k60NAIUrnWA'},
     {'author': 'rodneymattos',
      'channel': 'rodneymattos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:01](https://www.youtube.com/watch?v=bmIls2hM4uk&t=481s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You're allowed to see the numbers. Start with the one about your advisor. Has "
              'anyone ever shown you how your benefits advisor gets paid? Tell me yes or no '
              'and what your 2027 renewal came in at in the comments. Just comment paid and '
              'the checklist is yours.',
      'timestamp': 481,
      'timestamp_label': '[00:08:01]',
      'timestamp_seconds': 481,
      'tip': "You're allowed to see the numbers. Start with the one about your advisor. Has "
             'anyone ever shown you how your benefits advisor gets paid? Tell me yes or no and '
             'what your 2027 renewal came in at in the comments. Just comment paid and the '
             'checklist is yours.',
      'title': "I'm a Benefits Advisor. Here's Who Gets Paid When Your Health Insurance Goes "
               'Up (rodneymattos)',
      'url': 'https://www.youtube.com/watch?v=bmIls2hM4uk&t=481s',
      'video_id': 'bmIls2hM4uk'},
     {'author': 'American Trust Administrators | Level Funding',
      'channel': 'American Trust Administrators | Level Funding',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:35](https://www.youtube.com/watch?v=ise8qdroICE&t=155s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Number two, there's other stuff you're going to need, but these are the big "
              "ones. You're going to need your quarterly wage and tax for the underwriting "
              'process.',
      'timestamp': 155,
      'timestamp_label': '[00:02:35]',
      'timestamp_seconds': 155,
      'tip': "Number two, there's other stuff you're going to need, but these are the big "
             "ones. You're going to need your quarterly wage and tax for the underwriting "
             'process.',
      'title': 'Why buy Level-Funded Health Plans (Broker Step-by-Step questions + value '
               'explained vs fully insured) (American Trust Administrators | Level Funding)',
      'url': 'https://www.youtube.com/watch?v=ise8qdroICE&t=155s',
      'video_id': 'ise8qdroICE'},
     {'author': 'CancerCare',
      'channel': 'CancerCare',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:16](https://www.youtube.com/watch?v=f8oI5KtxoXM&t=256s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Anytime your doctor prescribes a new drug, ask if it might trigger step '
              'therapy. If it might, ask if there is an alternate drug that would work for '
              'you. Your doctor may also be able to request an exception for you based on '
              'medical necessity.',
      'timestamp': 256,
      'timestamp_label': '[00:04:16]',
      'timestamp_seconds': 256,
      'tip': 'Anytime your doctor prescribes a new drug, ask if it might trigger step therapy. '
             'If it might, ask if there is an alternate drug that would work for you. Your '
             'doctor may also be able to request an exception for you based on medical '
             'necessity.',
      'title': 'What is a Pharmacy Benefit Manager (PBM)? (CancerCare)',
      'url': 'https://www.youtube.com/watch?v=f8oI5KtxoXM&t=256s',
      'video_id': 'f8oI5KtxoXM'},
     {'author': 'Star Health Insurance',
      'channel': 'Star Health Insurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:16](https://www.youtube.com/watch?v=8lgOh6rb92g&t=16s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Cinema select your seats and your movie tickets are booked now in this process '
              "book my show app doesn't own the cinema Hall instead it's a mediator between "
              'you.',
      'timestamp': 16,
      'timestamp_label': '[00:00:16]',
      'timestamp_seconds': 16,
      'tip': 'Cinema select your seats and your movie tickets are booked now in this process '
             "book my show app doesn't own the cinema Hall instead it's a mediator between "
             'you.',
      'title': 'What is Third Party Administrator in Health Insurance | TPA Explained | Star '
               'Health Insurance (Star Health Insurance)',
      'url': 'https://www.youtube.com/watch?v=8lgOh6rb92g&t=16s',
      'video_id': '8lgOh6rb92g'},
     {'author': 'Wade Associates',
      'channel': 'Wade Associates',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=dLKCbT6-S3c&t=30s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And below one based on your injury history and ultimately determines how much '
              "you pay for workers comp but let's take it a step further if the mod is.",
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'And below one based on your injury history and ultimately determines how much '
             "you pay for workers comp but let's take it a step further if the mod is.",
      'title': 'The Workers Compensation Experience Mod | How Low Can It Go? (Wade Associates)',
      'url': 'https://www.youtube.com/watch?v=dLKCbT6-S3c&t=30s',
      'video_id': 'dLKCbT6-S3c'},
     {'author': 'This STUFF is complicated',
      'channel': 'This STUFF is complicated',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:20](https://www.youtube.com/watch?v=q36fieahkDs&t=260s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "There's eligibility requirements, there's plan requirements. They need to make "
              "sure the documents line up. They need to review all the claims. It's not an "
              'instantaneous process. And this is what you did when you ran a third party '
              'administrator.',
      'timestamp': 260,
      'timestamp_label': '[00:04:20]',
      'timestamp_seconds': 260,
      'tip': "There's eligibility requirements, there's plan requirements. They need to make "
             "sure the documents line up. They need to review all the claims. It's not an "
             'instantaneous process. And this is what you did when you ran a third party '
             'administrator.',
      'title': 'This STUFF Is Complicated. Episode : Stop Loss is a reimbursement. (This STUFF '
               'is complicated)',
      'url': 'https://www.youtube.com/watch?v=q36fieahkDs&t=260s',
      'video_id': 'q36fieahkDs'},
     {'author': 'Tyler Dutchover',
      'channel': 'Tyler Dutchover',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:18](https://www.youtube.com/watch?v=ExcUj28jzzc&t=138s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Instead of paying a flat amount to an insurance company, your monthly payment '
              'is split into three separate buckets. This goes to a third-party administrator '
              'to handle the paperwork, print the insurance cards, process the claims.',
      'timestamp': 138,
      'timestamp_label': '[00:02:18]',
      'timestamp_seconds': 138,
      'tip': 'Instead of paying a flat amount to an insurance company, your monthly payment is '
             'split into three separate buckets. This goes to a third-party administrator to '
             'handle the paperwork, print the insurance cards, process the claims.',
      'title': 'Level Funded Health Plans Explained - in Plain English (Tyler Dutchover)',
      'url': 'https://www.youtube.com/watch?v=ExcUj28jzzc&t=138s',
      'video_id': 'ExcUj28jzzc'},
     {'author': 'Self-Funded',
      'channel': 'Self-Funded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:01](https://www.youtube.com/watch?v=I7g6idLkgrc&t=181s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Types and over 20 benefit lines and point Solutions plansight is the only '
              "end-to-end RFP technology on the market today let's modernize your RFP process.",
      'timestamp': 181,
      'timestamp_label': '[00:03:01]',
      'timestamp_seconds': 181,
      'tip': 'Types and over 20 benefit lines and point Solutions plansight is the only '
             "end-to-end RFP technology on the market today let's modernize your RFP process.",
      'title': 'The CAA 101 - Comply or Die? (Self-Funded)',
      'url': 'https://www.youtube.com/watch?v=I7g6idLkgrc&t=181s',
      'video_id': 'I7g6idLkgrc'},
     {'author': 'Mel 😊 DeWeese',
      'channel': 'Mel 😊 DeWeese',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:06](https://www.youtube.com/watch?v=k0FZkQKH4SQ&t=486s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Would be surprised on how many hands are involved in between that process and '
              'there are rebates there are pbms there are all sorts of different money '
              'changing exchanges done in between those two endpoints.',
      'timestamp': 486,
      'timestamp_label': '[00:08:06]',
      'timestamp_seconds': 486,
      'tip': 'Would be surprised on how many hands are involved in between that process and '
             'there are rebates there are pbms there are all sorts of different money changing '
             'exchanges done in between those two endpoints.',
      'title': 'Cracking the Code: What Employers MUST Know about the CAA  (Consolidated '
               'Appropriations Act of 2021) (Mel 😊 DeWeese)',
      'url': 'https://www.youtube.com/watch?v=k0FZkQKH4SQ&t=486s',
      'video_id': 'k0FZkQKH4SQ'},
     {'author': 'Brantley Center',
      'channel': 'Brantley Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:50](https://www.youtube.com/watch?v=gVehEbhOJR4&t=290s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Things like the bonus programs health insurance logistics traditional versus '
              'Roth IRA accounts where to allocate your 401k contributions but the program '
              'also did not deep into a job market career one step ahead of your peers when '
              'you take classes.',
      'timestamp': 290,
      'timestamp_label': '[00:04:50]',
      'timestamp_seconds': 290,
      'tip': 'Things like the bonus programs health insurance logistics traditional versus '
             'Roth IRA accounts where to allocate your 401k contributions but the program also '
             'did not deep into a job market career one step ahead of your peers when you take '
             'classes.',
      'title': 'Learn More About the Employee Benefits Program - Brantley Risk & Insurance '
               'Center, Appalachian State (Brantley Center)',
      'url': 'https://www.youtube.com/watch?v=gVehEbhOJR4&t=290s',
      'video_id': 'gVehEbhOJR4'},
     {'author': 'QuickKnowledge',
      'channel': 'QuickKnowledge',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:02](https://www.youtube.com/watch?v=EoL1_du94c4&t=182s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Company for detailed information regarding the claims process and TPA specific '
              'guidelines thank you for watching our video we hope you enjoyed it stay tuned '
              'for more exciting content coming your way thank you and see you soon.',
      'timestamp': 182,
      'timestamp_label': '[00:03:02]',
      'timestamp_seconds': 182,
      'tip': 'Company for detailed information regarding the claims process and TPA specific '
             'guidelines thank you for watching our video we hope you enjoyed it stay tuned '
             'for more exciting content coming your way thank you and see you soon.',
      'title': 'Demystifying TPA in Health Insurance - Unravel the mystery behind Third Party '
               'Administrators (TPAs) (QuickKnowledge)',
      'url': 'https://www.youtube.com/watch?v=EoL1_du94c4&t=182s',
      'video_id': 'EoL1_du94c4'},
     {'author': 'Workers Compensation',
      'channel': 'Workers Compensation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:15](https://www.youtube.com/watch?v=S5nWU0Y_RpU&t=135s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Soap notes and ledgers we'll arrange a courier to securely deliver the files to "
              'our corporate office remember we can go back as far as seven years with our '
              "recovery process after we get the files you just sit back and we'll take care "
              'of the rest.',
      'timestamp': 135,
      'timestamp_label': '[00:02:15]',
      'timestamp_seconds': 135,
      'tip': "Soap notes and ledgers we'll arrange a courier to securely deliver the files to "
             'our corporate office remember we can go back as far as seven years with our '
             "recovery process after we get the files you just sit back and we'll take care of "
             'the rest.',
      'title': "Workers' Compensation Claims Recovery - We Don't Get Paid, Unless You Get "
               'Paid! (Workers Compensation)',
      'url': 'https://www.youtube.com/watch?v=S5nWU0Y_RpU&t=135s',
      'video_id': 'S5nWU0Y_RpU'},
     {'author': 'AHealthcareZ - Healthcare Finance Explained',
      'channel': 'AHealthcareZ - Healthcare Finance Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:04](https://www.youtube.com/watch?v=0XFk1m3yGuY&t=244s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Medicaid as well then what's going on at the municipality level what's going on "
              "at the school system level what's going on at the private employer level and "
              "I'll just ask you to think about that and that's my point for today thank you "
              'for watching a healthcare z.',
      'timestamp': 244,
      'timestamp_label': '[00:04:04]',
      'timestamp_seconds': 244,
      'tip': "Medicaid as well then what's going on at the municipality level what's going on "
             "at the school system level what's going on at the private employer level and "
             "I'll just ask you to think about that and that's my point for today thank you "
             'for watching a healthcare z.',
      'title': 'PBM Spread Pricing for Generic Prescriptions Explained (AHealthcareZ - '
               'Healthcare Finance Explained)',
      'url': 'https://www.youtube.com/watch?v=0XFk1m3yGuY&t=244s',
      'video_id': '0XFk1m3yGuY'},
     {'author': 'Self-Funded',
      'channel': 'Self-Funded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=8nD9sJwgMdE&t=139s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "In a captive space so I'd say it's good for all employees today right groups "
              'coming from fully insured groups that are Level funded you know groups existing '
              'self-funded groups bigger groups that are self.',
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': "In a captive space so I'd say it's good for all employees today right groups "
             'coming from fully insured groups that are Level funded you know groups existing '
             'self-funded groups bigger groups that are self.',
      'title': 'Part 8 - Benefit Captives (Self-Funded)',
      'url': 'https://www.youtube.com/watch?v=8nD9sJwgMdE&t=139s',
      'video_id': '8nD9sJwgMdE'}],
 8: [{'author': 'Ameriflex',
      'channel': 'Ameriflex',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:53](https://www.youtube.com/watch?v=l5tGs_zQ8xA&t=53s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And so we got way out in front of it and decided to really dive deep into the '
              'the Consolidated Appropriations Act, affectionately referred to as the CAA. So '
              '2021 is when it came about, so during COVID.',
      'timestamp': 53,
      'timestamp_label': '[00:00:53]',
      'timestamp_seconds': 53,
      'tip': 'And so we got way out in front of it and decided to really dive deep into the '
             'the Consolidated Appropriations Act, affectionately referred to as the CAA. So '
             '2021 is when it came about, so during COVID.',
      'title': 'Consolidated Appropriations Act (Ameriflex)',
      'url': 'https://www.youtube.com/watch?v=l5tGs_zQ8xA&t=53s',
      'video_id': 'l5tGs_zQ8xA'},
     {'author': 'National Drug Screening',
      'channel': 'National Drug Screening',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:41](https://www.youtube.com/watch?v=_gOdH2UYKBs&t=581s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll see all our information about our services as a Third Party Administrator. "
              'We have very robust software. You can schedule a drug test electronically, you '
              'can get results back by email, you can access our web portal to get results '
              'back.',
      'timestamp': 581,
      'timestamp_label': '[00:09:41]',
      'timestamp_seconds': 581,
      'tip': "'ll see all our information about our services as a Third Party Administrator. "
             'We have very robust software. You can schedule a drug test electronically, you '
             'can get results back by email, you can access our web portal to get results '
             'back.',
      'title': 'What is a TPA and what do they do? (Third Party Administrator) (National Drug '
               'Screening)',
      'url': 'https://www.youtube.com/watch?v=_gOdH2UYKBs&t=581s',
      'video_id': '_gOdH2UYKBs'},
     {'author': 'Partners MGU',
      'channel': 'Partners MGU',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:28](https://www.youtube.com/watch?v=YEFRBSmT3IE&t=208s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Dealing with and seen across our industry when it comes to balance billing et '
              "cetera that's still going to continue it's only.",
      'timestamp': 208,
      'timestamp_label': '[00:03:28]',
      'timestamp_seconds': 208,
      'tip': 'Dealing with and seen across our industry when it comes to balance billing et '
             "cetera that's still going to continue it's only.",
      'title': 'How Surprise Billing Impacts Reference-Based Pricing (Partners MGU)',
      'url': 'https://www.youtube.com/watch?v=YEFRBSmT3IE&t=208s',
      'video_id': 'YEFRBSmT3IE'},
     {'author': 'SmithRx',
      'channel': 'SmithRx',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=KB9tHMlyhyA&t=80s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'By having this platform-based structure, it allows us to operate in a world of '
              "true transparency. We're able to share insights, provide information to not "
              'only patients but plan sponsors and ecosystem partners as well.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': 'By having this platform-based structure, it allows us to operate in a world of '
             "true transparency. We're able to share insights, provide information to not only "
             'patients but plan sponsors and ecosystem partners as well.',
      'title': 'Modern PBM 101 with Alan Pannier, PharmD, MBA: Transparency (SmithRx)',
      'url': 'https://www.youtube.com/watch?v=KB9tHMlyhyA&t=80s',
      'video_id': 'KB9tHMlyhyA'},
     {'author': 'Benefit Whisperer',
      'channel': 'Benefit Whisperer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:41](https://www.youtube.com/watch?v=nrL0pYx-hQo&t=701s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Um, and we definitely got a great response. We're like, oh my gosh, we got to "
              "really staff up this nonprofit. Um, so like on the data platform, we've got "
              'seven companies, um, in production and another 20 that are kind of waiting in '
              'the wings.',
      'timestamp': 701,
      'timestamp_label': '[00:11:41]',
      'timestamp_seconds': 701,
      'tip': "Um, and we definitely got a great response. We're like, oh my gosh, we got to "
             "really staff up this nonprofit. Um, so like on the data platform, we've got "
             'seven companies, um, in production and another 20 that are kind of waiting in '
             'the wings.',
      'title': 'Dave Chase, CEO of Health Rosetta, Exposes the $5 Trillion Healthcare Scam '
               'Employers are Funding (Benefit Whisperer)',
      'url': 'https://www.youtube.com/watch?v=nrL0pYx-hQo&t=701s',
      'video_id': 'nrL0pYx-hQo'},
     {'author': 'Beyond Business Insurance',
      'channel': 'Beyond Business Insurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:52](https://www.youtube.com/watch?v=rnj58CEkGiE&t=232s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Letter is essentially kind of working for free until your new policy takes '
              "place so this is broker of record letters don't hate them I think they're a "
              "great tool if you understand what you're signing if you like this give it a "
              'thumbs up thanks for watching.',
      'timestamp': 232,
      'timestamp_label': '[00:03:52]',
      'timestamp_seconds': 232,
      'tip': 'Letter is essentially kind of working for free until your new policy takes place '
             "so this is broker of record letters don't hate them I think they're a great tool "
             "if you understand what you're signing if you like this give it a thumbs up "
             'thanks for watching.',
      'title': 'Broker of Record Letter - MYTHS BUSTED - Business Insurance (Beyond Business '
               'Insurance)',
      'url': 'https://www.youtube.com/watch?v=rnj58CEkGiE&t=232s',
      'video_id': 'rnj58CEkGiE'},
     {'author': 'Captive Resources',
      'channel': 'Captive Resources',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:15](https://www.youtube.com/watch?v=BQVeLgnIx8A&t=975s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Then, it's incredibly important to talk about all of the other aspects that the "
              "captive's going to bring to the table, including the data analytics and the "
              "other ways to control the other piece that they're likely not looking at within "
              'that analysis.',
      'timestamp': 975,
      'timestamp_label': '[00:16:15]',
      'timestamp_seconds': 975,
      'tip': "Then, it's incredibly important to talk about all of the other aspects that the "
             "captive's going to bring to the table, including the data analytics and the "
             "other ways to control the other piece that they're likely not looking at within "
             'that analysis.',
      'title': 'Health Captive Fundamentals: Traditional Stop Loss vs. Captive Stop Loss '
               '(Captive Resources)',
      'url': 'https://www.youtube.com/watch?v=BQVeLgnIx8A&t=975s',
      'video_id': 'BQVeLgnIx8A'},
     {'author': 'Dysrupt Healthcare Podcast',
      'channel': 'Dysrupt Healthcare Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=xVuFXA-gN8g&t=15s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Health benefits  industry and now here's your host Healthcare benefits industry "
              'expert and.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Health benefits  industry and now here's your host Healthcare benefits industry "
             'expert and.',
      'title': 'Is Reference-Based Pricing (RBP) Really That Controversial? (Dysrupt '
               'Healthcare Podcast)',
      'url': 'https://www.youtube.com/watch?v=xVuFXA-gN8g&t=15s',
      'video_id': 'xVuFXA-gN8g'},
     {'author': 'Colony Solutions - Business Insurance',
      'channel': 'Colony Solutions - Business Insurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=KAFn9iNy8cA&t=38s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'ve ever done any research on it asked any questions about it or even asked "
              'your insurance professional they broke out a hieroglyphic esque multiplication '
              'platform to try to explain it to you. What an X-mod is, how it works, and how '
              'you could use it to your advantage.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': "'ve ever done any research on it asked any questions about it or even asked your "
             'insurance professional they broke out a hieroglyphic esque multiplication '
             'platform to try to explain it to you. What an X-mod is, how it works, and how '
             'you could use it to your advantage.',
      'title': 'WORKERS COMP X-MOD | Demystifying The Experience Modification on Workers '
               'Compensation Insurance (Colony Solutions - Business Insurance)',
      'url': 'https://www.youtube.com/watch?v=KAFn9iNy8cA&t=38s',
      'video_id': 'KAFn9iNy8cA'},
     {'author': 'WorkCompConsultants',
      'channel': 'WorkCompConsultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:07](https://www.youtube.com/watch?v=FqRH7WDe5RQ&t=67s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'They gather data analyze and prepare workers comp industry Trends they provide '
              'rate making recommendations and proposed legislative impact studies to about 40 '
              'different state governments and over 900 insurance companies.',
      'timestamp': 67,
      'timestamp_label': '[00:01:07]',
      'timestamp_seconds': 67,
      'tip': 'They gather data analyze and prepare workers comp industry Trends they provide '
             'rate making recommendations and proposed legislative impact studies to about 40 '
             'different state governments and over 900 insurance companies.',
      'title': 'Workers Comp NCCI Rules and Procedures.wmv (WorkCompConsultants)',
      'url': 'https://www.youtube.com/watch?v=FqRH7WDe5RQ&t=67s',
      'video_id': 'FqRH7WDe5RQ'},
     {'author': 'Scott Simmonds',
      'channel': 'Scott Simmonds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=UkIk-T0NP3M&t=98s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Clerical the second column is the expected loss ratio this is a factor '
              'determined by Actuarial data each classification has its own unique ELR.',
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': 'Clerical the second column is the expected loss ratio this is a factor '
             'determined by Actuarial data each classification has its own unique ELR.',
      'title': 'Workers Compensation Insurance Experience Mod Worksheet (Scott Simmonds)',
      'url': 'https://www.youtube.com/watch?v=UkIk-T0NP3M&t=98s',
      'video_id': 'UkIk-T0NP3M'},
     {'author': "Amaxx | Workers' Comp for Employers",
      'channel': "Amaxx | Workers' Comp for Employers",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:48](https://www.youtube.com/watch?v=dBmf0MgN4_g&t=288s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Vs SWAT messeger intumescent main port account against other species reading '
              'matt lip rouge Edition grade in turn The World Cup I-provn in Places and Script '
              'data takistan game American Ball will have occurred on some sort of England đ.',
      'timestamp': 288,
      'timestamp_label': '[00:04:48]',
      'timestamp_seconds': 288,
      'tip': 'Vs SWAT messeger intumescent main port account against other species reading '
             'matt lip rouge Edition grade in turn The World Cup I-provn in Places and Script '
             'data takistan game American Ball will have occurred on some sort of England đ.',
      'title': 'The Experience Rating Adjustment in the Workers’ Comp Experience Mod (Amaxx | '
               "Workers' Comp for Employers)",
      'url': 'https://www.youtube.com/watch?v=dBmf0MgN4_g&t=288s',
      'video_id': 'dBmf0MgN4_g'},
     {'author': 'ParetoHealth',
      'channel': 'ParetoHealth',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:19](https://www.youtube.com/watch?v=4VhWXTCGo74&t=619s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Lot of times it's a conceptual sale right and we're trying to get into the "
              'concept so the make sure the concept makes sense so you can see where the '
              "opportunity comes in so I think we've covered.",
      'timestamp': 619,
      'timestamp_label': '[00:10:19]',
      'timestamp_seconds': 619,
      'tip': "Lot of times it's a conceptual sale right and we're trying to get into the "
             'concept so the make sure the concept makes sense so you can see where the '
             "opportunity comes in so I think we've covered.",
      'title': 'Specific vs. Aggregate Stop-Loss (ParetoHealth)',
      'url': 'https://www.youtube.com/watch?v=4VhWXTCGo74&t=619s',
      'video_id': '4VhWXTCGo74'},
     {'author': 'Foundation Benefits',
      'channel': 'Foundation Benefits',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:25](https://www.youtube.com/watch?v=R-MOuJrCG9Q&t=265s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Thing to do we always suggest using a TPA to help out with that because it just '
              'makes it easy if you have any questions about that please feel free to reach '
              'out to us I appreciate it and let us know if you have any questions.',
      'timestamp': 265,
      'timestamp_label': '[00:04:25]',
      'timestamp_seconds': 265,
      'tip': 'Thing to do we always suggest using a TPA to help out with that because it just '
             'makes it easy if you have any questions about that please feel free to reach out '
             'to us I appreciate it and let us know if you have any questions.',
      'title': 'Understanding Form 5500 (Foundation Benefits)',
      'url': 'https://www.youtube.com/watch?v=R-MOuJrCG9Q&t=265s',
      'video_id': 'R-MOuJrCG9Q'},
     {'author': 'Self-Funded',
      'channel': 'Self-Funded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:26](https://www.youtube.com/watch?v=hiWm3Y4k6SI&t=386s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Happening and also I have a bonus video plan it'll be pretty short but we're "
              'going to talk about something really cool called leverage trend again thanks '
              'for watching see you guys next time.',
      'timestamp': 386,
      'timestamp_label': '[00:06:26]',
      'timestamp_seconds': 386,
      'tip': "Happening and also I have a bonus video plan it'll be pretty short but we're "
             'going to talk about something really cool called leverage trend again thanks for '
             'watching see you guys next time.',
      'title': 'Episode 3. Stop Loss Lasers (Self-Funded)',
      'url': 'https://www.youtube.com/watch?v=hiWm3Y4k6SI&t=386s',
      'video_id': 'hiWm3Y4k6SI'}],
 9: [{'author': 'IBOR – Institutional Broker of Record Services',
      'channel': 'IBOR – Institutional Broker of Record Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=kqXSkncSX7Y&t=55s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, the team keeps continuity while the license framework sits in place. That '
              'support can include compliance review, file support, agreement execution, and '
              'license supervision in the states where those functions need to be formally '
              'covered.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'So, the team keeps continuity while the license framework sits in place. That '
             'support can include compliance review, file support, agreement execution, and '
             'license supervision in the states where those functions need to be formally '
             'covered.',
      'title': 'Broker of Record for NNN Retail Portfolios (IBOR – Institutional Broker of '
               'Record Services)',
      'url': 'https://www.youtube.com/watch?v=kqXSkncSX7Y&t=55s',
      'video_id': 'kqXSkncSX7Y'},
     {'author': 'HUB Midwest East (fka Henriott)',
      'channel': 'HUB Midwest East (fka Henriott)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=JY_hbh9Kxrc&t=103s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Compliance with the new regulations regarding the gag Clause they also need to '
              'attest every single year by December 31st that their insurance and their '
              "Pharmacy benefit contracts are compliant with the new regularization um it's "
              'called the gag Clause.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': 'Compliance with the new regulations regarding the gag Clause they also need to '
             'attest every single year by December 31st that their insurance and their '
             "Pharmacy benefit contracts are compliant with the new regularization um it's "
             'called the gag Clause.',
      'title': "Henriott's Chad Burdo on the Gag Clause in the Consolidated Appropriations Act "
               '(HUB Midwest East (fka Henriott))',
      'url': 'https://www.youtube.com/watch?v=JY_hbh9Kxrc&t=103s',
      'video_id': 'JY_hbh9Kxrc'},
     {'author': 'Butch Zemar',
      'channel': 'Butch Zemar',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:34](https://www.youtube.com/watch?v=2DrBScDIwrk&t=394s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Find out a little bit more but let's dive a little bit more in into the value "
              'that insurance breaker brokers come to in terms of money commissions is a hard.',
      'timestamp': 394,
      'timestamp_label': '[00:06:34]',
      'timestamp_seconds': 394,
      'tip': "Find out a little bit more but let's dive a little bit more in into the value "
             'that insurance breaker brokers come to in terms of money commissions is a hard.',
      'title': 'Resources to Solve Employee Benefits Problems - The Value of an Broker (Butch '
               'Zemar)',
      'url': 'https://www.youtube.com/watch?v=2DrBScDIwrk&t=394s',
      'video_id': '2DrBScDIwrk'},
     {'author': 'FOX 35 Orlando',
      'channel': 'FOX 35 Orlando',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=cPJFKseasX0&t=72s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The state's plan includes prohibiting PBMs from mandating mail order pharmacies "
              'for patients ensures that no Florida based PBM mandates a narrow network of '
              "affiliated pharmacies and preserves patient's ability to use their own "
              'community Pharmacist.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': "The state's plan includes prohibiting PBMs from mandating mail order pharmacies "
             'for patients ensures that no Florida based PBM mandates a narrow network of '
             "affiliated pharmacies and preserves patient's ability to use their own community "
             'Pharmacist.',
      'title': 'What pharmacy benefit managers? (FOX 35 Orlando)',
      'url': 'https://www.youtube.com/watch?v=cPJFKseasX0&t=72s',
      'video_id': 'cPJFKseasX0'},
     {'author': 'AHealthcareZ - Healthcare Finance Explained',
      'channel': 'AHealthcareZ - Healthcare Finance Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:52](https://www.youtube.com/watch?v=gpm3vtKEf5U&t=172s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Were receiving in tax benefits from the state so it was almost equal so '
              'remember brother did this analysis.',
      'timestamp': 172,
      'timestamp_label': '[00:02:52]',
      'timestamp_seconds': 172,
      'tip': 'Were receiving in tax benefits from the state so it was almost equal so remember '
             'brother did this analysis.',
      'title': '7 Best Practices in Reference-Based Pricing Negotiation (AHealthcareZ - '
               'Healthcare Finance Explained)',
      'url': 'https://www.youtube.com/watch?v=gpm3vtKEf5U&t=172s',
      'video_id': 'gpm3vtKEf5U'},
     {'author': 'WPS Health',
      'channel': 'WPS Health',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=g_TZcndr5ds&t=75s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Self-funded plans are often more flexible because they are subject to fewer '
              'state regulations or requirements. Self-funded puts employers in the driver’s '
              'seat. They fund the health plan and make the benefit decisions.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': 'Self-funded plans are often more flexible because they are subject to fewer '
             'state regulations or requirements. Self-funded puts employers in the driver’s '
             'seat. They fund the health plan and make the benefit decisions.',
      'title': 'Self funded vs fully insured health plans | WPS explains (WPS Health)',
      'url': 'https://www.youtube.com/watch?v=g_TZcndr5ds&t=75s',
      'video_id': 'g_TZcndr5ds'},
     {'author': 'American Health Law Association',
      'channel': 'American Health Law Association',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=bO0c-bD-CEA&t=21s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'PBMs and their role in drug pricing, as well as the increasing scrutiny of the '
              "industry at the both the federal and state level. I'm a partner in the "
              'healthcare and life sciences practice at Covington & Burling, based in '
              'Washington D.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'PBMs and their role in drug pricing, as well as the increasing scrutiny of the '
             "industry at the both the federal and state level. I'm a partner in the "
             'healthcare and life sciences practice at Covington & Burling, based in '
             'Washington D.',
      'title': 'The Evolving Landscape of the PBM Industry (American Health Law Association)',
      'url': 'https://www.youtube.com/watch?v=bO0c-bD-CEA&t=21s',
      'video_id': 'bO0c-bD-CEA'},
     {'author': 'Benefit Whisperer',
      'channel': 'Benefit Whisperer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=6E1eObzSNLc&t=65s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So if that person has 500,000 in eligible claims, for example, normally it '
              "would kick in after 150 for him. So you're on the hook for an extra 350,000. "
              "Total, you could be on the hook for 450 if it exceeds 600,000. So know what's "
              'in your contract.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': 'So if that person has 500,000 in eligible claims, for example, normally it would '
             "kick in after 150 for him. So you're on the hook for an extra 350,000. Total, "
             "you could be on the hook for 450 if it exceeds 600,000. So know what's in your "
             'contract.',
      'title': 'Stop-Loss Laser Explained: The $450,000 Hidden Risk in Your Renewal (Benefit '
               'Whisperer)',
      'url': 'https://www.youtube.com/watch?v=6E1eObzSNLc&t=65s',
      'video_id': '6E1eObzSNLc'},
     {'author': 'Walsh Insurance',
      'channel': 'Walsh Insurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:19](https://www.youtube.com/watch?v=9hPiS9wv_F4&t=1159s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "It ups our obligation in terms of our fiduciary role and you know I'm going to "
              'talk through a number of these caa provisions that are in effect currently and '
              'again a common thread throughout all of them is this increased access to '
              'information.',
      'timestamp': 1159,
      'timestamp_label': '[00:19:19]',
      'timestamp_seconds': 1159,
      'tip': "It ups our obligation in terms of our fiduciary role and you know I'm going to "
             'talk through a number of these caa provisions that are in effect currently and '
             'again a common thread throughout all of them is this increased access to '
             'information.',
      'title': 'Fiduciary Compliance and Key Provisions of the Consolidated Appropriations Act '
               '(Walsh Insurance)',
      'url': 'https://www.youtube.com/watch?v=9hPiS9wv_F4&t=1159s',
      'video_id': '9hPiS9wv_F4'},
     {'author': 'Alliant Idaho',
      'channel': 'Alliant Idaho',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=twKQWqVJ4zc&t=120s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Disclosure I'm happy to have a conversation with you about your brokerage "
              "relationship about the fees you're paying and about the services you're getting "
              "for those for those dollars you're spending thank you so much look forward to "
              'talking to you soon.',
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': "Disclosure I'm happy to have a conversation with you about your brokerage "
             "relationship about the fees you're paying and about the services you're getting "
             "for those for those dollars you're spending thank you so much look forward to "
             'talking to you soon.',
      'title': 'New for 2022 - Broker Compensation Disclosures (Alliant Idaho)',
      'url': 'https://www.youtube.com/watch?v=twKQWqVJ4zc&t=120s',
      'video_id': 'twKQWqVJ4zc'},
     {'author': 'BCF Group',
      'channel': 'BCF Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=c069PHgKa8Y&t=15s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'In minimizing your costs so what is it well the experience mod factor is a '
              'number that is calculated by the state of Pennsylvania for each business so.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'In minimizing your costs so what is it well the experience mod factor is a '
             'number that is calculated by the state of Pennsylvania for each business so.',
      'title': 'Workers’ Comp Experience Modification Factor. What you need to know. (BCF '
               'Group)',
      'url': 'https://www.youtube.com/watch?v=c069PHgKa8Y&t=15s',
      'video_id': 'c069PHgKa8Y'},
     {'author': 'The Coyle Group - Business Insurance',
      'channel': 'The Coyle Group - Business Insurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=V5MJi6gMjSg&t=31s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Compensation rating bureau or by the national bureau known as the ncci and '
              "that's depending on the state you're.",
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': 'Compensation rating bureau or by the national bureau known as the ncci and '
             "that's depending on the state you're.",
      'title': 'What is the Workers Comp Experience Mod? (The Coyle Group - Business '
               'Insurance)',
      'url': 'https://www.youtube.com/watch?v=V5MJi6gMjSg&t=31s',
      'video_id': 'V5MJi6gMjSg'},
     {'author': 'Frier Levitt',
      'channel': 'Frier Levitt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:58](https://www.youtube.com/watch?v=8mubYuuHvMI&t=238s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The PBM it's very important that the plan understands how to consult this paid "
              "if that consult is paid by the PBM that's a real conflict of interest and they "
              'have to have an independent consultant and and a competent law firm.',
      'timestamp': 238,
      'timestamp_label': '[00:03:58]',
      'timestamp_seconds': 238,
      'tip': "The PBM it's very important that the plan understands how to consult this paid "
             "if that consult is paid by the PBM that's a real conflict of interest and they "
             'have to have an independent consultant and and a competent law firm.',
      'title': 'Let’s Talk: Rebates and PBMs (Frier Levitt)',
      'url': 'https://www.youtube.com/watch?v=8mubYuuHvMI&t=238s',
      'video_id': '8mubYuuHvMI'},
     {'author': 'Seyfarth Shaw LLP',
      'channel': 'Seyfarth Shaw LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:45:13](https://www.youtube.com/watch?v=EwDJFTGZkoE&t=2713s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Stark in this context than it was in the 401K Fe cases is that the alleged '
              'wrongdoers are not being blamed here right the the alleged wrongdoers are '
              'really the pbms according to the plaintiffs who are overcharging um yet the '
              'plaintiffs come after the plan sponsor plan.',
      'timestamp': 2713,
      'timestamp_label': '[00:45:13]',
      'timestamp_seconds': 2713,
      'tip': 'Stark in this context than it was in the 401K Fe cases is that the alleged '
             'wrongdoers are not being blamed here right the the alleged wrongdoers are really '
             'the pbms according to the plaintiffs who are overcharging um yet the plaintiffs '
             'come after the plan sponsor plan.',
      'title': 'Seyfarth Webinar: Decoding ERISA Fiduciary Rules in the Prescription Landscape '
               '- April 2024 (Seyfarth Shaw LLP)',
      'url': 'https://www.youtube.com/watch?v=EwDJFTGZkoE&t=2713s',
      'video_id': 'EwDJFTGZkoE'},
     {'author': 'Self-Funded',
      'channel': 'Self-Funded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:05](https://www.youtube.com/watch?v=VatFfWseBbI&t=545s)',
      'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                   'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                   "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                   'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Questions let me know if something didn't make sense or if the text was too "
              'small or if you really want the yardstick to make another guest spot appearance '
              "I could do that too all right thanks for watching guys and I'll see you next "
              'time.',
      'timestamp': 545,
      'timestamp_label': '[00:09:05]',
      'timestamp_seconds': 545,
      'tip': "Questions let me know if something didn't make sense or if the text was too "
             'small or if you really want the yardstick to make another guest spot appearance '
             "I could do that too all right thanks for watching guys and I'll see you next "
             'time.',
      'title': 'Episode 6. Stop Loss Aggregating Specific Deductibles (Self-Funded)',
      'url': 'https://www.youtube.com/watch?v=VatFfWseBbI&t=545s',
      'video_id': 'VatFfWseBbI'}],
 10: [{'author': 'BBSI',
       'channel': 'BBSI',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:04](https://www.youtube.com/watch?v=BWeBZWs0_YU&t=664s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "So, I think it's important when an employer is building a benefits program to "
               'think about all three of those areas: physical health, mental health, and '
               'work-life balance. And different areas of those are more important to '
               'different groups of people, too, right?',
       'timestamp': 664,
       'timestamp_label': '[00:11:04]',
       'timestamp_seconds': 664,
       'tip': "So, I think it's important when an employer is building a benefits program to "
              'think about all three of those areas: physical health, mental health, and '
              'work-life balance. And different areas of those are more important to different '
              'groups of people, too, right?',
       'title': 'How to Develop a Competitive Employee Benefits Program (BBSI)',
       'url': 'https://www.youtube.com/watch?v=BWeBZWs0_YU&t=664s',
       'video_id': 'BWeBZWs0_YU'},
      {'author': 'Benefits On The Fly',
       'channel': 'Benefits On The Fly',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:47](https://www.youtube.com/watch?v=50kdf1lBaO8&t=167s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Always the same no matter which broker you worked with so I found myself '
               'trying to figure out how do I separate myself from all the other Brokers out '
               'there and.',
       'timestamp': 167,
       'timestamp_label': '[00:02:47]',
       'timestamp_seconds': 167,
       'tip': 'Always the same no matter which broker you worked with so I found myself trying '
              'to figure out how do I separate myself from all the other Brokers out there '
              'and.',
       'title': 'Is Your Broker Worth their Commission? - What you should expect from your '
                'Employee Benefits Broker. (Benefits On The Fly)',
       'url': 'https://www.youtube.com/watch?v=50kdf1lBaO8&t=167s',
       'video_id': '50kdf1lBaO8'},
      {'author': 'Warp',
       'channel': 'Warp',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:33](https://www.youtube.com/watch?v=XHSDGFk6y94&t=153s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Others other some carriers do allow for non imq plans but again then your '
               'rates are kind of a shot in the dark as well and so the reason that the '
               'brokers are not really bringing it up is it is just more work for the broker '
               'to be able to do essentially the same job.',
       'timestamp': 153,
       'timestamp_label': '[00:02:33]',
       'timestamp_seconds': 153,
       'tip': 'Others other some carriers do allow for non imq plans but again then your rates '
              'are kind of a shot in the dark as well and so the reason that the brokers are '
              'not really bringing it up is it is just more work for the broker to be able to '
              'do essentially the same job.',
       'title': 'Level Funded vs. Fully Insured Health Plans: What Every Employer Needs to '
                'Know (Warp)',
       'url': 'https://www.youtube.com/watch?v=XHSDGFk6y94&t=153s',
       'video_id': 'XHSDGFk6y94'},
      {'author': 'Rhett Robbins',
       'channel': 'Rhett Robbins',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:17](https://www.youtube.com/watch?v=8begy-typh4&t=137s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Solid advocacy but the payoff in the long term is savings and peace of mind '
               'have you considered reference-based pricing for your benefit strategy it might '
               "just be the game Cher your company needs thanks for watching and here's to "
               'smarter more affordable healthcare.',
       'timestamp': 137,
       'timestamp_label': '[00:02:17]',
       'timestamp_seconds': 137,
       'tip': 'Solid advocacy but the payoff in the long term is savings and peace of mind '
              'have you considered reference-based pricing for your benefit strategy it might '
              "just be the game Cher your company needs thanks for watching and here's to "
              'smarter more affordable healthcare.',
       'title': 'Reference-Based Pricing: How it works (Rhett Robbins)',
       'url': 'https://www.youtube.com/watch?v=8begy-typh4&t=137s',
       'video_id': '8begy-typh4'},
      {'author': 'Captive Resources',
       'channel': 'Captive Resources',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:39](https://www.youtube.com/watch?v=c_F-WNrCoqk&t=99s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'The group captive model allows companies to leverage the benefits of a '
               'self-funded health plan using a captive insurance overlay… Which results in '
               'the captive advantage.',
       'timestamp': 99,
       'timestamp_label': '[00:01:39]',
       'timestamp_seconds': 99,
       'tip': 'The group captive model allows companies to leverage the benefits of a '
              'self-funded health plan using a captive insurance overlay… Which results in the '
              'captive advantage.',
       'title': 'Medical Stop Loss Group Captives Explainer Video (Captive Resources)',
       'url': 'https://www.youtube.com/watch?v=c_F-WNrCoqk&t=99s',
       'video_id': 'c_F-WNrCoqk'},
      {'author': 'Fusco On Insurance',
       'channel': 'Fusco On Insurance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:41](https://www.youtube.com/watch?v=8Reu6Q_HdTE&t=221s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Uh also, your payroll levels are key factor. That's why here at the agency, we "
               'are extremely keen on making sure that your audits get done uh on time because '
               "if there's delays in audits uh you don't have the benefit of your payroll "
               'being reported to the WCIRB.',
       'timestamp': 221,
       'timestamp_label': '[00:03:41]',
       'timestamp_seconds': 221,
       'tip': "Uh also, your payroll levels are key factor. That's why here at the agency, we "
              'are extremely keen on making sure that your audits get done uh on time because '
              "if there's delays in audits uh you don't have the benefit of your payroll being "
              'reported to the WCIRB.',
       'title': 'Everything you need to know about California Experience Modification Factors '
                '(EMOD) (Fusco On Insurance)',
       'url': 'https://www.youtube.com/watch?v=8Reu6Q_HdTE&t=221s',
       'video_id': '8Reu6Q_HdTE'},
      {'author': 'KFF Health News',
       'channel': 'KFF Health News',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:36](https://www.youtube.com/watch?v=P21Zb_OySIg&t=156s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Another way PBMs make money is through rebates. Think of them like the coupons '
               'you send in when you buy a new brand of soap or an electronic gadget. Pop it '
               'in the mail and a few months later you get a check for $3. That happens with '
               'PBMs, but on a much larger scale.',
       'timestamp': 156,
       'timestamp_label': '[00:02:36]',
       'timestamp_seconds': 156,
       'tip': 'Another way PBMs make money is through rebates. Think of them like the coupons '
              'you send in when you buy a new brand of soap or an electronic gadget. Pop it in '
              'the mail and a few months later you get a check for $3. That happens with PBMs, '
              'but on a much larger scale.',
       'title': 'Pharmacy Benefit Managers: Companies In The Thick Of Prescription Drug '
                'Pricing (KFF Health News)',
       'url': 'https://www.youtube.com/watch?v=P21Zb_OySIg&t=156s',
       'video_id': 'P21Zb_OySIg'},
      {'author': 'Frier Levitt',
       'channel': 'Frier Levitt',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:23](https://www.youtube.com/watch?v=jpLEKhmPpLs&t=263s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Your medical and Pharmacy benefits s and and the same sets of laws standard of '
               "care got it and so anything when you're reading through.",
       'timestamp': 263,
       'timestamp_label': '[00:04:23]',
       'timestamp_seconds': 263,
       'tip': 'Your medical and Pharmacy benefits s and and the same sets of laws standard of '
              "care got it and so anything when you're reading through.",
       'title': 'Breaking: J&J ERISA Employee Benefit Lawsuit. Am I at Risk? (Frier Levitt)',
       'url': 'https://www.youtube.com/watch?v=jpLEKhmPpLs&t=263s',
       'video_id': 'jpLEKhmPpLs'},
      {'author': "Amaxx | Workers' Comp for Employers",
       'channel': "Amaxx | Workers' Comp for Employers",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:35](https://www.youtube.com/watch?v=IPw3yHxQGJM&t=155s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Frequency is going How's the weather and park Saigon sport completes the Speed "
               "game demonstrates that never see you miss me what's today's World corporation "
               'homogamy part will come back for Remind Voice will Of America impact on summer '
               'with the Big C.',
       'timestamp': 155,
       'timestamp_label': '[00:02:35]',
       'timestamp_seconds': 155,
       'tip': "Frequency is going How's the weather and park Saigon sport completes the Speed "
              "game demonstrates that never see you miss me what's today's World corporation "
              'homogamy part will come back for Remind Voice will Of America impact on summer '
              'with the Big C.',
       'title': "Workers' Comp Claim Frequency Vs Severity Impact on The Experience Mod (Amaxx "
                "| Workers' Comp for Employers)",
       'url': 'https://www.youtube.com/watch?v=IPw3yHxQGJM&t=155s',
       'video_id': 'IPw3yHxQGJM'},
      {'author': 'Employers Group',
       'channel': 'Employers Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:46:31](https://www.youtube.com/watch?v=XYYaHz216lk&t=2791s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Quickly and I think you all know know that the next two if you would one more '
               "um and get help from your broker know your broker isn't the guy providing the.",
       'timestamp': 2791,
       'timestamp_label': '[00:46:31]',
       'timestamp_seconds': 2791,
       'tip': 'Quickly and I think you all know know that the next two if you would one more '
              "um and get help from your broker know your broker isn't the guy providing the.",
       'title': 'Reducing Workers Compensation Rates- Tactical & Practical Strategies '
                '(Employers Group)',
       'url': 'https://www.youtube.com/watch?v=XYYaHz216lk&t=2791s',
       'video_id': 'XYYaHz216lk'},
      {'author': 'ClinardInsGroup',
       'channel': 'ClinardInsGroup',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:22](https://www.youtube.com/watch?v=-hUWvUBIr1A&t=22s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Short the calculation of your mod is done each year based on prior loss '
               'experience a mod of 1.0 has no effect on your final.',
       'timestamp': 22,
       'timestamp_label': '[00:00:22]',
       'timestamp_seconds': 22,
       'tip': 'Short the calculation of your mod is done each year based on prior loss '
              'experience a mod of 1.0 has no effect on your final.',
       'title': 'Work Comp Experience Mod Formula Is Changing (ClinardInsGroup)',
       'url': 'https://www.youtube.com/watch?v=-hUWvUBIr1A&t=22s',
       'video_id': '-hUWvUBIr1A'},
      {'author': 'Self-Funded',
       'channel': 'Self-Funded',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:22](https://www.youtube.com/watch?v=adwLQHPv5YI&t=202s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Have some form of specific stop loss okay so that's specific stop- loss in the "
               "next video we're going to go over aggregate stop loss again how they work "
               'together and how they differ thanks for joining guys.',
       'timestamp': 202,
       'timestamp_label': '[00:03:22]',
       'timestamp_seconds': 202,
       'tip': "Have some form of specific stop loss okay so that's specific stop- loss in the "
              "next video we're going to go over aggregate stop loss again how they work "
              'together and how they differ thanks for joining guys.',
       'title': 'Specific Stop-Loss Insurance EXPLAINED | The Self-Funded Sketchbook '
                '(Self-Funded)',
       'url': 'https://www.youtube.com/watch?v=adwLQHPv5YI&t=202s',
       'video_id': 'adwLQHPv5YI'},
      {'author': 'The Partners Group',
       'channel': 'The Partners Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:22](https://www.youtube.com/watch?v=Cxvmh46o824&t=1042s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Um just two years ago specialty drugs represented less than one percent of all '
               'scripts and only about 25 of your total drug spend however the projected '
               'spending on specialties expected to increase by 63 next year.',
       'timestamp': 1042,
       'timestamp_label': '[00:17:22]',
       'timestamp_seconds': 1042,
       'tip': 'Um just two years ago specialty drugs represented less than one percent of all '
              'scripts and only about 25 of your total drug spend however the projected '
              'spending on specialties expected to increase by 63 next year.',
       'title': 'Healthcare Savings Via Pharmacy Benefit Management Programs for Self-Funded '
                'Employers (The Partners Group)',
       'url': 'https://www.youtube.com/watch?v=Cxvmh46o824&t=1042s',
       'video_id': 'Cxvmh46o824'},
      {'author': 'Healthcare Solutions Connection',
       'channel': 'Healthcare Solutions Connection',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:15](https://www.youtube.com/watch?v=ypiI6d2Bnkk&t=135s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Around the nation to move towards direct Contracting with providers and more '
               'providers look to position themselves as good partners for these employers '
               "that's all for today see you next time on Healthcare Solutions connections two "
               'minute.',
       'timestamp': 135,
       'timestamp_label': '[00:02:15]',
       'timestamp_seconds': 135,
       'tip': 'Around the nation to move towards direct Contracting with providers and more '
              'providers look to position themselves as good partners for these employers '
              "that's all for today see you next time on Healthcare Solutions connections two "
              'minute.',
       'title': "Direct Contracting between Employers and Healthcare Providers: HSC's "
                'Two-Minute Warning (Healthcare Solutions Connection)',
       'url': 'https://www.youtube.com/watch?v=ypiI6d2Bnkk&t=135s',
       'video_id': 'ypiI6d2Bnkk'},
      {'author': 'Self-Funded',
       'channel': 'Self-Funded',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:47](https://www.youtube.com/watch?v=XWfu2p6Kaco&t=107s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Video screen audio wear you can plug and play the different things you want '
               "for that high level gaming experience you're going to custom build your pc for "
               "that gaming experience that's a tpa you're custom making how you want to "
               'approach your solution.',
       'timestamp': 107,
       'timestamp_label': '[00:01:47]',
       'timestamp_seconds': 107,
       'tip': 'Video screen audio wear you can plug and play the different things you want for '
              "that high level gaming experience you're going to custom build your pc for that "
              "gaming experience that's a tpa you're custom making how you want to approach "
              'your solution.',
       'title': 'How a TPA is like a Gaming PC (Self-Funded)',
       'url': 'https://www.youtube.com/watch?v=XWfu2p6Kaco&t=107s',
       'video_id': 'XWfu2p6Kaco'}],
 11: [{'author': 'HR Service, Inc.',
       'channel': 'HR Service, Inc.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:58](https://www.youtube.com/watch?v=K_Kmaqdjrns&t=58s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'So for 5,500 welfare benefit plans, the whole purpose of it is to just give '
               'transparency to the DO and the employees on the financial condition and '
               'operations of the benefit plan.',
       'timestamp': 58,
       'timestamp_label': '[00:00:58]',
       'timestamp_seconds': 58,
       'tip': 'So for 5,500 welfare benefit plans, the whole purpose of it is to just give '
              'transparency to the DO and the employees on the financial condition and '
              'operations of the benefit plan.',
       'title': 'Avoiding Form 5500 Late Filing Penalties | DFVCP Compliance & 2025 Updates '
                '(HR Service, Inc.)',
       'url': 'https://www.youtube.com/watch?v=K_Kmaqdjrns&t=58s',
       'video_id': 'K_Kmaqdjrns'},
      {'author': 'Imago Dei Insurance Advisors',
       'channel': 'Imago Dei Insurance Advisors',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:49](https://www.youtube.com/watch?v=Zej6tYKTOgE&t=229s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Level funded options tend to become more relevant when there is enough '
               'enrollment to evaluate the group meaningfully. Second, how stable is the '
               'organization? If you are growing, hiring, or trying to build a more '
               'intentional benefit strategy, the funding structure matters.',
       'timestamp': 229,
       'timestamp_label': '[00:03:49]',
       'timestamp_seconds': 229,
       'tip': 'Level funded options tend to become more relevant when there is enough '
              'enrollment to evaluate the group meaningfully. Second, how stable is the '
              'organization? If you are growing, hiring, or trying to build a more intentional '
              'benefit strategy, the funding structure matters.',
       'title': 'Level-Funded Health Plans Explained Simply for Christian Employers (Imago Dei '
                'Insurance Advisors)',
       'url': 'https://www.youtube.com/watch?v=Zej6tYKTOgE&t=229s',
       'video_id': 'Zej6tYKTOgE'},
      {'author': 'Dr. Glaucomflecken',
       'channel': 'Dr. Glaucomflecken',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:51](https://www.youtube.com/watch?v=5rw4kNHNZyk&t=51s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Determine which medications will be covered by your insurance all to the '
               'highest bidder god well do you know where I can find one of these Pharmacy '
               "benefit manage what's happening right now hi I'm the pharmacy benefit manager.",
       'timestamp': 51,
       'timestamp_label': '[00:00:51]',
       'timestamp_seconds': 51,
       'tip': 'Determine which medications will be covered by your insurance all to the '
              'highest bidder god well do you know where I can find one of these Pharmacy '
              "benefit manage what's happening right now hi I'm the pharmacy benefit manager.",
       'title': '30 Days of US Healthcare: Pharmacy Benefit Managers (Dr. Glaucomflecken)',
       'url': 'https://www.youtube.com/watch?v=5rw4kNHNZyk&t=51s',
       'video_id': '5rw4kNHNZyk'},
      {'author': 'Gusto',
       'channel': 'Gusto',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:25](https://www.youtube.com/watch?v=z_Qpt9fQLWg&t=25s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Gusto's licensed advisors will help you compare plans, build a package your "
               'team will value, and help you navigate benefits with confidence.',
       'timestamp': 25,
       'timestamp_label': '[00:00:25]',
       'timestamp_seconds': 25,
       'tip': "Gusto's licensed advisors will help you compare plans, build a package your "
              'team will value, and help you navigate benefits with confidence.',
       'title': 'How to Set Up Health Insurance & Employee Benefits in Gusto (Gusto)',
       'url': 'https://www.youtube.com/watch?v=z_Qpt9fQLWg&t=25s',
       'video_id': 'z_Qpt9fQLWg'},
      {'author': 'JJ Doorhy & Associates',
       'channel': 'JJ Doorhy & Associates',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:07](https://www.youtube.com/watch?v=cgxTiDoClOs&t=547s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "0 0 and below, you can qualify for contractor's credit and you can apply for "
               'that um through your broker and NCCI. So, um even if you have a 1. 01 mod, so '
               "in this example, 1. 10, but let's just say you have a 1. 01 mod, which is 1% "
               'worse than average.',
       'timestamp': 547,
       'timestamp_label': '[00:09:07]',
       'timestamp_seconds': 547,
       'tip': "0 0 and below, you can qualify for contractor's credit and you can apply for "
              'that um through your broker and NCCI. So, um even if you have a 1. 01 mod, so '
              "in this example, 1. 10, but let's just say you have a 1. 01 mod, which is 1% "
              'worse than average.',
       'title': "How Your EMR Actually Works | The Formula Behind Your Workers' Comp Mod (JJ "
                'Doorhy & Associates)',
       'url': 'https://www.youtube.com/watch?v=cgxTiDoClOs&t=547s',
       'video_id': 'cgxTiDoClOs'},
      {'author': 'Total Control Health Plans',
       'channel': 'Total Control Health Plans',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:44](https://www.youtube.com/watch?v=FvXAV4cqPRg&t=104s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Let's take a look at the arguments being made in the lawsuit. One of the "
               'primary complaints is that the pharmacy benefit manager was allowed to define '
               'generic specialty drugs how they saw fit.',
       'timestamp': 104,
       'timestamp_label': '[00:01:44]',
       'timestamp_seconds': 104,
       'tip': "Let's take a look at the arguments being made in the lawsuit. One of the "
              'primary complaints is that the pharmacy benefit manager was allowed to define '
              'generic specialty drugs how they saw fit.',
       'title': 'Johnson & Johnson ERISA Lawsuit — What You NEED to Know (Total Control Health '
                'Plans)',
       'url': 'https://www.youtube.com/watch?v=FvXAV4cqPRg&t=104s',
       'video_id': 'FvXAV4cqPRg'},
      {'author': 'Roundstone Insurance',
       'channel': 'Roundstone Insurance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:38](https://www.youtube.com/watch?v=FPn0kt8qe6U&t=578s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, um, I when I started at Roundstone, I was very briefly an account manager. '
               'And the best part was getting to email or call up a group or a broker and say, '
               '"Hey, you\'re getting a percentage of your premium back.".',
       'timestamp': 578,
       'timestamp_label': '[00:09:38]',
       'timestamp_seconds': 578,
       'tip': 'So, um, I when I started at Roundstone, I was very briefly an account manager. '
              'And the best part was getting to email or call up a group or a broker and say, '
              '"Hey, you\'re getting a percentage of your premium back.".',
       'title': 'Self-Funding’s Safety Net: Stop-Loss Explained (Roundstone Insurance)',
       'url': 'https://www.youtube.com/watch?v=FPn0kt8qe6U&t=578s',
       'video_id': 'FPn0kt8qe6U'},
      {'author': 'National Community Pharmacists Association',
       'channel': 'National Community Pharmacists Association',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:42](https://www.youtube.com/watch?v=lbfUr3FiuyU&t=162s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Who knows maybe tonight I'll dream up another Shady scheme to make even more "
               'money to learn more about lowering drug costs protecting patient choice of '
               'Pharmacy and reforming filma pockets and the pharmacy benefit managers he '
               'represents go to who runsy drug plan.com.',
       'timestamp': 162,
       'timestamp_label': '[00:02:42]',
       'timestamp_seconds': 162,
       'tip': "Who knows maybe tonight I'll dream up another Shady scheme to make even more "
              'money to learn more about lowering drug costs protecting patient choice of '
              'Pharmacy and reforming filma pockets and the pharmacy benefit managers he '
              'represents go to who runsy drug plan.com.',
       'title': 'What is a Pharmacy Benefit Manager (PBM)? -- Longer version (National '
                'Community Pharmacists Association)',
       'url': 'https://www.youtube.com/watch?v=lbfUr3FiuyU&t=162s',
       'video_id': 'lbfUr3FiuyU'},
      {'author': "Employers' Forum of Indiana",
       'channel': "Employers' Forum of Indiana",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:24:27](https://www.youtube.com/watch?v=zoRFywXBoLM&t=1467s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Attack kind of some simultaneously um but it is working um and we use the '
               'feedback we get from our members from my team from our vendors um you know to '
               'make changes in subsequent years and and make plans.',
       'timestamp': 1467,
       'timestamp_label': '[00:24:27]',
       'timestamp_seconds': 1467,
       'tip': 'Attack kind of some simultaneously um but it is working um and we use the '
              'feedback we get from our members from my team from our vendors um you know to '
              'make changes in subsequent years and and make plans.',
       'title': 'February 25 2021 All Stakeholder Meeting - Specialty Pharmacy Carve-Out '
                "(Employers' Forum of Indiana)",
       'url': 'https://www.youtube.com/watch?v=zoRFywXBoLM&t=1467s',
       'video_id': 'zoRFywXBoLM'},
      {'author': 'Nia Brooks',
       'channel': 'Nia Brooks',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:49](https://www.youtube.com/watch?v=POU9QtCmQZk&t=229s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Employments, occupations, or operations within the business. The business gets '
               'the code. Everybody inside it rides that code. Your welder.',
       'timestamp': 229,
       'timestamp_label': '[00:03:49]',
       'timestamp_seconds': 229,
       'tip': 'Employments, occupations, or operations within the business. The business gets '
              'the code. Everybody inside it rides that code. Your welder.',
       'title': 'Workers Comp Insurance Audit: What Actually Moves Your Premium (Nia Brooks)',
       'url': 'https://www.youtube.com/watch?v=POU9QtCmQZk&t=229s',
       'video_id': 'POU9QtCmQZk'},
      {'author': 'WorkCompConsultants',
       'channel': 'WorkCompConsultants',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:52](https://www.youtube.com/watch?v=tkOuTso-3RA&t=112s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Wait until a Miss classification is discovered by an auditor and the '
               'correction shows up in the form of a large additional premium and build due at '
               'audit time be proactive have a workers compensation code review performed '
               'today thanks for watching.',
       'timestamp': 112,
       'timestamp_label': '[00:01:52]',
       'timestamp_seconds': 112,
       'tip': 'Wait until a Miss classification is discovered by an auditor and the correction '
              'shows up in the form of a large additional premium and build due at audit time '
              'be proactive have a workers compensation code review performed today thanks for '
              'watching.',
       'title': 'Workers Compensation Codes (WorkCompConsultants)',
       'url': 'https://www.youtube.com/watch?v=tkOuTso-3RA&t=112s',
       'video_id': 'tkOuTso-3RA'},
      {'author': 'RxPreferred',
       'channel': 'RxPreferred',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:01](https://www.youtube.com/watch?v=15IQO_jTMUM&t=241s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Mail order pharmacies have Financial motivation to continue shipping unwanted '
               'or unnecessary medications hence the mail order waste game as one of multiple '
               'opportunities tied to the pbms ownership of mail order.',
       'timestamp': 241,
       'timestamp_label': '[00:04:01]',
       'timestamp_seconds': 241,
       'tip': 'Mail order pharmacies have Financial motivation to continue shipping unwanted '
              'or unnecessary medications hence the mail order waste game as one of multiple '
              'opportunities tied to the pbms ownership of mail order.',
       'title': 'Pharmacy Benefit Manager (PBM) Games (RxPreferred)',
       'url': 'https://www.youtube.com/watch?v=15IQO_jTMUM&t=241s',
       'video_id': '15IQO_jTMUM'},
      {'author': 'Strategic Builders-Dev Insurance & Risk Solutions',
       'channel': 'Strategic Builders-Dev Insurance & Risk Solutions',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:04](https://www.youtube.com/watch?v=79EPdRvCp3A&t=184s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Be talking about something a little bit more interesting but I haven't decided "
               'what the uh what the topic will be yet so I will keep that as a surprise have '
               "a terrific february remember remember it's heart month and get your heart "
               'checked out tick-tock.',
       'timestamp': 184,
       'timestamp_label': '[00:03:04]',
       'timestamp_seconds': 184,
       'tip': "Be talking about something a little bit more interesting but I haven't decided "
              'what the uh what the topic will be yet so I will keep that as a surprise have a '
              "terrific february remember remember it's heart month and get your heart checked "
              'out tick-tock.',
       'title': 'Broker of Record Letter- Should I sign? (Strategic Builders-Dev Insurance & '
                'Risk Solutions)',
       'url': 'https://www.youtube.com/watch?v=79EPdRvCp3A&t=184s',
       'video_id': '79EPdRvCp3A'},
      {'author': 'Texas Mutual Insurance Co',
       'channel': 'Texas Mutual Insurance Co',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:54](https://www.youtube.com/watch?v=gt3I3IxlEkE&t=234s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Out WorkSafe Texas comm for more workplace safety training for even more '
               'educational content click on the training and education tab at Texas Mutual '
               "comm thanks for watching we'll see you next time.",
       'timestamp': 234,
       'timestamp_label': '[00:03:54]',
       'timestamp_seconds': 234,
       'tip': 'Out WorkSafe Texas comm for more workplace safety training for even more '
              'educational content click on the training and education tab at Texas Mutual '
              "comm thanks for watching we'll see you next time.",
       'title': 'What is an experience modifier? (Texas Mutual Insurance Co)',
       'url': 'https://www.youtube.com/watch?v=gt3I3IxlEkE&t=234s',
       'video_id': 'gt3I3IxlEkE'},
      {'author': 'Berger Montague',
       'channel': 'Berger Montague',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:46](https://www.youtube.com/watch?v=WBl8smrz_3E&t=226s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Ramifications of the consolidated appropriations act thanks for your '
               'participation today again follow us on linkedin at one vision analytics or our '
               'website at www v hyphen a dot com or at burger montag at www.burgermontag.com.',
       'timestamp': 226,
       'timestamp_label': '[00:03:46]',
       'timestamp_seconds': 226,
       'tip': 'Ramifications of the consolidated appropriations act thanks for your '
              'participation today again follow us on linkedin at one vision analytics or our '
              'website at www v hyphen a dot com or at burger montag at www.burgermontag.com.',
       'title': 'Impact of the CAA of 2021 on Gag Clauses (Berger Montague)',
       'url': 'https://www.youtube.com/watch?v=WBl8smrz_3E&t=226s',
       'video_id': 'WBl8smrz_3E'}],
 12: [{'author': 'TheCoyPharmer',
       'channel': 'TheCoyPharmer',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:30](https://www.youtube.com/watch?v=H3p5Yw0Y-ek&t=810s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'MAC list being required each day or each week. In my personal opinion, this is '
               'an area where AI could really come into the pharmacy benefits industry and '
               'create a more nuanced mathematical link in helping the PBMs balance all of '
               'these different obligations.',
       'timestamp': 810,
       'timestamp_label': '[00:13:30]',
       'timestamp_seconds': 810,
       'tip': 'MAC list being required each day or each week. In my personal opinion, this is '
              'an area where AI could really come into the pharmacy benefits industry and '
              'create a more nuanced mathematical link in helping the PBMs balance all of '
              'these different obligations.',
       'title': 'Drug Pricing Indexes: Maximum Allowable Cost (MAC) (TheCoyPharmer)',
       'url': 'https://www.youtube.com/watch?v=H3p5Yw0Y-ek&t=810s',
       'video_id': 'H3p5Yw0Y-ek'},
      {'author': 'Max Revenue',
       'channel': 'Max Revenue',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:32:20](https://www.youtube.com/watch?v=vTPBeVqiUY4&t=1940s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "We might just make it free one day. We're playing that YouTube ad long game. I "
               'talked with our developer. We were supposed to launch it at the beginning of '
               'this month, but we ran into an API issue with LinkedIn.',
       'timestamp': 1940,
       'timestamp_label': '[00:32:20]',
       'timestamp_seconds': 1940,
       'tip': "We might just make it free one day. We're playing that YouTube ad long game. I "
              'talked with our developer. We were supposed to launch it at the beginning of '
              'this month, but we ran into an API issue with LinkedIn.',
       'title': 'How To Set Up Broker of Record Letters (BORs) Like a Pro (Max Revenue)',
       'url': 'https://www.youtube.com/watch?v=vTPBeVqiUY4&t=1940s',
       'video_id': 'vTPBeVqiUY4'},
      {'author': 'The HR Hub with Andrea Adams',
       'channel': 'The HR Hub with Andrea Adams',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:22](https://www.youtube.com/watch?v=d5PvJwohdPU&t=82s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'To the market you know quote unquote to get the best plan for them with the '
               'various carriers so a benefits broker yes is there any.',
       'timestamp': 82,
       'timestamp_label': '[00:01:22]',
       'timestamp_seconds': 82,
       'tip': 'To the market you know quote unquote to get the best plan for them with the '
              'various carriers so a benefits broker yes is there any.',
       'title': 'What Does An Employee Benefits Broker Do? (The HR Hub with Andrea Adams)',
       'url': 'https://www.youtube.com/watch?v=d5PvJwohdPU&t=82s',
       'video_id': 'd5PvJwohdPU'},
      {'author': 'American Trust Administrators | Level Funding',
       'channel': 'American Trust Administrators | Level Funding',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=dgpkKOJBv_s&t=15s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Level funding is of what Brokers are doing when they go out and they assist '
               'their clients in building a level funded plan for that employer for that group '
               'of.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Level funding is of what Brokers are doing when they go out and they assist '
              'their clients in building a level funded plan for that employer for that group '
              'of.',
       'title': 'Why Level-Funded Health Plans Are Better for Small Businesses (Level Funding '
                '101) (American Trust Administrators | Level Funding)',
       'url': 'https://www.youtube.com/watch?v=dgpkKOJBv_s&t=15s',
       'video_id': 'dgpkKOJBv_s'},
      {'author': 'Dysrupt Healthcare Podcast',
       'channel': 'Dysrupt Healthcare Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:39:38](https://www.youtube.com/watch?v=mPaz9R2yMrs&t=2378s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Will protect plan members from any sort of predatory billing practices that '
               'happen at the provider level um and so when it comes to having a program.',
       'timestamp': 2378,
       'timestamp_label': '[00:39:38]',
       'timestamp_seconds': 2378,
       'tip': 'Will protect plan members from any sort of predatory billing practices that '
              'happen at the provider level um and so when it comes to having a program.',
       'title': 'Unlocking Healthcare Savings with Reference-Based Pricing: Insights from Omar '
                'Arif (Dysrupt Healthcare Podcast)',
       'url': 'https://www.youtube.com/watch?v=mPaz9R2yMrs&t=2378s',
       'video_id': 'mPaz9R2yMrs'},
      {'author': 'Emparion',
       'channel': 'Emparion',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:38](https://www.youtube.com/watch?v=yGr9BaJ2hJ4&t=38s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "One thing that's very important to note is that when you combine retirement "
               "plans and this is significant if you've got a cash balance plan along with "
               'the.',
       'timestamp': 38,
       'timestamp_label': '[00:00:38]',
       'timestamp_seconds': 38,
       'tip': "One thing that's very important to note is that when you combine retirement "
              "plans and this is significant if you've got a cash balance plan along with the.",
       'title': 'Form 5500-EZ: The Quick Step by Step Guide (Emparion)',
       'url': 'https://www.youtube.com/watch?v=yGr9BaJ2hJ4&t=38s',
       'video_id': 'yGr9BaJ2hJ4'},
      {'author': 'The Class Action Weekly Wire',
       'channel': 'The Class Action Weekly Wire',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:55](https://www.youtube.com/watch?v=NtoIMU293PI&t=55s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "ERISA-based fiduciary duty claims. Adam, let's start with the basics. What was "
               "Goodyear's program and what were these employees challenging?",
       'timestamp': 55,
       'timestamp_label': '[00:00:55]',
       'timestamp_seconds': 55,
       'tip': "ERISA-based fiduciary duty claims. Adam, let's start with the basics. What was "
              "Goodyear's program and what were these employees challenging?",
       'title': 'Episode 172: ERISA Tobacco Surcharge Class Action Survives Motion To Dismiss '
                'In Ohio Federal Court (The Class Action Weekly Wire)',
       'url': 'https://www.youtube.com/watch?v=NtoIMU293PI&t=55s',
       'video_id': 'NtoIMU293PI'},
      {'author': 'Rob Freeman | Insuring The Built Environment',
       'channel': 'Rob Freeman | Insuring The Built Environment',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:17](https://www.youtube.com/watch?v=C_YjzkmKog0&t=137s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Insurance broker and that's it so if you have questions about a broker record "
               'letter or you are concerned about your own insurance feel free to schedule an '
               "appointment with me I'd love to talk to you and uh thanks again hope this has "
               'been helpful and have a great day.',
       'timestamp': 137,
       'timestamp_label': '[00:02:17]',
       'timestamp_seconds': 137,
       'tip': "Insurance broker and that's it so if you have questions about a broker record "
              'letter or you are concerned about your own insurance feel free to schedule an '
              "appointment with me I'd love to talk to you and uh thanks again hope this has "
              'been helpful and have a great day.',
       'title': 'What Does a Broker of Record Letter Do? (Rob Freeman | Insuring The Built '
                'Environment)',
       'url': 'https://www.youtube.com/watch?v=C_YjzkmKog0&t=137s',
       'video_id': 'C_YjzkmKog0'},
      {'author': 'Justin Burgess',
       'channel': 'Justin Burgess',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:36](https://www.youtube.com/watch?v=Bq89alxy8qQ&t=156s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Ones responsible for our plan meaning that we're doing the right thing for "
               'playing participants at the end of the day we all want to spend the least '
               'amount possible on insurance and we want to do things the right way so Justin '
               'bur is here thank you bye.',
       'timestamp': 156,
       'timestamp_label': '[00:02:36]',
       'timestamp_seconds': 156,
       'tip': "Ones responsible for our plan meaning that we're doing the right thing for "
              'playing participants at the end of the day we all want to spend the least '
              'amount possible on insurance and we want to do things the right way so Justin '
              'bur is here thank you bye.',
       'title': 'Compliance Overview: Group Health Plan Fiduciary Litigation on the Rise '
                '(Justin Burgess)',
       'url': 'https://www.youtube.com/watch?v=Bq89alxy8qQ&t=156s',
       'video_id': 'Bq89alxy8qQ'},
      {'author': 'Miller Johnson',
       'channel': 'Miller Johnson',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:31](https://www.youtube.com/watch?v=WVU2CeENchc&t=571s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Services services that were identified uh in the regulations uh and then the '
               'next plan year planners beginning the next year after on or after january 2024 '
               'uh the requirement applied to all uh covered services under the group health '
               'plan.',
       'timestamp': 571,
       'timestamp_label': '[00:09:31]',
       'timestamp_seconds': 571,
       'tip': 'Services services that were identified uh in the regulations uh and then the '
              'next plan year planners beginning the next year after on or after january 2024 '
              'uh the requirement applied to all uh covered services under the group health '
              'plan.',
       'title': 'A High-Level Review of the Transparency Provisions Under the Consolidated '
                'Appropriations Act, 2021 (Miller Johnson)',
       'url': 'https://www.youtube.com/watch?v=WVU2CeENchc&t=571s',
       'video_id': 'WVU2CeENchc'},
      {'author': 'Self-Funded',
       'channel': 'Self-Funded',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:23](https://www.youtube.com/watch?v=VPeObJ32l7M&t=263s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Guarantee a win okay so fully insured versus self-funded now you have a better '
               "understanding of those two funding arrangements and we're going to start "
               'building on this basic Foundation thanks guys.',
       'timestamp': 263,
       'timestamp_label': '[00:04:23]',
       'timestamp_seconds': 263,
       'tip': 'Guarantee a win okay so fully insured versus self-funded now you have a better '
              "understanding of those two funding arrangements and we're going to start "
              'building on this basic Foundation thanks guys.',
       'title': 'Self-Funded vs. Fully-Insured Health Insurance, EXPLAINED | The Self-Funded '
                'Sketchbook (Self-Funded)',
       'url': 'https://www.youtube.com/watch?v=VPeObJ32l7M&t=263s',
       'video_id': 'VPeObJ32l7M'},
      {'author': 'The Leapfrog Group',
       'channel': 'The Leapfrog Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:36](https://www.youtube.com/watch?v=QU7rxyEAEjQ&t=216s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Something they wanna they don't wanna talk about so that's what I think okay "
               'so what should they be worried about tell us well let me go ahead and start my '
               'presentation here for everybody.',
       'timestamp': 216,
       'timestamp_label': '[00:03:36]',
       'timestamp_seconds': 216,
       'tip': "Something they wanna they don't wanna talk about so that's what I think okay so "
              'what should they be worried about tell us well let me go ahead and start my '
              'presentation here for everybody.',
       'title': 'The Leapfrog Group CAA Compliance Webinar Series Session 4: Consultant & '
                'Broker Contracts (The Leapfrog Group)',
       'url': 'https://www.youtube.com/watch?v=QU7rxyEAEjQ&t=216s',
       'video_id': 'QU7rxyEAEjQ'},
      {'author': 'Jeremy Burris - Insurance Dad',
       'channel': 'Jeremy Burris - Insurance Dad',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:24](https://www.youtube.com/watch?v=IEUgSXep0xE&t=204s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Renew your policy for workers compensation insurance we strongly encourage you '
               "to give us a call at 813-754 we're really looking forward to helping you save "
               'money on your workers compensation insurance policy this year thank you and '
               'have a great day.',
       'timestamp': 204,
       'timestamp_label': '[00:03:24]',
       'timestamp_seconds': 204,
       'tip': 'Renew your policy for workers compensation insurance we strongly encourage you '
              "to give us a call at 813-754 we're really looking forward to helping you save "
              'money on your workers compensation insurance policy this year thank you and '
              'have a great day.',
       'title': 'Lower your Workers Compensation Insurance Cost (Jeremy Burris - Insurance '
                'Dad)',
       'url': 'https://www.youtube.com/watch?v=IEUgSXep0xE&t=204s',
       'video_id': 'IEUgSXep0xE'},
      {'author': 'Wade Associates',
       'channel': 'Wade Associates',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:33](https://www.youtube.com/watch?v=hX_4HXaXi4U&t=93s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Give you a great benchmark as to how your business compares against your '
               "industry's average and it will give you an idea as to how much money you're "
               'leaving on the table because remember the lower your mod the lower your '
               'premiums.',
       'timestamp': 93,
       'timestamp_label': '[00:01:33]',
       'timestamp_seconds': 93,
       'tip': 'Give you a great benchmark as to how your business compares against your '
              "industry's average and it will give you an idea as to how much money you're "
              'leaving on the table because remember the lower your mod the lower your '
              'premiums.',
       'title': 'What is the Workers Comp EXPERIENCE MOD? (Wade Associates)',
       'url': 'https://www.youtube.com/watch?v=hX_4HXaXi4U&t=93s',
       'video_id': 'hX_4HXaXi4U'},
      {'author': 'Ameriflex',
       'channel': 'Ameriflex',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:57](https://www.youtube.com/watch?v=l5tGs_zQ8xA&t=117s)',
       'relevance': 'Attributed practitioner commentary on mid-market `ERISA` '
                    'self-funded/captive stop-loss transitions, transparent pass-through `PBM` '
                    "rebate recovery, `Form 5500` renewal targeting, and retroactive Workers' "
                    'Comp `NCCI`/`E-Mod` overcharge brokerage (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'We started to see that be duplicated here in this CAA of 2021. So, for '
               'employer-sponsored benefits, plan sponsors, plan administrators, what does '
               "that start to trigger for you? What does that start to mean for them as we're "
               'reading through this piece of legislation?',
       'timestamp': 117,
       'timestamp_label': '[00:01:57]',
       'timestamp_seconds': 117,
       'tip': 'We started to see that be duplicated here in this CAA of 2021. So, for '
              'employer-sponsored benefits, plan sponsors, plan administrators, what does that '
              "start to trigger for you? What does that start to mean for them as we're "
              'reading through this piece of legislation?',
       'title': 'Consolidated Appropriations Act (Ameriflex)',
       'url': 'https://www.youtube.com/watch?v=l5tGs_zQ8xA&t=117s',
       'video_id': 'l5tGs_zQ8xA'}]}
