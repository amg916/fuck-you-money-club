"""Curated 180-citation Freight Brokerage baseline (15 per chapter across Q1-Q12) mined strictly from verified Freight Brokerage YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'371',
     '75000',
     'accessorial',
     'agent',
     'amendment',
     'ansonia',
     'ascendtms',
     'authority',
     'bad',
     'billing',
     'bmc',
     'bond',
     'boot',
     'broker',
     'brokerage',
     'brokering',
     'brown',
     'business',
     'calling',
     'camp',
     'capital',
     'cargo',
     'carmack',
     'carrier411',
     'carriers',
     'cfr',
     'checking',
     'claim',
     'client',
     'clients',
     'cold',
     'commission',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'371',
     '75000',
     'accessorial',
     'agent',
     'amendment',
     'ansonia',
     'ascendtms',
     'authority',
     'bad',
     'billing',
     'bmc',
     'bond',
     'boot',
     'broker',
     'brokerage',
     'brokering',
     'brown',
     'budget',
     'business',
     'buyer',
     'calling',
     'camp',
     'capital',
     'cargo',
     'carmack',
     'carrier411',
     'carriers',
     'cfr',
     'checking',
     'claim',
     'cold',
     'commission',
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
 3: {'371',
     '75000',
     'accessorial',
     'agent',
     'amendment',
     'ansonia',
     'ascendtms',
     'authority',
     'bad',
     'billing',
     'bmc',
     'bond',
     'boot',
     'broker',
     'brokerage',
     'brokering',
     'brown',
     'business',
     'calling',
     'camp',
     'capital',
     'cargo',
     'carmack',
     'carrier411',
     'carriers',
     'cash',
     'cashflow',
     'cfr',
     'checking',
     'claim',
     'cold',
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
 4: {'371',
     '75000',
     'accessorial',
     'agent',
     'amendment',
     'ansonia',
     'ascendtms',
     'authority',
     'bad',
     'billing',
     'bmc',
     'bond',
     'boot',
     'broker',
     'brokerage',
     'brokering',
     'brown',
     'budget',
     'business',
     'calling',
     'camp',
     'capital',
     'cargo',
     'carmack',
     'carrier411',
     'carriers',
     'cfr',
     'checking',
     'claim',
     'cold',
     'commission',
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
 5: {'371',
     '75000',
     'accessorial',
     'agent',
     'amendment',
     'ansonia',
     'ascendtms',
     'audit',
     'authority',
     'avoid',
     'bad',
     'billing',
     'bmc',
     'bond',
     'boot',
     'broker',
     'brokerage',
     'brokering',
     'brown',
     'business',
     'calling',
     'camp',
     'capital',
     'cargo',
     'carmack',
     'carrier411',
     'carriers',
     'cfr',
     'checking',
     'claim',
     'clawback',
     'cold',
     'commission',
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
 6: {'371',
     '75000',
     'accessorial',
     'agent',
     'amendment',
     'ansonia',
     'ascendtms',
     'authority',
     'bad',
     'billing',
     'bmc',
     'bond',
     'boot',
     'broker',
     'brokerage',
     'brokering',
     'brown',
     'business',
     'calling',
     'camp',
     'capital',
     'cargo',
     'carmack',
     'carrier411',
     'carriers',
     'cfr',
     'checking',
     'claim',
     'client',
     'cold',
     'commission',
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
 7: {'371',
     '75000',
     'accessorial',
     'agent',
     'amendment',
     'ansonia',
     'ascendtms',
     'authority',
     'bad',
     'billing',
     'bmc',
     'bond',
     'boot',
     'broker',
     'brokerage',
     'brokering',
     'brown',
     'business',
     'calling',
     'camp',
     'capital',
     'cargo',
     'carmack',
     'carrier411',
     'carriers',
     'cfr',
     'checking',
     'checklist',
     'claim',
     'cold',
     'commission',
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
 8: {'371',
     '75000',
     'accessorial',
     'agent',
     'amendment',
     'ansonia',
     'api',
     'ascendtms',
     'authority',
     'bad',
     'billing',
     'bmc',
     'bond',
     'boot',
     'broker',
     'brokerage',
     'brokering',
     'brown',
     'business',
     'calling',
     'camp',
     'capital',
     'cargo',
     'carmack',
     'carrier411',
     'carriers',
     'cfr',
     'checking',
     'claim',
     'cold',
     'commission',
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
 9: {'371',
     '75000',
     'accessorial',
     'agent',
     'agreement',
     'amendment',
     'ansonia',
     'ascendtms',
     'authority',
     'bad',
     'billing',
     'bmc',
     'bond',
     'boot',
     'broker',
     'brokerage',
     'brokering',
     'brown',
     'business',
     'calling',
     'camp',
     'capital',
     'cargo',
     'carmack',
     'carrier411',
     'carriers',
     'cfr',
     'checking',
     'claim',
     'cold',
     'commission',
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
 10: {'371',
      '75000',
      'accessorial',
      'agent',
      'ai',
      'amendment',
      'ansonia',
      'ascendtms',
      'authority',
      'automate',
      'automation',
      'bad',
      'billing',
      'bmc',
      'bond',
      'boot',
      'broker',
      'brokerage',
      'brokering',
      'brown',
      'business',
      'calling',
      'camp',
      'capital',
      'cargo',
      'carmack',
      'carrier411',
      'carriers',
      'cfr',
      'checking',
      'claim',
      'cold',
      'commission',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'371',
      '75000',
      'accessorial',
      'agent',
      'amendment',
      'ansonia',
      'ascendtms',
      'authority',
      'bad',
      'billing',
      'bmc',
      'bond',
      'boot',
      'broker',
      'brokerage',
      'brokering',
      'brown',
      'business',
      'calling',
      'camp',
      'capital',
      'cargo',
      'carmack',
      'carrier411',
      'carriers',
      'cfr',
      'checking',
      'claim',
      'cold',
      'commission',
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
 12: {'371',
      '75000',
      'accessorial',
      'action',
      'agent',
      'amendment',
      'ansonia',
      'ascendtms',
      'authority',
      'bad',
      'billing',
      'bmc',
      'bond',
      'boot',
      'broker',
      'brokerage',
      'brokering',
      'brown',
      'business',
      'calling',
      'camp',
      'capital',
      'cargo',
      'carmack',
      'carrier411',
      'carriers',
      'cfr',
      'checking',
      'claim',
      'cold',
      'commission',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Victor Mason',
      'channel': 'Victor Mason',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=4n9e0eEuFtM&t=83s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t need a bond, and you don't have to start a company. You operate under the "
              "brokerage's authority while you focus on the sales and relationships. Now, "
              "let's clear up the confusion between a freight agent and a freight broker. A "
              'freight broker owns the business.',
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': "'t need a bond, and you don't have to start a company. You operate under the "
             "brokerage's authority while you focus on the sales and relationships. Now, let's "
             'clear up the confusion between a freight agent and a freight broker. A freight '
             'broker owns the business.',
      'title': 'How to Be a Freight Agent in 2026 (No Truck, No MC, No Guessing) (Victor '
               'Mason)',
      'url': 'https://www.youtube.com/watch?v=4n9e0eEuFtM&t=83s',
      'video_id': '4n9e0eEuFtM'},
     {'author': 'Drew Taylor',
      'channel': 'Drew Taylor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:04](https://www.youtube.com/watch?v=xahcxGx0b30&t=484s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Step one was start your authority early, even if you're not ready. Step two was "
              'pick your niche, own a specific problem instead of trying to be everything to '
              'everyone. Step three, ask better questions because cold listening beats cold '
              'calling every time.',
      'timestamp': 484,
      'timestamp_label': '[00:08:04]',
      'timestamp_seconds': 484,
      'tip': "Step one was start your authority early, even if you're not ready. Step two was "
             'pick your niche, own a specific problem instead of trying to be everything to '
             'everyone. Step three, ask better questions because cold listening beats cold '
             'calling every time.',
      'title': 'How to Become a Freight Broker in 2026 What I Wish I Knew After 9 Months of '
               'Rejection (Drew Taylor)',
      'url': 'https://www.youtube.com/watch?v=xahcxGx0b30&t=484s',
      'video_id': 'xahcxGx0b30'},
     {'author': 'thatDOTcop',
      'channel': 'thatDOTcop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:25](https://www.youtube.com/watch?v=9gNEc3GjPKA&t=745s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The challenge is they all define better as something different. A shipper wants '
              'to reduce costs. A broker wants enough margin to stay in business. A carrier '
              "wants higher revenue. And drivers want what's fair compensation. All those "
              'goals exist at the same exact time.',
      'timestamp': 745,
      'timestamp_label': '[00:12:25]',
      'timestamp_seconds': 745,
      'tip': 'The challenge is they all define better as something different. A shipper wants '
             'to reduce costs. A broker wants enough margin to stay in business. A carrier '
             "wants higher revenue. And drivers want what's fair compensation. All those goals "
             'exist at the same exact time.',
      'title': 'FMCSA Is Finally Taking On Broker Transparency (thatDOTcop)',
      'url': 'https://www.youtube.com/watch?v=9gNEc3GjPKA&t=745s',
      'video_id': '9gNEc3GjPKA'},
     {'author': 'Matt Krause',
      'channel': 'Matt Krause',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=su_azzEYWO4&t=54s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '14-hour days for thin margins. The reality of this business follows the 8020 '
              'principle. 80% of your revenue will likely come from just 20% of your clients. '
              "So the strategy we're talking about today flips the volume model. So we "
              'prioritize depth over breath.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': '14-hour days for thin margins. The reality of this business follows the 8020 '
             'principle. 80% of your revenue will likely come from just 20% of your clients. '
             "So the strategy we're talking about today flips the volume model. So we "
             'prioritize depth over breath.',
      'title': 'The EXACT Freight Broker Sales System To Go From $0–$10K/Month (Matt Krause)',
      'url': 'https://www.youtube.com/watch?v=su_azzEYWO4&t=54s',
      'video_id': 'su_azzEYWO4'},
     {'author': 'Eagle Express',
      'channel': 'Eagle Express',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=952lbvkEVvM&t=15s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Business in order just to earn 50 percent of your profits in return we at Eagle '
              'express service understand that freight broker agents are the backbone.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Business in order just to earn 50 percent of your profits in return we at Eagle '
             'express service understand that freight broker agents are the backbone.',
      'title': 'How to Make 100% Commission as a Freight Broker Agent (Eagle Express)',
      'url': 'https://www.youtube.com/watch?v=952lbvkEVvM&t=15s',
      'video_id': '952lbvkEVvM'},
     {'author': 'Dispatch Trucks',
      'channel': 'Dispatch Trucks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:42](https://www.youtube.com/watch?v=5azQO8-P020&t=702s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Regularly review your performance and the market conditions and don't hesitate "
              'to adjust your approach as needed. By considering these six factors and being '
              'flexible in your approach, you can not only maximize your revenue, but also '
              'build more resilient business.',
      'timestamp': 702,
      'timestamp_label': '[00:11:42]',
      'timestamp_seconds': 702,
      'tip': "Regularly review your performance and the market conditions and don't hesitate "
             'to adjust your approach as needed. By considering these six factors and being '
             'flexible in your approach, you can not only maximize your revenue, but also '
             'build more resilient business.',
      'title': 'Spot vs Contract: The Strategy That Actually Makes Money (Dispatch Trucks)',
      'url': 'https://www.youtube.com/watch?v=5azQO8-P020&t=702s',
      'video_id': '5azQO8-P020'},
     {'author': 'TunedinTony',
      'channel': 'TunedinTony',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:09](https://www.youtube.com/watch?v=M6mVy3VEVoY&t=1449s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Was just about to ask you that like we have a client um that you know we run '
              'his coaching business and all that and he does the box trucks and he always.',
      'timestamp': 1449,
      'timestamp_label': '[00:24:09]',
      'timestamp_seconds': 1449,
      'tip': 'Was just about to ask you that like we have a client um that you know we run his '
             'coaching business and all that and he does the box trucks and he always.',
      'title': 'Freight Broker Secrets REVEALED: Victor Mason’s Blueprint for Work From Home '
               'Trucking Success (TunedinTony)',
      'url': 'https://www.youtube.com/watch?v=M6mVy3VEVoY&t=1449s',
      'video_id': 'M6mVy3VEVoY'},
     {'author': 'FreightWaves',
      'channel': 'FreightWaves',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:42:33](https://www.youtube.com/watch?v=iOTP-SdRDb4&t=2553s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "On the split model and they're they're doing a fantastic job uh booking "
              "carriers but they they're it's it maybe is monotonous to them and.",
      'timestamp': 2553,
      'timestamp_label': '[00:42:33]',
      'timestamp_seconds': 2553,
      'tip': "On the split model and they're they're doing a fantastic job uh booking carriers "
             "but they they're it's it maybe is monotonous to them and.",
      'title': 'Running a cradle to grave freight brokerage - Put That Coffee Down '
               '(FreightWaves)',
      'url': 'https://www.youtube.com/watch?v=iOTP-SdRDb4&t=2553s',
      'video_id': 'iOTP-SdRDb4'},
     {'author': 'Bobby Loads',
      'channel': 'Bobby Loads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:32](https://www.youtube.com/watch?v=jxL6kaRxoEo&t=452s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "All these people in the comments on my market updates are are crying. They're "
              "just I have no idea. I will not touch it unless it's minimum triple broker, "
              'bro. Florida has been has a lot of citrus.',
      'timestamp': 452,
      'timestamp_label': '[00:07:32]',
      'timestamp_seconds': 452,
      'tip': "All these people in the comments on my market updates are are crying. They're "
             "just I have no idea. I will not touch it unless it's minimum triple broker, bro. "
             'Florida has been has a lot of citrus.',
      'title': 'Why I’m Done With Dry Van: Reefer vs Flatbed in 2026 (Bobby Loads)',
      'url': 'https://www.youtube.com/watch?v=jxL6kaRxoEo&t=452s',
      'video_id': 'jxL6kaRxoEo'},
     {'author': 'FreightBrokers',
      'channel': 'FreightBrokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:59](https://www.youtube.com/watch?v=JKxqqgS6OBg&t=119s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And number four on the list of what shippers really want from freight brokers '
              'is authority. When you actually know your stuff, you know your freight niche, '
              'you know your market, you know your customers needs, it shows.',
      'timestamp': 119,
      'timestamp_label': '[00:01:59]',
      'timestamp_seconds': 119,
      'tip': 'And number four on the list of what shippers really want from freight brokers is '
             'authority. When you actually know your stuff, you know your freight niche, you '
             'know your market, you know your customers needs, it shows.',
      'title': 'Freight Broker Tips: What Do Shippers Really Want From Freight Brokers? '
               '(FreightBrokers)',
      'url': 'https://www.youtube.com/watch?v=JKxqqgS6OBg&t=119s',
      'video_id': 'JKxqqgS6OBg'},
     {'author': 'Matt Krause',
      'channel': 'Matt Krause',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:44](https://www.youtube.com/watch?v=bP4Dnpd58PE&t=1364s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, avoid the valueless check-in call or email and use the value drip via the '
              'market intel call. Two weeks later, say, "Hey, Mike, it\'s name. I\'m not '
              'calling for loads, okay?',
      'timestamp': 1364,
      'timestamp_label': '[00:22:44]',
      'timestamp_seconds': 1364,
      'tip': 'So, avoid the valueless check-in call or email and use the value drip via the '
             'market intel call. Two weeks later, say, "Hey, Mike, it\'s name. I\'m not '
             'calling for loads, okay?',
      'title': 'Full 2026 Freight Broker Training To Go From $0-$1,000,000 (Matt Krause)',
      'url': 'https://www.youtube.com/watch?v=bP4Dnpd58PE&t=1364s',
      'video_id': 'bP4Dnpd58PE'},
     {'author': 'Brandon Manney The Mentor',
      'channel': 'Brandon Manney The Mentor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:13](https://www.youtube.com/watch?v=8Mhf3iqBflw&t=553s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'When you are in business so if you guys have any questions hit me on my text '
              'message 317-953-8900 go visit my website www.extraordinarymovement.com.',
      'timestamp': 553,
      'timestamp_label': '[00:09:13]',
      'timestamp_seconds': 553,
      'tip': 'When you are in business so if you guys have any questions hit me on my text '
             'message 317-953-8900 go visit my website www.extraordinarymovement.com.',
      'title': 'HOW FREIGHT BROKERS EARN MORE MONEY WITH DETENTION & LAYOVER-PAY WHILE SOME '
               'TRUCK DRIVERS ARE MAD!!! (Brandon Manney The Mentor)',
      'url': 'https://www.youtube.com/watch?v=8Mhf3iqBflw&t=553s',
      'video_id': '8Mhf3iqBflw'},
     {'author': 'Trucking Made Successful',
      'channel': 'Trucking Made Successful',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:54](https://www.youtube.com/watch?v=ZlWGSiCM45c&t=834s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Have a bit more control in the current market situation anyways I hope you guys '
              "have have a wonderful rest of your weekend and I'll see you in the next video.",
      'timestamp': 834,
      'timestamp_label': '[00:13:54]',
      'timestamp_seconds': 834,
      'tip': 'Have a bit more control in the current market situation anyways I hope you guys '
             "have have a wonderful rest of your weekend and I'll see you in the next video.",
      'title': 'Trucking Market Update: Rejection Rates, Contract vs Spot, and Where To Get '
               'High Rates Per Mile (Trucking Made Successful)',
      'url': 'https://www.youtube.com/watch?v=ZlWGSiCM45c&t=834s',
      'video_id': 'ZlWGSiCM45c'},
     {'author': 'AFT Dispatch',
      'channel': 'AFT Dispatch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:51](https://www.youtube.com/watch?v=Gx_gladG4ps&t=531s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'On that one so as you can see it pays to run the short run uh short runs now '
              'Reggie he did something interesting from Friday morning to Thursday night was '
              'his his drive time.',
      'timestamp': 531,
      'timestamp_label': '[00:08:51]',
      'timestamp_seconds': 531,
      'tip': 'On that one so as you can see it pays to run the short run uh short runs now '
             'Reggie he did something interesting from Friday morning to Thursday night was '
             'his his drive time.',
      'title': "2024 Freight Market: We're Looking at Flatbeds, Vans, and Reefers (AFT "
               'Dispatch)',
      'url': 'https://www.youtube.com/watch?v=Gx_gladG4ps&t=531s',
      'video_id': 'Gx_gladG4ps'},
     {'author': 'Bobby Loads',
      'channel': 'Bobby Loads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:31](https://www.youtube.com/watch?v=C4qKjPG0gcY&t=271s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Bills pay your mortgages you know have have a place to a place to sleep eat you '
              "know and take care of your family so let's hope it gets better and we'll be in "
              'touch next video.',
      'timestamp': 271,
      'timestamp_label': '[00:04:31]',
      'timestamp_seconds': 271,
      'tip': 'Bills pay your mortgages you know have have a place to a place to sleep eat you '
             "know and take care of your family so let's hope it gets better and we'll be in "
             'touch next video.',
      'title': '🚛 Trucking Update: Dry Vans, Flatbeds & Reefers – Market Trends & Freight '
               'Rates 📉🚨 (Bobby Loads)',
      'url': 'https://www.youtube.com/watch?v=C4qKjPG0gcY&t=271s',
      'video_id': 'C4qKjPG0gcY'}],
 2: [{'author': 'Porter Capital',
      'channel': 'Porter Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=iJE2rZFL57E&t=51s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Porter Capital advances you a large portion of the invoice amount, usually '
              'within 1 to two business days. Then we follow up to collect the payment from '
              'your broker or shipper. Once the invoice is paid, you get the remaining balance '
              'minus a small fee.',
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': 'Porter Capital advances you a large portion of the invoice amount, usually '
             'within 1 to two business days. Then we follow up to collect the payment from '
             'your broker or shipper. Once the invoice is paid, you get the remaining balance '
             'minus a small fee.',
      'title': 'Quick Pay vs Freight Factoring (Porter Capital)',
      'url': 'https://www.youtube.com/watch?v=iJE2rZFL57E&t=51s',
      'video_id': 'iJE2rZFL57E'},
     {'author': 'FMCSA REGISTRATION dot com',
      'channel': 'FMCSA REGISTRATION dot com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:53](https://www.youtube.com/watch?v=fG1DJXPE2jk&t=53s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then, the bond must be renewed annually. So, why is a BMC 84 surety bond '
              'important for freight brokers and forwarders. The bond ensures that shippers '
              'and carriers are paid for their services, even if the broker or forwarder fails '
              'to pay.',
      'timestamp': 53,
      'timestamp_label': '[00:00:53]',
      'timestamp_seconds': 53,
      'tip': 'Then, the bond must be renewed annually. So, why is a BMC 84 surety bond '
             'important for freight brokers and forwarders. The bond ensures that shippers and '
             'carriers are paid for their services, even if the broker or forwarder fails to '
             'pay.',
      'title': 'BMC 84 Surety Bond | Is a Freight Broker Bond Requirement (BMC-84) (FMCSA '
               'REGISTRATION dot com)',
      'url': 'https://www.youtube.com/watch?v=fG1DJXPE2jk&t=53s',
      'video_id': 'fG1DJXPE2jk'},
     {'author': 'MillionsExplained',
      'channel': 'MillionsExplained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:17](https://www.youtube.com/watch?v=An8HIad4rIg&t=257s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "45 days for a broker to pay simply stops taking that broker's loads. So, you're "
              'stuck between a customer who pays slowly and a vendor who has to be paid fast, '
              'and the gap between them is money you have to find yourself.',
      'timestamp': 257,
      'timestamp_label': '[00:04:17]',
      'timestamp_seconds': 257,
      'tip': "45 days for a broker to pay simply stops taking that broker's loads. So, you're "
             'stuck between a customer who pays slowly and a vendor who has to be paid fast, '
             'and the gap between them is money you have to find yourself.',
      'title': 'The Economics of Owning a Freight Brokerage (MillionsExplained)',
      'url': 'https://www.youtube.com/watch?v=An8HIad4rIg&t=257s',
      'video_id': 'An8HIad4rIg'},
     {'author': 'Surety Bond Authority',
      'channel': 'Surety Bond Authority',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:21](https://www.youtube.com/watch?v=UPpi7ufHWec&t=141s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You will pay your premium and your bond documents will be sent to you right '
              'away. Ultimately, the goal of freight broker bonds is to guarantee that '
              'brokering is an ethical and fair industry where the people involved earn '
              'rightful payments for their work.',
      'timestamp': 141,
      'timestamp_label': '[00:02:21]',
      'timestamp_seconds': 141,
      'tip': 'You will pay your premium and your bond documents will be sent to you right '
             'away. Ultimately, the goal of freight broker bonds is to guarantee that '
             'brokering is an ethical and fair industry where the people involved earn '
             'rightful payments for their work.',
      'title': 'What is a (BMC-84) Freight Broker Bond? A Guide (Surety Bond Authority)',
      'url': 'https://www.youtube.com/watch?v=UPpi7ufHWec&t=141s',
      'video_id': 'UPpi7ufHWec'},
     {'author': 'ShipLeague',
      'channel': 'ShipLeague',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=OzmQFxT30NM&t=72s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So I personally have worked with shippers and receivers that do not pay '
              'detention. Your time is better spent with another customer growing your book of '
              "business in a better way. They will only ruin your reputation and they're gonna "
              'ruin your relationship with your carriers.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': 'So I personally have worked with shippers and receivers that do not pay '
             'detention. Your time is better spent with another customer growing your book of '
             "business in a better way. They will only ruin your reputation and they're gonna "
             'ruin your relationship with your carriers.',
      'title': "Broker didn't pay Detention?? Broker's take on Detention! (ShipLeague)",
      'url': 'https://www.youtube.com/watch?v=OzmQFxT30NM&t=72s',
      'video_id': 'OzmQFxT30NM'},
     {'author': 'Porter Capital',
      'channel': 'Porter Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=R4i90VgyHqk&t=22s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '80 to 90% of the invoice amount. Then they collect the full payment from your '
              'customer, deduct their fee, and send you the remaining balance. This process '
              'helps trucking businesses of all sizes stay financially stable, especially '
              'those running tight margins.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': '80 to 90% of the invoice amount. Then they collect the full payment from your '
             'customer, deduct their fee, and send you the remaining balance. This process '
             'helps trucking businesses of all sizes stay financially stable, especially those '
             'running tight margins.',
      'title': 'How Working With A Truck Factoring Company Gets You Paid Fast! (Porter '
               'Capital)',
      'url': 'https://www.youtube.com/watch?v=R4i90VgyHqk&t=22s',
      'video_id': 'R4i90VgyHqk'},
     {'author': 'Think Trucking',
      'channel': 'Think Trucking',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:17](https://www.youtube.com/watch?v=uHIZpxSLN-c&t=197s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'With one, you collect a flat fee that covers the wasted trip. You pay $100 out '
              'of pocket for someone to unload your trailer and if nobody reimburses you, that '
              'is $100 straight out of your settlement. Always confirm who pays the lumper '
              'before you arrive.',
      'timestamp': 197,
      'timestamp_label': '[00:03:17]',
      'timestamp_seconds': 197,
      'tip': 'With one, you collect a flat fee that covers the wasted trip. You pay $100 out '
             'of pocket for someone to unload your trailer and if nobody reimburses you, that '
             'is $100 straight out of your settlement. Always confirm who pays the lumper '
             'before you arrive.',
      'title': 'How to Get Paid Detention, Layover & Accessorial Pay as a Truck Driver (Think '
               'Trucking)',
      'url': 'https://www.youtube.com/watch?v=uHIZpxSLN-c&t=197s',
      'video_id': 'uHIZpxSLN-c'},
     {'author': 'MyFullCoverage',
      'channel': 'MyFullCoverage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:29](https://www.youtube.com/watch?v=x_fzUHiNELw&t=29s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "5,000 per truck and 10,000 per occurrence. For everyone else, it's your broker "
              'and shipper contracts that require it. A standard cargo policy usually pays for '
              'a collision or rollover, a fire, and theft of the whole truck with the load.',
      'timestamp': 29,
      'timestamp_label': '[00:00:29]',
      'timestamp_seconds': 29,
      'tip': "5,000 per truck and 10,000 per occurrence. For everyone else, it's your broker "
             'and shipper contracts that require it. A standard cargo policy usually pays for '
             'a collision or rollover, a fire, and theft of the whole truck with the load.',
      'title': "Cargo insurance: what it pays, what it doesn't, and your limit "
               '(MyFullCoverage)',
      'url': 'https://www.youtube.com/watch?v=x_fzUHiNELw&t=29s',
      'video_id': 'x_fzUHiNELw'},
     {'author': 'Never Stop Trucking',
      'channel': 'Never Stop Trucking',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:44](https://www.youtube.com/watch?v=tvnlRLMXRJ4&t=164s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Have them sit there and hold the truck but it is what it is so broker will pay '
              'the attention and usually they will use their customers money so the customer.',
      'timestamp': 164,
      'timestamp_label': '[00:02:44]',
      'timestamp_seconds': 164,
      'tip': 'Have them sit there and hold the truck but it is what it is so broker will pay '
             'the attention and usually they will use their customers money so the customer.',
      'title': 'Difference between layover and detention (Never Stop Trucking)',
      'url': 'https://www.youtube.com/watch?v=tvnlRLMXRJ4&t=164s',
      'video_id': 'tvnlRLMXRJ4'},
     {'author': 'Freight 360',
      'channel': 'Freight 360',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:49](https://www.youtube.com/watch?v=A7rlv69JAj8&t=349s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Because they were late to the pickup or late to the delivery your customer is '
              'not going to pay that layover and you might even have to charge a late fee to.',
      'timestamp': 349,
      'timestamp_label': '[00:05:49]',
      'timestamp_seconds': 349,
      'tip': 'Because they were late to the pickup or late to the delivery your customer is '
             'not going to pay that layover and you might even have to charge a late fee to.',
      'title': 'What are Accessorial Charges in Truckload Transportation? 🤔 🚛 (Freight 360)',
      'url': 'https://www.youtube.com/watch?v=A7rlv69JAj8&t=349s',
      'video_id': 'A7rlv69JAj8'},
     {'author': 'Drayage Academy',
      'channel': 'Drayage Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:34](https://www.youtube.com/watch?v=fhPReUtDXkI&t=214s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Sometimes you're waiting for your customer to clear the demurrage or storage "
              "fees. Always check the terminal or port's website before heading to the port. "
              'In step two, you will confirm there are are active holds or fees due on the '
              'container.',
      'timestamp': 214,
      'timestamp_label': '[00:03:34]',
      'timestamp_seconds': 214,
      'tip': "Sometimes you're waiting for your customer to clear the demurrage or storage "
             "fees. Always check the terminal or port's website before heading to the port. In "
             'step two, you will confirm there are are active holds or fees due on the '
             'container.',
      'title': 'Import Containers Explained: From Port Pickup to Empty Return #drayage '
               '#portlife #owneroperators (Drayage Academy)',
      'url': 'https://www.youtube.com/watch?v=fhPReUtDXkI&t=214s',
      'video_id': 'fhPReUtDXkI'},
     {'author': 'Matt Krause',
      'channel': 'Matt Krause',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:44](https://www.youtube.com/watch?v=nUM2jUENmpc&t=164s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Something called a freight broker Authority and that means registering with the '
              'FMCSA and getting your shity bond and.',
      'timestamp': 164,
      'timestamp_label': '[00:02:44]',
      'timestamp_seconds': 164,
      'tip': 'Something called a freight broker Authority and that means registering with the '
             'FMCSA and getting your shity bond and.',
      'title': 'The Untold Reality of Becoming a Freight Broker: Can You Handle It? (Matt '
               'Krause)',
      'url': 'https://www.youtube.com/watch?v=nUM2jUENmpc&t=164s',
      'video_id': 'nUM2jUENmpc'},
     {'author': 'Pauline Nabacwa',
      'channel': 'Pauline Nabacwa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:06](https://www.youtube.com/watch?v=fpu1Fhdo9Vs&t=246s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "At the dock it's not very comfortable sitting there anyway so as a dispatcher "
              'as a company owner these are things I pay attention to when I am booking a load '
              'I want to see that I keep in touch with my drivers I want to keep.',
      'timestamp': 246,
      'timestamp_label': '[00:04:06]',
      'timestamp_seconds': 246,
      'tip': "At the dock it's not very comfortable sitting there anyway so as a dispatcher as "
             'a company owner these are things I pay attention to when I am booking a load I '
             'want to see that I keep in touch with my drivers I want to keep.',
      'title': 'Detention and TONU Fees In Trucking. (Pauline Nabacwa)',
      'url': 'https://www.youtube.com/watch?v=fpu1Fhdo9Vs&t=246s',
      'video_id': 'fpu1Fhdo9Vs'},
     {'author': 'FreightBrokers',
      'channel': 'FreightBrokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:36](https://www.youtube.com/watch?v=HTQaqqy_CPs&t=216s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's say I want to make approximately 250 dollars in gross profit. I add the "
              'two together and get a customer rate of 1,550 bucks. 1300 dollar carrier rate '
              'plus 250 dollar gross profit equals 1550 customer rate. Gross profit is the '
              'amount left after I pay the carrier.',
      'timestamp': 216,
      'timestamp_label': '[00:03:36]',
      'timestamp_seconds': 216,
      'tip': "Let's say I want to make approximately 250 dollars in gross profit. I add the "
             'two together and get a customer rate of 1,550 bucks. 1300 dollar carrier rate '
             'plus 250 dollar gross profit equals 1550 customer rate. Gross profit is the '
             'amount left after I pay the carrier.',
      'title': 'How to Price Your First Load As A Freight Broker or Freight Agent [4 Key '
               'Numbers Explained] (FreightBrokers)',
      'url': 'https://www.youtube.com/watch?v=HTQaqqy_CPs&t=216s',
      'video_id': 'HTQaqqy_CPs'},
     {'author': 'FreightBrokers',
      'channel': 'FreightBrokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:50](https://www.youtube.com/watch?v=HeiPAKWzLsI&t=590s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Program where I work with you personally coach you and Mentor you and help you '
              'navigate through getting your first five or 10 shippers and helping you on your '
              'way to First million dollars sales you can check that out at Freight breger '
              'camp.com waitlist.',
      'timestamp': 590,
      'timestamp_label': '[00:09:50]',
      'timestamp_seconds': 590,
      'tip': 'Program where I work with you personally coach you and Mentor you and help you '
             'navigate through getting your first five or 10 shippers and helping you on your '
             'way to First million dollars sales you can check that out at Freight breger '
             'camp.com waitlist.',
      'title': 'How to Find Shippers As A Freight Broker | 30,000 Shipper Leads For FREE! 🔥🚀 '
               '(FreightBrokers)',
      'url': 'https://www.youtube.com/watch?v=HeiPAKWzLsI&t=590s',
      'video_id': 'HeiPAKWzLsI'}],
 3: [{'author': 'Freight 360',
      'channel': 'Freight 360',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=SPl9Y_xMJHA&t=146s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'All other back office tasks are completed by the licensed brokerage company. '
              'These tasks generally include billing, collections, claims, cash flow, '
              'marketing, IT support, agent development, and sometimes pricing and dispatching '
              'services.',
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': 'All other back office tasks are completed by the licensed brokerage company. '
             'These tasks generally include billing, collections, claims, cash flow, '
             'marketing, IT support, agent development, and sometimes pricing and dispatching '
             'services.',
      'title': 'Freight Broker Commission Percentage | Everything you need to know! 🚚 (Freight '
               '360)',
      'url': 'https://www.youtube.com/watch?v=SPl9Y_xMJHA&t=146s',
      'video_id': 'SPl9Y_xMJHA'},
     {'author': 'Matt Krause',
      'channel': 'Matt Krause',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:42](https://www.youtube.com/watch?v=xe6QTceV_JE&t=162s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, basically, you're trading profit margin for peace of mind. So, here's the "
              "here's the simple breakdown of what this means for you and what it means for "
              'your money and your life. The broker is building a business and the agent is '
              'building a job.',
      'timestamp': 162,
      'timestamp_label': '[00:02:42]',
      'timestamp_seconds': 162,
      'tip': "So, basically, you're trading profit margin for peace of mind. So, here's the "
             "here's the simple breakdown of what this means for you and what it means for "
             'your money and your life. The broker is building a business and the agent is '
             'building a job.',
      'title': 'Freight Agent or Broker: The Smarter Path for Beginners (Matt Krause)',
      'url': 'https://www.youtube.com/watch?v=xe6QTceV_JE&t=162s',
      'video_id': 'xe6QTceV_JE'},
     {'author': 'The Finance Pro',
      'channel': 'The Finance Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:35](https://www.youtube.com/watch?v=29d2gRCN8Ng&t=515s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "One guide says brokers should forecast cash weekly. That's also why the federal "
              'bond exists. The most common reason for a claim, according to one bond '
              'provider, is carriers not being paid on time. And the rules just got tighter.',
      'timestamp': 515,
      'timestamp_label': '[00:08:35]',
      'timestamp_seconds': 515,
      'tip': "One guide says brokers should forecast cash weekly. That's also why the federal "
             'bond exists. The most common reason for a claim, according to one bond provider, '
             'is carriers not being paid on time. And the rules just got tighter.',
      'title': 'The Economics of Owning a Freight Brokerage (The Finance Pro)',
      'url': 'https://www.youtube.com/watch?v=29d2gRCN8Ng&t=515s',
      'video_id': '29d2gRCN8Ng'},
     {'author': 'FreightBrokers',
      'channel': 'FreightBrokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:44](https://www.youtube.com/watch?v=Lpq9AHrz7nQ&t=404s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'An independent 1099 freight agent works under an established broker. Your '
              "compensation is usually based on whatever commission or split you've agreed to "
              "with the brokerage. For example, let's say our load produced 300 in gross "
              'profit.',
      'timestamp': 404,
      'timestamp_label': '[00:06:44]',
      'timestamp_seconds': 404,
      'tip': 'An independent 1099 freight agent works under an established broker. Your '
             "compensation is usually based on whatever commission or split you've agreed to "
             "with the brokerage. For example, let's say our load produced 300 in gross "
             'profit.',
      'title': 'How Do Freight Brokers Get Paid? From Invoicing to Profit. 💰🔥 (FreightBrokers)',
      'url': 'https://www.youtube.com/watch?v=Lpq9AHrz7nQ&t=404s',
      'video_id': 'Lpq9AHrz7nQ'},
     {'author': 'Cargolinked',
      'channel': 'Cargolinked',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=rbmdGEpBKCI&t=120s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If a ship's in trouble and cargo is sacrificed, or extra costs are paid, to "
              'save the voyage, everyone whose cargo was saved pays a share, by value. Your '
              "cargo's held until you give security: a bond, plus your insurer's guarantee, or "
              'a cash deposit.',
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': "If a ship's in trouble and cargo is sacrificed, or extra costs are paid, to save "
             "the voyage, everyone whose cargo was saved pays a share, by value. Your cargo's "
             "held until you give security: a bond, plus your insurer's guarantee, or a cash "
             'deposit.',
      'title': "Cargo Insurance Explained: Why Carrier Liability Isn't Enough (Cargolinked)",
      'url': 'https://www.youtube.com/watch?v=rbmdGEpBKCI&t=120s',
      'video_id': 'rbmdGEpBKCI'},
     {'author': 'FreightBrokers',
      'channel': 'FreightBrokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:05](https://www.youtube.com/watch?v=S0a8FejhkCA&t=545s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t worry about getting your freight broker authority right now. Start out as a "
              'freight agent. I say that because it costs less to get started.',
      'timestamp': 545,
      'timestamp_label': '[00:09:05]',
      'timestamp_seconds': 545,
      'tip': "'t worry about getting your freight broker authority right now. Start out as a "
             'freight agent. I say that because it costs less to get started.',
      'title': 'Freight Broker / Agent LIVE Q&A with Dennis Brown 1/19/25 📱 (FreightBrokers)',
      'url': 'https://www.youtube.com/watch?v=S0a8FejhkCA&t=545s',
      'video_id': 'S0a8FejhkCA'},
     {'author': 'Entre Mike',
      'channel': 'Entre Mike',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:38](https://www.youtube.com/watch?v=oytUZVvyF80&t=1238s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Oh, if you're a small time broker is going to do a thousand loads a year. You "
              "know, like um that that's as an independent agent, a thousand is a is a low "
              'number.',
      'timestamp': 1238,
      'timestamp_label': '[00:20:38]',
      'timestamp_seconds': 1238,
      'tip': "Oh, if you're a small time broker is going to do a thousand loads a year. You "
             "know, like um that that's as an independent agent, a thousand is a is a low "
             'number.',
      'title': 'Freight Broker Reveals How Truckers Can Make More Money in 2026 (Entre Mike)',
      'url': 'https://www.youtube.com/watch?v=oytUZVvyF80&t=1238s',
      'video_id': 'oytUZVvyF80'},
     {'author': 'Valerie Robfogel',
      'channel': 'Valerie Robfogel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:19](https://www.youtube.com/watch?v=EhqxL4P0ZTc&t=259s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Purchase price with no questions asked so read on check out the members-only '
              "video below and don't forget get to take advantage of the bonus offers "
              'available for subscribing today.',
      'timestamp': 259,
      'timestamp_label': '[00:04:19]',
      'timestamp_seconds': 259,
      'tip': 'Purchase price with no questions asked so read on check out the members-only '
             "video below and don't forget get to take advantage of the bonus offers available "
             'for subscribing today.',
      'title': 'Freight Broker Boot Camp Dennis Brown reviews SCAM OR LEGIT? (Valerie '
               'Robfogel)',
      'url': 'https://www.youtube.com/watch?v=EhqxL4P0ZTc&t=259s',
      'video_id': 'EhqxL4P0ZTc'},
     {'author': 'Bumble Bee Dispatch',
      'channel': 'Bumble Bee Dispatch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:07](https://www.youtube.com/watch?v=dTOcCujNdaw&t=127s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That driver so you're going to need some type of cash flow so standard pay "
              'usually is an option unless you have capital okay.',
      'timestamp': 127,
      'timestamp_label': '[00:02:07]',
      'timestamp_seconds': 127,
      'tip': "That driver so you're going to need some type of cash flow so standard pay "
             'usually is an option unless you have capital okay.',
      'title': 'Freight Invoice Factoring vs Quickpay with Brokers (Bumble Bee Dispatch)',
      'url': 'https://www.youtube.com/watch?v=dTOcCujNdaw&t=127s',
      'video_id': 'dTOcCujNdaw'},
     {'author': 'Surety Bonds Direct',
      'channel': 'Surety Bonds Direct',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:51](https://www.youtube.com/watch?v=tkM7CbVBoC0&t=171s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Personal credit and experience two who you decide to work with let us price '
              "shop for you and we'll do what we do best get you the lowest price and once we "
              "do we'll send you a firm price quote no obligation no charge thanks for "
              'watching.',
      'timestamp': 171,
      'timestamp_label': '[00:02:51]',
      'timestamp_seconds': 171,
      'tip': 'Personal credit and experience two who you decide to work with let us price shop '
             "for you and we'll do what we do best get you the lowest price and once we do "
             "we'll send you a firm price quote no obligation no charge thanks for watching.",
      'title': 'Freight Broker Bond Cost Explained With Real Examples (Surety Bonds Direct)',
      'url': 'https://www.youtube.com/watch?v=tkM7CbVBoC0&t=171s',
      'video_id': 'tkM7CbVBoC0'},
     {'author': 'Logistics Today',
      'channel': 'Logistics Today',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=5cyp2cCCUiA&t=25s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And how many trucks there are to move it. Right now demand is only a little '
              'stronger than normal. The real story is supply and the cost  of fuel to.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': 'And how many trucks there are to move it. Right now demand is only a little '
             'stronger than normal. The real story is supply and the cost  of fuel to.',
      'title': '$6 Diesel and Missing Trucks: The Q4 2026 Freight Market Explained (Logistics '
               'Today)',
      'url': 'https://www.youtube.com/watch?v=5cyp2cCCUiA&t=25s',
      'video_id': '5cyp2cCCUiA'},
     {'author': 'Drayage Specialist',
      'channel': 'Drayage Specialist',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:35](https://www.youtube.com/watch?v=7hSE1PjbOkI&t=95s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Long hauls and trucks for the last mile businesses can save big on fuel and '
              'transport costs fuel efficiency trains and ships use less Fuel per container.',
      'timestamp': 95,
      'timestamp_label': '[00:01:35]',
      'timestamp_seconds': 95,
      'tip': 'Long hauls and trucks for the last mile businesses can save big on fuel and '
             'transport costs fuel efficiency trains and ships use less Fuel per container.',
      'title': 'Intermodal Transportation Simplified: How It Works and Why It Matters (Drayage '
               'Specialist)',
      'url': 'https://www.youtube.com/watch?v=7hSE1PjbOkI&t=95s',
      'video_id': '7hSE1PjbOkI'},
     {'author': 'ET Transport',
      'channel': 'ET Transport',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:43](https://www.youtube.com/watch?v=UF-qDT9q1Bs&t=463s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Guys out if it did help you out please guys share the free information out '
              "there I'm Ronin and I'll catch you in my next video.",
      'timestamp': 463,
      'timestamp_label': '[00:07:43]',
      'timestamp_seconds': 463,
      'tip': 'Guys out if it did help you out please guys share the free information out there '
             "I'm Ronin and I'll catch you in my next video.",
      'title': 'Is FREIGHT BROKER TRANSPARENCY a Waste of Time? (ET Transport)',
      'url': 'https://www.youtube.com/watch?v=UF-qDT9q1Bs&t=463s',
      'video_id': 'UF-qDT9q1Bs'},
     {'author': 'Never Stop Trucking',
      'channel': 'Never Stop Trucking',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:05](https://www.youtube.com/watch?v=K5sqFMIL3IQ&t=425s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh but with reefers you have to know exactly what the commodities uh what kind '
              'of you know food produce so is it bulk is it something else that needs to be '
              'temperature temperature controlled.',
      'timestamp': 425,
      'timestamp_label': '[00:07:05]',
      'timestamp_seconds': 425,
      'tip': 'Uh but with reefers you have to know exactly what the commodities uh what kind '
             'of you know food produce so is it bulk is it something else that needs to be '
             'temperature temperature controlled.',
      'title': 'Booking reefer loads vs. flatbed loads vs. dry van loads (Never Stop Trucking)',
      'url': 'https://www.youtube.com/watch?v=K5sqFMIL3IQ&t=425s',
      'video_id': 'K5sqFMIL3IQ'},
     {'author': 'Freight 360',
      'channel': 'Freight 360',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:58:24](https://www.youtube.com/watch?v=U9PKl6-ulL4&t=3504s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Content if you'd like your question answered on the show fill out the contact "
              "us form on our site and we'll see you next week.",
      'timestamp': 3504,
      'timestamp_label': '[00:58:24]',
      'timestamp_seconds': 3504,
      'tip': "Content if you'd like your question answered on the show fill out the contact us "
             "form on our site and we'll see you next week.",
      'title': 'The Truth Behind Broker Transparency | Episode 272 (Freight 360)',
      'url': 'https://www.youtube.com/watch?v=U9PKl6-ulL4&t=3504s',
      'video_id': 'U9PKl6-ulL4'}],
 4: [{'author': 'FreightBrokers',
      'channel': 'FreightBrokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:18](https://www.youtube.com/watch?v=3NBT5XIIshA&t=318s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ale Tatusa has done the the boot camp, which is my startup program. Yeah, just '
              'so you guys are clear, uh, back in 2009 when I had my brokerage, I launched '
              "what's called Freight Broker Boot Camp, which was an online self-paced freight "
              'broker and freight agent startup course.',
      'timestamp': 318,
      'timestamp_label': '[00:05:18]',
      'timestamp_seconds': 318,
      'tip': 'Ale Tatusa has done the the boot camp, which is my startup program. Yeah, just '
             'so you guys are clear, uh, back in 2009 when I had my brokerage, I launched '
             "what's called Freight Broker Boot Camp, which was an online self-paced freight "
             'broker and freight agent startup course.',
      'title': 'Freight Broker Boot Camp LIVE with Dennis Brown 8-4-25 (FreightBrokers)',
      'url': 'https://www.youtube.com/watch?v=3NBT5XIIshA&t=318s',
      'video_id': '3NBT5XIIshA'},
     {'author': 'A3E ECOSYSTEM',
      'channel': 'A3E ECOSYSTEM',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:26](https://www.youtube.com/watch?v=b64rVWfkAsc&t=86s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'BMC 91X or BMC82, that form is the evidence for bodily injury and property '
              'damage liability. Only household goods motor carriers are required to file '
              'evidence of cargo insurance with FMCSA. That is a separate evidence track for '
              'that role.',
      'timestamp': 86,
      'timestamp_label': '[00:01:26]',
      'timestamp_seconds': 86,
      'tip': 'BMC 91X or BMC82, that form is the evidence for bodily injury and property '
             'damage liability. Only household goods motor carriers are required to file '
             'evidence of cargo insurance with FMCSA. That is a separate evidence track for '
             'that role.',
      'title': '49 CFR 371: Broker Authority Insurance Minimums (A3E ECOSYSTEM)',
      'url': 'https://www.youtube.com/watch?v=b64rVWfkAsc&t=86s',
      'video_id': 'b64rVWfkAsc'},
     {'author': 'Anderson Trucking Service',
      'channel': 'Anderson Trucking Service',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:49](https://www.youtube.com/watch?v=id2FXFnynHM&t=49s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "At this point, it's the carrier's responsibility to submit the claim to their "
              'insurance company, and the agent will then facilitate communication between the '
              'customer and the carrier. If you have any other questions such as, "What is a '
              'cargo claim?',
      'timestamp': 49,
      'timestamp_label': '[00:00:49]',
      'timestamp_seconds': 49,
      'tip': "At this point, it's the carrier's responsibility to submit the claim to their "
             'insurance company, and the agent will then facilitate communication between the '
             'customer and the carrier. If you have any other questions such as, "What is a '
             'cargo claim?',
      'title': 'Cargo Claims Explained [What Your Broker Actually Does] (Anderson Trucking '
               'Service)',
      'url': 'https://www.youtube.com/watch?v=id2FXFnynHM&t=49s',
      'video_id': 'id2FXFnynHM'},
     {'author': 'Matt Krause',
      'channel': 'Matt Krause',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:01](https://www.youtube.com/watch?v=hhT4X32MspU&t=481s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '1 year, he decides to stop. Well, he still owns an LLC, which is the company '
              'itself, and a license, and a bond, and a signed agreement with Skip, and a '
              'factoring company that already pays his carriers, all in his own name. And '
              'every one of those is worth something to a bank.',
      'timestamp': 481,
      'timestamp_label': '[00:08:01]',
      'timestamp_seconds': 481,
      'tip': '1 year, he decides to stop. Well, he still owns an LLC, which is the company '
             'itself, and a license, and a bond, and a signed agreement with Skip, and a '
             'factoring company that already pays his carriers, all in his own name. And every '
             'one of those is worth something to a bank.',
      'title': 'Freight Broker vs Freight Agent in 2027 (Which to Start First) (Matt Krause)',
      'url': 'https://www.youtube.com/watch?v=hhT4X32MspU&t=481s',
      'video_id': 'hhT4X32MspU'},
     {'author': 'CargoRex',
      'channel': 'CargoRex',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:13](https://www.youtube.com/watch?v=xQYjaYAvyms&t=733s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Especially in this business, especially with the plaintiff's bar and and all "
              "this stuff. And so, if you don't want risk, I don't think you're in the right "
              'business. Two, insurance, by by its setup, is a transfer of risk.',
      'timestamp': 733,
      'timestamp_label': '[00:12:13]',
      'timestamp_seconds': 733,
      'tip': "Especially in this business, especially with the plaintiff's bar and and all "
             "this stuff. And so, if you don't want risk, I don't think you're in the right "
             'business. Two, insurance, by by its setup, is a transfer of risk.',
      'title': 'Cargo Insurance, Evidence and Doing What Your Policy Says | Jared Palmer '
               '(CargoRex)',
      'url': 'https://www.youtube.com/watch?v=xQYjaYAvyms&t=733s',
      'video_id': 'xQYjaYAvyms'},
     {'author': 'Freight 360',
      'channel': 'Freight 360',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:12](https://www.youtube.com/watch?v=FtL-2SOSFOU&t=192s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '"Well, no, like you should pay this, right?" And then the broker\'s in the '
              'middle because the shipper\'s going like, "No, like I\'m just not paying you '
              'the other 100 grand I owe you until you get the claim paid." Carrier\'s '
              'insurance goes, "Denied.".',
      'timestamp': 192,
      'timestamp_label': '[00:03:12]',
      'timestamp_seconds': 192,
      'tip': '"Well, no, like you should pay this, right?" And then the broker\'s in the '
             'middle because the shipper\'s going like, "No, like I\'m just not paying you the '
             'other 100 grand I owe you until you get the claim paid." Carrier\'s insurance '
             'goes, "Denied.".',
      'title': 'The Truth About Contingent Cargo Insurance in Trucking | Freight 360 Clips '
               '(Freight 360)',
      'url': 'https://www.youtube.com/watch?v=FtL-2SOSFOU&t=192s',
      'video_id': 'FtL-2SOSFOU'},
     {'author': 'Truckstop . com',
      'channel': 'Truckstop . com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=9d907d-1DzE&t=111s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Daily updates change notifications and sourcing tools to safeguard your '
              'business remember in this industry knowledge is your best defense against fraud '
              'stay informed stay vigilant and together we can keep your business safe and '
              'thriving.',
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': 'Daily updates change notifications and sourcing tools to safeguard your business '
             'remember in this industry knowledge is your best defense against fraud stay '
             'informed stay vigilant and together we can keep your business safe and thriving.',
      'title': '5 Ways to Avoid Double-Brokering Scams: Fraud Prevention Friday | Truckstop '
               '(Truckstop . com)',
      'url': 'https://www.youtube.com/watch?v=9d907d-1DzE&t=111s',
      'video_id': '9d907d-1DzE'},
     {'author': 'B3FinalMile',
      'channel': 'B3FinalMile',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:01](https://www.youtube.com/watch?v=pRXH47gm66A&t=61s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re assuming liability, it's going to be much more difficult and challenging "
              'for any attorney, any insurance company to defend you and to defend the fact '
              "that you're not legally liable because now you're no longer acting as just a "
              'freight broker.',
      'timestamp': 61,
      'timestamp_label': '[00:01:01]',
      'timestamp_seconds': 61,
      'tip': "'re assuming liability, it's going to be much more difficult and challenging for "
             'any attorney, any insurance company to defend you and to defend the fact that '
             "you're not legally liable because now you're no longer acting as just a freight "
             'broker.',
      'title': 'Why Contingent Auto Pricing Breaks Down When You Act Like a Carrier '
               '(B3FinalMile)',
      'url': 'https://www.youtube.com/watch?v=pRXH47gm66A&t=61s',
      'video_id': 'pRXH47gm66A'},
     {'author': 'Freight 360',
      'channel': 'Freight 360',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:50:18](https://www.youtube.com/watch?v=qTcDOmwZMjI&t=3018s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The insurance agent goes, yeah, sure, it's primary. And I'm like, this person "
              'at this multi-billion dollar company thought by asking the insurance agent to '
              "make this a primary policy, it's all of a sudden not contingent cargo.",
      'timestamp': 3018,
      'timestamp_label': '[00:50:18]',
      'timestamp_seconds': 3018,
      'tip': "The insurance agent goes, yeah, sure, it's primary. And I'm like, this person at "
             'this multi-billion dollar company thought by asking the insurance agent to make '
             "this a primary policy, it's all of a sudden not contingent cargo.",
      'title': 'What Contingent Cargo Insurance Actually Covers | Episode 342 (Freight 360)',
      'url': 'https://www.youtube.com/watch?v=qTcDOmwZMjI&t=3018s',
      'video_id': 'qTcDOmwZMjI'},
     {'author': 'Cargo Rant',
      'channel': 'Cargo Rant',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:00](https://www.youtube.com/watch?v=NxIispBOkz8&t=480s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Line and then you turn to your consultant at that point you may have already '
              "jeopardized your claim Beyond repair so I'll urge you to contact them well "
              'before you establish any sort of meaningful communication with your shipping '
              'line.',
      'timestamp': 480,
      'timestamp_label': '[00:08:00]',
      'timestamp_seconds': 480,
      'tip': 'Line and then you turn to your consultant at that point you may have already '
             "jeopardized your claim Beyond repair so I'll urge you to contact them well "
             'before you establish any sort of meaningful communication with your shipping '
             'line.',
      'title': 'How to nail your next cargo claim against a shipping line (Cargo Rant)',
      'url': 'https://www.youtube.com/watch?v=NxIispBOkz8&t=480s',
      'video_id': 'NxIispBOkz8'},
     {'author': 'FreightWaves',
      'channel': 'FreightWaves',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=MobEZyaIjV4&t=60s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Not just communication with your partners or customers but communication '
              'between the systems that you use to run your business so we streamline '
              'communication between systems like financial management systems elds.',
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': 'Not just communication with your partners or customers but communication between '
             'the systems that you use to run your business so we streamline communication '
             'between systems like financial management systems elds.',
      'title': 'Rose Rocket - Transportation Management Software (TMS) - Demo (FreightWaves)',
      'url': 'https://www.youtube.com/watch?v=MobEZyaIjV4&t=60s',
      'video_id': 'MobEZyaIjV4'},
     {'author': 'Double Broker Bounty Hunter',
      'channel': 'Double Broker Bounty Hunter',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:46](https://www.youtube.com/watch?v=aSSPaOdn5ZI&t=406s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ask you to verify your ID so you click on secure my account it gives you a '
              'brief description of how the setup goes you submit the ID you take a selfie uh '
              'the AI then does an identity verification and then it uh accepts you and logs '
              'you in so you go ahead and hit.',
      'timestamp': 406,
      'timestamp_label': '[00:06:46]',
      'timestamp_seconds': 406,
      'tip': 'Ask you to verify your ID so you click on secure my account it gives you a brief '
             'description of how the setup goes you submit the ID you take a selfie uh the AI '
             'then does an identity verification and then it uh accepts you and logs you in so '
             'you go ahead and hit.',
      'title': 'DBBH Fraud Prevention   Truckstop MFA and RMIS Setups (Double Broker Bounty '
               'Hunter)',
      'url': 'https://www.youtube.com/watch?v=aSSPaOdn5ZI&t=406s',
      'video_id': 'aSSPaOdn5ZI'},
     {'author': 'Matt Krause',
      'channel': 'Matt Krause',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:29](https://www.youtube.com/watch?v=NF0itNMuQvY&t=749s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t chase it, you just stay a normal connection and you keep the commenting on "
              'their stuff because plants change carriers on a Friday afternoon and the '
              'freight broker they remember is the one who never pushed. Bruce says like, '
              '"Yeah, sure.',
      'timestamp': 749,
      'timestamp_label': '[00:12:29]',
      'timestamp_seconds': 749,
      'tip': "'t chase it, you just stay a normal connection and you keep the commenting on "
             'their stuff because plants change carriers on a Friday afternoon and the freight '
             'broker they remember is the one who never pushed. Bruce says like, "Yeah, sure.',
      'title': 'How Freight Brokers Get Shippers Without Cold Calling (Matt Krause)',
      'url': 'https://www.youtube.com/watch?v=NF0itNMuQvY&t=749s',
      'video_id': 'NF0itNMuQvY'},
     {'author': 'FreightBrokers',
      'channel': 'FreightBrokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:53:12](https://www.youtube.com/watch?v=90xG4lQaA6Q&t=3192s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Accelerator waight list if you're just getting started and you're looking for "
              "some startup help maybe you're not ready for the freight Breer sales acceler "
              "that's fine check out freightbrokerbootcamp.",
      'timestamp': 3192,
      'timestamp_label': '[00:53:12]',
      'timestamp_seconds': 3192,
      'tip': "Accelerator waight list if you're just getting started and you're looking for "
             "some startup help maybe you're not ready for the freight Breer sales acceler "
             "that's fine check out freightbrokerbootcamp.",
      'title': 'LIVE Freight Broker Cold Calling Training - Freight Broker Boot Camp with '
               'Dennis Brown (FreightBrokers)',
      'url': 'https://www.youtube.com/watch?v=90xG4lQaA6Q&t=3192s',
      'video_id': '90xG4lQaA6Q'},
     {'author': 'Freight 360',
      'channel': 'Freight 360',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:24](https://www.youtube.com/watch?v=kAT7s21mZIE&t=264s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Things for you let us know what you think in the comments down below and feel '
              'free to send us a message anytime at freight360.net if you have a question or a '
              "topic that you want us to cover thanks for watching and we'll see you in the "
              'next video.',
      'timestamp': 264,
      'timestamp_label': '[00:04:24]',
      'timestamp_seconds': 264,
      'tip': 'Things for you let us know what you think in the comments down below and feel '
             'free to send us a message anytime at freight360.net if you have a question or a '
             "topic that you want us to cover thanks for watching and we'll see you in the "
             'next video.',
      'title': 'What is contingent cargo insurance? Everything you need to know (Freight 360)',
      'url': 'https://www.youtube.com/watch?v=kAT7s21mZIE&t=264s',
      'video_id': 'kAT7s21mZIE'}],
 5: [{'author': 'FreightBrokers',
      'channel': 'FreightBrokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:17](https://www.youtube.com/watch?v=yiDO9s6ArZU&t=437s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The bond is required by the FMCSA. Insurance depends on your business model, '
              'your customers, and your risk tolerance. Can someone make a claim against your '
              "bond? That's why you need to operate properly. Don't work with bad customers.",
      'timestamp': 437,
      'timestamp_label': '[00:07:17]',
      'timestamp_seconds': 437,
      'tip': 'The bond is required by the FMCSA. Insurance depends on your business model, '
             'your customers, and your risk tolerance. Can someone make a claim against your '
             "bond? That's why you need to operate properly. Don't work with bad customers.",
      'title': 'Freight Broker Surety Bond in Simple Terms 🤔 (FreightBrokers)',
      'url': 'https://www.youtube.com/watch?v=yiDO9s6ArZU&t=437s',
      'video_id': 'yiDO9s6ArZU'},
     {'author': 'Matt Krause',
      'channel': 'Matt Krause',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:32](https://www.youtube.com/watch?v=LNT0OaH1J8s&t=512s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Okay, for starters, let's stop thinking of it as cold calling, even though it "
              "is. It's Yeah, like it might sound as though you're you're bugging these "
              "people, but think of it as problem solving. And you're not just dialing random "
              'numbers hoping to beg for business.',
      'timestamp': 512,
      'timestamp_label': '[00:08:32]',
      'timestamp_seconds': 512,
      'tip': "Okay, for starters, let's stop thinking of it as cold calling, even though it "
             "is. It's Yeah, like it might sound as though you're you're bugging these people, "
             "but think of it as problem solving. And you're not just dialing random numbers "
             'hoping to beg for business.',
      'title': 'What I Learned from 23,000 Cold Calls as a Freight Broker (My Script Included) '
               '(Matt Krause)',
      'url': 'https://www.youtube.com/watch?v=LNT0OaH1J8s&t=512s',
      'video_id': 'LNT0OaH1J8s'},
     {'author': 'ThinkFreight',
      'channel': 'ThinkFreight',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=s-qzw5ZxjmU&t=28s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This new rule gives the FMCSA expanded authority to step in when brokers and '
              'freight forwarders fail to pay carriers for services already performed. And as '
              'we know, at its core, this this rule targets a problem that carriers have '
              'complained about for years.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': 'This new rule gives the FMCSA expanded authority to step in when brokers and '
             'freight forwarders fail to pay carriers for services already performed. And as '
             'we know, at its core, this this rule targets a problem that carriers have '
             'complained about for years.',
      'title': 'FINALLY: FMCSA Targets Freight Brokers With New Rule (ThinkFreight)',
      'url': 'https://www.youtube.com/watch?v=s-qzw5ZxjmU&t=28s',
      'video_id': 's-qzw5ZxjmU'},
     {'author': 'Brandon Scott',
      'channel': 'Brandon Scott',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=V11p0IBJsTk&t=65s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So in today's video, I'm gonna highlight the issue that freight brokers and "
              "carriers often have. I'm gonna show you why they're having that issue, who is "
              "at fault and how we can avoid this problem moving forward. So now let's get "
              'into the business.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': "So in today's video, I'm gonna highlight the issue that freight brokers and "
             "carriers often have. I'm gonna show you why they're having that issue, who is at "
             "fault and how we can avoid this problem moving forward. So now let's get into "
             'the business.',
      'title': 'How Freight Brokers Handle Detention And Rate Issues! (Brandon Scott)',
      'url': 'https://www.youtube.com/watch?v=V11p0IBJsTk&t=65s',
      'video_id': 'V11p0IBJsTk'},
     {'author': 'Trade Risk Guaranty',
      'channel': 'Trade Risk Guaranty',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:36](https://www.youtube.com/watch?v=pbs3U-vmpzM&t=156s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'However, if your shipment is covered by all-risk cargo insurance, proof of '
              'value and loss is required, claims are typically paid within 30 days, claim '
              'payments cover all losses under the policy limit, and you are not required to '
              'prove carrier negligence.',
      'timestamp': 156,
      'timestamp_label': '[00:02:36]',
      'timestamp_seconds': 156,
      'tip': 'However, if your shipment is covered by all-risk cargo insurance, proof of value '
             'and loss is required, claims are typically paid within 30 days, claim payments '
             'cover all losses under the policy limit, and you are not required to prove '
             'carrier negligence.',
      'title': 'Carrier Limit of Liability: Filing a Claim (Trade Risk Guaranty)',
      'url': 'https://www.youtube.com/watch?v=pbs3U-vmpzM&t=156s',
      'video_id': 'pbs3U-vmpzM'},
     {'author': 'Truck Driver Nation',
      'channel': 'Truck Driver Nation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:56](https://www.youtube.com/watch?v=5dP6IV7sJW0&t=176s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Obviously they're going to say something to the broker if they've been doing "
              'business for any extensive period of time you know why have I got this.',
      'timestamp': 176,
      'timestamp_label': '[00:02:56]',
      'timestamp_seconds': 176,
      'tip': "Obviously they're going to say something to the broker if they've been doing "
             'business for any extensive period of time you know why have I got this.',
      'title': 'Trucking Scams & Fraud Prevention How to Avoid Double Brokering Pitfalls '
               '(Truck Driver Nation)',
      'url': 'https://www.youtube.com/watch?v=5dP6IV7sJW0&t=176s',
      'video_id': '5dP6IV7sJW0'},
     {'author': 'Bobby Loads',
      'channel': 'Bobby Loads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:36:07](https://www.youtube.com/watch?v=bkrMqfq4evM&t=2167s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They're scared, but like you know, any advice you have for them if they want to "
              'get into the freight broker game? Well, the only advice I got, especially if '
              "someone's afraid, uh is is fear is a good motivator to fail.",
      'timestamp': 2167,
      'timestamp_label': '[00:36:07]',
      'timestamp_seconds': 2167,
      'tip': "They're scared, but like you know, any advice you have for them if they want to "
             'get into the freight broker game? Well, the only advice I got, especially if '
             "someone's afraid, uh is is fear is a good motivator to fail.",
      'title': 'How to Become a Freight Agent—and How the Money Works (Bobby Loads)',
      'url': 'https://www.youtube.com/watch?v=bkrMqfq4evM&t=2167s',
      'video_id': 'bkrMqfq4evM'},
     {'author': '【Logistics YouTuber】 IINO san',
      'channel': '【Logistics YouTuber】 IINO san',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=xxk_vmQarVo&t=51s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Import and export cargo to cover various unforeseen accidents and risks that '
              'may occur during transportation since international transportation involves.',
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': 'Import and export cargo to cover various unforeseen accidents and risks that may '
             'occur during transportation since international transportation involves.',
      'title': 'Explanation of the basic of Cargo Insurance！Insured Amount and how to '
               'calculate Insurance Premium (【Logistics YouTuber】 IINO san)',
      'url': 'https://www.youtube.com/watch?v=xxk_vmQarVo&t=51s',
      'video_id': 'xxk_vmQarVo'},
     {'author': 'Trucking Territory',
      'channel': 'Trucking Territory',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:36](https://www.youtube.com/watch?v=Q-HgB9nn1jI&t=216s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Broker of course thank you the biggest problem with detentions and layovers is '
              'that a lot of Brokers will.',
      'timestamp': 216,
      'timestamp_label': '[00:03:36]',
      'timestamp_seconds': 216,
      'tip': 'Broker of course thank you the biggest problem with detentions and layovers is '
             'that a lot of Brokers will.',
      'title': 'How To Make Freight Brokers Pay For Detentions & Layovers (Trucking Territory)',
      'url': 'https://www.youtube.com/watch?v=Q-HgB9nn1jI&t=216s',
      'video_id': 'Q-HgB9nn1jI'},
     {'author': 'FMCSA',
      'channel': 'FMCSA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=B48yGdlbTbo&t=68s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Moving right along to the filing options box. Here, you're going to select the "
              'operating authority you want to make a filing for, as well as the specific form '
              'you need to file.',
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': "Moving right along to the filing options box. Here, you're going to select the "
             'operating authority you want to make a filing for, as well as the specific form '
             'you need to file.',
      'title': 'File a BMC-84 / BMC-85 | Motus Explainer Series (FMCSA)',
      'url': 'https://www.youtube.com/watch?v=B48yGdlbTbo&t=68s',
      'video_id': 'B48yGdlbTbo'},
     {'author': 'Freightbrokerchic',
      'channel': 'Freightbrokerchic',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:20](https://www.youtube.com/watch?v=zvX7UreND4E&t=500s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Send a modified rate con or updated rate con now i guess unless it's something "
              'that the broker honestly uh.',
      'timestamp': 500,
      'timestamp_label': '[00:08:20]',
      'timestamp_seconds': 500,
      'tip': "Send a modified rate con or updated rate con now i guess unless it's something "
             'that the broker honestly uh.',
      'title': 'FREIGHT BROKER CHIC—-“TONU or DETENTION THAT IS THE QUESTION!” '
               '(Freightbrokerchic)',
      'url': 'https://www.youtube.com/watch?v=zvX7UreND4E&t=500s',
      'video_id': 'zvX7UreND4E'},
     {'author': 'Freight 360',
      'channel': 'Freight 360',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=gnxgKnnz6Jw&t=15s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "At its worst since mid 2022 today I'm here to share five ways for you to stay "
              'vigilant as a freight broker and spot these Bad actors before.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "At its worst since mid 2022 today I'm here to share five ways for you to stay "
             'vigilant as a freight broker and spot these Bad actors before.',
      'title': "How to Identify Double Broker's | Freight 360 (Freight 360)",
      'url': 'https://www.youtube.com/watch?v=gnxgKnnz6Jw&t=15s',
      'video_id': 'gnxgKnnz6Jw'},
     {'author': 'Highway',
      'channel': 'Highway',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:50](https://www.youtube.com/watch?v=sKKld4Wdyqg&t=170s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You but we give you all the warning signs and all the information you need to '
              "make a great decision now if you haven't started your free trial of carrierless "
              'you can click on the link below in this description or as well you can always '
              'go to www.carrierless.com.',
      'timestamp': 170,
      'timestamp_label': '[00:02:50]',
      'timestamp_seconds': 170,
      'tip': 'You but we give you all the warning signs and all the information you need to '
             "make a great decision now if you haven't started your free trial of carrierless "
             'you can click on the link below in this description or as well you can always go '
             'to www.carrierless.com.',
      'title': 'Detecting double brokering and fraud (Highway)',
      'url': 'https://www.youtube.com/watch?v=sKKld4Wdyqg&t=170s',
      'video_id': 'sKKld4Wdyqg'},
     {'author': 'AscendTMS - The Free (and Best) TMS Software',
      'channel': 'AscendTMS - The Free (and Best) TMS Software',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:08](https://www.youtube.com/watch?v=ICIyOtMiEqY&t=1148s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Industry and you have no verification it's also if you already have carrier "
              "verification inside of your whatever you're using today this is also good to "
              'use in conjunction.',
      'timestamp': 1148,
      'timestamp_label': '[00:19:08]',
      'timestamp_seconds': 1148,
      'tip': "Industry and you have no verification it's also if you already have carrier "
             "verification inside of your whatever you're using today this is also good to use "
             'in conjunction.',
      'title': "A Full Tour of AscendTMS for 3PL's, Logistics Brokers and Shippers (AscendTMS "
               '- The Free (and Best) TMS Software)',
      'url': 'https://www.youtube.com/watch?v=ICIyOtMiEqY&t=1148s',
      'video_id': 'ICIyOtMiEqY'},
     {'author': 'Matt Krause',
      'channel': 'Matt Krause',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:21](https://www.youtube.com/watch?v=WsoJiATaDqk&t=561s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I know you hear it all day every day but it actually genuinely does help small '
              "channels like mine I'll see you in the next one.",
      'timestamp': 561,
      'timestamp_label': '[00:09:21]',
      'timestamp_seconds': 561,
      'tip': 'I know you hear it all day every day but it actually genuinely does help small '
             "channels like mine I'll see you in the next one.",
      'title': 'FMCSA vs. Broker Transparency: Are Carriers Being Left in the Cold? (Matt '
               'Krause)',
      'url': 'https://www.youtube.com/watch?v=WsoJiATaDqk&t=561s',
      'video_id': 'WsoJiATaDqk'}],
 6: [{'author': 'eCarrierCheck',
      'channel': 'eCarrierCheck',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=gwNcz_V8JZ0&t=108s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re a sourcing utility platform so if you're getting you know if you're a "
              "dispatcher freight broker per carrier, maybe an insurance. You know, we're here "
              'to help you find leads to carriers, shippers, and brokers.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': "'re a sourcing utility platform so if you're getting you know if you're a "
             "dispatcher freight broker per carrier, maybe an insurance. You know, we're here "
             'to help you find leads to carriers, shippers, and brokers.',
      'title': 'Freight Broker Sales Cold Calling: Unbeatable Techniques (eCarrierCheck)',
      'url': 'https://www.youtube.com/watch?v=gwNcz_V8JZ0&t=108s',
      'video_id': 'gwNcz_V8JZ0'},
     {'author': 'FreightBrokers',
      'channel': 'FreightBrokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:39:51](https://www.youtube.com/watch?v=dciVQpw-BWM&t=2391s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You still have to overcome those hurdles, right? That's where my freight broker "
              'boot camp startup training works, right? But this is my sales accelerator '
              "program. So, if you get on the wait list, you'll be the first to get notified.",
      'timestamp': 2391,
      'timestamp_label': '[00:39:51]',
      'timestamp_seconds': 2391,
      'tip': "You still have to overcome those hurdles, right? That's where my freight broker "
             'boot camp startup training works, right? But this is my sales accelerator '
             "program. So, if you get on the wait list, you'll be the first to get notified.",
      'title': 'Freight Broker / Agent LIVE Q&A with Dennis Brown 1/12/25 📱 (FreightBrokers)',
      'url': 'https://www.youtube.com/watch?v=dciVQpw-BWM&t=2391s',
      'video_id': 'dciVQpw-BWM'},
     {'author': 'FreightBrokers',
      'channel': 'FreightBrokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:39:51](https://www.youtube.com/watch?v=UhCy0ncTrTI&t=2391s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You still have to overcome those hurdles, right? That's where my freight broker "
              'boot camp startup training works, right? But this is my sales accelerator '
              "program. So, if you get on the weight list, you'll be the first to get "
              'notified.',
      'timestamp': 2391,
      'timestamp_label': '[00:39:51]',
      'timestamp_seconds': 2391,
      'tip': "You still have to overcome those hurdles, right? That's where my freight broker "
             'boot camp startup training works, right? But this is my sales accelerator '
             "program. So, if you get on the weight list, you'll be the first to get notified.",
      'title': 'Freight Broker / Agent LIVE Q&A with Dennis Brown 1/12/25 (FreightBrokers)',
      'url': 'https://www.youtube.com/watch?v=UhCy0ncTrTI&t=2391s',
      'video_id': 'UhCy0ncTrTI'},
     {'author': 'Freight Broker TV',
      'channel': 'Freight Broker TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:54](https://www.youtube.com/watch?v=wSNSmdThc6A&t=294s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Here's why a bond okay first of all if you go to a any bonding company website "
              "here's one this is jw shirty bonds but right there it says get started now you "
              "will choose in that box the first thing you're going to choose the bmc.",
      'timestamp': 294,
      'timestamp_label': '[00:04:54]',
      'timestamp_seconds': 294,
      'tip': "Here's why a bond okay first of all if you go to a any bonding company website "
             "here's one this is jw shirty bonds but right there it says get started now you "
             "will choose in that box the first thing you're going to choose the bmc.",
      'title': "Freight Broker Bond - BMC 84? BMC 85? Don't Be Taken To The Bank! (Freight "
               'Broker TV)',
      'url': 'https://www.youtube.com/watch?v=wSNSmdThc6A&t=294s',
      'video_id': 'wSNSmdThc6A'},
     {'author': 'Trucking Made Successful',
      'channel': 'Trucking Made Successful',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:12](https://www.youtube.com/watch?v=M0KZ3BZctSQ&t=132s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The reason we don't feel uh I would say the change as much just because of the "
              'diesel prices. All right, now an old chart that we are very familiar with. This '
              'is the ELP out of service orders by month and I have data up to May 30th from '
              'search carriers.',
      'timestamp': 132,
      'timestamp_label': '[00:02:12]',
      'timestamp_seconds': 132,
      'tip': "The reason we don't feel uh I would say the change as much just because of the "
             'diesel prices. All right, now an old chart that we are very familiar with. This '
             'is the ELP out of service orders by month and I have data up to May 30th from '
             'search carriers.',
      'title': 'Trucking Market Update: Spot Market: Flatbed, Reefer, Van, Hot Shot, '
               'Specialized (Trucking Made Successful)',
      'url': 'https://www.youtube.com/watch?v=M0KZ3BZctSQ&t=132s',
      'video_id': 'M0KZ3BZctSQ'},
     {'author': 'Thee Freight Broker Report',
      'channel': 'Thee Freight Broker Report',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:03](https://www.youtube.com/watch?v=O1ZmR8X3CRg&t=243s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Uh PFA protex that's company that I'm with right now but I applied to some of "
              "the big ones and I'm about to share with you what was uh what was discussed "
              'reason why my application was not approved CU my credit is not bad let me see '
              'see if I can find.',
      'timestamp': 243,
      'timestamp_label': '[00:04:03]',
      'timestamp_seconds': 243,
      'tip': "Uh PFA protex that's company that I'm with right now but I applied to some of "
             "the big ones and I'm about to share with you what was uh what was discussed "
             'reason why my application was not approved CU my credit is not bad let me see '
             'see if I can find.',
      'title': 'HOW TO GET YOUR (BMC-84) SURETY BOND (Thee Freight Broker Report)',
      'url': 'https://www.youtube.com/watch?v=O1ZmR8X3CRg&t=243s',
      'video_id': 'O1ZmR8X3CRg'},
     {'author': 'Craig Bliss',
      'channel': 'Craig Bliss',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:34](https://www.youtube.com/watch?v=WU9uuEFffXU&t=454s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Consider finding a new broker I hope this helps well you can find this cheat '
              'sheet written out with examples of average detention pay under the units tab '
              'and micro freight brokers and truck drivers let me know what works best for '
              'your operation.',
      'timestamp': 454,
      'timestamp_label': '[00:07:34]',
      'timestamp_seconds': 454,
      'tip': 'Consider finding a new broker I hope this helps well you can find this cheat '
             'sheet written out with examples of average detention pay under the units tab and '
             'micro freight brokers and truck drivers let me know what works best for your '
             'operation.',
      'title': "Detention Secrets Brokers Don't Want Carriers to Know About (Craig Bliss)",
      'url': 'https://www.youtube.com/watch?v=WU9uuEFffXU&t=454s',
      'video_id': 'WU9uuEFffXU'},
     {'author': 'Freightskills',
      'channel': 'Freightskills',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:07](https://www.youtube.com/watch?v=o6WTbGsyLqg&t=367s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "How do we move it where do we find carriers to do it now this part's a little "
              "bit harder because it's not as easy to just post these loads on a.",
      'timestamp': 367,
      'timestamp_label': '[00:06:07]',
      'timestamp_seconds': 367,
      'tip': "How do we move it where do we find carriers to do it now this part's a little "
             "bit harder because it's not as easy to just post these loads on a.",
      'title': 'What is Container Drayage | Freight Broker Edition (Freightskills)',
      'url': 'https://www.youtube.com/watch?v=o6WTbGsyLqg&t=367s',
      'video_id': 'o6WTbGsyLqg'},
     {'author': 'CONGO EXPRESS',
      'channel': 'CONGO EXPRESS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:24](https://www.youtube.com/watch?v=vSgjLSdmTKc&t=144s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Boys I would have to get on it find a load bid on it and hopefully my bid is '
              'low enough in order for the broker to book me to do that load load mesh on the '
              'other hand.',
      'timestamp': 144,
      'timestamp_label': '[00:02:24]',
      'timestamp_seconds': 144,
      'tip': 'Boys I would have to get on it find a load bid on it and hopefully my bid is low '
             'enough in order for the broker to book me to do that load load mesh on the other '
             'hand.',
      'title': 'How to find drayage / intermodal loads (CONGO EXPRESS)',
      'url': 'https://www.youtube.com/watch?v=vSgjLSdmTKc&t=144s',
      'video_id': 'vSgjLSdmTKc'},
     {'author': 'Matt Krause',
      'channel': 'Matt Krause',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:56](https://www.youtube.com/watch?v=afV63okbAMs&t=596s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So the real problem was never effort. And most of the hundred companies on that '
              "list didn't even have any freight that needed a freight broker. So it didn't "
              "matter how good I sounded. So let's fix that list first.",
      'timestamp': 596,
      'timestamp_label': '[00:09:56]',
      'timestamp_seconds': 596,
      'tip': 'So the real problem was never effort. And most of the hundred companies on that '
             "list didn't even have any freight that needed a freight broker. So it didn't "
             "matter how good I sounded. So let's fix that list first.",
      'title': 'Full 2027 Freight Broker Training (Start to First Load) (Matt Krause)',
      'url': 'https://www.youtube.com/watch?v=afV63okbAMs&t=596s',
      'video_id': 'afV63okbAMs'},
     {'author': 'Bobby Loads',
      'channel': 'Bobby Loads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:02](https://www.youtube.com/watch?v=Gz22R2KL_e4&t=1022s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, that's the update for the East Coast. We're not going to search them. We "
              'already know what the deal is. Get a good money going in, take cheap money '
              'going out. The volume is there in those areas.',
      'timestamp': 1022,
      'timestamp_label': '[00:17:02]',
      'timestamp_seconds': 1022,
      'tip': "So, that's the update for the East Coast. We're not going to search them. We "
             'already know what the deal is. Get a good money going in, take cheap money going '
             'out. The volume is there in those areas.',
      'title': 'DAT Trucking market update which lanes are making money right now (Bobby '
               'Loads)',
      'url': 'https://www.youtube.com/watch?v=Gz22R2KL_e4&t=1022s',
      'video_id': 'Gz22R2KL_e4'},
     {'author': 'FreightBrokers',
      'channel': 'FreightBrokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:19](https://www.youtube.com/watch?v=knW5LzcUJIw&t=319s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So the next time a shipper says, "We don\'t use brokers," don\'t argue or hang '
              "up. Find out whether it's a company policy or whether another broker burned "
              "them. If it's a bad experience, explain one meaningful way you're different.",
      'timestamp': 319,
      'timestamp_label': '[00:05:19]',
      'timestamp_seconds': 319,
      'tip': 'So the next time a shipper says, "We don\'t use brokers," don\'t argue or hang '
             "up. Find out whether it's a company policy or whether another broker burned "
             "them. If it's a bad experience, explain one meaningful way you're different.",
      'title': 'Freight Broker Cold Calling Script: Handle This Objection 📞 (FreightBrokers)',
      'url': 'https://www.youtube.com/watch?v=knW5LzcUJIw&t=319s',
      'video_id': 'knW5LzcUJIw'},
     {'author': 'Freight Master Resources',
      'channel': 'Freight Master Resources',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:32:18](https://www.youtube.com/watch?v=dFv317bclEU&t=1938s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Know I if somebody wants to explain that to me uh maybe they penalized you or '
              "something a you know with the load delivered for something I don't know.",
      'timestamp': 1938,
      'timestamp_label': '[00:32:18]',
      'timestamp_seconds': 1938,
      'tip': 'Know I if somebody wants to explain that to me uh maybe they penalized you or '
             "something a you know with the load delivered for something I don't know.",
      'title': 'Freight Broker Transparency   FMCSA Proposes New Rules (Freight Master '
               'Resources)',
      'url': 'https://www.youtube.com/watch?v=dFv317bclEU&t=1938s',
      'video_id': 'dFv317bclEU'},
     {'author': 'Matt Krause',
      'channel': 'Matt Krause',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:32](https://www.youtube.com/watch?v=6yGrLWuRK6g&t=152s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Someone to help move that Freight too they could have a product change that '
              'could increase sales so the that type of list can go on forever and you can '
              'find.',
      'timestamp': 152,
      'timestamp_label': '[00:02:32]',
      'timestamp_seconds': 152,
      'tip': 'Someone to help move that Freight too they could have a product change that '
             'could increase sales so the that type of list can go on forever and you can '
             'find.',
      'title': '6 Step Cold Call Guide For Freight Brokers (Matt Krause)',
      'url': 'https://www.youtube.com/watch?v=6yGrLWuRK6g&t=152s',
      'video_id': '6yGrLWuRK6g'},
     {'author': 'FreightBrokers',
      'channel': 'FreightBrokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:18](https://www.youtube.com/watch?v=BCLv7SfCxIo&t=1338s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Look at the label and you'll see the name sometimes you'll even see the address "
              'take a picture of it with your phone and then walk down the aisle and grab '
              'another product.',
      'timestamp': 1338,
      'timestamp_label': '[00:22:18]',
      'timestamp_seconds': 1338,
      'tip': "Look at the label and you'll see the name sometimes you'll even see the address "
             'take a picture of it with your phone and then walk down the aisle and grab '
             'another product.',
      'title': 'LIVE Freight Broker Training with Dennis Brown (FreightBrokers)',
      'url': 'https://www.youtube.com/watch?v=BCLv7SfCxIo&t=1338s',
      'video_id': 'BCLv7SfCxIo'}],
 7: [{'author': 'FMCSA REGISTRATION dot com',
      'channel': 'FMCSA REGISTRATION dot com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:14](https://www.youtube.com/watch?v=HPAThSeqX3c&t=74s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If your application is approved, you will receive your MC number, which is your '
              'unique identifier as a freight broker. Obtaining freight broker authority is an '
              'important step in starting your own brokerage business.',
      'timestamp': 74,
      'timestamp_label': '[00:01:14]',
      'timestamp_seconds': 74,
      'tip': 'If your application is approved, you will receive your MC number, which is your '
             'unique identifier as a freight broker. Obtaining freight broker authority is an '
             'important step in starting your own brokerage business.',
      'title': 'Apply for Freight Broker Authority | Easy Steps To Get Your Freight Broker '
               'License (FMCSA REGISTRATION dot com)',
      'url': 'https://www.youtube.com/watch?v=HPAThSeqX3c&t=74s',
      'video_id': 'HPAThSeqX3c'},
     {'author': 'FMCSA REGISTRATION dot com',
      'channel': 'FMCSA REGISTRATION dot com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:12](https://www.youtube.com/watch?v=_6EAOmYcoCY&t=132s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Trust Fund Agreement with a $75,000 Surety Bond and file Form: BMC-85. Every '
              'new broker of household goods also needs to file a BOC-3 form with the FMCSA. '
              'This is the official Designation of Process Agent Form.',
      'timestamp': 132,
      'timestamp_label': '[00:02:12]',
      'timestamp_seconds': 132,
      'tip': 'Trust Fund Agreement with a $75,000 Surety Bond and file Form: BMC-85. Every new '
             'broker of household goods also needs to file a BOC-3 form with the FMCSA. This '
             'is the official Designation of Process Agent Form.',
      'title': 'Broker Authority | Learn about Freight Broker authority Success (FMCSA '
               'REGISTRATION dot com)',
      'url': 'https://www.youtube.com/watch?v=_6EAOmYcoCY&t=132s',
      'video_id': '_6EAOmYcoCY'},
     {'author': 'Victor Mason',
      'channel': 'Victor Mason',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=8AGIyPDUcqY&t=114s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Step three is outreach, and this is where most people quit because outreach can '
              "be uncomfortable. Cold calling, emails, messages, showing up in person. You're "
              "going to hear no, and you're going to get ignored, but that's part of the "
              'process.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': 'Step three is outreach, and this is where most people quit because outreach can '
             "be uncomfortable. Cold calling, emails, messages, showing up in person. You're "
             "going to hear no, and you're going to get ignored, but that's part of the "
             'process.',
      'title': 'The Real Way Freight Brokers Land Shippers (Not What You Think) (Victor Mason)',
      'url': 'https://www.youtube.com/watch?v=8AGIyPDUcqY&t=114s',
      'video_id': '8AGIyPDUcqY'},
     {'author': 'Sales Scripter',
      'channel': 'Sales Scripter',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=sagwYgVmVaE&t=72s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, a really good cold call there. And there are some key things that this '
              'salesperson did that made this cold call easier and put him in such a good '
              'position to close the prospect on the next step of his sales process.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': 'So, a really good cold call there. And there are some key things that this '
             'salesperson did that made this cold call easier and put him in such a good '
             'position to close the prospect on the next step of his sales process.',
      'title': 'Example of a Cold Call for Logistics and Freight Services (Sales Scripter)',
      'url': 'https://www.youtube.com/watch?v=sagwYgVmVaE&t=72s',
      'video_id': 'sagwYgVmVaE'},
     {'author': 'Alfa X Logistics',
      'channel': 'Alfa X Logistics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:53](https://www.youtube.com/watch?v=CNjYZO0c1o4&t=53s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But, getting back to our question, are you responsible for getting them? You're "
              'not responsible, okay? The relationship or the agreement to transport cargo is '
              "between motor carrier and a freight broker, okay? You're just assisting with "
              'the process.',
      'timestamp': 53,
      'timestamp_label': '[00:00:53]',
      'timestamp_seconds': 53,
      'tip': "But, getting back to our question, are you responsible for getting them? You're "
             'not responsible, okay? The relationship or the agreement to transport cargo is '
             "between motor carrier and a freight broker, okay? You're just assisting with the "
             'process.',
      'title': 'Are Truck Dispatchers financially responsible for Detention, Layover and TONU? '
               '(Alfa X Logistics)',
      'url': 'https://www.youtube.com/watch?v=CNjYZO0c1o4&t=53s',
      'video_id': 'CNjYZO0c1o4'},
     {'author': 'FreightBrokers',
      'channel': 'FreightBrokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:30](https://www.youtube.com/watch?v=J9NA2KM5qzE&t=1710s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I mean, I'm not quite sure. If you are an agent working for a brokerage, then "
              "they should already have an onboarding process. If they don't have an "
              "onboarding process, then that's something you might want to question.",
      'timestamp': 1710,
      'timestamp_label': '[00:28:30]',
      'timestamp_seconds': 1710,
      'tip': "I mean, I'm not quite sure. If you are an agent working for a brokerage, then "
             "they should already have an onboarding process. If they don't have an onboarding "
             "process, then that's something you might want to question.",
      'title': 'Freight Broker LIVE Q & A with  Dennis Brown 2/23/26 (FreightBrokers)',
      'url': 'https://www.youtube.com/watch?v=J9NA2KM5qzE&t=1710s',
      'video_id': 'J9NA2KM5qzE'},
     {'author': 'Rose Rocket',
      'channel': 'Rose Rocket',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:29](https://www.youtube.com/watch?v=bYzHDrJqRgg&t=29s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, if you're a freight broker, you know, you're managing carriers, your "
              "partner carrier network, and if you're trucking company, then you're managing "
              'the trucks, the trailers, the drivers, things like that. So, why is it '
              'important to have a TMS?',
      'timestamp': 29,
      'timestamp_label': '[00:00:29]',
      'timestamp_seconds': 29,
      'tip': "So, if you're a freight broker, you know, you're managing carriers, your partner "
             "carrier network, and if you're trucking company, then you're managing the "
             'trucks, the trailers, the drivers, things like that. So, why is it important to '
             'have a TMS?',
      'title': 'What is a TMS (transportation management system)? (Rose Rocket)',
      'url': 'https://www.youtube.com/watch?v=bYzHDrJqRgg&t=29s',
      'video_id': 'bYzHDrJqRgg'},
     {'author': 'Matt Krause',
      'channel': 'Matt Krause',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:49](https://www.youtube.com/watch?v=ZG3bMHTCx1Y&t=529s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You know, are you relying on your core carriers or do you have a proactive '
              'backup system?" And this focuses on their process, not your service. And '
              "here's the secret weapon. I want to emphasize something critical. The words are "
              'only half of the equation.',
      'timestamp': 529,
      'timestamp_label': '[00:08:49]',
      'timestamp_seconds': 529,
      'tip': 'You know, are you relying on your core carriers or do you have a proactive '
             'backup system?" And this focuses on their process, not your service. And here\'s '
             'the secret weapon. I want to emphasize something critical. The words are only '
             'half of the equation.',
      'title': '11 Minutes of Freight Broker Sales Training to Explode Your Sales in 2026 '
               '(Matt Krause)',
      'url': 'https://www.youtube.com/watch?v=ZG3bMHTCx1Y&t=529s',
      'video_id': 'ZG3bMHTCx1Y'},
     {'author': 'Freight Master Resources',
      'channel': 'Freight Master Resources',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=1Fdc8KYk8M0&t=126s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The the broker had set uh their delivery appointment for noon and the driver '
              'arrived i believe it was about 10 30.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': 'The the broker had set uh their delivery appointment for noon and the driver '
             'arrived i believe it was about 10 30.',
      'title': 'Detention and Layover Pay (Freight Master Resources)',
      'url': 'https://www.youtube.com/watch?v=1Fdc8KYk8M0&t=126s',
      'video_id': '1Fdc8KYk8M0'},
     {'author': 'Freight 360',
      'channel': 'Freight 360',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:46](https://www.youtube.com/watch?v=XtDq2J8HLqY&t=166s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "What is that you say it's simple rather than trying to predict every step "
              "between one two three and ten you're going to map out the steps just a few.",
      'timestamp': 166,
      'timestamp_label': '[00:02:46]',
      'timestamp_seconds': 166,
      'tip': "What is that you say it's simple rather than trying to predict every step "
             "between one two three and ten you're going to map out the steps just a few.",
      'title': 'Freight Brokerage Business Planning (Freight 360)',
      'url': 'https://www.youtube.com/watch?v=XtDq2J8HLqY&t=166s',
      'video_id': 'XtDq2J8HLqY'},
     {'author': 'AscendTMS - The Free (and Best) TMS Software',
      'channel': 'AscendTMS - The Free (and Best) TMS Software',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:12](https://www.youtube.com/watch?v=idL8PXMlKjQ&t=1212s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'll have a pool of drivers and equipment I can choose from and if I click the "
              "blue button that's going to assign an outside carrier that I may have set up in "
              'my system.',
      'timestamp': 1212,
      'timestamp_label': '[00:20:12]',
      'timestamp_seconds': 1212,
      'tip': "I'll have a pool of drivers and equipment I can choose from and if I click the "
             "blue button that's going to assign an outside carrier that I may have set up in "
             'my system.',
      'title': 'FULL AscendTMS Operations Training! (AscendTMS - The Free (and Best) TMS '
               'Software)',
      'url': 'https://www.youtube.com/watch?v=idL8PXMlKjQ&t=1212s',
      'video_id': 'idL8PXMlKjQ'},
     {'author': 'Review By Maverick',
      'channel': 'Review By Maverick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:46](https://www.youtube.com/watch?v=i2KiR_LCj-Q&t=646s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'What I have for you thank you very much for your time I really appreciate it '
              "and I'm going to see you in some other video reviews peace and enjoy the of "
              'your day bye.',
      'timestamp': 646,
      'timestamp_label': '[00:10:46]',
      'timestamp_seconds': 646,
      'tip': 'What I have for you thank you very much for your time I really appreciate it and '
             "I'm going to see you in some other video reviews peace and enjoy the of your day "
             'bye.',
      'title': 'Freight Broker Bootcamp Reviews (Dennis Brown) | Can you make money with this? '
               '(Review By Maverick)',
      'url': 'https://www.youtube.com/watch?v=i2KiR_LCj-Q&t=646s',
      'video_id': 'i2KiR_LCj-Q'},
     {'author': 'AscendTMS - The Free (and Best) TMS Software',
      'channel': 'AscendTMS - The Free (and Best) TMS Software',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:52](https://www.youtube.com/watch?v=Eycc6Jod6t4&t=292s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Suggestion is to go ahead and just make sure all that information's already in "
              "the system before you begin okay so we're going to go ahead and click on new "
              'load wizard move this to over here all right and let me just write this load '
              'number down real.',
      'timestamp': 292,
      'timestamp_label': '[00:04:52]',
      'timestamp_seconds': 292,
      'tip': "Suggestion is to go ahead and just make sure all that information's already in "
             "the system before you begin okay so we're going to go ahead and click on new "
             'load wizard move this to over here all right and let me just write this load '
             'number down real.',
      'title': 'FULL AscendTMS Operations Training! (2024) (AscendTMS - The Free (and Best) '
               'TMS Software)',
      'url': 'https://www.youtube.com/watch?v=Eycc6Jod6t4&t=292s',
      'video_id': 'Eycc6Jod6t4'},
     {'author': 'Matt Krause',
      'channel': 'Matt Krause',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:36](https://www.youtube.com/watch?v=EJYdmoWKsmw&t=516s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, a bad broker would say, "Hey, I got a load paying 1,200 bucks. The '
              'multiplier is like, "Hey, I see you\'ve got a truck in Billings, you know, '
              "every Tuesday, and I've got a consistent run that needs a reliable guy.",
      'timestamp': 516,
      'timestamp_label': '[00:08:36]',
      'timestamp_seconds': 516,
      'tip': 'So, a bad broker would say, "Hey, I got a load paying 1,200 bucks. The '
             'multiplier is like, "Hey, I see you\'ve got a truck in Billings, you know, every '
             "Tuesday, and I've got a consistent run that needs a reliable guy.",
      'title': 'How A 24 Year Old Built A $500k/Mo Freight Business In 11 Months (Matt Krause)',
      'url': 'https://www.youtube.com/watch?v=EJYdmoWKsmw&t=516s',
      'video_id': 'EJYdmoWKsmw'},
     {'author': 'FreightBrokers',
      'channel': 'FreightBrokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:28](https://www.youtube.com/watch?v=Huke-ZINzYA&t=748s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Freightbrokerbootcamp.com we have a 60-day 100 money-back guarantee we've "
              "trained over 8 000 students it's got to be close to 9 000 by now I gotta check "
              "the numbers and um and we've been around for over a decade so I hope you guys "
              'enjoyed the training.',
      'timestamp': 748,
      'timestamp_label': '[00:12:28]',
      'timestamp_seconds': 748,
      'tip': "Freightbrokerbootcamp.com we have a 60-day 100 money-back guarantee we've "
             "trained over 8 000 students it's got to be close to 9 000 by now I gotta check "
             "the numbers and um and we've been around for over a decade so I hope you guys "
             'enjoyed the training.',
      'title': 'Freight Broker Training - How to Become A Freight Broker in 7 Simple Steps '
               '[Step by Step] (FreightBrokers)',
      'url': 'https://www.youtube.com/watch?v=Huke-ZINzYA&t=748s',
      'video_id': 'Huke-ZINzYA'}],
 8: [{'author': 'FreightBrokers',
      'channel': 'FreightBrokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:56](https://www.youtube.com/watch?v=yGyxzLrh7yE&t=1016s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, grab the free training and use it as your beginner road map. And if you '
              'want more help, my full freight broker boot camp training goes much more '
              'in-depth on how to start and grow a successful freight broker or freight agent '
              'business.',
      'timestamp': 1016,
      'timestamp_label': '[00:16:56]',
      'timestamp_seconds': 1016,
      'tip': 'So, grab the free training and use it as your beginner road map. And if you want '
             'more help, my full freight broker boot camp training goes much more in-depth on '
             'how to start and grow a successful freight broker or freight agent business.',
      'title': 'How I’d Become a Freight Broker in 2026 If I Started Over Today [You Might Be '
               'Shocked] 😳 (FreightBrokers)',
      'url': 'https://www.youtube.com/watch?v=yGyxzLrh7yE&t=1016s',
      'video_id': 'yGyxzLrh7yE'},
     {'author': 'Matt Krause',
      'channel': 'Matt Krause',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:53](https://www.youtube.com/watch?v=pXxS5GOHXZE&t=233s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Talking about agents today all right now Freight agents they work under the '
              "broker's Authority and use broker's tools tools like let's say their CRM and "
              'their TMS and their load board and rely.',
      'timestamp': 233,
      'timestamp_label': '[00:03:53]',
      'timestamp_seconds': 233,
      'tip': 'Talking about agents today all right now Freight agents they work under the '
             "broker's Authority and use broker's tools tools like let's say their CRM and "
             'their TMS and their load board and rely.',
      'title': 'How to Become a Freight Agent in 2027 (No Experience Needed) (Matt Krause)',
      'url': 'https://www.youtube.com/watch?v=pXxS5GOHXZE&t=233s',
      'video_id': 'pXxS5GOHXZE'},
     {'author': 'Brandon Scott',
      'channel': 'Brandon Scott',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:37](https://www.youtube.com/watch?v=lzC0i5OReRU&t=337s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Time in the business and your credit rating may get better you've paid carriers "
              'for a little while now then you reapply for your surety bond at the end.',
      'timestamp': 337,
      'timestamp_label': '[00:05:37]',
      'timestamp_seconds': 337,
      'tip': "Time in the business and your credit rating may get better you've paid carriers "
             'for a little while now then you reapply for your surety bond at the end.',
      'title': 'What You Need To Know About The Freight Broker Bond... (Brandon Scott)',
      'url': 'https://www.youtube.com/watch?v=lzC0i5OReRU&t=337s',
      'video_id': 'lzC0i5OReRU'},
     {'author': 'Commercial Carrier Journal',
      'channel': 'Commercial Carrier Journal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:03](https://www.youtube.com/watch?v=u2IgQ87ZELQ&t=243s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'As important as technology is as a tool in combating double brokering and '
              "fraud, it's also a tool used by bad actors that's driving growth in these types "
              "of crimes. The most impactful technology that's everywhere right now is is the "
              'advancement of AI.',
      'timestamp': 243,
      'timestamp_label': '[00:04:03]',
      'timestamp_seconds': 243,
      'tip': 'As important as technology is as a tool in combating double brokering and fraud, '
             "it's also a tool used by bad actors that's driving growth in these types of "
             "crimes. The most impactful technology that's everywhere right now is is the "
             'advancement of AI.',
      'title': 'Double brokering & freight fraud: How new laws will protect carriers '
               '(Commercial Carrier Journal)',
      'url': 'https://www.youtube.com/watch?v=u2IgQ87ZELQ&t=243s',
      'video_id': 'u2IgQ87ZELQ'},
     {'author': 'Double Broker Bounty Hunter',
      'channel': 'Double Broker Bounty Hunter',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:22](https://www.youtube.com/watch?v=3dI5z6SHDPc&t=502s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, I don't see this as much in this day and age, but early in double "
              'brokering, the scammers want to make sure that they are communicating '
              'constantly with the real broker and the real carrier to make sure that data is '
              'getting passed through very easily.',
      'timestamp': 502,
      'timestamp_label': '[00:08:22]',
      'timestamp_seconds': 502,
      'tip': "Now, I don't see this as much in this day and age, but early in double "
             'brokering, the scammers want to make sure that they are communicating constantly '
             'with the real broker and the real carrier to make sure that data is getting '
             'passed through very easily.',
      'title': "DBBH's Fraud Prevention Series 2.0 - Part 3 - Warning Signs Double Brokers "
               '(Double Broker Bounty Hunter)',
      'url': 'https://www.youtube.com/watch?v=3dI5z6SHDPc&t=502s',
      'video_id': '3dI5z6SHDPc'},
     {'author': 'FreightCaviar',
      'channel': 'FreightCaviar',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=PyjJOzy-a2s&t=168s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'All of my freight brokering life. And I worked at a company called Circle 8. '
              'Neville, who you mentioned earlier, hired me into this industry in 2011. You '
              'know, I started out tracking and tracing loads all day, every day.',
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': 'All of my freight brokering life. And I worked at a company called Circle 8. '
             'Neville, who you mentioned earlier, hired me into this industry in 2011. You '
             'know, I started out tracking and tracing loads all day, every day.',
      'title': 'How Cold Calls and Customer Service Built a $50M Freight Brokerage '
               '(FreightCaviar)',
      'url': 'https://www.youtube.com/watch?v=PyjJOzy-a2s&t=168s',
      'video_id': 'PyjJOzy-a2s'},
     {'author': 'Cole Fairbrook',
      'channel': 'Cole Fairbrook',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:52](https://www.youtube.com/watch?v=bEWh0t-c_5o&t=1192s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "18 after deadhead, it's not too bad. You might be able to come and go out of "
              'Texas not too bad. 35 is borderline a loss for most flatbed carriers. You You '
              "can't make any money at it. 35 a mile is uh pretty much a loss at this point.",
      'timestamp': 1192,
      'timestamp_label': '[00:19:52]',
      'timestamp_seconds': 1192,
      'tip': "18 after deadhead, it's not too bad. You might be able to come and go out of "
             'Texas not too bad. 35 is borderline a loss for most flatbed carriers. You You '
             "can't make any money at it. 35 a mile is uh pretty much a loss at this point.",
      'title': 'LoadBoard Video September 23 2026 Truck-Stop VS DAT (Cole Fairbrook)',
      'url': 'https://www.youtube.com/watch?v=bEWh0t-c_5o&t=1192s',
      'video_id': 'bEWh0t-c_5o'},
     {'author': 'Freight 360',
      'channel': 'Freight 360',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:25](https://www.youtube.com/watch?v=e9-lormMK4w&t=565s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Double brokerage aside like there's no reason for the carrier now to pick up "
              "the phone so it's very very common and and I understand carriers have other.",
      'timestamp': 565,
      'timestamp_label': '[00:09:25]',
      'timestamp_seconds': 565,
      'tip': "Double brokerage aside like there's no reason for the carrier now to pick up the "
             "phone so it's very very common and and I understand carriers have other.",
      'title': 'Crushing Cold Calls and Freight Agent Commissions | The Final Mile #23 '
               '(Freight 360)',
      'url': 'https://www.youtube.com/watch?v=e9-lormMK4w&t=565s',
      'video_id': 'e9-lormMK4w'},
     {'author': 'ConnectWithKamal',
      'channel': 'ConnectWithKamal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=tjwBtk3RgWI&t=50s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'ਵਿੱਚ ਕੀ ਹੁੰਦਾ ਤੁਸੀਂ ਇੱਕ ਐਨੂਅਲ ਪ੍ਰੀਮੀਅਮ ਪੇ ਕਰਨਾ ਹੁੰਦਾ ਅਗੇਂਸਟ ਦਿਸ 75000 ਯੂਐਸ ਡਾਲਰ '
              'ਇਹ ਪ੍ਰੀਮੀਅਮ ਦਾ ਅਮਾਊਂਟ ਤੁਹਾਡੇ ਕ੍ਰੈਡਿਟ ਸਕੋਰ ਤੇ ਡਿਪੈਂਡ ਕਰਦਾ ਹੁਣ ਓਨ ਐਨ ਐਵਰੇਜ ਜੋ.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': 'ਵਿੱਚ ਕੀ ਹੁੰਦਾ ਤੁਸੀਂ ਇੱਕ ਐਨੂਅਲ ਪ੍ਰੀਮੀਅਮ ਪੇ ਕਰਨਾ ਹੁੰਦਾ ਅਗੇਂਸਟ ਦਿਸ 75000 ਯੂਐਸ ਡਾਲਰ '
             'ਇਹ ਪ੍ਰੀਮੀਅਮ ਦਾ ਅਮਾਊਂਟ ਤੁਹਾਡੇ ਕ੍ਰੈਡਿਟ ਸਕੋਰ ਤੇ ਡਿਪੈਂਡ ਕਰਦਾ ਹੁਣ ਓਨ ਐਨ ਐਵਰੇਜ ਜੋ.',
      'title': 'Freight Broker $75,000 Surety Bond Explained in Punjabi | How to Get It at Low '
               'Cost (ConnectWithKamal)',
      'url': 'https://www.youtube.com/watch?v=tjwBtk3RgWI&t=50s',
      'video_id': 'tjwBtk3RgWI'},
     {'author': 'AscendTMS - The Free (and Best) TMS Software',
      'channel': 'AscendTMS - The Free (and Best) TMS Software',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:25](https://www.youtube.com/watch?v=zALRluYUGLI&t=145s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Choosing Ascend TMS part two you learn how to onboard yourself with the sun TMS '
              "so I'll see you next time and welcome to the send TMS family to schedule "
              'training you can always reach out to us at support emotionglobal.com Ascend TMS '
              'the logistics software for everyone.',
      'timestamp': 145,
      'timestamp_label': '[00:02:25]',
      'timestamp_seconds': 145,
      'tip': 'Choosing Ascend TMS part two you learn how to onboard yourself with the sun TMS '
             "so I'll see you next time and welcome to the send TMS family to schedule "
             'training you can always reach out to us at support emotionglobal.com Ascend TMS '
             'the logistics software for everyone.',
      'title': 'An Exciting Overview Of AscendTMS In Just 3 Minutes! (AscendTMS - The Free '
               '(and Best) TMS Software)',
      'url': 'https://www.youtube.com/watch?v=zALRluYUGLI&t=145s',
      'video_id': 'zALRluYUGLI'},
     {'author': 'Drayage Specialist',
      'channel': 'Drayage Specialist',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:41](https://www.youtube.com/watch?v=sv8u2e9X6Oc&t=41s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Via cargo train in global trade massive ships and long freight trains carry '
              "Goods over vast distances but they can't deliver.",
      'timestamp': 41,
      'timestamp_label': '[00:00:41]',
      'timestamp_seconds': 41,
      'tip': 'Via cargo train in global trade massive ships and long freight trains carry '
             "Goods over vast distances but they can't deliver.",
      'title': 'What Is Drayage? Understanding Its Importance in Shipping and Logistics '
               '(Drayage Specialist)',
      'url': 'https://www.youtube.com/watch?v=sv8u2e9X6Oc&t=41s',
      'video_id': 'sv8u2e9X6Oc'},
     {'author': 'CDL Shorty',
      'channel': 'CDL Shorty',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:00](https://www.youtube.com/watch?v=_uTvz6Ay4oQ&t=420s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "All some people don't want knowledge that's sad that's so sad some truckers "
              "don't want knowledge and that's why we can't never stick.",
      'timestamp': 420,
      'timestamp_label': '[00:07:00]',
      'timestamp_seconds': 420,
      'tip': "All some people don't want knowledge that's sad that's so sad some truckers "
             "don't want knowledge and that's why we can't never stick.",
      'title': '49 CFR 371.3 this is a law that all freight brokers are scared of. Let’s '
               'educate all truckers (CDL Shorty)',
      'url': 'https://www.youtube.com/watch?v=_uTvz6Ay4oQ&t=420s',
      'video_id': '_uTvz6Ay4oQ'},
     {'author': 'Bobby Loads',
      'channel': 'Bobby Loads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:28](https://www.youtube.com/watch?v=MDlMmII7ZrY&t=568s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It could be a a false positive, but I mean, most of these areas are really hot '
              'for the flat beds. So, if you guys are driving a flat bed right now, I mean, we '
              "can sit here all day, search loads, do everything, but I mean, just it's it's "
              'super hot most places.',
      'timestamp': 568,
      'timestamp_label': '[00:09:28]',
      'timestamp_seconds': 568,
      'tip': 'It could be a a false positive, but I mean, most of these areas are really hot '
             'for the flat beds. So, if you guys are driving a flat bed right now, I mean, we '
             "can sit here all day, search loads, do everything, but I mean, just it's it's "
             'super hot most places.',
      'title': '🔥 Which Trucking Lanes Are Paying the Most Right Now? (Bobby Loads)',
      'url': 'https://www.youtube.com/watch?v=MDlMmII7ZrY&t=568s',
      'video_id': 'MDlMmII7ZrY'},
     {'author': 'Freight 360',
      'channel': 'Freight 360',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:53](https://www.youtube.com/watch?v=d6HWIm_kCFk&t=353s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Frustrating it can damage relationships between shippers brokers and carriers '
              "and we need to do everything we can to prevent it thanks for watching and I'll "
              'see you in the next video.',
      'timestamp': 353,
      'timestamp_label': '[00:05:53]',
      'timestamp_seconds': 353,
      'tip': 'Frustrating it can damage relationships between shippers brokers and carriers '
             "and we need to do everything we can to prevent it thanks for watching and I'll "
             'see you in the next video.',
      'title': 'What is Detention Pay for Freight Brokers? (Freight 360)',
      'url': 'https://www.youtube.com/watch?v=d6HWIm_kCFk&t=353s',
      'video_id': 'd6HWIm_kCFk'},
     {'author': 'Victor Mason',
      'channel': 'Victor Mason',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=4n9e0eEuFtM&t=87s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s authority while you focus on the sales and relationships. Now, let's clear "
              'up the confusion between a freight agent and a freight broker. A freight broker '
              'owns the business. They have the MC number, the bond, the insurance, the '
              'compliance, and the back office.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': "'s authority while you focus on the sales and relationships. Now, let's clear up "
             'the confusion between a freight agent and a freight broker. A freight broker '
             'owns the business. They have the MC number, the bond, the insurance, the '
             'compliance, and the back office.',
      'title': 'How to Be a Freight Agent in 2026 (No Truck, No MC, No Guessing) (Victor '
               'Mason)',
      'url': 'https://www.youtube.com/watch?v=4n9e0eEuFtM&t=87s',
      'video_id': '4n9e0eEuFtM'}],
 9: [{'author': 'Trucking Justice - Pontificator',
      'channel': 'Trucking Justice - Pontificator',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=GjctUTtklxE&t=55s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I am unaware of any change in its enforcement stance on this issue and to my '
              'knowledge the rules in effect when the broker carrier agreement was signed '
              'remain unchanged. So you are leaning on the lack of enforcement rather than my '
              'legal rights under this law.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'I am unaware of any change in its enforcement stance on this issue and to my '
             'knowledge the rules in effect when the broker carrier agreement was signed '
             'remain unchanged. So you are leaning on the lack of enforcement rather than my '
             'legal rights under this law.',
      'title': 'Broker Attorney Claims FMCSA Doesn’t Enforce 49 CFR §371.3 (Trucking Justice - '
               'Pontificator)',
      'url': 'https://www.youtube.com/watch?v=GjctUTtklxE&t=55s',
      'video_id': 'GjctUTtklxE'},
     {'author': 'Matt Krause',
      'channel': 'Matt Krause',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=VD-td9ERDAU&t=22s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, the thing is, this video is about owning your brokerage, your own '
              "authority. That's the government license this business runs on, and your own "
              "shippers and your own checking account because that's who asks this question.",
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'So, the thing is, this video is about owning your brokerage, your own authority. '
             "That's the government license this business runs on, and your own shippers and "
             "your own checking account because that's who asks this question.",
      'title': 'How Much Freight Brokers ACTUALLY Make in 2027 (Owner Math) (Matt Krause)',
      'url': 'https://www.youtube.com/watch?v=VD-td9ERDAU&t=22s',
      'video_id': 'VD-td9ERDAU'},
     {'author': 'FreightBrokers',
      'channel': 'FreightBrokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:18](https://www.youtube.com/watch?v=j9lUdJynzFA&t=1878s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t have some capital set aside for your bond, right? Then I think starting as a "
              "freight agent is the best way to go. You don't have to get a bond. You don't "
              "have to get an authority. You don't have to get any certification, okay? You "
              "don't have to set up a big office.",
      'timestamp': 1878,
      'timestamp_label': '[00:31:18]',
      'timestamp_seconds': 1878,
      'tip': "'t have some capital set aside for your bond, right? Then I think starting as a "
             "freight agent is the best way to go. You don't have to get a bond. You don't "
             "have to get an authority. You don't have to get any certification, okay? You "
             "don't have to set up a big office.",
      'title': 'Freight Broker / Agent LIVE Q&A with Dennis Brown 1/19/25 (FreightBrokers)',
      'url': 'https://www.youtube.com/watch?v=j9lUdJynzFA&t=1878s',
      'video_id': 'j9lUdJynzFA'},
     {'author': 'Double Broker Bounty Hunter',
      'channel': 'Double Broker Bounty Hunter',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:12](https://www.youtube.com/watch?v=J96nZa6x_Ek&t=312s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Board who had to sit there and approve you to uh become a motor carrier or a '
              'broker none of that matters anymore now as long as you meet the statutory '
              'requirements to obtain an authority you can get one it really is that simple '
              'next comes Public Law 112-416.',
      'timestamp': 312,
      'timestamp_label': '[00:05:12]',
      'timestamp_seconds': 312,
      'tip': 'Board who had to sit there and approve you to uh become a motor carrier or a '
             'broker none of that matters anymore now as long as you meet the statutory '
             'requirements to obtain an authority you can get one it really is that simple '
             'next comes Public Law 112-416.',
      'title': 'Fraud Prevention   Part 1   Double Brokering Evolution (Double Broker Bounty '
               'Hunter)',
      'url': 'https://www.youtube.com/watch?v=J96nZa6x_Ek&t=312s',
      'video_id': 'J96nZa6x_Ek'},
     {'author': 'Freight 360',
      'channel': 'Freight 360',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:44](https://www.youtube.com/watch?v=_7T74xDXmPk&t=284s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Involved while protecting the business interest for all those parties as well '
              "so maybe it's time to give CFR 371.50 c a little makeover making sure it fits "
              "just right in the modern world of logistics thanks for watching we'll see you "
              'guys in the next video.',
      'timestamp': 284,
      'timestamp_label': '[00:04:44]',
      'timestamp_seconds': 284,
      'tip': 'Involved while protecting the business interest for all those parties as well so '
             "maybe it's time to give CFR 371.50 c a little makeover making sure it fits just "
             "right in the modern world of logistics thanks for watching we'll see you guys in "
             'the next video.',
      'title': "Let's Talk About CFR 371.3c and Why It's Time for a Refresh (Freight 360)",
      'url': 'https://www.youtube.com/watch?v=_7T74xDXmPk&t=284s',
      'video_id': '_7T74xDXmPk'},
     {'author': 'Sales Scripter',
      'channel': 'Sales Scripter',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=6W1ym-1hlkc&t=20s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I don't know if we're a fit or not with what you do and that's why I was "
              "calling with a question or two. And then after you've opened the call, you can "
              'then transition to asking a couple questions. You could either start out with '
              'pain questions or current state questions.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "I don't know if we're a fit or not with what you do and that's why I was calling "
             "with a question or two. And then after you've opened the call, you can then "
             'transition to asking a couple questions. You could either start out with pain '
             'questions or current state questions.',
      'title': 'Cold Call Script for Logistics and Freight Services (Sales Scripter)',
      'url': 'https://www.youtube.com/watch?v=6W1ym-1hlkc&t=20s',
      'video_id': '6W1ym-1hlkc'},
     {'author': 'LOGISTICS RISK EXPERT by Cassandra Gaines',
      'channel': 'LOGISTICS RISK EXPERT by Cassandra Gaines',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:33](https://www.youtube.com/watch?v=Ig6sI3O1a14&t=813s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Everything so if you have no contract in place no terms of bill leadings are '
              'governing my video will apply if you have a contract you need to read through '
              "it and figure out what differs from what I'm saying here in this presentation "
              'until next time.',
      'timestamp': 813,
      'timestamp_label': '[00:13:33]',
      'timestamp_seconds': 813,
      'tip': 'Everything so if you have no contract in place no terms of bill leadings are '
             'governing my video will apply if you have a contract you need to read through it '
             "and figure out what differs from what I'm saying here in this presentation until "
             'next time.',
      'title': 'Cargo Claims Basics! (LOGISTICS RISK EXPERT by Cassandra Gaines)',
      'url': 'https://www.youtube.com/watch?v=Ig6sI3O1a14&t=813s',
      'video_id': 'Ig6sI3O1a14'},
     {'author': 'Anderson Trucking Service',
      'channel': 'Anderson Trucking Service',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=b2-QjzInPJo&t=59s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Words they change day to day why would a business choose contract rates when '
              'you lock into contracted rates with a carrier you experience predictable costs.',
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': 'Words they change day to day why would a business choose contract rates when you '
             'lock into contracted rates with a carrier you experience predictable costs.',
      'title': 'Spot vs Contract Rates [Which Saves You More Money?] (Anderson Trucking '
               'Service)',
      'url': 'https://www.youtube.com/watch?v=b2-QjzInPJo&t=59s',
      'video_id': 'b2-QjzInPJo'},
     {'author': 'StillHawginTV',
      'channel': 'StillHawginTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:37](https://www.youtube.com/watch?v=eEOluDo3mZM&t=277s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Light on a surety bond situation and I hope you know best look to y'all out "
              "there was starting y'all brokerages once again is your boy ghosts love peace "
              "prosperity and I'll catch you on the next one do something.",
      'timestamp': 277,
      'timestamp_label': '[00:04:37]',
      'timestamp_seconds': 277,
      'tip': "Light on a surety bond situation and I hope you know best look to y'all out "
             "there was starting y'all brokerages once again is your boy ghosts love peace "
             "prosperity and I'll catch you on the next one do something.",
      'title': 'Freight Brokering | Top 6 Surety Bond Companies (StillHawginTV)',
      'url': 'https://www.youtube.com/watch?v=eEOluDo3mZM&t=277s',
      'video_id': 'eEOluDo3mZM'},
     {'author': 'Contract Fortune',
      'channel': 'Contract Fortune',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=ocF4fny2uH8&t=15s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '360 or Internet truck stop so for those that may not know a load board is where '
              "you go for a freight broker and a driver as a driver you're gonna go there to.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': '360 or Internet truck stop so for those that may not know a load board is where '
             "you go for a freight broker and a driver as a driver you're gonna go there to.",
      'title': 'Dat board vs. Internet Truckstop (Contract Fortune)',
      'url': 'https://www.youtube.com/watch?v=ocF4fny2uH8&t=15s',
      'video_id': 'ocF4fny2uH8'},
     {'author': 'Dispatching & Intermodal Training',
      'channel': 'Dispatching & Intermodal Training',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:57](https://www.youtube.com/watch?v=SvfUq9Udy60&t=357s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um and this is probably going to make the broker Overlook my quote okay so I'm "
              'just going to give it another uh number going in this area meaning that we just '
              "ran to Grand Prairie Texas for like fourteen hundred and that's so Grand "
              'Prairie.',
      'timestamp': 357,
      'timestamp_label': '[00:05:57]',
      'timestamp_seconds': 357,
      'tip': "Um and this is probably going to make the broker Overlook my quote okay so I'm "
             'just going to give it another uh number going in this area meaning that we just '
             "ran to Grand Prairie Texas for like fourteen hundred and that's so Grand "
             'Prairie.',
      'title': 'Freight Dispatcher | Bidding Intermodal Lane LIVE (Dispatching & Intermodal '
               'Training)',
      'url': 'https://www.youtube.com/watch?v=SvfUq9Udy60&t=357s',
      'video_id': 'SvfUq9Udy60'},
     {'author': 'Cerasis , now part of GlobalTranz',
      'channel': 'Cerasis , now part of GlobalTranz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:28](https://www.youtube.com/watch?v=mJw3vbSaJbw&t=328s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "In fact that blog is award-winning we promise that you're going to get a lot of "
              "information well we hope you enjoyed this week's episode of talking Freight "
              'have a great rest of your week and tune in next time.',
      'timestamp': 328,
      'timestamp_label': '[00:05:28]',
      'timestamp_seconds': 328,
      'tip': "In fact that blog is award-winning we promise that you're going to get a lot of "
             "information well we hope you enjoyed this week's episode of talking Freight have "
             'a great rest of your week and tune in next time.',
      'title': 'Talking Freight (5) - What is the Carmack Amendment? (Cerasis , now part of '
               'GlobalTranz)',
      'url': 'https://www.youtube.com/watch?v=mJw3vbSaJbw&t=328s',
      'video_id': 'mJw3vbSaJbw'},
     {'author': 'Guy in a Truck',
      'channel': 'Guy in a Truck',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:38](https://www.youtube.com/watch?v=6qAGWwbnmxA&t=278s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Like the Speedway but I think something's going on there music or they might "
              "even have a race I don't know but I was going to go to TGI Fridays out on the "
              "beach man it's so warm here and yeah what do you mean BOC.",
      'timestamp': 278,
      'timestamp_label': '[00:04:38]',
      'timestamp_seconds': 278,
      'tip': "Like the Speedway but I think something's going on there music or they might "
             "even have a race I don't know but I was going to go to TGI Fridays out on the "
             "beach man it's so warm here and yeah what do you mean BOC.",
      'title': 'Contract freight all miles 2.25 or wait for spot market rates to get better? '
               '(Guy in a Truck)',
      'url': 'https://www.youtube.com/watch?v=6qAGWwbnmxA&t=278s',
      'video_id': '6qAGWwbnmxA'},
     {'author': 'FreightBrokers',
      'channel': 'FreightBrokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:46](https://www.youtube.com/watch?v=N1uEW-kxNvE&t=226s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'What this does is this is a set of guidelines and rules for motor carriers as '
              'it relates to Ocean and rail providers as well as the.',
      'timestamp': 226,
      'timestamp_label': '[00:03:46]',
      'timestamp_seconds': 226,
      'tip': 'What this does is this is a set of guidelines and rules for motor carriers as it '
             'relates to Ocean and rail providers as well as the.',
      'title': 'What is Drayage? 4 Tips Every Freight Broker Must Know About the Drayage '
               'Freight Niche! (FreightBrokers)',
      'url': 'https://www.youtube.com/watch?v=N1uEW-kxNvE&t=226s',
      'video_id': 'N1uEW-kxNvE'},
     {'author': 'FMCSA REGISTRATION dot com',
      'channel': 'FMCSA REGISTRATION dot com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=fG1DJXPE2jk&t=62s)',
      'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                   'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                   'shipper-to-carrier float management (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This helps to protect the integrity of the industry and ensures that all '
              'parties are treated fairly. Not having a BMC 84 surety bond can result in '
              'fines, suspension or revocation of the broker or forwarders license, and even '
              'legal action.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': 'This helps to protect the integrity of the industry and ensures that all parties '
             'are treated fairly. Not having a BMC 84 surety bond can result in fines, '
             'suspension or revocation of the broker or forwarders license, and even legal '
             'action.',
      'title': 'BMC 84 Surety Bond | Is a Freight Broker Bond Requirement (BMC-84) (FMCSA '
               'REGISTRATION dot com)',
      'url': 'https://www.youtube.com/watch?v=fG1DJXPE2jk&t=62s',
      'video_id': 'fG1DJXPE2jk'}],
 10: [{'author': 'FreightBrokers',
       'channel': 'FreightBrokers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:08](https://www.youtube.com/watch?v=vvPudiQpMrY&t=68s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "'t know me, my name is Dennis Brown. I built a freight brokerage that did over "
               "$200 million in sales, and I've trained over 10,000 people worldwide through "
               'my freight broker boot camp. So, when I talk about whether freight brokerage '
               "is too saturated, I'm not guessing.",
       'timestamp': 68,
       'timestamp_label': '[00:01:08]',
       'timestamp_seconds': 68,
       'tip': "'t know me, my name is Dennis Brown. I built a freight brokerage that did over "
              "$200 million in sales, and I've trained over 10,000 people worldwide through my "
              'freight broker boot camp. So, when I talk about whether freight brokerage is '
              "too saturated, I'm not guessing.",
       'title': 'Is Freight Brokerage Too Saturated? [The REAL Truth] (FreightBrokers)',
       'url': 'https://www.youtube.com/watch?v=vvPudiQpMrY&t=68s',
       'video_id': 'vvPudiQpMrY'},
      {'author': 'Matt Krause',
       'channel': 'Matt Krause',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=AWq6iXM53f8&t=21s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'And that cost me all my leverage. And when the market spiked, I was stuck '
               "eating a huge loss because I hadn't built any real rapport. And most freight "
               "brokers think cold calling is about a killer script, but they're missing 80% "
               'of the game.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'And that cost me all my leverage. And when the market spiked, I was stuck '
              "eating a huge loss because I hadn't built any real rapport. And most freight "
              "brokers think cold calling is about a killer script, but they're missing 80% of "
              'the game.',
       'title': 'How to Make A Cold Call That Blows Up Your Brokerage (Matt Krause)',
       'url': 'https://www.youtube.com/watch?v=AWq6iXM53f8&t=21s',
       'video_id': 'AWq6iXM53f8'},
      {'author': 'Highway',
       'channel': 'Highway',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:25](https://www.youtube.com/watch?v=b-vDBH9GpuA&t=145s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'See our initial carrier shares phone numbers contacts email addresses even a '
               'physical address with other carriers one of these carriers is in fact the same '
               'carrier that we found to have a broker Authority and even shared a vehicle in '
               'the previous insights.',
       'timestamp': 145,
       'timestamp_label': '[00:02:25]',
       'timestamp_seconds': 145,
       'tip': 'See our initial carrier shares phone numbers contacts email addresses even a '
              'physical address with other carriers one of these carriers is in fact the same '
              'carrier that we found to have a broker Authority and even shared a vehicle in '
              'the previous insights.',
       'title': 'Detecting Double Brokering with Highway (Highway)',
       'url': 'https://www.youtube.com/watch?v=b-vDBH9GpuA&t=145s',
       'video_id': 'b-vDBH9GpuA'},
      {'author': 'FMCSA REGISTRATION dot com',
       'channel': 'FMCSA REGISTRATION dot com',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:11](https://www.youtube.com/watch?v=ZW6Aqdzv4uA&t=131s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': '84 and BMC 85 consider your financial standing and business strategy if you '
               'have sufficient capital and prefer direct control over your funds The BMC.',
       'timestamp': 131,
       'timestamp_label': '[00:02:11]',
       'timestamp_seconds': 131,
       'tip': '84 and BMC 85 consider your financial standing and business strategy if you '
              'have sufficient capital and prefer direct control over your funds The BMC.',
       'title': 'BMC-85 Trust Fund EXPLAINED: What Every Freight Broker Needs to Know (FMCSA '
                'REGISTRATION dot com)',
       'url': 'https://www.youtube.com/watch?v=ZW6Aqdzv4uA&t=131s',
       'video_id': 'ZW6Aqdzv4uA'},
      {'author': 'Keep Loadings',
       'channel': 'Keep Loadings',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:31](https://www.youtube.com/watch?v=FbcZES6peVA&t=91s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Double brokering was running rampant. You'd have a shady actor take a load "
               'from a real broker, turn around and re-broker it to you for cheaper, and then '
               "vanish with the shipper's payout, leaving you holding the bag with zero pay.",
       'timestamp': 91,
       'timestamp_label': '[00:01:31]',
       'timestamp_seconds': 91,
       'tip': "Double brokering was running rampant. You'd have a shady actor take a load from "
              'a real broker, turn around and re-broker it to you for cheaper, and then vanish '
              "with the shipper's payout, leaving you holding the bag with zero pay.",
       'title': 'How Highway is Fighting Double Brokerage & Cargo Theft in Trucking (2026 '
                'Update) (Keep Loadings)',
       'url': 'https://www.youtube.com/watch?v=FbcZES6peVA&t=91s',
       'video_id': 'FbcZES6peVA'},
      {'author': 'Bridge Logistics',
       'channel': 'Bridge Logistics',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:44](https://www.youtube.com/watch?v=uT4ymtB7YcA&t=44s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Meet certain operating Authority standards and is involved in an accident now '
               'while the word double commonly means two in the world of double brokering it.',
       'timestamp': 44,
       'timestamp_label': '[00:00:44]',
       'timestamp_seconds': 44,
       'tip': 'Meet certain operating Authority standards and is involved in an accident now '
              'while the word double commonly means two in the world of double brokering it.',
       'title': 'Identifying Double Brokering! (Fraudulent Activities Awareness for Brokers, '
                'Carriers & Shippers) (Bridge Logistics)',
       'url': 'https://www.youtube.com/watch?v=uT4ymtB7YcA&t=44s',
       'video_id': 'uT4ymtB7YcA'},
      {'author': 'Freight 360',
       'channel': 'Freight 360',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:46](https://www.youtube.com/watch?v=ImGEvDRAqaw&t=526s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Another reminder above that mirror that reminds you who to ask for the '
               'business for more on this topic check out our course freight broker basics and '
               'our group coaching program and remember whether you believe you can or believe '
               "you can't you're right.",
       'timestamp': 526,
       'timestamp_label': '[00:08:46]',
       'timestamp_seconds': 526,
       'tip': 'Another reminder above that mirror that reminds you who to ask for the business '
              'for more on this topic check out our course freight broker basics and our group '
              "coaching program and remember whether you believe you can or believe you can't "
              "you're right.",
       'title': 'Freight broker cold calling script. Everything you need to know! (Freight '
                '360)',
       'url': 'https://www.youtube.com/watch?v=ImGEvDRAqaw&t=526s',
       'video_id': 'ImGEvDRAqaw'},
      {'author': 'Brandon Scott',
       'channel': 'Brandon Scott',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:54](https://www.youtube.com/watch?v=xPxwiwivMXE&t=414s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Freight broker I'll leave a free video right here so until the next time I "
               'wish you the very best in your life in business see you at the top because the '
               'bottom is much too crowded.',
       'timestamp': 414,
       'timestamp_label': '[00:06:54]',
       'timestamp_seconds': 414,
       'tip': "Freight broker I'll leave a free video right here so until the next time I wish "
              'you the very best in your life in business see you at the top because the '
              'bottom is much too crowded.',
       'title': 'REEFER Freight: What Newbie Freight Brokers Need To Know (Brandon Scott)',
       'url': 'https://www.youtube.com/watch?v=xPxwiwivMXE&t=414s',
       'video_id': 'xPxwiwivMXE'},
      {'author': 'Victor Mason',
       'channel': 'Victor Mason',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:05:01](https://www.youtube.com/watch?v=o2G4zRoNHt4&t=3901s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "We're actually assisting a lot of our customers with reducing their demurge "
               'and and really assisting with things cold storage um on a large scale because '
               'we specialize in in um in importing seafood.',
       'timestamp': 3901,
       'timestamp_label': '[01:05:01]',
       'timestamp_seconds': 3901,
       'tip': "We're actually assisting a lot of our customers with reducing their demurge and "
              'and really assisting with things cold storage um on a large scale because we '
              'specialize in in um in importing seafood.',
       'title': 'Mastering Drayage: A Step by Step Guide for Beginning Freight Brokers (Victor '
                'Mason)',
       'url': 'https://www.youtube.com/watch?v=o2G4zRoNHt4&t=3901s',
       'video_id': 'o2G4zRoNHt4'},
      {'author': 'Chief Carriers',
       'channel': 'Chief Carriers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:40](https://www.youtube.com/watch?v=7kg1eMOTev8&t=40s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "And if you're like any other driver I know, you're always trying to figure out "
               "a way to make more money in this business. That's been really hard here over "
               'the last couple years with everything has been so flat.',
       'timestamp': 40,
       'timestamp_label': '[00:00:40]',
       'timestamp_seconds': 40,
       'tip': "And if you're like any other driver I know, you're always trying to figure out "
              "a way to make more money in this business. That's been really hard here over "
              'the last couple years with everything has been so flat.',
       'title': 'Unlocking Higher Pay in Oversized Freight (Chief Carriers)',
       'url': 'https://www.youtube.com/watch?v=7kg1eMOTev8&t=40s',
       'video_id': '7kg1eMOTev8'},
      {'author': 'FreightBrokers',
       'channel': 'FreightBrokers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:50:49](https://www.youtube.com/watch?v=kc6-g1EZ0Fk&t=3049s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'A reminder in your phone right in your iPhone or Android that every Monday at '
               'noon I do these live trainings free set a reminder and then join me live and '
               "I'll see you next Monday with the next freight broker boot camp live.",
       'timestamp': 3049,
       'timestamp_label': '[00:50:49]',
       'timestamp_seconds': 3049,
       'tip': 'A reminder in your phone right in your iPhone or Android that every Monday at '
              'noon I do these live trainings free set a reminder and then join me live and '
              "I'll see you next Monday with the next freight broker boot camp live.",
       'title': "You're Just 1 Shipper Away! [LIVE Freight Broker Training] (FreightBrokers)",
       'url': 'https://www.youtube.com/watch?v=kc6-g1EZ0Fk&t=3049s',
       'video_id': 'kc6-g1EZ0Fk'},
      {'author': 'Bobby Loads',
       'channel': 'Bobby Loads',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:41](https://www.youtube.com/watch?v=fwtKyVFD-8o&t=41s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'You are going to be making $4 plus average per mile. Personally, I did have a '
               'little bit slower week with the flatbeds. I think it was just a bad luck week '
               'cuz the drivers were late, other circumstances that led to me not being able '
               'to get my full potential out of the week.',
       'timestamp': 41,
       'timestamp_label': '[00:00:41]',
       'timestamp_seconds': 41,
       'tip': 'You are going to be making $4 plus average per mile. Personally, I did have a '
              'little bit slower week with the flatbeds. I think it was just a bad luck week '
              'cuz the drivers were late, other circumstances that led to me not being able to '
              'get my full potential out of the week.',
       'title': 'These Lanes Are On Fire Right Now | Trucking Market (Bobby Loads)',
       'url': 'https://www.youtube.com/watch?v=fwtKyVFD-8o&t=41s',
       'video_id': 'fwtKyVFD-8o'},
      {'author': 'Matt Krause',
       'channel': 'Matt Krause',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:26](https://www.youtube.com/watch?v=Bdydc4rCcVs&t=506s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, leading to more consultant work for you and a more stable business. When '
               'you consistently deliver this level of proactive communication, shippers will '
               'stop seeing you as just a broker and start seeing you as their broker.',
       'timestamp': 506,
       'timestamp_label': '[00:08:26]',
       'timestamp_seconds': 506,
       'tip': 'So, leading to more consultant work for you and a more stable business. When '
              'you consistently deliver this level of proactive communication, shippers will '
              'stop seeing you as just a broker and start seeing you as their broker.',
       'title': "Copy This Sales Script, It'll Blow Up Your Freight Brokerage (Matt Krause)",
       'url': 'https://www.youtube.com/watch?v=Bdydc4rCcVs&t=506s',
       'video_id': 'Bdydc4rCcVs'},
      {'author': 'Freight 360',
       'channel': 'Freight 360',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=7sfi19fbIzU&t=15s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Break down one of the most commonly disputed charges in brokerage and '
               'transportation the truck order not used or tonu.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Break down one of the most commonly disputed charges in brokerage and '
              'transportation the truck order not used or tonu.',
       'title': '**TONU** Explained for Freight Brokers 🚛 (Freight 360)',
       'url': 'https://www.youtube.com/watch?v=7sfi19fbIzU&t=15s',
       'video_id': '7sfi19fbIzU'},
      {'author': 'A3E ECOSYSTEM',
       'channel': 'A3E ECOSYSTEM',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:42](https://www.youtube.com/watch?v=b64rVWfkAsc&t=282s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'BMC 91, BMC 91X, and BMC 82 are the buy and PD evidence. BMC 34 and BMC83 are '
               'the cargo liability evidence. HHG carriers are the ones who file cargo '
               'insurance evidence. Self- insurance rests on a satisfactory safety rating. The '
               'form is not the whole file.',
       'timestamp': 282,
       'timestamp_label': '[00:04:42]',
       'timestamp_seconds': 282,
       'tip': 'BMC 91, BMC 91X, and BMC 82 are the buy and PD evidence. BMC 34 and BMC83 are '
              'the cargo liability evidence. HHG carriers are the ones who file cargo '
              'insurance evidence. Self- insurance rests on a satisfactory safety rating. The '
              'form is not the whole file.',
       'title': '49 CFR 371: Broker Authority Insurance Minimums (A3E ECOSYSTEM)',
       'url': 'https://www.youtube.com/watch?v=b64rVWfkAsc&t=282s',
       'video_id': 'b64rVWfkAsc'}],
 11: [{'author': 'FreightBrokers',
       'channel': 'FreightBrokers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:10](https://www.youtube.com/watch?v=9Yk3-F4z_xs&t=130s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'All right, so number five is a freight brokerage business is highly scalable. '
               'You can scale the business with freight agents or virtual assistants or even a '
               "small inside team. Growth doesn't require a large capital expenditure like "
               'many other businesses.',
       'timestamp': 130,
       'timestamp_label': '[00:02:10]',
       'timestamp_seconds': 130,
       'tip': 'All right, so number five is a freight brokerage business is highly scalable. '
              'You can scale the business with freight agents or virtual assistants or even a '
              "small inside team. Growth doesn't require a large capital expenditure like many "
              'other businesses.',
       'title': 'Why Start A Freight Broker Business vs Other Business Models 🔥💰 '
                '(FreightBrokers)',
       'url': 'https://www.youtube.com/watch?v=9Yk3-F4z_xs&t=130s',
       'video_id': '9Yk3-F4z_xs'},
      {'author': 'Freight 360',
       'channel': 'Freight 360',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:32](https://www.youtube.com/watch?v=uGu6NcZkt28&t=32s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Training check out the freight broker Basics course using the link below it's "
               'a self-paced program taught by us that covers everything including how to '
               'start your own brokerage land new customers grow the business and even hire '
               'the right.',
       'timestamp': 32,
       'timestamp_label': '[00:00:32]',
       'timestamp_seconds': 32,
       'tip': "Training check out the freight broker Basics course using the link below it's a "
              'self-paced program taught by us that covers everything including how to start '
              'your own brokerage land new customers grow the business and even hire the '
              'right.',
       'title': 'Secure Your Freight: Strategies to Prevent Double Brokering Scams (Freight '
                '360)',
       'url': 'https://www.youtube.com/watch?v=uGu6NcZkt28&t=32s',
       'video_id': 'uGu6NcZkt28'},
      {'author': 'Overdrive',
       'channel': 'Overdrive',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:41:27](https://www.youtube.com/watch?v=jnoJihiGSEA&t=2487s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'The location was that it was the business address for the first broker '
               "Authority he'd identified that had double brokered one of his loads.",
       'timestamp': 2487,
       'timestamp_label': '[00:41:27]',
       'timestamp_seconds': 2487,
       'tip': 'The location was that it was the business address for the first broker '
              "Authority he'd identified that had double brokered one of his loads.",
       'title': 'Fighting double-brokering fraud: Attorney Hank Seaton on prevention, ways to '
                'elevate the issue (Overdrive)',
       'url': 'https://www.youtube.com/watch?v=jnoJihiGSEA&t=2487s',
       'video_id': 'jnoJihiGSEA'},
      {'author': 'FreightWaves',
       'channel': 'FreightWaves',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:45](https://www.youtube.com/watch?v=OHagUq3qWcQ&t=705s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'You want to move fast, you need to have people that you trust. And so, being '
               'able to give people different areas of the business to to manage and handle um '
               'allows us to scale more effectively. So, still a small but mighty team.',
       'timestamp': 705,
       'timestamp_label': '[00:11:45]',
       'timestamp_seconds': 705,
       'tip': 'You want to move fast, you need to have people that you trust. And so, being '
              'able to give people different areas of the business to to manage and handle um '
              'allows us to scale more effectively. So, still a small but mighty team.',
       'title': 'Cradle to Grave: Grit, Growth & the Realities of Freight Brokerage | WHAT THE '
                'TRUCK?!? (FreightWaves)',
       'url': 'https://www.youtube.com/watch?v=OHagUq3qWcQ&t=705s',
       'video_id': 'OHagUq3qWcQ'},
      {'author': 'Freightskills',
       'channel': 'Freightskills',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:07](https://www.youtube.com/watch?v=UfDvLSjdYbE&t=427s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Let you in the group so that we can talk about rates shippers carriers and all '
               'that great stuff that comes with Freight brokering every single day all right '
               "until the next video I'll see you soon.",
       'timestamp': 427,
       'timestamp_label': '[00:07:07]',
       'timestamp_seconds': 427,
       'tip': 'Let you in the group so that we can talk about rates shippers carriers and all '
              'that great stuff that comes with Freight brokering every single day all right '
              "until the next video I'll see you soon.",
       'title': 'Everything You Need To Know about the BMC-84 Surety Bond (Freightskills)',
       'url': 'https://www.youtube.com/watch?v=UfDvLSjdYbE&t=427s',
       'video_id': 'UfDvLSjdYbE'},
      {'author': 'Matt Krause',
       'channel': 'Matt Krause',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:29](https://www.youtube.com/watch?v=wxTvTywQET4&t=389s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'But, with your own business, you have the ability to scale. So, you can find '
               'your own tools and your own methodologies to build a business more than your '
               'own, you know, like a salary paid job. Uh and you can also hire people.',
       'timestamp': 389,
       'timestamp_label': '[00:06:29]',
       'timestamp_seconds': 389,
       'tip': 'But, with your own business, you have the ability to scale. So, you can find '
              'your own tools and your own methodologies to build a business more than your '
              'own, you know, like a salary paid job. Uh and you can also hire people.',
       'title': 'Do you have what it takes to build a freight brokerage? (Matt Krause)',
       'url': 'https://www.youtube.com/watch?v=wxTvTywQET4&t=389s',
       'video_id': 'wxTvTywQET4'},
      {'author': 'AFT Dispatch',
       'channel': 'AFT Dispatch',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:04](https://www.youtube.com/watch?v=a4BwE6nAs9k&t=184s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "With this with this broker you're waiving your rights so you know in a "
               "nutshell that's what that means and ultimately motor carriers have the right.",
       'timestamp': 184,
       'timestamp_label': '[00:03:04]',
       'timestamp_seconds': 184,
       'tip': "With this with this broker you're waiving your rights so you know in a nutshell "
              "that's what that means and ultimately motor carriers have the right.",
       'title': 'Broker Transparency - Opening up Broker Transaction Records to American '
                'Trucking Companies (AFT Dispatch)',
       'url': 'https://www.youtube.com/watch?v=a4BwE6nAs9k&t=184s',
       'video_id': 'a4BwE6nAs9k'},
      {'author': 'Rose Rocket',
       'channel': 'Rose Rocket',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:39](https://www.youtube.com/watch?v=QYAwiBYhoVk&t=39s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Order history documents conversations and more so your team is always on the '
               'same page since all the information is in one system you can generate '
               'real-time reports to help you make decisions that improve the profitability of '
               'your business.',
       'timestamp': 39,
       'timestamp_label': '[00:00:39]',
       'timestamp_seconds': 39,
       'tip': 'Order history documents conversations and more so your team is always on the '
              'same page since all the information is in one system you can generate real-time '
              'reports to help you make decisions that improve the profitability of your '
              'business.',
       'title': 'What is Rose Rocket? - Transportation Management System (Rose Rocket)',
       'url': 'https://www.youtube.com/watch?v=QYAwiBYhoVk&t=39s',
       'video_id': 'QYAwiBYhoVk'},
      {'author': 'Brandon Manney The Mentor',
       'channel': 'Brandon Manney The Mentor',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:23](https://www.youtube.com/watch?v=i6KVZJUOBqs&t=203s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Manish Transcom and I could go a little bit more in-depth and help you guys '
               'out when it comes to how can you get paid out there if you are looking for any '
               'type of training freight broker dispatching or whatever it is mentorship go '
               'visit my website.',
       'timestamp': 203,
       'timestamp_label': '[00:03:23]',
       'timestamp_seconds': 203,
       'tip': 'Manish Transcom and I could go a little bit more in-depth and help you guys out '
              'when it comes to how can you get paid out there if you are looking for any type '
              'of training freight broker dispatching or whatever it is mentorship go visit my '
              'website.',
       'title': 'TRUCKING BUSINESS: HOW TO GET PAID? FACTORING SERVICE, COD, QUICK PAY & '
                'INVOICING THE BROKER!!! (Brandon Manney The Mentor)',
       'url': 'https://www.youtube.com/watch?v=i6KVZJUOBqs&t=203s',
       'video_id': 'i6KVZJUOBqs'},
      {'author': 'AscendTMS - The Free (and Best) TMS Software',
       'channel': 'AscendTMS - The Free (and Best) TMS Software',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:54](https://www.youtube.com/watch?v=Q6QrQJDEvDc&t=174s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'The last step is to make sure you keep your premium features running and put '
               'that credit card in and upgrade if you have any additional questions feel free '
               'to reach out to one of our amazing support team members at support '
               'emotionglobal.com.',
       'timestamp': 174,
       'timestamp_label': '[00:02:54]',
       'timestamp_seconds': 174,
       'tip': 'The last step is to make sure you keep your premium features running and put '
              'that credit card in and upgrade if you have any additional questions feel free '
              'to reach out to one of our amazing support team members at support '
              'emotionglobal.com.',
       'title': 'How To Onboard Yourself With AscendTMS! (AscendTMS - The Free (and Best) TMS '
                'Software)',
       'url': 'https://www.youtube.com/watch?v=Q6QrQJDEvDc&t=174s',
       'video_id': 'Q6QrQJDEvDc'},
      {'author': 'Never Stop Trucking',
       'channel': 'Never Stop Trucking',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:50](https://www.youtube.com/watch?v=izh0UL8y-_4&t=50s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'It can be 20 months it can be 150 miles to pick up that load and then the '
               'broker will pay you 150 maybe 250 dollars but 150 is like a standard rate and '
               "that's what they're gonna pay you and then that's the t or anu and then "
               'usually in most of the cases.',
       'timestamp': 50,
       'timestamp_label': '[00:00:50]',
       'timestamp_seconds': 50,
       'tip': 'It can be 20 months it can be 150 miles to pick up that load and then the '
              'broker will pay you 150 maybe 250 dollars but 150 is like a standard rate and '
              "that's what they're gonna pay you and then that's the t or anu and then usually "
              'in most of the cases.',
       'title': 'What are TONU, Detention and Layover? Trucking Phrases Explained (Never Stop '
                'Trucking)',
       'url': 'https://www.youtube.com/watch?v=izh0UL8y-_4&t=50s',
       'video_id': 'izh0UL8y-_4'},
      {'author': 'Bobby Loads',
       'channel': 'Bobby Loads',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:26](https://www.youtube.com/watch?v=s-t9YGcOJ8U&t=146s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Load Hunter make the load boards run a whole lot smoother, you can also link '
               "your factoring company, so you see the broker's credit score right there on a "
               "load posting, so you don't got to switch tabs to go check their credit with "
               'your factoring company.',
       'timestamp': 146,
       'timestamp_label': '[00:02:26]',
       'timestamp_seconds': 146,
       'tip': 'Load Hunter make the load boards run a whole lot smoother, you can also link '
              "your factoring company, so you see the broker's credit score right there on a "
              "load posting, so you don't got to switch tabs to go check their credit with "
              'your factoring company.',
       'title': 'DAT vs Truckstop The Real Difference Nobody Talks About (Bobby Loads)',
       'url': 'https://www.youtube.com/watch?v=s-t9YGcOJ8U&t=146s',
       'video_id': 's-t9YGcOJ8U'},
      {'author': 'Trucking From Scratch',
       'channel': 'Trucking From Scratch',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:07](https://www.youtube.com/watch?v=K9UPJJr_uzQ&t=247s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Actually has you know the factory company that I use so if you need a '
               'factoring company also if you know anybody else who can benefit from this '
               'information please share this video with them thanks again for watching.',
       'timestamp': 247,
       'timestamp_label': '[00:04:07]',
       'timestamp_seconds': 247,
       'tip': 'Actually has you know the factory company that I use so if you need a factoring '
              'company also if you know anybody else who can benefit from this information '
              'please share this video with them thanks again for watching.',
       'title': 'Trucking: What’s the Difference Between QuickPay & Factoring (Trucking From '
                'Scratch)',
       'url': 'https://www.youtube.com/watch?v=K9UPJJr_uzQ&t=247s',
       'video_id': 'K9UPJJr_uzQ'},
      {'author': 'FreightBrokers',
       'channel': 'FreightBrokers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:45](https://www.youtube.com/watch?v=57bmm_ipBSY&t=45s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Work on the hard stuff before you can get what's known as the good stuff right "
               "so I'm going to tell you a quick story I started my Brokerage in two th late "
               'in.',
       'timestamp': 45,
       'timestamp_label': '[00:00:45]',
       'timestamp_seconds': 45,
       'tip': "Work on the hard stuff before you can get what's known as the good stuff right "
              "so I'm going to tell you a quick story I started my Brokerage in two th late "
              'in.',
       'title': 'How to Get Your First Shipper as a NEW Freight Broker or Freight Agent '
                '(FreightBrokers)',
       'url': 'https://www.youtube.com/watch?v=57bmm_ipBSY&t=45s',
       'video_id': '57bmm_ipBSY'},
      {'author': 'Victor Mason',
       'channel': 'Victor Mason',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:07](https://www.youtube.com/watch?v=8AGIyPDUcqY&t=247s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "And the brokers who scale don't rely on luck, they build pipelines. Freight "
               'brokerage is a sales business first, operations come after. And if you can '
               "consistently get customers, you can build a real business. If you can't, "
               'nothing else matters.',
       'timestamp': 247,
       'timestamp_label': '[00:04:07]',
       'timestamp_seconds': 247,
       'tip': "And the brokers who scale don't rely on luck, they build pipelines. Freight "
              'brokerage is a sales business first, operations come after. And if you can '
              "consistently get customers, you can build a real business. If you can't, "
              'nothing else matters.',
       'title': 'The Real Way Freight Brokers Land Shippers (Not What You Think) (Victor '
                'Mason)',
       'url': 'https://www.youtube.com/watch?v=8AGIyPDUcqY&t=247s',
       'video_id': '8AGIyPDUcqY'}],
 12: [{'author': 'ShipLeague',
       'channel': 'ShipLeague',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:52](https://www.youtube.com/watch?v=bOzO119lSlI&t=52s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Even if they have a factoring company, it's still 30 days. And so if we just "
               "look at some numbers, I got some numbers right here. Let's assume that a small "
               'brokerage, very small, does 50 loads a day and the average load is only '
               "$1,500. It's a bad market right now.",
       'timestamp': 52,
       'timestamp_label': '[00:00:52]',
       'timestamp_seconds': 52,
       'tip': "Even if they have a factoring company, it's still 30 days. And so if we just "
              "look at some numbers, I got some numbers right here. Let's assume that a small "
              'brokerage, very small, does 50 loads a day and the average load is only $1,500. '
              "It's a bad market right now.",
       'title': 'Carriers Lose! FMCSA Broker Bond change (ShipLeague)',
       'url': 'https://www.youtube.com/watch?v=bOzO119lSlI&t=52s',
       'video_id': 'bOzO119lSlI'},
      {'author': 'Truckadium',
       'channel': 'Truckadium',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:15](https://www.youtube.com/watch?v=1YErjMy4aFQ&t=135s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'BMC84 filing, and financial institutions, which is the BMC85 filing, must '
               'notify FMCSA when the required minimum is breached and not timely restored. '
               "This is where Tracadium steps in. If you're ready to launch your freight "
               'broker business, you need that $75,000 shorty bond.',
       'timestamp': 135,
       'timestamp_label': '[00:02:15]',
       'timestamp_seconds': 135,
       'tip': 'BMC84 filing, and financial institutions, which is the BMC85 filing, must '
              'notify FMCSA when the required minimum is breached and not timely restored. '
              "This is where Tracadium steps in. If you're ready to launch your freight broker "
              'business, you need that $75,000 shorty bond.',
       'title': '$75,000 Surety Bond Explained | BMC-84 vs BMC-85 for Freight Brokers (FMCSA '
                'Rules 2026) (Truckadium)',
       'url': 'https://www.youtube.com/watch?v=1YErjMy4aFQ&t=135s',
       'video_id': '1YErjMy4aFQ'},
      {'author': 'Matt Krause',
       'channel': 'Matt Krause',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:35:00](https://www.youtube.com/watch?v=r0gf3CDabxw&t=2100s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "So, let's say Cody does 40 touches a day, five days a week. And I'm using "
               'round numbers the whole way through here. Yours will be different, whatever '
               "yours are. That's 200 a week, 800 a month. So, about 25 people a month said, "
               '"Hey, sure.',
       'timestamp': 2100,
       'timestamp_label': '[00:35:00]',
       'timestamp_seconds': 2100,
       'tip': "So, let's say Cody does 40 touches a day, five days a week. And I'm using round "
              'numbers the whole way through here. Yours will be different, whatever yours '
              'are. That\'s 200 a week, 800 a month. So, about 25 people a month said, "Hey, '
              'sure.',
       'title': 'The Freight Broker Cold Calling Script That Books Freight (Matt Krause)',
       'url': 'https://www.youtube.com/watch?v=r0gf3CDabxw&t=2100s',
       'video_id': 'r0gf3CDabxw'},
      {'author': "Tony's Topics",
       'channel': "Tony's Topics",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:11](https://www.youtube.com/watch?v=wOpAqd5AALo&t=191s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Listen guys, there's not much difference between 45 and 135, okay? Uh this is "
               'an investment in your business. These days you have to have something in your '
               'pocket that most other carriers are not using, all right? So, if you would '
               'like a free 30-day trial, you go to try dat.',
       'timestamp': 191,
       'timestamp_label': '[00:03:11]',
       'timestamp_seconds': 191,
       'tip': "Listen guys, there's not much difference between 45 and 135, okay? Uh this is "
              'an investment in your business. These days you have to have something in your '
              'pocket that most other carriers are not using, all right? So, if you would like '
              'a free 30-day trial, you go to try dat.',
       'title': 'Mastering Trucking Lane Rates | DAT Load Board Tutorial for Maximum Profit '
                "(Tony's Topics)",
       'url': 'https://www.youtube.com/watch?v=wOpAqd5AALo&t=191s',
       'video_id': 'wOpAqd5AALo'},
      {'author': 'Freight Broker 911',
       'channel': 'Freight Broker 911',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:40](https://www.youtube.com/watch?v=edDHTJiH5HM&t=40s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Your first 30 days of freight pricing AI are completely free, $0. And you can '
               'potentially keep the platform at $0 per month by maintaining an active shipper '
               'customer and processing at least one freight shipment during each applicable '
               '30-day period.',
       'timestamp': 40,
       'timestamp_label': '[00:00:40]',
       'timestamp_seconds': 40,
       'tip': 'Your first 30 days of freight pricing AI are completely free, $0. And you can '
              'potentially keep the platform at $0 per month by maintaining an active shipper '
              'customer and processing at least one freight shipment during each applicable '
              '30-day period.',
       'title': 'Freight Pricing AI - Earn While You Learn & Build Your Freight Brokerage '
                'Business (Freight Broker 911)',
       'url': 'https://www.youtube.com/watch?v=edDHTJiH5HM&t=40s',
       'video_id': 'edDHTJiH5HM'},
      {'author': 'Bobby Loads',
       'channel': 'Bobby Loads',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:04](https://www.youtube.com/watch?v=fzBhki-xaDc&t=784s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "And I didn't have anything in the book cuz the guys are either on the road, "
               'they messed up, or something happened, you know what I mean? And just a bad '
               "day today for me. But, next week, I'll try to be a little bit more "
               'enthusiastic for you guys.',
       'timestamp': 784,
       'timestamp_label': '[00:13:04]',
       'timestamp_seconds': 784,
       'tip': "And I didn't have anything in the book cuz the guys are either on the road, "
              'they messed up, or something happened, you know what I mean? And just a bad day '
              "today for me. But, next week, I'll try to be a little bit more enthusiastic for "
              'you guys.',
       'title': 'Trucking Market Update: Best Lanes to Run in 2026 (Bobby Loads)',
       'url': 'https://www.youtube.com/watch?v=fzBhki-xaDc&t=784s',
       'video_id': 'fzBhki-xaDc'},
      {'author': 'Trucking Made Successful',
       'channel': 'Trucking Made Successful',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:10](https://www.youtube.com/watch?v=l6yFrAoUZ2M&t=130s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'This is the national average. 6 cents since last week, up 9. 4 cents since '
               "last month, and up $2. So, diesel still leaves much to be desired. Now, let's "
               "take a look at the summaries and we're going to start with those flatbeds.",
       'timestamp': 130,
       'timestamp_label': '[00:02:10]',
       'timestamp_seconds': 130,
       'tip': 'This is the national average. 6 cents since last week, up 9. 4 cents since last '
              "month, and up $2. So, diesel still leaves much to be desired. Now, let's take a "
              "look at the summaries and we're going to start with those flatbeds.",
       'title': "Trucking Market Update: What's Happening On The Spot Market? (Trucking Made "
                'Successful)',
       'url': 'https://www.youtube.com/watch?v=l6yFrAoUZ2M&t=130s',
       'video_id': 'l6yFrAoUZ2M'},
      {'author': 'FreightBrokers',
       'channel': 'FreightBrokers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:03](https://www.youtube.com/watch?v=-_16MS3HWhA&t=603s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Sold out but you will get notified when new spots open up and I hope this '
               'works for you I hope you guys test this out hit me up in the comments with any '
               "questions you guys have and again thank you for joining me for this week's "
               'Freight Burger boot camp l.',
       'timestamp': 603,
       'timestamp_label': '[00:10:03]',
       'timestamp_seconds': 603,
       'tip': 'Sold out but you will get notified when new spots open up and I hope this works '
              'for you I hope you guys test this out hit me up in the comments with any '
              "questions you guys have and again thank you for joining me for this week's "
              'Freight Burger boot camp l.',
       'title': 'Freight Broker Cold Calling Script that Gets Your Prospects Attention! [Free '
                'Download] (FreightBrokers)',
       'url': 'https://www.youtube.com/watch?v=-_16MS3HWhA&t=603s',
       'video_id': '-_16MS3HWhA'},
      {'author': 'Matt Krause',
       'channel': 'Matt Krause',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:34](https://www.youtube.com/watch?v=yeFtuLvEdO8&t=814s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'But how do you go from just being another agent, one of the 20 agents maybe '
               "that's calling them in the week to someone that they actually want to work "
               "with, especially if you're a brand new freight broker or like a newly hired "
               'agent.',
       'timestamp': 814,
       'timestamp_label': '[00:13:34]',
       'timestamp_seconds': 814,
       'tip': 'But how do you go from just being another agent, one of the 20 agents maybe '
              "that's calling them in the week to someone that they actually want to work "
              "with, especially if you're a brand new freight broker or like a newly hired "
              'agent.',
       'title': '7 Step Freight Agent Training To Go From $0-$1,000,000 From Home (Matt '
                'Krause)',
       'url': 'https://www.youtube.com/watch?v=yeFtuLvEdO8&t=814s',
       'video_id': 'yeFtuLvEdO8'},
      {'author': 'Bobby Loads',
       'channel': 'Bobby Loads',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:52](https://www.youtube.com/watch?v=2vUXF3RIbqg&t=712s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "I'm going to send him to the closest best area, and then start the week off "
               'again with him, and start banging out the money. So, for just starting, I '
               "don't think that's bad at all.",
       'timestamp': 712,
       'timestamp_label': '[00:11:52]',
       'timestamp_seconds': 712,
       'tip': "I'm going to send him to the closest best area, and then start the week off "
              "again with him, and start banging out the money. So, for just starting, I don't "
              "think that's bad at all.",
       'title': 'These Hot Lanes Are Printing Money Right Now | Trucking Market Update (Bobby '
                'Loads)',
       'url': 'https://www.youtube.com/watch?v=2vUXF3RIbqg&t=712s',
       'video_id': '2vUXF3RIbqg'},
      {'author': 'Freight 360',
       'channel': 'Freight 360',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:23](https://www.youtube.com/watch?v=xe94bfEYHEU&t=383s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Now, the driver is at the concinee and they said they can't start loading "
               'until 12:00 p. The broker said they will only recognize the check-in from '
               '11:00 a. Left me with one hour detention while lost almost a whole day.',
       'timestamp': 383,
       'timestamp_label': '[00:06:23]',
       'timestamp_seconds': 383,
       'tip': "Now, the driver is at the concinee and they said they can't start loading until "
              '12:00 p. The broker said they will only recognize the check-in from 11:00 a. '
              'Left me with one hour detention while lost almost a whole day.',
       'title': 'How Clear Policies On Detention And Layover Save Headaches | Final Mile 133 '
                '(Freight 360)',
       'url': 'https://www.youtube.com/watch?v=xe94bfEYHEU&t=383s',
       'video_id': 'xe94bfEYHEU'},
      {'author': 'ShipLeague',
       'channel': 'ShipLeague',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:26](https://www.youtube.com/watch?v=rMpa5pbBWtI&t=206s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Thinks or predicts that the market will pay within the next eight days or at '
               "least the condition that it will be in let's look at current day very tight "
               'prior eight days.',
       'timestamp': 206,
       'timestamp_label': '[00:03:26]',
       'timestamp_seconds': 206,
       'tip': 'Thinks or predicts that the market will pay within the next eight days or at '
              "least the condition that it will be in let's look at current day very tight "
              'prior eight days.',
       'title': 'How Freight Brokers Quote Shippers - Explained (ShipLeague)',
       'url': 'https://www.youtube.com/watch?v=rMpa5pbBWtI&t=206s',
       'video_id': 'rMpa5pbBWtI'},
      {'author': 'Double Broker Bounty Hunter',
       'channel': 'Double Broker Bounty Hunter',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:24:23](https://www.youtube.com/watch?v=3WxrmhqpsyY&t=1463s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "All you got to do is contact me stay safe out there and whatever you do don't "
               'let scammers take you for a ride take care folks we will see you again next '
               'week.',
       'timestamp': 1463,
       'timestamp_label': '[00:24:23]',
       'timestamp_seconds': 1463,
       'tip': "All you got to do is contact me stay safe out there and whatever you do don't "
              'let scammers take you for a ride take care folks we will see you again next '
              'week.',
       'title': 'Transportation Fraud Prevention Series 2.0 - Part 1 - Basics of Double '
                'Brokering (Double Broker Bounty Hunter)',
       'url': 'https://www.youtube.com/watch?v=3WxrmhqpsyY&t=1463s',
       'video_id': '3WxrmhqpsyY'},
      {'author': 'FreightBrokers',
       'channel': 'FreightBrokers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:08](https://www.youtube.com/watch?v=JTrml3aFNrY&t=68s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Great job so that I can show you real life examples of how other people are '
               'using LinkedIn to Market their business create awareness start dialogues and '
               'yes.',
       'timestamp': 68,
       'timestamp_label': '[00:01:08]',
       'timestamp_seconds': 68,
       'tip': 'Great job so that I can show you real life examples of how other people are '
              'using LinkedIn to Market their business create awareness start dialogues and '
              'yes.',
       'title': 'Freight Broker Training: How to Find Shippers as a Freight Broker [Untapped '
                'Source] (FreightBrokers)',
       'url': 'https://www.youtube.com/watch?v=JTrml3aFNrY&t=68s',
       'video_id': 'JTrml3aFNrY'},
      {'author': 'ThinkFreight',
       'channel': 'ThinkFreight',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:41](https://www.youtube.com/watch?v=s-qzw5ZxjmU&t=101s)',
       'relevance': 'Attributed practitioner commentary on FMCSA-licensed niche freight '
                    'brokerage, double-brokering defense (`Highway`/`RMIS`), and '
                    'shipper-to-carrier float management (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Under the new rule, the FMCSA can immediately suspend a broker or a freight '
               "forwarder's operating authority if their bond or trust drops below that "
               'threshold and is not replenished within seven calendar days.',
       'timestamp': 101,
       'timestamp_label': '[00:01:41]',
       'timestamp_seconds': 101,
       'tip': 'Under the new rule, the FMCSA can immediately suspend a broker or a freight '
              "forwarder's operating authority if their bond or trust drops below that "
              'threshold and is not replenished within seven calendar days.',
       'title': 'FINALLY: FMCSA Targets Freight Brokers With New Rule (ThinkFreight)',
       'url': 'https://www.youtube.com/watch?v=s-qzw5ZxjmU&t=101s',
       'video_id': 's-qzw5ZxjmU'}]}
