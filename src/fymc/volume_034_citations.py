"""Curated 180-citation NEMT & Medical Courier Dispatch Arbitrage baseline (15 per chapter across Q1-Q12) mined strictly from verified NEMT & Medical Courier Dispatch Arbitrage YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'100k',
     '1099',
     '837p',
     'access2care',
     'accounts',
     'adult',
     'agreement',
     'ambulatory',
     'app',
     'assisted',
     'associate',
     'auto',
     'background',
     'bambi',
     'bank',
     'barcode',
     'beneficiary',
     'bidding',
     'billing',
     'biological',
     'blood',
     'bloodborne',
     'broker',
     'brokerage',
     'brokers',
     'building',
     'business',
     'call',
     'cancellations',
     'care',
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
 2: {'100k',
     '1099',
     '837p',
     'access2care',
     'accounts',
     'adult',
     'agreement',
     'ambulatory',
     'app',
     'assisted',
     'associate',
     'auto',
     'background',
     'bambi',
     'bank',
     'barcode',
     'beneficiary',
     'bidding',
     'billing',
     'biological',
     'blood',
     'bloodborne',
     'broker',
     'brokerage',
     'brokers',
     'budget',
     'building',
     'business',
     'buyer',
     'call',
     'cancellations',
     'care',
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
 3: {'100k',
     '1099',
     '837p',
     'access2care',
     'accounts',
     'adult',
     'agreement',
     'ambulatory',
     'app',
     'assisted',
     'associate',
     'auto',
     'background',
     'bambi',
     'bank',
     'barcode',
     'beneficiary',
     'bidding',
     'billing',
     'biological',
     'blood',
     'bloodborne',
     'broker',
     'brokerage',
     'brokers',
     'building',
     'business',
     'call',
     'cancellations',
     'care',
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
 4: {'100k',
     '1099',
     '837p',
     'access2care',
     'accounts',
     'adult',
     'agreement',
     'ambulatory',
     'app',
     'assisted',
     'associate',
     'auto',
     'background',
     'bambi',
     'bank',
     'barcode',
     'beneficiary',
     'bidding',
     'billing',
     'biological',
     'blood',
     'bloodborne',
     'broker',
     'brokerage',
     'brokers',
     'budget',
     'building',
     'business',
     'call',
     'cancellations',
     'capital',
     'care',
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
 5: {'100k',
     '1099',
     '837p',
     'access2care',
     'accounts',
     'adult',
     'agreement',
     'ambulatory',
     'app',
     'assisted',
     'associate',
     'audit',
     'auto',
     'avoid',
     'background',
     'bambi',
     'bank',
     'barcode',
     'beneficiary',
     'bidding',
     'billing',
     'biological',
     'blood',
     'bloodborne',
     'broker',
     'brokerage',
     'brokers',
     'building',
     'business',
     'call',
     'cancellations',
     'care',
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
 6: {'100k',
     '1099',
     '837p',
     'access2care',
     'accounts',
     'adult',
     'agreement',
     'ambulatory',
     'app',
     'assisted',
     'associate',
     'auto',
     'background',
     'bambi',
     'bank',
     'barcode',
     'beneficiary',
     'bidding',
     'billing',
     'biological',
     'blood',
     'bloodborne',
     'broker',
     'brokerage',
     'brokers',
     'building',
     'business',
     'call',
     'cancellations',
     'care',
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
 7: {'100k',
     '1099',
     '837p',
     'access2care',
     'accounts',
     'adult',
     'agreement',
     'ambulatory',
     'app',
     'assisted',
     'associate',
     'auto',
     'background',
     'bambi',
     'bank',
     'barcode',
     'beneficiary',
     'bidding',
     'billing',
     'biological',
     'blood',
     'bloodborne',
     'broker',
     'brokerage',
     'brokers',
     'building',
     'business',
     'call',
     'cancellations',
     'care',
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
 8: {'100k',
     '1099',
     '837p',
     'access2care',
     'accounts',
     'adult',
     'agreement',
     'ambulatory',
     'api',
     'app',
     'assisted',
     'associate',
     'auto',
     'background',
     'bambi',
     'bank',
     'barcode',
     'beneficiary',
     'bidding',
     'billing',
     'biological',
     'blood',
     'bloodborne',
     'broker',
     'brokerage',
     'brokers',
     'building',
     'business',
     'call',
     'cancellations',
     'care',
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
 9: {'100k',
     '1099',
     '837p',
     'access2care',
     'accounts',
     'adult',
     'agreement',
     'ambulatory',
     'app',
     'assisted',
     'associate',
     'auto',
     'background',
     'bambi',
     'bank',
     'barcode',
     'beneficiary',
     'bidding',
     'billing',
     'biological',
     'blood',
     'bloodborne',
     'broker',
     'brokerage',
     'brokers',
     'building',
     'business',
     'call',
     'cancellations',
     'care',
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
 10: {'100k',
      '1099',
      '837p',
      'access2care',
      'accounts',
      'adult',
      'agent',
      'agreement',
      'ai',
      'ambulatory',
      'app',
      'assisted',
      'associate',
      'auto',
      'automate',
      'automation',
      'background',
      'bambi',
      'bank',
      'barcode',
      'beneficiary',
      'bidding',
      'billing',
      'biological',
      'blood',
      'bloodborne',
      'broker',
      'brokerage',
      'brokers',
      'building',
      'business',
      'call',
      'cancellations',
      'care',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'100k',
      '1099',
      '837p',
      'access2care',
      'accounts',
      'adult',
      'agreement',
      'ambulatory',
      'app',
      'assisted',
      'associate',
      'auto',
      'background',
      'bambi',
      'bank',
      'barcode',
      'beneficiary',
      'bidding',
      'billing',
      'biological',
      'blood',
      'bloodborne',
      'broker',
      'brokerage',
      'brokers',
      'building',
      'business',
      'call',
      'cancellations',
      'care',
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
 12: {'100k',
      '1099',
      '837p',
      'access2care',
      'accounts',
      'action',
      'adult',
      'agreement',
      'ambulatory',
      'app',
      'assisted',
      'associate',
      'auto',
      'background',
      'bambi',
      'bank',
      'barcode',
      'beneficiary',
      'bidding',
      'billing',
      'biological',
      'blood',
      'bloodborne',
      'broker',
      'brokerage',
      'brokers',
      'building',
      'business',
      'call',
      'cancellations',
      'care',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Nemt University',
      'channel': 'Nemt University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:10](https://www.youtube.com/watch?v=iihLkCuH8NY&t=310s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Statewide Brokers Statewide Brokers under a Statewide brokerage EMT model the '
              'broker manages service Statewide centralizing call centers eligibility '
              'determination and trip authorization Statewide Brokers are typically for-profit '
              'National brokers.',
      'timestamp': 310,
      'timestamp_label': '[00:05:10]',
      'timestamp_seconds': 310,
      'tip': 'Statewide Brokers Statewide Brokers under a Statewide brokerage EMT model the '
             'broker manages service Statewide centralizing call centers eligibility '
             'determination and trip authorization Statewide Brokers are typically for-profit '
             'National brokers.',
      'title': 'WHAT ARE THE 4 DIFFERENT TYPES OF NEMT BROKER MODELS (🤐Explained) (Nemt '
               'University)',
      'url': 'https://www.youtube.com/watch?v=iihLkCuH8NY&t=310s',
      'video_id': 'iihLkCuH8NY'},
     {'author': 'Nemt University',
      'channel': 'Nemt University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:32](https://www.youtube.com/watch?v=DoH4BLPOrvI&t=152s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The profit margin on a private pay client might be much higher than a client '
              'who comes through a broker. How many trips do you need to hit that? And where '
              'are those trips coming from? Are you relying heavily on brokers or are you '
              'actively building a private pay clientele?',
      'timestamp': 152,
      'timestamp_label': '[00:02:32]',
      'timestamp_seconds': 152,
      'tip': 'The profit margin on a private pay client might be much higher than a client who '
             'comes through a broker. How many trips do you need to hit that? And where are '
             'those trips coming from? Are you relying heavily on brokers or are you actively '
             'building a private pay clientele?',
      'title': 'How To CALCULATE NEMT RATE Formulas| NEMT For Dummies Podcast '
               'Ep.11(NemtUniversity) (Nemt University)',
      'url': 'https://www.youtube.com/watch?v=DoH4BLPOrvI&t=152s',
      'video_id': 'DoH4BLPOrvI'},
     {'author': 'NEMT Growth Machine',
      'channel': 'NEMT Growth Machine',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:29](https://www.youtube.com/watch?v=wens2SHO0_A&t=149s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, super important question I think you got to ask yourself as well. The '
              'second thing you want to do, in my opinion, is call around. Get some quotes '
              'from people who are in your market. Every single NMT business owner operator '
              'has done this in the beginning.',
      'timestamp': 149,
      'timestamp_label': '[00:02:29]',
      'timestamp_seconds': 149,
      'tip': 'So, super important question I think you got to ask yourself as well. The second '
             'thing you want to do, in my opinion, is call around. Get some quotes from people '
             'who are in your market. Every single NMT business owner operator has done this '
             'in the beginning.',
      'title': 'Pricing your NEMT services! (NEMT Growth Machine)',
      'url': 'https://www.youtube.com/watch?v=wens2SHO0_A&t=149s',
      'video_id': 'wens2SHO0_A'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:05](https://www.youtube.com/watch?v=R4q_XZ1pARQ&t=305s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'By sending out reminders for passengers that choose to opt in to the service, '
              "you'll find more clients ready to go on time. So, you don't lose time or "
              'revenue. See how RouteGenie decreases the number of no shows at your business.',
      'timestamp': 305,
      'timestamp_label': '[00:05:05]',
      'timestamp_seconds': 305,
      'tip': 'By sending out reminders for passengers that choose to opt in to the service, '
             "you'll find more clients ready to go on time. So, you don't lose time or "
             'revenue. See how RouteGenie decreases the number of no shows at your business.',
      'title': 'How to Reduce No-Show Passengers | NEMT Business Education | RouteGenie '
               '(RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=R4q_XZ1pARQ&t=305s',
      'video_id': 'R4q_XZ1pARQ'},
     {'author': 'Business Assurance',
      'channel': 'Business Assurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:41](https://www.youtube.com/watch?v=-U66kxsJM0o&t=581s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Business thrives you'll enjoy the financial freedom and flexibility that comes "
              'with being Your Own Boss the medical Courier industry offers significant '
              'earning potential especially as you expand your client base and service.',
      'timestamp': 581,
      'timestamp_label': '[00:09:41]',
      'timestamp_seconds': 581,
      'tip': "Business thrives you'll enjoy the financial freedom and flexibility that comes "
             'with being Your Own Boss the medical Courier industry offers significant earning '
             'potential especially as you expand your client base and service.',
      'title': 'LLC for Medical Courier Business - Step by Step | How to Start Medical Courier '
               'Delivery Service 2026 (Business Assurance)',
      'url': 'https://www.youtube.com/watch?v=-U66kxsJM0o&t=581s',
      'video_id': '-U66kxsJM0o'},
     {'author': 'LearnCargo',
      'channel': 'LearnCargo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=MOdO2Zzw1wI&t=32s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I try to educate my clients when they get in the car or when I call them and '
              'they say I tried to call them to cancel the trip. I try to tell them, make sure '
              "you call the broker if you know you're not going because we are out here to "
              'come help you guys get back and forth.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': 'I try to educate my clients when they get in the car or when I call them and '
             'they say I tried to call them to cancel the trip. I try to tell them, make sure '
             "you call the broker if you know you're not going because we are out here to come "
             'help you guys get back and forth.',
      'title': 'How to Handle NEMT Cancelations (LearnCargo)',
      'url': 'https://www.youtube.com/watch?v=MOdO2Zzw1wI&t=32s',
      'video_id': 'MOdO2Zzw1wI'},
     {'author': 'Giganomic Era',
      'channel': 'Giganomic Era',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:43](https://www.youtube.com/watch?v=wJcNFJjkNwA&t=283s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, depending on your niche, some clients may ask for cargo van insurance, '
              'especially if medication, specimens, equipment, or expensive medical products '
              'are involved. General liability, that usually protects the business side '
              'itself.',
      'timestamp': 283,
      'timestamp_label': '[00:04:43]',
      'timestamp_seconds': 283,
      'tip': 'Now, depending on your niche, some clients may ask for cargo van insurance, '
             'especially if medication, specimens, equipment, or expensive medical products '
             'are involved. General liability, that usually protects the business side itself.',
      'title': 'Medical Courier Insurance: Stop Paying Too Much! (Giganomic Era)',
      'url': 'https://www.youtube.com/watch?v=wJcNFJjkNwA&t=283s',
      'video_id': 'wJcNFJjkNwA'},
     {'author': 'MJ Business Academy',
      'channel': 'MJ Business Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=rIDRpTROLM8&t=63s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'All right so now we got the two chairs um pulled out so we can accommodate um '
              'two ambulatory clients and one wheelchair passenger in this van or if Monica '
              'collapsed the chairs again then of course we could accommodate two wheelchair '
              'clients in this particular vehicle.',
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': 'All right so now we got the two chairs um pulled out so we can accommodate um '
             'two ambulatory clients and one wheelchair passenger in this van or if Monica '
             'collapsed the chairs again then of course we could accommodate two wheelchair '
             'clients in this particular vehicle.',
      'title': 'We made over 100,000 with this 30,000 van (MJ Business Academy)',
      'url': 'https://www.youtube.com/watch?v=rIDRpTROLM8&t=63s',
      'video_id': 'rIDRpTROLM8'},
     {'author': 'Nemt University',
      'channel': 'Nemt University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:56](https://www.youtube.com/watch?v=yrd3dFXxLmw&t=1316s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Frequent visits to clinics offering you another potential niche market okay 32 '
              'post Accident Recovery transport clients recovering from accidents we did that '
              'okay.',
      'timestamp': 1316,
      'timestamp_label': '[00:21:56]',
      'timestamp_seconds': 1316,
      'tip': 'Frequent visits to clinics offering you another potential niche market okay 32 '
             'post Accident Recovery transport clients recovering from accidents we did that '
             'okay.',
      'title': '30 WAYS TO MAKE MONEY|| How To Get Started with Private Pay Clients for Your '
               'NEMT Business (Nemt University)',
      'url': 'https://www.youtube.com/watch?v=yrd3dFXxLmw&t=1316s',
      'video_id': 'yrd3dFXxLmw'},
     {'author': 'Markie Williams Online Certification Courses',
      'channel': 'Markie Williams Online Certification Courses',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:01](https://www.youtube.com/watch?v=gTCFIB4W4q0&t=61s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'HIPPA which ensures compliance with the health insurance portability and '
              'accountability act. OSHA which will cover workplace safety health regulations '
              'bloodborne pathogens training on handling potentially infectious material when '
              'becoming an organ transport courier service.',
      'timestamp': 61,
      'timestamp_label': '[00:01:01]',
      'timestamp_seconds': 61,
      'tip': 'HIPPA which ensures compliance with the health insurance portability and '
             'accountability act. OSHA which will cover workplace safety health regulations '
             'bloodborne pathogens training on handling potentially infectious material when '
             'becoming an organ transport courier service.',
      'title': 'Organ Transport Courier Service 🚑 (Markie Williams Online Certification '
               'Courses)',
      'url': 'https://www.youtube.com/watch?v=gTCFIB4W4q0&t=61s',
      'video_id': 'gTCFIB4W4q0'},
     {'author': 'Giganomic Era',
      'channel': 'Giganomic Era',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=zKn-xcqMKhg&t=91s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll probably receive five different quotes for the exact same request. Not "
              'because somebody is wrong, because every company have different costs, '
              'different insurance, different scheduling, different service levels, different '
              'response times, and a different business model.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': "'ll probably receive five different quotes for the exact same request. Not "
             'because somebody is wrong, because every company have different costs, different '
             'insurance, different scheduling, different service levels, different response '
             'times, and a different business model.',
      'title': 'Medical Courier Pricing Secret | Pharmacies Will Pay More (Giganomic Era)',
      'url': 'https://www.youtube.com/watch?v=zKn-xcqMKhg&t=91s',
      'video_id': 'zKn-xcqMKhg'},
     {'author': 'Thank You',
      'channel': 'Thank You',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:13](https://www.youtube.com/watch?v=XlBuD6TGCWU&t=133s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You require you'll gain the competitive advantage in your corner of the "
              'healthcare Market thank you for allowing us to share these few moments with you '
              'and we look forward to speaking with you welcome to diligent Delivery Systems '
              'your total delivery solution.',
      'timestamp': 133,
      'timestamp_label': '[00:02:13]',
      'timestamp_seconds': 133,
      'tip': "You require you'll gain the competitive advantage in your corner of the "
             'healthcare Market thank you for allowing us to share these few moments with you '
             'and we look forward to speaking with you welcome to diligent Delivery Systems '
             'your total delivery solution.',
      'title': 'STAT MEDICAL COURIERS | Diligent Delivery Systems (Thank You)',
      'url': 'https://www.youtube.com/watch?v=XlBuD6TGCWU&t=133s',
      'video_id': 'XlBuD6TGCWU'},
     {'author': 'AMS Vans',
      'channel': 'AMS Vans',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:41](https://www.youtube.com/watch?v=-DCWDiGaTn0&t=101s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Them down to the low all the way low position that's where it has to be locked "
              'in you know push it up slide it forward into the antler cradles you have your '
              "pin right here it's gonna go over to the hook so now it's locked in place and "
              "you're done.",
      'timestamp': 101,
      'timestamp_label': '[00:01:41]',
      'timestamp_seconds': 101,
      'tip': "Them down to the low all the way low position that's where it has to be locked "
             'in you know push it up slide it forward into the antler cradles you have your '
             "pin right here it's gonna go over to the hook so now it's locked in place and "
             "you're done.",
      'title': 'Accessible Van as NEMT | AMS Vans (AMS Vans)',
      'url': 'https://www.youtube.com/watch?v=-DCWDiGaTn0&t=101s',
      'video_id': '-DCWDiGaTn0'},
     {'author': 'United Medical Transportation Providers Group',
      'channel': 'United Medical Transportation Providers Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:48](https://www.youtube.com/watch?v=0Z6CsGngipI&t=1428s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Some of it has to do with that in some way I'm not exactly sure but I'll "
              "continue to learn anyways I'm going to continue to learn and you need to "
              "continue to learn because when you do I'll see you at the top.",
      'timestamp': 1428,
      'timestamp_label': '[00:23:48]',
      'timestamp_seconds': 1428,
      'tip': "Some of it has to do with that in some way I'm not exactly sure but I'll "
             "continue to learn anyways I'm going to continue to learn and you need to "
             "continue to learn because when you do I'll see you at the top.",
      'title': "Let's Talk Movidcare and Associated Broker Tactics, Facility Contracts, "
               'Agreements, and More! (United Medical Transportation Providers Group)',
      'url': 'https://www.youtube.com/watch?v=0Z6CsGngipI&t=1428s',
      'video_id': '0Z6CsGngipI'},
     {'author': 'Nemiton',
      'channel': 'Nemiton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:38](https://www.youtube.com/watch?v=6nWzJ25nMDg&t=278s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Where these 10 clients fit in the bigger machine. The strongest revenue model '
              'in this industry, the one behind that half million-dollar 24-month case study, '
              'is 33 33 33. 1/3 Medicaid broker trips as your baseline. 1/3 direct facility '
              'contracts, recurring, higher margin.',
      'timestamp': 278,
      'timestamp_label': '[00:04:38]',
      'timestamp_seconds': 278,
      'tip': 'Where these 10 clients fit in the bigger machine. The strongest revenue model in '
             'this industry, the one behind that half million-dollar 24-month case study, is '
             '33 33 33. 1/3 Medicaid broker trips as your baseline. 1/3 direct facility '
             'contracts, recurring, higher margin.',
      'title': 'First 10 NEMT Clients Without a Broker (Nemiton)',
      'url': 'https://www.youtube.com/watch?v=6nWzJ25nMDg&t=278s',
      'video_id': '6nWzJ25nMDg'}],
 2: [{'author': 'Nemiton',
      'channel': 'Nemiton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:55](https://www.youtube.com/watch?v=6nWzJ25nMDg&t=295s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '1/3 direct facility contracts, recurring, higher margin. 1/3 private pay, '
              'fastest payment, highest margin of all. Your first 10 clients are you building '
              'legs two and three, and every client you add there makes you less hostage to '
              'broker rates.',
      'timestamp': 295,
      'timestamp_label': '[00:04:55]',
      'timestamp_seconds': 295,
      'tip': '1/3 direct facility contracts, recurring, higher margin. 1/3 private pay, '
             'fastest payment, highest margin of all. Your first 10 clients are you building '
             'legs two and three, and every client you add there makes you less hostage to '
             'broker rates.',
      'title': 'First 10 NEMT Clients Without a Broker (Nemiton)',
      'url': 'https://www.youtube.com/watch?v=6nWzJ25nMDg&t=295s',
      'video_id': '6nWzJ25nMDg'},
     {'author': 'ThatNEMTGirl',
      'channel': 'ThatNEMTGirl',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:47](https://www.youtube.com/watch?v=govQRXzu6Rg&t=47s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, I want to give you some background info on what you need to do to make sure '
              "that you're maximizing your loads to make the top dollar for each trip that you "
              "get. So, first things first, let's talk about the type of van that was used for "
              'this broker contract.',
      'timestamp': 47,
      'timestamp_label': '[00:00:47]',
      'timestamp_seconds': 47,
      'tip': 'So, I want to give you some background info on what you need to do to make sure '
             "that you're maximizing your loads to make the top dollar for each trip that you "
             "get. So, first things first, let's talk about the type of van that was used for "
             'this broker contract.',
      'title': 'How I Made $100K with ONE Van + ONE Broker | NEMT Business Strategy (2024) '
               '(ThatNEMTGirl)',
      'url': 'https://www.youtube.com/watch?v=govQRXzu6Rg&t=47s',
      'video_id': 'govQRXzu6Rg'},
     {'author': 'MJ Business Academy',
      'channel': 'MJ Business Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:43](https://www.youtube.com/watch?v=bX8mww6N5BM&t=643s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "We've seen individuals go from one vehicle and then 3 months later they got "
              'four and five. So, you know, I know that sometimes when you partner with the '
              'broker is really hard to really focus on your private pay clientele because '
              'some brokers keep you so busy.',
      'timestamp': 643,
      'timestamp_label': '[00:10:43]',
      'timestamp_seconds': 643,
      'tip': "We've seen individuals go from one vehicle and then 3 months later they got four "
             'and five. So, you know, I know that sometimes when you partner with the broker '
             'is really hard to really focus on your private pay clientele because some '
             'brokers keep you so busy.',
      'title': 'How to Find NEMT Clients for Your Business (MJ Business Academy)',
      'url': 'https://www.youtube.com/watch?v=bX8mww6N5BM&t=643s',
      'video_id': 'bX8mww6N5BM'},
     {'author': 'JT Automations',
      'channel': 'JT Automations',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:04](https://www.youtube.com/watch?v=gpeFpvbyWg4&t=1024s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, I would recommend at a bare minimum, go get a LLC in your state. Go get a '
              'EIN number for free from IRS. Go set up your business bank account once you get '
              'your letter of good standing and everything from that, right? And you might '
              'need basic invoice templates.',
      'timestamp': 1024,
      'timestamp_label': '[00:17:04]',
      'timestamp_seconds': 1024,
      'tip': 'So, I would recommend at a bare minimum, go get a LLC in your state. Go get a '
             'EIN number for free from IRS. Go set up your business bank account once you get '
             'your letter of good standing and everything from that, right? And you might need '
             'basic invoice templates.',
      'title': 'Step By Step Non - CDL Masterclass (Independent Medical Courier Course) (JT '
               'Automations)',
      'url': 'https://www.youtube.com/watch?v=gpeFpvbyWg4&t=1024s',
      'video_id': 'gpeFpvbyWg4'},
     {'author': 'Geoff Cole',
      'channel': 'Geoff Cole',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:23](https://www.youtube.com/watch?v=Gl5nc0qukvE&t=383s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s only about a 30-minut drive. Simple, consistent work that pays steadily. It "
              'may not be the biggest contract, but it gets your foot in the door. Once you '
              'prove yourself, you can start bidding on bigger contracts or stack multiple '
              'smaller ones.',
      'timestamp': 383,
      'timestamp_label': '[00:06:23]',
      'timestamp_seconds': 383,
      'tip': "'s only about a 30-minut drive. Simple, consistent work that pays steadily. It "
             'may not be the biggest contract, but it gets your foot in the door. Once you '
             'prove yourself, you can start bidding on bigger contracts or stack multiple '
             'smaller ones.',
      'title': 'The $2,000,000 Direct Medical Courier Contract (Must Watch) (Geoff Cole)',
      'url': 'https://www.youtube.com/watch?v=Gl5nc0qukvE&t=383s',
      'video_id': 'Gl5nc0qukvE'},
     {'author': 'Giganomic Era',
      'channel': 'Giganomic Era',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:58](https://www.youtube.com/watch?v=jv40GZPfRSc&t=418s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can have your first contract conversations this week. While everyone else '
              "is out here fighting for surge pricing on DoorDash, you'll be the one who owns "
              'your clients, owns your routes, and building something that actually pays.',
      'timestamp': 418,
      'timestamp_label': '[00:06:58]',
      'timestamp_seconds': 418,
      'tip': 'You can have your first contract conversations this week. While everyone else is '
             "out here fighting for surge pricing on DoorDash, you'll be the one who owns your "
             'clients, owns your routes, and building something that actually pays.',
      'title': 'Hospital Specimen Deliveries: The Untapped Gig Economy (Giganomic Era)',
      'url': 'https://www.youtube.com/watch?v=jv40GZPfRSc&t=418s',
      'video_id': 'jv40GZPfRSc'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:30](https://www.youtube.com/watch?v=BuyVTPmpWAQ&t=150s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Keeping track of all your rates for each account and calculating the price for '
              'each trip should be placed in the trust of your NEMT billing software. Types of '
              'fees include load fee, per mile rate, no show fee, minimum charge, flat rate '
              'fee, and weekend and holiday fees.',
      'timestamp': 150,
      'timestamp_label': '[00:02:30]',
      'timestamp_seconds': 150,
      'tip': 'Keeping track of all your rates for each account and calculating the price for '
             'each trip should be placed in the trust of your NEMT billing software. Types of '
             'fees include load fee, per mile rate, no show fee, minimum charge, flat rate '
             'fee, and weekend and holiday fees.',
      'title': 'Determining the Rate Structure for Your Paratransit Services | NEMT Business '
               'Education | RouteGenie (RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=BuyVTPmpWAQ&t=150s',
      'video_id': 'BuyVTPmpWAQ'},
     {'author': 'LearnCargo',
      'channel': 'LearnCargo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:13](https://www.youtube.com/watch?v=703O5MjUp9A&t=133s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "That means that you're pretty much on call 24/7. Now, many people don't like "
              "that because they have a steady schedule or they don't know what time they are "
              "going to be available. So, that's why these type of gigs do pay more money "
              "because it's urgent.",
      'timestamp': 133,
      'timestamp_label': '[00:02:13]',
      'timestamp_seconds': 133,
      'tip': "That means that you're pretty much on call 24/7. Now, many people don't like "
             "that because they have a steady schedule or they don't know what time they are "
             "going to be available. So, that's why these type of gigs do pay more money "
             "because it's urgent.",
      'title': '5 Types of Medical Courier Jobs: Which One Should You Choose? (LearnCargo)',
      'url': 'https://www.youtube.com/watch?v=703O5MjUp9A&t=133s',
      'video_id': '703O5MjUp9A'},
     {'author': 'MediRoutes NEMT Software',
      'channel': 'MediRoutes NEMT Software',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:02](https://www.youtube.com/watch?v=nLjDVheWODU&t=482s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Country and processes more than 10 million trips a year many routes simplified '
              'automated scheduling dispatching and billing means you can focus on what '
              'matters most your customer and your bottom line routes transforming nemt for '
              'you and your customer.',
      'timestamp': 482,
      'timestamp_label': '[00:08:02]',
      'timestamp_seconds': 482,
      'tip': 'Country and processes more than 10 million trips a year many routes simplified '
             'automated scheduling dispatching and billing means you can focus on what matters '
             'most your customer and your bottom line routes transforming nemt for you and '
             'your customer.',
      'title': 'MediRoutes NEMT Software (MediRoutes NEMT Software)',
      'url': 'https://www.youtube.com/watch?v=nLjDVheWODU&t=482s',
      'video_id': 'nLjDVheWODU'},
     {'author': 'Sarah Davis | The D&G Way',
      'channel': 'Sarah Davis | The D&G Way',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:02](https://www.youtube.com/watch?v=9gV2o-MVpEI&t=242s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Continue to do the work and that is what's going to make you like me, not "
              'looking like me, not dressing like me, not structuring your business like mine, '
              'but doing the actual work, making the phone calls. And then, when you get the '
              'contract, the real work actually begins.',
      'timestamp': 242,
      'timestamp_label': '[00:04:02]',
      'timestamp_seconds': 242,
      'tip': "Continue to do the work and that is what's going to make you like me, not "
             'looking like me, not dressing like me, not structuring your business like mine, '
             'but doing the actual work, making the phone calls. And then, when you get the '
             'contract, the real work actually begins.',
      'title': 'Medical Courier & Courier Contracts Advice From a 6-Figure Earner (Sarah Davis '
               '| The D&G Way)',
      'url': 'https://www.youtube.com/watch?v=9gV2o-MVpEI&t=242s',
      'video_id': '9gV2o-MVpEI'},
     {'author': 'United Medical Transportation Providers Group',
      'channel': 'United Medical Transportation Providers Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:43](https://www.youtube.com/watch?v=HvP2_Kts7vA&t=403s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Courtesy Transport Services LLC and its owners uh have agreed to collectively '
              'play pay $900,000 to resolve allegations that they defrauded Medicare and '
              'Medicaid by billing for ambulance transportation services that were not '
              'medically necessary.',
      'timestamp': 403,
      'timestamp_label': '[00:06:43]',
      'timestamp_seconds': 403,
      'tip': 'Courtesy Transport Services LLC and its owners uh have agreed to collectively '
             'play pay $900,000 to resolve allegations that they defrauded Medicare and '
             'Medicaid by billing for ambulance transportation services that were not '
             'medically necessary.',
      'title': 'NEMT: Use this information as leverage and inspiration when negotiating with '
               'Top Tier Targets! (United Medical Transportation Providers Group)',
      'url': 'https://www.youtube.com/watch?v=HvP2_Kts7vA&t=403s',
      'video_id': 'HvP2_Kts7vA'},
     {'author': 'Giganomic Era',
      'channel': 'Giganomic Era',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:55](https://www.youtube.com/watch?v=EgbN0cCrzpk&t=175s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I'll be your scheduled courier and your on-call stat driver. That locks you in "
              "as their primary contact. Nobody shopping around for a backup when you're "
              "already there. Model three is monthly retainer. So, you're going to charge a "
              'flat monthly fee for guaranteed availability.',
      'timestamp': 175,
      'timestamp_label': '[00:02:55]',
      'timestamp_seconds': 175,
      'tip': "I'll be your scheduled courier and your on-call stat driver. That locks you in "
             "as their primary contact. Nobody shopping around for a backup when you're "
             "already there. Model three is monthly retainer. So, you're going to charge a "
             'flat monthly fee for guaranteed availability.',
      'title': 'Medical Courier Daily Rate Negotiation | Price Anchoring Strategy (Giganomic '
               'Era)',
      'url': 'https://www.youtube.com/watch?v=EgbN0cCrzpk&t=175s',
      'video_id': 'EgbN0cCrzpk'},
     {'author': 'STICK WITH US DELIVERY 🚚 📦',
      'channel': 'STICK WITH US DELIVERY 🚚 📦',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:19](https://www.youtube.com/watch?v=gvxg69CITsE&t=319s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Their contracts from y'all they gonna be mad I gave y'all this man but I'm "
              "going give it to y'all so check it go to USA spending in.gov.",
      'timestamp': 319,
      'timestamp_label': '[00:05:19]',
      'timestamp_seconds': 319,
      'tip': "Their contracts from y'all they gonna be mad I gave y'all this man but I'm going "
             "give it to y'all so check it go to USA spending in.gov.",
      'title': 'MEDICAL COURIER DIRECT CONTRACT!!! MAKE $2500 A WEEK (STICK WITH US DELIVERY 🚚 '
               '📦)',
      'url': 'https://www.youtube.com/watch?v=gvxg69CITsE&t=319s',
      'video_id': 'gvxg69CITsE'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:55](https://www.youtube.com/watch?v=382JPpV04Tg&t=235s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Have control over their trip request when you use software with a built-in '
              'passenger app they do a passenger app gives your private pay clients the.',
      'timestamp': 235,
      'timestamp_label': '[00:03:55]',
      'timestamp_seconds': 235,
      'tip': 'Have control over their trip request when you use software with a built-in '
             'passenger app they do a passenger app gives your private pay clients the.',
      'title': "NEMT Dispatch Software: Why It's Essential for Every NEMT Business | "
               'RouteGenie (RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=382JPpV04Tg&t=235s',
      'video_id': '382JPpV04Tg'},
     {'author': 'MICHAEL PACHECO',
      'channel': 'MICHAEL PACHECO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:13](https://www.youtube.com/watch?v=QWuDUoAMiQU&t=133s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Depending on your business model, potential customers may include healthcare '
              'organizations, assisted living communities, schools, corporations, logistics '
              'companies, brokers, private pay customers, government agencies, and other '
              'organizations.',
      'timestamp': 133,
      'timestamp_label': '[00:02:13]',
      'timestamp_seconds': 133,
      'tip': 'Depending on your business model, potential customers may include healthcare '
             'organizations, assisted living communities, schools, corporations, logistics '
             'companies, brokers, private pay customers, government agencies, and other '
             'organizations.',
      'title': 'How to Start a Transportation Business in 2026 | NEMT, Medical Courier & '
               'Logistics (MICHAEL PACHECO)',
      'url': 'https://www.youtube.com/watch?v=QWuDUoAMiQU&t=133s',
      'video_id': 'QWuDUoAMiQU'}],
 3: [{'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:24](https://www.youtube.com/watch?v=OVN-rYxkYf8&t=264s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Establishing competitive and sustainable pricing for an NEMT business is a '
              'crucial element of success. Your prices must cover the cost of providing '
              'services and maintain a healthy profit margin. When setting rates for your NEMT '
              'service, the USOA recommends several points.',
      'timestamp': 264,
      'timestamp_label': '[00:04:24]',
      'timestamp_seconds': 264,
      'tip': 'Establishing competitive and sustainable pricing for an NEMT business is a '
             'crucial element of success. Your prices must cover the cost of providing '
             'services and maintain a healthy profit margin. When setting rates for your NEMT '
             'service, the USOA recommends several points.',
      'title': 'How to Justify Your NEMT Rates | NEMT Pricing | RouteGenie (RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=OVN-rYxkYf8&t=264s',
      'video_id': 'OVN-rYxkYf8'},
     {'author': 'Nemiton',
      'channel': 'Nemiton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:13](https://www.youtube.com/watch?v=LjAb-IUYxbM&t=613s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The hidden cost inside each one and what it does to your margins over time. We '
              'have built a free NEMT broker comparison worksheet that lets you track your '
              'actual per trip rate across multiple brokers and identify exactly where you are '
              'leaving money on the table.',
      'timestamp': 613,
      'timestamp_label': '[00:10:13]',
      'timestamp_seconds': 613,
      'tip': 'The hidden cost inside each one and what it does to your margins over time. We '
             'have built a free NEMT broker comparison worksheet that lets you track your '
             'actual per trip rate across multiple brokers and identify exactly where you are '
             'leaving money on the table.',
      'title': 'NEMT Broker Payment Models Explained: Fee-for-Service, Capitation, MCO & '
               'Hybrid (Nemiton)',
      'url': 'https://www.youtube.com/watch?v=LjAb-IUYxbM&t=613s',
      'video_id': 'LjAb-IUYxbM'},
     {'author': 'Giganomic Era',
      'channel': 'Giganomic Era',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:48](https://www.youtube.com/watch?v=YewfRfz9eUI&t=288s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'That allows you to generate more revenue without drastically increasing your '
              'mileage or your operating costs. That flexibility creates opportunities to '
              'stack multiple accounts together in a way that makes sense for your business.',
      'timestamp': 288,
      'timestamp_label': '[00:04:48]',
      'timestamp_seconds': 288,
      'tip': 'That allows you to generate more revenue without drastically increasing your '
             'mileage or your operating costs. That flexibility creates opportunities to stack '
             'multiple accounts together in a way that makes sense for your business.',
      'title': '"The Medical Courier Schedule Nobody Warns You About" (Giganomic Era)',
      'url': 'https://www.youtube.com/watch?v=YewfRfz9eUI&t=288s',
      'video_id': 'YewfRfz9eUI'},
     {'author': 'NEMT Growth Machine',
      'channel': 'NEMT Growth Machine',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:40](https://www.youtube.com/watch?v=nSB43YYfRs0&t=460s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, the costs of this video were for the full breakdown of this vehicle, right? '
              'If you got a sedan, then your cost will be different. My opinion is that this '
              'vehicle is on the higher end of a vehicle you would get for this type of '
              'business, right?',
      'timestamp': 460,
      'timestamp_label': '[00:07:40]',
      'timestamp_seconds': 460,
      'tip': 'So, the costs of this video were for the full breakdown of this vehicle, right? '
             'If you got a sedan, then your cost will be different. My opinion is that this '
             'vehicle is on the higher end of a vehicle you would get for this type of '
             'business, right?',
      'title': 'What Our Wheelchair Van Really Costs (and How We Made It Better) (NEMT Growth '
               'Machine)',
      'url': 'https://www.youtube.com/watch?v=nSB43YYfRs0&t=460s',
      'video_id': 'nSB43YYfRs0'},
     {'author': 'Alton Arell',
      'channel': 'Alton Arell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:18](https://www.youtube.com/watch?v=eOHfnK5euaw&t=318s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'t tell exactly what it is that you do right out the gate. Go get your business "
              "bank account. Get a separate bank account. Don't put this stuff in your "
              'personal bank account.',
      'timestamp': 318,
      'timestamp_label': '[00:05:18]',
      'timestamp_seconds': 318,
      'tip': "'t tell exactly what it is that you do right out the gate. Go get your business "
             "bank account. Get a separate bank account. Don't put this stuff in your personal "
             'bank account.',
      'title': 'How to start a Medical Courier Business (Alton Arell)',
      'url': 'https://www.youtube.com/watch?v=eOHfnK5euaw&t=318s',
      'video_id': 'eOHfnK5euaw'},
     {'author': 'Wheelchair & Stretcher Transportation Services',
      'channel': 'Wheelchair & Stretcher Transportation Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=svdIU5f-6tA&t=63s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Unless you understand how to to negotiate contracts, you shouldn't be doing "
              "that. And none of you, I don't care anybody who's talking to me, nobody will be "
              'able to tell me, "Oh, I only do broker work and I\'m making good money and I '
              'drive Dodge Caravans.".',
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': "Unless you understand how to to negotiate contracts, you shouldn't be doing "
             "that. And none of you, I don't care anybody who's talking to me, nobody will be "
             'able to tell me, "Oh, I only do broker work and I\'m making good money and I '
             'drive Dodge Caravans.".',
      'title': 'How to Build a Private Pay Medical Transportation Company (Wheelchair & '
               'Stretcher Transportation Services)',
      'url': 'https://www.youtube.com/watch?v=svdIU5f-6tA&t=63s',
      'video_id': 'svdIU5f-6tA'},
     {'author': 'United Medical Transportation Providers Group',
      'channel': 'United Medical Transportation Providers Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=gJ4V8yGqCFY&t=15s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And you are the broker.com helping you to build a highly effective and highly '
              "profitable broker business i'll try to make this video as.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'And you are the broker.com helping you to build a highly effective and highly '
             "profitable broker business i'll try to make this video as.",
      'title': "Let's Talk About Your Non-Emergency Medical Transportation Contracts and "
               'Service Agreements (United Medical Transportation Providers Group)',
      'url': 'https://www.youtube.com/watch?v=gJ4V8yGqCFY&t=15s',
      'video_id': 'gJ4V8yGqCFY'},
     {'author': 'Medical Courier Connection',
      'channel': 'Medical Courier Connection',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:08](https://www.youtube.com/watch?v=qLWRmpKkEP0&t=428s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And that's how you move from simply being busy to actually building a more "
              'profitable medical courier business. Shout out to our members here on YouTube. '
              "Thanks for becoming a member. We hope you're finding our member-only content "
              'informative and useful.',
      'timestamp': 428,
      'timestamp_label': '[00:07:08]',
      'timestamp_seconds': 428,
      'tip': "And that's how you move from simply being busy to actually building a more "
             'profitable medical courier business. Shout out to our members here on YouTube. '
             "Thanks for becoming a member. We hope you're finding our member-only content "
             'informative and useful.',
      'title': 'Stat vs. Route Delivery for Medical Couriers (Medical Courier Connection)',
      'url': 'https://www.youtube.com/watch?v=qLWRmpKkEP0&t=428s',
      'video_id': 'qLWRmpKkEP0'},
     {'author': 'Bambi',
      'channel': 'Bambi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=ICI0C5f_vjE&t=92s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um, I did my research on other systems out there and I work with certain '
              'systems that there it was it was similar to Bambi, but it was much harder to '
              "navigate and more it was c it was very high. It wasn't what we wanted to to "
              'experience with the the cost.',
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': 'Um, I did my research on other systems out there and I work with certain systems '
             'that there it was it was similar to Bambi, but it was much harder to navigate '
             "and more it was c it was very high. It wasn't what we wanted to to experience "
             'with the the cost.',
      'title': 'Private Pay NEMT (Non Emergency Medical Transport) Across Florida | NEMT '
               'Experts Podcast Episode 39 (Bambi)',
      'url': 'https://www.youtube.com/watch?v=ICI0C5f_vjE&t=92s',
      'video_id': 'ICI0C5f_vjE'},
     {'author': 'Sarah Davis | The D&G Way',
      'channel': 'Sarah Davis | The D&G Way',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=hxoZsGym9DU&t=115s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "At level four, you're often creating the offer, negotiating the rate, or "
              'submitting the bid. Regardless of the level, your responsibility is the same. '
              'Know the revenue, understand your cost, evaluate profitability, and make '
              'informed business decisions.',
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': "At level four, you're often creating the offer, negotiating the rate, or "
             'submitting the bid. Regardless of the level, your responsibility is the same. '
             'Know the revenue, understand your cost, evaluate profitability, and make '
             'informed business decisions.',
      'title': 'How to Know If a Medical Courier Job or Courier Contract Is Actually '
               'Profitable (Sarah Davis | The D&G Way)',
      'url': 'https://www.youtube.com/watch?v=hxoZsGym9DU&t=115s',
      'video_id': 'hxoZsGym9DU'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:21](https://www.youtube.com/watch?v=wrfiCapUB9s&t=621s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'As an emt operator the knowledge of their price factors paired with the right '
              'in emt billing software can help you convert these perceived cash hogs into '
              'cash cows contact isi technology today for the best non-emergency medical '
              'transportation software.',
      'timestamp': 621,
      'timestamp_label': '[00:10:21]',
      'timestamp_seconds': 621,
      'tip': 'As an emt operator the knowledge of their price factors paired with the right in '
             'emt billing software can help you convert these perceived cash hogs into cash '
             'cows contact isi technology today for the best non-emergency medical '
             'transportation software.',
      'title': 'Setting Non-Emergency Medical Transportation (NEMT) Trip Prices - One-Way '
               'Billing | RouteGenie (RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=wrfiCapUB9s&t=621s',
      'video_id': 'wrfiCapUB9s'},
     {'author': 'MJ Business Academy',
      'channel': 'MJ Business Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:08](https://www.youtube.com/watch?v=ohTDpW0zUS8&t=248s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I would have stopped her and I would have gave her our brochure business card '
              'but look coach Transportation coach transp I recall seeing them before it looks '
              'like I think they added on more vehicles I never heard of them before it looks '
              'new.',
      'timestamp': 248,
      'timestamp_label': '[00:04:08]',
      'timestamp_seconds': 248,
      'tip': 'I would have stopped her and I would have gave her our brochure business card '
             'but look coach Transportation coach transp I recall seeing them before it looks '
             'like I think they added on more vehicles I never heard of them before it looks '
             'new.',
      'title': 'Ride Along with Us: Join Us for a Wheelchair Ride as NEMT Business Owners (MJ '
               'Business Academy)',
      'url': 'https://www.youtube.com/watch?v=ohTDpW0zUS8&t=248s',
      'video_id': 'ohTDpW0zUS8'},
     {'author': 'Moore Business & Tax Solutions LLC',
      'channel': 'Moore Business & Tax Solutions LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=mdF3PItHYxc&t=115s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I wanted you guys to see like we're opening together. Let me get through this "
              'video. We have a hat and we have our shirts. We do have our branded shirts, '
              'okay? So, in the bag, this is like a little book bag here.',
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': "I wanted you guys to see like we're opening together. Let me get through this "
             'video. We have a hat and we have our shirts. We do have our branded shirts, '
             'okay? So, in the bag, this is like a little book bag here.',
      'title': 'Medical Courier Beginners: Essential Supplies You Need! 📦🚗 (Some Companies '
               'Provide Them!) (Moore Business & Tax Solutions LLC)',
      'url': 'https://www.youtube.com/watch?v=mdF3PItHYxc&t=115s',
      'video_id': 'mdF3PItHYxc'},
     {'author': 'MJ Business Academy',
      'channel': 'MJ Business Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:30](https://www.youtube.com/watch?v=P_pN6quM3G4&t=810s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Vehicles like the promas city probably not um and so we just wanted to give you '
              'a heads up yeah make sure you do your research okay all right till next.',
      'timestamp': 810,
      'timestamp_label': '[00:13:30]',
      'timestamp_seconds': 810,
      'tip': 'Vehicles like the promas city probably not um and so we just wanted to give you '
             'a heads up yeah make sure you do your research okay all right till next.',
      'title': 'Smaller Vans May Not Work for NEMT (MJ Business Academy)',
      'url': 'https://www.youtube.com/watch?v=P_pN6quM3G4&t=810s',
      'video_id': 'P_pN6quM3G4'},
     {'author': 'Shantasia_RN',
      'channel': 'Shantasia_RN',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:05](https://www.youtube.com/watch?v=hS8ke40DMr4&t=425s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Track revenue and cost by vehicle when possible. Watch driver hours, fuel, '
              'empty mileage, cancellations. If you do not understand why one vehicle is '
              'profitable, adding another vehicle may multiply the problem instead of the '
              'profit.',
      'timestamp': 425,
      'timestamp_label': '[00:07:05]',
      'timestamp_seconds': 425,
      'tip': 'Track revenue and cost by vehicle when possible. Watch driver hours, fuel, empty '
             'mileage, cancellations. If you do not understand why one vehicle is profitable, '
             'adding another vehicle may multiply the problem instead of the profit.',
      'title': 'How to Start an NEMT Business: 8 Steps to Start Right (Shantasia_RN)',
      'url': 'https://www.youtube.com/watch?v=hS8ke40DMr4&t=425s',
      'video_id': 'hS8ke40DMr4'}],
 4: [{'author': 'Diamond Hunter Enterprises',
      'channel': 'Diamond Hunter Enterprises',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:30](https://www.youtube.com/watch?v=jyu_AIm5pAw&t=510s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "US driver's license with at least 3 years driving experience, clean driving "
              'record, own your own vehicle with valid insurance meeting or exceeding SDS '
              'minimums with an LLC S corp or C corp, pass a criminal background '
              'investigation.',
      'timestamp': 510,
      'timestamp_label': '[00:08:30]',
      'timestamp_seconds': 510,
      'tip': "US driver's license with at least 3 years driving experience, clean driving "
             'record, own your own vehicle with valid insurance meeting or exceeding SDS '
             'minimums with an LLC S corp or C corp, pass a criminal background investigation.',
      'title': 'Find FIRST Courier Contract Jobs in Your Car 2026 | 3 Medical Courier & Driver '
               'Certifications (Diamond Hunter Enterprises)',
      'url': 'https://www.youtube.com/watch?v=jyu_AIm5pAw&t=510s',
      'video_id': 'jyu_AIm5pAw'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:40](https://www.youtube.com/watch?v=3VPGH67xGp8&t=280s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Since then, even the most progressive NEMT dispatch and billing software would '
              'be able to handle your workflow. Hence, you might end up breaking those '
              'agreements, which is never a great business move. What type of legal agreement '
              'to choose?',
      'timestamp': 280,
      'timestamp_label': '[00:04:40]',
      'timestamp_seconds': 280,
      'tip': 'Since then, even the most progressive NEMT dispatch and billing software would '
             'be able to handle your workflow. Hence, you might end up breaking those '
             'agreements, which is never a great business move. What type of legal agreement '
             'to choose?',
      'title': 'How to Get Non-Emergency Medical Transportation (NEMT) Contracts? | RouteGenie '
               '(RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=3VPGH67xGp8&t=280s',
      'video_id': '3VPGH67xGp8'},
     {'author': 'Geoff Cole',
      'channel': 'Geoff Cole',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:53](https://www.youtube.com/watch?v=dLgmDQavyEU&t=113s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '8 billion and is projected to reach between 15 billion and 19. This is a '
              'growing government backed industry with real recurring money in it. Step one, '
              'form your LLC and get your EIN. Before you touch a van, you need a legal '
              'business entity.',
      'timestamp': 113,
      'timestamp_label': '[00:01:53]',
      'timestamp_seconds': 113,
      'tip': '8 billion and is projected to reach between 15 billion and 19. This is a growing '
             'government backed industry with real recurring money in it. Step one, form your '
             'LLC and get your EIN. Before you touch a van, you need a legal business entity.',
      'title': 'Starting NEMT in 2026 | Licensing, Insurance & Contract Reality (Geoff Cole)',
      'url': 'https://www.youtube.com/watch?v=dLgmDQavyEU&t=113s',
      'video_id': 'dLgmDQavyEU'},
     {'author': 'Miles & Money',
      'channel': 'Miles & Money',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:01](https://www.youtube.com/watch?v=Z7JVP9RYCwc&t=181s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You already have an established business now. So, go ahead and get a business '
              'bank account cuz you want to be able to separate your money now that you have a '
              "business entity. So, we're going to go ahead and get a business account and our "
              'business name.',
      'timestamp': 181,
      'timestamp_label': '[00:03:01]',
      'timestamp_seconds': 181,
      'tip': 'You already have an established business now. So, go ahead and get a business '
             'bank account cuz you want to be able to separate your money now that you have a '
             "business entity. So, we're going to go ahead and get a business account and our "
             'business name.',
      'title': 'EXACTLY How to start a Medical Courier Business in  2026. 3 Easy steps! (Miles '
               '& Money)',
      'url': 'https://www.youtube.com/watch?v=Z7JVP9RYCwc&t=181s',
      'video_id': 'Z7JVP9RYCwc'},
     {'author': 'Alton Arell',
      'channel': 'Alton Arell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=9fB-wPdETAk&t=71s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, to answer your question, yes, you can do this in your personal name. No, '
              "you don't have to have an LLC or some sort of business entity. You're going to "
              "hear me say LLC a lot. Obviously, that's not the only business entity.",
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': 'So, to answer your question, yes, you can do this in your personal name. No, you '
             "don't have to have an LLC or some sort of business entity. You're going to hear "
             "me say LLC a lot. Obviously, that's not the only business entity.",
      'title': 'The #1 Thing Medical Couriers Need to Know About LLCs (Alton Arell)',
      'url': 'https://www.youtube.com/watch?v=9fB-wPdETAk&t=71s',
      'video_id': '9fB-wPdETAk'},
     {'author': 'Giganomic Era',
      'channel': 'Giganomic Era',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=lkdaLTtSbok&t=38s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The first is purchasing the vehicle directly through the business. The LLC '
              'becomes the buyer, the vehicle get titled under the LLC name, and the '
              'registration is issued to the LLC. Their insurance also is written based on how '
              'the vehicle will be used.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': 'The first is purchasing the vehicle directly through the business. The LLC '
             'becomes the buyer, the vehicle get titled under the LLC name, and the '
             'registration is issued to the LLC. Their insurance also is written based on how '
             'the vehicle will be used.',
      'title': '"The Vehicle Registration Decision Every New Courier Needs to Make (Medical '
               'Courier)" (Giganomic Era)',
      'url': 'https://www.youtube.com/watch?v=lkdaLTtSbok&t=38s',
      'video_id': 'lkdaLTtSbok'},
     {'author': 'WM NEMT Startup Coach',
      'channel': 'WM NEMT Startup Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:07](https://www.youtube.com/watch?v=TmcbGA0zH6Y&t=967s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'People what I call getting set up backwards where they go out and they purchase '
              "a vehicle they get the insurance and it's commercial but they.",
      'timestamp': 967,
      'timestamp_label': '[00:16:07]',
      'timestamp_seconds': 967,
      'tip': 'People what I call getting set up backwards where they go out and they purchase '
             "a vehicle they get the insurance and it's commercial but they.",
      'title': "Don't Let These 7 NEMT Mistakes BANKRUPT Your Business (WM NEMT Startup Coach)",
      'url': 'https://www.youtube.com/watch?v=TmcbGA0zH6Y&t=967s',
      'video_id': 'TmcbGA0zH6Y'},
     {'author': 'The Travae Willis Transportation Channel',
      'channel': 'The Travae Willis Transportation Channel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:03](https://www.youtube.com/watch?v=YFWOnVDBziM&t=423s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'t have any equipment, don't have any vans, these brokers that don't have any "
              'vans. You carry the insurance, the breakdowns, the fuel and the drivers. I '
              'never understood why in this world that we would be getting uh paid kind of '
              'like musicians.',
      'timestamp': 423,
      'timestamp_label': '[00:07:03]',
      'timestamp_seconds': 423,
      'tip': "'t have any equipment, don't have any vans, these brokers that don't have any "
             'vans. You carry the insurance, the breakdowns, the fuel and the drivers. I never '
             'understood why in this world that we would be getting uh paid kind of like '
             'musicians.',
      'title': 'VA hospital Contracts (The Travae Willis Transportation Channel)',
      'url': 'https://www.youtube.com/watch?v=YFWOnVDBziM&t=423s',
      'video_id': 'YFWOnVDBziM'},
     {'author': 'United Medical Transportation Providers Group',
      'channel': 'United Medical Transportation Providers Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:24](https://www.youtube.com/watch?v=xx3dHh731rY&t=684s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Shucks johnny here's how you do it just apply with the broker oh ralph come on "
              'just go get some insurance on your car.',
      'timestamp': 684,
      'timestamp_label': '[00:11:24]',
      'timestamp_seconds': 684,
      'tip': "Shucks johnny here's how you do it just apply with the broker oh ralph come on "
             'just go get some insurance on your car.',
      'title': 'Medicaid Brokers - the Benefits and Possibilities of Working Out of Network '
               'and Not Being Dependent! (United Medical Transportation Providers Group)',
      'url': 'https://www.youtube.com/watch?v=xx3dHh731rY&t=684s',
      'video_id': 'xx3dHh731rY'},
     {'author': 'LearnCargo',
      'channel': 'LearnCargo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=TkA2pcOAGoQ&t=103s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And just as a next tip, you still starting this business because some companies '
              "do provide the vehicle for you to drive. So, then you also don't have to worry "
              'about extra insurance or extra expenses or putting wear and tear on your car.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': 'And just as a next tip, you still starting this business because some companies '
             "do provide the vehicle for you to drive. So, then you also don't have to worry "
             'about extra insurance or extra expenses or putting wear and tear on your car.',
      'title': 'How to Become a Medical Courier in 2027 (LearnCargo)',
      'url': 'https://www.youtube.com/watch?v=TkA2pcOAGoQ&t=103s',
      'video_id': 'TkA2pcOAGoQ'},
     {'author': 'HIPAA Certify',
      'channel': 'HIPAA Certify',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:14](https://www.youtube.com/watch?v=evVpVMr62o0&t=74s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Especially if an insurance company is might ask you, do you have a HIPAA '
              'certificate, and just knowing the basics just makes you way more confident when '
              'it comes to handling patient information.',
      'timestamp': 74,
      'timestamp_label': '[00:01:14]',
      'timestamp_seconds': 74,
      'tip': 'Especially if an insurance company is might ask you, do you have a HIPAA '
             'certificate, and just knowing the basics just makes you way more confident when '
             'it comes to handling patient information.',
      'title': 'Do Medical Couriers Need HIPAA Training  Find Out! 📦 (HIPAA Certify)',
      'url': 'https://www.youtube.com/watch?v=evVpVMr62o0&t=74s',
      'video_id': 'evVpVMr62o0'},
     {'author': 'Nemt University',
      'channel': 'Nemt University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:36](https://www.youtube.com/watch?v=FB8bZXWmo1k&t=396s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Goes here your NPI number goes here said 10 numbers so number there you go get '
              'number for your business entity it will go there Corporation your corporation '
              "information goes here we're not filling out any information pertaining to a "
              'individual if you all.',
      'timestamp': 396,
      'timestamp_label': '[00:06:36]',
      'timestamp_seconds': 396,
      'tip': 'Goes here your NPI number goes here said 10 numbers so number there you go get '
             'number for your business entity it will go there Corporation your corporation '
             "information goes here we're not filling out any information pertaining to a "
             'individual if you all.',
      'title': 'NEMT PROVIDER ENROLLMENT APPLICATION #nemt #medicaid (Nemt University)',
      'url': 'https://www.youtube.com/watch?v=FB8bZXWmo1k&t=396s',
      'video_id': 'FB8bZXWmo1k'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:37](https://www.youtube.com/watch?v=wHWl2rSRGV0&t=217s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Customers now demand better services and you may have a tight budget. So, you '
              'should see what transportation software and technology can do for for business. '
              'Reporting no-shows in your software maintains efficiency as you can track the '
              'reasons behind missed appointments.',
      'timestamp': 217,
      'timestamp_label': '[00:03:37]',
      'timestamp_seconds': 217,
      'tip': 'Customers now demand better services and you may have a tight budget. So, you '
             'should see what transportation software and technology can do for for business. '
             'Reporting no-shows in your software maintains efficiency as you can track the '
             'reasons behind missed appointments.',
      'title': 'What Happens if a Passenger is a No Show in NEMT | RouteGenie (RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=wHWl2rSRGV0&t=217s',
      'video_id': 'wHWl2rSRGV0'},
     {'author': 'United Medical Transportation Providers Group',
      'channel': 'United Medical Transportation Providers Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:33](https://www.youtube.com/watch?v=FKvCovIVs3Q&t=393s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Whose services are paid for by various payers including Medicaid other '
              'third-party payers I.E like private insurance or something like that or the '
              'resident paying.',
      'timestamp': 393,
      'timestamp_label': '[00:06:33]',
      'timestamp_seconds': 393,
      'tip': 'Whose services are paid for by various payers including Medicaid other '
             'third-party payers I.E like private insurance or something like that or the '
             'resident paying.',
      'title': 'Contracts: Facilities paying NEMT providers DIRECTLY despite having Medicaid '
               'and Medicare residents. (United Medical Transportation Providers Group)',
      'url': 'https://www.youtube.com/watch?v=FKvCovIVs3Q&t=393s',
      'video_id': 'FKvCovIVs3Q'},
     {'author': 'My Business Vibe 9',
      'channel': 'My Business Vibe 9',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:07](https://www.youtube.com/watch?v=mm9doNupm1k&t=187s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Also, you want to get proper insurance. You want to make sure you have '
              'commercial auto insurance and cargo insurance. You can use sites like simply '
              'business. Also, these companies will tell you what type of coverage they '
              'require for your vehicle as well.',
      'timestamp': 187,
      'timestamp_label': '[00:03:07]',
      'timestamp_seconds': 187,
      'tip': 'Also, you want to get proper insurance. You want to make sure you have '
             'commercial auto insurance and cargo insurance. You can use sites like simply '
             'business. Also, these companies will tell you what type of coverage they require '
             'for your vehicle as well.',
      'title': 'Easy Steps To Land Your First Medical Courier Contract (My Business Vibe 9)',
      'url': 'https://www.youtube.com/watch?v=mm9doNupm1k&t=187s',
      'video_id': 'mm9doNupm1k'}],
 5: [{'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=pVsERYNlif4&t=57s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Understanding these regulations isn't just about avoiding penalties. It's about "
              'building credibility and trust within the health care system while protecting '
              'your business from costly mistakes. The five essential compliance areas.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': "Understanding these regulations isn't just about avoiding penalties. It's about "
             'building credibility and trust within the health care system while protecting '
             'your business from costly mistakes. The five essential compliance areas.',
      'title': 'The NEMT Compliance Checklist: 5 Legal Essentials for Medical Transportation '
               'Providers (RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=pVsERYNlif4&t=57s',
      'video_id': 'pVsERYNlif4'},
     {'author': 'Shantasia_RN',
      'channel': 'Shantasia_RN',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:16](https://www.youtube.com/watch?v=fWyD2LyLaKE&t=376s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Growth will expose weak processes. Building systems early can prevent small '
              'issues from becoming expensive problems. My sixth mistake was seeing money into '
              'the business account and assuming that all of it was available. In reality, '
              'most of that money already had a job.',
      'timestamp': 376,
      'timestamp_label': '[00:06:16]',
      'timestamp_seconds': 376,
      'tip': 'Growth will expose weak processes. Building systems early can prevent small '
             'issues from becoming expensive problems. My sixth mistake was seeing money into '
             'the business account and assuming that all of it was available. In reality, most '
             'of that money already had a job.',
      'title': '6 Costly NEMT Business Mistakes I Made and What I Learned (Shantasia_RN)',
      'url': 'https://www.youtube.com/watch?v=fWyD2LyLaKE&t=376s',
      'video_id': 'fWyD2LyLaKE'},
     {'author': 'Medical Courier Connection',
      'channel': 'Medical Courier Connection',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=0eV-OzFHmX8&t=20s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "We'll drive the heavy lifting that keeps your business innovative with the "
              'latest technology so that you can focus on building connections with your '
              'customers. This podcast is also brought to you by Risk Strategies.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "We'll drive the heavy lifting that keeps your business innovative with the "
             'latest technology so that you can focus on building connections with your '
             'customers. This podcast is also brought to you by Risk Strategies.',
      'title': 'Medical Courier Insurance Re-Visited w/ Brian Jungeberg - The MCC #podcast '
               '#medicalcourier #courier (Medical Courier Connection)',
      'url': 'https://www.youtube.com/watch?v=0eV-OzFHmX8&t=20s',
      'video_id': '0eV-OzFHmX8'},
     {'author': 'Shawn in Town',
      'channel': 'Shawn in Town',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:14](https://www.youtube.com/watch?v=LqGuhE6C6_g&t=314s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'These are the mistakes that these people make, and then they come back and '
              "blame the business and said the business ain't working. It's a great business "
              'to be in. The problem is people want to take shortcuts.',
      'timestamp': 314,
      'timestamp_label': '[00:05:14]',
      'timestamp_seconds': 314,
      'tip': 'These are the mistakes that these people make, and then they come back and blame '
             "the business and said the business ain't working. It's a great business to be "
             'in. The problem is people want to take shortcuts.',
      'title': "I QUIT Medical Courier The FIRST DAY!!! - Here's Why (Shawn in Town)",
      'url': 'https://www.youtube.com/watch?v=LqGuhE6C6_g&t=314s',
      'video_id': 'LqGuhE6C6_g'},
     {'author': 'STICK WITH US DELIVERY 🚚 📦',
      'channel': 'STICK WITH US DELIVERY 🚚 📦',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=cWa2fFpFFFU&t=90s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um HIPAA and bloodborne pathogens certification, learning about spill kits and '
              'all of that. That is extremely important when you starting this business. Um I '
              'will leave in the description um where you can get that training from and get '
              'your certificates.',
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': 'Um HIPAA and bloodborne pathogens certification, learning about spill kits and '
             'all of that. That is extremely important when you starting this business. Um I '
             'will leave in the description um where you can get that training from and get '
             'your certificates.',
      'title': '🚐 Want to Start a Medical Courier or Cargo Van Business? (STICK WITH US '
               'DELIVERY 🚚 📦)',
      'url': 'https://www.youtube.com/watch?v=cWa2fFpFFFU&t=90s',
      'video_id': 'cWa2fFpFFFU'},
     {'author': 'MediRoutes NEMT Software',
      'channel': 'MediRoutes NEMT Software',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:46](https://www.youtube.com/watch?v=g6k_yncRR8o&t=466s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Medicaid broker business, right? So there's different, um, there's different "
              'states. Some states require you to be, um, Medi-Cal approved, like California. '
              'So you have to more or less wait five to seven months before you get approved.',
      'timestamp': 466,
      'timestamp_label': '[00:07:46]',
      'timestamp_seconds': 466,
      'tip': "Medicaid broker business, right? So there's different, um, there's different "
             'states. Some states require you to be, um, Medi-Cal approved, like California. '
             'So you have to more or less wait five to seven months before you get approved.',
      'title': 'How to Start an NEMT Business and Win First Contracts with Joe Padilla '
               '(MediRoutes NEMT Software)',
      'url': 'https://www.youtube.com/watch?v=g6k_yncRR8o&t=466s',
      'video_id': 'g6k_yncRR8o'},
     {'author': 'Markie Williams Online Certification Courses',
      'channel': 'Markie Williams Online Certification Courses',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:57](https://www.youtube.com/watch?v=WizhPVJ0zVE&t=177s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Certification course will explain the risk involved when working with blood '
              'summarize how to establish a core sense of responsibility among participants to '
              'prevent exposure to bbps outline how to clean up blood and blood containing '
              'fluids.',
      'timestamp': 177,
      'timestamp_label': '[00:02:57]',
      'timestamp_seconds': 177,
      'tip': 'Certification course will explain the risk involved when working with blood '
             'summarize how to establish a core sense of responsibility among participants to '
             'prevent exposure to bbps outline how to clean up blood and blood containing '
             'fluids.',
      'title': 'Must Have Medical Courier Certifications (Markie Williams Online Certification '
               'Courses)',
      'url': 'https://www.youtube.com/watch?v=WizhPVJ0zVE&t=177s',
      'video_id': 'WizhPVJ0zVE'},
     {'author': 'MJ Business Academy',
      'channel': 'MJ Business Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:16](https://www.youtube.com/watch?v=OH1QaUPvJ8k&t=616s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I agree go watch that video um it'll help you avoid those mistakes for sure and "
              "if you are currently sitting on your NPI number you don't know what to do you "
              "don't know where to go we offer one-on-one consultation.",
      'timestamp': 616,
      'timestamp_label': '[00:10:16]',
      'timestamp_seconds': 616,
      'tip': "I agree go watch that video um it'll help you avoid those mistakes for sure and "
             "if you are currently sitting on your NPI number you don't know what to do you "
             "don't know where to go we offer one-on-one consultation.",
      'title': 'I have my NPI number—what should I do next? (MJ Business Academy)',
      'url': 'https://www.youtube.com/watch?v=OH1QaUPvJ8k&t=616s',
      'video_id': 'OH1QaUPvJ8k'},
     {'author': 'LearnCargo',
      'channel': 'LearnCargo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=A55v_6-hvG0&t=20s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'BPP, which stands for blood-borne pathogen. Number five is hazmat awareness. '
              "Number six is infection control training. And now we're moving into higher risk "
              'delivery. So, this is not for the faint of heart.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'BPP, which stands for blood-borne pathogen. Number five is hazmat awareness. '
             "Number six is infection control training. And now we're moving into higher risk "
             'delivery. So, this is not for the faint of heart.',
      'title': 'Medical Courier Certifications You Need in 2027 (LearnCargo)',
      'url': 'https://www.youtube.com/watch?v=A55v_6-hvG0&t=20s',
      'video_id': 'A55v_6-hvG0'},
     {'author': 'The Couvent Collective',
      'channel': 'The Couvent Collective',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:41](https://www.youtube.com/watch?v=tOXRoqW_-CM&t=221s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Be properly insured to make sure that this risk is removed from you personally '
              'and that whatever happens is covered under insurance and that you have the '
              'proper insurance if something should happen but do your research and make sure '
              'you fact check.',
      'timestamp': 221,
      'timestamp_label': '[00:03:41]',
      'timestamp_seconds': 221,
      'tip': 'Be properly insured to make sure that this risk is removed from you personally '
             'and that whatever happens is covered under insurance and that you have the '
             'proper insurance if something should happen but do your research and make sure '
             'you fact check.',
      'title': 'Do not run a medical courier business as a sole proprietorship! ￼ (The Couvent '
               'Collective)',
      'url': 'https://www.youtube.com/watch?v=tOXRoqW_-CM&t=221s',
      'video_id': 'tOXRoqW_-CM'},
     {'author': 'DriverCheck',
      'channel': 'DriverCheck',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=L6vVw1mPltU&t=50s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Longer history of drug use than oral fluid testing the longer time window of '
              'detection built into the process identifies risk and may therefore be preferred '
              'for risk-based programs the downside.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': 'Longer history of drug use than oral fluid testing the longer time window of '
             'detection built into the process identifies risk and may therefore be preferred '
             'for risk-based programs the downside.',
      'title': 'DriverCheck Drug Testing Sample Types Tutorial (DriverCheck)',
      'url': 'https://www.youtube.com/watch?v=L6vVw1mPltU&t=50s',
      'video_id': 'L6vVw1mPltU'},
     {'author': 'Medical Courier Connection',
      'channel': 'Medical Courier Connection',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:04](https://www.youtube.com/watch?v=VPzA_AFvr8E&t=304s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, definitely a purpose-driven lifestyle as a medical courier. What are some '
              'of the challenges of working as a medical courier? I mean, you have to you have '
              'to be dependable. Mistakes on the job can affect patients care.',
      'timestamp': 304,
      'timestamp_label': '[00:05:04]',
      'timestamp_seconds': 304,
      'tip': 'So, definitely a purpose-driven lifestyle as a medical courier. What are some of '
             'the challenges of working as a medical courier? I mean, you have to you have to '
             'be dependable. Mistakes on the job can affect patients care.',
      'title': 'The Pros and Cons of Medical Courier Work #medicalcourier #prosandcons '
               '#courierlife #medicaldelivery (Medical Courier Connection)',
      'url': 'https://www.youtube.com/watch?v=VPzA_AFvr8E&t=304s',
      'video_id': 'VPzA_AFvr8E'},
     {'author': 'Wheelchair & Stretcher Transportation Services',
      'channel': 'Wheelchair & Stretcher Transportation Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:24](https://www.youtube.com/watch?v=zn8XUaFzOCk&t=264s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Let them know that you're there to solve their problem hopefully this was "
              'helpful again this is marcus with all american health we provide non-emergency '
              'medical transportation services consulting services and digital marketing look '
              'forward to hearing from you bye guys.',
      'timestamp': 264,
      'timestamp_label': '[00:04:24]',
      'timestamp_seconds': 264,
      'tip': "Let them know that you're there to solve their problem hopefully this was "
             'helpful again this is marcus with all american health we provide non-emergency '
             'medical transportation services consulting services and digital marketing look '
             'forward to hearing from you bye guys.',
      'title': 'NEMT Industry Private Pay Tips (Wheelchair & Stretcher Transportation '
               'Services)',
      'url': 'https://www.youtube.com/watch?v=zn8XUaFzOCk&t=264s',
      'video_id': 'zn8XUaFzOCk'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=nSOlMk5hmjU&t=54s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'PACE program as they get medical care in these facilities. However, more '
              'seniors than ever prefer to stay at home instead of in assisted living '
              'facilities.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'PACE program as they get medical care in these facilities. However, more seniors '
             'than ever prefer to stay at home instead of in assisted living facilities.',
      'title': 'PACE Transportation Services for Seniors | RouteGenie (RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=nSOlMk5hmjU&t=54s',
      'video_id': 'nSOlMk5hmjU'},
     {'author': 'PractiScale',
      'channel': 'PractiScale',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:10](https://www.youtube.com/watch?v=R0U1p8_k4J0&t=250s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Case managers refer providers they already spoke with. And that's why building "
              'referral partners is the most stable way to grow an NMT business.',
      'timestamp': 250,
      'timestamp_label': '[00:04:10]',
      'timestamp_seconds': 250,
      'tip': "Case managers refer providers they already spoke with. And that's why building "
             'referral partners is the most stable way to grow an NMT business.',
      'title': 'How NEMT Companies Get Direct Referrals (No Brokers Needed) (PractiScale)',
      'url': 'https://www.youtube.com/watch?v=R0U1p8_k4J0&t=250s',
      'video_id': 'R0U1p8_k4J0'}],
 6: [{'author': 'JT Automations',
      'channel': 'JT Automations',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:02](https://www.youtube.com/watch?v=dHKhNi-IC-0&t=542s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I'll use the top states that watch this video as kind of references. So, first, "
              "business LLC, then your EIN number, then you need a NPI, that's sometimes "
              'required for billing, by the way. You need Medicaid provider enrollment, and '
              'you need a driver background check.',
      'timestamp': 542,
      'timestamp_label': '[00:09:02]',
      'timestamp_seconds': 542,
      'tip': "I'll use the top states that watch this video as kind of references. So, first, "
             "business LLC, then your EIN number, then you need a NPI, that's sometimes "
             'required for billing, by the way. You need Medicaid provider enrollment, and you '
             'need a driver background check.',
      'title': 'How to Start a Non-Emergency Medical Transportation Company in 2026 (NEMT '
               'Business) (JT Automations)',
      'url': 'https://www.youtube.com/watch?v=dHKhNi-IC-0&t=542s',
      'video_id': 'dHKhNi-IC-0'},
     {'author': 'Leelah The Entrepreneur',
      'channel': 'Leelah The Entrepreneur',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:33](https://www.youtube.com/watch?v=UUrhf6VurIA&t=393s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s going to save you weeks of work. I put together the medical courier starter "
              'kit workbook for only $27. This is everything I wish I would have had on day '
              "one. Inside, you'll get a lead list of 2,000 plus medical courier leads all "
              'across 50 states.',
      'timestamp': 393,
      'timestamp_label': '[00:06:33]',
      'timestamp_seconds': 393,
      'tip': "'s going to save you weeks of work. I put together the medical courier starter "
             'kit workbook for only $27. This is everything I wish I would have had on day '
             "one. Inside, you'll get a lead list of 2,000 plus medical courier leads all "
             'across 50 states.',
      'title': 'How I Made $9,235 in 21 Days as a Medical Courier | How to Get Started (Leelah '
               'The Entrepreneur)',
      'url': 'https://www.youtube.com/watch?v=UUrhf6VurIA&t=393s',
      'video_id': 'UUrhf6VurIA'},
     {'author': 'Six Figure Transportation',
      'channel': 'Six Figure Transportation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:22](https://www.youtube.com/watch?v=zyo_6OZNupU&t=142s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Don't um deal with the broker at all insurance companies contracts and private "
              "pay so um I'll be doing a more in-depth video um talking about the Brokers the "
              "insurance and the um skilled nursing part a little bit later this is Eric I'll "
              'see you soon.',
      'timestamp': 142,
      'timestamp_label': '[00:02:22]',
      'timestamp_seconds': 142,
      'tip': "Don't um deal with the broker at all insurance companies contracts and private "
             "pay so um I'll be doing a more in-depth video um talking about the Brokers the "
             "insurance and the um skilled nursing part a little bit later this is Eric I'll "
             'see you soon.',
      'title': '4 ways to get paid with NEMT!!! (Six Figure Transportation)',
      'url': 'https://www.youtube.com/watch?v=zyo_6OZNupU&t=142s',
      'video_id': 'zyo_6OZNupU'},
     {'author': 'Veterans Health Administration',
      'channel': 'Veterans Health Administration',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:12](https://www.youtube.com/watch?v=nQ12WJ2mSwE&t=132s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Scroll down until you see the heading that reads What if I need help submitting '
              'my claim? Then follow that link to find the travel contact for your facility. '
              'For additional help, contact the Beneficiary Travel Self-Service System '
              'Toll-Free Call Center.',
      'timestamp': 132,
      'timestamp_label': '[00:02:12]',
      'timestamp_seconds': 132,
      'tip': 'Scroll down until you see the heading that reads What if I need help submitting '
             'my claim? Then follow that link to find the travel contact for your facility. '
             'For additional help, contact the Beneficiary Travel Self-Service System '
             'Toll-Free Call Center.',
      'title': 'VA Travel Pay Reimbursement (Veterans Health Administration)',
      'url': 'https://www.youtube.com/watch?v=nQ12WJ2mSwE&t=132s',
      'video_id': 'nQ12WJ2mSwE'},
     {'author': 'Nemt University',
      'channel': 'Nemt University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:09](https://www.youtube.com/watch?v=zXw7440bths&t=549s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '3 years, FBI fingerprint, you have to have your HIPAA, you have to have defen- '
              'defensive driver training, ADA, bloodborne pathogen, CPR, and first aid. They '
              "ver- they verify between 7:00 a. Monday through Friday only. And that's their "
              'call center hours.',
      'timestamp': 549,
      'timestamp_label': '[00:09:09]',
      'timestamp_seconds': 549,
      'tip': '3 years, FBI fingerprint, you have to have your HIPAA, you have to have defen- '
             'defensive driver training, ADA, bloodborne pathogen, CPR, and first aid. They '
             "ver- they verify between 7:00 a. Monday through Friday only. And that's their "
             'call center hours.',
      'title': '🚨GEORGIA HANDS ONE COMPANY 2.1 MILLION MEDICAID RIDES🚗 (Nemt University)',
      'url': 'https://www.youtube.com/watch?v=zXw7440bths&t=549s',
      'video_id': 'zXw7440bths'},
     {'author': 'Giganomic Era',
      'channel': 'Giganomic Era',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:29](https://www.youtube.com/watch?v=FzfSZhrc8rM&t=509s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I need a commercial auto policy? It varies from state to state. All right, so '
              'now we list that five companies, MedZoomer, Dropoff, Roadie, Dispatch, and '
              "Curry. I know some of y'all are probably wondering which one would I apply to "
              'first.',
      'timestamp': 509,
      'timestamp_label': '[00:08:29]',
      'timestamp_seconds': 509,
      'tip': 'I need a commercial auto policy? It varies from state to state. All right, so '
             'now we list that five companies, MedZoomer, Dropoff, Roadie, Dispatch, and '
             "Curry. I know some of y'all are probably wondering which one would I apply to "
             'first.',
      'title': '5 Medical Courier Apps to Try in 2026 9 (Before You Apply Anywhere Else)! '
               '(Giganomic Era)',
      'url': 'https://www.youtube.com/watch?v=FzfSZhrc8rM&t=509s',
      'video_id': 'FzfSZhrc8rM'},
     {'author': 'Bambi',
      'channel': 'Bambi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=dxaejS8Bpis&t=80s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I can select which order that I want for pickup and drop off. So, let's say I "
              'wanted yellow stork to be picked up first and then Gerald and then we need '
              "Gerald to be dropped off and then yellow stork. So, this is how it'll appear in "
              'your driver app.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': "I can select which order that I want for pickup and drop off. So, let's say I "
             'wanted yellow stork to be picked up first and then Gerald and then we need '
             "Gerald to be dropped off and then yellow stork. So, this is how it'll appear in "
             'your driver app.',
      'title': 'How to Manually Create Multi Loads|| Bambi NEMT Knowledge Base (Bambi)',
      'url': 'https://www.youtube.com/watch?v=dxaejS8Bpis&t=80s',
      'video_id': 'dxaejS8Bpis'},
     {'author': 'Trucking Comply',
      'channel': 'Trucking Comply',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:07](https://www.youtube.com/watch?v=9mw1R5jfp5o&t=247s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '8 hours after the crash, or until the test, whichever comes first. The driver '
              'must stay available for the test, or may be treated as refusing it. But medical '
              'care for anyone hurt always comes first, and the driver may leave the scene to '
              'get help.',
      'timestamp': 247,
      'timestamp_label': '[00:04:07]',
      'timestamp_seconds': 247,
      'tip': '8 hours after the crash, or until the test, whichever comes first. The driver '
             'must stay available for the test, or may be treated as refusing it. But medical '
             'care for anyone hurt always comes first, and the driver may leave the scene to '
             'get help.',
      'title': 'When Is a DOT Drug Test Required? Post-Accident, Random, Reasonable Suspicion '
               'and More (Trucking Comply)',
      'url': 'https://www.youtube.com/watch?v=9mw1R5jfp5o&t=247s',
      'video_id': '9mw1R5jfp5o'},
     {'author': 'Dean Medical Courier Academy',
      'channel': 'Dean Medical Courier Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:06](https://www.youtube.com/watch?v=dhyibOQPAlA&t=186s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '" So, you go back to searching. You check CB Driver, you check Indeed, you '
              'search on Google, or maybe you download another courier list. I want you to '
              'think about something. Where is everyone else looking for contracts?',
      'timestamp': 186,
      'timestamp_label': '[00:03:06]',
      'timestamp_seconds': 186,
      'tip': '" So, you go back to searching. You check CB Driver, you check Indeed, you '
             'search on Google, or maybe you download another courier list. I want you to '
             'think about something. Where is everyone else looking for contracts?',
      'title': 'A Real $550 Medical Courier Week — Watch It and Decide If It’s Worth It to You '
               '(Dean Medical Courier Academy)',
      'url': 'https://www.youtube.com/watch?v=dhyibOQPAlA&t=186s',
      'video_id': 'dhyibOQPAlA'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:21](https://www.youtube.com/watch?v=Lh999r_-mi0&t=201s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Choosing the right vehicle that balances these factors significantly increases '
              'your chances of securing contracts with private customers and Medicaid brokers. '
              'First, passenger vehicles for ambulatory or outpatient transportation.',
      'timestamp': 201,
      'timestamp_label': '[00:03:21]',
      'timestamp_seconds': 201,
      'tip': 'Choosing the right vehicle that balances these factors significantly increases '
             'your chances of securing contracts with private customers and Medicaid brokers. '
             'First, passenger vehicles for ambulatory or outpatient transportation.',
      'title': 'How to Choose an NEMT Vehicle: Compliance, Costs, and Fleet Strategy '
               '(RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=Lh999r_-mi0&t=201s',
      'video_id': 'Lh999r_-mi0'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:04](https://www.youtube.com/watch?v=VSyBnPDVpR8&t=304s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Here are some ways NAMT companies can deal with improper billing. Unannounced '
              'internal audits, medical records reviews, passenger claims monitoring, data '
              'analysis, prepayment edits, monitoring Medicaid eligibility.',
      'timestamp': 304,
      'timestamp_label': '[00:05:04]',
      'timestamp_seconds': 304,
      'tip': 'Here are some ways NAMT companies can deal with improper billing. Unannounced '
             'internal audits, medical records reviews, passenger claims monitoring, data '
             'analysis, prepayment edits, monitoring Medicaid eligibility.',
      'title': 'How To Overcome Fraud in NEMT Services | RouteGenie (RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=VSyBnPDVpR8&t=304s',
      'video_id': 'VSyBnPDVpR8'},
     {'author': 'LearnCargo',
      'channel': 'LearnCargo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:35](https://www.youtube.com/watch?v=T4M_BMvKM10&t=95s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And I'll do a separate video on that so that you can find more information on "
              'that. And the last two are for medical flights, and that includes a medical jet '
              'and a medical helicopter. Of course, more advanced because you do need '
              'different types of certifications.',
      'timestamp': 95,
      'timestamp_label': '[00:01:35]',
      'timestamp_seconds': 95,
      'tip': "And I'll do a separate video on that so that you can find more information on "
             'that. And the last two are for medical flights, and that includes a medical jet '
             'and a medical helicopter. Of course, more advanced because you do need different '
             'types of certifications.',
      'title': 'NEMT Vehicles: 7 Types of Non-Emergency Medical Transportation Vehicles '
               '(LearnCargo)',
      'url': 'https://www.youtube.com/watch?v=T4M_BMvKM10&t=95s',
      'video_id': 'T4M_BMvKM10'},
     {'author': 'Zenpath Radio',
      'channel': 'Zenpath Radio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:36](https://www.youtube.com/watch?v=VOkoxr2bB2Q&t=1296s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Have that listed like we get calls I we just picked up somebody a couple of '
              "weeks ago that's in South Carolina but his appoint here in Charlotte he was in "
              'a car accident or something and he had to come.',
      'timestamp': 1296,
      'timestamp_label': '[00:21:36]',
      'timestamp_seconds': 1296,
      'tip': 'Have that listed like we get calls I we just picked up somebody a couple of '
             "weeks ago that's in South Carolina but his appoint here in Charlotte he was in a "
             'car accident or something and he had to come.',
      'title': 'How to Increase Private Pay Contracts for NEMT Providers (Zenpath Radio)',
      'url': 'https://www.youtube.com/watch?v=VOkoxr2bB2Q&t=1296s',
      'video_id': 'VOkoxr2bB2Q'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=9j6I5bSKP24&t=117s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The answer can vary between different companies. But if you have NEMT dispatch '
              'and billing software to keep track of pricing and when deadhead miles apply, it '
              'will be much easier. You first have to set a radius around the central location '
              'where your services are provided.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': 'The answer can vary between different companies. But if you have NEMT dispatch '
             'and billing software to keep track of pricing and when deadhead miles apply, it '
             'will be much easier. You first have to set a radius around the central location '
             'where your services are provided.',
      'title': 'Ways to Charge for NEMT Deadhead Miles | RouteGenie (RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=9j6I5bSKP24&t=117s',
      'video_id': '9j6I5bSKP24'},
     {'author': 'ThatNEMTGirl',
      'channel': 'ThatNEMTGirl',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:55](https://www.youtube.com/watch?v=govQRXzu6Rg&t=235s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You also may have to expand the hours of operation for your business. If you're "
              'operating from 8 to 5 or 9 to5, you may want to think about looking at the '
              'times that your your uh client sales or your broker are requesting you for '
              'trips.',
      'timestamp': 235,
      'timestamp_label': '[00:03:55]',
      'timestamp_seconds': 235,
      'tip': "You also may have to expand the hours of operation for your business. If you're "
             'operating from 8 to 5 or 9 to5, you may want to think about looking at the times '
             'that your your uh client sales or your broker are requesting you for trips.',
      'title': 'How I Made $100K with ONE Van + ONE Broker | NEMT Business Strategy (2024) '
               '(ThatNEMTGirl)',
      'url': 'https://www.youtube.com/watch?v=govQRXzu6Rg&t=235s',
      'video_id': 'govQRXzu6Rg'}],
 7: [{'author': 'Nemiton',
      'channel': 'Nemiton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:38](https://www.youtube.com/watch?v=w246jND2Ahw&t=578s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, document your growth timelines showing vehicle additions and driver hires. '
              'Brokers contract with providers demonstrating scalability. Step number eight, '
              'hire drivers who build your reputation. Driver quality determines your entire '
              'business reputation.',
      'timestamp': 578,
      'timestamp_label': '[00:09:38]',
      'timestamp_seconds': 578,
      'tip': 'So, document your growth timelines showing vehicle additions and driver hires. '
             'Brokers contract with providers demonstrating scalability. Step number eight, '
             'hire drivers who build your reputation. Driver quality determines your entire '
             'business reputation.',
      'title': '15 Steps to Start a NEMT Business (Complete 2026 Walkthrough) (Nemiton)',
      'url': 'https://www.youtube.com/watch?v=w246jND2Ahw&t=578s',
      'video_id': 'w246jND2Ahw'},
     {'author': 'PractiScale',
      'channel': 'PractiScale',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:51](https://www.youtube.com/watch?v=R0U1p8_k4J0&t=171s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And the problem is what usually happens is the strips stay inconsistent. So '
              'some weeks empty you have vehicles, you have drivers but no steady flow of '
              'rides. And that is exactly what we fix. We use a very simple system. We call it '
              'a three-step NMT referral partner system.',
      'timestamp': 171,
      'timestamp_label': '[00:02:51]',
      'timestamp_seconds': 171,
      'tip': 'And the problem is what usually happens is the strips stay inconsistent. So some '
             'weeks empty you have vehicles, you have drivers but no steady flow of rides. And '
             'that is exactly what we fix. We use a very simple system. We call it a '
             'three-step NMT referral partner system.',
      'title': 'How NEMT Companies Get Direct Referrals (No Brokers Needed) (PractiScale)',
      'url': 'https://www.youtube.com/watch?v=R0U1p8_k4J0&t=171s',
      'video_id': 'R0U1p8_k4J0'},
     {'author': 'Giganomic Era',
      'channel': 'Giganomic Era',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:03](https://www.youtube.com/watch?v=7Mz5ctFZBX0&t=303s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Use your lunch break for a short introductory call. The goal of the first call '
              "is not to deliver a long sales pitch. It's to identify the right person, "
              'understand their current delivery system, and schedule a better time to '
              'continue the conversation.',
      'timestamp': 303,
      'timestamp_label': '[00:05:03]',
      'timestamp_seconds': 303,
      'tip': 'Use your lunch break for a short introductory call. The goal of the first call '
             "is not to deliver a long sales pitch. It's to identify the right person, "
             'understand their current delivery system, and schedule a better time to continue '
             'the conversation.',
      'title': 'Don’t Quit Your Job—Start a Medical Courier Business After Work! (Giganomic '
               'Era)',
      'url': 'https://www.youtube.com/watch?v=7Mz5ctFZBX0&t=303s',
      'video_id': '7Mz5ctFZBX0'},
     {'author': 'Medical Courier Connection',
      'channel': 'Medical Courier Connection',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:05:41](https://www.youtube.com/watch?v=o1VRiVMJTpY&t=3941s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'First Steps class, you do you go over some of that stuff like setting up your '
              'business and having a bank account and all that kind of stuff?',
      'timestamp': 3941,
      'timestamp_label': '[01:05:41]',
      'timestamp_seconds': 3941,
      'tip': 'First Steps class, you do you go over some of that stuff like setting up your '
             'business and having a bank account and all that kind of stuff?',
      'title': "The Do's and Don'ts of Medical Courier Businesses #medicalcourier "
               '#courierservice #podcast (Medical Courier Connection)',
      'url': 'https://www.youtube.com/watch?v=o1VRiVMJTpY&t=3941s',
      'video_id': 'o1VRiVMJTpY'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:39](https://www.youtube.com/watch?v=j__fVq5xHLo&t=99s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Route Genie sends out an automatic reminder call to the passenger. These '
              'reminders, along with passenger app trip tracking, can reduce your no-show rate '
              'up to 50%. After a trip is complete, the system automatically creates an '
              'invoice.',
      'timestamp': 99,
      'timestamp_label': '[00:01:39]',
      'timestamp_seconds': 99,
      'tip': 'Route Genie sends out an automatic reminder call to the passenger. These '
             'reminders, along with passenger app trip tracking, can reduce your no-show rate '
             'up to 50%. After a trip is complete, the system automatically creates an '
             'invoice.',
      'title': 'RouteGenie - The Most Modern NEMT Software | Scheduling | Dispatching | '
               'Routing | Billing | And More (RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=j__fVq5xHLo&t=99s',
      'video_id': 'j__fVq5xHLo'},
     {'author': 'Boss up with Kae',
      'channel': 'Boss up with Kae',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=rwv6d5iSQQY&t=63s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So, contact them, try to get some business. Well, let's see how we can get "
              "rolling with Guardian. But first, we got to see where they are. Let's see if "
              "it's even worth going through the process.",
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': "So, contact them, try to get some business. Well, let's see how we can get "
             "rolling with Guardian. But first, we got to see where they are. Let's see if "
             "it's even worth going through the process.",
      'title': 'Major Pharmacy Hiring Medical Delivery Drivers — Company Vehicle Provided '
               '(Boss up with Kae)',
      'url': 'https://www.youtube.com/watch?v=rwv6d5iSQQY&t=63s',
      'video_id': 'rwv6d5iSQQY'},
     {'author': 'Motivational Charles',
      'channel': 'Motivational Charles',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=pFLQ24hu-Ac&t=39s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "State of north carolina for majority of the brokers that I've contacted you "
              "gotta be linked to nc trash you gotta hate npi number that's the second step "
              'now is the application fee that come with that 631 dollars so I just wanted '
              "y'all to know I made the step.",
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': "State of north carolina for majority of the brokers that I've contacted you "
             "gotta be linked to nc trash you gotta hate npi number that's the second step now "
             "is the application fee that come with that 631 dollars so I just wanted y'all to "
             'know I made the step.',
      'title': 'Second Step to take For Starting NEMT business After Getting NPI Number '
               '(Motivational Charles)',
      'url': 'https://www.youtube.com/watch?v=pFLQ24hu-Ac&t=39s',
      'video_id': 'pFLQ24hu-Ac'},
     {'author': 'KMD89 VA Claims Consulting - Dewayne Kimble',
      'channel': 'KMD89 VA Claims Consulting - Dewayne Kimble',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=mXUgy9Ypzrk&t=15s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Today I'm bring you another educational video but not on the VA claims process "
              'this is actually under VHA veterans healthc care administration and it is.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Today I'm bring you another educational video but not on the VA claims process "
             'this is actually under VHA veterans healthc care administration and it is.',
      'title': 'FREE Medical Transportation for Veterans! VHA-Uber Health Connect (KMD89 VA '
               'Claims Consulting - Dewayne Kimble)',
      'url': 'https://www.youtube.com/watch?v=mXUgy9Ypzrk&t=15s',
      'video_id': 'mXUgy9Ypzrk'},
     {'author': 'Green Spring US_Zero',
      'channel': 'Green Spring US_Zero',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:39](https://www.youtube.com/watch?v=8hlLcbvDBeM&t=99s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You don't need to manage the collection paperwork yourself, but you do have a "
              "role in confirming the details required of you. And what's the next step after "
              'the handoff? The secured specimen and its documentation are sent through the '
              'required process for laboratory testing.',
      'timestamp': 99,
      'timestamp_label': '[00:01:39]',
      'timestamp_seconds': 99,
      'tip': "You don't need to manage the collection paperwork yourself, but you do have a "
             "role in confirming the details required of you. And what's the next step after "
             'the handoff? The secured specimen and its documentation are sent through the '
             'required process for laboratory testing.',
      'title': 'DOT Drug Test Collection Procedure: What Drivers Can Expect (Green Spring '
               'US_Zero)',
      'url': 'https://www.youtube.com/watch?v=8hlLcbvDBeM&t=99s',
      'video_id': '8hlLcbvDBeM'},
     {'author': 'Zenpath Radio',
      'channel': 'Zenpath Radio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:25](https://www.youtube.com/watch?v=_BmJ_SxXCUY&t=1105s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Start an ent company to actually having or actually scheduling your first trip '
              'mm-hmm how long does that process let me take in.',
      'timestamp': 1105,
      'timestamp_label': '[00:18:25]',
      'timestamp_seconds': 1105,
      'tip': 'Start an ent company to actually having or actually scheduling your first trip '
             'mm-hmm how long does that process let me take in.',
      'title': 'Brokers vs Private Pay Clients for Your Non Emergency Medical Transportation '
               '(NEMT) Business (Zenpath Radio)',
      'url': 'https://www.youtube.com/watch?v=_BmJ_SxXCUY&t=1105s',
      'video_id': '_BmJ_SxXCUY'},
     {'author': 'United Medical Transportation Providers Group',
      'channel': 'United Medical Transportation Providers Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:32](https://www.youtube.com/watch?v=A2vs7pLblSk&t=1712s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'End when it comes time to acquire to sell your business acquire a business that '
              "they can't help you through the acquisition process what are we doing with them "
              "now run they haven't done.",
      'timestamp': 1712,
      'timestamp_label': '[00:28:32]',
      'timestamp_seconds': 1712,
      'tip': 'End when it comes time to acquire to sell your business acquire a business that '
             "they can't help you through the acquisition process what are we doing with them "
             "now run they haven't done.",
      'title': 'Lost Almost $200k Starting NEMT, Waiting on $45k from Modivcare, being "fined" '
               '$75k by MTM - Hijinks (United Medical Transportation Providers Group)',
      'url': 'https://www.youtube.com/watch?v=A2vs7pLblSk&t=1712s',
      'video_id': 'A2vs7pLblSk'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:24](https://www.youtube.com/watch?v=EPbM9tmaF8E&t=24s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Them back home the billing process begins while it might be the final step in a '
              "lengthy process it's one of the most important aspects of running an.",
      'timestamp': 24,
      'timestamp_label': '[00:00:24]',
      'timestamp_seconds': 24,
      'tip': 'Them back home the billing process begins while it might be the final step in a '
             "lengthy process it's one of the most important aspects of running an.",
      'title': 'How to Bill NEMT Trips | RouteGenie (RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=EPbM9tmaF8E&t=24s',
      'video_id': 'EPbM9tmaF8E'},
     {'author': 'Giganomic Era',
      'channel': 'Giganomic Era',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:50](https://www.youtube.com/watch?v=J9XCEoIfTU4&t=230s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Don't lock yourself into a $35 delivery that ends up consuming 2 to 3 hours of "
              'your day. Deliveries must use service entrance at the rear of building. But, in '
              'this case, I could just Oh my god. To the rear of the building. All right, the '
              'pharmacy workers handled.',
      'timestamp': 230,
      'timestamp_label': '[00:03:50]',
      'timestamp_seconds': 230,
      'tip': "Don't lock yourself into a $35 delivery that ends up consuming 2 to 3 hours of "
             'your day. Deliveries must use service entrance at the rear of building. But, in '
             'this case, I could just Oh my god. To the rear of the building. All right, the '
             'pharmacy workers handled.',
      'title': "The Truth About Medical Courier Work It's Not Just Driving! (Giganomic Era)",
      'url': 'https://www.youtube.com/watch?v=J9XCEoIfTU4&t=230s',
      'video_id': 'J9XCEoIfTU4'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:47](https://www.youtube.com/watch?v=eKdj-HOLoXU&t=287s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Confirmation messages within the system providers are immediately informed '
              'about cancellations or schedule changes offers schedule customization for.',
      'timestamp': 287,
      'timestamp_label': '[00:04:47]',
      'timestamp_seconds': 287,
      'tip': 'Confirmation messages within the system providers are immediately informed about '
             'cancellations or schedule changes offers schedule customization for.',
      'title': 'Challenges in Dealing with No Shows in the NEMT Industry  | RouteGenie '
               '(RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=eKdj-HOLoXU&t=287s',
      'video_id': 'eKdj-HOLoXU'},
     {'author': 'Veterans Health Administration',
      'channel': 'Veterans Health Administration',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:16](https://www.youtube.com/watch?v=nQ12WJ2mSwE&t=136s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'What if I need help submitting my claim? Then follow that link to find the '
              'travel contact for your facility. For additional help, contact the Beneficiary '
              'Travel Self-Service System Toll-Free Call Center.',
      'timestamp': 136,
      'timestamp_label': '[00:02:16]',
      'timestamp_seconds': 136,
      'tip': 'What if I need help submitting my claim? Then follow that link to find the '
             'travel contact for your facility. For additional help, contact the Beneficiary '
             'Travel Self-Service System Toll-Free Call Center.',
      'title': 'VA Travel Pay Reimbursement (Veterans Health Administration)',
      'url': 'https://www.youtube.com/watch?v=nQ12WJ2mSwE&t=136s',
      'video_id': 'nQ12WJ2mSwE'}],
 8: [{'author': 'United Medical Transportation Providers Group',
      'channel': 'United Medical Transportation Providers Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=PVivs9VOAyw&t=50s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "NMT business, but they've never done it themselves. They're strictly a software "
              "platform and they're giving you poor, foolish, nonsensical broker advice "
              'designed to enslave you, get you using their platforms, which are integrated '
              'with the brokers.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': "NMT business, but they've never done it themselves. They're strictly a software "
             "platform and they're giving you poor, foolish, nonsensical broker advice "
             'designed to enslave you, get you using their platforms, which are integrated '
             'with the brokers.',
      'title': 'These Hospitals are paying $6k per day to our Non-Emergency Medical '
               'Transportation Provider - Part 4 (United Medical Transportation Providers '
               'Group)',
      'url': 'https://www.youtube.com/watch?v=PVivs9VOAyw&t=50s',
      'video_id': 'PVivs9VOAyw'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=FBWU2kTGLwI&t=111s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Having a great NEMT scheduling software will track all of these different '
              'trips. Working with all of these accounts can seem overwhelming but with a NEMT '
              'billing software tool it can be made simple.',
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': 'Having a great NEMT scheduling software will track all of these different trips. '
             'Working with all of these accounts can seem overwhelming but with a NEMT billing '
             'software tool it can be made simple.',
      'title': "Does Modivcare Pay for Driver's Wait Time? NEMT Business | RouteGenie "
               '(RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=FBWU2kTGLwI&t=111s',
      'video_id': 'FBWU2kTGLwI'},
     {'author': 'Bambi',
      'channel': 'Bambi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:40](https://www.youtube.com/watch?v=CbCgWxHPCxU&t=760s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'What about invoicing like throughout the software? So going to go to the '
              'billing section. So this is invoicing and credit card processing. So all your '
              'trips are already in Bambi.',
      'timestamp': 760,
      'timestamp_label': '[00:12:40]',
      'timestamp_seconds': 760,
      'tip': 'What about invoicing like throughout the software? So going to go to the billing '
             'section. So this is invoicing and credit card processing. So all your trips are '
             'already in Bambi.',
      'title': 'How to demo NEMT software | NEMT Experts Podcast Episode 63 (Bambi)',
      'url': 'https://www.youtube.com/watch?v=CbCgWxHPCxU&t=760s',
      'video_id': 'CbCgWxHPCxU'},
     {'author': 'Shantasia_RN',
      'channel': 'Shantasia_RN',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:08](https://www.youtube.com/watch?v=3tRytphhdUU&t=128s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "When you're in your broker portal or your whatever dispatching software you use "
              'and you see extra trips that is not being used and you could use another driver '
              'to pick up those trips, then hire another driver and get another vehicle.',
      'timestamp': 128,
      'timestamp_label': '[00:02:08]',
      'timestamp_seconds': 128,
      'tip': "When you're in your broker portal or your whatever dispatching software you use "
             'and you see extra trips that is not being used and you could use another driver '
             'to pick up those trips, then hire another driver and get another vehicle.',
      'title': 'How Many NEMT Trips Does It Take to Make $10,000 a Month? (Shantasia_RN)',
      'url': 'https://www.youtube.com/watch?v=3tRytphhdUU&t=128s',
      'video_id': '3tRytphhdUU'},
     {'author': 'Medirydes Nemt Software',
      'channel': 'Medirydes Nemt Software',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:46](https://www.youtube.com/watch?v=6lnCunvrFc4&t=286s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Perfect software for becoming more organized paperless and successful visit our '
              'website today at www.medirides.com and download our app now on both app and '
              'play store we are eagerly waiting to walk with you side by side on this journey '
              'happy dispatching.',
      'timestamp': 286,
      'timestamp_label': '[00:04:46]',
      'timestamp_seconds': 286,
      'tip': 'Perfect software for becoming more organized paperless and successful visit our '
             'website today at www.medirides.com and download our app now on both app and play '
             'store we are eagerly waiting to walk with you side by side on this journey happy '
             'dispatching.',
      'title': 'MediRydes NEMT Scheduling, Routing, Dispatching & Billing Software (Medirydes '
               'Nemt Software)',
      'url': 'https://www.youtube.com/watch?v=6lnCunvrFc4&t=286s',
      'video_id': '6lnCunvrFc4'},
     {'author': 'Nemt University',
      'channel': 'Nemt University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:57](https://www.youtube.com/watch?v=mgK4ir9UXtc&t=597s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re not don't have you know what I'm saying a background as far as you know "
              'dealing with these different data data I guess data entry that >> what you just '
              "showed me is like something that's uh wow this is real powerful.",
      'timestamp': 597,
      'timestamp_label': '[00:09:57]',
      'timestamp_seconds': 597,
      'tip': "'re not don't have you know what I'm saying a background as far as you know "
             'dealing with these different data data I guess data entry that >> what you just '
             "showed me is like something that's uh wow this is real powerful.",
      'title': 'NEMT DISPATCHING WALK THROUGH--BAMBI SOFTWARE (Nemt University)',
      'url': 'https://www.youtube.com/watch?v=mgK4ir9UXtc&t=597s',
      'video_id': 'mgK4ir9UXtc'},
     {'author': 'ZeitRide NEMT Software',
      'channel': 'ZeitRide NEMT Software',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:22](https://www.youtube.com/watch?v=ajqkD-2jPd8&t=682s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Chinese and like then we completely changed the format for their software so '
              "that it was in Chinese for them cuz it's not about onesizefits-all, especially "
              'in this industry where you need something that makes sense for your team, your '
              'business.',
      'timestamp': 682,
      'timestamp_label': '[00:11:22]',
      'timestamp_seconds': 682,
      'tip': 'Chinese and like then we completely changed the format for their software so '
             "that it was in Chinese for them cuz it's not about onesizefits-all, especially "
             'in this industry where you need something that makes sense for your team, your '
             'business.',
      'title': 'NEMT Audits Are Getting Tighter: How to Prove Every Trip | ft. Zeit Ride '
               '(ZeitRide NEMT Software)',
      'url': 'https://www.youtube.com/watch?v=ajqkD-2jPd8&t=682s',
      'video_id': 'ajqkD-2jPd8'},
     {'author': 'Markie Williams Online Certification Courses',
      'channel': 'Markie Williams Online Certification Courses',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=i8W-39NkgDQ&t=114s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Description.  Regarding temperature monitoring and tracking software to check '
              'out  such software like sensors and internet.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': 'Description.  Regarding temperature monitoring and tracking software to check '
             'out  such software like sensors and internet.',
      'title': 'Medical Courier Cold Chain Delivery Course (Markie Williams Online '
               'Certification Courses)',
      'url': 'https://www.youtube.com/watch?v=i8W-39NkgDQ&t=114s',
      'video_id': 'i8W-39NkgDQ'},
     {'author': 'Medical Courier Connection',
      'channel': 'Medical Courier Connection',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:06](https://www.youtube.com/watch?v=oF-_Ka8kNzk&t=306s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can also take our specimen handling and transport course now available on '
              'Apple iOS. You can go into the App Store and search Integrity Medical Courier '
              'Training. You can download the app, purchase the specimen handling and '
              'transport course.',
      'timestamp': 306,
      'timestamp_label': '[00:05:06]',
      'timestamp_seconds': 306,
      'tip': 'You can also take our specimen handling and transport course now available on '
             'Apple iOS. You can go into the App Store and search Integrity Medical Courier '
             'Training. You can download the app, purchase the specimen handling and transport '
             'course.',
      'title': 'How To Set-Up A Specimen Cooler For Medical Courier Work (Medical Courier '
               'Connection)',
      'url': 'https://www.youtube.com/watch?v=oF-_Ka8kNzk&t=306s',
      'video_id': 'oF-_Ka8kNzk'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:59](https://www.youtube.com/watch?v=V_r1oFY0--w&t=179s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'More information on route Genie driver app, check out the video link in the '
              'description. Simplified  billing. Working with NMT dispatch software makes.',
      'timestamp': 179,
      'timestamp_label': '[00:02:59]',
      'timestamp_seconds': 179,
      'tip': 'More information on route Genie driver app, check out the video link in the '
             'description. Simplified  billing. Working with NMT dispatch software makes.',
      'title': 'How Does an NEMT Dispatch System Work | RouteGenie (RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=V_r1oFY0--w&t=179s',
      'video_id': 'V_r1oFY0--w'},
     {'author': 'MJ Business Academy',
      'channel': 'MJ Business Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=KSSO5Igfn2Y&t=15s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Inquire about broker contracts yeah that is the number one question that we get '
              'and we just kind of wanted to share some light on.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Inquire about broker contracts yeah that is the number one question that we get '
             'and we just kind of wanted to share some light on.',
      'title': 'Step-by-Step Guide to Finding NEMT Brokers (MJ Business Academy)',
      'url': 'https://www.youtube.com/watch?v=KSSO5Igfn2Y&t=15s',
      'video_id': 'KSSO5Igfn2Y'},
     {'author': 'HNL Lab Medicine',
      'channel': 'HNL Lab Medicine',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=C1dIA8HJSJc&t=62s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Headquarter we have roughly 140 couriers in our department we'll drive anywhere "
              'from 40 miles to 330 miles in an eight-hour tape and we drive roughly 2.7 '
              'million miles a year which could send us back and forth to the Moon six times '
              'or around the earth a hundred times.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': "Headquarter we have roughly 140 couriers in our department we'll drive anywhere "
             'from 40 miles to 330 miles in an eight-hour tape and we drive roughly 2.7 '
             'million miles a year which could send us back and forth to the Moon six times or '
             'around the earth a hundred times.',
      'title': 'A Day in the Life of an HNL Lab Medicine Courier (HNL Lab Medicine)',
      'url': 'https://www.youtube.com/watch?v=C1dIA8HJSJc&t=62s',
      'video_id': 'C1dIA8HJSJc'},
     {'author': 'Nemt University',
      'channel': 'Nemt University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:19](https://www.youtube.com/watch?v=sj-P7btgpOQ&t=619s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Play when it comes to dealing with uh you know passengers and clients and your '
              'business in particular so you want to go to uh CTA www.ctaa.org forward slash '
              'pass PA.',
      'timestamp': 619,
      'timestamp_label': '[00:10:19]',
      'timestamp_seconds': 619,
      'tip': 'Play when it comes to dealing with uh you know passengers and clients and your '
             'business in particular so you want to go to uh CTA www.ctaa.org forward slash '
             'pass PA.',
      'title': 'New Series “NEMT COACHES CORNER” Ep.2 HOW TO START MY NEMT IN VIRGINIA (Nemt '
               'University)',
      'url': 'https://www.youtube.com/watch?v=sj-P7btgpOQ&t=619s',
      'video_id': 'sj-P7btgpOQ'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:43](https://www.youtube.com/watch?v=uJV2f3MOJbI&t=643s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Once you've got the right fleet, explore new trip opportunities with routing "
              'software. No matter what segment you operate in, the right software can '
              'supercharge earnings through efficient scheduling, routing, billing, and '
              'dispatching.',
      'timestamp': 643,
      'timestamp_label': '[00:10:43]',
      'timestamp_seconds': 643,
      'tip': "Once you've got the right fleet, explore new trip opportunities with routing "
             'software. No matter what segment you operate in, the right software can '
             'supercharge earnings through efficient scheduling, routing, billing, and '
             'dispatching.',
      'title': 'Best NEMT Vehicles You Can Buy in 2026: Guide with Prices and Specifications '
               '(RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=uJV2f3MOJbI&t=643s',
      'video_id': 'uJV2f3MOJbI'},
     {'author': 'SwiftAid Transport',
      'channel': 'SwiftAid Transport',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:33:19](https://www.youtube.com/watch?v=YGC_f04Hg3g&t=1999s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The Office for Civil Rights, which enforces HIPAA, does not issue warnings. '
              'They have recently levied over $28 million in fines for data breaches. The '
              'software must be perfectly transparent with the broker but hermetically sealed '
              'from the public.',
      'timestamp': 1999,
      'timestamp_label': '[00:33:19]',
      'timestamp_seconds': 1999,
      'tip': 'The Office for Civil Rights, which enforces HIPAA, does not issue warnings. They '
             'have recently levied over $28 million in fines for data breaches. The software '
             'must be perfectly transparent with the broker but hermetically sealed from the '
             'public.',
      'title': 'GPS with NEMT (SwiftAid Transport)',
      'url': 'https://www.youtube.com/watch?v=YGC_f04Hg3g&t=1999s',
      'video_id': 'YGC_f04Hg3g'}],
 9: [{'author': 'Geoff Cole',
      'channel': 'Geoff Cole',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:51](https://www.youtube.com/watch?v=Op3a3Fthhno&t=171s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, you look at the go down, you know, scoop down. This is just some skimming '
              'through looking through the contract and you get your insurance requirements '
              'and the minimum requirements. Hey, man, you have to have a business in the '
              'state. You have to have a driver license.',
      'timestamp': 171,
      'timestamp_label': '[00:02:51]',
      'timestamp_seconds': 171,
      'tip': 'So, you look at the go down, you know, scoop down. This is just some skimming '
             'through looking through the contract and you get your insurance requirements and '
             'the minimum requirements. Hey, man, you have to have a business in the state. '
             'You have to have a driver license.',
      'title': 'How to land Medical Courier Contracts that Pay 10k per Month (Geoff Cole)',
      'url': 'https://www.youtube.com/watch?v=Op3a3Fthhno&t=171s',
      'video_id': 'Op3a3Fthhno'},
     {'author': 'Nemiton',
      'channel': 'Nemiton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:51](https://www.youtube.com/watch?v=qijT2a0o9VE&t=171s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The signed provider agreement. Read it before you sign it. It's a contract, not "
              'a formality. An ACH form for direct deposit because this is how you get paid. '
              'Copies of every license, business, driver, and vehicle.',
      'timestamp': 171,
      'timestamp_label': '[00:02:51]',
      'timestamp_seconds': 171,
      'tip': "The signed provider agreement. Read it before you sign it. It's a contract, not "
             'a formality. An ACH form for direct deposit because this is how you get paid. '
             'Copies of every license, business, driver, and vehicle.',
      'title': 'Medicaid Provider Enrollment The Step by Step Nobody Shows You (Nemiton)',
      'url': 'https://www.youtube.com/watch?v=qijT2a0o9VE&t=171s',
      'video_id': 'qijT2a0o9VE'},
     {'author': 'HIPAA Training',
      'channel': 'HIPAA Training',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:13](https://www.youtube.com/watch?v=zLJq8PlUMDQ&t=73s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Essential training and certifications. You get the following required '
              'self-paced online courses for $90. HIPAA privacy and security compliance '
              'training for business associates. OSHA hazard communication training. OSHA '
              'bloodborne pathogens BBP training.',
      'timestamp': 73,
      'timestamp_label': '[00:01:13]',
      'timestamp_seconds': 73,
      'tip': 'Essential training and certifications. You get the following required self-paced '
             'online courses for $90. HIPAA privacy and security compliance training for '
             'business associates. OSHA hazard communication training. OSHA bloodborne '
             'pathogens BBP training.',
      'title': 'Online Medical Courier Certification Training Pack – Complete Compliance & '
               'Safety Courses (HIPAA Training)',
      'url': 'https://www.youtube.com/watch?v=zLJq8PlUMDQ&t=73s',
      'video_id': 'zLJq8PlUMDQ'},
     {'author': 'Diamond Hunter Enterprises',
      'channel': 'Diamond Hunter Enterprises',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:10](https://www.youtube.com/watch?v=ErKSotzJID0&t=550s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The option year is year two. Uh the option period 2 is year three. So, it's a "
              "total of 3ear contract. It's 247 courier service on call for the transportation "
              'of general pharmacy supplies between tri-state area and the VAMC Huntington to '
              'include seabbox.',
      'timestamp': 550,
      'timestamp_label': '[00:09:10]',
      'timestamp_seconds': 550,
      'tip': "The option year is year two. Uh the option period 2 is year three. So, it's a "
             "total of 3ear contract. It's 247 courier service on call for the transportation "
             'of general pharmacy supplies between tri-state area and the VAMC Huntington to '
             'include seabbox.',
      'title': 'Land SAM.gov Driver Contracts: Medical Courier 2026 | How to Find Government '
               'Contracts Step-By-Step (Diamond Hunter Enterprises)',
      'url': 'https://www.youtube.com/watch?v=ErKSotzJID0&t=550s',
      'video_id': 'ErKSotzJID0'},
     {'author': 'NEMT Sales is now NEMT-Alliance.',
      'channel': 'NEMT Sales is now NEMT-Alliance.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=HxtN-7tsjNA&t=78s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Myself some kind of broker expert but number two every state has different '
              "requirements for what is needed but i'm going to do my best to you know.",
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'Myself some kind of broker expert but number two every state has different '
             "requirements for what is needed but i'm going to do my best to you know.",
      'title': 'How to sell NEMT Brokers (NEMT Sales is now NEMT-Alliance.)',
      'url': 'https://www.youtube.com/watch?v=HxtN-7tsjNA&t=78s',
      'video_id': 'HxtN-7tsjNA'},
     {'author': 'Lavish Life',
      'channel': 'Lavish Life',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=_GYJDRIHqL4&t=91s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Find you a dedicated contract with the company directly or a great dispatcher '
              "broker that can really make you some money out here because I'm never using "
              'apps and I never recommend them to anyone what whatsoever.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': 'Find you a dedicated contract with the company directly or a great dispatcher '
             "broker that can really make you some money out here because I'm never using apps "
             'and I never recommend them to anyone what whatsoever.',
      'title': 'APPS V.S. BROKERAGE COMPANIES AS A MEDICAL COURIER ❗ WHAT TO USE (MUST SEE)  '
               '💸💸💰 (Lavish Life)',
      'url': 'https://www.youtube.com/watch?v=_GYJDRIHqL4&t=91s',
      'video_id': '_GYJDRIHqL4'},
     {'author': 'No Boss Blueprint',
      'channel': 'No Boss Blueprint',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:23](https://www.youtube.com/watch?v=99Brd_naNps&t=503s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Must be based in the area where Amazon Flex operates, which is most major '
              "cities. Have a valid driver's license and SSN. Have a smartphone, pretty "
              'standard stuff. And also have a bank account. And you can also choose when to '
              'collect payment.',
      'timestamp': 503,
      'timestamp_label': '[00:08:23]',
      'timestamp_seconds': 503,
      'tip': 'Must be based in the area where Amazon Flex operates, which is most major '
             "cities. Have a valid driver's license and SSN. Have a smartphone, pretty "
             'standard stuff. And also have a bank account. And you can also choose when to '
             'collect payment.',
      'title': 'Pharmacies need drivers now! 💰 make extra Money with these medical delivery '
               'apps (No Boss Blueprint)',
      'url': 'https://www.youtube.com/watch?v=99Brd_naNps&t=503s',
      'video_id': '99Brd_naNps'},
     {'author': 'WM NEMT Startup Coach',
      'channel': 'WM NEMT Startup Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=8iqgyqMjxnk&t=25s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Just good business it's an ethical obligation let's start with Medicaid "
              'Medicaid is a joint effort between the federal and state governments to '
              'provide.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': "Just good business it's an ethical obligation let's start with Medicaid Medicaid "
             'is a joint effort between the federal and state governments to provide.',
      'title': 'Avoid the Biggest Mistakes with Medicare & Medicaid in NEMT (WM NEMT Startup '
               'Coach)',
      'url': 'https://www.youtube.com/watch?v=8iqgyqMjxnk&t=25s',
      'video_id': '8iqgyqMjxnk'},
     {'author': 'Ello Hunny Bun',
      'channel': 'Ello Hunny Bun',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:21](https://www.youtube.com/watch?v=E3e6CHFWKNE&t=321s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "No, you don't need a clean criminal background, but it also just depends on the "
              'contract. Every company is different, and it also depends on what your charge '
              "was. If your charge was stealing pharmaceuticals, then you probably won't get "
              'the job.',
      'timestamp': 321,
      'timestamp_label': '[00:05:21]',
      'timestamp_seconds': 321,
      'tip': "No, you don't need a clean criminal background, but it also just depends on the "
             'contract. Every company is different, and it also depends on what your charge '
             "was. If your charge was stealing pharmaceuticals, then you probably won't get "
             'the job.',
      'title': 'How I Make $3500/Week Using My Own Vehicle (No Experience Needed!) Step By '
               'Step (Ello Hunny Bun)',
      'url': 'https://www.youtube.com/watch?v=E3e6CHFWKNE&t=321s',
      'video_id': 'E3e6CHFWKNE'},
     {'author': 'Nemt University',
      'channel': 'Nemt University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:05](https://www.youtube.com/watch?v=0nJ9GYcr744&t=125s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you are in the broker state in a previous video we talked about what states '
              'are broker States such as New Mexico Arizona California Ohio Virginia West '
              'Virginia New York New Jersey Illinois.',
      'timestamp': 125,
      'timestamp_label': '[00:02:05]',
      'timestamp_seconds': 125,
      'tip': 'If you are in the broker state in a previous video we talked about what states '
             'are broker States such as New Mexico Arizona California Ohio Virginia West '
             'Virginia New York New Jersey Illinois.',
      'title': '(WATCH LIST👀) NEMT LIST OF BROKERS TO PARTNER WITH💡 (Nemt University)',
      'url': 'https://www.youtube.com/watch?v=0nJ9GYcr744&t=125s',
      'video_id': '0nJ9GYcr744'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:15](https://www.youtube.com/watch?v=_mEgB7bAsFE&t=135s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'On October 15th, the Louisiana Division of Administration opened bidding for a '
              'broker to run Medicaid fee-for-service transportation statewide, with proposals '
              'due November 24th. A new broker means a new network, and every provider in the '
              'state gets a fresh look.',
      'timestamp': 135,
      'timestamp_label': '[00:02:15]',
      'timestamp_seconds': 135,
      'tip': 'On October 15th, the Louisiana Division of Administration opened bidding for a '
             'broker to run Medicaid fee-for-service transportation statewide, with proposals '
             'due November 24th. A new broker means a new network, and every provider in the '
             'state gets a fresh look.',
      'title': 'Congress Wants Every Medicaid Trip Verified? Genie Journal Recap, NEMT News '
               'October 2026 (RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=_mEgB7bAsFE&t=135s',
      'video_id': '_mEgB7bAsFE'},
     {'author': 'Dean Medical Courier Academy',
      'channel': 'Dean Medical Courier Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:22](https://www.youtube.com/watch?v=ZJagcSpBYaQ&t=262s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Missouri Secretary of State. Notice all the opportunities there. I have '
              'developed a full method for finding medical carrier opportunities at the '
              'secretary of state level. Listen, once you get a list, you get a job alerts '
              'that are alerting you to jobs.',
      'timestamp': 262,
      'timestamp_label': '[00:04:22]',
      'timestamp_seconds': 262,
      'tip': 'Missouri Secretary of State. Notice all the opportunities there. I have '
             'developed a full method for finding medical carrier opportunities at the '
             'secretary of state level. Listen, once you get a list, you get a job alerts that '
             'are alerting you to jobs.',
      'title': 'The Truth About Medical Courier Work  (No One Tells You This) (Dean Medical '
               'Courier Academy)',
      'url': 'https://www.youtube.com/watch?v=ZJagcSpBYaQ&t=262s',
      'video_id': 'ZJagcSpBYaQ'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:01](https://www.youtube.com/watch?v=GWBpqyUYyjE&t=481s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'For NEMT, the split is what matters. Autonomous vehicles and rideshare can take '
              'on appropriate ambulatory demand, while specialized providers continue serving '
              'wheelchair assisted, rural, long-distance, and higher acuity trips.',
      'timestamp': 481,
      'timestamp_label': '[00:08:01]',
      'timestamp_seconds': 481,
      'tip': 'For NEMT, the split is what matters. Autonomous vehicles and rideshare can take '
             'on appropriate ambulatory demand, while specialized providers continue serving '
             'wheelchair assisted, rural, long-distance, and higher acuity trips.',
      'title': '$12M in Fake Medicaid Rides, GPS Spoofing, and a Broker Shakeup | NEMT News '
               'August 2026 (RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=GWBpqyUYyjE&t=481s',
      'video_id': 'GWBpqyUYyjE'},
     {'author': 'RouteGenie',
      'channel': 'RouteGenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=d8ocN3ERJag&t=36s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Operations and schedule for the day trip cancellation can cause a ripple effect '
              'leading to a loss of Revenue decreased customer satisfaction and even legal.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': 'Operations and schedule for the day trip cancellation can cause a ripple effect '
             'leading to a loss of Revenue decreased customer satisfaction and even legal.',
      'title': 'Canceled Trips in NEMT: What Medical Transportation Providers Need to Do  | '
               'RouteGenie (RouteGenie)',
      'url': 'https://www.youtube.com/watch?v=d8ocN3ERJag&t=36s',
      'video_id': 'd8ocN3ERJag'},
     {'author': 'Geoff Cole',
      'channel': 'Geoff Cole',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:42](https://www.youtube.com/watch?v=dLgmDQavyEU&t=282s)',
      'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                   'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                   'asset-light 1099 owner-operator dispatch brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Becoming an NEMT provider means complete medical provider enrollment, obtaining '
              "your NPI number, meeting your state's license requirements, and registering "
              'with NEMT broker networks. The full process takes 60 to 120 days.',
      'timestamp': 282,
      'timestamp_label': '[00:04:42]',
      'timestamp_seconds': 282,
      'tip': 'Becoming an NEMT provider means complete medical provider enrollment, obtaining '
             "your NPI number, meeting your state's license requirements, and registering with "
             'NEMT broker networks. The full process takes 60 to 120 days.',
      'title': 'Starting NEMT in 2026 | Licensing, Insurance & Contract Reality (Geoff Cole)',
      'url': 'https://www.youtube.com/watch?v=dLgmDQavyEU&t=282s',
      'video_id': 'dLgmDQavyEU'}],
 10: [{'author': 'MICHAEL PACHECO',
       'channel': 'MICHAEL PACHECO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:44](https://www.youtube.com/watch?v=QWuDUoAMiQU&t=224s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'AI assisted resources, templates, standard operating procedures, business '
               'guides and workbooks, implementation tools, action plans, coaching and '
               'community support. The system is organized around four stages: build, launch, '
               'operate, scale.',
       'timestamp': 224,
       'timestamp_label': '[00:03:44]',
       'timestamp_seconds': 224,
       'tip': 'AI assisted resources, templates, standard operating procedures, business '
              'guides and workbooks, implementation tools, action plans, coaching and '
              'community support. The system is organized around four stages: build, launch, '
              'operate, scale.',
       'title': 'How to Start a Transportation Business in 2026 | NEMT, Medical Courier & '
                'Logistics (MICHAEL PACHECO)',
       'url': 'https://www.youtube.com/watch?v=QWuDUoAMiQU&t=224s',
       'video_id': 'QWuDUoAMiQU'},
      {'author': 'SwiftAid Transport',
       'channel': 'SwiftAid Transport',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:40:09](https://www.youtube.com/watch?v=YGC_f04Hg3g&t=2409s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The next time you pass a medical transport van on the highway, remember the '
               'sheer volume of data, encryption, and AI running invisibly in the background '
               'making sure a vulnerable person makes it to the care they desperately need. We '
               'will see you on the next deep dive.',
       'timestamp': 2409,
       'timestamp_label': '[00:40:09]',
       'timestamp_seconds': 2409,
       'tip': 'The next time you pass a medical transport van on the highway, remember the '
              'sheer volume of data, encryption, and AI running invisibly in the background '
              'making sure a vulnerable person makes it to the care they desperately need. We '
              'will see you on the next deep dive.',
       'title': 'GPS with NEMT (SwiftAid Transport)',
       'url': 'https://www.youtube.com/watch?v=YGC_f04Hg3g&t=2409s',
       'video_id': 'YGC_f04Hg3g'},
      {'author': 'Nemt University',
       'channel': 'Nemt University',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:33](https://www.youtube.com/watch?v=ZerukPCXB6Q&t=633s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Our broker States and the main brokers that do these type of services where '
               'EMT would be Vo MTM mod of care LogistiCare which is mod of care now.',
       'timestamp': 633,
       'timestamp_label': '[00:10:33]',
       'timestamp_seconds': 633,
       'tip': 'Our broker States and the main brokers that do these type of services where EMT '
              'would be Vo MTM mod of care LogistiCare which is mod of care now.',
       'title': 'HOW MUCH DOES MEDICAID PAY NEMT BUSINESSES FOR SERVICES (Nemt University)',
       'url': 'https://www.youtube.com/watch?v=ZerukPCXB6Q&t=633s',
       'video_id': 'ZerukPCXB6Q'},
      {'author': 'RouteGenie',
       'channel': 'RouteGenie',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:30](https://www.youtube.com/watch?v=5usA-OlRapg&t=30s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Medical carriers deliver critical health care materials that can't wait for "
               'regular shipping. This includes medications, lab specimens, test results, '
               'medical supplies, and healthcare documents. Speed and safety are everything in '
               'this business.',
       'timestamp': 30,
       'timestamp_label': '[00:00:30]',
       'timestamp_seconds': 30,
       'tip': "Medical carriers deliver critical health care materials that can't wait for "
              'regular shipping. This includes medications, lab specimens, test results, '
              'medical supplies, and healthcare documents. Speed and safety are everything in '
              'this business.',
       'title': 'Medical Courier vs NEMT: Which Healthcare Transport Business Is Right for '
                'You? (RouteGenie)',
       'url': 'https://www.youtube.com/watch?v=5usA-OlRapg&t=30s',
       'video_id': '5usA-OlRapg'},
      {'author': 'Julian Sage',
       'channel': 'Julian Sage',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:56](https://www.youtube.com/watch?v=bxU3wwadyQA&t=356s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Website from a template and as you can see here we have literally hundreds of '
               'different websites that we could select from that you can choose for building.',
       'timestamp': 356,
       'timestamp_label': '[00:05:56]',
       'timestamp_seconds': 356,
       'tip': 'Website from a template and as you can see here we have literally hundreds of '
              'different websites that we could select from that you can choose for building.',
       'title': 'Start a Six Figure Medical Courier Business (Julian Sage)',
       'url': 'https://www.youtube.com/watch?v=bxU3wwadyQA&t=356s',
       'video_id': 'bxU3wwadyQA'},
      {'author': 'Ello Hunny Bun',
       'channel': 'Ello Hunny Bun',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=QxvapgKdXHI&t=20s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It's your gal or you can call me Miss Honey. I love to spread the wealth. On "
               'this channel, we talk about making money, building credit, helpful resources, '
               'opportunities, going from surviving to thriving.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': "It's your gal or you can call me Miss Honey. I love to spread the wealth. On "
              'this channel, we talk about making money, building credit, helpful resources, '
              'opportunities, going from surviving to thriving.',
       'title': 'How I Make $700/Day Using My Own Vehicle (No Experience Needed!) (Ello Hunny '
                'Bun)',
       'url': 'https://www.youtube.com/watch?v=QxvapgKdXHI&t=20s',
       'video_id': 'QxvapgKdXHI'},
      {'author': 'United Medical Transportation Providers Group',
       'channel': 'United Medical Transportation Providers Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:40](https://www.youtube.com/watch?v=qAPPJwM3HPI&t=40s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That's the ultimate goal because you want to build that honeypot so that the "
               'honeypot ultimately it makes more money than your actual frontline business, '
               'whatever that is, whether it is AMT, home care or other. Could be worse if if '
               'he went downstate New York.',
       'timestamp': 40,
       'timestamp_label': '[00:00:40]',
       'timestamp_seconds': 40,
       'tip': "That's the ultimate goal because you want to build that honeypot so that the "
              'honeypot ultimately it makes more money than your actual frontline business, '
              'whatever that is, whether it is AMT, home care or other. Could be worse if if '
              'he went downstate New York.',
       'title': "Abandon Non-Emergency Transportation if You're NOT Making REAL Money! STOP "
                'Working for FREE! (United Medical Transportation Providers Group)',
       'url': 'https://www.youtube.com/watch?v=qAPPJwM3HPI&t=40s',
       'video_id': 'qAPPJwM3HPI'},
      {'author': 'Giganomic Era',
       'channel': 'Giganomic Era',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:20](https://www.youtube.com/watch?v=VOBDHU3FYtA&t=380s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You need to understand, these companies are not looking for the fastest '
               "driver, they're not looking for the five-star app rating, they're looking for "
               'reliability, show up on time, handle packages with care, and communicate '
               'professionally.',
       'timestamp': 380,
       'timestamp_label': '[00:06:20]',
       'timestamp_seconds': 380,
       'tip': 'You need to understand, these companies are not looking for the fastest driver, '
              "they're not looking for the five-star app rating, they're looking for "
              'reliability, show up on time, handle packages with care, and communicate '
              'professionally.',
       'title': 'These 3 Medical Courier Companies Are Hiring With No Experience Right Now '
                '(Giganomic Era)',
       'url': 'https://www.youtube.com/watch?v=VOBDHU3FYtA&t=380s',
       'video_id': 'VOBDHU3FYtA'},
      {'author': 'Nemt Business Life',
       'channel': 'Nemt Business Life',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:51](https://www.youtube.com/watch?v=UtiLgcZo4dU&t=591s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "The nursing home they basically like went to the bank told the bank they don't "
               "know who this company is that's charging them.",
       'timestamp': 591,
       'timestamp_label': '[00:09:51]',
       'timestamp_seconds': 591,
       'tip': "The nursing home they basically like went to the bank told the bank they don't "
              "know who this company is that's charging them.",
       'title': 'NEMT PRIVATE PAY (Nemt Business Life)',
       'url': 'https://www.youtube.com/watch?v=UtiLgcZo4dU&t=591s',
       'video_id': 'UtiLgcZo4dU'},
      {'author': 'WTEN',
       'channel': 'WTEN',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:30](https://www.youtube.com/watch?v=qMb3ANIPN3Y&t=30s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "1 MILLION SETTLEMENT WAS REACHED IN THAT CASE BUT OFFICIALS CLAIM IT DIDN'T "
               'STOP THERE. SOT, ROBERT CARNEY, SCHENECTADY COUNTY DISTRICT ATTORNEY: "SO WE '
               'PICKED IT UP AND UNFORTUNATELY HE WAS STILL IN BUSINESS, STILL DOING THE SAME '
               'STUFF.".',
       'timestamp': 30,
       'timestamp_label': '[00:00:30]',
       'timestamp_seconds': 30,
       'tip': "1 MILLION SETTLEMENT WAS REACHED IN THAT CASE BUT OFFICIALS CLAIM IT DIDN'T "
              'STOP THERE. SOT, ROBERT CARNEY, SCHENECTADY COUNTY DISTRICT ATTORNEY: "SO WE '
              'PICKED IT UP AND UNFORTUNATELY HE WAS STILL IN BUSINESS, STILL DOING THE SAME '
              'STUFF.".',
       'title': 'Update on Medicaid Transportation fraud scheme (WTEN)',
       'url': 'https://www.youtube.com/watch?v=qMb3ANIPN3Y&t=30s',
       'video_id': 'qMb3ANIPN3Y'},
      {'author': 'LearnCargo',
       'channel': 'LearnCargo',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:33](https://www.youtube.com/watch?v=9AYrPh0PlLE&t=93s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "They'll give you a task that starts at 1:00 and you have 38 drop-offs. Uh they "
               "don't care how long it takes you to get it done. It needs to be done at "
               "appropriate time. I've seen people Excuse me. I've seen people take on work at "
               '1:00 p.',
       'timestamp': 93,
       'timestamp_label': '[00:01:33]',
       'timestamp_seconds': 93,
       'tip': "They'll give you a task that starts at 1:00 and you have 38 drop-offs. Uh they "
              "don't care how long it takes you to get it done. It needs to be done at "
              "appropriate time. I've seen people Excuse me. I've seen people take on work at "
              '1:00 p.',
       'title': 'Is Medical Courier Pay Worth It? (LearnCargo)',
       'url': 'https://www.youtube.com/watch?v=9AYrPh0PlLE&t=93s',
       'video_id': '9AYrPh0PlLE'},
      {'author': 'Giganomic Era',
       'channel': 'Giganomic Era',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:57](https://www.youtube.com/watch?v=2w9s8G4Gx9Q&t=357s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And please, get your paperwork right. Call your insurance agent before that '
               "driver moves one bag. 't cover a hired driver doing medical courier work. You "
               'need hired and non-owned coverage and or commercial coverage. And you also '
               'need to have that driver listed.',
       'timestamp': 357,
       'timestamp_label': '[00:05:57]',
       'timestamp_seconds': 357,
       'tip': 'And please, get your paperwork right. Call your insurance agent before that '
              "driver moves one bag. 't cover a hired driver doing medical courier work. You "
              'need hired and non-owned coverage and or commercial coverage. And you also need '
              'to have that driver listed.',
       'title': '“Hiring Your First Medical Courier Driver Without Losing Contracts ” '
                '(Giganomic Era)',
       'url': 'https://www.youtube.com/watch?v=2w9s8G4Gx9Q&t=357s',
       'video_id': '2w9s8G4Gx9Q'},
      {'author': 'MJ Business Academy',
       'channel': 'MJ Business Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:56](https://www.youtube.com/watch?v=aA7hgZoPF_Q&t=236s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Services that we offer it lets them know like hey this is everything that we '
               'can provide provide for our clients to provide them with a tailored experience '
               "right right it's almost like it's almost like a Build-A-Bear what's the "
               'Build-A-Bear.',
       'timestamp': 236,
       'timestamp_label': '[00:03:56]',
       'timestamp_seconds': 236,
       'tip': 'Services that we offer it lets them know like hey this is everything that we '
              'can provide provide for our clients to provide them with a tailored experience '
              "right right it's almost like it's almost like a Build-A-Bear what's the "
              'Build-A-Bear.',
       'title': 'Why Having a Rate Sheet is Crucial for Your NEMT Business (MJ Business '
                'Academy)',
       'url': 'https://www.youtube.com/watch?v=aA7hgZoPF_Q&t=236s',
       'video_id': 'aA7hgZoPF_Q'},
      {'author': 'Nemiton',
       'channel': 'Nemiton',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:03](https://www.youtube.com/watch?v=LjAb-IUYxbM&t=963s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'For managing multiple broker relationships without drowning in administrative '
               'work, RouteGenie has direct integrations with MTM, Modivcare, and Access2Care. '
               'They automate the billing that makes multi-broker operation actually '
               'manageable.',
       'timestamp': 963,
       'timestamp_label': '[00:16:03]',
       'timestamp_seconds': 963,
       'tip': 'For managing multiple broker relationships without drowning in administrative '
              'work, RouteGenie has direct integrations with MTM, Modivcare, and Access2Care. '
              'They automate the billing that makes multi-broker operation actually '
              'manageable.',
       'title': 'NEMT Broker Payment Models Explained: Fee-for-Service, Capitation, MCO & '
                'Hybrid (Nemiton)',
       'url': 'https://www.youtube.com/watch?v=LjAb-IUYxbM&t=963s',
       'video_id': 'LjAb-IUYxbM'},
      {'author': 'United Medical Transportation Providers Group',
       'channel': 'United Medical Transportation Providers Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:49](https://www.youtube.com/watch?v=PVivs9VOAyw&t=109s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Their version of strategy is, "Hey, here\'s my here\'s my call script. Would '
               'you like to purchase my call script?" Folks, if you think that this business '
               'and being able to build, grow, scale, and then sell at a future multiple.',
       'timestamp': 109,
       'timestamp_label': '[00:01:49]',
       'timestamp_seconds': 109,
       'tip': 'Their version of strategy is, "Hey, here\'s my here\'s my call script. Would '
              'you like to purchase my call script?" Folks, if you think that this business '
              'and being able to build, grow, scale, and then sell at a future multiple.',
       'title': 'These Hospitals are paying $6k per day to our Non-Emergency Medical '
                'Transportation Provider - Part 4 (United Medical Transportation Providers '
                'Group)',
       'url': 'https://www.youtube.com/watch?v=PVivs9VOAyw&t=109s',
       'video_id': 'PVivs9VOAyw'}],
 11: [{'author': 'Shantasia_RN',
       'channel': 'Shantasia_RN',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:38](https://www.youtube.com/watch?v=hS8ke40DMr4&t=158s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But commonly you will need a registered business an EIN, a business bank '
               'account, bookkeeping, appropriate licensing or permits, insurance, and any '
               'state broker or local approvals that apply. Keep personal and business money '
               'separate from the beginning.',
       'timestamp': 158,
       'timestamp_label': '[00:02:38]',
       'timestamp_seconds': 158,
       'tip': 'But commonly you will need a registered business an EIN, a business bank '
              'account, bookkeeping, appropriate licensing or permits, insurance, and any '
              'state broker or local approvals that apply. Keep personal and business money '
              'separate from the beginning.',
       'title': 'How to Start an NEMT Business: 8 Steps to Start Right (Shantasia_RN)',
       'url': 'https://www.youtube.com/watch?v=hS8ke40DMr4&t=158s',
       'video_id': 'hS8ke40DMr4'},
      {'author': 'Bambi',
       'channel': 'Bambi',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:03](https://www.youtube.com/watch?v=bGYVSmlvo90&t=63s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, we bought this company about five years ago. And when we bought it, it had '
               'ambulatory, wheelchair, and stretcher. And about 90% of the business was from '
               "brokers. Um, we did a whole bunch of math because I'm very analytical. I used "
               'to be private equity.',
       'timestamp': 63,
       'timestamp_label': '[00:01:03]',
       'timestamp_seconds': 63,
       'tip': 'So, we bought this company about five years ago. And when we bought it, it had '
              'ambulatory, wheelchair, and stretcher. And about 90% of the business was from '
              "brokers. Um, we did a whole bunch of math because I'm very analytical. I used "
              'to be private equity.',
       'title': '$2M/Year NEMT doing only stretcher/gurney hospital discharges | NEMT Experts '
                'Podcast Episode 72 (Bambi)',
       'url': 'https://www.youtube.com/watch?v=bGYVSmlvo90&t=63s',
       'video_id': 'bGYVSmlvo90'},
      {'author': 'ThatNEMTGirl',
       'channel': 'ThatNEMTGirl',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:11](https://www.youtube.com/watch?v=5gdeSbLFdzk&t=311s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Um, I have been scaling my own business for the past few years and so I'm back "
               'in a position now where I have a little bit more time. You know, my team is '
               'doing well. Um, we have we went through our scaling phase.',
       'timestamp': 311,
       'timestamp_label': '[00:05:11]',
       'timestamp_seconds': 311,
       'tip': "Um, I have been scaling my own business for the past few years and so I'm back "
              'in a position now where I have a little bit more time. You know, my team is '
              'doing well. Um, we have we went through our scaling phase.',
       'title': '5 Mistakes New NEMT Owners Make That Cost Them Thousands (ThatNEMTGirl)',
       'url': 'https://www.youtube.com/watch?v=5gdeSbLFdzk&t=311s',
       'video_id': '5gdeSbLFdzk'},
      {'author': 'Daeron Myers',
       'channel': 'Daeron Myers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:03](https://www.youtube.com/watch?v=bOb6m3Jtaqs&t=243s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "But as y'all can see, it's a lot of medical routes going on. And now is your "
               "time to to shift into being a medical carrier, okay? Where you're delivering "
               'pharmaceuticals, blood specimens, right? People are going to get sick. They '
               'are going to need care.',
       'timestamp': 243,
       'timestamp_label': '[00:04:03]',
       'timestamp_seconds': 243,
       'tip': "But as y'all can see, it's a lot of medical routes going on. And now is your "
              "time to to shift into being a medical carrier, okay? Where you're delivering "
              'pharmaceuticals, blood specimens, right? People are going to get sick. They are '
              'going to need care.',
       'title': 'How To Start A Medical Courier Business With No Experience (Step By Step) '
                '(Daeron Myers)',
       'url': 'https://www.youtube.com/watch?v=bOb6m3Jtaqs&t=243s',
       'video_id': 'bOb6m3Jtaqs'},
      {'author': 'Sarah Davis | The D&G Way',
       'channel': 'Sarah Davis | The D&G Way',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:27](https://www.youtube.com/watch?v=bzwpVnDnULQ&t=567s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, yes, level three can help you scale and grow, but it also requires a '
               "different level of maturity, responsibility, and management. Let's move on to "
               'level four. The prime contractor direct vendor level.',
       'timestamp': 567,
       'timestamp_label': '[00:09:27]',
       'timestamp_seconds': 567,
       'tip': 'So, yes, level three can help you scale and grow, but it also requires a '
              "different level of maturity, responsibility, and management. Let's move on to "
              'level four. The prime contractor direct vendor level.',
       'title': 'How To Start a Courier Business in 2026 | The 4 Levels Explained : The D&G '
                'Way️ (Sarah Davis | The D&G Way)',
       'url': 'https://www.youtube.com/watch?v=bzwpVnDnULQ&t=567s',
       'video_id': 'bzwpVnDnULQ'},
      {'author': 'RouteGenie',
       'channel': 'RouteGenie',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:22](https://www.youtube.com/watch?v=3Z74zrMSRtA&t=382s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Integration with business operations. Your NPI number should be integrated '
               'into all business documentation, contracts, insurance forms, marketing '
               'materials, and billing systems. This consistency prevents confusion and '
               'ensures smooth operations with all business partners.',
       'timestamp': 382,
       'timestamp_label': '[00:06:22]',
       'timestamp_seconds': 382,
       'tip': 'Integration with business operations. Your NPI number should be integrated into '
              'all business documentation, contracts, insurance forms, marketing materials, '
              'and billing systems. This consistency prevents confusion and ensures smooth '
              'operations with all business partners.',
       'title': 'NPI Number in Medical Transportation Explained: Benefits and Why Providers '
                'Need It (RouteGenie)',
       'url': 'https://www.youtube.com/watch?v=3Z74zrMSRtA&t=382s',
       'video_id': '3Z74zrMSRtA'},
      {'author': 'MONEY CENTRAL',
       'channel': 'MONEY CENTRAL',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:53](https://www.youtube.com/watch?v=GN6voRihdrc&t=173s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'It comes from switching from employee to independent contractor and building '
               'direct contracts with hospitals and transplant centers, cutting out the '
               'courier company or platform sitting in the middle, taking a cut.',
       'timestamp': 173,
       'timestamp_label': '[00:02:53]',
       'timestamp_seconds': 173,
       'tip': 'It comes from switching from employee to independent contractor and building '
              'direct contracts with hospitals and transplant centers, cutting out the courier '
              'company or platform sitting in the middle, taking a cut.',
       'title': 'How to Make $77,000/Year as a Medical Organ Courier! (Make money online!) '
                '(MONEY CENTRAL)',
       'url': 'https://www.youtube.com/watch?v=GN6voRihdrc&t=173s',
       'video_id': 'GN6voRihdrc'},
      {'author': 'Markie Williams Online Certification Courses',
       'channel': 'Markie Williams Online Certification Courses',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:31](https://www.youtube.com/watch?v=MyG3WwZsWlQ&t=91s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Trackpod strong for small to midsize couriers, offering robust pod and '
               'compliance features. Trackpod courier app allows you to manage all your '
               'deliveries and also collections.',
       'timestamp': 91,
       'timestamp_label': '[00:01:31]',
       'timestamp_seconds': 91,
       'tip': 'Trackpod strong for small to midsize couriers, offering robust pod and '
              'compliance features. Trackpod courier app allows you to manage all your '
              'deliveries and also collections.',
       'title': '4 Top Medical Courier Apps in 2026 (Markie Williams Online Certification '
                'Courses)',
       'url': 'https://www.youtube.com/watch?v=MyG3WwZsWlQ&t=91s',
       'video_id': 'MyG3WwZsWlQ'},
      {'author': 'Diamond Hunter Enterprises',
       'channel': 'Diamond Hunter Enterprises',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:06](https://www.youtube.com/watch?v=zQaL3OdQ2D8&t=546s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'My ultimate goal is for you to reach higher, think bigger, and better in '
               'scaling the medical career business. You will succeed in becoming the best '
               'medical courier amongst your competition.',
       'timestamp': 546,
       'timestamp_label': '[00:09:06]',
       'timestamp_seconds': 546,
       'tip': 'My ultimate goal is for you to reach higher, think bigger, and better in '
              'scaling the medical career business. You will succeed in becoming the best '
              'medical courier amongst your competition.',
       'title': 'How to Become a Medical Courier in 5 Easy Steps in 2026 (Diamond Hunter '
                'Enterprises)',
       'url': 'https://www.youtube.com/watch?v=zQaL3OdQ2D8&t=546s',
       'video_id': 'zQaL3OdQ2D8'},
      {'author': 'Nemt University',
       'channel': 'Nemt University',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:51](https://www.youtube.com/watch?v=VGWUx-p8MbM&t=771s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Um, having that ability to have have th those uh vehicles to offer those type '
               "of services in your business is imperial. You know what I'm talking about? "
               'Especially if you want to scale.',
       'timestamp': 771,
       'timestamp_label': '[00:12:51]',
       'timestamp_seconds': 771,
       'tip': 'Um, having that ability to have have th those uh vehicles to offer those type '
              "of services in your business is imperial. You know what I'm talking about? "
              'Especially if you want to scale.',
       'title': 'Don’t Buy a Wheelchair Van Until You WATCH THIS!!! | NEMT University | 2025 '
                '(Nemt University)',
       'url': 'https://www.youtube.com/watch?v=VGWUx-p8MbM&t=771s',
       'video_id': 'VGWUx-p8MbM'},
      {'author': 'Giganomic Era',
       'channel': 'Giganomic Era',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:03](https://www.youtube.com/watch?v=7k3sVGSbmRA&t=63s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "On Track Transport, you don't have to worry about that. You work as a 1099 "
               'independent contractor. You set your own schedule, use your own vehicle, and '
               "you're responsible for your own taxes. On Track operates through regional "
               'hubs.',
       'timestamp': 63,
       'timestamp_label': '[00:01:03]',
       'timestamp_seconds': 63,
       'tip': "On Track Transport, you don't have to worry about that. You work as a 1099 "
              'independent contractor. You set your own schedule, use your own vehicle, and '
              "you're responsible for your own taxes. On Track operates through regional hubs.",
       'title': 'Medical Courier Jobs With No Experience 4 Companies to Try in 2026 (Giganomic '
                'Era)',
       'url': 'https://www.youtube.com/watch?v=7k3sVGSbmRA&t=63s',
       'video_id': '7k3sVGSbmRA'},
      {'author': 'United Medical Transportation Providers Group',
       'channel': 'United Medical Transportation Providers Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:08](https://www.youtube.com/watch?v=Bvcsc1hEgT0&t=68s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I won't bore you with all of our experiences in the past with brokers but "
               "we've done a lot of pulling together and unifying of providers to battle the "
               'brokers and I love it one of my greatest.',
       'timestamp': 68,
       'timestamp_label': '[00:01:08]',
       'timestamp_seconds': 68,
       'tip': "I won't bore you with all of our experiences in the past with brokers but we've "
              'done a lot of pulling together and unifying of providers to battle the brokers '
              'and I love it one of my greatest.',
       'title': 'NEMT Provider?  Dealing with Brokers?  This is a MUST See! (United Medical '
                'Transportation Providers Group)',
       'url': 'https://www.youtube.com/watch?v=Bvcsc1hEgT0&t=68s',
       'video_id': 'Bvcsc1hEgT0'},
      {'author': 'LearnCargo',
       'channel': 'LearnCargo',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=7vzx8bJpxUE&t=20s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "The wage wasn't bad at all. I made roughly around $300 a day. My day consisted "
               "of maybe 6:00 a. Which was only like 4 or 4 and 1/2 hours. But there's a lot "
               'of work involved. I actually had to go to the warehouse.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': "The wage wasn't bad at all. I made roughly around $300 a day. My day consisted "
              "of maybe 6:00 a. Which was only like 4 or 4 and 1/2 hours. But there's a lot of "
              'work involved. I actually had to go to the warehouse.',
       'title': '$300 a Day with a Box Truck Medical Courier Contract (LearnCargo)',
       'url': 'https://www.youtube.com/watch?v=7vzx8bJpxUE&t=20s',
       'video_id': '7vzx8bJpxUE'},
      {'author': 'JT Automations',
       'channel': 'JT Automations',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:40](https://www.youtube.com/watch?v=dHKhNi-IC-0&t=700s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'They get paid per trip billing and of course the numbers will vary per ride '
               'depending on the type, the volume game, which is how many rides a day you can '
               "do, and the scale driver. So, in the drivers you hire, you don't necessarily "
               'got to provide them with the vehicle.',
       'timestamp': 700,
       'timestamp_label': '[00:11:40]',
       'timestamp_seconds': 700,
       'tip': 'They get paid per trip billing and of course the numbers will vary per ride '
              'depending on the type, the volume game, which is how many rides a day you can '
              "do, and the scale driver. So, in the drivers you hire, you don't necessarily "
              'got to provide them with the vehicle.',
       'title': 'How to Start a Non-Emergency Medical Transportation Company in 2026 (NEMT '
                'Business) (JT Automations)',
       'url': 'https://www.youtube.com/watch?v=dHKhNi-IC-0&t=700s',
       'video_id': 'dHKhNi-IC-0'},
      {'author': 'Diamond Hunter Enterprises',
       'channel': 'Diamond Hunter Enterprises',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:25](https://www.youtube.com/watch?v=jyu_AIm5pAw&t=565s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Check their website for details. Remember, this is an opportunity to earn '
               '$1,500 plus daily building your medical courier business as a flexible '
               'independent contractor. Jewels, you can grab these high-paying opportunities '
               'while managing your own schedule.',
       'timestamp': 565,
       'timestamp_label': '[00:09:25]',
       'timestamp_seconds': 565,
       'tip': 'Check their website for details. Remember, this is an opportunity to earn '
              '$1,500 plus daily building your medical courier business as a flexible '
              'independent contractor. Jewels, you can grab these high-paying opportunities '
              'while managing your own schedule.',
       'title': 'Find FIRST Courier Contract Jobs in Your Car 2026 | 3 Medical Courier & '
                'Driver Certifications (Diamond Hunter Enterprises)',
       'url': 'https://www.youtube.com/watch?v=jyu_AIm5pAw&t=565s',
       'video_id': 'jyu_AIm5pAw'}],
 12: [{'author': 'Giganomic Era',
       'channel': 'Giganomic Era',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:06](https://www.youtube.com/watch?v=YV5-h4wgh4Q&t=306s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'This route pays me $2,620 per month running 5 days a week. That breaks down to '
               'about $131 per day. And this is for only one pickup and one drop-off per day. '
               'The second client was completely different.',
       'timestamp': 306,
       'timestamp_label': '[00:05:06]',
       'timestamp_seconds': 306,
       'tip': 'This route pays me $2,620 per month running 5 days a week. That breaks down to '
              'about $131 per day. And this is for only one pickup and one drop-off per day. '
              'The second client was completely different.',
       'title': '"I Made $195 in 70 Minutes with Medical Courier Contracts No Apps Needed" '
                '(Giganomic Era)',
       'url': 'https://www.youtube.com/watch?v=YV5-h4wgh4Q&t=306s',
       'video_id': 'YV5-h4wgh4Q'},
      {'author': 'Sarah Davis | The D&G Way',
       'channel': 'Sarah Davis | The D&G Way',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:20](https://www.youtube.com/watch?v=XX29XpCCZO4&t=200s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "This is another medical courier independent contractor opportunity. They're "
               'advertising around $200 to $500 per day. That can come out to approximately '
               "$1,000 to $2,500 per week if you're working 5 days and roughly $4,000 to "
               '$10,000 per month based on 4 weeks.',
       'timestamp': 200,
       'timestamp_label': '[00:03:20]',
       'timestamp_seconds': 200,
       'tip': "This is another medical courier independent contractor opportunity. They're "
              'advertising around $200 to $500 per day. That can come out to approximately '
              "$1,000 to $2,500 per week if you're working 5 days and roughly $4,000 to "
              '$10,000 per month based on 4 weeks.',
       'title': 'Make up to $3,500 / Week as Medical Courier Today with These 10 Companies '
                'Hiring Now | Any Vehicle (Sarah Davis | The D&G Way)',
       'url': 'https://www.youtube.com/watch?v=XX29XpCCZO4&t=200s',
       'video_id': 'XX29XpCCZO4'},
      {'author': 'My Business Vibe 9',
       'channel': 'My Business Vibe 9',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:09](https://www.youtube.com/watch?v=mm9doNupm1k&t=249s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, you want to be confident. You want to show them that you're confident, "
               "that you know what you're doing, so they can trust you with these supplies. "
               'So, if you start submitting an online application, follow up that day with a '
               'phone call.',
       'timestamp': 249,
       'timestamp_label': '[00:04:09]',
       'timestamp_seconds': 249,
       'tip': "So, you want to be confident. You want to show them that you're confident, that "
              "you know what you're doing, so they can trust you with these supplies. So, if "
              'you start submitting an online application, follow up that day with a phone '
              'call.',
       'title': 'Easy Steps To Land Your First Medical Courier Contract (My Business Vibe 9)',
       'url': 'https://www.youtube.com/watch?v=mm9doNupm1k&t=249s',
       'video_id': 'mm9doNupm1k'},
      {'author': 'Motivational Charles',
       'channel': 'Motivational Charles',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:35](https://www.youtube.com/watch?v=BCwbkTt30cY&t=35s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Uh Trillium Sand Hills the managed care plan is what they call PHP all your '
               'private insurance companies that deals with Medicaid now they got Medicaid '
               "recipients now that's going to be United what is United uh healthy blue uh a "
               'mirror house.',
       'timestamp': 35,
       'timestamp_label': '[00:00:35]',
       'timestamp_seconds': 35,
       'tip': 'Uh Trillium Sand Hills the managed care plan is what they call PHP all your '
              'private insurance companies that deals with Medicaid now they got Medicaid '
              "recipients now that's going to be United what is United uh healthy blue uh a "
              'mirror house.',
       'title': 'Modivcare To Soon Take Over Most Of Medicaid NEMT in NC #NEMT #transportation '
                '(Motivational Charles)',
       'url': 'https://www.youtube.com/watch?v=BCwbkTt30cY&t=35s',
       'video_id': 'BCwbkTt30cY'},
      {'author': 'Diamond Hunter Enterprises',
       'channel': 'Diamond Hunter Enterprises',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:39](https://www.youtube.com/watch?v=rPBtFcgIPmQ&t=519s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Make sure you click every day of the week, 7 days a week until you're hired on "
               'to provide dedicated routes on demand or stat routes, Jewels. Click you '
               'confirm and done. The last company is American Logistics.',
       'timestamp': 519,
       'timestamp_label': '[00:08:39]',
       'timestamp_seconds': 519,
       'tip': "Make sure you click every day of the week, 7 days a week until you're hired on "
              'to provide dedicated routes on demand or stat routes, Jewels. Click you confirm '
              'and done. The last company is American Logistics.',
       'title': '4 Medical Courier Independent Contractor Companies Hiring in 2026 |This How '
                'Drivers Get Contracts! (Diamond Hunter Enterprises)',
       'url': 'https://www.youtube.com/watch?v=rPBtFcgIPmQ&t=519s',
       'video_id': 'rPBtFcgIPmQ'},
      {'author': 'Sarah Davis | The D&G Way',
       'channel': 'Sarah Davis | The D&G Way',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:27:33](https://www.youtube.com/watch?v=BMVHyfV5TC8&t=1653s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Because that is what separates people who stay stuck from people who actually '
               'start building a real business. Do not talk yourself out of this just because '
               "you don't have a van yet. Do not talk yourself out of this because you're not "
               'at level four yet.',
       'timestamp': 1653,
       'timestamp_label': '[00:27:33]',
       'timestamp_seconds': 1653,
       'tip': 'Because that is what separates people who stay stuck from people who actually '
              'start building a real business. Do not talk yourself out of this just because '
              "you don't have a van yet. Do not talk yourself out of this because you're not "
              'at level four yet.',
       'title': 'How To Get Your First Courier Contract With Your Car in 2026 (Step by Step) '
                '(Sarah Davis | The D&G Way)',
       'url': 'https://www.youtube.com/watch?v=BMVHyfV5TC8&t=1653s',
       'video_id': 'BMVHyfV5TC8'},
      {'author': 'RouteGenie',
       'channel': 'RouteGenie',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:48](https://www.youtube.com/watch?v=qceSg9X8F0E&t=408s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Adult day care etc leave your marketing materials there and try to set long '
               "lasting relationships with these organizations that's how you'll be able.",
       'timestamp': 408,
       'timestamp_label': '[00:06:48]',
       'timestamp_seconds': 408,
       'tip': 'Adult day care etc leave your marketing materials there and try to set long '
              "lasting relationships with these organizations that's how you'll be able.",
       'title': 'NEMT Rates: Is a NEMT Business Profitable? | NEMT Business Educational Videos '
                '| RouteGenie (RouteGenie)',
       'url': 'https://www.youtube.com/watch?v=qceSg9X8F0E&t=408s',
       'video_id': 'qceSg9X8F0E'},
      {'author': 'Samuel B.',
       'channel': 'Samuel B.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:54](https://www.youtube.com/watch?v=X99grw6uMuY&t=294s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Hours plus making 2500 a week is almost impossible if everything lines up I '
               'can make three hundred dollars a day and this other driver says I make three.',
       'timestamp': 294,
       'timestamp_label': '[00:04:54]',
       'timestamp_seconds': 294,
       'tip': 'Hours plus making 2500 a week is almost impossible if everything lines up I can '
              'make three hundred dollars a day and this other driver says I make three.',
       'title': 'The TRUTH About Being An Independent Medical Courier. (Samuel B.)',
       'url': 'https://www.youtube.com/watch?v=X99grw6uMuY&t=294s',
       'video_id': 'X99grw6uMuY'},
      {'author': 'MJ Business Academy',
       'channel': 'MJ Business Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:39](https://www.youtube.com/watch?v=LCV7CgKI3PQ&t=819s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "The link to schedule the discovery call so it's nothing personal but usually "
               'during the day we are working working with facilities no we booked and busy '
               "let's keep it real quick and busy boo.",
       'timestamp': 819,
       'timestamp_label': '[00:13:39]',
       'timestamp_seconds': 819,
       'tip': "The link to schedule the discovery call so it's nothing personal but usually "
              'during the day we are working working with facilities no we booked and busy '
              "let's keep it real quick and busy boo.",
       'title': 'How to Get Contracts l Non-Emergency Medical Transportation (MJ Business '
                'Academy)',
       'url': 'https://www.youtube.com/watch?v=LCV7CgKI3PQ&t=819s',
       'video_id': 'LCV7CgKI3PQ'},
      {'author': 'Pedro “Mr.BetonYou” Santiago',
       'channel': 'Pedro “Mr.BetonYou” Santiago',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:06](https://www.youtube.com/watch?v=BhO0ZqkVHFk&t=306s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Obstacles now in the app you got to get signatures for all of these actually '
               'on the packages is actually said name they had their name the address '
               'everything match with what the app said signature.',
       'timestamp': 306,
       'timestamp_label': '[00:05:06]',
       'timestamp_seconds': 306,
       'tip': 'Obstacles now in the app you got to get signatures for all of these actually on '
              'the packages is actually said name they had their name the address everything '
              'match with what the app said signature.',
       'title': 'My First Day as a Medical Courier Delivery Driver: How Much Can You Make '
                '(Pedro “Mr.BetonYou” Santiago)',
       'url': 'https://www.youtube.com/watch?v=BhO0ZqkVHFk&t=306s',
       'video_id': 'BhO0ZqkVHFk'},
      {'author': 'Side Hustle 247',
       'channel': 'Side Hustle 247',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:46](https://www.youtube.com/watch?v=NjZBEatuBlc&t=406s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Know if you've done work for them I'd love to hear from you and hit that "
               'thumbs up thank you as always you guys are awesome and have a great day peace.',
       'timestamp': 406,
       'timestamp_label': '[00:06:46]',
       'timestamp_seconds': 406,
       'tip': "Know if you've done work for them I'd love to hear from you and hit that thumbs "
              'up thank you as always you guys are awesome and have a great day peace.',
       'title': 'Part Time Medical Courier | $230-$300 Per Day!!! #medicalcourier #courier '
                '#independentcourier (Side Hustle 247)',
       'url': 'https://www.youtube.com/watch?v=NjZBEatuBlc&t=406s',
       'video_id': 'NjZBEatuBlc'},
      {'author': 'RouteGenie',
       'channel': 'RouteGenie',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:27](https://www.youtube.com/watch?v=qiZqLls0G-E&t=327s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Ending your shift with a well-maintained vehicle helps ensure you're ready for "
               "the next day's challenges. Finding qualified drivers is the first step in "
               'building a reliable NMT business.',
       'timestamp': 327,
       'timestamp_label': '[00:05:27]',
       'timestamp_seconds': 327,
       'tip': "Ending your shift with a well-maintained vehicle helps ensure you're ready for "
              "the next day's challenges. Finding qualified drivers is the first step in "
              'building a reliable NMT business.',
       'title': 'A Day in Life of NEMT Driver: Schedule, Responsibilities, and Routine '
                '(RouteGenie)',
       'url': 'https://www.youtube.com/watch?v=qiZqLls0G-E&t=327s',
       'video_id': 'qiZqLls0G-E'},
      {'author': 'Nemt University',
       'channel': 'Nemt University',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:51](https://www.youtube.com/watch?v=irqJHXZq5K8&t=531s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Consultation guess what we available for consultations as well um but we're "
               'going to try to turn this into overdrive 2025 see how many providers can get '
               'out here on the road say l.',
       'timestamp': 531,
       'timestamp_label': '[00:08:51]',
       'timestamp_seconds': 531,
       'tip': "Consultation guess what we available for consultations as well um but we're "
              'going to try to turn this into overdrive 2025 see how many providers can get '
              'out here on the road say l.',
       'title': 'Should I START 🚘AMBULATORY or WHEELCHAIR ♿️ NEMT BUSINESS 2025 edition… (Nemt '
                'University)',
       'url': 'https://www.youtube.com/watch?v=irqJHXZq5K8&t=531s',
       'video_id': 'irqJHXZq5K8'},
      {'author': 'Nemiton',
       'channel': 'Nemiton',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:00](https://www.youtube.com/watch?v=w246jND2Ahw&t=180s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The application is free through NPPES, but it takes 10 to 15 business days to '
               "process. That's why you need to start this immediately because every day "
               "without your NPI is a day you can't get broker contracts. Now, state "
               'requirements vary dramatically.',
       'timestamp': 180,
       'timestamp_label': '[00:03:00]',
       'timestamp_seconds': 180,
       'tip': 'The application is free through NPPES, but it takes 10 to 15 business days to '
              "process. That's why you need to start this immediately because every day "
              "without your NPI is a day you can't get broker contracts. Now, state "
              'requirements vary dramatically.',
       'title': '15 Steps to Start a NEMT Business (Complete 2026 Walkthrough) (Nemiton)',
       'url': 'https://www.youtube.com/watch?v=w246jND2Ahw&t=180s',
       'video_id': 'w246jND2Ahw'},
      {'author': 'Leelah The Entrepreneur',
       'channel': 'Leelah The Entrepreneur',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:35](https://www.youtube.com/watch?v=UUrhf6VurIA&t=335s)',
       'relevance': "Attributed practitioner commentary on Medicaid/workers'-comp `NEMT` TPA "
                    'standing orders, `CLIA`/`HIPAA` `STAT` lab specimen routes, and '
                    'asset-light 1099 owner-operator dispatch brokerage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I think it was like the seventh or eighth day. I was like hmm so all I needed '
               'was to just be consistent for seven days and apply for 25. The next week I was '
               'doing 40 to 50 per day.',
       'timestamp': 335,
       'timestamp_label': '[00:05:35]',
       'timestamp_seconds': 335,
       'tip': 'I think it was like the seventh or eighth day. I was like hmm so all I needed '
              'was to just be consistent for seven days and apply for 25. The next week I was '
              'doing 40 to 50 per day.',
       'title': 'How I Made $9,235 in 21 Days as a Medical Courier | How to Get Started '
                '(Leelah The Entrepreneur)',
       'url': 'https://www.youtube.com/watch?v=UUrhf6VurIA&t=335s',
       'video_id': 'UUrhf6VurIA'}]}
