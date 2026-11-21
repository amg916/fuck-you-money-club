"""Curated 180-citation Medical Equipment Resale baseline (15 per chapter across Q1-Q12) mined strictly from verified Medical Equipment Resale YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'510k',
     '820',
     'aesthetic',
     'air',
     'ambulatory',
     'america',
     'asc',
     'asset',
     'auction',
     'bimedis',
     'biomed',
     'biomedical',
     'building',
     'business',
     'buying',
     'calibration',
     'candela',
     'capital',
     'cbct',
     'center',
     'centurion',
     'cfr',
     'chair',
     'check',
     'client',
     'clients',
     'clinic',
     'contract',
     'crating',
     'cryogen',
     'cynosure',
     'dealer',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'510k',
     '820',
     'aesthetic',
     'air',
     'ambulatory',
     'america',
     'asc',
     'asset',
     'auction',
     'bimedis',
     'biomed',
     'biomedical',
     'budget',
     'building',
     'business',
     'buyer',
     'buying',
     'calibration',
     'candela',
     'capital',
     'cbct',
     'center',
     'centurion',
     'cfr',
     'chair',
     'check',
     'clinic',
     'contract',
     'crating',
     'cryogen',
     'customer',
     'cynosure',
     'dealer',
     'decision',
     'escrow',
     'fee',
     'fees',
     'invoice',
     'pay',
     'payment',
     'pays',
     'retainer'},
 3: {'510k',
     '820',
     'aesthetic',
     'air',
     'ambulatory',
     'america',
     'asc',
     'asset',
     'auction',
     'bimedis',
     'biomed',
     'biomedical',
     'building',
     'business',
     'buying',
     'calibration',
     'candela',
     'capital',
     'cash',
     'cashflow',
     'cbct',
     'center',
     'centurion',
     'cfr',
     'chair',
     'check',
     'clinic',
     'commission',
     'contract',
     'cost',
     'costs',
     'crating',
     'cryogen',
     'cynosure',
     'dealer',
     'economics',
     'margin',
     'margins',
     'price',
     'pricing',
     'profit',
     'roi',
     'unit'},
 4: {'510k',
     '820',
     'aesthetic',
     'air',
     'ambulatory',
     'america',
     'asc',
     'asset',
     'auction',
     'bimedis',
     'biomed',
     'biomedical',
     'budget',
     'building',
     'business',
     'buying',
     'calibration',
     'candela',
     'capital',
     'cbct',
     'center',
     'centurion',
     'cfr',
     'chair',
     'check',
     'clinic',
     'contract',
     'crating',
     'cryogen',
     'cynosure',
     'dealer',
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
 5: {'510k',
     '820',
     'aesthetic',
     'air',
     'ambulatory',
     'america',
     'asc',
     'asset',
     'auction',
     'audit',
     'avoid',
     'bimedis',
     'biomed',
     'biomedical',
     'building',
     'business',
     'buying',
     'calibration',
     'candela',
     'capital',
     'cbct',
     'center',
     'centurion',
     'cfr',
     'chair',
     'check',
     'clawback',
     'clinic',
     'contract',
     'crating',
     'cryogen',
     'cynosure',
     'dealer',
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
 6: {'510k',
     '820',
     'aesthetic',
     'air',
     'ambulatory',
     'america',
     'asc',
     'asset',
     'auction',
     'bimedis',
     'biomed',
     'biomedical',
     'building',
     'business',
     'buying',
     'calibration',
     'candela',
     'capital',
     'cbct',
     'center',
     'centurion',
     'cfr',
     'chair',
     'check',
     'client',
     'clinic',
     'contract',
     'crating',
     'cryogen',
     'cynosure',
     'data',
     'deal',
     'dealer',
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
 7: {'510k',
     '820',
     'aesthetic',
     'air',
     'ambulatory',
     'america',
     'asc',
     'asset',
     'auction',
     'bimedis',
     'biomed',
     'biomedical',
     'building',
     'business',
     'buying',
     'calibration',
     'candela',
     'capital',
     'cbct',
     'center',
     'centurion',
     'cfr',
     'chair',
     'check',
     'checklist',
     'clinic',
     'contract',
     'crating',
     'cryogen',
     'cynosure',
     'dealer',
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
 8: {'510k',
     '820',
     'aesthetic',
     'air',
     'ambulatory',
     'america',
     'api',
     'asc',
     'asset',
     'auction',
     'bimedis',
     'biomed',
     'biomedical',
     'building',
     'business',
     'buying',
     'calibration',
     'candela',
     'capital',
     'cbct',
     'center',
     'centurion',
     'cfr',
     'chair',
     'check',
     'clinic',
     'contract',
     'crating',
     'crm',
     'cryogen',
     'cynosure',
     'data',
     'database',
     'dealer',
     'platform',
     'portal',
     'scraper',
     'search',
     'software',
     'tool',
     'tools',
     'tracking'},
 9: {'510k',
     '820',
     'aesthetic',
     'agreement',
     'air',
     'ambulatory',
     'america',
     'asc',
     'asset',
     'auction',
     'bimedis',
     'biomed',
     'biomedical',
     'building',
     'business',
     'buying',
     'calibration',
     'candela',
     'capital',
     'cbct',
     'center',
     'centurion',
     'cfr',
     'chair',
     'check',
     'clinic',
     'compliance',
     'contract',
     'crating',
     'cryogen',
     'cynosure',
     'dealer',
     'disclosure',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'510k',
      '820',
      'aesthetic',
      'agent',
      'ai',
      'air',
      'ambulatory',
      'america',
      'asc',
      'asset',
      'auction',
      'automate',
      'automation',
      'bimedis',
      'biomed',
      'biomedical',
      'building',
      'business',
      'buying',
      'calibration',
      'candela',
      'capital',
      'cbct',
      'center',
      'centurion',
      'cfr',
      'chair',
      'check',
      'clinic',
      'contract',
      'crating',
      'cryogen',
      'cynosure',
      'dashboard',
      'dealer',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'510k',
      '820',
      'aesthetic',
      'air',
      'ambulatory',
      'america',
      'asc',
      'asset',
      'auction',
      'bimedis',
      'biomed',
      'biomedical',
      'building',
      'business',
      'buying',
      'calibration',
      'candela',
      'capital',
      'cbct',
      'center',
      'centurion',
      'cfr',
      'chair',
      'check',
      'clinic',
      'contract',
      'contractor',
      'crating',
      'cryogen',
      'cynosure',
      'dealer',
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
 12: {'510k',
      '820',
      'action',
      'aesthetic',
      'air',
      'ambulatory',
      'america',
      'asc',
      'asset',
      'auction',
      'bimedis',
      'biomed',
      'biomedical',
      'building',
      'business',
      'buying',
      'calibration',
      'candela',
      'capital',
      'cbct',
      'center',
      'centurion',
      'cfr',
      'chair',
      'check',
      'clinic',
      'contract',
      'crating',
      'cryogen',
      'cynosure',
      'day',
      'days',
      'dealer',
      'launch',
      'milestone',
      'month',
      'plan',
      'roadmap',
      'sprint',
      'start',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Quality Smart Solutions',
      'channel': 'Quality Smart Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:08](https://www.youtube.com/watch?v=4ICxQIfTktg&t=128s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Whereas in Canada, there is no predicate equivalence model in the same way as '
              'it is in the US. Instead, it evaluates safety and effectiveness based on the '
              'submitted evidence package. In the US, manufacturers must comply with 21 CFR '
              'part 820.',
      'timestamp': 128,
      'timestamp_label': '[00:02:08]',
      'timestamp_seconds': 128,
      'tip': 'Whereas in Canada, there is no predicate equivalence model in the same way as it '
             'is in the US. Instead, it evaluates safety and effectiveness based on the '
             'submitted evidence package. In the US, manufacturers must comply with 21 CFR '
             'part 820.',
      'title': 'FDA vs Health Canada: Medical Device Regulations Explained (510k, PMA & MDL) '
               '(Quality Smart Solutions)',
      'url': 'https://www.youtube.com/watch?v=4ICxQIfTktg&t=128s',
      'video_id': '4ICxQIfTktg'},
     {'author': 'Patient Guard | Medical Device Consultancy',
      'channel': 'Patient Guard | Medical Device Consultancy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=ZXn0JVoWAQk&t=57s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Business growth and Market expansion let's delve deeper into the process it "
              'begins with the preparation of a 510k submission this is a document that.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': "Business growth and Market expansion let's delve deeper into the process it "
             'begins with the preparation of a 510k submission this is a document that.',
      'title': 'Understanding the FDA Medical Device 510k Process (Patient Guard | Medical '
               'Device Consultancy)',
      'url': 'https://www.youtube.com/watch?v=ZXn0JVoWAQk&t=57s',
      'video_id': 'ZXn0JVoWAQk'},
     {'author': 'ATHEENAPANDIAN BIOMEDICAL INDUSTRY',
      'channel': 'ATHEENAPANDIAN BIOMEDICAL INDUSTRY',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:38:18](https://www.youtube.com/watch?v=-ZSbkKuzbMc&t=2298s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We need to check the particular device before entering to the market. So, for '
              'that 0% level then the 25% level then the 50% level 75% 100% level. Then the '
              '100% level if it is okay then only it is move into the next part next area.',
      'timestamp': 2298,
      'timestamp_label': '[00:38:18]',
      'timestamp_seconds': 2298,
      'tip': 'We need to check the particular device before entering to the market. So, for '
             'that 0% level then the 25% level then the 50% level 75% 100% level. Then the '
             '100% level if it is okay then only it is move into the next part next area.',
      'title': 'Testing and Calibration of Biomedical Equipment - Basics #calibrations '
               '#troubleshooting (ATHEENAPANDIAN BIOMEDICAL INDUSTRY)',
      'url': 'https://www.youtube.com/watch?v=-ZSbkKuzbMc&t=2298s',
      'video_id': '-ZSbkKuzbMc'},
     {'author': 'Easy Medical Device',
      'channel': 'Easy Medical Device',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:27](https://www.youtube.com/watch?v=USqn2QdZTCM&t=927s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Clients that have had notified bodies show up on their door and like in every '
              "notified body that I've signed a contract with over the last year is that.",
      'timestamp': 927,
      'timestamp_label': '[00:15:27]',
      'timestamp_seconds': 927,
      'tip': 'Clients that have had notified bodies show up on their door and like in every '
             "notified body that I've signed a contract with over the last year is that.",
      'title': 'How to register a Medical Device with FDA? (510k, PMA, de Novo...) (Easy '
               'Medical Device)',
      'url': 'https://www.youtube.com/watch?v=USqn2QdZTCM&t=927s',
      'video_id': 'USqn2QdZTCM'},
     {'author': 'Jessica Dela Cruz',
      'channel': 'Jessica Dela Cruz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:52](https://www.youtube.com/watch?v=QAlFneaY_MU&t=292s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm using a little cheat sheet here in the back of my badge. We today is also "
              'maximizing renov uh revenue. Uh yesterday was more about like the psychology of '
              'aesthetic medicine, you know, the um achieving a radiant glow.',
      'timestamp': 292,
      'timestamp_label': '[00:04:52]',
      'timestamp_seconds': 292,
      'tip': "I'm using a little cheat sheet here in the back of my badge. We today is also "
             'maximizing renov uh revenue. Uh yesterday was more about like the psychology of '
             'aesthetic medicine, you know, the um achieving a radiant glow.',
      'title': 'I Attended the Cynosure x Lutronic Academy | My Laser Training Experience '
               '(Jessica Dela Cruz)',
      'url': 'https://www.youtube.com/watch?v=QAlFneaY_MU&t=292s',
      'video_id': 'QAlFneaY_MU'},
     {'author': 'Block Imaging',
      'channel': 'Block Imaging',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=3203LTd64a8&t=15s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Service contracts we're talking about selling a piece of equipment tied into a "
              'warranty like a one-year warranty and then extended service contract beyond.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Service contracts we're talking about selling a piece of equipment tied into a "
             'warranty like a one-year warranty and then extended service contract beyond.',
      'title': 'Why Get Extended Service Contracts with Medical Imaging Equipment? (Block '
               'Imaging)',
      'url': 'https://www.youtube.com/watch?v=3203LTd64a8&t=15s',
      'video_id': '3203LTd64a8'},
     {'author': 'OR Today Magazine',
      'channel': 'OR Today Magazine',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:35:36](https://www.youtube.com/watch?v=4yS9pDHEcIs&t=2136s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'ANSIE document and the AON guidelines is that once again you need to have a '
              'contract with these uh different um organizations. And you want to make sure '
              'that if they do send in a technician to be a laser operator.',
      'timestamp': 2136,
      'timestamp_label': '[00:35:36]',
      'timestamp_seconds': 2136,
      'tip': 'ANSIE document and the AON guidelines is that once again you need to have a '
             'contract with these uh different um organizations. And you want to make sure '
             'that if they do send in a technician to be a laser operator.',
      'title': 'Medical Laser Safety Officer Compliance - A Gateway to Certification (OR Today '
               'Magazine)',
      'url': 'https://www.youtube.com/watch?v=4yS9pDHEcIs&t=2136s',
      'video_id': '4yS9pDHEcIs'},
     {'author': '23ABC News | KERO',
      'channel': '23ABC News | KERO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=-sk7wovpoZQ&t=43s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Market Harvard MD candidate kajal kadakia explains for the fda's okay devices "
              "must prove they're safe and that they work but something called the 510k.",
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': "Market Harvard MD candidate kajal kadakia explains for the fda's okay devices "
             "must prove they're safe and that they work but something called the 510k.",
      'title': 'FDA loophole led to years of unsafe medical devices (23ABC News | KERO)',
      'url': 'https://www.youtube.com/watch?v=-sk7wovpoZQ&t=43s',
      'video_id': '-sk7wovpoZQ'},
     {'author': 'Medmarc',
      'channel': 'Medmarc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:55](https://www.youtube.com/watch?v=nJblY5CRIVY&t=1735s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Really it's important that you get the input from all of these people because "
              'it does affect the overall business position of your firm. There should be a '
              'recall coordinator who is responsible for the recall.',
      'timestamp': 1735,
      'timestamp_label': '[00:28:55]',
      'timestamp_seconds': 1735,
      'tip': "Really it's important that you get the input from all of these people because it "
             'does affect the overall business position of your firm. There should be a recall '
             'coordinator who is responsible for the recall.',
      'title': 'Medical Device Recalls and Part 806: The Importance of Getting It Right '
               '(Medmarc)',
      'url': 'https://www.youtube.com/watch?v=nJblY5CRIVY&t=1735s',
      'video_id': 'nJblY5CRIVY'},
     {'author': 'All States MED',
      'channel': 'All States MED',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=60julptDir4&t=35s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Our customers by providing top quality medical  equipment sales service and an '
              'unparalleled level of customer service.  Our target market is.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'Our customers by providing top quality medical  equipment sales service and an '
             'unparalleled level of customer service.  Our target market is.',
      'title': 'All States MED Franchising - Medical Equipment Sales Franchise Opportunity '
               '(All States MED)',
      'url': 'https://www.youtube.com/watch?v=60julptDir4&t=35s',
      'video_id': '60julptDir4'},
     {'author': 'Berkeley Haas Case Series',
      'channel': 'Berkeley Haas Case Series',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:57](https://www.youtube.com/watch?v=NFqBMUIcgl4&t=177s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Limited medical and technical knowledge and limited financial accountability so '
              'they were content to simply have others dispose of the equipment and supplies '
              'resale of surplus equipment was also not a high priority because there was '
              'greater revenue gain in other areas.',
      'timestamp': 177,
      'timestamp_label': '[00:02:57]',
      'timestamp_seconds': 177,
      'tip': 'Limited medical and technical knowledge and limited financial accountability so '
             'they were content to simply have others dispose of the equipment and supplies '
             'resale of surplus equipment was also not a high priority because there was '
             'greater revenue gain in other areas.',
      'title': 'Medinas Health: Building a Medical Equipment Marketplace | Berkeley Haas Case '
               'Series (Berkeley Haas Case Series)',
      'url': 'https://www.youtube.com/watch?v=NFqBMUIcgl4&t=177s',
      'video_id': 'NFqBMUIcgl4'},
     {'author': 'Global Health Intelligence',
      'channel': 'Global Health Intelligence',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:19](https://www.youtube.com/watch?v=e1ChWLjN_6Q&t=1699s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Countries that are standing out um on the one hand uh we've seen the greatest "
              'changes in markets such as brazil and argentina brazil obviously being the '
              'biggest market by number of institutions by number of beds.',
      'timestamp': 1699,
      'timestamp_label': '[00:28:19]',
      'timestamp_seconds': 1699,
      'tip': "Countries that are standing out um on the one hand uh we've seen the greatest "
             'changes in markets such as brazil and argentina brazil obviously being the '
             'biggest market by number of institutions by number of beds.',
      'title': 'The Market Outlook for Medical Equipment in Latin America (Global Health '
               'Intelligence)',
      'url': 'https://www.youtube.com/watch?v=e1ChWLjN_6Q&t=1699s',
      'video_id': 'e1ChWLjN_6Q'},
     {'author': 'Intertek',
      'channel': 'Intertek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:38](https://www.youtube.com/watch?v=NTlv6-PNAuI&t=578s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Testing Labs achieved the CMA accreditation for an APA self-testing service '
              "among of them our intertek is one of them so which we're very excited about "
              'yes.',
      'timestamp': 578,
      'timestamp_label': '[00:09:38]',
      'timestamp_seconds': 578,
      'tip': 'Testing Labs achieved the CMA accreditation for an APA self-testing service '
             "among of them our intertek is one of them so which we're very excited about yes.",
      'title': 'Medical Compliance With Clarissa - Episode 16 - NMPA Process & Exporting '
               'Medical Devices to China (Intertek)',
      'url': 'https://www.youtube.com/watch?v=NTlv6-PNAuI&t=578s',
      'video_id': 'NTlv6-PNAuI'},
     {'author': 'Used Medical Equipment',
      'channel': 'Used Medical Equipment',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:56](https://www.youtube.com/watch?v=ezF-botYEqQ&t=416s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Can also go to a medical shop calm eye medical equipment and service formerly '
              'Hospital direct medical were one used medical equipment hospital direct medical '
              "I'm ed achill equipment and service your one-stop shop for all your medical "
              'equipment needs.',
      'timestamp': 416,
      'timestamp_label': '[00:06:56]',
      'timestamp_seconds': 416,
      'tip': 'Can also go to a medical shop calm eye medical equipment and service formerly '
             'Hospital direct medical were one used medical equipment hospital direct medical '
             "I'm ed achill equipment and service your one-stop shop for all your medical "
             'equipment needs.',
      'title': 'Used Medical Equipment for Sale USA (Used Medical Equipment)',
      'url': 'https://www.youtube.com/watch?v=ezF-botYEqQ&t=416s',
      'video_id': 'ezF-botYEqQ'},
     {'author': 'TechNation TV',
      'channel': 'TechNation TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:44](https://www.youtube.com/watch?v=lSIrqUmOamc&t=1904s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "High quality servicing maintaining of medical equipment so I'm in favor of this "
              "one and you'll see here just a little bit in the presentation how that in fact "
              "is happening and the value that it's bringing.",
      'timestamp': 1904,
      'timestamp_label': '[00:31:44]',
      'timestamp_seconds': 1904,
      'tip': "High quality servicing maintaining of medical equipment so I'm in favor of this "
             "one and you'll see here just a little bit in the presentation how that in fact "
             "is happening and the value that it's bringing.",
      'title': 'Updates to Servicing & Remanufacturing Through the Medical Device Servicing '
               'Collaborative Community (TechNation TV)',
      'url': 'https://www.youtube.com/watch?v=lSIrqUmOamc&t=1904s',
      'video_id': 'lSIrqUmOamc'}],
 2: [{'author': 'Industry Games',
      'channel': 'Industry Games',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=je3P4ran5jk&t=111s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This means the buyer, the user, and the decision-maker can all be different. '
              'This makes pricing very strange. Just like at a wedding, the one who eats the '
              "food doesn't pay the bill, and the one who pays the bill doesn't decide the "
              'menu.',
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': 'This means the buyer, the user, and the decision-maker can all be different. '
             'This makes pricing very strange. Just like at a wedding, the one who eats the '
             "food doesn't pay the bill, and the one who pays the bill doesn't decide the "
             'menu.',
      'title': 'The Economics of the Medical Devices Industry | How Medical Companies Make '
               'Billions (Industry Games)',
      'url': 'https://www.youtube.com/watch?v=je3P4ran5jk&t=111s',
      'video_id': 'je3P4ran5jk'},
     {'author': 'Sell My Data To AI',
      'channel': 'Sell My Data To AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:20](https://www.youtube.com/watch?v=K2WVBO_rnnA&t=200s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Please don't send any images or reports at this stage. Sellers pay nothing to "
              'be assessed. We charge a success fee only when a deal completes, agreed in '
              'writing before we introduce you to any buyer.',
      'timestamp': 200,
      'timestamp_label': '[00:03:20]',
      'timestamp_seconds': 200,
      'tip': "Please don't send any images or reports at this stage. Sellers pay nothing to be "
             'assessed. We charge a success fee only when a deal completes, agreed in writing '
             'before we introduce you to any buyer.',
      'title': 'Selling medical imaging data to AI: HIPAA and DICOM explained (Sell My Data To '
               'AI)',
      'url': 'https://www.youtube.com/watch?v=K2WVBO_rnnA&t=200s',
      'video_id': 'K2WVBO_rnnA'},
     {'author': 'Registrar Corp',
      'channel': 'Registrar Corp',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:08:50](https://www.youtube.com/watch?v=9Unzt431qg8&t=4130s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is kind of this decision and and how your relationship is. I know some of '
              "the companies, they do pay for their customers, but that's that's really up to "
              'the you know, your business.',
      'timestamp': 4130,
      'timestamp_label': '[01:08:50]',
      'timestamp_seconds': 4130,
      'tip': 'This is kind of this decision and and how your relationship is. I know some of '
             "the companies, they do pay for their customers, but that's that's really up to "
             'the you know, your business.',
      'title': 'Introduction to U.S. FDA Medical Device Regulations (Registrar Corp)',
      'url': 'https://www.youtube.com/watch?v=9Unzt431qg8&t=4130s',
      'video_id': '9Unzt431qg8'},
     {'author': 'CALISO9000',
      'channel': 'CALISO9000',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:49](https://www.youtube.com/watch?v=qs1HLi9K5XU&t=49s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'ISO 13485 2003 in that they are both written specifically to dictate or set '
              'forth the requirements by which a medical device is designed, developed, '
              'manufactured and monitored. And by monitor I mean how complaints are handled. '
              'The sections of 21 CFR 820 are as follows.',
      'timestamp': 49,
      'timestamp_label': '[00:00:49]',
      'timestamp_seconds': 49,
      'tip': 'ISO 13485 2003 in that they are both written specifically to dictate or set '
             'forth the requirements by which a medical device is designed, developed, '
             'manufactured and monitored. And by monitor I mean how complaints are handled. '
             'The sections of 21 CFR 820 are as follows.',
      'title': 'GMP for Medical Devices Overview ( FDA 21 CFR 820 ) (CALISO9000)',
      'url': 'https://www.youtube.com/watch?v=qs1HLi9K5XU&t=49s',
      'video_id': 'qs1HLi9K5XU'},
     {'author': 'Invent Healthcare',
      'channel': 'Invent Healthcare',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:23:34](https://www.youtube.com/watch?v=kwzaOqIZO2k&t=5014s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Before the time the application is submitted FDA will not accept the 510k for '
              'filing if the fee is not paid there is a standard user fee and a small.',
      'timestamp': 5014,
      'timestamp_label': '[01:23:34]',
      'timestamp_seconds': 5014,
      'tip': 'Before the time the application is submitted FDA will not accept the 510k for '
             'filing if the fee is not paid there is a standard user fee and a small.',
      'title': 'Webinar: Introduction to US FDA Medical Device Regulations (510k, De Novo, '
               'IDE, CAPA, eMDR) (Invent Healthcare)',
      'url': 'https://www.youtube.com/watch?v=kwzaOqIZO2k&t=5014s',
      'video_id': 'kwzaOqIZO2k'},
     {'author': 'MedicalMarcom',
      'channel': 'MedicalMarcom',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:43](https://www.youtube.com/watch?v=yIARvVKN5-s&t=943s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But you don't have that big a budget. So, the best way to do these 510k "
              "projects is as teams. And that's why we have two other people around the table "
              'here. These people are the real experts. Everybody I hire, they know more than '
              'I do about one area of special expertise.',
      'timestamp': 943,
      'timestamp_label': '[00:15:43]',
      'timestamp_seconds': 943,
      'tip': "But you don't have that big a budget. So, the best way to do these 510k projects "
             "is as teams. And that's why we have two other people around the table here. "
             'These people are the real experts. Everybody I hire, they know more than I do '
             'about one area of special expertise.',
      'title': '510k Workshop: How to Prepare an FDA Submission (Part I) (MedicalMarcom)',
      'url': 'https://www.youtube.com/watch?v=yIARvVKN5-s&t=943s',
      'video_id': 'yIARvVKN5-s'},
     {'author': 'Invent Healthcare',
      'channel': 'Invent Healthcare',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:47](https://www.youtube.com/watch?v=V3Fob6FXlCo&t=287s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Fda's decision-making process which we hope you will find very helpful and "
              'include an ex uh an appendix with a sample 510k summary to demonstrate the '
              "level of detail expected in each session a section which I'll also go into more "
              'detail.',
      'timestamp': 287,
      'timestamp_label': '[00:04:47]',
      'timestamp_seconds': 287,
      'tip': "Fda's decision-making process which we hope you will find very helpful and "
             'include an ex uh an appendix with a sample 510k summary to demonstrate the level '
             "of detail expected in each session a section which I'll also go into more "
             'detail.',
      'title': 'FDA 510K Premarket Notification Webinar (Invent Healthcare)',
      'url': 'https://www.youtube.com/watch?v=V3Fob6FXlCo&t=287s',
      'video_id': 'V3Fob6FXlCo'},
     {'author': 'Medical Sales U',
      'channel': 'Medical Sales U',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:27](https://www.youtube.com/watch?v=15ffob3rfCw&t=207s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So I'm in the oncology space and sometimes it's not always the end user who's "
              "going to be your person who champions the product. Sometimes it's someone who "
              "sees the patients in clinic after the fact and they see that there's a better "
              'way to do something.',
      'timestamp': 207,
      'timestamp_label': '[00:03:27]',
      'timestamp_seconds': 207,
      'tip': "So I'm in the oncology space and sometimes it's not always the end user who's "
             "going to be your person who champions the product. Sometimes it's someone who "
             "sees the patients in clinic after the fact and they see that there's a better "
             'way to do something.',
      'title': 'How to Master Medical Capital Equipment Sales (Medical Sales U)',
      'url': 'https://www.youtube.com/watch?v=15ffob3rfCw&t=207s',
      'video_id': '15ffob3rfCw'},
     {'author': 'Robert Remitz',
      'channel': 'Robert Remitz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:43](https://www.youtube.com/watch?v=_ue3Y22oMAA&t=283s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Difference in now in this industry but a way to save people money and make sure '
              "that you understand what you're ordering and buying and maybe we could be there "
              'to answer any questions that you have so we appreciate it and thanks a lot for '
              'coming to go Southern MD com.',
      'timestamp': 283,
      'timestamp_label': '[00:04:43]',
      'timestamp_seconds': 283,
      'tip': 'Difference in now in this industry but a way to save people money and make sure '
             "that you understand what you're ordering and buying and maybe we could be there "
             'to answer any questions that you have so we appreciate it and thanks a lot for '
             'coming to go Southern MD com.',
      'title': 'How to Sell or Buy Used Durable Medical Equipment. (Robert Remitz)',
      'url': 'https://www.youtube.com/watch?v=_ue3Y22oMAA&t=283s',
      'video_id': '_ue3Y22oMAA'},
     {'author': 'Centurion Service Group: A TRIMEDX Company',
      'channel': 'Centurion Service Group: A TRIMEDX Company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=dUZz08G_Dzc&t=117s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Buyer can come and fill a container and get everything anything that they '
              'possibly need all in one place is compared to having to go around and pick it '
              'up from different places different states and different regions of the United '
              'States.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': 'Buyer can come and fill a container and get everything anything that they '
             'possibly need all in one place is compared to having to go around and pick it up '
             'from different places different states and different regions of the United '
             'States.',
      'title': 'Medical Equipment Auctions (Centurion Service Group: A TRIMEDX Company)',
      'url': 'https://www.youtube.com/watch?v=dUZz08G_Dzc&t=117s',
      'video_id': 'dUZz08G_Dzc'},
     {'author': 'Laser Training',
      'channel': 'Laser Training',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:42](https://www.youtube.com/watch?v=KPlnFyWRwTQ&t=522s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Certifications and other government agencies will eventually follow suit it '
              'pays to be proactive with your certification the immediate benefit though is '
              'that you now have a professional credential that sets you apart from the rest.',
      'timestamp': 522,
      'timestamp_label': '[00:08:42]',
      'timestamp_seconds': 522,
      'tip': 'Certifications and other government agencies will eventually follow suit it pays '
             'to be proactive with your certification the immediate benefit though is that you '
             'now have a professional credential that sets you apart from the rest.',
      'title': 'NCLC Laser Certification Process (Laser Training)',
      'url': 'https://www.youtube.com/watch?v=KPlnFyWRwTQ&t=522s',
      'video_id': 'KPlnFyWRwTQ'},
     {'author': 'Dr. Hashem Abu Serhan',
      'channel': 'Dr. Hashem Abu Serhan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:05:37](https://www.youtube.com/watch?v=a_T4LqfP6zE&t=3937s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I will show now invitalize and other decision made to meet with you describe '
              'the the problem, explain how you found the reports and suggest the '
              'alternatives. When you suggesting the alternative, the solution, you need to '
              'consider three three things.',
      'timestamp': 3937,
      'timestamp_label': '[01:05:37]',
      'timestamp_seconds': 3937,
      'tip': 'I will show now invitalize and other decision made to meet with you describe the '
             'the problem, explain how you found the reports and suggest the alternatives. '
             'When you suggesting the alternative, the solution, you need to consider three '
             'three things.',
      'title': 'A Step-by-Step Guide to the Manufacturer and User Facility Device Experience '
               '(MAUDE) Database (Dr. Hashem Abu Serhan)',
      'url': 'https://www.youtube.com/watch?v=a_T4LqfP6zE&t=3937s',
      'video_id': 'a_T4LqfP6zE'},
     {'author': 'Medical Device Academy',
      'channel': 'Medical Device Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:14](https://www.youtube.com/watch?v=b1Ejw4mhVFU&t=614s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Like the user fee administrative stuff here all that's at the end whereas "
              "normally it's at the beginning so that's some stuff to look at that's a little "
              "bit different but I'm going to go back now I'll close this and I'll go back to "
              'our presentation.',
      'timestamp': 614,
      'timestamp_label': '[00:10:14]',
      'timestamp_seconds': 614,
      'tip': "Like the user fee administrative stuff here all that's at the end whereas "
             "normally it's at the beginning so that's some stuff to look at that's a little "
             "bit different but I'm going to go back now I'll close this and I'll go back to "
             'our presentation.',
      'title': 'How to prepare an FDA eSTAR 510(k) submission (Medical Device Academy)',
      'url': 'https://www.youtube.com/watch?v=b1Ejw4mhVFU&t=614s',
      'video_id': 'b1Ejw4mhVFU'},
     {'author': 'Marketing Tech',
      'channel': 'Marketing Tech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=cJ2aUSQgfeo&t=103s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Occurring so we were able to mitigate through some uh some dielectric dots we '
              'would call them some some added processing to eliminate that effect so that '
              'this product can still engage a large resistive touch panel in this kind of '
              'environment.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': 'Occurring so we were able to mitigate through some uh some dielectric dots we '
             'would call them some some added processing to eliminate that effect so that this '
             'product can still engage a large resistive touch panel in this kind of '
             'environment.',
      'title': 'Medical Equipment Case Study (Marketing Tech)',
      'url': 'https://www.youtube.com/watch?v=cJ2aUSQgfeo&t=103s',
      'video_id': 'cJ2aUSQgfeo'},
     {'author': 'Med Sales With Matt',
      'channel': 'Med Sales With Matt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:08](https://www.youtube.com/watch?v=2Nn9rL0ZXRg&t=308s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You out in any way shape or form um but hopefully that video helped you uh '
              'hopefully you had some reasonable takeaways of how to become a medical sales '
              'rep in 2024 um and would definitely love to hear from you so thanks.',
      'timestamp': 308,
      'timestamp_label': '[00:05:08]',
      'timestamp_seconds': 308,
      'tip': 'You out in any way shape or form um but hopefully that video helped you uh '
             'hopefully you had some reasonable takeaways of how to become a medical sales rep '
             'in 2024 um and would definitely love to hear from you so thanks.',
      'title': '5 Tips to Become a Medical Device Sales Rep in 2025 (Med Sales With Matt)',
      'url': 'https://www.youtube.com/watch?v=2Nn9rL0ZXRg&t=308s',
      'video_id': '2Nn9rL0ZXRg'}],
 3: [{'author': 'AI Training Data Broker',
      'channel': 'AI Training Data Broker',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:08](https://www.youtube.com/watch?v=p2c6HcivkAA&t=128s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Its sample clause goes to the other way, the vendor may use your data only to '
              'do the work in the contract. So, check who controls the data and whether you '
              'can export all of it. Now, flip it around, because some of you run a health '
              'software company, not a clinic.',
      'timestamp': 128,
      'timestamp_label': '[00:02:08]',
      'timestamp_seconds': 128,
      'tip': 'Its sample clause goes to the other way, the vendor may use your data only to do '
             'the work in the contract. So, check who controls the data and whether you can '
             'export all of it. Now, flip it around, because some of you run a health software '
             'company, not a clinic.',
      'title': 'Secondary Use: Can Your Clinic License Its Data? (AI Training Data Broker)',
      'url': 'https://www.youtube.com/watch?v=p2c6HcivkAA&t=128s',
      'video_id': 'p2c6HcivkAA'},
     {'author': 'Matrix One',
      'channel': 'Matrix One',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=URXL-ymHf4w&t=32s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It suits growing teams of 20 to 1,000 people who need an audit-ready, validated '
              'QMS without an enterprise price or an enterprise rollout. Start with the United '
              'States. Since 2 February 2026, 21 CFR Part 820 is the Quality Management System '
              'Regulation.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': 'It suits growing teams of 20 to 1,000 people who need an audit-ready, validated '
             'QMS without an enterprise price or an enterprise rollout. Start with the United '
             'States. Since 2 February 2026, 21 CFR Part 820 is the Quality Management System '
             'Regulation.',
      'title': 'QMS Software for Medical Electrical Equipment Companies | Matrix Quality '
               '(Matrix One)',
      'url': 'https://www.youtube.com/watch?v=URXL-ymHf4w&t=32s',
      'video_id': 'URXL-ymHf4w'},
     {'author': 'Earn Your Leisure',
      'channel': 'Earn Your Leisure',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:00](https://www.youtube.com/watch?v=hQY0qIkQ-xY&t=420s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Factual but that's what I was that was told so when okay so what's the profit "
              "margins the profit margins are good they're good it depends on what the.",
      'timestamp': 420,
      'timestamp_label': '[00:07:00]',
      'timestamp_seconds': 420,
      'tip': "Factual but that's what I was that was told so when okay so what's the profit "
             "margins the profit margins are good they're good it depends on what the.",
      'title': 'How To Build a Medical Equipment Business (Earn Your Leisure)',
      'url': 'https://www.youtube.com/watch?v=hQY0qIkQ-xY&t=420s',
      'video_id': 'hQY0qIkQ-xY'},
     {'author': 'NextGenMedTech',
      'channel': 'NextGenMedTech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:47](https://www.youtube.com/watch?v=sB46aiZG8lw&t=1607s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then 21 CFR part 1 to 99 also talks about the medical devices general medical '
              'requirements. Okay, in this class we are not going to go and check this 21 CFR.',
      'timestamp': 1607,
      'timestamp_label': '[00:26:47]',
      'timestamp_seconds': 1607,
      'tip': 'Then 21 CFR part 1 to 99 also talks about the medical devices general medical '
             'requirements. Okay, in this class we are not going to go and check this 21 CFR.',
      'title': 'USFDA Medical Device Submission Explained | 510(k), De Novo & PMA | Complete '
               'Introduction (NextGenMedTech)',
      'url': 'https://www.youtube.com/watch?v=sB46aiZG8lw&t=1607s',
      'video_id': 'sB46aiZG8lw'},
     {'author': 'Better Biomed Channel',
      'channel': 'Better Biomed Channel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=UQh0OoupetI&t=21s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I heard that they underbid the contract. That they did it for approximately '
              'half the price that the previous company did. This is a massive contract, guys. '
              'And I heard that they got the contract for about half the price of the previous '
              'company.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'I heard that they underbid the contract. That they did it for approximately half '
             'the price that the previous company did. This is a massive contract, guys. And I '
             'heard that they got the contract for about half the price of the previous '
             'company.',
      'title': 'Another Biomedical Repair company sold to private equity? (Better Biomed '
               'Channel)',
      'url': 'https://www.youtube.com/watch?v=UQh0OoupetI&t=21s',
      'video_id': 'UQh0OoupetI'},
     {'author': 'TechNation TV',
      'channel': 'TechNation TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:58:09](https://www.youtube.com/watch?v=7d4lxsuW9Xs&t=3489s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's not through that video outsource service costs not really an issue here "
              'replacement part cost yeah frequency and replacements definitely.',
      'timestamp': 3489,
      'timestamp_label': '[00:58:09]',
      'timestamp_seconds': 3489,
      'tip': "It's not through that video outsource service costs not really an issue here "
             'replacement part cost yeah frequency and replacements definitely.',
      'title': 'How Low Quality Remanufactured Parts Inside Medical Devices Increase Total '
               'Cost Of Ownership (TechNation TV)',
      'url': 'https://www.youtube.com/watch?v=7d4lxsuW9Xs&t=3489s',
      'video_id': '7d4lxsuW9Xs'},
     {'author': 'Centura College',
      'channel': 'Centura College',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:10](https://www.youtube.com/watch?v=edE21TMq6iY&t=130s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'On treating these patients I have friends right now that have been working '
              'overtime just to make sure they have the ventilators that are needed in their '
              'hospitals I love the biomed field because I feel like we do make a big '
              'difference without us there is no health care.',
      'timestamp': 130,
      'timestamp_label': '[00:02:10]',
      'timestamp_seconds': 130,
      'tip': 'On treating these patients I have friends right now that have been working '
             'overtime just to make sure they have the ventilators that are needed in their '
             'hospitals I love the biomed field because I feel like we do make a big '
             'difference without us there is no health care.',
      'title': 'Medical Equipment Training | Biomedical Equipment Technology (Centura College)',
      'url': 'https://www.youtube.com/watch?v=edE21TMq6iY&t=130s',
      'video_id': 'edE21TMq6iY'},
     {'author': 'FREE CME',
      'channel': 'FREE CME',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:51](https://www.youtube.com/watch?v=eWwVQyVC9X0&t=1911s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Magnet causing thisation and over our parking lot and luckily no one was '
              'injured no property damage at this point the unit was years old and was on its '
              'way back to the manufactur which toell it \u200fMRI.',
      'timestamp': 1911,
      'timestamp_label': '[00:31:51]',
      'timestamp_seconds': 1911,
      'tip': 'Magnet causing thisation and over our parking lot and luckily no one was injured '
             'no property damage at this point the unit was years old and was on its way back '
             'to the manufactur which toell it \u200fMRI.',
      'title': 'MRI Cryogen Safety (FREE CME)',
      'url': 'https://www.youtube.com/watch?v=eWwVQyVC9X0&t=1911s',
      'video_id': 'eWwVQyVC9X0'},
     {'author': 'EXPO NEWS',
      'channel': 'EXPO NEWS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=U-LBQwafIo8&t=88s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The world like excellent thermal water systems they look like neo and our '
              'original systems positive thing is the price difference between new and '
              "refurbished it's more than 50% less than when you buy a new assistant so you "
              'can find us on our website ww Club ratio calm.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'The world like excellent thermal water systems they look like neo and our '
             'original systems positive thing is the price difference between new and '
             "refurbished it's more than 50% less than when you buy a new assistant so you can "
             'find us on our website ww Club ratio calm.',
      'title': 'LAB RESALE | New, Used, Refurbished, Medical Equipment for SALE | ARABLAB | '
               'Expo News Dubai 2020 (EXPO NEWS)',
      'url': 'https://www.youtube.com/watch?v=U-LBQwafIo8&t=88s',
      'video_id': 'U-LBQwafIo8'},
     {'author': 'MRIPETCTSOURCE',
      'channel': 'MRIPETCTSOURCE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:46](https://www.youtube.com/watch?v=Bu466hadTu0&t=46s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Older systems have a higher boil-off rate as high as 5 to 10 liters per day. '
              'That’s up to $500 a day in liquid helium costs alone.',
      'timestamp': 46,
      'timestamp_label': '[00:00:46]',
      'timestamp_seconds': 46,
      'tip': 'Older systems have a higher boil-off rate as high as 5 to 10 liters per day. '
             'That’s up to $500 a day in liquid helium costs alone.',
      'title': 'How Much Liquid Helium Does MRI Use? (MRIPETCTSOURCE)',
      'url': 'https://www.youtube.com/watch?v=Bu466hadTu0&t=46s',
      'video_id': 'Bu466hadTu0'},
     {'author': 'VET talk TV',
      'channel': 'VET talk TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=Xn2oD7o0yyU&t=60s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'As a precaution everyone working near the MRI room is moved outside including a '
              'temporary emergency unit just in case close the door stand by close the door um '
              "we can leave the light on yeah ready 3 2 1 go it's on done.",
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': 'As a precaution everyone working near the MRI room is moved outside including a '
             'temporary emergency unit just in case close the door stand by close the door um '
             "we can leave the light on yeah ready 3 2 1 go it's on done.",
      'title': "ARH Homebush MRI 'Quench' - Ready For New MRI Install Soon (VET talk TV)",
      'url': 'https://www.youtube.com/watch?v=Xn2oD7o0yyU&t=60s',
      'video_id': 'Xn2oD7o0yyU'},
     {'author': 'Fast Forward Medical Innovation – Commercialization Education',
      'channel': 'Fast Forward Medical Innovation – Commercialization Education',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:29](https://www.youtube.com/watch?v=oAV1SBup8Q8&t=1229s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um uh you know you know the pharmacies online pharmacies so there's a lot of um "
              "very complicated system but one it's important to understand you know Pharmacy "
              'benefits Hospital benefits and how that can impact your pricing and in that '
              'Revenue.',
      'timestamp': 1229,
      'timestamp_label': '[00:20:29]',
      'timestamp_seconds': 1229,
      'tip': "Um uh you know you know the pharmacies online pharmacies so there's a lot of um "
             "very complicated system but one it's important to understand you know Pharmacy "
             'benefits Hospital benefits and how that can impact your pricing and in that '
             'Revenue.',
      'title': 'Medical Device, Diagnostics and Therapeutics Pricing, Revenue & Reimbursement '
               '(Fast Forward Medical Innovation – Commercialization Education)',
      'url': 'https://www.youtube.com/watch?v=oAV1SBup8Q8&t=1229s',
      'video_id': 'oAV1SBup8Q8'},
     {'author': 'The Endo Doc',
      'channel': 'The Endo Doc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:42](https://www.youtube.com/watch?v=e8IOdCXltj0&t=162s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The tooth that was really a problematic or painful which is the last molar as '
              'we can see here we can see on the two arrows here pointing at two big what I '
              'call mickey mouse ears or these two big black.',
      'timestamp': 162,
      'timestamp_label': '[00:02:42]',
      'timestamp_seconds': 162,
      'tip': 'The tooth that was really a problematic or painful which is the last molar as we '
             'can see here we can see on the two arrows here pointing at two big what I call '
             'mickey mouse ears or these two big black.',
      'title': 'Case Study: The advantages of having a CBCT & a dental operating microscope '
               '(The Endo Doc)',
      'url': 'https://www.youtube.com/watch?v=e8IOdCXltj0&t=162s',
      'video_id': 'e8IOdCXltj0'},
     {'author': 'Medical and Health Tips (MHT)',
      'channel': 'Medical and Health Tips (MHT)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:47](https://www.youtube.com/watch?v=8VMkq0EoUD4&t=647s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Technology involved in reprocessing reusable medical devices the '
              'recommendations in this guidance reflect the scientific advances in these '
              'areas.',
      'timestamp': 647,
      'timestamp_label': '[00:10:47]',
      'timestamp_seconds': 647,
      'tip': 'Technology involved in reprocessing reusable medical devices the recommendations '
             'in this guidance reflect the scientific advances in these areas.',
      'title': 'FDA Reprocessing Medical Devices: Validation Methods and '
               'Labeling.#MedicalDeviceReprocessing (Medical and Health Tips (MHT))',
      'url': 'https://www.youtube.com/watch?v=8VMkq0EoUD4&t=647s',
      'video_id': '8VMkq0EoUD4'},
     {'author': 'Better Biomed Channel',
      'channel': 'Better Biomed Channel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=sgJKIx288kY&t=111s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Trying to implement for years and I think I finally found a solution is used '
              "medical equipment it's you will save so much money just from the used medical "
              'equipment market either you can buy it for parts or you can buy the unit as a '
              'replacement.',
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': 'Trying to implement for years and I think I finally found a solution is used '
             "medical equipment it's you will save so much money just from the used medical "
             'equipment market either you can buy it for parts or you can buy the unit as a '
             'replacement.',
      'title': 'Save Major Dollars with Used Medical Equipment (Better Biomed Channel)',
      'url': 'https://www.youtube.com/watch?v=sgJKIx288kY&t=111s',
      'video_id': 'sgJKIx288kY'}],
 4: [{'author': 'US Regulations Explained',
      'channel': 'US Regulations Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:14](https://www.youtube.com/watch?v=3Qz3714kmCM&t=314s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s from, is held to the same incredibly high standard of quality. And that "
              'really leaves every manufacturer with a big question to answer. Are you '
              'building a system just to check a box and pass an inspection?',
      'timestamp': 314,
      'timestamp_label': '[00:05:14]',
      'timestamp_seconds': 314,
      'tip': "'s from, is held to the same incredibly high standard of quality. And that "
             'really leaves every manufacturer with a big question to answer. Are you building '
             'a system just to check a box and pass an inspection?',
      'title': '⚙️ (FDA) 21 CFR Part 820 Explained: Medical Device Quality System Compliance '
               '(US Regulations Explained)',
      'url': 'https://www.youtube.com/watch?v=3Qz3714kmCM&t=314s',
      'video_id': '3Qz3714kmCM'},
     {'author': 'Better Biomed Channel',
      'channel': 'Better Biomed Channel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:36](https://www.youtube.com/watch?v=Z56Xw5_JbNs&t=276s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Another thing I'm also going to check as we continue on kind of do our through "
              "our setup is I'm going to make sure I've got my three leads. I'm going to plug "
              "it up to my one step and we're going to go ahead and connect it to the proper "
              'leads.',
      'timestamp': 276,
      'timestamp_label': '[00:04:36]',
      'timestamp_seconds': 276,
      'tip': "Another thing I'm also going to check as we continue on kind of do our through "
             "our setup is I'm going to make sure I've got my three leads. I'm going to plug "
             "it up to my one step and we're going to go ahead and connect it to the proper "
             'leads.',
      'title': 'Defibrillator Electrical Safety Testing Featuring ReNew Biomedical (Better '
               'Biomed Channel)',
      'url': 'https://www.youtube.com/watch?v=Z56Xw5_JbNs&t=276s',
      'video_id': 'Z56Xw5_JbNs'},
     {'author': 'GoodSkin Clinics',
      'channel': 'GoodSkin Clinics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:49](https://www.youtube.com/watch?v=NCD01PVUcyY&t=49s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I have a clinic in Los Angeles and New York City and my specialty is in '
              "regenerative aesthetics using lasers, using bio stimulators. We're using a "
              'combination of the uh regenerative aesthetic side and then the zerf the deep '
              'structural tightening.',
      'timestamp': 49,
      'timestamp_label': '[00:00:49]',
      'timestamp_seconds': 49,
      'tip': 'I have a clinic in Los Angeles and New York City and my specialty is in '
             "regenerative aesthetics using lasers, using bio stimulators. We're using a "
             'combination of the uh regenerative aesthetic side and then the zerf the deep '
             'structural tightening.',
      'title': 'Cynosure Lutronic Academy (GoodSkin Clinics)',
      'url': 'https://www.youtube.com/watch?v=NCD01PVUcyY&t=49s',
      'video_id': 'NCD01PVUcyY'},
     {'author': 'Treomark',
      'channel': 'Treomark',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:09](https://www.youtube.com/watch?v=GoXd4_jxKBg&t=129s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Check dates and linked updates, then match the product and treatment record. '
              'Ask the clinic what the notice means for your care and who owns follow-up. '
              'Follow the notice’s specific instructions and clinical guidance rather than '
              'inventing a broader stop-or-continue rule.',
      'timestamp': 129,
      'timestamp_label': '[00:02:09]',
      'timestamp_seconds': 129,
      'tip': 'Check dates and linked updates, then match the product and treatment record. Ask '
             'the clinic what the notice means for your care and who owns follow-up. Follow '
             'the notice’s specific instructions and clinical guidance rather than inventing a '
             'broader stop-or-continue rule.',
      'title': 'FDA Recall vs Warning Letter vs Safety Communication: Know the Difference '
               '(Treomark)',
      'url': 'https://www.youtube.com/watch?v=GoXd4_jxKBg&t=129s',
      'video_id': 'GoXd4_jxKBg'},
     {'author': 'Innolitics',
      'channel': 'Innolitics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:51](https://www.youtube.com/watch?v=UdQw2LB0EYc&t=651s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'What does this change actually mean in practice and in clinic? And be able to '
              'better assess these changes by understanding the you know, the inside of the '
              'software a little bit better.',
      'timestamp': 651,
      'timestamp_label': '[00:10:51]',
      'timestamp_seconds': 651,
      'tip': 'What does this change actually mean in practice and in clinic? And be able to '
             'better assess these changes by understanding the you know, the inside of the '
             'software a little bit better.',
      'title': "Coffee and Q&A: When a Software Update Needs a New 510(k), FDA's Warning "
               'Letter to O.N. Diagnostics (Innolitics)',
      'url': 'https://www.youtube.com/watch?v=UdQw2LB0EYc&t=651s',
      'video_id': 'UdQw2LB0EYc'},
     {'author': 'A&A Associate LLC',
      'channel': 'A&A Associate LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=PoaIdM80c3c&t=134s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Select your business activity. Apply for your trade license. Register your '
              'medical devices with the authorities. Process your investor or partner visa.',
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': 'Select your business activity. Apply for your trade license. Register your '
             'medical devices with the authorities. Process your investor or partner visa.',
      'title': 'How to Start a Medical Equipment Business in Dubai (MOHAP Guide) (A&A '
               'Associate LLC)',
      'url': 'https://www.youtube.com/watch?v=PoaIdM80c3c&t=134s',
      'video_id': 'PoaIdM80c3c'},
     {'author': 'Dave The Biomed',
      'channel': 'Dave The Biomed',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:13](https://www.youtube.com/watch?v=0O9pt3qlw7E&t=73s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Excuse the mess of the back of my car, but I wanted to show y'all this that I "
              'can do 80% of my work with this set of tools. Um I need to do a video on that. '
              "I I I've done one, but I haven't showed my personal one.",
      'timestamp': 73,
      'timestamp_label': '[00:01:13]',
      'timestamp_seconds': 73,
      'tip': "Excuse the mess of the back of my car, but I wanted to show y'all this that I "
             'can do 80% of my work with this set of tools. Um I need to do a video on that. I '
             "I I've done one, but I haven't showed my personal one.",
      'title': 'Biomed Technician | Day in the life (Dave The Biomed)',
      'url': 'https://www.youtube.com/watch?v=0O9pt3qlw7E&t=73s',
      'video_id': '0O9pt3qlw7E'},
     {'author': 'Vet Tech - Beyond the Books:  Hands-on Skills',
      'channel': 'Vet Tech - Beyond the Books:  Hands-on Skills',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=PWqUy0mJWYw&t=22s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ve done your scrub and surgical prep, we'll then ask you to come in here and "
              'finish setting up surgery. You will then hook up your anesthetic machine to the '
              'appropriate circuit. We will have another video on that, and pressure check it '
              'with your instructor.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "'ve done your scrub and surgical prep, we'll then ask you to come in here and "
             'finish setting up surgery. You will then hook up your anesthetic machine to the '
             'appropriate circuit. We will have another video on that, and pressure check it '
             'with your instructor.',
      'title': '14. Sx Suite Setup 1 (Vet Tech - Beyond the Books:  Hands-on Skills)',
      'url': 'https://www.youtube.com/watch?v=PWqUy0mJWYw&t=22s',
      'video_id': 'PWqUy0mJWYw'},
     {'author': 'Hospital Beds and Medical Equipment for Sale',
      'channel': 'Hospital Beds and Medical Equipment for Sale',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:50](https://www.youtube.com/watch?v=mIjl1lP7-nA&t=170s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Stuff in stock as well but give us a Call hospital Direct Medical your '
              'wholesale hospital equipment dealer and Broker Sano California give us a Call '
              '858 263 4894 you can also get More information off Our website which is www.the '
              'number one used medicale equipment.',
      'timestamp': 170,
      'timestamp_label': '[00:02:50]',
      'timestamp_seconds': 170,
      'tip': 'Stuff in stock as well but give us a Call hospital Direct Medical your wholesale '
             'hospital equipment dealer and Broker Sano California give us a Call 858 263 4894 '
             'you can also get More information off Our website which is www.the number one '
             'used medicale equipment.',
      'title': 'Used Medical Equipment for Sale August 2016 Inventory (Hospital Beds and '
               'Medical Equipment for Sale)',
      'url': 'https://www.youtube.com/watch?v=mIjl1lP7-nA&t=170s',
      'video_id': 'mIjl1lP7-nA'},
     {'author': 'LopinMoetas',
      'channel': 'LopinMoetas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=8kG0BUAGcP4&t=20s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It has this soft silicone mat inside, so your tools don't slide around or get "
              'scratched up, and you can grab it in S, M, or L sizes.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "It has this soft silicone mat inside, so your tools don't slide around or get "
             'scratched up, and you can grab it in S, M, or L sizes.',
      'title': 'Best Top 5 Dental Autoclave Sterilizer Cases on AliExpress (LopinMoetas)',
      'url': 'https://www.youtube.com/watch?v=8kG0BUAGcP4&t=20s',
      'video_id': '8kG0BUAGcP4'},
     {'author': 'Radiology Frameworks',
      'channel': 'Radiology Frameworks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:19](https://www.youtube.com/watch?v=RYWamzzbeSc&t=499s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Air poses another challenge. Air's extremely low impedance creates a huge "
              'impedance mismatch with surrounding soft tissues, resulting in near total '
              'reflection .',
      'timestamp': 499,
      'timestamp_label': '[00:08:19]',
      'timestamp_seconds': 499,
      'tip': "Air poses another challenge. Air's extremely low impedance creates a huge "
             'impedance mismatch with surrounding soft tissues, resulting in near total '
             'reflection .',
      'title': 'Why X-ray, CT, Ultrasound, MRI & PET Imaging Work (Radiology Frameworks)',
      'url': 'https://www.youtube.com/watch?v=RYWamzzbeSc&t=499s',
      'video_id': 'RYWamzzbeSc'},
     {'author': 'Human Factors Engineering',
      'channel': 'Human Factors Engineering',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=NXLRmBcAe9U&t=20s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm not going to say which one, just received a class one recall. And that's "
              "the FDA's most serious level of recall. And why did they receive the recall? "
              'And why is this both a human factors and a software problem?',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "I'm not going to say which one, just received a class one recall. And that's the "
             "FDA's most serious level of recall. And why did they receive the recall? And why "
             'is this both a human factors and a software problem?',
      'title': 'Critical FDA Recall: A Usability Issue… or a Software Bug? #fdarecall '
               '#usability #software (Human Factors Engineering)',
      'url': 'https://www.youtube.com/watch?v=NXLRmBcAe9U&t=20s',
      'video_id': 'NXLRmBcAe9U'},
     {'author': 'Jess Cliffe',
      'channel': 'Jess Cliffe',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:47](https://www.youtube.com/watch?v=lIY2sYTUh2Y&t=767s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then let me know about that as well but I hope that this helped thank you so '
              'much for watching and I hope you enjoyed and I will see you next time.',
      'timestamp': 767,
      'timestamp_label': '[00:12:47]',
      'timestamp_seconds': 767,
      'tip': 'Then let me know about that as well but I hope that this helped thank you so '
             'much for watching and I hope you enjoyed and I will see you next time.',
      'title': 'VETERINARY BASICS: Things you should know before going into a clinic . . . | '
               'Vet School (Jess Cliffe)',
      'url': 'https://www.youtube.com/watch?v=lIY2sYTUh2Y&t=767s',
      'video_id': 'lIY2sYTUh2Y'},
     {'author': 'SILVER MEDICS',
      'channel': 'SILVER MEDICS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=PhTePMcMXpk&t=15s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'करूंगा या मुझे अगर ट्यूमर हो रखा है तो मैं क्या सिटी करूं? एक्सरे करूं या फिर '
              'अगर मेरी पथरी हो रही है, गॉड ब्लैडर कोई भी स्टोन है तो उसमें हमें क्या करना.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'करूंगा या मुझे अगर ट्यूमर हो रखा है तो मैं क्या सिटी करूं? एक्सरे करूं या फिर '
             'अगर मेरी पथरी हो रही है, गॉड ब्लैडर कोई भी स्टोन है तो उसमें हमें क्या करना.',
      'title': 'x ray vs ct vs mri vs usg #shorts #youtubeshorts #education (SILVER MEDICS)',
      'url': 'https://www.youtube.com/watch?v=PhTePMcMXpk&t=15s',
      'video_id': 'PhTePMcMXpk'},
     {'author': 'New to Medical Device Sales',
      'channel': 'New to Medical Device Sales',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=PaW-3LfksaU&t=15s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Little bit of information that can hopefully help you all first off I just want '
              'to say thank you to every single person that has been reaching out and.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Little bit of information that can hopefully help you all first off I just want '
             'to say thank you to every single person that has been reaching out and.',
      'title': "Let's Talk About Selling In Medical Device Sales (New to Medical Device Sales)",
      'url': 'https://www.youtube.com/watch?v=PaW-3LfksaU&t=15s',
      'video_id': 'PaW-3LfksaU'}],
 5: [{'author': 'Hidden Industries',
      'channel': 'Hidden Industries',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:05](https://www.youtube.com/watch?v=uNFHZlCznIw&t=305s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Some report risks accurately. Others over-report to drive services. Question '
              'their assumptions, sources, and coverage before they become your audit '
              'evidence. Support leverage gets sharp. Miss maintenance, lose patches. Fail '
              'audits, face back maintenance plus penalties.',
      'timestamp': 305,
      'timestamp_label': '[00:05:05]',
      'timestamp_seconds': 305,
      'tip': 'Some report risks accurately. Others over-report to drive services. Question '
             'their assumptions, sources, and coverage before they become your audit evidence. '
             'Support leverage gets sharp. Miss maintenance, lose patches. Fail audits, face '
             'back maintenance plus penalties.',
      'title': 'Software License Trap: Audits, Fees, Control (Hidden Industries)',
      'url': 'https://www.youtube.com/watch?v=uNFHZlCznIw&t=305s',
      'video_id': 'uNFHZlCznIw'},
     {'author': 'MedicalMarcom',
      'channel': 'MedicalMarcom',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:30](https://www.youtube.com/watch?v=-ceDuiClggg&t=1770s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um So, that's one of the other changes that we see. Another thing that we see "
              'is you have to really do a good job of your risk analysis and show the FDA, '
              "here are the risks that we identified and here's how we address them in the "
              'human factors testing.',
      'timestamp': 1770,
      'timestamp_label': '[00:29:30]',
      'timestamp_seconds': 1770,
      'tip': "Um So, that's one of the other changes that we see. Another thing that we see is "
             'you have to really do a good job of your risk analysis and show the FDA, here '
             "are the risks that we identified and here's how we address them in the human "
             'factors testing.',
      'title': 'How to Prepare a Medical Device 510k Submission for FDA | Rob Packard | Joe '
               'Hage (MedicalMarcom)',
      'url': 'https://www.youtube.com/watch?v=-ceDuiClggg&t=1770s',
      'video_id': '-ceDuiClggg'},
     {'author': 'TechNation TV',
      'channel': 'TechNation TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:26](https://www.youtube.com/watch?v=kBlmK6r6MgU&t=1106s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You have firsthand insight into potential risk and mitigate any thing that '
              'could happen and implement strategies for that change. And I I I talk about '
              'Bill, my biomedical engineer. I was at a hospital about 26 years and one of the '
              'most difficult things was stoing.',
      'timestamp': 1106,
      'timestamp_label': '[00:18:26]',
      'timestamp_seconds': 1106,
      'tip': 'You have firsthand insight into potential risk and mitigate any thing that could '
             'happen and implement strategies for that change. And I I I talk about Bill, my '
             'biomedical engineer. I was at a hospital about 26 years and one of the most '
             'difficult things was stoing.',
      'title': 'Laser Safe - The Biomed’s Path to LSO Certification (TechNation TV)',
      'url': 'https://www.youtube.com/watch?v=kBlmK6r6MgU&t=1106s',
      'video_id': 'kBlmK6r6MgU'},
     {'author': 'Laser Queen MD | Candela Laser & Electrolysis',
      'channel': 'Laser Queen MD | Candela Laser & Electrolysis',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=NarF87OCldw&t=70s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Stop retinol and vitamin A skincare products two weeks before treatment. Check '
              'your night creams, many contain vitamin A. Come with clean skin without makeup '
              'or lotions. Who should avoid this treatment? No active herpes infections, '
              'pustules, or open wounds.',
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': 'Stop retinol and vitamin A skincare products two weeks before treatment. Check '
             'your night creams, many contain vitamin A. Come with clean skin without makeup '
             'or lotions. Who should avoid this treatment? No active herpes infections, '
             'pustules, or open wounds.',
      'title': 'CANDELA SKIN REJUVENATION Laser Skin Tightening All you need to know before '
               'procedure (Laser Queen MD | Candela Laser & Electrolysis)',
      'url': 'https://www.youtube.com/watch?v=NarF87OCldw&t=70s',
      'video_id': 'NarF87OCldw'},
     {'author': 'NSF',
      'channel': 'NSF',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:00](https://www.youtube.com/watch?v=gfFy3QwozGE&t=780s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Here the standard is valid scientific evidence for safety and effectiveness is '
              'mentioned and clinical evidence is here requested. So if the 510k is the equ '
              'equivalent pathway and denovo is the novel but manageable pathway then the PMA '
              'is a full high risk evidence.',
      'timestamp': 780,
      'timestamp_label': '[00:13:00]',
      'timestamp_seconds': 780,
      'tip': 'Here the standard is valid scientific evidence for safety and effectiveness is '
             'mentioned and clinical evidence is here requested. So if the 510k is the equ '
             'equivalent pathway and denovo is the novel but manageable pathway then the PMA '
             'is a full high risk evidence.',
      'title': 'FDA Medical Device Market Entry: 510(k), De Novo, and PMA Explained for Life '
               'Sciences Leaders (NSF)',
      'url': 'https://www.youtube.com/watch?v=gfFy3QwozGE&t=780s',
      'video_id': 'gfFy3QwozGE'},
     {'author': 'Qualio',
      'channel': 'Qualio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=1GKnWm8UYVk&t=20s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And so, uh, agenda for today. Uh, hopefully um, we'll help you kind of "
              "understand what that process looks like. We'll talk about the process itself "
              'and then some top tips and mistakes to avoid um, and hopefully uh, give you '
              'lots of good information to take back and use.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "And so, uh, agenda for today. Uh, hopefully um, we'll help you kind of "
             "understand what that process looks like. We'll talk about the process itself and "
             'then some top tips and mistakes to avoid um, and hopefully uh, give you lots of '
             'good information to take back and use.',
      'title': 'Mastering your 510(k) submission process (Qualio)',
      'url': 'https://www.youtube.com/watch?v=1GKnWm8UYVk&t=20s',
      'video_id': '1GKnWm8UYVk'},
     {'author': 'FDA RECALLS',
      'channel': 'FDA RECALLS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:47](https://www.youtube.com/watch?v=4_qtgUz46GU&t=107s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Snack Right Superfoods doing business as Brad's Raw Chips is recalling its "
              'crunchy kale and chips. This recall is being issued because the product may '
              'contain thallium, a toxic heavy metal. Consuming food contaminated with '
              'thallium can pose serious health risks.',
      'timestamp': 107,
      'timestamp_label': '[00:01:47]',
      'timestamp_seconds': 107,
      'tip': "Snack Right Superfoods doing business as Brad's Raw Chips is recalling its "
             'crunchy kale and chips. This recall is being issued because the product may '
             'contain thallium, a toxic heavy metal. Consuming food contaminated with thallium '
             'can pose serious health risks.',
      'title': 'FDA Recall Update: Food and Medicine Nov 9. 2026 (FDA RECALLS)',
      'url': 'https://www.youtube.com/watch?v=4_qtgUz46GU&t=107s',
      'video_id': '4_qtgUz46GU'},
     {'author': 'Imaging Notes',
      'channel': 'Imaging Notes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:27](https://www.youtube.com/watch?v=fRqZHq_Gruc&t=387s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That measured contour is what defines the edge of zone three. Everything inside '
              'it is controlled and everything outside it is zone two. The third hazard is the '
              'one that empties the building and it is called a quench. A quench is the loss '
              'of superconductivity.',
      'timestamp': 387,
      'timestamp_label': '[00:06:27]',
      'timestamp_seconds': 387,
      'tip': 'That measured contour is what defines the edge of zone three. Everything inside '
             'it is controlled and everything outside it is zone two. The third hazard is the '
             'one that empties the building and it is called a quench. A quench is the loss of '
             'superconductivity.',
      'title': 'MRI Safety: Four Zones, Projectiles, Quench & Burns | Ep. 11 #mri #mrimasetry '
               '(Imaging Notes)',
      'url': 'https://www.youtube.com/watch?v=fRqZHq_Gruc&t=387s',
      'video_id': 'fRqZHq_Gruc'},
     {'author': 'Matrix One',
      'channel': 'Matrix One',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:36](https://www.youtube.com/watch?v=b_a74PE0Cn0&t=216s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Keep your risk management file current, because it steers the visit. Write '
              'management reviews and audit reports knowing FDA can read them. Make sure '
              'complaints, CAPAs and changes trace to each other. And keep the medical device '
              'file complete.',
      'timestamp': 216,
      'timestamp_label': '[00:03:36]',
      'timestamp_seconds': 216,
      'tip': 'Keep your risk management file current, because it steers the visit. Write '
             'management reviews and audit reports knowing FDA can read them. Make sure '
             'complaints, CAPAs and changes trace to each other. And keep the medical device '
             'file complete.',
      'title': 'QMSR Is Now in Force: What FDA Inspectors Look For Now | Matrix Quality '
               '(Matrix One)',
      'url': 'https://www.youtube.com/watch?v=b_a74PE0Cn0&t=216s',
      'video_id': 'b_a74PE0Cn0'},
     {'author': 'Traveling Alaskan Biomed Tech',
      'channel': 'Traveling Alaskan Biomed Tech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=UatkfSp7sHs&t=21s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm asked while I'm traveling is am I se certified? CBET meaning certified "
              'biomedical equipment technician. And I would told I told you I would do a video '
              'as to whether or not I pass or failed.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "I'm asked while I'm traveling is am I se certified? CBET meaning certified "
             'biomedical equipment technician. And I would told I told you I would do a video '
             'as to whether or not I pass or failed.',
      'title': 'CBET Exam: What to Study, Tips, and My Results (Traveling Alaskan Biomed Tech)',
      'url': 'https://www.youtube.com/watch?v=UatkfSp7sHs&t=21s',
      'video_id': 'UatkfSp7sHs'},
     {'author': 'GlobalCompliance Panel',
      'channel': 'GlobalCompliance Panel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:33:15](https://www.youtube.com/watch?v=1kYC2rBfPPA&t=1995s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Product malfunctions or fails in many cases you can use you can refer to the '
              'risk assessment that was done during the design process for your device in '
              'some.',
      'timestamp': 1995,
      'timestamp_label': '[00:33:15]',
      'timestamp_seconds': 1995,
      'tip': 'Product malfunctions or fails in many cases you can use you can refer to the '
             'risk assessment that was done during the design process for your device in some.',
      'title': 'Recalls, Removals, and Market Corrections in Compliance with FDA and ISO '
               'Requirements (GlobalCompliance Panel)',
      'url': 'https://www.youtube.com/watch?v=1kYC2rBfPPA&t=1995s',
      'video_id': '1kYC2rBfPPA'},
     {'author': 'Block Imaging',
      'channel': 'Block Imaging',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:59](https://www.youtube.com/watch?v=_-e12TPIFxw&t=119s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The helium would get vented the people in the imaging center a lot of times '
              "might want to watch it because of something they haven't seen before that "
              'happens relatively rarely as well.',
      'timestamp': 119,
      'timestamp_label': '[00:01:59]',
      'timestamp_seconds': 119,
      'tip': 'The helium would get vented the people in the imaging center a lot of times '
             "might want to watch it because of something they haven't seen before that "
             'happens relatively rarely as well.',
      'title': 'What Is an MRI Quench? (Block Imaging)',
      'url': 'https://www.youtube.com/watch?v=_-e12TPIFxw&t=119s',
      'video_id': '_-e12TPIFxw'},
     {'author': 'Biomedical Engineers TV',
      'channel': 'Biomedical Engineers TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:20](https://www.youtube.com/watch?v=wgffreMAiWI&t=140s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Is in direct conductive contact with the heart or other applications as '
              'considered necessary equipment providing a higher degree of protection against '
              'electric shock than type bf particularly with regard to allowable leakage '
              'currents and having floating applied parts.',
      'timestamp': 140,
      'timestamp_label': '[00:02:20]',
      'timestamp_seconds': 140,
      'tip': 'Is in direct conductive contact with the heart or other applications as '
             'considered necessary equipment providing a higher degree of protection against '
             'electric shock than type bf particularly with regard to allowable leakage '
             'currents and having floating applied parts.',
      'title': "Electrical Safety of Medical Equipment's | Part 3 | Biomedical Engineers TV "
               '(Biomedical Engineers TV)',
      'url': 'https://www.youtube.com/watch?v=wgffreMAiWI&t=140s',
      'video_id': 'wgffreMAiWI'},
     {'author': 'PEER at TAMU',
      'channel': 'PEER at TAMU',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=WoO-cNElJpg&t=15s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Registered veterinary technician I graduated from B Institute in Denver '
              'Colorado um I took um a few years of regular college courses um core courses.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Registered veterinary technician I graduated from B Institute in Denver Colorado '
             'um I took um a few years of regular college courses um core courses.',
      'title': 'Veterinary Procedure - Surgery Pack Preparation (PEER at TAMU)',
      'url': 'https://www.youtube.com/watch?v=WoO-cNElJpg&t=15s',
      'video_id': 'WoO-cNElJpg'},
     {'author': 'Medical Device Academy',
      'channel': 'Medical Device Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:48](https://www.youtube.com/watch?v=fB0ZiAL0q20&t=1488s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The main points of the UDI regulation this gives you a snapshot all the major '
              'aspects of the final UDI rule from label requirements through data submission '
              'to post market surveillance reporting interacting.',
      'timestamp': 1488,
      'timestamp_label': '[00:24:48]',
      'timestamp_seconds': 1488,
      'tip': 'The main points of the UDI regulation this gives you a snapshot all the major '
             'aspects of the final UDI rule from label requirements through data submission to '
             'post market surveillance reporting interacting.',
      'title': 'FDA UDI Regulation’s Impact on Medical Device Labelers Webinar (Medical Device '
               'Academy)',
      'url': 'https://www.youtube.com/watch?v=fB0ZiAL0q20&t=1488s',
      'video_id': 'fB0ZiAL0q20'}],
 6: [{'author': 'Nuronus',
      'channel': 'Nuronus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=iAwNQ3QON9c&t=78s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So when you run a gap assessment on a dental client, you'll almost always find "
              'the same things. No documented security risk analysis, the first thing OCR asks '
              'for. Missing or expired business associate agreements. Shared passwords at the '
              'front desk.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': "So when you run a gap assessment on a dental client, you'll almost always find "
             'the same things. No documented security risk analysis, the first thing OCR asks '
             'for. Missing or expired business associate agreements. Shared passwords at the '
             'front desk.',
      'title': 'HIPAA Compliance for Dental Practices: The 2026 Guide for MSPs (Nuronus)',
      'url': 'https://www.youtube.com/watch?v=iAwNQ3QON9c&t=78s',
      'video_id': 'iAwNQ3QON9c'},
     {'author': 'Break Into Medical Device Sales',
      'channel': 'Break Into Medical Device Sales',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=IaALQ3iuJp8&t=65s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, first, let's talk capital. These are the big-ticket items in medical device "
              'sales, right? And these have fewer transactions, but the deal sizes are, on '
              'average, way larger than all of the other transactions on this list.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': "So, first, let's talk capital. These are the big-ticket items in medical device "
             'sales, right? And these have fewer transactions, but the deal sizes are, on '
             'average, way larger than all of the other transactions on this list.',
      'title': 'What Type of Medical Device Sales Should You Pursue? (3 Paths Explained) '
               '(Break Into Medical Device Sales)',
      'url': 'https://www.youtube.com/watch?v=IaALQ3iuJp8&t=65s',
      'video_id': 'IaALQ3iuJp8'},
     {'author': 'U.S. Food and Drug Administration',
      'channel': 'U.S. Food and Drug Administration',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:27](https://www.youtube.com/watch?v=XMo038fEjH4&t=507s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You would need to search the De Novo database to find this first classified '
              'device under the newly created regulation. To find a 510(k) cleared or PMA '
              'approved device you can search the respective public databases using the '
              'hyperlinks provided on this slide.',
      'timestamp': 507,
      'timestamp_label': '[00:08:27]',
      'timestamp_seconds': 507,
      'tip': 'You would need to search the De Novo database to find this first classified '
             'device under the newly created regulation. To find a 510(k) cleared or PMA '
             'approved device you can search the respective public databases using the '
             'hyperlinks provided on this slide.',
      'title': 'Case Study: How is My Medical Device Classified? (U.S. Food and Drug '
               'Administration)',
      'url': 'https://www.youtube.com/watch?v=XMo038fEjH4&t=507s',
      'video_id': 'XMo038fEjH4'},
     {'author': 'K-Laser Australia',
      'channel': 'K-Laser Australia',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:22](https://www.youtube.com/watch?v=Hsmu9JQR5UM&t=142s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Third step, the laser room. If your clinic already has lasers, the laser room '
              'should already have a certificate of compliance. If not, you can find a list of '
              'laser consultants on the public register of Queensland Health. Click on the '
              'public register.',
      'timestamp': 142,
      'timestamp_label': '[00:02:22]',
      'timestamp_seconds': 142,
      'tip': 'Third step, the laser room. If your clinic already has lasers, the laser room '
             'should already have a certificate of compliance. If not, you can find a list of '
             'laser consultants on the public register of Queensland Health. Click on the '
             'public register.',
      'title': 'QLD - Laser license Application Process Explained - For Doctors (K-Laser '
               'Australia)',
      'url': 'https://www.youtube.com/watch?v=Hsmu9JQR5UM&t=142s',
      'video_id': 'Hsmu9JQR5UM'},
     {'author': 'AbishkarTECH',
      'channel': 'AbishkarTECH',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:26](https://www.youtube.com/watch?v=rqUE2pFiqUI&t=686s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Lead by lead you can check the Lees then you have to refer to standard actually '
              'what what about the booklet we have given no there is a mentioned in that leter '
              'that and pass.',
      'timestamp': 686,
      'timestamp_label': '[00:11:26]',
      'timestamp_seconds': 686,
      'tip': 'Lead by lead you can check the Lees then you have to refer to standard actually '
             'what what about the booklet we have given no there is a mentioned in that leter '
             'that and pass.',
      'title': 'ESA Training: How to Use a Fluke Electrical Safety Analyzer | ESA620 | '
               'Biomedical (AbishkarTECH)',
      'url': 'https://www.youtube.com/watch?v=rqUE2pFiqUI&t=686s',
      'video_id': 'rqUE2pFiqUI'},
     {'author': 'DICOM Code & Cure: MedPhysics and FDA Insights',
      'channel': 'DICOM Code & Cure: MedPhysics and FDA Insights',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:00](https://www.youtube.com/watch?v=l_IqH_YvZ68&t=180s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can check the FDA product classification database for more details but '
              'usually the first step you uh you will require is to identify a predi device '
              'and by that device you can look up its class you can look up its uh product.',
      'timestamp': 180,
      'timestamp_label': '[00:03:00]',
      'timestamp_seconds': 180,
      'tip': 'You can check the FDA product classification database for more details but '
             'usually the first step you uh you will require is to identify a predi device and '
             'by that device you can look up its class you can look up its uh product.',
      'title': 'How to Get FDA 510(k) Clearance? | Medical Device Submission Guide | Intro '
               'Video (DICOM Code & Cure: MedPhysics and FDA Insights)',
      'url': 'https://www.youtube.com/watch?v=l_IqH_YvZ68&t=180s',
      'video_id': 'l_IqH_YvZ68'},
     {'author': 'MRI R&D Program - TACTIX Twinning Project',
      'channel': 'MRI R&D Program - TACTIX Twinning Project',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:15](https://www.youtube.com/watch?v=BjPEga16VJY&t=1215s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So I'll try to go over them quickly. So in the first framework of data driven, "
              'basically we assume knowledge of k-space consistency encoding, so none of the '
              'physics of MRI is is involved.',
      'timestamp': 1215,
      'timestamp_label': '[00:20:15]',
      'timestamp_seconds': 1215,
      'tip': "So I'll try to go over them quickly. So in the first framework of data driven, "
             'basically we assume knowledge of k-space consistency encoding, so none of the '
             'physics of MRI is is involved.',
      'title': 'Deep Learning for MRI Reconstruction | MRI Data Acquisition #10 (MRI R&D '
               'Program - TACTIX Twinning Project)',
      'url': 'https://www.youtube.com/watch?v=BjPEga16VJY&t=1215s',
      'video_id': 'BjPEga16VJY'},
     {'author': 'CS Medical',
      'channel': 'CS Medical',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:42](https://www.youtube.com/watch?v=7hmnIP4pXbo&t=282s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And can you find the 510k paperwork online? Is it easy to find if if I was '
              'using something I thought was a class two device? Could I go and find that '
              'paperwork online? Um you could type in even into Google or something, type in '
              "the device's name, type in 510k.",
      'timestamp': 282,
      'timestamp_label': '[00:04:42]',
      'timestamp_seconds': 282,
      'tip': 'And can you find the 510k paperwork online? Is it easy to find if if I was using '
             'something I thought was a class two device? Could I go and find that paperwork '
             "online? Um you could type in even into Google or something, type in the device's "
             'name, type in 510k.',
      'title': 'Behind the 510(k): The Science of Material Compatibility and FDA Clearance Ft. '
               'CS Medical Staff (CS Medical)',
      'url': 'https://www.youtube.com/watch?v=7hmnIP4pXbo&t=282s',
      'video_id': '7hmnIP4pXbo'},
     {'author': 'National Library of Medicine',
      'channel': 'National Library of Medicine',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:34](https://www.youtube.com/watch?v=iWPkoBanBfY&t=94s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can filter several ways. For example, by company name or brand name, or '
              'even by GMDN term or FDA product code name, which are both general categories '
              'of medical devices. The list of results shows basic information about each '
              'record your search returned.',
      'timestamp': 94,
      'timestamp_label': '[00:01:34]',
      'timestamp_seconds': 94,
      'tip': 'You can filter several ways. For example, by company name or brand name, or even '
             'by GMDN term or FDA product code name, which are both general categories of '
             'medical devices. The list of results shows basic information about each record '
             'your search returned.',
      'title': 'AccessGUDID: Search and Download (National Library of Medicine)',
      'url': 'https://www.youtube.com/watch?v=iWPkoBanBfY&t=94s',
      'video_id': 'iWPkoBanBfY'},
     {'author': 'LexisNexis Life Sciences Solutions',
      'channel': 'LexisNexis Life Sciences Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:43](https://www.youtube.com/watch?v=nxzxvwNJELg&t=283s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Exception almost all class ones have the 510k exception but a few roughly 15 20 '
              'sort of thing have a good manufacturing exemption if you find that is true you '
              'have no udi requirements.',
      'timestamp': 283,
      'timestamp_label': '[00:04:43]',
      'timestamp_seconds': 283,
      'tip': 'Exception almost all class ones have the 510k exception but a few roughly 15 20 '
             'sort of thing have a good manufacturing exemption if you find that is true you '
             'have no udi requirements.',
      'title': 'US FDA Class I UDI Requirements and Exceptions (LexisNexis Life Sciences '
               'Solutions)',
      'url': 'https://www.youtube.com/watch?v=nxzxvwNJELg&t=283s',
      'video_id': 'nxzxvwNJELg'},
     {'author': 'Better Biomed Channel',
      'channel': 'Better Biomed Channel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=HBf8beE8tGc&t=21s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'BC meters, we actually have two studs on the side. One of them is 1 ohm, the '
              'other one is 100 microamps. And those are used for verifying the meter the lead '
              "integrity. So, the first step, we're going to connect to the 1 ohm. I'm going "
              'to hit the earth resistance.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'BC meters, we actually have two studs on the side. One of them is 1 ohm, the '
             'other one is 100 microamps. And those are used for verifying the meter the lead '
             "integrity. So, the first step, we're going to connect to the 1 ohm. I'm going to "
             'hit the earth resistance.',
      'title': 'Verify ANY Electrical Safety Analyzer (Better Biomed Channel)',
      'url': 'https://www.youtube.com/watch?v=HBf8beE8tGc&t=21s',
      'video_id': 'HBf8beE8tGc'},
     {'author': 'Vet Video Library',
      'channel': 'Vet Video Library',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:40](https://www.youtube.com/watch?v=zTKQ6_gG7iY&t=220s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Can be done one of two ways the first way is the pencil grip and so similar to '
              'holding a pencil you hold the blade handle with your thumb your index finger '
              'your middle finger and depending on the length of the scalpel handle your ring '
              'finger.',
      'timestamp': 220,
      'timestamp_label': '[00:03:40]',
      'timestamp_seconds': 220,
      'tip': 'Can be done one of two ways the first way is the pencil grip and so similar to '
             'holding a pencil you hold the blade handle with your thumb your index finger '
             'your middle finger and depending on the length of the scalpel handle your ring '
             'finger.',
      'title': 'Surgical Instruments And Their Use - Vet Video Library (Vet Video Library)',
      'url': 'https://www.youtube.com/watch?v=zTKQ6_gG7iY&t=220s',
      'video_id': 'zTKQ6_gG7iY'},
     {'author': 'Melissa McDowell',
      'channel': 'Melissa McDowell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:12](https://www.youtube.com/watch?v=-b8Z_S4V2mY&t=492s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm going to move into liver and do a couple of liver points um so I'm going to "
              'do liver 13 first um liver 13 is an act and pituitary gland acup Point liver '
              'points assist in regulation of blood sugar levels which can be issue for '
              "Cushing's.",
      'timestamp': 492,
      'timestamp_label': '[00:08:12]',
      'timestamp_seconds': 492,
      'tip': "I'm going to move into liver and do a couple of liver points um so I'm going to "
             'do liver 13 first um liver 13 is an act and pituitary gland acup Point liver '
             'points assist in regulation of blood sugar levels which can be issue for '
             "Cushing's.",
      'title': 'Cold Laser Therapy Certification - Video Case Study (Melissa McDowell)',
      'url': 'https://www.youtube.com/watch?v=-b8Z_S4V2mY&t=492s',
      'video_id': '-b8Z_S4V2mY'},
     {'author': 'Joe Verschoor',
      'channel': 'Joe Verschoor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:38](https://www.youtube.com/watch?v=-23KPzW6CW8&t=698s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Intent 21% we don't want the word used we would filter that out in Google ads "
              'as a negative keyword Pride power wheelchairs so this is a branded search term.',
      'timestamp': 698,
      'timestamp_label': '[00:11:38]',
      'timestamp_seconds': 698,
      'tip': "Intent 21% we don't want the word used we would filter that out in Google ads as "
             'a negative keyword Pride power wheelchairs so this is a branded search term.',
      'title': 'Medical Equipment: 7-Figure Niche or Waste of Time? (Joe Verschoor)',
      'url': 'https://www.youtube.com/watch?v=-23KPzW6CW8&t=698s',
      'video_id': '-23KPzW6CW8'},
     {'author': 'TechNation TV',
      'channel': 'TechNation TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:15:14](https://www.youtube.com/watch?v=C3pxzDnP6HM&t=4514s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Necessary for patient safety thanks Ryan um let's just close it out Jonathan "
              'are you available what do you think about number seven.',
      'timestamp': 4514,
      'timestamp_label': '[01:15:14]',
      'timestamp_seconds': 4514,
      'tip': "Necessary for patient safety thanks Ryan um let's just close it out Jonathan are "
             'you available what do you think about number seven.',
      'title': 'Special FDA Webinar for Medical Equipment Sales and Service Industry '
               '(TechNation TV)',
      'url': 'https://www.youtube.com/watch?v=C3pxzDnP6HM&t=4514s',
      'video_id': 'C3pxzDnP6HM'}],
 7: [{'author': 'Matrix One',
      'channel': 'Matrix One',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=Yi4V4HzJx-I&t=91s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '21 CFR Part 820 ensures that every aspect of production meets regulatory and '
              'customer requirements, from design to distribution. 21 CFR Part 820 is divided '
              'into 15 subparts, each addressing a specific aspect of the Quality System.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': '21 CFR Part 820 ensures that every aspect of production meets regulatory and '
             'customer requirements, from design to distribution. 21 CFR Part 820 is divided '
             'into 15 subparts, each addressing a specific aspect of the Quality System.',
      'title': 'What is 21 CFR Part 820? How does this impact your Medical Device in US. '
               '(Matrix One)',
      'url': 'https://www.youtube.com/watch?v=Yi4V4HzJx-I&t=91s',
      'video_id': 'Yi4V4HzJx-I'},
     {'author': 'Medical Device Academy',
      'channel': 'Medical Device Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=yX4mpyZCfjY&t=21s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'November I recorded a webinar that explained what why we need to modernize 21 '
              'CFR 820 in adopt ISO 1345 by reference for the quality system regulations in '
              'the U.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'November I recorded a webinar that explained what why we need to modernize 21 '
             'CFR 820 in adopt ISO 1345 by reference for the quality system regulations in the '
             'U.',
      'title': 'What is 21 CFR 820? (Medical Device Academy)',
      'url': 'https://www.youtube.com/watch?v=yX4mpyZCfjY&t=21s',
      'video_id': 'yX4mpyZCfjY'},
     {'author': 'Medical Device Academy',
      'channel': 'Medical Device Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=jUg2UuY-OlQ&t=15s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "21 CFR 820. this is the fda's regulation for Quality system requirements in the "
              'proposed amendment said instead of maintaining two different criteria for.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "21 CFR 820. this is the fda's regulation for Quality system requirements in the "
             'proposed amendment said instead of maintaining two different criteria for.',
      'title': 'Why does 21 CFR 820 need to be modernized to ISO 13485? (Medical Device '
               'Academy)',
      'url': 'https://www.youtube.com/watch?v=jUg2UuY-OlQ&t=15s',
      'video_id': 'jUg2UuY-OlQ'},
     {'author': 'Prime Path Medtech',
      'channel': 'Prime Path Medtech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=0CrtB8E2n30&t=15s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Submission process but you know exactly how it works don't worry we've got you "
              "covered today we're going to break down the steps to submit a 510k to the FDA.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Submission process but you know exactly how it works don't worry we've got you "
             "covered today we're going to break down the steps to submit a 510k to the FDA.",
      'title': 'How to Submit a 510(k) to the FDA | Step-by-Step Guide for Medical Device '
               'Approval (Prime Path Medtech)',
      'url': 'https://www.youtube.com/watch?v=0CrtB8E2n30&t=15s',
      'video_id': '0CrtB8E2n30'},
     {'author': 'Conference Panel',
      'channel': 'Conference Panel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:22](https://www.youtube.com/watch?v=aZkxlipyWRs&t=202s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So risk assessment and performance data. Now I'd like to briefly uh talk about "
              '510k summary format. So labeling requirement quality system labelings u you '
              'know there are some definitions.',
      'timestamp': 202,
      'timestamp_label': '[00:03:22]',
      'timestamp_seconds': 202,
      'tip': "So risk assessment and performance data. Now I'd like to briefly uh talk about "
             '510k summary format. So labeling requirement quality system labelings u you know '
             'there are some definitions.',
      'title': 'Mastering the FDA 510(k) Submission Process: A Practical Guide (Conference '
               'Panel)',
      'url': 'https://www.youtube.com/watch?v=aZkxlipyWRs&t=202s',
      'video_id': 'aZkxlipyWRs'},
     {'author': 'Block Imaging',
      'channel': 'Block Imaging',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:21](https://www.youtube.com/watch?v=xvO7-DA6X2w&t=81s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Question three: Does your refurbishment process include a HIPAA compliance '
              'step? HIPAA is a federal requirement that says all patient information needs to '
              'be removed from the system before it leaves one facility to go to another.',
      'timestamp': 81,
      'timestamp_label': '[00:01:21]',
      'timestamp_seconds': 81,
      'tip': 'Question three: Does your refurbishment process include a HIPAA compliance step? '
             'HIPAA is a federal requirement that says all patient information needs to be '
             'removed from the system before it leaves one facility to go to another.',
      'title': 'Seven Questions to Ask Your Provider for Refurbished Medical Equipment (Block '
               'Imaging)',
      'url': 'https://www.youtube.com/watch?v=xvO7-DA6X2w&t=81s',
      'video_id': 'xvO7-DA6X2w'},
     {'author': 'Learn Easy Science',
      'channel': 'Learn Easy Science',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:06](https://www.youtube.com/watch?v=9KwVs0WbeZI&t=366s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s painless and non-invasive. The limitations of an ultrasound scan includes "
              'the images are less detailed than CT or MRI, it cannot see clearly through '
              'bone, air can interfere with image quality, and the image quality will depend '
              "on the operator's skills.",
      'timestamp': 366,
      'timestamp_label': '[00:06:06]',
      'timestamp_seconds': 366,
      'tip': "'s painless and non-invasive. The limitations of an ultrasound scan includes the "
             'images are less detailed than CT or MRI, it cannot see clearly through bone, air '
             'can interfere with image quality, and the image quality will depend on the '
             "operator's skills.",
      'title': 'Types of imaging: X-RAY, MRI, CT, ULTRASOUND ✅ | How they work and what they '
               'are used for (Learn Easy Science)',
      'url': 'https://www.youtube.com/watch?v=9KwVs0WbeZI&t=366s',
      'video_id': '9KwVs0WbeZI'},
     {'author': 'Pharma Best Practices',
      'channel': 'Pharma Best Practices',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:35](https://www.youtube.com/watch?v=XOwMEZdq9q8&t=215s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The risk assessment process, the FDA's sequential approach. Okay, so once we "
              'clearly know the intended use we can step right into the actual risk assessment '
              'process itself. The FDA lays out this really logical four-step funnel for '
              'determining your risk-based approach.',
      'timestamp': 215,
      'timestamp_label': '[00:03:35]',
      'timestamp_seconds': 215,
      'tip': "The risk assessment process, the FDA's sequential approach. Okay, so once we "
             'clearly know the intended use we can step right into the actual risk assessment '
             'process itself. The FDA lays out this really logical four-step funnel for '
             'determining your risk-based approach.',
      'title': "Video 18 of 35 - FDA's 2026 CSA Guidance — Risk Assessment and Assurance "
               'Activities | (Pharma Best Practices)',
      'url': 'https://www.youtube.com/watch?v=XOwMEZdq9q8&t=215s',
      'video_id': 'XOwMEZdq9q8'},
     {'author': 'Break Into Medical Device Sales',
      'channel': 'Break Into Medical Device Sales',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:48](https://www.youtube.com/watch?v=fHUIy8gtER4&t=708s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, at this point, if you know you want to break into medical device sales, '
              "I've got this video here that you can check out that walks you through the "
              'three steps to land your first role in medical device sales. Now, a pretty big '
              'caveat, this is not a walk in the park.',
      'timestamp': 708,
      'timestamp_label': '[00:11:48]',
      'timestamp_seconds': 708,
      'tip': "So, at this point, if you know you want to break into medical device sales, I've "
             'got this video here that you can check out that walks you through the three '
             'steps to land your first role in medical device sales. Now, a pretty big caveat, '
             'this is not a walk in the park.',
      'title': 'The Truth About Medical Device Sales in 2026 (Don’t Do It Before Watching '
               'This) (Break Into Medical Device Sales)',
      'url': 'https://www.youtube.com/watch?v=fHUIy8gtER4&t=708s',
      'video_id': 'fHUIy8gtER4'},
     {'author': 'Henry Schein Medical',
      'channel': 'Henry Schein Medical',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:42](https://www.youtube.com/watch?v=VMonxNBLqE4&t=282s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Throughout the country who are utilizing this program and they love how much '
              "it's saving and the quality of these single-use devices so why don't we go over "
              'to the supply room.',
      'timestamp': 282,
      'timestamp_label': '[00:04:42]',
      'timestamp_seconds': 282,
      'tip': 'Throughout the country who are utilizing this program and they love how much '
             "it's saving and the quality of these single-use devices so why don't we go over "
             'to the supply room.',
      'title': 'Take a Tour of Our Ambulatory Surgery Center! (Henry Schein Medical)',
      'url': 'https://www.youtube.com/watch?v=VMonxNBLqE4&t=282s',
      'video_id': 'VMonxNBLqE4'},
     {'author': 'Center for Health Information and Decision Systems',
      'channel': 'Center for Health Information and Decision Systems',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:33](https://www.youtube.com/watch?v=Dbp4lOgGoT8&t=273s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Files subpart n contains the requirements for servicing of a medical device if '
              "it's applicable and lastly subpart o contains the requirements for statistical "
              'techniques for controlling and verifying the acceptability of process '
              'capability and product.',
      'timestamp': 273,
      'timestamp_label': '[00:04:33]',
      'timestamp_seconds': 273,
      'tip': 'Files subpart n contains the requirements for servicing of a medical device if '
             "it's applicable and lastly subpart o contains the requirements for statistical "
             'techniques for controlling and verifying the acceptability of process capability '
             'and product.',
      'title': 'GMP for Medical Devices Overview  FDA 21 CFR 820 (Center for Health '
               'Information and Decision Systems)',
      'url': 'https://www.youtube.com/watch?v=Dbp4lOgGoT8&t=273s',
      'video_id': 'Dbp4lOgGoT8'},
     {'author': 'Healthcare Direct USA',
      'channel': 'Healthcare Direct USA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:21](https://www.youtube.com/watch?v=09hrQ3SQK3E&t=1221s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Right that's the one thing we want to do and we minimize the number of steps "
              "that a user has to take to contact you right you know we're trying to be a.",
      'timestamp': 1221,
      'timestamp_label': '[00:20:21]',
      'timestamp_seconds': 1221,
      'tip': "Right that's the one thing we want to do and we minimize the number of steps "
             "that a user has to take to contact you right you know we're trying to be a.",
      'title': 'Selling Medical Equipment Into Latin America (Healthcare Direct USA)',
      'url': 'https://www.youtube.com/watch?v=09hrQ3SQK3E&t=1221s',
      'video_id': '09hrQ3SQK3E'},
     {'author': 'Quality Systems Explained',
      'channel': 'Quality Systems Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:17](https://www.youtube.com/watch?v=ohnyLE9h6ok&t=197s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Comment if you have any questions please send me an email at qm. Jedi gmail.com '
              'this is Aaron Snider from Quality Systems explained never stop learning.',
      'timestamp': 197,
      'timestamp_label': '[00:03:17]',
      'timestamp_seconds': 197,
      'tip': 'Comment if you have any questions please send me an email at qm. Jedi gmail.com '
             'this is Aaron Snider from Quality Systems explained never stop learning.',
      'title': 'Servicing 820.200 & ISO 13485 § 7.5.4, 8.4 (Executive Series #52) (Quality '
               'Systems Explained)',
      'url': 'https://www.youtube.com/watch?v=ohnyLE9h6ok&t=197s',
      'video_id': 'ohnyLE9h6ok'},
     {'author': 'RAYUS Radiology',
      'channel': 'RAYUS Radiology',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=aQZ8tTZnQ8A&t=31s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It’s utilizing radiation to take the images. It needs to be quick because in '
              'this day and age of course, the biggest concern we have being in imaging and '
              'radiology is to keep the doses as low and as safe as possible but still give us '
              'that good quality diagnostic study.".',
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': 'It’s utilizing radiation to take the images. It needs to be quick because in '
             'this day and age of course, the biggest concern we have being in imaging and '
             'radiology is to keep the doses as low and as safe as possible but still give us '
             'that good quality diagnostic study.".',
      'title': 'What’s the Difference Between an MRI and a CT? (RAYUS Radiology)',
      'url': 'https://www.youtube.com/watch?v=aQZ8tTZnQ8A&t=31s',
      'video_id': 'aQZ8tTZnQ8A'},
     {'author': 'TechNation TV',
      'channel': 'TechNation TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:43:27](https://www.youtube.com/watch?v=kmzmXxn2MBE&t=2607s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So there's a number of of isos and inhouse departments that are very active "
              'while in process right I would like to challenge the right to validate their '
              "everything is focused around their quity practices we' all.",
      'timestamp': 2607,
      'timestamp_label': '[00:43:27]',
      'timestamp_seconds': 2607,
      'tip': "So there's a number of of isos and inhouse departments that are very active "
             'while in process right I would like to challenge the right to validate their '
             "everything is focused around their quity practices we' all.",
      'title': 'Medical Device Servicing Community FDA Industry Updates (TechNation TV)',
      'url': 'https://www.youtube.com/watch?v=kmzmXxn2MBE&t=2607s',
      'video_id': 'kmzmXxn2MBE'}],
 8: [{'author': 'Global Health Intelligence',
      'channel': 'Global Health Intelligence',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=FzWeG7sw7qk&t=32s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Database called hospy scope hospy scope is the world's largest hospital "
              "demographics database focused on Latin America for this first search we're.",
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': "Database called hospy scope hospy scope is the world's largest hospital "
             "demographics database focused on Latin America for this first search we're.",
      'title': 'Increasing Sales of Medical Equipment in Latin America (Global Health '
               'Intelligence)',
      'url': 'https://www.youtube.com/watch?v=FzWeG7sw7qk&t=32s',
      'video_id': 'FzWeG7sw7qk'},
     {'author': 'REGSTALK',
      'channel': 'REGSTALK',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:51](https://www.youtube.com/watch?v=-6DRTqlDCP0&t=711s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So FDA will update it in then m database as a manufacturer we can uh go and see '
              'with the you know what with the product details available with us and we can '
              'search with the relevant data and fetch those information.',
      'timestamp': 711,
      'timestamp_label': '[00:11:51]',
      'timestamp_seconds': 711,
      'tip': 'So FDA will update it in then m database as a manufacturer we can uh go and see '
             'with the you know what with the product details available with us and we can '
             'search with the relevant data and fetch those information.',
      'title': 'Medical Device Complaint Handling Process | MAUDE Database & FDA 3500A '
               'Walkthrough (REGSTALK)',
      'url': 'https://www.youtube.com/watch?v=-6DRTqlDCP0&t=711s',
      'video_id': '-6DRTqlDCP0'},
     {'author': 'Cleared 인허가 노트',
      'channel': 'Cleared 인허가 노트',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:38](https://www.youtube.com/watch?v=6WEZ6ovm-PE&t=278s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And one without an associated design-related recall. Check FDA's recalls "
              'database. The draft also recommends explaining in your 510k summary why you '
              'chose your predicate. Your indications fall within it. Two, compare the '
              'technology line by line.',
      'timestamp': 278,
      'timestamp_label': '[00:04:38]',
      'timestamp_seconds': 278,
      'tip': "And one without an associated design-related recall. Check FDA's recalls "
             'database. The draft also recommends explaining in your 510k summary why you '
             'chose your predicate. Your indications fall within it. Two, compare the '
             'technology line by line.',
      'title': 'How to Pick a Predicate Device for Your 510(k): Intended Use, Split Predicates '
               '& FDA Best Practices (Cleared 인허가 노트)',
      'url': 'https://www.youtube.com/watch?v=6WEZ6ovm-PE&t=278s',
      'video_id': '6WEZ6ovm-PE'},
     {'author': 'Expert Institute',
      'channel': 'Expert Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:41](https://www.youtube.com/watch?v=xbxXTRwdVRs&t=881s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They're just not going to have clinical trial data for the most part. FDA's "
              'database there are manufacturer narratives and there are also enduser '
              'narratives like someone who was at the hospital or the clinic and perceived '
              'that they had a problem with the device.',
      'timestamp': 881,
      'timestamp_label': '[00:14:41]',
      'timestamp_seconds': 881,
      'tip': "They're just not going to have clinical trial data for the most part. FDA's "
             'database there are manufacturer narratives and there are also enduser narratives '
             'like someone who was at the hospital or the clinic and perceived that they had a '
             'problem with the device.',
      'title': 'Best Practices for Using Open FDA Data in Medical Device Cases (Expert '
               'Institute)',
      'url': 'https://www.youtube.com/watch?v=xbxXTRwdVRs&t=881s',
      'video_id': 'xbxXTRwdVRs'},
     {'author': 'Medical Device Academy',
      'channel': 'Medical Device Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=GPC9Ci11MuI&t=114s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They have a bunch of different databases and whatever database you're on on the "
              "right hand side they'll have a menu of all the other ones that you can look at. "
              "So this is the tool that I use to generate the data that we're presenting in "
              'this uh training.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': "They have a bunch of different databases and whatever database you're on on the "
             "right hand side they'll have a menu of all the other ones that you can look at. "
             "So this is the tool that I use to generate the data that we're presenting in "
             'this uh training.',
      'title': '8 Surprising Ways to Prevent Device Recalls! (Medical Device Academy)',
      'url': 'https://www.youtube.com/watch?v=GPC9Ci11MuI&t=114s',
      'video_id': 'GPC9Ci11MuI'},
     {'author': 'Dave Saunders',
      'channel': 'Dave Saunders',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:13](https://www.youtube.com/watch?v=6w27HXwMbmU&t=1093s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'COVID really forced the hands of a lot of companies. Um it is really best to '
              'have electronic document management with access control, revision tracking and '
              'search capability. It makes it easier for everybody.',
      'timestamp': 1093,
      'timestamp_label': '[00:18:13]',
      'timestamp_seconds': 1093,
      'tip': 'COVID really forced the hands of a lot of companies. Um it is really best to '
             'have electronic document management with access control, revision tracking and '
             'search capability. It makes it easier for everybody.',
      'title': 'Medical Device Design Controls: Complete FDA 510(k) Guide with ISO 13485 '
               'Compliance (Dave Saunders)',
      'url': 'https://www.youtube.com/watch?v=6w27HXwMbmU&t=1093s',
      'video_id': '6w27HXwMbmU'},
     {'author': 'Koven Technology Canada',
      'channel': 'Koven Technology Canada',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:08](https://www.youtube.com/watch?v=OS2unSk68KQ&t=188s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The mold database and you can search through them the same way we did before so '
              "that's an introductions of the database I hope you found that useful if you'd "
              "like more information reach out to me at Colvin's cardiovascular innovation "
              "let's connect.",
      'timestamp': 188,
      'timestamp_label': '[00:03:08]',
      'timestamp_seconds': 188,
      'tip': 'The mold database and you can search through them the same way we did before so '
             "that's an introductions of the database I hope you found that useful if you'd "
             "like more information reach out to me at Colvin's cardiovascular innovation "
             "let's connect.",
      'title': "FDA's MAUDE database: A medical device expert's insight (Koven Technology "
               'Canada)',
      'url': 'https://www.youtube.com/watch?v=OS2unSk68KQ&t=188s',
      'video_id': 'OS2unSk68KQ'},
     {'author': 'in2being',
      'channel': 'in2being',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:37](https://www.youtube.com/watch?v=0dpHnJj93Ns&t=37s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'MAUDE, into one central repository. 00:43): There are downloadable data files '
              "that consist of voluntary reports back to June 1993. There's actually data that "
              'goes before that. There are zip files all over the MAUDE database. You can pull '
              'these zip files.',
      'timestamp': 37,
      'timestamp_label': '[00:00:37]',
      'timestamp_seconds': 37,
      'tip': 'MAUDE, into one central repository. 00:43): There are downloadable data files '
             "that consist of voluntary reports back to June 1993. There's actually data that "
             'goes before that. There are zip files all over the MAUDE database. You can pull '
             'these zip files.',
      'title': "Who's Maude Anyway? Two FDA Databases Get Updates (in2being)",
      'url': 'https://www.youtube.com/watch?v=0dpHnJj93Ns&t=37s',
      'video_id': '0dpHnJj93Ns'},
     {'author': 'Health Watch USA',
      'channel': 'Health Watch USA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:49](https://www.youtube.com/watch?v=yKomHc_DWtw&t=289s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Program that then could sort through 7.5 million data files and sets and figure '
              'out all of the data that we can then analyze so from the entire mod database.',
      'timestamp': 289,
      'timestamp_label': '[00:04:49]',
      'timestamp_seconds': 289,
      'tip': 'Program that then could sort through 7.5 million data files and sets and figure '
             'out all of the data that we can then analyze so from the entire mod database.',
      'title': 'The FDA MAUDE Database.  Who is reporting and how good are the reports. '
               '(Health Watch USA)',
      'url': 'https://www.youtube.com/watch?v=yKomHc_DWtw&t=289s',
      'video_id': 'yKomHc_DWtw'},
     {'author': 'Metrasens',
      'channel': 'Metrasens',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:46:17](https://www.youtube.com/watch?v=DdLolB1kuRY&t=2777s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Uh okay we've had a number of questions about how people use the more database "
              "and how people get access to the data um one of the things that we're getting.",
      'timestamp': 2777,
      'timestamp_label': '[00:46:17]',
      'timestamp_seconds': 2777,
      'tip': "Uh okay we've had a number of questions about how people use the more database "
             "and how people get access to the data um one of the things that we're getting.",
      'title': 'MRI Accidents - Learning from the MAUDE Database (Metrasens)',
      'url': 'https://www.youtube.com/watch?v=DdLolB1kuRY&t=2777s',
      'video_id': 'DdLolB1kuRY'},
     {'author': 'Ofstead Insights',
      'channel': 'Ofstead Insights',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:21](https://www.youtube.com/watch?v=a-scTl1C2PA&t=501s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Another way to expand search results is to remove some detail from the search I '
              'might start by eliminating the brand name or making sure my search includes all '
              'event types.',
      'timestamp': 501,
      'timestamp_label': '[00:08:21]',
      'timestamp_seconds': 501,
      'tip': 'Another way to expand search results is to remove some detail from the search I '
             'might start by eliminating the brand name or making sure my search includes all '
             'event types.',
      'title': 'Searching the FDA MAUDE database (Ofstead Insights)',
      'url': 'https://www.youtube.com/watch?v=a-scTl1C2PA&t=501s',
      'video_id': 'a-scTl1C2PA'},
     {'author': 'Verdict Videos, Day in the Life Legal Video',
      'channel': 'Verdict Videos, Day in the Life Legal Video',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:32](https://www.youtube.com/watch?v=Tb7dnxPHBNo&t=152s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Implant on its incident reports database and see if there's been any other "
              'problems with it but do some research you have to know about this stuff because '
              'the the the damage can be horrific.',
      'timestamp': 152,
      'timestamp_label': '[00:02:32]',
      'timestamp_seconds': 152,
      'tip': "Implant on its incident reports database and see if there's been any other "
             'problems with it but do some research you have to know about this stuff because '
             'the the the damage can be horrific.',
      'title': 'FDA 510k process (Verdict Videos, Day in the Life Legal Video)',
      'url': 'https://www.youtube.com/watch?v=Tb7dnxPHBNo&t=152s',
      'video_id': 'Tb7dnxPHBNo'},
     {'author': 'POCTCTR',
      'channel': 'POCTCTR',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:50](https://www.youtube.com/watch?v=kiNTAANRFVM&t=1130s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Include data requirements Beyond those for non waved point of care ivds and '
              'ultimately the technology for Clear wave ivds must make their operation '
              'foolproof.',
      'timestamp': 1130,
      'timestamp_label': '[00:18:50]',
      'timestamp_seconds': 1130,
      'tip': 'Include data requirements Beyond those for non waved point of care ivds and '
             'ultimately the technology for Clear wave ivds must make their operation '
             'foolproof.',
      'title': 'FDA Approval and Licensing Process (POCTCTR)',
      'url': 'https://www.youtube.com/watch?v=kiNTAANRFVM&t=1130s',
      'video_id': 'kiNTAANRFVM'},
     {'author': 'norfolknhs',
      'channel': 'norfolknhs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:57](https://www.youtube.com/watch?v=D3YTNIGYcxQ&t=177s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Actually slowly bring them up through the ranks to make sure that they get '
              'their training and everything and the apprenticeship allows us to do this I get '
              "plenty of help I can ask anyone in the lab for help and they're all willing to "
              'help me and just amazing.',
      'timestamp': 177,
      'timestamp_label': '[00:02:57]',
      'timestamp_seconds': 177,
      'tip': 'Actually slowly bring them up through the ranks to make sure that they get their '
             'training and everything and the apprenticeship allows us to do this I get plenty '
             "of help I can ask anyone in the lab for help and they're all willing to help me "
             'and just amazing.',
      'title': 'Apprenticeships Case Study 5- Pathology (norfolknhs)',
      'url': 'https://www.youtube.com/watch?v=D3YTNIGYcxQ&t=177s',
      'video_id': 'D3YTNIGYcxQ'},
     {'author': 'Hidden Industries',
      'channel': 'Hidden Industries',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:35](https://www.youtube.com/watch?v=uNFHZlCznIw&t=215s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Vendors insist their tool is authoritative. Tactic three: indirect access. A '
              'portal, bot, or API touches licensed data. Now every person behind that system '
              'is counted as a user, even without direct login. Tactic four: time pressure.',
      'timestamp': 215,
      'timestamp_label': '[00:03:35]',
      'timestamp_seconds': 215,
      'tip': 'Vendors insist their tool is authoritative. Tactic three: indirect access. A '
             'portal, bot, or API touches licensed data. Now every person behind that system '
             'is counted as a user, even without direct login. Tactic four: time pressure.',
      'title': 'Software License Trap: Audits, Fees, Control (Hidden Industries)',
      'url': 'https://www.youtube.com/watch?v=uNFHZlCznIw&t=215s',
      'video_id': 'uNFHZlCznIw'}],
 9: [{'author': 'How to Start a Business that Prints Cash',
      'channel': 'How to Start a Business that Prints Cash',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:09](https://www.youtube.com/watch?v=Ahi8z5l5Yao&t=129s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Take this blueprint, um implement the compliance foundations, lock in your '
              'recurring contract revenue, um and start building your dominant medical supply '
              'position in Florida today.',
      'timestamp': 129,
      'timestamp_label': '[00:02:09]',
      'timestamp_seconds': 129,
      'tip': 'Take this blueprint, um implement the compliance foundations, lock in your '
             'recurring contract revenue, um and start building your dominant medical supply '
             'position in Florida today.',
      'title': 'How To Start A Medical Supply Business In Florida (How to Start a Business '
               'that Prints Cash)',
      'url': 'https://www.youtube.com/watch?v=Ahi8z5l5Yao&t=129s',
      'video_id': 'Ahi8z5l5Yao'},
     {'author': 'Isaac Erickson',
      'channel': 'Isaac Erickson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=TChhZNirpeM&t=98s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They're going to be very excited for you to go ahead with it. And uh but it "
              'also really protects you because that 510K is intellectual property and it '
              'gives you the legal license to sell the product in the United States as a '
              'medical device.',
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': "They're going to be very excited for you to go ahead with it. And uh but it also "
             'really protects you because that 510K is intellectual property and it gives you '
             'the legal license to sell the product in the United States as a medical device.',
      'title': 'Can Distributors File a 510(k) for Chinese Medical Devices?  YES! (Isaac '
               'Erickson)',
      'url': 'https://www.youtube.com/watch?v=TChhZNirpeM&t=98s',
      'video_id': 'TChhZNirpeM'},
     {'author': 'QT9 Software',
      'channel': 'QT9 Software',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:27](https://www.youtube.com/watch?v=2VNYkzxS9nA&t=27s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Welcome back to the QT9 Qcast, the show for quality and operations leaders '
              "building better systems. I'm your host, Christian Reyes. Quick reminder, this "
              'podcast is for general educational information. It is not legal or regulatory '
              'advice.',
      'timestamp': 27,
      'timestamp_label': '[00:00:27]',
      'timestamp_seconds': 27,
      'tip': 'Welcome back to the QT9 Qcast, the show for quality and operations leaders '
             "building better systems. I'm your host, Christian Reyes. Quick reminder, this "
             'podcast is for general educational information. It is not legal or regulatory '
             'advice.',
      'title': 'FDA QMSR Compliance Calls for a New Mindset | FDA 21 CFR Part 820 Evolution '
               'PART 2 (QT9 Software)',
      'url': 'https://www.youtube.com/watch?v=2VNYkzxS9nA&t=27s',
      'video_id': '2VNYkzxS9nA'},
     {'author': 'Software Connect',
      'channel': 'Software Connect',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=DWOABbtgSgI&t=57s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '"Hey, ISO 1345 is a nice thing to follow." They incorporate it by reference, so '
              'now it carries the full force of federal law. If you make or sell devices in '
              'the US, this compliance is no longer optional.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': '"Hey, ISO 1345 is a nice thing to follow." They incorporate it by reference, so '
             'now it carries the full force of federal law. If you make or sell devices in the '
             'US, this compliance is no longer optional.',
      'title': 'FDA QMSR: What it Means for Your Quality Management System (Software Connect)',
      'url': 'https://www.youtube.com/watch?v=DWOABbtgSgI&t=57s',
      'video_id': 'DWOABbtgSgI'},
     {'author': 'PublicResourceOrg',
      'channel': 'PublicResourceOrg',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:01](https://www.youtube.com/watch?v=ricZLyY1F1M&t=481s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Here they broaden their theoretical understanding of electricity, then go on to '
              'master the principles of solid state and digital electronics. This advanced '
              "training is a prerequisite for maintaining today's highly sophisticated "
              'electronic biomedical equipment.',
      'timestamp': 481,
      'timestamp_label': '[00:08:01]',
      'timestamp_seconds': 481,
      'tip': 'Here they broaden their theoretical understanding of electricity, then go on to '
             'master the principles of solid state and digital electronics. This advanced '
             "training is a prerequisite for maintaining today's highly sophisticated "
             'electronic biomedical equipment.',
      'title': 'BIOMEDICAL EQUIPMENT MAINTENANCE - TRAINING AND OPERATIONS (PublicResourceOrg)',
      'url': 'https://www.youtube.com/watch?v=ricZLyY1F1M&t=481s',
      'video_id': 'ricZLyY1F1M'},
     {'author': 'MedDeviceEngineerX  | Isiah',
      'channel': 'MedDeviceEngineerX  | Isiah',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:04](https://www.youtube.com/watch?v=bLqvmql3QHs&t=304s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'After all tests pass, complete the service record. Include serial numbers, '
              'technician signatures, calibration references, and measured values. A proper '
              'record demonstrates compliance and accountability. Once verified, attach a '
              'service verified label with inspection date.',
      'timestamp': 304,
      'timestamp_label': '[00:05:04]',
      'timestamp_seconds': 304,
      'tip': 'After all tests pass, complete the service record. Include serial numbers, '
             'technician signatures, calibration references, and measured values. A proper '
             'record demonstrates compliance and accountability. Once verified, attach a '
             'service verified label with inspection date.',
      'title': 'FT10 Functional Tests | Safety Checks and Output Verification (Part 6) '
               '(MedDeviceEngineerX  | Isiah)',
      'url': 'https://www.youtube.com/watch?v=bLqvmql3QHs&t=304s',
      'video_id': 'bLqvmql3QHs'},
     {'author': 'SAGAR TIPNE',
      'channel': 'SAGAR TIPNE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:36](https://www.youtube.com/watch?v=hJg3slOsTT8&t=636s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Maintain compliance moving forward taking a proactive structured approach like '
              'this ensures that dhfs are fully compliant audit ready and aligned with global '
              'regulatory.',
      'timestamp': 636,
      'timestamp_label': '[00:10:36]',
      'timestamp_seconds': 636,
      'tip': 'Maintain compliance moving forward taking a proactive structured approach like '
             'this ensures that dhfs are fully compliant audit ready and aligned with global '
             'regulatory.',
      'title': 'Medical Device DHF Remediation Interview | ISO 13485 | FDA 21 CFR 820 | Risk '
               'Management & Compliance (SAGAR TIPNE)',
      'url': 'https://www.youtube.com/watch?v=hJg3slOsTT8&t=636s',
      'video_id': 'hJg3slOsTT8'},
     {'author': 'Global Health Intelligence',
      'channel': 'Global Health Intelligence',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:30:13](https://www.youtube.com/watch?v=8l8Q1Q45u1s&t=1813s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Capitalizing the patients you know their consults Etc I think the the verdict '
              'is still out on how to turn infrastructure into a solid business case.',
      'timestamp': 1813,
      'timestamp_label': '[00:30:13]',
      'timestamp_seconds': 1813,
      'tip': 'Capitalizing the patients you know their consults Etc I think the the verdict is '
             'still out on how to turn infrastructure into a solid business case.',
      'title': '2022 Latin America Medical Equipment Market (Global Health Intelligence)',
      'url': 'https://www.youtube.com/watch?v=8l8Q1Q45u1s&t=1813s',
      'video_id': '8l8Q1Q45u1s'},
     {'author': 'DES Technologies',
      'channel': 'DES Technologies',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=xzb3hv6fB4g&t=79s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Incorporating audit reports guarantees that your data erasure efforts are '
              'verifiable, adding another layer of protection. Securely sell your medical '
              'equipment. Following essential steps to ensure both compliance and peace of '
              'mind.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': 'Incorporating audit reports guarantees that your data erasure efforts are '
             'verifiable, adding another layer of protection. Securely sell your medical '
             'equipment. Following essential steps to ensure both compliance and peace of '
             'mind.',
      'title': 'How to Legally Sell Used Medical Equipment | Compliance & Data Security '
               'Explained! (DES Technologies)',
      'url': 'https://www.youtube.com/watch?v=xzb3hv6fB4g&t=79s',
      'video_id': 'xzb3hv6fB4g'},
     {'author': 'Ohio Optometric',
      'channel': 'Ohio Optometric',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:06](https://www.youtube.com/watch?v=3pHyNlFBLO0&t=66s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh currently a lot of our state is in very remote locations and our patients '
              'have to travel and then even the ones that are in larger uh communities.',
      'timestamp': 66,
      'timestamp_label': '[00:01:06]',
      'timestamp_seconds': 66,
      'tip': 'Uh currently a lot of our state is in very remote locations and our patients '
             'have to travel and then even the ones that are in larger uh communities.',
      'title': 'Advanced Procedures Certification Course - Laser Training Course (Ohio '
               'Optometric)',
      'url': 'https://www.youtube.com/watch?v=3pHyNlFBLO0&t=66s',
      'video_id': '3pHyNlFBLO0'},
     {'author': 'CBS Philadelphia',
      'channel': 'CBS Philadelphia',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=NP8OXlNO1lE&t=39s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "WE'VE KIND OF BEEN UNDER WRAPS FOR LAST COUPLE OF YEARS NOT REALLY GOING OUT "
              "THERE AND NOT SOCIALIZING. I'M LOOKING FORWARD TO GETTING BACK OUT THERE AND "
              "MEETING PEOPLE. Stephanie: SHE'S TURNED TO DR. ERIC BERNSTEIN AT THE MAINLINE "
              'CENTER FOR LASER SURGERY.',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': "WE'VE KIND OF BEEN UNDER WRAPS FOR LAST COUPLE OF YEARS NOT REALLY GOING OUT "
             "THERE AND NOT SOCIALIZING. I'M LOOKING FORWARD TO GETTING BACK OUT THERE AND "
             "MEETING PEOPLE. Stephanie: SHE'S TURNED TO DR. ERIC BERNSTEIN AT THE MAINLINE "
             'CENTER FOR LASER SURGERY.',
      'title': 'New Laser Therapy Offers More Patient-Friendly Treatment For Skin '
               'Imperfections (CBS Philadelphia)',
      'url': 'https://www.youtube.com/watch?v=NP8OXlNO1lE&t=39s',
      'video_id': 'NP8OXlNO1lE'},
     {'author': 'Better Biomed Channel',
      'channel': 'Better Biomed Channel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:13](https://www.youtube.com/watch?v=7JgSRU2VyXE&t=373s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Access points that come out of it and from the emi filter i would then probably '
              'check right at the dc power supply where.',
      'timestamp': 373,
      'timestamp_label': '[00:06:13]',
      'timestamp_seconds': 373,
      'tip': 'Access points that come out of it and from the emi filter i would then probably '
             'check right at the dc power supply where.',
      'title': 'Beginners Troubleshooting Medical Device Power (Better Biomed Channel)',
      'url': 'https://www.youtube.com/watch?v=7JgSRU2VyXE&t=373s',
      'video_id': '7JgSRU2VyXE'},
     {'author': 'Laser Safety Certification',
      'channel': 'Laser Safety Certification',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=QnVjairPvRk&t=114s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Are available in both written or video formats ensuring you can learn in the '
              "way that suits you best don't wait to enhance your expertise and Safeguard your "
              'environment visit lasers safety certification.com and get certified.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': 'Are available in both written or video formats ensuring you can learn in the way '
             "that suits you best don't wait to enhance your expertise and Safeguard your "
             'environment visit lasers safety certification.com and get certified.',
      'title': 'Healthcare Laser Safety Certification Courses (Laser Safety Certification)',
      'url': 'https://www.youtube.com/watch?v=QnVjairPvRk&t=114s',
      'video_id': 'QnVjairPvRk'},
     {'author': 'MFI Medical',
      'channel': 'MFI Medical',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:12](https://www.youtube.com/watch?v=jzPWxnzAds0&t=132s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Successful practice for more information and to purchase these items visit mfi '
              "medical thank you for exploring mfi Medical's guide to setting up a veterinary "
              'office essential equipment and supplies visit mfim medical.com and find the '
              'perfect fit to day.',
      'timestamp': 132,
      'timestamp_label': '[00:02:12]',
      'timestamp_seconds': 132,
      'tip': 'Successful practice for more information and to purchase these items visit mfi '
             "medical thank you for exploring mfi Medical's guide to setting up a veterinary "
             'office essential equipment and supplies visit mfim medical.com and find the '
             'perfect fit to day.',
      'title': 'Setting Up a Veterinary Office: Essential Equipment and Supplies (MFI Medical)',
      'url': 'https://www.youtube.com/watch?v=jzPWxnzAds0&t=132s',
      'video_id': 'jzPWxnzAds0'},
     {'author': 'AI Training Data Broker',
      'channel': 'AI Training Data Broker',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:41](https://www.youtube.com/watch?v=p2c6HcivkAA&t=161s)',
      'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                   'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                   'FDA/HIPAA hygiene (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, the data your clinic sends you is not yours to license, unless each '
              'agreement says so. Next, look at the forms your patients signed, and at your '
              'privacy notice. Those papers can promise more than the law asks, such as never '
              'sharing your data for research.',
      'timestamp': 161,
      'timestamp_label': '[00:02:41]',
      'timestamp_seconds': 161,
      'tip': 'So, the data your clinic sends you is not yours to license, unless each '
             'agreement says so. Next, look at the forms your patients signed, and at your '
             'privacy notice. Those papers can promise more than the law asks, such as never '
             'sharing your data for research.',
      'title': 'Secondary Use: Can Your Clinic License Its Data? (AI Training Data Broker)',
      'url': 'https://www.youtube.com/watch?v=p2c6HcivkAA&t=161s',
      'video_id': 'p2c6HcivkAA'}],
 10: [{'author': 'Cerner Corporation',
       'channel': 'Cerner Corporation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:53](https://www.youtube.com/watch?v=hfx0fS26yO0&t=53s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Centers let's explore how cerner ambulatory surgery center can help enhance "
               'your patient care delivery and operations.',
       'timestamp': 53,
       'timestamp_label': '[00:00:53]',
       'timestamp_seconds': 53,
       'tip': "Centers let's explore how cerner ambulatory surgery center can help enhance "
              'your patient care delivery and operations.',
       'title': 'Cerner Ambulatory Surgery Center (ASC) overview (Cerner Corporation)',
       'url': 'https://www.youtube.com/watch?v=hfx0fS26yO0&t=53s',
       'video_id': 'hfx0fS26yO0'},
      {'author': 'The Derma Glow',
       'channel': 'The Derma Glow',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:34](https://www.youtube.com/watch?v=iZqTo4cU3Po&t=94s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And the bottom option is to control the speed of the DCD gas flowing. The '
               'standard values for the DCD gas options are 40 on 30. This is the counter '
               'reset button which resets the number of pulses to zero. Now we will carry a '
               'calibration to use the machine.',
       'timestamp': 94,
       'timestamp_label': '[00:01:34]',
       'timestamp_seconds': 94,
       'tip': 'And the bottom option is to control the speed of the DCD gas flowing. The '
              'standard values for the DCD gas options are 40 on 30. This is the counter reset '
              'button which resets the number of pulses to zero. Now we will carry a '
              'calibration to use the machine.',
       'title': 'Candela Pro Parameters Explained - How to use the Candela Pro series hair '
                'removal laser machine (The Derma Glow)',
       'url': 'https://www.youtube.com/watch?v=iZqTo4cU3Po&t=94s',
       'video_id': 'iZqTo4cU3Po'},
      {'author': 'Better Biomed Channel',
       'channel': 'Better Biomed Channel',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:11](https://www.youtube.com/watch?v=YXLWY7VHfxM&t=611s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Businesses are you going to is it going to be a home-based business are you um '
               "you know you're going to need you know if you get a building.",
       'timestamp': 611,
       'timestamp_label': '[00:10:11]',
       'timestamp_seconds': 611,
       'tip': 'Businesses are you going to is it going to be a home-based business are you um '
              "you know you're going to need you know if you get a building.",
       'title': 'Starting Your Own Biomed Business! (Better Biomed Channel)',
       'url': 'https://www.youtube.com/watch?v=YXLWY7VHfxM&t=611s',
       'video_id': 'YXLWY7VHfxM'},
      {'author': 'Break Into Medical Device Sales',
       'channel': 'Break Into Medical Device Sales',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:12](https://www.youtube.com/watch?v=-KxAlnmN4IY&t=852s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You can pivot into sales training, still make six figures. You can pivot out '
               'of the company you work for and go into starting your own distributorship, '
               "building your own med device distributor business, making I mean, hell, that's "
               'where people make seven figures.',
       'timestamp': 852,
       'timestamp_label': '[00:14:12]',
       'timestamp_seconds': 852,
       'tip': 'You can pivot into sales training, still make six figures. You can pivot out of '
              'the company you work for and go into starting your own distributorship, '
              "building your own med device distributor business, making I mean, hell, that's "
              'where people make seven figures.',
       'title': 'Medical Device Sales Explained (Everything You Need to Know) (Break Into '
                'Medical Device Sales)',
       'url': 'https://www.youtube.com/watch?v=-KxAlnmN4IY&t=852s',
       'video_id': '-KxAlnmN4IY'},
      {'author': 'Medical Device Academy',
       'channel': 'Medical Device Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:22](https://www.youtube.com/watch?v=bEKT9pNj8Sg&t=22s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, in this um this is a screen capture here or I'm actually displaying a copy "
               'of the FDA 510k FDA eSTAR template. And at the top of the screen here, if you '
               "can't read it very well, I'll try to blow it up a little bit. Um it says s- "
               "page 3 of 24. It's the device description.",
       'timestamp': 22,
       'timestamp_label': '[00:00:22]',
       'timestamp_seconds': 22,
       'tip': "So, in this um this is a screen capture here or I'm actually displaying a copy "
              'of the FDA 510k FDA eSTAR template. And at the top of the screen here, if you '
              "can't read it very well, I'll try to blow it up a little bit. Um it says s- "
              "page 3 of 24. It's the device description.",
       'title': "What's an RFD and when do I need one for a FDA 510(k)? (Medical Device "
                'Academy)',
       'url': 'https://www.youtube.com/watch?v=bEKT9pNj8Sg&t=22s',
       'video_id': 'bEKT9pNj8Sg'},
      {'author': 'Quality Systems Explained',
       'channel': 'Quality Systems Explained',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:19](https://www.youtube.com/watch?v=8Pgfw2y5xe0&t=19s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Check out the video description below for links to any supporting information '
               'and a summary of the material that we will cover in my executive series we.',
       'timestamp': 19,
       'timestamp_label': '[00:00:19]',
       'timestamp_seconds': 19,
       'tip': 'Check out the video description below for links to any supporting information '
              'and a summary of the material that we will cover in my executive series we.',
       'title': 'Corrections and Removals 21 CFR 806 & ISO 13485 § 8.3.3 (Executive Series '
                '#55) (Quality Systems Explained)',
       'url': 'https://www.youtube.com/watch?v=8Pgfw2y5xe0&t=19s',
       'video_id': '8Pgfw2y5xe0'},
      {'author': 'JHL SOLUTIONS',
       'channel': 'JHL SOLUTIONS',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:31](https://www.youtube.com/watch?v=1GAyLn0XcLI&t=211s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The usual amount of helium is placed in the magnet during manufacturing and '
               'then fully sealed and closing the coolant for the rest of its lifetime also no '
               'compromises are made on speed patient Comfort staff comfort and clinical '
               'confidence.',
       'timestamp': 211,
       'timestamp_label': '[00:03:31]',
       'timestamp_seconds': 211,
       'tip': 'The usual amount of helium is placed in the magnet during manufacturing and '
              'then fully sealed and closing the coolant for the rest of its lifetime also no '
              'compromises are made on speed patient Comfort staff comfort and clinical '
              'confidence.',
       'title': 'UNDERSTANDING  MRI - HELIUM  FILLED //MAGNET QUENCHING //HELIUM FREE MACHINES '
                'AS A BIOMED ENGINEER (JHL SOLUTIONS)',
       'url': 'https://www.youtube.com/watch?v=1GAyLn0XcLI&t=211s',
       'video_id': '1GAyLn0XcLI'},
      {'author': 'Used Medical Equipment',
       'channel': 'Used Medical Equipment',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:08](https://www.youtube.com/watch?v=0jN0a_8CpgI&t=68s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That item right there hiding behind the Dynam. Um that's a really high-end uh "
               'infant incubator or not incubator, infant bassinet. Uh this is another 3085 '
               'surgical table and a Steris AMC or APC allpurpose chair.',
       'timestamp': 68,
       'timestamp_label': '[00:01:08]',
       'timestamp_seconds': 68,
       'tip': "That item right there hiding behind the Dynam. Um that's a really high-end uh "
              'infant incubator or not incubator, infant bassinet. Uh this is another 3085 '
              'surgical table and a Steris AMC or APC allpurpose chair.',
       'title': 'Used Medical Equipment Company Current Inventory June 2026! (Used Medical '
                'Equipment)',
       'url': 'https://www.youtube.com/watch?v=0jN0a_8CpgI&t=68s',
       'video_id': '0jN0a_8CpgI'},
      {'author': 'Idi Cruz',
       'channel': 'Idi Cruz',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:50](https://www.youtube.com/watch?v=dcJl1DC6DM0&t=230s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Es ideal para compras formales de equipo nuevo y detallado, pero si estás '
               'empezando con poco capital no sería mi primera opción. La otra página la que '
               'más me gustó y te cuento por qué.',
       'timestamp': 230,
       'timestamp_label': '[00:03:50]',
       'timestamp_seconds': 230,
       'tip': 'Es ideal para compras formales de equipo nuevo y detallado, pero si estás '
              'empezando con poco capital no sería mi primera opción. La otra página la que '
              'más me gustó y te cuento por qué.',
       'title': '5 PÁGINAS para Comprar EQUIPOS MÉDICOS a BAJO PRECIO 💰  Nuevos, Usados y '
                'Envíos Internacionales (Idi Cruz)',
       'url': 'https://www.youtube.com/watch?v=dcJl1DC6DM0&t=230s',
       'video_id': 'dcJl1DC6DM0'},
      {'author': 'Surgical Direct (Surgical Direct)',
       'channel': 'Surgical Direct (Surgical Direct)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:31](https://www.youtube.com/watch?v=DrTCjk0roNk&t=91s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Prepare the scope for use insert the blue air water valve suction valve and '
               'attach the biopsy pork cap this is the veterinary bronchoscope to prepare it '
               'for use insert the suction cap and the biopsy port cap.',
       'timestamp': 91,
       'timestamp_label': '[00:01:31]',
       'timestamp_seconds': 91,
       'tip': 'Prepare the scope for use insert the blue air water valve suction valve and '
              'attach the biopsy pork cap this is the veterinary bronchoscope to prepare it '
              'for use insert the suction cap and the biopsy port cap.',
       'title': "Surgical Direct's Veterinary Endoscopy System (Surgical Direct (Surgical "
                'Direct))',
       'url': 'https://www.youtube.com/watch?v=DrTCjk0roNk&t=91s',
       'video_id': 'DrTCjk0roNk'},
      {'author': 'Medicare Rights Center',
       'channel': 'Medicare Rights Center',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:15](https://www.youtube.com/watch?v=BGvm2DdaLEs&t=75s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Medicare wouldn’t cover a motorized scooter that you only need outside the '
               'home. Second, Medicare doesn’t cover most equipment used to make things more '
               'convenient or comfortable. This includes stairway elevators, grab bars, air '
               'conditioners, and toilet seats.',
       'timestamp': 75,
       'timestamp_label': '[00:01:15]',
       'timestamp_seconds': 75,
       'tip': 'Medicare wouldn’t cover a motorized scooter that you only need outside the '
              'home. Second, Medicare doesn’t cover most equipment used to make things more '
              'convenient or comfortable. This includes stairway elevators, grab bars, air '
              'conditioners, and toilet seats.',
       'title': 'Understanding Medicare and Durable Medical Equipment (Medicare Rights Center)',
       'url': 'https://www.youtube.com/watch?v=BGvm2DdaLEs&t=75s',
       'video_id': 'BGvm2DdaLEs'},
      {'author': 'Biomedical Engineering with Ganesh',
       'channel': 'Biomedical Engineering with Ganesh',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=I59ePN89yx4&t=15s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'कैसे रिपेयर होगा एंड क्या प्रकॉशंस है सब कुछ ये वीडियो में आपको बताने वाला है। '
               'ठीक है? आई एम योर गणेश बायोमेडिकल इंजीनियरिंग वि गणेश। माय चैनल है.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'कैसे रिपेयर होगा एंड क्या प्रकॉशंस है सब कुछ ये वीडियो में आपको बताने वाला है। '
              'ठीक है? आई एम योर गणेश बायोमेडिकल इंजीनियरिंग वि गणेश। माय चैनल है.',
       'title': 'Medical Equipment Repair Tips 🔧 |Biomedical Engineers keliye Must Know (2026) '
                '| 18+ Years Experience (Biomedical Engineering with Ganesh)',
       'url': 'https://www.youtube.com/watch?v=I59ePN89yx4&t=15s',
       'video_id': 'I59ePN89yx4'},
      {'author': 'Mr. Regulatory',
       'channel': 'Mr. Regulatory',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:20:21](https://www.youtube.com/watch?v=sNeRd4nIrG8&t=1221s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Consignees to do and they want to see a response card or form included and fda '
               'also recommends that you provide examples of all of your recall '
               'communications.',
       'timestamp': 1221,
       'timestamp_label': '[00:20:21]',
       'timestamp_seconds': 1221,
       'tip': 'Consignees to do and they want to see a response card or form included and fda '
              'also recommends that you provide examples of all of your recall communications.',
       'title': 'EPISODE 2: Product Recalls, Including Removals and Corrections (Mr. '
                'Regulatory)',
       'url': 'https://www.youtube.com/watch?v=sNeRd4nIrG8&t=1221s',
       'video_id': 'sNeRd4nIrG8'},
      {'author': 'Ask the Vet',
       'channel': 'Ask the Vet',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:37](https://www.youtube.com/watch?v=1jEOjg29-e0&t=637s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Care of them so that's it for today thank you for tuning in if you have any "
               'specific questions please feel free to email me at ask the vet dot f f/a h @ '
               'gmail.com I love to hear from you and here we are forever family animal '
               'hospital.',
       'timestamp': 637,
       'timestamp_label': '[00:10:37]',
       'timestamp_seconds': 637,
       'tip': "Care of them so that's it for today thank you for tuning in if you have any "
              'specific questions please feel free to email me at ask the vet dot f f/a h @ '
              'gmail.com I love to hear from you and here we are forever family animal '
              'hospital.',
       'title': 'Ask the Vet - Surgery Instruments (Ask the Vet)',
       'url': 'https://www.youtube.com/watch?v=1jEOjg29-e0&t=637s',
       'video_id': '1jEOjg29-e0'},
      {'author': 'Quality Smart Solutions',
       'channel': 'Quality Smart Solutions',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:15](https://www.youtube.com/watch?v=4ICxQIfTktg&t=135s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Instead, it evaluates safety and effectiveness based on the submitted evidence '
               'package. In the US, manufacturers must comply with 21 CFR part 820. This is '
               'known as the quality system regulation.',
       'timestamp': 135,
       'timestamp_label': '[00:02:15]',
       'timestamp_seconds': 135,
       'tip': 'Instead, it evaluates safety and effectiveness based on the submitted evidence '
              'package. In the US, manufacturers must comply with 21 CFR part 820. This is '
              'known as the quality system regulation.',
       'title': 'FDA vs Health Canada: Medical Device Regulations Explained (510k, PMA & MDL) '
                '(Quality Smart Solutions)',
       'url': 'https://www.youtube.com/watch?v=4ICxQIfTktg&t=135s',
       'video_id': '4ICxQIfTktg'}],
 11: [{'author': 'The Business Beneath',
       'channel': 'The Business Beneath',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:24](https://www.youtube.com/watch?v=iWKTCfxvEUg&t=804s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'For hospitals, buying the technology is a financial decision that can shape '
               'operations for years. For manufacturers, the equipment can become the '
               'beginning of an ongoing business relationship, and for patients, all of it '
               'operates largely out of sight.',
       'timestamp': 804,
       'timestamp_label': '[00:13:24]',
       'timestamp_seconds': 804,
       'tip': 'For hospitals, buying the technology is a financial decision that can shape '
              'operations for years. For manufacturers, the equipment can become the beginning '
              'of an ongoing business relationship, and for patients, all of it operates '
              'largely out of sight.',
       'title': 'Who Really Profits From Hospital Technology? (The Business Beneath)',
       'url': 'https://www.youtube.com/watch?v=iWKTCfxvEUg&t=804s',
       'video_id': 'iWKTCfxvEUg'},
      {'author': 'American Association of Hip and Knee Surgeons',
       'channel': 'American Association of Hip and Knee Surgeons',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=AQIyPCz9bJM&t=15s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And those joining us virtually online today my name is sharon edwards and i'm "
               'the medical education manager for the asu solutions team of.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': "And those joining us virtually online today my name is sharon edwards and i'm "
              'the medical education manager for the asu solutions team of.',
       'title': 'Solutions to Expand or Optimize your Ambulatory Surgery Center (American '
                'Association of Hip and Knee Surgeons)',
       'url': 'https://www.youtube.com/watch?v=AQIyPCz9bJM&t=15s',
       'video_id': 'AQIyPCz9bJM'},
      {'author': 'Regulatory Compliance Associates',
       'channel': 'Regulatory Compliance Associates',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=cNSAixRUu9Q&t=21s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Now, although the FDA is using ISO 13485 as the backbone of the new '
               'requirement, it is important to note that several components of 21 CFR part '
               '820 are still applicable.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'Now, although the FDA is using ISO 13485 as the backbone of the new '
              'requirement, it is important to note that several components of 21 CFR part 820 '
              'are still applicable.',
       'title': 'FDA’s New QMSR Final Rule: What Medical Device Manufacturers Need to Know '
                '(2026) (Regulatory Compliance Associates)',
       'url': 'https://www.youtube.com/watch?v=cNSAixRUu9Q&t=21s',
       'video_id': 'cNSAixRUu9Q'},
      {'author': 'Cloud Accounting World',
       'channel': 'Cloud Accounting World',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:09](https://www.youtube.com/watch?v=ll03lU-_2LM&t=129s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Your business may have equipment rental income, delivery expenses, '
               'installation costs, warehouse expenses, employee payroll, contractor payments, '
               'warranty related costs, equipment maintenance, rent, and software '
               'subscriptions.',
       'timestamp': 129,
       'timestamp_label': '[00:02:09]',
       'timestamp_seconds': 129,
       'tip': 'Your business may have equipment rental income, delivery expenses, installation '
              'costs, warehouse expenses, employee payroll, contractor payments, warranty '
              'related costs, equipment maintenance, rent, and software subscriptions.',
       'title': 'Medical Equipment Suppliers Bookkeeping Services | Inventory, Accounting & '
                'Financial Management (Cloud Accounting World)',
       'url': 'https://www.youtube.com/watch?v=ll03lU-_2LM&t=129s',
       'video_id': 'll03lU-_2LM'},
      {'author': 'Med Sales With Matt',
       'channel': 'Med Sales With Matt',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:37](https://www.youtube.com/watch?v=ZLMuTtC8HM0&t=37s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So these are the skills that are going to separate the people who get hired '
               "from the ones that don't even get a call back. And by the end of this video, "
               "you'll know exactly what hiring managers are going to be looking for and how "
               'to start building these skills yourself.',
       'timestamp': 37,
       'timestamp_label': '[00:00:37]',
       'timestamp_seconds': 37,
       'tip': 'So these are the skills that are going to separate the people who get hired '
              "from the ones that don't even get a call back. And by the end of this video, "
              "you'll know exactly what hiring managers are going to be looking for and how to "
              'start building these skills yourself.',
       'title': '7 Skills NEEDED for a Medical Devices Sales Rep Job in 2025 (Med Sales With '
                'Matt)',
       'url': 'https://www.youtube.com/watch?v=ZLMuTtC8HM0&t=37s',
       'video_id': 'ZLMuTtC8HM0'},
      {'author': 'U.S. Food and Drug Administration',
       'channel': 'U.S. Food and Drug Administration',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:42:02](https://www.youtube.com/watch?v=an4G9gKy9wE&t=2522s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'To ensure the qualified facility manager or designated representative can '
               'fulfill the obligations to manage and out daily operations, FDA proposes to '
               'require that a 3PL provide them with the adequate authority and the necessary '
               'resources.',
       'timestamp': 2522,
       'timestamp_label': '[00:42:02]',
       'timestamp_seconds': 2522,
       'tip': 'To ensure the qualified facility manager or designated representative can '
              'fulfill the obligations to manage and out daily operations, FDA proposes to '
              'require that a 3PL provide them with the adequate authority and the necessary '
              'resources.',
       'title': 'National Standards for the Licensure of Wholesale Drug '
                'Distributors&Third-Party Logistics Providers (U.S. Food and Drug '
                'Administration)',
       'url': 'https://www.youtube.com/watch?v=an4G9gKy9wE&t=2522s',
       'video_id': 'an4G9gKy9wE'},
      {'author': 'Matrix One',
       'channel': 'Matrix One',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:48](https://www.youtube.com/watch?v=dd7dQRVr-mQ&t=648s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The 510k process feel free to reach out to the team at Matrix requirements as '
               "we're specialized in the medical device industry we're here to help you as you "
               'launch your medical device to Market we look forward to hearing from you soon.',
       'timestamp': 648,
       'timestamp_label': '[00:10:48]',
       'timestamp_seconds': 648,
       'tip': 'The 510k process feel free to reach out to the team at Matrix requirements as '
              "we're specialized in the medical device industry we're here to help you as you "
              'launch your medical device to Market we look forward to hearing from you soon.',
       'title': 'How to Prepare a Medical Device 510k Submission for FDA (Matrix One)',
       'url': 'https://www.youtube.com/watch?v=dd7dQRVr-mQ&t=648s',
       'video_id': 'dd7dQRVr-mQ'},
      {'author': 'Jon Sheppard Sells',
       'channel': 'Jon Sheppard Sells',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:12](https://www.youtube.com/watch?v=8meyld3BWGg&t=192s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Guarantee the person who bought this is a perfectionist. They they I mean when '
               'you look at things and you buy things on eBay, you need to actually look at '
               "the pictures. If you're buying a big bundle of stuff, you need to actually "
               'look at the pictures.',
       'timestamp': 192,
       'timestamp_label': '[00:03:12]',
       'timestamp_seconds': 192,
       'tip': 'Guarantee the person who bought this is a perfectionist. They they I mean when '
              'you look at things and you buy things on eBay, you need to actually look at the '
              "pictures. If you're buying a big bundle of stuff, you need to actually look at "
              'the pictures.',
       'title': 'Reselling Medical Equipment Is Where The BIG MONEY Is...MUST WATCH VIDEO (Jon '
                'Sheppard Sells)',
       'url': 'https://www.youtube.com/watch?v=8meyld3BWGg&t=192s',
       'video_id': '8meyld3BWGg'},
      {'author': 'Greenlight Guru',
       'channel': 'Greenlight Guru',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:38:59](https://www.youtube.com/watch?v=l108Vrz9wLo&t=2339s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I encourage you to go check out what Scott is up to at powered by MRP to learn '
               'more if you enjoyed this episode reach out to Scott on LinkedIn tell them what '
               "you thought and let them know also I'd personally love to hear from you via "
               'email etienne.',
       'timestamp': 2339,
       'timestamp_label': '[00:38:59]',
       'timestamp_seconds': 2339,
       'tip': 'I encourage you to go check out what Scott is up to at powered by MRP to learn '
              'more if you enjoyed this episode reach out to Scott on LinkedIn tell them what '
              "you thought and let them know also I'd personally love to hear from you via "
              'email etienne.',
       'title': 'The Future of Reprocessed Used Medical Equipment (Greenlight Guru)',
       'url': 'https://www.youtube.com/watch?v=l108Vrz9wLo&t=2339s',
       'video_id': 'l108Vrz9wLo'},
      {'author': 'FGI',
       'channel': 'FGI',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:43](https://www.youtube.com/watch?v=HPAddrORIJU&t=283s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '5 Tesla that three Tesla it is an electromagnet. It is generated by '
               'electricity but it is completely disconnected from building power. So you can '
               'go and turn off every circuit breaker in the building. You can kill power to '
               'the entire city.',
       'timestamp': 283,
       'timestamp_label': '[00:04:43]',
       'timestamp_seconds': 283,
       'tip': '5 Tesla that three Tesla it is an electromagnet. It is generated by electricity '
              'but it is completely disconnected from building power. So you can go and turn '
              'off every circuit breaker in the building. You can kill power to the entire '
              'city.',
       'title': 'S2 E8 – MRI Quench Pipes: Engineering Challenges and Safety Solutions (FGI)',
       'url': 'https://www.youtube.com/watch?v=HPAddrORIJU&t=283s',
       'video_id': 'HPAddrORIJU'},
      {'author': 'Boundary Bay Veterinary Specialty Hospital',
       'channel': 'Boundary Bay Veterinary Specialty Hospital',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:33](https://www.youtube.com/watch?v=xr3Vfmkli0Q&t=93s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Installed today so the quench pipe goes straight up from here out of the '
               'building and only in the event of an emergency if somebody has an emergency '
               'with a magnet we can hit a button and the healing will all vent out through '
               'that pipe.',
       'timestamp': 93,
       'timestamp_label': '[00:01:33]',
       'timestamp_seconds': 93,
       'tip': 'Installed today so the quench pipe goes straight up from here out of the '
              'building and only in the event of an emergency if somebody has an emergency '
              'with a magnet we can hit a button and the healing will all vent out through '
              'that pipe.',
       'title': 'MRI Suite (Boundary Bay Veterinary Specialty Hospital)',
       'url': 'https://www.youtube.com/watch?v=xr3Vfmkli0Q&t=93s',
       'video_id': 'xr3Vfmkli0Q'},
      {'author': 'Doctor Atousa',
       'channel': 'Doctor Atousa',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:39](https://www.youtube.com/watch?v=W-lVX6x4V2U&t=759s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "If I've missed anything let me know below because I'd love to hear what your "
               "experience has been like but other than that I'm going to leave it there and I "
               "will see you in tomorrow's video.",
       'timestamp': 759,
       'timestamp_label': '[00:12:39]',
       'timestamp_seconds': 759,
       'tip': "If I've missed anything let me know below because I'd love to hear what your "
              "experience has been like but other than that I'm going to leave it there and I "
              "will see you in tomorrow's video.",
       'title': 'Biomedical Science vs. Medicine | 6 Key Differences | Atousa (Doctor Atousa)',
       'url': 'https://www.youtube.com/watch?v=W-lVX6x4V2U&t=759s',
       'video_id': 'W-lVX6x4V2U'},
      {'author': 'Bill Whittemore',
       'channel': 'Bill Whittemore',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:21](https://www.youtube.com/watch?v=zLW0PtGvqQE&t=501s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Makes it a lot of fun but when you grow your organization you get to a certain '
               'point and you start finding that these are things that get in your way in in '
               'the in interfere with growth.',
       'timestamp': 501,
       'timestamp_label': '[00:08:21]',
       'timestamp_seconds': 501,
       'tip': 'Makes it a lot of fun but when you grow your organization you get to a certain '
              'point and you start finding that these are things that get in your way in in '
              'the in interfere with growth.',
       'title': 'The used medical equipment marketplace. (Bill Whittemore)',
       'url': 'https://www.youtube.com/watch?v=zLW0PtGvqQE&t=501s',
       'video_id': 'zLW0PtGvqQE'},
      {'author': 'BioFlex Laser Therapy',
       'channel': 'BioFlex Laser Therapy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:38](https://www.youtube.com/watch?v=XwxVKQ5h62U&t=38s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Two separate sections one is the manufacturer of Boflex therapy uh equipment '
               'uh we have different types or forms of equipment everything from professional '
               'systems to at home personal systems uh to veterinarian.',
       'timestamp': 38,
       'timestamp_label': '[00:00:38]',
       'timestamp_seconds': 38,
       'tip': 'Two separate sections one is the manufacturer of Boflex therapy uh equipment uh '
              'we have different types or forms of equipment everything from professional '
              'systems to at home personal systems uh to veterinarian.',
       'title': '1. The Bioflex Solution (BioFlex Laser Therapy)',
       'url': 'https://www.youtube.com/watch?v=XwxVKQ5h62U&t=38s',
       'video_id': 'XwxVKQ5h62U'},
      {'author': 'ATHEENAPANDIAN BIOMEDICAL INDUSTRY',
       'channel': 'ATHEENAPANDIAN BIOMEDICAL INDUSTRY',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:11:36](https://www.youtube.com/watch?v=-ZSbkKuzbMc&t=4296s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Behind this, there will be availability of some scaling mechanisms. Flow rate '
               "adjusting scale mechanisms. It's like a tap it's like a tap. It is uh it it "
               'gives some barrier.',
       'timestamp': 4296,
       'timestamp_label': '[01:11:36]',
       'timestamp_seconds': 4296,
       'tip': 'Behind this, there will be availability of some scaling mechanisms. Flow rate '
              "adjusting scale mechanisms. It's like a tap it's like a tap. It is uh it it "
              'gives some barrier.',
       'title': 'Testing and Calibration of Biomedical Equipment - Basics #calibrations '
                '#troubleshooting (ATHEENAPANDIAN BIOMEDICAL INDUSTRY)',
       'url': 'https://www.youtube.com/watch?v=-ZSbkKuzbMc&t=4296s',
       'video_id': '-ZSbkKuzbMc'}],
 12: [{'author': 'AMORIT EDUCATION',
       'channel': 'AMORIT EDUCATION',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:13](https://www.youtube.com/watch?v=PhHUunSO_iQ&t=313s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Okay, so you\'re probably thinking, "Where on earth do I even start?" Here\'s '
               'a simple four-step action plan. Step one, do a gap analysis, a deep dive '
               'comparing where you are to where the QMR says you need to be. Step two, update '
               'your documents.',
       'timestamp': 313,
       'timestamp_label': '[00:05:13]',
       'timestamp_seconds': 313,
       'tip': 'Okay, so you\'re probably thinking, "Where on earth do I even start?" Here\'s a '
              'simple four-step action plan. Step one, do a gap analysis, a deep dive '
              'comparing where you are to where the QMR says you need to be. Step two, update '
              'your documents.',
       'title': 'QSR to QMSR: What Changes Before Feb 2, 2026 (FDA Medical Devices) (AMORIT '
                'EDUCATION)',
       'url': 'https://www.youtube.com/watch?v=PhHUunSO_iQ&t=313s',
       'video_id': 'PhHUunSO_iQ'},
      {'author': 'Ntwdequiptrans',
       'channel': 'Ntwdequiptrans',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:57](https://www.youtube.com/watch?v=LXOka69hkxs&t=117s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That's why I make sure the carrier's insurance lines up with the freight value "
               'before the wheels ever start turning. When medical equipment is being moved, '
               "it's not just about logistics, it's about lives. That equipment might be "
               'scheduled for use in a clinic the next day.',
       'timestamp': 117,
       'timestamp_label': '[00:01:57]',
       'timestamp_seconds': 117,
       'tip': "That's why I make sure the carrier's insurance lines up with the freight value "
              'before the wheels ever start turning. When medical equipment is being moved, '
              "it's not just about logistics, it's about lives. That equipment might be "
              'scheduled for use in a clinic the next day.',
       'title': 'Don’t Ship Medical Equipment Like Regular Freight—Here’s Why (Ntwdequiptrans)',
       'url': 'https://www.youtube.com/watch?v=LXOka69hkxs&t=117s',
       'video_id': 'LXOka69hkxs'},
      {'author': 'New to Medical Device Sales',
       'channel': 'New to Medical Device Sales',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:39:20](https://www.youtube.com/watch?v=G5Dl1131xAw&t=2360s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Let's just just do this per day. You can elaborate on that because yours is "
               'even worse than mine. I do about 1,000 miles per week, 4,000 per month. So, on '
               "the day to day I'm typically driving It depends, but on average I would say at "
               'minimum at least like 3 hours a day.',
       'timestamp': 2360,
       'timestamp_label': '[00:39:20]',
       'timestamp_seconds': 2360,
       'tip': "Let's just just do this per day. You can elaborate on that because yours is "
              'even worse than mine. I do about 1,000 miles per week, 4,000 per month. So, on '
              "the day to day I'm typically driving It depends, but on average I would say at "
              'minimum at least like 3 hours a day.',
       'title': "The Most Valuable Medical Device Sales Training You'll Ever Watch (New to "
                'Medical Device Sales)',
       'url': 'https://www.youtube.com/watch?v=G5Dl1131xAw&t=2360s',
       'video_id': 'G5Dl1131xAw'},
      {'author': 'Joe Licata | Medical Sales Coach',
       'channel': 'Joe Licata | Medical Sales Coach',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:25:35](https://www.youtube.com/watch?v=KsMhJhbA73k&t=1535s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And you really want to impress them during the interview, have stages '
               'presented on what you think would be a good fit. Have this as part of your '
               'business plan. This is where, you know, I say it all the time, 30-60-90s are '
               'garbage.',
       'timestamp': 1535,
       'timestamp_label': '[00:25:35]',
       'timestamp_seconds': 1535,
       'tip': 'And you really want to impress them during the interview, have stages presented '
              'on what you think would be a good fit. Have this as part of your business plan. '
              'This is where, you know, I say it all the time, 30-60-90s are garbage.',
       'title': 'Navigating Long Sales Cycles in Capital Equipment or Hospital Systems (Joe '
                'Licata | Medical Sales Coach)',
       'url': 'https://www.youtube.com/watch?v=KsMhJhbA73k&t=1535s',
       'video_id': 'KsMhJhbA73k'},
      {'author': 'MedicalMarcom',
       'channel': 'MedicalMarcom',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:47](https://www.youtube.com/watch?v=gGje01O9B44&t=587s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "60-day point, so another 45 days. And at that point, they're going to make a "
               "decision whether it's going to be interactive review or request for additional "
               'information.',
       'timestamp': 587,
       'timestamp_label': '[00:09:47]',
       'timestamp_seconds': 587,
       'tip': "60-day point, so another 45 days. And at that point, they're going to make a "
              "decision whether it's going to be interactive review or request for additional "
              'information.',
       'title': 'How to prepare a 510k submission for FDA (MedicalMarcom)',
       'url': 'https://www.youtube.com/watch?v=gGje01O9B44&t=587s',
       'video_id': 'gGje01O9B44'},
      {'author': 'Vet Candy | Veterinary Education, CE & News',
       'channel': 'Vet Candy | Veterinary Education, CE & News',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:19:42](https://www.youtube.com/watch?v=Zb4YYmRy5x0&t=1182s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "As soon as that scrub gauze has touched an outer layer it's discarded and "
               "that's where your surgery kick bucket comes in so start in the center work "
               'your way in concentric circles outwards.',
       'timestamp': 1182,
       'timestamp_label': '[00:19:42]',
       'timestamp_seconds': 1182,
       'tip': "As soon as that scrub gauze has touched an outer layer it's discarded and "
              "that's where your surgery kick bucket comes in so start in the center work your "
              'way in concentric circles outwards.',
       'title': 'Does a vet tech assist in surgery? (Vet Candy | Veterinary Education, CE & '
                'News)',
       'url': 'https://www.youtube.com/watch?v=Zb4YYmRy5x0&t=1182s',
       'video_id': 'Zb4YYmRy5x0'},
      {'author': 'ISF Customs Broker',
       'channel': 'ISF Customs Broker',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=r84DBdhhg1k&t=15s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "To the USA whether you're looking to expand your product line start a new "
               'business or ensure your medical facility has the.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': "To the USA whether you're looking to expand your product line start a new "
              'business or ensure your medical facility has the.',
       'title': 'How to Import Medical Equipment to the USA: A Comprehensive Guide (ISF '
                'Customs Broker)',
       'url': 'https://www.youtube.com/watch?v=r84DBdhhg1k&t=15s',
       'video_id': 'r84DBdhhg1k'},
      {'author': 'TechNation TV',
       'channel': 'TechNation TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:34:30](https://www.youtube.com/watch?v=x772T1-4M-Q&t=2070s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So you can start building multiple procedures based on all the device types '
               'that you have. So, if you just wanted to do a quick electrical safety '
               "procedure, if you were setting up where you're doing incoming inspection, "
               'right?',
       'timestamp': 2070,
       'timestamp_label': '[00:34:30]',
       'timestamp_seconds': 2070,
       'tip': 'So you can start building multiple procedures based on all the device types '
              'that you have. So, if you just wanted to do a quick electrical safety '
              "procedure, if you were setting up where you're doing incoming inspection, "
              'right?',
       'title': 'ESA700 Series Electrical Safety Analyzers (TechNation TV)',
       'url': 'https://www.youtube.com/watch?v=x772T1-4M-Q&t=2070s',
       'video_id': 'x772T1-4M-Q'},
      {'author': 'MedicalMarcom',
       'channel': 'MedicalMarcom',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:20](https://www.youtube.com/watch?v=nUaPO0mfwKI&t=140s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re interested in, your competitor has said that they will comply to 21 CFR "
               '807. 93, which says, "I will make available all information included in this '
               'premarket premarket notification on safety and effectiveness within 30 days of '
               'request by any person.".',
       'timestamp': 140,
       'timestamp_label': '[00:02:20]',
       'timestamp_seconds': 140,
       'tip': "'re interested in, your competitor has said that they will comply to 21 CFR "
              '807. 93, which says, "I will make available all information included in this '
              'premarket premarket notification on safety and effectiveness within 30 days of '
              'request by any person.".',
       'title': '510k Workshop: How to Prepare an FDA Submission (Part II) (MedicalMarcom)',
       'url': 'https://www.youtube.com/watch?v=nUaPO0mfwKI&t=140s',
       'video_id': 'nUaPO0mfwKI'},
      {'author': 'New to Medical Device Sales',
       'channel': 'New to Medical Device Sales',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:27:48](https://www.youtube.com/watch?v=9bfKQdKe_vU&t=1668s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And then you're like, what does that look like per week? So now I know what I "
               'need per week, right? But I share that with you all because most people will '
               'come to me and they\'re like, "Jacob, I make 6K a month, right?',
       'timestamp': 1668,
       'timestamp_label': '[00:27:48]',
       'timestamp_seconds': 1668,
       'tip': "And then you're like, what does that look like per week? So now I know what I "
              'need per week, right? But I share that with you all because most people will '
              'come to me and they\'re like, "Jacob, I make 6K a month, right?',
       'title': '2026 Is Your Year: How to Break Into Medical Device Sales NOW (New to Medical '
                'Device Sales)',
       'url': 'https://www.youtube.com/watch?v=9bfKQdKe_vU&t=1668s',
       'video_id': '9bfKQdKe_vU'},
      {'author': 'Biomed Plus',
       'channel': 'Biomed Plus',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:39](https://www.youtube.com/watch?v=8Heo1FlDlts&t=39s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Then choose the auto test mode for this example we're going to use the nfpa 99 "
               '2012 ap or applied parts mode and from there you click start button and the '
               'test sequence will begin and the first test up will be the ground resistance '
               'test.',
       'timestamp': 39,
       'timestamp_label': '[00:00:39]',
       'timestamp_seconds': 39,
       'tip': "Then choose the auto test mode for this example we're going to use the nfpa 99 "
              '2012 ap or applied parts mode and from there you click start button and the '
              'test sequence will begin and the first test up will be the ground resistance '
              'test.',
       'title': 'Biomed Plus - Safe-T Sim Electrical Safety Analyzer (Biomed Plus)',
       'url': 'https://www.youtube.com/watch?v=8Heo1FlDlts&t=39s',
       'video_id': '8Heo1FlDlts'},
      {'author': 'Gardner Law',
       'channel': 'Gardner Law',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:30:51](https://www.youtube.com/watch?v=aYQu_0ujhyU&t=1851s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Demands then when the action is complete FDA will terminate the recall and '
               'provide a written notification to the recalling firm next.',
       'timestamp': 1851,
       'timestamp_label': '[00:30:51]',
       'timestamp_seconds': 1851,
       'tip': 'Demands then when the action is complete FDA will terminate the recall and '
              'provide a written notification to the recalling firm next.',
       'title': 'Medical Device Recalls Unpacked: FDA Compliance and Litigation Insights '
                '(Gardner Law)',
       'url': 'https://www.youtube.com/watch?v=aYQu_0ujhyU&t=1851s',
       'video_id': 'aYQu_0ujhyU'},
      {'author': 'Four Paws Animal Hospital & Wellness Center',
       'channel': 'Four Paws Animal Hospital & Wellness Center',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:25](https://www.youtube.com/watch?v=PlDJXzo7cN4&t=145s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The pack this allows a non sterile assistant to pull on the tab to start the '
               'unwrapping process of the pack in surgery by doing it this way they do not.',
       'timestamp': 145,
       'timestamp_label': '[00:02:25]',
       'timestamp_seconds': 145,
       'tip': 'The pack this allows a non sterile assistant to pull on the tab to start the '
              'unwrapping process of the pack in surgery by doing it this way they do not.',
       'title': 'Preparing sterile surgical packs (Four Paws Animal Hospital & Wellness '
                'Center)',
       'url': 'https://www.youtube.com/watch?v=PlDJXzo7cN4&t=145s',
       'video_id': 'PlDJXzo7cN4'},
      {'author': 'TechNation TV',
       'channel': 'TechNation TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:54:35](https://www.youtube.com/watch?v=B0yNPMYGzqM&t=3275s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Information or you know you don't want um you know the people in the lab to be "
               'able to um uh crack into your pxs network and start looking at uh images.',
       'timestamp': 3275,
       'timestamp_label': '[00:54:35]',
       'timestamp_seconds': 3275,
       'tip': "Information or you know you don't want um you know the people in the lab to be "
              'able to um uh crack into your pxs network and start looking at uh images.',
       'title': 'Introduction to AAMI’s Certified Associate Biomedical Technician CABT '
                'Certification (TechNation TV)',
       'url': 'https://www.youtube.com/watch?v=B0yNPMYGzqM&t=3275s',
       'video_id': 'B0yNPMYGzqM'},
      {'author': 'Cerner Corporation',
       'channel': 'Cerner Corporation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:16](https://www.youtube.com/watch?v=hfx0fS26yO0&t=76s)',
       'relevance': 'Attributed practitioner commentary on refurbished diagnostic, surgical, '
                    'veterinary, and aesthetic medical equipment resale, biomed QA, and '
                    'FDA/HIPAA hygiene (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Efficiently finalize procedure and care transition documentation on surgery '
               'day cerner ambulatory surgery center facilitates seamless updates to.',
       'timestamp': 76,
       'timestamp_label': '[00:01:16]',
       'timestamp_seconds': 76,
       'tip': 'Efficiently finalize procedure and care transition documentation on surgery day '
              'cerner ambulatory surgery center facilitates seamless updates to.',
       'title': 'Cerner Ambulatory Surgery Center (ASC) overview (Cerner Corporation)',
       'url': 'https://www.youtube.com/watch?v=hfx0fS26yO0&t=76s',
       'video_id': 'hfx0fS26yO0'}]}
