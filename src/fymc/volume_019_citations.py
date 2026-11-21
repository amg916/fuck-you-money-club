"""Curated 180-citation Enterprise Software Reselling baseline (15 per chapter across Q1-Q12) mined strictly from verified Enterprise Software Reselling YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'606',
     'added',
     'alto',
     'asc',
     'audit',
     'aws',
     'building',
     'business',
     'bypass',
     'canalys',
     'carahsoft',
     'channel',
     'client',
     'clients',
     'cloud',
     'collections',
     'consulting',
     'cppo',
     'credit',
     'crowdstrike',
     'csp',
     'cybersecurity',
     'data',
     'databricks',
     'deal',
     'defense',
     'development',
     'direct',
     'distributor',
     'dso',
     'economics',
     'enterprise',
     'finops',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'606',
     'added',
     'alto',
     'asc',
     'audit',
     'aws',
     'budget',
     'building',
     'buyer',
     'bypass',
     'canalys',
     'carahsoft',
     'channel',
     'cloud',
     'collections',
     'consulting',
     'contract',
     'cppo',
     'credit',
     'crowdstrike',
     'csp',
     'customer',
     'cybersecurity',
     'data',
     'databricks',
     'deal',
     'decision',
     'defense',
     'development',
     'direct',
     'distributor',
     'dso',
     'economics',
     'enterprise',
     'escrow',
     'fee',
     'fees',
     'finops',
     'invoice',
     'pay',
     'payment',
     'pays',
     'retainer'},
 3: {'606',
     'added',
     'alto',
     'asc',
     'audit',
     'aws',
     'building',
     'bypass',
     'canalys',
     'carahsoft',
     'cash',
     'cashflow',
     'channel',
     'cloud',
     'collections',
     'commission',
     'consulting',
     'cost',
     'costs',
     'cppo',
     'credit',
     'crowdstrike',
     'csp',
     'cybersecurity',
     'data',
     'databricks',
     'deal',
     'defense',
     'development',
     'direct',
     'distributor',
     'dso',
     'economics',
     'enterprise',
     'finops',
     'margin',
     'margins',
     'price',
     'pricing',
     'profit',
     'roi',
     'unit'},
 4: {'606',
     'added',
     'alto',
     'asc',
     'audit',
     'aws',
     'budget',
     'building',
     'bypass',
     'canalys',
     'capital',
     'carahsoft',
     'channel',
     'cloud',
     'collections',
     'consulting',
     'cppo',
     'credit',
     'crowdstrike',
     'csp',
     'cybersecurity',
     'data',
     'databricks',
     'deal',
     'defense',
     'development',
     'direct',
     'distributor',
     'dso',
     'economics',
     'enterprise',
     'entity',
     'finops',
     'insurance',
     'lean',
     'license',
     'llc',
     'setup',
     'software',
     'stack',
     'startup',
     'tools'},
 5: {'606',
     'added',
     'alto',
     'asc',
     'audit',
     'avoid',
     'aws',
     'building',
     'bypass',
     'canalys',
     'carahsoft',
     'channel',
     'clawback',
     'cloud',
     'collections',
     'consulting',
     'cppo',
     'credit',
     'crowdstrike',
     'csp',
     'cybersecurity',
     'data',
     'databricks',
     'deal',
     'defense',
     'development',
     'direct',
     'dispute',
     'distributor',
     'dso',
     'economics',
     'edge',
     'enterprise',
     'fail',
     'finops',
     'mistake',
     'mistakes',
     'problem',
     'risk',
     'risks',
     'trap',
     'traps'},
 6: {'606',
     'added',
     'alto',
     'asc',
     'audit',
     'aws',
     'building',
     'bypass',
     'canalys',
     'carahsoft',
     'channel',
     'client',
     'cloud',
     'collections',
     'consulting',
     'cppo',
     'credit',
     'crowdstrike',
     'csp',
     'cybersecurity',
     'data',
     'databricks',
     'deal',
     'defense',
     'development',
     'direct',
     'distributor',
     'dso',
     'economics',
     'enterprise',
     'find',
     'finops',
     'first',
     'lead',
     'leads',
     'list',
     'outbound',
     'prospect',
     'qualify',
     'search',
     'sourcing'},
 7: {'606',
     'added',
     'alto',
     'asc',
     'audit',
     'aws',
     'building',
     'bypass',
     'canalys',
     'carahsoft',
     'channel',
     'checklist',
     'cloud',
     'collections',
     'consulting',
     'cppo',
     'credit',
     'crowdstrike',
     'csp',
     'cybersecurity',
     'data',
     'databricks',
     'deal',
     'defense',
     'delivery',
     'development',
     'direct',
     'distributor',
     'dso',
     'economics',
     'enterprise',
     'execution',
     'finops',
     'process',
     'quality',
     'sop',
     'step',
     'steps',
     'system',
     'underwriting',
     'verify',
     'workflow'},
 8: {'606',
     'added',
     'alto',
     'api',
     'asc',
     'audit',
     'aws',
     'building',
     'bypass',
     'canalys',
     'carahsoft',
     'channel',
     'cloud',
     'collections',
     'consulting',
     'cppo',
     'credit',
     'crm',
     'crowdstrike',
     'csp',
     'cybersecurity',
     'data',
     'database',
     'databricks',
     'deal',
     'defense',
     'development',
     'direct',
     'distributor',
     'dso',
     'economics',
     'enterprise',
     'finops',
     'platform',
     'portal',
     'scraper',
     'search',
     'software',
     'tool',
     'tools',
     'tracking'},
 9: {'606',
     'added',
     'agreement',
     'alto',
     'asc',
     'audit',
     'aws',
     'building',
     'bypass',
     'canalys',
     'carahsoft',
     'channel',
     'cloud',
     'collections',
     'compliance',
     'consulting',
     'contract',
     'cppo',
     'credit',
     'crowdstrike',
     'csp',
     'cybersecurity',
     'data',
     'databricks',
     'deal',
     'defense',
     'development',
     'direct',
     'disclosure',
     'distributor',
     'dso',
     'economics',
     'enterprise',
     'finops',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'606',
      'added',
      'agent',
      'ai',
      'alto',
      'asc',
      'audit',
      'automate',
      'automation',
      'aws',
      'building',
      'bypass',
      'canalys',
      'carahsoft',
      'channel',
      'cloud',
      'collections',
      'consulting',
      'cppo',
      'credit',
      'crowdstrike',
      'csp',
      'cybersecurity',
      'dashboard',
      'data',
      'databricks',
      'deal',
      'defense',
      'development',
      'direct',
      'distributor',
      'dso',
      'economics',
      'enterprise',
      'finops',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'606',
      'added',
      'alto',
      'asc',
      'audit',
      'aws',
      'building',
      'bypass',
      'canalys',
      'carahsoft',
      'channel',
      'cloud',
      'collections',
      'consulting',
      'contractor',
      'cppo',
      'credit',
      'crowdstrike',
      'csp',
      'cybersecurity',
      'data',
      'databricks',
      'deal',
      'defense',
      'development',
      'direct',
      'distributor',
      'dso',
      'economics',
      'enterprise',
      'exit',
      'finops',
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
 12: {'606',
      'action',
      'added',
      'alto',
      'asc',
      'audit',
      'aws',
      'building',
      'bypass',
      'canalys',
      'carahsoft',
      'channel',
      'cloud',
      'collections',
      'consulting',
      'cppo',
      'credit',
      'crowdstrike',
      'csp',
      'cybersecurity',
      'data',
      'databricks',
      'day',
      'days',
      'deal',
      'defense',
      'development',
      'direct',
      'distributor',
      'dso',
      'economics',
      'enterprise',
      'finops',
      'launch',
      'milestone',
      'month',
      'plan',
      'roadmap',
      'sprint',
      'start',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Softspend',
      'channel': 'Softspend',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=ziNVpGkDNI4&t=59s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, one is the CSP transactional growth. Second is you have then the '
              'opportunity to build a new service line for FinOps uh and bring added '
              'tokenomics and bring added value towards these new customers and to your '
              "existing book of business. So, that's the second growth area.",
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': 'So, one is the CSP transactional growth. Second is you have then the opportunity '
             'to build a new service line for FinOps uh and bring added tokenomics and bring '
             'added value towards these new customers and to your existing book of business. '
             "So, that's the second growth area.",
      'title': 'Why should we adopt CSP? (Softspend)',
      'url': 'https://www.youtube.com/watch?v=ziNVpGkDNI4&t=59s',
      'video_id': 'ziNVpGkDNI4'},
     {'author': 'Amazon Web Services',
      'channel': 'Amazon Web Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:10](https://www.youtube.com/watch?v=qWl-wamuA-Q&t=490s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Progress of an aws marketplace transaction aws has also launched seller data '
              'feed delivery service often referred to as sdds to enable isvs to meet unique '
              'reporting and visualization needs and obtain business highlights daily.',
      'timestamp': 490,
      'timestamp_label': '[00:08:10]',
      'timestamp_seconds': 490,
      'tip': 'Progress of an aws marketplace transaction aws has also launched seller data '
             'feed delivery service often referred to as sdds to enable isvs to meet unique '
             'reporting and visualization needs and obtain business highlights daily.',
      'title': 'AWS Marketplace Private Offers overview for ISVs (Amazon Web Services)',
      'url': 'https://www.youtube.com/watch?v=qWl-wamuA-Q&t=490s',
      'video_id': 'qWl-wamuA-Q'},
     {'author': 'AppXite',
      'channel': 'AppXite',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:56](https://www.youtube.com/watch?v=rSX-pZstKp8&t=236s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Integrations can enable your entire multi-cloud business including your own '
              'managed services or intellectual properties catalog and as a company epoxide is '
              'the only market player that is no competitor to your csp market share.',
      'timestamp': 236,
      'timestamp_label': '[00:03:56]',
      'timestamp_seconds': 236,
      'tip': 'Integrations can enable your entire multi-cloud business including your own '
             'managed services or intellectual properties catalog and as a company epoxide is '
             'the only market player that is no competitor to your csp market share.',
      'title': 'Microsoft Cloud Ecosystem Explained: Cloud Solution Provider program (AppXite)',
      'url': 'https://www.youtube.com/watch?v=rSX-pZstKp8&t=236s',
      'video_id': 'rSX-pZstKp8'},
     {'author': 'FinOps Foundation',
      'channel': 'FinOps Foundation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:36](https://www.youtube.com/watch?v=hQDjTANIaTo&t=996s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Cloud if you take that as a finops principle and you apply it to SAS how does '
              'that work decisions need to be driven by the business value of the.',
      'timestamp': 996,
      'timestamp_label': '[00:16:36]',
      'timestamp_seconds': 996,
      'tip': 'Cloud if you take that as a finops principle and you apply it to SAS how does '
             'that work decisions need to be driven by the business value of the.',
      'title': 'Mastering FinOps for SaaS Optimization (FinOps Foundation)',
      'url': 'https://www.youtube.com/watch?v=hQDjTANIaTo&t=996s',
      'video_id': 'hQDjTANIaTo'},
     {'author': 'Ordway',
      'channel': 'Ordway',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=vPpXI4fjA1A&t=30s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Ism's favorite business model recurring Revenue my name is Steve Kyer I'm the "
              "chief marketing officer here at Ordway and I'm happy to welcome today's.",
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': "Ism's favorite business model recurring Revenue my name is Steve Kyer I'm the "
             "chief marketing officer here at Ordway and I'm happy to welcome today's.",
      'title': 'Revenue Recognition for SaaS Contracts under ASC 606 (Ordway)',
      'url': 'https://www.youtube.com/watch?v=vPpXI4fjA1A&t=30s',
      'video_id': 'vPpXI4fjA1A'},
     {'author': 'Summer Zaldivar',
      'channel': 'Summer Zaldivar',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=4qYKEjVIAjc&t=114s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Has on the last in during deployment this is only the beginning of a continued '
              'effort to ensure our data center and HEC chat customers are realizing value in '
              'their investment our end goal is to establish long-term customer loyalty and '
              'recurring revenue.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': 'Has on the last in during deployment this is only the beginning of a continued '
             'effort to ensure our data center and HEC chat customers are realizing value in '
             'their investment our end goal is to establish long-term customer loyalty and '
             'recurring revenue.',
      'title': 'Customer Success Video for Channel Partner ver 1 (Summer Zaldivar)',
      'url': 'https://www.youtube.com/watch?v=4qYKEjVIAjc&t=114s',
      'video_id': '4qYKEjVIAjc'},
     {'author': 'BrainSell',
      'channel': 'BrainSell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:37](https://www.youtube.com/watch?v=Y3mGiwmy2l0&t=37s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We sell software platforms but then we add value by providing the services to '
              'implement those platforms. So we provide the training, the implementation, the '
              'development, the understanding of applications of business with technology. '
              "Again that's the value add.",
      'timestamp': 37,
      'timestamp_label': '[00:00:37]',
      'timestamp_seconds': 37,
      'tip': 'We sell software platforms but then we add value by providing the services to '
             'implement those platforms. So we provide the training, the implementation, the '
             'development, the understanding of applications of business with technology. '
             "Again that's the value add.",
      'title': 'What the Heck is... a Value-Added Reseller (VAR)? (BrainSell)',
      'url': 'https://www.youtube.com/watch?v=Y3mGiwmy2l0&t=37s',
      'video_id': 'Y3mGiwmy2l0'},
     {'author': 'Innovia Consulting',
      'channel': 'Innovia Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:14](https://www.youtube.com/watch?v=WV0uRh3yMX4&t=194s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Consulting firm 30 plus years in business 50 plus team members um and we're "
              'kind of located primarily in the midwest but uh we go as far south as.',
      'timestamp': 194,
      'timestamp_label': '[00:03:14]',
      'timestamp_seconds': 194,
      'tip': "Consulting firm 30 plus years in business 50 plus team members um and we're kind "
             'of located primarily in the midwest but uh we go as far south as.',
      'title': 'Would Your Company Pass a Licensing Audit (Innovia Consulting)',
      'url': 'https://www.youtube.com/watch?v=WV0uRh3yMX4&t=194s',
      'video_id': 'WV0uRh3yMX4'},
     {'author': 'Microsoft Americas Partner Community',
      'channel': 'Microsoft Americas Partner Community',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:39](https://www.youtube.com/watch?v=ybzVv-GZvMc&t=219s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Partner will continue evolving together with the program itself as you can see '
              "csp indirect indirect resellers break even four times faster and this is what's "
              'so important to choose the right model for your specific business.',
      'timestamp': 219,
      'timestamp_label': '[00:03:39]',
      'timestamp_seconds': 219,
      'tip': 'Partner will continue evolving together with the program itself as you can see '
             "csp indirect indirect resellers break even four times faster and this is what's "
             'so important to choose the right model for your specific business.',
      'title': 'Cloud Solution Provider Program (Microsoft Americas Partner Community)',
      'url': 'https://www.youtube.com/watch?v=ybzVv-GZvMc&t=219s',
      'video_id': 'ybzVv-GZvMc'},
     {'author': 'Marketing Business Network',
      'channel': 'Marketing Business Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=YKXY9b__zcA&t=21s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A partner is another business that helps market or sell it. The funding might '
              'support a workshop, advertising campaign or event introducing the offering to '
              'potential customers. The purpose is to share the cost of reaching customers. A '
              'common model is reimbursement.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'A partner is another business that helps market or sell it. The funding might '
             'support a workshop, advertising campaign or event introducing the offering to '
             'potential customers. The purpose is to share the cost of reaching customers. A '
             'common model is reimbursement.',
      'title': 'What are Market Development Funds? (Marketing Business Network)',
      'url': 'https://www.youtube.com/watch?v=YKXY9b__zcA&t=21s',
      'video_id': 'YKXY9b__zcA'},
     {'author': 'GoldFinch Cloud Solutions',
      'channel': 'GoldFinch Cloud Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=tn0y9__lnqY&t=111s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Clients scalability is crucial choose an Erp partner that provides a scalable '
              'solution accommodating the growth of both your business and your clients gulfen '
              'Erp with its scalable architecture ensures smooth expansion handling increased '
              'data and user volumes.',
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': 'Clients scalability is crucial choose an Erp partner that provides a scalable '
             'solution accommodating the growth of both your business and your clients gulfen '
             'Erp with its scalable architecture ensures smooth expansion handling increased '
             'data and user volumes.',
      'title': 'VAR Talk: Finding the Right ERP Partner (GoldFinch Cloud Solutions)',
      'url': 'https://www.youtube.com/watch?v=tn0y9__lnqY&t=111s',
      'video_id': 'tn0y9__lnqY'},
     {'author': 'Channel Institute',
      'channel': 'Channel Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:03](https://www.youtube.com/watch?v=7tcEnD85CE4&t=183s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Recruit are aligned with those goals and that they have business models that '
              'are viable within those business goals as well and you need to ensure that new '
              'partners have that suitable business model for this particular strategic move '
              "that you're making.",
      'timestamp': 183,
      'timestamp_label': '[00:03:03]',
      'timestamp_seconds': 183,
      'tip': 'Recruit are aligned with those goals and that they have business models that are '
             'viable within those business goals as well and you need to ensure that new '
             'partners have that suitable business model for this particular strategic move '
             "that you're making.",
      'title': 'Channel Partner Recruitment Case Study - Channel Institute (Channel Institute)',
      'url': 'https://www.youtube.com/watch?v=7tcEnD85CE4&t=183s',
      'video_id': '7tcEnD85CE4'},
     {'author': 'Forest Lin',
      'channel': 'Forest Lin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:31](https://www.youtube.com/watch?v=SdoLFHhMm1Q&t=391s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The business value if there are significant business value aligned with this '
              'grow it maybe are a heresy growth otherwise it could potentially have the '
              'opportunity to save the cost.',
      'timestamp': 391,
      'timestamp_label': '[00:06:31]',
      'timestamp_seconds': 391,
      'tip': 'The business value if there are significant business value aligned with this '
             'grow it maybe are a heresy growth otherwise it could potentially have the '
             'opportunity to save the cost.',
      'title': '02: A FinOps Case Study (Forest Lin)',
      'url': 'https://www.youtube.com/watch?v=SdoLFHhMm1Q&t=391s',
      'video_id': 'SdoLFHhMm1Q'},
     {'author': 'Channel Marketing Academy',
      'channel': 'Channel Marketing Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:41](https://www.youtube.com/watch?v=vLO0gA3TgxE&t=221s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Amazing because I captured those notes but I have to sit there ask the '
              'questions write them all down the easier it is for me to really have an '
              'understanding of your value what you do what you offer and how you can help my '
              'clients.',
      'timestamp': 221,
      'timestamp_label': '[00:03:41]',
      'timestamp_seconds': 221,
      'tip': 'Amazing because I captured those notes but I have to sit there ask the questions '
             'write them all down the easier it is for me to really have an understanding of '
             'your value what you do what you offer and how you can help my clients.',
      'title': 'Ask a VAR: How Can an ISV Get Better Engagement and Build a Partnership? '
               '(Channel Marketing Academy)',
      'url': 'https://www.youtube.com/watch?v=vLO0gA3TgxE&t=221s',
      'video_id': 'vLO0gA3TgxE'},
     {'author': 'The SaaS CFO',
      'channel': 'The SaaS CFO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:55](https://www.youtube.com/watch?v=p4KgISWaH6s&t=535s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Should record revenue specific to your business I hope you enjoyed the lesson '
              'today on SAS revenue recognition and deferred revenue.',
      'timestamp': 535,
      'timestamp_label': '[00:08:55]',
      'timestamp_seconds': 535,
      'tip': 'Should record revenue specific to your business I hope you enjoyed the lesson '
             'today on SAS revenue recognition and deferred revenue.',
      'title': 'What is SaaS Revenue Recognition? (The SaaS CFO)',
      'url': 'https://www.youtube.com/watch?v=p4KgISWaH6s&t=535s',
      'video_id': 'p4KgISWaH6s'}],
 2: [{'author': 'Accounting and Auditing Hub',
      'channel': 'Accounting and Auditing Hub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=-5y55BOFAKA&t=31s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Cloud Nova Solutions is a B2B enterprise software provider. On January 1st, '
              '2026, they sign a non-cancellable 3-year contract with Global Corp. Because '
              'Global Corp has great credit, they pay the entire contract upfront on day one.',
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': 'Cloud Nova Solutions is a B2B enterprise software provider. On January 1st, '
             '2026, they sign a non-cancellable 3-year contract with Global Corp. Because '
             'Global Corp has great credit, they pay the entire contract upfront on day one.',
      'title': 'SaaS Revenue Recognition Explained: IFRS 15 & ASC 606 Case Study (Accounting '
               'and Auditing Hub)',
      'url': 'https://www.youtube.com/watch?v=-5y55BOFAKA&t=31s',
      'video_id': '-5y55BOFAKA'},
     {'author': 'Accounting Journal Entries',
      'channel': 'Accounting Journal Entries',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:16](https://www.youtube.com/watch?v=SgRytNI-ALo&t=136s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Hundred dollars per month when the customer pays for the subscription these are '
              'just a few examples of how ASC 606 works the specific application of ASC 606 '
              'will vary depending on the specific facts and circumstances of each contract.',
      'timestamp': 136,
      'timestamp_label': '[00:02:16]',
      'timestamp_seconds': 136,
      'tip': 'Hundred dollars per month when the customer pays for the subscription these are '
             'just a few examples of how ASC 606 works the specific application of ASC 606 '
             'will vary depending on the specific facts and circumstances of each contract.',
      'title': 'ASC 606 Simplified: Understanding Revenue Recognition in 3 Minutes (Accounting '
               'Journal Entries)',
      'url': 'https://www.youtube.com/watch?v=SgRytNI-ALo&t=136s',
      'video_id': 'SgRytNI-ALo'},
     {'author': '12th & Norwegian',
      'channel': '12th & Norwegian',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:18](https://www.youtube.com/watch?v=Q0XhS1B8mWE&t=618s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Fixes right how does ASC 606 deal with those elements so postc contract '
              'customer support or PCS okay can be a bit tricky okay the key is to.',
      'timestamp': 618,
      'timestamp_label': '[00:10:18]',
      'timestamp_seconds': 618,
      'tip': 'Fixes right how does ASC 606 deal with those elements so postc contract customer '
             'support or PCS okay can be a bit tricky okay the key is to.',
      'title': 'ASC 606 SaaS Basics - Revenue Recognition Podcast (12th & Norwegian)',
      'url': 'https://www.youtube.com/watch?v=Q0XhS1B8mWE&t=618s',
      'video_id': 'Q0XhS1B8mWE'},
     {'author': 'Amazon Web Services',
      'channel': 'Amazon Web Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:38](https://www.youtube.com/watch?v=vKzo7FINzss&t=158s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The issuance of the invoice while credit card purchases are immediate buyers on '
              'invoicing have standard payment terms of net 30 and some customers do get '
              'others such as 45 60 etc the invoice due date is determined off the payment '
              'terms agreed upon between buyer and aws.',
      'timestamp': 158,
      'timestamp_label': '[00:02:38]',
      'timestamp_seconds': 158,
      'tip': 'The issuance of the invoice while credit card purchases are immediate buyers on '
             'invoicing have standard payment terms of net 30 and some customers do get others '
             'such as 45 60 etc the invoice due date is determined off the payment terms '
             'agreed upon between buyer and aws.',
      'title': 'Buyer Invoicing - AWS Marketplace Private Offers (Amazon Web Services)',
      'url': 'https://www.youtube.com/watch?v=vKzo7FINzss&t=158s',
      'video_id': 'vKzo7FINzss'},
     {'author': 'Accounting Academy',
      'channel': 'Accounting Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:18](https://www.youtube.com/watch?v=rm7beKRTRko&t=198s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Please take a minute to read through fact pattern B and the slight changes that '
              'were made. Pay attention to the payment enforcability. Additionally, the '
              'contract does not meet the criteria to be recognized over time.',
      'timestamp': 198,
      'timestamp_label': '[00:03:18]',
      'timestamp_seconds': 198,
      'tip': 'Please take a minute to read through fact pattern B and the slight changes that '
             'were made. Pay attention to the payment enforcability. Additionally, the '
             'contract does not meet the criteria to be recognized over time.',
      'title': 'ASC 606: Revenue Recognition - Step 5 Recognize Revenue (Accounting Academy)',
      'url': 'https://www.youtube.com/watch?v=rm7beKRTRko&t=198s',
      'video_id': 'rm7beKRTRko'},
     {'author': 'Marketing Business Network',
      'channel': 'Marketing Business Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=gPoVTzxEwPw&t=39s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The partner proposes an activity and budget, gets approval, carries out the '
              'activity and submits a claim with supporting evidence. The vendor reviews that '
              'claim and pays the eligible amount under the program rules. An approved budget '
              'is not automatically a payment.',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': 'The partner proposes an activity and budget, gets approval, carries out the '
             'activity and submits a claim with supporting evidence. The vendor reviews that '
             'claim and pays the eligible amount under the program rules. An approved budget '
             'is not automatically a payment.',
      'title': 'What are Market Development Funds? (Marketing Business Network)',
      'url': 'https://www.youtube.com/watch?v=gPoVTzxEwPw&t=39s',
      'video_id': 'gPoVTzxEwPw'},
     {'author': 'Amazon Web Services',
      'channel': 'Amazon Web Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:02](https://www.youtube.com/watch?v=MlboB3rLbvE&t=122s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Previous payment schedule once the customer accepts if you would like the buyer '
              'to be billed up front for their subscription to the agreement-based offer you '
              'can schedule the invoice date for today this dictates that the buyer will be '
              'billed upon subscription.',
      'timestamp': 122,
      'timestamp_label': '[00:02:02]',
      'timestamp_seconds': 122,
      'tip': 'Previous payment schedule once the customer accepts if you would like the buyer '
             'to be billed up front for their subscription to the agreement-based offer you '
             'can schedule the invoice date for today this dictates that the buyer will be '
             'billed upon subscription.',
      'title': 'Create an Agreements Based Offer - AWS Marketplace Private Offers (Amazon Web '
               'Services)',
      'url': 'https://www.youtube.com/watch?v=MlboB3rLbvE&t=122s',
      'video_id': 'MlboB3rLbvE'},
     {'author': '10 Min For Supply Chain',
      'channel': '10 Min For Supply Chain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=vdxHe8A6Tkk&t=20s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'With net 30, payment is due 30 days after the agreed starting point, typically '
              'the invoice date. With net 60, you generally have 60 days from that agreed '
              'starting point to pay.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'With net 30, payment is due 30 days after the agreed starting point, typically '
             'the invoice date. With net 60, you generally have 60 days from that agreed '
             'starting point to pay.',
      'title': 'How to Negotiate Supplier Payment Terms | Upfront to Net 60 Explained (10 Min '
               'For Supply Chain)',
      'url': 'https://www.youtube.com/watch?v=vdxHe8A6Tkk&t=20s',
      'video_id': 'vdxHe8A6Tkk'},
     {'author': 'The SaaS CFO',
      'channel': 'The SaaS CFO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:06](https://www.youtube.com/watch?v=XcyrOPFaa6o&t=66s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Renewal not a booking so say that customer is paying 10K we sign them up for '
              'another annual contract or multi-year contract and again they pay.',
      'timestamp': 66,
      'timestamp_label': '[00:01:06]',
      'timestamp_seconds': 66,
      'tip': 'Renewal not a booking so say that customer is paying 10K we sign them up for '
             'another annual contract or multi-year contract and again they pay.',
      'title': 'Does Expansion MRR or ARR Include Renewals? | SaaS Metrics School | Renewals '
               '(The SaaS CFO)',
      'url': 'https://www.youtube.com/watch?v=XcyrOPFaa6o&t=66s',
      'video_id': 'XcyrOPFaa6o'},
     {'author': 'Microsoft AI Cloud Partner Program',
      'channel': 'Microsoft AI Cloud Partner Program',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=Ccgwwzx0ld4&t=100s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The other thing is, as we see the market evolving, Pax8 is starting to develop '
              "an advanced product roadmap and it's gonna truly modernize the industry. And "
              'the focus that we will have with this modernization, is driving customer '
              'acquisition for the channel ecosystem.',
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': 'The other thing is, as we see the market evolving, Pax8 is starting to develop '
             "an advanced product roadmap and it's gonna truly modernize the industry. And the "
             'focus that we will have with this modernization, is driving customer acquisition '
             'for the channel ecosystem.',
      'title': 'Partner Viewpoint: How Microsoft + Pax8 are skilling up the channel (Microsoft '
               'AI Cloud Partner Program)',
      'url': 'https://www.youtube.com/watch?v=Ccgwwzx0ld4&t=100s',
      'video_id': 'Ccgwwzx0ld4'},
     {'author': 'TD SYNNEX',
      'channel': 'TD SYNNEX',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:15](https://www.youtube.com/watch?v=8xAn9TMt7Ew&t=195s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re carrying the financial responsibility for this. Why doesn't that sit with "
              "say the hyperscaler or, you know the distributor? What's what's going on here? "
              'Yeah, well, under the reseller agreement, consumption billed to the customer is '
              "the reseller's responsibility.",
      'timestamp': 195,
      'timestamp_label': '[00:03:15]',
      'timestamp_seconds': 195,
      'tip': "'re carrying the financial responsibility for this. Why doesn't that sit with "
             "say the hyperscaler or, you know the distributor? What's what's going on here? "
             'Yeah, well, under the reseller agreement, consumption billed to the customer is '
             "the reseller's responsibility.",
      'title': 'Why Cloud Consumption Fraud Is Becoming a Bigger Business Risk (TD SYNNEX)',
      'url': 'https://www.youtube.com/watch?v=8xAn9TMt7Ew&t=195s',
      'video_id': '8xAn9TMt7Ew'},
     {'author': 'Demystifying Microsoft SMB Office Mix Series',
      'channel': 'Demystifying Microsoft SMB Office Mix Series',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=lGN8Dnmwb08&t=91s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The customer lifecycle my next segment we will discuss two options available '
              'through CSB in the interim please visit the resources available on this slide '
              'go to WWI kristov CSB comm read a little bit more about CSB and tune in into '
              'the next segment.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': 'The customer lifecycle my next segment we will discuss two options available '
             'through CSB in the interim please visit the resources available on this slide go '
             'to WWI kristov CSB comm read a little bit more about CSB and tune in into the '
             'next segment.',
      'title': 'What is the Cloud Solution Provider Program (CSP)? (Demystifying Microsoft SMB '
               'Office Mix Series)',
      'url': 'https://www.youtube.com/watch?v=lGN8Dnmwb08&t=91s',
      'video_id': 'lGN8Dnmwb08'},
     {'author': 'The SaaS CFO',
      'channel': 'The SaaS CFO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=X9tvWcO_2KI&t=60s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Boy, I'm worried we need to check our pipeline. Do we have are we over staffed "
              'now? Metric number three, billable utilization. And regardless of time and '
              'material or fixed fee scopes, you need to track the amount of time spent on '
              'customer projects.',
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': "Boy, I'm worried we need to check our pipeline. Do we have are we over staffed "
             'now? Metric number three, billable utilization. And regardless of time and '
             'material or fixed fee scopes, you need to track the amount of time spent on '
             'customer projects.',
      'title': 'My Top 4 Professional Services Metrics | SaaS Metrics School | SaaS '
               'Professional Services (The SaaS CFO)',
      'url': 'https://www.youtube.com/watch?v=X9tvWcO_2KI&t=60s',
      'video_id': 'X9tvWcO_2KI'},
     {'author': 'Peakflo',
      'channel': 'Peakflo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:48](https://www.youtube.com/watch?v=Y400sNeYMUw&t=228s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Toggle on the upper right corner once all the information is filled your '
              'vendors can click on the send to customer button to submit their information '
              'and complete the sign up process.',
      'timestamp': 228,
      'timestamp_label': '[00:03:48]',
      'timestamp_seconds': 228,
      'tip': 'Toggle on the upper right corner once all the information is filled your vendors '
             'can click on the send to customer button to submit their information and '
             'complete the sign up process.',
      'title': 'Vendor Onboarding Management | Peakflo (Peakflo)',
      'url': 'https://www.youtube.com/watch?v=Y400sNeYMUw&t=228s',
      'video_id': 'Y400sNeYMUw'},
     {'author': 'Gatekeeper Vendor & Contract Lifecycle Management',
      'channel': 'Gatekeeper Vendor & Contract Lifecycle Management',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:21](https://www.youtube.com/watch?v=-L_45dSkyaE&t=381s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Going to set your relationship up far better before you go check out this video '
              'which is all about rank statuses and how you can use right statuses to give '
              'full visibility to your business around the performance of your vendors and the '
              'vendor contracts see you soon.',
      'timestamp': 381,
      'timestamp_label': '[00:06:21]',
      'timestamp_seconds': 381,
      'tip': 'Going to set your relationship up far better before you go check out this video '
             'which is all about rank statuses and how you can use right statuses to give full '
             'visibility to your business around the performance of your vendors and the '
             'vendor contracts see you soon.',
      'title': 'What is Vendor Onboarding? (Gatekeeper Vendor & Contract Lifecycle Management)',
      'url': 'https://www.youtube.com/watch?v=-L_45dSkyaE&t=381s',
      'video_id': '-L_45dSkyaE'}],
 3: [{'author': 'Clazar',
      'channel': 'Clazar',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=h7liwzzA_-I&t=64s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Private offers are essentially useful for the following. Enterprise customers '
              'requiring tailored pricing and contract terms. CPPO and CPPO is channel partner '
              'private offer which is the channel motion for AWS.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': 'Private offers are essentially useful for the following. Enterprise customers '
             'requiring tailored pricing and contract terms. CPPO and CPPO is channel partner '
             'private offer which is the channel motion for AWS.',
      'title': 'How Private Offers work on AWS Marketplace explained step by step (Clazar)',
      'url': 'https://www.youtube.com/watch?v=h7liwzzA_-I&t=64s',
      'video_id': 'h7liwzzA_-I'},
     {'author': 'CodeLucky',
      'channel': 'CodeLucky',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:22](https://www.youtube.com/watch?v=472D_UGqdxA&t=382s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A well-implemented tagging strategy transforms raw billing data into actionable '
              'insights, enabling accurate chargebacks, informed decision-making, and '
              'effective cost optimization. Effective monitoring and reporting are essential '
              'for maintaining control over cloud costs.',
      'timestamp': 382,
      'timestamp_label': '[00:06:22]',
      'timestamp_seconds': 382,
      'tip': 'A well-implemented tagging strategy transforms raw billing data into actionable '
             'insights, enabling accurate chargebacks, informed decision-making, and effective '
             'cost optimization. Effective monitoring and reporting are essential for '
             'maintaining control over cloud costs.',
      'title': 'FinOps Explained: Master Cloud Cost Management & Optimization for Beginners '
               '(CodeLucky)',
      'url': 'https://www.youtube.com/watch?v=472D_UGqdxA&t=382s',
      'video_id': '472D_UGqdxA'},
     {'author': 'The SaaS CFO',
      'channel': 'The SaaS CFO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=gQvlawVvuzw&t=72s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "SASPL so we can understand in this case, say if you're not pricing your "
              "services that high, how much cash that's eating up in your business. So the "
              'proper SASPL setup is so critical so we can calculate the proper services '
              'margins that that correct gross profit.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': "SASPL so we can understand in this case, say if you're not pricing your services "
             "that high, how much cash that's eating up in your business. So the proper SASPL "
             'setup is so critical so we can calculate the proper services margins that that '
             'correct gross profit.',
      'title': 'My Top 4 Professional Services Metrics – Services Margins | SaaS Metrics '
               'School (The SaaS CFO)',
      'url': 'https://www.youtube.com/watch?v=gQvlawVvuzw&t=72s',
      'video_id': 'gQvlawVvuzw'},
     {'author': 'Amazon Web Services',
      'channel': 'Amazon Web Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:24](https://www.youtube.com/watch?v=2qDBJ9lxIdQ&t=144s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'With this pricing model, we would set a contract price for each contract '
              'dimension, and a unit price for each usage dimension. The buyer then chooses '
              'the desired quantity for each dimension and AWS invoices the buyer for the full '
              'amount upon acceptance of the private offer.',
      'timestamp': 144,
      'timestamp_label': '[00:02:24]',
      'timestamp_seconds': 144,
      'tip': 'With this pricing model, we would set a contract price for each contract '
             'dimension, and a unit price for each usage dimension. The buyer then chooses the '
             'desired quantity for each dimension and AWS invoices the buyer for the full '
             'amount upon acceptance of the private offer.',
      'title': 'Create AWS Marketplace Private Offers for SaaS Contracts | Amazon Web Services '
               '(Amazon Web Services)',
      'url': 'https://www.youtube.com/watch?v=2qDBJ9lxIdQ&t=144s',
      'video_id': '2qDBJ9lxIdQ'},
     {'author': 'FinOps Foundation',
      'channel': 'FinOps Foundation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=ryko_HHYy18&t=134s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Business strategy and tech strategy align on different sides. Business side's "
              'focused on unit economics. Tech strategy says, "Okay, well, I need to figure '
              'out how I\'m going to architect for cloud." Business side says, you know, give '
              'me benchmarking.',
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': "Business strategy and tech strategy align on different sides. Business side's "
             'focused on unit economics. Tech strategy says, "Okay, well, I need to figure out '
             'how I\'m going to architect for cloud." Business side says, you know, give me '
             'benchmarking.',
      'title': 'What Is a FinOps Scope? How FinOps Frames SaaS, Licensing, AI, Data Center, '
               'and Other Cost and Usage (FinOps Foundation)',
      'url': 'https://www.youtube.com/watch?v=ryko_HHYy18&t=134s',
      'video_id': 'ryko_HHYy18'},
     {'author': 'Demystifying Microsoft SMB Office Mix Series',
      'channel': 'Demystifying Microsoft SMB Office Mix Series',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:56](https://www.youtube.com/watch?v=wzXR-g6_lxo&t=296s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Will see that those 8% are exactly a mirrored here as well so we have parity in '
              'the two programs thank you that wraps my session on CSP pricing margins and '
              'incentives.',
      'timestamp': 296,
      'timestamp_label': '[00:04:56]',
      'timestamp_seconds': 296,
      'tip': 'Will see that those 8% are exactly a mirrored here as well so we have parity in '
             'the two programs thank you that wraps my session on CSP pricing margins and '
             'incentives.',
      'title': 'CSP Licensing, Margins & Incentives (Demystifying Microsoft SMB Office Mix '
               'Series)',
      'url': 'https://www.youtube.com/watch?v=wzXR-g6_lxo&t=296s',
      'video_id': 'wzXR-g6_lxo'},
     {'author': 'PartnerPortal io',
      'channel': 'PartnerPortal io',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=KpcTpbw5dho&t=20s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'With resellers, the reseller usually owns the customer relationship. They bill '
              'the customer and keep their margin, and you bill them the wholesale price. So '
              "there's no commission to pay. You set this up in Payment Settings, on the "
              'Partner Model card.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'With resellers, the reseller usually owns the customer relationship. They bill '
             'the customer and keep their margin, and you bill them the wholesale price. So '
             "there's no commission to pay. You set this up in Payment Settings, on the "
             'Partner Model card.',
      'title': 'How to Set Up Reseller Partners | PartnerPortal Tutorial (PartnerPortal io)',
      'url': 'https://www.youtube.com/watch?v=KpcTpbw5dho&t=20s',
      'video_id': 'KpcTpbw5dho'},
     {'author': 'Flexera | ITAM, FinOps & SaaS Management',
      'channel': 'Flexera | ITAM, FinOps & SaaS Management',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=2ns7Rlmm4GA&t=157s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "In order to have a true view of what potential savings could be achieved, it's "
              'important to add in the cost data. Over here details, edit subscription. '
              'Remember to update the cost per unit, purchase date, as well as the start and '
              'end dates.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': "In order to have a true view of what potential savings could be achieved, it's "
             'important to add in the cost data. Over here details, edit subscription. '
             'Remember to update the cost per unit, purchase date, as well as the start and '
             'end dates.',
      'title': 'SaaS Renewal Management | How to Manage Renewals with SaaS‑Only Vendors | '
               'Flexera (Flexera | ITAM, FinOps & SaaS Management)',
      'url': 'https://www.youtube.com/watch?v=2ns7Rlmm4GA&t=157s',
      'video_id': '2ns7Rlmm4GA'},
     {'author': 'SPK and Associates',
      'channel': 'SPK and Associates',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:59](https://www.youtube.com/watch?v=Y8SGLxkUJd8&t=299s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Yeah, so like you mentioned, the licensing landscape is changing a lot. Um '
              "we're seeing a lot more cloud subscriptions, um bundled products, and really "
              'this usage-based pricing, which has become pretty universal across all our '
              'vendors.',
      'timestamp': 299,
      'timestamp_label': '[00:04:59]',
      'timestamp_seconds': 299,
      'tip': "Yeah, so like you mentioned, the licensing landscape is changing a lot. Um we're "
             'seeing a lot more cloud subscriptions, um bundled products, and really this '
             'usage-based pricing, which has become pretty universal across all our vendors.',
      'title': 'Strategies for Optimizing Software License Costs (SPK and Associates)',
      'url': 'https://www.youtube.com/watch?v=Y8SGLxkUJd8&t=299s',
      'video_id': 'Y8SGLxkUJd8'},
     {'author': 'Viktor from Sales',
      'channel': 'Viktor from Sales',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:54](https://www.youtube.com/watch?v=6Z4v3jibmMw&t=1014s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You decide upfront who's going to be working how much on the deal so you have "
              "you you know fully who's going to earn what commission from that deal and I.",
      'timestamp': 1014,
      'timestamp_label': '[00:16:54]',
      'timestamp_seconds': 1014,
      'tip': "You decide upfront who's going to be working how much on the deal so you have "
             "you you know fully who's going to earn what commission from that deal and I.",
      'title': '5 Things Every Channel Partner Program Needs (Viktor from Sales)',
      'url': 'https://www.youtube.com/watch?v=6Z4v3jibmMw&t=1014s',
      'video_id': '6Z4v3jibmMw'},
     {'author': 'INFOC',
      'channel': 'INFOC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:07](https://www.youtube.com/watch?v=IpCHEJpOqrE&t=127s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Item charges help businesses account for costs beyond the base purchase price, '
              'such as freight, handling, or other landed costs.',
      'timestamp': 127,
      'timestamp_label': '[00:02:07]',
      'timestamp_seconds': 127,
      'tip': 'Item charges help businesses account for costs beyond the base purchase price, '
             'such as freight, handling, or other landed costs.',
      'title': 'Purchasing and Payables in Business Central | Vendor, Orders, Invoices & '
               'Payments Explained (INFOC)',
      'url': 'https://www.youtube.com/watch?v=IpCHEJpOqrE&t=127s',
      'video_id': 'IpCHEJpOqrE'},
     {'author': 'Amazon Web Services',
      'channel': 'Amazon Web Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=GMejbloTwGE&t=98s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Marketplace along with the AWS Service Catalog allows enterprise customers a '
              'lot of freedom and flexibility and also cost savings AWS is a highly available.',
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': 'Marketplace along with the AWS Service Catalog allows enterprise customers a lot '
             'of freedom and flexibility and also cost savings AWS is a highly available.',
      'title': 'AWS Consulting Partner Case Study with AWS Marketplace and AWS Service Catalog '
               '(Amazon Web Services)',
      'url': 'https://www.youtube.com/watch?v=GMejbloTwGE&t=98s',
      'video_id': 'GMejbloTwGE'},
     {'author': 'NetSuite',
      'channel': 'NetSuite',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:27](https://www.youtube.com/watch?v=5hYAlGkuizk&t=147s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Processes by bringing together the bid the vendors and the awards into a single '
              'spot I can create my RFQ by entering the items that I want as well as the '
              'additional pricing tiers that should be applied.',
      'timestamp': 147,
      'timestamp_label': '[00:02:27]',
      'timestamp_seconds': 147,
      'tip': 'Processes by bringing together the bid the vendors and the awards into a single '
             'spot I can create my RFQ by entering the items that I want as well as the '
             'additional pricing tiers that should be applied.',
      'title': 'NetSuite Procurement (NetSuite)',
      'url': 'https://www.youtube.com/watch?v=5hYAlGkuizk&t=147s',
      'video_id': '5hYAlGkuizk'},
     {'author': 'Amazon Web Services',
      'channel': 'Amazon Web Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:55](https://www.youtube.com/watch?v=dkBRJN0WvX8&t=535s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Months and then this allows me to provide the pricing that I'm setting as a "
              'seller for the reseller and that could be an isv or a Consulting partner or a '
              'channel partner I can select the opportunity.',
      'timestamp': 535,
      'timestamp_label': '[00:08:55]',
      'timestamp_seconds': 535,
      'tip': "Months and then this allows me to provide the pricing that I'm setting as a "
             'seller for the reseller and that could be an isv or a Consulting partner or a '
             'channel partner I can select the opportunity.',
      'title': 'Reselling Professional Services in AWS Marketplace | Amazon Web Services '
               '(Amazon Web Services)',
      'url': 'https://www.youtube.com/watch?v=dkBRJN0WvX8&t=535s',
      'video_id': 'dkBRJN0WvX8'},
     {'author': 'ISM New Jersey',
      'channel': 'ISM New Jersey',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:55:20](https://www.youtube.com/watch?v=ZeVBT8JVp-U&t=3320s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Today and we'll be sending we'll have this uh recording published uh soon very "
              'shortly great thank you bye then bye for now bye bye everybody bye.',
      'timestamp': 3320,
      'timestamp_label': '[00:55:20]',
      'timestamp_seconds': 3320,
      'tip': "Today and we'll be sending we'll have this uh recording published uh soon very "
             'shortly great thank you bye then bye for now bye bye everybody bye.',
      'title': 'Professional Services Category Spotlight (ISM New Jersey)',
      'url': 'https://www.youtube.com/watch?v=ZeVBT8JVp-U&t=3320s',
      'video_id': 'ZeVBT8JVp-U'}],
 4: [{'author': 'Boring, But Billions',
      'channel': 'Boring, But Billions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:53](https://www.youtube.com/watch?v=ZFZMcTSC-0M&t=713s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Web Services, Google Cloud, Microsoft tools, and frontline cybersecurity '
              'software from CrowdStrike and Palo Alto Networks. If the Pentagon suspended '
              'Carahsoft tomorrow, military IT systems would freeze.',
      'timestamp': 713,
      'timestamp_label': '[00:11:53]',
      'timestamp_seconds': 713,
      'tip': 'Web Services, Google Cloud, Microsoft tools, and frontline cybersecurity '
             'software from CrowdStrike and Palo Alto Networks. If the Pentagon suspended '
             'Carahsoft tomorrow, military IT systems would freeze.',
      'title': "The Government's Biggest Software Middleman Exposed (Boring, But Billions)",
      'url': 'https://www.youtube.com/watch?v=ZFZMcTSC-0M&t=713s',
      'video_id': 'ZFZMcTSC-0M'},
     {'author': 'Iron Software',
      'channel': 'Iron Software',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=lCobx44k0Tw&t=25s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So first, who is this program for? It's for software distributors, regional "
              'channel partners, and value-added resellers with developer customers. If your '
              "audience is asking for PDF, document, OCR, or barcode tools, you're in the "
              'right place.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': "So first, who is this program for? It's for software distributors, regional "
             'channel partners, and value-added resellers with developer customers. If your '
             "audience is asking for PDF, document, OCR, or barcode tools, you're in the right "
             'place.',
      'title': 'Join the Iron Software Reseller Partner Program (Iron Software)',
      'url': 'https://www.youtube.com/watch?v=lCobx44k0Tw&t=25s',
      'video_id': 'lCobx44k0Tw'},
     {'author': 'Virtualization Options LLC Free Learning Portal',
      'channel': 'Virtualization Options LLC Free Learning Portal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:29](https://www.youtube.com/watch?v=L-DrE5qghM8&t=29s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Virtualization Options LLC. Their comprehensive guide essentially equips us '
              'with the exact frameworks we need to neutralize aggressive software sales '
              'tactics and ultimately protect our corporate capital.',
      'timestamp': 29,
      'timestamp_label': '[00:00:29]',
      'timestamp_seconds': 29,
      'tip': 'Virtualization Options LLC. Their comprehensive guide essentially equips us with '
             'the exact frameworks we need to neutralize aggressive software sales tactics and '
             'ultimately protect our corporate capital.',
      'title': 'Enterprise Procurement Secrets: How to Win the License Audit War '
               '(Virtualization Options LLC Free Learning Portal)',
      'url': 'https://www.youtube.com/watch?v=L-DrE5qghM8&t=29s',
      'video_id': 'L-DrE5qghM8'},
     {'author': '[mnainstitute.com] M&A Certification & Courses',
      'channel': '[mnainstitute.com] M&A Certification & Courses',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=7IqQXBLa14Y&t=71s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A software license that transfers control at a single point in time is '
              'recognized immediately upon delivery. A cloud subscription that delivers '
              'service continuously over a contract period is recognized ratably each month '
              'over that period.',
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': 'A software license that transfers control at a single point in time is '
             'recognized immediately upon delivery. A cloud subscription that delivers service '
             'continuously over a contract period is recognized ratably each month over that '
             'period.',
      'title': 'Revenue Recognition ASC 606 & IFRS 15 — 5-Step Quality Test with AI ⭐ '
               'mnainstitute.com ([mnainstitute.com] M&A Certification & Courses)',
      'url': 'https://www.youtube.com/watch?v=7IqQXBLa14Y&t=71s',
      'video_id': '7IqQXBLa14Y'},
     {'author': 'CFO AI',
      'channel': 'CFO AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=MAsF2w47iew&t=20s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You know, imagine your company sells a big bundle deal. It's got a software "
              'license, a full year of maintenance, and maybe some professional services '
              "thrown in. You get one single payment, but the value you're delivering that "
              'happens over completely different timelines.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "You know, imagine your company sells a big bundle deal. It's got a software "
             'license, a full year of maintenance, and maybe some professional services thrown '
             "in. You get one single payment, but the value you're delivering that happens "
             'over completely different timelines.',
      'title': 'NetSuite Advanced Revenue Management ASC 606 ARM (CFO AI)',
      'url': 'https://www.youtube.com/watch?v=MAsF2w47iew&t=20s',
      'video_id': 'MAsF2w47iew'},
     {'author': 'Eye on Tech',
      'channel': 'Eye on Tech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:58](https://www.youtube.com/watch?v=WEqXH4PuF8c&t=58s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'VARs often offer products and services like extended warranties, service '
              'contracts, supplemental hardware, software and installation and setup services. '
              'Working with a value added reseller can provide many benefits.',
      'timestamp': 58,
      'timestamp_label': '[00:00:58]',
      'timestamp_seconds': 58,
      'tip': 'VARs often offer products and services like extended warranties, service '
             'contracts, supplemental hardware, software and installation and setup services. '
             'Working with a value added reseller can provide many benefits.',
      'title': 'What is a VAR (Value-Added Reseller)? (Eye on Tech)',
      'url': 'https://www.youtube.com/watch?v=WEqXH4PuF8c&t=58s',
      'video_id': 'WEqXH4PuF8c'},
     {'author': 'Ambition, Aligned with Devon Coombs',
      'channel': 'Ambition, Aligned with Devon Coombs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:22](https://www.youtube.com/watch?v=B4Ckh2wjlgc&t=922s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm just keeping the lights on because that's the standard way that we sold "
              'things in software converted to kind of our traditional cloud world versus '
              'those are the big two decision points. Am I stand ready delivering over time '
              'flat?',
      'timestamp': 922,
      'timestamp_label': '[00:15:22]',
      'timestamp_seconds': 922,
      'tip': "I'm just keeping the lights on because that's the standard way that we sold "
             'things in software converted to kind of our traditional cloud world versus those '
             'are the big two decision points. Am I stand ready delivering over time flat?',
      'title': 'Consumption Based Revenue Recognition: ASC 606 & Usage-Based Pricing (SaaS & '
               'Cloud Accounting) (Ambition, Aligned with Devon Coombs)',
      'url': 'https://www.youtube.com/watch?v=B4Ckh2wjlgc&t=922s',
      'video_id': 'B4Ckh2wjlgc'},
     {'author': 'MetrixData 360',
      'channel': 'MetrixData 360',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:09](https://www.youtube.com/watch?v=ViSmcebdPlM&t=1509s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'SVP said to me, he said, "No, Mike, actually, it was you knowing what to do '
              "with the data that was the foundation of the the deal. We didn't know what to "
              'do with it." So you have to know what to do with that data to turn it in, '
              'right?',
      'timestamp': 1509,
      'timestamp_label': '[00:25:09]',
      'timestamp_seconds': 1509,
      'tip': 'SVP said to me, he said, "No, Mike, actually, it was you knowing what to do with '
             "the data that was the foundation of the the deal. We didn't know what to do with "
             'it." So you have to know what to do with that data to turn it in, right?',
      'title': 'The Renewal Illusion: Why Software Vendor Discounts Matter Less Than Data '
               'Accuracy (MetrixData 360)',
      'url': 'https://www.youtube.com/watch?v=ViSmcebdPlM&t=1509s',
      'video_id': 'ViSmcebdPlM'},
     {'author': 'Cloud Trailz',
      'channel': 'Cloud Trailz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:01](https://www.youtube.com/watch?v=wMMt_gTxRls&t=61s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Salesforce, make it fit your business structure, your process. Um so, it tends '
              'to be uh what drives up the cost. Now, when you were thinking about Salesforce, '
              "you didn't have consulting in your budget, that's where this starts to go awry.",
      'timestamp': 61,
      'timestamp_label': '[00:01:01]',
      'timestamp_seconds': 61,
      'tip': 'Salesforce, make it fit your business structure, your process. Um so, it tends '
             'to be uh what drives up the cost. Now, when you were thinking about Salesforce, '
             "you didn't have consulting in your budget, that's where this starts to go awry.",
      'title': 'Salesforce License Cost Vs Consultant Cost: Why Consultants Often Cost More '
               'Than Licenses (Cloud Trailz)',
      'url': 'https://www.youtube.com/watch?v=wMMt_gTxRls&t=61s',
      'video_id': 'wMMt_gTxRls'},
     {'author': 'WIBU-SYSTEMS AG',
      'channel': 'WIBU-SYSTEMS AG',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:51](https://www.youtube.com/watch?v=BmR1sqXk9DA&t=231s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'As well there is a component like error management tracing or logging. The '
              'dashboards bring the data from CodeMeter License Central to SAP and visualize '
              'the connection between the data regarding SAP objects.',
      'timestamp': 231,
      'timestamp_label': '[00:03:51]',
      'timestamp_seconds': 231,
      'tip': 'As well there is a component like error management tracing or logging. The '
             'dashboards bring the data from CodeMeter License Central to SAP and visualize '
             'the connection between the data regarding SAP objects.',
      'title': 'Effortless SAP Integration with CodeMeter License Central: Scenarios, '
               'Benefits, and Key Features (WIBU-SYSTEMS AG)',
      'url': 'https://www.youtube.com/watch?v=BmR1sqXk9DA&t=231s',
      'video_id': 'BmR1sqXk9DA'},
     {'author': 'Amazon Web Services',
      'channel': 'Amazon Web Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=w6XECzZOfXY&t=20s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, to sell paid software licenses in AWS Marketplace, you must be a permanent '
              'resident, a citizen, or a business entity organized or incorporated in one of '
              'our eligible jurisdictions. Please take a moment to review our current list of '
              'eligible jurisdictions.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'Now, to sell paid software licenses in AWS Marketplace, you must be a permanent '
             'resident, a citizen, or a business entity organized or incorporated in one of '
             'our eligible jurisdictions. Please take a moment to review our current list of '
             'eligible jurisdictions.',
      'title': 'How to register as an AWS Marketplace seller | Amazon Web Services (Amazon Web '
               'Services)',
      'url': 'https://www.youtube.com/watch?v=w6XECzZOfXY&t=20s',
      'video_id': 'w6XECzZOfXY'},
     {'author': 'AT&T Business',
      'channel': 'AT&T Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=-gG3jIROESw&t=75s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, congratulations to to you and your team. You've really kept kept it super "
              "simple. You've made it really easy to apply hardware, the services, software, "
              'the the software software services, support, hardware, all that together.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': "So, congratulations to to you and your team. You've really kept kept it super "
             "simple. You've made it really easy to apply hardware, the services, software, "
             'the the software software services, support, hardware, all that together.',
      'title': 'AT&T Value Added Reseller Program: Empowering VAR Growth and Success (AT&T '
               'Business)',
      'url': 'https://www.youtube.com/watch?v=-gG3jIROESw&t=75s',
      'video_id': '-gG3jIROESw'},
     {'author': 'Phil Morettini',
      'channel': 'Phil Morettini',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:59](https://www.youtube.com/watch?v=L1YsH5QkIus&t=239s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's it for now I'll look forward to talking about many more software company "
              'management topics in another edition of martini on management.',
      'timestamp': 239,
      'timestamp_label': '[00:03:59]',
      'timestamp_seconds': 239,
      'tip': "That's it for now I'll look forward to talking about many more software company "
             'management topics in another edition of martini on management.',
      'title': 'Selling and Marketing Software Through the VAR Channel -Morettini on '
               'Management Video Edition (Phil Morettini)',
      'url': 'https://www.youtube.com/watch?v=L1YsH5QkIus&t=239s',
      'video_id': 'L1YsH5QkIus'},
     {'author': 'Zylo | The Leader in Enterprise SaaS Management',
      'channel': 'Zylo | The Leader in Enterprise SaaS Management',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:20](https://www.youtube.com/watch?v=Cm2h-fPMxJ8&t=320s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Renewal remember SAS renewal management is most effective when combined with '
              'inventory and license management be sure to check out the last two episodes for '
              "details on those two practices that's all I have for today thank you for "
              'joining and we will catch you next time.',
      'timestamp': 320,
      'timestamp_label': '[00:05:20]',
      'timestamp_seconds': 320,
      'tip': 'Renewal remember SAS renewal management is most effective when combined with '
             'inventory and license management be sure to check out the last two episodes for '
             "details on those two practices that's all I have for today thank you for joining "
             'and we will catch you next time.',
      'title': 'SaaS Renewal Management, Explained (Zylo | The Leader in Enterprise SaaS '
               'Management)',
      'url': 'https://www.youtube.com/watch?v=Cm2h-fPMxJ8&t=320s',
      'video_id': 'Cm2h-fPMxJ8'},
     {'author': 'Amazon Web Services',
      'channel': 'Amazon Web Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:53](https://www.youtube.com/watch?v=PVL4069oqC0&t=173s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Complete for a sas product you've just seen how to create a private offer for a "
              'software purchase transaction in aws marketplace you can learn more about this '
              "topic in the description and links for this video thanks for watching now it's "
              'your turn to try.',
      'timestamp': 173,
      'timestamp_label': '[00:02:53]',
      'timestamp_seconds': 173,
      'tip': "Complete for a sas product you've just seen how to create a private offer for a "
             'software purchase transaction in aws marketplace you can learn more about this '
             "topic in the description and links for this video thanks for watching now it's "
             'your turn to try.',
      'title': 'Create Private Offer in AWS Marketplace | Amazon Web Services (Amazon Web '
               'Services)',
      'url': 'https://www.youtube.com/watch?v=PVL4069oqC0&t=173s',
      'video_id': 'PVL4069oqC0'}],
 5: [{'author': 'Jobank CPA',
      'channel': 'Jobank CPA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:35](https://www.youtube.com/watch?v=KjWijHo8iMI&t=215s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The absolute biggest trap to avoid is assuming credit risk equals control. '
              'Resellers so often think, "Hey, I issue the invoice. I take the hit if the '
              'customer defaults, so obviously I\'m the principal." ASC 606 intentionally '
              'removed credit risk as a primary indicator.',
      'timestamp': 215,
      'timestamp_label': '[00:03:35]',
      'timestamp_seconds': 215,
      'tip': 'The absolute biggest trap to avoid is assuming credit risk equals control. '
             'Resellers so often think, "Hey, I issue the invoice. I take the hit if the '
             'customer defaults, so obviously I\'m the principal." ASC 606 intentionally '
             'removed credit risk as a primary indicator.',
      'title': 'Episode 16 ASC 606 Principal vs Agent Explained: Gross vs Net Revenue Rules '
               '(Jobank CPA)',
      'url': 'https://www.youtube.com/watch?v=KjWijHo8iMI&t=215s',
      'video_id': 'KjWijHo8iMI'},
     {'author': 'FinOps Foundation',
      'channel': 'FinOps Foundation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:26](https://www.youtube.com/watch?v=F-5GIklN_Ps&t=446s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That can inflate costs significantly. This is high risk on our agenda. We've "
              'collaborated across the business: security, finance, procurement, end-user '
              "services, enterprise architecture. What we've done is provide the vehicle — the "
              'data — to make the right decisions.',
      'timestamp': 446,
      'timestamp_label': '[00:07:26]',
      'timestamp_seconds': 446,
      'tip': "That can inflate costs significantly. This is high risk on our agenda. We've "
             'collaborated across the business: security, finance, procurement, end-user '
             "services, enterprise architecture. What we've done is provide the vehicle — the "
             'data — to make the right decisions.',
      'title': 'FinOps for SaaS: Realities of Managing SaaS Value at Danske Bank (FinOps '
               'Foundation)',
      'url': 'https://www.youtube.com/watch?v=F-5GIklN_Ps&t=446s',
      'video_id': 'F-5GIklN_Ps'},
     {'author': 'ZINFI Technologies, Inc.',
      'channel': 'ZINFI Technologies, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=lET3Wc2a74o&t=32s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Most partners do not use market development funds or MDF. In fact, our '
              'worldwide channel survey data shows as much as 60% of market development funds '
              'are not used on a quarterly basis.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': 'Most partners do not use market development funds or MDF. In fact, our worldwide '
             'channel survey data shows as much as 60% of market development funds are not '
             'used on a quarterly basis.',
      'title': 'Why Channel Partners Don’t Use Market Development Funds (MDF) (ZINFI '
               'Technologies, Inc.)',
      'url': 'https://www.youtube.com/watch?v=lET3Wc2a74o&t=32s',
      'video_id': 'lET3Wc2a74o'},
     {'author': 'Virtualization Options LLC Free Learning Portal',
      'channel': 'Virtualization Options LLC Free Learning Portal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=jVnAwe2gfHg&t=72s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then, avoiding the anchoring trap. Third, calculating total cost of ownership. '
              'Fourth, building your defense team. And finally, enforcing real vendor '
              "accountability. Let's kick things off with section one, the tech sales "
              'playbook.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': 'Then, avoiding the anchoring trap. Third, calculating total cost of ownership. '
             'Fourth, building your defense team. And finally, enforcing real vendor '
             "accountability. Let's kick things off with section one, the tech sales playbook.",
      'title': 'Vendor Contracts Are Designed to Fail You — Here Is the Fix (Virtualization '
               'Options LLC Free Learning Portal)',
      'url': 'https://www.youtube.com/watch?v=jVnAwe2gfHg&t=72s',
      'video_id': 'jVnAwe2gfHg'},
     {'author': 'Learn TPRM with Rahul Tyagi',
      'channel': 'Learn TPRM with Rahul Tyagi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=TjkI3hqYZJY&t=33s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This includes VPN access, SSO accounts, shared drives, cloud environments, and '
              'any privileged accounts. If access is still active after the contract ends, '
              "that's a risk you don't want to keep. Step two, secure your data.",
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': 'This includes VPN access, SSO accounts, shared drives, cloud environments, and '
             'any privileged accounts. If access is still active after the contract ends, '
             "that's a risk you don't want to keep. Step two, secure your data.",
      'title': 'Vendor Offboarding Checklist: How to Safely Remove a Third Party (Learn TPRM '
               'with Rahul Tyagi)',
      'url': 'https://www.youtube.com/watch?v=TjkI3hqYZJY&t=33s',
      'video_id': 'TjkI3hqYZJY'},
     {'author': 'Partner Insight',
      'channel': 'Partner Insight',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:05](https://www.youtube.com/watch?v=3uRf7nlQ_JY&t=125s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Experts and partnership leaders we will dive into Marketplace strategies '
              'internal buyin building relationships with the cloud and mastering coell join.',
      'timestamp': 125,
      'timestamp_label': '[00:02:05]',
      'timestamp_seconds': 125,
      'tip': 'Experts and partnership leaders we will dive into Marketplace strategies '
             'internal buyin building relationships with the cloud and mastering coell join.',
      'title': 'Why 2024 will be known as 📈 inflection point for marketplaces and partners -  '
               'w/ Jay McBain, Canalys (Partner Insight)',
      'url': 'https://www.youtube.com/watch?v=3uRf7nlQ_JY&t=125s',
      'video_id': '3uRf7nlQ_JY'},
     {'author': 'Stratos Cloud Alliance',
      'channel': 'Stratos Cloud Alliance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:25](https://www.youtube.com/watch?v=rV-Q2IVur6I&t=685s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re a direct bill partner, uh you know, your partnership basically could be at, "
              "you know, serious risk and we don't want partners to, you know, get to October "
              '1st and then be scrambling.',
      'timestamp': 685,
      'timestamp_label': '[00:11:25]',
      'timestamp_seconds': 685,
      'tip': "'re a direct bill partner, uh you know, your partnership basically could be at, "
             "you know, serious risk and we don't want partners to, you know, get to October "
             '1st and then be scrambling.',
      'title': 'New Requirements for Microsoft CSP Direct-Bill Partners: What You Need to Know '
               'Before October 1st (Stratos Cloud Alliance)',
      'url': 'https://www.youtube.com/watch?v=rV-Q2IVur6I&t=685s',
      'video_id': 'rV-Q2IVur6I'},
     {'author': 'Anglepoint',
      'channel': 'Anglepoint',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:31](https://www.youtube.com/watch?v=gWDTRf_kGHI&t=271s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Few companies that are fully run across all of finops and all of cloud but it '
              'is something that companies should strive for thank you for watching this video '
              'if you have any questions reach out to us at anglepoint.',
      'timestamp': 271,
      'timestamp_label': '[00:04:31]',
      'timestamp_seconds': 271,
      'tip': 'Few companies that are fully run across all of finops and all of cloud but it is '
             'something that companies should strive for thank you for watching this video if '
             'you have any questions reach out to us at anglepoint.',
      'title': 'FinOps Explained in 5 Minutes | What is FinOps? (Anglepoint)',
      'url': 'https://www.youtube.com/watch?v=gWDTRf_kGHI&t=271s',
      'video_id': 'gWDTRf_kGHI'},
     {'author': 'TD SYNNEX',
      'channel': 'TD SYNNEX',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=fllmKjJXmBk&t=85s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So the PHF Intelligence Hub was designed to provide a better event experience '
              'to our resellers and our vendors. And it does that through looking at key data '
              'metrics and specific channel insights and putting that in your hands in the '
              'app.',
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': 'So the PHF Intelligence Hub was designed to provide a better event experience to '
             'our resellers and our vendors. And it does that through looking at key data '
             'metrics and specific channel insights and putting that in your hands in the app.',
      'title': 'From Data to Decisions: Smarter Partner Growth with AI | Tech Talk (TD SYNNEX)',
      'url': 'https://www.youtube.com/watch?v=fllmKjJXmBk&t=85s',
      'video_id': 'fllmKjJXmBk'},
     {'author': 'Leader Academy',
      'channel': 'Leader Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:31](https://www.youtube.com/watch?v=GAif9Dapd50&t=1111s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Reserved instances are only prepaid for the compute component there will still '
              'be charges for for example for your disk usage data flow into region transfers '
              'etc etc as well.',
      'timestamp': 1111,
      'timestamp_label': '[00:18:31]',
      'timestamp_seconds': 1111,
      'tip': 'Reserved instances are only prepaid for the compute component there will still '
             'be charges for for example for your disk usage data flow into region transfers '
             'etc etc as well.',
      'title': 'Getting started as a Microsoft CSP | Transacting through Leader Cloud (Leader '
               'Academy)',
      'url': 'https://www.youtube.com/watch?v=GAif9Dapd50&t=1111s',
      'video_id': 'GAif9Dapd50'},
     {'author': 'UpperEdge, LLC',
      'channel': 'UpperEdge, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=x34vxEJV40A&t=64s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But the problem is, and this is a big one, and and these in these vendors could '
              "learn something by approaching this a little differently, is that they're still "
              'digging their heels on a few things.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': 'But the problem is, and this is a big one, and and these in these vendors could '
             "learn something by approaching this a little differently, is that they're still "
             'digging their heels on a few things.',
      'title': 'The Hidden Traps in SaaS Renewals: What Vendors Don’t Want You to Know '
               '(UpperEdge, LLC)',
      'url': 'https://www.youtube.com/watch?v=x34vxEJV40A&t=64s',
      'video_id': 'x34vxEJV40A'},
     {'author': 'Crimson Line - Solving IT',
      'channel': 'Crimson Line - Solving IT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:15](https://www.youtube.com/watch?v=pRWl0RalG28&t=135s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Wide commitment at a minimum of 500 users or devices with little flexibility to '
              'change quantities until anniversary CSP on the other hand does not have a '
              'minimum user requirement and thus accommodates customers of different sizes and '
              'types.',
      'timestamp': 135,
      'timestamp_label': '[00:02:15]',
      'timestamp_seconds': 135,
      'tip': 'Wide commitment at a minimum of 500 users or devices with little flexibility to '
             'change quantities until anniversary CSP on the other hand does not have a '
             'minimum user requirement and thus accommodates customers of different sizes and '
             'types.',
      'title': "What is Microsoft's Cloud Solution Provider program? (Crimson Line - Solving "
               'IT)',
      'url': 'https://www.youtube.com/watch?v=pRWl0RalG28&t=135s',
      'video_id': 'pRWl0RalG28'},
     {'author': 'SAMexpert TV – Microsoft Licensing and Cloud',
      'channel': 'SAMexpert TV – Microsoft Licensing and Cloud',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:40](https://www.youtube.com/watch?v=S-D4c7b8-94&t=880s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Specific scenarios which don't account for flexibility changes edge cases uh "
              'and scenarios that are not even edge case scenarios cannot cannot be even '
              'predicted.',
      'timestamp': 880,
      'timestamp_label': '[00:14:40]',
      'timestamp_seconds': 880,
      'tip': "Specific scenarios which don't account for flexibility changes edge cases uh and "
             'scenarios that are not even edge case scenarios cannot cannot be even predicted.',
      'title': 'Protecting Your Hosting Margin as the Rules of the Game Change (SAMexpert TV – '
               'Microsoft Licensing and Cloud)',
      'url': 'https://www.youtube.com/watch?v=S-D4c7b8-94&t=880s',
      'video_id': 'S-D4c7b8-94'},
     {'author': 'Positive Results',
      'channel': 'Positive Results',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:48](https://www.youtube.com/watch?v=z6rVTIy-FOg&t=228s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'As your partner even if the solution we show is the right fit for your business '
              'our relationship with you is something we cherish we will always be honest '
              'ethical and upfront in everything we do thanks for watching and we hope to '
              'speak with you soon.',
      'timestamp': 228,
      'timestamp_label': '[00:03:48]',
      'timestamp_seconds': 228,
      'tip': 'As your partner even if the solution we show is the right fit for your business '
             'our relationship with you is something we cherish we will always be honest '
             'ethical and upfront in everything we do thanks for watching and we hope to speak '
             'with you soon.',
      'title': 'Value Added Reseller Explained - Should You Utilize One? (Positive Results)',
      'url': 'https://www.youtube.com/watch?v=z6rVTIy-FOg&t=228s',
      'video_id': 'z6rVTIy-FOg'},
     {'author': 'Zylo | The Leader in Enterprise SaaS Management',
      'channel': 'Zylo | The Leader in Enterprise SaaS Management',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:41:10](https://www.youtube.com/watch?v=8wZiGBXdOBo&t=2470s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Consolidating to one term and you're showing them hey this is the full scope of "
              'the relationship and this is how much we should be getting off based on this '
              'full scope not instance to instance all right let me see I think this is our '
              'final.',
      'timestamp': 2470,
      'timestamp_label': '[00:41:10]',
      'timestamp_seconds': 2470,
      'tip': "Consolidating to one term and you're showing them hey this is the full scope of "
             'the relationship and this is how much we should be getting off based on this '
             'full scope not instance to instance all right let me see I think this is our '
             'final.',
      'title': '4 Secrets to SaaS Subscription Renewals (Zylo | The Leader in Enterprise SaaS '
               'Management)',
      'url': 'https://www.youtube.com/watch?v=8wZiGBXdOBo&t=2470s',
      'video_id': '8wZiGBXdOBo'}],
 6: [{'author': 'Pax8 APAC',
      'channel': 'Pax8 APAC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:32](https://www.youtube.com/watch?v=Xywyds1IfvM&t=152s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'CSP program and CSP is a cloud solution provider. So, as we look at some of '
              'these changes that are happening in the CSP program, can you just kind of give '
              'us a bit of an overview and what does that mean for partners that are buying '
              'through the channel versus direct?',
      'timestamp': 152,
      'timestamp_label': '[00:02:32]',
      'timestamp_seconds': 152,
      'tip': 'CSP program and CSP is a cloud solution provider. So, as we look at some of '
             'these changes that are happening in the CSP program, can you just kind of give '
             'us a bit of an overview and what does that mean for partners that are buying '
             'through the channel versus direct?',
      'title': 'Microsoft CSP Direct vs Indirect: Which Model Saves You More? (Pax8 APAC)',
      'url': 'https://www.youtube.com/watch?v=Xywyds1IfvM&t=152s',
      'video_id': 'Xywyds1IfvM'},
     {'author': 'AWS Partner Network',
      'channel': 'AWS Partner Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:38](https://www.youtube.com/watch?v=OhzDVC956Os&t=158s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Partner to resell their software listings in aws marketplace and can offer a '
              "discount off the public list price creating the consulting partner's wholesale "
              'price multiple discount types are supported.',
      'timestamp': 158,
      'timestamp_label': '[00:02:38]',
      'timestamp_seconds': 158,
      'tip': 'Partner to resell their software listings in aws marketplace and can offer a '
             "discount off the public list price creating the consulting partner's wholesale "
             'price multiple discount types are supported.',
      'title': 'Channel Partner Private Offers in AWS Marketplace (AWS Partner Network)',
      'url': 'https://www.youtube.com/watch?v=OhzDVC956Os&t=158s',
      'video_id': 'OhzDVC956Os'},
     {'author': 'Channel Partners Events',
      'channel': 'Channel Partners Events',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:37](https://www.youtube.com/watch?v=SwebwmaZR2I&t=97s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's also one and a half times if you look to the left at cloud infrastructure, "
              'larger than the hyperscalers, not just AWS, Microsoft, and Google, but all of '
              'the Alibabas and Oracles and everyone down the list.',
      'timestamp': 97,
      'timestamp_label': '[00:01:37]',
      'timestamp_seconds': 97,
      'tip': "It's also one and a half times if you look to the left at cloud infrastructure, "
             'larger than the hyperscalers, not just AWS, Microsoft, and Google, but all of '
             'the Alibabas and Oracles and everyone down the list.',
      'title': 'Jay McBain Canalys 2025 (Channel Partners Events)',
      'url': 'https://www.youtube.com/watch?v=SwebwmaZR2I&t=97s',
      'video_id': 'SwebwmaZR2I'},
     {'author': 'Willingness to Pay',
      'channel': 'Willingness to Pay',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:27](https://www.youtube.com/watch?v=_pp2kmBgn7s&t=1647s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Them in through a sales funnel so they would qualify the leads they would do '
              'the initial first call with the customer explain the product and then they '
              'would.',
      'timestamp': 1647,
      'timestamp_label': '[00:27:27]',
      'timestamp_seconds': 1647,
      'tip': 'Them in through a sales funnel so they would qualify the leads they would do the '
             'initial first call with the customer explain the product and then they would.',
      'title': 'SaaS Partners & Resellers [Lessons From 30+ Client Projects] (Willingness to '
               'Pay)',
      'url': 'https://www.youtube.com/watch?v=_pp2kmBgn7s&t=1647s',
      'video_id': '_pp2kmBgn7s'},
     {'author': 'AWS Events',
      'channel': 'AWS Events',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:36](https://www.youtube.com/watch?v=K-GonrtXvKA&t=756s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Marketplace, become leads, and get access to larger deals in the private offer. '
              'Another way to sell more is to leverage channel partners on AWS Marketplace to '
              'help you resell and distribute your product.',
      'timestamp': 756,
      'timestamp_label': '[00:12:36]',
      'timestamp_seconds': 756,
      'tip': 'Marketplace, become leads, and get access to larger deals in the private offer. '
             'Another way to sell more is to leverage channel partners on AWS Marketplace to '
             'help you resell and distribute your product.',
      'title': "AWS re:Invent 2024 - Custom pricing: What's new with AWS Marketplace private "
               'offers (PEX113) (AWS Events)',
      'url': 'https://www.youtube.com/watch?v=K-GonrtXvKA&t=756s',
      'video_id': 'K-GonrtXvKA'},
     {'author': 'CRN',
      'channel': 'CRN',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:41](https://www.youtube.com/watch?v=ULy4t5kvUt0&t=1301s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ve just alluded to um the channel and tech enablement very much thrive and "
              "depend on um strong relationships. Um, to that end, I'd love to find out more "
              'about the day-to-day um, within the TD Synex services business. Um, you lead a '
              'geographically diverse team.',
      'timestamp': 1301,
      'timestamp_label': '[00:21:41]',
      'timestamp_seconds': 1301,
      'tip': "'ve just alluded to um the channel and tech enablement very much thrive and "
             "depend on um strong relationships. Um, to that end, I'd love to find out more "
             'about the day-to-day um, within the TD Synex services business. Um, you lead a '
             'geographically diverse team.',
      'title': 'TD SYNNEX: Helping partners deliver across the full technology lifecycle (CRN)',
      'url': 'https://www.youtube.com/watch?v=ULy4t5kvUt0&t=1301s',
      'video_id': 'ULy4t5kvUt0'},
     {'author': 'Scogo AI',
      'channel': 'Scogo AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:07](https://www.youtube.com/watch?v=hkNjUpPIx6M&t=127s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It has first of all identify the 365 business licenses can use those identify '
              'targeted user strip their business license and verify the reclamation. It has '
              'first of all search for all the licenses. It has found that okay, I have 25 '
              'licenses for SPB and I have four consumer.',
      'timestamp': 127,
      'timestamp_label': '[00:02:07]',
      'timestamp_seconds': 127,
      'tip': 'It has first of all identify the 365 business licenses can use those identify '
             'targeted user strip their business license and verify the reclamation. It has '
             'first of all search for all the licenses. It has found that okay, I have 25 '
             'licenses for SPB and I have four consumer.',
      'title': 'Advanced FinOps License Optimization in Microsoft 365 (Scogo AI)',
      'url': 'https://www.youtube.com/watch?v=hkNjUpPIx6M&t=127s',
      'video_id': 'hkNjUpPIx6M'},
     {'author': 'FinOps Weekly',
      'channel': 'FinOps Weekly',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:06](https://www.youtube.com/watch?v=sqpO85TKjEI&t=306s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, what are the tips that you got from from your talk and from your teammates '
              'and also from from the audience? Yeah, so first was having a central source of '
              "truth, right? A list of your SaaS vendors. A lot of organizations, you don't "
              'know where it all is, right?',
      'timestamp': 306,
      'timestamp_label': '[00:05:06]',
      'timestamp_seconds': 306,
      'tip': 'So, what are the tips that you got from from your talk and from your teammates '
             'and also from from the audience? Yeah, so first was having a central source of '
             "truth, right? A list of your SaaS vendors. A lot of organizations, you don't "
             'know where it all is, right?',
      'title': 'The Complete SaaS FinOps Playbook Explained in 17 Minutes | FinOps X Interview '
               '(FinOps Weekly)',
      'url': 'https://www.youtube.com/watch?v=sqpO85TKjEI&t=306s',
      'video_id': 'sqpO85TKjEI'},
     {'author': 'SuperTraining',
      'channel': 'SuperTraining',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:23](https://www.youtube.com/watch?v=EgxNMaMzml0&t=23s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And if you click this without going to the right there with the list and '
              'search, if you just click on Enter purchase order, it will actually take you to '
              'a blank purchase order to fill out. So here we are on our purchase order, so '
              "let's go down.",
      'timestamp': 23,
      'timestamp_label': '[00:00:23]',
      'timestamp_seconds': 23,
      'tip': 'And if you click this without going to the right there with the list and search, '
             'if you just click on Enter purchase order, it will actually take you to a blank '
             "purchase order to fill out. So here we are on our purchase order, so let's go "
             'down.',
      'title': 'NetSuite Procure to Pay Example (SuperTraining)',
      'url': 'https://www.youtube.com/watch?v=EgxNMaMzml0&t=23s',
      'video_id': 'EgxNMaMzml0'},
     {'author': 'TD SYNNEX',
      'channel': 'TD SYNNEX',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:22](https://www.youtube.com/watch?v=LRb1jC_Ao-s&t=382s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So this comes from McKinsey. Some of this is internal because I'll be honest I "
              "didn't but you know 1. But we want to be the first commercial distributor in "
              "space. And so the thing is you don't have to be a space expert.",
      'timestamp': 382,
      'timestamp_label': '[00:06:22]',
      'timestamp_seconds': 382,
      'tip': "So this comes from McKinsey. Some of this is internal because I'll be honest I "
             "didn't but you know 1. But we want to be the first commercial distributor in "
             "space. And so the thing is you don't have to be a space expert.",
      'title': 'The Space Economy: New Opportunities for the IT Channel | Tech Talk (TD '
               'SYNNEX)',
      'url': 'https://www.youtube.com/watch?v=LRb1jC_Ao-s&t=382s',
      'video_id': 'LRb1jC_Ao-s'},
     {'author': 'FinOps Foundation',
      'channel': 'FinOps Foundation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:11](https://www.youtube.com/watch?v=iIwpcQbBkmM&t=1091s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Cost and so we're starting to really see an uptick in finops being tapped to "
              "come in and do what we're doing with cloud and taking that and applying it to "
              'consumption based.',
      'timestamp': 1091,
      'timestamp_label': '[00:18:11]',
      'timestamp_seconds': 1091,
      'tip': "Cost and so we're starting to really see an uptick in finops being tapped to "
             "come in and do what we're doing with cloud and taking that and applying it to "
             'consumption based.',
      'title': 'Applying the FinOps Framework to SaaS at Scale (FinOps Foundation)',
      'url': 'https://www.youtube.com/watch?v=iIwpcQbBkmM&t=1091s',
      'video_id': 'iIwpcQbBkmM'},
     {'author': 'Ingram Micro Cloud UK',
      'channel': 'Ingram Micro Cloud UK',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:41](https://www.youtube.com/watch?v=M5I7gKJnNwU&t=221s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you would like to find out more about anything you've heard in this video "
              "please don't hesitate to contact the specialist clarity on the details provided "
              'thank you for taking the time to watch this video and I look forward to '
              'connecting with you soon.',
      'timestamp': 221,
      'timestamp_label': '[00:03:41]',
      'timestamp_seconds': 221,
      'tip': "If you would like to find out more about anything you've heard in this video "
             "please don't hesitate to contact the specialist clarity on the details provided "
             'thank you for taking the time to watch this video and I look forward to '
             'connecting with you soon.',
      'title': 'Introduction to Ingram Micro Cloud (Ingram Micro Cloud UK)',
      'url': 'https://www.youtube.com/watch?v=M5I7gKJnNwU&t=221s',
      'video_id': 'M5I7gKJnNwU'},
     {'author': 'Stitchflow',
      'channel': 'Stitchflow',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=7vly2W7M-Ew&t=39s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'License counts filled up for you and everything is organized in one simple view '
              "so let's see how to get started with the app you can manually add an app such "
              'as picking from the list that we have and you can go on to edit and autofill '
              'the details.',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': 'License counts filled up for you and everything is organized in one simple view '
             "so let's see how to get started with the app you can manually add an app such as "
             'picking from the list that we have and you can go on to edit and autofill the '
             'details.',
      'title': 'Renewal Tracker - A free tool to organize SaaS contracts, track renewals & get '
               'auto-reminders (Stitchflow)',
      'url': 'https://www.youtube.com/watch?v=7vly2W7M-Ew&t=39s',
      'video_id': '7vly2W7M-Ew'},
     {'author': 'Tom Bruining',
      'channel': 'Tom Bruining',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:28](https://www.youtube.com/watch?v=meEqyWq6yX0&t=508s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Little bit easier to do that sort of overarching story after the fact because '
              "you've it's all been planned and structured in the first.",
      'timestamp': 508,
      'timestamp_label': '[00:08:28]',
      'timestamp_seconds': 508,
      'tip': 'Little bit easier to do that sort of overarching story after the fact because '
             "you've it's all been planned and structured in the first.",
      'title': 'How to Create a SaaS Customer Case Study (Tom Bruining)',
      'url': 'https://www.youtube.com/watch?v=meEqyWq6yX0&t=508s',
      'video_id': 'meEqyWq6yX0'},
     {'author': 'Amazon Web Services',
      'channel': 'Amazon Web Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:28](https://www.youtube.com/watch?v=WP9Y1cRxhAI&t=208s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Can authorize you to resell their listing in AWS marketplace to become a seller '
              'of record you agree to the AWS marketplace terms which are the same terms sell '
              'for vendor sign when they list their products in AWS marketplace.',
      'timestamp': 208,
      'timestamp_label': '[00:03:28]',
      'timestamp_seconds': 208,
      'tip': 'Can authorize you to resell their listing in AWS marketplace to become a seller '
             'of record you agree to the AWS marketplace terms which are the same terms sell '
             'for vendor sign when they list their products in AWS marketplace.',
      'title': 'Getting Started with AWS Marketplace for Consulting Partners (Amazon Web '
               'Services)',
      'url': 'https://www.youtube.com/watch?v=WP9Y1cRxhAI&t=208s',
      'video_id': 'WP9Y1cRxhAI'}],
 7: [{'author': 'Ledger & Logic',
      'channel': 'Ledger & Logic',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=lYs19gfynCE&t=21s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We're going to unpack exactly how modern software companies actually process "
              "these super complex financial realities. Okay, here's our road map for today. "
              'Number one, the SaaS revenue illusion. Two, the ASC 606 five-step model. Three, '
              'surviving mid-cycle modifications.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "We're going to unpack exactly how modern software companies actually process "
             "these super complex financial realities. Okay, here's our road map for today. "
             'Number one, the SaaS revenue illusion. Two, the ASC 606 five-step model. Three, '
             'surviving mid-cycle modifications.',
      'title': 'ASC 606 Masterclass: Automating SaaS Revenue Recognition (Ledger & Logic)',
      'url': 'https://www.youtube.com/watch?v=lYs19gfynCE&t=21s',
      'video_id': 'lYs19gfynCE'},
     {'author': 'Accounting: Concierge CPA',
      'channel': 'Accounting: Concierge CPA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:18](https://www.youtube.com/watch?v=I8dBdXuT7cA&t=198s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Okay, so let's translate the steps. Step one of ASC 606 is to identify the "
              'contract with the customer. Now, this sounds obvious at first, but ASC 606 lays '
              'out specific criteria for what actually qualifies as a contract for revenue '
              'recognition purposes.',
      'timestamp': 198,
      'timestamp_label': '[00:03:18]',
      'timestamp_seconds': 198,
      'tip': "Okay, so let's translate the steps. Step one of ASC 606 is to identify the "
             'contract with the customer. Now, this sounds obvious at first, but ASC 606 lays '
             'out specific criteria for what actually qualifies as a contract for revenue '
             'recognition purposes.',
      'title': "ASC 606 Revenue Recognition in Plain English: A CPA's Walkthrough of the "
               '5-Step Model (Accounting: Concierge CPA)',
      'url': 'https://www.youtube.com/watch?v=I8dBdXuT7cA&t=198s',
      'video_id': 'I8dBdXuT7cA'},
     {'author': 'chanimalvideos',
      'channel': 'chanimalvideos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=hdz5UsJS-qY&t=15s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Building a SAS Channel a step-by-step approach within the material that I go '
              "through I'm going to talk about the channel I'm going to set up some.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Building a SAS Channel a step-by-step approach within the material that I go '
             "through I'm going to talk about the channel I'm going to set up some.",
      'title': 'How to Create a Reseller Program  - SaaS & Enterprise Software & Hardware '
               '(chanimalvideos)',
      'url': 'https://www.youtube.com/watch?v=hdz5UsJS-qY&t=15s',
      'video_id': 'hdz5UsJS-qY'},
     {'author': 'SecureOps with Ayden Connor',
      'channel': 'SecureOps with Ayden Connor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:48](https://www.youtube.com/watch?v=fOUGaSjlTBY&t=48s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If the vendor denies making the request, do not process the payment. Report the '
              'attempt to your IT and finance teams. If the vendor is unavailable, delay the '
              'payment until you can verify through a trusted channel.',
      'timestamp': 48,
      'timestamp_label': '[00:00:48]',
      'timestamp_seconds': 48,
      'tip': 'If the vendor denies making the request, do not process the payment. Report the '
             'attempt to your IT and finance teams. If the vendor is unavailable, delay the '
             'payment until you can verify through a trusted channel.',
      'title': 'Prevent Vendor Payment Fraud: A Step-by-Step Guide (SecureOps with Ayden '
               'Connor)',
      'url': 'https://www.youtube.com/watch?v=fOUGaSjlTBY&t=48s',
      'video_id': 'fOUGaSjlTBY'},
     {'author': 'PROKURIA',
      'channel': 'PROKURIA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:41](https://www.youtube.com/watch?v=_R1e9FCXKyI&t=161s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Well, it boils down to a structured uh six-step process, a kind of blueprint. '
              'First, pre-qualification and risk assessment before you really start. Screening '
              'against sanctions lists, credit checks, maybe initial ESG checks. So, weed out '
              'problems early makes sense.',
      'timestamp': 161,
      'timestamp_label': '[00:02:41]',
      'timestamp_seconds': 161,
      'tip': 'Well, it boils down to a structured uh six-step process, a kind of blueprint. '
             'First, pre-qualification and risk assessment before you really start. Screening '
             'against sanctions lists, credit checks, maybe initial ESG checks. So, weed out '
             'problems early makes sense.',
      'title': 'Vendor Onboarding Made Simple: Supplier Compliance and Management Tools '
               '(PROKURIA)',
      'url': 'https://www.youtube.com/watch?v=_R1e9FCXKyI&t=161s',
      'video_id': '_R1e9FCXKyI'},
     {'author': 'Plow Networks',
      'channel': 'Plow Networks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=KkM553ycNrA&t=39s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Safe hands getting started with plow networks as your Microsoft CSP is easy and '
              'it only takes four simple Steps step one fill out a quick form to share your.',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': 'Safe hands getting started with plow networks as your Microsoft CSP is easy and '
             'it only takes four simple Steps step one fill out a quick form to share your.',
      'title': 'How to transition to Plow Networks as your Microsoft CSP (Plow Networks)',
      'url': 'https://www.youtube.com/watch?v=KkM553ycNrA&t=39s',
      'video_id': 'KkM553ycNrA'},
     {'author': 'Datadog',
      'channel': 'Datadog',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:54](https://www.youtube.com/watch?v=hmqskc5iaNc&t=1014s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Zones we paid a lot of money for it so this was a really nice save and this is '
              "relevant for not only elasticsearch right if you're using uh Kafka Kinesis on "
              'every every distributed system that moves a lot of data uh from uh regions or '
              'availability zones.',
      'timestamp': 1014,
      'timestamp_label': '[00:16:54]',
      'timestamp_seconds': 1014,
      'tip': 'Zones we paid a lot of money for it so this was a really nice save and this is '
             "relevant for not only elasticsearch right if you're using uh Kafka Kinesis on "
             'every every distributed system that moves a lot of data uh from uh regions or '
             'availability zones.',
      'title': 'FinOps and Cloud Cost Optimization (Datadog)',
      'url': 'https://www.youtube.com/watch?v=hmqskc5iaNc&t=1014s',
      'video_id': 'hmqskc5iaNc'},
     {'author': 'rAVe [PUBS]',
      'channel': 'rAVe [PUBS]',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:23](https://www.youtube.com/watch?v=4HmZZT3HBnA&t=143s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And that's where our product managers and business development managers come "
              'into play can really dial in a specific solution for that opportunity and then '
              'again the folks that I mentioned earlier are going to be there throughout this '
              'entire process.',
      'timestamp': 143,
      'timestamp_label': '[00:02:23]',
      'timestamp_seconds': 143,
      'tip': "And that's where our product managers and business development managers come "
             'into play can really dial in a specific solution for that opportunity and then '
             'again the folks that I mentioned earlier are going to be there throughout this '
             'entire process.',
      'title': 'InfoComm 2025: TD SYNNEX’s Graham Kelly Talks Integrator Needs, Value-Added '
               'Distribution and More (rAVe [PUBS])',
      'url': 'https://www.youtube.com/watch?v=4HmZZT3HBnA&t=143s',
      'video_id': '4HmZZT3HBnA'},
     {'author': 'LeadSquared',
      'channel': 'LeadSquared',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:14](https://www.youtube.com/watch?v=mR8B4VcLNjU&t=914s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now with system what you'll have is uh with system you'll have a data which is "
              'feeding which is processed driven. You can mandate the users to feed in the '
              'correct set of data at correct point.',
      'timestamp': 914,
      'timestamp_label': '[00:15:14]',
      'timestamp_seconds': 914,
      'tip': "Now with system what you'll have is uh with system you'll have a data which is "
             'feeding which is processed driven. You can mandate the users to feed in the '
             'correct set of data at correct point.',
      'title': 'Vendor Onboarding Process - What is Vendor Onboarding and How to Build an '
               'Optimal Process? (LeadSquared)',
      'url': 'https://www.youtube.com/watch?v=mR8B4VcLNjU&t=914s',
      'video_id': 'mR8B4VcLNjU'},
     {'author': 'Amazon Web Services',
      'channel': 'Amazon Web Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=iROp007IYLs&t=111s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'AWS Marketplace software catalog by vendor name delivery method operating '
              "system or pricing plan we'll search for a vendor that are organization has "
              'vetted and add the product to our private Marketplace.',
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': 'AWS Marketplace software catalog by vendor name delivery method operating system '
             "or pricing plan we'll search for a vendor that are organization has vetted and "
             'add the product to our private Marketplace.',
      'title': 'AWS Private Marketplace Overview (Amazon Web Services)',
      'url': 'https://www.youtube.com/watch?v=iROp007IYLs&t=111s',
      'video_id': 'iROp007IYLs'},
     {'author': 'The SaaS CFO',
      'channel': 'The SaaS CFO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=G9iKRE0cqZU&t=146s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Revenue retention and renewal rates on a dollar basis and on a account basis '
              "and typically we're pulling that data from our CRM system for those renewal.",
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': 'Revenue retention and renewal rates on a dollar basis and on a account basis and '
             "typically we're pulling that data from our CRM system for those renewal.",
      'title': 'How Do We Track Retention When We Offer Multi-year Contracts | SaaS Metrics '
               'School | Retention (The SaaS CFO)',
      'url': 'https://www.youtube.com/watch?v=G9iKRE0cqZU&t=146s',
      'video_id': 'G9iKRE0cqZU'},
     {'author': 'AWS Public Sector',
      'channel': 'AWS Public Sector',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=F4gkR0s1Blw&t=30s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Demonstrate the creation and acceptance of a private offer in AWS Marketplace '
              'both from the reseller side as well as showing you the customers.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'Demonstrate the creation and acceptance of a private offer in AWS Marketplace '
             'both from the reseller side as well as showing you the customers.',
      'title': 'Creating a private partner offer on AWS Marketplace for public sector '
               'customers - demo (AWS Public Sector)',
      'url': 'https://www.youtube.com/watch?v=F4gkR0s1Blw&t=30s',
      'video_id': 'F4gkR0s1Blw'},
     {'author': 'Vistack',
      'channel': 'Vistack',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=0I4GdLiHF5Y&t=77s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Important not to miss these steps once you have built your calendar the next '
              'things to do is to do some research about the vendors that you have to.',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': 'Important not to miss these steps once you have built your calendar the next '
             'things to do is to do some research about the vendors that you have to.',
      'title': 'Best Strategies to Renew SaaS Contracts (Vistack)',
      'url': 'https://www.youtube.com/watch?v=0I4GdLiHF5Y&t=77s',
      'video_id': '0I4GdLiHF5Y'},
     {'author': 'Channeltivity - Channel Partner Portal',
      'channel': 'Channeltivity - Channel Partner Portal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:14](https://www.youtube.com/watch?v=5iuG2nYpJ0U&t=194s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Pages and four is that's it you're done and ready to go thank you I hope you "
              "found this video helpful of course we're happy to provide additional details "
              "and answer any questions just get in touch if there's any way we can help.",
      'timestamp': 194,
      'timestamp_label': '[00:03:14]',
      'timestamp_seconds': 194,
      'tip': "Pages and four is that's it you're done and ready to go thank you I hope you "
             "found this video helpful of course we're happy to provide additional details and "
             "answer any questions just get in touch if there's any way we can help.",
      'title': "Integrate Salesforce w/ Channeltivity's PRM Software - Deal Registration and "
               'Lead Distribution (Channeltivity - Channel Partner Portal)',
      'url': 'https://www.youtube.com/watch?v=5iuG2nYpJ0U&t=194s',
      'video_id': '5iuG2nYpJ0U'},
     {'author': 'TD SYNNEX',
      'channel': 'TD SYNNEX',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:22](https://www.youtube.com/watch?v=5GVULJyWQFc&t=82s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I've never really expected. 's going to help you build your business and the "
              'practices that you have that are really the the pain points that our customers '
              'are going to need tomorrow and into the future.',
      'timestamp': 82,
      'timestamp_label': '[00:01:22]',
      'timestamp_seconds': 82,
      'tip': "I've never really expected. 's going to help you build your business and the "
             'practices that you have that are really the the pain points that our customers '
             'are going to need tomorrow and into the future.',
      'title': 'InaCOMP + TD SYNNEX: Making IT Personal (TD SYNNEX)',
      'url': 'https://www.youtube.com/watch?v=5GVULJyWQFc&t=82s',
      'video_id': '5GVULJyWQFc'}],
 8: [{'author': 'Eddy Says Hi #EddySaysHi',
      'channel': 'Eddy Says Hi #EddySaysHi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:18](https://www.youtube.com/watch?v=byD2FJ-NF0M&t=558s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So the shift isn't from auditing to not auditing. It's from scheduled scrutiny "
              'to pervasive real-time data scrutiny. This connects directly to trend 4. Then '
              'AI changes the economics of software and cloud in two very distinct ways.',
      'timestamp': 558,
      'timestamp_label': '[00:09:18]',
      'timestamp_seconds': 558,
      'tip': "So the shift isn't from auditing to not auditing. It's from scheduled scrutiny "
             'to pervasive real-time data scrutiny. This connects directly to trend 4. Then AI '
             'changes the economics of software and cloud in two very distinct ways.',
      'title': '(Podcast) Preparing for 2026: Software Licensing, ITAM and FinOps Trends (Eddy '
               'Says Hi #EddySaysHi)',
      'url': 'https://www.youtube.com/watch?v=byD2FJ-NF0M&t=558s',
      'video_id': 'byD2FJ-NF0M'},
     {'author': 'Kanerika Inc.',
      'channel': 'Kanerika Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:23](https://www.youtube.com/watch?v=mhNqARg0Yi8&t=503s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You are paying Databricks for the compute management software, but you are also '
              'paying your underlying cloud provider, like AWS or Google Cloud, separately for '
              'the actual infrastructure, the raw storage, and the networking.',
      'timestamp': 503,
      'timestamp_label': '[00:08:23]',
      'timestamp_seconds': 503,
      'tip': 'You are paying Databricks for the compute management software, but you are also '
             'paying your underlying cloud provider, like AWS or Google Cloud, separately for '
             'the actual infrastructure, the raw storage, and the networking.',
      'title': 'Databricks vs Snowflake 2026: Pricing, AI, Security Compared (Kanerika Inc.)',
      'url': 'https://www.youtube.com/watch?v=mhNqARg0Yi8&t=503s',
      'video_id': 'mhNqARg0Yi8'},
     {'author': 'The Data & AI Playground',
      'channel': 'The Data & AI Playground',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:54](https://www.youtube.com/watch?v=yhgHAMKkOqc&t=294s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Databricks is basically a purpose-built ML operations platform, MLflow for '
              'experiments tracking, feature stores, model serving endpoints, vector search '
              'for RAG applications, notebooks in Python, Scala, and R. The full MLops life '
              'cycle is native.',
      'timestamp': 294,
      'timestamp_label': '[00:04:54]',
      'timestamp_seconds': 294,
      'tip': 'Databricks is basically a purpose-built ML operations platform, MLflow for '
             'experiments tracking, feature stores, model serving endpoints, vector search for '
             'RAG applications, notebooks in Python, Scala, and R. The full MLops life cycle '
             'is native.',
      'title': 'Databricks vs Snowflake -Complete Architectural and Technical Decision '
               'Framework (The Data & AI Playground)',
      'url': 'https://www.youtube.com/watch?v=yhgHAMKkOqc&t=294s',
      'video_id': 'yhgHAMKkOqc'},
     {'author': 'TAP Innovations',
      'channel': 'TAP Innovations',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:24](https://www.youtube.com/watch?v=6_xruMdmmjM&t=24s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Commissions selling a dynamic cloud SAS web and mobile software platform to '
              'organizations in all industries in any geographical market with 50 to 10,000.',
      'timestamp': 24,
      'timestamp_label': '[00:00:24]',
      'timestamp_seconds': 24,
      'tip': 'Commissions selling a dynamic cloud SAS web and mobile software platform to '
             'organizations in all industries in any geographical market with 50 to 10,000.',
      'title': 'TAP Reseller/Channel Partner Video (TAP Innovations)',
      'url': 'https://www.youtube.com/watch?v=6_xruMdmmjM&t=24s',
      'video_id': '6_xruMdmmjM'},
     {'author': 'AWS Events',
      'channel': 'AWS Events',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:17](https://www.youtube.com/watch?v=cOyZpsRxxE4&t=257s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'll pace myself accordingly. So what Marketplace is, is a global, "
              'ever-expanding catalog of software products, services, and data products, and '
              'ML, and agents and tools. We recently launched the agents and tools category in '
              "July. So it's an ever-expanding catalog.",
      'timestamp': 257,
      'timestamp_label': '[00:04:17]',
      'timestamp_seconds': 257,
      'tip': "I'll pace myself accordingly. So what Marketplace is, is a global, "
             'ever-expanding catalog of software products, services, and data products, and '
             'ML, and agents and tools. We recently launched the agents and tools category in '
             "July. So it's an ever-expanding catalog.",
      'title': 'AWS re:Invent 2025 - Driving business outcomes with complete AWS Marketplace '
               'solutions (PEX111) (AWS Events)',
      'url': 'https://www.youtube.com/watch?v=cOyZpsRxxE4&t=257s',
      'video_id': 'cOyZpsRxxE4'},
     {'author': 'CSM Practice',
      'channel': 'CSM Practice',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:14](https://www.youtube.com/watch?v=OjPZFAoutfA&t=734s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It had some reporting capabilities so I think the bottom line is as long as you '
              'can harvest all your data from your crm system your crm system does not have '
              'great bis reporting tools.',
      'timestamp': 734,
      'timestamp_label': '[00:12:14]',
      'timestamp_seconds': 734,
      'tip': 'It had some reporting capabilities so I think the bottom line is as long as you '
             'can harvest all your data from your crm system your crm system does not have '
             'great bis reporting tools.',
      'title': 'SAAS RENEWALS Report and How to Analyze it (CSM Practice)',
      'url': 'https://www.youtube.com/watch?v=OjPZFAoutfA&t=734s',
      'video_id': 'OjPZFAoutfA'},
     {'author': 'Clovity',
      'channel': 'Clovity',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:00](https://www.youtube.com/watch?v=fwAcWt5Q8oA&t=180s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '12 to 15 core tools that um are associated alongside of about 2,000 plus '
              'marketplace add-ons um that are able to be purchased alongside these core '
              'products but enhance the kind of the out of the box tool which is awesome. No, '
              'I I just want to double click.',
      'timestamp': 180,
      'timestamp_label': '[00:03:00]',
      'timestamp_seconds': 180,
      'tip': '12 to 15 core tools that um are associated alongside of about 2,000 plus '
             'marketplace add-ons um that are able to be purchased alongside these core '
             'products but enhance the kind of the out of the box tool which is awesome. No, I '
             'I just want to double click.',
      'title': 'Streamline @Atlassian  Software Licensing & Procurement for Government | '
               'Clovity × Carahsoft (Clovity)',
      'url': 'https://www.youtube.com/watch?v=fwAcWt5Q8oA&t=180s',
      'video_id': 'fwAcWt5Q8oA'},
     {'author': 'Amazon Web Services',
      'channel': 'Amazon Web Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:55](https://www.youtube.com/watch?v=PkznZxwv3eg&t=415s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Dedicated to isv authorizations next we are going to see how consulting '
              'partners create a private author for this we are going to once again log into '
              'the aws marketplace management portal.',
      'timestamp': 415,
      'timestamp_label': '[00:06:55]',
      'timestamp_seconds': 415,
      'tip': 'Dedicated to isv authorizations next we are going to see how consulting partners '
             'create a private author for this we are going to once again log into the aws '
             'marketplace management portal.',
      'title': 'Consulting Partners Private Offers Overview (Amazon Web Services)',
      'url': 'https://www.youtube.com/watch?v=PkznZxwv3eg&t=415s',
      'video_id': 'PkznZxwv3eg'},
     {'author': 'PROKURIA',
      'channel': 'PROKURIA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:11](https://www.youtube.com/watch?v=_tfz6kZ8JZo&t=131s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Every element of this message is fully customizable. The supplier receives an '
              'access button that leads them to the supplier portal. No username or password '
              'is needed, just an email address added to the system by the vendor manager.',
      'timestamp': 131,
      'timestamp_label': '[00:02:11]',
      'timestamp_seconds': 131,
      'tip': 'Every element of this message is fully customizable. The supplier receives an '
             'access button that leads them to the supplier portal. No username or password is '
             'needed, just an email address added to the system by the vendor manager.',
      'title': 'Automate Supplier Onboarding | No-Code Procurement Tools (PROKURIA)',
      'url': 'https://www.youtube.com/watch?v=_tfz6kZ8JZo&t=131s',
      'video_id': '_tfz6kZ8JZo'},
     {'author': 'Virtualization Options LLC Free Learning Portal',
      'channel': 'Virtualization Options LLC Free Learning Portal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:19](https://www.youtube.com/watch?v=fTqBORy9ePo&t=439s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'TCO performance remedies, meaning if their projected savings fall below 75% in '
              'reality, you get a credit. Enforce automatic fee clawbacks for any SLA platform '
              'degradations.',
      'timestamp': 439,
      'timestamp_label': '[00:07:19]',
      'timestamp_seconds': 439,
      'tip': 'TCO performance remedies, meaning if their projected savings fall below 75% in '
             'reality, you get a credit. Enforce automatic fee clawbacks for any SLA platform '
             'degradations.',
      'title': 'Enterprise Software Vendors HATE When You Use This Negotiation Tactic '
               '(Virtualization Options LLC Free Learning Portal)',
      'url': 'https://www.youtube.com/watch?v=fTqBORy9ePo&t=439s',
      'video_id': 'fTqBORy9ePo'},
     {'author': 'ServiceNow Community',
      'channel': 'ServiceNow Community',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:39](https://www.youtube.com/watch?v=8mJc7j3DW28&t=99s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Information in one platform to help you make decisions quickly and efficiently '
              'the last option is a custom integration so if they have an open API then we '
              'can.',
      'timestamp': 99,
      'timestamp_label': '[00:01:39]',
      'timestamp_seconds': 99,
      'tip': 'Information in one platform to help you make decisions quickly and efficiently '
             'the last option is a custom integration so if they have an open API then we can.',
      'title': 'How To: SaaS License Management to reduce and optimize spend (ServiceNow '
               'Community)',
      'url': 'https://www.youtube.com/watch?v=8mJc7j3DW28&t=99s',
      'video_id': '8mJc7j3DW28'},
     {'author': 'Charted (formerly SquareWorks)',
      'channel': 'Charted (formerly SquareWorks)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:41](https://www.youtube.com/watch?v=1wlmLTmDAfc&t=1721s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "NetSuite maybe via an export and feeding that into whatever tool you're using "
              'for kind of your business management you can basically pull in all this '
              'information and these the raw data back into your BI tool and use that for '
              'downstream reporting, obviously.',
      'timestamp': 1721,
      'timestamp_label': '[00:28:41]',
      'timestamp_seconds': 1721,
      'tip': "NetSuite maybe via an export and feeding that into whatever tool you're using "
             'for kind of your business management you can basically pull in all this '
             'information and these the raw data back into your BI tool and use that for '
             'downstream reporting, obviously.',
      'title': 'The modern way to work with vendors in NetSuite: Faster onboarding, smoother '
               'invoices (Charted (formerly SquareWorks))',
      'url': 'https://www.youtube.com/watch?v=1wlmLTmDAfc&t=1721s',
      'video_id': '1wlmLTmDAfc'},
     {'author': 'TD SYNNEX',
      'channel': 'TD SYNNEX',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:14](https://www.youtube.com/watch?v=1Rg0jWCs65Y&t=554s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "StreamOne, if you're not familiar, it's our cloud platform. Well, a lot of our "
              'cloud vendors are within there. But imagine it just giving you that single '
              'location where you can keep track of all those opportunities.',
      'timestamp': 554,
      'timestamp_label': '[00:09:14]',
      'timestamp_seconds': 554,
      'tip': "StreamOne, if you're not familiar, it's our cloud platform. Well, a lot of our "
             'cloud vendors are within there. But imagine it just giving you that single '
             'location where you can keep track of all those opportunities.',
      'title': 'How PartnerFirst Is Simplifying B2B Commerce with AI | TD SYNNEX Inspire Tech '
               'Talk (TD SYNNEX)',
      'url': 'https://www.youtube.com/watch?v=1Rg0jWCs65Y&t=554s',
      'video_id': '1Rg0jWCs65Y'},
     {'author': 'samit',
      'channel': 'samit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:13](https://www.youtube.com/watch?v=bek-1YEtW80&t=313s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'At talk until O the Affordable simple fully managed predictably priced VoIP PBX '
              'platform learn more at taka Dillo comm and help to support Sam MIT.',
      'timestamp': 313,
      'timestamp_label': '[00:05:13]',
      'timestamp_seconds': 313,
      'tip': 'At talk until O the Affordable simple fully managed predictably priced VoIP PBX '
             'platform learn more at taka Dillo comm and help to support Sam MIT.',
      'title': 'What Is the Difference Between an MSP and a VAR (samit)',
      'url': 'https://www.youtube.com/watch?v=bek-1YEtW80&t=313s',
      'video_id': 'bek-1YEtW80'},
     {'author': 'Amazon Web Services',
      'channel': 'Amazon Web Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:22](https://www.youtube.com/watch?v=O_1B3vFfVJ4&t=442s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Private offer using the AWS partner CRM connector check out these resources to '
              'learn how to configure and use the partner CRM connector thanks for watching.',
      'timestamp': 442,
      'timestamp_label': '[00:07:22]',
      'timestamp_seconds': 442,
      'tip': 'Private offer using the AWS partner CRM connector check out these resources to '
             'learn how to configure and use the partner CRM connector thanks for watching.',
      'title': 'Create an AWS Marketplace Private Offer from your Salesforce CRM | Amazon Web '
               'Services (Amazon Web Services)',
      'url': 'https://www.youtube.com/watch?v=O_1B3vFfVJ4&t=442s',
      'video_id': 'O_1B3vFfVJ4'}],
 9: [{'author': 'Virtualization Options LLC Free Learning Portal',
      'channel': 'Virtualization Options LLC Free Learning Portal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:04](https://www.youtube.com/watch?v=rJtYtwh2Ees&t=244s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But, when internal champions let the vendor bypass the rules, we get trapped in '
              'vendor lock-in, face massive data migration costs, and take on severe legal and '
              'compliance exposure. Competitive bidding requirements.',
      'timestamp': 244,
      'timestamp_label': '[00:04:04]',
      'timestamp_seconds': 244,
      'tip': 'But, when internal champions let the vendor bypass the rules, we get trapped in '
             'vendor lock-in, face massive data migration costs, and take on severe legal and '
             'compliance exposure. Competitive bidding requirements.',
      'title': 'There are Consequences if an Employee Aids a Vendor in Circumventing Official '
               'Procurement Processes (Virtualization Options LLC Free Learning Portal)',
      'url': 'https://www.youtube.com/watch?v=rJtYtwh2Ees&t=244s',
      'video_id': 'rJtYtwh2Ees'},
     {'author': 'DevOps Simplified',
      'channel': 'DevOps Simplified',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:33](https://www.youtube.com/watch?v=YF1T0fd9wPE&t=153s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Legal and regulatory: what laws allow or require. Geography/jurisdiction: '
              "another country's law. Financial/ROI: is it worth the cost? Vendor lock-in: "
              'lost leverage. Assurance mechanisms: attestations, insurance, contract terms.',
      'timestamp': 153,
      'timestamp_label': '[00:02:33]',
      'timestamp_seconds': 153,
      'tip': 'Legal and regulatory: what laws allow or require. Geography/jurisdiction: '
             "another country's law. Financial/ROI: is it worth the cost? Vendor lock-in: lost "
             'leverage. Assurance mechanisms: attestations, insurance, contract terms.',
      'title': 'Third-Party Risk II: Vendor Monitoring and Rules of Engagement | CompTIA '
               'Security+ SY0-801 (DevOps Simplified)',
      'url': 'https://www.youtube.com/watch?v=YF1T0fd9wPE&t=153s',
      'video_id': 'YF1T0fd9wPE'},
     {'author': 'Amazon Web Services',
      'channel': 'Amazon Web Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:46](https://www.youtube.com/watch?v=pOUxsKDRzvM&t=106s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Here is the pricing that the seller has associated with the product. The seller '
              'has also associated a reseller contract, which the channel partner must accept, '
              "and an enduser license agreement that the buyer must accept. Here's a quick "
              'sneak peek of the reseller contract.',
      'timestamp': 106,
      'timestamp_label': '[00:01:46]',
      'timestamp_seconds': 106,
      'tip': 'Here is the pricing that the seller has associated with the product. The seller '
             'has also associated a reseller contract, which the channel partner must accept, '
             "and an enduser license agreement that the buyer must accept. Here's a quick "
             'sneak peek of the reseller contract.',
      'title': 'Creating AWS Marketplace Channel Partner private offers from your Salesforce '
               'CRM (Amazon Web Services)',
      'url': 'https://www.youtube.com/watch?v=pOUxsKDRzvM&t=106s',
      'video_id': 'pOUxsKDRzvM'},
     {'author': 'Stuart Sutton',
      'channel': 'Stuart Sutton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:46](https://www.youtube.com/watch?v=yasPH-UlTQo&t=286s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This will be to assist with additional training, answering how-to questions, '
              'and resolving basic data leveled issues. Ensuring the technology works in your '
              'local VAR area. This would include correcting language translations, setting up '
              'region specific compliance rules, etc.',
      'timestamp': 286,
      'timestamp_label': '[00:04:46]',
      'timestamp_seconds': 286,
      'tip': 'This will be to assist with additional training, answering how-to questions, and '
             'resolving basic data leveled issues. Ensuring the technology works in your local '
             'VAR area. This would include correcting language translations, setting up region '
             'specific compliance rules, etc.',
      'title': 'Value Added Reseller Overview (Stuart Sutton)',
      'url': 'https://www.youtube.com/watch?v=yasPH-UlTQo&t=286s',
      'video_id': 'yasPH-UlTQo'},
     {'author': 'Version 1',
      'channel': 'Version 1',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:25](https://www.youtube.com/watch?v=PLfTJs7m4ww&t=1405s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'One single enterprise agreement it does ease on license management headaches '
              "assuming that you've got the right process in place to take control of.",
      'timestamp': 1405,
      'timestamp_label': '[00:23:25]',
      'timestamp_seconds': 1405,
      'tip': 'One single enterprise agreement it does ease on license management headaches '
             "assuming that you've got the right process in place to take control of.",
      'title': 'Enable Software Procurement ROI with Microsoft CSP (Version 1)',
      'url': 'https://www.youtube.com/watch?v=PLfTJs7m4ww&t=1405s',
      'video_id': 'PLfTJs7m4ww'},
     {'author': 'Venduris',
      'channel': 'Venduris',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=saQOnMvtxrQ&t=120s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The gap between paid seats and active seats is your strongest negotiating '
              "point, and it doesn't depend on the vendor agreeing with you. Which brings us "
              'to SaaS renewal management: turning contract terms and usage data into a '
              'decision, on time.',
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': 'The gap between paid seats and active seats is your strongest negotiating point, '
             "and it doesn't depend on the vendor agreeing with you. Which brings us to SaaS "
             'renewal management: turning contract terms and usage data into a decision, on '
             'time.',
      'title': 'SaaS Contract Management, License Management & Renewal Management (Explained) '
               '(Venduris)',
      'url': 'https://www.youtube.com/watch?v=saQOnMvtxrQ&t=120s',
      'video_id': 'saQOnMvtxrQ'},
     {'author': 'Ingram Micro Cloud',
      'channel': 'Ingram Micro Cloud',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:40](https://www.youtube.com/watch?v=ynfBBQclUKU&t=220s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Just made to this agreement it's really that simple with the power of the ID "
              'sync billing connector you can now have your data directly synced from the '
              'ingram micro cloud marketplace to your connectwise app spreadsheet free real '
              'time and with confidence and ease.',
      'timestamp': 220,
      'timestamp_label': '[00:03:40]',
      'timestamp_seconds': 220,
      'tip': "Just made to this agreement it's really that simple with the power of the ID "
             'sync billing connector you can now have your data directly synced from the '
             'ingram micro cloud marketplace to your connectwise app spreadsheet free real '
             'time and with confidence and ease.',
      'title': 'Ingram Micro Cloud Marketplace: ID Sync Billing Connector for ConnectWise '
               '(Ingram Micro Cloud)',
      'url': 'https://www.youtube.com/watch?v=ynfBBQclUKU&t=220s',
      'video_id': 'ynfBBQclUKU'},
     {'author': 'Leegality',
      'channel': 'Leegality',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:03](https://www.youtube.com/watch?v=DeATzRK3azc&t=243s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, it's going to scan your agreement for renewal terms. It's going to see, "
              '"Okay, these are my terms for renewals. " And it\'s going to assign this as a '
              "task to a relevant owner in your team. So, this way you don't have to pull out "
              'any data from the agreement.',
      'timestamp': 243,
      'timestamp_label': '[00:04:03]',
      'timestamp_seconds': 243,
      'tip': "So, it's going to scan your agreement for renewal terms. It's going to see, "
             '"Okay, these are my terms for renewals. " And it\'s going to assign this as a '
             "task to a relevant owner in your team. So, this way you don't have to pull out "
             'any data from the agreement.',
      'title': 'Where vendor agreements break, and how to fix both | Leegality Digital '
               'Contracts (Leegality)',
      'url': 'https://www.youtube.com/watch?v=DeATzRK3azc&t=243s',
      'video_id': 'DeATzRK3azc'},
     {'author': 'Finconvo Animation',
      'channel': 'Finconvo Animation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:25](https://www.youtube.com/watch?v=JEqCIJmR4Mg&t=325s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I coordinate with legal, finance, technical, and user departments when needed. '
              'I also monitor contract performance and follow up on delays, quality problems, '
              'or other non-compliance.',
      'timestamp': 325,
      'timestamp_label': '[00:05:25]',
      'timestamp_seconds': 325,
      'tip': 'I coordinate with legal, finance, technical, and user departments when needed. I '
             'also monitor contract performance and follow up on delays, quality problems, or '
             'other non-compliance.',
      'title': 'Procurement & Vendor Manager Interview Questions and Answers (Finconvo '
               'Animation)',
      'url': 'https://www.youtube.com/watch?v=JEqCIJmR4Mg&t=325s',
      'video_id': 'JEqCIJmR4Mg'},
     {'author': 'SAMexpert TV – Microsoft Licensing and Cloud',
      'channel': 'SAMexpert TV – Microsoft Licensing and Cloud',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:01](https://www.youtube.com/watch?v=7shzxv1SUFc&t=1561s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Nda between microsoft and kpmg what's written there what are the terms and "
              "conditions what's non-disclosure what goes to microsoft what doesn't go.",
      'timestamp': 1561,
      'timestamp_label': '[00:26:01]',
      'timestamp_seconds': 1561,
      'tip': "Nda between microsoft and kpmg what's written there what are the terms and "
             "conditions what's non-disclosure what goes to microsoft what doesn't go.",
      'title': 'Microsoft Licensing Audit Readiness and Audit Defence: a survival guide '
               '[Training 6/8] (SAMexpert TV – Microsoft Licensing and Cloud)',
      'url': 'https://www.youtube.com/watch?v=7shzxv1SUFc&t=1561s',
      'video_id': '7shzxv1SUFc'},
     {'author': 'How To Sell To & Win Federal Government Contracts',
      'channel': 'How To Sell To & Win Federal Government Contracts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:53:29](https://www.youtube.com/watch?v=p3DsAuDE32c&t=3209s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Modifications and that could be increasing your pricing adding labor categories '
              'um even getting access to reporting and compliance for contract administration '
              'purposes.',
      'timestamp': 3209,
      'timestamp_label': '[00:53:29]',
      'timestamp_seconds': 3209,
      'tip': 'Modifications and that could be increasing your pricing adding labor categories '
             'um even getting access to reporting and compliance for contract administration '
             'purposes.',
      'title': "Government Contracting - VIRTUAL CLASS:  GSA Schedule: What's In It For You? - "
               'Win Federal Contracts (How To Sell To & Win Federal Government Contracts)',
      'url': 'https://www.youtube.com/watch?v=p3DsAuDE32c&t=3209s',
      'video_id': 'p3DsAuDE32c'},
     {'author': 'Amazon Web Services',
      'channel': 'Amazon Web Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=KzcE0ZWyjzk&t=100s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Buyers to be on invoicing terms with AWS once logged into your AWS Marketplace '
              'seller portal click the agreement tab in the agreement tab search the active.',
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': 'Buyers to be on invoicing terms with AWS once logged into your AWS Marketplace '
             'seller portal click the agreement tab in the agreement tab search the active.',
      'title': 'Renew SaaS Contract Private Offers - AWS Marketplace | Amazon Web Services '
               '(Amazon Web Services)',
      'url': 'https://www.youtube.com/watch?v=KzcE0ZWyjzk&t=100s',
      'video_id': 'KzcE0ZWyjzk'},
     {'author': 'GSA (General Services Administration)',
      'channel': 'GSA (General Services Administration)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:35:25](https://www.youtube.com/watch?v=NVfgGOTkm4Q&t=2125s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's completely foreign to me I got a three inch tall contract that I had to "
              "sign so yeah there's evidence of another contracting vehicle place not a "
              'reportable sale but if no no no evidence of another contracting vehicle or it '
              'is a reportable sale in this situation.',
      'timestamp': 2125,
      'timestamp_label': '[00:35:25]',
      'timestamp_seconds': 2125,
      'tip': "That's completely foreign to me I got a three inch tall contract that I had to "
             "sign so yeah there's evidence of another contracting vehicle place not a "
             'reportable sale but if no no no evidence of another contracting vehicle or it is '
             'a reportable sale in this situation.',
      'title': 'Sales Tracking System Training for GSA Schedule Industry Partners (GSA '
               '(General Services Administration))',
      'url': 'https://www.youtube.com/watch?v=NVfgGOTkm4Q&t=2125s',
      'video_id': 'NVfgGOTkm4Q'},
     {'author': 'Federal Schedules, Inc. | FEDSched',
      'channel': 'Federal Schedules, Inc. | FEDSched',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=FnZjjws-i_s&t=110s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Government sales experience can increase success rates since 1986 federal '
              'schedules Inc has been saving companies time and relieving the stress in '
              "obtaining GSA mas contracts contact us for a quote download our beginner's "
              'guide or check out our FAQ.',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': 'Government sales experience can increase success rates since 1986 federal '
             'schedules Inc has been saving companies time and relieving the stress in '
             "obtaining GSA mas contracts contact us for a quote download our beginner's guide "
             'or check out our FAQ.',
      'title': 'What is a GSA Schedule? Learn How to Get on the GSA Schedule, Multiple Award '
               'Schedule (MAS) Contract (Federal Schedules, Inc. | FEDSched)',
      'url': 'https://www.youtube.com/watch?v=FnZjjws-i_s&t=110s',
      'video_id': 'FnZjjws-i_s'},
     {'author': 'Amazon Web Services',
      'channel': 'Amazon Web Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=XvBBSBimMn4&t=88s)',
      'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                   'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                   'implementation spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Private offers Ami hourly private offers SAS contract private offers SAS '
              'subscription private offers container private offers and Professional Services '
              'private offers today we will be discussing SAS contract private offers.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'Private offers Ami hourly private offers SAS contract private offers SAS '
             'subscription private offers container private offers and Professional Services '
             'private offers today we will be discussing SAS contract private offers.',
      'title': 'Subscribing to SaaS Contract Private Offers - AWS Marketplace (Amazon Web '
               'Services)',
      'url': 'https://www.youtube.com/watch?v=XvBBSBimMn4&t=88s',
      'video_id': 'XvBBSBimMn4'}],
 10: [{'author': 'Jobank CPA',
       'channel': 'Jobank CPA',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:31](https://www.youtube.com/watch?v=WeV8GbQwaPE&t=31s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'ASC 606 step one, uncover the side letter trap, talk about fixing the balance '
               'sheet, and wrap up with implementing SOX controls. All right, part one, the '
               "million-dollar illusion. Let's look at our case study on a fictional but "
               'highly realistic company called Cloud Scale AI.',
       'timestamp': 31,
       'timestamp_label': '[00:00:31]',
       'timestamp_seconds': 31,
       'tip': 'ASC 606 step one, uncover the side letter trap, talk about fixing the balance '
              'sheet, and wrap up with implementing SOX controls. All right, part one, the '
              "million-dollar illusion. Let's look at our case study on a fictional but highly "
              'realistic company called Cloud Scale AI.',
       'title': 'ASC 606 Revenue Recognition Edge Cases: Side Letters & Contract '
                'Enforceability (SaaS Accounting) (Jobank CPA)',
       'url': 'https://www.youtube.com/watch?v=WeV8GbQwaPE&t=31s',
       'video_id': 'WeV8GbQwaPE'},
      {'author': 'Schwab Network',
       'channel': 'Schwab Network',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:06](https://www.youtube.com/watch?v=V9sCxI7fIKk&t=366s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I think when when we're thinking about cybersecurity, the three names that I "
               'would focus on as, as, as, as sort of like the main beneficiaries of this AI, '
               'AI driven spending would be CrowdStrike, Palo Alto, and then, and then '
               'Fortinet.',
       'timestamp': 366,
       'timestamp_label': '[00:06:06]',
       'timestamp_seconds': 366,
       'tip': "I think when when we're thinking about cybersecurity, the three names that I "
              'would focus on as, as, as, as sort of like the main beneficiaries of this AI, '
              'AI driven spending would be CrowdStrike, Palo Alto, and then, and then '
              'Fortinet.',
       'title': "AI's Double-Edged Sword for Cybersecurity: Outlook for CRWD, PANW, OKTA "
                '(Schwab Network)',
       'url': 'https://www.youtube.com/watch?v=V9sCxI7fIKk&t=366s',
       'video_id': 'V9sCxI7fIKk'},
      {'author': 'TD SYNNEX',
       'channel': 'TD SYNNEX',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:11](https://www.youtube.com/watch?v=4NI20Et258M&t=131s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But that one Copilot sale should have five or six follow-up questions wrapped '
               "around it. That's the growth strategy. Is their data governed well enough to "
               'trust AI with it? Is their Azure or AWS consumption ready to scale? Will '
               'people actually adopt the technology?',
       'timestamp': 131,
       'timestamp_label': '[00:02:11]',
       'timestamp_seconds': 131,
       'tip': 'But that one Copilot sale should have five or six follow-up questions wrapped '
              "around it. That's the growth strategy. Is their data governed well enough to "
              'trust AI with it? Is their Azure or AWS consumption ready to scale? Will people '
              'actually adopt the technology?',
       'title': "Your Next $1M Customer Might Already Be Yours | Inspire 2026 | TD SYNNEX's "
                'Inspire Tech Talk (TD SYNNEX)',
       'url': 'https://www.youtube.com/watch?v=4NI20Et258M&t=131s',
       'video_id': '4NI20Et258M'},
      {'author': 'Virtualization Options LLC Free Learning Portal',
       'channel': 'Virtualization Options LLC Free Learning Portal',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:11](https://www.youtube.com/watch?v=xP4R2F8hbBw&t=311s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Do not pay for click speed. Only pay for audited tangible business outcomes. '
               'The enterprise defense framework, which is all about building your enterprise '
               'shield. So, we know their tactics, and we see right through their math.',
       'timestamp': 311,
       'timestamp_label': '[00:05:11]',
       'timestamp_seconds': 311,
       'tip': 'Do not pay for click speed. Only pay for audited tangible business outcomes. '
              'The enterprise defense framework, which is all about building your enterprise '
              'shield. So, we know their tactics, and we see right through their math.',
       'title': '9 The Truth About Enterprise Software Procurement (And How to Fight Back) '
                '(Virtualization Options LLC Free Learning Portal)',
       'url': 'https://www.youtube.com/watch?v=xP4R2F8hbBw&t=311s',
       'video_id': 'xP4R2F8hbBw'},
      {'author': 'CloudStrategist',
       'channel': 'CloudStrategist',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:51](https://www.youtube.com/watch?v=-_TJlxiXPJc&t=111s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Distributor who's the CSP disti who's the cloud solution provider in this case "
               'would be signing something called the MPA which is the Microsoft partner.',
       'timestamp': 111,
       'timestamp_label': '[00:01:51]',
       'timestamp_seconds': 111,
       'tip': "Distributor who's the CSP disti who's the cloud solution provider in this case "
              'would be signing something called the MPA which is the Microsoft partner.',
       'title': 'Microsoft CSP Agreements (CloudStrategist)',
       'url': 'https://www.youtube.com/watch?v=-_TJlxiXPJc&t=111s',
       'video_id': '-_TJlxiXPJc'},
      {'author': 'Snowflake Inc.',
       'channel': 'Snowflake Inc.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:43](https://www.youtube.com/watch?v=S0AC7agW8Uc&t=283s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And so at literally at every layer, the data layer, the catalog layer, the '
               'semantic layer, the AI model layer, Snowflake is completely open and '
               'interoperable.',
       'timestamp': 283,
       'timestamp_label': '[00:04:43]',
       'timestamp_seconds': 283,
       'tip': 'And so at literally at every layer, the data layer, the catalog layer, the '
              'semantic layer, the AI model layer, Snowflake is completely open and '
              'interoperable.',
       'title': 'Snowflake vs Databricks: Why Interoperability Matters for AI Agents '
                '(Snowflake Inc.)',
       'url': 'https://www.youtube.com/watch?v=S0AC7agW8Uc&t=283s',
       'video_id': 'S0AC7agW8Uc'},
      {'author': '10K',
       'channel': '10K',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:03](https://www.youtube.com/watch?v=wI9SWTi8f3E&t=183s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Businesses reduce manual work, prevent risky downgrades, and unlock expansion '
               'opportunities, all through deterministic logic built in the new Agent Force '
               'Builder experience. The result is higher retention, better aligned contracts '
               'and a renewal process that works at scale.',
       'timestamp': 183,
       'timestamp_label': '[00:03:03]',
       'timestamp_seconds': 183,
       'tip': 'Businesses reduce manual work, prevent risky downgrades, and unlock expansion '
              'opportunities, all through deterministic logic built in the new Agent Force '
              'Builder experience. The result is higher retention, better aligned contracts '
              'and a renewal process that works at scale.',
       'title': 'The AI Era Is Reshaping SaaS Renewals. Is Your Business Ready? (10K)',
       'url': 'https://www.youtube.com/watch?v=wI9SWTi8f3E&t=183s',
       'video_id': 'wI9SWTi8f3E'},
      {'author': 'Channel Insider',
       'channel': 'Channel Insider',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:50](https://www.youtube.com/watch?v=WF4x0_79W_w&t=170s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Not to mention, we're investing in training on our teams so that they "
               'understand how to answer the questions from the channel uh on on the scale '
               'computing products.',
       'timestamp': 170,
       'timestamp_label': '[00:02:50]',
       'timestamp_seconds': 170,
       'tip': "Not to mention, we're investing in training on our teams so that they "
              'understand how to answer the questions from the channel uh on on the scale '
              'computing products.',
       'title': 'How TD SYNNEX Empowers Scale Computing Partners Globally (Channel Insider)',
       'url': 'https://www.youtube.com/watch?v=WF4x0_79W_w&t=170s',
       'video_id': 'WF4x0_79W_w'},
      {'author': 'Zylo | The Leader in Enterprise SaaS Management',
       'channel': 'Zylo | The Leader in Enterprise SaaS Management',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:00](https://www.youtube.com/watch?v=Os3h9DFeKBU&t=180s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So after that's all done Wendy's like how do I scale my efforts here she "
               "realizes that she's wasted a lot of time looking for basic data to make a.",
       'timestamp': 180,
       'timestamp_label': '[00:03:00]',
       'timestamp_seconds': 180,
       'tip': "So after that's all done Wendy's like how do I scale my efforts here she "
              "realizes that she's wasted a lot of time looking for basic data to make a.",
       'title': 'What’s an Effective Strategy to Manage My SaaS Renewals? (Zylo | The Leader '
                'in Enterprise SaaS Management)',
       'url': 'https://www.youtube.com/watch?v=Os3h9DFeKBU&t=180s',
       'video_id': 'Os3h9DFeKBU'},
      {'author': 'AWS Events',
       'channel': 'AWS Events',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:08](https://www.youtube.com/watch?v=42TotVxOC44&t=428s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I have an example here from two of our launch partners, Accenture and Elastic. '
               "Accenture has created a data readiness engine for Gen AI solution that's "
               'available on our marketplace website. The solution combines four products.',
       'timestamp': 428,
       'timestamp_label': '[00:07:08]',
       'timestamp_seconds': 428,
       'tip': 'I have an example here from two of our launch partners, Accenture and Elastic. '
              "Accenture has created a data readiness engine for Gen AI solution that's "
              'available on our marketplace website. The solution combines four products.',
       'title': 'AWS re:Invent 2025 - Solution-based selling strategies in AWS Marketplace '
                '(PEX110) (AWS Events)',
       'url': 'https://www.youtube.com/watch?v=42TotVxOC44&t=428s',
       'video_id': '42TotVxOC44'},
      {'author': 'Pete Matheson - Not a Business Coach',
       'channel': 'Pete Matheson - Not a Business Coach',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:52](https://www.youtube.com/watch?v=lcMWkAWGxSU&t=52s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You can actually run in-person events, lunch and learns, beer and backup, all '
               "sorts of different events. But it's not just for events, so you can use direct "
               'mails, social media campaigns, telemarketing even video content creation could '
               'all be potentially funded through MDF.',
       'timestamp': 52,
       'timestamp_label': '[00:00:52]',
       'timestamp_seconds': 52,
       'tip': 'You can actually run in-person events, lunch and learns, beer and backup, all '
              "sorts of different events. But it's not just for events, so you can use direct "
              'mails, social media campaigns, telemarketing even video content creation could '
              'all be potentially funded through MDF.',
       'title': 'What is Market Development Funds (MDF) (Pete Matheson - Not a Business Coach)',
       'url': 'https://www.youtube.com/watch?v=lcMWkAWGxSU&t=52s',
       'video_id': 'lcMWkAWGxSU'},
      {'author': 'Bridgepoint Consulting',
       'channel': 'Bridgepoint Consulting',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:15](https://www.youtube.com/watch?v=KL4guXcGWDU&t=195s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That's gonna take you back to their response thanks so much for watching if "
               'you have any questions feel free to reach out to jay Holtzman at Bridge point '
               'consulting calm and stay tuned for some more videos tips and tricks and '
               'netsuite thanks.',
       'timestamp': 195,
       'timestamp_label': '[00:03:15]',
       'timestamp_seconds': 195,
       'tip': "That's gonna take you back to their response thanks so much for watching if you "
              'have any questions feel free to reach out to jay Holtzman at Bridge point '
              'consulting calm and stay tuned for some more videos tips and tricks and '
              'netsuite thanks.',
       'title': 'NetSuite Procurement Module: Request for Quote Demo (Bridgepoint Consulting)',
       'url': 'https://www.youtube.com/watch?v=KL4guXcGWDU&t=195s',
       'video_id': 'KL4guXcGWDU'},
      {'author': 'TD SYNNEX',
       'channel': 'TD SYNNEX',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:26](https://www.youtube.com/watch?v=2qmTwyQCa_o&t=206s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re your chosen distributor. Let us be your chosen service provider in the "
               "areas that you don't have the capacity or capabilities to deliver yourself. "
               'Well, actually that brings me perfectly to the next point. You mentioned '
               'things like scale.',
       'timestamp': 206,
       'timestamp_label': '[00:03:26]',
       'timestamp_seconds': 206,
       'tip': "'re your chosen distributor. Let us be your chosen service provider in the "
              "areas that you don't have the capacity or capabilities to deliver yourself. "
              'Well, actually that brings me perfectly to the next point. You mentioned things '
              'like scale.',
       'title': 'How TD SYNNEX Services Help Partners Grow Faster | Partner Services Explained '
                '(TD SYNNEX)',
       'url': 'https://www.youtube.com/watch?v=2qmTwyQCa_o&t=206s',
       'video_id': '2qmTwyQCa_o'},
      {'author': 'Staying Connected',
       'channel': 'Staying Connected',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:41](https://www.youtube.com/watch?v=BJPNVL1CIiM&t=581s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Shoot us an email you can also stay current by subscribing to these staying '
               'connected podcasts by checking out our websites and by following us on '
               'linkedin.',
       'timestamp': 581,
       'timestamp_label': '[00:09:41]',
       'timestamp_seconds': 581,
       'tip': 'Shoot us an email you can also stay current by subscribing to these staying '
              'connected podcasts by checking out our websites and by following us on '
              'linkedin.',
       'title': 'Get the Most Value from Value Added Resellers (Staying Connected)',
       'url': 'https://www.youtube.com/watch?v=BJPNVL1CIiM&t=581s',
       'video_id': 'BJPNVL1CIiM'},
      {'author': 'Amazon Web Services',
       'channel': 'Amazon Web Services',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:06](https://www.youtube.com/watch?v=gNv2wvhYkzA&t=246s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Drafts I think saving as drafts is huge for our partners um now folks don't "
               'have to complete the private offer Creation in one step they can save um and '
               'walk away uh when they have all of the information so draft is going to be the '
               'one for me Game Changer I love it Cher.',
       'timestamp': 246,
       'timestamp_label': '[00:04:06]',
       'timestamp_seconds': 246,
       'tip': "Drafts I think saving as drafts is huge for our partners um now folks don't "
              'have to complete the private offer Creation in one step they can save um and '
              'walk away uh when they have all of the information so draft is going to be the '
              'one for me Game Changer I love it Cher.',
       'title': 'AWS Marketplace Ops Squad | Amazon Web Services (Amazon Web Services)',
       'url': 'https://www.youtube.com/watch?v=gNv2wvhYkzA&t=246s',
       'video_id': 'gNv2wvhYkzA'}],
 11: [{'author': 'FinOps Foundation',
       'channel': 'FinOps Foundation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=LF1AK1WypX0&t=20s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It's my manager, a data engineer, and myself. However, the cloud center of "
               'excellence is part of a larger team with 130 engineers um which is called '
               'central technology and infrastructure.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': "It's my manager, a data engineer, and myself. However, the cloud center of "
              'excellence is part of a larger team with 130 engineers um which is called '
              'central technology and infrastructure.',
       'title': 'Licensing and SaaS at Scale: Cloud+ FinOps Scopes Intersecting with ITAM & '
                'SAM (FinOps Foundation)',
       'url': 'https://www.youtube.com/watch?v=LF1AK1WypX0&t=20s',
       'video_id': 'LF1AK1WypX0'},
      {'author': 'PartnerCloud',
       'channel': 'PartnerCloud',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:36](https://www.youtube.com/watch?v=qXei9F9hLNU&t=756s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I need a short description. I've got that kind of queued up right here. "
               'External PDM for hire is a fractional embedded support model that places an '
               'experienced AWS partner manager inside your team. And then here is my long '
               'description.',
       'timestamp': 756,
       'timestamp_label': '[00:12:36]',
       'timestamp_seconds': 756,
       'tip': "I need a short description. I've got that kind of queued up right here. "
              'External PDM for hire is a fractional embedded support model that places an '
              'experienced AWS partner manager inside your team. And then here is my long '
              'description.',
       'title': 'AWS Marketplace 101  Building a Profile and My First Listing! (PartnerCloud)',
       'url': 'https://www.youtube.com/watch?v=qXei9F9hLNU&t=756s',
       'video_id': 'qXei9F9hLNU'},
      {'author': 'Flexera | ITAM, FinOps & SaaS Management',
       'channel': 'Flexera | ITAM, FinOps & SaaS Management',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:07](https://www.youtube.com/watch?v=O3FqsxJScI4&t=307s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s kind of like on-prem data center teams, SAS, enterprise architecture, "
               "technology strategy. So, it's also expanding across the business as kind of "
               'different technology categories come under the remit of the FinOps team as '
               'well and working with those partners.',
       'timestamp': 307,
       'timestamp_label': '[00:05:07]',
       'timestamp_seconds': 307,
       'tip': "'s kind of like on-prem data center teams, SAS, enterprise architecture, "
              "technology strategy. So, it's also expanding across the business as kind of "
              'different technology categories come under the remit of the FinOps team as well '
              'and working with those partners.',
       'title': 'FinOps Forward 2026: FinOps Foundation Keynote (Flexera | ITAM, FinOps & SaaS '
                'Management)',
       'url': 'https://www.youtube.com/watch?v=O3FqsxJScI4&t=307s',
       'video_id': 'O3FqsxJScI4'},
      {'author': 'TD SYNNEX',
       'channel': 'TD SYNNEX',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:19](https://www.youtube.com/watch?v=K3d3674aDZ8&t=79s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I've got services that cover the whole spectrum of IT, so networking, "
               "cybersecurity, cloud, data centre, you name it, we kind of do it. And we've "
               'got literally hundreds and hundreds of partners with thousands of customers of '
               'all different types of needs and wants.',
       'timestamp': 79,
       'timestamp_label': '[00:01:19]',
       'timestamp_seconds': 79,
       'tip': "I've got services that cover the whole spectrum of IT, so networking, "
              "cybersecurity, cloud, data centre, you name it, we kind of do it. And we've got "
              'literally hundreds and hundreds of partners with thousands of customers of all '
              'different types of needs and wants.',
       'title': 'Meet the Expert: How TD SYNNEX services help partners scale and grow (TD '
                'SYNNEX)',
       'url': 'https://www.youtube.com/watch?v=K3d3674aDZ8&t=79s',
       'video_id': 'K3d3674aDZ8'},
      {'author': 'Amazon Web Services',
       'channel': 'Amazon Web Services',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:22](https://www.youtube.com/watch?v=xLqQjXa2edo&t=22s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'ISVs) to authorize Channel Partner Private Offer (CPPO) support. Other key '
               'benefits include automated notifications about key agreement milestones, '
               'integrated reporting capabilities, and accelerated transactions on AWS '
               'Marketplace.',
       'timestamp': 22,
       'timestamp_label': '[00:00:22]',
       'timestamp_seconds': 22,
       'tip': 'ISVs) to authorize Channel Partner Private Offer (CPPO) support. Other key '
              'benefits include automated notifications about key agreement milestones, '
              'integrated reporting capabilities, and accelerated transactions on AWS '
              'Marketplace.',
       'title': 'Create an AWS Marketplace Future Dated Private Offer | Amazon Web Services '
                '(Amazon Web Services)',
       'url': 'https://www.youtube.com/watch?v=xLqQjXa2edo&t=22s',
       'video_id': 'xLqQjXa2edo'},
      {'author': 'RSM US LLP',
       'channel': 'RSM US LLP',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=Qxj-ooX7WrE&t=15s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Core principles that we work with here RSM specifically within our technology '
               'and management consulting team is to help companies like yours manage your.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Core principles that we work with here RSM specifically within our technology '
              'and management consulting team is to help companies like yours manage your.',
       'title': 'NetSuite Advanced Revenue Management (ARM) demo | ASC 606 overview for '
                'NetSuite users (RSM US LLP)',
       'url': 'https://www.youtube.com/watch?v=Qxj-ooX7WrE&t=15s',
       'video_id': 'Qxj-ooX7WrE'},
      {'author': 'Carahsoft',
       'channel': 'Carahsoft',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:58](https://www.youtube.com/watch?v=7Vc9xJqVhSs&t=58s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "20 years right at different software companies big enterprise companies. It's "
               'interesting to see that this topic has continued on and I can just say like '
               "there's a lot more urgency to it. But having said that, um I lead the federal "
               'civilian sales team at Atlassian.',
       'timestamp': 58,
       'timestamp_label': '[00:00:58]',
       'timestamp_seconds': 58,
       'tip': "20 years right at different software companies big enterprise companies. It's "
              'interesting to see that this topic has continued on and I can just say like '
              "there's a lot more urgency to it. But having said that, um I lead the federal "
              'civilian sales team at Atlassian.',
       'title': 'Streamline Atlassian Software Licensing and Procurement with Clovity and '
                'Carahsoft (Preview) (Carahsoft)',
       'url': 'https://www.youtube.com/watch?v=7Vc9xJqVhSs&t=58s',
       'video_id': '7Vc9xJqVhSs'},
      {'author': 'The Crancer Group',
       'channel': 'The Crancer Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:39](https://www.youtube.com/watch?v=dM62o5Vq5U4&t=699s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '300, 500 seats, you can go to the Microsoft account team and sit down and talk '
               'to them and say, "Hey, I\'ve got this opportunity. I know they want to do '
               'this. Is there anything you guys can do to help sweeten deal?".',
       'timestamp': 699,
       'timestamp_label': '[00:11:39]',
       'timestamp_seconds': 699,
       'tip': '300, 500 seats, you can go to the Microsoft account team and sit down and talk '
              'to them and say, "Hey, I\'ve got this opportunity. I know they want to do this. '
              'Is there anything you guys can do to help sweeten deal?".',
       'title': 'VOMP Highlights: Stop Missing Out on Microsoft Market Development Funds (The '
                'Crancer Group)',
       'url': 'https://www.youtube.com/watch?v=dM62o5Vq5U4&t=699s',
       'video_id': 'dM62o5Vq5U4'},
      {'author': 'WeTransact',
       'channel': 'WeTransact',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=jJAskh3xNOM&t=15s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Development manager at Microsoft and I've been here for about three years now "
               "I'm super excited to to welcome you to today's session in collaboration with.",
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': "Development manager at Microsoft and I've been here for about three years now "
              "I'm super excited to to welcome you to today's session in collaboration with.",
       'title': 'How to grow on Microsoft Marketplace through resellers (CSP and multi-party '
                'offers) (WeTransact)',
       'url': 'https://www.youtube.com/watch?v=jJAskh3xNOM&t=15s',
       'video_id': 'jJAskh3xNOM'},
      {'author': 'Vanuko',
       'channel': 'Vanuko',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:22](https://www.youtube.com/watch?v=wMnj47JPiwE&t=82s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Let's follow a sales process for Alderbrook Consulting and then see how the "
               "team manages the next year's business alongside all its existing customers. "
               'Alderbrook is interested in two annual team licenses.',
       'timestamp': 82,
       'timestamp_label': '[00:01:22]',
       'timestamp_seconds': 82,
       'tip': "Let's follow a sales process for Alderbrook Consulting and then see how the "
              "team manages the next year's business alongside all its existing customers. "
              'Alderbrook is interested in two annual team licenses.',
       'title': 'Using Vanuko for Managing SaaS Software Renewals (Vanuko)',
       'url': 'https://www.youtube.com/watch?v=wMnj47JPiwE&t=82s',
       'video_id': 'wMnj47JPiwE'},
      {'author': 'AVC-Licensing',
       'channel': 'AVC-Licensing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:51](https://www.youtube.com/watch?v=8S2AXmoUSJY&t=171s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "We didn't measure an ROI or a change in processing time, so we don't claim "
               'one. What the AP team reported was this. They could finally trust and navigate '
               'their vendor data. A vendor master is a control the business relies on. Part '
               'two covers the technical side.',
       'timestamp': 171,
       'timestamp_label': '[00:02:51]',
       'timestamp_seconds': 171,
       'tip': "We didn't measure an ROI or a change in processing time, so we don't claim one. "
              'What the AP team reported was this. They could finally trust and navigate their '
              'vendor data. A vendor master is a control the business relies on. Part two '
              'covers the technical side.',
       'title': 'One Vendor Master Across 30 D365 Legal Entities: The Win Was Trust (Case '
                'Study) (AVC-Licensing)',
       'url': 'https://www.youtube.com/watch?v=8S2AXmoUSJY&t=171s',
       'video_id': '8S2AXmoUSJY'},
      {'author': 'Spend And Procurement with Mike',
       'channel': 'Spend And Procurement with Mike',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:46](https://www.youtube.com/watch?v=xPYn_cF6f1E&t=106s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Supplier's responsibility to fix calls from suppliers to the accounts payable "
               'team is also vastly reduced as the supplier has access to the invoice status '
               'via the network itself to track if the invoice has been received and when the '
               'suppli is going to get paid.',
       'timestamp': 106,
       'timestamp_label': '[00:01:46]',
       'timestamp_seconds': 106,
       'tip': "Supplier's responsibility to fix calls from suppliers to the accounts payable "
              'team is also vastly reduced as the supplier has access to the invoice status '
              'via the network itself to track if the invoice has been received and when the '
              'suppli is going to get paid.',
       'title': 'SAP Business Network for Procurement - Demo (Spend And Procurement with Mike)',
       'url': 'https://www.youtube.com/watch?v=xPYn_cF6f1E&t=106s',
       'video_id': 'xPYn_cF6f1E'},
      {'author': 'The SaaS CFO',
       'channel': 'The SaaS CFO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:37](https://www.youtube.com/watch?v=pC3bnU1ivL8&t=37s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So there's a formula with this. So in the numerator we have the number of "
               'hours that our team is working against those services projects.',
       'timestamp': 37,
       'timestamp_label': '[00:00:37]',
       'timestamp_seconds': 37,
       'tip': "So there's a formula with this. So in the numerator we have the number of hours "
              'that our team is working against those services projects.',
       'title': 'My Top 4 Professional Services Metrics – Billable Utilization | SaaS Metrics '
                'School (The SaaS CFO)',
       'url': 'https://www.youtube.com/watch?v=pC3bnU1ivL8&t=37s',
       'video_id': 'pC3bnU1ivL8'},
      {'author': 'Sheldon Needle',
       'channel': 'Sheldon Needle',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:59](https://www.youtube.com/watch?v=2tRDmrgGASk&t=119s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Dry just be aware that uh of the issues that you have to concern yourself with '
               'a VAR who who is not going to be as large and stable as the vendor themselves '
               'thanks for listening and have a great day.',
       'timestamp': 119,
       'timestamp_label': '[00:01:59]',
       'timestamp_seconds': 119,
       'tip': 'Dry just be aware that uh of the issues that you have to concern yourself with '
              'a VAR who who is not going to be as large and stable as the vendor themselves '
              'thanks for listening and have a great day.',
       'title': 'Working Successfully with Value-Added Resellers (VARs) (Sheldon Needle)',
       'url': 'https://www.youtube.com/watch?v=2tRDmrgGASk&t=119s',
       'video_id': '2tRDmrgGASk'},
      {'author': 'Clazar',
       'channel': 'Clazar',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:11](https://www.youtube.com/watch?v=h7liwzzA_-I&t=71s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Enterprise customers requiring tailored pricing and contract terms. CPPO and '
               'CPPO is channel partner private offer which is the channel motion for AWS. To '
               'sum it up, private offers enable custom pricing for individual buyers.',
       'timestamp': 71,
       'timestamp_label': '[00:01:11]',
       'timestamp_seconds': 71,
       'tip': 'Enterprise customers requiring tailored pricing and contract terms. CPPO and '
              'CPPO is channel partner private offer which is the channel motion for AWS. To '
              'sum it up, private offers enable custom pricing for individual buyers.',
       'title': 'How Private Offers work on AWS Marketplace explained step by step (Clazar)',
       'url': 'https://www.youtube.com/watch?v=h7liwzzA_-I&t=71s',
       'video_id': 'h7liwzzA_-I'}],
 12: [{'author': 'Luasai',
       'channel': 'Luasai',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:22:57](https://www.youtube.com/watch?v=9ijiF4Aas8o&t=1377s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "You're going from a nine month onboarding process to a three week sales cycle "
               'if you leverage an existing supplier into an enterprise.',
       'timestamp': 1377,
       'timestamp_label': '[00:22:57]',
       'timestamp_seconds': 1377,
       'tip': "You're going from a nine month onboarding process to a three week sales cycle "
              'if you leverage an existing supplier into an enterprise.',
       'title': 'Why Most ISVs Get Channel Wrong | Building an Enterprise Software Ecosystem '
                '(Luasai)',
       'url': 'https://www.youtube.com/watch?v=9ijiF4Aas8o&t=1377s',
       'video_id': '9ijiF4Aas8o'},
      {'author': 'Eddy Says Hi #EddySaysHi',
       'channel': 'Eddy Says Hi #EddySaysHi',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:41](https://www.youtube.com/watch?v=sIJo4dVD-jc&t=101s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'If you ignore software, you are making huge decisions based on totally '
               'incomplete data about what your cloud truly costs. Okay, so how do we get this '
               "beast under control? Well, the good news is you don't have to start from "
               'scratch.',
       'timestamp': 101,
       'timestamp_label': '[00:01:41]',
       'timestamp_seconds': 101,
       'tip': 'If you ignore software, you are making huge decisions based on totally '
              'incomplete data about what your cloud truly costs. Okay, so how do we get this '
              "beast under control? Well, the good news is you don't have to start from "
              'scratch.',
       'title': 'SaaS & Licensing in FinOps (Eddy Says Hi #EddySaysHi)',
       'url': 'https://www.youtube.com/watch?v=sIJo4dVD-jc&t=101s',
       'video_id': 'sIJo4dVD-jc'},
      {'author': 'Venduris',
       'channel': 'Venduris',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:21](https://www.youtube.com/watch?v=0W4a6u1-zMQ&t=141s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Then run a 30-minute review every month. Urgent items first, then everything '
               "due in 90 days, new contracts, owners who've left, and one number for "
               'leadership. A spreadsheet works until you pass 30 contracts, several owners, '
               'or you need usage data next to each renewal.',
       'timestamp': 141,
       'timestamp_label': '[00:02:21]',
       'timestamp_seconds': 141,
       'tip': 'Then run a 30-minute review every month. Urgent items first, then everything '
              "due in 90 days, new contracts, owners who've left, and one number for "
              'leadership. A spreadsheet works until you pass 30 contracts, several owners, or '
              'you need usage data next to each renewal.',
       'title': 'How to Track SaaS Renewals (Free Tracker + Notice Deadline Formula) '
                '(Venduris)',
       'url': 'https://www.youtube.com/watch?v=0W4a6u1-zMQ&t=141s',
       'video_id': '0W4a6u1-zMQ'},
      {'author': 'Vektorindex',
       'channel': 'Vektorindex',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:57](https://www.youtube.com/watch?v=lR3RrM_hqMg&t=357s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A $48,000 renewal discovered a week before payment leaves no time to check '
               'usage, gather evidence, compare alternatives, or get approvals. The only '
               'available action is paying. Discover it 120 days out and every option exists. '
               'Rightize, negotiate, consolidate, even exit.',
       'timestamp': 357,
       'timestamp_label': '[00:05:57]',
       'timestamp_seconds': 357,
       'tip': 'A $48,000 renewal discovered a week before payment leaves no time to check '
              'usage, gather evidence, compare alternatives, or get approvals. The only '
              'available action is paying. Discover it 120 days out and every option exists. '
              'Rightize, negotiate, consolidate, even exit.',
       'title': "Is Your SaaS Spend Out of Control? Here's How To Fix It (Vektorindex)",
       'url': 'https://www.youtube.com/watch?v=lR3RrM_hqMg&t=357s',
       'video_id': 'lR3RrM_hqMg'},
      {'author': "James And Jenna's Tutorials",
       'channel': "James And Jenna's Tutorials",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:04](https://www.youtube.com/watch?v=gkHpTkP_2Zg&t=124s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'We have the premium plan which is going to cost to around $35 per month per '
               'user and then they have the enterprise plan which is going to cost to around '
               '$75 per user per month. When it is built annually, you will get some of the '
               'discounts.',
       'timestamp': 124,
       'timestamp_label': '[00:02:04]',
       'timestamp_seconds': 124,
       'tip': 'We have the premium plan which is going to cost to around $35 per month per '
              'user and then they have the enterprise plan which is going to cost to around '
              '$75 per user per month. When it is built annually, you will get some of the '
              'discounts.',
       'title': 'Zoho Procurement Demo, Tutorial & Review | Purchase Orders & Vendor '
                "Management (2026) (James And Jenna's Tutorials)",
       'url': 'https://www.youtube.com/watch?v=gkHpTkP_2Zg&t=124s',
       'video_id': 'gkHpTkP_2Zg'},
      {'author': 'Softspend',
       'channel': 'Softspend',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:26](https://www.youtube.com/watch?v=zwXrzaNyZB0&t=26s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It's both $57 per user per month list price in the CSP and in the EA. There "
               'are even products like Windows 365 who are better priced from a list price '
               'perspective compared to EA. So, also CSP is giving more advantages sometimes '
               'over the Enterprise Agreement.',
       'timestamp': 26,
       'timestamp_label': '[00:00:26]',
       'timestamp_seconds': 26,
       'tip': "It's both $57 per user per month list price in the CSP and in the EA. There are "
              'even products like Windows 365 who are better priced from a list price '
              'perspective compared to EA. So, also CSP is giving more advantages sometimes '
              'over the Enterprise Agreement.',
       'title': 'The CSP Commercial Opportunity (Softspend)',
       'url': 'https://www.youtube.com/watch?v=zwXrzaNyZB0&t=26s',
       'video_id': 'zwXrzaNyZB0'},
      {'author': 'Amazon Web Services',
       'channel': 'Amazon Web Services',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:15](https://www.youtube.com/watch?v=HU_SJTFHcGU&t=375s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Has more information on requirements and how to get started lastly check out '
               'our YouTube channel this includes content on AWS Marketplace recent launch '
               'announcements and product demos all right that is all for today thank you for '
               'watching and I will see you next time.',
       'timestamp': 375,
       'timestamp_label': '[00:06:15]',
       'timestamp_seconds': 375,
       'tip': 'Has more information on requirements and how to get started lastly check out '
              'our YouTube channel this includes content on AWS Marketplace recent launch '
              'announcements and product demos all right that is all for today thank you for '
              'watching and I will see you next time.',
       'title': 'Introduction to AWS Marketplace | Amazon Web Services (Amazon Web Services)',
       'url': 'https://www.youtube.com/watch?v=HU_SJTFHcGU&t=375s',
       'video_id': 'HU_SJTFHcGU'},
      {'author': 'Manage Protect',
       'channel': 'Manage Protect',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:30:07](https://www.youtube.com/watch?v=Je2jbg9tm0Q&t=1807s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So if we can start that process earlier then there's less urgency coming "
               'closer to the day of the 1st of October or your anniversary date of course. '
               "Well then I think that's it for questions for now.",
       'timestamp': 1807,
       'timestamp_label': '[00:30:07]',
       'timestamp_seconds': 1807,
       'tip': "So if we can start that process earlier then there's less urgency coming closer "
              'to the day of the 1st of October or your anniversary date of course. Well then '
              "I think that's it for questions for now.",
       'title': 'CSP Reseller Partners: New Microsoft Requirements (Manage Protect)',
       'url': 'https://www.youtube.com/watch?v=Je2jbg9tm0Q&t=1807s',
       'video_id': 'Je2jbg9tm0Q'},
      {'author': 'Microsoft Cloud',
       'channel': 'Microsoft Cloud',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:20](https://www.youtube.com/watch?v=REkZmdc2hYE&t=140s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You can create a flexible schedule of charges and set market pricing in the '
               'currencies supported. Here you have the option to set the plan to start at a '
               'future date. Setting future dated agreements streamlines renewals to avoid any '
               'service gaps.',
       'timestamp': 140,
       'timestamp_label': '[00:02:20]',
       'timestamp_seconds': 140,
       'tip': 'You can create a flexible schedule of charges and set market pricing in the '
              'currencies supported. Here you have the option to set the plan to start at a '
              'future date. Setting future dated agreements streamlines renewals to avoid any '
              'service gaps.',
       'title': 'Private offer enhancements in Microsoft Marketplace | Partner demo (Microsoft '
                'Cloud)',
       'url': 'https://www.youtube.com/watch?v=REkZmdc2hYE&t=140s',
       'video_id': 'REkZmdc2hYE'},
      {'author': 'Ncontracts',
       'channel': 'Ncontracts',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:01](https://www.youtube.com/watch?v=GsLnrTOe4bw&t=1021s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re seeing class action lawsuits. So, um I I'll share something from my kind "
               'of days, you know, as an examiner in the banking world. We would often tell uh '
               'uh financial institutions that you you know, um you can outsource the '
               "function, but you can't outsource the risk.",
       'timestamp': 1021,
       'timestamp_label': '[00:17:01]',
       'timestamp_seconds': 1021,
       'tip': "'re seeing class action lawsuits. So, um I I'll share something from my kind of "
              'days, you know, as an examiner in the banking world. We would often tell uh uh '
              'financial institutions that you you know, um you can outsource the function, '
              "but you can't outsource the risk.",
       'title': "You Can't Outsource the Risk: Reg S-P and Vendor Oversight (Ncontracts)",
       'url': 'https://www.youtube.com/watch?v=GsLnrTOe4bw&t=1021s',
       'video_id': 'GsLnrTOe4bw'},
      {'author': 'Agreement Automation Lab',
       'channel': 'Agreement Automation Lab',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:34](https://www.youtube.com/watch?v=A91pl3huL6s&t=34s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Let's run it for Northfield. Day to day, the Baton Launcher starts it right "
               'from the NetSuite record. Here, we start it from Docusign and give it the '
               "vendor's record number. Within seconds, the agreement is on its way to Marcus "
               "Lee, Northfield's contact.",
       'timestamp': 34,
       'timestamp_label': '[00:00:34]',
       'timestamp_seconds': 34,
       'tip': "Let's run it for Northfield. Day to day, the Baton Launcher starts it right "
              'from the NetSuite record. Here, we start it from Docusign and give it the '
              "vendor's record number. Within seconds, the agreement is on its way to Marcus "
              "Lee, Northfield's contact.",
       'title': 'Supplier Onboarding with Zero Retyping | NetSuite + Docusign (Agreement '
                'Automation Lab)',
       'url': 'https://www.youtube.com/watch?v=A91pl3huL6s&t=34s',
       'video_id': 'A91pl3huL6s'},
      {'author': 'Procure IT',
       'channel': 'Procure IT',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:07](https://www.youtube.com/watch?v=_PyR6G51QW4&t=187s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Need to be looked at and we recommend we work with our clients to look at '
               'those targeted accounts to see if those accounts should remain active or if '
               'our users should take action and disable those accounts and remove those '
               'licensing ultimately reducing spent.',
       'timestamp': 187,
       'timestamp_label': '[00:03:07]',
       'timestamp_seconds': 187,
       'tip': 'Need to be looked at and we recommend we work with our clients to look at those '
              'targeted accounts to see if those accounts should remain active or if our users '
              'should take action and disable those accounts and remove those licensing '
              'ultimately reducing spent.',
       'title': 'SaaS FinOps Module: Taking Control of SaaS Costs and User Data with AI '
                '(Procure IT)',
       'url': 'https://www.youtube.com/watch?v=_PyR6G51QW4&t=187s',
       'video_id': '_PyR6G51QW4'},
      {'author': 'Steve Preda',
       'channel': 'Steve Preda',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:37](https://www.youtube.com/watch?v=5n6g3xVFV88&t=517s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Have a great day this was the profserv traction podcast with steve prata to '
               'learn how your professional services or technology business could break '
               'through the ceiling with eos visit tractionequity.com.',
       'timestamp': 517,
       'timestamp_label': '[00:08:37]',
       'timestamp_seconds': 517,
       'tip': 'Have a great day this was the profserv traction podcast with steve prata to '
              'learn how your professional services or technology business could break through '
              'the ceiling with eos visit tractionequity.com.',
       'title': 'Value-Added Reseller | The ProfServ Traction Podcast (Steve Preda)',
       'url': 'https://www.youtube.com/watch?v=5n6g3xVFV88&t=517s',
       'video_id': '5n6g3xVFV88'},
      {'author': 'GovClose | DoD Contract Academy',
       'channel': 'GovClose | DoD Contract Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:31](https://www.youtube.com/watch?v=WZkYFEEekIk&t=571s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Out a Premiere video talking about the latest changes in Government '
               'Contracting how you can take advantage of it how you can start a career here '
               "if you're looking for a career change thanks again for watching take care.",
       'timestamp': 571,
       'timestamp_label': '[00:09:31]',
       'timestamp_seconds': 571,
       'tip': 'Out a Premiere video talking about the latest changes in Government Contracting '
              "how you can take advantage of it how you can start a career here if you're "
              'looking for a career change thanks again for watching take care.',
       'title': 'Will You Need a GSA Schedule to Sell to the Government? (GovClose | DoD '
                'Contract Academy)',
       'url': 'https://www.youtube.com/watch?v=WZkYFEEekIk&t=571s',
       'video_id': 'WZkYFEEekIk'},
      {'author': 'Jobank CPA',
       'channel': 'Jobank CPA',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:46](https://www.youtube.com/watch?v=KjWijHo8iMI&t=226s)',
       'relevance': 'Attributed practitioner commentary on enterprise software VAR & '
                    'cloud-marketplace private offers (`CPPO`/`CSP`), deal registration, and '
                    'implementation spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I take the hit if the customer defaults, so obviously I\'m the principal." ASC '
               '606 intentionally removed credit risk as a primary indicator. Collecting cash '
               "is just a billing mechanic. It's not proof of controlling the cloud service.",
       'timestamp': 226,
       'timestamp_label': '[00:03:46]',
       'timestamp_seconds': 226,
       'tip': 'I take the hit if the customer defaults, so obviously I\'m the principal." ASC '
              '606 intentionally removed credit risk as a primary indicator. Collecting cash '
              "is just a billing mechanic. It's not proof of controlling the cloud service.",
       'title': 'Episode 16 ASC 606 Principal vs Agent Explained: Gross vs Net Revenue Rules '
                '(Jobank CPA)',
       'url': 'https://www.youtube.com/watch?v=KjWijHo8iMI&t=226s',
       'video_id': 'KjWijHo8iMI'}]}
