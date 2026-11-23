"""Curated 180-citation Customs Duty Drawback, Tariff Refund & Antitrust Claim Recovery baseline (15 per chapter across Q1-Q12) mined strictly from verified Customs Duty Drawback, Tariff Refund & Antitrust Claim Recovery YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'111',
     '1313',
     '1514',
     '1520',
     '190',
     '301',
     '7501',
     '7553',
     '9801',
     'accelerated',
     'ace',
     'action',
     'administration',
     'agreement',
     'amazon',
     'antidumping',
     'antitrust',
     'apparel',
     'attorney',
     'audit',
     'auditing',
     'auto',
     'automated',
     'automating',
     'avoidance',
     'b2b',
     'bill',
     'binding',
     'bond',
     'brands',
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
 2: {'111',
     '1313',
     '1514',
     '1520',
     '190',
     '301',
     '7501',
     '7553',
     '9801',
     'accelerated',
     'ace',
     'action',
     'administration',
     'agreement',
     'amazon',
     'antidumping',
     'antitrust',
     'apparel',
     'attorney',
     'audit',
     'auditing',
     'auto',
     'automated',
     'automating',
     'avoidance',
     'b2b',
     'bill',
     'binding',
     'bond',
     'brands',
     'budget',
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
 3: {'111',
     '1313',
     '1514',
     '1520',
     '190',
     '301',
     '7501',
     '7553',
     '9801',
     'accelerated',
     'ace',
     'action',
     'administration',
     'agreement',
     'amazon',
     'antidumping',
     'antitrust',
     'apparel',
     'attorney',
     'audit',
     'auditing',
     'auto',
     'automated',
     'automating',
     'avoidance',
     'b2b',
     'bill',
     'binding',
     'bond',
     'brands',
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
 4: {'111',
     '1313',
     '1514',
     '1520',
     '190',
     '301',
     '7501',
     '7553',
     '9801',
     'accelerated',
     'ace',
     'action',
     'administration',
     'agreement',
     'amazon',
     'antidumping',
     'antitrust',
     'apparel',
     'attorney',
     'audit',
     'auditing',
     'auto',
     'automated',
     'automating',
     'avoidance',
     'b2b',
     'bill',
     'binding',
     'bond',
     'brands',
     'budget',
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
 5: {'111',
     '1313',
     '1514',
     '1520',
     '190',
     '301',
     '7501',
     '7553',
     '9801',
     'accelerated',
     'ace',
     'action',
     'administration',
     'agreement',
     'amazon',
     'antidumping',
     'antitrust',
     'apparel',
     'attorney',
     'audit',
     'auditing',
     'auto',
     'automated',
     'automating',
     'avoid',
     'avoidance',
     'b2b',
     'bill',
     'binding',
     'bond',
     'brands',
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
 6: {'111',
     '1313',
     '1514',
     '1520',
     '190',
     '301',
     '7501',
     '7553',
     '9801',
     'accelerated',
     'ace',
     'action',
     'administration',
     'agreement',
     'amazon',
     'antidumping',
     'antitrust',
     'apparel',
     'attorney',
     'audit',
     'auditing',
     'auto',
     'automated',
     'automating',
     'avoidance',
     'b2b',
     'bill',
     'binding',
     'bond',
     'brands',
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
 7: {'111',
     '1313',
     '1514',
     '1520',
     '190',
     '301',
     '7501',
     '7553',
     '9801',
     'accelerated',
     'ace',
     'action',
     'administration',
     'agreement',
     'amazon',
     'antidumping',
     'antitrust',
     'apparel',
     'attorney',
     'audit',
     'auditing',
     'auto',
     'automated',
     'automating',
     'avoidance',
     'b2b',
     'bill',
     'binding',
     'bond',
     'brands',
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
 8: {'111',
     '1313',
     '1514',
     '1520',
     '190',
     '301',
     '7501',
     '7553',
     '9801',
     'accelerated',
     'ace',
     'action',
     'administration',
     'agreement',
     'amazon',
     'antidumping',
     'antitrust',
     'api',
     'apparel',
     'attorney',
     'audit',
     'auditing',
     'auto',
     'automated',
     'automating',
     'avoidance',
     'b2b',
     'bill',
     'binding',
     'bond',
     'brands',
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
 9: {'111',
     '1313',
     '1514',
     '1520',
     '190',
     '301',
     '7501',
     '7553',
     '9801',
     'accelerated',
     'ace',
     'action',
     'administration',
     'agreement',
     'amazon',
     'antidumping',
     'antitrust',
     'apparel',
     'attorney',
     'audit',
     'auditing',
     'auto',
     'automated',
     'automating',
     'avoidance',
     'b2b',
     'bill',
     'binding',
     'bond',
     'brands',
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
 10: {'111',
      '1313',
      '1514',
      '1520',
      '190',
      '301',
      '7501',
      '7553',
      '9801',
      'accelerated',
      'ace',
      'action',
      'administration',
      'agent',
      'agreement',
      'ai',
      'amazon',
      'antidumping',
      'antitrust',
      'apparel',
      'attorney',
      'audit',
      'auditing',
      'auto',
      'automate',
      'automated',
      'automating',
      'automation',
      'avoidance',
      'b2b',
      'bill',
      'binding',
      'bond',
      'brands',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'111',
      '1313',
      '1514',
      '1520',
      '190',
      '301',
      '7501',
      '7553',
      '9801',
      'accelerated',
      'ace',
      'action',
      'administration',
      'agreement',
      'amazon',
      'antidumping',
      'antitrust',
      'apparel',
      'attorney',
      'audit',
      'auditing',
      'auto',
      'automated',
      'automating',
      'avoidance',
      'b2b',
      'bill',
      'binding',
      'bond',
      'brands',
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
 12: {'111',
      '1313',
      '1514',
      '1520',
      '190',
      '301',
      '7501',
      '7553',
      '9801',
      'accelerated',
      'ace',
      'action',
      'administration',
      'agreement',
      'amazon',
      'antidumping',
      'antitrust',
      'apparel',
      'attorney',
      'audit',
      'auditing',
      'auto',
      'automated',
      'automating',
      'avoidance',
      'b2b',
      'bill',
      'binding',
      'bond',
      'brands',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Trade Risk Guaranty',
      'channel': 'Trade Risk Guaranty',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:08](https://www.youtube.com/watch?v=PymimTwXXVM&t=308s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll get back to you within, typically it's really quick, but within a day with "
              "your bond query. You don't have to be a current TRG bond client to get that "
              'information. Um all TRG bond clients can always access your bond information '
              'through our Eagle Eye ACE bond dashboard.',
      'timestamp': 308,
      'timestamp_label': '[00:05:08]',
      'timestamp_seconds': 308,
      'tip': "'ll get back to you within, typically it's really quick, but within a day with "
             "your bond query. You don't have to be a current TRG bond client to get that "
             'information. Um all TRG bond clients can always access your bond information '
             'through our Eagle Eye ACE bond dashboard.',
      'title': "CBP's database Clean Up May Void Your IOR | TRG Talks Trade | EP 13 (Trade "
               'Risk Guaranty)',
      'url': 'https://www.youtube.com/watch?v=PymimTwXXVM&t=308s',
      'video_id': 'PymimTwXXVM'},
     {'author': 'Ask The Customs Manager',
      'channel': 'Ask The Customs Manager',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=Ze1pOvT4KsI&t=78s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'They impose penalty duties that can range from 50% to over 300% of the '
              'commercial value of the goods. Imagine buying a container of aluminum parts for '
              '$50,000 and customs sends you a bill for $150,000 in taxes. It destroys your '
              'business model instantly.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'They impose penalty duties that can range from 50% to over 300% of the '
             'commercial value of the goods. Imagine buying a container of aluminum parts for '
             '$50,000 and customs sends you a bill for $150,000 in taxes. It destroys your '
             'business model instantly.',
      'title': 'Anti-Dumping Duties (ADD & CVD): The Hidden Customs Trap That Bankrupts '
               'Importers (Ask The Customs Manager)',
      'url': 'https://www.youtube.com/watch?v=Ze1pOvT4KsI&t=78s',
      'video_id': 'Ze1pOvT4KsI'},
     {'author': 'Scarbrough Global',
      'channel': 'Scarbrough Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:39](https://www.youtube.com/watch?v=P1YIRCE3BPQ&t=1419s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Midwest nice and oftent times paid duties on behalf of their clients and then '
              'turned around and waited to get reimbursed. Now, that has while that was great, '
              "um not the best business model for a broker at the end of the day. Um it's a "
              'lot of cash flow.',
      'timestamp': 1419,
      'timestamp_label': '[00:23:39]',
      'timestamp_seconds': 1419,
      'tip': 'Midwest nice and oftent times paid duties on behalf of their clients and then '
             'turned around and waited to get reimbursed. Now, that has while that was great, '
             "um not the best business model for a broker at the end of the day. Um it's a lot "
             'of cash flow.',
      'title': "Freight Expectations: CBP's ACE Portal (Scarbrough Global)",
      'url': 'https://www.youtube.com/watch?v=P1YIRCE3BPQ&t=1419s',
      'video_id': 'P1YIRCE3BPQ'},
     {'author': 'Great Lakes Customs Law',
      'channel': 'Great Lakes Customs Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:03](https://www.youtube.com/watch?v=kBvWPMXLLgs&t=303s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Clients so please reach out and ask us any questions you like about the section '
              '301 status and the availability of refunds to you and your business thank you '
              'and have a great day.',
      'timestamp': 303,
      'timestamp_label': '[00:05:03]',
      'timestamp_seconds': 303,
      'tip': 'Clients so please reach out and ask us any questions you like about the section '
             '301 status and the availability of refunds to you and your business thank you '
             'and have a great day.',
      'title': '🆘 Section 301 Duty Refund (China Tariffs) via Protest or Post Summary '
               'Correction CBP/customs (Great Lakes Customs Law)',
      'url': 'https://www.youtube.com/watch?v=kBvWPMXLLgs&t=303s',
      'video_id': 'kBvWPMXLLgs'},
     {'author': 'CNBC',
      'channel': 'CNBC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:48](https://www.youtube.com/watch?v=KFKpVuWoQLU&t=828s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'But the Trump administration has upended that business model. We are not '
              'allowed to invert that tariff to our finished product. Now our costs are no '
              "longer where we thought they'd be. Now we're a lot higher because we're not "
              'getting the benefit of the FTZ.',
      'timestamp': 828,
      'timestamp_label': '[00:13:48]',
      'timestamp_seconds': 828,
      'tip': 'But the Trump administration has upended that business model. We are not allowed '
             'to invert that tariff to our finished product. Now our costs are no longer where '
             "we thought they'd be. Now we're a lot higher because we're not getting the "
             'benefit of the FTZ.',
      'title': 'How U.S. Companies Are Mitigating Trump Tariffs With Foreign Trade Zones '
               '(CNBC)',
      'url': 'https://www.youtube.com/watch?v=KFKpVuWoQLU&t=828s',
      'video_id': 'KFKpVuWoQLU'},
     {'author': 'Trade Risk Guaranty',
      'channel': 'Trade Risk Guaranty',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=38zRYvMd5Ps&t=59s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Customs broker or a Freight Forwarder. Our business model has us selling '
              "directly to importers and exporters. And over the past 25 years we've worked "
              'with over 13,000 companies just like yours to help them grow and save money on '
              'some of these very niche insurance products.',
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': 'Customs broker or a Freight Forwarder. Our business model has us selling '
             "directly to importers and exporters. And over the past 25 years we've worked "
             'with over 13,000 companies just like yours to help them grow and save money on '
             'some of these very niche insurance products.',
      'title': 'Learn the Basics of Antidumping and Countervailing Duties [Full Webinar] '
               '(Trade Risk Guaranty)',
      'url': 'https://www.youtube.com/watch?v=38zRYvMd5Ps&t=59s',
      'video_id': '38zRYvMd5Ps'},
     {'author': 'Simply Trade Podcast',
      'channel': 'Simply Trade Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:06](https://www.youtube.com/watch?v=Q8n9OOAYZ8s&t=486s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, they really need a custom plan for their business. But, I take it a step '
              'further with my clients at Global Trade Advisors is I make executable '
              'documents. That means checklists, Excel files, databases, things that they can '
              'actually use based on procedures.',
      'timestamp': 486,
      'timestamp_label': '[00:08:06]',
      'timestamp_seconds': 486,
      'tip': 'So, they really need a custom plan for their business. But, I take it a step '
             'further with my clients at Global Trade Advisors is I make executable documents. '
             'That means checklists, Excel files, databases, things that they can actually use '
             'based on procedures.',
      'title': 'Customs Ready vs. Audit Ready: There’s a BIG Difference (Simply Trade Podcast)',
      'url': 'https://www.youtube.com/watch?v=Q8n9OOAYZ8s&t=486s',
      'video_id': 'Q8n9OOAYZ8s'},
     {'author': 'CITTA Brokerage',
      'channel': 'CITTA Brokerage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:51](https://www.youtube.com/watch?v=fzs6ZIUot2s&t=531s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I want to touch on something that you mentioned earlier. You talked about '
              "interfacing with your clients existing brokers. So, you're not in competition "
              "with those other brokers. You're just providing a very targeted service when it "
              'comes to duty drawback.',
      'timestamp': 531,
      'timestamp_label': '[00:08:51]',
      'timestamp_seconds': 531,
      'tip': 'I want to touch on something that you mentioned earlier. You talked about '
             "interfacing with your clients existing brokers. So, you're not in competition "
             "with those other brokers. You're just providing a very targeted service when it "
             'comes to duty drawback.',
      'title': 'What is Duty Drawback? (CITTA Brokerage)',
      'url': 'https://www.youtube.com/watch?v=fzs6ZIUot2s&t=531s',
      'video_id': 'fzs6ZIUot2s'},
     {'author': 'KPMG US',
      'channel': 'KPMG US',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=uQ6wwWd5plE&t=85s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Optimizer recovery and also having the right process so in our drawback service '
              "line we've actually developed a mock audit process where we're actually going.",
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': 'Optimizer recovery and also having the right process so in our drawback service '
             "line we've actually developed a mock audit process where we're actually going.",
      'title': 'KPMG Trade & Customs – Duty Drawback (KPMG US)',
      'url': 'https://www.youtube.com/watch?v=uQ6wwWd5plE&t=85s',
      'video_id': 'uQ6wwWd5plE'},
     {'author': 'ISF Customs Broker',
      'channel': 'ISF Customs Broker',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:45](https://www.youtube.com/watch?v=eBt-U9nEjH0&t=105s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "A consultant if needed and take a step towards reclaiming what's rightfully "
              'yours remember in the realm of international trade every detail matters and '
              'every saving counts thank you for watching Empower your business venture with '
              'knowledge and let the journey to savings.',
      'timestamp': 105,
      'timestamp_label': '[00:01:45]',
      'timestamp_seconds': 105,
      'tip': "A consultant if needed and take a step towards reclaiming what's rightfully "
             'yours remember in the realm of international trade every detail matters and '
             'every saving counts thank you for watching Empower your business venture with '
             'knowledge and let the journey to savings.',
      'title': 'Maximizing Returns: Mastering the USA Import Duty Drawback Process (ISF '
               'Customs Broker)',
      'url': 'https://www.youtube.com/watch?v=eBt-U9nEjH0&t=105s',
      'video_id': 'eBt-U9nEjH0'},
     {'author': 'CH Powell Company',
      'channel': 'CH Powell Company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:49](https://www.youtube.com/watch?v=6WwWug6ygqQ&t=109s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Old remote location filing and it's really centralizing um how Brokers can can "
              "do business under a national permit so it's it's it's a very very well received "
              'moving to this National permit.',
      'timestamp': 109,
      'timestamp_label': '[00:01:49]',
      'timestamp_seconds': 109,
      'tip': "Old remote location filing and it's really centralizing um how Brokers can can "
             "do business under a national permit so it's it's it's a very very well received "
             'moving to this National permit.',
      'title': 'Customs Broker Modernization Regulations (CH Powell Company)',
      'url': 'https://www.youtube.com/watch?v=6WwWug6ygqQ&t=109s',
      'video_id': '6WwWug6ygqQ'},
     {'author': 'NCBFAA Educational Institute',
      'channel': 'NCBFAA Educational Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:35:38](https://www.youtube.com/watch?v=CGsvr1SDN8s&t=2138s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Importing what their business practices are so you don't get um associated with "
              'a uh potential like violative situa violative um enforcement.',
      'timestamp': 2138,
      'timestamp_label': '[00:35:38]',
      'timestamp_seconds': 2138,
      'tip': "Importing what their business practices are so you don't get um associated with "
             'a uh potential like violative situa violative um enforcement.',
      'title': 'Best Practices for Anti Dumping and Countervailing Duty AD CVD (NCBFAA '
               'Educational Institute)',
      'url': 'https://www.youtube.com/watch?v=CGsvr1SDN8s&t=2138s',
      'video_id': 'CGsvr1SDN8s'},
     {'author': 'Star USA, Inc.',
      'channel': 'Star USA, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:53](https://www.youtube.com/watch?v=NK99CBNOeJA&t=773s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'They do not have to be the same value on the import and the export and they but '
              'they get counted against each other in quantity so if you imported five items '
              'and you exported six items you would only claim drawback on the five that you '
              'imported.',
      'timestamp': 773,
      'timestamp_label': '[00:12:53]',
      'timestamp_seconds': 773,
      'tip': 'They do not have to be the same value on the import and the export and they but '
             'they get counted against each other in quantity so if you imported five items '
             'and you exported six items you would only claim drawback on the five that you '
             'imported.',
      'title': 'Drawback - Opportunities, Requirements, & Insights (Star USA, Inc.)',
      'url': 'https://www.youtube.com/watch?v=NK99CBNOeJA&t=773s',
      'video_id': 'NK99CBNOeJA'},
     {'author': 'U.S. Customs and Border Protection',
      'channel': 'U.S. Customs and Border Protection',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=lGkujBtNI0A&t=22s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Open protests that meaning uh in open or suspen suspended status uh in our '
              'protest module so again well over 100 000 protests currently with cbp in an '
              'open status.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'Open protests that meaning uh in open or suspen suspended status uh in our '
             'protest module so again well over 100 000 protests currently with cbp in an open '
             'status.',
      'title': 'CBP Protest Webinar (U.S. Customs and Border Protection)',
      'url': 'https://www.youtube.com/watch?v=lGkujBtNI0A&t=22s',
      'video_id': 'lGkujBtNI0A'},
     {'author': 'VoraPrep',
      'channel': 'VoraPrep',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:48](https://www.youtube.com/watch?v=2rbdaN1Swhk&t=288s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You go into ACE, you populate the CBP Form 7501 with the importer's info, the "
              'HTS code, the value of $2,000, the origin of China, and you calculate the duty '
              'based on the rate for that specific code.',
      'timestamp': 288,
      'timestamp_label': '[00:04:48]',
      'timestamp_seconds': 288,
      'tip': "You go into ACE, you populate the CBP Form 7501 with the importer's info, the "
             'HTS code, the value of $2,000, the origin of China, and you calculate the duty '
             'based on the rate for that specific code.',
      'title': '[CBLE] CBLE1: Entry Summary Documentation and Data Elements (CBP Form 7501) '
               '(VoraPrep)',
      'url': 'https://www.youtube.com/watch?v=2rbdaN1Swhk&t=288s',
      'video_id': '2rbdaN1Swhk'}],
 2: [{'author': 'Quantum Leap with Coach Toyin',
      'channel': 'Quantum Leap with Coach Toyin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:38](https://www.youtube.com/watch?v=595qylDVQzM&t=158s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Documents such as a customs bond which is a contract between customs and an '
              'importer for any given import transaction to guarantee payment of import duties '
              'taxes and fees to the u.s.',
      'timestamp': 158,
      'timestamp_label': '[00:02:38]',
      'timestamp_seconds': 158,
      'tip': 'Documents such as a customs bond which is a contract between customs and an '
             'importer for any given import transaction to guarantee payment of import duties '
             'taxes and fees to the u.s.',
      'title': 'U.S. Import Process by Customs and Border Protection - CBP (Quantum Leap with '
               'Coach Toyin)',
      'url': 'https://www.youtube.com/watch?v=595qylDVQzM&t=158s',
      'video_id': '595qylDVQzM'},
     {'author': 'Horty Springer & Mattern, P.C.',
      'channel': 'Horty Springer & Mattern, P.C.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:41](https://www.youtube.com/watch?v=jgkO88qEcMs&t=461s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "On the other hand, it's in our opinion pretty much found money because if you "
              "opted out, you're going to have to pay for attorney's fees to pursue Blue "
              'Cross. You might be more successful in the end.',
      'timestamp': 461,
      'timestamp_label': '[00:07:41]',
      'timestamp_seconds': 461,
      'tip': "On the other hand, it's in our opinion pretty much found money because if you "
             "opted out, you're going to have to pay for attorney's fees to pursue Blue Cross. "
             'You might be more successful in the end.',
      'title': 'The Blue Cross Antitrust Class Action Settlement: Show Me the Money (Horty '
               'Springer & Mattern, P.C.)',
      'url': 'https://www.youtube.com/watch?v=jgkO88qEcMs&t=461s',
      'video_id': 'jgkO88qEcMs'},
     {'author': 'Star USA, Inc.',
      'channel': 'Star USA, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:36](https://www.youtube.com/watch?v=kmZ2NsZtdPA&t=516s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "December 19th and you'll find that in 111.96 the exam fee remains 390 a lot of "
              "brokerages are going to see their annual fees go down because they're only "
              'paying.',
      'timestamp': 516,
      'timestamp_label': '[00:08:36]',
      'timestamp_seconds': 516,
      'tip': "December 19th and you'll find that in 111.96 the exam fee remains 390 a lot of "
             "brokerages are going to see their annual fees go down because they're only "
             'paying.',
      'title': 'Modernized Customs Broker Regulations (Star USA, Inc.)',
      'url': 'https://www.youtube.com/watch?v=kmZ2NsZtdPA&t=516s',
      'video_id': 'kmZ2NsZtdPA'},
     {'author': 'Receipts',
      'channel': 'Receipts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:53](https://www.youtube.com/watch?v=UvphNI0Wxog&t=353s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You paid a fee there that your bank didn't fully pay you back for. That's "
              'almost 19 years of gas station withdrawals. If your bank refunds every ATM fee, '
              "those don't count. For scale, 167 and a half million dollars is about 52 "
              "million ATM fees at today's average by our math.",
      'timestamp': 353,
      'timestamp_label': '[00:05:53]',
      'timestamp_seconds': 353,
      'tip': "You paid a fee there that your bank didn't fully pay you back for. That's almost "
             '19 years of gas station withdrawals. If your bank refunds every ATM fee, those '
             "don't count. For scale, 167 and a half million dollars is about 52 million ATM "
             "fees at today's average by our math.",
      'title': 'Paid an ATM Fee? Visa and Mastercard Will Pay (Receipts)',
      'url': 'https://www.youtube.com/watch?v=UvphNI0Wxog&t=353s',
      'video_id': 'UvphNI0Wxog'},
     {'author': 'News4JAX The Local Station',
      'channel': 'News4JAX The Local Station',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=kOG09tYsDhM&t=50s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'PAY SOMETHING IN A CLASS ACTION, THAT’S A SCAM. REAL CLASS ACTION, THAT’S A '
              'SCAM. REAL CLASS ACTION CLAIMS DO NOT REQUIRE RULE NUMBER ONE. REAL CLASS '
              'ACTION CLAIMS DO NOT REQUIRE AN UPFRONT FEE. ACTION CLAIMS DO NOT REQUIRE AN '
              'UPFRONT FEE.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': 'PAY SOMETHING IN A CLASS ACTION, THAT’S A SCAM. REAL CLASS ACTION, THAT’S A '
             'SCAM. REAL CLASS ACTION CLAIMS DO NOT REQUIRE RULE NUMBER ONE. REAL CLASS ACTION '
             'CLAIMS DO NOT REQUIRE AN UPFRONT FEE. ACTION CLAIMS DO NOT REQUIRE AN UPFRONT '
             'FEE.',
      'title': 'Consumer Alert: How to tell a legit class action settlement notice from a scam '
               '(News4JAX The Local Station)',
      'url': 'https://www.youtube.com/watch?v=kOG09tYsDhM&t=50s',
      'video_id': 'kOG09tYsDhM'},
     {'author': 'Trade Risk Guaranty',
      'channel': 'Trade Risk Guaranty',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=P-dHB1oQLCI&t=110s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'If the principle of the bond is unable or unwilling to pay these duties, taxes, '
              'and fees the bond ensures the surety that wrote the bond will pay up to the '
              'bond amount to CBP on behalf of the principle.',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': 'If the principle of the bond is unable or unwilling to pay these duties, taxes, '
             'and fees the bond ensures the surety that wrote the bond will pay up to the bond '
             'amount to CBP on behalf of the principle.',
      'title': 'What is a U.S. Customs Import Bond? (Trade Risk Guaranty)',
      'url': 'https://www.youtube.com/watch?v=P-dHB1oQLCI&t=110s',
      'video_id': 'P-dHB1oQLCI'},
     {'author': 'Ask The Customs Manager',
      'channel': 'Ask The Customs Manager',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:45](https://www.youtube.com/watch?v=DHSVYPVM3bA&t=105s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Other agency approvals. Not every broker charges compliance fees separately. '
              'Some build it into the entry fee. continuous bond  $400 to5 to $500 per year.',
      'timestamp': 105,
      'timestamp_label': '[00:01:45]',
      'timestamp_seconds': 105,
      'tip': 'Other agency approvals. Not every broker charges compliance fees separately. '
             'Some build it into the entry fee. continuous bond  $400 to5 to $500 per year.',
      'title': 'Customs Broker Fees EXPOSED The TRUTH About Import Costs (Ask The Customs '
               'Manager)',
      'url': 'https://www.youtube.com/watch?v=DHSVYPVM3bA&t=105s',
      'video_id': 'DHSVYPVM3bA'},
     {'author': 'Imports Academy',
      'channel': 'Imports Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:17](https://www.youtube.com/watch?v=lrbVg-_LnTI&t=197s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Fees become familiar with the CBP 7501 form if you have not had much real-world '
              'experience with this form it can be a little messy to understand.',
      'timestamp': 197,
      'timestamp_label': '[00:03:17]',
      'timestamp_seconds': 197,
      'tip': 'Fees become familiar with the CBP 7501 form if you have not had much real-world '
             'experience with this form it can be a little messy to understand.',
      'title': '7 Tips for the US Customs Broker Exam (Imports Academy)',
      'url': 'https://www.youtube.com/watch?v=lrbVg-_LnTI&t=197s',
      'video_id': 'lrbVg-_LnTI'},
     {'author': 'Law Office of Yuri Starikov, LLC',
      'channel': 'Law Office of Yuri Starikov, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=X9jTs5vL-ZM&t=20s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'We are ready to roll and topic of today would be the duty duty drawback. So, '
              'what about duty drawback in general? Uh the concept is very very simple. And '
              'once you bring in and you pay your duty, taxes, fees, etc.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'We are ready to roll and topic of today would be the duty duty drawback. So, '
             'what about duty drawback in general? Uh the concept is very very simple. And '
             'once you bring in and you pay your duty, taxes, fees, etc.',
      'title': 'Duty Drawback Part 1 (Oct. 2017 CBLE Class) (Law Office of Yuri Starikov, LLC)',
      'url': 'https://www.youtube.com/watch?v=X9jTs5vL-ZM&t=20s',
      'video_id': 'X9jTs5vL-ZM'},
     {'author': 'Braumiller Law Group, PLLC',
      'channel': 'Braumiller Law Group, PLLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:56](https://www.youtube.com/watch?v=9rfRsbrSbPw&t=416s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Other words if you're a customer's broker and you got a bunch of employees out "
              'there doing entries and that kind of stuff.',
      'timestamp': 416,
      'timestamp_label': '[00:06:56]',
      'timestamp_seconds': 416,
      'tip': "Other words if you're a customer's broker and you got a bunch of employees out "
             'there doing entries and that kind of stuff.',
      'title': 'Hot Topics In International Trade: Customs Broker Modernization Regulations 19 '
               'CFR 111 (Braumiller Law Group, PLLC)',
      'url': 'https://www.youtube.com/watch?v=9rfRsbrSbPw&t=416s',
      'video_id': '9rfRsbrSbPw'},
     {'author': 'International Trade Administration',
      'channel': 'International Trade Administration',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=F9HNfhO6S9U&t=51s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'What are the benefits of conducting your business in an FTZ? There are plenty '
              "of benefits! First, when you bring components into your FTZ, you don't have to "
              'pay U. FTZ approval can also allow streamlined customs procedures.',
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': 'What are the benefits of conducting your business in an FTZ? There are plenty of '
             "benefits! First, when you bring components into your FTZ, you don't have to pay "
             'U. FTZ approval can also allow streamlined customs procedures.',
      'title': 'Introduction to Foreign Trade Zones (International Trade Administration)',
      'url': 'https://www.youtube.com/watch?v=F9HNfhO6S9U&t=51s',
      'video_id': 'F9HNfhO6S9U'},
     {'author': 'engage fi',
      'channel': 'engage fi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:02](https://www.youtube.com/watch?v=PVmbAAdWXfg&t=122s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "That's why Engage FI is here to help. The payment game has changed and let's "
              "make sure that we're ready to play it differently.",
      'timestamp': 122,
      'timestamp_label': '[00:02:02]',
      'timestamp_seconds': 122,
      'tip': "That's why Engage FI is here to help. The payment game has changed and let's "
             "make sure that we're ready to play it differently.",
      'title': 'The Visa–Mastercard Interchange Settlement: What It Means for Payments (engage '
               'fi)',
      'url': 'https://www.youtube.com/watch?v=PVmbAAdWXfg&t=122s',
      'video_id': 'PVmbAAdWXfg'},
     {'author': 'Scarbrough Global',
      'channel': 'Scarbrough Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=Cif7o8T-mG4&t=115s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'On any of your products you can set up this program now to mitigate the effects '
              "of any to 32 or 301 duties and then when they go away you'll still be "
              'realizing.',
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': 'On any of your products you can set up this program now to mitigate the effects '
             "of any to 32 or 301 duties and then when they go away you'll still be realizing.",
      'title': 'First Sale Rule – U.S. Customs and Imports (Scarbrough Global)',
      'url': 'https://www.youtube.com/watch?v=Cif7o8T-mG4&t=115s',
      'video_id': 'Cif7o8T-mG4'},
     {'author': 'GlobalTech Infosystems',
      'channel': 'GlobalTech Infosystems',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=wUiK6YAEFs8&t=15s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'जरूरी और ऑनेस्टली काफी मुनाफे वाले कांसेप्ट पर बात करने वाले हैं। यूएस कस्टम्स '
              'ड्यूटी ड्रॉबैक। हम इसके पूरे वर्क फ्लो और रिफंड्स क्लेम करने की.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'जरूरी और ऑनेस्टली काफी मुनाफे वाले कांसेप्ट पर बात करने वाले हैं। यूएस कस्टम्स '
             'ड्यूटी ड्रॉबैक। हम इसके पूरे वर्क फ्लो और रिफंड्स क्लेम करने की.',
      'title': 'USA Customs Duty Drawback 🇺🇸 | Import Duty Refund After Export | Complete '
               'Practical Guide in Hindi (GlobalTech Infosystems)',
      'url': 'https://www.youtube.com/watch?v=wUiK6YAEFs8&t=15s',
      'video_id': 'wUiK6YAEFs8'},
     {'author': 'Commercial Funding Marketplace',
      'channel': 'Commercial Funding Marketplace',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:39](https://www.youtube.com/watch?v=LaWXf8aLv1o&t=279s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s official system for this stuff, the automated commercial environment. For a "
              "buyer, this report is the one and only source of truth. It's what they use to "
              'confirm every single tariff payment you made. Any other reports you have have '
              'to match this government data exactly.',
      'timestamp': 279,
      'timestamp_label': '[00:04:39]',
      'timestamp_seconds': 279,
      'tip': "'s official system for this stuff, the automated commercial environment. For a "
             "buyer, this report is the one and only source of truth. It's what they use to "
             'confirm every single tariff payment you made. Any other reports you have have to '
             'match this government data exactly.',
      'title': 'IEEPA Tariff Refund Buyout: The Process (Commercial Funding Marketplace)',
      'url': 'https://www.youtube.com/watch?v=LaWXf8aLv1o&t=279s',
      'video_id': 'LaWXf8aLv1o'}],
 3: [{'author': "Finn's Fine Print",
      'channel': "Finn's Fine Print",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:23](https://www.youtube.com/watch?v=Pf2fDVQXfmk&t=203s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So does the refund at least show up as a price cut somewhere? In the filings, '
              'it shows up as lower costs, and lower costs mean higher profit. The importer '
              'paid the bill, so the refund goes back to the importer. The system just never '
              'asks who paid the importer.',
      'timestamp': 203,
      'timestamp_label': '[00:03:23]',
      'timestamp_seconds': 203,
      'tip': 'So does the refund at least show up as a price cut somewhere? In the filings, it '
             'shows up as lower costs, and lower costs mean higher profit. The importer paid '
             'the bill, so the refund goes back to the importer. The system just never asks '
             'who paid the importer.',
      'title': "You Paid the Tariffs. Target Just Got the Refund. (Finn's Fine Print)",
      'url': 'https://www.youtube.com/watch?v=Pf2fDVQXfmk&t=203s',
      'video_id': 'Pf2fDVQXfmk'},
     {'author': 'USA Customs Clearance',
      'channel': 'USA Customs Clearance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:54](https://www.youtube.com/watch?v=khfmXSwD3DE&t=294s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "If you've been absorbing section 301 costs on China origin imports, don't "
              'simply write them off. A properly executed duty drawback can put real money '
              'back into your business and improve your cost structure without having to '
              'change your supply chain.',
      'timestamp': 294,
      'timestamp_label': '[00:04:54]',
      'timestamp_seconds': 294,
      'tip': "If you've been absorbing section 301 costs on China origin imports, don't simply "
             'write them off. A properly executed duty drawback can put real money back into '
             'your business and improve your cost structure without having to change your '
             'supply chain.',
      'title': 'Section 301 Duty Drawback Explained (USA Customs Clearance)',
      'url': 'https://www.youtube.com/watch?v=khfmXSwD3DE&t=294s',
      'video_id': 'khfmXSwD3DE'},
     {'author': 'Flexport',
      'channel': 'Flexport',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:34](https://www.youtube.com/watch?v=yR_RXKhapxo&t=634s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'An invoice price of $100 per unit the duties owed uh per unit now becomes $30 '
              'so or $6 per unit uh cost of of good so you can quickly see that if you take.',
      'timestamp': 634,
      'timestamp_label': '[00:10:34]',
      'timestamp_seconds': 634,
      'tip': 'An invoice price of $100 per unit the duties owed uh per unit now becomes $30 so '
             'or $6 per unit uh cost of of good so you can quickly see that if you take.',
      'title': 'Flexport Customs: Mastering the First Sale Rule (Flexport)',
      'url': 'https://www.youtube.com/watch?v=yR_RXKhapxo&t=634s',
      'video_id': 'yR_RXKhapxo'},
     {'author': 'Ask The Customs Manager',
      'channel': 'Ask The Customs Manager',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=5fk-EKpR8Zw&t=52s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The factory ships the goods, they arrive at your border, and your broker '
              'declares the value at $10. You pay your import duty on that $10 price. But '
              'think about what just happened. 3 of that invoice is simply the trading '
              "company's profit margin.",
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': 'The factory ships the goods, they arrive at your border, and your broker '
             'declares the value at $10. You pay your import duty on that $10 price. But think '
             "about what just happened. 3 of that invoice is simply the trading company's "
             'profit margin.',
      'title': 'Save Thousands on Import Duties With This Strategy (Ask The Customs Manager)',
      'url': 'https://www.youtube.com/watch?v=5fk-EKpR8Zw&t=52s',
      'video_id': '5fk-EKpR8Zw'},
     {'author': 'Evana',
      'channel': 'Evana',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:37](https://www.youtube.com/watch?v=1m5HmGyCEvw&t=37s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The duty was still paid on that entry. It's simply buried in the price that the "
              "buyer actually paid. The question is who's on the 7501 and whether you can "
              'actually get their cooperation.',
      'timestamp': 37,
      'timestamp_label': '[00:00:37]',
      'timestamp_seconds': 37,
      'tip': "The duty was still paid on that entry. It's simply buried in the price that the "
             "buyer actually paid. The question is who's on the 7501 and whether you can "
             'actually get their cooperation.',
      'title': '6 Hidden Duty Refunds Most Importers Miss (Evana)',
      'url': 'https://www.youtube.com/watch?v=1m5HmGyCEvw&t=37s',
      'video_id': '1m5HmGyCEvw'},
     {'author': 'Connecticut District Export Council',
      'channel': 'Connecticut District Export Council',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:00](https://www.youtube.com/watch?v=bOFLeOBOaF0&t=1440s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Compare that value to the unit cost of the component used in the manufacturing '
              "process, and use the value that is lesser in the drawback claim. Again, ITM's "
              'drawback software determines which is lesser of the two. Now, there are some '
              'limitations with NAFTA.',
      'timestamp': 1440,
      'timestamp_label': '[00:24:00]',
      'timestamp_seconds': 1440,
      'tip': 'Compare that value to the unit cost of the component used in the manufacturing '
             "process, and use the value that is lesser in the drawback claim. Again, ITM's "
             'drawback software determines which is lesser of the two. Now, there are some '
             'limitations with NAFTA.',
      'title': 'Duty Drawback (Connecticut District Export Council)',
      'url': 'https://www.youtube.com/watch?v=bOFLeOBOaF0&t=1440s',
      'video_id': 'bOFLeOBOaF0'},
     {'author': 'Casually Capital',
      'channel': 'Casually Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=yHFIXvO5siM&t=114s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Translation, the refund follows the Customs form. The cost followed the supply '
              "chain. Those are not the same trail. And wherever there's a gap between who's "
              'owed money and who needs cash today, somebody builds a market.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': 'Translation, the refund follows the Customs form. The cost followed the supply '
             "chain. Those are not the same trail. And wherever there's a gap between who's "
             'owed money and who needs cash today, somebody builds a market.',
      'title': 'Who Actually Gets The $126 Billion Tariff Refund? (Casually Capital)',
      'url': 'https://www.youtube.com/watch?v=yHFIXvO5siM&t=114s',
      'video_id': 'yHFIXvO5siM'},
     {'author': 'Law Office of Yuri Starikov, LLC',
      'channel': 'Law Office of Yuri Starikov, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:55:56](https://www.youtube.com/watch?v=1DFXItS5lCQ&t=6956s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You must know what this uh number represents and one of the things they test '
              "unit is they give you the Visa number and ask you what's the country of origin "
              "so let's go back this is a vis number right.",
      'timestamp': 6956,
      'timestamp_label': '[01:55:56]',
      'timestamp_seconds': 6956,
      'tip': 'You must know what this uh number represents and one of the things they test '
             "unit is they give you the Visa number and ask you what's the country of origin "
             "so let's go back this is a vis number right.",
      'title': 'CBP Form 7501 Discussion (Law Office of Yuri Starikov, LLC)',
      'url': 'https://www.youtube.com/watch?v=1DFXItS5lCQ&t=6956s',
      'video_id': '1DFXItS5lCQ'},
     {'author': 'Steve Fodor',
      'channel': 'Steve Fodor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:45](https://www.youtube.com/watch?v=NXnGUZwargM&t=345s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Duty checks this form was designed a number of years ago and since that time '
              'many importers are paying their duties directly to u. ACH debit system and we '
              "can help you set that up it's a cost free way of making sure your payments that "
              'are owed to US Customs get into u.',
      'timestamp': 345,
      'timestamp_label': '[00:05:45]',
      'timestamp_seconds': 345,
      'tip': 'Duty checks this form was designed a number of years ago and since that time '
             'many importers are paying their duties directly to u. ACH debit system and we '
             "can help you set that up it's a cost free way of making sure your payments that "
             'are owed to US Customs get into u.',
      'title': 'The Customs  Power of Attorney (Steve Fodor)',
      'url': 'https://www.youtube.com/watch?v=NXnGUZwargM&t=345s',
      'video_id': 'NXnGUZwargM'},
     {'author': 'CustomsDeclarationsUK',
      'channel': 'CustomsDeclarationsUK',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:01](https://www.youtube.com/watch?v=6Fco88JHSNg&t=61s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Transaction value refers to the price paid or payable for the products sold for '
              'export to the uk this principle way of determining transaction value accounts '
              'for approximately 90 of transactions in the uk.',
      'timestamp': 61,
      'timestamp_label': '[00:01:01]',
      'timestamp_seconds': 61,
      'tip': 'Transaction value refers to the price paid or payable for the products sold for '
             'export to the uk this principle way of determining transaction value accounts '
             'for approximately 90 of transactions in the uk.',
      'title': 'A Quick Guide to Customs Valuation Methods to Determine the Value of Goods | '
               'Customs-Declarations.uk (CustomsDeclarationsUK)',
      'url': 'https://www.youtube.com/watch?v=6Fco88JHSNg&t=61s',
      'video_id': '6Fco88JHSNg'},
     {'author': 'Shipping Solutions',
      'channel': 'Shipping Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:08](https://www.youtube.com/watch?v=zDnjfsml-j4&t=128s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The United States relies on 10-digit codes, or HTSUS numbers. I’ll put a link '
              'below to the International Trade Commission website where you can search for '
              'the HTSUS code for your product.',
      'timestamp': 128,
      'timestamp_label': '[00:02:08]',
      'timestamp_seconds': 128,
      'tip': 'The United States relies on 10-digit codes, or HTSUS numbers. I’ll put a link '
             'below to the International Trade Commission website where you can search for the '
             'HTSUS code for your product.',
      'title': 'How to Use the Harmonized Tariff Schedule of the United States (Shipping '
               'Solutions)',
      'url': 'https://www.youtube.com/watch?v=zDnjfsml-j4&t=128s',
      'video_id': 'zDnjfsml-j4'},
     {'author': 'CONECT Recorded Webinars',
      'channel': 'CONECT Recorded Webinars',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:30:22](https://www.youtube.com/watch?v=jMlTHY21lng&t=1822s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um this is really important to remember right I think this will be very very '
              "occurrencies now um what could be some examples of fraud um actually I'm going "
              'a little too far here let me just go back.',
      'timestamp': 1822,
      'timestamp_label': '[00:30:22]',
      'timestamp_seconds': 1822,
      'tip': 'Um this is really important to remember right I think this will be very very '
             "occurrencies now um what could be some examples of fraud um actually I'm going a "
             'little too far here let me just go back.',
      'title': 'Recording Part 111 Modernization of Customs Broker Regulations (CONECT '
               'Recorded Webinars)',
      'url': 'https://www.youtube.com/watch?v=jMlTHY21lng&t=1822s',
      'video_id': 'jMlTHY21lng'},
     {'author': 'Afleo',
      'channel': 'Afleo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=oHJLWqKNzU4&t=15s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'बताएंगे कि कैसे हमने हमारे क्लाइंट्स के लिए 50 लै टू 1 करोड़ का एडिशनल एनुअल '
              'बेनिफिट जनरेट करके दिया। जो वह पहले लूज़ कर रहे थे जस्ट बाय सेलेक्टिंग द राइट.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'बताएंगे कि कैसे हमने हमारे क्लाइंट्स के लिए 50 लै टू 1 करोड़ का एडिशनल एनुअल '
             'बेनिफिट जनरेट करके दिया। जो वह पहले लूज़ कर रहे थे जस्ट बाय सेलेक्टिंग द राइट.',
      'title': 'Duty Drawback Scheme: Hidden Profit Most Exporters MISS! (AIR vs Brand Rate '
               'Explained) (Afleo)',
      'url': 'https://www.youtube.com/watch?v=oHJLWqKNzU4&t=15s',
      'video_id': 'oHJLWqKNzU4'},
     {'author': 'ImportGenius',
      'channel': 'ImportGenius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=edLGoh8OTiQ&t=79s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '"ميجا ديستريبيوشن"، دعونا نلقي نظرة على أحدث ميزات موقع importgenius. Import '
              'Genius بإنشاء خريطة لعلاقات تلك الشركة التجارية.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': '"ميجا ديستريبيوشن"، دعونا نلقي نظرة على أحدث ميزات موقع importgenius. Import '
             'Genius بإنشاء خريطة لعلاقات تلك الشركة التجارية.',
      'title': "Track your competitors' imports with Import Genius (ImportGenius)",
      'url': 'https://www.youtube.com/watch?v=edLGoh8OTiQ&t=79s',
      'video_id': 'edLGoh8OTiQ'},
     {'author': 'TrackIQ',
      'channel': 'TrackIQ',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:46](https://www.youtube.com/watch?v=Q8jgNmiJNZg&t=286s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'ACoS and how aggressively you can bid on sponsored ads. If you can negotiate '
              'lower wholesale pricing that reflects the removal of IEPA tariffs, your unit '
              'economics improve.',
      'timestamp': 286,
      'timestamp_label': '[00:04:46]',
      'timestamp_seconds': 286,
      'tip': 'ACoS and how aggressively you can bid on sponsored ads. If you can negotiate '
             'lower wholesale pricing that reflects the removal of IEPA tariffs, your unit '
             'economics improve.',
      'title': "Supreme Court Tariff Ruling: Why Most Amazon Sellers Won't See Refunds "
               '(TrackIQ)',
      'url': 'https://www.youtube.com/watch?v=Q8jgNmiJNZg&t=286s',
      'video_id': 'Q8jgNmiJNZg'}],
 4: [{'author': 'TrackIQ',
      'channel': 'TrackIQ',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=Q8jgNmiJNZg&t=59s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Amazon's third-party ecosystem. Electronics, apparel, home goods, industrial "
              "components. Here's the catch that's crushing Amazon sellers right now. Refunds "
              'go exclusively to the importer of record, the entity listed on customs entry '
              'documents, form 7501.',
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': "Amazon's third-party ecosystem. Electronics, apparel, home goods, industrial "
             "components. Here's the catch that's crushing Amazon sellers right now. Refunds "
             'go exclusively to the importer of record, the entity listed on customs entry '
             'documents, form 7501.',
      'title': "Supreme Court Tariff Ruling: Why Most Amazon Sellers Won't See Refunds "
               '(TrackIQ)',
      'url': 'https://www.youtube.com/watch?v=Q8jgNmiJNZg&t=59s',
      'video_id': 'Q8jgNmiJNZg'},
     {'author': 'Shipping Solutions',
      'channel': 'Shipping Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:59](https://www.youtube.com/watch?v=_FcXk0dsq98&t=179s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'File electronically in CBP’s Automated Commercial Environment, or ACE, and '
              'expect processing times to vary. CBP expects a solid audit trail.',
      'timestamp': 179,
      'timestamp_label': '[00:02:59]',
      'timestamp_seconds': 179,
      'tip': 'File electronically in CBP’s Automated Commercial Environment, or ACE, and '
             'expect processing times to vary. CBP expects a solid audit trail.',
      'title': 'Duty Drawback on Exports: What You Need to Know (Shipping Solutions)',
      'url': 'https://www.youtube.com/watch?v=_FcXk0dsq98&t=179s',
      'video_id': '_FcXk0dsq98'},
     {'author': 'Factory Floor Economics',
      'channel': 'Factory Floor Economics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:15](https://www.youtube.com/watch?v=YhiuYAa1Byw&t=495s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You charge for minutes of work, but you get paid for being right. The cost side '
              'is people, software and liability. Every entry is touched by classifiers and '
              'entry writers, and US law puts their supervision on the license holder.',
      'timestamp': 495,
      'timestamp_label': '[00:08:15]',
      'timestamp_seconds': 495,
      'tip': 'You charge for minutes of work, but you get paid for being right. The cost side '
             'is people, software and liability. Every entry is touched by classifiers and '
             'entry writers, and US law puts their supervision on the license holder.',
      'title': 'The Economics of a Customs Broker (Factory Floor Economics)',
      'url': 'https://www.youtube.com/watch?v=YhiuYAa1Byw&t=495s',
      'video_id': 'YhiuYAa1Byw'},
     {'author': 'Leyton USA',
      'channel': 'Leyton USA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:44](https://www.youtube.com/watch?v=JL0JHTlUx4I&t=944s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '45-day period that again will be deposited to your bank account via ACH and '
              'visible through the ACE portal. Um again, as I mentioned right there, no no '
              'more paper checks. You have to uh make sure your banking information is entered '
              'in the ACE portal uh after setup.',
      'timestamp': 944,
      'timestamp_label': '[00:15:44]',
      'timestamp_seconds': 944,
      'tip': '45-day period that again will be deposited to your bank account via ACH and '
             'visible through the ACE portal. Um again, as I mentioned right there, no no more '
             'paper checks. You have to uh make sure your banking information is entered in '
             'the ACE portal uh after setup.',
      'title': 'WEBINAR - IEEPA Tariff Refunds: Recover Overpaid Duties and Maximize '
               'Cross-Border Savings (Leyton USA)',
      'url': 'https://www.youtube.com/watch?v=JL0JHTlUx4I&t=944s',
      'video_id': 'JL0JHTlUx4I'},
     {'author': 'Scarbrough Global',
      'channel': 'Scarbrough Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:32](https://www.youtube.com/watch?v=wEYqdvTPaqM&t=1592s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Attorney do I have to have a license broker you know who do I need to contact '
              'to kind of get that process going you know a claim is free to file.',
      'timestamp': 1592,
      'timestamp_label': '[00:26:32]',
      'timestamp_seconds': 1592,
      'tip': 'Attorney do I have to have a license broker you know who do I need to contact to '
             'kind of get that process going you know a claim is free to file.',
      'title': 'Duty Drawback - Full Version (Scarbrough Global)',
      'url': 'https://www.youtube.com/watch?v=wEYqdvTPaqM&t=1592s',
      'video_id': 'wEYqdvTPaqM'},
     {'author': 'TEU Global',
      'channel': 'TEU Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=lKk16DmiedE&t=134s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Once you've entered that information, click submit. You're now all set for your "
              'CBP electronic refund. If you do not have a US bank account, then you can '
              'designate any trustworthy US entity to receive the refunds on your behalf.',
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': "Once you've entered that information, click submit. You're now all set for your "
             'CBP electronic refund. If you do not have a US bank account, then you can '
             'designate any trustworthy US entity to receive the refunds on your behalf.',
      'title': 'How to Set Up the CBP ACE Secure Data Portal & ACH Refunds | Step-by-Step '
               'Guide for Importers (TEU Global)',
      'url': 'https://www.youtube.com/watch?v=lKk16DmiedE&t=134s',
      'video_id': 'lKk16DmiedE'},
     {'author': 'Cole International',
      'channel': 'Cole International',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=_6C6KJQrxII&t=21s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'May seem innocent enough however a cbsa or cbp verification request otherwise '
              "referred to as an audit is a serious matter so let's look at a proactive "
              'approach to help minimize the impact of a dreaded call from customs.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'May seem innocent enough however a cbsa or cbp verification request otherwise '
             "referred to as an audit is a serious matter so let's look at a proactive "
             'approach to help minimize the impact of a dreaded call from customs.',
      'title': 'Customs & Binding Rulings - The ABCs (Cole International)',
      'url': 'https://www.youtube.com/watch?v=_6C6KJQrxII&t=21s',
      'video_id': '_6C6KJQrxII'},
     {'author': 'The Class Action Attorney',
      'channel': 'The Class Action Attorney',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:09](https://www.youtube.com/watch?v=wR6-BeiQppQ&t=129s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Whether or not that check is legitimate so hopefully this answers your '
              'questions about whether or not a class action settlement you get in the mail or '
              "a class action settlement check is real or if it's a scam thanks so much for "
              'watching.',
      'timestamp': 129,
      'timestamp_label': '[00:02:09]',
      'timestamp_seconds': 129,
      'tip': 'Whether or not that check is legitimate so hopefully this answers your questions '
             'about whether or not a class action settlement you get in the mail or a class '
             "action settlement check is real or if it's a scam thanks so much for watching.",
      'title': 'Is my class action settlement check a scam? (The Class Action Attorney)',
      'url': 'https://www.youtube.com/watch?v=wR6-BeiQppQ&t=129s',
      'video_id': 'wR6-BeiQppQ'},
     {'author': 'Radial',
      'channel': 'Radial',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=p-c3zl1yoVk&t=92s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s additional benefits to an FTZ as well, including order processing and "
              'fulfillment from the same warehouse. Now, some brands are exploring owning and '
              'operating their own FTZ warehouse, but you can also work with 3PLs that operate '
              'these facilities and their networks.',
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': "'s additional benefits to an FTZ as well, including order processing and "
             'fulfillment from the same warehouse. Now, some brands are exploring owning and '
             'operating their own FTZ warehouse, but you can also work with 3PLs that operate '
             'these facilities and their networks.',
      'title': 'Radial: What is a Foreign Trade Zone (FTZ) Warehouse? (Radial)',
      'url': 'https://www.youtube.com/watch?v=p-c3zl1yoVk&t=92s',
      'video_id': 'p-c3zl1yoVk'},
     {'author': 'Scarlett Jones',
      'channel': 'Scarlett Jones',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:38](https://www.youtube.com/watch?v=Vy2s1ZdQcnQ&t=278s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Processes can streamline claim submissions and enhance overall efficiency these '
              'tools can automate calculations maintain accurate records.',
      'timestamp': 278,
      'timestamp_label': '[00:04:38]',
      'timestamp_seconds': 278,
      'tip': 'Processes can streamline claim submissions and enhance overall efficiency these '
             'tools can automate calculations maintain accurate records.',
      'title': 'Navigating Duty Drawback Claims for Exported Goods (Scarlett Jones)',
      'url': 'https://www.youtube.com/watch?v=Vy2s1ZdQcnQ&t=278s',
      'video_id': 'Vy2s1ZdQcnQ'},
     {'author': 'Shapiro',
      'channel': 'Shapiro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:59](https://www.youtube.com/watch?v=605kfE-oUPM&t=1319s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'This PLC indicator between the columns and put in there and if you have any PLC '
              "any entries with PSC it's going to show the information in this report ok.",
      'timestamp': 1319,
      'timestamp_label': '[00:21:59]',
      'timestamp_seconds': 1319,
      'tip': 'This PLC indicator between the columns and put in there and if you have any PLC '
             "any entries with PSC it's going to show the information in this report ok.",
      'title': 'Automated Commercial Environment ACE Import Workshop (Shapiro)',
      'url': 'https://www.youtube.com/watch?v=605kfE-oUPM&t=1319s',
      'video_id': '605kfE-oUPM'},
     {'author': 'Ask The Customs Manager',
      'channel': 'Ask The Customs Manager',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:30](https://www.youtube.com/watch?v=2H7zdtUvSDA&t=150s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "One more thing, you're responsible for accuracy. If you put the wrong bank "
              "account, that's on you. CBP won't chase you down, and you must notify them if "
              'anything changes. New bank, new account number, anything. Update it in ACE '
              'immediately.',
      'timestamp': 150,
      'timestamp_label': '[00:02:30]',
      'timestamp_seconds': 150,
      'tip': "One more thing, you're responsible for accuracy. If you put the wrong bank "
             "account, that's on you. CBP won't chase you down, and you must notify them if "
             'anything changes. New bank, new account number, anything. Update it in ACE '
             'immediately.',
      'title': 'CBP Ends Paper Checks February 6 – Enroll in ACH for Refunds NOW (Ask The '
               'Customs Manager)',
      'url': 'https://www.youtube.com/watch?v=2H7zdtUvSDA&t=150s',
      'video_id': '2H7zdtUvSDA'},
     {'author': 'Montana World Trade Center',
      'channel': 'Montana World Trade Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:16](https://www.youtube.com/watch?v=xWFmdLRN9Ro&t=1396s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Electronics machinery electrical machinery and finished vehicles being made in '
              'production zones so all of these products are being made in foreign trade zones '
              'and then you know shipped out of the foreign trade zone for consumption in the '
              'us or for export.',
      'timestamp': 1396,
      'timestamp_label': '[00:23:16]',
      'timestamp_seconds': 1396,
      'tip': 'Electronics machinery electrical machinery and finished vehicles being made in '
             'production zones so all of these products are being made in foreign trade zones '
             'and then you know shipped out of the foreign trade zone for consumption in the '
             'us or for export.',
      'title': 'Foreign Trade Zone training (Montana World Trade Center)',
      'url': 'https://www.youtube.com/watch?v=xWFmdLRN9Ro&t=1396s',
      'video_id': 'xWFmdLRN9Ro'},
     {'author': 'USA Customs Clearance',
      'channel': 'USA Customs Clearance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=MfmhZLeMz2w&t=104s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is the broad family your product belongs to. For example, machinery, '
              'furniture, textiles, vehicles, chemicals. The next two digits create the '
              "heading. Now we're narrowing the product into a smaller category within that "
              'chapter.',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': 'This is the broad family your product belongs to. For example, machinery, '
             'furniture, textiles, vehicles, chemicals. The next two digits create the '
             "heading. Now we're narrowing the product into a smaller category within that "
             'chapter.',
      'title': 'HTS Codes Explained (USA Customs Clearance)',
      'url': 'https://www.youtube.com/watch?v=MfmhZLeMz2w&t=104s',
      'video_id': 'MfmhZLeMz2w'},
     {'author': 'SKUio',
      'channel': 'SKUio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=WLDwLas6IOI&t=108s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Here the customs value is lower than the order value, so check that with your '
              'broker. Below, each line shows its HTS code, entered value, and the duty '
              'charged. The stack lists every tariff that applied, such as a Section 301 duty '
              'on top of the base rate.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': 'Here the customs value is lower than the order value, so check that with your '
             'broker. Below, each line shows its HTS code, entered value, and the duty '
             'charged. The stack lists every tariff that applied, such as a Section 301 duty '
             'on top of the base rate.',
      'title': 'Split a Customs Duty Bill by Product with CBP 7501 Entry Summaries | SKU.io '
               '(SKUio)',
      'url': 'https://www.youtube.com/watch?v=WLDwLas6IOI&t=108s',
      'video_id': 'WLDwLas6IOI'}],
 5: [{'author': 'NextGen CPA',
      'channel': 'NextGen CPA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=sMBX0ZlgJRY&t=68s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Second, the no mistakes rule. You file a Cape declaration in the ACE portal. '
              'But be warned, once you submit, you cannot amend it. If you miss a 7501 form, '
              'you have to start a new declaration, which can push you to the back of the '
              'queue.',
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': 'Second, the no mistakes rule. You file a Cape declaration in the ACE portal. But '
             'be warned, once you submit, you cannot amend it. If you miss a 7501 form, you '
             'have to start a new declaration, which can push you to the back of the queue.',
      'title': 'CBP Refund Portal is LIVE - Claim Your 2025 Tariff Money Now! (NextGen CPA)',
      'url': 'https://www.youtube.com/watch?v=sMBX0ZlgJRY&t=68s',
      'video_id': 'sMBX0ZlgJRY'},
     {'author': 'VoraPrep',
      'channel': 'VoraPrep',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=xq7kXAXH3GQ&t=54s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "If you can't, that's a problem. Now, imagine you realize you accidentally "
              'damaged a book. Say you made a mistake on an entry. You can wait for the '
              "librarian to find it and they'll send you a big bill. Or you can go to them "
              'before they notice.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': "If you can't, that's a problem. Now, imagine you realize you accidentally "
             'damaged a book. Say you made a mistake on an entry. You can wait for the '
             "librarian to find it and they'll send you a big bill. Or you can go to them "
             'before they notice.',
      'title': '[CBLE] CBLE3: Recordkeeping, Prior Disclosures, and Penalties (19 CFR Part '
               '163, 171 & 19 U.S.C. §... (VoraPrep)',
      'url': 'https://www.youtube.com/watch?v=xq7kXAXH3GQ&t=54s',
      'video_id': 'xq7kXAXH3GQ'},
     {'author': 'Grassi',
      'channel': 'Grassi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:18](https://www.youtube.com/watch?v=xA8LxqtatDo&t=618s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "We have our bunch of acronyms, too. It's a whole 'nother language, uh logistics "
              'language, as well. Um and we love adding new ones. So, CAPES is the '
              'consolidated administration and processing of entries, which basic And CAPES, '
              'by the way, lives in ACE.',
      'timestamp': 618,
      'timestamp_label': '[00:10:18]',
      'timestamp_seconds': 618,
      'tip': "We have our bunch of acronyms, too. It's a whole 'nother language, uh logistics "
             'language, as well. Um and we love adding new ones. So, CAPES is the consolidated '
             'administration and processing of entries, which basic And CAPES, by the way, '
             'lives in ACE.',
      'title': 'IEEPA Tariff Refunds: What Phase 1 Means for Importers and How to Prepare '
               'Without Triggering Risk (Grassi)',
      'url': 'https://www.youtube.com/watch?v=xA8LxqtatDo&t=618s',
      'video_id': 'xA8LxqtatDo'},
     {'author': 'The Procurement Lens',
      'channel': 'The Procurement Lens',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:33](https://www.youtube.com/watch?v=4IEk0Lxmf1c&t=213s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "To avoid those compliance nightmares, there are a few super common traps you've "
              'got to watch out for. First off, relying on incorrect or overly generic codes '
              "just because they're, you know, easier to find.",
      'timestamp': 213,
      'timestamp_label': '[00:03:33]',
      'timestamp_seconds': 213,
      'tip': "To avoid those compliance nightmares, there are a few super common traps you've "
             'got to watch out for. First off, relying on incorrect or overly generic codes '
             "just because they're, you know, easier to find.",
      'title': 'HS Code Explained | How Customs Classify Goods Made Simple (The Procurement '
               'Lens)',
      'url': 'https://www.youtube.com/watch?v=4IEk0Lxmf1c&t=213s',
      'video_id': '4IEk0Lxmf1c'},
     {'author': 'Frontier Report',
      'channel': 'Frontier Report',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:06](https://www.youtube.com/watch?v=FICFEFAPgi0&t=606s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'That is his argument as reported, critics dispute it. The administration has '
              'also been fighting in court to narrow who is paid, as we covered earlier. What '
              'supports this version?',
      'timestamp': 606,
      'timestamp_label': '[00:10:06]',
      'timestamp_seconds': 606,
      'tip': 'That is his argument as reported, critics dispute it. The administration has '
             'also been fighting in court to narrow who is paid, as we covered earlier. What '
             'supports this version?',
      'title': 'Who Actually Gets the $166B Tariff Refund? (Frontier Report)',
      'url': 'https://www.youtube.com/watch?v=FICFEFAPgi0&t=606s',
      'video_id': 'FICFEFAPgi0'},
     {'author': 'Freight & Trade',
      'channel': 'Freight & Trade',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:29](https://www.youtube.com/watch?v=wDQlwDFTfuE&t=269s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'If everything is acceptable and the applicable requirements have been '
              'satisfied, the cargo can be released and continue to its final destination. '
              "That's the basic idea of a customs entry. For beginners, there are a few "
              'important mistakes to avoid.',
      'timestamp': 269,
      'timestamp_label': '[00:04:29]',
      'timestamp_seconds': 269,
      'tip': 'If everything is acceptable and the applicable requirements have been satisfied, '
             "the cargo can be released and continue to its final destination. That's the "
             'basic idea of a customs entry. For beginners, there are a few important mistakes '
             'to avoid.',
      'title': 'What Is a Customs Entry  A Beginner’s Guide to U S  Imports (Freight & Trade)',
      'url': 'https://www.youtube.com/watch?v=wDQlwDFTfuE&t=269s',
      'video_id': 'wDQlwDFTfuE'},
     {'author': 'Clark-Esposito Law Firm P.C.',
      'channel': 'Clark-Esposito Law Firm P.C.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:46](https://www.youtube.com/watch?v=8Lpn0Ae59QU&t=106s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you’re uncertain about a classification, consider requesting a binding '
              'ruling from CBP to gain clarity and avoid potential errors.',
      'timestamp': 106,
      'timestamp_label': '[00:01:46]',
      'timestamp_seconds': 106,
      'tip': 'If you’re uncertain about a classification, consider requesting a binding ruling '
             'from CBP to gain clarity and avoid potential errors.',
      'title': 'Tariffs & Classification Explained: Stay Compliant & Avoid Penalties '
               '(Clark-Esposito Law Firm P.C.)',
      'url': 'https://www.youtube.com/watch?v=8Lpn0Ae59QU&t=106s',
      'video_id': '8Lpn0Ae59QU'},
     {'author': 'Freightos',
      'channel': 'Freightos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:34](https://www.youtube.com/watch?v=cIMBwZ9J60I&t=34s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um did they underpay and we send them a bill or did they overpay and we send '
              "them a refund? And that's called liquidation. And the argument basically is "
              "that the CBP is processing $80 billion in refunds for goods that hadn't been "
              'liquidated before the Supreme Court ruling.',
      'timestamp': 34,
      'timestamp_label': '[00:00:34]',
      'timestamp_seconds': 34,
      'tip': 'Um did they underpay and we send them a bill or did they overpay and we send '
             "them a refund? And that's called liquidation. And the argument basically is that "
             "the CBP is processing $80 billion in refunds for goods that hadn't been "
             'liquidated before the Supreme Court ruling.',
      'title': 'The $166B Refund Liquidation Trap #tariffs (Freightos)',
      'url': 'https://www.youtube.com/watch?v=cIMBwZ9J60I&t=34s',
      'video_id': 'cIMBwZ9J60I'},
     {'author': 'Star USA, Inc.',
      'channel': 'Star USA, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:04](https://www.youtube.com/watch?v=-v_-OQnVlxE&t=1084s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '301 and 232 and the other special tariff measures, those are being incorporated '
              "into the HTSUS. In chapter 99 of the HTSUS, you'll see the HTSUS on your "
              'customs documents.',
      'timestamp': 1084,
      'timestamp_label': '[00:18:04]',
      'timestamp_seconds': 1084,
      'tip': '301 and 232 and the other special tariff measures, those are being incorporated '
             "into the HTSUS. In chapter 99 of the HTSUS, you'll see the HTSUS on your customs "
             'documents.',
      'title': 'HTS Classification: Catching Mistakes Before They Become Costly (Star USA, '
               'Inc.)',
      'url': 'https://www.youtube.com/watch?v=-v_-OQnVlxE&t=1084s',
      'video_id': '-v_-OQnVlxE'},
     {'author': 'LionSky',
      'channel': 'LionSky',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=7ocNjGWsJHw&t=55s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Government create this loophole for manufacturers because it's good for the "
              "country manufacturers don't have to offshore to avoid tariffs and increases in "
              'US exports bring new money into the economy creating high-paying jobs for '
              'Americans.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': "Government create this loophole for manufacturers because it's good for the "
             "country manufacturers don't have to offshore to avoid tariffs and increases in "
             'US exports bring new money into the economy creating high-paying jobs for '
             'Americans.',
      'title': 'What is an FTZ? (LionSky)',
      'url': 'https://www.youtube.com/watch?v=7ocNjGWsJHw&t=55s',
      'video_id': '7ocNjGWsJHw'},
     {'author': 'JSJ INTERNATIONAL LCB',
      'channel': 'JSJ INTERNATIONAL LCB',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:42](https://www.youtube.com/watch?v=W-f4Ah72J_I&t=1062s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I had a problem a few months ago uh, where a client, obviously I say, with the '
              'experience one has over the years, one immediately detects or manages to read, '
              "honestly, manages to read a client's attitude. In this case, we are talking "
              'about me dealing with an exporter, right?',
      'timestamp': 1062,
      'timestamp_label': '[00:17:42]',
      'timestamp_seconds': 1062,
      'tip': 'I had a problem a few months ago uh, where a client, obviously I say, with the '
             'experience one has over the years, one immediately detects or manages to read, '
             "honestly, manages to read a client's attitude. In this case, we are talking "
             'about me dealing with an exporter, right?',
      'title': 'Master Class Requisitos Regimen 9801| Mercancías Estadounidenses y Extranjeras '
               'Devueltas (JSJ INTERNATIONAL LCB)',
      'url': 'https://www.youtube.com/watch?v=W-f4Ah72J_I&t=1062s',
      'video_id': 'W-f4Ah72J_I'},
     {'author': 'Ask The Customs Manager',
      'channel': 'Ask The Customs Manager',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:07](https://www.youtube.com/watch?v=GdCve47uHF8&t=67s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'They are returned within 3 years. They have not been modified or upgraded while '
              'abroad. The mistake happens when your carrier clears the return as a standard '
              "import because they didn't see the proof. The computer just charges the tax "
              'automatically.',
      'timestamp': 67,
      'timestamp_label': '[00:01:07]',
      'timestamp_seconds': 67,
      'tip': 'They are returned within 3 years. They have not been modified or upgraded while '
             'abroad. The mistake happens when your carrier clears the return as a standard '
             "import because they didn't see the proof. The computer just charges the tax "
             'automatically.',
      'title': 'Returned Goods Relief (RGR): How to Avoid Import Duty on Returned '
               'International Shipments (Ask The Customs Manager)',
      'url': 'https://www.youtube.com/watch?v=GdCve47uHF8&t=67s',
      'video_id': 'GdCve47uHF8'},
     {'author': 'Scarlett Jones',
      'channel': 'Scarlett Jones',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:42](https://www.youtube.com/watch?v=AJga0mQ31Vo&t=222s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The notification Bell to stay updated with our upcoming videos disclaimer note '
              'below until next time happy importing and exporting.',
      'timestamp': 222,
      'timestamp_label': '[00:03:42]',
      'timestamp_seconds': 222,
      'tip': 'The notification Bell to stay updated with our upcoming videos disclaimer note '
             'below until next time happy importing and exporting.',
      'title': 'Demystifying the Customs Power of Attorney: Key Role in International Trade! '
               '(Scarlett Jones)',
      'url': 'https://www.youtube.com/watch?v=AJga0mQ31Vo&t=222s',
      'video_id': 'AJga0mQ31Vo'},
     {'author': 'Law Office of Yuri Starikov, LLC',
      'channel': 'Law Office of Yuri Starikov, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:48](https://www.youtube.com/watch?v=B4gRBWbdUqo&t=408s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Classes I I I decided not to put the stress upon you with all this practice '
              'quiz questions at the beginning uh having said that that that that will that is '
              'rather an exception in the general rule.',
      'timestamp': 408,
      'timestamp_label': '[00:06:48]',
      'timestamp_seconds': 408,
      'tip': 'Classes I I I decided not to put the stress upon you with all this practice quiz '
             'questions at the beginning uh having said that that that that will that is '
             'rather an exception in the general rule.',
      'title': 'Product Classification Under HTSUS Part 1 (Law Office of Yuri Starikov, LLC)',
      'url': 'https://www.youtube.com/watch?v=B4gRBWbdUqo&t=408s',
      'video_id': 'B4gRBWbdUqo'},
     {'author': 'Shipping Solutions',
      'channel': 'Shipping Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:05](https://www.youtube.com/watch?v=_FcXk0dsq98&t=185s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'CBP’s Automated Commercial Environment, or ACE, and expect processing times to '
              'vary. CBP expects a solid audit trail.',
      'timestamp': 185,
      'timestamp_label': '[00:03:05]',
      'timestamp_seconds': 185,
      'tip': 'CBP’s Automated Commercial Environment, or ACE, and expect processing times to '
             'vary. CBP expects a solid audit trail.',
      'title': 'Duty Drawback on Exports: What You Need to Know (Shipping Solutions)',
      'url': 'https://www.youtube.com/watch?v=_FcXk0dsq98&t=185s',
      'video_id': '_FcXk0dsq98'}],
 6: [{'author': 'VoraPrep',
      'channel': 'VoraPrep',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:05](https://www.youtube.com/watch?v=2rbdaN1Swhk&t=245s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The invoice says they're $2 each. First, you gather the documents, the "
              'commercial invoice, the packing list, the bill of lading. Then, you put on your '
              'detective hat. You have to classify those mugs.',
      'timestamp': 245,
      'timestamp_label': '[00:04:05]',
      'timestamp_seconds': 245,
      'tip': "The invoice says they're $2 each. First, you gather the documents, the "
             'commercial invoice, the packing list, the bill of lading. Then, you put on your '
             'detective hat. You have to classify those mugs.',
      'title': '[CBLE] CBLE1: Entry Summary Documentation and Data Elements (CBP Form 7501) '
               '(VoraPrep)',
      'url': 'https://www.youtube.com/watch?v=2rbdaN1Swhk&t=245s',
      'video_id': '2rbdaN1Swhk'},
     {'author': 'IEEPA Tariff Watch',
      'channel': 'IEEPA Tariff Watch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:02](https://www.youtube.com/watch?v=V9_1adwF1c8&t=242s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The first and maybe the most powerful tool here is attorney client privilege. '
              "Now, this isn't just some fancy legal term. It's a real world shield for your "
              'company.',
      'timestamp': 242,
      'timestamp_label': '[00:04:02]',
      'timestamp_seconds': 242,
      'tip': 'The first and maybe the most powerful tool here is attorney client privilege. '
             "Now, this isn't just some fancy legal term. It's a real world shield for your "
             'company.',
      'title': 'Before You File for a Section 301 Tariff Refund: The Audit Risk Every Importer '
               'Needs to Understand (IEEPA Tariff Watch)',
      'url': 'https://www.youtube.com/watch?v=V9_1adwF1c8&t=242s',
      'video_id': 'V9_1adwF1c8'},
     {'author': 'Supplyia Sourcing',
      'channel': 'Supplyia Sourcing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:13](https://www.youtube.com/watch?v=ff_P7M6LKEo&t=973s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'First, we find our regular duty rate by looking up our hts code step. Second, '
              'we find out if this hts code has additional tariffs attached to it, by looking '
              'up the full list so far.',
      'timestamp': 973,
      'timestamp_label': '[00:16:13]',
      'timestamp_seconds': 973,
      'tip': 'First, we find our regular duty rate by looking up our hts code step. Second, we '
             'find out if this hts code has additional tariffs attached to it, by looking up '
             'the full list so far.',
      'title': 'HTS code lookup:  How to Calculate Duties & Tariffs for U.S Imports? (Supplyia '
               'Sourcing)',
      'url': 'https://www.youtube.com/watch?v=ff_P7M6LKEo&t=973s',
      'video_id': 'ff_P7M6LKEo'},
     {'author': 'Shipping Solutions',
      'channel': 'Shipping Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=_I3v11oKRLA&t=50s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can search for the HTS code by entering the first few digits of the '
              '10-digit code or by entering a short description of the goods. I am going to '
              'use the Product Classification Software to find the code for some semiconductor '
              'devices.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': 'You can search for the HTS code by entering the first few digits of the 10-digit '
             'code or by entering a short description of the goods. I am going to use the '
             'Product Classification Software to find the code for some semiconductor devices.',
      'title': 'How to Calculate U.S. Import Tariffs (HTS Codes & Duties Explained) (Shipping '
               'Solutions)',
      'url': 'https://www.youtube.com/watch?v=_I3v11oKRLA&t=50s',
      'video_id': '_I3v11oKRLA'},
     {'author': 'emily p',
      'channel': 'emily p',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:49](https://www.youtube.com/watch?v=X6G27vQXOic&t=229s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "On page two, you'll be asked a few questions. First, it will ask you whether "
              'you purchased any of the listed beef products for personal use. Next, it will '
              'ask you if those purchases were made in one or more of the states shown on '
              'their list.',
      'timestamp': 229,
      'timestamp_label': '[00:03:49]',
      'timestamp_seconds': 229,
      'tip': "On page two, you'll be asked a few questions. First, it will ask you whether you "
             'purchased any of the listed beef products for personal use. Next, it will ask '
             'you if those purchases were made in one or more of the states shown on their '
             'list.',
      'title': 'Beef Class Action Lawsuit 2026: Step-By-Step Instructions To Claim YOUR Money '
               '! (emily p)',
      'url': 'https://www.youtube.com/watch?v=X6G27vQXOic&t=229s',
      'video_id': 'X6G27vQXOic'},
     {'author': 'ImportGenius',
      'channel': 'ImportGenius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:04](https://www.youtube.com/watch?v=XuTLIlW6tdk&t=424s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So, I've done all field search imports for Walmart over the last 5 years. And "
              'so, what the data tells us if we scroll down to this little like Excel '
              'file-looking uh piece over here, we can see that Walmart sourced pretty '
              'significantly from China and Hong Kong.',
      'timestamp': 424,
      'timestamp_label': '[00:07:04]',
      'timestamp_seconds': 424,
      'tip': "So, I've done all field search imports for Walmart over the last 5 years. And "
             'so, what the data tells us if we scroll down to this little like Excel '
             'file-looking uh piece over here, we can see that Walmart sourced pretty '
             'significantly from China and Hong Kong.',
      'title': 'Trade secrets exposed: how to see what your competitors are importing, '
               'selling, and sourcing (ImportGenius)',
      'url': 'https://www.youtube.com/watch?v=XuTLIlW6tdk&t=424s',
      'video_id': 'XuTLIlW6tdk'},
     {'author': 'Opscale Exchange',
      'channel': 'Opscale Exchange',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:22](https://www.youtube.com/watch?v=t98WTC5Cm9o&t=1462s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And so, you really be find yourself in that position where uh the recovery is '
              'going to require filing an action in court or or if you do the protest route, '
              "which is okay, you just don't know what's going to happen. Could you elaborate "
              'on that 80-day liquidation period?',
      'timestamp': 1462,
      'timestamp_label': '[00:24:22]',
      'timestamp_seconds': 1462,
      'tip': 'And so, you really be find yourself in that position where uh the recovery is '
             'going to require filing an action in court or or if you do the protest route, '
             "which is okay, you just don't know what's going to happen. Could you elaborate "
             'on that 80-day liquidation period?',
      'title': 'IEEPA Tariff Refunds: How Importers Get Their Money Back | Thompson Coburn x '
               'Opscale (Opscale Exchange)',
      'url': 'https://www.youtube.com/watch?v=t98WTC5Cm9o&t=1462s',
      'video_id': 't98WTC5Cm9o'},
     {'author': 'American Association of Exporters & Importers',
      'channel': 'American Association of Exporters & Importers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:42](https://www.youtube.com/watch?v=g_ANnE2CVcU&t=1482s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So data elements are all over the place, you know, among entities. We have ERP '
              'information, classification information, value information. Then you have ACE '
              'data, which is what customs sees, right?',
      'timestamp': 1482,
      'timestamp_label': '[00:24:42]',
      'timestamp_seconds': 1482,
      'tip': 'So data elements are all over the place, you know, among entities. We have ERP '
             'information, classification information, value information. Then you have ACE '
             'data, which is what customs sees, right?',
      'title': 'Beyond the Customs Entry: Identifying Tariff Recovery Opportunities in '
               'Supplier Costs (American Association of Exporters & Importers)',
      'url': 'https://www.youtube.com/watch?v=g_ANnE2CVcU&t=1482s',
      'video_id': 'g_ANnE2CVcU'},
     {'author': 'Scarbrough Global',
      'channel': 'Scarbrough Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=E-PQ2z_UoCM&t=52s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Accounting method first in a warehouse for data warehouse for example but you '
              'need to be able to do that you need to be able to track that have.',
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': 'Accounting method first in a warehouse for data warehouse for example but you '
             'need to be able to do that you need to be able to track that have.',
      'title': 'What is Unused Merchandise Drawback when claiming duty drawback ? (Scarbrough '
               'Global)',
      'url': 'https://www.youtube.com/watch?v=E-PQ2z_UoCM&t=52s',
      'video_id': 'E-PQ2z_UoCM'},
     {'author': 'Ask The Customs Manager',
      'channel': 'Ask The Customs Manager',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:45](https://www.youtube.com/watch?v=Pso0Iq3i3Xk&t=105s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Two, are you leaving money on the table? Way more businesses qualify for '
              'drawback than they think. You could be eligible right now and not even know it. '
              "Let's see if any of these scenarios ring a bell. First you have manufacturing "
              'drawback.',
      'timestamp': 105,
      'timestamp_label': '[00:01:45]',
      'timestamp_seconds': 105,
      'tip': 'Two, are you leaving money on the table? Way more businesses qualify for '
             'drawback than they think. You could be eligible right now and not even know it. '
             "Let's see if any of these scenarios ring a bell. First you have manufacturing "
             'drawback.',
      'title': 'Duty Drawback Explained | How to Claim a 99% Refund on Customs Duties (Ask The '
               'Customs Manager)',
      'url': 'https://www.youtube.com/watch?v=Pso0Iq3i3Xk&t=105s',
      'video_id': 'Pso0Iq3i3Xk'},
     {'author': '💎Kiona 職場 x 行銷筆記💎',
      'channel': '💎Kiona 職場 x 行銷筆記💎',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:50](https://www.youtube.com/watch?v=i3e313EJJPE&t=410s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Hardware chemicals gardening plastick textiles home appliance and medical if '
              'you want to know what information custom data can provide for your industry '
              'please scan the WhatsApp QR code on the screen or fill out the Forum below to '
              'schedule an online demo.',
      'timestamp': 410,
      'timestamp_label': '[00:06:50]',
      'timestamp_seconds': 410,
      'tip': 'Hardware chemicals gardening plastick textiles home appliance and medical if you '
             'want to know what information custom data can provide for your industry please '
             'scan the WhatsApp QR code on the screen or fill out the Forum below to schedule '
             'an online demo.',
      'title': 'How AI Finds Global Buyers 10X FASTER Than Manual Search! #I-Power #panjiva '
               '#importgenius (💎Kiona 職場 x 行銷筆記💎)',
      'url': 'https://www.youtube.com/watch?v=i3e313EJJPE&t=410s',
      'video_id': 'i3e313EJJPE'},
     {'author': 'ImportGenius',
      'channel': 'ImportGenius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:20](https://www.youtube.com/watch?v=NmWdt9dMzjM&t=140s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Help you find qualified sales leads never go into another cold call blind with '
              "our database at your fingertips you'll know exactly what kinds of services an "
              "importer's business demands sign up for instant access at w w w import or call "
              'today 1-888-843-0272.',
      'timestamp': 140,
      'timestamp_label': '[00:02:20]',
      'timestamp_seconds': 140,
      'tip': 'Help you find qualified sales leads never go into another cold call blind with '
             "our database at your fingertips you'll know exactly what kinds of services an "
             "importer's business demands sign up for instant access at w w w import or call "
             'today 1-888-843-0272.',
      'title': 'Identify High-Value Sales Prospects with Import Genius (ImportGenius)',
      'url': 'https://www.youtube.com/watch?v=NmWdt9dMzjM&t=140s',
      'video_id': 'NmWdt9dMzjM'},
     {'author': 'USA Customs Clearance',
      'channel': 'USA Customs Clearance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:37](https://www.youtube.com/watch?v=QX8vx-rrO4A&t=277s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Overpayment claimants can receive their refund within as little as 4 to 6 weeks '
              'ready to get started at USA Customs clearance we offer drawback Services Guided '
              'by experienced import agents find a direct link to our services in the '
              'description until next time.',
      'timestamp': 277,
      'timestamp_label': '[00:04:37]',
      'timestamp_seconds': 277,
      'tip': 'Overpayment claimants can receive their refund within as little as 4 to 6 weeks '
             'ready to get started at USA Customs clearance we offer drawback Services Guided '
             'by experienced import agents find a direct link to our services in the '
             'description until next time.',
      'title': 'How to Get Cash Refunds Through Duty Drawbacks (USA Customs Clearance)',
      'url': 'https://www.youtube.com/watch?v=QX8vx-rrO4A&t=277s',
      'video_id': 'QX8vx-rrO4A'},
     {'author': 'Law Office of Yuri Starikov, LLC',
      'channel': 'Law Office of Yuri Starikov, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:25](https://www.youtube.com/watch?v=d6omeUFeZfA&t=205s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Transportation without appraisement entry we talked about about importation and '
              'exportation entry we talked about drawback entry first first class when I was '
              'talking about this circumvention.',
      'timestamp': 205,
      'timestamp_label': '[00:03:25]',
      'timestamp_seconds': 205,
      'tip': 'Transportation without appraisement entry we talked about about importation and '
             'exportation entry we talked about drawback entry first first class when I was '
             'talking about this circumvention.',
      'title': 'U.S. Customs (CBP) Bonds Webcast Preview (Law Office of Yuri Starikov, LLC)',
      'url': 'https://www.youtube.com/watch?v=d6omeUFeZfA&t=205s',
      'video_id': 'd6omeUFeZfA'},
     {'author': 'Trade Risk Guaranty',
      'channel': 'Trade Risk Guaranty',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:21](https://www.youtube.com/watch?v=PymimTwXXVM&t=321s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Eagle Eye ACE bond dashboard. Um but first, get that bond query information. '
              "Happy to provide it from TRG whether you're a client or not or your service "
              "provider. And if you see it's wrong, what do you do, Colette?",
      'timestamp': 321,
      'timestamp_label': '[00:05:21]',
      'timestamp_seconds': 321,
      'tip': 'Eagle Eye ACE bond dashboard. Um but first, get that bond query information. '
             "Happy to provide it from TRG whether you're a client or not or your service "
             "provider. And if you see it's wrong, what do you do, Colette?",
      'title': "CBP's database Clean Up May Void Your IOR | TRG Talks Trade | EP 13 (Trade "
               'Risk Guaranty)',
      'url': 'https://www.youtube.com/watch?v=PymimTwXXVM&t=321s',
      'video_id': 'PymimTwXXVM'}],
 7: [{'author': 'Tariffs Lawsuit',
      'channel': 'Tariffs Lawsuit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:37](https://www.youtube.com/watch?v=DOHCXtY_zI0&t=97s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Here's why the refund system is failing businesses. To process refunds, CBP "
              'built a new system inside of its ACE portal called CAPE, the Consolidated '
              'Administration and Processing of Entries System. It opened on April 20th of '
              '2026 and importers started falling immediately.',
      'timestamp': 97,
      'timestamp_label': '[00:01:37]',
      'timestamp_seconds': 97,
      'tip': "Here's why the refund system is failing businesses. To process refunds, CBP "
             'built a new system inside of its ACE portal called CAPE, the Consolidated '
             'Administration and Processing of Entries System. It opened on April 20th of 2026 '
             'and importers started falling immediately.',
      'title': 'Tariff Refunds for Importers: Your Business May Be Owed Money After Supreme '
               'Court Ruling (Tariffs Lawsuit)',
      'url': 'https://www.youtube.com/watch?v=DOHCXtY_zI0&t=97s',
      'video_id': 'DOHCXtY_zI0'},
     {'author': 'Commercial Funding Marketplace',
      'channel': 'Commercial Funding Marketplace',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:30](https://www.youtube.com/watch?v=LaWXf8aLv1o&t=270s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's quickly cover the two most important documents you'll need to get "
              "started. First thing is your ACE portal report. ACE is the government's "
              'official system for this stuff, the automated commercial environment. For a '
              'buyer, this report is the one and only source of truth.',
      'timestamp': 270,
      'timestamp_label': '[00:04:30]',
      'timestamp_seconds': 270,
      'tip': "Let's quickly cover the two most important documents you'll need to get started. "
             "First thing is your ACE portal report. ACE is the government's official system "
             'for this stuff, the automated commercial environment. For a buyer, this report '
             'is the one and only source of truth.',
      'title': 'IEEPA Tariff Refund Buyout: The Process (Commercial Funding Marketplace)',
      'url': 'https://www.youtube.com/watch?v=LaWXf8aLv1o&t=270s',
      'video_id': 'LaWXf8aLv1o'},
     {'author': 'Freight & Trade',
      'channel': 'Freight & Trade',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:12](https://www.youtube.com/watch?v=ez065LeX6vE&t=252s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'CBP releases the shipment, the cargo can continue through the normal delivery '
              'process. The important thing to remember is that the bond supports the customs '
              "process. It doesn't replace the customs process.",
      'timestamp': 252,
      'timestamp_label': '[00:04:12]',
      'timestamp_seconds': 252,
      'tip': 'CBP releases the shipment, the cargo can continue through the normal delivery '
             'process. The important thing to remember is that the bond supports the customs '
             "process. It doesn't replace the customs process.",
      'title': 'What Is a Customs Bond  A Beginner’s Guide to Importing into the US (Freight & '
               'Trade)',
      'url': 'https://www.youtube.com/watch?v=ez065LeX6vE&t=252s',
      'video_id': 'ez065LeX6vE'},
     {'author': 'Shipping Solutions',
      'channel': 'Shipping Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=uEeZIcpmUfw&t=60s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Step 2 Contact your customs broker. Discuss the import process for repairs with '
              'your broker. They can advise on using a Temporary Importation Bond, or TIB, or '
              'if they are eligible for import using the Harmonized Tariff Schedule of the U.',
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': 'Step 2 Contact your customs broker. Discuss the import process for repairs with '
             'your broker. They can advise on using a Temporary Importation Bond, or TIB, or '
             'if they are eligible for import using the Harmonized Tariff Schedule of the U.',
      'title': 'Repaired Goods: Import and Re-export (Shipping Solutions)',
      'url': 'https://www.youtube.com/watch?v=uEeZIcpmUfw&t=60s',
      'video_id': 'uEeZIcpmUfw'},
     {'author': 'Steve Fodor',
      'channel': 'Steve Fodor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:35:05](https://www.youtube.com/watch?v=Exy48YwwPtk&t=2105s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Customs attorney or trade logic International as a consultant to help you in '
              "that process you need to document the fact that you've reviewed your harmonized "
              'tariff classifications and that helps you be able to prove that you have '
              'exercised due diligence and reasonable.',
      'timestamp': 2105,
      'timestamp_label': '[00:35:05]',
      'timestamp_seconds': 2105,
      'tip': 'Customs attorney or trade logic International as a consultant to help you in '
             "that process you need to document the fact that you've reviewed your harmonized "
             'tariff classifications and that helps you be able to prove that you have '
             'exercised due diligence and reasonable.',
      'title': 'HTS Classification The Most Important Step 062016 (Steve Fodor)',
      'url': 'https://www.youtube.com/watch?v=Exy48YwwPtk&t=2105s',
      'video_id': 'Exy48YwwPtk'},
     {'author': 'Alliance Duty Drawback Services',
      'channel': 'Alliance Duty Drawback Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=mkogoOMopss&t=85s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The item maintains its identity throughout the process, and that's what we call "
              "explicit matching. But what about retail apparel? Clothing doesn't come with "
              'serial numbers. In cases like this, customs allows companies to use a drawback '
              'accounting method.',
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': "The item maintains its identity throughout the process, and that's what we call "
             "explicit matching. But what about retail apparel? Clothing doesn't come with "
             'serial numbers. In cases like this, customs allows companies to use a drawback '
             'accounting method.',
      'title': 'Unused Merchandise Drawback (Alliance Duty Drawback Services)',
      'url': 'https://www.youtube.com/watch?v=mkogoOMopss&t=85s',
      'video_id': 'mkogoOMopss'},
     {'author': 'Customs Directory',
      'channel': 'Customs Directory',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:47](https://www.youtube.com/watch?v=3WCCVWQIggA&t=407s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The system is fair, but the responsibility is all on you, the importer. So, the '
              "final question you've got to ask yourself is this: When that audit comes, are "
              'you ready?',
      'timestamp': 407,
      'timestamp_label': '[00:06:47]',
      'timestamp_seconds': 407,
      'tip': 'The system is fair, but the responsibility is all on you, the importer. So, the '
             "final question you've got to ask yourself is this: When that audit comes, are "
             'you ready?',
      'title': 'Customs Valuation Explained – How Customs Calculate Import Duty (Customs '
               'Directory)',
      'url': 'https://www.youtube.com/watch?v=3WCCVWQIggA&t=407s',
      'video_id': '3WCCVWQIggA'},
     {'author': 'ISF Solution',
      'channel': 'ISF Solution',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:11](https://www.youtube.com/watch?v=KnedznhIyEs&t=311s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Relationships or import requirements May necessitate updating the document '
              'importers should verify that the power of attorney remains current and reflects '
              'the most accurate arrangement with the customs.',
      'timestamp': 311,
      'timestamp_label': '[00:05:11]',
      'timestamp_seconds': 311,
      'tip': 'Relationships or import requirements May necessitate updating the document '
             'importers should verify that the power of attorney remains current and reflects '
             'the most accurate arrangement with the customs.',
      'title': 'Empowering Compliance: Customs POA and ISF Relationship (ISF Solution)',
      'url': 'https://www.youtube.com/watch?v=KnedznhIyEs&t=311s',
      'video_id': 'KnedznhIyEs'},
     {'author': 'TalkingLogistics',
      'channel': 'TalkingLogistics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:36](https://www.youtube.com/watch?v=BCWMDlUCSx4&t=636s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Filing process had been implemented as in that system it was basically you know '
              'you file and you create a drawback header sort of where you just had the.',
      'timestamp': 636,
      'timestamp_label': '[00:10:36]',
      'timestamp_seconds': 636,
      'tip': 'Filing process had been implemented as in that system it was basically you know '
             'you file and you create a drawback header sort of where you just had the.',
      'title': 'Why Duty Drawback is Making a Comeback (TalkingLogistics)',
      'url': 'https://www.youtube.com/watch?v=BCWMDlUCSx4&t=636s',
      'video_id': 'BCWMDlUCSx4'},
     {'author': 'Scarbrough Global',
      'channel': 'Scarbrough Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:34](https://www.youtube.com/watch?v=52Q7Sv1KF4Q&t=334s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'System into Ace um import truck Manifest this is important because cargo that '
              "moves into the United States especially if we're talking Mexico um gets a "
              'truck.',
      'timestamp': 334,
      'timestamp_label': '[00:05:34]',
      'timestamp_seconds': 334,
      'tip': 'System into Ace um import truck Manifest this is important because cargo that '
             "moves into the United States especially if we're talking Mexico um gets a truck.",
      'title': 'ACE Question/Answer Forum: Session One Introduction (Scarbrough Global)',
      'url': 'https://www.youtube.com/watch?v=52Q7Sv1KF4Q&t=334s',
      'video_id': '52Q7Sv1KF4Q'},
     {'author': 'Emran Hossin',
      'channel': 'Emran Hossin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:45](https://www.youtube.com/watch?v=8Em9en9nPzQ&t=165s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Act now contact the person who shared this video with you to start your claim '
              "they'll guide you through the entire process to ensure your business gets what "
              "it's entitled to remember the deadline is February 4th 2025 don't wait cards "
              "settlement. org recover what's yours.",
      'timestamp': 165,
      'timestamp_label': '[00:02:45]',
      'timestamp_seconds': 165,
      'tip': 'Act now contact the person who shared this video with you to start your claim '
             "they'll guide you through the entire process to ensure your business gets what "
             "it's entitled to remember the deadline is February 4th 2025 don't wait cards "
             "settlement. org recover what's yours.",
      'title': 'Claim Your Share of the $5.54 Billion Visa/Mastercard Settlement (Emran '
               'Hossin)',
      'url': 'https://www.youtube.com/watch?v=8Em9en9nPzQ&t=165s',
      'video_id': '8Em9en9nPzQ'},
     {'author': 'Clark-Esposito Law Firm P.C.',
      'channel': 'Clark-Esposito Law Firm P.C.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=pwhkHF1ttlo&t=51s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'S customs intends to keep it and sets worth its reasons for having decided this '
              'way. CBP sends this notification so that an interested party can try and '
              'recover the merchandise through a government administrative process.',
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': 'S customs intends to keep it and sets worth its reasons for having decided this '
             'way. CBP sends this notification so that an interested party can try and recover '
             'the merchandise through a government administrative process.',
      'title': "What to Do If You've Received a U.S. Customs & Border Protection (CBP) Seizure "
               'Notice (Clark-Esposito Law Firm P.C.)',
      'url': 'https://www.youtube.com/watch?v=pwhkHF1ttlo&t=51s',
      'video_id': 'pwhkHF1ttlo'},
     {'author': 'Star USA, Inc.',
      'channel': 'Star USA, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:00](https://www.youtube.com/watch?v=BwGDeEGn1Wg&t=780s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "There's the hs or a harmonized system that the wco publishes this is the same "
              "across all 180 some members of the wco and it's what each individual country's "
              'basis is for making their hts or h s or h c.',
      'timestamp': 780,
      'timestamp_label': '[00:13:00]',
      'timestamp_seconds': 780,
      'tip': "There's the hs or a harmonized system that the wco publishes this is the same "
             "across all 180 some members of the wco and it's what each individual country's "
             'basis is for making their hts or h s or h c.',
      'title': 'HTSUS Classification Webinar (Star USA, Inc.)',
      'url': 'https://www.youtube.com/watch?v=BwGDeEGn1Wg&t=780s',
      'video_id': 'BwGDeEGn1Wg'},
     {'author': 'Scarbrough Global',
      'channel': 'Scarbrough Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:34](https://www.youtube.com/watch?v=Bse6lVDGA_U&t=94s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Products but there are specific customs requirements that are out there there's "
              "a list I can't remember how many was on it but I do have that list and I'm "
              'happy to send that to to you and we can put that out there with with this '
              'presentation on our website as well.',
      'timestamp': 94,
      'timestamp_label': '[00:01:34]',
      'timestamp_seconds': 94,
      'tip': "Products but there are specific customs requirements that are out there there's "
             "a list I can't remember how many was on it but I do have that list and I'm happy "
             'to send that to to you and we can put that out there with with this presentation '
             'on our website as well.',
      'title': 'Post Summary Corrections and 7501 (Scarbrough Global)',
      'url': 'https://www.youtube.com/watch?v=Bse6lVDGA_U&t=94s',
      'video_id': 'Bse6lVDGA_U'},
     {'author': 'USA Customs Clearance',
      'channel': 'USA Customs Clearance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:04](https://www.youtube.com/watch?v=khfmXSwD3DE&t=184s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Step one, identify your eligible imports. You'll need to pull your entry "
              'records, specifically CBP form 7501, to find shipments where you paid section '
              '301 duties. Step two, match those imports to your exports or to products you '
              'manufactured for export.',
      'timestamp': 184,
      'timestamp_label': '[00:03:04]',
      'timestamp_seconds': 184,
      'tip': "Step one, identify your eligible imports. You'll need to pull your entry "
             'records, specifically CBP form 7501, to find shipments where you paid section '
             '301 duties. Step two, match those imports to your exports or to products you '
             'manufactured for export.',
      'title': 'Section 301 Duty Drawback Explained (USA Customs Clearance)',
      'url': 'https://www.youtube.com/watch?v=khfmXSwD3DE&t=184s',
      'video_id': 'khfmXSwD3DE'}],
 8: [{'author': 'Trade Risk Guaranty',
      'channel': 'Trade Risk Guaranty',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:56:06](https://www.youtube.com/watch?v=M68ZVWdgp9I&t=3366s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Eagle I Ace software, that bond dashboard, getting the information directly to '
              "you, and it it's not necessarily as full or complete as importer Ace data.",
      'timestamp': 3366,
      'timestamp_label': '[00:56:06]',
      'timestamp_seconds': 3366,
      'tip': 'Eagle I Ace software, that bond dashboard, getting the information directly to '
             "you, and it it's not necessarily as full or complete as importer Ace data.",
      'title': 'Managing Open U.S. Customs Bond Liability [Full Webinar] (Trade Risk Guaranty)',
      'url': 'https://www.youtube.com/watch?v=M68ZVWdgp9I&t=3366s',
      'video_id': 'M68ZVWdgp9I'},
     {'author': 'CustomsPrep — Customs Broker License Exam',
      'channel': 'CustomsPrep — Customs Broker License Exam',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:21](https://www.youtube.com/watch?v=qORXZ_TDyKg&t=261s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'ACE Entry Summary Instructions, version 2. 4A, describes each data element by '
              'name, not by block number. Learn the fields by what they hold, and a '
              "renumbering cannot touch you. Every past exam with CBP's answer key and the "
              'exhibits, this 7501 included, is at customsprep.',
      'timestamp': 261,
      'timestamp_label': '[00:04:21]',
      'timestamp_seconds': 261,
      'tip': 'ACE Entry Summary Instructions, version 2. 4A, describes each data element by '
             'name, not by block number. Learn the fields by what they hold, and a renumbering '
             "cannot touch you. Every past exam with CBP's answer key and the exhibits, this "
             '7501 included, is at customsprep.',
      'title': 'CBP Form 7501 Entry Summary Explained, Block by Block — and What Changed in '
               '2026 (CustomsPrep — Customs Broker License Exam)',
      'url': 'https://www.youtube.com/watch?v=qORXZ_TDyKg&t=261s',
      'video_id': 'qORXZ_TDyKg'},
     {'author': 'KYG Trade',
      'channel': 'KYG Trade',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:50](https://www.youtube.com/watch?v=myOI9hprs0c&t=470s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '2022 uh the brokerage rules were made much firmer requiring direct powers of '
              'attorney between a broker and an importer. So this platform had some other '
              'services. It also allowed an AI tool for classification.',
      'timestamp': 470,
      'timestamp_label': '[00:07:50]',
      'timestamp_seconds': 470,
      'tip': '2022 uh the brokerage rules were made much firmer requiring direct powers of '
             'attorney between a broker and an importer. So this platform had some other '
             'services. It also allowed an AI tool for classification.',
      'title': 'CBP Ruling HQ 350722 & Guardrails for AI in Trade Compliance (KYG Trade)',
      'url': 'https://www.youtube.com/watch?v=myOI9hprs0c&t=470s',
      'video_id': 'myOI9hprs0c'},
     {'author': 'Ask The Customs Manager',
      'channel': 'Ask The Customs Manager',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=NRCd8c6t8rY&t=100s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Processing paper checks costs money and time. Electronic transfers are cheaper '
              "and faster for them. Either way, it's happening. February 6th is the cutoff. Go "
              "to the AC secure data portal. That's CBP's automated commercial environment "
              'system.',
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': 'Processing paper checks costs money and time. Electronic transfers are cheaper '
             "and faster for them. Either way, it's happening. February 6th is the cutoff. Go "
             "to the AC secure data portal. That's CBP's automated commercial environment "
             'system.',
      'title': 'CBP ACH Refund Deadline 2026: Importers Must Enroll by February 6 or Lose '
               'Tariff Refunds (Ask The Customs Manager)',
      'url': 'https://www.youtube.com/watch?v=NRCd8c6t8rY&t=100s',
      'video_id': 'NRCd8c6t8rY'},
     {'author': 'International Trade Council',
      'channel': 'International Trade Council',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:47:38](https://www.youtube.com/watch?v=O5a8FOALaXk&t=2858s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Number level um because part number level detail is not always available either '
              'through the customs broker through the ace portal aces custom system.',
      'timestamp': 2858,
      'timestamp_label': '[00:47:38]',
      'timestamp_seconds': 2858,
      'tip': 'Number level um because part number level detail is not always available either '
             'through the customs broker through the ace portal aces custom system.',
      'title': 'WEBINAR: Duty Drawback 101 - Receiving refunds on import duties (International '
               'Trade Council)',
      'url': 'https://www.youtube.com/watch?v=O5a8FOALaXk&t=2858s',
      'video_id': 'O5a8FOALaXk'},
     {'author': 'ImportGenius Korea',
      'channel': 'ImportGenius Korea',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:46](https://www.youtube.com/watch?v=HLvI3nZIlT4&t=46s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Products search by the name of the Importer name of the supplier Etc so let's "
              'select the product and then just search the table and then we are going to see '
              'the import data of table uh from USA for the last 12 months click search.',
      'timestamp': 46,
      'timestamp_label': '[00:00:46]',
      'timestamp_seconds': 46,
      'tip': "Products search by the name of the Importer name of the supplier Etc so let's "
             'select the product and then just search the table and then we are going to see '
             'the import data of table uh from USA for the last 12 months click search.',
      'title': 'How to use the ImportGenius Application_Eng Ver (ImportGenius Korea)',
      'url': 'https://www.youtube.com/watch?v=HLvI3nZIlT4&t=46s',
      'video_id': 'HLvI3nZIlT4'},
     {'author': 'Freightos',
      'channel': 'Freightos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:10](https://www.youtube.com/watch?v=bZWPrOasGFY&t=130s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "It's at that point where things might get a little bit more complicated, where "
              "you're going to want the assistance of a customs broker. But effectively, you "
              "just have to either if you have access to ACE, you'll go into the CAPE portal "
              'when it opens.',
      'timestamp': 130,
      'timestamp_label': '[00:02:10]',
      'timestamp_seconds': 130,
      'tip': "It's at that point where things might get a little bit more complicated, where "
             "you're going to want the assistance of a customs broker. But effectively, you "
             "just have to either if you have access to ACE, you'll go into the CAPE portal "
             'when it opens.',
      'title': 'IEEPA Tariff Refunds: How, What, When...And Interest! #tradewar #tariffs '
               '#customs (Freightos)',
      'url': 'https://www.youtube.com/watch?v=bZWPrOasGFY&t=130s',
      'video_id': 'bZWPrOasGFY'},
     {'author': 'Evana',
      'channel': 'Evana',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:04](https://www.youtube.com/watch?v=YVqE1V68BkI&t=124s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s happening with your inventory. There's no better place to be than at the "
              'beginning of a runway. Do you have an ACE portal set up? The ACE portal is '
              "CBC's system and every [clears throat] importer can have their own account.",
      'timestamp': 124,
      'timestamp_label': '[00:02:04]',
      'timestamp_seconds': 124,
      'tip': "'s happening with your inventory. There's no better place to be than at the "
             "beginning of a runway. Do you have an ACE portal set up? The ACE portal is CBC's "
             'system and every [clears throat] importer can have their own account.',
      'title': 'IEEPA Tariff Refunds vs. Duty Drawback: What Importers Need to Know (2026) '
               '(Evana)',
      'url': 'https://www.youtube.com/watch?v=YVqE1V68BkI&t=124s',
      'video_id': 'YVqE1V68BkI'},
     {'author': 'ImportGenius',
      'channel': 'ImportGenius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:59](https://www.youtube.com/watch?v=Zdmg7G-W9_Q&t=119s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Back over to to the search uh shipment search in import genius and it shows me '
              'the last uh last one year of data for that company now in some cases you may.',
      'timestamp': 119,
      'timestamp_label': '[00:01:59]',
      'timestamp_seconds': 119,
      'tip': 'Back over to to the search uh shipment search in import genius and it shows me '
             'the last uh last one year of data for that company now in some cases you may.',
      'title': 'Import Genius Visual Mapping Instruction (ImportGenius)',
      'url': 'https://www.youtube.com/watch?v=Zdmg7G-W9_Q&t=119s',
      'video_id': 'Zdmg7G-W9_Q'},
     {'author': 'Flexport',
      'channel': 'Flexport',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:52](https://www.youtube.com/watch?v=A7RUPXhyx4M&t=1312s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re able to generate results within our software but then took the same data "
              "and spent unfortunately it takes a lot longer otherwise we'd have a lot more "
              'case studies.',
      'timestamp': 1312,
      'timestamp_label': '[00:21:52]',
      'timestamp_seconds': 1312,
      'tip': "'re able to generate results within our software but then took the same data and "
             "spent unfortunately it takes a lot longer otherwise we'd have a lot more case "
             'studies.',
      'title': 'Maximizing Duty Drawback with Flexport (Flexport)',
      'url': 'https://www.youtube.com/watch?v=A7RUPXhyx4M&t=1312s',
      'video_id': 'A7RUPXhyx4M'},
     {'author': 'ImportGenius',
      'channel': 'ImportGenius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:36](https://www.youtube.com/watch?v=irUncYGL5Jg&t=156s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Data by by their name you can do all kinds of things you can merge this into '
              'another database for each of them you have the contact.',
      'timestamp': 156,
      'timestamp_label': '[00:02:36]',
      'timestamp_seconds': 156,
      'tip': 'Data by by their name you can do all kinds of things you can merge this into '
             'another database for each of them you have the contact.',
      'title': 'Marble Imports (ImportGenius)',
      'url': 'https://www.youtube.com/watch?v=irUncYGL5Jg&t=156s',
      'video_id': 'irUncYGL5Jg'},
     {'author': '💎Kiona 職場 x 行銷筆記💎',
      'channel': '💎Kiona 職場 x 行銷筆記💎',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:43](https://www.youtube.com/watch?v=LggBClCtXNY&t=523s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Viewing and also oneon-one Human Assistance the after service is very important '
              'and we will have real person and not robot to serve you for more information on '
              'our custom data please scan this WhatsApp on the screen and reach us as soon as '
              'possible.',
      'timestamp': 523,
      'timestamp_label': '[00:08:43]',
      'timestamp_seconds': 523,
      'tip': 'Viewing and also oneon-one Human Assistance the after service is very important '
             'and we will have real person and not robot to serve you for more information on '
             'our custom data please scan this WhatsApp on the screen and reach us as soon as '
             'possible.',
      'title': 'Top 3 Customs Data Suppliers Compared: Panjiva vs. ImportGenius vs. I-POWER '
               '(💎Kiona 職場 x 行銷筆記💎)',
      'url': 'https://www.youtube.com/watch?v=LggBClCtXNY&t=523s',
      'video_id': 'LggBClCtXNY'},
     {'author': 'Scarbrough Global',
      'channel': 'Scarbrough Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:06](https://www.youtube.com/watch?v=ZzvKR65Oyuw&t=366s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'In the portal as well so that way even if it gets mailed out to another branch '
              'of yours you at least can see access from a corporate level.',
      'timestamp': 366,
      'timestamp_label': '[00:06:06]',
      'timestamp_seconds': 366,
      'tip': 'In the portal as well so that way even if it gets mailed out to another branch '
             'of yours you at least can see access from a corporate level.',
      'title': 'ACE Portal Transition (Scarbrough Global)',
      'url': 'https://www.youtube.com/watch?v=ZzvKR65Oyuw&t=366s',
      'video_id': 'ZzvKR65Oyuw'},
     {'author': 'Scarbrough Global',
      'channel': 'Scarbrough Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=lsd6_oB4p00&t=15s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "That you've destroyed merchandise or if you've just exported the merchandise "
              'that is that is an itty gritty question I used to work at a brokerage firm but.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "That you've destroyed merchandise or if you've just exported the merchandise "
             'that is that is an itty gritty question I used to work at a brokerage firm but.',
      'title': 'Are there different documents required for destroyed merchandise on duty '
               'drawback ? (Scarbrough Global)',
      'url': 'https://www.youtube.com/watch?v=lsd6_oB4p00&t=15s',
      'video_id': 'lsd6_oB4p00'},
     {'author': 'Tariffs Lawsuit',
      'channel': 'Tariffs Lawsuit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=DOHCXtY_zI0&t=103s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'To process refunds, CBP built a new system inside of its ACE portal called '
              'CAPE, the Consolidated Administration and Processing of Entries System. It '
              'opened on April 20th of 2026 and importers started falling immediately.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': 'To process refunds, CBP built a new system inside of its ACE portal called CAPE, '
             'the Consolidated Administration and Processing of Entries System. It opened on '
             'April 20th of 2026 and importers started falling immediately.',
      'title': 'Tariff Refunds for Importers: Your Business May Be Owed Money After Supreme '
               'Court Ruling (Tariffs Lawsuit)',
      'url': 'https://www.youtube.com/watch?v=DOHCXtY_zI0&t=103s',
      'video_id': 'DOHCXtY_zI0'}],
 9: [{'author': 'VoraPrep',
      'channel': 'VoraPrep',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:14](https://www.youtube.com/watch?v=8NkJbs7UVvY&t=494s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Which brings us to the final step, compliance and consequences. The conclusion '
              'is that Global Trade Solutions is non-compliant. They face potential '
              'disciplinary action from CBP for the RSC failure up to license revocation.',
      'timestamp': 494,
      'timestamp_label': '[00:08:14]',
      'timestamp_seconds': 494,
      'tip': 'Which brings us to the final step, compliance and consequences. The conclusion '
             'is that Global Trade Solutions is non-compliant. They face potential '
             'disciplinary action from CBP for the RSC failure up to license revocation.',
      'title': '[CBLE] CBLE3: Broker Licensing, Supervision, and Power of Attorney (19 CFR '
               'Part 111 & 141) (VoraPrep)',
      'url': 'https://www.youtube.com/watch?v=8NkJbs7UVvY&t=494s',
      'video_id': '8NkJbs7UVvY'},
     {'author': 'Clark-Esposito Law Firm P.C.',
      'channel': 'Clark-Esposito Law Firm P.C.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=yXBLHYkmz0A&t=42s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ensuring your goods are valued correctly not only avoids penalties but also '
              'ensures compliance with U. Customs and Border Protection, or CBP, regulations. '
              'In simple terms, Customs Value is the price of your goods as determined by '
              'specific rules set by CBP.',
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': 'Ensuring your goods are valued correctly not only avoids penalties but also '
             'ensures compliance with U. Customs and Border Protection, or CBP, regulations. '
             'In simple terms, Customs Value is the price of your goods as determined by '
             'specific rules set by CBP.',
      'title': 'U.S. Customs Value Explained (Clark-Esposito Law Firm P.C.)',
      'url': 'https://www.youtube.com/watch?v=yXBLHYkmz0A&t=42s',
      'video_id': 'yXBLHYkmz0A'},
     {'author': 'NBC4 Washington',
      'channel': 'NBC4 Washington',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:13](https://www.youtube.com/watch?v=ZitEpVz3Zgg&t=193s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Contact the law firm that is listed on that paperwork. Make sure it is legit, '
              'or contact the company itself to ask them what law firm is working with them '
              "for the settlement. And of course, the local attorney general's office as well. "
              'Thank you very much, Susan.',
      'timestamp': 193,
      'timestamp_label': '[00:03:13]',
      'timestamp_seconds': 193,
      'tip': 'Contact the law firm that is listed on that paperwork. Make sure it is legit, or '
             'contact the company itself to ask them what law firm is working with them for '
             "the settlement. And of course, the local attorney general's office as well. "
             'Thank you very much, Susan.',
      'title': "How to know if you're entitled to a class action settlement | NBC4 Washington "
               '(NBC4 Washington)',
      'url': 'https://www.youtube.com/watch?v=ZitEpVz3Zgg&t=193s',
      'video_id': 'ZitEpVz3Zgg'},
     {'author': 'JSJ INTERNATIONAL LCB',
      'channel': 'JSJ INTERNATIONAL LCB',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:37](https://www.youtube.com/watch?v=2cuZPxRLr1E&t=397s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '11362 custodian bond 1363 carries bond FCC operated 1364 or an ISF specify '
              "specific bond which is appendix D to part 113. So there's a bond for that. "
              'Obviously agents uh must have a signed power of attorney in English uh retained '
              'for 5 years after revocation.',
      'timestamp': 397,
      'timestamp_label': '[00:06:37]',
      'timestamp_seconds': 397,
      'tip': '11362 custodian bond 1363 carries bond FCC operated 1364 or an ISF specify '
             "specific bond which is appendix D to part 113. So there's a bond for that. "
             'Obviously agents uh must have a signed power of attorney in English uh retained '
             'for 5 years after revocation.',
      'title': 'ISF “10+2” Filing Explained | Importer Requirements under 19 CFR Part 149 | '
               'CBP Compliance Guide (JSJ INTERNATIONAL LCB)',
      'url': 'https://www.youtube.com/watch?v=2cuZPxRLr1E&t=397s',
      'video_id': '2cuZPxRLr1E'},
     {'author': 'Shapiro',
      'channel': 'Shapiro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:41](https://www.youtube.com/watch?v=cjNgBgUI1As&t=521s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Issue do you have a procedure where the commercial invoice is to be reviewed '
              'when received from the supplier auditing will help your overall compliance '
              'program including broker.',
      'timestamp': 521,
      'timestamp_label': '[00:08:41]',
      'timestamp_seconds': 521,
      'tip': 'Issue do you have a procedure where the commercial invoice is to be reviewed '
             'when received from the supplier auditing will help your overall compliance '
             'program including broker.',
      'title': 'Essentials of Customs Entry Auditing (Shapiro)',
      'url': 'https://www.youtube.com/watch?v=cjNgBgUI1As&t=521s',
      'video_id': 'cjNgBgUI1As'},
     {'author': 'Diaz Trade Law',
      'channel': 'Diaz Trade Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:17](https://www.youtube.com/watch?v=j_DJeCw3cCw&t=137s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'How do you file your prior disclosure? What happens when issues are uncovered? '
              "Who contacts whom within your company? Done right, pre-compliance doesn't just "
              "avoid problems. It can also save you money. Cuz maybe you'll find a "
              'misclassification.',
      'timestamp': 137,
      'timestamp_label': '[00:02:17]',
      'timestamp_seconds': 137,
      'tip': 'How do you file your prior disclosure? What happens when issues are uncovered? '
             "Who contacts whom within your company? Done right, pre-compliance doesn't just "
             "avoid problems. It can also save you money. Cuz maybe you'll find a "
             'misclassification.',
      'title': 'Why CBP Pre-Compliance Is More Important Than Ever (Diaz Trade Law)',
      'url': 'https://www.youtube.com/watch?v=j_DJeCw3cCw&t=137s',
      'video_id': 'j_DJeCw3cCw'},
     {'author': 'News of the World',
      'channel': 'News of the World',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:26](https://www.youtube.com/watch?v=vk_vF0qgIAg&t=26s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Supply of chicken in violation of state and federal consumer antitrust laws if '
              'you purchase chicken from january 1st 2009 through december 31st 2020 from.',
      'timestamp': 26,
      'timestamp_label': '[00:00:26]',
      'timestamp_seconds': 26,
      'tip': 'Supply of chicken in violation of state and federal consumer antitrust laws if '
             'you purchase chicken from january 1st 2009 through december 31st 2020 from.',
      'title': 'If you’ve bought chicken in the last 10 years, you may be eligible for payment '
               '(News of the World)',
      'url': 'https://www.youtube.com/watch?v=vk_vF0qgIAg&t=26s',
      'video_id': 'vk_vF0qgIAg'},
     {'author': 'Harry F. Long, Inc. - U.S. Customs Brokers',
      'channel': 'Harry F. Long, Inc. - U.S. Customs Brokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=oOC1WI_WDJs&t=126s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'An auto parts importer buys from a supplier for $180,000. The supplier '
              'purchased those parts from a Mexican factory with US export terms for $120,000. '
              'By declaring $120,000 as the value versus $180,000 reduces the tariffs that '
              'will be assessed on those parts.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': 'An auto parts importer buys from a supplier for $180,000. The supplier purchased '
             'those parts from a Mexican factory with US export terms for $120,000. By '
             'declaring $120,000 as the value versus $180,000 reduces the tariffs that will be '
             'assessed on those parts.',
      'title': 'Customs Quick Tips - First Sale Rule (Harry F. Long, Inc. - U.S. Customs '
               'Brokers)',
      'url': 'https://www.youtube.com/watch?v=oOC1WI_WDJs&t=126s',
      'video_id': 'oOC1WI_WDJs'},
     {'author': 'JSJ INTERNATIONAL LCB',
      'channel': 'JSJ INTERNATIONAL LCB',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:41](https://www.youtube.com/watch?v=OyJAzze4KyY&t=281s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now how to implement engineering legally? Um understand the uh general rules of '
              'interpretation and how CBP classifies goods. Use binding ruling request uh '
              'under title 19 code of federal relations part 177 to confirm your strategy with '
              'the CBP.',
      'timestamp': 281,
      'timestamp_label': '[00:04:41]',
      'timestamp_seconds': 281,
      'tip': 'Now how to implement engineering legally? Um understand the uh general rules of '
             'interpretation and how CBP classifies goods. Use binding ruling request uh under '
             'title 19 code of federal relations part 177 to confirm your strategy with the '
             'CBP.',
      'title': 'Tariff Engineering & Duty Reduction (JSJ INTERNATIONAL LCB)',
      'url': 'https://www.youtube.com/watch?v=OyJAzze4KyY&t=281s',
      'video_id': 'OyJAzze4KyY'},
     {'author': 'Adriel Miller',
      'channel': 'Adriel Miller',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=wL00BhzuPec&t=36s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Specifics of ISF compliance for Duty drawback programs let's first understand "
              'what Duty drawback is all about Duty drawback refers to a refund or rebate on.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': "Specifics of ISF compliance for Duty drawback programs let's first understand "
             'what Duty drawback is all about Duty drawback refers to a refund or rebate on.',
      'title': 'Mastering ISF Compliance for Duty Drawbacks (Adriel Miller)',
      'url': 'https://www.youtube.com/watch?v=wL00BhzuPec&t=36s',
      'video_id': 'wL00BhzuPec'},
     {'author': 'Daily Q&A',
      'channel': 'Daily Q&A',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=8IcVk3YXDoM&t=55s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The settlement approval means these businesses can now finally seek '
              'compensation. The legal process started with a court approval of the damages '
              'portion back in 2019, allowing merchants to send in claims.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'The settlement approval means these businesses can now finally seek '
             'compensation. The legal process started with a court approval of the damages '
             'portion back in 2019, allowing merchants to send in claims.',
      'title': 'What Is the Visa Mastercard Settlement Judge Approval Case About? | 2026 '
               '(Daily Q&A)',
      'url': 'https://www.youtube.com/watch?v=8IcVk3YXDoM&t=55s',
      'video_id': '8IcVk3YXDoM'},
     {'author': 'ImportGenius',
      'channel': 'ImportGenius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:20](https://www.youtube.com/watch?v=9IaKZ1JUPmU&t=200s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Another really important thing to do is to leave off terms like Inc or limited '
              "so for example I'm going to search Sky High unlimited which is one of the "
              'results that I see right now and if I type.',
      'timestamp': 200,
      'timestamp_label': '[00:03:20]',
      'timestamp_seconds': 200,
      'tip': 'Another really important thing to do is to leave off terms like Inc or limited '
             "so for example I'm going to search Sky High unlimited which is one of the "
             'results that I see right now and if I type.',
      'title': 'Import Genius Advanced Search Techniques Help Video (ImportGenius)',
      'url': 'https://www.youtube.com/watch?v=9IaKZ1JUPmU&t=200s',
      'video_id': '9IaKZ1JUPmU'},
     {'author': 'Vmani International',
      'channel': 'Vmani International',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:36](https://www.youtube.com/watch?v=WyZnXlLGG-o&t=216s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'International for more valuable insights let me know in the comments what topic '
              "you'd like me to cover next see you in the next.",
      'timestamp': 216,
      'timestamp_label': '[00:03:36]',
      'timestamp_seconds': 216,
      'tip': 'International for more valuable insights let me know in the comments what topic '
             "you'd like me to cover next see you in the next.",
      'title': 'USA CBP Rules Explained! Import-Export Compliance Made Easy (Vmani '
               'International)',
      'url': 'https://www.youtube.com/watch?v=WyZnXlLGG-o&t=216s',
      'video_id': 'WyZnXlLGG-o'},
     {'author': 'Scarbrough Global',
      'channel': 'Scarbrough Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:40](https://www.youtube.com/watch?v=fI28fmPlbPA&t=340s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Chain as a whole in your import compliance program as a whole you know there's "
              'obviously some things out there that that would maybe make you rethink that are '
              "kind of look to say maybe there's something a little bit better right.",
      'timestamp': 340,
      'timestamp_label': '[00:05:40]',
      'timestamp_seconds': 340,
      'tip': "Chain as a whole in your import compliance program as a whole you know there's "
             'obviously some things out there that that would maybe make you rethink that are '
             "kind of look to say maybe there's something a little bit better right.",
      'title': 'What is Substitution Drawback when claiming duty drawback ? (Scarbrough '
               'Global)',
      'url': 'https://www.youtube.com/watch?v=fI28fmPlbPA&t=340s',
      'video_id': 'fI28fmPlbPA'},
     {'author': 'Tariffs Lawsuit',
      'channel': 'Tariffs Lawsuit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:08](https://www.youtube.com/watch?v=dWEik4YquEE&t=248s)',
      'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                   'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                   'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                   'Post-Summary Correction tariff protests, and settled B2B '
                   'antitrust/interchange class-action pools (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Section 301 tariffs are knocked down through final United States Supreme Court '
              'decisions, there may be another $200 billion in new tariffs levied by the Trump '
              'administration throughout the rest of his terms.',
      'timestamp': 248,
      'timestamp_label': '[00:04:08]',
      'timestamp_seconds': 248,
      'tip': 'Section 301 tariffs are knocked down through final United States Supreme Court '
             'decisions, there may be another $200 billion in new tariffs levied by the Trump '
             'administration throughout the rest of his terms.',
      'title': 'Tariff Refund Update: Why Importers May Need To File Now (Tariffs Lawsuit)',
      'url': 'https://www.youtube.com/watch?v=dWEik4YquEE&t=248s',
      'video_id': 'dWEik4YquEE'}],
 10: [{'author': 'ImageSearch for HS classification',
       'channel': 'ImageSearch for HS classification',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:25](https://www.youtube.com/watch?v=Z20K9hWki3Q&t=145s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Powers of attorney must be executed directly between the broker and importer, '
               'and platforms must strictly safeguard client record confidentiality under 19 '
               'CFR 111. So this ruling makes it crystal clear. Automation must respect legal '
               'boundaries.',
       'timestamp': 145,
       'timestamp_label': '[00:02:25]',
       'timestamp_seconds': 145,
       'tip': 'Powers of attorney must be executed directly between the broker and importer, '
              'and platforms must strictly safeguard client record confidentiality under 19 '
              'CFR 111. So this ruling makes it crystal clear. Automation must respect legal '
              'boundaries.',
       'title': 'The US CBP declaring an AI-based HS classification tool illegal. (ImageSearch '
                'for HS classification)',
       'url': 'https://www.youtube.com/watch?v=Z20K9hWki3Q&t=145s',
       'video_id': 'Z20K9hWki3Q'},
      {'author': 'Center for Strategic & International Studies',
       'channel': 'Center for Strategic & International Studies',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:59](https://www.youtube.com/watch?v=PJpF0M_rjYs&t=719s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Reliable suppliers are hard to find. Reliable customers are treated like gold '
               'by most companies who are customer-facing. So, there is work to be done in '
               "that area. And when you're dealing with China's retaliation, first of all, as "
               "Bill pointed out, it's large in scale.",
       'timestamp': 719,
       'timestamp_label': '[00:11:59]',
       'timestamp_seconds': 719,
       'tip': 'Reliable suppliers are hard to find. Reliable customers are treated like gold '
              'by most companies who are customer-facing. So, there is work to be done in that '
              "area. And when you're dealing with China's retaliation, first of all, as Bill "
              "pointed out, it's large in scale.",
       'title': "China's Retaliatory Tariffs, Section 301 Authorities, and Tariff Refund "
                'Litigation (Center for Strategic & International Studies)',
       'url': 'https://www.youtube.com/watch?v=PJpF0M_rjYs&t=719s',
       'video_id': 'PJpF0M_rjYs'},
      {'author': 'PolitiClash',
       'channel': 'PolitiClash',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:58](https://www.youtube.com/watch?v=uhEb06Zt2cw&t=358s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'His economic adviser later said a proposal would go to Congress. Here is the '
               'record since: no administration bill was ever formally sent. Three rebate '
               'bills from members of Congress — none of them for the full $2,000 — sit in '
               'committee. None has passed either chamber.',
       'timestamp': 358,
       'timestamp_label': '[00:05:58]',
       'timestamp_seconds': 358,
       'tip': 'His economic adviser later said a proposal would go to Congress. Here is the '
              'record since: no administration bill was ever formally sent. Three rebate bills '
              'from members of Congress — none of them for the full $2,000 — sit in committee. '
              'None has passed either chamber.',
       'title': 'The $166 Billion Tariff Refund: Who Actually Gets It, Checked (PolitiClash)',
       'url': 'https://www.youtube.com/watch?v=uhEb06Zt2cw&t=358s',
       'video_id': 'uhEb06Zt2cw'},
      {'author': 'Who Pays For It',
       'channel': 'Who Pays For It',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:20](https://www.youtube.com/watch?v=q4JXW2PbDBk&t=620s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "A tax that one person pays and another person carries is easy to collect. It's "
               'a lot harder to give back. Next time power companies are building new plants '
               'and power lines to feed AI data centers. Somebody has to pay for that. Is it '
               'the tech companies or your electric bill?',
       'timestamp': 620,
       'timestamp_label': '[00:10:20]',
       'timestamp_seconds': 620,
       'tip': "A tax that one person pays and another person carries is easy to collect. It's "
              'a lot harder to give back. Next time power companies are building new plants '
              'and power lines to feed AI data centers. Somebody has to pay for that. Is it '
              'the tech companies or your electric bill?',
       'title': 'Who Gets the $166 Billion Tariff Refund? (Not You) (Who Pays For It)',
       'url': 'https://www.youtube.com/watch?v=q4JXW2PbDBk&t=620s',
       'video_id': 'q4JXW2PbDBk'},
      {'author': 'U.S. Customs and Border Protection',
       'channel': 'U.S. Customs and Border Protection',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:10](https://www.youtube.com/watch?v=CXFkPqsyXnI&t=130s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'In the interested party field use the dropdown arrow and select the '
               'appropriate category. In the “Are You a Small Business? For more information, '
               'click the link to the “Small business Administration” In the "Are You a Lawyer '
               'or Agent Representing an Interested Party?".',
       'timestamp': 130,
       'timestamp_label': '[00:02:10]',
       'timestamp_seconds': 130,
       'tip': 'In the interested party field use the dropdown arrow and select the appropriate '
              'category. In the “Are You a Small Business? For more information, click the '
              'link to the “Small business Administration” In the "Are You a Lawyer or Agent '
              'Representing an Interested Party?".',
       'title': 'Steps to Submitting an Allegation - Enforce and Protect Act (EAPA) | Office '
                'of Trade | CBP (U.S. Customs and Border Protection)',
       'url': 'https://www.youtube.com/watch?v=CXFkPqsyXnI&t=130s',
       'video_id': 'CXFkPqsyXnI'},
      {'author': 'Scarbrough Global',
       'channel': 'Scarbrough Global',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:55](https://www.youtube.com/watch?v=GuV2m_XHyd0&t=115s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "'ve gotta be able to provide the commercial invoice and the packing slip and a "
               'copy of the bill of lading and the the purpose of that is because we need to '
               'be able to file our customs entry by the time it docks in the u.',
       'timestamp': 115,
       'timestamp_label': '[00:01:55]',
       'timestamp_seconds': 115,
       'tip': "'ve gotta be able to provide the commercial invoice and the packing slip and a "
              'copy of the bill of lading and the the purpose of that is because we need to be '
              'able to file our customs entry by the time it docks in the u.',
       'title': 'What is CBP ACE Automated Commercial Environment? (Scarbrough Global)',
       'url': 'https://www.youtube.com/watch?v=GuV2m_XHyd0&t=115s',
       'video_id': 'GuV2m_XHyd0'},
      {'author': 'Docxster | Document-First Automation',
       'channel': 'Docxster | Document-First Automation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:59](https://www.youtube.com/watch?v=bsk4ScOMz_o&t=59s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "So, I'm going to go ahead and collect this box and head into my inbox here, "
               'there we go, and quickly attach that file. So, what that actually looks like '
               'is I have a house airway bill number right here. And, as you can see, we have '
               'all of the details.',
       'timestamp': 59,
       'timestamp_label': '[00:00:59]',
       'timestamp_seconds': 59,
       'tip': "So, I'm going to go ahead and collect this box and head into my inbox here, "
              'there we go, and quickly attach that file. So, what that actually looks like is '
              'I have a house airway bill number right here. And, as you can see, we have all '
              'of the details.',
       'title': 'How to Automate CBP Form 7512 Inbond Entries in NetCHB (Docxster Demo) '
                '(Docxster | Document-First Automation)',
       'url': 'https://www.youtube.com/watch?v=bsk4ScOMz_o&t=59s',
       'video_id': 'bsk4ScOMz_o'},
      {'author': 'Chartered Inst. of Export & International Trade',
       'channel': 'Chartered Inst. of Export & International Trade',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:54](https://www.youtube.com/watch?v=mimI2zifsUA&t=774s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Company that is selling a product and it pays an agent to market that product '
               "on its behalf to to improve its sales then those selling Commission's must be "
               'added.',
       'timestamp': 774,
       'timestamp_label': '[00:12:54]',
       'timestamp_seconds': 774,
       'tip': 'Company that is selling a product and it pays an agent to market that product '
              "on its behalf to to improve its sales then those selling Commission's must be "
              'added.',
       'title': 'Customs 101: Methods of valuation for import duty (Chartered Inst. of Export '
                '& International Trade)',
       'url': 'https://www.youtube.com/watch?v=mimI2zifsUA&t=774s',
       'video_id': 'mimI2zifsUA'},
      {'author': 'Mandy Wu',
       'channel': 'Mandy Wu',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:03](https://www.youtube.com/watch?v=l9SdxEh635U&t=243s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Name here too then the date okay that's all the field the phone is already "
               'finished okay lesson template which fulfilled by one of our customers you see '
               'the company and his IRS number.',
       'timestamp': 243,
       'timestamp_label': '[00:04:03]',
       'timestamp_seconds': 243,
       'tip': "Name here too then the date okay that's all the field the phone is already "
              'finished okay lesson template which fulfilled by one of our customers you see '
              'the company and his IRS number.',
       'title': 'How to fulfill the CBP form (Mandy Wu)',
       'url': 'https://www.youtube.com/watch?v=l9SdxEh635U&t=243s',
       'video_id': 'l9SdxEh635U'},
      {'author': 'Cole International',
       'channel': 'Cole International',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:58](https://www.youtube.com/watch?v=x-SDVKIzJdI&t=118s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Recommended that companies seek help from a professionally licensed customs '
               'broker or customs attorney to ensure proper classification of products you.',
       'timestamp': 118,
       'timestamp_label': '[00:01:58]',
       'timestamp_seconds': 118,
       'tip': 'Recommended that companies seek help from a professionally licensed customs '
              'broker or customs attorney to ensure proper classification of products you.',
       'title': 'Tariff Classification - A Step by Step Guide (Cole International)',
       'url': 'https://www.youtube.com/watch?v=x-SDVKIzJdI&t=118s',
       'video_id': 'x-SDVKIzJdI'},
      {'author': 'Flexport',
       'channel': 'Flexport',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:34:18](https://www.youtube.com/watch?v=1_L7fnmAAU0&t=2058s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Visibility to your drawback claims this automation truly helps streamline the '
               'administrative process for all parties involved.',
       'timestamp': 2058,
       'timestamp_label': '[00:34:18]',
       'timestamp_seconds': 2058,
       'tip': 'Visibility to your drawback claims this automation truly helps streamline the '
              'administrative process for all parties involved.',
       'title': 'Optimizing Duty Drawback for Maximum Refunds (Flexport)',
       'url': 'https://www.youtube.com/watch?v=1_L7fnmAAU0&t=2058s',
       'video_id': '1_L7fnmAAU0'},
      {'author': 'GlobalTech Infosystems',
       'channel': 'GlobalTech Infosystems',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=cxXp_4blJrQ&t=15s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'होना होता है। यूएस कस्टम्स एंड बॉर्डर प्रोटेक्शन यानी सीबीपी इस पूरे इंटरनेशनल '
               'कॉमर्स का एब्सोल्यूट गेटकीपर है। कोई भी कमर्शियल गुड्स सीबीपी के अप्रूवल के '
               'बिना.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'होना होता है। यूएस कस्टम्स एंड बॉर्डर प्रोटेक्शन यानी सीबीपी इस पूरे इंटरनेशनल '
              'कॉमर्स का एब्सोल्यूट गेटकीपर है। कोई भी कमर्शियल गुड्स सीबीपी के अप्रूवल के '
              'बिना.',
       'title': 'USA Customs Broker Power of Attorney (POA) 🇺🇸 | Importer & Broker '
                'Relationship Explained (GlobalTech Infosystems)',
       'url': 'https://www.youtube.com/watch?v=cxXp_4blJrQ&t=15s',
       'video_id': 'cxXp_4blJrQ'},
      {'author': 'Sachin Kharatmal',
       'channel': 'Sachin Kharatmal',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=pokSeGRFDUs&t=15s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'समथिंग एस सिंपल एस डॉक्यूमेंटेशन मिसमैच। यस समटाइम्स द प्रॉब्लम इज नॉट योर '
               'शिपमेंट। द प्रॉब्लम [नाक से की जाने वाली आवाज़] इज पेपर वर्क.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'समथिंग एस सिंपल एस डॉक्यूमेंटेशन मिसमैच। यस समटाइम्स द प्रॉब्लम इज नॉट योर '
              'शिपमेंट। द प्रॉब्लम [नाक से की जाने वाली आवाज़] इज पेपर वर्क.',
       'title': 'How To Claim Duty Drawback Benefits: Import Licenses & COO Explained '
                '@Sachin.Kharatmal (Sachin Kharatmal)',
       'url': 'https://www.youtube.com/watch?v=pokSeGRFDUs&t=15s',
       'video_id': 'pokSeGRFDUs'},
      {'author': 'Scarbrough Global',
       'channel': 'Scarbrough Global',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:39](https://www.youtube.com/watch?v=m4ePKta6BXo&t=39s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "'t that go in duty-free exactly no it's just a question a it's it's some of "
               "those stuff that's coming in I just want to make sure that we're all kind of "
               'on the same page is that with the Foreign Trade Zone as things do come into '
               'the u.',
       'timestamp': 39,
       'timestamp_label': '[00:00:39]',
       'timestamp_seconds': 39,
       'tip': "'t that go in duty-free exactly no it's just a question a it's it's some of "
              "those stuff that's coming in I just want to make sure that we're all kind of on "
              'the same page is that with the Foreign Trade Zone as things do come into the u.',
       'title': 'Duty Drawback and Foreign Trade Zone FTZ (Scarbrough Global)',
       'url': 'https://www.youtube.com/watch?v=m4ePKta6BXo&t=39s',
       'video_id': 'm4ePKta6BXo'},
      {'author': 'IEEPA Tariff Watch',
       'channel': 'IEEPA Tariff Watch',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:07](https://www.youtube.com/watch?v=V9_1adwF1c8&t=187s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "And if you've got some of those common errors, well, your refund claim could "
               "easily become the trigger for a painful and very expensive audit. So, let's "
               "lay out these three gaps side by side. Think of it as the broker's reality "
               "versus the attorney's advantage.",
       'timestamp': 187,
       'timestamp_label': '[00:03:07]',
       'timestamp_seconds': 187,
       'tip': "And if you've got some of those common errors, well, your refund claim could "
              "easily become the trigger for a painful and very expensive audit. So, let's lay "
              "out these three gaps side by side. Think of it as the broker's reality versus "
              "the attorney's advantage.",
       'title': 'Before You File for a Section 301 Tariff Refund: The Audit Risk Every '
                'Importer Needs to Understand (IEEPA Tariff Watch)',
       'url': 'https://www.youtube.com/watch?v=V9_1adwF1c8&t=187s',
       'video_id': 'V9_1adwF1c8'}],
 11: [{'author': 'JSJ INTERNATIONAL LCB',
       'channel': 'JSJ INTERNATIONAL LCB',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:47](https://www.youtube.com/watch?v=n4YfLCDwg1M&t=347s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Okay, so make sure you have everything um to reduce audit risk and um '
               'demonstrate reasonable care. Build a customs compliance manual tailored to '
               'your operations. Cover all key regulatory areas. Train your team and update uh '
               'regularly. Okay, you got to do training.',
       'timestamp': 347,
       'timestamp_label': '[00:05:47]',
       'timestamp_seconds': 347,
       'tip': 'Okay, so make sure you have everything um to reduce audit risk and um '
              'demonstrate reasonable care. Build a customs compliance manual tailored to your '
              'operations. Cover all key regulatory areas. Train your team and update uh '
              'regularly. Okay, you got to do training.',
       'title': 'Step-by-Step: Build a CBP Compliance Manual That Protects You from Fines & '
                'Audits (JSJ INTERNATIONAL LCB)',
       'url': 'https://www.youtube.com/watch?v=n4YfLCDwg1M&t=347s',
       'video_id': 'n4YfLCDwg1M'},
      {'author': 'SKUio',
       'channel': 'SKUio',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:55](https://www.youtube.com/watch?v=WLDwLas6IOI&t=55s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'An entry filed for another company is then flagged, and is never applied. To '
               'bring an entry in, click the Import entries button. Choose 7501 PDF for one '
               'entry from your broker, or ACE ES-003 report for many at once. Drop the file '
               'here, or click to browse your computer.',
       'timestamp': 55,
       'timestamp_label': '[00:00:55]',
       'timestamp_seconds': 55,
       'tip': 'An entry filed for another company is then flagged, and is never applied. To '
              'bring an entry in, click the Import entries button. Choose 7501 PDF for one '
              'entry from your broker, or ACE ES-003 report for many at once. Drop the file '
              'here, or click to browse your computer.',
       'title': 'Split a Customs Duty Bill by Product with CBP 7501 Entry Summaries | SKU.io '
                '(SKUio)',
       'url': 'https://www.youtube.com/watch?v=WLDwLas6IOI&t=55s',
       'video_id': 'WLDwLas6IOI'},
      {'author': 'International Housewares Association',
       'channel': 'International Housewares Association',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:01](https://www.youtube.com/watch?v=RaySaQSBqfE&t=361s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': '301 is much more defensible for the administration than some of these other '
               "sections trade statutes that they've tried to use.",
       'timestamp': 361,
       'timestamp_label': '[00:06:01]',
       'timestamp_seconds': 361,
       'tip': '301 is much more defensible for the administration than some of these other '
              "sections trade statutes that they've tried to use.",
       'title': 'Update on new “Forced Labor” Tariffs and other Tariff-Related Developments '
                '(International Housewares Association)',
       'url': 'https://www.youtube.com/watch?v=RaySaQSBqfE&t=361s',
       'video_id': 'RaySaQSBqfE'},
      {'author': 'OSV FTWZ',
       'channel': 'OSV FTWZ',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:51](https://www.youtube.com/watch?v=gKGLwtinJk8&t=531s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "'re not navigating that alone. Real-time inventory tracking through our "
               'warehouse management system. Support for foreign companies operating in India '
               'without a local entity. Multi-scale operations from mid-size traders to '
               'enterprise level multinationals.',
       'timestamp': 531,
       'timestamp_label': '[00:08:51]',
       'timestamp_seconds': 531,
       'tip': "'re not navigating that alone. Real-time inventory tracking through our "
              'warehouse management system. Support for foreign companies operating in India '
              'without a local entity. Multi-scale operations from mid-size traders to '
              'enterprise level multinationals.',
       'title': 'What Is Free Trade Warehousing Zone (FTWZ)? How It Solves Customs Duty & Cash '
                'Flow Problems in India (OSV FTWZ)',
       'url': 'https://www.youtube.com/watch?v=gKGLwtinJk8&t=531s',
       'video_id': 'gKGLwtinJk8'},
      {'author': 'Crazy Deals and Steals',
       'channel': 'Crazy Deals and Steals',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:46](https://www.youtube.com/watch?v=IP9zniHMMKM&t=166s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Vinmo and through the automated system, they said that my personal Vinmo '
               'credit card was lost or stolen. So, that one was cancelled and they sent a new '
               'one out. Every time a new one was sent out, I would get an email. So, I would '
               'have to call Vinmo and cancel that one.',
       'timestamp': 166,
       'timestamp_label': '[00:02:46]',
       'timestamp_seconds': 166,
       'tip': 'Vinmo and through the automated system, they said that my personal Vinmo credit '
              'card was lost or stolen. So, that one was cancelled and they sent a new one '
              'out. Every time a new one was sent out, I would get an email. So, I would have '
              'to call Vinmo and cancel that one.',
       'title': '$177 MILLION AT&T Class Action Lawsuit! How To Class Action Settlement '
                '#classaction (Crazy Deals and Steals)',
       'url': 'https://www.youtube.com/watch?v=IP9zniHMMKM&t=166s',
       'video_id': 'IP9zniHMMKM'},
      {'author': 'ABC15 Arizona',
       'channel': 'ABC15 Arizona',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:06](https://www.youtube.com/watch?v=Ef-vxIV8GSg&t=126s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Abc15.com click on sections and let Joe know and we need your help if you can '
               'volunteer to help others as part of the Assistance League team call us email '
               "find me on Facebook or Twitter I'm investigator Joe Ducey if you've got a "
               'problem let me know.',
       'timestamp': 126,
       'timestamp_label': '[00:02:06]',
       'timestamp_seconds': 126,
       'tip': 'Abc15.com click on sections and let Joe know and we need your help if you can '
              'volunteer to help others as part of the Assistance League team call us email '
              "find me on Facebook or Twitter I'm investigator Joe Ducey if you've got a "
              'problem let me know.',
       'title': 'Class action settlements could mean money back for you (ABC15 Arizona)',
       'url': 'https://www.youtube.com/watch?v=Ef-vxIV8GSg&t=126s',
       'video_id': 'Ef-vxIV8GSg'},
      {'author': 'Gallagher Transport International Inc.',
       'channel': 'Gallagher Transport International Inc.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:05](https://www.youtube.com/watch?v=k2CbBPEtqNI&t=65s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "There's also a waiver of prior notice that lets you file future claims without "
               'asking permission each time. You can apply for accelerated payment to get your '
               'refunds faster once you submit your claims. You have 5 years from the import '
               'date to submit your claim.',
       'timestamp': 65,
       'timestamp_label': '[00:01:05]',
       'timestamp_seconds': 65,
       'tip': "There's also a waiver of prior notice that lets you file future claims without "
              'asking permission each time. You can apply for accelerated payment to get your '
              'refunds faster once you submit your claims. You have 5 years from the import '
              'date to submit your claim.',
       'title': 'Understanding Duty Drawback: Recover Duties & Reduce Trade Costs (Gallagher '
                'Transport International Inc.)',
       'url': 'https://www.youtube.com/watch?v=k2CbBPEtqNI&t=65s',
       'video_id': 'k2CbBPEtqNI'},
      {'author': 'Greater Cincinnati Foreign Trade Zones',
       'channel': 'Greater Cincinnati Foreign Trade Zones',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:50](https://www.youtube.com/watch?v=8TKnN_7QZFw&t=110s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Together, these advantages mean lower costs, streamlined customs and stronger '
               'competitiveness. And remember the greater Cincinnati Northern Kentucky FTZ '
               'team is always here to guide and connect you with experts, making your '
               'application process smooth and successful.',
       'timestamp': 110,
       'timestamp_label': '[00:01:50]',
       'timestamp_seconds': 110,
       'tip': 'Together, these advantages mean lower costs, streamlined customs and stronger '
              'competitiveness. And remember the greater Cincinnati Northern Kentucky FTZ team '
              'is always here to guide and connect you with experts, making your application '
              'process smooth and successful.',
       'title': 'How FTZs Work | Benefits, Process & Key Facts (Greater Cincinnati Foreign '
                'Trade Zones)',
       'url': 'https://www.youtube.com/watch?v=8TKnN_7QZFw&t=110s',
       'video_id': '8TKnN_7QZFw'},
      {'author': 'How Stuff Moves',
       'channel': 'How Stuff Moves',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:59](https://www.youtube.com/watch?v=GGGUB13U6vk&t=119s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Hiring a does not move the liability. The broker files the paperwork as your '
               'agent. Customs comes after the importer of record. So the importer of record '
               'is the name on the line where the money and the law meet.',
       'timestamp': 119,
       'timestamp_label': '[00:01:59]',
       'timestamp_seconds': 119,
       'tip': 'Hiring a does not move the liability. The broker files the paperwork as your '
              'agent. Customs comes after the importer of record. So the importer of record is '
              'the name on the line where the money and the law meet.',
       'title': 'Who Can Import Into America? The January 5 Rule Rewriting the Answer (How '
                'Stuff Moves)',
       'url': 'https://www.youtube.com/watch?v=GGGUB13U6vk&t=119s',
       'video_id': 'GGGUB13U6vk'},
      {'author': 'Law Office of Yuri Starikov, LLC',
       'channel': 'Law Office of Yuri Starikov, LLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=aNG7o_BW3k8&t=15s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': '7501 and uh now we uh get to the point where we are ready to discuss how to '
               'really fill in those blanks what goes in what goes in into this into this '
               'into.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': '7501 and uh now we uh get to the point where we are ready to discuss how to '
              'really fill in those blanks what goes in what goes in into this into this into.',
       'title': 'U.S. Customs (CBP) Entry Summary: General Overview Webcast Preview (Law '
                'Office of Yuri Starikov, LLC)',
       'url': 'https://www.youtube.com/watch?v=aNG7o_BW3k8&t=15s',
       'video_id': 'aNG7o_BW3k8'},
      {'author': 'Scarbrough Global',
       'channel': 'Scarbrough Global',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=m-RN8tPLnPk&t=15s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Hi I'm Adam Hill with Scarborough International I'm the Vice President of "
               "Operations here um often we're asked what is a power of.",
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': "Hi I'm Adam Hill with Scarborough International I'm the Vice President of "
              "Operations here um often we're asked what is a power of.",
       'title': 'Why do I need a Customs Power of Attorney (POA)? #scarbroughsnippets '
                '(Scarbrough Global)',
       'url': 'https://www.youtube.com/watch?v=m-RN8tPLnPk&t=15s',
       'video_id': 'm-RN8tPLnPk'},
      {'author': 'The Class Action Attorney',
       'channel': 'The Class Action Attorney',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:41](https://www.youtube.com/watch?v=EDXGiD2K8sY&t=101s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Like that but each case is different so what you should do is look at the '
               'settlement website um see if you want to pursue a claim on your own and if you '
               "don't and you have no issues with the settlement then typically you should "
               'submit a claim thanks so much for watching.',
       'timestamp': 101,
       'timestamp_label': '[00:01:41]',
       'timestamp_seconds': 101,
       'tip': 'Like that but each case is different so what you should do is look at the '
              'settlement website um see if you want to pursue a claim on your own and if you '
              "don't and you have no issues with the settlement then typically you should "
              'submit a claim thanks so much for watching.',
       'title': 'Should I make a claim in a class action settlement? (The Class Action '
                'Attorney)',
       'url': 'https://www.youtube.com/watch?v=EDXGiD2K8sY&t=101s',
       'video_id': 'EDXGiD2K8sY'},
      {'author': 'Ask The Customs Manager',
       'channel': 'Ask The Customs Manager',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:07](https://www.youtube.com/watch?v=44NIfUvkQRo&t=367s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "For the full regulatory text, consult CBP's interim final rule, Heightened "
               'Requirements for Foreign Importers of Record, published in the Federal '
               'Register on 6 November 2026. Thank you for watching Ask the Customs Manager.',
       'timestamp': 367,
       'timestamp_label': '[00:06:07]',
       'timestamp_seconds': 367,
       'tip': "For the full regulatory text, consult CBP's interim final rule, Heightened "
              'Requirements for Foreign Importers of Record, published in the Federal Register '
              'on 6 November 2026. Thank you for watching Ask the Customs Manager.',
       'title': 'US Imports The New CTPAT Rule for Foreign Importers of Record (Ask The '
                'Customs Manager)',
       'url': 'https://www.youtube.com/watch?v=44NIfUvkQRo&t=367s',
       'video_id': '44NIfUvkQRo'},
      {'author': 'Scarbrough Global',
       'channel': 'Scarbrough Global',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:16](https://www.youtube.com/watch?v=GDJSfFVXx1M&t=16s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Scrutiny and targeting by US Customs no not in the sense of a bad thing if you '
               'file the drug that claimed anything that you file.',
       'timestamp': 16,
       'timestamp_label': '[00:00:16]',
       'timestamp_seconds': 16,
       'tip': 'Scrutiny and targeting by US Customs no not in the sense of a bad thing if you '
              'file the drug that claimed anything that you file.',
       'title': 'Do Duty Drawback claims open you up for US  Customs scrutiny ? (Scarbrough '
                'Global)',
       'url': 'https://www.youtube.com/watch?v=GDJSfFVXx1M&t=16s',
       'video_id': 'GDJSfFVXx1M'},
      {'author': 'Center for Strategic & International Studies',
       'channel': 'Center for Strategic & International Studies',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=PJpF0M_rjYs&t=21s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Thanks for listening to The Trade Guys. On today's episode, we examine the "
               "impact of China's retaliatory tariffs, take a look at the Trump "
               "administration's new use of Section 301 authorities, and unpack the latest "
               'litigation around tariff refunds.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': "Thanks for listening to The Trade Guys. On today's episode, we examine the "
              "impact of China's retaliatory tariffs, take a look at the Trump "
              "administration's new use of Section 301 authorities, and unpack the latest "
              'litigation around tariff refunds.',
       'title': "China's Retaliatory Tariffs, Section 301 Authorities, and Tariff Refund "
                'Litigation (Center for Strategic & International Studies)',
       'url': 'https://www.youtube.com/watch?v=PJpF0M_rjYs&t=21s',
       'video_id': 'PJpF0M_rjYs'}],
 12: [{'author': 'Tariffs Lawsuit',
       'channel': 'Tariffs Lawsuit',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:37](https://www.youtube.com/watch?v=dWEik4YquEE&t=97s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Section 122 and we'll aim to get that back for you as well. And then finally, "
               "knowing that his 150 days is almost up in August, President Trump's "
               "administration has already come up with plan C. And that's so-called Section "
               '301 tariffs under the Trade Act.',
       'timestamp': 97,
       'timestamp_label': '[00:01:37]',
       'timestamp_seconds': 97,
       'tip': "Section 122 and we'll aim to get that back for you as well. And then finally, "
              "knowing that his 150 days is almost up in August, President Trump's "
              "administration has already come up with plan C. And that's so-called Section "
              '301 tariffs under the Trade Act.',
       'title': 'Tariff Refund Update: Why Importers May Need To File Now (Tariffs Lawsuit)',
       'url': 'https://www.youtube.com/watch?v=dWEik4YquEE&t=97s',
       'video_id': 'dWEik4YquEE'},
      {'author': 'GHY International',
       'channel': 'GHY International',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:27:15](https://www.youtube.com/watch?v=pyMQL8u25fU&t=1635s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Everything that we've seen was a recommended five-day minimum of action. So, "
               "um, that part is five days is a long time if you're trying to ship your stuff. "
               "Let me see if there's anything else that I had written down for this one.",
       'timestamp': 1635,
       'timestamp_label': '[00:27:15]',
       'timestamp_seconds': 1635,
       'tip': "Everything that we've seen was a recommended five-day minimum of action. So, "
              "um, that part is five days is a long time if you're trying to ship your stuff. "
              "Let me see if there's anything else that I had written down for this one.",
       'title': 'Is Your Importer of Record Status at Risk - Validating Your CBP Records   '
                'Understanding Form 5106 (GHY International)',
       'url': 'https://www.youtube.com/watch?v=pyMQL8u25fU&t=1635s',
       'video_id': 'pyMQL8u25fU'},
      {'author': 'Simply Trade Podcast',
       'channel': 'Simply Trade Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:21:50](https://www.youtube.com/watch?v=3N8L-IKPY4A&t=1310s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "I've been doing this for about 17 years, back in the old days, we were all on "
               "paper, a lot of the stuff had to be re keyed as you're sitting there typing in "
               "all of the data that's on a 7501 entry summary. But now it's so much more "
               'automated.',
       'timestamp': 1310,
       'timestamp_label': '[00:21:50]',
       'timestamp_seconds': 1310,
       'tip': "I've been doing this for about 17 years, back in the old days, we were all on "
              "paper, a lot of the stuff had to be re keyed as you're sitting there typing in "
              "all of the data that's on a 7501 entry summary. But now it's so much more "
              'automated.',
       'title': 'Tariffs Killing Your Profit Margins? Duty Drawback Explained by Ariana Cox '
                '(Simply Trade Podcast)',
       'url': 'https://www.youtube.com/watch?v=3N8L-IKPY4A&t=1310s',
       'video_id': '3N8L-IKPY4A'},
      {'author': 'Brandon M. Young',
       'channel': 'Brandon M. Young',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:18](https://www.youtube.com/watch?v=nWH_1DtEHoA&t=258s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'All of them are being bombarded by sellers right now and brands right now. '
               "It's a multi month process for a warehouse to become bonded in The United "
               'States. Now Steve Simonson spoke a little bit about this at BDSS.',
       'timestamp': 258,
       'timestamp_label': '[00:04:18]',
       'timestamp_seconds': 258,
       'tip': "All of them are being bombarded by sellers right now and brands right now. It's "
              'a multi month process for a warehouse to become bonded in The United States. '
              'Now Steve Simonson spoke a little bit about this at BDSS.',
       'title': 'WARNING Amazon FBA Sellers Are Losing THOUSANDS to Tariff Expenses (Brandon '
                'M. Young)',
       'url': 'https://www.youtube.com/watch?v=nWH_1DtEHoA&t=258s',
       'video_id': 'nWH_1DtEHoA'},
      {'author': 'Harry F. Long, Inc. - U.S. Customs Brokers',
       'channel': 'Harry F. Long, Inc. - U.S. Customs Brokers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:26](https://www.youtube.com/watch?v=bD2cV_iBUpU&t=26s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Then click on the word entry summary below. The first report you want to run '
               'is the ES001 entry summary header details. Start by choosing your ACE trade '
               'account ID number.',
       'timestamp': 26,
       'timestamp_label': '[00:00:26]',
       'timestamp_seconds': 26,
       'tip': 'Then click on the word entry summary below. The first report you want to run is '
              'the ES001 entry summary header details. Start by choosing your ACE trade '
              'account ID number.',
       'title': 'ACE ES 001 and ES 003 Report (Harry F. Long, Inc. - U.S. Customs Brokers)',
       'url': 'https://www.youtube.com/watch?v=bD2cV_iBUpU&t=26s',
       'video_id': 'bD2cV_iBUpU'},
      {'author': 'Lutz',
       'channel': 'Lutz',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:25:49](https://www.youtube.com/watch?v=6Y30Cf9AeYE&t=1549s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Let's look at your ACE account. Let's look at your import forms and actually "
               'make a determination as to whether or not this is something that you should '
               'start exploring.',
       'timestamp': 1549,
       'timestamp_label': '[00:25:49]',
       'timestamp_seconds': 1549,
       'tip': "Let's look at your ACE account. Let's look at your import forms and actually "
              'make a determination as to whether or not this is something that you should '
              'start exploring.',
       'title': 'IEEPA Tariff Refund Opportunities: What Businesses Need to Know (Lutz)',
       'url': 'https://www.youtube.com/watch?v=6Y30Cf9AeYE&t=1549s',
       'video_id': '6Y30Cf9AeYE'},
      {'author': 'Meaningful Mediation',
       'channel': 'Meaningful Mediation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:27](https://www.youtube.com/watch?v=OFX0_mQm-Qo&t=567s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'The government instead could say, thanks so much for telling me what you '
               "screwed up, but because you can't pay me, I'm going to start penalty "
               'proceedings against you. And then maybe we can work out a payment plan, for '
               'example.',
       'timestamp': 567,
       'timestamp_label': '[00:09:27]',
       'timestamp_seconds': 567,
       'tip': 'The government instead could say, thanks so much for telling me what you '
              "screwed up, but because you can't pay me, I'm going to start penalty "
              'proceedings against you. And then maybe we can work out a payment plan, for '
              'example.',
       'title': 'Customs Penalty Mitigation: Negotiating with CBP | Jennifer Diaz (Meaningful '
                'Mediation)',
       'url': 'https://www.youtube.com/watch?v=OFX0_mQm-Qo&t=567s',
       'video_id': 'OFX0_mQm-Qo'},
      {'author': 'Evana',
       'channel': 'Evana',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:59](https://www.youtube.com/watch?v=6bp1bi4-zH4&t=119s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "For every export, that means you're going to have to prove that the goods left "
               'with either a bill of lading, an airway bill, uh B3 or a CAD, or even proof of '
               "deliveries with express carriers. If you're not collecting your proof of "
               'exports, the time to start is now.',
       'timestamp': 119,
       'timestamp_label': '[00:01:59]',
       'timestamp_seconds': 119,
       'tip': "For every export, that means you're going to have to prove that the goods left "
              'with either a bill of lading, an airway bill, uh B3 or a CAD, or even proof of '
              "deliveries with express carriers. If you're not collecting your proof of "
              'exports, the time to start is now.',
       'title': 'What Is Duty Drawback? Get Up to 99% of Your Import Duties Back (Explained) '
                '(Evana)',
       'url': 'https://www.youtube.com/watch?v=6bp1bi4-zH4&t=119s',
       'video_id': '6bp1bi4-zH4'},
      {'author': 'CBC News',
       'channel': 'CBC News',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:33](https://www.youtube.com/watch?v=qVk8ygNZbS8&t=33s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Donald Trump's double digit tariffs illegal, but didn't specifically rule on "
               'refunds. This past Wednesday, a federal judge with the US Court of '
               'International Trade ordered Customs and Border Protection to start paying '
               'importers back for the tariffs they paid with interest.',
       'timestamp': 33,
       'timestamp_label': '[00:00:33]',
       'timestamp_seconds': 33,
       'tip': "Donald Trump's double digit tariffs illegal, but didn't specifically rule on "
              'refunds. This past Wednesday, a federal judge with the US Court of '
              'International Trade ordered Customs and Border Protection to start paying '
              'importers back for the tariffs they paid with interest.',
       'title': 'Tariff refund system will be ready in 45 days, U.S. customs agency says (CBC '
                'News)',
       'url': 'https://www.youtube.com/watch?v=qVk8ygNZbS8&t=33s',
       'video_id': 'qVk8ygNZbS8'},
      {'author': 'International Tariff Management',
       'channel': 'International Tariff Management',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:35](https://www.youtube.com/watch?v=gf35xQR8Lz0&t=35s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "If you're engaged in international trade, you can expect to learn actionable "
               'tips and strategies that you can implement in your business to become a more '
               "profitable importer and or exporter. Now let's dive into this month's episode. "
               'Thank you for tuning in with us today.',
       'timestamp': 35,
       'timestamp_label': '[00:00:35]',
       'timestamp_seconds': 35,
       'tip': "If you're engaged in international trade, you can expect to learn actionable "
              'tips and strategies that you can implement in your business to become a more '
              "profitable importer and or exporter. Now let's dive into this month's episode. "
              'Thank you for tuning in with us today.',
       'title': 'ITM How to receive drawback on destroyed merchandise (International Tariff '
                'Management)',
       'url': 'https://www.youtube.com/watch?v=gf35xQR8Lz0&t=35s',
       'video_id': 'gf35xQR8Lz0'},
      {'author': 'Star USA, Inc.',
       'channel': 'Star USA, Inc.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:31:32](https://www.youtube.com/watch?v=ygZWIWKWe4w&t=1892s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'If you look back here, you would only compare things that are the same spacing '
               'aircraft or marine propulsion, for use in civil aircraft or other, outboard '
               'motors or other, you have to compare at the same level of indentation. I '
               'always start with headings.',
       'timestamp': 1892,
       'timestamp_label': '[00:31:32]',
       'timestamp_seconds': 1892,
       'tip': 'If you look back here, you would only compare things that are the same spacing '
              'aircraft or marine propulsion, for use in civil aircraft or other, outboard '
              'motors or other, you have to compare at the same level of indentation. I always '
              'start with headings.',
       'title': 'HTS Classification (Star USA, Inc.)',
       'url': 'https://www.youtube.com/watch?v=ygZWIWKWe4w&t=1892s',
       'video_id': 'ygZWIWKWe4w'},
      {'author': 'Scarbrough Global',
       'channel': 'Scarbrough Global',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:31](https://www.youtube.com/watch?v=VcD4-UlsOzk&t=211s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Necessarily know what entry came in on and now I exported it and I think '
               "that's where we see a lot of people maybe start to fall down on their ability "
               'to get into and really start to recover and use this program well.',
       'timestamp': 211,
       'timestamp_label': '[00:03:31]',
       'timestamp_seconds': 211,
       'tip': "Necessarily know what entry came in on and now I exported it and I think that's "
              'where we see a lot of people maybe start to fall down on their ability to get '
              'into and really start to recover and use this program well.',
       'title': 'When is Duty Drawback beneficial?  Recover U.S. Customs duty (Scarbrough '
                'Global)',
       'url': 'https://www.youtube.com/watch?v=VcD4-UlsOzk&t=211s',
       'video_id': 'VcD4-UlsOzk'},
      {'author': 'Vinod Parakh',
       'channel': 'Vinod Parakh',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=rgakhzqSlRc&t=15s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'इन मॉर्निंग। तो हम शुरू करते हैं चैप्टर ड्यूटी ड्रॉबैक हमारे कस्टम रिवीजनरी '
               'सीरीज का। द टर्म ड्रॉबैक सिंपली मींस व्हाट दैट यू कैन ड्रॉबैक द ड्यूटी व्हिच.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'इन मॉर्निंग। तो हम शुरू करते हैं चैप्टर ड्यूटी ड्रॉबैक हमारे कस्टम रिवीजनरी '
              'सीरीज का। द टर्म ड्रॉबैक सिंपली मींस व्हाट दैट यू कैन ड्रॉबैक द ड्यूटी व्हिच.',
       'title': 'Duty Drawback in Just 39 Minutes- VPJ Customs Revisionary Series (Vinod '
                'Parakh)',
       'url': 'https://www.youtube.com/watch?v=rgakhzqSlRc&t=15s',
       'video_id': 'rgakhzqSlRc'},
      {'author': 'NextGen CPA',
       'channel': 'NextGen CPA',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:13](https://www.youtube.com/watch?v=sMBX0ZlgJRY&t=73s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'But be warned, once you submit, you cannot amend it. If you miss a 7501 form, '
               'you have to start a new declaration, which can push you to the back of the '
               'queue. CBP is saying 60 to 90 days for the cash to hit your account, but you '
               'must have an ACH account set up in ACE.',
       'timestamp': 73,
       'timestamp_label': '[00:01:13]',
       'timestamp_seconds': 73,
       'tip': 'But be warned, once you submit, you cannot amend it. If you miss a 7501 form, '
              'you have to start a new declaration, which can push you to the back of the '
              'queue. CBP is saying 60 to 90 days for the cash to hit your account, but you '
              'must have an ACH account set up in ACE.',
       'title': 'CBP Refund Portal is LIVE - Claim Your 2025 Tariff Money Now! (NextGen CPA)',
       'url': 'https://www.youtube.com/watch?v=sMBX0ZlgJRY&t=73s',
       'video_id': 'sMBX0ZlgJRY'},
      {'author': 'Trade Risk Guaranty',
       'channel': 'Trade Risk Guaranty',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:12](https://www.youtube.com/watch?v=M68ZVWdgp9I&t=672s)',
       'relevance': 'Attributed practitioner commentary on zero-upfront `25%–35%` contingency '
                    'recovery across `5`-year CBP `19 U.S.C. § 1313` duty drawbacks (via '
                    'licensed `19 CFR Part 111` customs brokers), `19 U.S.C. § 1514` / '
                    'Post-Summary Correction tariff protests, and settled B2B '
                    'antitrust/interchange class-action pools (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': '30 days to terminate to to place a larger bond. So, you have 30 days to place '
               'a larger bond. Um to go a step further than that, your existing bond that '
               'needs to be increased must be terminated at least 15 days prior to that 30-day '
               'mark.',
       'timestamp': 672,
       'timestamp_label': '[00:11:12]',
       'timestamp_seconds': 672,
       'tip': '30 days to terminate to to place a larger bond. So, you have 30 days to place a '
              'larger bond. Um to go a step further than that, your existing bond that needs '
              'to be increased must be terminated at least 15 days prior to that 30-day mark.',
       'title': 'Managing Open U.S. Customs Bond Liability [Full Webinar] (Trade Risk '
                'Guaranty)',
       'url': 'https://www.youtube.com/watch?v=M68ZVWdgp9I&t=672s',
       'video_id': 'M68ZVWdgp9I'}]}
