"""Curated 180-citation Government Contract Brokering baseline (15 per chapter across Q1-Q12) mined strictly from verified Government Contract Brokering YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'219',
     'acquisition',
     'acquisitions',
     'act',
     'affiliation',
     'agency',
     'agreement',
     'area',
     'aside',
     'avoiding',
     'award',
     'bid',
     'boards',
     'bona',
     'brokering',
     'building',
     'business',
     'cage',
     'capability',
     'capital',
     'client',
     'clients',
     'code',
     'commercial',
     'compliance',
     'compliant',
     'contingent',
     'contracting',
     'contracts',
     'cooperative',
     'derek',
     'desk',
     'destination',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'219',
     'acquisition',
     'acquisitions',
     'act',
     'affiliation',
     'agency',
     'agreement',
     'area',
     'aside',
     'avoiding',
     'award',
     'bid',
     'boards',
     'bona',
     'brokering',
     'budget',
     'building',
     'buyer',
     'cage',
     'capability',
     'capital',
     'code',
     'commercial',
     'compliance',
     'compliant',
     'contingent',
     'contract',
     'contracting',
     'contracts',
     'cooperative',
     'customer',
     'decision',
     'derek',
     'desk',
     'destination',
     'escrow',
     'fee',
     'fees',
     'invoice',
     'pay',
     'payment',
     'pays',
     'retainer'},
 3: {'219',
     'acquisition',
     'acquisitions',
     'act',
     'affiliation',
     'agency',
     'agreement',
     'area',
     'aside',
     'avoiding',
     'award',
     'bid',
     'boards',
     'bona',
     'brokering',
     'building',
     'cage',
     'capability',
     'capital',
     'cash',
     'cashflow',
     'code',
     'commercial',
     'commission',
     'compliance',
     'compliant',
     'contingent',
     'contracting',
     'contracts',
     'cooperative',
     'cost',
     'costs',
     'derek',
     'desk',
     'destination',
     'economics',
     'margin',
     'margins',
     'price',
     'pricing',
     'profit',
     'roi',
     'unit'},
 4: {'219',
     'acquisition',
     'acquisitions',
     'act',
     'affiliation',
     'agency',
     'agreement',
     'area',
     'aside',
     'avoiding',
     'award',
     'bid',
     'boards',
     'bona',
     'brokering',
     'budget',
     'building',
     'cage',
     'capability',
     'capital',
     'code',
     'commercial',
     'compliance',
     'compliant',
     'contingent',
     'contracting',
     'contracts',
     'cooperative',
     'derek',
     'desk',
     'destination',
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
 5: {'219',
     'acquisition',
     'acquisitions',
     'act',
     'affiliation',
     'agency',
     'agreement',
     'area',
     'aside',
     'audit',
     'avoid',
     'avoiding',
     'award',
     'bid',
     'boards',
     'bona',
     'brokering',
     'building',
     'cage',
     'capability',
     'capital',
     'clawback',
     'code',
     'commercial',
     'compliance',
     'compliant',
     'contingent',
     'contracting',
     'contracts',
     'cooperative',
     'derek',
     'desk',
     'destination',
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
 6: {'219',
     'acquisition',
     'acquisitions',
     'act',
     'affiliation',
     'agency',
     'agreement',
     'area',
     'aside',
     'avoiding',
     'award',
     'bid',
     'boards',
     'bona',
     'brokering',
     'building',
     'cage',
     'capability',
     'capital',
     'client',
     'code',
     'commercial',
     'compliance',
     'compliant',
     'contingent',
     'contracting',
     'contracts',
     'cooperative',
     'data',
     'deal',
     'derek',
     'desk',
     'destination',
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
 7: {'219',
     'acquisition',
     'acquisitions',
     'act',
     'affiliation',
     'agency',
     'agreement',
     'area',
     'aside',
     'avoiding',
     'award',
     'bid',
     'boards',
     'bona',
     'brokering',
     'building',
     'cage',
     'capability',
     'capital',
     'checklist',
     'code',
     'commercial',
     'compliance',
     'compliant',
     'contingent',
     'contracting',
     'contracts',
     'cooperative',
     'delivery',
     'derek',
     'desk',
     'destination',
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
 8: {'219',
     'acquisition',
     'acquisitions',
     'act',
     'affiliation',
     'agency',
     'agreement',
     'api',
     'area',
     'aside',
     'avoiding',
     'award',
     'bid',
     'boards',
     'bona',
     'brokering',
     'building',
     'cage',
     'capability',
     'capital',
     'code',
     'commercial',
     'compliance',
     'compliant',
     'contingent',
     'contracting',
     'contracts',
     'cooperative',
     'crm',
     'data',
     'database',
     'derek',
     'desk',
     'destination',
     'platform',
     'portal',
     'scraper',
     'search',
     'software',
     'tool',
     'tools',
     'tracking'},
 9: {'219',
     'acquisition',
     'acquisitions',
     'act',
     'affiliation',
     'agency',
     'agreement',
     'area',
     'aside',
     'avoiding',
     'award',
     'bid',
     'boards',
     'bona',
     'brokering',
     'building',
     'cage',
     'capability',
     'capital',
     'code',
     'commercial',
     'compliance',
     'compliant',
     'contingent',
     'contract',
     'contracting',
     'contracts',
     'cooperative',
     'derek',
     'desk',
     'destination',
     'disclosure',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'219',
      'acquisition',
      'acquisitions',
      'act',
      'affiliation',
      'agency',
      'agent',
      'agreement',
      'ai',
      'area',
      'aside',
      'automate',
      'automation',
      'avoiding',
      'award',
      'bid',
      'boards',
      'bona',
      'brokering',
      'building',
      'cage',
      'capability',
      'capital',
      'code',
      'commercial',
      'compliance',
      'compliant',
      'contingent',
      'contracting',
      'contracts',
      'cooperative',
      'dashboard',
      'derek',
      'desk',
      'destination',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'219',
      'acquisition',
      'acquisitions',
      'act',
      'affiliation',
      'agency',
      'agreement',
      'area',
      'aside',
      'avoiding',
      'award',
      'bid',
      'boards',
      'bona',
      'brokering',
      'building',
      'cage',
      'capability',
      'capital',
      'code',
      'commercial',
      'compliance',
      'compliant',
      'contingent',
      'contracting',
      'contractor',
      'contracts',
      'cooperative',
      'derek',
      'desk',
      'destination',
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
 12: {'219',
      'acquisition',
      'acquisitions',
      'act',
      'action',
      'affiliation',
      'agency',
      'agreement',
      'area',
      'aside',
      'avoiding',
      'award',
      'bid',
      'boards',
      'bona',
      'brokering',
      'building',
      'cage',
      'capability',
      'capital',
      'code',
      'commercial',
      'compliance',
      'compliant',
      'contingent',
      'contracting',
      'contracts',
      'cooperative',
      'day',
      'days',
      'derek',
      'desk',
      'destination',
      'launch',
      'milestone',
      'month',
      'plan',
      'roadmap',
      'sprint',
      'start',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'FedOpp',
      'channel': 'FedOpp',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:41](https://www.youtube.com/watch?v=bTlxn6BVHJ0&t=101s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Set aside narrows the list to small business, HUBZone, service disabled '
              'veteran, and other set asides. Status and due lets you show open quotes or ones '
              'due soon. MSC filters by the acquisition method suffix code.',
      'timestamp': 101,
      'timestamp_label': '[00:01:41]',
      'timestamp_seconds': 101,
      'tip': 'Set aside narrows the list to small business, HUBZone, service disabled veteran, '
             'and other set asides. Status and due lets you show open quotes or ones due soon. '
             'MSC filters by the acquisition method suffix code.',
      'title': 'How to Find DIBBS RFQs on the DLA Bid Board by FSC, NSN and Due Date (FedOpp)',
      'url': 'https://www.youtube.com/watch?v=bTlxn6BVHJ0&t=101s',
      'video_id': 'bTlxn6BVHJ0'},
     {'author': 'Squared Compass',
      'channel': 'Squared Compass',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:08](https://www.youtube.com/watch?v=IXmVYXIEfdQ&t=188s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That is where the Government starts asking a simple question. Are we paying for '
              'value, or are we paying for air? Model four is the Set-aside Front. A small '
              'business prime is used mainly to access a set-aside contract while another '
              'company performs the primary and vital work.',
      'timestamp': 188,
      'timestamp_label': '[00:03:08]',
      'timestamp_seconds': 188,
      'tip': 'That is where the Government starts asking a simple question. Are we paying for '
             'value, or are we paying for air? Model four is the Set-aside Front. A small '
             'business prime is used mainly to access a set-aside contract while another '
             'company performs the primary and vital work.',
      'title': '4 Middleman Models in Government Contracting | Which Triggers DOJ Scrutiny? '
               '(Squared Compass)',
      'url': 'https://www.youtube.com/watch?v=IXmVYXIEfdQ&t=188s',
      'video_id': 'IXmVYXIEfdQ'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:54](https://www.youtube.com/watch?v=R-2hdJLvKUM&t=1314s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you're awarded a simplified acquisition at the small business set-aside, the "
              'FAR instructs the contracting officer, "Don\'t put that in there." The The '
              "clause belongs doesn't belong in that contract. And so you shouldn't see the "
              'clause, which is FAR 52.',
      'timestamp': 1314,
      'timestamp_label': '[00:21:54]',
      'timestamp_seconds': 1314,
      'tip': "If you're awarded a simplified acquisition at the small business set-aside, the "
             'FAR instructs the contracting officer, "Don\'t put that in there." The The '
             "clause belongs doesn't belong in that contract. And so you shouldn't see the "
             'clause, which is FAR 52.',
      'title': 'How to Make Money with Middleman Strategy in 2026 The Legal Way (Kizzy Parks)',
      'url': 'https://www.youtube.com/watch?v=R-2hdJLvKUM&t=1314s',
      'video_id': 'R-2hdJLvKUM'},
     {'author': 'PilieroMazza PLLC',
      'channel': 'PilieroMazza PLLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:33:21](https://www.youtube.com/watch?v=qxE-37z0qfw&t=2001s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Limitations and subcontracting do not apply for small business set-aside '
              'contracts between the micro purchase threshold and the simplified acquisition.',
      'timestamp': 2001,
      'timestamp_label': '[00:33:21]',
      'timestamp_seconds': 2001,
      'tip': 'Limitations and subcontracting do not apply for small business set-aside '
             'contracts between the micro purchase threshold and the simplified acquisition.',
      'title': 'Limitations on Subcontracting New Rules (PilieroMazza PLLC)',
      'url': 'https://www.youtube.com/watch?v=qxE-37z0qfw&t=2001s',
      'video_id': 'qxE-37z0qfw'},
     {'author': 'SamSearch - AI for Government Contracting',
      'channel': 'SamSearch - AI for Government Contracting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:03](https://www.youtube.com/watch?v=PPOCeCEkaBk&t=183s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, you can go to this calculator. It's called size standard tool and you go "
              'and answer the questions to see if you qualify as a small business for '
              'government contracting purposes. You start, you just type in your NAK code.',
      'timestamp': 183,
      'timestamp_label': '[00:03:03]',
      'timestamp_seconds': 183,
      'tip': "So, you can go to this calculator. It's called size standard tool and you go and "
             'answer the questions to see if you qualify as a small business for government '
             'contracting purposes. You start, you just type in your NAK code.',
      'title': 'Government Set Aside Contracts for Small Businesses (SamSearch - AI for '
               'Government Contracting)',
      'url': 'https://www.youtube.com/watch?v=PPOCeCEkaBk&t=183s',
      'video_id': 'PPOCeCEkaBk'},
     {'author': 'GovKidMethod',
      'channel': 'GovKidMethod',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:33](https://www.youtube.com/watch?v=xXM1cyLQ_jY&t=513s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Veterans you know i talked to so many of you derek okay i'm out of the service "
              'i want to start my own business or hey i already have a business or i want to.',
      'timestamp': 513,
      'timestamp_label': '[00:08:33]',
      'timestamp_seconds': 513,
      'tip': "Veterans you know i talked to so many of you derek okay i'm out of the service i "
             'want to start my own business or hey i already have a business or i want to.',
      'title': 'When to REALLY Apply For Federal Contracting Set-Asides like 8a, WOSB, HUBZone '
               'and SDVOSB (GovKidMethod)',
      'url': 'https://www.youtube.com/watch?v=xXM1cyLQ_jY&t=513s',
      'video_id': 'xXM1cyLQ_jY'},
     {'author': 'Neil McDonnell',
      'channel': 'Neil McDonnell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:20](https://www.youtube.com/watch?v=9sogImn1jJQ&t=140s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Restaurants and hair salons, real estate offices, real estate sales people '
              'individually might be a business with a couple of people working for them. '
              'Small construction companies, people who serve the the education market, the '
              'commercial market.',
      'timestamp': 140,
      'timestamp_label': '[00:02:20]',
      'timestamp_seconds': 140,
      'tip': 'Restaurants and hair salons, real estate offices, real estate sales people '
             'individually might be a business with a couple of people working for them. Small '
             'construction companies, people who serve the the education market, the '
             'commercial market.',
      'title': 'Intro to the 4 Small Business Programs in Federal Contracting | WOSB, SDVOSB, '
               '8(a), HUBZone (Neil McDonnell)',
      'url': 'https://www.youtube.com/watch?v=9sogImn1jJQ&t=140s',
      'video_id': '9sogImn1jJQ'},
     {'author': 'Win Government Contracts with GovSuccess',
      'channel': 'Win Government Contracts with GovSuccess',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:24](https://www.youtube.com/watch?v=LgX6N2c9-S4&t=24s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Registration requirements have exceptions. Registration alone is not evidence '
              'that a business is ready to perform every contract. Before applying this to a '
              "real acquisition, check the current FAR, the agency's applicable deviation, and "
              'the solicitation or contract.',
      'timestamp': 24,
      'timestamp_label': '[00:00:24]',
      'timestamp_seconds': 24,
      'tip': 'Registration requirements have exceptions. Registration alone is not evidence '
             'that a business is ready to perform every contract. Before applying this to a '
             "real acquisition, check the current FAR, the agency's applicable deviation, and "
             'the solicitation or contract.',
      'title': 'FAR PART 4 (Simplified) | Treat Registration and Contract Data as Operating '
               'Controls (Win Government Contracts with GovSuccess)',
      'url': 'https://www.youtube.com/watch?v=LgX6N2c9-S4&t=24s',
      'video_id': 'LgX6N2c9-S4'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=GA5_o6kPhnw&t=15s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Statement I know small business administration maybe Apex maybe even a '
              "government agency said to you where's your capability don't you have a.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Statement I know small business administration maybe Apex maybe even a '
             "government agency said to you where's your capability don't you have a.",
      'title': 'How To Write A Winning Capability Statement For Government Contracting (Kizzy '
               'Parks)',
      'url': 'https://www.youtube.com/watch?v=GA5_o6kPhnw&t=15s',
      'video_id': 'GA5_o6kPhnw'},
     {'author': 'Neil McDonnell',
      'channel': 'Neil McDonnell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:22](https://www.youtube.com/watch?v=4poj2n7iLrs&t=262s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Build your business and so that's what we're going to be talking about today "
              "okay so let's get more Federal uh set aside contracts and by the way so I said.",
      'timestamp': 262,
      'timestamp_label': '[00:04:22]',
      'timestamp_seconds': 262,
      'tip': "Build your business and so that's what we're going to be talking about today "
             "okay so let's get more Federal uh set aside contracts and by the way so I said.",
      'title': 'How To Get More Set Asides for WOSBs, SDVOSBs, and HUBZone Small Businesses '
               '(Neil McDonnell)',
      'url': 'https://www.youtube.com/watch?v=4poj2n7iLrs&t=262s',
      'video_id': '4poj2n7iLrs'},
     {'author': 'Tris10 @ MeND',
      'channel': 'Tris10 @ MeND',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=JE_OOJ3NAVk&t=15s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Find the right suppliers to win more government contracts now many of the '
              'clients that we work one of the biggest problems they initially have is they.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Find the right suppliers to win more government contracts now many of the '
             'clients that we work one of the biggest problems they initially have is they.',
      'title': 'Find the Right Supplier - DLA / DIBBS Government Contracting (Tris10 @ MeND)',
      'url': 'https://www.youtube.com/watch?v=JE_OOJ3NAVk&t=15s',
      'video_id': 'JE_OOJ3NAVk'},
     {'author': 'Keck Legal, LLC',
      'channel': 'Keck Legal, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:15](https://www.youtube.com/watch?v=x1-UtiYGpVc&t=375s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "One of the ways uh that that's very helpful to a lot of my clients is is a "
              "chapter 11 filing for the business or personally a lot of people don't realize "
              'that oh I thought chapter 11 was for big corporations.',
      'timestamp': 375,
      'timestamp_label': '[00:06:15]',
      'timestamp_seconds': 375,
      'tip': "One of the ways uh that that's very helpful to a lot of my clients is is a "
             "chapter 11 filing for the business or personally a lot of people don't realize "
             'that oh I thought chapter 11 was for big corporations.',
      'title': 'How to Fight the SBA: Stop Collections on Your EIDL Loan (Keck Legal, LLC)',
      'url': 'https://www.youtube.com/watch?v=x1-UtiYGpVc&t=375s',
      'video_id': 'x1-UtiYGpVc'},
     {'author': 'FDIC International',
      'channel': 'FDIC International',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:27](https://www.youtube.com/watch?v=511aPYJ9WjI&t=207s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They can reach us at 87758 5976 that's our service line uh they could visit the "
              'website sourcewell mn.gov well my thanks to all my guests today again this has '
              'been Chris mclone at FDIC International 2023 have a good one and stay safe.',
      'timestamp': 207,
      'timestamp_label': '[00:03:27]',
      'timestamp_seconds': 207,
      'tip': "They can reach us at 87758 5976 that's our service line uh they could visit the "
             'website sourcewell mn.gov well my thanks to all my guests today again this has '
             'been Chris mclone at FDIC International 2023 have a good one and stay safe.',
      'title': 'Sourcewell Contracts: Offering Choice, Value & Time Savings (FDIC '
               'International)',
      'url': 'https://www.youtube.com/watch?v=511aPYJ9WjI&t=207s',
      'video_id': '511aPYJ9WjI'},
     {'author': 'Centurion Research Solutions',
      'channel': 'Centurion Research Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:47](https://www.youtube.com/watch?v=L-BpgTTiESM&t=287s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Contract to one or more of these categories these requirements will benefit '
              'your company if you are a small business or drive your teaming and vendor '
              'selection strategy if you are a midsize or large company.',
      'timestamp': 287,
      'timestamp_label': '[00:04:47]',
      'timestamp_seconds': 287,
      'tip': 'Contract to one or more of these categories these requirements will benefit your '
             'company if you are a small business or drive your teaming and vendor selection '
             'strategy if you are a midsize or large company.',
      'title': 'How to Successfully Navigate the World of Teaming and Subcontracting '
               '(Centurion Research Solutions)',
      'url': 'https://www.youtube.com/watch?v=L-BpgTTiESM&t=287s',
      'video_id': 'L-BpgTTiESM'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:28](https://www.youtube.com/watch?v=ol1KkwjDTqg&t=268s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Paying a company to register my flagship business into all of the supply '
              'directories of these huge government contracting firms yes I did I sure did and '
              'guess what guess how many contracts that led phone calls meetings.',
      'timestamp': 268,
      'timestamp_label': '[00:04:28]',
      'timestamp_seconds': 268,
      'tip': 'Paying a company to register my flagship business into all of the supply '
             'directories of these huge government contracting firms yes I did I sure did and '
             'guess what guess how many contracts that led phone calls meetings.',
      'title': 'Teaming In Government Contracting | Government Contracts (Kizzy Parks)',
      'url': 'https://www.youtube.com/watch?v=ol1KkwjDTqg&t=268s',
      'video_id': 'ol1KkwjDTqg'}],
 2: [{'author': 'Acquisition Pro Tips',
      'channel': 'Acquisition Pro Tips',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:19](https://www.youtube.com/watch?v=WXCymE9NjBg&t=319s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Two in one for services where invoice and receiving reports go together. '
              'Commercial invoice used with fast pay when allowed by the contract. Cost '
              'vouchers for cost reimbursement and labor hour contracts.',
      'timestamp': 319,
      'timestamp_label': '[00:05:19]',
      'timestamp_seconds': 319,
      'tip': 'Two in one for services where invoice and receiving reports go together. '
             'Commercial invoice used with fast pay when allowed by the contract. Cost '
             'vouchers for cost reimbursement and labor hour contracts.',
      'title': 'Ep. 2: Wide Area Workflow (WAWF) Explained | How to Invoice with the DoD & '
               'Avoid Rejections (Acquisition Pro Tips)',
      'url': 'https://www.youtube.com/watch?v=WXCymE9NjBg&t=319s',
      'video_id': 'WXCymE9NjBg'},
     {'author': "Don't Know Much About Construction",
      'channel': "Don't Know Much About Construction",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:34](https://www.youtube.com/watch?v=uUf-xLjfPf8&t=154s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This work and submitted an invoice right so according to the prompt payment act '
              'the federal agency is required to pay you within a specific time frame and.',
      'timestamp': 154,
      'timestamp_label': '[00:02:34]',
      'timestamp_seconds': 154,
      'tip': 'This work and submitted an invoice right so according to the prompt payment act '
             'the federal agency is required to pay you within a specific time frame and.',
      'title': 'The Prompt Payment Act exists to ensure quick payment to contractors and subs '
               "in federal projects. (Don't Know Much About Construction)",
      'url': 'https://www.youtube.com/watch?v=uUf-xLjfPf8&t=154s',
      'video_id': 'uUf-xLjfPf8'},
     {'author': 'Frank Reilly',
      'channel': 'Frank Reilly',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:15](https://www.youtube.com/watch?v=l13_GjjLw8g&t=135s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Successful performance of the contract or even upon receiving the contract '
              'award is not sufficient by itself to bring a fee agreement under the.',
      'timestamp': 135,
      'timestamp_label': '[00:02:15]',
      'timestamp_seconds': 135,
      'tip': 'Successful performance of the contract or even upon receiving the contract award '
             'is not sufficient by itself to bring a fee agreement under the.',
      'title': 'FAR Subpart 3.4 - Contingent Fees (Frank Reilly)',
      'url': 'https://www.youtube.com/watch?v=l13_GjjLw8g&t=135s',
      'video_id': 'l13_GjjLw8g'},
     {'author': 'Government Contract Blueprint',
      'channel': 'Government Contract Blueprint',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:52](https://www.youtube.com/watch?v=ZL3JyvzdhyE&t=352s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Micro purchases are still paid through the federal government's payment system, "
              'which can be slower than commercial work. You might invoice the agency and it '
              'could take 30, 60, or even 90 days to get paid.',
      'timestamp': 352,
      'timestamp_label': '[00:05:52]',
      'timestamp_seconds': 352,
      'tip': "Micro purchases are still paid through the federal government's payment system, "
             'which can be slower than commercial work. You might invoice the agency and it '
             'could take 30, 60, or even 90 days to get paid.',
      'title': 'How to Find Micro-Purchases on SAM.gov (Under $10,000 Without Bidding) '
               '(Government Contract Blueprint)',
      'url': 'https://www.youtube.com/watch?v=ZL3JyvzdhyE&t=352s',
      'video_id': 'ZL3JyvzdhyE'},
     {'author': 'Win Government Contracts with GovSuccess',
      'channel': 'Win Government Contracts with GovSuccess',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:36](https://www.youtube.com/watch?v=jTTWqhTfPMM&t=96s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Identify who receives the invoice, what makes it proper, and what evidence '
              'establishes acceptance. This lesson uses the codified FAR text displayed on '
              'Acquisition. Check the applicable agency deviation and your solicitation or '
              'contract before applying a section.',
      'timestamp': 96,
      'timestamp_label': '[00:01:36]',
      'timestamp_seconds': 96,
      'tip': 'Identify who receives the invoice, what makes it proper, and what evidence '
             'establishes acceptance. This lesson uses the codified FAR text displayed on '
             'Acquisition. Check the applicable agency deviation and your solicitation or '
             'contract before applying a section.',
      'title': 'FAR Part 32 (Simplified) | Check Payment Triggers Before Planning Cash Flow '
               '(Win Government Contracts with GovSuccess)',
      'url': 'https://www.youtube.com/watch?v=jTTWqhTfPMM&t=96s',
      'video_id': 'jTTWqhTfPMM'},
     {'author': 'Government Contracting Strategist & Host',
      'channel': 'Government Contracting Strategist & Host',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=-S6wZyOulKA&t=103s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Third, we're seeing a paper to digital record scanning contract with a $13,000 "
              'budget, which includes indexing and quality control. Record modernization '
              'remains active at the city and agency level.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': "Third, we're seeing a paper to digital record scanning contract with a $13,000 "
             'budget, which includes indexing and quality control. Record modernization '
             'remains active at the city and agency level.',
      'title': '5 State & Local Government Contracts You Can Bid on This Week | SLED '
               'Opportunities Breakdown (Government Contracting Strategist & Host)',
      'url': 'https://www.youtube.com/watch?v=-S6wZyOulKA&t=103s',
      'video_id': '-S6wZyOulKA'},
     {'author': 'Debra Smith',
      'channel': 'Debra Smith',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:40](https://www.youtube.com/watch?v=NusotbSsCa4&t=880s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So lenders trust the government POS because they're easier to approve and it "
              'guarantees that the government is going to pay on time. It also lets you take '
              'on bigger contracts without upfront capital, which is really nice to know.',
      'timestamp': 880,
      'timestamp_label': '[00:14:40]',
      'timestamp_seconds': 880,
      'tip': "So lenders trust the government POS because they're easier to approve and it "
             'guarantees that the government is going to pay on time. It also lets you take on '
             'bigger contracts without upfront capital, which is really nice to know.',
      'title': '3 Smart Ways to Fund Your Government Contract *Credit Cards, Factoring, & '
               'Purchase Orders* (Debra Smith)',
      'url': 'https://www.youtube.com/watch?v=NusotbSsCa4&t=880s',
      'video_id': 'NusotbSsCa4'},
     {'author': 'CO-',
      'channel': 'CO-',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:07](https://www.youtube.com/watch?v=C6VmvdA7JT4&t=67s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Either the borrower or then the fee to pay them has to come out of the bank the '
              'bank has to pay for it not the borrower and the company fees are set by.',
      'timestamp': 67,
      'timestamp_label': '[00:01:07]',
      'timestamp_seconds': 67,
      'tip': 'Either the borrower or then the fee to pay them has to come out of the bank the '
             'bank has to pay for it not the borrower and the company fees are set by.',
      'title': 'How to Avoid SBA Loan Scams (CO-)',
      'url': 'https://www.youtube.com/watch?v=C6VmvdA7JT4&t=67s',
      'video_id': 'C6VmvdA7JT4'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:46](https://www.youtube.com/watch?v=WR8VA1o3VMU&t=346s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Payment I think the most we've ever run on a government contract was right "
              "around $30,000 we've run contracts for a little less than 3,000 so those are.",
      'timestamp': 346,
      'timestamp_label': '[00:05:46]',
      'timestamp_seconds': 346,
      'tip': "Payment I think the most we've ever run on a government contract was right "
             "around $30,000 we've run contracts for a little less than 3,000 so those are.",
      'title': 'The Ultimate Government Contracting Guide for Beginners 2024 (Kizzy Parks)',
      'url': 'https://www.youtube.com/watch?v=WR8VA1o3VMU&t=346s',
      'video_id': 'WR8VA1o3VMU'},
     {'author': 'Mark Ryan',
      'channel': 'Mark Ryan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:55](https://www.youtube.com/watch?v=ne7XpEiLNKE&t=235s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Not the way it's going to be done it's been done on a contract year so you must "
              "be compliant every year of the contract additionally they're clarifying that "
              'if.',
      'timestamp': 235,
      'timestamp_label': '[00:03:55]',
      'timestamp_seconds': 235,
      'tip': "Not the way it's going to be done it's been done on a contract year so you must "
             "be compliant every year of the contract additionally they're clarifying that if.",
      'title': 'Limitations on Subcontracting Rule 13 C.F.R. § 125.6 Overview and Updates to '
               'the Regulations (Mark Ryan)',
      'url': 'https://www.youtube.com/watch?v=ne7XpEiLNKE&t=235s',
      'video_id': 'ne7XpEiLNKE'},
     {'author': 'Mobilization Capital',
      'channel': 'Mobilization Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=oOQSsJO94kM&t=92s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Could take a contract immobilization capital and get money up front you don't "
              "have to go through all the red tape it's a lot of red tape with you know your "
              "traditional banks you don't have to have those problems when you go into the "
              'mobilization capital.',
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': "Could take a contract immobilization capital and get money up front you don't "
             "have to go through all the red tape it's a lot of red tape with you know your "
             "traditional banks you don't have to have those problems when you go into the "
             'mobilization capital.',
      'title': 'Mobilization Capital Gov Contract Funding (Mobilization Capital)',
      'url': 'https://www.youtube.com/watch?v=oOQSsJO94kM&t=92s',
      'video_id': 'oOQSsJO94kM'},
     {'author': 'Scamverge',
      'channel': 'Scamverge',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:33](https://www.youtube.com/watch?v=7GhlupAi3Jg&t=93s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'When federal loan and grant money arrives, the school takes its tuition and '
              'fees, and the leftover money is paid out as a refund. In a legitimate case, '
              'that refund helps a real student pay for rent, books, or food.',
      'timestamp': 93,
      'timestamp_label': '[00:01:33]',
      'timestamp_seconds': 93,
      'tip': 'When federal loan and grant money arrives, the school takes its tuition and '
             'fees, and the leftover money is paid out as a refund. In a legitimate case, that '
             'refund helps a real student pay for rent, books, or food.',
      'title': 'OPERATION GHOSTBUSTERS — The $200 Million Ghost Student Fraud (Scamverge)',
      'url': 'https://www.youtube.com/watch?v=7GhlupAi3Jg&t=93s',
      'video_id': '7GhlupAi3Jg'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:28](https://www.youtube.com/watch?v=2GThNGqMOJQ&t=688s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You use AI, you don't use AI. If you miss any of these things I'm sharing with "
              "you, it's going to be a burden. And if you understand that, if this is clear, "
              'type yes. Number nine, I put pay, contract, agreement, or more. For number '
              "nine, here's how that works.",
      'timestamp': 688,
      'timestamp_label': '[00:11:28]',
      'timestamp_seconds': 688,
      'tip': "You use AI, you don't use AI. If you miss any of these things I'm sharing with "
             "you, it's going to be a burden. And if you understand that, if this is clear, "
             'type yes. Number nine, I put pay, contract, agreement, or more. For number nine, '
             "here's how that works.",
      'title': 'The Ultimate Guide to Middleman Contracting in 2025 | $0-$100k Guide (Kizzy '
               'Parks)',
      'url': 'https://www.youtube.com/watch?v=2GThNGqMOJQ&t=688s',
      'video_id': '2GThNGqMOJQ'},
     {'author': 'The Proposal Pro Coach',
      'channel': 'The Proposal Pro Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:33](https://www.youtube.com/watch?v=EesWMxgpXqk&t=273s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Asterisk make sure you fill it out don't have an asterisk leave it alone okay "
              "don't even touch it so once you put in your contract number you're going to "
              'click on next.',
      'timestamp': 273,
      'timestamp_label': '[00:04:33]',
      'timestamp_seconds': 273,
      'tip': "Asterisk make sure you fill it out don't have an asterisk leave it alone okay "
             "don't even touch it so once you put in your contract number you're going to "
             'click on next.',
      'title': 'Submitting Invoice In WAWF (The Proposal Pro Coach)',
      'url': 'https://www.youtube.com/watch?v=EesWMxgpXqk&t=273s',
      'video_id': 'EesWMxgpXqk'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:46:39](https://www.youtube.com/watch?v=RrDUfb8vNms&t=2799s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Stumbling blocks that someone getting into Government Contracting faces when '
              "they first start out is that usually when you're when you get a contract to.",
      'timestamp': 2799,
      'timestamp_label': '[00:46:39]',
      'timestamp_seconds': 2799,
      'tip': 'Stumbling blocks that someone getting into Government Contracting faces when '
             "they first start out is that usually when you're when you get a contract to.",
      'title': 'REAL Story Behind $300M Government Contract With David Packouz (Kizzy Parks)',
      'url': 'https://www.youtube.com/watch?v=RrDUfb8vNms&t=2799s',
      'video_id': 'RrDUfb8vNms'}],
 3: [{'author': 'The DLA Vendor Network (DVN)',
      'channel': 'The DLA Vendor Network (DVN)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:37:42](https://www.youtube.com/watch?v=jjX9klCZFKI&t=2262s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'NSN, who your plug is, all that good stuff. Let you know what your bid price '
              "was, what your profit margins were. It's just a fantastic tool to help you "
              'manage building your national stock number product catalog.',
      'timestamp': 2262,
      'timestamp_label': '[00:37:42]',
      'timestamp_seconds': 2262,
      'tip': 'NSN, who your plug is, all that good stuff. Let you know what your bid price '
             "was, what your profit margins were. It's just a fantastic tool to help you "
             'manage building your national stock number product catalog.',
      'title': 'TOP DLA Vendors Use DIBBS Batch Bidding to Win Big!🤯 (The DLA Vendor Network '
               '(DVN))',
      'url': 'https://www.youtube.com/watch?v=jjX9klCZFKI&t=2262s',
      'video_id': 'jjX9klCZFKI'},
     {'author': 'How To Sell To & Win Federal Government Contracts',
      'channel': 'How To Sell To & Win Federal Government Contracts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:53](https://www.youtube.com/watch?v=qWeiLfjB7k0&t=173s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Commercial 'ti determinations and pricing of commercial items and price "
              'reasonableness for commercial items and those are those are topics that are '
              "kind of a hot topic within commercial item contracting and we'll talk a little "
              'bit more about about those so next slide.',
      'timestamp': 173,
      'timestamp_label': '[00:02:53]',
      'timestamp_seconds': 173,
      'tip': "Commercial 'ti determinations and pricing of commercial items and price "
             'reasonableness for commercial items and those are those are topics that are kind '
             "of a hot topic within commercial item contracting and we'll talk a little bit "
             'more about about those so next slide.',
      'title': 'Government Contacting - FAR Part 12 - Acquisition Of Commercial Items - Win '
               'Federal Contracts (How To Sell To & Win Federal Government Contracts)',
      'url': 'https://www.youtube.com/watch?v=qWeiLfjB7k0&t=173s',
      'video_id': 'qWeiLfjB7k0'},
     {'author': 'Win Government Contracts with GovSuccess',
      'channel': 'Win Government Contracts with GovSuccess',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=i7_rrrRpotk&t=55s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A fixed-price award does not turn every expense into a separately reimbursable '
              'item. Pricing a modification and requesting reimbursement are different '
              'transactions, even when both involve cost information.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'A fixed-price award does not turn every expense into a separately reimbursable '
             'item. Pricing a modification and requesting reimbursement are different '
             'transactions, even when both involve cost information.',
      'title': 'FAR Part 31 (Simplified) | Support the Cost Before You Claim It (Win '
               'Government Contracts with GovSuccess)',
      'url': 'https://www.youtube.com/watch?v=i7_rrrRpotk&t=55s',
      'video_id': 'i7_rrrRpotk'},
     {'author': 'Neybor Consulting',
      'channel': 'Neybor Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:15](https://www.youtube.com/watch?v=TFl20T0yyig&t=555s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And cost type contracts are prohibited entirely under part 12. So when you '
              'propose, expect FFP and price accordingly. 3 covers the clauses you will see in '
              'every commercial solicitation. 212-1 212-1 instructions to offers. This is the '
              'streamlined set of submission rules.',
      'timestamp': 555,
      'timestamp_label': '[00:09:15]',
      'timestamp_seconds': 555,
      'tip': 'And cost type contracts are prohibited entirely under part 12. So when you '
             'propose, expect FFP and price accordingly. 3 covers the clauses you will see in '
             'every commercial solicitation. 212-1 212-1 instructions to offers. This is the '
             'streamlined set of submission rules.',
      'title': 'Neybor FAR Part12 (Neybor Consulting)',
      'url': 'https://www.youtube.com/watch?v=TFl20T0yyig&t=555s',
      'video_id': 'TFl20T0yyig'},
     {'author': 'Virtual 24-7',
      'channel': 'Virtual 24-7',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=yH2TsdfzuTM&t=157s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Many successful businesses do both. Finally, let's talk about price. It might "
              'be tempting to bid low just to win, but never price your bid below what it '
              'actually costs you to do the work.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': "Many successful businesses do both. Finally, let's talk about price. It might be "
             'tempting to bid low just to win, but never price your bid below what it actually '
             'costs you to do the work.',
      'title': 'Build a Winning Proposal | RFP vs RFQ vs RFI, Compliance Matrix & Pricing Your '
               'Bid (Virtual 24-7)',
      'url': 'https://www.youtube.com/watch?v=yH2TsdfzuTM&t=157s',
      'video_id': 'yH2TsdfzuTM'},
     {'author': 'Toledo Small Business Development Center',
      'channel': 'Toledo Small Business Development Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:44](https://www.youtube.com/watch?v=WqniKXcYJAw&t=44s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'An ifb an invitation to bid and an rfp which is a request for a proposal the '
              'contract types can be any of the following which include a fixed contract price '
              'an indefinite delivery contract time and material cost reimbursement or an '
              'incentive contract.',
      'timestamp': 44,
      'timestamp_label': '[00:00:44]',
      'timestamp_seconds': 44,
      'tip': 'An ifb an invitation to bid and an rfp which is a request for a proposal the '
             'contract types can be any of the following which include a fixed contract price '
             'an indefinite delivery contract time and material cost reimbursement or an '
             'incentive contract.',
      'title': "Responding to Government RFP's (Toledo Small Business Development Center)",
      'url': 'https://www.youtube.com/watch?v=WqniKXcYJAw&t=44s',
      'video_id': 'WqniKXcYJAw'},
     {'author': 'FedOpp',
      'channel': 'FedOpp',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:01](https://www.youtube.com/watch?v=bTs2wy13K1c&t=61s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Each NSN here is either one DL as bought before in your classes, or one with an '
              'open dibs RFQ right now. Parts with an open RFQ are listed first. The columns '
              'show the NSN, item name, FSC, approved source count, last award unit price, and '
              'open RFQ.',
      'timestamp': 61,
      'timestamp_label': '[00:01:01]',
      'timestamp_seconds': 61,
      'tip': 'Each NSN here is either one DL as bought before in your classes, or one with an '
             'open dibs RFQ right now. Parts with an open RFQ are listed first. The columns '
             'show the NSN, item name, FSC, approved source count, last award unit price, and '
             'open RFQ.',
      'title': 'Find DLA Parts to Quote by FSC Code: Open DIBBS RFQs in FedOpp (FedOpp)',
      'url': 'https://www.youtube.com/watch?v=bTs2wy13K1c&t=61s',
      'video_id': 'bTs2wy13K1c'},
     {'author': 'Sheenapreneur',
      'channel': 'Sheenapreneur',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:33](https://www.youtube.com/watch?v=B6uLsI5zZTQ&t=333s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They're just gonna Max it out at 250 000 that just means that the agency has a "
              'reasonable understanding of what the price would be for one million apples I.',
      'timestamp': 333,
      'timestamp_label': '[00:05:33]',
      'timestamp_seconds': 333,
      'tip': "They're just gonna Max it out at 250 000 that just means that the agency has a "
             'reasonable understanding of what the price would be for one million apples I.',
      'title': 'Government Contracting Made Easy: Simplified Acquisitions & Micro-Purchases '
               'for Beginners | GPC Card (Sheenapreneur)',
      'url': 'https://www.youtube.com/watch?v=B6uLsI5zZTQ&t=333s',
      'video_id': 'B6uLsI5zZTQ'},
     {'author': 'US Federal Contractor Registration',
      'channel': 'US Federal Contractor Registration',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=SpRIyXgvkg0&t=51s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you are a sole-source and you are putting a proposal together that's over $2 "
              'million, then you fall under FAR Part 15 table 15. 2 and that is a description '
              'of how you build certified cost or pricing data for a proposal.',
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': "If you are a sole-source and you are putting a proposal together that's over $2 "
             'million, then you fall under FAR Part 15 table 15. 2 and that is a description '
             'of how you build certified cost or pricing data for a proposal.',
      'title': 'Breakdown of FAR Part 12 & 15 | Selling Commercial Items or Non-Commercial '
               'Items to the Government (US Federal Contractor Registration)',
      'url': 'https://www.youtube.com/watch?v=SpRIyXgvkg0&t=51s',
      'video_id': 'SpRIyXgvkg0'},
     {'author': 'ExamPrepAI CPA Review',
      'channel': 'ExamPrepAI CPA Review',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=mZqOwnA0HbE&t=120s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's say that we sold these goods for $20,000. So we would do cash or AR for "
              "$20,000 we would do revenue for $20,000. But you're not going to sell it at "
              "break even at least you know hopefully you're not. So your your inventory cost "
              'of goods sold numbers will be different.',
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': "Let's say that we sold these goods for $20,000. So we would do cash or AR for "
             "$20,000 we would do revenue for $20,000. But you're not going to sell it at "
             "break even at least you know hopefully you're not. So your your inventory cost "
             'of goods sold numbers will be different.',
      'title': 'Title Transfer: FOB Shipping Point and FOB Destination - FAR Exam Prep '
               '(ExamPrepAI CPA Review)',
      'url': 'https://www.youtube.com/watch?v=mZqOwnA0HbE&t=120s',
      'video_id': 'mZqOwnA0HbE'},
     {'author': 'GovKidMethod',
      'channel': 'GovKidMethod',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:32](https://www.youtube.com/watch?v=wot0JsK9qCc&t=572s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Pricing they'll be in a mount there and sometimes they'll be it's called the "
              "Clin underneath it where you insert your price but right here they're telling "
              'us.',
      'timestamp': 572,
      'timestamp_label': '[00:09:32]',
      'timestamp_seconds': 572,
      'tip': "Pricing they'll be in a mount there and sometimes they'll be it's called the "
             "Clin underneath it where you insert your price but right here they're telling "
             'us.',
      'title': 'Government Contracts - Janitorial Services RFP Breakdown on FBO (GovKidMethod)',
      'url': 'https://www.youtube.com/watch?v=wot0JsK9qCc&t=572s',
      'video_id': 'wot0JsK9qCc'},
     {'author': 'Tris10 @ MeND',
      'channel': 'Tris10 @ MeND',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:29](https://www.youtube.com/watch?v=Z9MLGFqFXtM&t=389s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "There are 25 pages in The PDF and we've really been able just to extract just "
              'the most pertinent pieces of information needed that allows me to the bid on '
              'the contract and provide an actual price for that specific bid.',
      'timestamp': 389,
      'timestamp_label': '[00:06:29]',
      'timestamp_seconds': 389,
      'tip': "There are 25 pages in The PDF and we've really been able just to extract just "
             'the most pertinent pieces of information needed that allows me to the bid on the '
             'contract and provide an actual price for that specific bid.',
      'title': 'What Information to Extract in a DLA / DIBBS RFQs (Tris10 @ MeND)',
      'url': 'https://www.youtube.com/watch?v=Z9MLGFqFXtM&t=389s',
      'video_id': 'Z9MLGFqFXtM'},
     {'author': 'How To Sell To & Win Federal Government Contracts',
      'channel': 'How To Sell To & Win Federal Government Contracts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:19](https://www.youtube.com/watch?v=Tj7x3UDuOSE&t=979s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Requirements do not you know mess around with the margins and the font size or '
              "anything else stick to it comply with it if you're not in compliance excess "
              'pages will be dropped next.',
      'timestamp': 979,
      'timestamp_label': '[00:16:19]',
      'timestamp_seconds': 979,
      'tip': 'Requirements do not you know mess around with the margins and the font size or '
             "anything else stick to it comply with it if you're not in compliance excess "
             'pages will be dropped next.',
      'title': '2024:  FAR Part 15 - Contracting by Negotiation (How To Sell To & Win Federal '
               'Government Contracts)',
      'url': 'https://www.youtube.com/watch?v=Tj7x3UDuOSE&t=979s',
      'video_id': 'Tj7x3UDuOSE'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:34](https://www.youtube.com/watch?v=F6Hwh89ornQ&t=514s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Date that's all you got to do because then the next time you bid on something "
              "perhaps they can refer you out maybe they'll lower their price and at the end.",
      'timestamp': 514,
      'timestamp_label': '[00:08:34]',
      'timestamp_seconds': 514,
      'tip': "Date that's all you got to do because then the next time you bid on something "
             "perhaps they can refer you out maybe they'll lower their price and at the end.",
      'title': 'How to Master Subcontracting & Win Government Contracts in 2025 (Step by Step) '
               '(Kizzy Parks)',
      'url': 'https://www.youtube.com/watch?v=F6Hwh89ornQ&t=514s',
      'video_id': 'F6Hwh89ornQ'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:05](https://www.youtube.com/watch?v=iOVkNIsRYV4&t=845s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Place to respond this is my company uh solicitation blank for amusing their '
              'language required as requested um requested or you can say required and I would '
              'put in your pissy parks president your PC and you put your cage.',
      'timestamp': 845,
      'timestamp_label': '[00:14:05]',
      'timestamp_seconds': 845,
      'tip': 'Place to respond this is my company uh solicitation blank for amusing their '
             'language required as requested um requested or you can say required and I would '
             'put in your pissy parks president your PC and you put your cage.',
      'title': 'Bid As A MiddleMan - Full Walkthrough |  Kizzy Highlights #7 (Kizzy Parks)',
      'url': 'https://www.youtube.com/watch?v=iOVkNIsRYV4&t=845s',
      'video_id': 'iOVkNIsRYV4'}],
 4: [{'author': 'Eric Coffie',
      'channel': 'Eric Coffie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=wcz-GpTaAp8&t=62s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A commercial and government entity cage code is a five character ID number used '
              'extensively within the federal government it is assigned by the.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': 'A commercial and government entity cage code is a five character ID number used '
             'extensively within the federal government it is assigned by the.',
      'title': 'What is a CAGE Code | SAM Registration Help Desk | Start Government '
               'Contracting (Eric Coffie)',
      'url': 'https://www.youtube.com/watch?v=wcz-GpTaAp8&t=62s',
      'video_id': 'wcz-GpTaAp8'},
     {'author': 'The DLA Vendor Network (DVN)',
      'channel': 'The DLA Vendor Network (DVN)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:36:03](https://www.youtube.com/watch?v=MyfmHjDF9HI&t=2163s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Anything in in white you can pretty much scroll past. And again, that's more "
              'advanced training. Uh but you want to focus in on the yellow area. So the '
              'yellow areas of your bid, you\'re going to say, "Hey, we\'re bidding an exact '
              'match to that cage code, which is OJ uh YC2.',
      'timestamp': 2163,
      'timestamp_label': '[00:36:03]',
      'timestamp_seconds': 2163,
      'tip': "Anything in in white you can pretty much scroll past. And again, that's more "
             'advanced training. Uh but you want to focus in on the yellow area. So the yellow '
             'areas of your bid, you\'re going to say, "Hey, we\'re bidding an exact match to '
             'that cage code, which is OJ uh YC2.',
      'title': 'How to Win DLA Contracts: Live DIBBS Solicitation Review & Bid (The DLA Vendor '
               'Network (DVN))',
      'url': 'https://www.youtube.com/watch?v=MyfmHjDF9HI&t=2163s',
      'video_id': 'MyfmHjDF9HI'},
     {'author': 'Win Government Contracts with GovSuccess',
      'channel': 'Win Government Contracts with GovSuccess',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=IiWbsx5Iudg&t=79s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Consider a software provider responding to a commercial services request. The '
              'sales team wants to attach its standard subscription agreement. Contracts and '
              'technical staff first compare that agreement with the solicitation.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': 'Consider a software provider responding to a commercial services request. The '
             'sales team wants to attach its standard subscription agreement. Contracts and '
             'technical staff first compare that agreement with the solicitation.',
      'title': 'FAR Part 12 (Simplified) | Selling Commercial Products and Services (Win '
               'Government Contracts with GovSuccess)',
      'url': 'https://www.youtube.com/watch?v=IiWbsx5Iudg&t=79s',
      'video_id': 'IiWbsx5Iudg'},
     {'author': 'FedOpp',
      'channel': 'FedOpp',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:19](https://www.youtube.com/watch?v=2Bp78kNCVGI&t=319s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Use Renew Entity, and never request a second Unique Entity ID. The Unique '
              'Entity ID identifies your entity in federal award systems. The CAGE code '
              'identifies a location, and DLA systems like DIBBS use it. You need both to '
              'finish a DIBBS vendor account.',
      'timestamp': 319,
      'timestamp_label': '[00:05:19]',
      'timestamp_seconds': 319,
      'tip': 'Use Renew Entity, and never request a second Unique Entity ID. The Unique Entity '
             'ID identifies your entity in federal award systems. The CAGE code identifies a '
             'location, and DLA systems like DIBBS use it. You need both to finish a DIBBS '
             'vendor account.',
      'title': 'How to Register on SAM.gov: Login.gov, UEI and CAGE (Step by Step) | FedOpp '
               '(FedOpp)',
      'url': 'https://www.youtube.com/watch?v=2Bp78kNCVGI&t=319s',
      'video_id': '2Bp78kNCVGI'},
     {'author': 'NSBGCA',
      'channel': 'NSBGCA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:13](https://www.youtube.com/watch?v=ka1Q_JhjM8w&t=1273s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Establish internal controls. Don't wait for an audit to find out if your "
              'accounting system or cyber systems are compliant. Establishing written '
              'policies, implement implementing secure software and monitoring your own '
              'compliance continuously. Number three, train your staff.',
      'timestamp': 1273,
      'timestamp_label': '[00:21:13]',
      'timestamp_seconds': 1273,
      'tip': "Establish internal controls. Don't wait for an audit to find out if your "
             'accounting system or cyber systems are compliant. Establishing written policies, '
             'implement implementing secure software and monitoring your own compliance '
             'continuously. Number three, train your staff.',
      'title': 'Understanding FAR Compliance (NSBGCA)',
      'url': 'https://www.youtube.com/watch?v=ka1Q_JhjM8w&t=1273s',
      'video_id': 'ka1Q_JhjM8w'},
     {'author': 'Theodore Watson',
      'channel': 'Theodore Watson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=NP_UB6qiZhw&t=139s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Arrangements when it comes to federal government contracting to keep your '
              'contract or if you have grounds to challenge an award call our government '
              'contract lawyers at Watson & Associates LLC we help federal government '
              'contractors in all states.',
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': 'Arrangements when it comes to federal government contracting to keep your '
             'contract or if you have grounds to challenge an award call our government '
             'contract lawyers at Watson & Associates LLC we help federal government '
             'contractors in all states.',
      'title': 'Contractor Teaming Agreements (Theodore Watson)',
      'url': 'https://www.youtube.com/watch?v=NP_UB6qiZhw&t=139s',
      'video_id': 'NP_UB6qiZhw'},
     {'author': 'Court Files',
      'channel': 'Court Files',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:32](https://www.youtube.com/watch?v=-RjbcsAnouU&t=632s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Meanwhile, lawmakers are moving. In May, Minnesota set aside $3 million for '
              'software to detect and prevent ghost student fraud. In Washington, a bill '
              'called the No Aid for Ghost Students Act passed the House of Representatives in '
              'June.',
      'timestamp': 632,
      'timestamp_label': '[00:10:32]',
      'timestamp_seconds': 632,
      'tip': 'Meanwhile, lawmakers are moving. In May, Minnesota set aside $3 million for '
             'software to detect and prevent ghost student fraud. In Washington, a bill called '
             'the No Aid for Ghost Students Act passed the House of Representatives in June.',
      'title': "Operation Ghostbusters: 5 Charged in the 'Ghost Student' Financial Aid Fraud "
               '(Court Files)',
      'url': 'https://www.youtube.com/watch?v=-RjbcsAnouU&t=632s',
      'video_id': '-RjbcsAnouU'},
     {'author': 'SamSearch - AI for Government Contracting',
      'channel': 'SamSearch - AI for Government Contracting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:14](https://www.youtube.com/watch?v=RY7zan9X3oY&t=254s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Do this well I'm going to introduce to you uh Sam search. go which is the "
              'easiest Government Contracting software and you can search for both federal '
              'and.',
      'timestamp': 254,
      'timestamp_label': '[00:04:14]',
      'timestamp_seconds': 254,
      'tip': "Do this well I'm going to introduce to you uh Sam search. go which is the "
             'easiest Government Contracting software and you can search for both federal and.',
      'title': 'How to bid on City Government Contracts (SamSearch - AI for Government '
               'Contracting)',
      'url': 'https://www.youtube.com/watch?v=RY7zan9X3oY&t=254s',
      'video_id': 'RY7zan9X3oY'},
     {'author': 'US Federal Contractor Registration',
      'channel': 'US Federal Contractor Registration',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:53](https://www.youtube.com/watch?v=yFsBD592FN8&t=953s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Simplified acquisition look at how many offers received what is this one Julie '
              "says Microsoft below the line for DISA so it's some type of Microsoft software "
              'I would assume oh okay but one offer received.',
      'timestamp': 953,
      'timestamp_label': '[00:15:53]',
      'timestamp_seconds': 953,
      'tip': 'Simplified acquisition look at how many offers received what is this one Julie '
             "says Microsoft below the line for DISA so it's some type of Microsoft software I "
             'would assume oh okay but one offer received.',
      'title': 'HUBZone 8A WOSB SDVOSB WOSB DBE MBE GSA SAP DAPA FSS SUB Contracts John Wayne '
               'government contracts g (US Federal Contractor Registration)',
      'url': 'https://www.youtube.com/watch?v=yFsBD592FN8&t=953s',
      'video_id': 'yFsBD592FN8'},
     {'author': 'Neil McDonnell',
      'channel': 'Neil McDonnell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:48](https://www.youtube.com/watch?v=QIEmDXcWhSE&t=468s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'To go after all Awards which is what you want to do um it allows you to bid on '
              'contracts and other stuff and blah blah blah or sometimes people say financial.',
      'timestamp': 468,
      'timestamp_label': '[00:07:48]',
      'timestamp_seconds': 468,
      'tip': 'To go after all Awards which is what you want to do um it allows you to bid on '
             'contracts and other stuff and blah blah blah or sometimes people say financial.',
      'title': 'Journey to $1M as a New GovCon - Day 23 (SAM.gov Pre-Requisites and numbers - '
               'TIN/SSN/EIN/UEI/CAGE) (Neil McDonnell)',
      'url': 'https://www.youtube.com/watch?v=QIEmDXcWhSE&t=468s',
      'video_id': 'QIEmDXcWhSE'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:05](https://www.youtube.com/watch?v=9DngtysNXpA&t=125s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Small business set aside 5 April to 10 April. So that means by the time they '
              'issue the award, whoever wins this, you got to be ready to cook. This is not '
              'the time to say, "Well, I\'m busy because it\'s my kids\' birthday." Ladybull, '
              'I would love to have a retreat here.',
      'timestamp': 125,
      'timestamp_label': '[00:02:05]',
      'timestamp_seconds': 125,
      'tip': 'Small business set aside 5 April to 10 April. So that means by the time they '
             'issue the award, whoever wins this, you got to be ready to cook. This is not the '
             'time to say, "Well, I\'m busy because it\'s my kids\' birthday." Ladybull, I '
             'would love to have a retreat here.',
      'title': 'Middleman Contracting Will Make Millionaires in 2025 (Be One) (Kizzy Parks)',
      'url': 'https://www.youtube.com/watch?v=9DngtysNXpA&t=125s',
      'video_id': '9DngtysNXpA'},
     {'author': 'How To Sell To & Win Federal Government Contracts',
      'channel': 'How To Sell To & Win Federal Government Contracts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:33](https://www.youtube.com/watch?v=CbeDp1nctog&t=213s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sbirs uh which is I think a um um underrated uh Topic in Government Contracting '
              'so please join us those again are also complimentary the links.',
      'timestamp': 213,
      'timestamp_label': '[00:03:33]',
      'timestamp_seconds': 213,
      'tip': 'Sbirs uh which is I think a um um underrated uh Topic in Government Contracting '
             'so please join us those again are also complimentary the links.',
      'title': '2024: FAR Part 12 - Acquisition of Commercial Items (How To Sell To & Win '
               'Federal Government Contracts)',
      'url': 'https://www.youtube.com/watch?v=CbeDp1nctog&t=213s',
      'video_id': 'CbeDp1nctog'},
     {'author': 'FedAccess',
      'channel': 'FedAccess',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:03](https://www.youtube.com/watch?v=6X_5wgYeeDo&t=243s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Binding and the other big difference is that responding to an rfq is typically '
              'much less work than responding to an rfp rfqs are used more for smaller '
              'contracts.',
      'timestamp': 243,
      'timestamp_label': '[00:04:03]',
      'timestamp_seconds': 243,
      'tip': 'Binding and the other big difference is that responding to an rfq is typically '
             'much less work than responding to an rfp rfqs are used more for smaller '
             'contracts.',
      'title': 'RFP vs RFQ vs RFI  Explained! (FedAccess)',
      'url': 'https://www.youtube.com/watch?v=6X_5wgYeeDo&t=243s',
      'video_id': '6X_5wgYeeDo'},
     {'author': 'Provident',
      'channel': 'Provident',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:33](https://www.youtube.com/watch?v=V3qc9e4w-4M&t=1893s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now your solicitation documents and their contact information something that '
              "Provident has done that I think is really smart is they've created their own "
              "landing page on their own website we're navigating to that right.",
      'timestamp': 1893,
      'timestamp_label': '[00:31:33]',
      'timestamp_seconds': 1893,
      'tip': 'Now your solicitation documents and their contact information something that '
             "Provident has done that I think is really smart is they've created their own "
             "landing page on their own website we're navigating to that right.",
      'title': 'Sourcewell Cooperative Purchasing: Where RFP Means Ready For Purchase - '
               'Provident Webinar (Provident)',
      'url': 'https://www.youtube.com/watch?v=V3qc9e4w-4M&t=1893s',
      'video_id': 'V3qc9e4w-4M'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:39](https://www.youtube.com/watch?v=K_zNUytFOQo&t=579s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "As a PDF if you're meeting in person you can print it you can use a QR code "
              'whatever it is you desire just make sure the key information is there till next '
              'time everything is possible my amazing gov con winners.',
      'timestamp': 579,
      'timestamp_label': '[00:09:39]',
      'timestamp_seconds': 579,
      'tip': "As a PDF if you're meeting in person you can print it you can use a QR code "
             'whatever it is you desire just make sure the key information is there till next '
             'time everything is possible my amazing gov con winners.',
      'title': 'How To Write A Winning Capability Statement (Kizzy Parks)',
      'url': 'https://www.youtube.com/watch?v=K_zNUytFOQo&t=579s',
      'video_id': 'K_zNUytFOQo'}],
 5: [{'author': 'Public Contracting Institute (PCI)',
      'channel': 'Public Contracting Institute (PCI)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:51:46](https://www.youtube.com/watch?v=Gisvrg813kY&t=3106s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But it's all there, whether you want to take a case to the GAO or to the "
              'contracting officer in a bid protest or if you have a dispute how you start '
              "under the Contract Disputes Act of 1978. It's all laid out in far part 33.",
      'timestamp': 3106,
      'timestamp_label': '[00:51:46]',
      'timestamp_seconds': 3106,
      'tip': "But it's all there, whether you want to take a case to the GAO or to the "
             'contracting officer in a bid protest or if you have a dispute how you start '
             "under the Contract Disputes Act of 1978. It's all laid out in far part 33.",
      'title': 'GovCon 101   Federal Acquisition Regulation FAR (Public Contracting Institute '
               '(PCI))',
      'url': 'https://www.youtube.com/watch?v=Gisvrg813kY&t=3106s',
      'video_id': 'Gisvrg813kY'},
     {'author': 'SEMSCIO',
      'channel': 'SEMSCIO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:29](https://www.youtube.com/watch?v=rRWCLLWqrV0&t=29s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A valid cage or end cage code is necessary for completing the SAM. So this code '
              "is a five character alpha numeric classifier and it's actually issued by the "
              'DA, the Defense Logistics Agency for US entities engaged in government '
              'contracts.',
      'timestamp': 29,
      'timestamp_label': '[00:00:29]',
      'timestamp_seconds': 29,
      'tip': 'A valid cage or end cage code is necessary for completing the SAM. So this code '
             "is a five character alpha numeric classifier and it's actually issued by the DA, "
             'the Defense Logistics Agency for US entities engaged in government contracts.',
      'title': 'Sam.gov registration: CAGE & NCAGE Codes - Colleen Spiegel (SEMSCIO)',
      'url': 'https://www.youtube.com/watch?v=rRWCLLWqrV0&t=29s',
      'video_id': 'rRWCLLWqrV0'},
     {'author': 'Federal Processing Registry',
      'channel': 'Federal Processing Registry',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:29](https://www.youtube.com/watch?v=ifMU9O8Ydmg&t=149s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Established registration services often offer support, ensuring compliance, and '
              'preventing costly mistakes. Annual reviews and updates to your cage information '
              'can prevent emergency situations amid potential contract opportunities.',
      'timestamp': 149,
      'timestamp_label': '[00:02:29]',
      'timestamp_seconds': 149,
      'tip': 'Established registration services often offer support, ensuring compliance, and '
             'preventing costly mistakes. Annual reviews and updates to your cage information '
             'can prevent emergency situations amid potential contract opportunities.',
      'title': 'How to Correct or Update Your CAGE Code in SAM.gov | Visual Walkthrough '
               '(Federal Processing Registry)',
      'url': 'https://www.youtube.com/watch?v=ifMU9O8Ydmg&t=149s',
      'video_id': 'ifMU9O8Ydmg'},
     {'author': 'Federal Contracts Lab',
      'channel': 'Federal Contracts Lab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=NUKVGhkCHbg&t=54s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Think of it like a government's quick checkout lane. When an agency needs "
              'training, supplies, equipment, a repair, or something urgent, they do not '
              'always want to go through a long contracting process. They may need a qualified '
              'vendor who can solve the problem quickly.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': "Think of it like a government's quick checkout lane. When an agency needs "
             'training, supplies, equipment, a repair, or something urgent, they do not always '
             'want to go through a long contracting process. They may need a qualified vendor '
             'who can solve the problem quickly.',
      'title': 'How to start government contracting with 0$ |Micro Purchases (Federal '
               'Contracts Lab)',
      'url': 'https://www.youtube.com/watch?v=NUKVGhkCHbg&t=54s',
      'video_id': 'NUKVGhkCHbg'},
     {'author': 'Point2Pivot',
      'channel': 'Point2Pivot',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:33:48](https://www.youtube.com/watch?v=LmEpAxUzd94&t=2028s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And finally, it's giving uh uh commercial fish uh harvesters, communication "
              'material, training resources, regional support networks, and help desk risk '
              'mitigation u section is next.',
      'timestamp': 2028,
      'timestamp_label': '[00:33:48]',
      'timestamp_seconds': 2028,
      'tip': "And finally, it's giving uh uh commercial fish uh harvesters, communication "
             'material, training resources, regional support networks, and help desk risk '
             'mitigation u section is next.',
      'title': 'Turn 40-Hour RFP Responses Into 4-Hour Wins Using AI (Point2Pivot)',
      'url': 'https://www.youtube.com/watch?v=LmEpAxUzd94&t=2028s',
      'video_id': 'LmEpAxUzd94'},
     {'author': 'Diamond Hunter Enterprises',
      'channel': 'Diamond Hunter Enterprises',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:05](https://www.youtube.com/watch?v=hdZFRp2VG8E&t=305s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Life experiences me and strategies for building strong relationships with '
              "Contracting officers and agencies let's grow together by winning multi-million "
              'dollar contracts in your lines.',
      'timestamp': 305,
      'timestamp_label': '[00:05:05]',
      'timestamp_seconds': 305,
      'tip': 'Life experiences me and strategies for building strong relationships with '
             "Contracting officers and agencies let's grow together by winning multi-million "
             'dollar contracts in your lines.',
      'title': 'How Government Contracting Works for Beginners | First GovCon 8a CEO Success '
               'Story (Diamond Hunter Enterprises)',
      'url': 'https://www.youtube.com/watch?v=hdZFRp2VG8E&t=305s',
      'video_id': 'hdZFRp2VG8E'},
     {'author': 'Bid and Comply',
      'channel': 'Bid and Comply',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=c73xWsLDDhc&t=87s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mark each requirement as mandatory or scored. Mandatory items are pass or fail. '
              'Miss one, and your bid can be rejected before anyone reads your technical '
              'proposal. Scored items earn points, so they tell you where to spend your best '
              'writing time.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': 'Mark each requirement as mandatory or scored. Mandatory items are pass or fail. '
             'Miss one, and your bid can be rejected before anyone reads your technical '
             'proposal. Scored items earn points, so they tell you where to spend your best '
             'writing time.',
      'title': 'How to Build a Tender Compliance Matrix in 6 Steps (Bid and Comply)',
      'url': 'https://www.youtube.com/watch?v=c73xWsLDDhc&t=87s',
      'video_id': 'c73xWsLDDhc'},
     {'author': "D'S Construction",
      'channel': "D'S Construction",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:49](https://www.youtube.com/watch?v=yxjYYFbCa5E&t=169s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Painting and janitorial, South Louisiana under $50,000 first, and the '
              "set-aside  jobs first because that's where a small certified business has the "
              'edge.',
      'timestamp': 169,
      'timestamp_label': '[00:02:49]',
      'timestamp_seconds': 169,
      'tip': 'Painting and janitorial, South Louisiana under $50,000 first, and the set-aside  '
             "jobs first because that's where a small certified business has the edge.",
      'title': "Learning the Bid Sites | D'S Construction Podcast Ep. 3 (D'S Construction)",
      'url': 'https://www.youtube.com/watch?v=yxjYYFbCa5E&t=169s',
      'video_id': 'yxjYYFbCa5E'},
     {'author': 'FedAccess',
      'channel': 'FedAccess',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:50](https://www.youtube.com/watch?v=T_cRpZF2IUo&t=410s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Has agency specific contract clauses that are in addition to the fart losses so '
              "what are the biggest mistakes i've seen people make and what's my advice.",
      'timestamp': 410,
      'timestamp_label': '[00:06:50]',
      'timestamp_seconds': 410,
      'tip': 'Has agency specific contract clauses that are in addition to the fart losses so '
             "what are the biggest mistakes i've seen people make and what's my advice.",
      'title': 'TLDR  Which Parts of the Federal Acquisition Regulation Matter? (FedAccess)',
      'url': 'https://www.youtube.com/watch?v=T_cRpZF2IUo&t=410s',
      'video_id': 'T_cRpZF2IUo'},
     {'author': 'CHCEDC',
      'channel': 'CHCEDC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:01:36](https://www.youtube.com/watch?v=46vBsddH6zQ&t=3696s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s where it's coming from, that's fine. Um to have some consistency in the uh "
              'proposal number and your your agency, your business, but I would avoid logos '
              "because I think that's going to take up too much space.",
      'timestamp': 3696,
      'timestamp_label': '[01:01:36]',
      'timestamp_seconds': 3696,
      'tip': "'s where it's coming from, that's fine. Um to have some consistency in the uh "
             'proposal number and your your agency, your business, but I would avoid logos '
             "because I think that's going to take up too much space.",
      'title': 'How to Respond to an RFP/RFQ – Mastering Proposal Writing presented by Keli '
               'Krueger-Huhra (CHCEDC)',
      'url': 'https://www.youtube.com/watch?v=46vBsddH6zQ&t=3696s',
      'video_id': '46vBsddH6zQ'},
     {'author': 'Tris10 @ MeND',
      'channel': 'Tris10 @ MeND',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:43](https://www.youtube.com/watch?v=yXqp5I7wQK0&t=643s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Accordingly if we do have a problem with the quantity of a shipment First Step '
              'that we do in all this is we call the da service desk you can call the da '
              'service.',
      'timestamp': 643,
      'timestamp_label': '[00:10:43]',
      'timestamp_seconds': 643,
      'tip': 'Accordingly if we do have a problem with the quantity of a shipment First Step '
             'that we do in all this is we call the da service desk you can call the da '
             'service.',
      'title': 'Handling DLA Payment Issues - Invoicing Issues with the DLA Explained! 💡 '
               '(Tris10 @ MeND)',
      'url': 'https://www.youtube.com/watch?v=yXqp5I7wQK0&t=643s',
      'video_id': 'yXqp5I7wQK0'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:34](https://www.youtube.com/watch?v=AHQVro9N9HM&t=1294s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I was like, you know, okay. " He goes, "We me and my brother have done this for '
              '20 years on the side." And we talked through it and okay, I\'m going to start '
              "I'm going to put out a put out a bid to trap pigs for one of my local cities. "
              'And it was pigs and beavers.',
      'timestamp': 1294,
      'timestamp_label': '[00:21:34]',
      'timestamp_seconds': 1294,
      'tip': 'I was like, you know, okay. " He goes, "We me and my brother have done this for '
             '20 years on the side." And we talked through it and okay, I\'m going to start '
             "I'm going to put out a put out a bid to trap pigs for one of my local cities. "
             'And it was pigs and beavers.',
      'title': 'He Knew NOTHING About GovCon… Then Won $68K in Government Contracts (Kizzy '
               'Parks)',
      'url': 'https://www.youtube.com/watch?v=AHQVro9N9HM&t=1294s',
      'video_id': 'AHQVro9N9HM'},
     {'author': 'Sternberg Law Group',
      'channel': 'Sternberg Law Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=IMjYXOH8UoU&t=146s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '"Hey, I want to see how these funds are spent." Now, if you took a quart '
              'million dollars, signed a personal guarantee, dumped all that money into Robin '
              'Hood, and bought Bitcoin, you had a problem.',
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': '"Hey, I want to see how these funds are spent." Now, if you took a quart million '
             'dollars, signed a personal guarantee, dumped all that money into Robin Hood, and '
             'bought Bitcoin, you had a problem.',
      'title': 'Who Should Really Worry About EIDL Loans | Sternberg Law Group (Sternberg Law '
               'Group)',
      'url': 'https://www.youtube.com/watch?v=IMjYXOH8UoU&t=146s',
      'video_id': 'IMjYXOH8UoU'},
     {'author': 'Sheenapreneur',
      'channel': 'Sheenapreneur',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=JnxlzAHCjkY&t=117s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Like yeah we know each other and we about to put this together together joint '
              "ventures an official that's like marriage with a prenup okay that's like really "
              'really like we really want to work together and a lot of uh Mentor Protege '
              'programs will require a joint venture.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': 'Like yeah we know each other and we about to put this together together joint '
             "ventures an official that's like marriage with a prenup okay that's like really "
             'really like we really want to work together and a lot of uh Mentor Protege '
             'programs will require a joint venture.',
      'title': "What's the Difference Between JVs, Subcontracting & Teaming? | Government "
               'Contracting (Sheenapreneur)',
      'url': 'https://www.youtube.com/watch?v=JnxlzAHCjkY&t=117s',
      'video_id': 'JnxlzAHCjkY'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:10](https://www.youtube.com/watch?v=FWfV2m3K4jY&t=910s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "EDI no there's nothing that that doesn't apply do you want to be included if "
              "you want to be included click yes I'm clicking no this is not really an area "
              "that we're interested.",
      'timestamp': 910,
      'timestamp_label': '[00:15:10]',
      'timestamp_seconds': 910,
      'tip': "EDI no there's nothing that that doesn't apply do you want to be included if you "
             "want to be included click yes I'm clicking no this is not really an area that "
             "we're interested.",
      'title': 'How To Register In Sam.Gov 2024 (Step-by-Step Guide) (Kizzy Parks)',
      'url': 'https://www.youtube.com/watch?v=FWfV2m3K4jY&t=910s',
      'video_id': 'FWfV2m3K4jY'}],
 6: [{'author': 'annica at Bill Bright',
      'channel': 'annica at Bill Bright',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:05](https://www.youtube.com/watch?v=WDekT_xRXC0&t=245s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You can act like the field doesn't exist unless you get a red error message. "
              "The first screen is simple. It'll ask for your cage code, your contract number, "
              'and if you have a delivery order number. Choose your cage code from the drop- '
              'down list.',
      'timestamp': 245,
      'timestamp_label': '[00:04:05]',
      'timestamp_seconds': 245,
      'tip': "You can act like the field doesn't exist unless you get a red error message. The "
             "first screen is simple. It'll ask for your cage code, your contract number, and "
             'if you have a delivery order number. Choose your cage code from the drop- down '
             'list.',
      'title': 'WAWF Invoicing How To: Expert Guidance to Get Paid FAST and Avoid Delays! '
               '(annica at Bill Bright)',
      'url': 'https://www.youtube.com/watch?v=WDekT_xRXC0&t=245s',
      'video_id': 'WDekT_xRXC0'},
     {'author': 'Neil McDonnell',
      'channel': 'Neil McDonnell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:22](https://www.youtube.com/watch?v=YR_aPfXedtA&t=502s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, I'm going to instead of building all the filters, I want to build them one "
              "at a time so I show you kind of working their way down. Um so, I'm going to say "
              "build me a new search here. And the first thing I'm going to do is that uh set "
              'aside. So, where was that little guy?',
      'timestamp': 502,
      'timestamp_label': '[00:08:22]',
      'timestamp_seconds': 502,
      'tip': "So, I'm going to instead of building all the filters, I want to build them one "
             "at a time so I show you kind of working their way down. Um so, I'm going to say "
             "build me a new search here. And the first thing I'm going to do is that uh set "
             'aside. So, where was that little guy?',
      'title': 'How to Find WOSB Set Asides Using FPDS | Government Contracting (Neil '
               'McDonnell)',
      'url': 'https://www.youtube.com/watch?v=YR_aPfXedtA&t=502s',
      'video_id': 'YR_aPfXedtA'},
     {'author': 'FedOpp',
      'channel': 'FedOpp',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:20](https://www.youtube.com/watch?v=qmdunkO7mts&t=140s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then type your FSC, a solicitation, or a purchase request number. You can also '
              'search by NSN or NIIN, item name, cage code, keyword, or NAICS. The AMC and '
              'AMSC boxes filter by acquisition method codes, which show whether a buy is '
              'limited to approved sources.',
      'timestamp': 140,
      'timestamp_label': '[00:02:20]',
      'timestamp_seconds': 140,
      'tip': 'Then type your FSC, a solicitation, or a purchase request number. You can also '
             'search by NSN or NIIN, item name, cage code, keyword, or NAICS. The AMC and AMSC '
             'boxes filter by acquisition method codes, which show whether a buy is limited to '
             'approved sources.',
      'title': 'DLA Urgent Need and DIBBS No Bid List: In-Stock Parts | FedOpp (FedOpp)',
      'url': 'https://www.youtube.com/watch?v=qmdunkO7mts&t=140s',
      'video_id': 'qmdunkO7mts'},
     {'author': 'FedAccess',
      'channel': 'FedAccess',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:25](https://www.youtube.com/watch?v=GrYP5KyxBho&t=145s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now the words can be a bit confusing, but what it means is that only small '
              "businesses can bid on these contracts, so you're not competing against big "
              'companies. Now, over on the right, we have a list of contracts that match our '
              'search criteria.',
      'timestamp': 145,
      'timestamp_label': '[00:02:25]',
      'timestamp_seconds': 145,
      'tip': 'Now the words can be a bit confusing, but what it means is that only small '
             "businesses can bid on these contracts, so you're not competing against big "
             'companies. Now, over on the right, we have a list of contracts that match our '
             'search criteria.',
      'title': 'How to Find Past Prices for Better Gov Contract Bids (Using Free Resources) '
               '(FedAccess)',
      'url': 'https://www.youtube.com/watch?v=GrYP5KyxBho&t=145s',
      'video_id': 'GrYP5KyxBho'},
     {'author': 'Squared Compass',
      'channel': 'Squared Compass',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=oSSAuniLuDI&t=36s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So let's dive into the first round of data. Here's the breakdown of the "
              'targeted set aside certifications and what the government wants to do. ADA '
              'companies are at 5% of the total contracting dollars for set aides.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': "So let's dive into the first round of data. Here's the breakdown of the targeted "
             'set aside certifications and what the government wants to do. ADA companies are '
             'at 5% of the total contracting dollars for set aides.',
      'title': 'Federal Contracting Strategy: HUBZone vs Every Other SBA Cert (Squared '
               'Compass)',
      'url': 'https://www.youtube.com/watch?v=oSSAuniLuDI&t=36s',
      'video_id': 'oSSAuniLuDI'},
     {'author': 'Nick Waters GovCon',
      'channel': 'Nick Waters GovCon',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:14](https://www.youtube.com/watch?v=sqfiBzNcTPI&t=74s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can also click the should I apply button to find out if you do qualify for '
              "any of the certifications. What I'd like to do is click on the certifications "
              'individually. So the first one we are going to click on is the ADA business '
              'development certification.',
      'timestamp': 74,
      'timestamp_label': '[00:01:14]',
      'timestamp_seconds': 74,
      'tip': 'You can also click the should I apply button to find out if you do qualify for '
             "any of the certifications. What I'd like to do is click on the certifications "
             'individually. So the first one we are going to click on is the ADA business '
             'development certification.',
      'title': 'Government Contracting Certifications for Beginners: WOSB, SDVOSB, 8(a) & '
               'HUBZone (Nick Waters GovCon)',
      'url': 'https://www.youtube.com/watch?v=sqfiBzNcTPI&t=74s',
      'video_id': 'sqfiBzNcTPI'},
     {'author': 'GovClose | DoD Contract Academy',
      'channel': 'GovClose | DoD Contract Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:34](https://www.youtube.com/watch?v=z6ZNrmprd-o&t=394s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Government Contracting you've never worked as a consultant and you just uh "
              "closed your first deal is that correct that's fa and I got a couple small "
              'projects on the side as well so definitely.',
      'timestamp': 394,
      'timestamp_label': '[00:06:34]',
      'timestamp_seconds': 394,
      'tip': "Government Contracting you've never worked as a consultant and you just uh "
             "closed your first deal is that correct that's fa and I got a couple small "
             'projects on the side as well so definitely.',
      'title': 'Subcontracting Government Contracts In 2025! (GovClose | DoD Contract Academy)',
      'url': 'https://www.youtube.com/watch?v=z6ZNrmprd-o&t=394s',
      'video_id': 'z6ZNrmprd-o'},
     {'author': 'Contract Warrior',
      'channel': 'Contract Warrior',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:38](https://www.youtube.com/watch?v=pktnZU4AWIE&t=458s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You'll find a free course that I personally put together for you so that you "
              'can learn how to think like your contracting officer. It will absolutely get '
              'you a leg up and help you navigate the federal government both pre-award and '
              'post-award.',
      'timestamp': 458,
      'timestamp_label': '[00:07:38]',
      'timestamp_seconds': 458,
      'tip': "You'll find a free course that I personally put together for you so that you can "
             'learn how to think like your contracting officer. It will absolutely get you a '
             'leg up and help you navigate the federal government both pre-award and '
             'post-award.',
      'title': "Don't Work for Free: Unauthorized Commitments in Federal Construction "
               '(Contract Warrior)',
      'url': 'https://www.youtube.com/watch?v=pktnZU4AWIE&t=458s',
      'video_id': 'pktnZU4AWIE'},
     {'author': 'SamSearch - AI for Government Contracting',
      'channel': 'SamSearch - AI for Government Contracting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:36](https://www.youtube.com/watch?v=NiWdxgnr3xo&t=636s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, here you're going to find all the contracts that have been awarded in the "
              'past. And you can see here the business name. Now each one of these businesses '
              "you're seeing the contract, the award description and how much they've won.",
      'timestamp': 636,
      'timestamp_label': '[00:10:36]',
      'timestamp_seconds': 636,
      'tip': "So, here you're going to find all the contracts that have been awarded in the "
             'past. And you can see here the business name. Now each one of these businesses '
             "you're seeing the contract, the award description and how much they've won.",
      'title': 'Government Contractor’s Guide to USASpending.gov [2025 Tutorial] (SamSearch - '
               'AI for Government Contracting)',
      'url': 'https://www.youtube.com/watch?v=NiWdxgnr3xo&t=636s',
      'video_id': 'NiWdxgnr3xo'},
     {'author': 'Estimight',
      'channel': 'Estimight',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:06](https://www.youtube.com/watch?v=PP70aCudT_s&t=426s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Pick a template from the list, then apply. History opens once a revision has '
              "been sent. Refresh re-prices the proposal from the estimate. When it's ready, "
              'export PDF downloads it, or send to client freezes the revision and emails the '
              'PDF.',
      'timestamp': 426,
      'timestamp_label': '[00:07:06]',
      'timestamp_seconds': 426,
      'tip': 'Pick a template from the list, then apply. History opens once a revision has '
             "been sent. Refresh re-prices the proposal from the estimate. When it's ready, "
             'export PDF downloads it, or send to client freezes the revision and emails the '
             'PDF.',
      'title': 'Project Bid-Desk - Proposal (Estimight)',
      'url': 'https://www.youtube.com/watch?v=PP70aCudT_s&t=426s',
      'video_id': 'PP70aCudT_s'},
     {'author': 'VA OSDBU (On Demand)',
      'channel': 'VA OSDBU (On Demand)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:22](https://www.youtube.com/watch?v=iLuva0z2cMA&t=1342s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Performance and a reputation with that client imagine coming on board with all '
              "of your people with the first day or within a week or two so it's strategic and "
              "it's smart and it helps to helps her with her return on her investment next "
              'slide.',
      'timestamp': 1342,
      'timestamp_label': '[00:22:22]',
      'timestamp_seconds': 1342,
      'tip': 'Performance and a reputation with that client imagine coming on board with all '
             "of your people with the first day or within a week or two so it's strategic and "
             "it's smart and it helps to helps her with her return on her investment next "
             'slide.',
      'title': 'Prime Sub, Teaming Agreements and Subcontracts (VA OSDBU (On Demand))',
      'url': 'https://www.youtube.com/watch?v=iLuva0z2cMA&t=1342s',
      'video_id': 'iLuva0z2cMA'},
     {'author': 'GovKidMethod',
      'channel': 'GovKidMethod',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:44](https://www.youtube.com/watch?v=LnPiGkUTs2E&t=704s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Set aside a lot of work for vets but now everything has to go to vets first and '
              "then if vets can't do it then the other set asides get a chance at it or it'll.",
      'timestamp': 704,
      'timestamp_label': '[00:11:44]',
      'timestamp_seconds': 704,
      'tip': 'Set aside a lot of work for vets but now everything has to go to vets first and '
             "then if vets can't do it then the other set asides get a chance at it or it'll.",
      'title': 'Government Contracts Set-Asides : 8(a), WOSB, EDWOSB, VOSB, SDVOSB, HUBZone '
               'Certification Process (GovKidMethod)',
      'url': 'https://www.youtube.com/watch?v=LnPiGkUTs2E&t=704s',
      'video_id': 'LnPiGkUTs2E'},
     {'author': 'Dr. Mel',
      'channel': 'Dr. Mel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:44](https://www.youtube.com/watch?v=HKtAZzSL_GQ&t=224s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Out my book The trillion dooll client click the link below to make sure your '
              "next partnership is built to win I'm Dr Melissa J Williams helping you protect "
              'your interests power your profits and partner with Clarity thanks for watching.',
      'timestamp': 224,
      'timestamp_label': '[00:03:44]',
      'timestamp_seconds': 224,
      'tip': 'Out my book The trillion dooll client click the link below to make sure your '
             "next partnership is built to win I'm Dr Melissa J Williams helping you protect "
             'your interests power your profits and partner with Clarity thanks for watching.',
      'title': 'BEST Teaming Agreement Strategies For 2025 Government Contracts (Dr. Mel)',
      'url': 'https://www.youtube.com/watch?v=HKtAZzSL_GQ&t=224s',
      'video_id': 'HKtAZzSL_GQ'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:13](https://www.youtube.com/watch?v=OKLXh8NcJxQ&t=1213s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, how does this make sense?" First, I paused cuz I was I was shocked, right? '
              'I haven\'t heard this before. And I\'m like, "How could this be?" And I said, '
              '"Well, how have your bids changed from like bid number four to bid number 50?".',
      'timestamp': 1213,
      'timestamp_label': '[00:20:13]',
      'timestamp_seconds': 1213,
      'tip': 'So, how does this make sense?" First, I paused cuz I was I was shocked, right? I '
             'haven\'t heard this before. And I\'m like, "How could this be?" And I said, '
             '"Well, how have your bids changed from like bid number four to bid number 50?".',
      'title': 'How Derek Got Rich With Government Contracts and You Can Too (Kizzy Parks)',
      'url': 'https://www.youtube.com/watch?v=OKLXh8NcJxQ&t=1213s',
      'video_id': 'OKLXh8NcJxQ'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:32:28](https://www.youtube.com/watch?v=eIFlVzfusWo&t=1948s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Email me at I don't know I'm trying to be funny y'all trying they're letting "
              'you know that may be used keep in mind anyone you list here is going to be able '
              'to obtain access to all of this so be careful just be careful.',
      'timestamp': 1948,
      'timestamp_label': '[00:32:28]',
      'timestamp_seconds': 1948,
      'tip': "Email me at I don't know I'm trying to be funny y'all trying they're letting you "
             'know that may be used keep in mind anyone you list here is going to be able to '
             'obtain access to all of this so be careful just be careful.',
      'title': 'Sam.Gov Registration Success: Get UEI and Cage Code Successfully | Part 2 '
               '(Updated) (Kizzy Parks)',
      'url': 'https://www.youtube.com/watch?v=eIFlVzfusWo&t=1948s',
      'video_id': 'eIFlVzfusWo'}],
 7: [{'author': 'GovCon TechLab',
      'channel': 'GovCon TechLab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:15](https://www.youtube.com/watch?v=JYbjE63rG-Y&t=135s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And this is a four-step system. So, the P stands for position yourself, right? '
              'So, that primes actually want to partner with you. We need to assess whether '
              'the teaming agreement makes sense for this particular bid.',
      'timestamp': 135,
      'timestamp_label': '[00:02:15]',
      'timestamp_seconds': 135,
      'tip': 'And this is a four-step system. So, the P stands for position yourself, right? '
             'So, that primes actually want to partner with you. We need to assess whether the '
             'teaming agreement makes sense for this particular bid.',
      'title': 'How to Structure a Teaming Agreement in Government Contracting (So That You '
               'Don’t Get Burned) (GovCon TechLab)',
      'url': 'https://www.youtube.com/watch?v=JYbjE63rG-Y&t=135s',
      'video_id': 'JYbjE63rG-Y'},
     {'author': 'Intel by CandiMentor',
      'channel': 'Intel by CandiMentor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:59](https://www.youtube.com/watch?v=jF1M1NGuye8&t=299s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For example, delivery capability might carry more weight than presentation '
              'quality because it has greater business impact. The RFP process needs '
              'discipline because every clarification can affect fairness. Questions are '
              'shared consistently.',
      'timestamp': 299,
      'timestamp_label': '[00:04:59]',
      'timestamp_seconds': 299,
      'tip': 'For example, delivery capability might carry more weight than presentation '
             'quality because it has greater business impact. The RFP process needs discipline '
             'because every clarification can affect fairness. Questions are shared '
             'consistently.',
      'title': 'RFQ, RFP, and RFI Explained: How to Run a Procurement Bid Process (Intel by '
               'CandiMentor)',
      'url': 'https://www.youtube.com/watch?v=jF1M1NGuye8&t=299s',
      'video_id': 'jF1M1NGuye8'},
     {'author': 'Acquisition Pro Tips',
      'channel': 'Acquisition Pro Tips',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:10](https://www.youtube.com/watch?v=cdachjXPX3k&t=670s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If it says warning, double check the field it mentions. But if it says error in '
              "red, that means stop. You can't move forward until it's fixed. Most of the time "
              "it's something small like a missing delivery order number or a mismatch cage "
              'code. Acquisition pro tip number six.',
      'timestamp': 670,
      'timestamp_label': '[00:11:10]',
      'timestamp_seconds': 670,
      'tip': 'If it says warning, double check the field it mentions. But if it says error in '
             "red, that means stop. You can't move forward until it's fixed. Most of the time "
             "it's something small like a missing delivery order number or a mismatch cage "
             'code. Acquisition pro tip number six.',
      'title': 'Ep. 9: How to Submit a WAWF COMBO Invoice | Vendor Step-by-Step Tutorial '
               '(Acquisition Pro Tips)',
      'url': 'https://www.youtube.com/watch?v=cdachjXPX3k&t=670s',
      'video_id': 'cdachjXPX3k'},
     {'author': 'Secureframe',
      'channel': 'Secureframe',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:00](https://www.youtube.com/watch?v=v7nJCLRc0uo&t=360s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, our cage code and you can see all of the awards that we have won or at '
              'least the last 18 months inside of the DIP system, but our cage code is 8HU7 '
              'based out of Los Angeles.',
      'timestamp': 360,
      'timestamp_label': '[00:06:00]',
      'timestamp_seconds': 360,
      'tip': 'So, our cage code and you can see all of the awards that we have won or at least '
             'the last 18 months inside of the DIP system, but our cage code is 8HU7 based out '
             'of Los Angeles.',
      'title': 'Defense Logistics Agency Contracts: How to Bid Effectively with the DLA '
               '(Secureframe)',
      'url': 'https://www.youtube.com/watch?v=v7nJCLRc0uo&t=360s',
      'video_id': 'v7nJCLRc0uo'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=wNMt73DArFc&t=20s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Everything that they have asked for in order to access over 500 billion dollars '
              "in federal government contracts you must have a cage code I'm going to walk you "
              "through those steps let's go along so I can walk you through using my "
              'Foundation.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'Everything that they have asked for in order to access over 500 billion dollars '
             "in federal government contracts you must have a cage code I'm going to walk you "
             "through those steps let's go along so I can walk you through using my "
             'Foundation.',
      'title': 'Sam.Gov Registration 2023 | Getting To Cage Code Successfully | Part 2 (Kizzy '
               'Parks)',
      'url': 'https://www.youtube.com/watch?v=wNMt73DArFc&t=20s',
      'video_id': 'wNMt73DArFc'},
     {'author': 'Government Contract Blueprint',
      'channel': 'Government Contract Blueprint',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:01](https://www.youtube.com/watch?v=jSDqXlz5MbI&t=301s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can use AI to help organize publicly available solicitation requirements '
              'into a draft checklist. But then, you should manually verify every row against '
              'the original solicitation. Remember, AI can assist the process.',
      'timestamp': 301,
      'timestamp_label': '[00:05:01]',
      'timestamp_seconds': 301,
      'tip': 'You can use AI to help organize publicly available solicitation requirements '
             'into a draft checklist. But then, you should manually verify every row against '
             'the original solicitation. Remember, AI can assist the process.',
      'title': 'Government Proposal Writing: Build a Compliance Matrix Step-by-Step '
               '(Government Contract Blueprint)',
      'url': 'https://www.youtube.com/watch?v=jSDqXlz5MbI&t=301s',
      'video_id': 'jSDqXlz5MbI'},
     {'author': 'ELINT Capital',
      'channel': 'ELINT Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:39:54](https://www.youtube.com/watch?v=EpUc9OVjb4g&t=2394s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They're trying to streamline the acquisition process and so they're relying "
              'more and more on vehicles. A lot of these are GSA vehicles, but a lot but also '
              "agency IDIQs and it's just hard.",
      'timestamp': 2394,
      'timestamp_label': '[00:39:54]',
      'timestamp_seconds': 2394,
      'tip': "They're trying to streamline the acquisition process and so they're relying more "
             'and more on vehicles. A lot of these are GSA vehicles, but a lot but also agency '
             "IDIQs and it's just hard.",
      'title': 'Subcontracting & Teaming - Prime vs Sub: The Financial Trade-offs (ELINT '
               'Capital)',
      'url': 'https://www.youtube.com/watch?v=EpUc9OVjb4g&t=2394s',
      'video_id': 'EpUc9OVjb4g'},
     {'author': 'ProcuraFind',
      'channel': 'ProcuraFind',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:48](https://www.youtube.com/watch?v=UcFlKExo_dc&t=468s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your 20 knee deep down and dirty right this is no no no high level five to '
              'seven process steps on how we do what we do very well as it relates to what.',
      'timestamp': 468,
      'timestamp_label': '[00:07:48]',
      'timestamp_seconds': 468,
      'tip': 'Your 20 knee deep down and dirty right this is no no no high level five to seven '
             'process steps on how we do what we do very well as it relates to what.',
      'title': 'How to WIN More Contracts: Responding to RFIs, RFQs & RFPs (ProcuraFind)',
      'url': 'https://www.youtube.com/watch?v=UcFlKExo_dc&t=468s',
      'video_id': 'UcFlKExo_dc'},
     {'author': 'Industrial Development Corporation - IDC',
      'channel': 'Industrial Development Corporation - IDC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:35:04](https://www.youtube.com/watch?v=Sh4XERIYcuY&t=2104s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So I'm going to hand over to us PL and he will use a pre-registered example "
              'that we can then move through the process um uh quickly without having you know '
              "to wait for a registration workflow and I'm going to hand over to us now to "
              'take you through that process.',
      'timestamp': 2104,
      'timestamp_label': '[00:35:04]',
      'timestamp_seconds': 2104,
      'tip': "So I'm going to hand over to us PL and he will use a pre-registered example that "
             'we can then move through the process um uh quickly without having you know to '
             "wait for a registration workflow and I'm going to hand over to us now to take "
             'you through that process.',
      'title': 'Tirisano Bid Window 5 Webinar 3 (Industrial Development Corporation - IDC)',
      'url': 'https://www.youtube.com/watch?v=Sh4XERIYcuY&t=2104s',
      'video_id': 'Sh4XERIYcuY'},
     {'author': 'Neil McDonnell',
      'channel': 'Neil McDonnell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:19](https://www.youtube.com/watch?v=17foq325L5w&t=199s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '20 years after I got out of the army as a small business government contractor. '
              "Um, and since 2018, I've been helping people like you understand that "
              'government contracting is not a secret. When we follow a process A to Z, we '
              'have repeatable, predictable results.',
      'timestamp': 199,
      'timestamp_label': '[00:03:19]',
      'timestamp_seconds': 199,
      'tip': '20 years after I got out of the army as a small business government contractor. '
             "Um, and since 2018, I've been helping people like you understand that government "
             'contracting is not a secret. When we follow a process A to Z, we have '
             'repeatable, predictable results.',
      'title': 'Searching Federal Procurement Data System (FPDS) for Government Contracts '
               '(Neil McDonnell)',
      'url': 'https://www.youtube.com/watch?v=17foq325L5w&t=199s',
      'video_id': '17foq325L5w'},
     {'author': 'Dr. Wes Fisher',
      'channel': 'Dr. Wes Fisher',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:24](https://www.youtube.com/watch?v=xH6KWT7x8Ac&t=84s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re like what's oh my goodness that's overwhelming however guess what some of "
              "you guys have had cage codes for a year or two years and you didn't even know "
              "how to do that right let me do it again that's you guys will replay it but let "
              'me do it again sam.',
      'timestamp': 84,
      'timestamp_label': '[00:01:24]',
      'timestamp_seconds': 84,
      'tip': "'re like what's oh my goodness that's overwhelming however guess what some of "
             "you guys have had cage codes for a year or two years and you didn't even know "
             "how to do that right let me do it again that's you guys will replay it but let "
             'me do it again sam.',
      'title': 'How To Bid On A Government Contract In 5 Days (2025) | Step-by-Step Guide (Dr. '
               'Wes Fisher)',
      'url': 'https://www.youtube.com/watch?v=xH6KWT7x8Ac&t=84s',
      'video_id': 'xH6KWT7x8Ac'},
     {'author': 'GovPrep',
      'channel': 'GovPrep',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:24](https://www.youtube.com/watch?v=bg9NY9VUfsE&t=84s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And again set aside if this block is checked if this box is checked then uh '
              "what that's going to look like is.",
      'timestamp': 84,
      'timestamp_label': '[00:01:24]',
      'timestamp_seconds': 84,
      'tip': 'And again set aside if this block is checked if this box is checked then uh what '
             "that's going to look like is.",
      'title': 'Limits on Subcontracting (GovPrep)',
      'url': 'https://www.youtube.com/watch?v=bg9NY9VUfsE&t=84s',
      'video_id': 'bg9NY9VUfsE'},
     {'author': 'Politics_Shmolitics',
      'channel': 'Politics_Shmolitics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:39](https://www.youtube.com/watch?v=rcSJIi02YnA&t=459s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That single statistic explains why officials are talking about a system-wide '
              'problem, not just a single ring. The charged defendants will face their cases '
              'and prosecutors have signaled more charges could follow as the 45 '
              'investigations develop.',
      'timestamp': 459,
      'timestamp_label': '[00:07:39]',
      'timestamp_seconds': 459,
      'tip': 'That single statistic explains why officials are talking about a system-wide '
             'problem, not just a single ring. The charged defendants will face their cases '
             'and prosecutors have signaled more charges could follow as the 45 investigations '
             'develop.',
      'title': 'BREAKING NEWS: DOJ Busts Ghost Student Fraud Ring — October 29th, 2026 '
               '(Politics_Shmolitics)',
      'url': 'https://www.youtube.com/watch?v=rcSJIi02YnA&t=459s',
      'video_id': 'rcSJIi02YnA'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:41](https://www.youtube.com/watch?v=YHptbPFEaPQ&t=701s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'How I should be putting things in wave a wide area workflow got it right yes '
              "and how I should you know submit my bids and it's been working out fine ever "
              'since.',
      'timestamp': 701,
      'timestamp_label': '[00:11:41]',
      'timestamp_seconds': 701,
      'tip': 'How I should be putting things in wave a wide area workflow got it right yes and '
             "how I should you know submit my bids and it's been working out fine ever since.",
      'title': 'How To Get Rich With Government Contracts (Kizzy Parks)',
      'url': 'https://www.youtube.com/watch?v=YHptbPFEaPQ&t=701s',
      'video_id': 'YHptbPFEaPQ'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:38](https://www.youtube.com/watch?v=kpISY6VCkNY&t=218s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Of the day there's usually a human being involved at least one step in the "
              "payment process so keep that in mind so if there's a holiday or it's summer.",
      'timestamp': 218,
      'timestamp_label': '[00:03:38]',
      'timestamp_seconds': 218,
      'tip': "Of the day there's usually a human being involved at least one step in the "
             "payment process so keep that in mind so if there's a holiday or it's summer.",
      'title': 'How To Get Rich with Subcontracting in 2025 (Kizzy Parks)',
      'url': 'https://www.youtube.com/watch?v=kpISY6VCkNY&t=218s',
      'video_id': 'kpISY6VCkNY'}],
 8: [{'author': 'The DLA Vendor Network (DVN)',
      'channel': 'The DLA Vendor Network (DVN)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=OiMCYKFBggE&t=88s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Online software tool is the most comprehensive source of u.s government '
              'logistics and product data in the world its multi-tiered search engine allows.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'Online software tool is the most comprehensive source of u.s government '
             'logistics and product data in the world its multi-tiered search engine allows.',
      'title': 'Increase your DLA | DIBBS | Government Contracting Success with Intertek / SAI '
               'Global Online Tools! (The DLA Vendor Network (DVN))',
      'url': 'https://www.youtube.com/watch?v=OiMCYKFBggE&t=88s',
      'video_id': 'OiMCYKFBggE'},
     {'author': 'SamSearch - AI for Government Contracting',
      'channel': 'SamSearch - AI for Government Contracting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:23](https://www.youtube.com/watch?v=e7wypJIJZpw&t=623s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I can't think of an easier way to get into government contracting than "
              "simplified acquisition. So, if you're serious about getting into this space and "
              'you want to filter for simplified acquisition contracts, make sure to get sam '
              'search.',
      'timestamp': 623,
      'timestamp_label': '[00:10:23]',
      'timestamp_seconds': 623,
      'tip': "I can't think of an easier way to get into government contracting than "
             "simplified acquisition. So, if you're serious about getting into this space and "
             'you want to filter for simplified acquisition contracts, make sure to get sam '
             'search.',
      'title': 'Simplified Acquisitions & Micro-Purchases Tutorial - Easiest Way to Win '
               'Government Contracts (SamSearch - AI for Government Contracting)',
      'url': 'https://www.youtube.com/watch?v=e7wypJIJZpw&t=623s',
      'video_id': 'e7wypJIJZpw'},
     {'author': 'GovCon with Humam',
      'channel': 'GovCon with Humam',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:12](https://www.youtube.com/watch?v=IEV3HAgB8jA&t=432s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And then you can ask your local agency for a simplified acquisition procedure '
              'guide which could be very helpful to get you started. And lastly, we can do '
              "this by some magic using free government tools such as sam. Let's get started "
              'with sam.',
      'timestamp': 432,
      'timestamp_label': '[00:07:12]',
      'timestamp_seconds': 432,
      'tip': 'And then you can ask your local agency for a simplified acquisition procedure '
             'guide which could be very helpful to get you started. And lastly, we can do this '
             "by some magic using free government tools such as sam. Let's get started with "
             'sam.',
      'title': 'Simplified Acquisitions & Micro-Purchases Tutorial - Easiest Way to Win '
               'Government Contracts (GovCon with Humam)',
      'url': 'https://www.youtube.com/watch?v=IEV3HAgB8jA&t=432s',
      'video_id': 'IEV3HAgB8jA'},
     {'author': 'GovCon Empire with Derrick Green “Theo”',
      'channel': 'GovCon Empire with Derrick Green “Theo”',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:56](https://www.youtube.com/watch?v=k1EsNHPfqXY&t=296s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This section supports buying items and services commonly sold in the commercial '
              'marketplace. Instead of is instead of spending 14 months designing a custom '
              'project management platform, an agency may buy a secure commercial platform '
              'with configuration options.',
      'timestamp': 296,
      'timestamp_label': '[00:04:56]',
      'timestamp_seconds': 296,
      'tip': 'This section supports buying items and services commonly sold in the commercial '
             'marketplace. Instead of is instead of spending 14 months designing a custom '
             'project management platform, an agency may buy a secure commercial platform with '
             'configuration options.',
      'title': 'Federal Contracts Moving Faster in 2026 - FAR Overhaul. (GovCon Empire with '
               'Derrick Green “Theo”)',
      'url': 'https://www.youtube.com/watch?v=k1EsNHPfqXY&t=296s',
      'video_id': 'k1EsNHPfqXY'},
     {'author': 'Humam Finding Sam',
      'channel': 'Humam Finding Sam',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:34](https://www.youtube.com/watch?v=wxZNfwOuung&t=34s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It stands for the defense logistics agency internet bid board system. It's the "
              'official web-based portal for government procurement specifically for the DA.',
      'timestamp': 34,
      'timestamp_label': '[00:00:34]',
      'timestamp_seconds': 34,
      'tip': "It stands for the defense logistics agency internet bid board system. It's the "
             'official web-based portal for government procurement specifically for the DA.',
      'title': 'How to Win DIBBS Contracts (Step-by-Step Beginner Guide) (Humam Finding Sam)',
      'url': 'https://www.youtube.com/watch?v=wxZNfwOuung&t=34s',
      'video_id': 'wxZNfwOuung'},
     {'author': 'Neil McDonnell',
      'channel': 'Neil McDonnell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:52](https://www.youtube.com/watch?v=0cGdQvymmvY&t=1012s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "FPDS, you're going to keep refining what's your entry point. What do you like "
              'searching on? You know, it might be uh it might be an agency. It might be a '
              'nakes code or whatever, but this is what you would search on. And so this is '
              'what I want to show just initially.',
      'timestamp': 1012,
      'timestamp_label': '[00:16:52]',
      'timestamp_seconds': 1012,
      'tip': "FPDS, you're going to keep refining what's your entry point. What do you like "
             'searching on? You know, it might be uh it might be an agency. It might be a '
             'nakes code or whatever, but this is what you would search on. And so this is '
             'what I want to show just initially.',
      'title': 'Introduction to the Federal Procurement Data System (FPDS) - Part 1 (Neil '
               'McDonnell)',
      'url': 'https://www.youtube.com/watch?v=0cGdQvymmvY&t=1012s',
      'video_id': '0cGdQvymmvY'},
     {'author': 'GovCon TechLab',
      'channel': 'GovCon TechLab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:59](https://www.youtube.com/watch?v=uYFWvLCSDgA&t=299s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I have had other contracts with this agency. So I was submitting my invoices as '
              'I had been doing pre previous with other contracts that I won and that was '
              'through their online portal called WAT.',
      'timestamp': 299,
      'timestamp_label': '[00:04:59]',
      'timestamp_seconds': 299,
      'tip': 'I have had other contracts with this agency. So I was submitting my invoices as '
             'I had been doing pre previous with other contracts that I won and that was '
             'through their online portal called WAT.',
      'title': 'I Won 4 Government Contracts With the Middleman Strategy…And I Regret It. '
               '(GovCon TechLab)',
      'url': 'https://www.youtube.com/watch?v=uYFWvLCSDgA&t=299s',
      'video_id': 'uYFWvLCSDgA'},
     {'author': 'GovCon with Humam',
      'channel': 'GovCon with Humam',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:45](https://www.youtube.com/watch?v=NRMYxAAOPYo&t=405s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Before I finish I want to introduce you to Sam search the ultimate government '
              'contracting platform that you can use to streamline the whole process.',
      'timestamp': 405,
      'timestamp_label': '[00:06:45]',
      'timestamp_seconds': 405,
      'tip': 'Before I finish I want to introduce you to Sam search the ultimate government '
             'contracting platform that you can use to streamline the whole process.',
      'title': 'The Truth About Middleman Strategy in Government Contracting (Legal way!) '
               '(GovCon with Humam)',
      'url': 'https://www.youtube.com/watch?v=NRMYxAAOPYo&t=405s',
      'video_id': 'NRMYxAAOPYo'},
     {'author': 'Tris10 @ MeND',
      'channel': 'Tris10 @ MeND',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:57](https://www.youtube.com/watch?v=weLOISkZc5k&t=297s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Receiving report and so forth um another great piece of the pi system is it '
              "allows you to check electronic data uh through a uh portal that's inside of "
              'the.',
      'timestamp': 297,
      'timestamp_label': '[00:04:57]',
      'timestamp_seconds': 297,
      'tip': 'Receiving report and so forth um another great piece of the pi system is it '
             "allows you to check electronic data uh through a uh portal that's inside of the.",
      'title': 'PIEE and WAWF: Invoices and Receiving Reports for DIBBS Government Contracts '
               '(Tris10 @ MeND)',
      'url': 'https://www.youtube.com/watch?v=weLOISkZc5k&t=297s',
      'video_id': 'weLOISkZc5k'},
     {'author': 'Skip',
      'channel': 'Skip',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:53](https://www.youtube.com/watch?v=FZ6VO4mNzF4&t=113s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Seek enforcement well it turns out that management did not follow the policies '
              'when it began migrating this data from the service providers cloud platform to.',
      'timestamp': 113,
      'timestamp_label': '[00:01:53]',
      'timestamp_seconds': 113,
      'tip': 'Seek enforcement well it turns out that management did not follow the policies '
             'when it began migrating this data from the service providers cloud platform to.',
      'title': 'Major SBA EIDL Record Keeping Problems (Skip)',
      'url': 'https://www.youtube.com/watch?v=FZ6VO4mNzF4&t=113s',
      'video_id': 'FZ6VO4mNzF4'},
     {'author': 'Neil McDonnell',
      'channel': 'Neil McDonnell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:07](https://www.youtube.com/watch?v=g-mx_oRCj0k&t=307s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'FPDS search techniques or skill sets that I want you to um look at and and get '
              "good at. When you get good at the basics of using a tool, then you're able to "
              "master the information that's in that tool.",
      'timestamp': 307,
      'timestamp_label': '[00:05:07]',
      'timestamp_seconds': 307,
      'tip': 'FPDS search techniques or skill sets that I want you to um look at and and get '
             "good at. When you get good at the basics of using a tool, then you're able to "
             "master the information that's in that tool.",
      'title': 'Searching Federal Procurement Data System (FPDS) for Government Contracts '
               '(Neil McDonnell)',
      'url': 'https://www.youtube.com/watch?v=g-mx_oRCj0k&t=307s',
      'video_id': 'g-mx_oRCj0k'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:50](https://www.youtube.com/watch?v=DAbMwnUtgfI&t=530s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's all you do and you look to see what is being offered under that code "
              "under that set-aside. You can you can break down the 60/40 not just what you're "
              'bidding on, but also by set-aside.',
      'timestamp': 530,
      'timestamp_label': '[00:08:50]',
      'timestamp_seconds': 530,
      'tip': "That's all you do and you look to see what is being offered under that code "
             "under that set-aside. You can you can break down the 60/40 not just what you're "
             'bidding on, but also by set-aside.',
      'title': 'How to Make $3K/Month With Government Contracts (No Experience) (Kizzy Parks)',
      'url': 'https://www.youtube.com/watch?v=DAbMwnUtgfI&t=530s',
      'video_id': 'DAbMwnUtgfI'},
     {'author': 'Eric Coffie',
      'channel': 'Eric Coffie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=AOa0-iEhmks&t=115s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'VA Hospital fire damper actuator replacement router replacement uh some power '
              "tools at Warren's Air Force Base 15 month lease of 75 nmci certified mfds I "
              'know what that is bulk fertilizer I like this let put on this bulk fertilizer.',
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': 'VA Hospital fire damper actuator replacement router replacement uh some power '
             "tools at Warren's Air Force Base 15 month lease of 75 nmci certified mfds I know "
             'what that is bulk fertilizer I like this let put on this bulk fertilizer.',
      'title': 'How do I find micro purchase government contracts wins using SAM.gov (Eric '
               'Coffie)',
      'url': 'https://www.youtube.com/watch?v=AOa0-iEhmks&t=115s',
      'video_id': 'AOa0-iEhmks'},
     {'author': 'GovKidMethod',
      'channel': 'GovKidMethod',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:06](https://www.youtube.com/watch?v=nRXCetmIWUs&t=186s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Any questions in the comments it's very straightforward very simple I'm trying "
              'to make these gov con quick tips very bite-sized for you all so I hope they '
              "help consider subscribing it to the channel if you like gov con videos and I'll "
              'see you in the next one.',
      'timestamp': 186,
      'timestamp_label': '[00:03:06]',
      'timestamp_seconds': 186,
      'tip': "Any questions in the comments it's very straightforward very simple I'm trying "
             'to make these gov con quick tips very bite-sized for you all so I hope they help '
             "consider subscribing it to the channel if you like gov con videos and I'll see "
             'you in the next one.',
      'title': 'Search Beta.Sam.Gov by Set-Aside (WOSB, SDVOSB, 8(a), HUBZone etc) | GovCon '
               'Quick-Tips (GovKidMethod)',
      'url': 'https://www.youtube.com/watch?v=nRXCetmIWUs&t=186s',
      'video_id': 'nRXCetmIWUs'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:35](https://www.youtube.com/watch?v=ITZqqfI1Eig&t=935s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Understanding what they're asking for as well as understanding the flags so "
              'join my Facebook group these are definitely things I talk about more is to come '
              "govcom winners y'all are amazing don't forget everything is bull.",
      'timestamp': 935,
      'timestamp_label': '[00:15:35]',
      'timestamp_seconds': 935,
      'tip': "Understanding what they're asking for as well as understanding the flags so join "
             'my Facebook group these are definitely things I talk about more is to come '
             "govcom winners y'all are amazing don't forget everything is bull.",
      'title': 'I Got My Cage Code Now What? (Kizzy Parks)',
      'url': 'https://www.youtube.com/watch?v=ITZqqfI1Eig&t=935s',
      'video_id': 'ITZqqfI1Eig'}],
 9: [{'author': 'How To Sell To & Win Federal Government Contracts',
      'channel': 'How To Sell To & Win Federal Government Contracts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:23](https://www.youtube.com/watch?v=yp5LO51vPi8&t=323s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um in one uh sense, it is just simply a contract between two businesses um in a '
              'commercial transaction where standard commercial terms apply and um you know, a '
              'choice of law provision is included making whatever state law applicable.',
      'timestamp': 323,
      'timestamp_label': '[00:05:23]',
      'timestamp_seconds': 323,
      'tip': 'Um in one uh sense, it is just simply a contract between two businesses um in a '
             'commercial transaction where standard commercial terms apply and um you know, a '
             'choice of law provision is included making whatever state law applicable.',
      'title': 'Government Contracting - FAR Compliance - What Every Sub Needs To Know - Win '
               'Federal Contracts (How To Sell To & Win Federal Government Contracts)',
      'url': 'https://www.youtube.com/watch?v=yp5LO51vPi8&t=323s',
      'video_id': 'yp5LO51vPi8'},
     {'author': 'Dr. Wes Fisher',
      'channel': 'Dr. Wes Fisher',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:40](https://www.youtube.com/watch?v=7NhHddZW0kE&t=580s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I' I've already got my money's worth today. You know, just just a full "
              'disclosure, I had pushed and went all the way through everything. Registration, '
              'website, nakes codes, set aside, all of that stuff set up. Cage code, all of '
              "that's been done myself.",
      'timestamp': 580,
      'timestamp_label': '[00:09:40]',
      'timestamp_seconds': 580,
      'tip': "I' I've already got my money's worth today. You know, just just a full "
             'disclosure, I had pushed and went all the way through everything. Registration, '
             'website, nakes codes, set aside, all of that stuff set up. Cage code, all of '
             "that's been done myself.",
      'title': 'Is the Middleman Strategy LEGAL?! | Government Contracting FAR 52.219-14 '
               'Explained for Beginners (Dr. Wes Fisher)',
      'url': 'https://www.youtube.com/watch?v=7NhHddZW0kE&t=580s',
      'video_id': '7NhHddZW0kE'},
     {'author': 'FedBiz Access',
      'channel': 'FedBiz Access',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:20](https://www.youtube.com/watch?v=eEBn_eN0py8&t=260s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Awarded to out-of-state contractors contracts that received a single bid and '
              'contracts not publicly posted you also have access to our government '
              'contracting resource page.',
      'timestamp': 260,
      'timestamp_label': '[00:04:20]',
      'timestamp_seconds': 260,
      'tip': 'Awarded to out-of-state contractors contracts that received a single bid and '
             'contracts not publicly posted you also have access to our government contracting '
             'resource page.',
      'title': 'FedBiz Find | Government Contracting | Award History & New Opportunities '
               '(FedBiz Access)',
      'url': 'https://www.youtube.com/watch?v=eEBn_eN0py8&t=260s',
      'video_id': 'eEBn_eN0py8'},
     {'author': 'Win Government Contracts with GovSuccess',
      'channel': 'Win Government Contracts with GovSuccess',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=x7xmTiXnwQ4&t=21s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That role does not carry authority to change contractual price, quantity, '
              'delivery, or other terms. Before applying this to a real acquisition, check the '
              "current FAR, the agency's applicable deviation, and the solicitation or "
              'contract.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'That role does not carry authority to change contractual price, quantity, '
             'delivery, or other terms. Before applying this to a real acquisition, check the '
             "current FAR, the agency's applicable deviation, and the solicitation or "
             'contract.',
      'title': 'FAR PART 1 (Simplified) | Who Can Authorize the Work? (Win Government '
               'Contracts with GovSuccess)',
      'url': 'https://www.youtube.com/watch?v=x7xmTiXnwQ4&t=21s',
      'video_id': 'x7xmTiXnwQ4'},
     {'author': 'GovClose | DoD Contract Academy',
      'channel': 'GovClose | DoD Contract Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:45:22](https://www.youtube.com/watch?v=Qij-5QQmwc8&t=2722s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh Federal Acquisition Service is a sub agency to GSA, right? And a lot of you '
              'think of GSA as a contract vehicle. Some of you think of them as an agency. But '
              'um yeah, so this just makes me think that GSA they have a schedule.',
      'timestamp': 2722,
      'timestamp_label': '[00:45:22]',
      'timestamp_seconds': 2722,
      'tip': 'Uh Federal Acquisition Service is a sub agency to GSA, right? And a lot of you '
             'think of GSA as a contract vehicle. Some of you think of them as an agency. But '
             'um yeah, so this just makes me think that GSA they have a schedule.',
      'title': 'Does the #sdvosb Certification Help Win Government Contracts? (GovClose | DoD '
               'Contract Academy)',
      'url': 'https://www.youtube.com/watch?v=Qij-5QQmwc8&t=2722s',
      'video_id': 'Qij-5QQmwc8'},
     {'author': 'Government Contracting Strategist & Host',
      'channel': 'Government Contracting Strategist & Host',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=iTD46ZpHbdI&t=98s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Janitorial is moving on our state bid boards like crazy. It has jumped 25% in '
              "just one week. That's why I wanted to particularly focus on janitorial.",
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': 'Janitorial is moving on our state bid boards like crazy. It has jumped 25% in '
             "just one week. That's why I wanted to particularly focus on janitorial.",
      'title': 'Janitorial Government Contracts Up 25% | 5 SLED Bids to Watch | TWIP Ep. 42 '
               '(Government Contracting Strategist & Host)',
      'url': 'https://www.youtube.com/watch?v=iTD46ZpHbdI&t=98s',
      'video_id': 'iTD46ZpHbdI'},
     {'author': 'The Money Rules',
      'channel': 'The Money Rules',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:04](https://www.youtube.com/watch?v=rlj1s_mZ7uo&t=124s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The franchisor emails its agreement and disclosure document to the SBA, the SBA '
              'reviews brands in the order they arrive, and an eligible brand signs a '
              'certification and gets a code on the list.',
      'timestamp': 124,
      'timestamp_label': '[00:02:04]',
      'timestamp_seconds': 124,
      'tip': 'The franchisor emails its agreement and disclosure document to the SBA, the SBA '
             'reviews brands in the order they arrive, and an eligible brand signs a '
             'certification and gets a code on the list.',
      'title': 'SBA Franchise Directory 2026: Is Your Franchise on the SBA List? (The Money '
               'Rules)',
      'url': 'https://www.youtube.com/watch?v=rlj1s_mZ7uo&t=124s',
      'video_id': 'rlj1s_mZ7uo'},
     {'author': 'Public Contracting Institute (PCI)',
      'channel': 'Public Contracting Institute (PCI)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:08:54](https://www.youtube.com/watch?v=UV6zJLRHfHw&t=4134s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um each clause has a specific date so the government and contractors alike can '
              'know the exact contract requirement. The contract specific terms are typically '
              'set on the date the parties sign the agreement absent a later modification to '
              'the contract.',
      'timestamp': 4134,
      'timestamp_label': '[01:08:54]',
      'timestamp_seconds': 4134,
      'tip': 'Um each clause has a specific date so the government and contractors alike can '
             'know the exact contract requirement. The contract specific terms are typically '
             'set on the date the parties sign the agreement absent a later modification to '
             'the contract.',
      'title': 'GovCon 101 - A Guide to Navigating FAR Part 52 (Public Contracting Institute '
               '(PCI))',
      'url': 'https://www.youtube.com/watch?v=UV6zJLRHfHw&t=4134s',
      'video_id': 'UV6zJLRHfHw'},
     {'author': 'Fox Wade',
      'channel': 'Fox Wade',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:44](https://www.youtube.com/watch?v=Z2ZeI5rayvk&t=284s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Already seen that was the title before it's a blanket purchase agreement no uh "
              'but you can see here that the contract overall value for three years was one '
              'million 686.',
      'timestamp': 284,
      'timestamp_label': '[00:04:44]',
      'timestamp_seconds': 284,
      'tip': "Already seen that was the title before it's a blanket purchase agreement no uh "
             'but you can see here that the contract overall value for three years was one '
             'million 686.',
      'title': 'How to find what the government paid on previously awarded contracts! #govcon '
               '#governmentcontracting (Fox Wade)',
      'url': 'https://www.youtube.com/watch?v=Z2ZeI5rayvk&t=284s',
      'video_id': 'Z2ZeI5rayvk'},
     {'author': 'ASI Education',
      'channel': 'ASI Education',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:39](https://www.youtube.com/watch?v=jYYGaPkanFU&t=1899s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Rules of thumb for what constitutes a cardinal change and there's no agreement "
              "on that there's like I think I worked for a office that said if it's over 30%.",
      'timestamp': 1899,
      'timestamp_label': '[00:31:39]',
      'timestamp_seconds': 1899,
      'tip': "Rules of thumb for what constitutes a cardinal change and there's no agreement "
             "on that there's like I think I worked for a office that said if it's over 30%.",
      'title': 'Government Acquisition for Dummies - Prime Contractors & Subcontractors (ASI '
               'Education)',
      'url': 'https://www.youtube.com/watch?v=jYYGaPkanFU&t=1899s',
      'video_id': 'jYYGaPkanFU'},
     {'author': 'Sheenapreneur',
      'channel': 'Sheenapreneur',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:35](https://www.youtube.com/watch?v=MB8IFp5mwWc&t=335s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Federal Contracting local contract and corporate Contracting and something for '
              'my veterans based on my experience and based on experience of others that I '
              'know that are in the industry so until next time.',
      'timestamp': 335,
      'timestamp_label': '[00:05:35]',
      'timestamp_seconds': 335,
      'tip': 'Federal Contracting local contract and corporate Contracting and something for '
             'my veterans based on my experience and based on experience of others that I know '
             'that are in the industry so until next time.',
      'title': 'Prime Contractor or A Subcontractor (Sheenapreneur)',
      'url': 'https://www.youtube.com/watch?v=MB8IFp5mwWc&t=335s',
      'video_id': 'MB8IFp5mwWc'},
     {'author': 'SamSearch - AI for Government Contracting',
      'channel': 'SamSearch - AI for Government Contracting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=xeEO2U-Vy38&t=15s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "To win your first government contract let's get into it so with new government "
              "contractors they usually go for big contracts I don't blame them it looks so.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "To win your first government contract let's get into it so with new government "
             "contractors they usually go for big contracts I don't blame them it looks so.",
      'title': 'Simplified Acquisitions & Micro-Purchases Tutorial (SamSearch - AI for '
               'Government Contracting)',
      'url': 'https://www.youtube.com/watch?v=xeEO2U-Vy38&t=15s',
      'video_id': 'xeEO2U-Vy38'},
     {'author': 'SamSearch - AI for Government Contracting',
      'channel': 'SamSearch - AI for Government Contracting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=OmEqzgzoKlc&t=40s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Competition compared to federal government contracts less people on uh Texas '
              "State procurement websites than sam.gov so you're going to.",
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': 'Competition compared to federal government contracts less people on uh Texas '
             "State procurement websites than sam.gov so you're going to.",
      'title': 'How to Bid on Texas Government Contracts (SamSearch - AI for Government '
               'Contracting)',
      'url': 'https://www.youtube.com/watch?v=OmEqzgzoKlc&t=40s',
      'video_id': 'OmEqzgzoKlc'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:07:26](https://www.youtube.com/watch?v=386MNSeLv9E&t=4046s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's some dedication that's some dedication y'all however a person who is in "
              'an organization to help entrepreneurs especially those interested in Government '
              'Contracting and they have never won a government contract or been a part of '
              'Government Contracting.',
      'timestamp': 4046,
      'timestamp_label': '[01:07:26]',
      'timestamp_seconds': 4046,
      'tip': "That's some dedication that's some dedication y'all however a person who is in "
             'an organization to help entrepreneurs especially those interested in Government '
             'Contracting and they have never won a government contract or been a part of '
             'Government Contracting.',
      'title': 'How to Win Middleman Government Contracts in a Trump Economy (Kizzy Parks)',
      'url': 'https://www.youtube.com/watch?v=386MNSeLv9E&t=4046s',
      'video_id': '386MNSeLv9E'},
     {'author': 'Kizzy Parks',
      'channel': 'Kizzy Parks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=Ac9lYLwR6QQ&t=80s)',
      'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                   'government contract bid desk operations, lawful prime/sub teaming, and FAR '
                   'compliance (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s under $10,000 hey what's up Dawn what's up here's how it typically works and "
              "if you haven't checked out my book check out winners way book.",
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': "'s under $10,000 hey what's up Dawn what's up here's how it typically works and "
             "if you haven't checked out my book check out winners way book.",
      'title': 'How to Win Micro-Purchase Contracts with the Government For Beginners (Kizzy '
               'Parks)',
      'url': 'https://www.youtube.com/watch?v=Ac9lYLwR6QQ&t=80s',
      'video_id': 'Ac9lYLwR6QQ'}],
 10: [{'author': 'Humam Finding Sam',
       'channel': 'Humam Finding Sam',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:54](https://www.youtube.com/watch?v=T_HZxPdh7B8&t=414s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Success is through preparation. Master compliance requirements. Build strong '
               'capability statements and leverage platforms like SAM search to systematically '
               'identify and pursue opportunities. Begin developing your subcontracting '
               'pipeline now.',
       'timestamp': 414,
       'timestamp_label': '[00:06:54]',
       'timestamp_seconds': 414,
       'tip': 'Success is through preparation. Master compliance requirements. Build strong '
              'capability statements and leverage platforms like SAM search to systematically '
              'identify and pursue opportunities. Begin developing your subcontracting '
              'pipeline now.',
       'title': 'How to Win GovCon Contracts (2025) with Subcontracting (Humam Finding Sam)',
       'url': 'https://www.youtube.com/watch?v=T_HZxPdh7B8&t=414s',
       'video_id': 'T_HZxPdh7B8'},
      {'author': 'ASI Education',
       'channel': 'ASI Education',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:44](https://www.youtube.com/watch?v=_0QnHiuRnhc&t=104s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But either way, at its core, Part 12 implements FASA, the Federal Acquisition '
               'Streamlining Act of 1994, pushing government to buy commercial like the '
               "private sector. The RFO doesn't retreat from that. 201-1 for acquisitions "
               'under 9 million and not using an ordering vehicle.',
       'timestamp': 104,
       'timestamp_label': '[00:01:44]',
       'timestamp_seconds': 104,
       'tip': 'But either way, at its core, Part 12 implements FASA, the Federal Acquisition '
              'Streamlining Act of 1994, pushing government to buy commercial like the private '
              "sector. The RFO doesn't retreat from that. 201-1 for acquisitions under 9 "
              'million and not using an ordering vehicle.',
       'title': 'Mastering FAR Part 12: The Revolutionary FAR Overhaul (RFO) (ASI Education)',
       'url': 'https://www.youtube.com/watch?v=_0QnHiuRnhc&t=104s',
       'video_id': '_0QnHiuRnhc'},
      {'author': 'APMP',
       'channel': 'APMP',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:59](https://www.youtube.com/watch?v=MSvfidBACFs&t=59s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'For simpler bids, your brain is enough. For more complex ones, smart tools or '
               'even AI can help speed things up — just be sure to verify everything. '
               "Automation is no substitute for accuracy. Now that you've made sense of the "
               'structure, the real work begins.',
       'timestamp': 59,
       'timestamp_label': '[00:00:59]',
       'timestamp_seconds': 59,
       'tip': 'For simpler bids, your brain is enough. For more complex ones, smart tools or '
              'even AI can help speed things up — just be sure to verify everything. '
              "Automation is no substitute for accuracy. Now that you've made sense of the "
              'structure, the real work begins.',
       'title': 'Bid Teams: This Is How You Break Down an RFP Like a Pro (APMP)',
       'url': 'https://www.youtube.com/watch?v=MSvfidBACFs&t=59s',
       'video_id': 'MSvfidBACFs'},
      {'author': 'Fed Gov Today',
       'channel': 'Fed Gov Today',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:57](https://www.youtube.com/watch?v=MM4DJrI2Od0&t=237s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "AI is is that humans won't work for AI, rather AI will be working for humans "
               "and I dare say that's super important for the contracting and acquisition "
               'workforce as well.',
       'timestamp': 237,
       'timestamp_label': '[00:03:57]',
       'timestamp_seconds': 237,
       'tip': "AI is is that humans won't work for AI, rather AI will be working for humans "
              "and I dare say that's super important for the contracting and acquisition "
              'workforce as well.',
       'title': 'The New Rules of Federal Buying: How the FAR Overhaul Is Changing Everything '
                '(Fed Gov Today)',
       'url': 'https://www.youtube.com/watch?v=MM4DJrI2Od0&t=237s',
       'video_id': 'MM4DJrI2Od0'},
      {'author': 'The DLA Vendor Network (DVN)',
       'channel': 'The DLA Vendor Network (DVN)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:43](https://www.youtube.com/watch?v=YlwuuaCoHzQ&t=1063s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re manually bidding those contracts. That's why I say you want to have at "
               "least 100 national stock numbers that you've bid on in the past to use a "
               'system like this. So that helps you to scale your business instead of you you '
               'know you got to start somewhere.',
       'timestamp': 1063,
       'timestamp_label': '[00:17:43]',
       'timestamp_seconds': 1063,
       'tip': "'re manually bidding those contracts. That's why I say you want to have at "
              "least 100 national stock numbers that you've bid on in the past to use a system "
              'like this. So that helps you to scale your business instead of you you know you '
              'got to start somewhere.',
       'title': 'How to Automate DLA Bidding: The DLA BUS (DIBBS Batch Bidding)🚀 (The DLA '
                'Vendor Network (DVN))',
       'url': 'https://www.youtube.com/watch?v=YlwuuaCoHzQ&t=1063s',
       'video_id': 'YlwuuaCoHzQ'},
      {'author': 'The Promptly App',
       'channel': 'The Promptly App',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:37](https://www.youtube.com/watch?v=VvYb0nAHXrc&t=277s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Create an account and start building better prompts today. When you're ready "
               'for more, unlock the full proposal management success collection for just $9. '
               'No contracts, cancel anytime. Create your free account at the promptlyapp.',
       'timestamp': 277,
       'timestamp_label': '[00:04:37]',
       'timestamp_seconds': 277,
       'tip': "Create an account and start building better prompts today. When you're ready "
              'for more, unlock the full proposal management success collection for just $9. '
              'No contracts, cancel anytime. Create your free account at the promptlyapp.',
       'title': 'How to Create an RFP Compliance Matrix with AI | Promptly (The Promptly App)',
       'url': 'https://www.youtube.com/watch?v=VvYb0nAHXrc&t=277s',
       'video_id': 'VvYb0nAHXrc'},
      {'author': 'J. White - The Federal Code',
       'channel': 'J. White - The Federal Code',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=FYViP-mtnqI&t=20s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I've gotten really good at that allows you to win federal government contracts "
               'without actually doing the physical work yourself. One of the biggest reasons '
               'people struggle in government contracting, especially at the federal level, is '
               'they think a few things.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': "I've gotten really good at that allows you to win federal government contracts "
              'without actually doing the physical work yourself. One of the biggest reasons '
              'people struggle in government contracting, especially at the federal level, is '
              'they think a few things.',
       'title': 'How to Win Federal Contracts as a Middleman (Free Live Training) (J. White - '
                'The Federal Code)',
       'url': 'https://www.youtube.com/watch?v=FYViP-mtnqI&t=20s',
       'video_id': 'FYViP-mtnqI'},
      {'author': 'GovCon Empire with Derrick Green “Theo”',
       'channel': 'GovCon Empire with Derrick Green “Theo”',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:27:32](https://www.youtube.com/watch?v=h72zKiJRBe4&t=1652s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'F, United States Code, statutory requirements in contracting, and it will give '
               'you a whole list of things that you can literally sit there and read for a '
               'couple minutes to make your proposal stronger, to make your operation '
               'stronger.',
       'timestamp': 1652,
       'timestamp_label': '[00:27:32]',
       'timestamp_seconds': 1652,
       'tip': 'F, United States Code, statutory requirements in contracting, and it will give '
              'you a whole list of things that you can literally sit there and read for a '
              'couple minutes to make your proposal stronger, to make your operation stronger.',
       'title': 'The Middleman Lie in Government Contracting (What’s Legal vs What Gets You '
                'Debarred) (GovCon Empire with Derrick Green “Theo”)',
       'url': 'https://www.youtube.com/watch?v=h72zKiJRBe4&t=1652s',
       'video_id': 'h72zKiJRBe4'},
      {'author': 'Eric Coffie',
       'channel': 'Eric Coffie',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:31](https://www.youtube.com/watch?v=8-4Lml2bZj4&t=91s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Remember, guys, when I was doing GovCon, a lot of times the contracting people '
               "would come to me and ask me how to do things because they weren't up to speed "
               'on all the new training.',
       'timestamp': 91,
       'timestamp_label': '[00:01:31]',
       'timestamp_seconds': 91,
       'tip': 'Remember, guys, when I was doing GovCon, a lot of times the contracting people '
              "would come to me and ask me how to do things because they weren't up to speed "
              'on all the new training.',
       'title': 'Similarly Situated Entity helps Limitations on SUBCONTRACTING for small firms '
                '- Eric Coffie (Eric Coffie)',
       'url': 'https://www.youtube.com/watch?v=8-4Lml2bZj4&t=91s',
       'video_id': '8-4Lml2bZj4'},
      {'author': 'Kizzy Parks',
       'channel': 'Kizzy Parks',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=etvo2gL7_Cs&t=15s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Telling you right now an agency is not going to go with your bid you want a '
               "huge windfall you think that's how everybody operates because you've read.",
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Telling you right now an agency is not going to go with your bid you want a '
              "huge windfall you think that's how everybody operates because you've read.",
       'title': 'How to Price Government Contracts To Win Fast (Kizzy Parks)',
       'url': 'https://www.youtube.com/watch?v=etvo2gL7_Cs&t=15s',
       'video_id': 'etvo2gL7_Cs'},
      {'author': 'Neil McDonnell',
       'channel': 'Neil McDonnell',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:27:49](https://www.youtube.com/watch?v=zqg5q_pZvdc&t=1669s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "SAM, uh but I can't put it all into this training. And so I'm building this "
               "SAM pipeline system or course called SAM Mastery. And if that's something "
               "you're interested in seeing when I drop it, go to govconchamber. Um when you "
               'go there, just join the waitlist.',
       'timestamp': 1669,
       'timestamp_label': '[00:27:49]',
       'timestamp_seconds': 1669,
       'tip': "SAM, uh but I can't put it all into this training. And so I'm building this SAM "
              "pipeline system or course called SAM Mastery. And if that's something you're "
              'interested in seeing when I drop it, go to govconchamber. Um when you go there, '
              'just join the waitlist.',
       'title': 'Subcontracting with Prime Government Contractors is a Must (Neil McDonnell)',
       'url': 'https://www.youtube.com/watch?v=zqg5q_pZvdc&t=1669s',
       'video_id': 'zqg5q_pZvdc'},
      {'author': 'The DLA Vendor Network (DVN)',
       'channel': 'The DLA Vendor Network (DVN)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:06](https://www.youtube.com/watch?v=YNtu76ny5MI&t=726s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Supply chain 4. artificial intelligence and machine learning the dla is '
               'leveraging AI and ml to automate processes improve predictive maintenance and '
               'enhance supply chain planning and execution.',
       'timestamp': 726,
       'timestamp_label': '[00:12:06]',
       'timestamp_seconds': 726,
       'tip': 'Supply chain 4. artificial intelligence and machine learning the dla is '
              'leveraging AI and ml to automate processes improve predictive maintenance and '
              'enhance supply chain planning and execution.',
       'title': '🎓How To Sell to the DLA | DIBBS 🏆The DLA Need to Know Guide (The DLA Vendor '
                'Network (DVN))',
       'url': 'https://www.youtube.com/watch?v=YNtu76ny5MI&t=726s',
       'video_id': 'YNtu76ny5MI'},
      {'author': 'How To Sell To & Win Federal Government Contracts',
       'channel': 'How To Sell To & Win Federal Government Contracts',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=h1yszOmFw3w&t=15s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Federal acquisition regulations we are coming to you live today from '
               "Washington DC and we're glad you all could make it okay A bit about this "
               'series as usual.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Federal acquisition regulations we are coming to you live today from Washington '
              "DC and we're glad you all could make it okay A bit about this series as usual.",
       'title': '2024 FAR Part 52 - Solicitation Provisions And Contract Clauses (How To Sell '
                'To & Win Federal Government Contracts)',
       'url': 'https://www.youtube.com/watch?v=h1yszOmFw3w&t=15s',
       'video_id': 'h1yszOmFw3w'},
      {'author': 'Theodore Watson',
       'channel': 'Theodore Watson',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:05](https://www.youtube.com/watch?v=28K_7987r8w&t=665s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Contractors out there you might want to pay attention to these five tips if '
               'you have any additional questions or concerns feel free to reach out to us one '
               'eight six six six zero one five five one eight again this is theodore watson '
               'from watson and associates.',
       'timestamp': 665,
       'timestamp_label': '[00:11:05]',
       'timestamp_seconds': 665,
       'tip': 'Contractors out there you might want to pay attention to these five tips if you '
              'have any additional questions or concerns feel free to reach out to us one '
              'eight six six six zero one five five one eight again this is theodore watson '
              'from watson and associates.',
       'title': 'FAR Limitations on Subcontracting Lawyers & 13 CFR 125.6 (Theodore Watson)',
       'url': 'https://www.youtube.com/watch?v=28K_7987r8w&t=665s',
       'video_id': '28K_7987r8w'},
      {'author': 'Kizzy Parks',
       'channel': 'Kizzy Parks',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:24](https://www.youtube.com/watch?v=L0SM3XAM3IE&t=624s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Services the other place to go and to check out if they don't have any "
               "archival information I'm going to show you this place in just one second I'm "
               'going to share my screen again and that is by.gsa.gov.',
       'timestamp': 624,
       'timestamp_label': '[00:10:24]',
       'timestamp_seconds': 624,
       'tip': "Services the other place to go and to check out if they don't have any archival "
              "information I'm going to show you this place in just one second I'm going to "
              'share my screen again and that is by.gsa.gov.',
       'title': 'How To Find Price Paid For Past Contracts | Learn About Pricing in Gov Con '
                '(Kizzy Parks)',
       'url': 'https://www.youtube.com/watch?v=L0SM3XAM3IE&t=624s',
       'video_id': 'L0SM3XAM3IE'}],
 11: [{'author': 'Solvability',
       'channel': 'Solvability',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:44](https://www.youtube.com/watch?v=EBQwejU6UUQ&t=644s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re a prime contractor yourself working cost plus contracts or cost type "
               'contracts and some contracting officer requested DCAA to do a pre-award survey '
               'or accounting system review and you pass that and they will send you an email '
               'after a little bit of work.',
       'timestamp': 644,
       'timestamp_label': '[00:10:44]',
       'timestamp_seconds': 644,
       'tip': "'re a prime contractor yourself working cost plus contracts or cost type "
              'contracts and some contracting officer requested DCAA to do a pre-award survey '
              'or accounting system review and you pass that and they will send you an email '
              'after a little bit of work.',
       'title': 'GovCon Accounting Explained: How to Price, Bill and Win Contracts '
                '(Solvability)',
       'url': 'https://www.youtube.com/watch?v=EBQwejU6UUQ&t=644s',
       'video_id': 'EBQwejU6UUQ'},
      {'author': 'THE FEDERAL PROPOSAL EXPERTS',
       'channel': 'THE FEDERAL PROPOSAL EXPERTS',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:49](https://www.youtube.com/watch?v=zeJUuxLmj6s&t=109s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Make a proposal compliance matrix for your proposal effort. It will be given '
               'to the entire team of writers and reviewers and the proposal manager and your '
               'contracts manager.',
       'timestamp': 109,
       'timestamp_label': '[00:01:49]',
       'timestamp_seconds': 109,
       'tip': 'Make a proposal compliance matrix for your proposal effort. It will be given to '
              'the entire team of writers and reviewers and the proposal manager and your '
              'contracts manager.',
       'title': 'How to Create and Use a Proposal Compliance Matrix (THE FEDERAL PROPOSAL '
                'EXPERTS)',
       'url': 'https://www.youtube.com/watch?v=zeJUuxLmj6s&t=109s',
       'video_id': 'zeJUuxLmj6s'},
      {'author': 'How To Sell To & Win Federal Government Contracts',
       'channel': 'How To Sell To & Win Federal Government Contracts',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:19:13](https://www.youtube.com/watch?v=IP2vqKHZqlE&t=1153s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Uh what of the products and services that you use are really specific to your '
               'agency versus what can be met by commercial item contracting.',
       'timestamp': 1153,
       'timestamp_label': '[00:19:13]',
       'timestamp_seconds': 1153,
       'tip': 'Uh what of the products and services that you use are really specific to your '
              'agency versus what can be met by commercial item contracting.',
       'title': 'Government Contracting - DFARS Part 212 - Acquisition of Commercial Items - '
                'Win Federal Contracts (How To Sell To & Win Federal Government Contracts)',
       'url': 'https://www.youtube.com/watch?v=IP2vqKHZqlE&t=1153s',
       'video_id': 'IP2vqKHZqlE'},
      {'author': 'Kizzy Parks',
       'channel': 'Kizzy Parks',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:50](https://www.youtube.com/watch?v=qVThWm83wus&t=50s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And then you need to have a cage code to be a prime contractor. So when it '
               'comes to this space, it is vital that you are ready. You must be government '
               "ready. If you say to yourself, well, I just want a middleman. Well, that's "
               'called subcontracting out the work.',
       'timestamp': 50,
       'timestamp_label': '[00:00:50]',
       'timestamp_seconds': 50,
       'tip': 'And then you need to have a cage code to be a prime contractor. So when it '
              'comes to this space, it is vital that you are ready. You must be government '
              "ready. If you say to yourself, well, I just want a middleman. Well, that's "
              'called subcontracting out the work.',
       'title': 'How To Win Government Contracts In 2026 | Beginners Guide 2026 (Kizzy Parks)',
       'url': 'https://www.youtube.com/watch?v=qVThWm83wus&t=50s',
       'video_id': 'qVThWm83wus'},
      {'author': 'Public Contracting Institute (PCI)',
       'channel': 'Public Contracting Institute (PCI)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:46:13](https://www.youtube.com/watch?v=NB57wtT4xfs&t=2773s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'They team again almost the exact same solicitation or same teaming agreement. '
               'Information experts gets the prime contract award. This time though they '
               "couldn't close the deal on the sub contract. And so information experts walked "
               'away.',
       'timestamp': 2773,
       'timestamp_label': '[00:46:13]',
       'timestamp_seconds': 2773,
       'tip': 'They team again almost the exact same solicitation or same teaming agreement. '
              'Information experts gets the prime contract award. This time though they '
              "couldn't close the deal on the sub contract. And so information experts walked "
              'away.',
       'title': 'GovCon 101- Teaming (Public Contracting Institute (PCI))',
       'url': 'https://www.youtube.com/watch?v=NB57wtT4xfs&t=2773s',
       'video_id': 'NB57wtT4xfs'},
      {'author': 'Federal Contracts Lab',
       'channel': 'Federal Contracts Lab',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:20](https://www.youtube.com/watch?v=3eoJWm0WffU&t=80s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A direct contract with the government. In other words, they want to be a prime '
               'contractor. On the surface, it makes sense. Your company name is on the award. '
               'You build past performance. But here is the part most beginners miss. Prime '
               'contracting is not just an opportunity.',
       'timestamp': 80,
       'timestamp_label': '[00:01:20]',
       'timestamp_seconds': 80,
       'tip': 'A direct contract with the government. In other words, they want to be a prime '
              'contractor. On the surface, it makes sense. Your company name is on the award. '
              'You build past performance. But here is the part most beginners miss. Prime '
              'contracting is not just an opportunity.',
       'title': 'Prime vs Subcontractor: Which Path Should Beginners Choose in GovCon? '
                '(Federal Contracts Lab)',
       'url': 'https://www.youtube.com/watch?v=3eoJWm0WffU&t=80s',
       'video_id': '3eoJWm0WffU'},
      {'author': 'Win Government Contracts with GovSuccess',
       'channel': 'Win Government Contracts with GovSuccess',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:47](https://www.youtube.com/watch?v=z7tDxORX_pQ&t=47s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'For a contractor, the practical starting point is the solicitation: identify '
               "the program's acquisition approach, required system capabilities, development "
               'stages, and management requirements before deciding what your team must '
               'propose.',
       'timestamp': 47,
       'timestamp_label': '[00:00:47]',
       'timestamp_seconds': 47,
       'tip': 'For a contractor, the practical starting point is the solicitation: identify '
              "the program's acquisition approach, required system capabilities, development "
              'stages, and management requirements before deciding what your team must '
              'propose.',
       'title': 'FAR Part 34 (Simplified) | Connect Scope, Schedule, and Cost Before You '
                'Commit (Win Government Contracts with GovSuccess)',
       'url': 'https://www.youtube.com/watch?v=z7tDxORX_pQ&t=47s',
       'video_id': 'z7tDxORX_pQ'},
      {'author': 'ASI Education',
       'channel': 'ASI Education',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:49](https://www.youtube.com/watch?v=MTy_zJd0RsY&t=49s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'For example a US Air Force Contracting officer or Co will understand the same '
               'types of requirements as a US Forestry Co but each agency also has their own.',
       'timestamp': 49,
       'timestamp_label': '[00:00:49]',
       'timestamp_seconds': 49,
       'tip': 'For example a US Air Force Contracting officer or Co will understand the same '
              'types of requirements as a US Forestry Co but each agency also has their own.',
       'title': 'The Federal Acquisition Regulation (FAR) Explained in 5 Minutes (ASI '
                'Education)',
       'url': 'https://www.youtube.com/watch?v=MTy_zJd0RsY&t=49s',
       'video_id': 'MTy_zJd0RsY'},
      {'author': 'Natalie Rosario | GovCon Coach',
       'channel': 'Natalie Rosario | GovCon Coach',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:17](https://www.youtube.com/watch?v=G44VRBscagY&t=197s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Now, once I hire them as an employee, I'm only do what is required in the "
               "contract. So, I'm not going to provide any employee handbooks or any "
               "additional extra perks as an employer, because I'm just trying to be compliant "
               'with the contract.',
       'timestamp': 197,
       'timestamp_label': '[00:03:17]',
       'timestamp_seconds': 197,
       'tip': "Now, once I hire them as an employee, I'm only do what is required in the "
              "contract. So, I'm not going to provide any employee handbooks or any additional "
              "extra perks as an employer, because I'm just trying to be compliant with the "
              'contract.',
       'title': 'UNDERSTANDING LIMTATIONS TO SUBCONTRACTING -The FPF Academyx (Natalie Rosario '
                '| GovCon Coach)',
       'url': 'https://www.youtube.com/watch?v=G44VRBscagY&t=197s',
       'video_id': 'G44VRBscagY'},
      {'author': 'Streamline Government Contracts, LLC',
       'channel': 'Streamline Government Contracts, LLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:03](https://www.youtube.com/watch?v=W-f5dCQEEkE&t=903s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Terminates so what that means is you still can't bid on the solicitation even "
               'if another company um even if another company um you know uh wants to team '
               'with you so so again it really is something that should not be overlocked.',
       'timestamp': 903,
       'timestamp_label': '[00:15:03]',
       'timestamp_seconds': 903,
       'tip': "Terminates so what that means is you still can't bid on the solicitation even "
              'if another company um even if another company um you know uh wants to team with '
              'you so so again it really is something that should not be overlocked.',
       'title': "Tips of the Trade: Negotiating Teaming Agreements - Subcontractors' "
                'Perspective (Streamline Government Contracts, LLC)',
       'url': 'https://www.youtube.com/watch?v=W-f5dCQEEkE&t=903s',
       'video_id': 'W-f5dCQEEkE'},
      {'author': 'Eric Coffie',
       'channel': 'Eric Coffie',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:41](https://www.youtube.com/watch?v=JVBkE6J1jPc&t=461s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Plays and you could probably start off at a much smaller scale where maybe '
               "you're more comfortable spill some past performance build some history and "
               'start working with agencies and start earning money today alright thanks for '
               "watching we'll see you next time.",
       'timestamp': 461,
       'timestamp_label': '[00:07:41]',
       'timestamp_seconds': 461,
       'tip': 'Plays and you could probably start off at a much smaller scale where maybe '
              "you're more comfortable spill some past performance build some history and "
              'start working with agencies and start earning money today alright thanks for '
              "watching we'll see you next time.",
       'title': 'Low hanging fruit contracts (SAP) Simplified Acquisition Procedures - Eric '
                'Coffie (Eric Coffie)',
       'url': 'https://www.youtube.com/watch?v=JVBkE6J1jPc&t=461s',
       'video_id': 'JVBkE6J1jPc'},
      {'author': 'Theodore Watson',
       'channel': 'Theodore Watson',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:18](https://www.youtube.com/watch?v=k1ZkyITmwWM&t=138s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Obvious problems with the relationships or sometimes the not so obvious '
               'problems the primary regulation that deals with affiliation is 13 cfr 121.103.',
       'timestamp': 138,
       'timestamp_label': '[00:02:18]',
       'timestamp_seconds': 138,
       'tip': 'Obvious problems with the relationships or sometimes the not so obvious '
              'problems the primary regulation that deals with affiliation is 13 cfr 121.103.',
       'title': 'SBA Affiliation Rules 13 CFR 121.103 Ostensible Contractor Rule Lawyers. SBA '
                'OHA Appeal Lawyers (Theodore Watson)',
       'url': 'https://www.youtube.com/watch?v=k1ZkyITmwWM&t=138s',
       'video_id': 'k1ZkyITmwWM'},
      {'author': 'Kizzy Parks',
       'channel': 'Kizzy Parks',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:03](https://www.youtube.com/watch?v=kejmg4Gzuuc&t=123s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Business set aside so let's dig deep into this so from here they talk about "
               'the contractor must own operate and or lease facilities that means you can.',
       'timestamp': 123,
       'timestamp_label': '[00:02:03]',
       'timestamp_seconds': 123,
       'tip': "Business set aside so let's dig deep into this so from here they talk about the "
              'contractor must own operate and or lease facilities that means you can.',
       'title': 'How to Make Money as a Middleman in Government Contracts (2025) (Kizzy Parks)',
       'url': 'https://www.youtube.com/watch?v=kejmg4Gzuuc&t=123s',
       'video_id': 'kejmg4Gzuuc'},
      {'author': 'Eric Coffie',
       'channel': 'Eric Coffie',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:08](https://www.youtube.com/watch?v=Hr_U9z1xK2g&t=128s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Still going to be pushing out and publishing regular content but this is a '
               "different level where we're actually going to be just grabbing the q a "
               "sections that we're doing and sharing them with everybody thank you so much "
               'for watching.',
       'timestamp': 128,
       'timestamp_label': '[00:02:08]',
       'timestamp_seconds': 128,
       'tip': 'Still going to be pushing out and publishing regular content but this is a '
              "different level where we're actually going to be just grabbing the q a sections "
              "that we're doing and sharing them with everybody thank you so much for "
              'watching.',
       'title': 'How to get AWARD Data from USA Spending? (Eric Coffie)',
       'url': 'https://www.youtube.com/watch?v=Hr_U9z1xK2g&t=128s',
       'video_id': 'Hr_U9z1xK2g'},
      {'author': 'SEMSCIO',
       'channel': 'SEMSCIO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:31](https://www.youtube.com/watch?v=rRWCLLWqrV0&t=31s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A valid cage or end cage code is necessary for completing the SAM. So this '
               "code is a five character alpha numeric classifier and it's actually issued by "
               'the DA, the Defense Logistics Agency for US entities engaged in government '
               'contracts. So, when you go to submit your SAM.',
       'timestamp': 31,
       'timestamp_label': '[00:00:31]',
       'timestamp_seconds': 31,
       'tip': 'A valid cage or end cage code is necessary for completing the SAM. So this code '
              "is a five character alpha numeric classifier and it's actually issued by the "
              'DA, the Defense Logistics Agency for US entities engaged in government '
              'contracts. So, when you go to submit your SAM.',
       'title': 'Sam.gov registration: CAGE & NCAGE Codes - Colleen Spiegel (SEMSCIO)',
       'url': 'https://www.youtube.com/watch?v=rRWCLLWqrV0&t=31s',
       'video_id': 'rRWCLLWqrV0'}],
 12: [{'author': 'FedOpp',
       'channel': 'FedOpp',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:07](https://www.youtube.com/watch?v=iTxJkLPYuqc&t=127s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Pick your answers for affirmative action, previous contracts, disputes, and '
               'child labor. Quote for cage uses your match profile cage when left blank. '
               'Enter the quantity, your unit price, and delivery days. Bid type starts at bid '
               'without exception.',
       'timestamp': 127,
       'timestamp_label': '[00:02:07]',
       'timestamp_seconds': 127,
       'tip': 'Pick your answers for affirmative action, previous contracts, disputes, and '
              'child labor. Quote for cage uses your match profile cage when left blank. Enter '
              'the quantity, your unit price, and delivery days. Bid type starts at bid '
              'without exception.',
       'title': 'FedOpp DIBBS Batch Quote File: Build It, Check It, Upload It on DIBBS '
                '(FedOpp)',
       'url': 'https://www.youtube.com/watch?v=iTxJkLPYuqc&t=127s',
       'video_id': 'iTxJkLPYuqc'},
      {'author': 'Diamond Hunter Enterprises',
       'channel': 'Diamond Hunter Enterprises',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:42](https://www.youtube.com/watch?v=-0giDdnv0RA&t=522s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, don\'t just look at me and think, "Oh, she\'s a multi-millionaire." Bid on '
               "opportunities before hitting these damn streets. Y'all remember, contracting "
               "officers is your plug. So, here's your action plan.",
       'timestamp': 522,
       'timestamp_label': '[00:08:42]',
       'timestamp_seconds': 522,
       'tip': 'So, don\'t just look at me and think, "Oh, she\'s a multi-millionaire." Bid on '
              "opportunities before hitting these damn streets. Y'all remember, contracting "
              "officers is your plug. So, here's your action plan.",
       'title': 'HUBZone Certification Program 2026 | 8a, SBA Small Business Set-Asides '
                'Explained (Diamond Hunter Enterprises)',
       'url': 'https://www.youtube.com/watch?v=-0giDdnv0RA&t=522s',
       'video_id': '-0giDdnv0RA'},
      {'author': 'Kizzy Parks',
       'channel': 'Kizzy Parks',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:45:00](https://www.youtube.com/watch?v=BZyPDVXuMMk&t=2700s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Now is the time to take full advantage to win contracts. There's no reason you "
               "can't win a contract [snorts] for leasing. Get a cage code and then you're "
               "going to have to start you have to look to see what they're leasing because of "
               'everything with Doge.',
       'timestamp': 2700,
       'timestamp_label': '[00:45:00]',
       'timestamp_seconds': 2700,
       'tip': "Now is the time to take full advantage to win contracts. There's no reason you "
              "can't win a contract [snorts] for leasing. Get a cage code and then you're "
              "going to have to start you have to look to see what they're leasing because of "
              'everything with Doge.',
       'title': 'How to Win Government Contracts in 2026 as a Beginner (Kizzy Parks)',
       'url': 'https://www.youtube.com/watch?v=BZyPDVXuMMk&t=2700s',
       'video_id': 'BZyPDVXuMMk'},
      {'author': 'Win Government Contracts with GovSuccess',
       'channel': 'Win Government Contracts with GovSuccess',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:35](https://www.youtube.com/watch?v=QvsXldnQyAg&t=275s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Use the practical exercise to find one gap your team can close this week. '
               'Explore GovAssessment at govsuccess. It does not approve a contract action, '
               'certify compliance, or guarantee an award.',
       'timestamp': 275,
       'timestamp_label': '[00:04:35]',
       'timestamp_seconds': 275,
       'tip': 'Use the practical exercise to find one gap your team can close this week. '
              'Explore GovAssessment at govsuccess. It does not approve a contract action, '
              'certify compliance, or guarantee an award.',
       'title': 'FAR Part 47 (Simplified) | Align Delivery, Freight, and Risk Before Shipment '
                '(Win Government Contracts with GovSuccess)',
       'url': 'https://www.youtube.com/watch?v=QvsXldnQyAg&t=275s',
       'video_id': 'QvsXldnQyAg'},
      {'author': 'Tris10 @ MeND',
       'channel': 'Tris10 @ MeND',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:30](https://www.youtube.com/watch?v=v4ulUMKE5xA&t=990s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Keeping track of how many bids we submit per week, per month, and so on. But '
               'also going a step further, when the government comes back to you, maybe they '
               'ask for a trace, you can tag it as a trace. Or when you do win that award, you '
               'can tag it as an award one.',
       'timestamp': 990,
       'timestamp_label': '[00:16:30]',
       'timestamp_seconds': 990,
       'tip': 'Keeping track of how many bids we submit per week, per month, and so on. But '
              'also going a step further, when the government comes back to you, maybe they '
              'ask for a trace, you can tag it as a trace. Or when you do win that award, you '
              'can tag it as an award one.',
       'title': 'How to Bid on DLA / DIBBS and Win in 2025 - Government Contracting (Tris10 @ '
                'MeND)',
       'url': 'https://www.youtube.com/watch?v=v4ulUMKE5xA&t=990s',
       'video_id': 'v4ulUMKE5xA'},
      {'author': 'Win the Bid',
       'channel': 'Win the Bid',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=roNNP4jeQpc&t=21s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'New Jersey, New York, and Pennsylvania, and a weekly routine you can start '
               'this week. Most local governments buy in two ways. Smaller purchases are done '
               'with quotes where the buyer asks a few businesses for a price. Bigger '
               'purchases go out as a formal public bid.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'New Jersey, New York, and Pennsylvania, and a weekly routine you can start this '
              'week. Most local governments buy in two ways. Smaller purchases are done with '
              'quotes where the buyer asks a few businesses for a price. Bigger purchases go '
              'out as a formal public bid.',
       'title': 'How to Find Local Government Contracts (Counties, Towns and Schools) (Win the '
                'Bid)',
       'url': 'https://www.youtube.com/watch?v=roNNP4jeQpc&t=21s',
       'video_id': 'roNNP4jeQpc'},
      {'author': 'TendersPage Corp.',
       'channel': 'TendersPage Corp.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:18](https://www.youtube.com/watch?v=xobcboYBB6w&t=318s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Track of the latest government procurements there's always plenty of work the "
               "government needs done and there's no reason to deny yourself a piece of that "
               'set aside action so let me give you the takeaway the federal.',
       'timestamp': 318,
       'timestamp_label': '[00:05:18]',
       'timestamp_seconds': 318,
       'tip': "Track of the latest government procurements there's always plenty of work the "
              "government needs done and there's no reason to deny yourself a piece of that "
              'set aside action so let me give you the takeaway the federal.',
       'title': 'Simplified acquisition threshold - Federal Micro Purchases for small '
                'businesses (TendersPage Corp.)',
       'url': 'https://www.youtube.com/watch?v=xobcboYBB6w&t=318s',
       'video_id': 'xobcboYBB6w'},
      {'author': 'myContractScout',
       'channel': 'myContractScout',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:33](https://www.youtube.com/watch?v=SeWe_WAhyVg&t=573s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'My Contract Scout AI can help you out, but you can get started by yourself '
               'right here. And this is free to look at DLA DIBBS all day long. So, you can '
               'start practicing on finding opportunities.',
       'timestamp': 573,
       'timestamp_label': '[00:09:33]',
       'timestamp_seconds': 573,
       'tip': 'My Contract Scout AI can help you out, but you can get started by yourself '
              'right here. And this is free to look at DLA DIBBS all day long. So, you can '
              'start practicing on finding opportunities.',
       'title': 'How to Find 400+ Government Contracts on DLA DIBBS (myContractScout)',
       'url': 'https://www.youtube.com/watch?v=SeWe_WAhyVg&t=573s',
       'video_id': 'SeWe_WAhyVg'},
      {'author': 'Presales Talk',
       'channel': 'Presales Talk',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:44](https://www.youtube.com/watch?v=V5HydwGhK8o&t=464s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'When we getting fit to go with this bid then we will go with the kickoff. It '
               'is actually internal kickoff meetings with the stakeholders to plan the '
               'response. When I say meeting with the stakeholders to plan the response, what '
               'is your understanding?',
       'timestamp': 464,
       'timestamp_label': '[00:07:44]',
       'timestamp_seconds': 464,
       'tip': 'When we getting fit to go with this bid then we will go with the kickoff. It is '
              'actually internal kickoff meetings with the stakeholders to plan the response. '
              'When I say meeting with the stakeholders to plan the response, what is your '
              'understanding?',
       'title': 'Bid Management Part 2 | RFP Analysis, Compliance Matrix & Clarification '
                'Process | Presales Training (Presales Talk)',
       'url': 'https://www.youtube.com/watch?v=V5HydwGhK8o&t=464s',
       'video_id': 'V5HydwGhK8o'},
      {'author': 'Loocey DLA & GovCon',
       'channel': 'Loocey DLA & GovCon',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:24](https://www.youtube.com/watch?v=LzmJyrGyMBw&t=24s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'ll walk you through how to filter and find RFQS that do not already have "
               'specified approved sources or manufacturers, hence are open for other '
               'manufacturers. To bid and manufacture these parts to start, go to DA RFQS and '
               "let's add a filter to show us these specific RFQS.",
       'timestamp': 24,
       'timestamp_label': '[00:00:24]',
       'timestamp_seconds': 24,
       'tip': "'ll walk you through how to filter and find RFQS that do not already have "
              'specified approved sources or manufacturers, hence are open for other '
              'manufacturers. To bid and manufacture these parts to start, go to DA RFQS and '
              "let's add a filter to show us these specific RFQS.",
       'title': 'How To Find DLA RFQs For Manufacturing / AMSC (RFQs With No Approved Sources) '
                '– DLA/DIBBS (Loocey DLA & GovCon)',
       'url': 'https://www.youtube.com/watch?v=LzmJyrGyMBw&t=24s',
       'video_id': 'LzmJyrGyMBw'},
      {'author': 'Business Cash Now',
       'channel': 'Business Cash Now',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:02](https://www.youtube.com/watch?v=4V1zq5q3VuQ&t=122s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Government or saw no government already and do not have enough working capital '
               'to fund your purchase orders or your accounts receivable please use the '
               "clickable link to my left or there's a toll-free number you'll see also thanks "
               'again and have a great day bye-bye.',
       'timestamp': 122,
       'timestamp_label': '[00:02:02]',
       'timestamp_seconds': 122,
       'tip': 'Government or saw no government already and do not have enough working capital '
              'to fund your purchase orders or your accounts receivable please use the '
              "clickable link to my left or there's a toll-free number you'll see also thanks "
              'again and have a great day bye-bye.',
       'title': 'Government Contract Invoice Factoring and PO Financing (Business Cash Now)',
       'url': 'https://www.youtube.com/watch?v=4V1zq5q3VuQ&t=122s',
       'video_id': '4V1zq5q3VuQ'},
      {'author': 'PilieroMazza PLLC',
       'channel': 'PilieroMazza PLLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:53:18](https://www.youtube.com/watch?v=i9prjadeAyM&t=3198s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Questions so um thank you everybody if you don't have any other questions "
               "we'll close out the webinar thank you megan thank you everybody and have a "
               'nice day thank you bye.',
       'timestamp': 3198,
       'timestamp_label': '[00:53:18]',
       'timestamp_seconds': 3198,
       'tip': "Questions so um thank you everybody if you don't have any other questions we'll "
              'close out the webinar thank you megan thank you everybody and have a nice day '
              'thank you bye.',
       'title': 'Limitations on Subcontracting: Key Updates and Tips for Compliance '
                '(PilieroMazza PLLC)',
       'url': 'https://www.youtube.com/watch?v=i9prjadeAyM&t=3198s',
       'video_id': 'i9prjadeAyM'},
      {'author': 'Fed Biz Exchange',
       'channel': 'Fed Biz Exchange',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:05](https://www.youtube.com/watch?v=kgPkC78OKzs&t=605s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Do not want to do management consulting of people and large situations and '
               'quite frankly I think this is the smarter thing to do while you are still '
               'involved in your career.',
       'timestamp': 605,
       'timestamp_label': '[00:10:05]',
       'timestamp_seconds': 605,
       'tip': 'Do not want to do management consulting of people and large situations and '
              'quite frankly I think this is the smarter thing to do while you are still '
              'involved in your career.',
       'title': 'Win Government Contracts with the Consultant Middle Man Business Model (Fed '
                'Biz Exchange)',
       'url': 'https://www.youtube.com/watch?v=kgPkC78OKzs&t=605s',
       'video_id': 'kgPkC78OKzs'},
      {'author': 'How To Sell To & Win Federal Government Contracts',
       'channel': 'How To Sell To & Win Federal Government Contracts',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:45:23](https://www.youtube.com/watch?v=36eRQkU2X_I&t=2723s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Boe okay this also doesn't say anything about um about how much um dollars you "
               'spend annually or the next 12 months uh on subcontracts or purchase orders '
               'this is sales this is your sales not your buys okay next.',
       'timestamp': 2723,
       'timestamp_label': '[00:45:23]',
       'timestamp_seconds': 2723,
       'tip': "Boe okay this also doesn't say anything about um about how much um dollars you "
              'spend annually or the next 12 months uh on subcontracts or purchase orders this '
              'is sales this is your sales not your buys okay next.',
       'title': 'Government Contacting - FAR Part 44 - Subcontracting Policies and Procedures '
                '- Win Federal Contracts (How To Sell To & Win Federal Government Contracts)',
       'url': 'https://www.youtube.com/watch?v=36eRQkU2X_I&t=2723s',
       'video_id': '36eRQkU2X_I'},
      {'author': 'Acquisition Pro Tips',
       'channel': 'Acquisition Pro Tips',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:37](https://www.youtube.com/watch?v=WXCymE9NjBg&t=637s)',
       'relevance': 'Attributed practitioner commentary on federal `SAM.gov` & municipal '
                    'government contract bid desk operations, lawful prime/sub teaming, and '
                    'FAR compliance (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Do it right the first time. So, let's wrap this video up with a few "
               'acquisition pro tips. Here are your pro tips for WAFT success. Number one, get '
               'a valid cage code or end cage code before you start. Number two, match invoice '
               'type to the contract every time.',
       'timestamp': 637,
       'timestamp_label': '[00:10:37]',
       'timestamp_seconds': 637,
       'tip': "Do it right the first time. So, let's wrap this video up with a few acquisition "
              'pro tips. Here are your pro tips for WAFT success. Number one, get a valid cage '
              'code or end cage code before you start. Number two, match invoice type to the '
              'contract every time.',
       'title': 'Ep. 2: Wide Area Workflow (WAWF) Explained | How to Invoice with the DoD & '
                'Avoid Rejections (Acquisition Pro Tips)',
       'url': 'https://www.youtube.com/watch?v=WXCymE9NjBg&t=637s',
       'video_id': 'WXCymE9NjBg'}]}
