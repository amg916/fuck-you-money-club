"""Curated 180-citation Subject-To & Wraparound Note Arbitrage baseline (15 per chapter across Q1-Q12) mined strictly from verified Subject-To & Wraparound Note Arbitrage YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'016',
     '40k',
     '453',
     '650',
     'ability',
     'acquisitions',
     'act',
     'agent',
     'agreement',
     'aitd',
     'all',
     'arbitrage',
     'arrears',
     'atr',
     'bankruptcy',
     'building',
     'business',
     'buyers',
     'buying',
     'calculating',
     'carolinasafe',
     'carry',
     'case',
     'cash',
     'clause',
     'client',
     'clients',
     'closing',
     'code',
     'commission',
     'company',
     'comparison',
     'creative',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'016',
     '40k',
     '453',
     '650',
     'ability',
     'acquisitions',
     'act',
     'agent',
     'agreement',
     'aitd',
     'all',
     'arbitrage',
     'arrears',
     'atr',
     'bankruptcy',
     'budget',
     'building',
     'buyer',
     'buyers',
     'buying',
     'calculating',
     'carolinasafe',
     'carry',
     'case',
     'cash',
     'clause',
     'closing',
     'code',
     'commission',
     'company',
     'comparison',
     'contract',
     'creative',
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
 3: {'016',
     '40k',
     '453',
     '650',
     'ability',
     'acquisitions',
     'act',
     'agent',
     'agreement',
     'aitd',
     'all',
     'arbitrage',
     'arrears',
     'atr',
     'bankruptcy',
     'building',
     'buyers',
     'buying',
     'calculating',
     'carolinasafe',
     'carry',
     'case',
     'cash',
     'cashflow',
     'clause',
     'closing',
     'code',
     'commission',
     'company',
     'comparison',
     'cost',
     'costs',
     'creative',
     'economics',
     'margin',
     'margins',
     'price',
     'pricing',
     'profit',
     'roi',
     'unit'},
 4: {'016',
     '40k',
     '453',
     '650',
     'ability',
     'acquisitions',
     'act',
     'agent',
     'agreement',
     'aitd',
     'all',
     'arbitrage',
     'arrears',
     'atr',
     'bankruptcy',
     'budget',
     'building',
     'buyers',
     'buying',
     'calculating',
     'capital',
     'carolinasafe',
     'carry',
     'case',
     'cash',
     'clause',
     'closing',
     'code',
     'commission',
     'company',
     'comparison',
     'creative',
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
 5: {'016',
     '40k',
     '453',
     '650',
     'ability',
     'acquisitions',
     'act',
     'agent',
     'agreement',
     'aitd',
     'all',
     'arbitrage',
     'arrears',
     'atr',
     'audit',
     'avoid',
     'bankruptcy',
     'building',
     'buyers',
     'buying',
     'calculating',
     'carolinasafe',
     'carry',
     'case',
     'cash',
     'clause',
     'clawback',
     'closing',
     'code',
     'commission',
     'company',
     'comparison',
     'creative',
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
 6: {'016',
     '40k',
     '453',
     '650',
     'ability',
     'acquisitions',
     'act',
     'agent',
     'agreement',
     'aitd',
     'all',
     'arbitrage',
     'arrears',
     'atr',
     'bankruptcy',
     'building',
     'buyers',
     'buying',
     'calculating',
     'carolinasafe',
     'carry',
     'case',
     'cash',
     'clause',
     'client',
     'closing',
     'code',
     'commission',
     'company',
     'comparison',
     'creative',
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
 7: {'016',
     '40k',
     '453',
     '650',
     'ability',
     'acquisitions',
     'act',
     'agent',
     'agreement',
     'aitd',
     'all',
     'arbitrage',
     'arrears',
     'atr',
     'bankruptcy',
     'building',
     'buyers',
     'buying',
     'calculating',
     'carolinasafe',
     'carry',
     'case',
     'cash',
     'checklist',
     'clause',
     'closing',
     'code',
     'commission',
     'company',
     'comparison',
     'creative',
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
 8: {'016',
     '40k',
     '453',
     '650',
     'ability',
     'acquisitions',
     'act',
     'agent',
     'agreement',
     'aitd',
     'all',
     'api',
     'arbitrage',
     'arrears',
     'atr',
     'bankruptcy',
     'building',
     'buyers',
     'buying',
     'calculating',
     'carolinasafe',
     'carry',
     'case',
     'cash',
     'clause',
     'closing',
     'code',
     'commission',
     'company',
     'comparison',
     'creative',
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
 9: {'016',
     '40k',
     '453',
     '650',
     'ability',
     'acquisitions',
     'act',
     'agent',
     'agreement',
     'aitd',
     'all',
     'arbitrage',
     'arrears',
     'atr',
     'bankruptcy',
     'building',
     'buyers',
     'buying',
     'calculating',
     'carolinasafe',
     'carry',
     'case',
     'cash',
     'clause',
     'closing',
     'code',
     'commission',
     'company',
     'comparison',
     'compliance',
     'contract',
     'creative',
     'disclosure',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'016',
      '40k',
      '453',
      '650',
      'ability',
      'acquisitions',
      'act',
      'agent',
      'agreement',
      'ai',
      'aitd',
      'all',
      'arbitrage',
      'arrears',
      'atr',
      'automate',
      'automation',
      'bankruptcy',
      'building',
      'buyers',
      'buying',
      'calculating',
      'carolinasafe',
      'carry',
      'case',
      'cash',
      'clause',
      'closing',
      'code',
      'commission',
      'company',
      'comparison',
      'creative',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'016',
      '40k',
      '453',
      '650',
      'ability',
      'acquisitions',
      'act',
      'agent',
      'agreement',
      'aitd',
      'all',
      'arbitrage',
      'arrears',
      'atr',
      'bankruptcy',
      'building',
      'buyers',
      'buying',
      'calculating',
      'carolinasafe',
      'carry',
      'case',
      'cash',
      'clause',
      'closing',
      'code',
      'commission',
      'company',
      'comparison',
      'contractor',
      'creative',
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
 12: {'016',
      '40k',
      '453',
      '650',
      'ability',
      'acquisitions',
      'act',
      'action',
      'agent',
      'agreement',
      'aitd',
      'all',
      'arbitrage',
      'arrears',
      'atr',
      'bankruptcy',
      'building',
      'buyers',
      'buying',
      'calculating',
      'carolinasafe',
      'carry',
      'case',
      'cash',
      'clause',
      'closing',
      'code',
      'commission',
      'company',
      'comparison',
      'creative',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:29](https://www.youtube.com/watch?v=p0ukMOdzoAc&t=989s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This was completely separate. Sub two car, agreement for sale for the building, '
              'seller finance for the business. Creative car, creative Carley, bro. Creative '
              'Carley just doing all the creative deals.',
      'timestamp': 989,
      'timestamp_label': '[00:16:29]',
      'timestamp_seconds': 989,
      'tip': 'This was completely separate. Sub two car, agreement for sale for the building, '
             'seller finance for the business. Creative car, creative Carley, bro. Creative '
             'Carley just doing all the creative deals.',
      'title': 'Buying a Business - Seller Finance Explained (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=p0ukMOdzoAc&t=989s',
      'video_id': 'p0ukMOdzoAc'},
     {'author': 'Sub2Investor',
      'channel': 'Sub2Investor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:23](https://www.youtube.com/watch?v=1oenw8zc-5s&t=383s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ve got to send a loan estimate to your borrower seven business days before you "
              'close and a closing disclosure three business days before you close. And that '
              'gives the consumer, right, the the ability to go through and read all the fine '
              'print, you know, they so choose.',
      'timestamp': 383,
      'timestamp_label': '[00:06:23]',
      'timestamp_seconds': 383,
      'tip': "'ve got to send a loan estimate to your borrower seven business days before you "
             'close and a closing disclosure three business days before you close. And that '
             'gives the consumer, right, the the ability to go through and read all the fine '
             'print, you know, they so choose.',
      'title': '#67 - Master Seller Financing & Dodge Dodd-Frank Traps with Dan Deppen (with '
               'Call the Underwriter) (Sub2Investor)',
      'url': 'https://www.youtube.com/watch?v=1oenw8zc-5s&t=383s',
      'video_id': '1oenw8zc-5s'},
     {'author': 'Ironclad Wealth Management',
      'channel': 'Ironclad Wealth Management',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:23](https://www.youtube.com/watch?v=48sBi3Y9sgE&t=503s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Having said all of that, who are installment sales best for? They are best for '
              "people that you trust who don't have the upfront cash. Buyers that you know and "
              'with an absolutely kind of unbiased eye believe they can make the business run '
              'and work.',
      'timestamp': 503,
      'timestamp_label': '[00:08:23]',
      'timestamp_seconds': 503,
      'tip': 'Having said all of that, who are installment sales best for? They are best for '
             "people that you trust who don't have the upfront cash. Buyers that you know and "
             'with an absolutely kind of unbiased eye believe they can make the business run '
             'and work.',
      'title': 'Using an Installment Sale to Reduce Taxes - When Selling Your Business '
               '(Ironclad Wealth Management)',
      'url': 'https://www.youtube.com/watch?v=48sBi3Y9sgE&t=503s',
      'video_id': '48sBi3Y9sgE'},
     {'author': 'Preferred Trust',
      'channel': 'Preferred Trust',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:07](https://www.youtube.com/watch?v=nauUgmh1YZg&t=1027s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They are saying this company has the ability to market and accept funds from '
              'accredited and non -accredited investors. And we provide annual audited '
              'financials, quarterly or semi -annual, unaudited financials.',
      'timestamp': 1027,
      'timestamp_label': '[00:17:07]',
      'timestamp_seconds': 1027,
      'tip': 'They are saying this company has the ability to market and accept funds from '
             'accredited and non -accredited investors. And we provide annual audited '
             'financials, quarterly or semi -annual, unaudited financials.',
      'title': 'Building Wealth through Non-Performing Mortgage Note Investing (Preferred '
               'Trust)',
      'url': 'https://www.youtube.com/watch?v=nauUgmh1YZg&t=1027s',
      'video_id': 'nauUgmh1YZg'},
     {'author': 'Jeff Jinks Law',
      'channel': 'Jeff Jinks Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:26](https://www.youtube.com/watch?v=TZPUpsL8ecI&t=26s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your wealth and and help your family out so this video is about Internal '
              'Revenue Code section 453 and deals with installment sales and the key issue is.',
      'timestamp': 26,
      'timestamp_label': '[00:00:26]',
      'timestamp_seconds': 26,
      'tip': 'Your wealth and and help your family out so this video is about Internal Revenue '
             'Code section 453 and deals with installment sales and the key issue is.',
      'title': '058 Section 453 Installment Sale v 1 (Jeff Jinks Law)',
      'url': 'https://www.youtube.com/watch?v=TZPUpsL8ecI&t=26s',
      'video_id': 'TZPUpsL8ecI'},
     {'author': 'Paperstac',
      'channel': 'Paperstac',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:47](https://www.youtube.com/watch?v=zhg1k-uMJM0&t=887s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We train a new model on all the past trades that have taken place on '
              "Paperstack. And then we compare it to There's There's like 40 data points that "
              "we're looking at. Some part of the collateral file, some part of the asset, "
              'some part of the market.',
      'timestamp': 887,
      'timestamp_label': '[00:14:47]',
      'timestamp_seconds': 887,
      'tip': 'We train a new model on all the past trades that have taken place on Paperstack. '
             "And then we compare it to There's There's like 40 data points that we're looking "
             'at. Some part of the collateral file, some part of the asset, some part of the '
             'market.',
      'title': 'Inside the New Paperstac: A New Era for Mortgage Note Trading (Paperstac)',
      'url': 'https://www.youtube.com/watch?v=zhg1k-uMJM0&t=887s',
      'video_id': 'zhg1k-uMJM0'},
     {'author': 'Chris Goff',
      'channel': 'Chris Goff',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=X_UODDIMvFs&t=15s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It works and when you would use one so today i queried all absentee owners in '
              'the entire u.s where the property value was above three hundred thousand with '
              'at.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'It works and when you would use one so today i queried all absentee owners in '
             'the entire u.s where the property value was above three hundred thousand with '
             'at.',
      'title': 'What is a Seller Finance Wrap Around Mortgage | EXPLAINED! (Chris Goff)',
      'url': 'https://www.youtube.com/watch?v=X_UODDIMvFs&t=15s',
      'video_id': 'X_UODDIMvFs'},
     {'author': 'Note Unlimited',
      'channel': 'Note Unlimited',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:04](https://www.youtube.com/watch?v=gUg3ObEfMB0&t=184s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Made by switching to the advanced interface investors can access the equity '
              "table and chart which provide insights into the property's market value over "
              'time and the potential growth in equity an essential factor in long-term '
              'investment.',
      'timestamp': 184,
      'timestamp_label': '[00:03:04]',
      'timestamp_seconds': 184,
      'tip': 'Made by switching to the advanced interface investors can access the equity '
             "table and chart which provide insights into the property's market value over "
             'time and the potential growth in equity an essential factor in long-term '
             'investment.',
      'title': 'Wraparound Mortgages Explained (Note Unlimited)',
      'url': 'https://www.youtube.com/watch?v=gUg3ObEfMB0&t=184s',
      'video_id': 'gUg3ObEfMB0'},
     {'author': 'Potential CPE',
      'channel': 'Potential CPE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:23](https://www.youtube.com/watch?v=mGwBpI_LQw0&t=203s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Thousand dollars in sales expenses at closing a $10,000 down payment is made '
              'the sale occurs on December 28 and payments will begin on January 28 of the '
              'following year during the time it was used as business property it had $50,000 '
              'of depreciation allowed or allowable.',
      'timestamp': 203,
      'timestamp_label': '[00:03:23]',
      'timestamp_seconds': 203,
      'tip': 'Thousand dollars in sales expenses at closing a $10,000 down payment is made the '
             'sale occurs on December 28 and payments will begin on January 28 of the '
             'following year during the time it was used as business property it had $50,000 '
             'of depreciation allowed or allowable.',
      'title': 'Taxes in Ten: Installment Sales (Potential CPE)',
      'url': 'https://www.youtube.com/watch?v=mGwBpI_LQw0&t=203s',
      'video_id': 'mGwBpI_LQw0'},
     {'author': 'Maximilian Dier',
      'channel': 'Maximilian Dier',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:10](https://www.youtube.com/watch?v=49GchpJCUB0&t=370s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Banks they don't qualify because I don't know maybe they have a cash business "
              "Banks don't like cash or maybe they got through a divorce and their credits.",
      'timestamp': 370,
      'timestamp_label': '[00:06:10]',
      'timestamp_seconds': 370,
      'tip': "Banks they don't qualify because I don't know maybe they have a cash business "
             "Banks don't like cash or maybe they got through a divorce and their credits.",
      'title': 'What is a Wraparound Mortgage in Real Estate? (Maximilian Dier)',
      'url': 'https://www.youtube.com/watch?v=49GchpJCUB0&t=370s',
      'video_id': '49GchpJCUB0'},
     {'author': 'Note Investing & Seller Financing - JKP Holdings',
      'channel': 'Note Investing & Seller Financing - JKP Holdings',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:19](https://www.youtube.com/watch?v=b-4NVMQ1GZ8&t=379s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t know what yield is, learn. When I first began this business, I was buying "
              "non-performers. I didn't know what yield was and I had to learn, right?",
      'timestamp': 379,
      'timestamp_label': '[00:06:19]',
      'timestamp_seconds': 379,
      'tip': "'t know what yield is, learn. When I first began this business, I was buying "
             "non-performers. I didn't know what yield was and I had to learn, right?",
      'title': 'Note Hypothecation with Local Banks w/ Justin Roberts | Real Estate Notes Show '
               'Ep 134 (Note Investing & Seller Financing - JKP Holdings)',
      'url': 'https://www.youtube.com/watch?v=b-4NVMQ1GZ8&t=379s',
      'video_id': 'b-4NVMQ1GZ8'},
     {'author': 'Caleb Christopher',
      'channel': 'Caleb Christopher',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:47](https://www.youtube.com/watch?v=UBngwrCrCxM&t=647s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You have a situation creative TC does wraps we do it we love it we advise on it '
              'our goal is to help you make informed decisions we are the premier transaction '
              'consulting firm in cretive real.',
      'timestamp': 647,
      'timestamp_label': '[00:10:47]',
      'timestamp_seconds': 647,
      'tip': 'You have a situation creative TC does wraps we do it we love it we advise on it '
             'our goal is to help you make informed decisions we are the premier transaction '
             'consulting firm in cretive real.',
      'title': 'Mirror Wrap vs Subto - When should you wrap? (Caleb Christopher)',
      'url': 'https://www.youtube.com/watch?v=UBngwrCrCxM&t=647s',
      'video_id': 'UBngwrCrCxM'},
     {'author': 'Hans Goldstein: Tax & Exit Planning',
      'channel': 'Hans Goldstein: Tax & Exit Planning',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:26](https://www.youtube.com/watch?v=-0WdI-B7uuM&t=26s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We can definitely map this out using published guidance. So under revenue '
              'ruling 2026-19, the October 2026 rates on a monthly compounding basis are 4. '
              'OK, so those are the October rates?',
      'timestamp': 26,
      'timestamp_label': '[00:00:26]',
      'timestamp_seconds': 26,
      'tip': 'We can definitely map this out using published guidance. So under revenue ruling '
             '2026-19, the October 2026 rates on a monthly compounding basis are 4. OK, so '
             'those are the October rates?',
      'title': 'Installment Sale Interest Rate AFR: What Is the Minimum? (2026) (Hans '
               'Goldstein: Tax & Exit Planning)',
      'url': 'https://www.youtube.com/watch?v=-0WdI-B7uuM&t=26s',
      'video_id': '-0WdI-B7uuM'},
     {'author': 'Edspira',
      'channel': 'Edspira',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:05](https://www.youtube.com/watch?v=OXZZS-KeaXc&t=185s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mortgage here so she conveys she conveys title title of the home to you and she '
              "extends a mortgage right or gives a mortgage right she's giving you a loan and "
              "that's that 200,000 let's say at the 8.5 perc.",
      'timestamp': 185,
      'timestamp_label': '[00:03:05]',
      'timestamp_seconds': 185,
      'tip': 'Mortgage here so she conveys she conveys title title of the home to you and she '
             "extends a mortgage right or gives a mortgage right she's giving you a loan and "
             "that's that 200,000 let's say at the 8.5 perc.",
      'title': 'Wraparound Mortages (Edspira)',
      'url': 'https://www.youtube.com/watch?v=OXZZS-KeaXc&t=185s',
      'video_id': 'OXZZS-KeaXc'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:06](https://www.youtube.com/watch?v=RZpKVqqUZPQ&t=66s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Even care about the due on sale clause especially in a in a subject-to '
              "transaction but it's something you should bring up i have had the due on.",
      'timestamp': 66,
      'timestamp_label': '[00:01:06]',
      'timestamp_seconds': 66,
      'tip': 'Even care about the due on sale clause especially in a in a subject-to '
             "transaction but it's something you should bring up i have had the due on.",
      'title': 'What is a Due on Sale Clause | What you Need to Know (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=RZpKVqqUZPQ&t=66s',
      'video_id': 'RZpKVqqUZPQ'}],
 2: [{'author': 'TerraFunded',
      'channel': 'TerraFunded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:00](https://www.youtube.com/watch?v=Q9c1Be5WnWI&t=600s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We don't use contracts for deed. One example is Olney, in Young County, listed "
              'at $99,000 cash, with $5,940 down, then $1,213 a month for 180 payments, at a '
              "10% APR, fixed. There's no balloon payment. Closing costs are about $1,500, "
              'paid to the title company.',
      'timestamp': 600,
      'timestamp_label': '[00:10:00]',
      'timestamp_seconds': 600,
      'tip': "We don't use contracts for deed. One example is Olney, in Young County, listed "
             'at $99,000 cash, with $5,940 down, then $1,213 a month for 180 payments, at a '
             "10% APR, fixed. There's no balloon payment. Closing costs are about $1,500, paid "
             'to the title company.',
      'title': 'Contract for Deed vs Deed of Trust Texas: 3 Scenarios Side by Side, With an '
               'Equity Example (TerraFunded)',
      'url': 'https://www.youtube.com/watch?v=Q9c1Be5WnWI&t=600s',
      'video_id': 'Q9c1Be5WnWI'},
     {'author': 'Toby Mathis Esq | Tax Planning & Asset Protection',
      'channel': 'Toby Mathis Esq | Tax Planning & Asset Protection',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:53](https://www.youtube.com/watch?v=LuxJXWLFKHI&t=113s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now normally they would go to a bank or some other lender and get that cash. '
              'Well, in this case, the seller of the property says, no, I will take back a '
              "note. It'll be 9% interest, 15 years, and the property buyer will then pay the "
              'seller instead of the bank.',
      'timestamp': 113,
      'timestamp_label': '[00:01:53]',
      'timestamp_seconds': 113,
      'tip': 'Now normally they would go to a bank or some other lender and get that cash. '
             'Well, in this case, the seller of the property says, no, I will take back a '
             "note. It'll be 9% interest, 15 years, and the property buyer will then pay the "
             'seller instead of the bank.',
      'title': 'How To Be A Note Investor (A Step-By-Step GUIDE) (Toby Mathis Esq | Tax '
               'Planning & Asset Protection)',
      'url': 'https://www.youtube.com/watch?v=LuxJXWLFKHI&t=113s',
      'video_id': 'LuxJXWLFKHI'},
     {'author': 'Hans Goldstein: Tax & Exit Planning',
      'channel': 'Hans Goldstein: Tax & Exit Planning',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:24](https://www.youtube.com/watch?v=v8iQSeRjmR8&t=84s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Okay, so let's walk through the worked example to see the exact application. An "
              'owner sells a building with an adjusted basis well below its existing mortgage. '
              'And the buyer pays a modest down payment and signs a wrap note covering the '
              'rest of the price.',
      'timestamp': 84,
      'timestamp_label': '[00:01:24]',
      'timestamp_seconds': 84,
      'tip': "Okay, so let's walk through the worked example to see the exact application. An "
             'owner sells a building with an adjusted basis well below its existing mortgage. '
             'And the buyer pays a modest down payment and signs a wrap note covering the rest '
             'of the price.',
      'title': 'Wrap Around Mortgage: How Is the Seller Taxed? (2026) (Hans Goldstein: Tax & '
               'Exit Planning)',
      'url': 'https://www.youtube.com/watch?v=v8iQSeRjmR8&t=84s',
      'video_id': 'v8iQSeRjmR8'},
     {'author': 'Mr No FluFF (My Real Estate DOJO)',
      'channel': 'Mr No FluFF (My Real Estate DOJO)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:16](https://www.youtube.com/watch?v=oHV9AiZdwro&t=256s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Without qualifying it without using my credit without using down payment uh '
              'without paying all the junk fees of title company I can just step into the.',
      'timestamp': 256,
      'timestamp_label': '[00:04:16]',
      'timestamp_seconds': 256,
      'tip': 'Without qualifying it without using my credit without using down payment uh '
             'without paying all the junk fees of title company I can just step into the.',
      'title': 'Subject-To vs Wraparound Mortgage: The Key Differences & Which One Makes You '
               'More Money? 💰🔥 (Mr No FluFF (My Real Estate DOJO))',
      'url': 'https://www.youtube.com/watch?v=oHV9AiZdwro&t=256s',
      'video_id': 'oHV9AiZdwro'},
     {'author': "Scott Horne's Owner Finance Network",
      'channel': "Scott Horne's Owner Finance Network",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:05](https://www.youtube.com/watch?v=VDXOvtqzbZk&t=485s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can negotiate your closing costs with them. Usually, the buyer pays all the '
              'closing costs in these kinds of deals, but not always.',
      'timestamp': 485,
      'timestamp_label': '[00:08:05]',
      'timestamp_seconds': 485,
      'tip': 'You can negotiate your closing costs with them. Usually, the buyer pays all the '
             'closing costs in these kinds of deals, but not always.',
      'title': 'Wraparound Mortgage 101: How Wraps Work, When to Use Them, and Required '
               "Disclosures (Scott Horne's Owner Finance Network)",
      'url': 'https://www.youtube.com/watch?v=VDXOvtqzbZk&t=485s',
      'video_id': 'VDXOvtqzbZk'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[02:27:01](https://www.youtube.com/watch?v=IHTKcj3dVN0&t=8821s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm happy to pay that agent. I just brought I just brought in a partner to pay "
              "that so I didn't have to. And that partner paid for closing costs, agents, paid "
              'for my acquisition fee, and even put $60,000 in the bank account the day we '
              'bought the the park.',
      'timestamp': 8821,
      'timestamp_label': '[02:27:01]',
      'timestamp_seconds': 8821,
      'tip': "I'm happy to pay that agent. I just brought I just brought in a partner to pay "
             "that so I didn't have to. And that partner paid for closing costs, agents, paid "
             'for my acquisition fee, and even put $60,000 in the bank account the day we '
             'bought the the park.',
      'title': 'Generating Leads for Creative Finance pt 2 (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=IHTKcj3dVN0&t=8821s',
      'video_id': 'IHTKcj3dVN0'},
     {'author': 'Caleb Christopher',
      'channel': 'Caleb Christopher',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=UOyoE5Fc7VE&t=78s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "75 so let's see what that or 7. 450 or plus 275 the two of you are bringing in "
              '729 a month on Equity pay down and interest okay that sounds good now the total '
              "monthly payment for your buyer that's the other thing you have to look at 230 "
              "so I'll do the real full price 250.",
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': "75 so let's see what that or 7. 450 or plus 275 the two of you are bringing in "
             '729 a month on Equity pay down and interest okay that sounds good now the total '
             "monthly payment for your buyer that's the other thing you have to look at 230 so "
             "I'll do the real full price 250.",
      'title': 'How to wrap mortgage cash flow with Creative Underwriter Spreadsheet (Caleb '
               'Christopher)',
      'url': 'https://www.youtube.com/watch?v=UOyoE5Fc7VE&t=78s',
      'video_id': 'UOyoE5Fc7VE'},
     {'author': 'Ron LeGrand',
      'channel': 'Ron LeGrand',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:33](https://www.youtube.com/watch?v=qGlXYUEjyr8&t=153s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "He ain't going to scound and not pay his payment. Take away a bunch of his "
              'equity for screwing up his own deal. You get your attorney to help you on that '
              "and he'll know exactly what to do. But you have to write the contract up as a "
              '$450,000 seller carryback.',
      'timestamp': 153,
      'timestamp_label': '[00:02:33]',
      'timestamp_seconds': 153,
      'tip': "He ain't going to scound and not pay his payment. Take away a bunch of his "
             'equity for screwing up his own deal. You get your attorney to help you on that '
             "and he'll know exactly what to do. But you have to write the contract up as a "
             '$450,000 seller carryback.',
      'title': 'Structuring A Wraparound Mortgage (Ron LeGrand)',
      'url': 'https://www.youtube.com/watch?v=qGlXYUEjyr8&t=153s',
      'video_id': 'qGlXYUEjyr8'},
     {'author': 'Moxxie Education - Seller Financing & Notes',
      'channel': 'Moxxie Education - Seller Financing & Notes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:44](https://www.youtube.com/watch?v=usXnfzN3Wmc&t=44s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A note with zero payment history is harder for a note buyer to evaluate because '
              "there's no track record yet to prove your borrower will will actually pay "
              'reliably.',
      'timestamp': 44,
      'timestamp_label': '[00:00:44]',
      'timestamp_seconds': 44,
      'tip': 'A note with zero payment history is harder for a note buyer to evaluate because '
             "there's no track record yet to prove your borrower will will actually pay "
             'reliably.',
      'title': 'Can I Sell My Seller Financed Mortgage Note After Just ONE Payment? (Moxxie '
               'Education - Seller Financing & Notes)',
      'url': 'https://www.youtube.com/watch?v=usXnfzN3Wmc&t=44s',
      'video_id': 'usXnfzN3Wmc'},
     {'author': 'KELLY ZITLOW',
      'channel': 'KELLY ZITLOW',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=pYujIjfIOkE&t=108s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mortgage level so Kelly in a traditional purchase and sale where we have a '
              "seller and a buyer the the seller's mortgage loan gets paid off at close of "
              'escrow.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': 'Mortgage level so Kelly in a traditional purchase and sale where we have a '
             "seller and a buyer the the seller's mortgage loan gets paid off at close of "
             'escrow.',
      'title': 'Subject-To & Wrap Financing EXPLAINED by a Real Estate Lawyer (KELLY ZITLOW)',
      'url': 'https://www.youtube.com/watch?v=pYujIjfIOkE&t=108s',
      'video_id': 'pYujIjfIOkE'},
     {'author': 'The Real Estate Lawyer',
      'channel': 'The Real Estate Lawyer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:37](https://www.youtube.com/watch?v=2PWuaqjQVgc&t=37s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Closing table then you have heard me say in the past or you will hear me say '
              "when explaining this is it means if you don't pay you don't stay and you only "
              'get to.',
      'timestamp': 37,
      'timestamp_label': '[00:00:37]',
      'timestamp_seconds': 37,
      'tip': 'Closing table then you have heard me say in the past or you will hear me say '
             "when explaining this is it means if you don't pay you don't stay and you only "
             'get to.',
      'title': 'What is a Deed of Trust?  (Legal Definition + Examples) (The Real Estate '
               'Lawyer)',
      'url': 'https://www.youtube.com/watch?v=2PWuaqjQVgc&t=37s',
      'video_id': '2PWuaqjQVgc'},
     {'author': 'kris haskins',
      'channel': 'kris haskins',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:21](https://www.youtube.com/watch?v=DhOoZcypJCM&t=141s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Year so what happens in the bankruptcy let's say they file Boom the payment "
              "stopped that doesn't mean that the interest still doesn't accrue.",
      'timestamp': 141,
      'timestamp_label': '[00:02:21]',
      'timestamp_seconds': 141,
      'tip': "Year so what happens in the bankruptcy let's say they file Boom the payment "
             "stopped that doesn't mean that the interest still doesn't accrue.",
      'title': 'HOW to buy pre-foreclosures Subject To before auction (kris haskins)',
      'url': 'https://www.youtube.com/watch?v=DhOoZcypJCM&t=141s',
      'video_id': 'DhOoZcypJCM'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:29](https://www.youtube.com/watch?v=t7aFESM6V_k&t=389s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Grand so I'd rather take his assignment fee pay towards that cover all of those "
              "costs than give him a $10,000 fee but what I will do is I'll say I will pay.",
      'timestamp': 389,
      'timestamp_label': '[00:06:29]',
      'timestamp_seconds': 389,
      'tip': "Grand so I'd rather take his assignment fee pay towards that cover all of those "
             "costs than give him a $10,000 fee but what I will do is I'll say I will pay.",
      'title': 'Determining if a Creative Finance Deal Is Good or Not (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=t7aFESM6V_k&t=389s',
      'video_id': 't7aFESM6V_k'},
     {'author': 'Caleb Christopher',
      'channel': 'Caleb Christopher',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:45](https://www.youtube.com/watch?v=369aexLYPNM&t=165s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Didn't consult so the pricing difference should you know should tell you the "
              'the thing with the refinance the only person that can refinance a property is '
              'the owner when you buy Sub 2 then then but the buyer becomes the owner of title '
              'officially.',
      'timestamp': 165,
      'timestamp_label': '[00:02:45]',
      'timestamp_seconds': 165,
      'tip': "Didn't consult so the pricing difference should you know should tell you the the "
             'thing with the refinance the only person that can refinance a property is the '
             'owner when you buy Sub 2 then then but the buyer becomes the owner of title '
             'officially.',
      'title': 'Who gets title on a subto? And what if the Seller files bankruptcy? (Caleb '
               'Christopher)',
      'url': 'https://www.youtube.com/watch?v=369aexLYPNM&t=165s',
      'video_id': '369aexLYPNM'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:16](https://www.youtube.com/watch?v=W60Ytz4Wb5U&t=1036s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They get synced up two if that does not work which that does happen we'll we'll "
              "actually have to go through and we'll do one of multiple options we'll do an "
              'executory contract.',
      'timestamp': 1036,
      'timestamp_label': '[00:17:16]',
      'timestamp_seconds': 1036,
      'tip': "They get synced up two if that does not work which that does happen we'll we'll "
             "actually have to go through and we'll do one of multiple options we'll do an "
             'executory contract.',
      'title': 'Should You Be Worried About the Due on Sale Clause? (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=W60Ytz4Wb5U&t=1036s',
      'video_id': 'W60Ytz4Wb5U'}],
 3: [{'author': 'Lex Levinrad Real Estate Training and Coaching',
      'channel': 'Lex Levinrad Real Estate Training and Coaching',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:33](https://www.youtube.com/watch?v=NKTKZd6UIHg&t=333s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Keep in mind, if they were to sell it at $170 with an agent, they'd have a 6% "
              'commission and have three or 4% in closing costs. So $170 less, 10% would knock '
              "them down to, what is that $170 minus $17? So basically they're only going to "
              'net $153 but they owe the bank $170.',
      'timestamp': 333,
      'timestamp_label': '[00:05:33]',
      'timestamp_seconds': 333,
      'tip': "Keep in mind, if they were to sell it at $170 with an agent, they'd have a 6% "
             'commission and have three or 4% in closing costs. So $170 less, 10% would knock '
             "them down to, what is that $170 minus $17? So basically they're only going to "
             'net $153 but they owe the bank $170.',
      'title': 'Buying Houses Subject To The Existing Mortgage | Sub To Real Estate Investing '
               '(Lex Levinrad Real Estate Training and Coaching)',
      'url': 'https://www.youtube.com/watch?v=NKTKZd6UIHg&t=333s',
      'video_id': 'NKTKZd6UIHg'},
     {'author': 'The Landlord Dropout',
      'channel': 'The Landlord Dropout',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:33](https://www.youtube.com/watch?v=hIflx_8aWVI&t=213s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s a $400 monthly improvement before those remaining costs. Over 12 months, "
              'that difference is $4,800. And the $4,000 down payment is separate cash '
              "received up front. I'm not counting it again in the monthly comparison.",
      'timestamp': 213,
      'timestamp_label': '[00:03:33]',
      'timestamp_seconds': 213,
      'tip': "'s a $400 monthly improvement before those remaining costs. Over 12 months, that "
             'difference is $4,800. And the $4,000 down payment is separate cash received up '
             "front. I'm not counting it again in the monthly comparison.",
      'title': 'My First Creative Finance Deal (The Landlord Dropout)',
      'url': 'https://www.youtube.com/watch?v=hIflx_8aWVI&t=213s',
      'video_id': 'hIflx_8aWVI'},
     {'author': 'Caleb Christopher',
      'channel': 'Caleb Christopher',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:20](https://www.youtube.com/watch?v=BBTWC2u7edM&t=140s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Cash uh I don't know how fees yes as far as the the costs of closing etc but "
              "there may not be any any cash to seller in the transaction well and it's not a "
              "mortgage assumption it's just to continue paying on behalf of the mortgagor.",
      'timestamp': 140,
      'timestamp_label': '[00:02:20]',
      'timestamp_seconds': 140,
      'tip': "Cash uh I don't know how fees yes as far as the the costs of closing etc but "
             "there may not be any any cash to seller in the transaction well and it's not a "
             "mortgage assumption it's just to continue paying on behalf of the mortgagor.",
      'title': 'Why are title companies scared of creative finance?? (Caleb Christopher)',
      'url': 'https://www.youtube.com/watch?v=BBTWC2u7edM&t=140s',
      'video_id': 'BBTWC2u7edM'},
     {'author': 'Evan Ragsdale',
      'channel': 'Evan Ragsdale',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:25](https://www.youtube.com/watch?v=m8scT0nPuzY&t=145s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s name and we still controlled the property, the cash flow, and the upside "
              'with the same economics, but just less exposure and no harm to the homeowner. '
              "The lesson isn't don't do subject two deals. The lesson is that creative "
              "finance isn't about shortcuts.",
      'timestamp': 145,
      'timestamp_label': '[00:02:25]',
      'timestamp_seconds': 145,
      'tip': "'s name and we still controlled the property, the cash flow, and the upside with "
             'the same economics, but just less exposure and no harm to the homeowner. The '
             "lesson isn't don't do subject two deals. The lesson is that creative finance "
             "isn't about shortcuts.",
      'title': 'I Had The Due-On-Sale Clause Called on My Subject-To Deal (Real Story) (Evan '
               'Ragsdale)',
      'url': 'https://www.youtube.com/watch?v=m8scT0nPuzY&t=145s',
      'video_id': 'm8scT0nPuzY'},
     {'author': 'Sierra Davis',
      'channel': 'Sierra Davis',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:44:17](https://www.youtube.com/watch?v=UimgP_cJydU&t=2657s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And so making sure that you're pricing it um well so that you're you know able "
              "to do these things um whether it's legal cost or you know foreclosure the state "
              'um make sure that you kind of pricing everything within a worst case scenario.',
      'timestamp': 2657,
      'timestamp_label': '[00:44:17]',
      'timestamp_seconds': 2657,
      'tip': "And so making sure that you're pricing it um well so that you're you know able "
             "to do these things um whether it's legal cost or you know foreclosure the state "
             'um make sure that you kind of pricing everything within a worst case scenario.',
      'title': 'How to Become the Bank in 2026 (Note Investing Full Breakdown) (Sierra Davis)',
      'url': 'https://www.youtube.com/watch?v=UimgP_cJydU&t=2657s',
      'video_id': 'UimgP_cJydU'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:03](https://www.youtube.com/watch?v=cOTyo3LTDPk&t=123s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'There are companies out there that um will provide due on sale clause '
              "insurance. There's a business for everything. There is a business for "
              'everything. So, the the cost of due on sale clauses insurance is about 1% of '
              'the purchase price of the home.',
      'timestamp': 123,
      'timestamp_label': '[00:02:03]',
      'timestamp_seconds': 123,
      'tip': 'There are companies out there that um will provide due on sale clause insurance. '
             "There's a business for everything. There is a business for everything. So, the "
             'the cost of due on sale clauses insurance is about 1% of the purchase price of '
             'the home.',
      'title': 'Overcoming The Due On Sale Clause In Subject To (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=cOTyo3LTDPk&t=123s',
      'video_id': 'cOTyo3LTDPk'},
     {'author': 'Creative Finance Playbook',
      'channel': 'Creative Finance Playbook',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:11](https://www.youtube.com/watch?v=u3lV-kVx-LU&t=251s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sitting there they took a VA loan out a VA loan means that he put zero money '
              'down he bought it they rolled in closing costs and everything so this seller '
              'has.',
      'timestamp': 251,
      'timestamp_label': '[00:04:11]',
      'timestamp_seconds': 251,
      'tip': 'Sitting there they took a VA loan out a VA loan means that he put zero money '
             'down he bought it they rolled in closing costs and everything so this seller '
             'has.',
      'title': "How a Wrap Mortgage Turns a Seller's Low Rate Into Profit (Creative Finance "
               'Playbook)',
      'url': 'https://www.youtube.com/watch?v=u3lV-kVx-LU&t=251s',
      'video_id': 'u3lV-kVx-LU'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:13](https://www.youtube.com/watch?v=FeymZ_67wns&t=373s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That doesn't leave you very much margin. All right, so what if the property's "
              "in disrepair? That's gonna cause you even more scratching your head. You "
              "probably don't want that. So foreclosure properties are not easy. This is not a "
              'piece of cake.',
      'timestamp': 373,
      'timestamp_label': '[00:06:13]',
      'timestamp_seconds': 373,
      'tip': "That doesn't leave you very much margin. All right, so what if the property's in "
             "disrepair? That's gonna cause you even more scratching your head. You probably "
             "don't want that. So foreclosure properties are not easy. This is not a piece of "
             'cake.',
      'title': 'Deed in Lieu of Foreclosure Part 2 (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=FeymZ_67wns&t=373s',
      'video_id': 'FeymZ_67wns'},
     {'author': 'Ed Billheimer',
      'channel': 'Ed Billheimer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:39](https://www.youtube.com/watch?v=z2sAmk5whKo&t=639s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sure that everything is what they want it to be and then the buyer and the '
              "seller go to closing so that's pretty much everything I'm happy to answer "
              'whatever questions.',
      'timestamp': 639,
      'timestamp_label': '[00:10:39]',
      'timestamp_seconds': 639,
      'tip': 'Sure that everything is what they want it to be and then the buyer and the '
             "seller go to closing so that's pretty much everything I'm happy to answer "
             'whatever questions.',
      'title': 'Dodd Frank compliance for owner carry (Ed Billheimer)',
      'url': 'https://www.youtube.com/watch?v=z2sAmk5whKo&t=639s',
      'video_id': 'z2sAmk5whKo'},
     {'author': 'My Mortgage Trainer, Inc.',
      'channel': 'My Mortgage Trainer, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:18](https://www.youtube.com/watch?v=3qzRqAVS2ZA&t=138s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Obligations seven monthly debt to income ratio or residual income that you '
              'calculated using the total of all the mortgage and non-mortgage obligations '
              'listed above as a ratio of the gross monthly income and then finally number '
              'eight credit history.',
      'timestamp': 138,
      'timestamp_label': '[00:02:18]',
      'timestamp_seconds': 138,
      'tip': 'Obligations seven monthly debt to income ratio or residual income that you '
             'calculated using the total of all the mortgage and non-mortgage obligations '
             'listed above as a ratio of the gross monthly income and then finally number '
             'eight credit history.',
      'title': 'Dodd Frank Ability to Repay Rule (Module 3) | NMLS SAFE MLO Exam Study Series '
               'and Test Prep (My Mortgage Trainer, Inc.)',
      'url': 'https://www.youtube.com/watch?v=3qzRqAVS2ZA&t=138s',
      'video_id': '3qzRqAVS2ZA'},
     {'author': 'The Lee Arnold System of Real Estate Investing',
      'channel': 'The Lee Arnold System of Real Estate Investing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:22](https://www.youtube.com/watch?v=tszcHb-Spo4&t=262s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "$100,000 so your $40,000 investment becomes a $60,000 profit if you'd like to "
              'learn more about these stages of the ugly note and how you can take advantage '
              'and get involved in this style of real estate investing simply click the link.',
      'timestamp': 262,
      'timestamp_label': '[00:04:22]',
      'timestamp_seconds': 262,
      'tip': "$100,000 so your $40,000 investment becomes a $60,000 profit if you'd like to "
             'learn more about these stages of the ugly note and how you can take advantage '
             'and get involved in this style of real estate investing simply click the link.',
      'title': 'How to Buy Mortgage Notes at GREAT Discounts (The Lee Arnold System of Real '
               'Estate Investing)',
      'url': 'https://www.youtube.com/watch?v=tszcHb-Spo4&t=262s',
      'video_id': 'tszcHb-Spo4'},
     {'author': 'Brian Gibbons',
      'channel': 'Brian Gibbons',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:00](https://www.youtube.com/watch?v=Ee0wPpu_LNc&t=180s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Just by a natural person to be able to own or Finance their property without '
              "interference from the government so I hope you've enjoyed this particular "
              'recording about what are the seller finance consumer exemptions under dodf '
              'Frank Act.',
      'timestamp': 180,
      'timestamp_label': '[00:03:00]',
      'timestamp_seconds': 180,
      'tip': 'Just by a natural person to be able to own or Finance their property without '
             "interference from the government so I hope you've enjoyed this particular "
             'recording about what are the seller finance consumer exemptions under dodf Frank '
             'Act.',
      'title': 'Seller Financing - Exemptions Under Dodd Frank Act (Brian Gibbons)',
      'url': 'https://www.youtube.com/watch?v=Ee0wPpu_LNc&t=180s',
      'video_id': 'Ee0wPpu_LNc'},
     {'author': 'Flipping Mastery TV',
      'channel': 'Flipping Mastery TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:29](https://www.youtube.com/watch?v=rYMNGajRMfo&t=569s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'How does everything play together if everything sucks like high interest rate '
              "high down payment high price high high high No Deal No One's Gonna want it so "
              "everything kind of comes together there's give and take I guess right so I "
              "don't know.",
      'timestamp': 569,
      'timestamp_label': '[00:09:29]',
      'timestamp_seconds': 569,
      'tip': 'How does everything play together if everything sucks like high interest rate '
             "high down payment high price high high high No Deal No One's Gonna want it so "
             "everything kind of comes together there's give and take I guess right so I don't "
             'know.',
      'title': 'How To Explain A Subject To Offer to A Real Estate Agent (Flipping Mastery TV)',
      'url': 'https://www.youtube.com/watch?v=rYMNGajRMfo&t=569s',
      'video_id': 'rYMNGajRMfo'},
     {'author': 'Ron LeGrand',
      'channel': 'Ron LeGrand',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:23](https://www.youtube.com/watch?v=-3xVEOBXFzc&t=563s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Questions you can go to ask here it is ask ron legrand.com and I'll answer your "
              'questions uh very quickly and uh you can uh also go to ronaldgrand.com and '
              "there's a whole host of things on there that you can get a lot of it for free.",
      'timestamp': 563,
      'timestamp_label': '[00:09:23]',
      'timestamp_seconds': 563,
      'tip': "Questions you can go to ask here it is ask ron legrand.com and I'll answer your "
             'questions uh very quickly and uh you can uh also go to ronaldgrand.com and '
             "there's a whole host of things on there that you can get a lot of it for free.",
      'title': 'Ron LeGrand Reviews the Pros and Cons of a Wrap-Around Mortgage vs Subject To '
               'Mortgage (Ron LeGrand)',
      'url': 'https://www.youtube.com/watch?v=-3xVEOBXFzc&t=563s',
      'video_id': '-3xVEOBXFzc'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:14](https://www.youtube.com/watch?v=Yw9I--p2Ef8&t=494s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Understand how do we determine what the renovation costs are I don't think he "
              "borrowed enough money personally yeah right yeah he's in a bad situation we're "
              'going to talk about how much that renovation is in part two of Pepper Place see '
              'you in that video.',
      'timestamp': 494,
      'timestamp_label': '[00:08:14]',
      'timestamp_seconds': 494,
      'tip': "Understand how do we determine what the renovation costs are I don't think he "
             "borrowed enough money personally yeah right yeah he's in a bad situation we're "
             'going to talk about how much that renovation is in part two of Pepper Place see '
             'you in that video.',
      'title': 'Cash Flowing From This Subject To/Seller Finance Hybrid (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=Yw9I--p2Ef8&t=494s',
      'video_id': 'Yw9I--p2Ef8'}],
 4: [{'author': 'Music City TC',
      'channel': 'Music City TC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:18](https://www.youtube.com/watch?v=-AAdJ4WwUuM&t=138s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Typically, that's the signed purchase agreement and every addendum, the "
              "seller's most recent mortgage statement, a signed authorization so the title "
              "company can talk to the seller's lender, and if you're buying in an LLC, your "
              'entity documents.',
      'timestamp': 138,
      'timestamp_label': '[00:02:18]',
      'timestamp_seconds': 138,
      'tip': "Typically, that's the signed purchase agreement and every addendum, the seller's "
             'most recent mortgage statement, a signed authorization so the title company can '
             "talk to the seller's lender, and if you're buying in an LLC, your entity "
             'documents.',
      'title': '12 Questions to Ask a Title Company Before You Send a Subject-To or Creative '
               'Finance Deal (Music City TC)',
      'url': 'https://www.youtube.com/watch?v=-AAdJ4WwUuM&t=138s',
      'video_id': '-AAdJ4WwUuM'},
     {'author': 'Clint Coons Esq. | Real Estate Asset Protection',
      'channel': 'Clint Coons Esq. | Real Estate Asset Protection',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:42](https://www.youtube.com/watch?v=0hSERgZotJM&t=162s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "All we're doing is creating the perception the seller does not own it. Well, in "
              "order to do that, we're not going to use a limited liability company as as our "
              "entity. In fact, what I want to use is I'm going to set up here a land trust.",
      'timestamp': 162,
      'timestamp_label': '[00:02:42]',
      'timestamp_seconds': 162,
      'tip': "All we're doing is creating the perception the seller does not own it. Well, in "
             "order to do that, we're not going to use a limited liability company as as our "
             "entity. In fact, what I want to use is I'm going to set up here a land trust.",
      'title': 'How To Overcome The Due On Sale Clause On A Subject To Deal (Clint Coons Esq. '
               '| Real Estate Asset Protection)',
      'url': 'https://www.youtube.com/watch?v=0hSERgZotJM&t=162s',
      'video_id': '0hSERgZotJM'},
     {'author': 'Agent2Investor Podcast',
      'channel': 'Agent2Investor Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:44:07](https://www.youtube.com/watch?v=XsNZ5SQXdCI&t=2647s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s buy just 72 would be good and they accept that and you get the one to 2% 1 "
              "to 3% at closing. Um so that's a nice way to kind of get some cash if you don't "
              'have a lot of cash >> um and to make some good really strong connections. Do '
              'you have to have any kind of license?',
      'timestamp': 2647,
      'timestamp_label': '[00:44:07]',
      'timestamp_seconds': 2647,
      'tip': "'s buy just 72 would be good and they accept that and you get the one to 2% 1 to "
             "3% at closing. Um so that's a nice way to kind of get some cash if you don't "
             'have a lot of cash >> um and to make some good really strong connections. Do you '
             'have to have any kind of license?',
      'title': 'The Note Investing Strategy for Busy W-2 Professionals with Sierra Davis '
               '(Agent2Investor Podcast)',
      'url': 'https://www.youtube.com/watch?v=XsNZ5SQXdCI&t=2647s',
      'video_id': 'XsNZ5SQXdCI'},
     {'author': 'Ken McElroy',
      'channel': 'Ken McElroy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:08](https://www.youtube.com/watch?v=ulx_sqYnYVA&t=308s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "LLC and the same percentages. And I think if you do that, you shouldn't have to "
              'fear about the due on sale clause and think about it. Just imagine if Bank of '
              'America started calling all of these loans.',
      'timestamp': 308,
      'timestamp_label': '[00:05:08]',
      'timestamp_seconds': 308,
      'tip': "LLC and the same percentages. And I think if you do that, you shouldn't have to "
             'fear about the due on sale clause and think about it. Just imagine if Bank of '
             'America started calling all of these loans.',
      'title': "Transferring Property to an LLC: Don't Fear the Due On Sale Clause (Ken "
               'McElroy)',
      'url': 'https://www.youtube.com/watch?v=ulx_sqYnYVA&t=308s',
      'video_id': 'ulx_sqYnYVA'},
     {'author': 'REISkills.com - Where you learn Real Estate Investing',
      'channel': 'REISkills.com - Where you learn Real Estate Investing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:05](https://www.youtube.com/watch?v=9rVA292DHlY&t=245s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Clause on the underlying first lean this is due to the fact that the title of '
              'the property has transferred without the underlying loan getting paid off or '
              'assumed we do use Land Trust many times in a wraparound.',
      'timestamp': 245,
      'timestamp_label': '[00:04:05]',
      'timestamp_seconds': 245,
      'tip': 'Clause on the underlying first lean this is due to the fact that the title of '
             'the property has transferred without the underlying loan getting paid off or '
             'assumed we do use Land Trust many times in a wraparound.',
      'title': 'Wrap Around Mortgage - AITD - All Inclusive Trust Deed (REISkills.com - Where '
               'you learn Real Estate Investing)',
      'url': 'https://www.youtube.com/watch?v=9rVA292DHlY&t=245s',
      'video_id': '9rVA292DHlY'},
     {'author': 'National Mortgage Exam',
      'channel': 'National Mortgage Exam',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:55](https://www.youtube.com/watch?v=xZohXlsFnks&t=1195s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "In order to file for renew of a new license all right and if you've been "
              'expired for more than five years then you have to take the national exam again '
              "wouldn't that be fun all right change of employer loan originator must notify "
              'the current employer.',
      'timestamp': 1195,
      'timestamp_label': '[00:19:55]',
      'timestamp_seconds': 1195,
      'tip': "In order to file for renew of a new license all right and if you've been expired "
             "for more than five years then you have to take the national exam again wouldn't "
             'that be fun all right change of employer loan originator must notify the current '
             'employer.',
      'title': 'SAFE Act - Part 2 (Free Tutorial) (National Mortgage Exam)',
      'url': 'https://www.youtube.com/watch?v=xZohXlsFnks&t=1195s',
      'video_id': 'xZohXlsFnks'},
     {'author': 'Ben Jensen | Preforeclosure Real Estate',
      'channel': 'Ben Jensen | Preforeclosure Real Estate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:29](https://www.youtube.com/watch?v=t96wzMUDN58&t=329s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll literally give you what your monthly payment will be. And then you can add "
              'annual taxes and insurance to see what your total is. But basically, all I did, '
              'I\'m not some science wizard or anything. I said, "Okay, they want $150,000 and '
              'I want a 0% interest rate.".',
      'timestamp': 329,
      'timestamp_label': '[00:05:29]',
      'timestamp_seconds': 329,
      'tip': "'ll literally give you what your monthly payment will be. And then you can add "
             'annual taxes and insurance to see what your total is. But basically, all I did, '
             'I\'m not some science wizard or anything. I said, "Okay, they want $150,000 and '
             'I want a 0% interest rate.".',
      'title': 'How To Use Wrap Around Mortgages With SubTo & Seller Finance (Ben Jensen | '
               'Preforeclosure Real Estate)',
      'url': 'https://www.youtube.com/watch?v=t96wzMUDN58&t=329s',
      'video_id': 't96wzMUDN58'},
     {'author': 'LawCall',
      'channel': 'LawCall',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:09](https://www.youtube.com/watch?v=5VQnTCJTxZ0&t=69s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If they do not pay those fees in accordance with the terms of their covenants '
              'restrictions and their declarations and all the other things that come with '
              'that stack of paperwork that they sign when they purchase the property, those '
              "fees aren't paid.",
      'timestamp': 69,
      'timestamp_label': '[00:01:09]',
      'timestamp_seconds': 69,
      'tip': 'If they do not pay those fees in accordance with the terms of their covenants '
             'restrictions and their declarations and all the other things that come with that '
             'stack of paperwork that they sign when they purchase the property, those fees '
             "aren't paid.",
      'title': 'LawCall Panama City, FL - HOA Foreclosure: Do I Still Owe the Mortgage? - 2025 '
               '(LawCall)',
      'url': 'https://www.youtube.com/watch?v=5VQnTCJTxZ0&t=69s',
      'video_id': '5VQnTCJTxZ0'},
     {'author': 'Lex Levinrad Real Estate Training and Coaching',
      'channel': 'Lex Levinrad Real Estate Training and Coaching',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:08](https://www.youtube.com/watch?v=YY7F8y8K0cU&t=548s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Instead is keep the insurance in place that's originally there and simply call "
              'up the insurance agent and add the land trust as an additional Insurance say '
              'my.',
      'timestamp': 548,
      'timestamp_label': '[00:09:08]',
      'timestamp_seconds': 548,
      'tip': "Instead is keep the insurance in place that's originally there and simply call "
             'up the insurance agent and add the land trust as an additional Insurance say my.',
      'title': 'How To Buy Houses Subject To The Existing Mortgage Explained in Detail (Lex '
               'Levinrad Real Estate Training and Coaching)',
      'url': 'https://www.youtube.com/watch?v=YY7F8y8K0cU&t=548s',
      'video_id': 'YY7F8y8K0cU'},
     {'author': 'Paperstac',
      'channel': 'Paperstac',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=_BvWeumu2WI&t=15s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The paper stack podcast i am brett burkey this is rick allen and we're here "
              'today to talk to you about something that a lot of buyers.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "The paper stack podcast i am brett burkey this is rick allen and we're here "
             'today to talk to you about something that a lot of buyers.',
      'title': '5 Creative Ways to Fund Your Next Mortgage Note Purchase (Paperstac)',
      'url': 'https://www.youtube.com/watch?v=_BvWeumu2WI&t=15s',
      'video_id': '_BvWeumu2WI'},
     {'author': 'Seller Finance Consultants, Inc.',
      'channel': 'Seller Finance Consultants, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:06](https://www.youtube.com/watch?v=0jNAfoc37ko&t=186s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Insurance and service provider so stop discounting real estate you to can get '
              'unlimited benefits and maximum sales prices right now go to seller finance '
              "consultants.com orfr notes.com and get your free dfr disclosure and we'll see "
              'at the race.',
      'timestamp': 186,
      'timestamp_label': '[00:03:06]',
      'timestamp_seconds': 186,
      'tip': 'Insurance and service provider so stop discounting real estate you to can get '
             'unlimited benefits and maximum sales prices right now go to seller finance '
             "consultants.com orfr notes.com and get your free dfr disclosure and we'll see at "
             'the race.',
      'title': 'Seller Financing for Maximum Benefits in The Dodd Frank Era (Seller Finance '
               'Consultants, Inc.)',
      'url': 'https://www.youtube.com/watch?v=0jNAfoc37ko&t=186s',
      'video_id': '0jNAfoc37ko'},
     {'author': 'Fusion Notes',
      'channel': 'Fusion Notes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:53](https://www.youtube.com/watch?v=PXDW2SqUfMA&t=173s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That I just outlined and the different places you can go to buy notes then you '
              'can check out my note launchpad online training course at notelaunchpad.com '
              "where you'll find all of those details plus a lot of other information on their "
              'investing thanks.',
      'timestamp': 173,
      'timestamp_label': '[00:02:53]',
      'timestamp_seconds': 173,
      'tip': 'That I just outlined and the different places you can go to buy notes then you '
             'can check out my note launchpad online training course at notelaunchpad.com '
             "where you'll find all of those details plus a lot of other information on their "
             'investing thanks.',
      'title': 'Dan Explains Where to Buy Mortgage Notes (Fusion Notes)',
      'url': 'https://www.youtube.com/watch?v=PXDW2SqUfMA&t=173s',
      'video_id': 'PXDW2SqUfMA'},
     {'author': 'Paperstac',
      'channel': 'Paperstac',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:53](https://www.youtube.com/watch?v=5bOm5hdSRXc&t=533s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Yeah the wraps just go crazy they do but the every time they're buying a wrap "
              "the underlying lean's getting paid off right so.",
      'timestamp': 533,
      'timestamp_label': '[00:08:53]',
      'timestamp_seconds': 533,
      'tip': "Yeah the wraps just go crazy they do but the every time they're buying a wrap "
             "the underlying lean's getting paid off right so.",
      'title': 'Turn a Rental with a Current Mortgage into a Mortgage Note (How to) '
               '(Paperstac)',
      'url': 'https://www.youtube.com/watch?v=5bOm5hdSRXc&t=533s',
      'video_id': '5bOm5hdSRXc'},
     {'author': 'Flipping Mastery TV',
      'channel': 'Flipping Mastery TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:54](https://www.youtube.com/watch?v=DAhcIhHIoI0&t=1914s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Families that wouldn't be able to I mean it's really cool yeah thanks man "
              'awesome great call everybody super proud of you guys keep up the hard work.',
      'timestamp': 1914,
      'timestamp_label': '[00:31:54]',
      'timestamp_seconds': 1914,
      'tip': "Families that wouldn't be able to I mean it's really cool yeah thanks man "
             'awesome great call everybody super proud of you guys keep up the hard work.',
      'title': 'Creating Massive Cash Flow With Real Estate Wraps (NOT Rentals) - Ft. Nick '
               'Disney (Flipping Mastery TV)',
      'url': 'https://www.youtube.com/watch?v=DAhcIhHIoI0&t=1914s',
      'video_id': 'DAhcIhHIoI0'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:46](https://www.youtube.com/watch?v=_M0q3Da-vxU&t=226s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That you you're like checking out the hospital yep I'll put that on the AMX no "
              'problem we almost named our baby AMX just so you guys know.',
      'timestamp': 226,
      'timestamp_label': '[00:03:46]',
      'timestamp_seconds': 226,
      'tip': "That you you're like checking out the hospital yep I'll put that on the AMX no "
             'problem we almost named our baby AMX just so you guys know.',
      'title': 'Creative Finance Explained for BEGINNER Investors (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=_M0q3Da-vxU&t=226s',
      'video_id': '_M0q3Da-vxU'}],
 5: [{'author': 'Clint Coons Esq. | Real Estate Asset Protection',
      'channel': 'Clint Coons Esq. | Real Estate Asset Protection',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:12](https://www.youtube.com/watch?v=nS_9Os_42MQ&t=492s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So many times we'll give you a the ability to cure. So is violating the due on "
              'sale clause worth the risk to put your property into a limited liability '
              'company or a land trust for asset protection? Because if it does happen that '
              'somebody finds out about it, you have options.',
      'timestamp': 492,
      'timestamp_label': '[00:08:12]',
      'timestamp_seconds': 492,
      'tip': "So many times we'll give you a the ability to cure. So is violating the due on "
             'sale clause worth the risk to put your property into a limited liability company '
             'or a land trust for asset protection? Because if it does happen that somebody '
             'finds out about it, you have options.',
      'title': 'Due On Sale Clause and How To AVOID It (Real Estate Investments!) (Clint Coons '
               'Esq. | Real Estate Asset Protection)',
      'url': 'https://www.youtube.com/watch?v=nS_9Os_42MQ&t=492s',
      'video_id': 'nS_9Os_42MQ'},
     {'author': 'William Tingle',
      'channel': 'William Tingle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:19](https://www.youtube.com/watch?v=D8NZHrMYpSE&t=739s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But just wanted to make these these things clear that there are other risk '
              'involved in a sub two deal uh besides just the do on sale clause. The do on '
              'sale clause in my opinion uh is probably a lesser worry than the bankruptcy.',
      'timestamp': 739,
      'timestamp_label': '[00:12:19]',
      'timestamp_seconds': 739,
      'tip': 'But just wanted to make these these things clear that there are other risk '
             'involved in a sub two deal uh besides just the do on sale clause. The do on sale '
             'clause in my opinion uh is probably a lesser worry than the bankruptcy.',
      'title': "The Real Sub2 Risks No One Talks About (It's NOT the Due on Sale Clause!) "
               '(William Tingle)',
      'url': 'https://www.youtube.com/watch?v=D8NZHrMYpSE&t=739s',
      'video_id': 'D8NZHrMYpSE'},
     {'author': 'PrepAgent',
      'channel': 'PrepAgent',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:33](https://www.youtube.com/watch?v=uHpaHL4qN84&t=153s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This has to be assumable and not have a do on sale clause. A do on sale clause '
              'means that when you convey title to somebody else, the bank has the right to '
              'demand payment immediately. And the most obvious problem is that Sam runs the '
              'risk of Bill not making the payment.',
      'timestamp': 153,
      'timestamp_label': '[00:02:33]',
      'timestamp_seconds': 153,
      'tip': 'This has to be assumable and not have a do on sale clause. A do on sale clause '
             'means that when you convey title to somebody else, the bank has the right to '
             'demand payment immediately. And the most obvious problem is that Sam runs the '
             'risk of Bill not making the payment.',
      'title': 'Wrap Around Mortgage (PrepAgent)',
      'url': 'https://www.youtube.com/watch?v=uHpaHL4qN84&t=153s',
      'video_id': 'uHpaHL4qN84'},
     {'author': 'UpCounsel',
      'channel': 'UpCounsel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=o5_cemzYC-w&t=70s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Some homeowners explore using living trusts or land trusts as a way to transfer '
              'property without triggering the do on sale clause. While these methods can be '
              'effective for estate planning, using them solely to avoid the clause carries '
              'risks.',
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': 'Some homeowners explore using living trusts or land trusts as a way to transfer '
             'property without triggering the do on sale clause. While these methods can be '
             'effective for estate planning, using them solely to avoid the clause carries '
             'risks.',
      'title': 'Due on Sale Clauses  What Property Owners Need to Know (UpCounsel)',
      'url': 'https://www.youtube.com/watch?v=o5_cemzYC-w&t=70s',
      'video_id': 'o5_cemzYC-w'},
     {'author': 'Shop Rates',
      'channel': 'Shop Rates',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=Z_X2-JRfBYs&t=111s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Pros: lower interest rates, potentially easier qualification, lower closing '
              'costs. Cons: limited availability. Still need lender approval. Pros: Extreme '
              'flexibility, especially for buyers with less than perfect credit. Cons: higher '
              'risk for both buyer do on sale and seller.',
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': 'Pros: lower interest rates, potentially easier qualification, lower closing '
             'costs. Cons: limited availability. Still need lender approval. Pros: Extreme '
             'flexibility, especially for buyers with less than perfect credit. Cons: higher '
             'risk for both buyer do on sale and seller.',
      'title': 'Ditch the Bank? 🏡 Assumable vs. Wraparound Mortgages Explained! | Shop Rates '
               '(Shop Rates)',
      'url': 'https://www.youtube.com/watch?v=Z_X2-JRfBYs&t=111s',
      'video_id': 'Z_X2-JRfBYs'},
     {'author': 'Bramlett Partners Real Estate',
      'channel': 'Bramlett Partners Real Estate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:27](https://www.youtube.com/watch?v=dge6WTAROFI&t=207s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "With the risk then it's something you should consider the first thing you need "
              "to understand is what's called a do on sale clause and.",
      'timestamp': 207,
      'timestamp_label': '[00:03:27]',
      'timestamp_seconds': 207,
      'tip': "With the risk then it's something you should consider the first thing you need "
             "to understand is what's called a do on sale clause and.",
      'title': 'Risks and Considerations of Wraparound and Subject-To Financing Offers '
               '(Bramlett Partners Real Estate)',
      'url': 'https://www.youtube.com/watch?v=dge6WTAROFI&t=207s',
      'video_id': 'dge6WTAROFI'},
     {'author': 'Vena Jones Cox',
      'channel': 'Vena Jones Cox',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:07:20](https://www.youtube.com/watch?v=jeHouEguhhE&t=4040s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They're gonna pay it all off in four or five months anyway so guess what the "
              "problem was this property isn't paid off I have a 64 000 mortgage on this "
              'property.',
      'timestamp': 4040,
      'timestamp_label': '[01:07:20]',
      'timestamp_seconds': 4040,
      'tip': "They're gonna pay it all off in four or five months anyway so guess what the "
             "problem was this property isn't paid off I have a 64 000 mortgage on this "
             'property.',
      'title': 'Wrap mortgage/All-Inclusive Deed of Trust class (Vena Jones Cox)',
      'url': 'https://www.youtube.com/watch?v=jeHouEguhhE&t=4040s',
      'video_id': 'jeHouEguhhE'},
     {'author': 'James Heller -- Hellerman Industries',
      'channel': 'James Heller -- Hellerman Industries',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:20](https://www.youtube.com/watch?v=nO_A1GtSlaA&t=200s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The problem that a lot of people run into when the mortgage is much lower than '
              'the asking price is okay what do you do with all the sellers Equity right.',
      'timestamp': 200,
      'timestamp_label': '[00:03:20]',
      'timestamp_seconds': 200,
      'tip': 'The problem that a lot of people run into when the mortgage is much lower than '
             'the asking price is okay what do you do with all the sellers Equity right.',
      'title': 'How to do a Subto and Seller Finance Hybrid Deal (James Heller -- Hellerman '
               'Industries)',
      'url': 'https://www.youtube.com/watch?v=nO_A1GtSlaA&t=200s',
      'video_id': 'nO_A1GtSlaA'},
     {'author': 'Investor Army Podcast',
      'channel': 'Investor Army Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:37](https://www.youtube.com/watch?v=WFGzQCgPP54&t=337s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're not the primary mortgagee and that's gonna be Wells Fargo and then like "
              'I said they owe you money right they owe your company your BIOS your.',
      'timestamp': 337,
      'timestamp_label': '[00:05:37]',
      'timestamp_seconds': 337,
      'tip': "You're not the primary mortgagee and that's gonna be Wells Fargo and then like I "
             'said they owe you money right they owe your company your BIOS your.',
      'title': 'Subject To Investing and How To Avoid the Due on Sale Clause (Investor Army '
               'Podcast)',
      'url': 'https://www.youtube.com/watch?v=WFGzQCgPP54&t=337s',
      'video_id': 'WFGzQCgPP54'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:55](https://www.youtube.com/watch?v=EO9EtMTTjm4&t=175s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You know, listing a house takes up calls at all hours of the night and all '
              "sorts of stuff, right? So, she decides, I'm not going to go through an agent. "
              'She goes and calls a TV ad of one of those people say, "We buy ugly houses.',
      'timestamp': 175,
      'timestamp_label': '[00:02:55]',
      'timestamp_seconds': 175,
      'tip': 'You know, listing a house takes up calls at all hours of the night and all sorts '
             "of stuff, right? So, she decides, I'm not going to go through an agent. She goes "
             'and calls a TV ad of one of those people say, "We buy ugly houses.',
      'title': 'Teaching SubTo & Creative Finance to Those In Need (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=EO9EtMTTjm4&t=175s',
      'video_id': 'EO9EtMTTjm4'},
     {'author': 'Personal Finance for Everyone',
      'channel': 'Personal Finance for Everyone',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:57](https://www.youtube.com/watch?v=HXkjpvAG51k&t=657s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Success in the lucrative world of mortgage note investing remember the key to '
              'successful investing is not just about finding the right opportunities but also '
              'about avoiding the common pitfalls that can lead to costly mistakes.',
      'timestamp': 657,
      'timestamp_label': '[00:10:57]',
      'timestamp_seconds': 657,
      'tip': 'Success in the lucrative world of mortgage note investing remember the key to '
             'successful investing is not just about finding the right opportunities but also '
             'about avoiding the common pitfalls that can lead to costly mistakes.',
      'title': 'Mortgage Note Investing A Profitable Path to Real (Personal Finance for '
               'Everyone)',
      'url': 'https://www.youtube.com/watch?v=HXkjpvAG51k&t=657s',
      'video_id': 'HXkjpvAG51k'},
     {'author': 'Mr No FluFF (My Real Estate DOJO)',
      'channel': 'Mr No FluFF (My Real Estate DOJO)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:10](https://www.youtube.com/watch?v=RPbZyS3NPFI&t=430s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "There for free all right guys don't take no for answer always remember you're "
              'braver than you believe stronger than you seen smarter than you and twice as '
              'beautiful as you ever imagined Ro me peace guys.',
      'timestamp': 430,
      'timestamp_label': '[00:07:10]',
      'timestamp_seconds': 430,
      'tip': "There for free all right guys don't take no for answer always remember you're "
             'braver than you believe stronger than you seen smarter than you and twice as '
             'beautiful as you ever imagined Ro me peace guys.',
      'title': 'Subject-To vs. Wraparound Mortgage: The 2 BIGGEST Differences EXPLAINED! (Mr '
               'No FluFF (My Real Estate DOJO))',
      'url': 'https://www.youtube.com/watch?v=RPbZyS3NPFI&t=430s',
      'video_id': 'RPbZyS3NPFI'},
     {'author': 'My Mortgage Trainer, Inc.',
      'channel': 'My Mortgage Trainer, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:32](https://www.youtube.com/watch?v=C1it2AZx0B4&t=272s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Financial education to research con consumer Behavior to monitor financial '
              'markets for new risks to Consumers and finally to enforce laws that Outlaw '
              'discrimination and other unfair treatment in Consumer Finance.',
      'timestamp': 272,
      'timestamp_label': '[00:04:32]',
      'timestamp_seconds': 272,
      'tip': 'Financial education to research con consumer Behavior to monitor financial '
             'markets for new risks to Consumers and finally to enforce laws that Outlaw '
             'discrimination and other unfair treatment in Consumer Finance.',
      'title': 'Introduction to Dodd-Frank (Module 3) | NMLS SAFE MLO Exam Study Series and '
               'Test Prep (My Mortgage Trainer, Inc.)',
      'url': 'https://www.youtube.com/watch?v=C1it2AZx0B4&t=272s',
      'video_id': 'C1it2AZx0B4'},
     {'author': 'Paperstac',
      'channel': 'Paperstac',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:56](https://www.youtube.com/watch?v=XRyBErGyKgQ&t=1316s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Podcast right after this one well I always wear this shirt yeah we might who '
              "knows you might get two today all right well that's it for today we'll talk to "
              'you soon thanks.',
      'timestamp': 1316,
      'timestamp_label': '[00:21:56]',
      'timestamp_seconds': 1316,
      'tip': 'Podcast right after this one well I always wear this shirt yeah we might who '
             "knows you might get two today all right well that's it for today we'll talk to "
             'you soon thanks.',
      'title': 'Mortgage Note Partials – The How & Why To Do It (Paperstac)',
      'url': 'https://www.youtube.com/watch?v=XRyBErGyKgQ&t=1316s',
      'video_id': 'XRyBErGyKgQ'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:42](https://www.youtube.com/watch?v=6FXApQ1y2KE&t=402s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Me terms there we go there's that word terms again she had no idea what the "
              "heck that meant and so what did I do she says to me she goes what's terms I go "
              'well let me tell you a story about an F-150 I then went to tell Susan this '
              'story.',
      'timestamp': 402,
      'timestamp_label': '[00:06:42]',
      'timestamp_seconds': 402,
      'tip': "Me terms there we go there's that word terms again she had no idea what the heck "
             "that meant and so what did I do she says to me she goes what's terms I go well "
             'let me tell you a story about an F-150 I then went to tell Susan this story.',
      'title': 'What is Seller Finance? Creative Real Estate Explained (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=6FXApQ1y2KE&t=402s',
      'video_id': '6FXApQ1y2KE'}],
 6: [{'author': 'Dom Inglese',
      'channel': 'Dom Inglese',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:59](https://www.youtube.com/watch?v=StKrDLiCONM&t=719s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Some of them work with buyers who may not qualify for traditional financing. '
              "And if you do enough of these types of deals, you'll be the first person that "
              'they think of to send their buyer to. So, in that scenario, agent gets paid a '
              'commission.',
      'timestamp': 719,
      'timestamp_label': '[00:11:59]',
      'timestamp_seconds': 719,
      'tip': 'Some of them work with buyers who may not qualify for traditional financing. And '
             "if you do enough of these types of deals, you'll be the first person that they "
             'think of to send their buyer to. So, in that scenario, agent gets paid a '
             'commission.',
      'title': '$1,000/Month Passive Income with a Wrap Mortgage | How A Real Estate Investor '
               'Becomes The Bank (Dom Inglese)',
      'url': 'https://www.youtube.com/watch?v=StKrDLiCONM&t=719s',
      'video_id': 'StKrDLiCONM'},
     {'author': 'Cal Ewing',
      'channel': 'Cal Ewing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=LCY-eZOK6gw&t=50s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s a perfect case study on how you can cash out an investor, or take some cash "
              "out of a note by selling off partial payments, and we're going to use a real "
              'deal to break all this down.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': "'s a perfect case study on how you can cash out an investor, or take some cash "
             "out of a note by selling off partial payments, and we're going to use a real "
             'deal to break all this down.',
      'title': 'How to Cash Out of a Performing Note Without Selling It – Real Case Study on '
               'Selling Partials! (Cal Ewing)',
      'url': 'https://www.youtube.com/watch?v=LCY-eZOK6gw&t=50s',
      'video_id': 'LCY-eZOK6gw'},
     {'author': 'kris haskins',
      'channel': 'kris haskins',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:56](https://www.youtube.com/watch?v=X4XzY55e_n4&t=1136s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll know what your intentions are. Don't lead them on and then try to do a "
              'switcheroo on this stuff because there there actually is no equity to do this '
              'deal. So you he who understands this creative financing is going to destroy it '
              "over the next few years, y'all.",
      'timestamp': 1136,
      'timestamp_label': '[00:18:56]',
      'timestamp_seconds': 1136,
      'tip': "'ll know what your intentions are. Don't lead them on and then try to do a "
             'switcheroo on this stuff because there there actually is no equity to do this '
             'deal. So you he who understands this creative financing is going to destroy it '
             "over the next few years, y'all.",
      'title': 'How to explain a subject to real estate deal to a seller (kris haskins)',
      'url': 'https://www.youtube.com/watch?v=X4XzY55e_n4&t=1136s',
      'video_id': 'X4XzY55e_n4'},
     {'author': 'Sub2Investor',
      'channel': 'Sub2Investor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=WxPHAXmQ-j4&t=22s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Lender the lender on the sub 2 loan right after you close the deal send it all '
              'directly to the doorstep of the lender and you can have the do on sale Clause '
              "called on your sub 2 deal that's exactly what we did stay tuned to find out "
              'what happened.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'Lender the lender on the sub 2 loan right after you close the deal send it all '
             'directly to the doorstep of the lender and you can have the do on sale Clause '
             "called on your sub 2 deal that's exactly what we did stay tuned to find out what "
             'happened.',
      'title': '#16 - My "Due On Sales" Nightmare Story on "Subject to" Loan (Sub2Investor)',
      'url': 'https://www.youtube.com/watch?v=WxPHAXmQ-j4&t=22s',
      'video_id': 'WxPHAXmQ-j4'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[02:12:39](https://www.youtube.com/watch?v=w1wq3uZtNx8&t=7959s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They said they're interested in having a conversation. That would now be a "
              "prospect because I have prospected. Lead means they're willing to negotiate "
              "either on cash or on creative terms. They're open to conversations around an "
              'offer.',
      'timestamp': 7959,
      'timestamp_label': '[02:12:39]',
      'timestamp_seconds': 7959,
      'tip': "They said they're interested in having a conversation. That would now be a "
             "prospect because I have prospected. Lead means they're willing to negotiate "
             "either on cash or on creative terms. They're open to conversations around an "
             'offer.',
      'title': 'How To Use Seller Finance In Real Estate Deals (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=w1wq3uZtNx8&t=7959s',
      'video_id': 'w1wq3uZtNx8'},
     {'author': 'Flipping Mastery TV',
      'channel': 'Flipping Mastery TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:28](https://www.youtube.com/watch?v=-E2cCPmM_Q0&t=448s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Do with it they will pay a premium for that deal because you've created an "
              "opportunity where they don't have to come up with a lot of cash to get into.",
      'timestamp': 448,
      'timestamp_label': '[00:07:28]',
      'timestamp_seconds': 448,
      'tip': "Do with it they will pay a premium for that deal because you've created an "
             "opportunity where they don't have to come up with a lot of cash to get into.",
      'title': 'Introduction To Creative Finance - Masterclass Video 1 w/ Pace Morby (Flipping '
               'Mastery TV)',
      'url': 'https://www.youtube.com/watch?v=-E2cCPmM_Q0&t=448s',
      'video_id': '-E2cCPmM_Q0'},
     {'author': 'Fusion Notes',
      'channel': 'Fusion Notes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:33:04](https://www.youtube.com/watch?v=JAyoDBTIEIE&t=1984s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Like they just won't even make an offer from it. Um, the other thing I've kind "
              'of observed that I find a little bit interesting is that the dynamic between '
              'call retail and institutional buyers and the note world is kind of backwards.',
      'timestamp': 1984,
      'timestamp_label': '[00:33:04]',
      'timestamp_seconds': 1984,
      'tip': "Like they just won't even make an offer from it. Um, the other thing I've kind "
             'of observed that I find a little bit interesting is that the dynamic between '
             'call retail and institutional buyers and the note world is kind of backwards.',
      'title': 'Underwriting Secrets for Creative Finance, Wraps and Subto Deals (Fusion '
               'Notes)',
      'url': 'https://www.youtube.com/watch?v=JAyoDBTIEIE&t=1984s',
      'video_id': 'JAyoDBTIEIE'},
     {'author': 'Paperstac',
      'channel': 'Paperstac',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:15](https://www.youtube.com/watch?v=MkofIE1Xq0o&t=255s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "All that information is provided you. There's a lot of rich data there that "
              'will allow you to put together a good bid on an asset up front and immediate '
              'and have a have a quality start to your transaction. Rick, Rick, what is an '
              'indicative bid just so people know?',
      'timestamp': 255,
      'timestamp_label': '[00:04:15]',
      'timestamp_seconds': 255,
      'tip': "All that information is provided you. There's a lot of rich data there that will "
             'allow you to put together a good bid on an asset up front and immediate and have '
             'a have a quality start to your transaction. Rick, Rick, what is an indicative '
             'bid just so people know?',
      'title': '5 Mistakes That Will Wreck Your First Mortgage Note Deal (Paperstac)',
      'url': 'https://www.youtube.com/watch?v=MkofIE1Xq0o&t=255s',
      'video_id': 'MkofIE1Xq0o'},
     {'author': 'Barry Zalma',
      'channel': 'Barry Zalma',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=fnta0i2LMYQ&t=15s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'About the importance of the union or standard mortgage clause to every first '
              'party property claim where mortgage.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'About the importance of the union or standard mortgage clause to every first '
             'party property claim where mortgage.',
      'title': 'The Rights of Mortgagees (Barry Zalma)',
      'url': 'https://www.youtube.com/watch?v=fnta0i2LMYQ&t=15s',
      'video_id': 'fnta0i2LMYQ'},
     {'author': 'PrepAgent',
      'channel': 'PrepAgent',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=-8VDqc249XY&t=38s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A junior refers to the priority of liens in the case of foreclosure the senior '
              'mortgage will be paid down first then any junior mortgages are paid based on.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': 'A junior refers to the priority of liens in the case of foreclosure the senior '
             'mortgage will be paid down first then any junior mortgages are paid based on.',
      'title': 'Wraparound Mortgages | Real Estate Exam Prep Key Concepts (PrepAgent)',
      'url': 'https://www.youtube.com/watch?v=-8VDqc249XY&t=38s',
      'video_id': '-8VDqc249XY'},
     {'author': "Scott Horne's Owner Finance Network",
      'channel': "Scott Horne's Owner Finance Network",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:10](https://www.youtube.com/watch?v=adTW0EyLeRk&t=670s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Is an existing escrow account in existence usually because there's an existing "
              'mortgage company a first lien.',
      'timestamp': 670,
      'timestamp_label': '[00:11:10]',
      'timestamp_seconds': 670,
      'tip': "Is an existing escrow account in existence usually because there's an existing "
             'mortgage company a first lien.',
      'title': "What is the Timeline and Process for Loan Servicing (Scott Horne's Owner "
               'Finance Network)',
      'url': 'https://www.youtube.com/watch?v=adTW0EyLeRk&t=670s',
      'video_id': 'adTW0EyLeRk'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:50](https://www.youtube.com/watch?v=Teh6C2LGk8g&t=530s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The deal based on how little I can come out of pocket and how much I can make '
              "on the cash flow that's it and in the situation all I want to do is help the "
              "seller that's it yeah.",
      'timestamp': 530,
      'timestamp_label': '[00:08:50]',
      'timestamp_seconds': 530,
      'tip': 'The deal based on how little I can come out of pocket and how much I can make on '
             "the cash flow that's it and in the situation all I want to do is help the seller "
             "that's it yeah.",
      'title': 'Creative Financing Benefits | HOW SELLERS WIN IN REAL ESTATE! (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=Teh6C2LGk8g&t=530s',
      'video_id': 'Teh6C2LGk8g'},
     {'author': 'James Bealer',
      'channel': 'James Bealer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:25](https://www.youtube.com/watch?v=Y7CyY8gLd3U&t=385s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Investors regularly because they're able to keep up with any changes in the "
              'industry and adjustments you may have to make so you know try that first and if '
              'you have any issues or you can contact somebody.',
      'timestamp': 385,
      'timestamp_label': '[00:06:25]',
      'timestamp_seconds': 385,
      'tip': "Investors regularly because they're able to keep up with any changes in the "
             'industry and adjustments you may have to make so you know try that first and if '
             'you have any issues or you can contact somebody.',
      'title': 'Buying Houses "Subject To" - What to do about the Home Owners Insurance? '
               '(James Bealer)',
      'url': 'https://www.youtube.com/watch?v=Y7CyY8gLd3U&t=385s',
      'video_id': 'Y7CyY8gLd3U'},
     {'author': 'Paperstac',
      'channel': 'Paperstac',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:50](https://www.youtube.com/watch?v=Il6eOQ_69VM&t=350s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You know back then prices were much lower but it was 31 500. the seller let me '
              'put fifteen hundred dollars down and they did an owner carry note at nine.',
      'timestamp': 350,
      'timestamp_label': '[00:05:50]',
      'timestamp_seconds': 350,
      'tip': 'You know back then prices were much lower but it was 31 500. the seller let me '
             'put fifteen hundred dollars down and they did an owner carry note at nine.',
      'title': 'My First Mortgage Note Purchase - Tracy Rewey (Paperstac)',
      'url': 'https://www.youtube.com/watch?v=Il6eOQ_69VM&t=350s',
      'video_id': 'Il6eOQ_69VM'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:43](https://www.youtube.com/watch?v=Ou7n95pTZFE&t=763s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Training on the YouTube channel so go check that out so let's go back to the "
              "Channel with raw bill I'll go through and answer the other questions.",
      'timestamp': 763,
      'timestamp_label': '[00:12:43]',
      'timestamp_seconds': 763,
      'tip': "Training on the YouTube channel so go check that out so let's go back to the "
             "Channel with raw bill I'll go through and answer the other questions.",
      'title': 'Top Questions Answered About Creative Finance SubTo and Seller Finance (Pace '
               'Morby)',
      'url': 'https://www.youtube.com/watch?v=Ou7n95pTZFE&t=763s',
      'video_id': 'Ou7n95pTZFE'}],
 7: [{'author': "Scott Horne's Owner Finance Network",
      'channel': "Scott Horne's Owner Finance Network",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:54](https://www.youtube.com/watch?v=fNubolIgxnE&t=474s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They don't understand the compliance and they really don't care because all "
              "they want to do is close your transaction and make a quick buck. It's when you "
              'can find that that quality closing agent law firm that understands this '
              'business.',
      'timestamp': 474,
      'timestamp_label': '[00:07:54]',
      'timestamp_seconds': 474,
      'tip': "They don't understand the compliance and they really don't care because all they "
             "want to do is close your transaction and make a quick buck. It's when you can "
             'find that that quality closing agent law firm that understands this business.',
      'title': "Title Company vs Law Firm: Best Way to Close Subject‑To & Wraps (Scott Horne's "
               'Owner Finance Network)',
      'url': 'https://www.youtube.com/watch?v=fNubolIgxnE&t=474s',
      'video_id': 'fNubolIgxnE'},
     {'author': 'Paperstac',
      'channel': 'Paperstac',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:53](https://www.youtube.com/watch?v=WaCgDRVF1rY&t=53s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Our price negotiator, makes it easy for buyers and sellers to communicate, '
              'sending counter offers back and forth. Once both parties have agreed on a '
              'price, our automated to-do list, walks you through each step of the closing '
              'process.',
      'timestamp': 53,
      'timestamp_label': '[00:00:53]',
      'timestamp_seconds': 53,
      'tip': 'Our price negotiator, makes it easy for buyers and sellers to communicate, '
             'sending counter offers back and forth. Once both parties have agreed on a price, '
             'our automated to-do list, walks you through each step of the closing process.',
      'title': 'How to Buy and Sell Mortgage Notes Online (Without the Headache) (Paperstac)',
      'url': 'https://www.youtube.com/watch?v=WaCgDRVF1rY&t=53s',
      'video_id': 'WaCgDRVF1rY'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:41](https://www.youtube.com/watch?v=11lUs1njQMw&t=101s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I take over through an agreement for sale, and at some point in five years, I '
              "refinance it with my own loan once there's enough equity in the deal and I can "
              'get her all the way out." That\'s the easiest way to Easiest way. Here\'s the '
              'first step of Morby Method, okay?',
      'timestamp': 101,
      'timestamp_label': '[00:01:41]',
      'timestamp_seconds': 101,
      'tip': 'I take over through an agreement for sale, and at some point in five years, I '
             "refinance it with my own loan once there's enough equity in the deal and I can "
             'get her all the way out." That\'s the easiest way to Easiest way. Here\'s the '
             'first step of Morby Method, okay?',
      'title': 'Underwriting A Creative Finance Deal: The Morby Method (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=11lUs1njQMw&t=101s',
      'video_id': '11lUs1njQMw'},
     {'author': 'Greg Schwartz | Investing in Bryan-College Station',
      'channel': 'Greg Schwartz | Investing in Bryan-College Station',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:34](https://www.youtube.com/watch?v=_xN91ltYUa0&t=34s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "IOU on the back of a Denny's napkin. So today we're going to cover the exact "
              'steps from negotiating to closing all the way to how a seller eventually gets '
              "paid off. If you don't know who I am, my name is Greg Schwartz.",
      'timestamp': 34,
      'timestamp_label': '[00:00:34]',
      'timestamp_seconds': 34,
      'tip': "IOU on the back of a Denny's napkin. So today we're going to cover the exact "
             'steps from negotiating to closing all the way to how a seller eventually gets '
             "paid off. If you don't know who I am, my name is Greg Schwartz.",
      'title': 'How Owner Financing Works in Texas: Step-by-Step (Buyer & Seller Guide) (Greg '
               'Schwartz | Investing in Bryan-College Station)',
      'url': 'https://www.youtube.com/watch?v=_xN91ltYUa0&t=34s',
      'video_id': '_xN91ltYUa0'},
     {'author': 'Brian Gibbons',
      'channel': 'Brian Gibbons',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:52](https://www.youtube.com/watch?v=r0FyiCHdxVU&t=112s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, the ability to repay rules. It should be noted that the DoddFrank Act '
              'creates special rights and defenses for borrowers whose lenders have failed to '
              'verify the ability to repay as per these eight particular aspects.',
      'timestamp': 112,
      'timestamp_label': '[00:01:52]',
      'timestamp_seconds': 112,
      'tip': 'Now, the ability to repay rules. It should be noted that the DoddFrank Act '
             'creates special rights and defenses for borrowers whose lenders have failed to '
             'verify the ability to repay as per these eight particular aspects.',
      'title': 'Seller Financing - Ability To Repay Rule as per Dodd Frank (Brian Gibbons)',
      'url': 'https://www.youtube.com/watch?v=r0FyiCHdxVU&t=112s',
      'video_id': 'r0FyiCHdxVU'},
     {'author': 'Texas Capital Finance',
      'channel': 'Texas Capital Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:44](https://www.youtube.com/watch?v=w4PRGbUrreA&t=404s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Way to explain price is the closer your mortgage resembles a traditional bank's "
              'mortgage the higher the price and vice versa step six closing process '
              'Gathering.',
      'timestamp': 404,
      'timestamp_label': '[00:06:44]',
      'timestamp_seconds': 404,
      'tip': "Way to explain price is the closer your mortgage resembles a traditional bank's "
             'mortgage the higher the price and vice versa step six closing process Gathering.',
      'title': 'How to Sell Your Mortgage Note for the Best Price | Step-by-Step Guide (Texas '
               'Capital Finance)',
      'url': 'https://www.youtube.com/watch?v=w4PRGbUrreA&t=404s',
      'video_id': 'w4PRGbUrreA'},
     {'author': 'IT Gbox',
      'channel': 'IT Gbox',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:29](https://www.youtube.com/watch?v=vJwZmvzudlk&t=209s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Alternative solution to satisfying the ATR rules so please take that into '
              'consideration in our current and future guidelines when evaluating exceptions '
              'when evaluating conditions and boundaries of our guidelines and our exception '
              'process.',
      'timestamp': 209,
      'timestamp_label': '[00:03:29]',
      'timestamp_seconds': 209,
      'tip': 'Alternative solution to satisfying the ATR rules so please take that into '
             'consideration in our current and future guidelines when evaluating exceptions '
             'when evaluating conditions and boundaries of our guidelines and our exception '
             'process.',
      'title': 'ATR - Ability To Repay (IT Gbox)',
      'url': 'https://www.youtube.com/watch?v=vJwZmvzudlk&t=209s',
      'video_id': 'vJwZmvzudlk'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=X94W660WDh8&t=15s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's what we're going to be doing for you today timeline and process of a "
              "subject two deal here's what you should expect step one all the way through "
              'step.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "That's what we're going to be doing for you today timeline and process of a "
             "subject two deal here's what you should expect step one all the way through "
             'step.',
      'title': 'Full Breakdown of Buying a House Subject To! (NO MONEY DOWN) (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=X94W660WDh8&t=15s',
      'video_id': 'X94W660WDh8'},
     {'author': 'Loan Note Exchange',
      'channel': 'Loan Note Exchange',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:48](https://www.youtube.com/watch?v=epnA26NInuc&t=48s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Your buyer couldn't get a bank loan  or didn't want one, so you became the "
              'bank. Instead of getting all your money at.',
      'timestamp': 48,
      'timestamp_label': '[00:00:48]',
      'timestamp_seconds': 48,
      'tip': "Your buyer couldn't get a bank loan  or didn't want one, so you became the bank. "
             'Instead of getting all your money at.',
      'title': 'What Is a Seller-Financed Note? The 5 Steps Explained (Loan Note Exchange)',
      'url': 'https://www.youtube.com/watch?v=epnA26NInuc&t=48s',
      'video_id': 'epnA26NInuc'},
     {'author': 'In Rem Podcast',
      'channel': 'In Rem Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:18](https://www.youtube.com/watch?v=d9fjKwIC-VE&t=498s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Property do a third party and pay off the existing Loan in the process or three '
              'you refinance and pay off the existing Loan in the process.',
      'timestamp': 498,
      'timestamp_label': '[00:08:18]',
      'timestamp_seconds': 498,
      'tip': 'Property do a third party and pay off the existing Loan in the process or three '
             'you refinance and pay off the existing Loan in the process.',
      'title': 'What if your lender invokes the due on sale clause following a Subject To '
               'Transaction? (In Rem Podcast)',
      'url': 'https://www.youtube.com/watch?v=d9fjKwIC-VE&t=498s',
      'video_id': 'd9fjKwIC-VE'},
     {'author': 'Cherif Medawar',
      'channel': 'Cherif Medawar',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:37](https://www.youtube.com/watch?v=bhfdMe7Dpwk&t=217s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Advertise looking for a discounted note with a good yield and um good cash flow '
              'so now what are the biggest challenges for a new investor investing in notes.',
      'timestamp': 217,
      'timestamp_label': '[00:03:37]',
      'timestamp_seconds': 217,
      'tip': 'Advertise looking for a discounted note with a good yield and um good cash flow '
             'so now what are the biggest challenges for a new investor investing in notes.',
      'title': 'How To Buy Mortgage Notes With No Money? | @CherifMedawar (Cherif Medawar)',
      'url': 'https://www.youtube.com/watch?v=bhfdMe7Dpwk&t=217s',
      'video_id': 'bhfdMe7Dpwk'},
     {'author': 'My Mortgage Trainer, Inc.',
      'channel': 'My Mortgage Trainer, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:02](https://www.youtube.com/watch?v=nPRf3YuUI2o&t=122s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Originator creditor or an affiliate of the Creditor or originator except that '
              'the board May by rule waiver provide exemptions to this Clause if the board '
              'determines that such waiver exemption is in the interest of the consumers and '
              "in the Public's best interest.",
      'timestamp': 122,
      'timestamp_label': '[00:02:02]',
      'timestamp_seconds': 122,
      'tip': 'Originator creditor or an affiliate of the Creditor or originator except that '
             'the board May by rule waiver provide exemptions to this Clause if the board '
             'determines that such waiver exemption is in the interest of the consumers and in '
             "the Public's best interest.",
      'title': 'Dodd Frank MLO Compensation Rule (Module 3) | NMLS SAFE MLO Exam Study Series '
               'and Test Prep (My Mortgage Trainer, Inc.)',
      'url': 'https://www.youtube.com/watch?v=nPRf3YuUI2o&t=122s',
      'video_id': 'nPRf3YuUI2o'},
     {'author': 'William Tingle',
      'channel': 'William Tingle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=ccfeK6C6SeI&t=72s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Just want out they don't care I I can't guarantee you that you'll never have a "
              'loan Call Due what I can tell you is in in 24 plus years uh making the payments '
              "on time ensuring the the loan the the property properly I've never had it "
              "happen I don't expect it to happen.",
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': "Just want out they don't care I I can't guarantee you that you'll never have a "
             'loan Call Due what I can tell you is in in 24 plus years uh making the payments '
             "on time ensuring the the loan the the property properly I've never had it happen "
             "I don't expect it to happen.",
      'title': "Why the Due on Sale Clause Doesn't Keep Me Up at Night! (William Tingle)",
      'url': 'https://www.youtube.com/watch?v=ccfeK6C6SeI&t=72s',
      'video_id': 'ccfeK6C6SeI'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:06](https://www.youtube.com/watch?v=bKMcgnoYXfQ&t=186s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Process to sell your house before you have the same closing attorney the same '
              "people handling the transaction the only difference is I'm not going to get a.",
      'timestamp': 186,
      'timestamp_label': '[00:03:06]',
      'timestamp_seconds': 186,
      'tip': 'Process to sell your house before you have the same closing attorney the same '
             "people handling the transaction the only difference is I'm not going to get a.",
      'title': 'What to Say to Sellers on the Phone | Pitching Creative Finance (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=bKMcgnoYXfQ&t=186s',
      'video_id': 'bKMcgnoYXfQ'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:45](https://www.youtube.com/watch?v=ajwU62m3ADk&t=165s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So does this mortgage get wiped out and his name gets removed from the mortgage '
              "no this mortgage stays in the gentleman's name his name is actually xavier.",
      'timestamp': 165,
      'timestamp_label': '[00:02:45]',
      'timestamp_seconds': 165,
      'tip': 'So does this mortgage get wiped out and his name gets removed from the mortgage '
             "no this mortgage stays in the gentleman's name his name is actually xavier.",
      'title': '"Subject To" vs. Seller Finance | Pace Morby Creative Finance - Real Estate '
               '(Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=ajwU62m3ADk&t=165s',
      'video_id': 'ajwU62m3ADk'}],
 8: [{'author': 'Patrick Franz',
      'channel': 'Patrick Franz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:32:47](https://www.youtube.com/watch?v=y6ljJ3T0eNg&t=1967s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s if it's a good note, like you said, there's 10,000 buyers that are on there "
              'that have safe searches set up and as soon as that note hits the the platform, '
              'they all get emails saying, "Hey, this meets your buying criteria.".',
      'timestamp': 1967,
      'timestamp_label': '[00:32:47]',
      'timestamp_seconds': 1967,
      'tip': "'s if it's a good note, like you said, there's 10,000 buyers that are on there "
             'that have safe searches set up and as soon as that note hits the the platform, '
             'they all get emails saying, "Hey, this meets your buying criteria.".',
      'title': 'PaperStac Marketplace & Mortgage Note Investing Guide (Patrick Franz)',
      'url': 'https://www.youtube.com/watch?v=y6ljJ3T0eNg&t=1967s',
      'video_id': 'y6ljJ3T0eNg'},
     {'author': 'Larry Hoffman',
      'channel': 'Larry Hoffman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=R_jwbBWh1LA&t=83s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The core concept here is note investing. And all that means is purchasing '
              "secured debt to act as the bank. So in traditional real estate, you're buying "
              'bricks, mortar, roofs, plumbing, the whole shebang.',
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': 'The core concept here is note investing. And all that means is purchasing '
             "secured debt to act as the bank. So in traditional real estate, you're buying "
             'bricks, mortar, roofs, plumbing, the whole shebang.',
      'title': 'Note Investing Explained: How to Become the Bank in 2026 (Larry Hoffman)',
      'url': 'https://www.youtube.com/watch?v=R_jwbBWh1LA&t=83s',
      'video_id': 'R_jwbBWh1LA'},
     {'author': 'FIXnotes | Non-Performing Note Investing',
      'channel': 'FIXnotes | Non-Performing Note Investing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:03](https://www.youtube.com/watch?v=lxjMbDIOEGw&t=423s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We put those all in the Podio blueprints portal and we got a link here to two '
              "case studies in that video. One's a loan mod, the other is a payoff that is all "
              'linked here.',
      'timestamp': 423,
      'timestamp_label': '[00:07:03]',
      'timestamp_seconds': 423,
      'tip': 'We put those all in the Podio blueprints portal and we got a link here to two '
             "case studies in that video. One's a loan mod, the other is a payoff that is all "
             'linked here.',
      'title': "The Beginner's Guide to Resolutions (Non-Performing Mortgage Notes) (FIXnotes "
               '| Non-Performing Note Investing)',
      'url': 'https://www.youtube.com/watch?v=lxjMbDIOEGw&t=423s',
      'video_id': 'lxjMbDIOEGw'},
     {'author': "Scott Horne's Owner Finance Network",
      'channel': "Scott Horne's Owner Finance Network",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=1WQyfpf7efQ&t=25s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, what the heck is the SAFE Act and how does it affect us in the seller '
              "finance world? And the SAFE Act really doesn't affect us if we're buying a "
              'property as an investor.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': 'So, what the heck is the SAFE Act and how does it affect us in the seller '
             "finance world? And the SAFE Act really doesn't affect us if we're buying a "
             'property as an investor.',
      'title': 'SAFE Act & Dodd‑Frank for Seller Financing: RMLO, RESPA & ATR Explained (Scott '
               "Horne's Owner Finance Network)",
      'url': 'https://www.youtube.com/watch?v=1WQyfpf7efQ&t=25s',
      'video_id': '1WQyfpf7efQ'},
     {'author': 'Randy Rodenhouse',
      'channel': 'Randy Rodenhouse',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:25](https://www.youtube.com/watch?v=BjTl8XnBotM&t=265s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In the dodd-frank rules you cannot balloon and you have to show the the '
              'homeowners ability to pay however in this case you do not have to follow.',
      'timestamp': 265,
      'timestamp_label': '[00:04:25]',
      'timestamp_seconds': 265,
      'tip': 'In the dodd-frank rules you cannot balloon and you have to show the the '
             'homeowners ability to pay however in this case you do not have to follow.',
      'title': 'Dodd Frank Rules And Seller Financing (Randy Rodenhouse)',
      'url': 'https://www.youtube.com/watch?v=BjTl8XnBotM&t=265s',
      'video_id': 'BjTl8XnBotM'},
     {'author': 'The Flip Flop Flipper - Robert Crager',
      'channel': 'The Flip Flop Flipper - Robert Crager',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=q1drqFk-FH4&t=15s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Buying a house assuming an existing mortgage so guys you've been hearing all of "
              'this stuff this year especially in 2023 as the times get tough Pace morbies.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Buying a house assuming an existing mortgage so guys you've been hearing all of "
             'this stuff this year especially in 2023 as the times get tough Pace morbies.',
      'title': 'Subject To Is BETTER Than Assuming A Mortgage | Explained (The Flip Flop '
               'Flipper - Robert Crager)',
      'url': 'https://www.youtube.com/watch?v=q1drqFk-FH4&t=15s',
      'video_id': 'q1drqFk-FH4'},
     {'author': 'Flipping Mastery TV',
      'channel': 'Flipping Mastery TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=6Bdxz-HKeFI&t=15s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Ton of videos all creative financing and on this video specifically we're going "
              'to talk about a unique strategy which is a combination of subject two and '
              "there's.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Ton of videos all creative financing and on this video specifically we're going "
             'to talk about a unique strategy which is a combination of subject two and '
             "there's.",
      'title': 'Subto + Seller Finance (Hybrid) - Masterclass Video 6 w/ Pace Morby (Flipping '
               'Mastery TV)',
      'url': 'https://www.youtube.com/watch?v=6Bdxz-HKeFI&t=15s',
      'video_id': '6Bdxz-HKeFI'},
     {'author': 'Paperstac',
      'channel': 'Paperstac',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:01](https://www.youtube.com/watch?v=EdBetMgLDeQ&t=1141s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I got reached I was reached out to by an agent that I used to work with the '
              'Bagel. And he is like, "They\'re getting a lot He\'s like, I\'m seeing a huge '
              "uptick in foreclosures and they're buying and selling a lot of MPL now.",
      'timestamp': 1141,
      'timestamp_label': '[00:19:01]',
      'timestamp_seconds': 1141,
      'tip': 'I got reached I was reached out to by an agent that I used to work with the '
             'Bagel. And he is like, "They\'re getting a lot He\'s like, I\'m seeing a huge '
             "uptick in foreclosures and they're buying and selling a lot of MPL now.",
      'title': 'Should You Invest in a Mortgage Note Fund or Buy Notes Yourself? (Paperstac)',
      'url': 'https://www.youtube.com/watch?v=EdBetMgLDeQ&t=1141s',
      'video_id': 'EdBetMgLDeQ'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:28](https://www.youtube.com/watch?v=H8hA7c9SehA&t=568s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We know how to manage the tenants. We know how to collect the money, balance '
              'the checkbooks. We know how to actually manage cash flow and distribute money '
              'to our partners, right? We know how to do all of those things. Did I learn that '
              'through a multif family course?',
      'timestamp': 568,
      'timestamp_label': '[00:09:28]',
      'timestamp_seconds': 568,
      'tip': 'We know how to manage the tenants. We know how to collect the money, balance the '
             'checkbooks. We know how to actually manage cash flow and distribute money to our '
             'partners, right? We know how to do all of those things. Did I learn that through '
             'a multif family course?',
      'title': 'How to do Creative Finance on Multifamily (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=H8hA7c9SehA&t=568s',
      'video_id': 'H8hA7c9SehA'},
     {'author': 'Colin Whitenack | Real Estate & Investing',
      'channel': 'Colin Whitenack | Real Estate & Investing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=gxiK62dzE34&t=71s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, if you help them come up with a solution, all of a sudden you have a '
              'performing note and you can just keep collecting on that or you can turn around '
              "and sell it to somebody who's mostly investing in performing notes.",
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': 'So, if you help them come up with a solution, all of a sudden you have a '
             'performing note and you can just keep collecting on that or you can turn around '
             "and sell it to somebody who's mostly investing in performing notes.",
      'title': 'How does investing in a non-performing mortgage note work? - Colin Whitenack '
               '(Colin Whitenack | Real Estate & Investing)',
      'url': 'https://www.youtube.com/watch?v=gxiK62dzE34&t=71s',
      'video_id': 'gxiK62dzE34'},
     {'author': 'Florida Real Estate Scene',
      'channel': 'Florida Real Estate Scene',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:04](https://www.youtube.com/watch?v=9fmPGWpE4qo&t=244s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Straight out we do not recommend subject to or creative financing so if you got '
              "questions let me know got comments put them in the comments I'd love to hear "
              'what you have to say thank you for watching bye.',
      'timestamp': 244,
      'timestamp_label': '[00:04:04]',
      'timestamp_seconds': 244,
      'tip': 'Straight out we do not recommend subject to or creative financing so if you got '
             "questions let me know got comments put them in the comments I'd love to hear "
             'what you have to say thank you for watching bye.',
      'title': 'The latest real estate scam: "Subject To" aka "Creative Financing" (Florida '
               'Real Estate Scene)',
      'url': 'https://www.youtube.com/watch?v=9fmPGWpE4qo&t=244s',
      'video_id': '9fmPGWpE4qo'},
     {'author': 'Paperstac',
      'channel': 'Paperstac',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=chL0454K1Zs&t=71s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Data I'm going to make them private that way in a transaction I can toggle "
              'whether or not I feel like sharing them with potential buyers if you have '
              "something that shows the value of the property you can add it here I'm going to "
              'go ahead and add a recent bpo.',
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': "Data I'm going to make them private that way in a transaction I can toggle "
             'whether or not I feel like sharing them with potential buyers if you have '
             "something that shows the value of the property you can add it here I'm going to "
             'go ahead and add a recent bpo.',
      'title': 'How to List a Mortgage Note That Sells in Under 30 Days (Paperstac)',
      'url': 'https://www.youtube.com/watch?v=chL0454K1Zs&t=71s',
      'video_id': 'chL0454K1Zs'},
     {'author': '7e Investments',
      'channel': '7e Investments',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:06](https://www.youtube.com/watch?v=SZhJFIusBp4&t=306s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Forms my calculator and we have group sessions of education with different '
              'attorneys different vendors and also work in teams to co-elevate everyone to '
              'understand and educate themselves better so thanks for watching this video and '
              'as always go out and do some good deeds.',
      'timestamp': 306,
      'timestamp_label': '[00:05:06]',
      'timestamp_seconds': 306,
      'tip': 'Forms my calculator and we have group sessions of education with different '
             'attorneys different vendors and also work in teams to co-elevate everyone to '
             'understand and educate themselves better so thanks for watching this video and '
             'as always go out and do some good deeds.',
      'title': 'Selecting a Loan Servicer For Your Note Investing Business (7e Investments)',
      'url': 'https://www.youtube.com/watch?v=SZhJFIusBp4&t=306s',
      'video_id': 'SZhJFIusBp4'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=vJ6uGVFs4M4&t=77s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Yeah I agree with I agree with your wife why do you have to get the renter out '
              "there what if I buy if we're buying it from you guys on seller finance I'll "
              'just take over the renter.',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': 'Yeah I agree with I agree with your wife why do you have to get the renter out '
             "there what if I buy if we're buying it from you guys on seller finance I'll just "
             'take over the renter.',
      'title': 'How To Talk Seller Finance On A Call - Live Call! (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=vJ6uGVFs4M4&t=77s',
      'video_id': 'vJ6uGVFs4M4'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:35](https://www.youtube.com/watch?v=hTxjhDN2Cyo&t=395s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A note okay the note is the structure of the payment term so people say I have '
              'a mortgage note or I have a car note do I have a web app right or when you lend '
              "money like Marta has loan money to me and where's congratulations.",
      'timestamp': 395,
      'timestamp_label': '[00:06:35]',
      'timestamp_seconds': 395,
      'tip': 'A note okay the note is the structure of the payment term so people say I have a '
             'mortgage note or I have a car note do I have a web app right or when you lend '
             "money like Marta has loan money to me and where's congratulations.",
      'title': 'Understanding Real Estate Wraps | Wrap Around Mortgages Explained (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=hTxjhDN2Cyo&t=395s',
      'video_id': 'hTxjhDN2Cyo'}],
 9: [{'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:18](https://www.youtube.com/watch?v=dMDfltvY39k&t=618s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The title company does the transfer. I go through a legal transaction through a '
              'third party. The company we use is Creative Title and escrow. You can use them '
              "all you want. We'll pop up their logo right on the screen and you can see their "
              'domain.',
      'timestamp': 618,
      'timestamp_label': '[00:10:18]',
      'timestamp_seconds': 618,
      'tip': 'The title company does the transfer. I go through a legal transaction through a '
             'third party. The company we use is Creative Title and escrow. You can use them '
             "all you want. We'll pop up their logo right on the screen and you can see their "
             'domain.',
      'title': 'Busting the Biggest Myth in Creative Finance (Due on Sale Clause) (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=dMDfltvY39k&t=618s',
      'video_id': 'dMDfltvY39k'},
     {'author': 'Key & Capital',
      'channel': 'Key & Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:46](https://www.youtube.com/watch?v=dzuLMB2Szxc&t=646s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, check the Fannie Mae seasoning rules with your lender before you sign. The '
              'balloon, the due on sale clause, and the 12-month wait. All three are deadly if '
              'you ignore them. Because seller financing is not the wild west, the law has '
              'lines.',
      'timestamp': 646,
      'timestamp_label': '[00:10:46]',
      'timestamp_seconds': 646,
      'tip': 'So, check the Fannie Mae seasoning rules with your lender before you sign. The '
             'balloon, the due on sale clause, and the 12-month wait. All three are deadly if '
             'you ignore them. Because seller financing is not the wild west, the law has '
             'lines.',
      'title': 'Seller Financing Explained: How to Buy Property Without a Bank (Key & Capital)',
      'url': 'https://www.youtube.com/watch?v=dzuLMB2Szxc&t=646s',
      'video_id': 'dzuLMB2Szxc'},
     {'author': 'Dom Inglese',
      'channel': 'Dom Inglese',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:50](https://www.youtube.com/watch?v=Lv34MZLHg1I&t=350s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s rates in terms of what he'd get from a bank without having to jump through "
              'all those hoops. So, he made out on this deal. Tom, he owns the asset and I '
              'made it out on this deal because I have that cash flow. I have that equity and '
              'I have that great rate.',
      'timestamp': 350,
      'timestamp_label': '[00:05:50]',
      'timestamp_seconds': 350,
      'tip': "'s rates in terms of what he'd get from a bank without having to jump through "
             'all those hoops. So, he made out on this deal. Tom, he owns the asset and I made '
             'it out on this deal because I have that cash flow. I have that equity and I have '
             'that great rate.',
      'title': 'Subject-To Wraparound: The Creative Finance Cheat Code You’re Not Using '
               '(Tampa) (Dom Inglese)',
      'url': 'https://www.youtube.com/watch?v=Lv34MZLHg1I&t=350s',
      'video_id': 'Lv34MZLHg1I'},
     {'author': 'Maximilian Dier',
      'channel': 'Maximilian Dier',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:34](https://www.youtube.com/watch?v=GqiH4Kh8eaQ&t=394s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Richard Taylor has buyers for properties with balloons, that's ultimately all "
              'that matters. Balloons are a lot more common in multif family, guys. '
              'Residential, I I hate balloons. This property I got under contract, guys, this '
              'was 30 years 0% interest.',
      'timestamp': 394,
      'timestamp_label': '[00:06:34]',
      'timestamp_seconds': 394,
      'tip': "Richard Taylor has buyers for properties with balloons, that's ultimately all "
             'that matters. Balloons are a lot more common in multif family, guys. '
             'Residential, I I hate balloons. This property I got under contract, guys, this '
             'was 30 years 0% interest.',
      'title': "I Tested Richard Taylor's Seller Finance Script ... and IT WORKED (Maximilian "
               'Dier)',
      'url': 'https://www.youtube.com/watch?v=GqiH4Kh8eaQ&t=394s',
      'video_id': 'GqiH4Kh8eaQ'},
     {'author': 'FDICchannel',
      'channel': 'FDICchannel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:37](https://www.youtube.com/watch?v=MfYdg5BCNlk&t=97s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you don\'t have a "covered transaction," you can stop here. The ATR/QM rules '
              "will not apply. For the rest of this video, we'll be presuming you do have a "
              'covered transaction, and focusing on how to demonstrate compliance with the '
              'ATR/QM requirements.',
      'timestamp': 97,
      'timestamp_label': '[00:01:37]',
      'timestamp_seconds': 97,
      'tip': 'If you don\'t have a "covered transaction," you can stop here. The ATR/QM rules '
             "will not apply. For the rest of this video, we'll be presuming you do have a "
             'covered transaction, and focusing on how to demonstrate compliance with the '
             'ATR/QM requirements.',
      'title': 'ATR-QM: The Core Requirement - A Reasonable Determination of an '
               'Ability-to-Repay (FDICchannel)',
      'url': 'https://www.youtube.com/watch?v=MfYdg5BCNlk&t=97s',
      'video_id': 'MfYdg5BCNlk'},
     {'author': 'Investor Fuel - Real Estate Mastermind',
      'channel': 'Investor Fuel - Real Estate Mastermind',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:09](https://www.youtube.com/watch?v=VrGeElvxk5E&t=1749s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But other states like Michigan have a contract for deed law where it's much "
              'better to do that versus a foreclosure. So those are more common uh up there '
              'because the the law recognizes those type of arrangements. You can do them in '
              'all states.',
      'timestamp': 1749,
      'timestamp_label': '[00:29:09]',
      'timestamp_seconds': 1749,
      'tip': "But other states like Michigan have a contract for deed law where it's much "
             'better to do that versus a foreclosure. So those are more common uh up there '
             'because the the law recognizes those type of arrangements. You can do them in '
             'all states.',
      'title': 'Why Note Investing Beats Rentals: 11% Returns, Less Risk, and No Tenants with '
               'Kevin Shortle (Investor Fuel - Real Estate Mastermind)',
      'url': 'https://www.youtube.com/watch?v=VrGeElvxk5E&t=1749s',
      'video_id': 'VrGeElvxk5E'},
     {'author': 'Affinity Real Estate & Mortgage Training',
      'channel': 'Affinity Real Estate & Mortgage Training',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=5IxbTVhJdr8&t=15s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Are several sections of the Safe Act exam or the nmls exam one portion of that '
              'deals with the uniform State content and the Safe Act rules and.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Are several sections of the Safe Act exam or the nmls exam one portion of that '
             'deals with the uniform State content and the Safe Act rules and.',
      'title': 'Passing the NMLS Exam - THE SAFE ACT REGULATION  - POP QUIZ (Affinity Real '
               'Estate & Mortgage Training)',
      'url': 'https://www.youtube.com/watch?v=5IxbTVhJdr8&t=15s',
      'video_id': '5IxbTVhJdr8'},
     {'author': 'Note Investing & Seller Financing - JKP Holdings',
      'channel': 'Note Investing & Seller Financing - JKP Holdings',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:37:45](https://www.youtube.com/watch?v=uKK5_EVlvus&t=2265s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Having the right to entry is a landlord tenant scenario or a contract for deed '
              'scenario. No, I I would argue that if the buyer agrees to this is it there is '
              "it against the law? It's just very weird wording for you guys out there. Is it "
              'something that will not stand in court?',
      'timestamp': 2265,
      'timestamp_label': '[00:37:45]',
      'timestamp_seconds': 2265,
      'tip': 'Having the right to entry is a landlord tenant scenario or a contract for deed '
             'scenario. No, I I would argue that if the buyer agrees to this is it there is it '
             "against the law? It's just very weird wording for you guys out there. Is it "
             'something that will not stand in court?',
      'title': 'Most Seller Finance Notes Are Legally Worthless | Sohail Badruddin (Note '
               'Investing & Seller Financing - JKP Holdings)',
      'url': 'https://www.youtube.com/watch?v=uKK5_EVlvus&t=2265s',
      'video_id': 'uKK5_EVlvus'},
     {'author': 'Andrea Saavedra, Realtor',
      'channel': 'Andrea Saavedra, Realtor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=VhziKmSIpLQ&t=15s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sellers disclosure notice correctly this information will be very beneficial '
              "for buyers sellers and in real estate agents I do believe that it's very "
              'important.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Sellers disclosure notice correctly this information will be very beneficial for '
             "buyers sellers and in real estate agents I do believe that it's very important.",
      'title': "Seller's Disclosure Notice Explanation (Andrea Saavedra, Realtor)",
      'url': 'https://www.youtube.com/watch?v=VhziKmSIpLQ&t=15s',
      'video_id': 'VhziKmSIpLQ'},
     {'author': "Scott Horne's Owner Finance Network",
      'channel': "Scott Horne's Owner Finance Network",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:56](https://www.youtube.com/watch?v=it6vSh38OhY&t=236s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You have checked your specific state to ensure you're meeting any of the other "
              "rules and regulations that might be out there when you're selling a home to a.",
      'timestamp': 236,
      'timestamp_label': '[00:03:56]',
      'timestamp_seconds': 236,
      'tip': "You have checked your specific state to ensure you're meeting any of the other "
             "rules and regulations that might be out there when you're selling a home to a.",
      'title': "Wrap Around Mortgages: What You Need to Know (Scott Horne's Owner Finance "
               'Network)',
      'url': 'https://www.youtube.com/watch?v=it6vSh38OhY&t=236s',
      'video_id': 'it6vSh38OhY'},
     {'author': 'Mark J Kohler',
      'channel': 'Mark J Kohler',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=jThMHTcyEdY&t=92s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You don't get to do the installment sale. You got to pay all the taxes from now "
              "that's not the end of the world you still may sell property with a note and Do "
              'some seller financing so that you can sell your fix and flips or rehabs?',
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': "You don't get to do the installment sale. You got to pay all the taxes from now "
             "that's not the end of the world you still may sell property with a note and Do "
             'some seller financing so that you can sell your fix and flips or rehabs?',
      'title': 'When To Use An Installment Sale With Real Estate | Mark J Kohler | Tax & Legal '
               'Tip (Mark J Kohler)',
      'url': 'https://www.youtube.com/watch?v=jThMHTcyEdY&t=92s',
      'video_id': 'jThMHTcyEdY'},
     {'author': 'Make Your Money Multiply',
      'channel': 'Make Your Money Multiply',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:10](https://www.youtube.com/watch?v=upiVxcM_yIM&t=250s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Prefer to have a trusted expert handle it? If you want a licensed broker and '
              'consultant to guide or represent you, a deal done with total compliance and '
              'confidence, and a custom strategy tailored to your property and goals, go to '
              'green meadowinvestmentslc.',
      'timestamp': 250,
      'timestamp_label': '[00:04:10]',
      'timestamp_seconds': 250,
      'tip': 'Prefer to have a trusted expert handle it? If you want a licensed broker and '
             'consultant to guide or represent you, a deal done with total compliance and '
             'confidence, and a custom strategy tailored to your property and goals, go to '
             'green meadowinvestmentslc.',
      'title': 'Subject-To + Wraparound Mortgage Explained: Pros & Cons (Make Your Money '
               'Multiply)',
      'url': 'https://www.youtube.com/watch?v=upiVxcM_yIM&t=250s',
      'video_id': 'upiVxcM_yIM'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:46:19](https://www.youtube.com/watch?v=IdhS21bvT_o&t=2779s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Property that is a pure seller finance deal okay an executory contract same '
              'thing except in an executory contract okay remember an executory contract is um '
              "all of these things right indeed um sorry bonfer deed that one's pretty rare "
              'but bond for deed installment sale.',
      'timestamp': 2779,
      'timestamp_label': '[00:46:19]',
      'timestamp_seconds': 2779,
      'tip': 'Property that is a pure seller finance deal okay an executory contract same '
             'thing except in an executory contract okay remember an executory contract is um '
             "all of these things right indeed um sorry bonfer deed that one's pretty rare but "
             'bond for deed installment sale.',
      'title': 'Creative Finance Q and A SubTo Paperwork Seller Finance Paperwork (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=IdhS21bvT_o&t=2779s',
      'video_id': 'IdhS21bvT_o'},
     {'author': 'Paperstac',
      'channel': 'Paperstac',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:25](https://www.youtube.com/watch?v=jFBvJbcMbFA&t=1405s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Taught to leverage their equity it was the way to return the equity in your '
              "house zero right yeah that's good do you teach your like your grandkids your "
              'kids like did you start hammering them on on notes and stuff like that or yeah.',
      'timestamp': 1405,
      'timestamp_label': '[00:23:25]',
      'timestamp_seconds': 1405,
      'tip': 'Taught to leverage their equity it was the way to return the equity in your '
             "house zero right yeah that's good do you teach your like your grandkids your "
             'kids like did you start hammering them on on notes and stuff like that or yeah.',
      'title': 'Mortgage Note Arbitrage & the Future of the Industry (Interview) (Paperstac)',
      'url': 'https://www.youtube.com/watch?v=jFBvJbcMbFA&t=1405s',
      'video_id': 'jFBvJbcMbFA'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:15](https://www.youtube.com/watch?v=Kk_nfIhy2LY&t=255s)',
      'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                   'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                   'mortgages, and licensed-servicer performing note spreads (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Even insert yourself as an equity partner on these deals which would be pretty '
              'amazing so if you want to learn how Gators are making money in these real '
              'estate transactions and get a little bit deeper dive then click the video on '
              'your screen.',
      'timestamp': 255,
      'timestamp_label': '[00:04:15]',
      'timestamp_seconds': 255,
      'tip': 'Even insert yourself as an equity partner on these deals which would be pretty '
             'amazing so if you want to learn how Gators are making money in these real estate '
             'transactions and get a little bit deeper dive then click the video on your '
             'screen.',
      'title': 'Subject To vs Seller Finance (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=Kk_nfIhy2LY&t=255s',
      'video_id': 'Kk_nfIhy2LY'}],
 10: [{'author': 'Ameritrain Mortgage Institute',
       'channel': 'Ameritrain Mortgage Institute',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:43](https://www.youtube.com/watch?v=35EmXeZQAsY&t=103s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "You can just call this the no surprises at the closing table act. It's all "
               'about making sure borrowers see every settlement cost upfront. But just as '
               'importantly, it completely outlaws kickbacks.',
       'timestamp': 103,
       'timestamp_label': '[00:01:43]',
       'timestamp_seconds': 103,
       'tip': "You can just call this the no surprises at the closing table act. It's all "
              'about making sure borrowers see every settlement cost upfront. But just as '
              'importantly, it completely outlaws kickbacks.',
       'title': 'Federal Mortgage Laws Explained: RESPA, TILA, ECOA & the SAFE Act (Ameritrain '
                'Mortgage Institute)',
       'url': 'https://www.youtube.com/watch?v=35EmXeZQAsY&t=103s',
       'video_id': '35EmXeZQAsY'},
      {'author': 'Real Estate Law Guys I Asset Protection',
       'channel': 'Real Estate Law Guys I Asset Protection',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:35](https://www.youtube.com/watch?v=nAfkFrw2mTU&t=95s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "If you're the buyer of a subject to deal, right before the seller files for "
               "bankruptcy, you fit the profile. And now you're going to have that trustee "
               'eyeing your transaction. You say, "Wait a minute, Jeff. Maybe you paid all in '
               'cash.',
       'timestamp': 95,
       'timestamp_label': '[00:01:35]',
       'timestamp_seconds': 95,
       'tip': "If you're the buyer of a subject to deal, right before the seller files for "
              "bankruptcy, you fit the profile. And now you're going to have that trustee "
              'eyeing your transaction. You say, "Wait a minute, Jeff. Maybe you paid all in '
              'cash.',
       'title': 'LAWYER: How to Protect Your "Subject-To" Deal From a Seller Bankruptcy! (Real '
                'Estate Law Guys I Asset Protection)',
       'url': 'https://www.youtube.com/watch?v=nAfkFrw2mTU&t=95s',
       'video_id': 'nAfkFrw2mTU'},
      {'author': 'Hans Goldstein: Tax & Exit Planning',
       'channel': 'Hans Goldstein: Tax & Exit Planning',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:10](https://www.youtube.com/watch?v=mIvRRP_DEd0&t=70s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The straight line building depreciation here is unrecaptured section 1250 '
               'gain. It is not recapture income. Under Treasury Regulation 1. 453-12, it '
               'stays inside the gain and is reported first as payments arrive. It waits for '
               'the cash flow.',
       'timestamp': 70,
       'timestamp_label': '[00:01:10]',
       'timestamp_seconds': 70,
       'tip': 'The straight line building depreciation here is unrecaptured section 1250 gain. '
              'It is not recapture income. Under Treasury Regulation 1. 453-12, it stays '
              'inside the gain and is reported first as payments arrive. It waits for the cash '
              'flow.',
       'title': 'Form 6252: How Do You Report an Installment Sale? (2026) (Hans Goldstein: Tax '
                '& Exit Planning)',
       'url': 'https://www.youtube.com/watch?v=mIvRRP_DEd0&t=70s',
       'video_id': 'mIvRRP_DEd0'},
      {'author': 'Tim Talks Real Estate',
       'channel': 'Tim Talks Real Estate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:03](https://www.youtube.com/watch?v=Dklhw3jMfVo&t=183s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'That clause says if you sell or transfer the property, the lender has the '
               'right to demand the entire loan balance back immediately. Not the monthly '
               'payment, the whole thing all at once.',
       'timestamp': 183,
       'timestamp_label': '[00:03:03]',
       'timestamp_seconds': 183,
       'tip': 'That clause says if you sell or transfer the property, the lender has the right '
              'to demand the entire loan balance back immediately. Not the monthly payment, '
              'the whole thing all at once.',
       'title': 'Wraparound Mortgages Explained How They Work and the Due on Sale Landmine '
                '(Tim Talks Real Estate)',
       'url': 'https://www.youtube.com/watch?v=Dklhw3jMfVo&t=183s',
       'video_id': 'Dklhw3jMfVo'},
      {'author': 'My Divorce Mortgage Planning with Karla Kyte, CDLP',
       'channel': 'My Divorce Mortgage Planning with Karla Kyte, CDLP',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:58](https://www.youtube.com/watch?v=DANV_9GW0PU&t=178s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The gar St Germaine Act of 1982 this is what protects you from the do on sale '
               'Clause that is in that deed of trust when you purchase the property.',
       'timestamp': 178,
       'timestamp_label': '[00:02:58]',
       'timestamp_seconds': 178,
       'tip': 'The gar St Germaine Act of 1982 this is what protects you from the do on sale '
              'Clause that is in that deed of trust when you purchase the property.',
       'title': 'Protect Your Rights | Garn-St Germain Act (My Divorce Mortgage Planning with '
                'Karla Kyte, CDLP)',
       'url': 'https://www.youtube.com/watch?v=DANV_9GW0PU&t=178s',
       'video_id': 'DANV_9GW0PU'},
      {'author': 'PPR Capital Management',
       'channel': 'PPR Capital Management',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:21:09](https://www.youtube.com/watch?v=DEk2gIFHJiM&t=1269s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Now, step back a little bit. So, at our current scale, once again, I '
               "mentioned, you know, we're buying these in large pools.",
       'timestamp': 1269,
       'timestamp_label': '[00:21:09]',
       'timestamp_seconds': 1269,
       'tip': 'Now, step back a little bit. So, at our current scale, once again, I mentioned, '
              "you know, we're buying these in large pools.",
       'title': 'Mortgage Note Investing Explained: The Non-Performing Loan Opportunity (PPR '
                'Capital Management)',
       'url': 'https://www.youtube.com/watch?v=DEk2gIFHJiM&t=1269s',
       'video_id': 'DEk2gIFHJiM'},
      {'author': 'Jeff Jinks Law',
       'channel': 'Jeff Jinks Law',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=93T1nghQfhs&t=15s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Under code section 453 i know that sounds boring and whatnot but a lot of '
               "people have done monetized installment sales over the years they've been a.",
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Under code section 453 i know that sounds boring and whatnot but a lot of '
              "people have done monetized installment sales over the years they've been a.",
       'title': '173 Monetized Installment Sale and the Dirty Dozen (Jeff Jinks Law)',
       'url': 'https://www.youtube.com/watch?v=93T1nghQfhs&t=15s',
       'video_id': '93T1nghQfhs'},
      {'author': "Scott Horne's Owner Finance Network",
       'channel': "Scott Horne's Owner Finance Network",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:15](https://www.youtube.com/watch?v=ZLt_A_LBSu0&t=315s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "They're exempt from RESPA, Dodd-Frank, the SAFE Act, those kind of things. "
               "Here in Texas, they're exempt from the property code as well as the finance "
               'code other than some basic disclosures that need to be done.',
       'timestamp': 315,
       'timestamp_label': '[00:05:15]',
       'timestamp_seconds': 315,
       'tip': "They're exempt from RESPA, Dodd-Frank, the SAFE Act, those kind of things. Here "
              "in Texas, they're exempt from the property code as well as the finance code "
              'other than some basic disclosures that need to be done.',
       'title': "Can You Buy a Wraparound Mortgage  How “Sub 3” Deals Work (Scott Horne's "
                'Owner Finance Network)',
       'url': 'https://www.youtube.com/watch?v=ZLt_A_LBSu0&t=315s',
       'video_id': 'ZLt_A_LBSu0'},
      {'author': 'Asset Preservation, Inc.',
       'channel': 'Asset Preservation, Inc.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:21](https://www.youtube.com/watch?v=uBB6B7Fz6Xc&t=381s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': '30,000 dollars of exchange proceeds the qualified intermediary is the '
               'beneficiary on the note the taxpayer comes in with $70,000 of additional cash.',
       'timestamp': 381,
       'timestamp_label': '[00:06:21]',
       'timestamp_seconds': 381,
       'tip': '30,000 dollars of exchange proceeds the qualified intermediary is the '
              'beneficiary on the note the taxpayer comes in with $70,000 of additional cash.',
       'title': 'Seller Financing  IRC Section 453 | FAQ | Asset Preservation, Inc. (Asset '
                'Preservation, Inc.)',
       'url': 'https://www.youtube.com/watch?v=uBB6B7Fz6Xc&t=381s',
       'video_id': 'uBB6B7Fz6Xc'},
      {'author': 'Propelio TV',
       'channel': 'Propelio TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:27](https://www.youtube.com/watch?v=pCK7ihJF_-Q&t=927s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Charging interest on a larger amount for longer period of time and collecting '
               'all the benefits from that so what does that actually mean as far as profits '
               'well.',
       'timestamp': 927,
       'timestamp_label': '[00:15:27]',
       'timestamp_seconds': 927,
       'tip': 'Charging interest on a larger amount for longer period of time and collecting '
              'all the benefits from that so what does that actually mean as far as profits '
              'well.',
       'title': 'Wrap Around Mortgages | Make Money w/ Subject To & Wraps (Propelio TV)',
       'url': 'https://www.youtube.com/watch?v=pCK7ihJF_-Q&t=927s',
       'video_id': 'pCK7ihJF_-Q'},
      {'author': 'On The Market',
       'channel': 'On The Market',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=coT9sTaZqQg&t=15s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Me is Kathy Fey Kathy you're bringing on one of your old friends today as our "
               "guest can you tell us about him yeah I've known Eddie speed for years he is.",
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': "Me is Kathy Fey Kathy you're bringing on one of your old friends today as our "
              "guest can you tell us about him yeah I've known Eddie speed for years he is.",
       'title': 'The Hidden Danger of “Subject To” Real Estate… (On The Market)',
       'url': 'https://www.youtube.com/watch?v=coT9sTaZqQg&t=15s',
       'video_id': 'coT9sTaZqQg'},
      {'author': 'kris haskins',
       'channel': 'kris haskins',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:08](https://www.youtube.com/watch?v=kM__5b36grI&t=188s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The first mortgage to the first mortgage lender okay so what does all that '
               'mean i know this a lot.',
       'timestamp': 188,
       'timestamp_label': '[00:03:08]',
       'timestamp_seconds': 188,
       'tip': 'The first mortgage to the first mortgage lender okay so what does all that mean '
              'i know this a lot.',
       'title': 'What is a Wraparound Wrap Note Mortgage-Subject to-Land Contract (kris '
                'haskins)',
       'url': 'https://www.youtube.com/watch?v=kM__5b36grI&t=188s',
       'video_id': 'kM__5b36grI'},
      {'author': 'Pace Morby',
       'channel': 'Pace Morby',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:21:37](https://www.youtube.com/watch?v=B5EMtjV6RJM&t=1297s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Information over in the case of this deal you'll be able to change it all over "
               "in in the login and I'll give you that before we close Okay so that's it "
               "that's all of the documents that you'll be signing with with Hannah today "
               'sweet okay what we doing next.',
       'timestamp': 1297,
       'timestamp_label': '[00:21:37]',
       'timestamp_seconds': 1297,
       'tip': "Information over in the case of this deal you'll be able to change it all over "
              "in in the login and I'll give you that before we close Okay so that's it that's "
              "all of the documents that you'll be signing with with Hannah today sweet okay "
              'what we doing next.',
       'title': 'In-Depth Explanation of Seller Finance Paperwork (Pace Morby)',
       'url': 'https://www.youtube.com/watch?v=B5EMtjV6RJM&t=1297s',
       'video_id': 'B5EMtjV6RJM'},
      {'author': 'Paperstac',
       'channel': 'Paperstac',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:34](https://www.youtube.com/watch?v=kXMfkHu1Tu0&t=334s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Interface it's going to allow me to easily access my stuff that's smart yeah "
               "so that's a little snackable for you hopefully a little knowledge bomb boom "
               "we'll uh we'll catch you on the next one see ya.",
       'timestamp': 334,
       'timestamp_label': '[00:05:34]',
       'timestamp_seconds': 334,
       'tip': "Interface it's going to allow me to easily access my stuff that's smart yeah so "
              "that's a little snackable for you hopefully a little knowledge bomb boom we'll "
              "uh we'll catch you on the next one see ya.",
       'title': 'Mortgage Note Servicers - How to Pick Yours (Snackable) (Paperstac)',
       'url': 'https://www.youtube.com/watch?v=kXMfkHu1Tu0&t=334s',
       'video_id': 'kXMfkHu1Tu0'},
      {'author': 'Pace Morby',
       'channel': 'Pace Morby',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:30](https://www.youtube.com/watch?v=-IIDN2AQQsg&t=150s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Okay I'm going to sprinkle scorpions on the house you know like once a seller "
               "understands that it's not a bad thing it's actually a good thing for that to "
               'happen you can convince a seller to do just about anything you need in order '
               'to buy that property.',
       'timestamp': 150,
       'timestamp_label': '[00:02:30]',
       'timestamp_seconds': 150,
       'tip': "Okay I'm going to sprinkle scorpions on the house you know like once a seller "
              "understands that it's not a bad thing it's actually a good thing for that to "
              'happen you can convince a seller to do just about anything you need in order to '
              'buy that property.',
       'title': 'Can You Do A Subject To AND Seller Finance Deal? (Pace Morby)',
       'url': 'https://www.youtube.com/watch?v=-IIDN2AQQsg&t=150s',
       'video_id': '-IIDN2AQQsg'}],
 11: [{'author': 'FIXnotes | Non-Performing Note Investing',
       'channel': 'FIXnotes | Non-Performing Note Investing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:59](https://www.youtube.com/watch?v=qxx8ymWOrGU&t=119s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Agreement ments that have fully amortised terms and a bunch more all right so '
               'now we have our next exit strategy and that is a cash for keys.',
       'timestamp': 119,
       'timestamp_label': '[00:01:59]',
       'timestamp_seconds': 119,
       'tip': 'Agreement ments that have fully amortised terms and a bunch more all right so '
              'now we have our next exit strategy and that is a cash for keys.',
       'title': '6 Ways to Profit from Non-Performing Notes (FIXnotes | Non-Performing Note '
                'Investing)',
       'url': 'https://www.youtube.com/watch?v=qxx8ymWOrGU&t=119s',
       'video_id': 'qxx8ymWOrGU'},
      {'author': 'Richard Taylor',
       'channel': 'Richard Taylor',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:45](https://www.youtube.com/watch?v=fu3wlMepckY&t=45s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "But it's not just all the other investors who saw this ad, it is our entire "
               'buyers list that my team has been collecting for the past four and a half '
               'years. Guys, I have over a million followers across my platforms.',
       'timestamp': 45,
       'timestamp_label': '[00:00:45]',
       'timestamp_seconds': 45,
       'tip': "But it's not just all the other investors who saw this ad, it is our entire "
              'buyers list that my team has been collecting for the past four and a half '
              'years. Guys, I have over a million followers across my platforms.',
       'title': 'How to Find Off-Market Creative Finance Deals (0% Seller Financing) (Richard '
                'Taylor)',
       'url': 'https://www.youtube.com/watch?v=fu3wlMepckY&t=45s',
       'video_id': 'fu3wlMepckY'},
      {'author': 'Pace Morby',
       'channel': 'Pace Morby',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:43](https://www.youtube.com/watch?v=4krb0pqCMC8&t=103s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Mortgage company it's going to us I have zero worry about the due on sale "
               'clause we know how to handle it um and worst case scenario I end up '
               'refinancing it out and then we you just pay us a monthly bill and guess what '
               'we make interest we make money on the money.',
       'timestamp': 103,
       'timestamp_label': '[00:01:43]',
       'timestamp_seconds': 103,
       'tip': "Mortgage company it's going to us I have zero worry about the due on sale "
              'clause we know how to handle it um and worst case scenario I end up refinancing '
              'it out and then we you just pay us a monthly bill and guess what we make '
              'interest we make money on the money.',
       'title': 'How To Handle A Due On Sale Clause (Pace Morby)',
       'url': 'https://www.youtube.com/watch?v=4krb0pqCMC8&t=103s',
       'video_id': '4krb0pqCMC8'},
      {'author': 'My Mortgage Trainer, Inc.',
       'channel': 'My Mortgage Trainer, Inc.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=rmcxN_JOvoY&t=20s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'To address these issues, it is crucial to have a consistent definition of '
               'unfair practices or treatment. The consistent definition of unfairness is '
               'found in the Federal Trade Commission Act.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'To address these issues, it is crucial to have a consistent definition of '
              'unfair practices or treatment. The consistent definition of unfairness is found '
              'in the Federal Trade Commission Act.',
       'title': 'Dodd Frank Loan Originator Compensation (Module 3) | NMLS SAFE MLO Exam Study '
                'Series and Test Prep (My Mortgage Trainer, Inc.)',
       'url': 'https://www.youtube.com/watch?v=rmcxN_JOvoY&t=20s',
       'video_id': 'rmcxN_JOvoY'},
      {'author': 'In Rem Podcast',
       'channel': 'In Rem Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:29](https://www.youtube.com/watch?v=2ZZq6UibGDE&t=329s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Impacted or affected by the bankruptcy filing so that's it it's somewhat "
               'complicated hopefully it never happens but what if a seller files for '
               "bankruptcy post uh closing out subject to transaction there's the analysis.",
       'timestamp': 329,
       'timestamp_label': '[00:05:29]',
       'timestamp_seconds': 329,
       'tip': "Impacted or affected by the bankruptcy filing so that's it it's somewhat "
              'complicated hopefully it never happens but what if a seller files for '
              "bankruptcy post uh closing out subject to transaction there's the analysis.",
       'title': 'What if the Seller files for Bankruptcy after the Closing of a Subject To '
                'Transaction? (In Rem Podcast)',
       'url': 'https://www.youtube.com/watch?v=2ZZq6UibGDE&t=329s',
       'video_id': '2ZZq6UibGDE'},
      {'author': 'Jason D. Knott',
       'channel': 'Jason D. Knott',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:22](https://www.youtube.com/watch?v=ifqWkX-3DBI&t=82s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Five-year period right so john sold the property in 2020 but he's not getting "
               "the cash all up front he's gonna record the income under the installment sale.",
       'timestamp': 82,
       'timestamp_label': '[00:01:22]',
       'timestamp_seconds': 82,
       'tip': "Five-year period right so john sold the property in 2020 but he's not getting "
              "the cash all up front he's gonna record the income under the installment sale.",
       'title': 'How to Complete IRS Form 6252 - Income Reported Using the Installment Method '
                '(Jason D. Knott)',
       'url': 'https://www.youtube.com/watch?v=ifqWkX-3DBI&t=82s',
       'video_id': 'ifqWkX-3DBI'},
      {'author': 'Flipping Mastery TV',
       'channel': 'Flipping Mastery TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=pvgEqb4r4gw&t=15s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Series on creative financing in part one we did this big overview we gave some '
               "examples we talked about all the things we're going to cover in the series "
               "it's.",
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Series on creative financing in part one we did this big overview we gave some '
              "examples we talked about all the things we're going to cover in the series "
              "it's.",
       'title': 'How to Structure Creative Finance Deals - Masterclass Video 2 w/ Pace Morby '
                '(Flipping Mastery TV)',
       'url': 'https://www.youtube.com/watch?v=pvgEqb4r4gw&t=15s',
       'video_id': 'pvgEqb4r4gw'},
      {'author': 'TrustThisTV',
       'channel': 'TrustThisTV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:08](https://www.youtube.com/watch?v=yd3L18YPXDU&t=68s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Absolutely yes there is the Garn St Germain act that allows you to sell your '
               'property or to uh not sell your property but convey your property into a '
               'trust.',
       'timestamp': 68,
       'timestamp_label': '[00:01:08]',
       'timestamp_seconds': 68,
       'tip': 'Absolutely yes there is the Garn St Germain act that allows you to sell your '
              'property or to uh not sell your property but convey your property into a trust.',
       'title': 'Exceptions to the Due on Sale Clause & the Garn-St. Germain Act (TrustThisTV)',
       'url': 'https://www.youtube.com/watch?v=yd3L18YPXDU&t=68s',
       'video_id': 'yd3L18YPXDU'},
      {'author': 'kris haskins',
       'channel': 'kris haskins',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:20](https://www.youtube.com/watch?v=FybFcuS9T7s&t=920s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Money good Lord how much time have I been on here with these fools hello sir '
               'yes sir okay thanks for being patient waiting here for me um yeah based of on '
               "what I'm seeing here this all started in November okay you have my undivided.",
       'timestamp': 920,
       'timestamp_label': '[00:15:20]',
       'timestamp_seconds': 920,
       'tip': 'Money good Lord how much time have I been on here with these fools hello sir '
              'yes sir okay thanks for being patient waiting here for me um yeah based of on '
              "what I'm seeing here this all started in November okay you have my undivided.",
       'title': 'how to talk to sellers mortgage company on subject to real estate deal (kris '
                'haskins)',
       'url': 'https://www.youtube.com/watch?v=FybFcuS9T7s&t=920s',
       'video_id': 'FybFcuS9T7s'},
      {'author': 'Straight Up Mortgage Talk',
       'channel': 'Straight Up Mortgage Talk',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:00](https://www.youtube.com/watch?v=Qnk52S1LXHI&t=120s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Very cautious of these These are risky for both buyer and seller this is Tim '
               'Harrison the hlc team at Cornerstone Home lending this is our straight up '
               'mortgage talk our educational series talk to you soon and hope that helps.',
       'timestamp': 120,
       'timestamp_label': '[00:02:00]',
       'timestamp_seconds': 120,
       'tip': 'Very cautious of these These are risky for both buyer and seller this is Tim '
              'Harrison the hlc team at Cornerstone Home lending this is our straight up '
              'mortgage talk our educational series talk to you soon and hope that helps.',
       'title': "Don't Get Burned by Wrap-Around Mortgages and Subject-to Financing! (Straight "
                'Up Mortgage Talk)',
       'url': 'https://www.youtube.com/watch?v=Qnk52S1LXHI&t=120s',
       'video_id': 'Qnk52S1LXHI'},
      {'author': 'Dani Rudd',
       'channel': 'Dani Rudd',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:05](https://www.youtube.com/watch?v=5VZzJLRM1kI&t=65s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re just not meeting the the guidelines for those traditional loans, but "
               "otherwise they're high credit, high net worth, high cash flow individuals that "
               'would absolutely be able to sustain and pay a mortgage.',
       'timestamp': 65,
       'timestamp_label': '[00:01:05]',
       'timestamp_seconds': 65,
       'tip': "'re just not meeting the the guidelines for those traditional loans, but "
              "otherwise they're high credit, high net worth, high cash flow individuals that "
              'would absolutely be able to sustain and pay a mortgage.',
       'title': 'Non QM Mortgage Loan Explained | 3 Ways Self Employed Borrowers Can Qualify '
                '(Dani Rudd)',
       'url': 'https://www.youtube.com/watch?v=5VZzJLRM1kI&t=65s',
       'video_id': '5VZzJLRM1kI'},
      {'author': 'Sub2Empire',
       'channel': 'Sub2Empire',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:02](https://www.youtube.com/watch?v=3_e0FAwLlwU&t=542s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Fast response or physical Damage of jade website to impart not come over to '
               'work in the studio Ultimate is indispensable nourished watching performance à.',
       'timestamp': 542,
       'timestamp_label': '[00:09:02]',
       'timestamp_seconds': 542,
       'tip': 'Fast response or physical Damage of jade website to impart not come over to '
              'work in the studio Ultimate is indispensable nourished watching performance à.',
       'title': 'What Is The Due On Sale Clause (And How To Avoid It When Buying Houses '
                'Subject-To) (Sub2Empire)',
       'url': 'https://www.youtube.com/watch?v=3_e0FAwLlwU&t=542s',
       'video_id': '3_e0FAwLlwU'},
      {'author': 'Paperstac',
       'channel': 'Paperstac',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:10](https://www.youtube.com/watch?v=UwiEQOh84Y4&t=190s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Wouldn't be married that's cool that's a cool story great actually pretty safe "
               'and so you guys started your own company you said in late 90s well I.',
       'timestamp': 190,
       'timestamp_label': '[00:03:10]',
       'timestamp_seconds': 190,
       'tip': "Wouldn't be married that's cool that's a cool story great actually pretty safe "
              'and so you guys started your own company you said in late 90s well I.',
       'title': 'Partial Mortgage Note Training with Fred & Tracy Rewey (Paperstac)',
       'url': 'https://www.youtube.com/watch?v=UwiEQOh84Y4&t=190s',
       'video_id': 'UwiEQOh84Y4'},
      {'author': 'Pace Morby',
       'channel': 'Pace Morby',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:19](https://www.youtube.com/watch?v=oBTB4KZYxq8&t=559s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Ownership of that back in the event that you default on your payments right '
               "all of that needs to be laid out now part number four once you've got your.",
       'timestamp': 559,
       'timestamp_label': '[00:09:19]',
       'timestamp_seconds': 559,
       'tip': 'Ownership of that back in the event that you default on your payments right all '
              "of that needs to be laid out now part number four once you've got your.",
       'title': 'NO BANK NEEDED! | How To Buy or Sell a Car on Seller Finance (Pace Morby)',
       'url': 'https://www.youtube.com/watch?v=oBTB4KZYxq8&t=559s',
       'video_id': 'oBTB4KZYxq8'},
      {'author': 'Music City TC',
       'channel': 'Music City TC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:26](https://www.youtube.com/watch?v=-AAdJ4WwUuM&t=146s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s lender, and if you're buying in an LLC, your entity documents. That usually "
               'means the articles, the operating agreement, and proof the company is in good '
               "standing. In many states, a title company can't give legal advice or draft "
               'certain documents.',
       'timestamp': 146,
       'timestamp_label': '[00:02:26]',
       'timestamp_seconds': 146,
       'tip': "'s lender, and if you're buying in an LLC, your entity documents. That usually "
              'means the articles, the operating agreement, and proof the company is in good '
              "standing. In many states, a title company can't give legal advice or draft "
              'certain documents.',
       'title': '12 Questions to Ask a Title Company Before You Send a Subject-To or Creative '
                'Finance Deal (Music City TC)',
       'url': 'https://www.youtube.com/watch?v=-AAdJ4WwUuM&t=146s',
       'video_id': '-AAdJ4WwUuM'}],
 12: [{'author': 'Paperstac',
       'channel': 'Paperstac',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:44](https://www.youtube.com/watch?v=VkGqESM8fdY&t=104s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s happened over the past day, two days, week, weeks, or months, years, and "
               "see what's going on, or if you're potentially gonna be buying a loan, to get "
               "an idea of the history. It's very important, I would say the servicing notes "
               'are as important as the payment history.',
       'timestamp': 104,
       'timestamp_label': '[00:01:44]',
       'timestamp_seconds': 104,
       'tip': "'s happened over the past day, two days, week, weeks, or months, years, and see "
              "what's going on, or if you're potentially gonna be buying a loan, to get an "
              "idea of the history. It's very important, I would say the servicing notes are "
              'as important as the payment history.',
       'title': 'How to Read Payment History on a Mortgage Note (Decode the Servicing Notes) '
                '(Paperstac)',
       'url': 'https://www.youtube.com/watch?v=VkGqESM8fdY&t=104s',
       'video_id': 'VkGqESM8fdY'},
      {'author': 'Attorney Hamilton Rucker',
       'channel': 'Attorney Hamilton Rucker',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:11](https://www.youtube.com/watch?v=4coBBRVrtIA&t=311s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "There's a mandatory 7-day warning period before closing. The seller must give "
               'the buyer a list of all existing loans on the property at least 7 days before '
               'closing.',
       'timestamp': 311,
       'timestamp_label': '[00:05:11]',
       'timestamp_seconds': 311,
       'tip': "There's a mandatory 7-day warning period before closing. The seller must give "
              'the buyer a list of all existing loans on the property at least 7 days before '
              'closing.',
       'title': 'Texas Wraparound Mortgages: Too Good To Be True? (Attorney Hamilton Rucker)',
       'url': 'https://www.youtube.com/watch?v=4coBBRVrtIA&t=311s',
       'video_id': '4coBBRVrtIA'},
      {'author': 'Epic Real Estate',
       'channel': 'Epic Real Estate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:44](https://www.youtube.com/watch?v=5n5x76_xKLU&t=44s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I did say 10 times faster, than all of those people going to work every day, '
               'making sacrifices, saving their money in things like a 401k, and having to '
               'wait 30 to 40 years before they can even begin to enjoy it. Can you believe '
               "that's the plan we've all been told to follow?",
       'timestamp': 44,
       'timestamp_label': '[00:00:44]',
       'timestamp_seconds': 44,
       'tip': 'I did say 10 times faster, than all of those people going to work every day, '
              'making sacrifices, saving their money in things like a 401k, and having to wait '
              "30 to 40 years before they can even begin to enjoy it. Can you believe that's "
              "the plan we've all been told to follow?",
       'title': 'Wraparound Mortgage & All Inclusive Trust Deed (AITD) | Creative Real Estate '
                'Investing | Video 9 (Epic Real Estate)',
       'url': 'https://www.youtube.com/watch?v=5n5x76_xKLU&t=44s',
       'video_id': '5n5x76_xKLU'},
      {'author': 'Ritchie School of Real Estate Finance',
       'channel': 'Ritchie School of Real Estate Finance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:45](https://www.youtube.com/watch?v=NXTK3N8EVO8&t=105s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Afford so if the lender does not abide by the requirements of the ATR of the '
               "ability to repay that's when an action could be brought against that.",
       'timestamp': 105,
       'timestamp_label': '[00:01:45]',
       'timestamp_seconds': 105,
       'tip': 'Afford so if the lender does not abide by the requirements of the ATR of the '
              "ability to repay that's when an action could be brought against that.",
       'title': 'Dodd Frank Ability to Repay (Ritchie School of Real Estate Finance)',
       'url': 'https://www.youtube.com/watch?v=NXTK3N8EVO8&t=105s',
       'video_id': 'NXTK3N8EVO8'},
      {'author': 'Philip Louden | WrapAcademy',
       'channel': 'Philip Louden | WrapAcademy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:15](https://www.youtube.com/watch?v=oGD3QKECaGk&t=675s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, 5 to 10 year lease options. This is more of a strategy for me. Like, once '
               'you have at least 10,000 a month in cash flow, now we want to start looking at '
               "shorter term lease options. It doesn't need to be 5 10 years. It can be two "
               'years regardless.',
       'timestamp': 675,
       'timestamp_label': '[00:11:15]',
       'timestamp_seconds': 675,
       'tip': 'So, 5 to 10 year lease options. This is more of a strategy for me. Like, once '
              'you have at least 10,000 a month in cash flow, now we want to start looking at '
              "shorter term lease options. It doesn't need to be 5 10 years. It can be two "
              'years regardless.',
       'title': 'Wrap Mortgages VS Lease Options VS Contract for Deed (Full Breakdown) (Philip '
                'Louden | WrapAcademy)',
       'url': 'https://www.youtube.com/watch?v=oGD3QKECaGk&t=675s',
       'video_id': 'oGD3QKECaGk'},
      {'author': 'Mamadou Diallo',
       'channel': 'Mamadou Diallo',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:18:44](https://www.youtube.com/watch?v=UpPEu5m2V4Y&t=1124s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'How many transactions happen per day um until I actually have a friend who '
               "owns a title company uh in Arizona Michael and it's they actually you know.",
       'timestamp': 1124,
       'timestamp_label': '[00:18:44]',
       'timestamp_seconds': 1124,
       'tip': 'How many transactions happen per day um until I actually have a friend who owns '
              "a title company uh in Arizona Michael and it's they actually you know.",
       'title': 'Is Subto Real Estate Investing Legal? Attorney Michael Answers | Creative '
                'Finance 101 (Mamadou Diallo)',
       'url': 'https://www.youtube.com/watch?v=UpPEu5m2V4Y&t=1124s',
       'video_id': 'UpPEu5m2V4Y'},
      {'author': 'Stealth Wealth',
       'channel': 'Stealth Wealth',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:30](https://www.youtube.com/watch?v=0m8vHNeASRY&t=270s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'All those smaller balloons they all start coming together into one big one the '
               'point is balloon payments can be risky because they mean that if your.',
       'timestamp': 270,
       'timestamp_label': '[00:04:30]',
       'timestamp_seconds': 270,
       'tip': 'All those smaller balloons they all start coming together into one big one the '
              'point is balloon payments can be risky because they mean that if your.',
       'title': 'Mortgage Note Investing (Explained) in 8 Minutes! (Stealth Wealth)',
       'url': 'https://www.youtube.com/watch?v=0m8vHNeASRY&t=270s',
       'video_id': '0m8vHNeASRY'},
      {'author': 'Ironclad Wealth Management',
       'channel': 'Ironclad Wealth Management',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:42](https://www.youtube.com/watch?v=wCs54NX0Oe8&t=522s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "5 million house when you sell your business, I don't know if that's smart. I'm "
               "just saying if that's your plan, hey, you might not want to do this because "
               "you can't get all the money up front.",
       'timestamp': 522,
       'timestamp_label': '[00:08:42]',
       'timestamp_seconds': 522,
       'tip': "5 million house when you sell your business, I don't know if that's smart. I'm "
              "just saying if that's your plan, hey, you might not want to do this because you "
              "can't get all the money up front.",
       'title': 'Structured Installment Sales - Eliminate Buyer Risk While Deferring Taxes '
                '(Ironclad Wealth Management)',
       'url': 'https://www.youtube.com/watch?v=wCs54NX0Oe8&t=522s',
       'video_id': 'wCs54NX0Oe8'},
      {'author': 'Pace Morby',
       'channel': 'Pace Morby',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:05](https://www.youtube.com/watch?v=rQCg4GFRLAI&t=245s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "But don't you have a seller that has a mortgage payment that you pay them "
               "every month? Okay, so you're getting >> a Morby with cash back. I get that, "
               "but if it's a Morby deal that means that you have a first position lender. Oh "
               'yeah, yeah, yeah, exactly, exactly.',
       'timestamp': 245,
       'timestamp_label': '[00:04:05]',
       'timestamp_seconds': 245,
       'tip': "But don't you have a seller that has a mortgage payment that you pay them every "
              "month? Okay, so you're getting >> a Morby with cash back. I get that, but if "
              "it's a Morby deal that means that you have a first position lender. Oh yeah, "
              'yeah, yeah, exactly, exactly.',
       'title': 'How to Properly Structure Creative Finance Deals (Pace Morby)',
       'url': 'https://www.youtube.com/watch?v=rQCg4GFRLAI&t=245s',
       'video_id': 'rQCg4GFRLAI'},
      {'author': 'Shari Olefson',
       'channel': 'Shari Olefson',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:54](https://www.youtube.com/watch?v=g-UjM12V8m0&t=174s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Dodd-frank is the action congress took to keep that from ever happening again '
               "now four years later we're essentially getting what we asked for tell us what "
               'you think about the new dodd-frank laws or email your questions to ask the '
               'expert at sherry oliveson.com.',
       'timestamp': 174,
       'timestamp_label': '[00:02:54]',
       'timestamp_seconds': 174,
       'tip': 'Dodd-frank is the action congress took to keep that from ever happening again '
              "now four years later we're essentially getting what we asked for tell us what "
              'you think about the new dodd-frank laws or email your questions to ask the '
              'expert at sherry oliveson.com.',
       'title': "New Dodd Frank Mortgage Laws & What's In Store For Banks & Borrowers? (Shari "
                'Olefson)',
       'url': 'https://www.youtube.com/watch?v=g-UjM12V8m0&t=174s',
       'video_id': 'g-UjM12V8m0'},
      {'author': 'Horne Real Estate Law',
       'channel': 'Horne Real Estate Law',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=00RujvVfDRc&t=15s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And Associates uh what do you do Scott what is it exactly that you do too damn '
               'much to be honest with you there are days.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'And Associates uh what do you do Scott what is it exactly that you do too damn '
              'much to be honest with you there are days.',
       'title': 'Low Equity, Big Profits  Owner Finance Wraps (Horne Real Estate Law)',
       'url': 'https://www.youtube.com/watch?v=00RujvVfDRc&t=15s',
       'video_id': '00RujvVfDRc'},
      {'author': 'FIXnotes | Non-Performing Note Investing',
       'channel': 'FIXnotes | Non-Performing Note Investing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:27](https://www.youtube.com/watch?v=5H6jVWw2QK0&t=327s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Talking about the revolution happening in real estate where regular investors '
               'can earn great profits while helping homeowners that the banks have failed '
               'join the movement and start your journey into note investing at fix.com.',
       'timestamp': 327,
       'timestamp_label': '[00:05:27]',
       'timestamp_seconds': 327,
       'tip': 'Talking about the revolution happening in real estate where regular investors '
              'can earn great profits while helping homeowners that the banks have failed join '
              'the movement and start your journey into note investing at fix.com.',
       'title': "The Beginner's Guide To Loan Servicing (FIXnotes | Non-Performing Note "
                'Investing)',
       'url': 'https://www.youtube.com/watch?v=5H6jVWw2QK0&t=327s',
       'video_id': '5H6jVWw2QK0'},
      {'author': 'Tax Sale Academy',
       'channel': 'Tax Sale Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:31](https://www.youtube.com/watch?v=o4SYyovrZw4&t=151s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Over to taxol academy.com don't forget your free copy tax off playbook which "
               'you can get at exile kami calm and my web class tax like every icon click on '
               'web class web class is completely free so is the book just cover shipping on '
               'the book hey take care guys man.',
       'timestamp': 151,
       'timestamp_label': '[00:02:31]',
       'timestamp_seconds': 151,
       'tip': "Over to taxol academy.com don't forget your free copy tax off playbook which "
              'you can get at exile kami calm and my web class tax like every icon click on '
              'web class web class is completely free so is the book just cover shipping on '
              'the book hey take care guys man.',
       'title': 'Tax Sales, Owner Financing and Dodd Frank (Tax Sale Academy)',
       'url': 'https://www.youtube.com/watch?v=o4SYyovrZw4&t=151s',
       'video_id': 'o4SYyovrZw4'},
      {'author': 'Pace Morby',
       'channel': 'Pace Morby',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:19:29](https://www.youtube.com/watch?v=1GjR0GDWoyo&t=1169s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That I make some she's one month behind on payment so I'm going to pay catch "
               "up that payment where does that money come from we'll break all of that down "
               'on a future YouTube video in part two of this Saga.',
       'timestamp': 1169,
       'timestamp_label': '[00:19:29]',
       'timestamp_seconds': 1169,
       'tip': "That I make some she's one month behind on payment so I'm going to pay catch up "
              "that payment where does that money come from we'll break all of that down on a "
              'future YouTube video in part two of this Saga.',
       'title': 'Explaining Subject To IN PERSON With A Seller (Pace Morby)',
       'url': 'https://www.youtube.com/watch?v=1GjR0GDWoyo&t=1169s',
       'video_id': '1GjR0GDWoyo'},
      {'author': 'Larry Hoffman',
       'channel': 'Larry Hoffman',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:23](https://www.youtube.com/watch?v=R_jwbBWh1LA&t=143s)',
       'relevance': 'Attributed practitioner commentary on low-rate `Subject-To` debt '
                    'acquisition, `SAFE Act`/`Dodd-Frank` `RMLO`-underwritten wraparound '
                    'mortgages, and licensed-servicer performing note spreads (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'When you buy a note, this is the legal agreement that dictates the cash flow '
               "you're going to receive every single month. Now, it's absolutely crucial to "
               'understand the clear distinction between two documents that people confuse all '
               'the time.',
       'timestamp': 143,
       'timestamp_label': '[00:02:23]',
       'timestamp_seconds': 143,
       'tip': 'When you buy a note, this is the legal agreement that dictates the cash flow '
              "you're going to receive every single month. Now, it's absolutely crucial to "
              'understand the clear distinction between two documents that people confuse all '
              'the time.',
       'title': 'Note Investing Explained: How to Become the Bank in 2026 (Larry Hoffman)',
       'url': 'https://www.youtube.com/watch?v=R_jwbBWh1LA&t=143s',
       'video_id': 'R_jwbBWh1LA'}]}
