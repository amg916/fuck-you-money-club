"""Curated 180-citation SaaS Discount Brokerage & GPO Arbitrage baseline (15 per chapter across Q1-Q12) mined strictly from verified SaaS Discount Brokerage & GPO Arbitrage YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'50k',
     'added',
     'adobe',
     'advisor',
     'agency',
     'agent',
     'aggregation',
     'agreements',
     'annual',
     'apollo',
     'appdirect',
     'asana',
     'atlassian',
     'audit',
     'auto',
     'avant',
     'aws',
     'b2b',
     'beat',
     'benchmarking',
     'bill',
     'bills',
     'brokerage',
     'brokers',
     'building',
     'builtwith',
     'business',
     'businesses',
     'buyer',
     'call',
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
 2: {'50k',
     'added',
     'adobe',
     'advisor',
     'agency',
     'agent',
     'aggregation',
     'agreements',
     'annual',
     'apollo',
     'appdirect',
     'asana',
     'atlassian',
     'audit',
     'auto',
     'avant',
     'aws',
     'b2b',
     'beat',
     'benchmarking',
     'bill',
     'bills',
     'brokerage',
     'brokers',
     'budget',
     'building',
     'builtwith',
     'business',
     'businesses',
     'buyer',
     'call',
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
 3: {'50k',
     'added',
     'adobe',
     'advisor',
     'agency',
     'agent',
     'aggregation',
     'agreements',
     'annual',
     'apollo',
     'appdirect',
     'asana',
     'atlassian',
     'audit',
     'auto',
     'avant',
     'aws',
     'b2b',
     'beat',
     'benchmarking',
     'bill',
     'bills',
     'brokerage',
     'brokers',
     'building',
     'builtwith',
     'business',
     'businesses',
     'buyer',
     'call',
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
 4: {'50k',
     'added',
     'adobe',
     'advisor',
     'agency',
     'agent',
     'aggregation',
     'agreements',
     'annual',
     'apollo',
     'appdirect',
     'asana',
     'atlassian',
     'audit',
     'auto',
     'avant',
     'aws',
     'b2b',
     'beat',
     'benchmarking',
     'bill',
     'bills',
     'brokerage',
     'brokers',
     'budget',
     'building',
     'builtwith',
     'business',
     'businesses',
     'buyer',
     'call',
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
 5: {'50k',
     'added',
     'adobe',
     'advisor',
     'agency',
     'agent',
     'aggregation',
     'agreements',
     'annual',
     'apollo',
     'appdirect',
     'asana',
     'atlassian',
     'audit',
     'auto',
     'avant',
     'avoid',
     'aws',
     'b2b',
     'beat',
     'benchmarking',
     'bill',
     'bills',
     'brokerage',
     'brokers',
     'building',
     'builtwith',
     'business',
     'businesses',
     'buyer',
     'call',
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
 6: {'50k',
     'added',
     'adobe',
     'advisor',
     'agency',
     'agent',
     'aggregation',
     'agreements',
     'annual',
     'apollo',
     'appdirect',
     'asana',
     'atlassian',
     'audit',
     'auto',
     'avant',
     'aws',
     'b2b',
     'beat',
     'benchmarking',
     'bill',
     'bills',
     'brokerage',
     'brokers',
     'building',
     'builtwith',
     'business',
     'businesses',
     'buyer',
     'call',
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
 7: {'50k',
     'added',
     'adobe',
     'advisor',
     'agency',
     'agent',
     'aggregation',
     'agreements',
     'annual',
     'apollo',
     'appdirect',
     'asana',
     'atlassian',
     'audit',
     'auto',
     'avant',
     'aws',
     'b2b',
     'beat',
     'benchmarking',
     'bill',
     'bills',
     'brokerage',
     'brokers',
     'building',
     'builtwith',
     'business',
     'businesses',
     'buyer',
     'call',
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
 8: {'50k',
     'added',
     'adobe',
     'advisor',
     'agency',
     'agent',
     'aggregation',
     'agreements',
     'annual',
     'api',
     'apollo',
     'appdirect',
     'asana',
     'atlassian',
     'audit',
     'auto',
     'avant',
     'aws',
     'b2b',
     'beat',
     'benchmarking',
     'bill',
     'bills',
     'brokerage',
     'brokers',
     'building',
     'builtwith',
     'business',
     'businesses',
     'buyer',
     'call',
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
 9: {'50k',
     'added',
     'adobe',
     'advisor',
     'agency',
     'agent',
     'aggregation',
     'agreement',
     'agreements',
     'annual',
     'apollo',
     'appdirect',
     'asana',
     'atlassian',
     'audit',
     'auto',
     'avant',
     'aws',
     'b2b',
     'beat',
     'benchmarking',
     'bill',
     'bills',
     'brokerage',
     'brokers',
     'building',
     'builtwith',
     'business',
     'businesses',
     'buyer',
     'call',
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
 10: {'50k',
      'added',
      'adobe',
      'advisor',
      'agency',
      'agent',
      'aggregation',
      'agreements',
      'ai',
      'annual',
      'apollo',
      'appdirect',
      'asana',
      'atlassian',
      'audit',
      'auto',
      'automate',
      'automation',
      'avant',
      'aws',
      'b2b',
      'beat',
      'benchmarking',
      'bill',
      'bills',
      'brokerage',
      'brokers',
      'building',
      'builtwith',
      'business',
      'businesses',
      'buyer',
      'call',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'50k',
      'added',
      'adobe',
      'advisor',
      'agency',
      'agent',
      'aggregation',
      'agreements',
      'annual',
      'apollo',
      'appdirect',
      'asana',
      'atlassian',
      'audit',
      'auto',
      'avant',
      'aws',
      'b2b',
      'beat',
      'benchmarking',
      'bill',
      'bills',
      'brokerage',
      'brokers',
      'building',
      'builtwith',
      'business',
      'businesses',
      'buyer',
      'call',
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
 12: {'50k',
      'action',
      'added',
      'adobe',
      'advisor',
      'agency',
      'agent',
      'aggregation',
      'agreements',
      'annual',
      'apollo',
      'appdirect',
      'asana',
      'atlassian',
      'audit',
      'auto',
      'avant',
      'aws',
      'b2b',
      'beat',
      'benchmarking',
      'bill',
      'bills',
      'brokerage',
      'brokers',
      'building',
      'builtwith',
      'business',
      'businesses',
      'buyer',
      'call',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Willingness to Pay',
      'channel': 'Willingness to Pay',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:26](https://www.youtube.com/watch?v=cdQzCVUJybY&t=326s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, actually generating value for the client. Probably the service cost, the '
              'fixed costs in the business are the same. And we actually can still end up with '
              'more profit.',
      'timestamp': 326,
      'timestamp_label': '[00:05:26]',
      'timestamp_seconds': 326,
      'tip': 'So, actually generating value for the client. Probably the service cost, the '
             'fixed costs in the business are the same. And we actually can still end up with '
             'more profit.',
      'title': 'Pricing for B2B SaaS (Willingness to Pay)',
      'url': 'https://www.youtube.com/watch?v=cdQzCVUJybY&t=326s',
      'video_id': 'cdQzCVUJybY'},
     {'author': 'Pax8',
      'channel': 'Pax8',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:41](https://www.youtube.com/watch?v=KcmWalqZBzk&t=41s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Major League Baseball franchise would, but it doesn't cost anywhere near that "
              'amount of money to get started. The beauty of owning a managed service and '
              'security practice today is the recurring model of revenue it provides.',
      'timestamp': 41,
      'timestamp_label': '[00:00:41]',
      'timestamp_seconds': 41,
      'tip': "Major League Baseball franchise would, but it doesn't cost anywhere near that "
             'amount of money to get started. The beauty of owning a managed service and '
             'security practice today is the recurring model of revenue it provides.',
      'title': 'Building a Profitable MSP | Pax8 (Pax8)',
      'url': 'https://www.youtube.com/watch?v=KcmWalqZBzk&t=41s',
      'video_id': 'KcmWalqZBzk'},
     {'author': 'Tech Meets East',
      'channel': 'Tech Meets East',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:03](https://www.youtube.com/watch?v=IIVbCmH7kHA&t=843s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Firefly on its own was closing in on $300 million in annual recurring revenue. '
              'Real money, but still small next to a company bringing in more than six and a '
              'half billion dollars every quarter. The market hated it anyway.',
      'timestamp': 843,
      'timestamp_label': '[00:14:03]',
      'timestamp_seconds': 843,
      'tip': 'Firefly on its own was closing in on $300 million in annual recurring revenue. '
             'Real money, but still small next to a company bringing in more than six and a '
             'half billion dollars every quarter. The market hated it anyway.',
      'title': 'Adobe Just Changed Photoshop Sales Forever (Tech Meets East)',
      'url': 'https://www.youtube.com/watch?v=IIVbCmH7kHA&t=843s',
      'video_id': 'IIVbCmH7kHA'},
     {'author': 'Ingram Micro Cloud',
      'channel': 'Ingram Micro Cloud',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:01](https://www.youtube.com/watch?v=ggEr5VKX-S8&t=61s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We're also able to open up a cloud marketplace and make that available to all "
              'of our customers so that they can go procure various licenses on their own they '
              'can have a self-service model that really suits both us as resellers and the '
              'client.',
      'timestamp': 61,
      'timestamp_label': '[00:01:01]',
      'timestamp_seconds': 61,
      'tip': "We're also able to open up a cloud marketplace and make that available to all of "
             'our customers so that they can go procure various licenses on their own they can '
             'have a self-service model that really suits both us as resellers and the client.',
      'title': 'Selling Google Workspace through Ingram Micro Cloud at Observian (Ingram Micro '
               'Cloud)',
      'url': 'https://www.youtube.com/watch?v=ggEr5VKX-S8&t=61s',
      'video_id': 'ggEr5VKX-S8'},
     {'author': 'RadiusPoint',
      'channel': 'RadiusPoint',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:18](https://www.youtube.com/watch?v=mFoRTIncoOI&t=258s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Priority number one is to ensure the service delivered by Telecom vendors fits '
              'your business model and exceeds expectations.',
      'timestamp': 258,
      'timestamp_label': '[00:04:18]',
      'timestamp_seconds': 258,
      'tip': 'Priority number one is to ensure the service delivered by Telecom vendors fits '
             'your business model and exceeds expectations.',
      'title': 'What does a Telecom Expense Management Specialist Do? How does TEM Help '
               'Cutting Costs? (RadiusPoint)',
      'url': 'https://www.youtube.com/watch?v=mFoRTIncoOI&t=258s',
      'video_id': 'mFoRTIncoOI'},
     {'author': 'OMNIA Partners',
      'channel': 'OMNIA Partners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=eTxETdL4Omg&t=54s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Utilizing the lead public agency contracting model that government and '
              'educational institutions rely upon as best practice, OMNIA Partners brings '
              'compliance, difference-making efficiencies, and maximum value to the purchasing '
              'process.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'Utilizing the lead public agency contracting model that government and '
             'educational institutions rely upon as best practice, OMNIA Partners brings '
             'compliance, difference-making efficiencies, and maximum value to the purchasing '
             'process.',
      'title': 'Cooperative Purchasing Provides Value to Public Agencies Through OMNIA '
               'Partners (OMNIA Partners)',
      'url': 'https://www.youtube.com/watch?v=eTxETdL4Omg&t=54s',
      'video_id': 'eTxETdL4Omg'},
     {'author': 'AeroCom Inc',
      'channel': 'AeroCom Inc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:56](https://www.youtube.com/watch?v=H1SvYMYWK1o&t=296s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And the biggest thing that Zoom added in 2026 is something they call the Zoom '
              "Revenue Accelerator product. It's an add-on that you can add on to Zoom Phone "
              "and it's really geared, in my opinion, towards sales teams.",
      'timestamp': 296,
      'timestamp_label': '[00:04:56]',
      'timestamp_seconds': 296,
      'tip': 'And the biggest thing that Zoom added in 2026 is something they call the Zoom '
             "Revenue Accelerator product. It's an add-on that you can add on to Zoom Phone "
             "and it's really geared, in my opinion, towards sales teams.",
      'title': "Zoom Phone - What's New in 2026 (AeroCom Inc)",
      'url': 'https://www.youtube.com/watch?v=H1SvYMYWK1o&t=296s',
      'video_id': 'H1SvYMYWK1o'},
     {'author': 'Ingram Micro Cloud UK',
      'channel': 'Ingram Micro Cloud UK',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:34](https://www.youtube.com/watch?v=bGmD7XlTNZI&t=94s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Wouldn't have been able to do that naturally as an infrastructure partner our "
              'go to market has always been particularly on premise Solutions the market is '
              'moving towards a cloud Compu model we have to embrace.',
      'timestamp': 94,
      'timestamp_label': '[00:01:34]',
      'timestamp_seconds': 94,
      'tip': "Wouldn't have been able to do that naturally as an infrastructure partner our go "
             'to market has always been particularly on premise Solutions the market is moving '
             'towards a cloud Compu model we have to embrace.',
      'title': 'How an IT reseller transformed their business with Ingram Micro Cloud (Ingram '
               'Micro Cloud UK)',
      'url': 'https://www.youtube.com/watch?v=bGmD7XlTNZI&t=94s',
      'video_id': 'bGmD7XlTNZI'},
     {'author': 'Partner Insight',
      'channel': 'Partner Insight',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:30](https://www.youtube.com/watch?v=LPPIZuIcjuA&t=150s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'SI or GSI, that could be a value-added reseller, specialized reseller, or even '
              'an MSP partner. I like starting with data so that everyone understands the the '
              'importance.',
      'timestamp': 150,
      'timestamp_label': '[00:02:30]',
      'timestamp_seconds': 150,
      'tip': 'SI or GSI, that could be a value-added reseller, specialized reseller, or even '
             'an MSP partner. I like starting with data so that everyone understands the the '
             'importance.',
      'title': 'How ISVs can scale revenue on Google Cloud Marketplace with Partners.  '
               'Underappreciated opportunity (Partner Insight)',
      'url': 'https://www.youtube.com/watch?v=LPPIZuIcjuA&t=150s',
      'video_id': 'LPPIZuIcjuA'},
     {'author': 'bobvalueadded',
      'channel': 'bobvalueadded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:19](https://www.youtube.com/watch?v=z-ZzUEITMGM&t=439s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Is there recognition and demand for your solution within the current '
              'marketplace? What is the opportunity this business relationship presents '
              'relative to net profit, gross dollar sales, opportunities, and strategic value?',
      'timestamp': 439,
      'timestamp_label': '[00:07:19]',
      'timestamp_seconds': 439,
      'tip': 'Is there recognition and demand for your solution within the current '
             'marketplace? What is the opportunity this business relationship presents '
             'relative to net profit, gross dollar sales, opportunities, and strategic value?',
      'title': 'Reseller - VAR  Value Added  Reseller Part 1 (bobvalueadded)',
      'url': 'https://www.youtube.com/watch?v=z-ZzUEITMGM&t=439s',
      'video_id': 'z-ZzUEITMGM'},
     {'author': 'Sherweb',
      'channel': 'Sherweb',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:16](https://www.youtube.com/watch?v=kD54qMCh58A&t=76s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '25,000 revenue is going to hold true both for last fiscal year and, uh, the ne '
              'next fiscal year. Um, for the business applications and modern work incentives, '
              'um, any of the solution partner designations, uh, will allow you to earn '
              'rebates for those two clouds.',
      'timestamp': 76,
      'timestamp_label': '[00:01:16]',
      'timestamp_seconds': 76,
      'tip': '25,000 revenue is going to hold true both for last fiscal year and, uh, the ne '
             'next fiscal year. Um, for the business applications and modern work incentives, '
             'um, any of the solution partner designations, uh, will allow you to earn rebates '
             'for those two clouds.',
      'title': 'How to qualify for Microsoft partner program cashback incentives in 2026 | '
               'MAICPP FY26 (Sherweb)',
      'url': 'https://www.youtube.com/watch?v=kD54qMCh58A&t=76s',
      'video_id': 'kD54qMCh58A'},
     {'author': 'Redress Compliance',
      'channel': 'Redress Compliance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=sALcv-71Klw&t=77s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You can counter an exorbitant proposal by calmly stating that it's out of line "
              'with what the market is paying. Often Oracle will come back with a much better '
              "offer when they realize you're an informed buyer. Remember, Oracle's first "
              'offer is rarely their best.',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': "You can counter an exorbitant proposal by calmly stating that it's out of line "
             'with what the market is paying. Often Oracle will come back with a much better '
             "offer when they realize you're an informed buyer. Remember, Oracle's first offer "
             'is rarely their best.',
      'title': '🎥 Oracle ERP Cloud Negotiation Tip #9: Benchmark and Know the Market Rates '
               '(Redress Compliance)',
      'url': 'https://www.youtube.com/watch?v=sALcv-71Klw&t=77s',
      'video_id': 'sALcv-71Klw'},
     {'author': 'UC Today News',
      'channel': 'UC Today News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:42](https://www.youtube.com/watch?v=Wcqc4eUu_5o&t=1062s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um I guess the big question is this uh just another a bandwagon kind of '
              "exercise from Zoom they're jumping on or you know is this going to drive a real "
              'value in another sort of UC area of the market what do people think.',
      'timestamp': 1062,
      'timestamp_label': '[00:17:42]',
      'timestamp_seconds': 1062,
      'tip': 'Um I guess the big question is this uh just another a bandwagon kind of exercise '
             "from Zoom they're jumping on or you know is this going to drive a real value in "
             'another sort of UC area of the market what do people think.',
      'title': "The Latest Big News on ALE Doubling Down on UCaaS, Enterprise ChatGPT & Zoom's "
               'AI Companion (UC Today News)',
      'url': 'https://www.youtube.com/watch?v=Wcqc4eUu_5o&t=1062s',
      'video_id': 'Wcqc4eUu_5o'},
     {'author': 'Rob Walling',
      'channel': 'Rob Walling',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:50](https://www.youtube.com/watch?v=lC6Gpn0ugFI&t=230s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Revenue share on the gmv then that would be your sas revenue in addition to any '
              'monthly recurring charges thanks so much for joining me as we walk through '
              "these five sas pricing models explained I hope you enjoyed the video and I'll "
              'see in the next one.',
      'timestamp': 230,
      'timestamp_label': '[00:03:50]',
      'timestamp_seconds': 230,
      'tip': 'Revenue share on the gmv then that would be your sas revenue in addition to any '
             'monthly recurring charges thanks so much for joining me as we walk through these '
             "five sas pricing models explained I hope you enjoyed the video and I'll see in "
             'the next one.',
      'title': 'SaaS Pricing Models Explained in 5 Minutes (Rob Walling)',
      'url': 'https://www.youtube.com/watch?v=lC6Gpn0ugFI&t=230s',
      'video_id': 'lC6Gpn0ugFI'},
     {'author': 'Una',
      'channel': 'Una',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=pKhFVbBzkz4&t=103s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That there's no catch we show value in the savings but also in our "
              "relationships with you and with the supplier and there's no there's nothing "
              "hidden there's no fees anything like that we just want to make sure that we're "
              'helping you succeed.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': "That there's no catch we show value in the savings but also in our relationships "
             "with you and with the supplier and there's no there's nothing hidden there's no "
             "fees anything like that we just want to make sure that we're helping you "
             'succeed.',
      'title': 'GPO FAQ: Exploring the Benefits of a Group Purchasing Organization (Una)',
      'url': 'https://www.youtube.com/watch?v=pKhFVbBzkz4&t=103s',
      'video_id': 'pKhFVbBzkz4'}],
 2: [{'author': 'Una',
      'channel': 'Una',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:39](https://www.youtube.com/watch?v=N9511Ln5CfE&t=99s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So in a fancy way, we always kind of say it’s like the Costco for B2B. The '
              'whole membership model, the leverage model. Only you don’t have to pay a fee. '
              'And you get all the savings, the real-life savings to operate your business.',
      'timestamp': 99,
      'timestamp_label': '[00:01:39]',
      'timestamp_seconds': 99,
      'tip': 'So in a fancy way, we always kind of say it’s like the Costco for B2B. The whole '
             'membership model, the leverage model. Only you don’t have to pay a fee. And you '
             'get all the savings, the real-life savings to operate your business.',
      'title': 'What Businesses Need To Know About GPOs (Una)',
      'url': 'https://www.youtube.com/watch?v=N9511Ln5CfE&t=99s',
      'video_id': 'N9511Ln5CfE'},
     {'author': 'Soft Learn Hub',
      'channel': 'Soft Learn Hub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:36](https://www.youtube.com/watch?v=oDjXoRkYaA0&t=96s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You pay only when the job gets done. HubSpot's Customer Agent costs fifty cents "
              'per resolved conversation, and escalated ones are free. Intercom charges '
              'ninety-nine cents per resolution. Model three: the enterprise flat fee.',
      'timestamp': 96,
      'timestamp_label': '[00:01:36]',
      'timestamp_seconds': 96,
      'tip': "You pay only when the job gets done. HubSpot's Customer Agent costs fifty cents "
             'per resolved conversation, and escalated ones are free. Intercom charges '
             'ninety-nine cents per resolution. Model three: the enterprise flat fee.',
      'title': 'Per Seat Pricing Is Ending? 3 SaaS Pricing Models Replacing It (Atlassian '
               'Rovo, Dec 3) (Soft Learn Hub)',
      'url': 'https://www.youtube.com/watch?v=oDjXoRkYaA0&t=96s',
      'video_id': 'oDjXoRkYaA0'},
     {'author': 'Ingram Micro USA',
      'channel': 'Ingram Micro USA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:18](https://www.youtube.com/watch?v=ADZwWSQGFFI&t=438s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ingram Micro Financial Solutions is a value added resource within Ingram Micro. '
              'Dedicated to creating customized financing solutions tailored to your business. '
              'We offer flexible financing, fast approvals, and payment options that fit any '
              'project timeline and budget.',
      'timestamp': 438,
      'timestamp_label': '[00:07:18]',
      'timestamp_seconds': 438,
      'tip': 'Ingram Micro Financial Solutions is a value added resource within Ingram Micro. '
             'Dedicated to creating customized financing solutions tailored to your business. '
             'We offer flexible financing, fast approvals, and payment options that fit any '
             'project timeline and budget.',
      'title': 'How Ingram Micro and Cisco help partners grow together (Ingram Micro USA)',
      'url': 'https://www.youtube.com/watch?v=ADZwWSQGFFI&t=438s',
      'video_id': 'ADZwWSQGFFI'},
     {'author': 'WeAreVoxFlo',
      'channel': 'WeAreVoxFlo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:33](https://www.youtube.com/watch?v=Zbk_QOoXQ_M&t=93s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And if your customer wants to, they can add manual call wrap-up notes. A call '
              "doesn't have to be recorded into the CRM. Simply press close and nothing is "
              'stored for you. That means winning more new business, bigger deals, and '
              'stickier customers.',
      'timestamp': 93,
      'timestamp_label': '[00:01:33]',
      'timestamp_seconds': 93,
      'tip': 'And if your customer wants to, they can add manual call wrap-up notes. A call '
             "doesn't have to be recorded into the CRM. Simply press close and nothing is "
             'stored for you. That means winning more new business, bigger deals, and stickier '
             'customers.',
      'title': 'VoxFlo | CRM Integration for UCaaS & CCaaS Resellers #wearevoxflo '
               '(WeAreVoxFlo)',
      'url': 'https://www.youtube.com/watch?v=Zbk_QOoXQ_M&t=93s',
      'video_id': 'Zbk_QOoXQ_M'},
     {'author': 'Ancy Alphonse',
      'channel': 'Ancy Alphonse',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=RV9K4EXWxJs&t=157s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Like you know one organization uh they actually like you know audit your '
              'invoice and make sure that you know the charges are as per the contract in '
              'case.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': 'Like you know one organization uh they actually like you know audit your invoice '
             'and make sure that you know the charges are as per the contract in case.',
      'title': 'Telecom Expense Management (Ancy Alphonse)',
      'url': 'https://www.youtube.com/watch?v=RV9K4EXWxJs&t=157s',
      'video_id': 'RV9K4EXWxJs'},
     {'author': 'Adobe Care',
      'channel': 'Adobe Care',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=LCbK1S1leOQ&t=21s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s unique needs, and simplify selling and managing Adobe licenses so you can "
              'get the best customer retention. Okay, more about the roles. Direct Partners or '
              'Adobe Partner Connection, or APC, reseller partners who contract with Adobe.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "'s unique needs, and simplify selling and managing Adobe licenses so you can get "
             'the best customer retention. Okay, more about the roles. Direct Partners or '
             'Adobe Partner Connection, or APC, reseller partners who contract with Adobe.',
      'title': 'VIP MarketPlace Overview in Adobe Admin Console (Adobe Care)',
      'url': 'https://www.youtube.com/watch?v=LCbK1S1leOQ&t=21s',
      'video_id': 'LCbK1S1leOQ'},
     {'author': 'Marcus Harris Software & Tech Attorney',
      'channel': 'Marcus Harris Software & Tech Attorney',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:25](https://www.youtube.com/watch?v=xY5Bk1dd768&t=325s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re not giving that vendor the ability to extract additional fees from you as "
              'you go ahead and and utilize that software in your business. You want to make '
              "sure that you've got the ability to add users at defined prices.",
      'timestamp': 325,
      'timestamp_label': '[00:05:25]',
      'timestamp_seconds': 325,
      'tip': "'re not giving that vendor the ability to extract additional fees from you as "
             'you go ahead and and utilize that software in your business. You want to make '
             "sure that you've got the ability to add users at defined prices.",
      'title': 'Don’t Fall for These Sneaky SaaS Contract Negotiation Gotchas! (Marcus Harris '
               'Software & Tech Attorney)',
      'url': 'https://www.youtube.com/watch?v=xY5Bk1dd768&t=325s',
      'video_id': 'xY5Bk1dd768'},
     {'author': 'Educationleaves',
      'channel': 'Educationleaves',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:47](https://www.youtube.com/watch?v=Nx4UI5uowcw&t=107s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Members and some may do both these fees can be set as a percentage of the '
              'purchase or set as an annual flat rate members participate based on their '
              'purchasing needs and their level of confidence in what should be competitive '
              'pricing negotiated by their gpos.',
      'timestamp': 107,
      'timestamp_label': '[00:01:47]',
      'timestamp_seconds': 107,
      'tip': 'Members and some may do both these fees can be set as a percentage of the '
             'purchase or set as an annual flat rate members participate based on their '
             'purchasing needs and their level of confidence in what should be competitive '
             'pricing negotiated by their gpos.',
      'title': 'What is Group Purchasing Organization (GPO)?  Explained in 3 Minutes! '
               '(Educationleaves)',
      'url': 'https://www.youtube.com/watch?v=Nx4UI5uowcw&t=107s',
      'video_id': 'Nx4UI5uowcw'},
     {'author': 'Rahul Bhavsar',
      'channel': 'Rahul Bhavsar',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=5WTYMwbF2fc&t=15s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And not go to the price discussion rule with your customer welcome to this '
              'channel journey to cloud here we do business strategies product reviews.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'And not go to the price discussion rule with your customer welcome to this '
             'channel journey to cloud here we do business strategies product reviews.',
      'title': '5 Ways to Sell Microsoft 365 to Enterprise Buyers (Rahul Bhavsar)',
      'url': 'https://www.youtube.com/watch?v=5WTYMwbF2fc&t=15s',
      'video_id': '5WTYMwbF2fc'},
     {'author': 'Technical Support Online',
      'channel': 'Technical Support Online',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=DKHVlefC0YE&t=33s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, from here in this in this box, I select the VIP number which I want to '
              'reseller change. So, I select the customer VIP number and the customer email '
              'address which is admin email address, the admin account of this Adobe portal.',
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': 'So, from here in this in this box, I select the VIP number which I want to '
             'reseller change. So, I select the customer VIP number and the customer email '
             'address which is admin email address, the admin account of this Adobe portal.',
      'title': 'Need To Change Your Adobe Reseller? Watch This Tutorial (Technical Support '
               'Online)',
      'url': 'https://www.youtube.com/watch?v=DKHVlefC0YE&t=33s',
      'video_id': 'DKHVlefC0YE'},
     {'author': 'Inside Microsoft AI Cloud Partner Program',
      'channel': 'Inside Microsoft AI Cloud Partner Program',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=uHFljjNXztI&t=22s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So CSP counts in the designations for modern work SMB only. It counts for '
              'business applications, security, data and AI infrastructure and digital and app '
              'innovation. CPOR allows for partners to be recognized for servicing a '
              "customer's cloud environment.",
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'So CSP counts in the designations for modern work SMB only. It counts for '
             'business applications, security, data and AI infrastructure and digital and app '
             "innovation. CPOR allows for partners to be recognized for servicing a customer's "
             'cloud environment.',
      'title': 'CPOR Claiming Partner of Record Essentials to Unlock More Microsoft Partner '
               'Points! (Inside Microsoft AI Cloud Partner Program)',
      'url': 'https://www.youtube.com/watch?v=uHFljjNXztI&t=22s',
      'video_id': 'uHFljjNXztI'},
     {'author': 'Willingness to Pay',
      'channel': 'Willingness to Pay',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:32:42](https://www.youtube.com/watch?v=BGb6-WKMNN4&t=1962s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Flat fee in the model to just lift every customer up and then whatever is in '
              'the modules then drives sort of on a volume basis per employee year per.',
      'timestamp': 1962,
      'timestamp_label': '[00:32:42]',
      'timestamp_seconds': 1962,
      'tip': 'Flat fee in the model to just lift every customer up and then whatever is in the '
             'modules then drives sort of on a volume basis per employee year per.',
      'title': 'SaaS Pricing Architecture (Full Training) (Willingness to Pay)',
      'url': 'https://www.youtube.com/watch?v=BGb6-WKMNN4&t=1962s',
      'video_id': 'BGb6-WKMNN4'},
     {'author': 'Cloud Software Association',
      'channel': 'Cloud Software Association',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:42](https://www.youtube.com/watch?v=phXe8eJoVeo&t=762s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Partners about these products the stats are pretty conclusive about this Amazon '
              'raise it in terms of how much research and end customer is doing on the.',
      'timestamp': 762,
      'timestamp_label': '[00:12:42]',
      'timestamp_seconds': 762,
      'tip': 'Partners about these products the stats are pretty conclusive about this Amazon '
             'raise it in terms of how much research and end customer is doing on the.',
      'title': 'Pax8  - A Cloud Distributor that MSPs Actually Use (Cloud Software '
               'Association)',
      'url': 'https://www.youtube.com/watch?v=phXe8eJoVeo&t=762s',
      'video_id': 'phXe8eJoVeo'},
     {'author': 'Pax8',
      'channel': 'Pax8',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:08](https://www.youtube.com/watch?v=t4mdVMK1xl0&t=248s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And then as we we kind of started to work that in the business, we didn't go "
              'down the the typical customer zero route. We decided to kind of look outside of '
              "the MSP first. And we've got a fairly large customer in the care sector.",
      'timestamp': 248,
      'timestamp_label': '[00:04:08]',
      'timestamp_seconds': 248,
      'tip': "And then as we we kind of started to work that in the business, we didn't go "
             'down the the typical customer zero route. We decided to kind of look outside of '
             "the MSP first. And we've got a fairly large customer in the care sector.",
      'title': 'How MSPs Are Becoming Managed Intelligence Providers | Pax8 Beyond EMEA 2026 '
               'Partner Panel (Pax8)',
      'url': 'https://www.youtube.com/watch?v=t4mdVMK1xl0&t=248s',
      'video_id': 't4mdVMK1xl0'},
     {'author': 'Staying Connected',
      'channel': 'Staying Connected',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:41](https://www.youtube.com/watch?v=6YNd6Xcyekw&t=581s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Shoot us an email you can also stay current by subscribing to these staying '
              'connected podcasts by checking out our websites and by following us on '
              'linkedin.',
      'timestamp': 581,
      'timestamp_label': '[00:09:41]',
      'timestamp_seconds': 581,
      'tip': 'Shoot us an email you can also stay current by subscribing to these staying '
             'connected podcasts by checking out our websites and by following us on linkedin.',
      'title': 'Get the Most Value from Value Added Resellers (Staying Connected)',
      'url': 'https://www.youtube.com/watch?v=6YNd6Xcyekw&t=581s',
      'video_id': '6YNd6Xcyekw'}],
 3: [{'author': 'Ultimate CFO',
      'channel': 'Ultimate CFO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:56](https://www.youtube.com/watch?v=xmq83cmzth4&t=116s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Second, let's talk about the unit economics issue. In traditional SaaS, the "
              'marginal cost of a user was near zero. So you had this really high gross '
              'margins from your flat-fee per-user model and you had security in your gross '
              'margin.',
      'timestamp': 116,
      'timestamp_label': '[00:01:56]',
      'timestamp_seconds': 116,
      'tip': "Second, let's talk about the unit economics issue. In traditional SaaS, the "
             'marginal cost of a user was near zero. So you had this really high gross margins '
             'from your flat-fee per-user model and you had security in your gross margin.',
      'title': 'Why Enterprise Buyers Hate AI Pricing Models - The AI vs. SaaS Pricing War '
               '(Ultimate CFO)',
      'url': 'https://www.youtube.com/watch?v=xmq83cmzth4&t=116s',
      'video_id': 'xmq83cmzth4'},
     {'author': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
      'channel': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:25](https://www.youtube.com/watch?v=LGgw20GtaDQ&t=325s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Most businesses go with the annual term paid monthly because it sits right '
              "between cost and flexibility. Then there's the triennial term, which locks in "
              'your price for 3 years, and saves you about 12 to 18% compared to renewing '
              'annually.',
      'timestamp': 325,
      'timestamp_label': '[00:05:25]',
      'timestamp_seconds': 325,
      'tip': 'Most businesses go with the annual term paid monthly because it sits right '
             "between cost and flexibility. Then there's the triennial term, which locks in "
             'your price for 3 years, and saves you about 12 to 18% compared to renewing '
             'annually.',
      'title': 'Microsoft Cloud Solution Provider (CSP) - Simply Explained (m365 Show | M365, '
               'Azure Cloud, Power Platform & AI)',
      'url': 'https://www.youtube.com/watch?v=LGgw20GtaDQ&t=325s',
      'video_id': 'LGgw20GtaDQ'},
     {'author': 'Daniel Studios',
      'channel': 'Daniel Studios',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:44](https://www.youtube.com/watch?v=vQ-PbEC-qMw&t=44s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Okay, so let's start off with the pricing difference. So here, as you can see, "
              "for small businesses, you'll be able to see the price right ahead if you click "
              'on buy now.',
      'timestamp': 44,
      'timestamp_label': '[00:00:44]',
      'timestamp_seconds': 44,
      'tip': "Okay, so let's start off with the pricing difference. So here, as you can see, "
             "for small businesses, you'll be able to see the price right ahead if you click "
             'on buy now.',
      'title': 'Adobe Teams vs Enterprise Plans & Pricing Explained – Honest Comparison '
               '(Daniel Studios)',
      'url': 'https://www.youtube.com/watch?v=vQ-PbEC-qMw&t=44s',
      'video_id': 'vQ-PbEC-qMw'},
     {'author': 'singlesourcetelecom',
      'channel': 'singlesourcetelecom',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:59](https://www.youtube.com/watch?v=GcLqzAGpP2s&t=119s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your phone bills there is valuable assistance available normally at a fraction '
              'of the cost of doing an internal audit most of the time.',
      'timestamp': 119,
      'timestamp_label': '[00:01:59]',
      'timestamp_seconds': 119,
      'tip': 'Your phone bills there is valuable assistance available normally at a fraction '
             'of the cost of doing an internal audit most of the time.',
      'title': 'Bill Auditing and Telecom Expense Management Tips (singlesourcetelecom)',
      'url': 'https://www.youtube.com/watch?v=GcLqzAGpP2s&t=119s',
      'video_id': 'GcLqzAGpP2s'},
     {'author': 'Andrew Garberson',
      'channel': 'Andrew Garberson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:54](https://www.youtube.com/watch?v=l1Q6q8yDjTQ&t=414s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, take all of this as permission to be wrong about the first price that you '
              "introduced to market as long as you're right about the mechanism that supports "
              'it. So, pick a unit that the buyer already counts.',
      'timestamp': 414,
      'timestamp_label': '[00:06:54]',
      'timestamp_seconds': 414,
      'tip': 'So, take all of this as permission to be wrong about the first price that you '
             "introduced to market as long as you're right about the mechanism that supports "
             'it. So, pick a unit that the buyer already counts.',
      'title': 'SaaS Pricing Strategy: Why Most New Startups Moved Beyond Per-Seat (Andrew '
               'Garberson)',
      'url': 'https://www.youtube.com/watch?v=l1Q6q8yDjTQ&t=414s',
      'video_id': 'l1Q6q8yDjTQ'},
     {'author': 'Vendasta',
      'channel': 'Vendasta',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:49](https://www.youtube.com/watch?v=i4hzXM9eyQY&t=49s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Integration or they want to reduce costs of the software they're using to run "
              'their business Google workspace is essential for businesses of all sizes.',
      'timestamp': 49,
      'timestamp_label': '[00:00:49]',
      'timestamp_seconds': 49,
      'tip': "Integration or they want to reduce costs of the software they're using to run "
             'their business Google workspace is essential for businesses of all sizes.',
      'title': 'Four reasons to become a Google Workspace reseller (Vendasta)',
      'url': 'https://www.youtube.com/watch?v=i4hzXM9eyQY&t=49s',
      'video_id': 'i4hzXM9eyQY'},
     {'author': 'Startup Akademia',
      'channel': 'Startup Akademia',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:49](https://www.youtube.com/watch?v=8ORoloHxouk&t=169s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Selling price he will be optimizing his cost and in this way also your costs as '
              "well so that's in short if you have any questions regarding the framework "
              "please let me know I'm always happy to give more details and additional "
              'examples.',
      'timestamp': 169,
      'timestamp_label': '[00:02:49]',
      'timestamp_seconds': 169,
      'tip': 'Selling price he will be optimizing his cost and in this way also your costs as '
             "well so that's in short if you have any questions regarding the framework please "
             "let me know I'm always happy to give more details and additional examples.",
      'title': 'Management Consulting Case Interview – a framework for cost cutting (Startup '
               'Akademia)',
      'url': 'https://www.youtube.com/watch?v=8ORoloHxouk&t=169s',
      'video_id': '8ORoloHxouk'},
     {'author': 'MonetizeNow',
      'channel': 'MonetizeNow',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:47](https://www.youtube.com/watch?v=x0K0bAATQIA&t=167s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Most importantly, the renewal uplift configured on the original new business '
              'quote carries forward to this next contract automatically and MonetizeNow has '
              'increased the price for all products by 5%. Previously, the cost per user was '
              '$100 per user per month.',
      'timestamp': 167,
      'timestamp_label': '[00:02:47]',
      'timestamp_seconds': 167,
      'tip': 'Most importantly, the renewal uplift configured on the original new business '
             'quote carries forward to this next contract automatically and MonetizeNow has '
             'increased the price for all products by 5%. Previously, the cost per user was '
             '$100 per user per month.',
      'title': 'SaaS Renewal Price Uplifts: Automate Price Increases | MonetizeNow '
               '(MonetizeNow)',
      'url': 'https://www.youtube.com/watch?v=x0K0bAATQIA&t=167s',
      'video_id': 'x0K0bAATQIA'},
     {'author': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
      'channel': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:16](https://www.youtube.com/watch?v=rD2YxxfsOa4&t=376s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You pay a 20% premium over the annual list price. So, if the annual price is  '
              "$100 per user per month, the monthly price hits 120. That's the cost.",
      'timestamp': 376,
      'timestamp_label': '[00:06:16]',
      'timestamp_seconds': 376,
      'tip': 'You pay a 20% premium over the annual list price. So, if the annual price is  '
             "$100 per user per month, the monthly price hits 120. That's the cost.",
      'title': 'Microsoft Cloud Solution Provider CSP   Simply Explained (m365 Show | M365, '
               'Azure Cloud, Power Platform & AI)',
      'url': 'https://www.youtube.com/watch?v=rD2YxxfsOa4&t=376s',
      'video_id': 'rD2YxxfsOa4'},
     {'author': 'PBM Insider',
      'channel': 'PBM Insider',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:49](https://www.youtube.com/watch?v=uyVsmq0w3FM&t=49s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'PBM set up a new type of subsidiary called a group purchasing organization or '
              'GPO. GPOS are designed to aggregate the contracted wholesale price and '
              'negotiate the associated back-end rebates on behalf of the PBMs in an effort to '
              'lower costs by buying in bulk.',
      'timestamp': 49,
      'timestamp_label': '[00:00:49]',
      'timestamp_seconds': 49,
      'tip': 'PBM set up a new type of subsidiary called a group purchasing organization or '
             'GPO. GPOS are designed to aggregate the contracted wholesale price and negotiate '
             'the associated back-end rebates on behalf of the PBMs in an effort to lower '
             'costs by buying in bulk.',
      'title': "The PBM Insider - Group Purchasing Organizations (GPO's) (PBM Insider)",
      'url': 'https://www.youtube.com/watch?v=uyVsmq0w3FM&t=49s',
      'video_id': 'uyVsmq0w3FM'},
     {'author': 'Binary Stream Software',
      'channel': 'Binary Stream Software',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=ydyjI39LlNw&t=90s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ve been convinced of the value. Free versions are often ad supported. Hybrid "
              'pricing is a combination of any of the other pricing models and gives companies '
              'the flexibility to better price their services based on customer and market '
              'research.',
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': "'ve been convinced of the value. Free versions are often ad supported. Hybrid "
             'pricing is a combination of any of the other pricing models and gives companies '
             'the flexibility to better price their services based on customer and market '
             'research.',
      'title': '8 SaaS pricing models explained in under 3 minutes (Binary Stream Software)',
      'url': 'https://www.youtube.com/watch?v=ydyjI39LlNw&t=90s',
      'video_id': 'ydyjI39LlNw'},
     {'author': 'Zylo | The Leader in Enterprise SaaS Management',
      'channel': 'Zylo | The Leader in Enterprise SaaS Management',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:57](https://www.youtube.com/watch?v=ftGGihhAn3g&t=297s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Executive buy into the program to success and then lastly partner with your '
              'procurement peers to cash in on cost savings stay tuned to the next episode '
              "where we'll dive into the details of renewal management thank you for joining "
              'me and I will catch you next time.',
      'timestamp': 297,
      'timestamp_label': '[00:04:57]',
      'timestamp_seconds': 297,
      'tip': 'Executive buy into the program to success and then lastly partner with your '
             'procurement peers to cash in on cost savings stay tuned to the next episode '
             "where we'll dive into the details of renewal management thank you for joining me "
             'and I will catch you next time.',
      'title': 'SaaS License Management, Explained (Zylo | The Leader in Enterprise SaaS '
               'Management)',
      'url': 'https://www.youtube.com/watch?v=ftGGihhAn3g&t=297s',
      'video_id': 'ftGGihhAn3g'},
     {'author': 'UpperEdge, LLC',
      'channel': 'UpperEdge, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=nrJ8yyEVHmY&t=28s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s Microsoft service now Salesforce or any of them right so let's take a step "
              "back renewable price protections. There's always been conditions in there. You "
              'have to maintain the volume. You have to maintain the products.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': "'s Microsoft service now Salesforce or any of them right so let's take a step "
             "back renewable price protections. There's always been conditions in there. You "
             'have to maintain the volume. You have to maintain the products.',
      'title': 'SaaS Vendors’ New Trick: Multiplying Pricing Caps by Term Length (UpperEdge, '
               'LLC)',
      'url': 'https://www.youtube.com/watch?v=nrJ8yyEVHmY&t=28s',
      'video_id': 'nrJ8yyEVHmY'},
     {'author': 'Caliber (Formerly pclub.io)',
      'channel': 'Caliber (Formerly pclub.io)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:43](https://www.youtube.com/watch?v=B5SsF-kHahw&t=763s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now if they answer number two they say we have legitimate cash issues or '
              "logistical issues or other constraints we're sold on the value we want to move.",
      'timestamp': 763,
      'timestamp_label': '[00:12:43]',
      'timestamp_seconds': 763,
      'tip': 'Now if they answer number two they say we have legitimate cash issues or '
             "logistical issues or other constraints we're sold on the value we want to move.",
      'title': 'CEO EXPLAINS: 9 SaaS Negotiation Tips to Close SaaS Deals (At the Price YOU '
               'Want) (Caliber (Formerly pclub.io))',
      'url': 'https://www.youtube.com/watch?v=B5SsF-kHahw&t=763s',
      'video_id': 'B5SsF-kHahw'},
     {'author': 'Deutsche Telekom - B2B Europe',
      'channel': 'Deutsche Telekom - B2B Europe',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:16](https://www.youtube.com/watch?v=aIRwF9gyA-w&t=196s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Get a proper spending overview this reduces costs and increases productivity '
              'our goal is to help you make the complex simple your reports organized your '
              'orders simplified your efficiency enhanced.',
      'timestamp': 196,
      'timestamp_label': '[00:03:16]',
      'timestamp_seconds': 196,
      'tip': 'Get a proper spending overview this reduces costs and increases productivity our '
             'goal is to help you make the complex simple your reports organized your orders '
             'simplified your efficiency enhanced.',
      'title': 'Telecom Expense Management (Deutsche Telekom - B2B Europe)',
      'url': 'https://www.youtube.com/watch?v=aIRwF9gyA-w&t=196s',
      'video_id': 'aIRwF9gyA-w'}],
 4: [{'author': 'TD SYNNEX Spain',
      'channel': 'TD SYNNEX Spain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:55](https://www.youtube.com/watch?v=824bcq4wI-Q&t=1555s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, it's all for commercial or standard businesses, as you call it here. Uh, "
              'yes, we simply have business licenses with discounted levels. Okay, in Stream '
              "One, in the opportunities section, I don't see the Adobe option to transfer the "
              'VIP.',
      'timestamp': 1555,
      'timestamp_label': '[00:25:55]',
      'timestamp_seconds': 1555,
      'tip': "So, it's all for commercial or standard businesses, as you call it here. Uh, "
             'yes, we simply have business licenses with discounted levels. Okay, in Stream '
             "One, in the opportunities section, I don't see the Adobe option to transfer the "
             'VIP.',
      'title': 'Adobe VIP Marketplace (TD SYNNEX Spain)',
      'url': 'https://www.youtube.com/watch?v=824bcq4wI-Q&t=1555s',
      'video_id': '824bcq4wI-Q'},
     {'author': 'Sales Scripter',
      'channel': 'Sales Scripter',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:49](https://www.youtube.com/watch?v=u9D8WbQixac&t=709s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Michael] Well, that's why I'm reaching out. Because I'm with an agency, we "
              'provide software development services, have a full team of experienced '
              'developers. Mary] We do not have any budget right now. Michael] Hey, I '
              'understand.',
      'timestamp': 709,
      'timestamp_label': '[00:11:49]',
      'timestamp_seconds': 709,
      'tip': "Michael] Well, that's why I'm reaching out. Because I'm with an agency, we "
             'provide software development services, have a full team of experienced '
             'developers. Mary] We do not have any budget right now. Michael] Hey, I '
             'understand.',
      'title': 'Cold Call Example for Software Development (Sales Scripter)',
      'url': 'https://www.youtube.com/watch?v=u9D8WbQixac&t=709s',
      'video_id': 'u9D8WbQixac'},
     {'author': 'Auditel, Inc. Telecom Expense Management',
      'channel': 'Auditel, Inc. Telecom Expense Management',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:10](https://www.youtube.com/watch?v=F00NVfaC6Tk&t=250s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Confident is keeping your expense as lean as it can be give us a call and let's "
              'get started saving your business money eight hundred four seven three five six '
              'five five thanks for your time and thanks for watching.',
      'timestamp': 250,
      'timestamp_label': '[00:04:10]',
      'timestamp_seconds': 250,
      'tip': "Confident is keeping your expense as lean as it can be give us a call and let's "
             'get started saving your business money eight hundred four seven three five six '
             'five five thanks for your time and thanks for watching.',
      'title': 'Telecom Expense Management: Why have a telecom audit? Part 3 Forward Savings '
               '(Auditel, Inc. Telecom Expense Management)',
      'url': 'https://www.youtube.com/watch?v=F00NVfaC6Tk&t=250s',
      'video_id': 'F00NVfaC6Tk'},
     {'author': 'AeroCom Inc',
      'channel': 'AeroCom Inc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:16](https://www.youtube.com/watch?v=viRtp8k9GAo&t=376s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "In case your company wants more features and functionality that's included in "
              'the base license like call center software. Zoom has call center software '
              'available.',
      'timestamp': 376,
      'timestamp_label': '[00:06:16]',
      'timestamp_seconds': 376,
      'tip': "In case your company wants more features and functionality that's included in "
             'the base license like call center software. Zoom has call center software '
             'available.',
      'title': 'Zoom Phone Pricing for Mid-Large-Size Companies in 2025 (AeroCom Inc)',
      'url': 'https://www.youtube.com/watch?v=viRtp8k9GAo&t=376s',
      'video_id': 'viRtp8k9GAo'},
     {'author': 'Flexera | ITAM, FinOps & SaaS Management',
      'channel': 'Flexera | ITAM, FinOps & SaaS Management',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:45](https://www.youtube.com/watch?v=XMooFDnRJEE&t=165s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Assessment of your exposure to software license audits and an understanding of '
              'the actual savings of up to 30% of your software budget that you can expect to '
              'realize please contact Lex error today and ask for a free no-obligation '
              'software estate assessment.',
      'timestamp': 165,
      'timestamp_label': '[00:02:45]',
      'timestamp_seconds': 165,
      'tip': 'Assessment of your exposure to software license audits and an understanding of '
             'the actual savings of up to 30% of your software budget that you can expect to '
             'realize please contact Lex error today and ask for a free no-obligation software '
             'estate assessment.',
      'title': 'Saving with Software License Optimization | Flexera (Flexera | ITAM, FinOps & '
               'SaaS Management)',
      'url': 'https://www.youtube.com/watch?v=XMooFDnRJEE&t=165s',
      'video_id': 'XMooFDnRJEE'},
     {'author': 'Pax8',
      'channel': 'Pax8',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=7HqXWzAK1WM&t=146s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um, you know, contracts and agreements, tools, there's a lot of different "
              "areas, but that's just some of the highlights, highlevel things to start "
              "thinking about when you're getting into this business.",
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': "Um, you know, contracts and agreements, tools, there's a lot of different areas, "
             "but that's just some of the highlights, highlevel things to start thinking about "
             "when you're getting into this business.",
      'title': 'Your MSP Questions, Answered: Stack, Security, Coaching & Community | Pax8 '
               '(Pax8)',
      'url': 'https://www.youtube.com/watch?v=7HqXWzAK1WM&t=146s',
      'video_id': '7HqXWzAK1WM'},
     {'author': 'Bechtle UK',
      'channel': 'Bechtle UK',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:17](https://www.youtube.com/watch?v=v3ZCe1YINus&t=677s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'He will take you through the guided tour of the Beckler clouds and complete any '
              'renewal changes ready for your renewal date can I adjust my licenses before the '
              'auto renew window yes you can reduce or increase your license quti in the '
              'Readiness of your auto renew.',
      'timestamp': 677,
      'timestamp_label': '[00:11:17]',
      'timestamp_seconds': 677,
      'tip': 'He will take you through the guided tour of the Beckler clouds and complete any '
             'renewal changes ready for your renewal date can I adjust my licenses before the '
             'auto renew window yes you can reduce or increase your license quti in the '
             'Readiness of your auto renew.',
      'title': 'Are you ready for the changes coming to Adobe VIP? (Bechtle UK)',
      'url': 'https://www.youtube.com/watch?v=v3ZCe1YINus&t=677s',
      'video_id': 'v3ZCe1YINus'},
     {'author': 'MT Purchasing',
      'channel': 'MT Purchasing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:41](https://www.youtube.com/watch?v=e9uItyw_9cI&t=101s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Their valuable time on direct spending and improving your business not looking '
              'for a cheap deal on office supplies this cuts internal costs as well as '
              'overhead which frees up capital.',
      'timestamp': 101,
      'timestamp_label': '[00:01:41]',
      'timestamp_seconds': 101,
      'tip': 'Their valuable time on direct spending and improving your business not looking '
             'for a cheap deal on office supplies this cuts internal costs as well as overhead '
             'which frees up capital.',
      'title': 'GPOs: Everything You Need To Know (MT Purchasing)',
      'url': 'https://www.youtube.com/watch?v=e9uItyw_9cI&t=101s',
      'video_id': 'e9uItyw_9cI'},
     {'author': 'Tubblog - The Hub for MSPs',
      'channel': 'Tubblog - The Hub for MSPs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:34:09](https://www.youtube.com/watch?v=NVSw5ZYgQzw&t=2049s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So you had the phone call, which was with a maybe came into the sales guy, '
              "which was Hey, can you switch this guy off? Because he's leaving the business "
              'this Friday? Claire, call her that is joining next Monday.',
      'timestamp': 2049,
      'timestamp_label': '[00:34:09]',
      'timestamp_seconds': 2049,
      'tip': 'So you had the phone call, which was with a maybe came into the sales guy, which '
             "was Hey, can you switch this guy off? Because he's leaving the business this "
             'Friday? Claire, call her that is joining next Monday.',
      'title': 'Pax8 Demo and Product Tour | MSP Cloud Services Marketplace (Tubblog - The Hub '
               'for MSPs)',
      'url': 'https://www.youtube.com/watch?v=NVSw5ZYgQzw&t=2049s',
      'video_id': 'NVSw5ZYgQzw'},
     {'author': 'TBSC',
      'channel': 'TBSC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:16](https://www.youtube.com/watch?v=9veqF5Bgt4E&t=16s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's the most important thing um my name is Madison I'm the marketing "
              "executive at the business software Center and in today's presentation I'm.",
      'timestamp': 16,
      'timestamp_label': '[00:00:16]',
      'timestamp_seconds': 16,
      'tip': "That's the most important thing um my name is Madison I'm the marketing "
             "executive at the business software Center and in today's presentation I'm.",
      'title': 'Claim Microsoft Co-Op/ Rebate Funding in 3 EASY Steps #CoffeeTalkTBSC (TBSC)',
      'url': 'https://www.youtube.com/watch?v=9veqF5Bgt4E&t=16s',
      'video_id': '9veqF5Bgt4E'},
     {'author': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
      'channel': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=uiVjifpxK38&t=89s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Building on Azure, Partner Center is how you  manage your entire Microsoft '
              "relationship. Miss it, and you're leaving money and tools on the table.",
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': 'Building on Azure, Partner Center is how you  manage your entire Microsoft '
             "relationship. Miss it, and you're leaving money and tools on the table.",
      'title': 'Microsoft Partner Center Explained: FY26 Benefits & CSP Guide (m365 Show | '
               'M365, Azure Cloud, Power Platform & AI)',
      'url': 'https://www.youtube.com/watch?v=uiVjifpxK38&t=89s',
      'video_id': 'uiVjifpxK38'},
     {'author': 'The SaaS CFO',
      'channel': 'The SaaS CFO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:22](https://www.youtube.com/watch?v=uBngVWkX0K4&t=1582s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Annually and my AC is 20K well then I'm closing 25 deals a year versus so I'm "
              'probably aligned with maybe a quarterly b or something like that but if my ACV '
              'is 100k that5 that going be pretty challenging for me to call like beond.',
      'timestamp': 1582,
      'timestamp_label': '[00:26:22]',
      'timestamp_seconds': 1582,
      'tip': "Annually and my AC is 20K well then I'm closing 25 deals a year versus so I'm "
             'probably aligned with maybe a quarterly b or something like that but if my ACV '
             'is 100k that5 that going be pretty challenging for me to call like beond.',
      'title': 'Unlocking Sales Success: Ben Murray and QuotaPath on Building Scalable '
               'Compensation Plans (The SaaS CFO)',
      'url': 'https://www.youtube.com/watch?v=uBngVWkX0K4&t=1582s',
      'video_id': 'uBngVWkX0K4'},
     {'author': 'Hospital Supply Chain Education',
      'channel': 'Hospital Supply Chain Education',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=f5FL9qjTeE0&t=87s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A single entity the GPO instead of negotiating with multiple suppliers this '
              'saves time and administrative effort allowing Healthcare Providers to.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': 'A single entity the GPO instead of negotiating with multiple suppliers this '
             'saves time and administrative effort allowing Healthcare Providers to.',
      'title': 'What is a healthcare Group Purchasing Organization or GPO? (Hospital Supply '
               'Chain Education)',
      'url': 'https://www.youtube.com/watch?v=f5FL9qjTeE0&t=87s',
      'video_id': 'f5FL9qjTeE0'},
     {'author': 'itGenius 🤓 Biz Tech Experts',
      'channel': 'itGenius 🤓 Biz Tech Experts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:22](https://www.youtube.com/watch?v=aAQpTV4Ybnk&t=202s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Account or you're looking to do a project in the tech World well you can take "
              'advantage of our free consultation and if you need help right now now then '
              'consider joining concierge or taking up a quick fix with our team for '
              'professional support for your Tech stack.',
      'timestamp': 202,
      'timestamp_label': '[00:03:22]',
      'timestamp_seconds': 202,
      'tip': "Account or you're looking to do a project in the tech World well you can take "
             'advantage of our free consultation and if you need help right now now then '
             'consider joining concierge or taking up a quick fix with our team for '
             'professional support for your Tech stack.',
      'title': 'Google Workspace Volume & Special Licensing | Discount Pricing and Split '
               'Billing Explained (itGenius 🤓 Biz Tech Experts)',
      'url': 'https://www.youtube.com/watch?v=aAQpTV4Ybnk&t=202s',
      'video_id': 'aAQpTV4Ybnk'},
     {'author': 'AHealthcareZ - Healthcare Finance Explained',
      'channel': 'AHealthcareZ - Healthcare Finance Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:11](https://www.youtube.com/watch?v=N0B0bUjLrUE&t=431s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If we work in healthcare we have to understand just a little bit of it and '
              "that's my point for today thank you for watching a healthcare z.",
      'timestamp': 431,
      'timestamp_label': '[00:07:11]',
      'timestamp_seconds': 431,
      'tip': 'If we work in healthcare we have to understand just a little bit of it and '
             "that's my point for today thank you for watching a healthcare z.",
      'title': 'Hospital Group Purchasing Organizations (GPOs) Explained (AHealthcareZ - '
               'Healthcare Finance Explained)',
      'url': 'https://www.youtube.com/watch?v=N0B0bUjLrUE&t=431s',
      'video_id': 'N0B0bUjLrUE'}],
 5: [{'author': 'Tech Meets East',
      'channel': 'Tech Meets East',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:35](https://www.youtube.com/watch?v=ZnXsR4iADwM&t=1355s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Then there's the growth itself. In April, Adobe bought SEMrush, a marketing "
              'data company for about $1. That deal added roughly $480 million in annual '
              "recurring revenue. Strip it out and Adobe's organic growth looks a lot slower.",
      'timestamp': 1355,
      'timestamp_label': '[00:22:35]',
      'timestamp_seconds': 1355,
      'tip': "Then there's the growth itself. In April, Adobe bought SEMrush, a marketing data "
             'company for about $1. That deal added roughly $480 million in annual recurring '
             "revenue. Strip it out and Adobe's organic growth looks a lot slower.",
      'title': 'Adobe’s CRAWLING Back To Customers! (Tech Meets East)',
      'url': 'https://www.youtube.com/watch?v=ZnXsR4iADwM&t=1355s',
      'video_id': 'ZnXsR4iADwM'},
     {'author': 'The Salary Negotiator',
      'channel': 'The Salary Negotiator',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=CnpFwgvhMNc&t=38s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And I'll close out the episode by highlighting three common mistakes you should "
              "avoid in sales for a salary negotiation. That way you don't risk the "
              'opportunity and you do actually secure competitive compensation before you '
              'start with their team.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': "And I'll close out the episode by highlighting three common mistakes you should "
             "avoid in sales for a salary negotiation. That way you don't risk the opportunity "
             'and you do actually secure competitive compensation before you start with their '
             'team.',
      'title': 'Salesforce Salary Negotiation | How to Navigate a Salesforce Offer Negotiation '
               '(The Salary Negotiator)',
      'url': 'https://www.youtube.com/watch?v=CnpFwgvhMNc&t=38s',
      'video_id': 'CnpFwgvhMNc'},
     {'author': 'Sell Better',
      'channel': 'Sell Better',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:53](https://www.youtube.com/watch?v=aW8jAYnvqyI&t=353s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I should call this person, or they're very tight in your ICP. I think a lot of "
              'salespeople fail to make that abundantly clear to the prospect up front.',
      'timestamp': 353,
      'timestamp_label': '[00:05:53]',
      'timestamp_seconds': 353,
      'tip': "I should call this person, or they're very tight in your ICP. I think a lot of "
             'salespeople fail to make that abundantly clear to the prospect up front.',
      'title': '35 Minutes of Expert Cold Calling Tips (B2B & Software Sales) (Sell Better)',
      'url': 'https://www.youtube.com/watch?v=aW8jAYnvqyI&t=353s',
      'video_id': 'aW8jAYnvqyI'},
     {'author': 'Redress Compliance',
      'channel': 'Redress Compliance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=-1Sqw4pgdxY&t=22s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're stuck paying for shelfware. One, negotiate annual downscaling rights. "
              'Push for the ability to reduce license counts each year, not just at renewal. '
              'You can offer to commit to a baseline number and allow reductions above that '
              'threshold if business needs shift.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "You're stuck paying for shelfware. One, negotiate annual downscaling rights. "
             'Push for the ability to reduce license counts each year, not just at renewal. '
             'You can offer to commit to a baseline number and allow reductions above that '
             'threshold if business needs shift.',
      'title': 'True-Up Flexibility in Microsoft EA – How to Avoid Paying for Unused Licenses '
               '(Redress Compliance)',
      'url': 'https://www.youtube.com/watch?v=-1Sqw4pgdxY&t=22s',
      'video_id': '-1Sqw4pgdxY'},
     {'author': 'Microsoft AI Cloud Partner Program',
      'channel': 'Microsoft AI Cloud Partner Program',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:46](https://www.youtube.com/watch?v=wMz3Phqj6cA&t=106s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sourcepass built an agent in Copilot Studio that handles it automatically. That '
              'one deployment opened up the door for three more engagements with the same '
              'customer, because once you solve a real problem, they want to know what else is '
              'possible.',
      'timestamp': 106,
      'timestamp_label': '[00:01:46]',
      'timestamp_seconds': 106,
      'tip': 'Sourcepass built an agent in Copilot Studio that handles it automatically. That '
             'one deployment opened up the door for three more engagements with the same '
             'customer, because once you solve a real problem, they want to know what else is '
             'possible.',
      'title': 'Pax8 + Microsoft: Accelerating Partner Growth With AI Adoption (Microsoft AI '
               'Cloud Partner Program)',
      'url': 'https://www.youtube.com/watch?v=wMz3Phqj6cA&t=106s',
      'video_id': 'wMz3Phqj6cA'},
     {'author': 'Caliber (Formerly pclub.io)',
      'channel': 'Caliber (Formerly pclub.io)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:58](https://www.youtube.com/watch?v=lmaQjDuWaSY&t=478s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Of the business value you're providing but if that's what they answer with they "
              'open the door with you to do additional Discovery to go deeper on the problem.',
      'timestamp': 478,
      'timestamp_label': '[00:07:58]',
      'timestamp_seconds': 478,
      'tip': "Of the business value you're providing but if that's what they answer with they "
             'open the door with you to do additional Discovery to go deeper on the problem.',
      'title': 'How We Negotiated a $385k SaaS Deal with Procurement (Without Discounting) '
               '(Caliber (Formerly pclub.io))',
      'url': 'https://www.youtube.com/watch?v=lmaQjDuWaSY&t=478s',
      'video_id': 'lmaQjDuWaSY'},
     {'author': 'Healthcare Supply Chain Hub: Angelique W. Beslic',
      'channel': 'Healthcare Supply Chain Hub: Angelique W. Beslic',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:16](https://www.youtube.com/watch?v=K2Slgt-y1wo&t=1276s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Secondary suppliers, other innovation can kind of creep into this leftover '
              'outside of commitments percentage, okay? I want to avoid compliance risk and '
              'rebate loss. So, try not to fall under the 80% commitment.',
      'timestamp': 1276,
      'timestamp_label': '[00:21:16]',
      'timestamp_seconds': 1276,
      'tip': 'Secondary suppliers, other innovation can kind of creep into this leftover '
             'outside of commitments percentage, okay? I want to avoid compliance risk and '
             'rebate loss. So, try not to fall under the 80% commitment.',
      'title': 'Demystifying GPO Contracts: How Healthcare Supply Chain Unlocks Savings and '
               'Strategy (Healthcare Supply Chain Hub: Angelique W. Beslic)',
      'url': 'https://www.youtube.com/watch?v=K2Slgt-y1wo&t=1276s',
      'video_id': 'K2Slgt-y1wo'},
     {'author': 'UC Today News',
      'channel': 'UC Today News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:39](https://www.youtube.com/watch?v=bQwapQbcKSk&t=459s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You know it's very easy to get excited about new technologies as they come out "
              "and they're very consumable but also that creates risk for the businesses.",
      'timestamp': 459,
      'timestamp_label': '[00:07:39]',
      'timestamp_seconds': 459,
      'tip': "You know it's very easy to get excited about new technologies as they come out "
             "and they're very consumable but also that creates risk for the businesses.",
      'title': 'Next Level UCaaS Expense Management for Zoom - UC Today News (UC Today News)',
      'url': 'https://www.youtube.com/watch?v=bQwapQbcKSk&t=459s',
      'video_id': 'bQwapQbcKSk'},
     {'author': 'Magic Chats',
      'channel': 'Magic Chats',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:12](https://www.youtube.com/watch?v=fM8cQVJ3oh8&t=252s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, that's what the problem that you have from that is is three things around "
              'people, protect process, and technology. And as an MSP, of course, on on the '
              'rest of their business, people, process, and technology is limited to to a '
              'certain extent.',
      'timestamp': 252,
      'timestamp_label': '[00:04:12]',
      'timestamp_seconds': 252,
      'tip': "Now, that's what the problem that you have from that is is three things around "
             'people, protect process, and technology. And as an MSP, of course, on on the '
             'rest of their business, people, process, and technology is limited to to a '
             'certain extent.',
      'title': '90%+ Customer Adoption? The Cybersecurity Sales Strategy MSPs Should Know | '
               'Blackpoint at Pax8 EMEA (Magic Chats)',
      'url': 'https://www.youtube.com/watch?v=fM8cQVJ3oh8&t=252s',
      'video_id': 'fM8cQVJ3oh8'},
     {'author': 'OMNIA Partners',
      'channel': 'OMNIA Partners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=QYe90AHibvQ&t=57s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I would just say in broader sense, supply chain plays a huge role. Everything '
              'from risk management to make sure that supply is uh is available and all the '
              'way down to operational improvement to make sure that the lights are on and the '
              'the business is running smoothly.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': 'I would just say in broader sense, supply chain plays a huge role. Everything '
             'from risk management to make sure that supply is uh is available and all the way '
             'down to operational improvement to make sure that the lights are on and the the '
             'business is running smoothly.',
      'title': 'Unlocking Private Equity Value with OMNIA Partners’ Spend Path and The Power '
               'of Group Purchasing (OMNIA Partners)',
      'url': 'https://www.youtube.com/watch?v=QYe90AHibvQ&t=57s',
      'video_id': 'QYe90AHibvQ'},
     {'author': 'Flexera | ITAM, FinOps & SaaS Management',
      'channel': 'Flexera | ITAM, FinOps & SaaS Management',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:47](https://www.youtube.com/watch?v=PNMNLFBOp7E&t=47s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Flexer customer, you would already have the agent installed and that could '
              'automatically push the browser extension to Google Chrome, Mozilla Firefox, '
              'Microsoft Edge, and Apple Safari.',
      'timestamp': 47,
      'timestamp_label': '[00:00:47]',
      'timestamp_seconds': 47,
      'tip': 'Flexer customer, you would already have the agent installed and that could '
             'automatically push the browser extension to Google Chrome, Mozilla Firefox, '
             'Microsoft Edge, and Apple Safari.',
      'title': 'SaaS Licence Rightsizing | How to Rightsize SaaS Licences, Subscriptions, and '
               'Features | Flexera (Flexera | ITAM, FinOps & SaaS Management)',
      'url': 'https://www.youtube.com/watch?v=PNMNLFBOp7E&t=47s',
      'video_id': 'PNMNLFBOp7E'},
     {'author': 'Pax8',
      'channel': 'Pax8',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:57](https://www.youtube.com/watch?v=HLMRv3YJ-sI&t=417s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is just a new set of technology solutions that can be applied to fixing a '
              "business problem. And so I think that's what's going to happen to the majority "
              'of service providers.',
      'timestamp': 417,
      'timestamp_label': '[00:06:57]',
      'timestamp_seconds': 417,
      'tip': 'This is just a new set of technology solutions that can be applied to fixing a '
             "business problem. And so I think that's what's going to happen to the majority "
             'of service providers.',
      'title': 'What Is the MIP Program? A Complete Guide for MSPs | Pax8 (Pax8)',
      'url': 'https://www.youtube.com/watch?v=HLMRv3YJ-sI&t=417s',
      'video_id': 'HLMRv3YJ-sI'},
     {'author': 'InstantHowTo',
      'channel': 'InstantHowTo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=qD94D5D7Z0E&t=62s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t you have to use a company email address. So, of course, this will not work "
              'with your basic email address just like this. So, personal email domains such '
              'as Gmail, Yahoo, Hotmail will not be accepted. So, you actually have to own a '
              'business.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': "'t you have to use a company email address. So, of course, this will not work "
             'with your basic email address just like this. So, personal email domains such as '
             'Gmail, Yahoo, Hotmail will not be accepted. So, you actually have to own a '
             'business.',
      'title': 'How To BECOME Google Workspace Reseller (QUICK & EASY) 2026 (InstantHowTo)',
      'url': 'https://www.youtube.com/watch?v=qD94D5D7Z0E&t=62s',
      'video_id': 'qD94D5D7Z0E'},
     {'author': 'Una',
      'channel': 'Una',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=wRrnU1fw7P0&t=98s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Una absolutely uh in fact one of the most common misconceptions is that gpos '
              "are only for for small businesses and that's not the case at all um we in fact.",
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': 'Una absolutely uh in fact one of the most common misconceptions is that gpos are '
             "only for for small businesses and that's not the case at all um we in fact.",
      'title': 'GPO FAQ: Understanding Group Purchasing Organizations (Una)',
      'url': 'https://www.youtube.com/watch?v=wRrnU1fw7P0&t=98s',
      'video_id': 'wRrnU1fw7P0'},
     {'author': 'GNB MENTOR',
      'channel': 'GNB MENTOR',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=1P1PwU7EeD8&t=15s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'कैसे बनना है। लास्ट वाली वीडियो में हमने रिसेलर बनने की जो वीडियो बनाई थी उसमें '
              'हमने पार्टनर प्रोफाइल बनाना सीखा था और पार्टनर प्रोफाइल की हम स्टेज पर पहुंचे.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'कैसे बनना है। लास्ट वाली वीडियो में हमने रिसेलर बनने की जो वीडियो बनाई थी उसमें '
             'हमने पार्टनर प्रोफाइल बनाना सीखा था और पार्टनर प्रोफाइल की हम स्टेज पर पहुंचे.',
      'title': 'Become a Google Workspace Reseller Partner in Asia Pacific and United States '
               'Region Part 2 (GNB MENTOR)',
      'url': 'https://www.youtube.com/watch?v=1P1PwU7EeD8&t=15s',
      'video_id': '1P1PwU7EeD8'}],
 6: [{'author': 'Money Machine',
      'channel': 'Money Machine',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:04](https://www.youtube.com/watch?v=cjmKIrc6hgE&t=124s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You are given a list of 250 names and phone numbers every morning. You are '
              'given a software called a dialer, which auto dials the next number the second '
              'your previous call ends. The first week you are terrified of the phone.',
      'timestamp': 124,
      'timestamp_label': '[00:02:04]',
      'timestamp_seconds': 124,
      'tip': 'You are given a list of 250 names and phone numbers every morning. You are given '
             'a software called a dialer, which auto dials the next number the second your '
             'previous call ends. The first week you are terrified of the phone.',
      'title': 'Your Life as Every Level of a SaaS Sales Rep — From SDR to VP (Money Machine)',
      'url': 'https://www.youtube.com/watch?v=cjmKIrc6hgE&t=124s',
      'video_id': 'cjmKIrc6hgE'},
     {'author': 'CloudEagle',
      'channel': 'CloudEagle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:34](https://www.youtube.com/watch?v=M0ICfl_2HyY&t=94s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's dig into the first step, building an inventory. How do you suggest people "
              'start? Begin with accounting records every expense line for software, no matter '
              'how small. Then cross-check with your IT admin list and look for any apps '
              'employees install on their own.',
      'timestamp': 94,
      'timestamp_label': '[00:01:34]',
      'timestamp_seconds': 94,
      'tip': "Let's dig into the first step, building an inventory. How do you suggest people "
             'start? Begin with accounting records every expense line for software, no matter '
             'how small. Then cross-check with your IT admin list and look for any apps '
             'employees install on their own.',
      'title': 'How to Run a SaaS Audit and Cut Unused Tools Before Renewal (CloudEagle)',
      'url': 'https://www.youtube.com/watch?v=M0ICfl_2HyY&t=94s',
      'video_id': 'M0ICfl_2HyY'},
     {'author': 'SoftwareOne Platform',
      'channel': 'SoftwareOne Platform',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=nnAd6F22fiw&t=40s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Go to marketplace then agreements and select the agreement you need. Open the '
              'subscriptions tab and check the current auto-renewal status for each '
              "subscription. When you're ready select configure. In the configure flow first "
              'select the renewal option.',
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': 'Go to marketplace then agreements and select the agreement you need. Open the '
             'subscriptions tab and check the current auto-renewal status for each '
             "subscription. When you're ready select configure. In the configure flow first "
             'select the renewal option.',
      'title': 'Configure Auto-renewal (SoftwareOne Platform)',
      'url': 'https://www.youtube.com/watch?v=nnAd6F22fiw&t=40s',
      'video_id': 'nnAd6F22fiw'},
     {'author': 'Sell Better',
      'channel': 'Sell Better',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=m2z1tgfv8Kc&t=45s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "There's a few things that actually might surprise you. Number one is top "
              'performers deal with call reluctance. So they get scared to pick up the phone '
              'as well. Number two is they speak more than the prospect.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': "There's a few things that actually might surprise you. Number one is top "
             'performers deal with call reluctance. So they get scared to pick up the phone as '
             'well. Number two is they speak more than the prospect.',
      'title': 'Full 18-Minute Cold Calling Course (For SaaS Sales) (Sell Better)',
      'url': 'https://www.youtube.com/watch?v=m2z1tgfv8Kc&t=45s',
      'video_id': 'm2z1tgfv8Kc'},
     {'author': 'Pax8',
      'channel': 'Pax8',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:35](https://www.youtube.com/watch?v=TxvzhnvDnxA&t=1475s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "There's one that always sticks in my mind and that is uh we were showing "
              "someone the data for the first time and he had come to me and he said uh let's "
              'look at this one law firm. He wanted to look at a client.',
      'timestamp': 1475,
      'timestamp_label': '[00:24:35]',
      'timestamp_seconds': 1475,
      'tip': "There's one that always sticks in my mind and that is uh we were showing someone "
             "the data for the first time and he had come to me and he said uh let's look at "
             'this one law firm. He wanted to look at a client.',
      'title': 'From Data to Dollars: Using the Portfolio Approach to Improve Margins in Your '
               'MSP | Pax8 (Pax8)',
      'url': 'https://www.youtube.com/watch?v=TxvzhnvDnxA&t=1475s',
      'video_id': 'TxvzhnvDnxA'},
     {'author': 'GrowthSpree - AI Native B2B Marketing Agency',
      'channel': 'GrowthSpree - AI Native B2B Marketing Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=2dLvgvK0qCY&t=38s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '6:1, and ramp time, which sets first year ROI. Median SDR 11 meetings booked, '
              '7. 5 attended, six SQLs, 48,000 pipeline, 68% attainment, four-month ramp. '
              'Inbound heavy SDRs book 14 to 18, outbound heavy six to 10. About 85 activities '
              'a day per 11 meetings.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': '6:1, and ramp time, which sets first year ROI. Median SDR 11 meetings booked, 7. '
             '5 attended, six SQLs, 48,000 pipeline, 68% attainment, four-month ramp. Inbound '
             'heavy SDRs book 14 to 18, outbound heavy six to 10. About 85 activities a day '
             'per 11 meetings.',
      'title': 'B2B SaaS Sales Quota Benchmarks 2026: SDR Meetings, AE Quota, OTE, Ratios '
               '(GrowthSpree - AI Native B2B Marketing Agency)',
      'url': 'https://www.youtube.com/watch?v=2dLvgvK0qCY&t=38s',
      'video_id': '2dLvgvK0qCY'},
     {'author': 'CX without the BS',
      'channel': 'CX without the BS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:39](https://www.youtube.com/watch?v=DKzL7oMyWis&t=99s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But then you go to Trustpilot, where the people who actually use the phones '
              "every single day and deal with billing leave reviews. It's a lot of zeros "
              "Speaker: And the BBB, the Better Business Bureau, it's even worse. 00:02:00] "
              'They give a roughly 1.',
      'timestamp': 99,
      'timestamp_label': '[00:01:39]',
      'timestamp_seconds': 99,
      'tip': 'But then you go to Trustpilot, where the people who actually use the phones '
             "every single day and deal with billing leave reviews. It's a lot of zeros "
             "Speaker: And the BBB, the Better Business Bureau, it's even worse. 00:02:00] "
             'They give a roughly 1.',
      'title': 'Gartner UCaaS Magic Quadrant 2026 EXPLAINED (Cisco, Microsoft, RingCentral, '
               'Zoom) (CX without the BS)',
      'url': 'https://www.youtube.com/watch?v=DKzL7oMyWis&t=99s',
      'video_id': 'DKzL7oMyWis'},
     {'author': 'Inside Microsoft AI Cloud Partner Program',
      'channel': 'Inside Microsoft AI Cloud Partner Program',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:51](https://www.youtube.com/watch?v=jcYTmMdEGPo&t=171s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, the first strategic accelerator is tier one, Microsoft 365 business '
              'premium, E3, Copilot business, M365 business and Copilot business bundles, '
              'Defender suite, Purview suite, Defender suite for business premium, and Purview '
              'suite for business premium.',
      'timestamp': 171,
      'timestamp_label': '[00:02:51]',
      'timestamp_seconds': 171,
      'tip': 'So, the first strategic accelerator is tier one, Microsoft 365 business premium, '
             'E3, Copilot business, M365 business and Copilot business bundles, Defender '
             'suite, Purview suite, Defender suite for business premium, and Purview suite for '
             'business premium.',
      'title': 'How to Enroll in Microsoft Commerce Incentives (MCI) | Every CSP Partner '
               'Should Know This (Inside Microsoft AI Cloud Partner Program)',
      'url': 'https://www.youtube.com/watch?v=jcYTmMdEGPo&t=171s',
      'video_id': 'jcYTmMdEGPo'},
     {'author': 'Benny Rossaer',
      'channel': 'Benny Rossaer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:41:19](https://www.youtube.com/watch?v=XVyGRE_S-vY&t=6079s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Eh Defender for Office 365 om uw hyperlinks en uw bijlage te gaan beveiligen. '
              'Defender for Business is een volledig antivirus met EDR. Intune naar device '
              'management. Azure information protection kan je data gaan labelen. Kan ook naar '
              'koop toe interessant zijn.',
      'timestamp': 6079,
      'timestamp_label': '[01:41:19]',
      'timestamp_seconds': 6079,
      'tip': 'Eh Defender for Office 365 om uw hyperlinks en uw bijlage te gaan beveiligen. '
             'Defender for Business is een volledig antivirus met EDR. Intune naar device '
             'management. Azure information protection kan je data gaan labelen. Kan ook naar '
             'koop toe interessant zijn.',
      'title': 'Smartworx webinar: Microsoft CSP - Partner Center - MAICPP - Microsoft 365 & '
               'Azure commercial basics (Benny Rossaer)',
      'url': 'https://www.youtube.com/watch?v=XVyGRE_S-vY&t=6079s',
      'video_id': 'XVyGRE_S-vY'},
     {'author': 'AppOmni',
      'channel': 'AppOmni',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=EEuTZMr-lgI&t=64s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'll take a look at the downloads and upload columns. Moving a lot of data can "
              'point to file transfers, exports, or users working with sensitive information '
              'in environments outside company control. Nexttop AI stands out at the top of '
              'our list.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': "I'll take a look at the downloads and upload columns. Moving a lot of data can "
             'point to file transfers, exports, or users working with sensitive information in '
             'environments outside company control. Nexttop AI stands out at the top of our '
             'list.',
      'title': 'Shadow IT SaaS Usage: Discover and Assess Your Risk (AppOmni)',
      'url': 'https://www.youtube.com/watch?v=EEuTZMr-lgI&t=64s',
      'video_id': 'EEuTZMr-lgI'},
     {'author': 'usecure',
      'channel': 'usecure',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:06](https://www.youtube.com/watch?v=oQIMe7F_kaw&t=726s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I know we're all busy, but you know, you could jump from one solution to "
              "another and find pitfalls that you didn't didn't look at properly. You know, so "
              'the single search solutions is sometimes you think, oh, I need the integration.',
      'timestamp': 726,
      'timestamp_label': '[00:12:06]',
      'timestamp_seconds': 726,
      'tip': "I know we're all busy, but you know, you could jump from one solution to another "
             "and find pitfalls that you didn't didn't look at properly. You know, so the "
             'single search solutions is sometimes you think, oh, I need the integration.',
      'title': 'From £2 Add-On to a Service Clients Understand: Lessons From Pax8 (usecure)',
      'url': 'https://www.youtube.com/watch?v=oQIMe7F_kaw&t=726s',
      'video_id': 'oQIMe7F_kaw'},
     {'author': 'Technical Support Online',
      'channel': 'Technical Support Online',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:46](https://www.youtube.com/watch?v=tlmDeX5UBJs&t=286s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Reseller program so you can choose the rough I select the first one for '
              'Microsoft partner program and select next I want to be authorized first upload '
              'Network then I will be authorized reseller so I provide my information and '
              'search.',
      'timestamp': 286,
      'timestamp_label': '[00:04:46]',
      'timestamp_seconds': 286,
      'tip': 'Reseller program so you can choose the rough I select the first one for '
             'Microsoft partner program and select next I want to be authorized first upload '
             'Network then I will be authorized reseller so I provide my information and '
             'search.',
      'title': 'I will help to join the Microsoft Partner Program | Join the Microsoft AI '
               'Cloud Partner Program (Technical Support Online)',
      'url': 'https://www.youtube.com/watch?v=tlmDeX5UBJs&t=286s',
      'video_id': 'tlmDeX5UBJs'},
     {'author': 'Tattooed Nerd',
      'channel': 'Tattooed Nerd',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:31](https://www.youtube.com/watch?v=CHFSW3MiXcU&t=1411s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Shared on a screen shared on a whiteboard shared in a chat shared in a direct '
              'message the list goes on and on data lake is able to capture that and.',
      'timestamp': 1411,
      'timestamp_label': '[00:23:31]',
      'timestamp_seconds': 1411,
      'tip': 'Shared on a screen shared on a whiteboard shared in a chat shared in a direct '
             'message the list goes on and on data lake is able to capture that and.',
      'title': 'Is your Zoom compliance actually secure? (Tattooed Nerd)',
      'url': 'https://www.youtube.com/watch?v=CHFSW3MiXcU&t=1411s',
      'video_id': 'CHFSW3MiXcU'},
     {'author': 'Marcus Harris Software & Tech Attorney',
      'channel': 'Marcus Harris Software & Tech Attorney',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=PQUXMXjSfjw&t=68s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I think one of the first caps that we will typically see is that in order to be '
              'able to take advantage of the price cap, the new purchase needs to be subject '
              'to a certain volume. And you know that volume can be whatever you negotiate.',
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': 'I think one of the first caps that we will typically see is that in order to be '
             'able to take advantage of the price cap, the new purchase needs to be subject to '
             'a certain volume. And you know that volume can be whatever you negotiate.',
      'title': 'Renewing SaaS Contracts? Don’t Fall for These Common Traps! (Marcus Harris '
               'Software & Tech Attorney)',
      'url': 'https://www.youtube.com/watch?v=PQUXMXjSfjw&t=68s',
      'video_id': 'PQUXMXjSfjw'},
     {'author': 'The Negotiator Guru',
      'channel': 'The Negotiator Guru',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:00](https://www.youtube.com/watch?v=dOTg4A37x5g&t=240s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you're not doing that you're not going to leave yourself enough time the "
              'real negotiation happens about happens about three months prior to the renewal '
              "date this all has to do with salesforce's playbook and how they play into their "
              'renewal.',
      'timestamp': 240,
      'timestamp_label': '[00:04:00]',
      'timestamp_seconds': 240,
      'tip': "If you're not doing that you're not going to leave yourself enough time the real "
             'negotiation happens about happens about three months prior to the renewal date '
             "this all has to do with salesforce's playbook and how they play into their "
             'renewal.',
      'title': 'Salesforce Renewal - Top Negotiation Tips (The Negotiator Guru)',
      'url': 'https://www.youtube.com/watch?v=dOTg4A37x5g&t=240s',
      'video_id': 'dOTg4A37x5g'}],
 7: [{'author': 'Microsoft Events',
      'channel': 'Microsoft Events',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:35:34](https://www.youtube.com/watch?v=z4JbWkKJagI&t=2134s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Microsoft 365 copilot specialization proves delivery capability through an '
              'audit, and then the Frontier Partner specialization is a further step towards '
              'delivering Agentic work at scale. Run the method on one piece of work in your '
              'own business.',
      'timestamp': 2134,
      'timestamp_label': '[00:35:34]',
      'timestamp_seconds': 2134,
      'tip': 'Microsoft 365 copilot specialization proves delivery capability through an '
             'audit, and then the Frontier Partner specialization is a further step towards '
             'delivering Agentic work at scale. Run the method on one piece of work in your '
             'own business.',
      'title': 'Build the managed intelligence stack for SMBs with Pax8 and Microsoft | '
               'BRKSP590 (Microsoft Events)',
      'url': 'https://www.youtube.com/watch?v=z4JbWkKJagI&t=2134s',
      'video_id': 'z4JbWkKJagI'},
     {'author': 'Tech Meets East',
      'channel': 'Tech Meets East',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:00](https://www.youtube.com/watch?v=xCgcup4z6CI&t=1200s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Adobe is going all in on artificial intelligence agents. Its creative agent, a '
              'system that takes a plain language request and carries out the steps for you, '
              'is expanding into Illustrator, Premiere, InDesign, After Effects, and frame.',
      'timestamp': 1200,
      'timestamp_label': '[00:20:00]',
      'timestamp_seconds': 1200,
      'tip': 'Adobe is going all in on artificial intelligence agents. Its creative agent, a '
             'system that takes a plain language request and carries out the steps for you, is '
             'expanding into Illustrator, Premiere, InDesign, After Effects, and frame.',
      'title': 'Adobe Is Losing Everything: Photoshop, Illustrator & Premiere on the Brink '
               '(Tech Meets East)',
      'url': 'https://www.youtube.com/watch?v=xCgcup4z6CI&t=1200s',
      'video_id': 'xCgcup4z6CI'},
     {'author': 'Sub-Zero To Wealth',
      'channel': 'Sub-Zero To Wealth',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=VP4hPTXkPIs&t=91s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "All right, let's walk through the step-by-step process of how to become a "
              'Microsoft partner. Step one is to create a business account, which is also '
              'known as a Microsoft Azure tenant, or what you might have known as Azure Active '
              'Directory.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': "All right, let's walk through the step-by-step process of how to become a "
             'Microsoft partner. Step one is to create a business account, which is also known '
             'as a Microsoft Azure tenant, or what you might have known as Azure Active '
             'Directory.',
      'title': '✅Affiliate Series Guide 1| Become a Microsoft Partner in 2026| Sell Microsoft '
               'Products & Solutions (Sub-Zero To Wealth)',
      'url': 'https://www.youtube.com/watch?v=VP4hPTXkPIs&t=91s',
      'video_id': 'VP4hPTXkPIs'},
     {'author': 'Technical Support Online',
      'channel': 'Technical Support Online',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:50](https://www.youtube.com/watch?v=wjgyQO9jIAM&t=290s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Complete here is the sum step to complete your Microsoft for LPN ID so this is '
              'the verification process uh by entering this step you need to submit your '
              'documents for company documents uh that Microsoft can check it and verify on '
              'your portal foreign ID.',
      'timestamp': 290,
      'timestamp_label': '[00:04:50]',
      'timestamp_seconds': 290,
      'tip': 'Complete here is the sum step to complete your Microsoft for LPN ID so this is '
             'the verification process uh by entering this step you need to submit your '
             'documents for company documents uh that Microsoft can check it and verify on '
             'your portal foreign ID.',
      'title': 'Microsoft Partner Center: How to Setup Your Company Profile Correctly '
               '(Technical Support Online)',
      'url': 'https://www.youtube.com/watch?v=wjgyQO9jIAM&t=290s',
      'video_id': 'wjgyQO9jIAM'},
     {'author': 'Yusuf Young',
      'channel': 'Yusuf Young',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=O6H36x0A6_g&t=65s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm gonna take this in five steps and stay for step five because most people "
              'who have HubSpot skip it and it decides if you should even renew at all. Step '
              'one, switch off auto-renew today.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': "I'm gonna take this in five steps and stay for step five because most people who "
             'have HubSpot skip it and it decides if you should even renew at all. Step one, '
             'switch off auto-renew today.',
      'title': 'HubSpot Renewal: $5,000 for Empty Seats. 5 Steps to Avoid It (Yusuf Young)',
      'url': 'https://www.youtube.com/watch?v=O6H36x0A6_g&t=65s',
      'video_id': 'O6H36x0A6_g'},
     {'author': 'AeroCom Inc',
      'channel': 'AeroCom Inc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:47](https://www.youtube.com/watch?v=auYElw4sYi8&t=227s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You can't have a lot of customers or be doing a good job if you have bad call "
              'quality. So, their call quality has been great. Their uptime is also great. And '
              'they actually list their uptime statistics right here on their website.',
      'timestamp': 227,
      'timestamp_label': '[00:03:47]',
      'timestamp_seconds': 227,
      'tip': "You can't have a lot of customers or be doing a good job if you have bad call "
             'quality. So, their call quality has been great. Their uptime is also great. And '
             'they actually list their uptime statistics right here on their website.',
      'title': 'Zoom Phone System (UCaaS) Review & Demo | Hard to Beat (AeroCom Inc)',
      'url': 'https://www.youtube.com/watch?v=auYElw4sYi8&t=227s',
      'video_id': 'auYElw4sYi8'},
     {'author': 'Tropic',
      'channel': 'Tropic',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:31](https://www.youtube.com/watch?v=veu6EUBTdBE&t=151s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'These become useful later on. Step four, run your discovery call strategically. '
              'Your goal here is to understand their position before revealing yours. Start by '
              "asking them to walk through your current agreement. What's changing, what's "
              'staying, and request any missing data.',
      'timestamp': 151,
      'timestamp_label': '[00:02:31]',
      'timestamp_seconds': 151,
      'tip': 'These become useful later on. Step four, run your discovery call strategically. '
             'Your goal here is to understand their position before revealing yours. Start by '
             "asking them to walk through your current agreement. What's changing, what's "
             'staying, and request any missing data.',
      'title': '6 Steps to Win Every Software Negotiation (Tropic)',
      'url': 'https://www.youtube.com/watch?v=veu6EUBTdBE&t=151s',
      'video_id': 'veu6EUBTdBE'},
     {'author': 'Horror FM',
      'channel': 'Horror FM',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:20](https://www.youtube.com/watch?v=jUFbUlIkcm0&t=320s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Paper ship now select the settings icon and account settings check the legal '
              "info and you can see here the partner tab is coming here but uh it's showing "
              'for pending so there are some option to complete to complete the process or '
              'verify your account.',
      'timestamp': 320,
      'timestamp_label': '[00:05:20]',
      'timestamp_seconds': 320,
      'tip': 'Paper ship now select the settings icon and account settings check the legal '
             "info and you can see here the partner tab is coming here but uh it's showing for "
             'pending so there are some option to complete to complete the process or verify '
             'your account.',
      'title': 'Create Microsoft Partner account | Microsoft Partner Center | Partner MPN '
               'account setup | MPN | CSP (Horror FM)',
      'url': 'https://www.youtube.com/watch?v=jUFbUlIkcm0&t=320s',
      'video_id': 'jUFbUlIkcm0'},
     {'author': 'HowTo With Glen',
      'channel': 'HowTo With Glen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=o7bsmkpf6kA&t=51s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re a small business or just getting started. Google uses this to verify that "
              "you're a legitimate business and not just an individual signing up casually.",
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': "'re a small business or just getting started. Google uses this to verify that "
             "you're a legitimate business and not just an individual signing up casually.",
      'title': 'How to Become a Google Workspace Reseller (Complete Guide) (HowTo With Glen)',
      'url': 'https://www.youtube.com/watch?v=o7bsmkpf6kA&t=51s',
      'video_id': 'o7bsmkpf6kA'},
     {'author': 'Synergy Advisors LLC',
      'channel': 'Synergy Advisors LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:09](https://www.youtube.com/watch?v=KNnxTcJ4cEE&t=129s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Association while achieving your business objectives with Synergy advisors and '
              'Microsoft contact your Synergy advisors sales representative or email us at '
              "wwpnpm at synergyadvisors.biz to receive more information on this process let's "
              'keep making Synergy together.',
      'timestamp': 129,
      'timestamp_label': '[00:02:09]',
      'timestamp_seconds': 129,
      'tip': 'Association while achieving your business objectives with Synergy advisors and '
             'Microsoft contact your Synergy advisors sales representative or email us at '
             "wwpnpm at synergyadvisors.biz to receive more information on this process let's "
             'keep making Synergy together.',
      'title': 'Create a customer association via the Claiming Partner of Record [CPOR] '
               '(Synergy Advisors LLC)',
      'url': 'https://www.youtube.com/watch?v=KNnxTcJ4cEE&t=129s',
      'video_id': 'KNnxTcJ4cEE'},
     {'author': 'Pax8',
      'channel': 'Pax8',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:19](https://www.youtube.com/watch?v=_98wIAhek0M&t=1099s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um so when I think about go to market that concept of go to market is not a '
              "campaign, it's an operating system really resonates with me because we are we "
              'are talking about go to market being the full service delivery chain.',
      'timestamp': 1099,
      'timestamp_label': '[00:18:19]',
      'timestamp_seconds': 1099,
      'tip': 'Um so when I think about go to market that concept of go to market is not a '
             "campaign, it's an operating system really resonates with me because we are we "
             'are talking about go to market being the full service delivery chain.',
      'title': 'How MSPs Can Turn Strategy into Real Business Results | Pax8 (Pax8)',
      'url': 'https://www.youtube.com/watch?v=_98wIAhek0M&t=1099s',
      'video_id': '_98wIAhek0M'},
     {'author': 'SoftwareOne Benelux',
      'channel': 'SoftwareOne Benelux',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=6-M7SxMm3Yc&t=111s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Get a better overview and click on place order in this step the migration order '
              'is processing the status of the migration order will out automatically change '
              'to complete it once you refresh the page you can now view your order or close '
              'the window.',
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': 'Get a better overview and click on place order in this step the migration order '
             'is processing the status of the migration order will out automatically change to '
             'complete it once you refresh the page you can now view your order or close the '
             'window.',
      'title': 'Migrate Adobe VIP to Client Portal Marketplace (SoftwareOne Benelux)',
      'url': 'https://www.youtube.com/watch?v=6-M7SxMm3Yc&t=111s',
      'video_id': '6-M7SxMm3Yc'},
     {'author': 'InboxKit',
      'channel': 'InboxKit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:39](https://www.youtube.com/watch?v=0Vk8NzIt_RM&t=99s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "In my case, it's going to be this. After that, I'll just put my email to get a "
              'Google official to reach out to me for this specific query. I the mode of '
              "communication to be phone because it's much faster and I got this phone call "
              'within a few hours post submitting this form.',
      'timestamp': 99,
      'timestamp_label': '[00:01:39]',
      'timestamp_seconds': 99,
      'tip': "In my case, it's going to be this. After that, I'll just put my email to get a "
             'Google official to reach out to me for this specific query. I the mode of '
             "communication to be phone because it's much faster and I got this phone call "
             'within a few hours post submitting this form.',
      'title': 'How to Check if Your Google Workspace Reseller is Legit (InboxKit)',
      'url': 'https://www.youtube.com/watch?v=0Vk8NzIt_RM&t=99s',
      'video_id': '0Vk8NzIt_RM'},
     {'author': 'UC Today News',
      'channel': 'UC Today News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:27](https://www.youtube.com/watch?v=YnbZO1fa7BQ&t=507s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Discovery process to hear and listen to our partners our customers to make sure '
              "that we're aligning them with what is going to be best long.",
      'timestamp': 507,
      'timestamp_label': '[00:08:27]',
      'timestamp_seconds': 507,
      'tip': 'Discovery process to hear and listen to our partners our customers to make sure '
             "that we're aligning them with what is going to be best long.",
      'title': 'AI Disruption in UC: Copilot, Zoom & Webex Face Off (UC Today News)',
      'url': 'https://www.youtube.com/watch?v=YnbZO1fa7BQ&t=507s',
      'video_id': 'YnbZO1fa7BQ'},
     {'author': 'GSG',
      'channel': 'GSG',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=Fgb-rjcpBI8&t=15s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '법학 버스 밖 베어버릴 원하고 않으세요 비유 2 ij 엄마보고 싸움 키바 프 트 채 오스템 넣어 제 2의 아스트로 나오지 서비스 이를 부득.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': '법학 버스 밖 베어버릴 원하고 않으세요 비유 2 ij 엄마보고 싸움 키바 프 트 채 오스템 넣어 제 2의 아스트로 나오지 서비스 이를 부득.',
      'title': 'Mobility 101: Telecom Expense Management, or TEM (GSG)',
      'url': 'https://www.youtube.com/watch?v=Fgb-rjcpBI8&t=15s',
      'video_id': 'Fgb-rjcpBI8'}],
 8: [{'author': 'SAP Concur',
      'channel': 'SAP Concur',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:32](https://www.youtube.com/watch?v=ARjBgExQ3oQ&t=512s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Every year we put out what we call the SaaS Management Index. It's an annual "
              "report that we produce that's looking at holistically SaaS data that's coming "
              'into the Zylo platform.',
      'timestamp': 512,
      'timestamp_label': '[00:08:32]',
      'timestamp_seconds': 512,
      'tip': "Every year we put out what we call the SaaS Management Index. It's an annual "
             "report that we produce that's looking at holistically SaaS data that's coming "
             'into the Zylo platform.',
      'title': 'Zylo Overview: Saas Optimization (SAP Concur)',
      'url': 'https://www.youtube.com/watch?v=ARjBgExQ3oQ&t=512s',
      'video_id': 'ARjBgExQ3oQ'},
     {'author': 'fynk',
      'channel': 'fynk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=QLqtDhk3PoI&t=54s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Build one list of every software contract. Go through the invoices and company '
              'card charges, check what IT knows about, and ask the team leads. For each tool, '
              'note the team, an owner, a backup, and where the contract lives. Watch for '
              'tools whose buyer has left the company.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'Build one list of every software contract. Go through the invoices and company '
             'card charges, check what IT knows about, and ask the team leads. For each tool, '
             'note the team, an owner, a backup, and where the contract lives. Watch for tools '
             'whose buyer has left the company.',
      'title': 'SaaS renewal management: a renewal strategy to stop paying for unused software '
               '(fynk)',
      'url': 'https://www.youtube.com/watch?v=QLqtDhk3PoI&t=54s',
      'video_id': 'QLqtDhk3PoI'},
     {'author': 'MetrixData 360',
      'channel': 'MetrixData 360',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:00](https://www.youtube.com/watch?v=lB5ThkY4hMA&t=1320s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But the tools themselves are not the answer, right? You have to dive into the '
              "data. So, if a tool's just aggregating data or making data easier to uh make "
              "decisions on, that's what the tools do. They're not going to give you the data.",
      'timestamp': 1320,
      'timestamp_label': '[00:22:00]',
      'timestamp_seconds': 1320,
      'tip': 'But the tools themselves are not the answer, right? You have to dive into the '
             "data. So, if a tool's just aggregating data or making data easier to uh make "
             "decisions on, that's what the tools do. They're not going to give you the data.",
      'title': 'Shadow IT & SaaS Sprawl: Controlling the Hidden Software Costs Draining Your '
               'Budget (MetrixData 360)',
      'url': 'https://www.youtube.com/watch?v=lB5ThkY4hMA&t=1320s',
      'video_id': 'lB5ThkY4hMA'},
     {'author': 'AppXite',
      'channel': 'AppXite',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:20](https://www.youtube.com/watch?v=GDHnAQ3r53A&t=620s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Changes and say no I don't need eight extra I need only five extra licenses on "
              'the renewal date and apply the change contact us to discuss your Adobe business '
              'case and how we can support it in the Epic site platform.',
      'timestamp': 620,
      'timestamp_label': '[00:10:20]',
      'timestamp_seconds': 620,
      'tip': "Changes and say no I don't need eight extra I need only five extra licenses on "
             'the renewal date and apply the change contact us to discuss your Adobe business '
             'case and how we can support it in the Epic site platform.',
      'title': 'How to Scale and Automate Your Adobe VIP Marketplace Business with AppXite '
               '(Program Overview & Demo) (AppXite)',
      'url': 'https://www.youtube.com/watch?v=GDHnAQ3r53A&t=620s',
      'video_id': 'GDHnAQ3r53A'},
     {'author': 'Provision Networks',
      'channel': 'Provision Networks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:13](https://www.youtube.com/watch?v=Q3VZHAsymcg&t=193s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Yeah, it completely bypasses all corporate quality control. But by connecting '
              'expense tracking directly to SSO data, tools like Provision Networks flag those '
              'unauthorized credit card swipes immediately. Bringing rogue spending back into '
              'the light.',
      'timestamp': 193,
      'timestamp_label': '[00:03:13]',
      'timestamp_seconds': 193,
      'tip': 'Yeah, it completely bypasses all corporate quality control. But by connecting '
             'expense tracking directly to SSO data, tools like Provision Networks flag those '
             'unauthorized credit card swipes immediately. Bringing rogue spending back into '
             'the light.',
      'title': '**The Hidden IT Tax: 5 Surprising Ways Your SaaS Stack Is Wasting Money** '
               '(Provision Networks)',
      'url': 'https://www.youtube.com/watch?v=Q3VZHAsymcg&t=193s',
      'video_id': 'Q3VZHAsymcg'},
     {'author': 'Willingness to Pay',
      'channel': 'Willingness to Pay',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=rTGrwbYBlXg&t=35s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Infrastructure related software sold per API call or per CPU usage or and so '
              'forth so picking a good metric is usually a core component of attaining pricing '
              'Market fit so I wanted to in this short.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'Infrastructure related software sold per API call or per CPU usage or and so '
             'forth so picking a good metric is usually a core component of attaining pricing '
             'Market fit so I wanted to in this short.',
      'title': 'SaaS Pricing Metrics Explained: Operational Viability (Willingness to Pay)',
      'url': 'https://www.youtube.com/watch?v=rTGrwbYBlXg&t=35s',
      'video_id': 'rTGrwbYBlXg'},
     {'author': 'Microsoft Helps',
      'channel': 'Microsoft Helps',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:16](https://www.youtube.com/watch?v=9Q30FhN41LI&t=76s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's an evolving platform where additional features are being added constantly "
              'to help CSP partners to improve customer experience. As a CSP partner you can '
              'use partner Center to manage your partner organization and your end customer '
              'service end to end.',
      'timestamp': 76,
      'timestamp_label': '[00:01:16]',
      'timestamp_seconds': 76,
      'tip': "It's an evolving platform where additional features are being added constantly "
             'to help CSP partners to improve customer experience. As a CSP partner you can '
             'use partner Center to manage your partner organization and your end customer '
             'service end to end.',
      'title': 'Overview of Microsoft Partner Center Portal, new features, & common scenario '
               'discussion | Microsoft (Microsoft Helps)',
      'url': 'https://www.youtube.com/watch?v=9Q30FhN41LI&t=76s',
      'video_id': '9Q30FhN41LI'},
     {'author': 'Tattooed Nerd',
      'channel': 'Tattooed Nerd',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:22](https://www.youtube.com/watch?v=pW6NJcmH21E&t=262s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The ability to use analytics and research and all the dashboard for reporting '
              'to make your sales force better, to use the tools of Zoom One and Zoom Phone to '
              'sell more using the data that you collect from Zoom IQ.',
      'timestamp': 262,
      'timestamp_label': '[00:04:22]',
      'timestamp_seconds': 262,
      'tip': 'The ability to use analytics and research and all the dashboard for reporting to '
             'make your sales force better, to use the tools of Zoom One and Zoom Phone to '
             'sell more using the data that you collect from Zoom IQ.',
      'title': 'Is Zoom the best UCaaS Platform? (Tattooed Nerd)',
      'url': 'https://www.youtube.com/watch?v=pW6NJcmH21E&t=262s',
      'video_id': 'pW6NJcmH21E'},
     {'author': 'IWI Consulting Group',
      'channel': 'IWI Consulting Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:18](https://www.youtube.com/watch?v=s-VGS7d821o&t=138s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s what's posted in the general ledger with statistical accounts, which is what "
              "allows you to see the best of the 6 C's of cloud finance tracking metrics. And "
              'you can see all this data and all posts in the contract, so you can track it '
              'all synced back into the salesforce.',
      'timestamp': 138,
      'timestamp_label': '[00:02:18]',
      'timestamp_seconds': 138,
      'tip': "'s what's posted in the general ledger with statistical accounts, which is what "
             "allows you to see the best of the 6 C's of cloud finance tracking metrics. And "
             'you can see all this data and all posts in the contract, so you can track it all '
             'synced back into the salesforce.',
      'title': 'Sage Intacct Subscription Billing | SaaS Revenue & Reporting (IWI Consulting '
               'Group)',
      'url': 'https://www.youtube.com/watch?v=s-VGS7d821o&t=138s',
      'video_id': 's-VGS7d821o'},
     {'author': 'Marcus Harris Software & Tech Attorney',
      'channel': 'Marcus Harris Software & Tech Attorney',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:08](https://www.youtube.com/watch?v=2XJmAjfVmQw&t=128s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s, you know, business intelligence, databases, but then have to execute an "
              'additional contract with a thirdparty vendor to be able to use that software.',
      'timestamp': 128,
      'timestamp_label': '[00:02:08]',
      'timestamp_seconds': 128,
      'tip': "'s, you know, business intelligence, databases, but then have to execute an "
             'additional contract with a thirdparty vendor to be able to use that software.',
      'title': 'Key Negotiation Points in SaaS Contracts (Marcus Harris Software & Tech '
               'Attorney)',
      'url': 'https://www.youtube.com/watch?v=2XJmAjfVmQw&t=128s',
      'video_id': '2XJmAjfVmQw'},
     {'author': 'Una',
      'channel': 'Una',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=vXeviFgIR1I&t=31s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're paying on average is going to be between 18 to 22% however we will get "
              'you your specific numbers that we will be able to save you once we have our '
              'onboarding call and certainly dive into the data a little bit more but de '
              'definitely on average double digit.',
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': "You're paying on average is going to be between 18 to 22% however we will get "
             'you your specific numbers that we will be able to save you once we have our '
             'onboarding call and certainly dive into the data a little bit more but de '
             'definitely on average double digit.',
      'title': "GPO FAQ: Evaluating a Group Purchasing Organization's Potential (Una)",
      'url': 'https://www.youtube.com/watch?v=vXeviFgIR1I&t=31s',
      'video_id': 'vXeviFgIR1I'},
     {'author': 'Luís Guzmán',
      'channel': 'Luís Guzmán',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:24](https://www.youtube.com/watch?v=OvtYYoCkO-w&t=24s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Months but you can also create extended agreements um which are more than 12 '
              "months in this case let's say for example we need to.",
      'timestamp': 24,
      'timestamp_label': '[00:00:24]',
      'timestamp_seconds': 24,
      'tip': 'Months but you can also create extended agreements um which are more than 12 '
             "months in this case let's say for example we need to.",
      'title': 'Reseller Console   Creating Extended VIP (Luís Guzmán)',
      'url': 'https://www.youtube.com/watch?v=OvtYYoCkO-w&t=24s',
      'video_id': 'OvtYYoCkO-w'},
     {'author': 'Sage Expense Management',
      'channel': 'Sage Expense Management',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=HJSf4yb3-CM&t=43s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s no need for manual data entry or reconciliation. Sage Expense Management "
              'also offers multiple ways to submit receipts through the mobile and web app or '
              'even via Gmail and Outlook plugins, making it easy for everyone.',
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': "'s no need for manual data entry or reconciliation. Sage Expense Management also "
             'offers multiple ways to submit receipts through the mobile and web app or even '
             'via Gmail and Outlook plugins, making it easy for everyone.',
      'title': 'Introducing Sage Expense Management (Sage Expense Management)',
      'url': 'https://www.youtube.com/watch?v=HJSf4yb3-CM&t=43s',
      'video_id': 'HJSf4yb3-CM'},
     {'author': 'Zylo | The Leader in Enterprise SaaS Management',
      'channel': 'Zylo | The Leader in Enterprise SaaS Management',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:12](https://www.youtube.com/watch?v=r6xTyjDAFrQ&t=132s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'How vendors are portraying their tool selling their tool things of that nature '
              'um and and those three things are definitely the three that stick out in my '
              'mind that make this the most challenging thing to manage and monitor on a daily '
              'basis.',
      'timestamp': 132,
      'timestamp_label': '[00:02:12]',
      'timestamp_seconds': 132,
      'tip': 'How vendors are portraying their tool selling their tool things of that nature '
             'um and and those three things are definitely the three that stick out in my mind '
             'that make this the most challenging thing to manage and monitor on a daily '
             'basis.',
      'title': '#Procurement Expert Shares His TOP 3 Challenges of #SaaS Contract Renewals '
               '(Zylo | The Leader in Enterprise SaaS Management)',
      'url': 'https://www.youtube.com/watch?v=r6xTyjDAFrQ&t=132s',
      'video_id': 'r6xTyjDAFrQ'},
     {'author': 'Tech Field Day Plus',
      'channel': 'Tech Field Day Plus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:13](https://www.youtube.com/watch?v=oB21xupXerM&t=973s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'World of IT so we will wrap it up here for our esteemed panelists for myself '
              'Tom Hollingsworth and the rest of the gestalt IT family thank you all very much '
              'for tuning in and we hope to see you again soon.',
      'timestamp': 973,
      'timestamp_label': '[00:16:13]',
      'timestamp_seconds': 973,
      'tip': 'World of IT so we will wrap it up here for our esteemed panelists for myself Tom '
             'Hollingsworth and the rest of the gestalt IT family thank you all very much for '
             'tuning in and we hope to see you again soon.',
      'title': 'VARs are Useless – The On-Premise IT Roundtable (Tech Field Day Plus)',
      'url': 'https://www.youtube.com/watch?v=oB21xupXerM&t=973s',
      'video_id': 'oB21xupXerM'}],
 9: [{'author': 'The Tech Compliance Blueprint',
      'channel': 'The Tech Compliance Blueprint',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=WiNczR6ugRY&t=92s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Every vendor agreement must include four non-negotiable clauses. Your contract '
              'must grant your team or third-party assessors the right to review annual '
              'security certifications and independent audit reports. Second, minimum security '
              'warranties.',
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': 'Every vendor agreement must include four non-negotiable clauses. Your contract '
             'must grant your team or third-party assessors the right to review annual '
             'security certifications and independent audit reports. Second, minimum security '
             'warranties.',
      'title': 'Vendor Risk Management: Auditing Your SaaS Vendors for Cyber Liability (The '
               'Tech Compliance Blueprint)',
      'url': 'https://www.youtube.com/watch?v=WiNczR6ugRY&t=92s',
      'video_id': 'WiNczR6ugRY'},
     {'author': 'Tropic',
      'channel': 'Tropic',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:14](https://www.youtube.com/watch?v=FESALIJcxS0&t=254s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Having the ability to audit and right-size usage is important to ensure that '
              "you're maintaining low costs. Ensure there are clear terms negotiated into your "
              'contract to provide protection from skyrocketing costs.',
      'timestamp': 254,
      'timestamp_label': '[00:04:14]',
      'timestamp_seconds': 254,
      'tip': 'Having the ability to audit and right-size usage is important to ensure that '
             "you're maintaining low costs. Ensure there are clear terms negotiated into your "
             'contract to provide protection from skyrocketing costs.',
      'title': 'What Most People Miss in Software and AI Contracts That Costs Them Thousands '
               '(Tropic)',
      'url': 'https://www.youtube.com/watch?v=FESALIJcxS0&t=254s',
      'video_id': 'FESALIJcxS0'},
     {'author': 'NinjaOne IT Tech Tips',
      'channel': 'NinjaOne IT Tech Tips',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=ORh7DquM3lY&t=139s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Security and compliance: identify unsanctioned shadow IT applications that may '
              "introduce audit exposure. Business value: if an application's ROI is unclear, "
              'evaluate consolidation or retirement.',
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': 'Security and compliance: identify unsanctioned shadow IT applications that may '
             "introduce audit exposure. Business value: if an application's ROI is unclear, "
             'evaluate consolidation or retirement.',
      'title': 'How to Build Recurring SaaS Review Cycles (NinjaOne IT Tech Tips)',
      'url': 'https://www.youtube.com/watch?v=ORh7DquM3lY&t=139s',
      'video_id': 'ORh7DquM3lY'},
     {'author': 'Rook Technology Consulting',
      'channel': 'Rook Technology Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=-uYS0eABgbk&t=108s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The annual option has a lower rate, but you generally can't reduce the "
              'committed license count until renewal. If your staffing drops after a busy '
              'season, model that change before choosing the plan. Check your reseller terms '
              "if that's how you buy.",
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': "The annual option has a lower rate, but you generally can't reduce the committed "
             'license count until renewal. If your staffing drops after a busy season, model '
             "that change before choosing the plan. Check your reseller terms if that's how "
             'you buy.',
      'title': 'Will Switching to Google Workspace Actually Save You Money? (Rook Technology '
               'Consulting)',
      'url': 'https://www.youtube.com/watch?v=-uYS0eABgbk&t=108s',
      'video_id': '-uYS0eABgbk'},
     {'author': 'Docusign',
      'channel': 'Docusign',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:26](https://www.youtube.com/watch?v=HlJxNYkv7AY&t=26s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Robin opens the Acme account record and selects the DocuSign Agreements tab '
              'powered by Agreement Manager. Robin instantly sees all active contracts linked '
              'to this account, complete with key fields like contract value, effective dates, '
              'and renewal notice periods.',
      'timestamp': 26,
      'timestamp_label': '[00:00:26]',
      'timestamp_seconds': 26,
      'tip': 'Robin opens the Acme account record and selects the DocuSign Agreements tab '
             'powered by Agreement Manager. Robin instantly sees all active contracts linked '
             'to this account, complete with key fields like contract value, effective dates, '
             'and renewal notice periods.',
      'title': 'Docusign IAM for Sales: Customer Renewal Management (Docusign)',
      'url': 'https://www.youtube.com/watch?v=HlJxNYkv7AY&t=26s',
      'video_id': 'HlJxNYkv7AY'},
     {'author': 'CloudEagle',
      'channel': 'CloudEagle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:33](https://www.youtube.com/watch?v=8klvxfhjzF4&t=333s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Second, matching the right license types to your business needs makes a massive '
              'difference in both cost and productivity. And third, setting up automation and '
              "regular audits isn't just a nice-to-have, it's essential for ongoing control "
              'and compliance.',
      'timestamp': 333,
      'timestamp_label': '[00:05:33]',
      'timestamp_seconds': 333,
      'tip': 'Second, matching the right license types to your business needs makes a massive '
             'difference in both cost and productivity. And third, setting up automation and '
             "regular audits isn't just a nice-to-have, it's essential for ongoing control and "
             'compliance.',
      'title': "How to Stop Renewing SaaS Licenses at Last Year's Count (CloudEagle)",
      'url': 'https://www.youtube.com/watch?v=8klvxfhjzF4&t=333s',
      'video_id': '8klvxfhjzF4'},
     {'author': 'Vistack',
      'channel': 'Vistack',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=B8MSOZzfQLk&t=98s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The table and what you're comfortable with third do not leave important "
              'documents like the MSA terms of agreement and so on at the end of the.',
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': "The table and what you're comfortable with third do not leave important "
             'documents like the MSA terms of agreement and so on at the end of the.',
      'title': 'How To Negotiate A SaaS Contract (Vistack)',
      'url': 'https://www.youtube.com/watch?v=B8MSOZzfQLk&t=98s',
      'video_id': 'B8MSOZzfQLk'},
     {'author': 'Heather Meeker',
      'channel': 'Heather Meeker',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:10](https://www.youtube.com/watch?v=RDxElFsVuWs&t=250s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You don't want your overarching sas agreement to be drafted as an on-premises "
              'license now you might be thinking to yourself if.',
      'timestamp': 250,
      'timestamp_label': '[00:04:10]',
      'timestamp_seconds': 250,
      'tip': "You don't want your overarching sas agreement to be drafted as an on-premises "
             'license now you might be thinking to yourself if.',
      'title': 'How to Negotiate a SaaS Agreement (Heather Meeker)',
      'url': 'https://www.youtube.com/watch?v=RDxElFsVuWs&t=250s',
      'video_id': 'RDxElFsVuWs'},
     {'author': 'Oz SaaS Master',
      'channel': 'Oz SaaS Master',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:44](https://www.youtube.com/watch?v=m505TQagq7g&t=44s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Six, offering an end-of-month discount only ever works if your buyer has total '
              'control over pulling the trigger. If they have to get approval from others, go '
              "through legal, procurement, etc. 's not going to move the needle.",
      'timestamp': 44,
      'timestamp_label': '[00:00:44]',
      'timestamp_seconds': 44,
      'tip': 'Six, offering an end-of-month discount only ever works if your buyer has total '
             'control over pulling the trigger. If they have to get approval from others, go '
             "through legal, procurement, etc. 's not going to move the needle.",
      'title': '🔥 20 SaaS Sales Hacks That’ll Make You Close Deals Like a Boss 💰🚀 (Oz SaaS '
               'Master)',
      'url': 'https://www.youtube.com/watch?v=m505TQagq7g&t=44s',
      'video_id': 'm505TQagq7g'},
     {'author': 'Ingram Micro Cloud',
      'channel': 'Ingram Micro Cloud',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:23](https://www.youtube.com/watch?v=W-fGvHNBEiM&t=203s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Accept the microsoft customer agreement and verify the customer information '
              'click to continue in the review order screen once you reviewed your order and '
              'read the terms of service on the link select I agree then click on the buy '
              'button to complete the order.',
      'timestamp': 203,
      'timestamp_label': '[00:03:23]',
      'timestamp_seconds': 203,
      'tip': 'Accept the microsoft customer agreement and verify the customer information '
             'click to continue in the review order screen once you reviewed your order and '
             'read the terms of service on the link select I agree then click on the buy '
             'button to complete the order.',
      'title': 'Tutorial To Transact Microsoft NCE on Ingram Micro Cloud Marketplace (Ingram '
               'Micro Cloud)',
      'url': 'https://www.youtube.com/watch?v=W-fGvHNBEiM&t=203s',
      'video_id': 'W-fGvHNBEiM'},
     {'author': 'OMNIA Partners',
      'channel': 'OMNIA Partners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:55](https://www.youtube.com/watch?v=iaBVYfYH_ro&t=235s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's where we want to make sure that we also maintain the flexibility for "
              'individual members to customize the agreement to still meet their specific '
              'needs of their business and their location.',
      'timestamp': 235,
      'timestamp_label': '[00:03:55]',
      'timestamp_seconds': 235,
      'tip': "That's where we want to make sure that we also maintain the flexibility for "
             'individual members to customize the agreement to still meet their specific needs '
             'of their business and their location.',
      'title': 'What is a Group Purchasing Organization or GPO? (OMNIA Partners)',
      'url': 'https://www.youtube.com/watch?v=iaBVYfYH_ro&t=235s',
      'video_id': 'iaBVYfYH_ro'},
     {'author': 'ITAM Now',
      'channel': 'ITAM Now',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:55](https://www.youtube.com/watch?v=JLEo4uQ_STM&t=835s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Description it's not required um I'm going to have to put in a contract number "
              "so we'll just say test contract 002 we'll give it a start and end date so we'll "
              "say the new contract runs from 2024 January 30th and it's going to lapse on the "
              '29th of the following.',
      'timestamp': 835,
      'timestamp_label': '[00:13:55]',
      'timestamp_seconds': 835,
      'tip': "Description it's not required um I'm going to have to put in a contract number "
             "so we'll just say test contract 002 we'll give it a start and end date so we'll "
             "say the new contract runs from 2024 January 30th and it's going to lapse on the "
             '29th of the following.',
      'title': 'ServiceNow SAM: Software License and Contract Renewal (ITAM Now)',
      'url': 'https://www.youtube.com/watch?v=JLEo4uQ_STM&t=835s',
      'video_id': 'JLEo4uQ_STM'},
     {'author': 'Telarus',
      'channel': 'Telarus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:30](https://www.youtube.com/watch?v=8ge4I4KL5kQ&t=330s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Things to be simple in terms of how partners are transacting with us and you '
              "know the number one priority for us is to limit Channel conflict and that's "
              'why.',
      'timestamp': 330,
      'timestamp_label': '[00:05:30]',
      'timestamp_seconds': 330,
      'tip': 'Things to be simple in terms of how partners are transacting with us and you '
             "know the number one priority for us is to limit Channel conflict and that's why.",
      'title': 'How RingCentral is Currently Innovating in the Contact Center Space and their '
               'IGNITE! Program (Telarus)',
      'url': 'https://www.youtube.com/watch?v=8ge4I4KL5kQ&t=330s',
      'video_id': '8ge4I4KL5kQ'},
     {'author': 'Willingness to Pay',
      'channel': 'Willingness to Pay',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=KGmwDKTR6fQ&t=117s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Commercial redesigns and I'm just trying to give it to all of you because this "
              'is the book that I would have wanted when I started one of my three businesses '
              "so I hope it's a good read I hope that you get everything out of it that I'll "
              'try to give you so read and enjoy.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': "Commercial redesigns and I'm just trying to give it to all of you because this "
             'is the book that I would have wanted when I started one of my three businesses '
             "so I hope it's a good read I hope that you get everything out of it that I'll "
             'try to give you so read and enjoy.',
      'title': 'How to Get Your SaaS Pricing Structure Right (Willingness to Pay)',
      'url': 'https://www.youtube.com/watch?v=KGmwDKTR6fQ&t=117s',
      'video_id': 'KGmwDKTR6fQ'},
     {'author': 'OMNIA Partners',
      'channel': 'OMNIA Partners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:47](https://www.youtube.com/watch?v=qPpAutcFjBw&t=107s)',
      'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                   '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                   'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                   'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                   'shared-savings audits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Necessarily right if there's no GL coding if there's no you know another "
              'identifier saying exactly what does that supplier do for our organization you '
              'know you may not know exactly what suppliers fit within categories.',
      'timestamp': 107,
      'timestamp_label': '[00:01:47]',
      'timestamp_seconds': 107,
      'tip': "Necessarily right if there's no GL coding if there's no you know another "
             'identifier saying exactly what does that supplier do for our organization you '
             'know you may not know exactly what suppliers fit within categories.',
      'title': 'Spend Visibility: Your Tool for Greater Efficiencies and Cost Savings (OMNIA '
               'Partners)',
      'url': 'https://www.youtube.com/watch?v=qPpAutcFjBw&t=107s',
      'video_id': 'qPpAutcFjBw'}],
 10: [{'author': 'Pax8',
       'channel': 'Pax8',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:05](https://www.youtube.com/watch?v=P960HFmyakQ&t=665s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And that's your pipeline built in seconds. And in preparation for the sales "
               "call, my AI agent can query what's trending as a next recommendation. You can "
               "see that it recommends I upsell Microsoft Defender as we've had a lot of luck "
               'with that with other clients.',
       'timestamp': 665,
       'timestamp_label': '[00:11:05]',
       'timestamp_seconds': 665,
       'tip': "And that's your pipeline built in seconds. And in preparation for the sales "
              "call, my AI agent can query what's trending as a next recommendation. You can "
              "see that it recommends I upsell Microsoft Defender as we've had a lot of luck "
              'with that with other clients.',
       'title': 'Building the Next-Gen MSP Stack: How Pax8 Is Simplifying MSP Integrations | '
                'Pax8 (Pax8)',
       'url': 'https://www.youtube.com/watch?v=P960HFmyakQ&t=665s',
       'video_id': 'P960HFmyakQ'},
      {'author': 'LONDON FILM',
       'channel': 'LONDON FILM',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:10](https://www.youtube.com/watch?v=GA4lZkmVP-w&t=190s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Zoom Mate require additional licensing. Zoom Mate offers ready to use AI '
               'workflows that help businesses automate meeting follow ups, share information, '
               'and manage tasks across connected applications.',
       'timestamp': 190,
       'timestamp_label': '[00:03:10]',
       'timestamp_seconds': 190,
       'tip': 'Zoom Mate require additional licensing. Zoom Mate offers ready to use AI '
              'workflows that help businesses automate meeting follow ups, share information, '
              'and manage tasks across connected applications.',
       'title': 'ZOOM PHONE EXPERT REVIEW FOR BUSINESSES B2B -COMPLETE PROFESSIONAL ANALYSIS '
                '(LONDON FILM)',
       'url': 'https://www.youtube.com/watch?v=GA4lZkmVP-w&t=190s',
       'video_id': 'GA4lZkmVP-w'},
      {'author': 'Telarus',
       'channel': 'Telarus',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:52](https://www.youtube.com/watch?v=-0tioUlVICE&t=412s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Um and then so we assist so you can start in a bot, elevate to human assist. '
               "Um and then we have agent assist where the now off to the side the uh it's "
               'listen to the phone call and AI is going to kind of guide the agent on and '
               'provide knowledge to the agent.',
       'timestamp': 412,
       'timestamp_label': '[00:06:52]',
       'timestamp_seconds': 412,
       'tip': 'Um and then so we assist so you can start in a bot, elevate to human assist. Um '
              "and then we have agent assist where the now off to the side the uh it's listen "
              'to the phone call and AI is going to kind of guide the agent on and provide '
              'knowledge to the agent.',
       'title': 'Understanding Agentic AI in CX- An Executive Interview with Zoom (Telarus)',
       'url': 'https://www.youtube.com/watch?v=-0tioUlVICE&t=412s',
       'video_id': '-0tioUlVICE'},
      {'author': 'Optimize Information Systems',
       'channel': 'Optimize Information Systems',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:54](https://www.youtube.com/watch?v=tex2cNz4vcc&t=234s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I just described or a host of other similar systems they can automate and '
               'streamline all your business processes. The automation that I just described '
               "is just like one. There's so much low-hanging fruit out there when it comes to "
               'automation and Airtable.',
       'timestamp': 234,
       'timestamp_label': '[00:03:54]',
       'timestamp_seconds': 234,
       'tip': 'I just described or a host of other similar systems they can automate and '
              'streamline all your business processes. The automation that I just described is '
              "just like one. There's so much low-hanging fruit out there when it comes to "
              'automation and Airtable.',
       'title': 'How to Automate SaaS License Audits Using Airtable (Optimize Information '
                'Systems)',
       'url': 'https://www.youtube.com/watch?v=tex2cNz4vcc&t=234s',
       'video_id': 'tex2cNz4vcc'},
      {'author': 'Champion Leadership',
       'channel': 'Champion Leadership',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:36](https://www.youtube.com/watch?v=jOL79tUtq3o&t=216s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Roei has helped B2B SaaS companies scale from 10 million to 1 billion ARR. And '
               'his argument today is a blunt one. AI just broke the SaaS model most founders '
               "are still running on and the majority still haven't figured it out. That's the "
               'thing about pricing.',
       'timestamp': 216,
       'timestamp_label': '[00:03:36]',
       'timestamp_seconds': 216,
       'tip': 'Roei has helped B2B SaaS companies scale from 10 million to 1 billion ARR. And '
              'his argument today is a blunt one. AI just broke the SaaS model most founders '
              "are still running on and the majority still haven't figured it out. That's the "
              'thing about pricing.',
       'title': "The Founder's Guide to SaaS Pricing in the AI Era: Seat-Based, Usage-Based, "
                'or Hybrid? | Roee Hartuv (Champion Leadership)',
       'url': 'https://www.youtube.com/watch?v=jOL79tUtq3o&t=216s',
       'video_id': 'jOL79tUtq3o'},
      {'author': 'The SaaS CFO',
       'channel': 'The SaaS CFO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:06](https://www.youtube.com/watch?v=FvNIaRG9sxI&t=66s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Self-service SAS businesses selling $10 products per month and we can't "
               'Benchmark an Enterprise business against a self-service business and vice '
               'versa.',
       'timestamp': 66,
       'timestamp_label': '[00:01:06]',
       'timestamp_seconds': 66,
       'tip': "Self-service SAS businesses selling $10 products per month and we can't "
              'Benchmark an Enterprise business against a self-service business and vice '
              'versa.',
       'title': 'How to Benchmark Your SaaS Business | SaaS Metrics School | BenchMarkIt.ai | '
                'SaaS Business (The SaaS CFO)',
       'url': 'https://www.youtube.com/watch?v=FvNIaRG9sxI&t=66s',
       'video_id': 'FvNIaRG9sxI'},
      {'author': 'Insight Sourcing Group',
       'channel': 'Insight Sourcing Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:25](https://www.youtube.com/watch?v=h348wGhEx-8&t=25s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Traditionally a company would join to leverage the economies of scale in a '
               'category provided by the spin volume in the GPO to achieve savings at no cost.',
       'timestamp': 25,
       'timestamp_label': '[00:00:25]',
       'timestamp_seconds': 25,
       'tip': 'Traditionally a company would join to leverage the economies of scale in a '
              'category provided by the spin volume in the GPO to achieve savings at no cost.',
       'title': 'InsightGPO | Group Purchasing Programs (Insight Sourcing Group)',
       'url': 'https://www.youtube.com/watch?v=h348wGhEx-8&t=25s',
       'video_id': 'h348wGhEx-8'},
      {'author': 'IronEdge Group',
       'channel': 'IronEdge Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:48:04](https://www.youtube.com/watch?v=nsIixe4EZI0&t=2884s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re, you know, dotting the eyes, crossing the tees, asking the vendor the "
               'right questions. The biggest thing anytime I hear AI, I go, where does that '
               'information live? Like, does it live in an AWS platform? Does it live in an '
               'Azure platform?',
       'timestamp': 2884,
       'timestamp_label': '[00:48:04]',
       'timestamp_seconds': 2884,
       'tip': "'re, you know, dotting the eyes, crossing the tees, asking the vendor the right "
              'questions. The biggest thing anytime I hear AI, I go, where does that '
              'information live? Like, does it live in an AWS platform? Does it live in an '
              'Azure platform?',
       'title': 'Shadow IT and SaaS Sprawl: Managing Hidden Cyber Risks (IronEdge Group)',
       'url': 'https://www.youtube.com/watch?v=nsIixe4EZI0&t=2884s',
       'video_id': 'nsIixe4EZI0'},
      {'author': 'Dylan Rich',
       'channel': 'Dylan Rich',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:05](https://www.youtube.com/watch?v=D_gkFglCscs&t=245s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "How to use follow-up tasks and pipeline stages so for the most part you're "
               "going to have someone you get on the phone hey I'm super busy call me back on "
               'Wednesday.',
       'timestamp': 245,
       'timestamp_label': '[00:04:05]',
       'timestamp_seconds': 245,
       'tip': "How to use follow-up tasks and pipeline stages so for the most part you're "
              "going to have someone you get on the phone hey I'm super busy call me back on "
              'Wednesday.',
       'title': 'How to Hit Your Quota EVERY Single Month as a Sales Rep (Dylan Rich)',
       'url': 'https://www.youtube.com/watch?v=D_gkFglCscs&t=245s',
       'video_id': 'D_gkFglCscs'},
      {'author': 'UC Today News',
       'channel': 'UC Today News',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:02](https://www.youtube.com/watch?v=dqTXnYdAKdQ&t=182s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Much more appealing right enabling businesses to leverage these broad spectrum '
               'of tools and services across multiple Cloud environments is is so.',
       'timestamp': 182,
       'timestamp_label': '[00:03:02]',
       'timestamp_seconds': 182,
       'tip': 'Much more appealing right enabling businesses to leverage these broad spectrum '
              'of tools and services across multiple Cloud environments is is so.',
       'title': 'Zoom Multicast: The Next UC Channel Opportunity (UC Today News)',
       'url': 'https://www.youtube.com/watch?v=dqTXnYdAKdQ&t=182s',
       'video_id': 'dqTXnYdAKdQ'},
      {'author': 'The Crancer Group',
       'channel': 'The Crancer Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:25](https://www.youtube.com/watch?v=-zF8JCzzp8w&t=265s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'They just call it specialization. But this is where you want to go. And '
               "there's a reason why you want to go here is because this opens up the "
               'thousands and hundreds of thousands of buckets of money right now for the '
               'three that are underneath advanced specialization.',
       'timestamp': 265,
       'timestamp_label': '[00:04:25]',
       'timestamp_seconds': 265,
       'tip': "They just call it specialization. But this is where you want to go. And there's "
              'a reason why you want to go here is because this opens up the thousands and '
              'hundreds of thousands of buckets of money right now for the three that are '
              'underneath advanced specialization.',
       'title': 'Which Microsoft Partner Level Unlocks the Most Incentives? (AI Cloud '
                'Explained) (The Crancer Group)',
       'url': 'https://www.youtube.com/watch?v=-zF8JCzzp8w&t=265s',
       'video_id': '-zF8JCzzp8w'},
      {'author': 'MicroAge',
       'channel': 'MicroAge',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:22:44](https://www.youtube.com/watch?v=Ap8gUtRq32o&t=1364s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Those environments bringing in new technology and vetting those out and also '
               'bringing together quite frankly the the time it takes to understand the '
               'changes that are occurring being able to get on the phone and and call and '
               'talk to somebody yeah.',
       'timestamp': 1364,
       'timestamp_label': '[00:22:44]',
       'timestamp_seconds': 1364,
       'tip': 'Those environments bringing in new technology and vetting those out and also '
              'bringing together quite frankly the the time it takes to understand the changes '
              'that are occurring being able to get on the phone and and call and talk to '
              'somebody yeah.',
       'title': 'Everything you need to know about Microsoft licensing for CSP in 2025 | Tech '
                'Instinct Podcast Ep.2 (MicroAge)',
       'url': 'https://www.youtube.com/watch?v=Ap8gUtRq32o&t=1364s',
       'video_id': 'Ap8gUtRq32o'},
      {'author': 'SaasRise',
       'channel': 'SaasRise',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:07](https://www.youtube.com/watch?v=3enRkyZlcQk&t=67s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Part three, budget for the ramp. In the Bridge Group data, a new AE takes 6. 2 '
               "months on average to ramp. That's the longest in studies history. Ramp it up "
               'over those six months and plan your cash for half a year of base before a rep '
               'sells at full speed.',
       'timestamp': 67,
       'timestamp_label': '[00:01:07]',
       'timestamp_seconds': 67,
       'tip': 'Part three, budget for the ramp. In the Bridge Group data, a new AE takes 6. 2 '
              "months on average to ramp. That's the longest in studies history. Ramp it up "
              'over those six months and plan your cash for half a year of base before a rep '
              'sells at full speed.',
       'title': 'What quota a $200,000 rep should carry (SaasRise)',
       'url': 'https://www.youtube.com/watch?v=3enRkyZlcQk&t=67s',
       'video_id': '3enRkyZlcQk'},
      {'author': 'Pugh Computers Ltd',
       'channel': 'Pugh Computers Ltd',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=qQoPO5MwZ60&t=20s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Cover any questions you have and if you prefer to come off mute we can do that '
               'as well so if you just raise your hand in the Q&A at the end I can take you '
               'off mute then if you prefer to ask them directly.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'Cover any questions you have and if you prefer to come off mute we can do that '
              'as well so if you just raise your hand in the Q&A at the end I can take you off '
              'mute then if you prefer to ask them directly.',
       'title': 'Webinar: Monthly Adobe Spotlight: VIP Marketplace  - May 22nd 2024 (Pugh '
                'Computers Ltd)',
       'url': 'https://www.youtube.com/watch?v=qQoPO5MwZ60&t=20s',
       'video_id': 'qQoPO5MwZ60'},
      {'author': 'Willingness to Pay',
       'channel': 'Willingness to Pay',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:13](https://www.youtube.com/watch?v=tNlpy7MZ8Vk&t=73s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'How do you validate with the customer if your price is good? Well, you took a '
               'customer and you showed them a presentation. The presentation has to have five '
               'slides. Slide number one, your value proposition.',
       'timestamp': 73,
       'timestamp_label': '[00:01:13]',
       'timestamp_seconds': 73,
       'tip': 'How do you validate with the customer if your price is good? Well, you took a '
              'customer and you showed them a presentation. The presentation has to have five '
              'slides. Slide number one, your value proposition.',
       'title': 'What Good SaaS Pricing Looks Like: Bechmarks, Signals and Metrics '
                '(Willingness to Pay)',
       'url': 'https://www.youtube.com/watch?v=tNlpy7MZ8Vk&t=73s',
       'video_id': 'tNlpy7MZ8Vk'}],
 11: [{'author': 'LONDON FILM',
       'channel': 'LONDON FILM',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:23](https://www.youtube.com/watch?v=ZHjObNVm5_Y&t=83s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'However, businesses with more advanced call routing, multiple office '
               'locations, or complex permission structures should expect implementation to '
               'take longer than it would for a smaller team.',
       'timestamp': 83,
       'timestamp_label': '[00:01:23]',
       'timestamp_seconds': 83,
       'tip': 'However, businesses with more advanced call routing, multiple office locations, '
              'or complex permission structures should expect implementation to take longer '
              'than it would for a smaller team.',
       'title': 'ZOOM PHONE REVIEW - IMPLEMENTATION/ ONBOARDING - CUSTOMER SUPPORT B2B '
                'BUSINESS EXPERT  ANALYSIS (LONDON FILM)',
       'url': 'https://www.youtube.com/watch?v=ZHjObNVm5_Y&t=83s',
       'video_id': 'ZHjObNVm5_Y'},
      {'author': 'Adobe Care',
       'channel': 'Adobe Care',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:38](https://www.youtube.com/watch?v=-rVmsfC5Agk&t=158s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Marketplace partners technical support team is responsible for viewing the API '
               'implementation and testing to ensure that there is a need to escalate. If an '
               'issue needs to be escalated to Adobe, this should be done by the designated '
               'technical relationship manager.',
       'timestamp': 158,
       'timestamp_label': '[00:02:38]',
       'timestamp_seconds': 158,
       'tip': 'Marketplace partners technical support team is responsible for viewing the API '
              'implementation and testing to ensure that there is a need to escalate. If an '
              'issue needs to be escalated to Adobe, this should be done by the designated '
              'technical relationship manager.',
       'title': 'VIP MarketPlace Support for the Adobe Admin Console (Adobe Care)',
       'url': 'https://www.youtube.com/watch?v=-rVmsfC5Agk&t=158s',
       'video_id': '-rVmsfC5Agk'},
      {'author': 'Ingram Micro Canada',
       'channel': 'Ingram Micro Canada',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:54](https://www.youtube.com/watch?v=ZoUkvQ-5m3c&t=354s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And then we've also got a great team at AWS and they've been super "
               "collaborative. Uh again, in a moment's notice, they'll get on a call, they'll "
               'help strategize on the specific account with their account reps.',
       'timestamp': 354,
       'timestamp_label': '[00:05:54]',
       'timestamp_seconds': 354,
       'tip': "And then we've also got a great team at AWS and they've been super "
              "collaborative. Uh again, in a moment's notice, they'll get on a call, they'll "
              'help strategize on the specific account with their account reps.',
       'title': 'IBM + AWS + Ingram Micro: Your Shortcut to Smarter Reseller Success (Ingram '
                'Micro Canada)',
       'url': 'https://www.youtube.com/watch?v=ZoUkvQ-5m3c&t=354s',
       'video_id': 'ZoUkvQ-5m3c'},
      {'author': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
       'channel': 'm365 Show | M365, Azure Cloud, Power Platform & AI',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:57](https://www.youtube.com/watch?v=by9BiS2U7xo&t=357s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Microsoft 365 Business Premium, five users for Teams Enterprise, $700 in '
               'annual Azure credits, and a Visual Studio Enterprise license for your '
               "developers. That's the foundation for a small team. This one's for partners "
               'who are growing.',
       'timestamp': 357,
       'timestamp_label': '[00:05:57]',
       'timestamp_seconds': 357,
       'tip': 'Microsoft 365 Business Premium, five users for Teams Enterprise, $700 in annual '
              'Azure credits, and a Visual Studio Enterprise license for your developers. '
              "That's the foundation for a small team. This one's for partners who are "
              'growing.',
       'title': 'Microsoft Partner Center - Simply Explained (m365 Show | M365, Azure Cloud, '
                'Power Platform & AI)',
       'url': 'https://www.youtube.com/watch?v=by9BiS2U7xo&t=357s',
       'video_id': 'by9BiS2U7xo'},
      {'author': 'Pax8',
       'channel': 'Pax8',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:08](https://www.youtube.com/watch?v=eszZfSp1S1g&t=428s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So co-pilot and agents is really about building that repeatable skill for you. '
               'But then agents a and agent 365 is really about how to govern and monitor and '
               "secure those agents. So, think of it as if you're a manager.",
       'timestamp': 428,
       'timestamp_label': '[00:07:08]',
       'timestamp_seconds': 428,
       'tip': 'So co-pilot and agents is really about building that repeatable skill for you. '
              'But then agents a and agent 365 is really about how to govern and monitor and '
              "secure those agents. So, think of it as if you're a manager.",
       'title': "Microsoft's FY27 Start for Partners Recap | Pax8 (Pax8)",
       'url': 'https://www.youtube.com/watch?v=eszZfSp1S1g&t=428s',
       'video_id': 'eszZfSp1S1g'},
      {'author': 'Channel Talk',
       'channel': 'Channel Talk',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:14](https://www.youtube.com/watch?v=hsCUDuKzpaw&t=434s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'That you can share with us yeah so today i was on a new hire call that i host '
               'once a month for an hour and a half with any new higher class coming.',
       'timestamp': 434,
       'timestamp_label': '[00:07:14]',
       'timestamp_seconds': 434,
       'tip': 'That you can share with us yeah so today i was on a new hire call that i host '
              'once a month for an hour and a half with any new higher class coming.',
       'title': 'Nick Heddy - Getting to know Pax8, a Microsoft Indirect Provider. (Channel '
                'Talk)',
       'url': 'https://www.youtube.com/watch?v=hsCUDuKzpaw&t=434s',
       'video_id': 'hsCUDuKzpaw'},
      {'author': 'Value Analysis Expert',
       'channel': 'Value Analysis Expert',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:39](https://www.youtube.com/watch?v=0F5PDJ2Sxds&t=159s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'They still run their business, but they have access to negotiated prices that '
               'are negotiated at some scale, at a larger scale. Makes total sense, I think, '
               'probably, right? GPOs in healthcare that we interact with these days are '
               'Health Trust or HPG for short.',
       'timestamp': 159,
       'timestamp_label': '[00:02:39]',
       'timestamp_seconds': 159,
       'tip': 'They still run their business, but they have access to negotiated prices that '
              'are negotiated at some scale, at a larger scale. Makes total sense, I think, '
              'probably, right? GPOs in healthcare that we interact with these days are Health '
              'Trust or HPG for short.',
       'title': 'Everything You Need to Know About GPOs and Value Analysis / GPOs - Sutures '
                'and Cents / S4 Ep1 (Value Analysis Expert)',
       'url': 'https://www.youtube.com/watch?v=0F5PDJ2Sxds&t=159s',
       'video_id': '0F5PDJ2Sxds'},
      {'author': 'The Innovation Attorney',
       'channel': 'The Innovation Attorney',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:39](https://www.youtube.com/watch?v=ubYfOw6FSPA&t=939s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Cursor's June 2025 shift to usage-based billing for premium model requests "
               "produced by its own users' public accounts, a case in which a team's $7,000 "
               'annual subscription was consumed in a single day.',
       'timestamp': 939,
       'timestamp_label': '[00:15:39]',
       'timestamp_seconds': 939,
       'tip': "Cursor's June 2025 shift to usage-based billing for premium model requests "
              "produced by its own users' public accounts, a case in which a team's $7,000 "
              'annual subscription was consumed in a single day.',
       'title': 'Seat Pricing or Token Pricing: What Zendesk and HubSpot Chose (The Innovation '
                'Attorney)',
       'url': 'https://www.youtube.com/watch?v=ubYfOw6FSPA&t=939s',
       'video_id': 'ubYfOw6FSPA'},
      {'author': 'YouAttest',
       'channel': 'YouAttest',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:19](https://www.youtube.com/watch?v=NCcXkxFkX8k&t=199s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Call it jira licenses and most importantly I'll just select the date by which "
               'this audit needs to be completed now on the next page since the.',
       'timestamp': 199,
       'timestamp_label': '[00:03:19]',
       'timestamp_seconds': 199,
       'tip': "Call it jira licenses and most importantly I'll just select the date by which "
              'this audit needs to be completed now on the next page since the.',
       'title': 'Rightsizing your SAAS licenses w/ YouAttest (YouAttest)',
       'url': 'https://www.youtube.com/watch?v=NCcXkxFkX8k&t=199s',
       'video_id': 'NCcXkxFkX8k'},
      {'author': 'kconole2011',
       'channel': 'kconole2011',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:31](https://www.youtube.com/watch?v=meAxKn8Td5k&t=151s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Solution we can not only see it we can recover those same millions of dollars '
               'on your behalf our comprehensive expertise means guaranteed savings for you so '
               'give us a call or visit us on the web we look forward to talking with you in '
               'person thanks again.',
       'timestamp': 151,
       'timestamp_label': '[00:02:31]',
       'timestamp_seconds': 151,
       'tip': 'Solution we can not only see it we can recover those same millions of dollars '
              'on your behalf our comprehensive expertise means guaranteed savings for you so '
              'give us a call or visit us on the web we look forward to talking with you in '
              'person thanks again.',
       'title': 'Business Cost Reduction Consultants FREE Consultation, San Deigo, Irvine CA '
                '(kconole2011)',
       'url': 'https://www.youtube.com/watch?v=meAxKn8Td5k&t=151s',
       'video_id': 'meAxKn8Td5k'},
      {'author': 'Auditel, Inc. Telecom Expense Management',
       'channel': 'Auditel, Inc. Telecom Expense Management',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:10](https://www.youtube.com/watch?v=YAHf-FXxBCM&t=130s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Lose alternative to continuing to overpay for your telecom expense so if the '
               'question is is it worthwhile for us to do a telecom on it we think the answer '
               'is yes and we think you will too give us a call today 847 three five six five '
               'five thanks for watching.',
       'timestamp': 130,
       'timestamp_label': '[00:02:10]',
       'timestamp_seconds': 130,
       'tip': 'Lose alternative to continuing to overpay for your telecom expense so if the '
              'question is is it worthwhile for us to do a telecom on it we think the answer '
              'is yes and we think you will too give us a call today 847 three five six five '
              'five thanks for watching.',
       'title': 'Technology expense management - Why Do a telecom audit? (Auditel, Inc. '
                'Telecom Expense Management)',
       'url': 'https://www.youtube.com/watch?v=YAHf-FXxBCM&t=130s',
       'video_id': 'YAHf-FXxBCM'},
      {'author': 'Intalere',
       'channel': 'Intalere',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:36](https://www.youtube.com/watch?v=qlmtp85_1-Q&t=96s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Solutions every healthcare provider is different so we have a wide breadth of '
               'options for you to choose from so join us to start saving visit until our calm '
               'or contact our friendly customer service team at 877 seven one one five six '
               'zero zero today.',
       'timestamp': 96,
       'timestamp_label': '[00:01:36]',
       'timestamp_seconds': 96,
       'tip': 'Solutions every healthcare provider is different so we have a wide breadth of '
              'options for you to choose from so join us to start saving visit until our calm '
              'or contact our friendly customer service team at 877 seven one one five six '
              'zero zero today.',
       'title': 'Who is Intalere and What is a GPO? (Intalere)',
       'url': 'https://www.youtube.com/watch?v=qlmtp85_1-Q&t=96s',
       'video_id': 'qlmtp85_1-Q'},
      {'author': 'Expense Consulting',
       'channel': 'Expense Consulting',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:33](https://www.youtube.com/watch?v=o2wyRpIYL0w&t=33s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Leak out of course we're talking about financial leaks our highly trained team "
               'of financial experts work off-site to conduct an objective inspection of your '
               'expenditures we provide the manpower so you and your team experience no '
               'downtime or inconvenience.',
       'timestamp': 33,
       'timestamp_label': '[00:00:33]',
       'timestamp_seconds': 33,
       'tip': "Leak out of course we're talking about financial leaks our highly trained team "
              'of financial experts work off-site to conduct an objective inspection of your '
              'expenditures we provide the manpower so you and your team experience no '
              'downtime or inconvenience.',
       'title': 'Cost Reduction Consultants - Contingency Based - Expense Consulting (Expense '
                'Consulting)',
       'url': 'https://www.youtube.com/watch?v=o2wyRpIYL0w&t=33s',
       'video_id': 'o2wyRpIYL0w'},
      {'author': 'OMNIA Partners',
       'channel': 'OMNIA Partners',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:35](https://www.youtube.com/watch?v=fdEV8yBr5eM&t=35s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Search process themselves and then come to us and say, hey, here's what I'm "
               "thinking, here's what I have found. We have a small team, so having.",
       'timestamp': 35,
       'timestamp_label': '[00:00:35]',
       'timestamp_seconds': 35,
       'tip': "Search process themselves and then come to us and say, hey, here's what I'm "
              "thinking, here's what I have found. We have a small team, so having.",
       'title': 'How Gonzaga University Simplifies Procurement with OMNIA Partners (OMNIA '
                'Partners)',
       'url': 'https://www.youtube.com/watch?v=fdEV8yBr5eM&t=35s',
       'video_id': 'fdEV8yBr5eM'},
      {'author': 'Ingram Micro USA',
       'channel': 'Ingram Micro USA',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:35](https://www.youtube.com/watch?v=ADZwWSQGFFI&t=395s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Cisco partnership today and in the future. We're your strategic partner in "
               "delivering real business outcomes. I'm proud to lead our S2V professional "
               'services team where we focus on our ASC implementations and training teams so '
               'you can scale smarter and faster.',
       'timestamp': 395,
       'timestamp_label': '[00:06:35]',
       'timestamp_seconds': 395,
       'tip': "Cisco partnership today and in the future. We're your strategic partner in "
              "delivering real business outcomes. I'm proud to lead our S2V professional "
              'services team where we focus on our ASC implementations and training teams so '
              'you can scale smarter and faster.',
       'title': 'How Ingram Micro and Cisco help partners grow together (Ingram Micro USA)',
       'url': 'https://www.youtube.com/watch?v=ADZwWSQGFFI&t=395s',
       'video_id': 'ADZwWSQGFFI'}],
 12: [{'author': 'SaaS Procurement Insider',
       'channel': 'SaaS Procurement Insider',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:47](https://www.youtube.com/watch?v=udHdwtjP7yM&t=107s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Upload a CSV of transactions and ask the model to categorize by vendor type. '
               "What used to take 2 days takes 2 hours. What you're building is a master list. "
               'Vendor name, annual cost, cost center, renewal date, contract owner.',
       'timestamp': 107,
       'timestamp_label': '[00:01:47]',
       'timestamp_seconds': 107,
       'tip': 'Upload a CSV of transactions and ask the model to categorize by vendor type. '
              "What used to take 2 days takes 2 hours. What you're building is a master list. "
              'Vendor name, annual cost, cost center, renewal date, contract owner.',
       'title': 'The SaaS Licence Audit: You are Paying for More Than You Think. (SaaS '
                'Procurement Insider)',
       'url': 'https://www.youtube.com/watch?v=udHdwtjP7yM&t=107s',
       'video_id': 'udHdwtjP7yM'},
      {'author': 'ExpenseSavvy',
       'channel': 'ExpenseSavvy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:27](https://www.youtube.com/watch?v=2RDXap2GiBE&t=207s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'At the end of the day, our goal is to get you as much annual savings as we can '
               "across all of your operational expenses. We don't start and go after all 100 "
               'of your vendors. We usually start with three to five of those vendors, and our '
               'services are free.',
       'timestamp': 207,
       'timestamp_label': '[00:03:27]',
       'timestamp_seconds': 207,
       'tip': 'At the end of the day, our goal is to get you as much annual savings as we can '
              "across all of your operational expenses. We don't start and go after all 100 of "
              'your vendors. We usually start with three to five of those vendors, and our '
              'services are free.',
       'title': 'Cost Reduction Strategies for Business Owners (ExpenseSavvy)',
       'url': 'https://www.youtube.com/watch?v=2RDXap2GiBE&t=207s',
       'video_id': '2RDXap2GiBE'},
      {'author': 'CloudEagle',
       'channel': 'CloudEagle',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:45](https://www.youtube.com/watch?v=s8wp3enRPD8&t=345s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'ROI wins to make a strong case for every renewal. It makes approval '
               "conversations much smoother. And as a concrete action step, don't wait. Pick a "
               'renewal management tool, even a simple one, and start uploading your contracts '
               'and setting up automated alerts this week.',
       'timestamp': 345,
       'timestamp_label': '[00:05:45]',
       'timestamp_seconds': 345,
       'tip': 'ROI wins to make a strong case for every renewal. It makes approval '
              "conversations much smoother. And as a concrete action step, don't wait. Pick a "
              'renewal management tool, even a simple one, and start uploading your contracts '
              'and setting up automated alerts this week.',
       'title': 'How to Review Every SaaS Renewal Before It Auto Renews (CloudEagle)',
       'url': 'https://www.youtube.com/watch?v=s8wp3enRPD8&t=345s',
       'video_id': 's8wp3enRPD8'},
      {'author': 'itGenius 🤓 Biz Tech Experts',
       'channel': 'itGenius 🤓 Biz Tech Experts',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:33](https://www.youtube.com/watch?v=LHbzmi3Otpg&t=273s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Whether you're a sole operator, a micro business with just a couple of staff, "
               "or if you're a large organization with hundreds or even thousands of staff, we "
               'help businesses all over the world with their workspace accounts. And we do '
               'this stuff all day, every day.',
       'timestamp': 273,
       'timestamp_label': '[00:04:33]',
       'timestamp_seconds': 273,
       'tip': "Whether you're a sole operator, a micro business with just a couple of staff, "
              "or if you're a large organization with hundreds or even thousands of staff, we "
              'help businesses all over the world with their workspace accounts. And we do '
              'this stuff all day, every day.',
       'title': 'Switching from Google Reseller to Direct: Pros & Cons (itGenius 🤓 Biz Tech '
                'Experts)',
       'url': 'https://www.youtube.com/watch?v=LHbzmi3Otpg&t=273s',
       'video_id': 'LHbzmi3Otpg'},
      {'author': 'HubSpot Data Analytics by MergeYourData',
       'channel': 'HubSpot Data Analytics by MergeYourData',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:00](https://www.youtube.com/watch?v=ahHk4naTV0s&t=180s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "30 days after the action running. So now we know it's closing on the renewal "
               'date itself. For the amount, we can pull that from the contract. If we could '
               'just pull in annual contract value, it would work. And so that would be the '
               'total value of the deal.',
       'timestamp': 180,
       'timestamp_label': '[00:03:00]',
       'timestamp_seconds': 180,
       'tip': "30 days after the action running. So now we know it's closing on the renewal "
              'date itself. For the amount, we can pull that from the contract. If we could '
              'just pull in annual contract value, it would work. And so that would be the '
              'total value of the deal.',
       'title': 'Triggering Renewal Deal Creation Automatically with Contracts in HubSpot '
                '(HubSpot Data Analytics by MergeYourData)',
       'url': 'https://www.youtube.com/watch?v=ahHk4naTV0s&t=180s',
       'video_id': 'ahHk4naTV0s'},
      {'author': 'brightfin',
       'channel': 'brightfin',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:05](https://www.youtube.com/watch?v=lxObl7Zpr2A&t=65s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Agreements uh with at t with t-mobile to say keith is on the 100 a month plan '
               'with x amount of usage and sarah is on the.',
       'timestamp': 65,
       'timestamp_label': '[00:01:05]',
       'timestamp_seconds': 65,
       'tip': 'Agreements uh with at t with t-mobile to say keith is on the 100 a month plan '
              'with x amount of usage and sarah is on the.',
       'title': 'What is Telecom Expense Management (TEM)? (brightfin)',
       'url': 'https://www.youtube.com/watch?v=lxObl7Zpr2A&t=65s',
       'video_id': 'lxObl7Zpr2A'},
      {'author': 'Daniel Studios',
       'channel': 'Daniel Studios',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:12](https://www.youtube.com/watch?v=kt871J4EiG4&t=72s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Since I'm recording this video in Europe, it's almost Black Friday, so Adobe "
               'is giving us this 44% discount for 12 months. But this is usually around €80 '
               'per month for 12 months on this annual build monthly option.',
       'timestamp': 72,
       'timestamp_label': '[00:01:12]',
       'timestamp_seconds': 72,
       'tip': "Since I'm recording this video in Europe, it's almost Black Friday, so Adobe is "
              'giving us this 44% discount for 12 months. But this is usually around €80 per '
              'month for 12 months on this annual build monthly option.',
       'title': 'Which Adobe to Buy? (Full Breakdown) - Plans and Pricing Comparison (Daniel '
                'Studios)',
       'url': 'https://www.youtube.com/watch?v=kt871J4EiG4&t=72s',
       'video_id': 'kt871J4EiG4'},
      {'author': 'Pax8',
       'channel': 'Pax8',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:25:47](https://www.youtube.com/watch?v=tsL0gg_Jy9U&t=1547s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Uh we have our using M365 co-pilot for nonprofit coming up next week and our '
               'co-pilot agent for nonprofit session coming up next month.',
       'timestamp': 1547,
       'timestamp_label': '[00:25:47]',
       'timestamp_seconds': 1547,
       'tip': 'Uh we have our using M365 co-pilot for nonprofit coming up next week and our '
              'co-pilot agent for nonprofit session coming up next month.',
       'title': 'Pax8 + Microsoft Monthly Update (August 2026) (Pax8)',
       'url': 'https://www.youtube.com/watch?v=tsL0gg_Jy9U&t=1547s',
       'video_id': 'tsL0gg_Jy9U'},
      {'author': 'VMblog',
       'channel': 'VMblog',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:21](https://www.youtube.com/watch?v=UXqaaLTNfFk&t=201s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'MSPs avoiding those same mistakes and pitfalls. So a lot of our partners come '
               'to us for the billing efficiency and then they start growing their business '
               'more by using some of our training, some of our our resources. On top of that, '
               'our support.',
       'timestamp': 201,
       'timestamp_label': '[00:03:21]',
       'timestamp_seconds': 201,
       'tip': 'MSPs avoiding those same mistakes and pitfalls. So a lot of our partners come '
              'to us for the billing efficiency and then they start growing their business '
              'more by using some of our training, some of our our resources. On top of that, '
              'our support.',
       'title': "Pax8's Eric Torres Discusses Enhanced Nerdio Partnership & MSP Marketplace "
                'Solutions: NerdioCon 2025 (VMblog)',
       'url': 'https://www.youtube.com/watch?v=UXqaaLTNfFk&t=201s',
       'video_id': 'UXqaaLTNfFk'},
      {'author': 'Tattooed Nerd',
       'channel': 'Tattooed Nerd',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:01](https://www.youtube.com/watch?v=cHY6UbMTjDA&t=421s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Screen I have an outbound activity that I need to do I need to start this task '
               "going on I just make a simple click of the button here and it's going to "
               'launch.',
       'timestamp': 421,
       'timestamp_label': '[00:07:01]',
       'timestamp_seconds': 421,
       'tip': 'Screen I have an outbound activity that I need to do I need to start this task '
              "going on I just make a simple click of the button here and it's going to "
              'launch.',
       'title': 'Zoom Phone & Outreach Integration - DEMO! (Tattooed Nerd)',
       'url': 'https://www.youtube.com/watch?v=cHY6UbMTjDA&t=421s',
       'video_id': 'cHY6UbMTjDA'},
      {'author': 'Startup Akademia',
       'channel': 'Startup Akademia',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:37](https://www.youtube.com/watch?v=T9lHBjJeZVI&t=37s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Then you can change the specification and here we will have a two sub ways to '
               'do it. The first one is to use less of a certain thing. So, for example, you '
               'are cleaning your office not every day, but you are doing it once a week.',
       'timestamp': 37,
       'timestamp_label': '[00:00:37]',
       'timestamp_seconds': 37,
       'tip': 'Then you can change the specification and here we will have a two sub ways to '
              'do it. The first one is to use less of a certain thing. So, for example, you '
              'are cleaning your office not every day, but you are doing it once a week.',
       'title': 'How to cut costs – Cost Reduction Framework from Management Consulting '
                'Projects (Startup Akademia)',
       'url': 'https://www.youtube.com/watch?v=T9lHBjJeZVI&t=37s',
       'video_id': 'T9lHBjJeZVI'},
      {'author': 'Inside Microsoft AI Cloud Partner Program',
       'channel': 'Inside Microsoft AI Cloud Partner Program',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:08](https://www.youtube.com/watch?v=jz1cE7UYBO4&t=248s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Are called the partner launch the success core and the success expanded you'll "
               'see the annual prices there for these benefit packages but the value that you '
               'get in each of them is substantial.',
       'timestamp': 248,
       'timestamp_label': '[00:04:08]',
       'timestamp_seconds': 248,
       'tip': "Are called the partner launch the success core and the success expanded you'll "
              'see the annual prices there for these benefit packages but the value that you '
              'get in each of them is substantial.',
       'title': 'Unlock Microsoft AI Cloud Partner Program Benefits (Inside Microsoft AI Cloud '
                'Partner Program)',
       'url': 'https://www.youtube.com/watch?v=jz1cE7UYBO4&t=248s',
       'video_id': 'jz1cE7UYBO4'},
      {'author': 'Spyglass MTG',
       'channel': 'Spyglass MTG',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:28](https://www.youtube.com/watch?v=yNBOfW1MoPs&t=88s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Contact information on this screen I can be reached by email at kiler Spyglass '
               'mg.com or by phone at 41437 4692 thank you and have a great day.',
       'timestamp': 88,
       'timestamp_label': '[00:01:28]',
       'timestamp_seconds': 88,
       'tip': 'Contact information on this screen I can be reached by email at kiler Spyglass '
              'mg.com or by phone at 41437 4692 thank you and have a great day.',
       'title': 'Difference Between CSP Direct Partner, Indirect Provider & Indirect Reseller '
                '(Spyglass MTG)',
       'url': 'https://www.youtube.com/watch?v=yNBOfW1MoPs&t=88s',
       'video_id': 'yNBOfW1MoPs'},
      {'author': 'Willingness to Pay',
       'channel': 'Willingness to Pay',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:14](https://www.youtube.com/watch?v=Ieuyh9RZzvM&t=734s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Onboarding here but you can put that in right but you can say Okay so the '
               "basic salmon is whatever 1K per per month and then it's $1 per salmon per "
               "month it's probably way too much but you know you you get the point.",
       'timestamp': 734,
       'timestamp_label': '[00:12:14]',
       'timestamp_seconds': 734,
       'tip': 'Onboarding here but you can put that in right but you can say Okay so the basic '
              "salmon is whatever 1K per per month and then it's $1 per salmon per month it's "
              'probably way too much but you know you you get the point.',
       'title': 'Validating Pricing Models in B2B SaaS (Willingness to Pay)',
       'url': 'https://www.youtube.com/watch?v=Ieuyh9RZzvM&t=734s',
       'video_id': 'Ieuyh9RZzvM'},
      {'author': 'LONDON FILM',
       'channel': 'LONDON FILM',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:50](https://www.youtube.com/watch?v=GA4lZkmVP-w&t=350s)',
       'relevance': 'Attributed practitioner commentary on authorized Partner-of-Record '
                    '(`CPOR`/`VIP`/`CSP`) wholesale software margin splits, `Telarus`/`Avant` '
                    'master-agent `Zoom`/`UCaaS` evergreen residuals, private `GPO` '
                    'volume-bracket rebates, and contingent `25%–35%` SaaS renewal '
                    'shared-savings audits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Zoom Workplace's free basic plan supports video meetings with up to 100 "
               'participants and a 40-minute time limit. Businesses that upgrade to Zoom '
               'Workplace Business can host meetings lasting up to 30 hours with as many as '
               '300 participants.',
       'timestamp': 350,
       'timestamp_label': '[00:05:50]',
       'timestamp_seconds': 350,
       'tip': "Zoom Workplace's free basic plan supports video meetings with up to 100 "
              'participants and a 40-minute time limit. Businesses that upgrade to Zoom '
              'Workplace Business can host meetings lasting up to 30 hours with as many as 300 '
              'participants.',
       'title': 'ZOOM PHONE EXPERT REVIEW FOR BUSINESSES B2B -COMPLETE PROFESSIONAL ANALYSIS '
                '(LONDON FILM)',
       'url': 'https://www.youtube.com/watch?v=GA4lZkmVP-w&t=350s',
       'video_id': 'GA4lZkmVP-w'}]}
