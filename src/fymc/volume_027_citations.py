"""Curated 180-citation Business Acquisition baseline (15 per chapter across Q1-Q12) mined strictly from verified Business Acquisition YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'100',
     '197',
     '338h10',
     'acquire',
     'acquired',
     'acquisition',
     'add',
     'adjustment',
     'asset',
     'avoiding',
     'axial',
     'baby',
     'backs',
     'bankruptcy',
     'bizbuysell',
     'boomer',
     'breakup',
     'build',
     'bulk',
     'business',
     'buy',
     'buying',
     'capital',
     'change',
     'clearance',
     'client',
     'clients',
     'closing',
     'codie',
     'com',
     'concentration',
     'contractor',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'100',
     '197',
     '338h10',
     'acquire',
     'acquired',
     'acquisition',
     'add',
     'adjustment',
     'asset',
     'avoiding',
     'axial',
     'baby',
     'backs',
     'bankruptcy',
     'bizbuysell',
     'boomer',
     'breakup',
     'budget',
     'build',
     'bulk',
     'business',
     'buy',
     'buyer',
     'buying',
     'capital',
     'change',
     'clearance',
     'closing',
     'codie',
     'com',
     'concentration',
     'contract',
     'contractor',
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
 3: {'100',
     '197',
     '338h10',
     'acquire',
     'acquired',
     'acquisition',
     'add',
     'adjustment',
     'asset',
     'avoiding',
     'axial',
     'baby',
     'backs',
     'bankruptcy',
     'bizbuysell',
     'boomer',
     'breakup',
     'build',
     'bulk',
     'business',
     'buy',
     'buying',
     'capital',
     'cash',
     'cashflow',
     'change',
     'clearance',
     'closing',
     'codie',
     'com',
     'commission',
     'concentration',
     'contractor',
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
 4: {'100',
     '197',
     '338h10',
     'acquire',
     'acquired',
     'acquisition',
     'add',
     'adjustment',
     'asset',
     'avoiding',
     'axial',
     'baby',
     'backs',
     'bankruptcy',
     'bizbuysell',
     'boomer',
     'breakup',
     'budget',
     'build',
     'bulk',
     'business',
     'buy',
     'buying',
     'capital',
     'change',
     'clearance',
     'closing',
     'codie',
     'com',
     'concentration',
     'contractor',
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
 5: {'100',
     '197',
     '338h10',
     'acquire',
     'acquired',
     'acquisition',
     'add',
     'adjustment',
     'asset',
     'audit',
     'avoid',
     'avoiding',
     'axial',
     'baby',
     'backs',
     'bankruptcy',
     'bizbuysell',
     'boomer',
     'breakup',
     'build',
     'bulk',
     'business',
     'buy',
     'buying',
     'capital',
     'change',
     'clawback',
     'clearance',
     'closing',
     'codie',
     'com',
     'concentration',
     'contractor',
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
 6: {'100',
     '197',
     '338h10',
     'acquire',
     'acquired',
     'acquisition',
     'add',
     'adjustment',
     'asset',
     'avoiding',
     'axial',
     'baby',
     'backs',
     'bankruptcy',
     'bizbuysell',
     'boomer',
     'breakup',
     'build',
     'bulk',
     'business',
     'buy',
     'buying',
     'capital',
     'change',
     'clearance',
     'client',
     'closing',
     'codie',
     'com',
     'concentration',
     'contractor',
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
 7: {'100',
     '197',
     '338h10',
     'acquire',
     'acquired',
     'acquisition',
     'add',
     'adjustment',
     'asset',
     'avoiding',
     'axial',
     'baby',
     'backs',
     'bankruptcy',
     'bizbuysell',
     'boomer',
     'breakup',
     'build',
     'bulk',
     'business',
     'buy',
     'buying',
     'capital',
     'change',
     'checklist',
     'clearance',
     'closing',
     'codie',
     'com',
     'concentration',
     'contractor',
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
 8: {'100',
     '197',
     '338h10',
     'acquire',
     'acquired',
     'acquisition',
     'add',
     'adjustment',
     'api',
     'asset',
     'avoiding',
     'axial',
     'baby',
     'backs',
     'bankruptcy',
     'bizbuysell',
     'boomer',
     'breakup',
     'build',
     'bulk',
     'business',
     'buy',
     'buying',
     'capital',
     'change',
     'clearance',
     'closing',
     'codie',
     'com',
     'concentration',
     'contractor',
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
 9: {'100',
     '197',
     '338h10',
     'acquire',
     'acquired',
     'acquisition',
     'add',
     'adjustment',
     'agreement',
     'asset',
     'avoiding',
     'axial',
     'baby',
     'backs',
     'bankruptcy',
     'bizbuysell',
     'boomer',
     'breakup',
     'build',
     'bulk',
     'business',
     'buy',
     'buying',
     'capital',
     'change',
     'clearance',
     'closing',
     'codie',
     'com',
     'compliance',
     'concentration',
     'contract',
     'contractor',
     'disclosure',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'100',
      '197',
      '338h10',
      'acquire',
      'acquired',
      'acquisition',
      'add',
      'adjustment',
      'agent',
      'ai',
      'asset',
      'automate',
      'automation',
      'avoiding',
      'axial',
      'baby',
      'backs',
      'bankruptcy',
      'bizbuysell',
      'boomer',
      'breakup',
      'build',
      'bulk',
      'business',
      'buy',
      'buying',
      'capital',
      'change',
      'clearance',
      'closing',
      'codie',
      'com',
      'concentration',
      'contractor',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'100',
      '197',
      '338h10',
      'acquire',
      'acquired',
      'acquisition',
      'add',
      'adjustment',
      'asset',
      'avoiding',
      'axial',
      'baby',
      'backs',
      'bankruptcy',
      'bizbuysell',
      'boomer',
      'breakup',
      'build',
      'bulk',
      'business',
      'buy',
      'buying',
      'capital',
      'change',
      'clearance',
      'closing',
      'codie',
      'com',
      'concentration',
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
 12: {'100',
      '197',
      '338h10',
      'acquire',
      'acquired',
      'acquisition',
      'action',
      'add',
      'adjustment',
      'asset',
      'avoiding',
      'axial',
      'baby',
      'backs',
      'bankruptcy',
      'bizbuysell',
      'boomer',
      'breakup',
      'build',
      'bulk',
      'business',
      'buy',
      'buying',
      'capital',
      'change',
      'clearance',
      'closing',
      'codie',
      'com',
      'concentration',
      'contractor',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'The Money Rules',
      'channel': 'The Money Rules',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:47](https://www.youtube.com/watch?v=DyCKwhKRtK0&t=167s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Jordan is buying a landscaping company for $1,000,000, with no real estate. Add '
              '$100,000 for working capital and closing costs, and the whole project is '
              '$1,100,000. The seller can carry up to $55,000 of it on standby. The other '
              "$55,000 has to be Jordan's own cash.",
      'timestamp': 167,
      'timestamp_label': '[00:02:47]',
      'timestamp_seconds': 167,
      'tip': 'Jordan is buying a landscaping company for $1,000,000, with no real estate. Add '
             '$100,000 for working capital and closing costs, and the whole project is '
             '$1,100,000. The seller can carry up to $55,000 of it on standby. The other '
             "$55,000 has to be Jordan's own cash.",
      'title': 'SBA Loan to Buy a Business: What Changed on October 1, 2026 (The Money Rules)',
      'url': 'https://www.youtube.com/watch?v=DyCKwhKRtK0&t=167s',
      'video_id': 'DyCKwhKRtK0'},
     {'author': 'Michael S Glaspie',
      'channel': 'Michael S Glaspie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:39](https://www.youtube.com/watch?v=WfgrSa37vaA&t=459s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'But there is something referred to as goodwill. And so goodwill is essentially '
              'the value above the physical assets, right? Then often times when you buy a '
              "business, you're buying customers, you're buying potential lead revenue.",
      'timestamp': 459,
      'timestamp_label': '[00:07:39]',
      'timestamp_seconds': 459,
      'tip': 'But there is something referred to as goodwill. And so goodwill is essentially '
             'the value above the physical assets, right? Then often times when you buy a '
             "business, you're buying customers, you're buying potential lead revenue.",
      'title': 'New SBA Rules 2027: What Changed for Buying a Business (Michael S Glaspie)',
      'url': 'https://www.youtube.com/watch?v=WfgrSa37vaA&t=459s',
      'video_id': 'WfgrSa37vaA'},
     {'author': 'Jonathan Jay',
      'channel': 'Jonathan Jay',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:01](https://www.youtube.com/watch?v=zrmjVDmvL1w&t=841s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I have private clients doing very very well at this in all manner of sectors '
              'all around the world. The buy and build strategy is certainly a route to great '
              'wealth. So, how do you feel right now? Do you feel excited about the '
              'possibility of buying a business?',
      'timestamp': 841,
      'timestamp_label': '[00:14:01]',
      'timestamp_seconds': 841,
      'tip': 'I have private clients doing very very well at this in all manner of sectors all '
             'around the world. The buy and build strategy is certainly a route to great '
             'wealth. So, how do you feel right now? Do you feel excited about the possibility '
             'of buying a business?',
      'title': 'Complete Guide to Buying a Business (For Beginners) 2026 | Jonathan Jay '
               '(Jonathan Jay)',
      'url': 'https://www.youtube.com/watch?v=zrmjVDmvL1w&t=841s',
      'video_id': 'zrmjVDmvL1w'},
     {'author': 'Master Afle',
      'channel': 'Master Afle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:10](https://www.youtube.com/watch?v=LzJITHl_i2k&t=1510s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'ROI of over 100% on her initial $94,120 investment. The power of active value '
              'creation becomes clear when we project these numbers over a 10-year horizon. '
              "Suppose Nancy uses her CEO skill set to grow the business's revenue by a "
              'healthy, modest rate of 10% every year.',
      'timestamp': 1510,
      'timestamp_label': '[00:25:10]',
      'timestamp_seconds': 1510,
      'tip': 'ROI of over 100% on her initial $94,120 investment. The power of active value '
             'creation becomes clear when we project these numbers over a 10-year horizon. '
             "Suppose Nancy uses her CEO skill set to grow the business's revenue by a "
             'healthy, modest rate of 10% every year.',
      'title': 'Buy Then Build by Walker Deibel | audiobook summary | Mastering the '
               'Acquisition Game (Master Afle)',
      'url': 'https://www.youtube.com/watch?v=LzJITHl_i2k&t=1510s',
      'video_id': 'LzJITHl_i2k'},
     {'author': 'Walker Deibel',
      'channel': 'Walker Deibel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:30:18](https://www.youtube.com/watch?v=6KZrugmBkcs&t=1818s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Right so you've got to have that peace and um if you start with that then uh "
              "everything's just better off than sort of frankensteining on the that strategy "
              'later so how do we get started okay drum roll the buy and build value creation '
              'model.',
      'timestamp': 1818,
      'timestamp_label': '[00:30:18]',
      'timestamp_seconds': 1818,
      'tip': "Right so you've got to have that peace and um if you start with that then uh "
             "everything's just better off than sort of frankensteining on the that strategy "
             'later so how do we get started okay drum roll the buy and build value creation '
             'model.',
      'title': 'Walker at Codie Sanchez Mastermind Event (Walker Deibel)',
      'url': 'https://www.youtube.com/watch?v=6KZrugmBkcs&t=1818s',
      'video_id': '6KZrugmBkcs'},
     {'author': 'Kenny Finance',
      'channel': 'Kenny Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:12](https://www.youtube.com/watch?v=7znMZDlxFBU&t=1212s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And then secondly, build a network of incredible business brokers that have '
              'armies of people reaching out to business owners every single day. Get your '
              "name out there that you're in the market to buy a business.",
      'timestamp': 1212,
      'timestamp_label': '[00:20:12]',
      'timestamp_seconds': 1212,
      'tip': 'And then secondly, build a network of incredible business brokers that have '
             'armies of people reaching out to business owners every single day. Get your name '
             "out there that you're in the market to buy a business.",
      'title': 'How I Find Businesses to Buy: Step-by-Step Method (Kenny Finance)',
      'url': 'https://www.youtube.com/watch?v=7znMZDlxFBU&t=1212s',
      'video_id': '7znMZDlxFBU'},
     {'author': 'Chris Barrett, CPA',
      'channel': 'Chris Barrett, CPA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:02](https://www.youtube.com/watch?v=36OTOiIXSrk&t=122s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Finally, if you're buying a business that's over $10 million in enterprise "
              "value, we're going to have to go through and build a custom scope with you, and "
              "you're usually going to be $25 plus,000 for that type of project. At Midwest "
              'CPA, we do deals like this all the time.',
      'timestamp': 122,
      'timestamp_label': '[00:02:02]',
      'timestamp_seconds': 122,
      'tip': "Finally, if you're buying a business that's over $10 million in enterprise "
             "value, we're going to have to go through and build a custom scope with you, and "
             "you're usually going to be $25 plus,000 for that type of project. At Midwest "
             'CPA, we do deals like this all the time.',
      'title': 'How Much Does a Quality of Earnings (QoE) Analysis Cost? (Chris Barrett, CPA)',
      'url': 'https://www.youtube.com/watch?v=36OTOiIXSrk&t=122s',
      'video_id': '36OTOiIXSrk'},
     {'author': 'David Nazeem Aboud',
      'channel': 'David Nazeem Aboud',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=_exEOi-Wxuk&t=22s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '"This is just a complete waste of my time. " like he just stormed out like '
              'downstairs down to the warehouse and started building stuff. Um, so just to '
              "introduce you, Pete. Um, you're a entrepreneur through acquisition, um, "
              'investor, business operator, coach, and mentor.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': '"This is just a complete waste of my time. " like he just stormed out like '
             'downstairs down to the warehouse and started building stuff. Um, so just to '
             "introduce you, Pete. Um, you're a entrepreneur through acquisition, um, "
             'investor, business operator, coach, and mentor.',
      'title': 'How to Buy and Scale Businesses (ETA Explained) | Pete Seligman x David Aboud '
               '[Part 1] (David Nazeem Aboud)',
      'url': 'https://www.youtube.com/watch?v=_exEOi-Wxuk&t=22s',
      'video_id': '_exEOi-Wxuk'},
     {'author': 'The University of Chicago Booth School of Business',
      'channel': 'The University of Chicago Booth School of Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:34:28](https://www.youtube.com/watch?v=60ZOJolZwOo&t=2068s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'What happens then is that $2 million EBITDA business, bought it five times, so '
              "$10 million in enterprise value. Chances are you're gonna maybe lever that up "
              '50% of the capital structure.',
      'timestamp': 2068,
      'timestamp_label': '[00:34:28]',
      'timestamp_seconds': 2068,
      'tip': 'What happens then is that $2 million EBITDA business, bought it five times, so '
             "$10 million in enterprise value. Chances are you're gonna maybe lever that up "
             '50% of the capital structure.',
      'title': 'Understanding the Basics of Entrepreneurship Through Acquisition - Event '
               'Series (The University of Chicago Booth School of Business)',
      'url': 'https://www.youtube.com/watch?v=60ZOJolZwOo&t=2068s',
      'video_id': '60ZOJolZwOo'},
     {'author': 'ProjectionHub',
      'channel': 'ProjectionHub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:09](https://www.youtube.com/watch?v=uXEbfHnDSes&t=129s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Now based on the data that I have input into the model right now we've got "
              'plenty of room for air plenty of margin here with a 4.64 uh debt service.',
      'timestamp': 129,
      'timestamp_label': '[00:02:09]',
      'timestamp_seconds': 129,
      'tip': "Now based on the data that I have input into the model right now we've got "
             'plenty of room for air plenty of margin here with a 4.64 uh debt service.',
      'title': 'How to Create Financial Projections for a Search Fund Acquisition (Template '
               'Walkthrough) (ProjectionHub)',
      'url': 'https://www.youtube.com/watch?v=uXEbfHnDSes&t=129s',
      'video_id': 'uXEbfHnDSes'},
     {'author': 'CandiMentor',
      'channel': 'CandiMentor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:45](https://www.youtube.com/watch?v=a5aX7QK8vKA&t=165s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The key question is whether the buyer will effectively fund it after closing. '
              'Picture the diligence room. One person traces revenue to contracts, another '
              'challenges an add-back, and a third reconciles the balance sheet.',
      'timestamp': 165,
      'timestamp_label': '[00:02:45]',
      'timestamp_seconds': 165,
      'tip': 'The key question is whether the buyer will effectively fund it after closing. '
             'Picture the diligence room. One person traces revenue to contracts, another '
             'challenges an add-back, and a third reconciles the balance sheet.',
      'title': 'Financial Due Diligence: Quality of Earnings Analysis Step-by-Step '
               '(CandiMentor)',
      'url': 'https://www.youtube.com/watch?v=a5aX7QK8vKA&t=165s',
      'video_id': 'a5aX7QK8vKA'},
     {'author': 'SaaStr AI',
      'channel': 'SaaStr AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=KAz03HJ5nHg&t=15s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Through how to build go to market efficiency specifically in SNB sales Kyle '
              'welcome thanks for joining us thank you for having me excited to chat with.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Through how to build go to market efficiency specifically in SNB sales Kyle '
             'welcome thanks for joining us thank you for having me excited to chat with.',
      'title': 'How to Build Go-to-Market Efficiency in SMB Sales with Owner.com CRO Kyle '
               'Norton (SaaStr AI)',
      'url': 'https://www.youtube.com/watch?v=KAz03HJ5nHg&t=15s',
      'video_id': 'KAz03HJ5nHg'},
     {'author': '100 Days and Beyond Podcast',
      'channel': '100 Days and Beyond Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:33](https://www.youtube.com/watch?v=4jPZ0fzlgQY&t=273s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Market so um most people that were in the end buying that equipment and at the '
              'retail and were using it to grow plants that.',
      'timestamp': 273,
      'timestamp_label': '[00:04:33]',
      'timestamp_seconds': 273,
      'tip': 'Market so um most people that were in the end buying that equipment and at the '
             'retail and were using it to grow plants that.',
      'title': 'How to make a successful M&A deal - 100 Days and Beyond (100 Days and Beyond '
               'Podcast)',
      'url': 'https://www.youtube.com/watch?v=4jPZ0fzlgQY&t=273s',
      'video_id': '4jPZ0fzlgQY'},
     {'author': 'Acquiring Minds',
      'channel': 'Acquiring Minds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:41:12](https://www.youtube.com/watch?v=0lg8Gh_uAPU&t=2472s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Just segment it into talk to me about how the self-funded model increases '
              'probability of closing and then talk to me about how the self-funded its.',
      'timestamp': 2472,
      'timestamp_label': '[00:41:12]',
      'timestamp_seconds': 2472,
      'tip': 'Just segment it into talk to me about how the self-funded model increases '
             'probability of closing and then talk to me about how the self-funded its.',
      'title': 'Self-Funded Search vs. Traditional Search Funds (Acquiring Minds)',
      'url': 'https://www.youtube.com/watch?v=0lg8Gh_uAPU&t=2472s',
      'video_id': '0lg8Gh_uAPU'},
     {'author': 'UNSW eLearning',
      'channel': 'UNSW eLearning',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:30](https://www.youtube.com/watch?v=WUI9T65UP54&t=390s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Driving the evolution of real-life synergies over time in m a integrations '
              'these feedback loops explain a range of different performance outcomes '
              'including integrations that exceed initial synergy expectations and those that '
              'destroy significant value.',
      'timestamp': 390,
      'timestamp_label': '[00:06:30]',
      'timestamp_seconds': 390,
      'tip': 'Driving the evolution of real-life synergies over time in m a integrations these '
             'feedback loops explain a range of different performance outcomes including '
             'integrations that exceed initial synergy expectations and those that destroy '
             'significant value.',
      'title': 'Post-Acquisition Integration Dynamics (UNSW eLearning)',
      'url': 'https://www.youtube.com/watch?v=WUI9T65UP54&t=390s',
      'video_id': 'WUI9T65UP54'}],
 2: [{'author': 'Ed Weeks Jr. MBA',
      'channel': 'Ed Weeks Jr. MBA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=aJcoLYwi6vo&t=75s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'It also has to document every add back and look at customer concentration. '
              "Change three, seller notes. A note only counts toward the buyer's down payment "
              "if it's on full standby, meaning no payments of principal or interest for the "
              'life of the SBA loan.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': 'It also has to document every add back and look at customer concentration. '
             "Change three, seller notes. A note only counts toward the buyer's down payment "
             "if it's on full standby, meaning no payments of principal or interest for the "
             'life of the SBA loan.',
      'title': 'SBA Loan Changes 2026: What Business Sellers Need to Know (Ed Weeks Jr. MBA)',
      'url': 'https://www.youtube.com/watch?v=aJcoLYwi6vo&t=75s',
      'video_id': 'aJcoLYwi6vo'},
     {'author': 'John Colley | The Investment Banking Practitioner',
      'channel': 'John Colley | The Investment Banking Practitioner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:27](https://www.youtube.com/watch?v=x_72u8PgHpc&t=147s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'At closing, actual working capital is measured. If actual exceeds the peg, the '
              'buyer pays extra. If actual falls below, the seller gets less, dollar for '
              'dollar. This is a direct post-signing purchase price adjustment.',
      'timestamp': 147,
      'timestamp_label': '[00:02:27]',
      'timestamp_seconds': 147,
      'tip': 'At closing, actual working capital is measured. If actual exceeds the peg, the '
             'buyer pays extra. If actual falls below, the seller gets less, dollar for '
             'dollar. This is a direct post-signing purchase price adjustment.',
      'title': 'The Working Capital Peg in M&A: How Sellers Steal Millions at Closing (John '
               'Colley | The Investment Banking Practitioner)',
      'url': 'https://www.youtube.com/watch?v=x_72u8PgHpc&t=147s',
      'video_id': 'x_72u8PgHpc'},
     {'author': 'Morse',
      'channel': 'Morse',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=0V-By_uyuhM&t=22s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Important is because a buyer when they're buying a business they don't want to "
              'buy a business with the cupboards bare they want to buy a.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "Important is because a buyer when they're buying a business they don't want to "
             'buy a business with the cupboards bare they want to buy a.',
      'title': 'Working Capital Adjustment: Common Issues in M&A Transactions (Morse)',
      'url': 'https://www.youtube.com/watch?v=0V-By_uyuhM&t=22s',
      'video_id': '0V-By_uyuhM'},
     {'author': 'jackhaigh',
      'channel': 'jackhaigh',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:32](https://www.youtube.com/watch?v=_m1Q0kLTooU&t=272s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, you guys can see if your business is 250K, you will have an 8% closing fee. '
              "If it's between 250 to a million, it's 7. And then if it's over a million, it's "
              'going to be 6%. Then, when it comes to you as a buyer, what would you be '
              'paying? You have a free basic membership.',
      'timestamp': 272,
      'timestamp_label': '[00:04:32]',
      'timestamp_seconds': 272,
      'tip': 'So, you guys can see if your business is 250K, you will have an 8% closing fee. '
             "If it's between 250 to a million, it's 7. And then if it's over a million, it's "
             'going to be 6%. Then, when it comes to you as a buyer, what would you be paying? '
             'You have a free basic membership.',
      'title': 'Acquire.com Review: An Honest Look At The Pros & Cons 👍👎 (2026) (jackhaigh)',
      'url': 'https://www.youtube.com/watch?v=_m1Q0kLTooU&t=272s',
      'video_id': '_m1Q0kLTooU'},
     {'author': 'A Simple Model',
      'channel': 'A Simple Model',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:35](https://www.youtube.com/watch?v=C-seCQXqtM4&t=215s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Have to go out and purchase that inventory to continue to run the business but '
              'fortunately the funds released from the working capital escrow account make the '
              "buyer whole for this purchase all right team that's all for now thanks for "
              'watching.',
      'timestamp': 215,
      'timestamp_label': '[00:03:35]',
      'timestamp_seconds': 215,
      'tip': 'Have to go out and purchase that inventory to continue to run the business but '
             'fortunately the funds released from the working capital escrow account make the '
             "buyer whole for this purchase all right team that's all for now thanks for "
             'watching.',
      'title': 'Working Capital Adjustment Process (A Simple Model)',
      'url': 'https://www.youtube.com/watch?v=C-seCQXqtM4&t=215s',
      'video_id': 'C-seCQXqtM4'},
     {'author': 'Anchor Partners',
      'channel': 'Anchor Partners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=ob7Q-yxAsNs&t=36s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'A buyer will not pay full price for a business that arrives empty. The peg is a '
              'target level of working capital, usually the trailing twelve month average, and '
              'it gets negotiated in the letter of intent.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': 'A buyer will not pay full price for a business that arrives empty. The peg is a '
             'target level of working capital, usually the trailing twelve month average, and '
             'it gets negotiated in the letter of intent.',
      'title': 'The Working Capital Peg: Why the Price Is Not What You Get at Closing (Anchor '
               'Partners)',
      'url': 'https://www.youtube.com/watch?v=ob7Q-yxAsNs&t=36s',
      'video_id': 'ob7Q-yxAsNs'},
     {'author': 'Josh Kim',
      'channel': 'Josh Kim',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=W3nhTnkKZcU&t=157s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, why would sellers agree to seller financing? Usually, the biggest element '
              "of it is it helps get the deal done. You as the buyer shouldn't want to pay "
              '100% cash for a business.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': 'So, why would sellers agree to seller financing? Usually, the biggest element of '
             "it is it helps get the deal done. You as the buyer shouldn't want to pay 100% "
             'cash for a business.',
      'title': 'How Seller Financing Actually Works in SBA Deals (Josh Kim)',
      'url': 'https://www.youtube.com/watch?v=W3nhTnkKZcU&t=157s',
      'video_id': 'W3nhTnkKZcU'},
     {'author': 'Chris Barrett, CPA',
      'channel': 'Chris Barrett, CPA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=Ru9e1wYKGHc&t=15s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "A few weeks earlier. This change is very key, especially  if you're going to be "
              'a buyer buying a business above $3 million.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "A few weeks earlier. This change is very key, especially  if you're going to be "
             'a buyer buying a business above $3 million.',
      'title': 'Midwest CPA Breaks Down the SBA SOP 50 10 8.1 Technical Update (Chris Barrett, '
               'CPA)',
      'url': 'https://www.youtube.com/watch?v=Ru9e1wYKGHc&t=15s',
      'video_id': 'Ru9e1wYKGHc'},
     {'author': 'Brett Cenkus',
      'channel': 'Brett Cenkus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:54](https://www.youtube.com/watch?v=ydfu0lpiDjc&t=414s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'t matter what happens between now and closing from a working capital "
              'perspective. The buyer doesn\'t have to be worried about the seller "riding the '
              'trade", which is where the seller just doesn\'t pay its payables and collects '
              'really aggressively out its receivables.',
      'timestamp': 414,
      'timestamp_label': '[00:06:54]',
      'timestamp_seconds': 414,
      'tip': "'t matter what happens between now and closing from a working capital "
             'perspective. The buyer doesn\'t have to be worried about the seller "riding the '
             'trade", which is where the seller just doesn\'t pay its payables and collects '
             'really aggressively out its receivables.',
      'title': 'M&A Deal Structures: Working Capital Adjustments vs. Locked Box Closing '
               'Approach (Brett Cenkus)',
      'url': 'https://www.youtube.com/watch?v=ydfu0lpiDjc&t=414s',
      'video_id': 'ydfu0lpiDjc'},
     {'author': 'Kirk Michie',
      'channel': 'Kirk Michie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:13](https://www.youtube.com/watch?v=QqemANnN2ZM&t=133s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s a monthly, quarterly, annual basis, what the average net working capital of "
              "the business is. If you deliver the business with less than that, then you're "
              "going to owe part of the purchase proceeds that you're getting back to the "
              'buyer.',
      'timestamp': 133,
      'timestamp_label': '[00:02:13]',
      'timestamp_seconds': 133,
      'tip': "'s a monthly, quarterly, annual basis, what the average net working capital of "
             "the business is. If you deliver the business with less than that, then you're "
             "going to owe part of the purchase proceeds that you're getting back to the "
             'buyer.',
      'title': 'Net Working Capital Peg for Business Owners (Kirk Michie)',
      'url': 'https://www.youtube.com/watch?v=QqemANnN2ZM&t=133s',
      'video_id': 'QqemANnN2ZM'},
     {'author': 'Walker Deibel',
      'channel': 'Walker Deibel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=t_yGWsgaZ_s&t=52s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "In the space and being able to take advantage of deals like that when you're in "
              "the right place at the right time but it's very uncommon for a first-time buyer "
              'to run out and buy a business.',
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': "In the space and being able to take advantage of deals like that when you're in "
             "the right place at the right time but it's very uncommon for a first-time buyer "
             'to run out and buy a business.',
      'title': 'The Four Paths of Acquisition Entrepreneurship (Walker Deibel)',
      'url': 'https://www.youtube.com/watch?v=t_yGWsgaZ_s&t=52s',
      'video_id': 't_yGWsgaZ_s'},
     {'author': 'Hans Goldstein: Tax & Exit Planning',
      'channel': 'Hans Goldstein: Tax & Exit Planning',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:08](https://www.youtube.com/watch?v=I8L23gqP5to&t=128s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Under Internal Revenue Code section 453B2 and section 453B2B, inventory is '
              'treated as ordinary income. It is completely ineligible for installment '
              'reporting. So the gain on inventory is reported in the year of sale, even if '
              'the buyer pays it later.',
      'timestamp': 128,
      'timestamp_label': '[00:02:08]',
      'timestamp_seconds': 128,
      'tip': 'Under Internal Revenue Code section 453B2 and section 453B2B, inventory is '
             'treated as ordinary income. It is completely ineligible for installment '
             'reporting. So the gain on inventory is reported in the year of sale, even if the '
             'buyer pays it later.',
      'title': "Asset Sale Allocation: What Can't a Seller Note Spread? (2026) (Hans "
               'Goldstein: Tax & Exit Planning)',
      'url': 'https://www.youtube.com/watch?v=I8L23gqP5to&t=128s',
      'video_id': 'I8L23gqP5to'},
     {'author': 'Keira Hamilton',
      'channel': 'Keira Hamilton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:34](https://www.youtube.com/watch?v=JulvxMkY4VY&t=214s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sold our laund matat you know finding the right buyer was is this someone that '
              'we feel comfortable handing our business off to right right and not everyone '
              'who.',
      'timestamp': 214,
      'timestamp_label': '[00:03:34]',
      'timestamp_seconds': 214,
      'tip': 'Sold our laund matat you know finding the right buyer was is this someone that '
             'we feel comfortable handing our business off to right right and not everyone '
             'who.',
      'title': 'Structuring Your Business Acquisition LOI For Success (Keira Hamilton)',
      'url': 'https://www.youtube.com/watch?v=JulvxMkY4VY&t=214s',
      'video_id': 'JulvxMkY4VY'},
     {'author': 'Built to Sell',
      'channel': 'Built to Sell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=3FGfilDTCro&t=31s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'As soon as we were done with that um I mean we worked out little things like if '
              "the deal goes through they're going to pay us you know X for our legal fees.",
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': 'As soon as we were done with that um I mean we worked out little things like if '
             "the deal goes through they're going to pay us you know X for our legal fees.",
      'title': 'How to Negotiate a Letter of Intent With an Acquirer (LOI) (Built to Sell)',
      'url': 'https://www.youtube.com/watch?v=3FGfilDTCro&t=31s',
      'video_id': '3FGfilDTCro'},
     {'author': 'Anna Stepura: AI for Business',
      'channel': 'Anna Stepura: AI for Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:12](https://www.youtube.com/watch?v=oplaAtHYPlU&t=492s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "It's also some limited periods during which uh both of you should transfer the "
              'assets and then es scroll will send the money to the seller.',
      'timestamp': 492,
      'timestamp_label': '[00:08:12]',
      'timestamp_seconds': 492,
      'tip': "It's also some limited periods during which uh both of you should transfer the "
             'assets and then es scroll will send the money to the seller.',
      'title': 'How to Sell Your Startup Company | Acquire.com *full guide in 10 min* (Anna '
               'Stepura: AI for Business)',
      'url': 'https://www.youtube.com/watch?v=oplaAtHYPlU&t=492s',
      'video_id': 'oplaAtHYPlU'}],
 3: [{'author': 'John Colley | The Investment Banking Practitioner',
      'channel': 'John Colley | The Investment Banking Practitioner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=ha9dRzcYak4&t=111s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "If you're pricing a deal on EBITDA, but the cash isn't there, you're buying a "
              'mirage. EBITDA is a useful shorthand, but it ignores five things that consume '
              'real cash. First, capital expenditure. The business needs investment to '
              'maintain its asset base.',
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': "If you're pricing a deal on EBITDA, but the cash isn't there, you're buying a "
             'mirage. EBITDA is a useful shorthand, but it ignores five things that consume '
             'real cash. First, capital expenditure. The business needs investment to maintain '
             'its asset base.',
      'title': 'EBITDA Is an Opinion. Cash Flow Is a Fact. (M&A Practitioner Walkthrough) '
               '(John Colley | The Investment Banking Practitioner)',
      'url': 'https://www.youtube.com/watch?v=ha9dRzcYak4&t=111s',
      'video_id': 'ha9dRzcYak4'},
     {'author': 'Matthias Smith',
      'channel': 'Matthias Smith',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:50](https://www.youtube.com/watch?v=3tkWRQX9WjI&t=650s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "10% of this whole project cost, the purchase price of the company that you're "
              "buying plus everything else, that's going to be the required down payment if "
              'you need to get financed working capital into the acquisition from the bank.',
      'timestamp': 650,
      'timestamp_label': '[00:10:50]',
      'timestamp_seconds': 650,
      'tip': "10% of this whole project cost, the purchase price of the company that you're "
             "buying plus everything else, that's going to be the required down payment if you "
             'need to get financed working capital into the acquisition from the bank.',
      'title': 'The New SBA Rules are LIVE: How to Plan Business Acquisition in 2026 (Matthias '
               'Smith)',
      'url': 'https://www.youtube.com/watch?v=3tkWRQX9WjI&t=650s',
      'video_id': '3tkWRQX9WjI'},
     {'author': 'Corporate Finance Institute',
      'channel': 'Corporate Finance Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:53](https://www.youtube.com/watch?v=FvywvHEpXKU&t=473s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The unit economics of attention. I like that >> the due diligence team '
              'uncovered this insane user engagement, almost zero customer acquisition cost '
              "because it was so viral and crucially very little technical debt. They weren't "
              'buying revenue stream.',
      'timestamp': 473,
      'timestamp_label': '[00:07:53]',
      'timestamp_seconds': 473,
      'tip': 'The unit economics of attention. I like that >> the due diligence team uncovered '
             'this insane user engagement, almost zero customer acquisition cost because it '
             "was so viral and crucially very little technical debt. They weren't buying "
             'revenue stream.',
      'title': 'Corporate Finance Explained | Financial Due Diligence (Corporate Finance '
               'Institute)',
      'url': 'https://www.youtube.com/watch?v=FvywvHEpXKU&t=473s',
      'video_id': 'FvywvHEpXKU'},
     {'author': 'Exit Ready Valuation',
      'channel': 'Exit Ready Valuation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:26](https://www.youtube.com/watch?v=Tt3Ae9PDn8A&t=26s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "But 10% of what? Not the price, the whole project. That's the price  plus "
              'working capital to run the business plus closing.',
      'timestamp': 26,
      'timestamp_label': '[00:00:26]',
      'timestamp_seconds': 26,
      'tip': "But 10% of what? Not the price, the whole project. That's the price  plus "
             'working capital to run the business plus closing.',
      'title': 'How to Buy a Business With an SBA Loan (2026 Rules Explained) (Exit Ready '
               'Valuation)',
      'url': 'https://www.youtube.com/watch?v=Tt3Ae9PDn8A&t=26s',
      'video_id': 'Tt3Ae9PDn8A'},
     {'author': 'Accounting Rescue with Lisa',
      'channel': 'Accounting Rescue with Lisa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:28](https://www.youtube.com/watch?v=t0rj9LcHTgw&t=328s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The business acquired merchandise on credit and still owes a little more to '
              'suppliers at year-end. It paid less cash than its purchases would otherwise '
              'suggest. Under our simplified facts here, we add the $3,000 increase in '
              'accounts payable in the indirect operating section.',
      'timestamp': 328,
      'timestamp_label': '[00:05:28]',
      'timestamp_seconds': 328,
      'tip': 'The business acquired merchandise on credit and still owes a little more to '
             'suppliers at year-end. It paid less cash than its purchases would otherwise '
             'suggest. Under our simplified facts here, we add the $3,000 increase in accounts '
             'payable in the indirect operating section.',
      'title': 'Working Capital Adjustments in the Indirect Method (Add or Subtract?) '
               '(Accounting Rescue with Lisa)',
      'url': 'https://www.youtube.com/watch?v=t0rj9LcHTgw&t=328s',
      'video_id': 't0rj9LcHTgw'},
     {'author': 'Transact Capital',
      'channel': 'Transact Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:10](https://www.youtube.com/watch?v=YAk3dxgnsBU&t=730s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Closing this slide is simply to remind listeners that there are many more '
              'purchase price closing adjustments in addition to the networking Capital '
              'adjustment we may cover those in later videos but they are also important.',
      'timestamp': 730,
      'timestamp_label': '[00:12:10]',
      'timestamp_seconds': 730,
      'tip': 'Closing this slide is simply to remind listeners that there are many more '
             'purchase price closing adjustments in addition to the networking Capital '
             'adjustment we may cover those in later videos but they are also important.',
      'title': 'Investment Banking - How To Calculate Net Working Capital for an M&A '
               'Transaction - Transact Capital (Transact Capital)',
      'url': 'https://www.youtube.com/watch?v=YAk3dxgnsBU&t=730s',
      'video_id': 'YAk3dxgnsBU'},
     {'author': 'Brett Cenkus',
      'channel': 'Brett Cenkus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=aNioqOmfOe4&t=103s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, purchase price How much is the buyer paying? How is the buyer paying that '
              'is it all in cash? Is the seller going to hold a note, carry back some '
              'financing? What exactly is the buyer purchasing? Are they buying the assets of '
              'the business?',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': 'So, purchase price How much is the buyer paying? How is the buyer paying that is '
             'it all in cash? Is the seller going to hold a note, carry back some financing? '
             'What exactly is the buyer purchasing? Are they buying the assets of the '
             'business?',
      'title': 'M&A Letters of Intent: Are They Really Necessary? (Brett Cenkus)',
      'url': 'https://www.youtube.com/watch?v=aNioqOmfOe4&t=103s',
      'video_id': 'aNioqOmfOe4'},
     {'author': 'Break Into Finance',
      'channel': 'Break Into Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:18](https://www.youtube.com/watch?v=S31vo0Umk5M&t=858s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'That dcf ie the cash flow of the business and working capital and as i '
              'mentioned before kind of when you do your dcf.',
      'timestamp': 858,
      'timestamp_label': '[00:14:18]',
      'timestamp_seconds': 858,
      'tip': 'That dcf ie the cash flow of the business and working capital and as i mentioned '
             'before kind of when you do your dcf.',
      'title': 'Net Working Capital Adjustment - M&A Transactions (#5) (Break Into Finance)',
      'url': 'https://www.youtube.com/watch?v=S31vo0Umk5M&t=858s',
      'video_id': 'S31vo0Umk5M'},
     {'author': 'ProjectionHub',
      'channel': 'ProjectionHub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:18](https://www.youtube.com/watch?v=OiLlMiZv9ZQ&t=258s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's say they moved the business moved and now they own the building or maybe "
              "they're in a very long-term lease so that was just a kind of onetime onetime "
              "thing and let's say it cost $25,000 to move we can add that back here as well "
              'we call this you know moving.',
      'timestamp': 258,
      'timestamp_label': '[00:04:18]',
      'timestamp_seconds': 258,
      'tip': "Let's say they moved the business moved and now they own the building or maybe "
             "they're in a very long-term lease so that was just a kind of onetime onetime "
             "thing and let's say it cost $25,000 to move we can add that back here as well we "
             'call this you know moving.',
      'title': 'What are Common EBITDA Add Backs When Calculating SDE (ProjectionHub)',
      'url': 'https://www.youtube.com/watch?v=OiLlMiZv9ZQ&t=258s',
      'video_id': 'OiLlMiZv9ZQ'},
     {'author': 'Walker Deibel',
      'channel': 'Walker Deibel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:21](https://www.youtube.com/watch?v=NM-ZwBNBHQE&t=441s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "20% of the business and you're gonna buy 80% of the company in sort of a "
              'private equity situation there might be a reason in this structure to do a '
              "stock sale. If I'm going to buy a purchase price on assets, it's usually higher "
              'than if you buy it with stock.',
      'timestamp': 441,
      'timestamp_label': '[00:07:21]',
      'timestamp_seconds': 441,
      'tip': "20% of the business and you're gonna buy 80% of the company in sort of a private "
             'equity situation there might be a reason in this structure to do a stock sale. '
             "If I'm going to buy a purchase price on assets, it's usually higher than if you "
             'buy it with stock.',
      'title': 'Asset Sale vs Stock Sale (Walker Deibel)',
      'url': 'https://www.youtube.com/watch?v=NM-ZwBNBHQE&t=441s',
      'video_id': 'NM-ZwBNBHQE'},
     {'author': 'Teach Me! Personal Finance',
      'channel': 'Teach Me! Personal Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:16](https://www.youtube.com/watch?v=G0f0r8tYMnk&t=196s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Social security number under the other party's identifying number and then "
              'address to include city state and zip code data sale so what date do the '
              'closing actually take place on and then the total sales price or consideration.',
      'timestamp': 196,
      'timestamp_label': '[00:03:16]',
      'timestamp_seconds': 196,
      'tip': "Social security number under the other party's identifying number and then "
             'address to include city state and zip code data sale so what date do the closing '
             'actually take place on and then the total sales price or consideration.',
      'title': 'IRS Form 8594 walkthrough (Asset Acquisition Statement under IRC Section 1060) '
               '(Teach Me! Personal Finance)',
      'url': 'https://www.youtube.com/watch?v=G0f0r8tYMnk&t=196s',
      'video_id': 'G0f0r8tYMnk'},
     {'author': 'RareBrain',
      'channel': 'RareBrain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:40](https://www.youtube.com/watch?v=fPwi8HVhX3Q&t=160s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Capital helps companies improve performance and sell for maximum value how '
              "ready is your company to grow or to sell want to know how you're doing get your "
              'free score plus customized report in just a few minutes at no cost or '
              'obligation visit Reverend comm slash score.',
      'timestamp': 160,
      'timestamp_label': '[00:02:40]',
      'timestamp_seconds': 160,
      'tip': 'Capital helps companies improve performance and sell for maximum value how ready '
             "is your company to grow or to sell want to know how you're doing get your free "
             'score plus customized report in just a few minutes at no cost or obligation '
             'visit Reverend comm slash score.',
      'title': 'Working Capital Adjustments in a Business Sale Can Be a Nasty Surprise (S3) '
               '(RareBrain)',
      'url': 'https://www.youtube.com/watch?v=fPwi8HVhX3Q&t=160s',
      'video_id': 'fPwi8HVhX3Q'},
     {'author': 'ProjectionHub',
      'channel': 'ProjectionHub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:06](https://www.youtube.com/watch?v=8Gok1YA-HS8&t=306s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Different timing and price points and you'll be able to see here like your debt "
              'surface coverage ratio here to make sure that the project cash flows if you '
              "have questions about that reach out to us at support projectionhub.com and we'd "
              'be happy to help thanks foreign.',
      'timestamp': 306,
      'timestamp_label': '[00:05:06]',
      'timestamp_seconds': 306,
      'tip': "Different timing and price points and you'll be able to see here like your debt "
             'surface coverage ratio here to make sure that the project cash flows if you have '
             "questions about that reach out to us at support projectionhub.com and we'd be "
             'happy to help thanks foreign.',
      'title': 'SBA Changes to Seller Note Full Standby Rules (BIG improvement!) '
               '(ProjectionHub)',
      'url': 'https://www.youtube.com/watch?v=8Gok1YA-HS8&t=306s',
      'video_id': '8Gok1YA-HS8'},
     {'author': 'Roland Frasier',
      'channel': 'Roland Frasier',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:18](https://www.youtube.com/watch?v=onN8dTJIXAM&t=318s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "They're you know they're not they're not killing it profit margin wise which is "
              "good uh because it means that you're you know you're not uh you're not forced "
              "to keep that um I mean I'd.",
      'timestamp': 318,
      'timestamp_label': '[00:05:18]',
      'timestamp_seconds': 318,
      'tip': "They're you know they're not they're not killing it profit margin wise which is "
             "good uh because it means that you're you know you're not uh you're not forced to "
             "keep that um I mean I'd.",
      'title': "Roland's Earnouts and Seller Financing Secrets 🤯 (Roland Frasier)",
      'url': 'https://www.youtube.com/watch?v=onN8dTJIXAM&t=318s',
      'video_id': 'onN8dTJIXAM'},
     {'author': 'Leveling Up Clips',
      'channel': 'Leveling Up Clips',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:00](https://www.youtube.com/watch?v=zVSWRRAfFO8&t=240s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "About to hit that so we can just like boom 20 and then it's like and you're "
              "you're aligning with them it's like hey if we want to hold forever you're like "
              "hey like if I like you maybe right yeah I'm good on either way.",
      'timestamp': 240,
      'timestamp_label': '[00:04:00]',
      'timestamp_seconds': 240,
      'tip': "About to hit that so we can just like boom 20 and then it's like and you're "
             "you're aligning with them it's like hey if we want to hold forever you're like "
             "hey like if I like you maybe right yeah I'm good on either way.",
      'title': 'How To Start A Business Acquisition Company - With Alex Hormozi (Leveling Up '
               'Clips)',
      'url': 'https://www.youtube.com/watch?v=zVSWRRAfFO8&t=240s',
      'video_id': 'zVSWRRAfFO8'}],
 4: [{'author': 'Acquireman M&A',
      'channel': 'Acquireman M&A',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:07](https://www.youtube.com/watch?v=VBNjS7UATHo&t=67s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, option two, an asset purchase. Instead of buying the company's shares, you "
              'acquire specified assets or business operations directly. For example, you '
              'might purchase its software, brand, customer relationships, equipment, and '
              'selected contracts.',
      'timestamp': 67,
      'timestamp_label': '[00:01:07]',
      'timestamp_seconds': 67,
      'tip': "Now, option two, an asset purchase. Instead of buying the company's shares, you "
             'acquire specified assets or business operations directly. For example, you might '
             'purchase its software, brand, customer relationships, equipment, and selected '
             'contracts.',
      'title': 'What Exactly Are You Buying in an M&A Deal? Share Purchase vs Asset Purchase '
               '#mergersandacquisitions (Acquireman M&A)',
      'url': 'https://www.youtube.com/watch?v=VBNjS7UATHo&t=67s',
      'video_id': 'VBNjS7UATHo'},
     {'author': 'Walker Deibel',
      'channel': 'Walker Deibel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=uY1iPCwJqk8&t=15s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '$100,000 into 50 million through business Acquisitions okay um listen this is '
              "an advanced acquisition strategy uh it's more closer to Capital.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': '$100,000 into 50 million through business Acquisitions okay um listen this is an '
             "advanced acquisition strategy uh it's more closer to Capital.",
      'title': 'Turning $100K into $50 Million Through Business Acquisitions (Walker Deibel)',
      'url': 'https://www.youtube.com/watch?v=uY1iPCwJqk8&t=15s',
      'video_id': 'uY1iPCwJqk8'},
     {'author': 'Lean Stack',
      'channel': 'Lean Stack',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:01](https://www.youtube.com/watch?v=CoNZbm4aVto&t=301s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '80 calls a day, choose Close. Skip HubSpot entirely unless you have raised '
              'venture capital and need enterprise marketing automation from day one. Before '
              'we wrap up, keep these three rules of a lean tech stack in mind. Rule number '
              'one, software pricing is a trap.',
      'timestamp': 301,
      'timestamp_label': '[00:05:01]',
      'timestamp_seconds': 301,
      'tip': '80 calls a day, choose Close. Skip HubSpot entirely unless you have raised '
             'venture capital and need enterprise marketing automation from day one. Before we '
             'wrap up, keep these three rules of a lean tech stack in mind. Rule number one, '
             'software pricing is a trap.',
      'title': 'HubSpot vs Pipedrive vs Close CRM: Stop Overpaying for B2B SaaS (Full Cost '
               'Audit) (Lean Stack)',
      'url': 'https://www.youtube.com/watch?v=CoNZbm4aVto&t=301s',
      'video_id': 'CoNZbm4aVto'},
     {'author': 'Mind Of Monte',
      'channel': 'Mind Of Monte',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:38](https://www.youtube.com/watch?v=MVmF4HlTHGM&t=218s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So I want to put in everyone's mind that there is a real world where you could "
              'find a business to acquire that will allow your business to grow very quickly '
              'and add a ad revenue literally instantly.',
      'timestamp': 218,
      'timestamp_label': '[00:03:38]',
      'timestamp_seconds': 218,
      'tip': "So I want to put in everyone's mind that there is a real world where you could "
             'find a business to acquire that will allow your business to grow very quickly '
             'and add a ad revenue literally instantly.',
      'title': 'How to Buy Boomer Business With No Competition (Mind Of Monte)',
      'url': 'https://www.youtube.com/watch?v=MVmF4HlTHGM&t=218s',
      'video_id': 'MVmF4HlTHGM'},
     {'author': 'Technically News',
      'channel': 'Technically News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:07](https://www.youtube.com/watch?v=nOnsMlkLh10&t=907s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Focusing on one specific industry like like um like pet care or or an insurance '
              'brokerage business you can get you can buy lists of those companies and do a.',
      'timestamp': 907,
      'timestamp_label': '[00:15:07]',
      'timestamp_seconds': 907,
      'tip': 'Focusing on one specific industry like like um like pet care or or an insurance '
             'brokerage business you can get you can buy lists of those companies and do a.',
      'title': 'Entrepreneurship through acquisition: How to buy a business (Technically News)',
      'url': 'https://www.youtube.com/watch?v=nOnsMlkLh10&t=907s',
      'video_id': 'nOnsMlkLh10'},
     {'author': 'Start Up University',
      'channel': 'Start Up University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:09](https://www.youtube.com/watch?v=pTSIi3Y4_TA&t=309s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s been a great opportunity and I've seen some significant success going after "
              'and working with boomer business owners who are at or near retirement. Hey, do '
              "you like what you hear? If so, I'd love to introduce you to my course called "
              'Startup University.',
      'timestamp': 309,
      'timestamp_label': '[00:05:09]',
      'timestamp_seconds': 309,
      'tip': "'s been a great opportunity and I've seen some significant success going after "
             'and working with boomer business owners who are at or near retirement. Hey, do '
             "you like what you hear? If so, I'd love to introduce you to my course called "
             'Startup University.',
      'title': 'Boomers Are Selling — How You Can Buy a Great Business with Little Cash Down '
               '(Start Up University)',
      'url': 'https://www.youtube.com/watch?v=pTSIi3Y4_TA&t=309s',
      'video_id': 'pTSIi3Y4_TA'},
     {'author': 'Beau Eckstein, Business Ownership Coach',
      'channel': 'Beau Eckstein, Business Ownership Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:54](https://www.youtube.com/watch?v=1-sviMTVjUs&t=414s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re going to continue to see a strong year in SBA financing. So, if you're "
              'interested in business acquisition, franchise startup, these are all eligible '
              'for SBA financing. So, anyway, if you have any questions on SBA financing, you '
              'can go to bookwithboe.',
      'timestamp': 414,
      'timestamp_label': '[00:06:54]',
      'timestamp_seconds': 414,
      'tip': "'re going to continue to see a strong year in SBA financing. So, if you're "
             'interested in business acquisition, franchise startup, these are all eligible '
             'for SBA financing. So, anyway, if you have any questions on SBA financing, you '
             'can go to bookwithboe.',
      'title': 'How to Buy a Business with SBA 7a or Seller Finance (Beau Eckstein, Business '
               'Ownership Coach)',
      'url': 'https://www.youtube.com/watch?v=1-sviMTVjUs&t=414s',
      'video_id': '1-sviMTVjUs'},
     {'author': 'acquiredotcom',
      'channel': 'acquiredotcom',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:37:01](https://www.youtube.com/watch?v=nu3zh5FOFME&t=2221s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Technical and you're looking at all these businesses I'm not technical at all "
              'either and it is really hard for me to run this business and not want to '
              "acquire a startup I'll show you one business that that actually gets me kind of "
              'excited.',
      'timestamp': 2221,
      'timestamp_label': '[00:37:01]',
      'timestamp_seconds': 2221,
      'tip': "Technical and you're looking at all these businesses I'm not technical at all "
             'either and it is really hard for me to run this business and not want to acquire '
             "a startup I'll show you one business that that actually gets me kind of excited.",
      'title': 'An Acquire com Guide to Buying the Best Startups with Andrew Gazdecki '
               '(acquiredotcom)',
      'url': 'https://www.youtube.com/watch?v=nu3zh5FOFME&t=2221s',
      'video_id': 'nu3zh5FOFME'},
     {'author': 'ToolColumn',
      'channel': 'ToolColumn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:04](https://www.youtube.com/watch?v=W6A4gRp6eow&t=184s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Use the budget variant when Apollo, HubSpot, and Smartle are enough. Add clay '
              'and deeper N8 in logic only when enrichment depth becomes a repeatable '
              'constraint. Do not use this stack when nobody owns rev ops.',
      'timestamp': 184,
      'timestamp_label': '[00:03:04]',
      'timestamp_seconds': 184,
      'tip': 'Use the budget variant when Apollo, HubSpot, and Smartle are enough. Add clay '
             'and deeper N8 in logic only when enrichment depth becomes a repeatable '
             'constraint. Do not use this stack when nobody owns rev ops.',
      'title': 'HubSpot + Apollo + Clay + Smartlead: The Outbound Stack Boundary (ToolColumn)',
      'url': 'https://www.youtube.com/watch?v=W6A4gRp6eow&t=184s',
      'video_id': 'W6A4gRp6eow'},
     {'author': 'Walker Deibel',
      'channel': 'Walker Deibel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:15](https://www.youtube.com/watch?v=LlIJ71_IXbs&t=1275s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Acquiring uniform printing a 43 million dollar printer specialty insurance '
              "documents jim served as the company's ceo and chairman for 10 years investor "
              "returns under jim's tenure as ceo were 24 times the acquisition capital.",
      'timestamp': 1275,
      'timestamp_label': '[00:21:15]',
      'timestamp_seconds': 1275,
      'tip': 'Acquiring uniform printing a 43 million dollar printer specialty insurance '
             "documents jim served as the company's ceo and chairman for 10 years investor "
             "returns under jim's tenure as ceo were 24 times the acquisition capital.",
      'title': 'MIT Entrepreneurship Through Acquisition Conference Keynote by Walker Deibel '
               'of Buy Then Build (Walker Deibel)',
      'url': 'https://www.youtube.com/watch?v=LlIJ71_IXbs&t=1275s',
      'video_id': 'LlIJ71_IXbs'},
     {'author': 'The Wall Street Skinny',
      'channel': 'The Wall Street Skinny',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:47:44](https://www.youtube.com/watch?v=MpeYmBDptXs&t=2864s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The that I teach in Emin like this I mean literally was working on these slides '
              "yesterday so I'm like this is exciting yeah so uh Oriana Capital LLC.",
      'timestamp': 2864,
      'timestamp_label': '[00:47:44]',
      'timestamp_seconds': 2864,
      'tip': 'The that I teach in Emin like this I mean literally was working on these slides '
             "yesterday so I'm like this is exciting yeah so uh Oriana Capital LLC.",
      'title': 'Entrepreneurship Through Acquisition 101 (The Wall Street Skinny)',
      'url': 'https://www.youtube.com/watch?v=MpeYmBDptXs&t=2864s',
      'video_id': 'MpeYmBDptXs'},
     {'author': 'McGuireWoods LLP',
      'channel': 'McGuireWoods LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:35](https://www.youtube.com/watch?v=OzPzqbUSgPw&t=935s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And then typically we've got, you know, in both deal structures, we have an "
              "indemnity structure, but um there's no excluded liability concept where the "
              'pre-closing liabilities in like in an asset deal remain with the seller.',
      'timestamp': 935,
      'timestamp_label': '[00:15:35]',
      'timestamp_seconds': 935,
      'tip': "And then typically we've got, you know, in both deal structures, we have an "
             "indemnity structure, but um there's no excluded liability concept where the "
             'pre-closing liabilities in like in an asset deal remain with the seller.',
      'title': 'Deal-by-Deal: Ep. 12 - How to Craft an M&A Letter of Intent with Greg Hawver '
               'and Jeff Brooker (Pt 1) (McGuireWoods LLP)',
      'url': 'https://www.youtube.com/watch?v=OzPzqbUSgPw&t=935s',
      'video_id': 'OzPzqbUSgPw'},
     {'author': 'Brett Cenkus',
      'channel': 'Brett Cenkus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:36](https://www.youtube.com/watch?v=cnvG-qb6w9Q&t=756s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '\'t have material adverse effect on the business". So it\'s like look I mean '
              "there might be some little stuff. We- there's always a representation or almost "
              "always that the business is qualified as a foreign entity- it's a weird word. "
              'It means like an out-of-state entity.',
      'timestamp': 756,
      'timestamp_label': '[00:12:36]',
      'timestamp_seconds': 756,
      'tip': '\'t have material adverse effect on the business". So it\'s like look I mean '
             "there might be some little stuff. We- there's always a representation or almost "
             "always that the business is qualified as a foreign entity- it's a weird word. It "
             'means like an out-of-state entity.',
      'title': 'Representations and Warranties in Mergers and Acquisitions (M&A) (Brett '
               'Cenkus)',
      'url': 'https://www.youtube.com/watch?v=cnvG-qb6w9Q&t=756s',
      'video_id': 'cnvG-qb6w9Q'},
     {'author': 'Keira Hamilton',
      'channel': 'Keira Hamilton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=7RAyVC1b9Pg&t=78s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Structure I see lenders most likely to use this structure for borrowers who are '
              'really experienced so for example someone who is buying the company that.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'Structure I see lenders most likely to use this structure for borrowers who are '
             'really experienced so for example someone who is buying the company that.',
      'title': 'How to Use a Seller Note with an SBA Loan 2024 (Keira Hamilton)',
      'url': 'https://www.youtube.com/watch?v=7RAyVC1b9Pg&t=78s',
      'video_id': '7RAyVC1b9Pg'},
     {'author': 'SBA University',
      'channel': 'SBA University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=s5o1MBGuspY&t=21s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'That they will help stay involved post sale in this lesson we will Deep dive '
              "into everything you need to know about a seller's note how it works your "
              'options with it and why I think it kind of benefits every party.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'That they will help stay involved post sale in this lesson we will Deep dive '
             "into everything you need to know about a seller's note how it works your options "
             'with it and why I think it kind of benefits every party.',
      'title': 'Seller Notes in Business Acquisitions (BEGINNERS Guide for 2025) | SBA Loans '
               '(SBA University)',
      'url': 'https://www.youtube.com/watch?v=s5o1MBGuspY&t=21s',
      'video_id': 's5o1MBGuspY'}],
 5: [{'author': 'HBS Rock Center for Entrepreneurship',
      'channel': 'HBS Rock Center for Entrepreneurship',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:22](https://www.youtube.com/watch?v=oJcm3Bn-lXE&t=682s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Rick Ruback: higher risks, higher woods, but you may you you can control the '
              'risk a little bit by the business you buy.',
      'timestamp': 682,
      'timestamp_label': '[00:11:22]',
      'timestamp_seconds': 682,
      'tip': 'Rick Ruback: higher risks, higher woods, but you may you you can control the '
             'risk a little bit by the business you buy.',
      'title': 'Search to Success: Entrepreneurship Through Acquisition (HBS Rock Center for '
               'Entrepreneurship)',
      'url': 'https://www.youtube.com/watch?v=oJcm3Bn-lXE&t=682s',
      'video_id': 'oJcm3Bn-lXE'},
     {'author': 'Dominik Höhener',
      'channel': 'Dominik Höhener',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=ybzODlrITiw&t=146s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you buy an existing business that already has customers, cash flow, and so '
              'on and so forth, you have definitely way lower risk than starting something '
              "from scratch. In general, the business you're buying is most likely already "
              'working.',
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': 'If you buy an existing business that already has customers, cash flow, and so on '
             'and so forth, you have definitely way lower risk than starting something from '
             "scratch. In general, the business you're buying is most likely already working.",
      'title': 'How to Get Into Entrepreneurship Through Acquisition (ETA) (Dominik Höhener)',
      'url': 'https://www.youtube.com/watch?v=ybzODlrITiw&t=146s',
      'video_id': 'ybzODlrITiw'},
     {'author': 'acquiredotcom',
      'channel': 'acquiredotcom',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:14](https://www.youtube.com/watch?v=3Cgn92T6L1Y&t=194s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ensure that you get the most out of your acquisition you minimize your risk and '
              'the business that you buy is a complete success postacquisition.',
      'timestamp': 194,
      'timestamp_label': '[00:03:14]',
      'timestamp_seconds': 194,
      'tip': 'Ensure that you get the most out of your acquisition you minimize your risk and '
             'the business that you buy is a complete success postacquisition.',
      'title': 'Structuring your deal for success (acquiredotcom)',
      'url': 'https://www.youtube.com/watch?v=3Cgn92T6L1Y&t=194s',
      'video_id': '3Cgn92T6L1Y'},
     {'author': 'THE M&A DESK',
      'channel': 'THE M&A DESK',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=MvN2Q7SWbgY&t=32s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Deals fall apart at predictable points for predictable reasons. And if you know '
              "what's coming, you can avoid the mistakes that kill most sale processes before "
              "they ever reach a closing table. Here's exactly what happens stage by stage "
              'when a business actually gets sold.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': 'Deals fall apart at predictable points for predictable reasons. And if you know '
             "what's coming, you can avoid the mistakes that kill most sale processes before "
             "they ever reach a closing table. Here's exactly what happens stage by stage when "
             'a business actually gets sold.',
      'title': 'How to Sell Your Business: The 8-Stage M&A Process Explained (THE M&A DESK)',
      'url': 'https://www.youtube.com/watch?v=MvN2Q7SWbgY&t=32s',
      'video_id': 'MvN2Q7SWbgY'},
     {'author': 'Darius Mirshahzadeh',
      'channel': 'Darius Mirshahzadeh',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:17](https://www.youtube.com/watch?v=AKE-710SdA4&t=1757s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s sort of like, [clears throat] you know, I mean, when you look at the "
              "textbook of like how do you reduce risk, it's always diversification and the "
              "problem is is that when you look at how people make a lot of money, it's always "
              'concentration. So, like this balance, right?',
      'timestamp': 1757,
      'timestamp_label': '[00:29:17]',
      'timestamp_seconds': 1757,
      'tip': "'s sort of like, [clears throat] you know, I mean, when you look at the textbook "
             "of like how do you reduce risk, it's always diversification and the problem is "
             "is that when you look at how people make a lot of money, it's always "
             'concentration. So, like this balance, right?',
      'title': 'Walker Deibel | Buy Then Build: How Acquisition Entrepreneurs Outsmart the '
               'Startup Game (Darius Mirshahzadeh)',
      'url': 'https://www.youtube.com/watch?v=AKE-710SdA4&t=1757s',
      'video_id': 'AKE-710SdA4'},
     {'author': 'David C Barnett Small Business and Deal Making SMB',
      'channel': 'David C Barnett Small Business and Deal Making SMB',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=gFJZwK-3sq0&t=20s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Barnett and you're tuned in to Small Business and Dealm, the podcast, YouTube "
              'channel, and blog, where I talk about buying, selling, financing, and managing '
              'small and medium-sized businesses while controlling risk.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Barnett and you're tuned in to Small Business and Dealm, the podcast, YouTube "
             'channel, and blog, where I talk about buying, selling, financing, and managing '
             'small and medium-sized businesses while controlling risk.',
      'title': 'Working Capital Adjustments on Closing (David C Barnett Small Business and '
               'Deal Making SMB)',
      'url': 'https://www.youtube.com/watch?v=gFJZwK-3sq0&t=20s',
      'video_id': 'gFJZwK-3sq0'},
     {'author': 'Acquira',
      'channel': 'Acquira',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:55](https://www.youtube.com/watch?v=g_fy5eeJpHE&t=1255s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "It's important in every deal of every size because that's real dollars. I "
              'always tell people, listen, if I tell you the working capital is 1. 3, you can '
              'go out and buy that business for 800K in working capital with 800K, sorry.',
      'timestamp': 1255,
      'timestamp_label': '[00:20:55]',
      'timestamp_seconds': 1255,
      'tip': "It's important in every deal of every size because that's real dollars. I always "
             'tell people, listen, if I tell you the working capital is 1. 3, you can go out '
             'and buy that business for 800K in working capital with 800K, sorry.',
      'title': 'Quality of Earnings Explained: Financial Due Diligence Mistakes That Kill '
               'Deals (Acquira)',
      'url': 'https://www.youtube.com/watch?v=g_fy5eeJpHE&t=1255s',
      'video_id': 'g_fy5eeJpHE'},
     {'author': 'Lockaby PLLC',
      'channel': 'Lockaby PLLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:32](https://www.youtube.com/watch?v=NCbzskaBTdQ&t=392s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'t mean that working capital isn't going to be a proper adjustment at closing. "
              "So, again, let's deal with working capital in the letter of intent and let's "
              'make sure those conversations are held early with every seller.',
      'timestamp': 392,
      'timestamp_label': '[00:06:32]',
      'timestamp_seconds': 392,
      'tip': "'t mean that working capital isn't going to be a proper adjustment at closing. "
             "So, again, let's deal with working capital in the letter of intent and let's "
             'make sure those conversations are held early with every seller.',
      'title': 'The Anatomy of an LOI (Lockaby PLLC)',
      'url': 'https://www.youtube.com/watch?v=NCbzskaBTdQ&t=392s',
      'video_id': 'NCbzskaBTdQ'},
     {'author': 'Bootstrapping to Billions',
      'channel': 'Bootstrapping to Billions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:52](https://www.youtube.com/watch?v=BDlt56r8cRk&t=712s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Way to hedge your your risks right mitigate risk early and often by doing this '
              'very very well and intentionally and then again those contingencies you.',
      'timestamp': 712,
      'timestamp_label': '[00:11:52]',
      'timestamp_seconds': 712,
      'tip': 'Way to hedge your your risks right mitigate risk early and often by doing this '
             'very very well and intentionally and then again those contingencies you.',
      'title': 'How a Letter of Intent (LOI) works when buying a business (Bootstrapping to '
               'Billions)',
      'url': 'https://www.youtube.com/watch?v=BDlt56r8cRk&t=712s',
      'video_id': 'BDlt56r8cRk'},
     {'author': 'Strategy Leaders Inc.',
      'channel': 'Strategy Leaders Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:49](https://www.youtube.com/watch?v=OeJwN9bz5dE&t=169s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And a big part of that success is knowing how to lead through moments of change '
              "like acquisitions. We're grounded in research, but we live in the real world, "
              'building, buying, coaching, and advising companies just like yours. Bad B '
              'Marketing is the CMO arm of that legacy.',
      'timestamp': 169,
      'timestamp_label': '[00:02:49]',
      'timestamp_seconds': 169,
      'tip': 'And a big part of that success is knowing how to lead through moments of change '
             "like acquisitions. We're grounded in research, but we live in the real world, "
             'building, buying, coaching, and advising companies just like yours. Bad B '
             'Marketing is the CMO arm of that legacy.',
      'title': 'What to Do After an Acquisition: A No-BS Marketing Playbook (Strategy Leaders '
               'Inc.)',
      'url': 'https://www.youtube.com/watch?v=OeJwN9bz5dE&t=169s',
      'video_id': 'OeJwN9bz5dE'},
     {'author': 'Jon Stoddard',
      'channel': 'Jon Stoddard',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:01](https://www.youtube.com/watch?v=Yr06Fv79PU0&t=121s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Position where every business we represent you could buy not do any due '
              'diligence and the business would be as.',
      'timestamp': 121,
      'timestamp_label': '[00:02:01]',
      'timestamp_seconds': 121,
      'tip': 'Position where every business we represent you could buy not do any due '
             'diligence and the business would be as.',
      'title': 'Due Diligence,  Quality of Earnings and Why Deals Fail (Jon Stoddard)',
      'url': 'https://www.youtube.com/watch?v=Yr06Fv79PU0&t=121s',
      'video_id': 'Yr06Fv79PU0'},
     {'author': 'Built to Sell',
      'channel': 'Built to Sell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:02](https://www.youtube.com/watch?v=NBxRy2fAY-s&t=302s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You're supposed to be doing well and how to build a scalable business that can "
              'be sold building a business that can be sold is much different than building a '
              'profitable business that relies on you and you are the bottleneck inside your '
              'entire company.',
      'timestamp': 302,
      'timestamp_label': '[00:05:02]',
      'timestamp_seconds': 302,
      'tip': "You're supposed to be doing well and how to build a scalable business that can "
             'be sold building a business that can be sold is much different than building a '
             'profitable business that relies on you and you are the bottleneck inside your '
             'entire company.',
      'title': 'How to Negotiate Your Letter of Intent (LOI) When Selling Your Business (Built '
               'to Sell)',
      'url': 'https://www.youtube.com/watch?v=NBxRy2fAY-s&t=302s',
      'video_id': 'NBxRy2fAY-s'},
     {'author': 'Walker Deibel',
      'channel': 'Walker Deibel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:18](https://www.youtube.com/watch?v=SXwOv9QUWws&t=498s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And I and I learned a lot of lessons from it. And I do think that there are '
              'proper ways to sort of engineer success in that model. The thing that I really '
              'preach when people want to get into acquisition entrepreneurship is like do '
              'guys buy one focus on one.',
      'timestamp': 498,
      'timestamp_label': '[00:08:18]',
      'timestamp_seconds': 498,
      'tip': 'And I and I learned a lot of lessons from it. And I do think that there are '
             'proper ways to sort of engineer success in that model. The thing that I really '
             'preach when people want to get into acquisition entrepreneurship is like do guys '
             'buy one focus on one.',
      'title': 'Making Billions Buying Businesses: A Masterclass (Walker Deibel)',
      'url': 'https://www.youtube.com/watch?v=SXwOv9QUWws&t=498s',
      'video_id': 'SXwOv9QUWws'},
     {'author': 'FinanceKid',
      'channel': 'FinanceKid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:56](https://www.youtube.com/watch?v=JSIfjvnhOco&t=356s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Defined in the offer now another mistake and and this is one for buyers in '
              "particular is often times firsttime sellers don't really understand the m&a "
              'stuff so our recommendation is that you always try to overcommunication.',
      'timestamp': 356,
      'timestamp_label': '[00:05:56]',
      'timestamp_seconds': 356,
      'tip': 'Defined in the offer now another mistake and and this is one for buyers in '
             "particular is often times firsttime sellers don't really understand the m&a "
             'stuff so our recommendation is that you always try to overcommunication.',
      'title': 'Mastering the Letter of Intent (LOI) in M&A: Best Practices & Common Mistakes '
               '(FinanceKid)',
      'url': 'https://www.youtube.com/watch?v=JSIfjvnhOco&t=356s',
      'video_id': 'JSIfjvnhOco'},
     {'author': 'Beau Eckstein, Business Ownership Coach',
      'channel': 'Beau Eckstein, Business Ownership Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:00](https://www.youtube.com/watch?v=4Pg78F28qCM&t=180s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Channel we talk all things financing I've been in the lending industry for over "
              "20 years and I'm happy to answer your questions and provide great content.",
      'timestamp': 180,
      'timestamp_label': '[00:03:00]',
      'timestamp_seconds': 180,
      'tip': "Channel we talk all things financing I've been in the lending industry for over "
             "20 years and I'm happy to answer your questions and provide great content.",
      'title': 'What Really Happens When You Sign a Letter of Intent to Buy a Business? (Beau '
               'Eckstein, Business Ownership Coach)',
      'url': 'https://www.youtube.com/watch?v=4Pg78F28qCM&t=180s',
      'video_id': '4Pg78F28qCM'}],
 6: [{'author': 'Joel Ankney',
      'channel': 'Joel Ankney',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:32:36](https://www.youtube.com/watch?v=cl31TiHq92Y&t=1956s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'t need to read my book until you get close to a deal. The other two books are, "
              '“Buy Then Build” and the “Harvard Business Review: Buying a Small Business. '
              "They're kind of like the Bibles of this ETA movement from a business "
              'perspective.',
      'timestamp': 1956,
      'timestamp_label': '[00:32:36]',
      'timestamp_seconds': 1956,
      'tip': "'t need to read my book until you get close to a deal. The other two books are, "
             '“Buy Then Build” and the “Harvard Business Review: Buying a Small Business. '
             "They're kind of like the Bibles of this ETA movement from a business "
             'perspective.',
      'title': 'ETA - Entrepreneurship Through Acquisition Introduction | William & Mary '
               'Entrepreneurship Hub (Joel Ankney)',
      'url': 'https://www.youtube.com/watch?v=cl31TiHq92Y&t=1956s',
      'video_id': 'cl31TiHq92Y'},
     {'author': 'Newton Campos',
      'channel': 'Newton Campos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:42](https://www.youtube.com/watch?v=LOtte4Lq1OY&t=402s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Investors for you to search search for a company to acquire for you to manage '
              'after you find this company you raise another amount of capital much bigger '
              'than that usually you raise from five to 20 million dollars to which we call '
              'acquisition Capital acquisition capital.',
      'timestamp': 402,
      'timestamp_label': '[00:06:42]',
      'timestamp_seconds': 402,
      'tip': 'Investors for you to search search for a company to acquire for you to manage '
             'after you find this company you raise another amount of capital much bigger than '
             'that usually you raise from five to 20 million dollars to which we call '
             'acquisition Capital acquisition capital.',
      'title': 'Dr. Newton Campos crash Course on Entrepreneurship through Acquisition - '
               'Understanding Search Funds (Newton Campos)',
      'url': 'https://www.youtube.com/watch?v=LOtte4Lq1OY&t=402s',
      'video_id': 'LOtte4Lq1OY'},
     {'author': 'Marco Palmero',
      'channel': 'Marco Palmero',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:26](https://www.youtube.com/watch?v=6qKxeAkc2YY&t=86s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And compared to their first acquisition, that was a huge downside because '
              'before, you know, buying the first facility, they basically had all their time '
              'available to find that deal.',
      'timestamp': 86,
      'timestamp_label': '[00:01:26]',
      'timestamp_seconds': 86,
      'tip': 'And compared to their first acquisition, that was a huge downside because '
             'before, you know, buying the first facility, they basically had all their time '
             'available to find that deal.',
      'title': 'Roll-Up Buyer Case Study: Deal Origination System Built in 4 Weeks (Marco '
               'Palmero)',
      'url': 'https://www.youtube.com/watch?v=6qKxeAkc2YY&t=86s',
      'video_id': '6qKxeAkc2YY'},
     {'author': 'Before You Buy or Sell a Business Podcast',
      'channel': 'Before You Buy or Sell a Business Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:47](https://www.youtube.com/watch?v=pqmsev-3MPY&t=767s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And then comparing it directly to the business that they want to buy. When '
              'people do that, many times they can find that their experience actually does '
              "correlate directly to the business they're buying. So, we'd like to see at a "
              "minimum that they've managed people.",
      'timestamp': 767,
      'timestamp_label': '[00:12:47]',
      'timestamp_seconds': 767,
      'tip': 'And then comparing it directly to the business that they want to buy. When '
             'people do that, many times they can find that their experience actually does '
             "correlate directly to the business they're buying. So, we'd like to see at a "
             "minimum that they've managed people.",
      'title': 'ETA Reality Check: SBA Lending, Buyer Mistakes, Deal Killers, and the Truth '
               'About Buying a Business (Before You Buy or Sell a Business Podcast)',
      'url': 'https://www.youtube.com/watch?v=pqmsev-3MPY&t=767s',
      'video_id': 'pqmsev-3MPY'},
     {'author': 'McGuireWoods LLP',
      'channel': 'McGuireWoods LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=_sFK2HgcBFo&t=21s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Hello and welcome back to Dealby Deal, a podcast for independent sponsors and '
              "other investors in the middle market. I'm a partner at Magguire Woods. And "
              "today, I'm happy to be diving into the first 100 days postacquisition. This is "
              'after a sponsor has acquired a company.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'Hello and welcome back to Dealby Deal, a podcast for independent sponsors and '
             "other investors in the middle market. I'm a partner at Magguire Woods. And "
             "today, I'm happy to be diving into the first 100 days postacquisition. This is "
             'after a sponsor has acquired a company.',
      'title': 'The First 100 Days: Practical Guidance for PE Investors Post-Acquisition '
               '(McGuireWoods LLP)',
      'url': 'https://www.youtube.com/watch?v=_sFK2HgcBFo&t=21s',
      'video_id': '_sFK2HgcBFo'},
     {'author': 'UWContinuingEd',
      'channel': 'UWContinuingEd',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:39:56](https://www.youtube.com/watch?v=c0fXb_wXv7A&t=2396s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So the first one, really for the panel generally is, what would be a good '
              'starting point for search? How do we find businesses that are ready to be sold? '
              'Nikita, do you want me to give a general answer, and maybe, I don’t know, you '
              'could add, you guys can add some specifics?',
      'timestamp': 2396,
      'timestamp_label': '[00:39:56]',
      'timestamp_seconds': 2396,
      'tip': 'So the first one, really for the panel generally is, what would be a good '
             'starting point for search? How do we find businesses that are ready to be sold? '
             'Nikita, do you want me to give a general answer, and maybe, I don’t know, you '
             'could add, you guys can add some specifics?',
      'title': 'Expert Insights: Exploring Entrepreneurship Through Acquisition '
               '(UWContinuingEd)',
      'url': 'https://www.youtube.com/watch?v=c0fXb_wXv7A&t=2396s',
      'video_id': 'c0fXb_wXv7A'},
     {'author': 'Loan To Launch',
      'channel': 'Loan To Launch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:35](https://www.youtube.com/watch?v=OSZgayF9jHw&t=155s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Of view, this makes the deal less risky. Let's say you're buying a business for "
              "a million dollars. Normally, you'd need $100,000 down.",
      'timestamp': 155,
      'timestamp_label': '[00:02:35]',
      'timestamp_seconds': 155,
      'tip': "Of view, this makes the deal less risky. Let's say you're buying a business for "
             "a million dollars. Normally, you'd need $100,000 down.",
      'title': 'Seller Notes with SBA Loans Explained — The 2025 Rules You Can’t Ignore! (Loan '
               'To Launch)',
      'url': 'https://www.youtube.com/watch?v=OSZgayF9jHw&t=155s',
      'video_id': 'OSZgayF9jHw'},
     {'author': 'PRIME exits M&A Advisory',
      'channel': 'PRIME exits M&A Advisory',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:29](https://www.youtube.com/watch?v=32xGWYMqfWk&t=29s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So why is the LOI more than just a formality? First off, it sets the tone for '
              'your entire deal. Get it right and you build serious momentum. Get it wrong and '
              'you might find yourself in endless renegotiations or even watching your deal '
              'fall apart after months of hard work.',
      'timestamp': 29,
      'timestamp_label': '[00:00:29]',
      'timestamp_seconds': 29,
      'tip': 'So why is the LOI more than just a formality? First off, it sets the tone for '
             'your entire deal. Get it right and you build serious momentum. Get it wrong and '
             'you might find yourself in endless renegotiations or even watching your deal '
             'fall apart after months of hard work.',
      'title': 'How to Write a Strong M&A Letter of Intent (LOI) | PRIME exits (PRIME exits '
               'M&A Advisory)',
      'url': 'https://www.youtube.com/watch?v=32xGWYMqfWk&t=29s',
      'video_id': '32xGWYMqfWk'},
     {'author': 'VCPete',
      'channel': 'VCPete',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=i_Ownd9smbk&t=22s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And the idea was there was a professor that had a couple students that wanted '
              'to buy a business and so he gave them some money to go and find a company, buy '
              'it and run it. And then ultimately they sold it and he generated this great '
              'return.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'And the idea was there was a professor that had a couple students that wanted to '
             'buy a business and so he gave them some money to go and find a company, buy it '
             'and run it. And then ultimately they sold it and he generated this great return.',
      'title': 'How to Start a Search Fund from Nothing! | Funding with Peter Harris (VCPete)',
      'url': 'https://www.youtube.com/watch?v=i_Ownd9smbk&t=22s',
      'video_id': 'i_Ownd9smbk'},
     {'author': 'Oberman Law Firm',
      'channel': 'Oberman Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:35](https://www.youtube.com/watch?v=2RBitaEo6mY&t=95s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So first, on on my side of the fence, we deal with probably a hundred and some '
              'odd transactions a year for buying and selling businesses. To me, the letter of '
              'intent is probably the most one of the most important provisions, right?',
      'timestamp': 95,
      'timestamp_label': '[00:01:35]',
      'timestamp_seconds': 95,
      'tip': 'So first, on on my side of the fence, we deal with probably a hundred and some '
             'odd transactions a year for buying and selling businesses. To me, the letter of '
             'intent is probably the most one of the most important provisions, right?',
      'title': 'Why a Letter of Intent Is Critical to the Sale of a Business (Oberman Law '
               'Firm)',
      'url': 'https://www.youtube.com/watch?v=2RBitaEo6mY&t=95s',
      'video_id': '2RBitaEo6mY'},
     {'author': 'Middle Market Smart',
      'channel': 'Middle Market Smart',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=9fvL0IINg6k&t=21s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "This part I don't know which part is better, part one or part two, because now "
              "we're into the first 100 days post-deal. We're really getting into the nuts and "
              'bolts of the integration, about systems, certainly people, and everything else.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "This part I don't know which part is better, part one or part two, because now "
             "we're into the first 100 days post-deal. We're really getting into the nuts and "
             'bolts of the integration, about systems, certainly people, and everything else.',
      'title': 'Middle Market Smart – Episode 3 (Part 2 of 2) The M&A Playbook for Middle '
               'Market Leaders (Middle Market Smart)',
      'url': 'https://www.youtube.com/watch?v=9fvL0IINg6k&t=21s',
      'video_id': '9fvL0IINg6k'},
     {'author': 'Jason Paul Rogers',
      'channel': 'Jason Paul Rogers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:48](https://www.youtube.com/watch?v=7w05y7xLcNI&t=228s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Million dollars in sales with this client in the first six months post close '
              "then you're going to get an extra hundred thousand dollars.",
      'timestamp': 228,
      'timestamp_label': '[00:03:48]',
      'timestamp_seconds': 228,
      'tip': 'Million dollars in sales with this client in the first six months post close '
             "then you're going to get an extra hundred thousand dollars.",
      'title': 'Structure your first "M&A EARN-OUT" - without all the legal fees (here\'s '
               'how...) (Jason Paul Rogers)',
      'url': 'https://www.youtube.com/watch?v=7w05y7xLcNI&t=228s',
      'video_id': '7w05y7xLcNI'},
     {'author': 'XPX - Exit Planning Exchange',
      'channel': 'XPX - Exit Planning Exchange',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=gRV7segOzzo&t=15s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'In buy side or sell side regions is it because i can list all the all the '
              "disasters i've found.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'In buy side or sell side regions is it because i can list all the all the '
             "disasters i've found.",
      'title': 'Behind the Numbers: Quality of Earnings in a Transaction (XPX - Exit Planning '
               'Exchange)',
      'url': 'https://www.youtube.com/watch?v=gRV7segOzzo&t=15s',
      'video_id': 'gRV7segOzzo'},
     {'author': 'POWERS Pod',
      'channel': 'POWERS Pod',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:20](https://www.youtube.com/watch?v=AWJaRrNXru8&t=200s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Opportunities like that where there's a fragmented base of businesses within an "
              'industry that have those characteristics and then we developed a contact list '
              'and start doing the outreach.',
      'timestamp': 200,
      'timestamp_label': '[00:03:20]',
      'timestamp_seconds': 200,
      'tip': "Opportunities like that where there's a fragmented base of businesses within an "
             'industry that have those characteristics and then we developed a contact list '
             'and start doing the outreach.',
      'title': 'Tim Ludwig on What Industries Excite him as a Search Fund (POWERS Pod)',
      'url': 'https://www.youtube.com/watch?v=AWJaRrNXru8&t=200s',
      'video_id': 'AWJaRrNXru8'},
     {'author': 'KreischerMiller',
      'channel': 'KreischerMiller',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:45](https://www.youtube.com/watch?v=Q6exObbgCgk&t=225s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Seen a couple of times but it has come up where a seller said look we're going "
              'to insist on the ability to entertain another offer as long as it came in on an '
              'unsolicited basis and it was a higher offer than your offer.',
      'timestamp': 225,
      'timestamp_label': '[00:03:45]',
      'timestamp_seconds': 225,
      'tip': "Seen a couple of times but it has come up where a seller said look we're going "
             'to insist on the ability to entertain another offer as long as it came in on an '
             'unsolicited basis and it was a higher offer than your offer.',
      'title': 'The M&A Term Sheet or LOI (KreischerMiller)',
      'url': 'https://www.youtube.com/watch?v=Q6exObbgCgk&t=225s',
      'video_id': 'Q6exObbgCgk'}],
 7: [{'author': 'Codie Sanchez',
      'channel': 'Codie Sanchez',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:34:52](https://www.youtube.com/watch?v=3mtS8rOAqoM&t=2092s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'He used Biscout to dive into this business and started tracking every single '
              'one of his steps of where he was at in the business buying process. He realized '
              'that it would take him in this case about 3 months to close a deal.',
      'timestamp': 2092,
      'timestamp_label': '[00:34:52]',
      'timestamp_seconds': 2092,
      'tip': 'He used Biscout to dive into this business and started tracking every single one '
             'of his steps of where he was at in the business buying process. He realized that '
             'it would take him in this case about 3 months to close a deal.',
      'title': 'How to Find Businesses to Buy NO ONE ELSE Knows About (80 MINUTE Playbook) '
               '(Codie Sanchez)',
      'url': 'https://www.youtube.com/watch?v=3mtS8rOAqoM&t=2092s',
      'video_id': '3mtS8rOAqoM'},
     {'author': 'Lion Business Advisors',
      'channel': 'Lion Business Advisors',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:28](https://www.youtube.com/watch?v=orHTcAJcuAM&t=1228s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'For an initial acquisition or business expansion, the seller generally may not '
              'stay as an officer, director, stockholder, or employee after closing, subject '
              "to the SOP's stated exceptions.",
      'timestamp': 1228,
      'timestamp_label': '[00:20:28]',
      'timestamp_seconds': 1228,
      'tip': 'For an initial acquisition or business expansion, the seller generally may not '
             'stay as an officer, director, stockholder, or employee after closing, subject to '
             "the SOP's stated exceptions.",
      'title': 'SBA SOP 50 10 8.1: What Changed for Business Acquisitions, and What Didn’t '
               '(Lion Business Advisors)',
      'url': 'https://www.youtube.com/watch?v=orHTcAJcuAM&t=1228s',
      'video_id': 'orHTcAJcuAM'},
     {'author': 'Commercial Lending X',
      'channel': 'Commercial Lending X',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:26](https://www.youtube.com/watch?v=Rsg9fKAzdAo&t=206s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The third major change has to do with quality of earnings. With the update in '
              'August, the SOP and SBA through that SOP states that any buyer purchasing a '
              'business where the business purchase price is 3 million or higher, excluding '
              'real estate, must get a quality of earnings.',
      'timestamp': 206,
      'timestamp_label': '[00:03:26]',
      'timestamp_seconds': 206,
      'tip': 'The third major change has to do with quality of earnings. With the update in '
             'August, the SOP and SBA through that SOP states that any buyer purchasing a '
             'business where the business purchase price is 3 million or higher, excluding '
             'real estate, must get a quality of earnings.',
      'title': 'The SBA Does It Again: More Changes to the New SBA SOP (Commercial Lending X)',
      'url': 'https://www.youtube.com/watch?v=Rsg9fKAzdAo&t=206s',
      'video_id': 'Rsg9fKAzdAo'},
     {'author': 'Marco Palmero',
      'channel': 'Marco Palmero',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=iPMw4FjbyRQ&t=70s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And so, they didn't have time to build a proprietary system that could "
              'ultimately put them in control of their deal flow process, get them more deals, '
              'and help them close an acquisition faster.',
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': "And so, they didn't have time to build a proprietary system that could "
             'ultimately put them in control of their deal flow process, get them more deals, '
             'and help them close an acquisition faster.',
      'title': 'Search Fund Case Study: 5–10 Qualified Seller Meetings Every Month (Marco '
               'Palmero)',
      'url': 'https://www.youtube.com/watch?v=iPMw4FjbyRQ&t=70s',
      'video_id': 'iPMw4FjbyRQ'},
     {'author': 'Making Billions with Ryan Miller',
      'channel': 'Making Billions with Ryan Miller',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=iYE-lc1tFUI&t=21s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'No venture capital, no endless fundraising, just pure strategy around private '
              "equity acquisition. You see, this isn't about luck. This is about a proven "
              'system that has the potential to transform your financial future in a matter of '
              'months, not decades.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'No venture capital, no endless fundraising, just pure strategy around private '
             "equity acquisition. You see, this isn't about luck. This is about a proven "
             'system that has the potential to transform your financial future in a matter of '
             'months, not decades.',
      'title': 'BUY THEN BUILD: Your Private Equity Masterclass on Buying Companies - Walker '
               'Deibel (Making Billions with Ryan Miller)',
      'url': 'https://www.youtube.com/watch?v=iYE-lc1tFUI&t=21s',
      'video_id': 'iYE-lc1tFUI'},
     {'author': 'acquiredotcom',
      'channel': 'acquiredotcom',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:34](https://www.youtube.com/watch?v=MYKKpeF0xMM&t=214s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Forward to working with you and just like that I can go ahead and send an Loi '
              'on acquire.com and that is one of the first steps of acquiring a business if '
              'you have any questions feel free to reach out cheers.',
      'timestamp': 214,
      'timestamp_label': '[00:03:34]',
      'timestamp_seconds': 214,
      'tip': 'Forward to working with you and just like that I can go ahead and send an Loi on '
             'acquire.com and that is one of the first steps of acquiring a business if you '
             'have any questions feel free to reach out cheers.',
      'title': 'Letter of Intent Document Builder - Acquire.com (acquiredotcom)',
      'url': 'https://www.youtube.com/watch?v=MYKKpeF0xMM&t=214s',
      'video_id': 'MYKKpeF0xMM'},
     {'author': 'growthink',
      'channel': 'growthink',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:03](https://www.youtube.com/watch?v=UfQ-Ho_j61s&t=903s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "This is uh kind of a the key to any due diligence process when you know you're "
              'thinking about selling a business. Um, historically and and of course going '
              'forward, this has usually been a buy side or uh, you know, applied to the buyer '
              'part of the the due diligence process.',
      'timestamp': 903,
      'timestamp_label': '[00:15:03]',
      'timestamp_seconds': 903,
      'tip': "This is uh kind of a the key to any due diligence process when you know you're "
             'thinking about selling a business. Um, historically and and of course going '
             'forward, this has usually been a buy side or uh, you know, applied to the buyer '
             'part of the the due diligence process.',
      'title': 'Qualifying EBITDA Add-Backs - Separating Fact From Fiction | Masterclass '
               '(growthink)',
      'url': 'https://www.youtube.com/watch?v=UfQ-Ho_j61s&t=903s',
      'video_id': 'UfQ-Ho_j61s'},
     {'author': 'ProjectionHub',
      'channel': 'ProjectionHub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:29](https://www.youtube.com/watch?v=BvJfOb1y6x8&t=509s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You need help with financial projections in your acquisition process please let '
              'me know you can reach out to us again at support projection hub.com all right '
              'thanks.',
      'timestamp': 509,
      'timestamp_label': '[00:08:29]',
      'timestamp_seconds': 509,
      'tip': 'You need help with financial projections in your acquisition process please let '
             'me know you can reach out to us again at support projection hub.com all right '
             'thanks.',
      'title': 'How to Perform a Net Working Capital True-Up Calculation for a Small Business '
               'Acquisition (ProjectionHub)',
      'url': 'https://www.youtube.com/watch?v=BvJfOb1y6x8&t=509s',
      'video_id': 'BvJfOb1y6x8'},
     {'author': 'Verified Metrics',
      'channel': 'Verified Metrics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:27](https://www.youtube.com/watch?v=EzOFN-69wBU&t=147s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "2022 to the last 12 months. Let's now take a look at networking capital. Before "
              'we proceed to the numbers. Do note that at default the adjustment Logics for '
              'networking capital is the same with the quality of earnings.',
      'timestamp': 147,
      'timestamp_label': '[00:02:27]',
      'timestamp_seconds': 147,
      'tip': "2022 to the last 12 months. Let's now take a look at networking capital. Before "
             'we proceed to the numbers. Do note that at default the adjustment Logics for '
             'networking capital is the same with the quality of earnings.',
      'title': 'Quality of Earnings Databook - A Case Walkthrough (Verified Metrics)',
      'url': 'https://www.youtube.com/watch?v=EzOFN-69wBU&t=147s',
      'video_id': 'EzOFN-69wBU'},
     {'author': 'Digital Transformation with Eric Kimberling',
      'channel': 'Digital Transformation with Eric Kimberling',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:57](https://www.youtube.com/watch?v=a7XwL5Q-ttE&t=177s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Challenges that this company was facing and so they hired us to come in and do '
              "a merger and acquisition integration strategy and I'll talk about some of the "
              'steps we went through to help them through the process.',
      'timestamp': 177,
      'timestamp_label': '[00:02:57]',
      'timestamp_seconds': 177,
      'tip': 'Challenges that this company was facing and so they hired us to come in and do a '
             "merger and acquisition integration strategy and I'll talk about some of the "
             'steps we went through to help them through the process.',
      'title': 'How A $3B Multinational Company Integrated 40+ Mergers and Acquisitions [M&A '
               'Integration Case Study] (Digital Transformation with Eric Kimberling)',
      'url': 'https://www.youtube.com/watch?v=a7XwL5Q-ttE&t=177s',
      'video_id': 'a7XwL5Q-ttE'},
     {'author': 'Marco Palmero',
      'channel': 'Marco Palmero',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:07](https://www.youtube.com/watch?v=x4qfCP1pVmE&t=187s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And then it spits out a series of options that you can um you know pursue in '
              'terms of acquisition with a clear action step on what to do next in how to take '
              "your first steps towards uh the deal. So do that if you don't have clarity on "
              'on the your thesis.',
      'timestamp': 187,
      'timestamp_label': '[00:03:07]',
      'timestamp_seconds': 187,
      'tip': 'And then it spits out a series of options that you can um you know pursue in '
             'terms of acquisition with a clear action step on what to do next in how to take '
             "your first steps towards uh the deal. So do that if you don't have clarity on on "
             'the your thesis.',
      'title': 'How Search Funds Source Proprietary Deals Without Cold Calling (Marco Palmero)',
      'url': 'https://www.youtube.com/watch?v=x4qfCP1pVmE&t=187s',
      'video_id': 'x4qfCP1pVmE'},
     {'author': 'Edspira',
      'channel': 'Edspira',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:46](https://www.youtube.com/watch?v=itIweMi_DyU&t=106s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "They're trying to sell the company a quality of earnings report tells you "
              'whether the financial situation is as good as the seller says it is thus '
              'getting a quality of earnings report is similar to having a mechanic look at a '
              'used car before you buy.',
      'timestamp': 106,
      'timestamp_label': '[00:01:46]',
      'timestamp_seconds': 106,
      'tip': "They're trying to sell the company a quality of earnings report tells you "
             'whether the financial situation is as good as the seller says it is thus getting '
             'a quality of earnings report is similar to having a mechanic look at a used car '
             'before you buy.',
      'title': 'Quality of Earnings Report (Edspira)',
      'url': 'https://www.youtube.com/watch?v=itIweMi_DyU&t=106s',
      'video_id': 'itIweMi_DyU'},
     {'author': 'Pacific Mergers and Acquisitions Inc.',
      'channel': 'Pacific Mergers and Acquisitions Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:20](https://www.youtube.com/watch?v=329Ul-sT1ps&t=200s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Process in order to determine if one they are interested in closing the '
              "transaction and two if the purchase price they're paying is Justified in.",
      'timestamp': 200,
      'timestamp_label': '[00:03:20]',
      'timestamp_seconds': 200,
      'tip': 'Process in order to determine if one they are interested in closing the '
             "transaction and two if the purchase price they're paying is Justified in.",
      'title': 'Components of a Letter of Intent (Pacific Mergers and Acquisitions Inc.)',
      'url': 'https://www.youtube.com/watch?v=329Ul-sT1ps&t=200s',
      'video_id': '329Ul-sT1ps'},
     {'author': 'CandiMentor',
      'channel': 'CandiMentor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:30](https://www.youtube.com/watch?v=3hIMMSUc5gQ&t=270s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You might be asked, "Walk us through a typical QE analysis process. Outline '
              'steps like data collection, financial statement adjustments, cash flow '
              'analysis, and the identification of red flags. Mention the importance of '
              'understanding industry specific factors.',
      'timestamp': 270,
      'timestamp_label': '[00:04:30]',
      'timestamp_seconds': 270,
      'tip': 'You might be asked, "Walk us through a typical QE analysis process. Outline '
             'steps like data collection, financial statement adjustments, cash flow analysis, '
             'and the identification of red flags. Mention the importance of understanding '
             'industry specific factors.',
      'title': 'Quality of Earnings (QoE) Explained | Financial Due Diligence Interview '
               'Questions (CandiMentor)',
      'url': 'https://www.youtube.com/watch?v=3hIMMSUc5gQ&t=270s',
      'video_id': '3hIMMSUc5gQ'},
     {'author': 'The Acquisition Manager',
      'channel': 'The Acquisition Manager',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:21](https://www.youtube.com/watch?v=zYUvLwZ6ipc&t=81s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm going to understand certain things that I may not know. Some things I "
              "already know, but we going we going to learn it. I just wanted to show y'all "
              "take y'all through this process of me you know, how I get these deals closed, "
              'how I bring people to the table.',
      'timestamp': 81,
      'timestamp_label': '[00:01:21]',
      'timestamp_seconds': 81,
      'tip': "I'm going to understand certain things that I may not know. Some things I "
             "already know, but we going we going to learn it. I just wanted to show y'all "
             "take y'all through this process of me you know, how I get these deals closed, "
             'how I bring people to the table.',
      'title': 'How I Study Closed Deals Before Calling Brokers | Commercial Real Estate Case '
               'Study Review (The Acquisition Manager)',
      'url': 'https://www.youtube.com/watch?v=zYUvLwZ6ipc&t=81s',
      'video_id': 'zYUvLwZ6ipc'}],
 8: [{'author': 'INSEAD',
      'channel': 'INSEAD',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:38](https://www.youtube.com/watch?v=i7FBr84AUfY&t=158s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'It was invented at Stanford and Harvard and it entails investors providing '
              "capital to support an entrepreneur's full-time search for a business to acquire "
              'and then fund the acquisition the target itself.',
      'timestamp': 158,
      'timestamp_label': '[00:02:38]',
      'timestamp_seconds': 158,
      'tip': 'It was invented at Stanford and Harvard and it entails investors providing '
             "capital to support an entrepreneur's full-time search for a business to acquire "
             'and then fund the acquisition the target itself.',
      'title': 'INSEAD Explains Entrepreneurship: Becoming an Entrepreneur by Acquisition '
               '(INSEAD)',
      'url': 'https://www.youtube.com/watch?v=i7FBr84AUfY&t=158s',
      'video_id': 'i7FBr84AUfY'},
     {'author': 'Byron Thomas Recruitment',
      'channel': 'Byron Thomas Recruitment',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:55](https://www.youtube.com/watch?v=NotNaT329hg&t=1495s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You cannot just leave them to manage the transition alone. The acquiring '
              'business must surround them with interim support, deploying a robust systems '
              'accountant to handle the data mapping, or an interim FP&A specialist to build '
              'the synergy tracking models.',
      'timestamp': 1495,
      'timestamp_label': '[00:24:55]',
      'timestamp_seconds': 1495,
      'tip': 'You cannot just leave them to manage the transition alone. The acquiring '
             'business must surround them with interim support, deploying a robust systems '
             'accountant to handle the data mapping, or an interim FP&A specialist to build '
             'the synergy tracking models.',
      'title': 'Post-Deal Finance Integration: Why Acquisitions Underperform in the First 100 '
               'Days (Byron Thomas Recruitment)',
      'url': 'https://www.youtube.com/watch?v=NotNaT329hg&t=1495s',
      'video_id': 'NotNaT329hg'},
     {'author': 'Acquiring Minds',
      'channel': 'Acquiring Minds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=YsZAnvfQAqk&t=21s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, a key theme to this journey is how to build a rollup starting with an SBA '
              'loan to buy your platform acquisition. That was also, of course, Brian, the '
              'subject of an acquiring minds webinar that you co-hosted back in May. We will '
              'link to that in the show notes.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'So, a key theme to this journey is how to build a rollup starting with an SBA '
             'loan to buy your platform acquisition. That was also, of course, Brian, the '
             'subject of an acquiring minds webinar that you co-hosted back in May. We will '
             'link to that in the show notes.',
      'title': '$60m Roll-Up That Started With an SBA Acquisition | Brian Boland and Onu '
               'Okebie Interview (Acquiring Minds)',
      'url': 'https://www.youtube.com/watch?v=YsZAnvfQAqk&t=21s',
      'video_id': 'YsZAnvfQAqk'},
     {'author': "Patrick O'Connell - M&A Transaction Services",
      'channel': "Patrick O'Connell - M&A Transaction Services",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:36](https://www.youtube.com/watch?v=6AT45jrM2CU&t=336s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I jokingly call them kind of kholes that you just like fall into. But um it '
              "then there's some like kind of required reading uh Harvard Business Reviews, "
              'how to buy a small business, Walker Debbles, buy then build.',
      'timestamp': 336,
      'timestamp_label': '[00:05:36]',
      'timestamp_seconds': 336,
      'tip': 'I jokingly call them kind of kholes that you just like fall into. But um it then '
             "there's some like kind of required reading uh Harvard Business Reviews, how to "
             'buy a small business, Walker Debbles, buy then build.',
      'title': 'The First 100 Days: How to Succeed After a Business Acquisition (Patrick '
               "O'Connell - M&A Transaction Services)",
      'url': 'https://www.youtube.com/watch?v=6AT45jrM2CU&t=336s',
      'video_id': '6AT45jrM2CU'},
     {'author': 'Martin Godfrey Legido',
      'channel': 'Martin Godfrey Legido',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=04Uy5gfO_PU&t=50s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I think I would divide Well, firstly that the normal method of acquisition of a '
              "company certainly in in our business that we come across and deals that I've "
              'done over the last 30 years I would always prefer to go for the buying the '
              'actual shares in the company.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': 'I think I would divide Well, firstly that the normal method of acquisition of a '
             "company certainly in in our business that we come across and deals that I've "
             'done over the last 30 years I would always prefer to go for the buying the '
             'actual shares in the company.',
      'title': 'One Wrong Move, Scary Result: Asset Purchase vs Share Purchase (Martin Godfrey '
               'Legido)',
      'url': 'https://www.youtube.com/watch?v=04Uy5gfO_PU&t=50s',
      'video_id': '04Uy5gfO_PU'},
     {'author': 'SoftSavvy',
      'channel': 'SoftSavvy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:17](https://www.youtube.com/watch?v=uJWyOGsPXbA&t=197s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So if your team uses tools like HubSpot, Salesforce, Pipedrive, Zapier, or any '
              'of the 100+ integrations CloudTalk supports, the platform is designed to '
              'connect calls and conversation history back into the tools you already use.',
      'timestamp': 197,
      'timestamp_label': '[00:03:17]',
      'timestamp_seconds': 197,
      'tip': 'So if your team uses tools like HubSpot, Salesforce, Pipedrive, Zapier, or any '
             'of the 100+ integrations CloudTalk supports, the platform is designed to connect '
             'calls and conversation history back into the tools you already use.',
      'title': 'Best Cold Calling Software for SMB Sales Teams in 2026 (SoftSavvy)',
      'url': 'https://www.youtube.com/watch?v=uJWyOGsPXbA&t=197s',
      'video_id': 'uJWyOGsPXbA'},
     {'author': 'Evan DiLeonardi | Acquisitions',
      'channel': 'Evan DiLeonardi | Acquisitions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:43](https://www.youtube.com/watch?v=zBzv99U7MyE&t=403s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Claude or Codex or one of these tools to build an app. I have a friend doing '
              'this right now. He might be the kind of person who could buy a SaaS company '
              'because he knows how a go-to-market strategy works, and he knows how to build '
              'and update apps using AI.',
      'timestamp': 403,
      'timestamp_label': '[00:06:43]',
      'timestamp_seconds': 403,
      'tip': 'Claude or Codex or one of these tools to build an app. I have a friend doing '
             'this right now. He might be the kind of person who could buy a SaaS company '
             'because he knows how a go-to-market strategy works, and he knows how to build '
             'and update apps using AI.',
      'title': 'EP. 1: Can a Seller Note Cover Your SBA Down Payment? Plus, What Business '
               'Should You Buy? (Evan DiLeonardi | Acquisitions)',
      'url': 'https://www.youtube.com/watch?v=zBzv99U7MyE&t=403s',
      'video_id': 'zBzv99U7MyE'},
     {'author': 'Stanford Graduate School of Business',
      'channel': 'Stanford Graduate School of Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=_rMBWgqtfUI&t=39s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'To raise a little bit of walking around money, to conduct a thoughtful two year '
              'search, to find a small business to buy.',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': 'To raise a little bit of walking around money, to conduct a thoughtful two year '
             'search, to find a small business to buy.',
      'title': 'Coley Andrews:  What it Takes to be a Search Fund Entrepreneur (Stanford '
               'Graduate School of Business)',
      'url': 'https://www.youtube.com/watch?v=_rMBWgqtfUI&t=39s',
      'video_id': '_rMBWgqtfUI'},
     {'author': 'The Intentional Owner',
      'channel': 'The Intentional Owner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:07](https://www.youtube.com/watch?v=cC2-F0YZb9M&t=487s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So, I'll flip it back to you. What's your generic approach to the non-tactical "
              'piece? No, I mean, it I wanted to talk about this because one of the search '
              "deals I've invested in, they just closed an add-on acquisition.",
      'timestamp': 487,
      'timestamp_label': '[00:08:07]',
      'timestamp_seconds': 487,
      'tip': "So, I'll flip it back to you. What's your generic approach to the non-tactical "
             'piece? No, I mean, it I wanted to talk about this because one of the search '
             "deals I've invested in, they just closed an add-on acquisition.",
      'title': 'How to Navigate the First 90 Days Post-Acquisition - The Intentional Owner #15 '
               '(The Intentional Owner)',
      'url': 'https://www.youtube.com/watch?v=cC2-F0YZb9M&t=487s',
      'video_id': 'cC2-F0YZb9M'},
     {'author': 'The University of Chicago Booth School of Business',
      'channel': 'The University of Chicago Booth School of Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:11](https://www.youtube.com/watch?v=ccaGmVeLcto&t=1211s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "When the professor that's sort of founded this model back to promising a "
              'student or graduate of their class and ultimately this asset class around '
              'search funds and entrepreneurship through acquisition was born.',
      'timestamp': 1211,
      'timestamp_label': '[00:20:11]',
      'timestamp_seconds': 1211,
      'tip': "When the professor that's sort of founded this model back to promising a student "
             'or graduate of their class and ultimately this asset class around search funds '
             'and entrepreneurship through acquisition was born.',
      'title': 'The Acquisition Search Process - Entrepreneurship Through Acquisition Event '
               'Series (The University of Chicago Booth School of Business)',
      'url': 'https://www.youtube.com/watch?v=ccaGmVeLcto&t=1211s',
      'video_id': 'ccaGmVeLcto'},
     {'author': 'SMB Law Group LLP',
      'channel': 'SMB Law Group LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:49](https://www.youtube.com/watch?v=iNOj__jXGpE&t=829s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm still out half a million dollars today, and in a small business, that means "
              "I'm likely bankrupt. And networking capital is one of the big three sources of "
              'liquidity.',
      'timestamp': 829,
      'timestamp_label': '[00:13:49]',
      'timestamp_seconds': 829,
      'tip': "I'm still out half a million dollars today, and in a small business, that means "
             "I'm likely bankrupt. And networking capital is one of the big three sources of "
             'liquidity.',
      'title': 'Seller Financing and Set-Off Rights: Recovery Mechanisms in M&A Deals (SMB Law '
               'Group LLP)',
      'url': 'https://www.youtube.com/watch?v=iNOj__jXGpE&t=829s',
      'video_id': 'iNOj__jXGpE'},
     {'author': 'Tresle Inc',
      'channel': 'Tresle Inc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:40:42](https://www.youtube.com/watch?v=NmgNpE_W_po&t=2442s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Dot com um I'll also include um jack your information as well uh further you "
              'know if you have any other suggestions for future webinars or guests drop us an '
              'email at hello trestle.com and thank you guys all so much and stay safe thank '
              'you thanks joel thanks everybody.',
      'timestamp': 2442,
      'timestamp_label': '[00:40:42]',
      'timestamp_seconds': 2442,
      'tip': "Dot com um I'll also include um jack your information as well uh further you "
             'know if you have any other suggestions for future webinars or guests drop us an '
             'email at hello trestle.com and thank you guys all so much and stay safe thank '
             'you thanks joel thanks everybody.',
      'title': 'SBA 7(a) Loan for Business Acquisition | Tresle Talks (Tresle Inc)',
      'url': 'https://www.youtube.com/watch?v=NmgNpE_W_po&t=2442s',
      'video_id': 'NmgNpE_W_po'},
     {'author': 'Peak Frameworks',
      'channel': 'Peak Frameworks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:01](https://www.youtube.com/watch?v=0KhOZrLBMVQ&t=361s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Should check out stanford search firm primer they released a publication that '
              'includes tons of statistics as well as the instructions to start your own '
              "search fund so thanks for watching this video and I'll see you in the next one.",
      'timestamp': 361,
      'timestamp_label': '[00:06:01]',
      'timestamp_seconds': 361,
      'tip': 'Should check out stanford search firm primer they released a publication that '
             'includes tons of statistics as well as the instructions to start your own search '
             "fund so thanks for watching this video and I'll see you in the next one.",
      'title': 'Search Funds: How to Buy a Small Business (Peak Frameworks)',
      'url': 'https://www.youtube.com/watch?v=0KhOZrLBMVQ&t=361s',
      'video_id': '0KhOZrLBMVQ'},
     {'author': 'David C Barnett Small Business and Deal Making SMB',
      'channel': 'David C Barnett Small Business and Deal Making SMB',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:07](https://www.youtube.com/watch?v=LStVgWOM2LI&t=487s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Had given them some incorrect technical data about the product and it led to a '
              'problem on a building site and he had a really bad relationship with that '
              'architecture firm and he tried to hide that from the buyer now.',
      'timestamp': 487,
      'timestamp_label': '[00:08:07]',
      'timestamp_seconds': 487,
      'tip': 'Had given them some incorrect technical data about the product and it led to a '
             'problem on a building site and he had a really bad relationship with that '
             'architecture firm and he tried to hide that from the buyer now.',
      'title': 'Do Representations and Warranties have any value?  business broker vendor '
               'financing seller financing (David C Barnett Small Business and Deal Making '
               'SMB)',
      'url': 'https://www.youtube.com/watch?v=LStVgWOM2LI&t=487s',
      'video_id': 'LStVgWOM2LI'},
     {'author': 'Acquireman M&A',
      'channel': 'Acquireman M&A',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=VBNjS7UATHo&t=71s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Instead of buying the company's shares, you acquire specified assets or "
              'business operations directly. For example, you might purchase its software, '
              'brand, customer relationships, equipment, and selected contracts.',
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': "Instead of buying the company's shares, you acquire specified assets or business "
             'operations directly. For example, you might purchase its software, brand, '
             'customer relationships, equipment, and selected contracts.',
      'title': 'What Exactly Are You Buying in an M&A Deal? Share Purchase vs Asset Purchase '
               '#mergersandacquisitions (Acquireman M&A)',
      'url': 'https://www.youtube.com/watch?v=VBNjS7UATHo&t=71s',
      'video_id': 'VBNjS7UATHo'}],
 9: [{'author': 'PCE Investment Bankers - M&A | ESOP | Valuation',
      'channel': 'PCE Investment Bankers - M&A | ESOP | Valuation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=YJMOV57uFMk&t=91s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Working capital is a critical piece that makes sure that the seller operates '
              'the business in the normal course from the time you sign a letter of intent '
              'until closing. Examples of binding terms include exclusivity, disclosure and '
              'confidentiality, and governing law.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': 'Working capital is a critical piece that makes sure that the seller operates the '
             'business in the normal course from the time you sign a letter of intent until '
             'closing. Examples of binding terms include exclusivity, disclosure and '
             'confidentiality, and governing law.',
      'title': 'Key Terms to Know When Negotiating a Letter of Intent (PCE Investment Bankers '
               '- M&A | ESOP | Valuation)',
      'url': 'https://www.youtube.com/watch?v=YJMOV57uFMk&t=91s',
      'video_id': 'YJMOV57uFMk'},
     {'author': 'SBA Ray',
      'channel': 'SBA Ray',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:23](https://www.youtube.com/watch?v=BJojYQ4nJho&t=323s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'With the SBA 7A, typically 0%. Buying a business with a conventional loan, try '
              '40% down. In every situation, the SBA loan allows you to preserve more of your '
              'capital compared to the other options. Pro number two, longer terms, which '
              'means lower payments.',
      'timestamp': 323,
      'timestamp_label': '[00:05:23]',
      'timestamp_seconds': 323,
      'tip': 'With the SBA 7A, typically 0%. Buying a business with a conventional loan, try '
             '40% down. In every situation, the SBA loan allows you to preserve more of your '
             'capital compared to the other options. Pro number two, longer terms, which means '
             'lower payments.',
      'title': 'The Pros and Cons of the SBA 7(a) Loan [2026 Update] (SBA Ray)',
      'url': 'https://www.youtube.com/watch?v=BJojYQ4nJho&t=323s',
      'video_id': 'BJojYQ4nJho'},
     {'author': 'Lower Hudson Small Business Development Center',
      'channel': 'Lower Hudson Small Business Development Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:12](https://www.youtube.com/watch?v=y_3r9__pQR0&t=432s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s very important with the SBA. And you are okay with working through a "
              'transition period in terms of your income. There are six ways to acquire a '
              'business. You can buy all the assets, leave all the liabilities behind. You um '
              'create your own LLC.',
      'timestamp': 432,
      'timestamp_label': '[00:07:12]',
      'timestamp_seconds': 432,
      'tip': "'s very important with the SBA. And you are okay with working through a "
             'transition period in terms of your income. There are six ways to acquire a '
             'business. You can buy all the assets, leave all the liabilities behind. You um '
             'create your own LLC.',
      'title': 'How to Buy a Business Using an SBA Loan | SBDC Workshop (Lower Hudson Small '
               'Business Development Center)',
      'url': 'https://www.youtube.com/watch?v=y_3r9__pQR0&t=432s',
      'video_id': 'y_3r9__pQR0'},
     {'author': 'Escamilla Law Office',
      'channel': 'Escamilla Law Office',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:18](https://www.youtube.com/watch?v=juS-FdGX2o0&t=378s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'In the equity acquisition, the buyer purchases ownership interest in the '
              'company itself. That means the legal entity generally continues to exist along '
              'with the assets, contracts, liabilities subject to the terms of those '
              'arrangements in and applicable law.',
      'timestamp': 378,
      'timestamp_label': '[00:06:18]',
      'timestamp_seconds': 378,
      'tip': 'In the equity acquisition, the buyer purchases ownership interest in the company '
             'itself. That means the legal entity generally continues to exist along with the '
             'assets, contracts, liabilities subject to the terms of those arrangements in and '
             'applicable law.',
      'title': 'Letter of Intent Terms to Settle Before Due Diligence (Escamilla Law Office)',
      'url': 'https://www.youtube.com/watch?v=juS-FdGX2o0&t=378s',
      'video_id': 'juS-FdGX2o0'},
     {'author': 'PCE Investment Bankers - M&A | ESOP | Valuation',
      'channel': 'PCE Investment Bankers - M&A | ESOP | Valuation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=n_gxsr8QgBM&t=91s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Non-binding terms include purchase price structure contingencies due diligence '
              'process and working capital examples of binding terms include exclusivity '
              "disclosure and confidentiality and governing law let's get started by reviewing "
              'the non-binding terms in detail.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': 'Non-binding terms include purchase price structure contingencies due diligence '
             'process and working capital examples of binding terms include exclusivity '
             "disclosure and confidentiality and governing law let's get started by reviewing "
             'the non-binding terms in detail.',
      'title': 'Letter of Intent (PCE Investment Bankers - M&A | ESOP | Valuation)',
      'url': 'https://www.youtube.com/watch?v=n_gxsr8QgBM&t=91s',
      'video_id': 'n_gxsr8QgBM'},
     {'author': 'Built to Sell',
      'channel': 'Built to Sell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:57](https://www.youtube.com/watch?v=004ptgWQ2TE&t=177s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Uh Rick, maybe do you want to walk me through like in in a basic layman's "
              'terms, how are they getting the money to buy a business? At the time they go to '
              "buy the business, it's not really hard. Um there's uh local commercial banks "
              'that lend.',
      'timestamp': 177,
      'timestamp_label': '[00:02:57]',
      'timestamp_seconds': 177,
      'tip': "Uh Rick, maybe do you want to walk me through like in in a basic layman's terms, "
             'how are they getting the money to buy a business? At the time they go to buy the '
             "business, it's not really hard. Um there's uh local commercial banks that lend.",
      'title': 'Inside the Mind of an Acquirer: The Harvard Playbook for Buying Your Business '
               '(Built to Sell)',
      'url': 'https://www.youtube.com/watch?v=004ptgWQ2TE&t=177s',
      'video_id': '004ptgWQ2TE'},
     {'author': 'The University of Chicago Booth School of Business',
      'channel': 'The University of Chicago Booth School of Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:39:26](https://www.youtube.com/watch?v=kKwXdeUVNOw&t=2366s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'A couple of more specific examples, though, would be legal documentation. So '
              'these legal docs are not simple. They, I mean a purchase agreement, 90, 100 '
              "pages, whatever it is, and it's not in plain English.",
      'timestamp': 2366,
      'timestamp_label': '[00:39:26]',
      'timestamp_seconds': 2366,
      'tip': 'A couple of more specific examples, though, would be legal documentation. So '
             'these legal docs are not simple. They, I mean a purchase agreement, 90, 100 '
             "pages, whatever it is, and it's not in plain English.",
      'title': 'Structuring the Acquisition Deal - Entrepreneurship Through Acquisition Event '
               'Series (The University of Chicago Booth School of Business)',
      'url': 'https://www.youtube.com/watch?v=kKwXdeUVNOw&t=2366s',
      'video_id': 'kKwXdeUVNOw'},
     {'author': 'MySaasForSale',
      'channel': 'MySaasForSale',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:51](https://www.youtube.com/watch?v=OOlka50xFck&t=411s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And the support period, capped in weeks and hours. This is general information, '
              'not legal advice: for a real deal, the letter and the final agreement are worth '
              'having checked by a lawyer you choose. Next, the last episode of this playlist: '
              'closing and handover.',
      'timestamp': 411,
      'timestamp_label': '[00:06:51]',
      'timestamp_seconds': 411,
      'tip': 'And the support period, capped in weeks and hours. This is general information, '
             'not legal advice: for a real deal, the letter and the final agreement are worth '
             'having checked by a lawyer you choose. Next, the last episode of this playlist: '
             'closing and handover.',
      'title': 'Negotiating a SaaS sale: the letter of intent, exclusivity and the terms that '
               'matter (MySaasForSale)',
      'url': 'https://www.youtube.com/watch?v=OOlka50xFck&t=411s',
      'video_id': 'OOlka50xFck'},
     {'author': 'JackQuisitions',
      'channel': 'JackQuisitions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:32](https://www.youtube.com/watch?v=I6M8wAaqm5s&t=452s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'t lean on the lender in terms of like their job is not due diligence for you. "
              'Their job is not sussing out if you should buy this business or not, but '
              "definitely having someone who's on your side is No, for sure.",
      'timestamp': 452,
      'timestamp_label': '[00:07:32]',
      'timestamp_seconds': 452,
      'tip': "'t lean on the lender in terms of like their job is not due diligence for you. "
             'Their job is not sussing out if you should buy this business or not, but '
             "definitely having someone who's on your side is No, for sure.",
      'title': 'SBA Loan Strategies for Acquiring a Business | Expert Advice #6 '
               '(JackQuisitions)',
      'url': 'https://www.youtube.com/watch?v=I6M8wAaqm5s&t=452s',
      'video_id': 'I6M8wAaqm5s'},
     {'author': 'Brett Cenkus',
      'channel': 'Brett Cenkus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:06](https://www.youtube.com/watch?v=ASUM5illI98&t=66s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Those are kind of terms of art, but just so you understand what's going on, "
              'these are smaller deals and this content is aimed at someone buying or selling '
              "in that space. So, deal structures - there's 3 primary ways to structure the "
              'sale of a business.',
      'timestamp': 66,
      'timestamp_label': '[00:01:06]',
      'timestamp_seconds': 66,
      'tip': "Those are kind of terms of art, but just so you understand what's going on, "
             'these are smaller deals and this content is aimed at someone buying or selling '
             "in that space. So, deal structures - there's 3 primary ways to structure the "
             'sale of a business.',
      'title': 'Merger & Acquisition (M&A) Deal Structures Explained (Brett Cenkus)',
      'url': 'https://www.youtube.com/watch?v=ASUM5illI98&t=66s',
      'video_id': 'ASUM5illI98'},
     {'author': 'Owner Actions | Buy a Business with Us',
      'channel': 'Owner Actions | Buy a Business with Us',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=lfjqb1es1E4&t=22s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, these are 10-year term loans. So, on full standby for 10 years. Now, this '
              'is a change from the most recent rules that only required that note to be on '
              'standby for 24 months. Now, the 10-year requirement was the rule not that long '
              'ago.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'So, these are 10-year term loans. So, on full standby for 10 years. Now, this is '
             'a change from the most recent rules that only required that note to be on '
             'standby for 24 months. Now, the 10-year requirement was the rule not that long '
             'ago.',
      'title': 'BIG Update: Seller Note Standby Rules When Buying a Business (Owner Actions | '
               'Buy a Business with Us)',
      'url': 'https://www.youtube.com/watch?v=lfjqb1es1E4&t=22s',
      'video_id': 'lfjqb1es1E4'},
     {'author': 'MCM Capital',
      'channel': 'MCM Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:32](https://www.youtube.com/watch?v=almKwAlo5T4&t=152s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The contracts of the deals we worked on but it's definitely something to think "
              "about in terms of hey that cash you've already received is that something that "
              'we call debt in the transaction or something that goes into the calculation of '
              'working capital.',
      'timestamp': 152,
      'timestamp_label': '[00:02:32]',
      'timestamp_seconds': 152,
      'tip': "The contracts of the deals we worked on but it's definitely something to think "
             "about in terms of hey that cash you've already received is that something that "
             'we call debt in the transaction or something that goes into the calculation of '
             'working capital.',
      'title': 'Most Common Working Capital Adjustments (MCM Capital)',
      'url': 'https://www.youtube.com/watch?v=almKwAlo5T4&t=152s',
      'video_id': 'almKwAlo5T4'},
     {'author': 'Transact Capital',
      'channel': 'Transact Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=Axofinu0FSU&t=118s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Purchase agreement this will be covered in in our next video be sure to '
              'continue watching the rest of our aart series on the Milestones of m&a '
              'presented by transact capital.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': 'Purchase agreement this will be covered in in our next video be sure to continue '
             'watching the rest of our aart series on the Milestones of m&a presented by '
             'transact capital.',
      'title': 'What is the Letter Of Intent in Investment Banking - 8 Milestones of M&A - '
               'Transact Capital (Transact Capital)',
      'url': 'https://www.youtube.com/watch?v=Axofinu0FSU&t=118s',
      'video_id': 'Axofinu0FSU'},
     {'author': 'Mergers & Inquisitions / Breaking Into Wall Street',
      'channel': 'Mergers & Inquisitions / Breaking Into Wall Street',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:21](https://www.youtube.com/watch?v=oa8dUICluLM&t=621s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Relative to the company's revenue and free cash flow and ebit and other metrics "
              'like that over time hopefully now you know a little bit more about this topic '
              "and why it doesn't really matter that much but it is still good to know for "
              'modeling purposes.',
      'timestamp': 621,
      'timestamp_label': '[00:10:21]',
      'timestamp_seconds': 621,
      'tip': "Relative to the company's revenue and free cash flow and ebit and other metrics "
             'like that over time hopefully now you know a little bit more about this topic '
             "and why it doesn't really matter that much but it is still good to know for "
             'modeling purposes.',
      'title': 'The Working Capital Adjustment in M&A Deals and Leveraged Buyouts (Mergers & '
               'Inquisitions / Breaking Into Wall Street)',
      'url': 'https://www.youtube.com/watch?v=oa8dUICluLM&t=621s',
      'video_id': 'oa8dUICluLM'},
     {'author': 'Matthias Smith',
      'channel': 'Matthias Smith',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:07](https://www.youtube.com/watch?v=3tkWRQX9WjI&t=367s)',
      'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE business '
                   'acquisitions (`ETA`), Quality of Earnings (`QoE`), SBA/seller-note '
                   'structuring, and 100-day turnarounds (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re going to typically get a better interest rate. And it's also going to help "
              "you sleep better at night, especially if business is going slow after you're "
              "closing the acquisition of the company that you're buying.",
      'timestamp': 367,
      'timestamp_label': '[00:06:07]',
      'timestamp_seconds': 367,
      'tip': "'re going to typically get a better interest rate. And it's also going to help "
             "you sleep better at night, especially if business is going slow after you're "
             "closing the acquisition of the company that you're buying.",
      'title': 'The New SBA Rules are LIVE: How to Plan Business Acquisition in 2026 (Matthias '
               'Smith)',
      'url': 'https://www.youtube.com/watch?v=3tkWRQX9WjI&t=367s',
      'video_id': '3tkWRQX9WjI'}],
 10: [{'author': 'The Explainer USA - Business & Finance',
       'channel': 'The Explainer USA - Business & Finance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:02](https://www.youtube.com/watch?v=9Kv6npBoTpQ&t=182s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Or, you could even use a holding company model, where you acquire multiple '
               'businesses over time to build economies of scale. Section three, the small '
               'business succession crisis. So, why is this opportunity so incredibly massive '
               'right at this very moment?',
       'timestamp': 182,
       'timestamp_label': '[00:03:02]',
       'timestamp_seconds': 182,
       'tip': 'Or, you could even use a holding company model, where you acquire multiple '
              'businesses over time to build economies of scale. Section three, the small '
              'business succession crisis. So, why is this opportunity so incredibly massive '
              'right at this very moment?',
       'title': 'Entrepreneurship Through Acquisition: The Smarter Way to Become a CEO? (The '
                'Explainer USA - Business & Finance)',
       'url': 'https://www.youtube.com/watch?v=9Kv6npBoTpQ&t=182s',
       'video_id': '9Kv6npBoTpQ'},
      {'author': 'Jon Stoddard',
       'channel': 'Jon Stoddard',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:26](https://www.youtube.com/watch?v=104miMfvJRg&t=146s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Look at the supplier agreements. Ask what could kill this business in the next '
               "12 months. You wouldn't want to buy a uh bookw writing service knowing AI "
               'could do this for you in minutes. Sometimes an asset purchase deal is safer '
               'than a stock purchase.',
       'timestamp': 146,
       'timestamp_label': '[00:02:26]',
       'timestamp_seconds': 146,
       'tip': 'Look at the supplier agreements. Ask what could kill this business in the next '
              "12 months. You wouldn't want to buy a uh bookw writing service knowing AI could "
              'do this for you in minutes. Sometimes an asset purchase deal is safer than a '
              'stock purchase.',
       'title': 'SBA Loan Personal Guarantee: Protect Yourself Before You Sign (Jon Stoddard)',
       'url': 'https://www.youtube.com/watch?v=104miMfvJRg&t=146s',
       'video_id': '104miMfvJRg'},
      {'author': 'Avi',
       'channel': 'Avi',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:58](https://www.youtube.com/watch?v=cS2OjyHbq8U&t=358s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Reason being this was a long-term acquisition strategy. So they were looking '
               "to buy these businesses and acquire them in a permanent fashion. And so that's "
               'exactly what they were doing. They were looking to build their portfolio.',
       'timestamp': 358,
       'timestamp_label': '[00:05:58]',
       'timestamp_seconds': 358,
       'tip': 'Reason being this was a long-term acquisition strategy. So they were looking to '
              "buy these businesses and acquire them in a permanent fashion. And so that's "
              'exactly what they were doing. They were looking to build their portfolio.',
       'title': "23 Off-Market HVAC Opportunities: Here's Exactly How We Got Them (Private "
                'Equity Case Study) (Avi)',
       'url': 'https://www.youtube.com/watch?v=cS2OjyHbq8U&t=358s',
       'video_id': 'cS2OjyHbq8U'},
      {'author': 'Paper Rich',
       'channel': 'Paper Rich',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:38](https://www.youtube.com/watch?v=Qqgfjq8CujE&t=38s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Buy the shares and they're yours. The company's old debts and lawsuits are "
               "still the company's, and a change of owner doesn't wipe them out. Now picture "
               'buying just the assets instead.',
       'timestamp': 38,
       'timestamp_label': '[00:00:38]',
       'timestamp_seconds': 38,
       'tip': "Buy the shares and they're yours. The company's old debts and lawsuits are "
              "still the company's, and a change of owner doesn't wipe them out. Now picture "
              'buying just the assets instead.',
       'title': 'Part 1 of Acquiring a Business (Asset purchase vs Stock purchase) (Paper '
                'Rich)',
       'url': 'https://www.youtube.com/watch?v=Qqgfjq8CujE&t=38s',
       'video_id': 'Qqgfjq8CujE'},
      {'author': 'Kristina M. Wynne',
       'channel': 'Kristina M. Wynne',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:23](https://www.youtube.com/watch?v=uwpDjf5v_jM&t=143s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A bank can get behind lending money to you for that. Most people need to work '
               "with a lender. If I bought a business tomorrow, I I'm not depleting all of my "
               'cap my liquid capital to buy a business. Not when I can work with a lender and '
               'get a loan.',
       'timestamp': 143,
       'timestamp_label': '[00:02:23]',
       'timestamp_seconds': 143,
       'tip': 'A bank can get behind lending money to you for that. Most people need to work '
              "with a lender. If I bought a business tomorrow, I I'm not depleting all of my "
              'cap my liquid capital to buy a business. Not when I can work with a lender and '
              'get a loan.',
       'title': 'Easy Breakdown of Entrepreneurship Through Acquisition. (Kristina M. Wynne)',
       'url': 'https://www.youtube.com/watch?v=uwpDjf5v_jM&t=143s',
       'video_id': 'uwpDjf5v_jM'},
      {'author': 'SMB Law Group LLP',
       'channel': 'SMB Law Group LLP',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:22:00](https://www.youtube.com/watch?v=OIcTvUbSEgM&t=1320s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re not listing the assets that you're acquiring. You are buying all of the "
               'assets of the business save for what a seller specifically says is not going '
               'to be included. Remember, they know the business extremely well, right? They '
               'know probably every asset, right?',
       'timestamp': 1320,
       'timestamp_label': '[00:22:00]',
       'timestamp_seconds': 1320,
       'tip': "'re not listing the assets that you're acquiring. You are buying all of the "
              'assets of the business save for what a seller specifically says is not going to '
              'be included. Remember, they know the business extremely well, right? They know '
              'probably every asset, right?',
       'title': 'How to Structure a Winning LOI for a Small Business Acquisition (SMB Law '
                'Group LLP)',
       'url': 'https://www.youtube.com/watch?v=OIcTvUbSEgM&t=1320s',
       'video_id': 'OIcTvUbSEgM'},
      {'author': 'FinanceKid',
       'channel': 'FinanceKid',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:08](https://www.youtube.com/watch?v=8AOvKeCdAH0&t=908s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Working capital adjustment and if it's set too low then the bars gonna have to "
               'put more money into the business which means the transaction costed them.',
       'timestamp': 908,
       'timestamp_label': '[00:15:08]',
       'timestamp_seconds': 908,
       'tip': "Working capital adjustment and if it's set too low then the bars gonna have to "
              'put more money into the business which means the transaction costed them.',
       'title': 'Negotiating Net Working Capital Adjustments in M&A – Definitions and How to '
                'Calculate (FinanceKid)',
       'url': 'https://www.youtube.com/watch?v=8AOvKeCdAH0&t=908s',
       'video_id': '8AOvKeCdAH0'},
      {'author': 'Walker Deibel',
       'channel': 'Walker Deibel',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:25](https://www.youtube.com/watch?v=1blBuzvtWoA&t=25s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Get ready because today, we're going to look at some research, and we're going "
               'deep to figure out how to determine that. I am the Wall Street Journal '
               'best-selling author of "Buy Then Build" and creator of the Acquisition Lab.',
       'timestamp': 25,
       'timestamp_label': '[00:00:25]',
       'timestamp_seconds': 25,
       'tip': "Get ready because today, we're going to look at some research, and we're going "
              'deep to figure out how to determine that. I am the Wall Street Journal '
              'best-selling author of "Buy Then Build" and creator of the Acquisition Lab.',
       'title': 'Acquiring a Company vs. Innovating an Industry (Walker Deibel)',
       'url': 'https://www.youtube.com/watch?v=1blBuzvtWoA&t=25s',
       'video_id': '1blBuzvtWoA'},
      {'author': 'DigitalTriggers',
       'channel': 'DigitalTriggers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:19:01](https://www.youtube.com/watch?v=u2bZWIf9b5k&t=1141s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'There is an estimated ten trillion dollars in business assets that need to '
               'change hands as they retire okay they started retiring about two or three.',
       'timestamp': 1141,
       'timestamp_label': '[00:19:01]',
       'timestamp_seconds': 1141,
       'tip': 'There is an estimated ten trillion dollars in business assets that need to '
              'change hands as they retire okay they started retiring about two or three.',
       'title': 'Buying the Right Business & Building It Up - A Guide to Acquisition '
                'Entrepreneurship | Walker Deibel (DigitalTriggers)',
       'url': 'https://www.youtube.com/watch?v=u2bZWIf9b5k&t=1141s',
       'video_id': 'u2bZWIf9b5k'},
      {'author': "Let's Buy a Business",
       'channel': "Let's Buy a Business",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:24](https://www.youtube.com/watch?v=WP5MdYhV05A&t=864s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Create okay and the thing is is that um so if you so if a company's buying "
               "another company it's a coin flip.",
       'timestamp': 864,
       'timestamp_label': '[00:14:24]',
       'timestamp_seconds': 864,
       'tip': "Create okay and the thing is is that um so if you so if a company's buying "
              "another company it's a coin flip.",
       'title': "Buy Then Build: 3 Acquisition Secrets with Walker Deibel | Let's Buy a "
                "Business #83 (Let's Buy a Business)",
       'url': 'https://www.youtube.com/watch?v=WP5MdYhV05A&t=864s',
       'video_id': 'WP5MdYhV05A'},
      {'author': 'Acquiring Minds',
       'channel': 'Acquiring Minds',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=c1OtHjDpymM&t=15s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Having us Royce Rick you are the co-authors of a book that is read by '
               'literally almost everyone considering buying a small business in.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Having us Royce Rick you are the co-authors of a book that is read by literally '
              'almost everyone considering buying a small business in.',
       'title': 'The 2 Professors Who Helped Start the ETA Movement | Royce Yudkoff & Rick '
                'Ruback Interview (Acquiring Minds)',
       'url': 'https://www.youtube.com/watch?v=c1OtHjDpymM&t=15s',
       'video_id': 'c1OtHjDpymM'},
      {'author': 'Before You Buy or Sell a Business Podcast',
       'channel': 'Before You Buy or Sell a Business Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:47](https://www.youtube.com/watch?v=Hh83Lc7sWf4&t=287s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Friends are going to back me and I'm going to find a business and at that "
               'point we were doing a lot of like really small deals like so think a mechanic.',
       'timestamp': 287,
       'timestamp_label': '[00:04:47]',
       'timestamp_seconds': 287,
       'tip': "Friends are going to back me and I'm going to find a business and at that point "
              'we were doing a lot of like really small deals like so think a mechanic.',
       'title': 'Navigating Entrepreneurship Through Acquisition | Ep. 43 Part 1 | Before You '
                'Buy or Sell a Business (Before You Buy or Sell a Business Podcast)',
       'url': 'https://www.youtube.com/watch?v=Hh83Lc7sWf4&t=287s',
       'video_id': 'Hh83Lc7sWf4'},
      {'author': 'PwC US',
       'channel': 'PwC US',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:28:44](https://www.youtube.com/watch?v=b43cWRS8RKE&t=1724s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Wherever you listen to your podcasts and to stay up todate on all the latest '
               'accounting and reporting news sign up for our newsletter at viewpoint. pwc.com '
               "from thought leadership at PWC I'm I'm Heather horn thanks for tuning.",
       'timestamp': 1724,
       'timestamp_label': '[00:28:44]',
       'timestamp_seconds': 1724,
       'tip': 'Wherever you listen to your podcasts and to stay up todate on all the latest '
              'accounting and reporting news sign up for our newsletter at viewpoint. pwc.com '
              "from thought leadership at PWC I'm I'm Heather horn thanks for tuning.",
       'title': 'Fixed asset toolkit: Asset acquisitions (PwC US)',
       'url': 'https://www.youtube.com/watch?v=b43cWRS8RKE&t=1724s',
       'video_id': 'b43cWRS8RKE'},
      {'author': 'Jake & Gino',
       'channel': 'Jake & Gino',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:23](https://www.youtube.com/watch?v=xpFa8hcRy_k&t=923s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Intelligent like in the market cycle is just so interesting just to Loop it '
               'back around and land it um the thing is is that when I get a pro forma from a '
               "seller I don't wipe my backside with it because it's an insult to my backside "
               "[Laughter] that's for him.",
       'timestamp': 923,
       'timestamp_label': '[00:15:23]',
       'timestamp_seconds': 923,
       'tip': 'Intelligent like in the market cycle is just so interesting just to Loop it '
              'back around and land it um the thing is is that when I get a pro forma from a '
              "seller I don't wipe my backside with it because it's an insult to my backside "
              "[Laughter] that's for him.",
       'title': "Master the 'Moneyball' of Business: Unveiling Acquisition Entrepreneurship "
                'with Walker Deibel (Jake & Gino)',
       'url': 'https://www.youtube.com/watch?v=xpFa8hcRy_k&t=923s',
       'video_id': 'xpFa8hcRy_k'},
      {'author': 'The Money Rules',
       'channel': 'The Money Rules',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:10](https://www.youtube.com/watch?v=DyCKwhKRtK0&t=70s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "If you're buying a business you've never owned, and you haven't worked there "
               "for at least two years, you're an initial acquisition. That's the default "
               "type, and it's the strictest one. A viewer asked if an SBA loan can even buy "
               'an existing business.',
       'timestamp': 70,
       'timestamp_label': '[00:01:10]',
       'timestamp_seconds': 70,
       'tip': "If you're buying a business you've never owned, and you haven't worked there "
              "for at least two years, you're an initial acquisition. That's the default type, "
              "and it's the strictest one. A viewer asked if an SBA loan can even buy an "
              'existing business.',
       'title': 'SBA Loan to Buy a Business: What Changed on October 1, 2026 (The Money Rules)',
       'url': 'https://www.youtube.com/watch?v=DyCKwhKRtK0&t=70s',
       'video_id': 'DyCKwhKRtK0'}],
 11: [{'author': 'Escamilla Law Office',
       'channel': 'Escamilla Law Office',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:48](https://www.youtube.com/watch?v=ZGklOUqHKYg&t=408s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'After closing, the buyer may hire more employees, change compensation, add '
               'management, increase advertising, change corporate overhead, change accounting '
               'systems, or spend money integrating the business. Those may all be reasonable '
               'decisions, but they can also reduce IBIDA.',
       'timestamp': 408,
       'timestamp_label': '[00:06:48]',
       'timestamp_seconds': 408,
       'tip': 'After closing, the buyer may hire more employees, change compensation, add '
              'management, increase advertising, change corporate overhead, change accounting '
              'systems, or spend money integrating the business. Those may all be reasonable '
              'decisions, but they can also reduce IBIDA.',
       'title': 'Earnouts vs Seller Financing - How to Document Each (Escamilla Law Office)',
       'url': 'https://www.youtube.com/watch?v=ZGklOUqHKYg&t=408s',
       'video_id': 'ZGklOUqHKYg'},
      {'author': 'Kevin Henderson',
       'channel': 'Kevin Henderson',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:17](https://www.youtube.com/watch?v=YXFpxJrIjD0&t=137s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'If you buy an existing business, you buy a business that has 10, 15, 30, '
               'potentially more years of historical operations. The business is probably '
               "already profitable or I'm going to guess you're not looking at buying it. Uh "
               'that addresses your cash flow problem.',
       'timestamp': 137,
       'timestamp_label': '[00:02:17]',
       'timestamp_seconds': 137,
       'tip': 'If you buy an existing business, you buy a business that has 10, 15, 30, '
              'potentially more years of historical operations. The business is probably '
              "already profitable or I'm going to guess you're not looking at buying it. Uh "
              'that addresses your cash flow problem.',
       'title': 'What is Entrepreneurship through Acquisition? (Kevin Henderson)',
       'url': 'https://www.youtube.com/watch?v=YXFpxJrIjD0&t=137s',
       'video_id': 'YXFpxJrIjD0'},
      {'author': 'acquiredotcom',
       'channel': 'acquiredotcom',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:04](https://www.youtube.com/watch?v=qjwlutaiugE&t=364s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'We do have a fantastic team that is more than willing to connect and speak '
               'with you about buying or selling so definitely feel free to reach out and I '
               'hope you enjoy your experience on acquire.com Cheers foreign.',
       'timestamp': 364,
       'timestamp_label': '[00:06:04]',
       'timestamp_seconds': 364,
       'tip': 'We do have a fantastic team that is more than willing to connect and speak with '
              'you about buying or selling so definitely feel free to reach out and I hope you '
              'enjoy your experience on acquire.com Cheers foreign.',
       'title': 'Acquire.com - How It Works (acquiredotcom)',
       'url': 'https://www.youtube.com/watch?v=qjwlutaiugE&t=364s',
       'video_id': 'qjwlutaiugE'},
      {'author': "Prince George's Chamber of Commerce",
       'channel': "Prince George's Chamber of Commerce",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:37:26](https://www.youtube.com/watch?v=QtvW_tq7sAQ&t=2246s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It's the concept of other people's money or other capital stacks that you use. "
               'But you need money >> to buy a business. Now, >> one more time, you need '
               'money. You want >> You need money to dig into, right?',
       'timestamp': 2246,
       'timestamp_label': '[00:37:26]',
       'timestamp_seconds': 2246,
       'tip': "It's the concept of other people's money or other capital stacks that you use. "
              'But you need money >> to buy a business. Now, >> one more time, you need money. '
              'You want >> You need money to dig into, right?',
       'title': 'Buy a Business Instead of Starting One | Entrepreneurship Through Acquisition '
                "(ETA) (Prince George's Chamber of Commerce)",
       'url': 'https://www.youtube.com/watch?v=QtvW_tq7sAQ&t=2246s',
       'video_id': 'QtvW_tq7sAQ'},
      {'author': 'SBA University',
       'channel': 'SBA University',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:51](https://www.youtube.com/watch?v=92Nd2yD33As&t=111s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "10 years and now you're about to buy a business that allow you to keep doing "
               'it but in ownership capacity. Direct industry experience that demonstrates '
               'that you know this industry, you know the operations, you just know how it '
               'works.',
       'timestamp': 111,
       'timestamp_label': '[00:01:51]',
       'timestamp_seconds': 111,
       'tip': "10 years and now you're about to buy a business that allow you to keep doing it "
              'but in ownership capacity. Direct industry experience that demonstrates that '
              'you know this industry, you know the operations, you just know how it works.',
       'title': 'What a Perfect Business Acquisition Application Looks Like | SBA Loans (SBA '
                'University)',
       'url': 'https://www.youtube.com/watch?v=92Nd2yD33As&t=111s',
       'video_id': '92Nd2yD33As'},
      {'author': 'Neo Expertise',
       'channel': 'Neo Expertise',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:57](https://www.youtube.com/watch?v=4kQ8R30J5q4&t=177s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'We reconcile the balances, build the mapping, chase the documentation with the '
               'local finance team, and get your first group package out. Capacity, not a '
               'report you have to act on later. So, if you are inside the first 100 days, do '
               'not spend them alone.',
       'timestamp': 177,
       'timestamp_label': '[00:02:57]',
       'timestamp_seconds': 177,
       'tip': 'We reconcile the balances, build the mapping, chase the documentation with the '
              'local finance team, and get your first group package out. Capacity, not a '
              'report you have to act on later. So, if you are inside the first 100 days, do '
              'not spend them alone.',
       'title': 'Post-Acquisition Finance Integration: First 100 Days Checklist '
                '#PostAcquisitionIntegration (Neo Expertise)',
       'url': 'https://www.youtube.com/watch?v=4kQ8R30J5q4&t=177s',
       'video_id': '4kQ8R30J5q4'},
      {'author': 'CandiMentor',
       'channel': 'CandiMentor',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:38](https://www.youtube.com/watch?v=siH_wi11PX8&t=38s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'From there, the team builds a monthly history, identifies unusual movements, '
               'establishes a normalized target, and calculates the deal impact. A buyer wants '
               'to know how much cash the business normally needs to operate after closing.',
       'timestamp': 38,
       'timestamp_label': '[00:00:38]',
       'timestamp_seconds': 38,
       'tip': 'From there, the team builds a monthly history, identifies unusual movements, '
              'establishes a normalized target, and calculates the deal impact. A buyer wants '
              'to know how much cash the business normally needs to operate after closing.',
       'title': 'Financial Due Diligence Working Capital Analysis: Practical Case Study '
                '(CandiMentor)',
       'url': 'https://www.youtube.com/watch?v=siH_wi11PX8&t=38s',
       'video_id': 'siH_wi11PX8'},
      {'author': 'Pioneer Capital Advisory LLC',
       'channel': 'Pioneer Capital Advisory LLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:49:30](https://www.youtube.com/watch?v=WF2-6ODNQms&t=2970s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re buying, which would be determined based on third party business valuation, "
               'and then any difference you could bridge with equity and, and seller '
               'financing.',
       'timestamp': 2970,
       'timestamp_label': '[00:49:30]',
       'timestamp_seconds': 2970,
       'tip': "'re buying, which would be determined based on third party business valuation, "
              'and then any difference you could bridge with equity and, and seller financing.',
       'title': 'SBA SOP 50 10 8.1: The New Rules for Buying a Business (Effective Oct 1, '
                '2026) (Pioneer Capital Advisory LLC)',
       'url': 'https://www.youtube.com/watch?v=WF2-6ODNQms&t=2970s',
       'video_id': 'WF2-6ODNQms'},
      {'author': 'Elliott Holland',
       'channel': 'Elliott Holland',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:16](https://www.youtube.com/watch?v=KJPGQ94h_GY&t=76s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'t have time to reconcile and validate while you're trying to raise capital, "
               'talk to lenders, talk to equity, understand the business, visit the seller, '
               "understand the operations, figure out how you're going to move to the "
               'location, and all these other things.',
       'timestamp': 76,
       'timestamp_label': '[00:01:16]',
       'timestamp_seconds': 76,
       'tip': "'t have time to reconcile and validate while you're trying to raise capital, "
              'talk to lenders, talk to equity, understand the business, visit the seller, '
              "understand the operations, figure out how you're going to move to the location, "
              'and all these other things.',
       'title': 'Quality of Earnings Explained (Elliott Holland)',
       'url': 'https://www.youtube.com/watch?v=KJPGQ94h_GY&t=76s',
       'video_id': 'KJPGQ94h_GY'},
      {'author': 'John Colley | The Investment Banking Practitioner',
       'channel': 'John Colley | The Investment Banking Practitioner',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:38](https://www.youtube.com/watch?v=zQE4R-z6Yww&t=398s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Normalized EBITDA feeds directly into the valuation. Adjustment categories '
               'feed into the working capital mechanism. And specific findings like the below '
               'market lease feed into the share purchase agreement as negotiation points. '
               "Here's what I want you to remember.",
       'timestamp': 398,
       'timestamp_label': '[00:06:38]',
       'timestamp_seconds': 398,
       'tip': 'Normalized EBITDA feeds directly into the valuation. Adjustment categories feed '
              'into the working capital mechanism. And specific findings like the below market '
              "lease feed into the share purchase agreement as negotiation points. Here's what "
              'I want you to remember.',
       'title': "How to Read a Quality of Earnings Report (M&A Practitioner's Method) (John "
                'Colley | The Investment Banking Practitioner)',
       'url': 'https://www.youtube.com/watch?v=zQE4R-z6Yww&t=398s',
       'video_id': 'zQE4R-z6Yww'},
      {'author': 'Letters of Intent',
       'channel': 'Letters of Intent',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:17](https://www.youtube.com/watch?v=VuuLz-8NiYg&t=737s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re asking for seller financing, that that usually means they can't get a loan "
               'from the bank, which is a red flag. I mean, there are times where there are '
               "related party transactions. Maybe someone who's a manager of a business is "
               'taking over and wants seller financing.',
       'timestamp': 737,
       'timestamp_label': '[00:12:17]',
       'timestamp_seconds': 737,
       'tip': "'re asking for seller financing, that that usually means they can't get a loan "
              'from the bank, which is a red flag. I mean, there are times where there are '
              "related party transactions. Maybe someone who's a manager of a business is "
              'taking over and wants seller financing.',
       'title': 'SPECIAL EPISODE - Structuring the Deal: Letters of Intent Explained (Letters '
                'of Intent)',
       'url': 'https://www.youtube.com/watch?v=VuuLz-8NiYg&t=737s',
       'video_id': 'VuuLz-8NiYg'},
      {'author': 'Built to Sell',
       'channel': 'Built to Sell',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=GYvpRW21sSY&t=15s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'That they were looking to um transition the business to the next group of '
               'owners however over time became very disillusioned with the typical exit.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'That they were looking to um transition the business to the next group of '
              'owners however over time became very disillusioned with the typical exit.',
       'title': 'How search fund operators convince owners to sell their business with Steve '
                'Divitikos (Built to Sell)',
       'url': 'https://www.youtube.com/watch?v=GYvpRW21sSY&t=15s',
       'video_id': 'GYvpRW21sSY'},
      {'author': 'Chris Barsness - Securities Law Media',
       'channel': 'Chris Barsness - Securities Law Media',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:14](https://www.youtube.com/watch?v=-DthgkqGsGA&t=494s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Again buyers usually like to do asset purchases sellers prefer to do stock or '
               "ownership interest purchases because they're a little bit more free and clear "
               'of the prior company but a lot of issues come into play so these are all '
               'things that we go over with our clients.',
       'timestamp': 494,
       'timestamp_label': '[00:08:14]',
       'timestamp_seconds': 494,
       'tip': 'Again buyers usually like to do asset purchases sellers prefer to do stock or '
              "ownership interest purchases because they're a little bit more free and clear "
              'of the prior company but a lot of issues come into play so these are all things '
              'that we go over with our clients.',
       'title': 'Asset purchase or stock purchase? (Chris Barsness - Securities Law Media)',
       'url': 'https://www.youtube.com/watch?v=-DthgkqGsGA&t=494s',
       'video_id': '-DthgkqGsGA'},
      {'author': 'A Simple Model',
       'channel': 'A Simple Model',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:21](https://www.youtube.com/watch?v=mADDz83tbN0&t=201s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'It will give you a better understanding of why this document is so critical '
               'and why someone would fly around the country waiting in hotel rooms to '
               "negotiate it all right team that's all for now thanks for watching.",
       'timestamp': 201,
       'timestamp_label': '[00:03:21]',
       'timestamp_seconds': 201,
       'tip': 'It will give you a better understanding of why this document is so critical and '
              'why someone would fly around the country waiting in hotel rooms to negotiate it '
              "all right team that's all for now thanks for watching.",
       'title': 'Private Equity Letter Of Intent Negotiation | Favorite LOI Negotiation Story '
                '(A Simple Model)',
       'url': 'https://www.youtube.com/watch?v=mADDz83tbN0&t=201s',
       'video_id': 'mADDz83tbN0'},
      {'author': 'Mind Of Monte',
       'channel': 'Mind Of Monte',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:37](https://www.youtube.com/watch?v=MVmF4HlTHGM&t=97s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Maybe they have complementary customers, maybe it's a profitable business that "
               "can be easily run by the management team you have in place. There's a number "
               'of ways that you could possibly acquire a small business.',
       'timestamp': 97,
       'timestamp_label': '[00:01:37]',
       'timestamp_seconds': 97,
       'tip': "Maybe they have complementary customers, maybe it's a profitable business that "
              "can be easily run by the management team you have in place. There's a number of "
              'ways that you could possibly acquire a small business.',
       'title': 'How to Buy Boomer Business With No Competition (Mind Of Monte)',
       'url': 'https://www.youtube.com/watch?v=MVmF4HlTHGM&t=97s',
       'video_id': 'MVmF4HlTHGM'}],
 12: [{'author': 'Brett Cenkus',
       'channel': 'Brett Cenkus',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:44](https://www.youtube.com/watch?v=lPy47SFZqDw&t=224s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'t know exactly what the working capital is in the business on the closing "
               "date you just know what the target is, that's why we call it a target and in "
               "the 90 days or something after closing it gets trued up and that's the working "
               'capital adjustment.',
       'timestamp': 224,
       'timestamp_label': '[00:03:44]',
       'timestamp_seconds': 224,
       'tip': "'t know exactly what the working capital is in the business on the closing date "
              "you just know what the target is, that's why we call it a target and in the 90 "
              "days or something after closing it gets trued up and that's the working capital "
              'adjustment.',
       'title': 'Working Capital: Targets & Adjustments (Brett Cenkus)',
       'url': 'https://www.youtube.com/watch?v=lPy47SFZqDw&t=224s',
       'video_id': 'lPy47SFZqDw'},
      {'author': 'Bridgeyard',
       'channel': 'Bridgeyard',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=wjVsYwI5G_E&t=20s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Seven decisions that create a workable integration plan before you start '
               'moving systems. We will use a fictional company with 100 employees across '
               'three sites. The sequence is a planning example, not a promise that every '
               'acquisition can be ready in 30 days.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'Seven decisions that create a workable integration plan before you start moving '
              'systems. We will use a fictional company with 100 employees across three sites. '
              'The sequence is a planning example, not a promise that every acquisition can be '
              'ready in 30 days.',
       'title': 'The First 30 Days After an Acquisition: What IT Must Decide Before Migration '
                '(Bridgeyard)',
       'url': 'https://www.youtube.com/watch?v=wjVsYwI5G_E&t=20s',
       'video_id': 'wjVsYwI5G_E'},
      {'author': 'Dean Street Law',
       'channel': 'Dean Street Law',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:27:37](https://www.youtube.com/watch?v=ScOjsEfBwZQ&t=1657s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And then the next chapter is on post-closing integration and transition '
               'planning. What you can be expecting to do postc closing your 100 day plan '
               'communications with employees, customers, suppliers.',
       'timestamp': 1657,
       'timestamp_label': '[00:27:37]',
       'timestamp_seconds': 1657,
       'tip': 'And then the next chapter is on post-closing integration and transition '
              'planning. What you can be expecting to do postc closing your 100 day plan '
              'communications with employees, customers, suppliers.',
       'title': 'Entrepreneurship Through Acquisition: A Legal Guide to Buying a Small '
                'Business // Ep 32 of DWLD (Dean Street Law)',
       'url': 'https://www.youtube.com/watch?v=ScOjsEfBwZQ&t=1657s',
       'video_id': 'ScOjsEfBwZQ'},
      {'author': 'Lighthouse Capital',
       'channel': 'Lighthouse Capital',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:07](https://www.youtube.com/watch?v=slGlxgrDvps&t=127s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Let's look at section 3, the three-stage action plan. Now, there is some old "
               'data from a 2013 Grant Thornton and PitchBook survey showing almost 90% of '
               'private equity firms claim to use a 100-day plan. But, honestly, having a '
               "theoretical plan just isn't enough.",
       'timestamp': 127,
       'timestamp_label': '[00:02:07]',
       'timestamp_seconds': 127,
       'tip': "Let's look at section 3, the three-stage action plan. Now, there is some old "
              'data from a 2013 Grant Thornton and PitchBook survey showing almost 90% of '
              'private equity firms claim to use a 100-day plan. But, honestly, having a '
              "theoretical plan just isn't enough.",
       'title': 'The First 100 Days After a Private Equity Deal: What LPs Should Check '
                '(Lighthouse Capital)',
       'url': 'https://www.youtube.com/watch?v=slGlxgrDvps&t=127s',
       'video_id': 'slGlxgrDvps'},
      {'author': 'CandiMentor',
       'channel': 'CandiMentor',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:32](https://www.youtube.com/watch?v=QVDTq7Qd6-A&t=272s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You start with the reported number, add only supported items, remove anything '
               'questionable, and check that the same benefit has not been counted twice. '
               'Working capital connects accounting earnings with the cash required to run the '
               'business.',
       'timestamp': 272,
       'timestamp_label': '[00:04:32]',
       'timestamp_seconds': 272,
       'tip': 'You start with the reported number, add only supported items, remove anything '
              'questionable, and check that the same benefit has not been counted twice. '
              'Working capital connects accounting earnings with the cash required to run the '
              'business.',
       'title': 'Quality of Earnings (QoE) vs EBITDA | Key Differences Explained (CandiMentor)',
       'url': 'https://www.youtube.com/watch?v=QVDTq7Qd6-A&t=272s',
       'video_id': 'QVDTq7Qd6-A'},
      {'author': 'Lighthouse Capital',
       'channel': 'Lighthouse Capital',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:39](https://www.youtube.com/watch?v=OwAOc9xgv9U&t=39s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': '13 week cash flow forecast, requiring two signatures on every bank account, '
               "and completing a monthly close within 10 business days. Then we'll look at the "
               'Day 30 Control Memo, which is the single document that proves it all to '
               "investors. Let's jump right into the forecast.",
       'timestamp': 39,
       'timestamp_label': '[00:00:39]',
       'timestamp_seconds': 39,
       'tip': '13 week cash flow forecast, requiring two signatures on every bank account, and '
              "completing a monthly close within 10 business days. Then we'll look at the Day "
              '30 Control Memo, which is the single document that proves it all to investors. '
              "Let's jump right into the forecast.",
       'title': 'Post-Acquisition Financial Controls: The First 30 Days (Lighthouse Capital)',
       'url': 'https://www.youtube.com/watch?v=OwAOc9xgv9U&t=39s',
       'video_id': 'OwAOc9xgv9U'},
      {'author': 'Oberman Law Firm',
       'channel': 'Oberman Law Firm',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:32](https://www.youtube.com/watch?v=6uqSoqOVnsg&t=152s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s going to take a significant significant financial disclosures, legal "
               "reviews. This takes months and months of negotiation. It doesn't happen like "
               "in 10 days. So, before you buy a business, whether you're on a buy-sell side, "
               "it doesn't really It doesn't matter, right?",
       'timestamp': 152,
       'timestamp_label': '[00:02:32]',
       'timestamp_seconds': 152,
       'tip': "'s going to take a significant significant financial disclosures, legal "
              "reviews. This takes months and months of negotiation. It doesn't happen like in "
              "10 days. So, before you buy a business, whether you're on a buy-sell side, it "
              "doesn't really It doesn't matter, right?",
       'title': 'Why a Letter of Intent Is Critical to the Sale of a Business (Oberman Law '
                'Firm)',
       'url': 'https://www.youtube.com/watch?v=6uqSoqOVnsg&t=152s',
       'video_id': '6uqSoqOVnsg'},
      {'author': 'Figuring Out with Rahul',
       'channel': 'Figuring Out with Rahul',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:31](https://www.youtube.com/watch?v=xgCInPpZDiQ&t=271s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'First up is networking capital or NWC. This is a crucial check that answers a '
               'really simple question. Does this business have enough fuel in the tank to '
               'operate on day one?',
       'timestamp': 271,
       'timestamp_label': '[00:04:31]',
       'timestamp_seconds': 271,
       'tip': 'First up is networking capital or NWC. This is a crucial check that answers a '
              'really simple question. Does this business have enough fuel in the tank to '
              'operate on day one?',
       'title': 'Quality of Earnings Analysis in Mergers and Acquisitions || CFA (Figuring Out '
                'with Rahul)',
       'url': 'https://www.youtube.com/watch?v=xgCInPpZDiQ&t=271s',
       'video_id': 'xgCInPpZDiQ'},
      {'author': 'Dennis Unrein / SMB PE LLC',
       'channel': 'Dennis Unrein / SMB PE LLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:30:40](https://www.youtube.com/watch?v=PF2SOneLrJ0&t=1840s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Usually comes out of the escrow so let's say after closing 60 to 90 days we "
               "calculate the working capital and we do what's called a true up and it "
               'actually.',
       'timestamp': 1840,
       'timestamp_label': '[00:30:40]',
       'timestamp_seconds': 1840,
       'tip': "Usually comes out of the escrow so let's say after closing 60 to 90 days we "
              "calculate the working capital and we do what's called a true up and it "
              'actually.',
       'title': 'SMB PE Experts: The Essential Guide To The Letter Of Intent ("LOI") in M&A – '
                'Advice from a Lawyer (Dennis Unrein / SMB PE LLC)',
       'url': 'https://www.youtube.com/watch?v=PF2SOneLrJ0&t=1840s',
       'video_id': 'PF2SOneLrJ0'},
      {'author': 'Walker Deibel',
       'channel': 'Walker Deibel',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:38](https://www.youtube.com/watch?v=fFDPLnXTi0o&t=218s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re buying a successful business with employees, customers and vendors and a "
               "nice cash flow is making changes. You're buying it for a reason. No, you know "
               "like, I think that changes aren't needed but not in the first 30-60 days.",
       'timestamp': 218,
       'timestamp_label': '[00:03:38]',
       'timestamp_seconds': 218,
       'tip': "'re buying a successful business with employees, customers and vendors and a "
              "nice cash flow is making changes. You're buying it for a reason. No, you know "
              "like, I think that changes aren't needed but not in the first 30-60 days.",
       'title': 'Everything you need to know about Post Acquisition and Execution (Walker '
                'Deibel)',
       'url': 'https://www.youtube.com/watch?v=fFDPLnXTi0o&t=218s',
       'video_id': 'fFDPLnXTi0o'},
      {'author': 'Kirk Michie',
       'channel': 'Kirk Michie',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:12](https://www.youtube.com/watch?v=BHyx6-mgFe8&t=132s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Taxes appreciation and amortization to get to kind of an adjustability we have '
               'a ton of resources in this area some we have internally a lot we have in our '
               'national network so if we can be helpful here please reach out to us '
               'candorhyphenadvisors.com have a great week.',
       'timestamp': 132,
       'timestamp_label': '[00:02:12]',
       'timestamp_seconds': 132,
       'tip': 'Taxes appreciation and amortization to get to kind of an adjustability we have '
              'a ton of resources in this area some we have internally a lot we have in our '
              'national network so if we can be helpful here please reach out to us '
              'candorhyphenadvisors.com have a great week.',
       'title': 'Add Backs for Adjusted EBITDA (Kirk Michie)',
       'url': 'https://www.youtube.com/watch?v=BHyx6-mgFe8&t=132s',
       'video_id': 'BHyx6-mgFe8'},
      {'author': 'David C Barnett Small Business and Deal Making SMB',
       'channel': 'David C Barnett Small Business and Deal Making SMB',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:17](https://www.youtube.com/watch?v=PO1M-_wq-m4&t=317s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Acquiring your business which you know very well and they're going to start "
               "running it and they're going to now have this debt.",
       'timestamp': 317,
       'timestamp_label': '[00:05:17]',
       'timestamp_seconds': 317,
       'tip': "Acquiring your business which you know very well and they're going to start "
              "running it and they're going to now have this debt.",
       'title': 'Why Would a Seller Want to Finance the Deal? Owner Will Carry Seller '
                'Financing | business broker smb (David C Barnett Small Business and Deal '
                'Making SMB)',
       'url': 'https://www.youtube.com/watch?v=PO1M-_wq-m4&t=317s',
       'video_id': 'PO1M-_wq-m4'},
      {'author': 'Acquiring Minds',
       'channel': 'Acquiring Minds',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:56:05](https://www.youtube.com/watch?v=KT5T3j2jVQ4&t=3365s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Easy to start a business in that space But if the total addressable Market is '
               '150 or 200 million dollars and your business is making five million dollars.',
       'timestamp': 3365,
       'timestamp_label': '[00:56:05]',
       'timestamp_seconds': 3365,
       'tip': 'Easy to start a business in that space But if the total addressable Market is '
              '150 or 200 million dollars and your business is making five million dollars.',
       'title': 'The Self Funded Search Model | Robert Graham & Jordan carter (Acquiring '
                'Minds)',
       'url': 'https://www.youtube.com/watch?v=KT5T3j2jVQ4&t=3365s',
       'video_id': 'KT5T3j2jVQ4'},
      {'author': 'Walker Deibel',
       'channel': 'Walker Deibel',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:31](https://www.youtube.com/watch?v=aoPPGxWI8dY&t=511s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Day I mean we you know we pay low six figures for all the advisory calls that '
               "you know are given out to everybody and it's really the diamond approach to "
               "finding your truth and finding that business that's right for you thanks so "
               "much we'll see you on the inside.",
       'timestamp': 511,
       'timestamp_label': '[00:08:31]',
       'timestamp_seconds': 511,
       'tip': 'Day I mean we you know we pay low six figures for all the advisory calls that '
              "you know are given out to everybody and it's really the diamond approach to "
              "finding your truth and finding that business that's right for you thanks so "
              "much we'll see you on the inside.",
       'title': 'New to Buying Businesses? Here’s What NOT to Do (Walker Deibel)',
       'url': 'https://www.youtube.com/watch?v=aoPPGxWI8dY&t=511s',
       'video_id': 'aoPPGxWI8dY'},
      {'author': 'John Colley | The Investment Banking Practitioner',
       'channel': 'John Colley | The Investment Banking Practitioner',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:44](https://www.youtube.com/watch?v=ha9dRzcYak4&t=164s)',
       'relevance': 'Attributed practitioner commentary on cash-flowing SMB & Micro-PE '
                    'business acquisitions (`ETA`), Quality of Earnings (`QoE`), '
                    'SBA/seller-note structuring, and 100-day turnarounds (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Start with normalized EBITDA. Subtract maintenance CapEx, the minimum '
               'investment needed to keep the asset base running. Subtract the annual working '
               'capital change. That gives you unlevered free cash flow. This is the cash the '
               'business generates for all capital providers.',
       'timestamp': 164,
       'timestamp_label': '[00:02:44]',
       'timestamp_seconds': 164,
       'tip': 'Start with normalized EBITDA. Subtract maintenance CapEx, the minimum '
              'investment needed to keep the asset base running. Subtract the annual working '
              'capital change. That gives you unlevered free cash flow. This is the cash the '
              'business generates for all capital providers.',
       'title': 'EBITDA Is an Opinion. Cash Flow Is a Fact. (M&A Practitioner Walkthrough) '
                '(John Colley | The Investment Banking Practitioner)',
       'url': 'https://www.youtube.com/watch?v=ha9dRzcYak4&t=164s',
       'video_id': 'ha9dRzcYak4'}]}
