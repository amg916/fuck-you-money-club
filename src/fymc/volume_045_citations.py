"""Curated 180-citation No Surprises Act (IDR) Medical Arbitration & Out-of-Network Recovery baseline (15 per chapter across Q1-Q12) mined strictly from verified No Surprises Act (IDR) Medical Arbitration & Out-of-Network Recovery YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'835',
     'above',
     'act',
     'acuity',
     'adding',
     'administrative',
     'after',
     'against',
     'agreement',
     'air',
     'ambulance',
     'amount',
     'anesthesia',
     'api',
     'arbitration',
     'asc',
     'assist',
     'associate',
     'association',
     'auditing',
     'automating',
     'automation',
     'avoiding',
     'award',
     'awards',
     'baa',
     'baseball',
     'based',
     'batching',
     'behavioral',
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
 2: {'835',
     'above',
     'act',
     'acuity',
     'adding',
     'administrative',
     'after',
     'against',
     'agreement',
     'air',
     'ambulance',
     'amount',
     'anesthesia',
     'api',
     'arbitration',
     'asc',
     'assist',
     'associate',
     'association',
     'auditing',
     'automating',
     'automation',
     'avoiding',
     'award',
     'awards',
     'baa',
     'baseball',
     'based',
     'batching',
     'behavioral',
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
 3: {'835',
     'above',
     'act',
     'acuity',
     'adding',
     'administrative',
     'after',
     'against',
     'agreement',
     'air',
     'ambulance',
     'amount',
     'anesthesia',
     'api',
     'arbitration',
     'asc',
     'assist',
     'associate',
     'association',
     'auditing',
     'automating',
     'automation',
     'avoiding',
     'award',
     'awards',
     'baa',
     'baseball',
     'based',
     'batching',
     'behavioral',
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
 4: {'835',
     'above',
     'act',
     'acuity',
     'adding',
     'administrative',
     'after',
     'against',
     'agreement',
     'air',
     'ambulance',
     'amount',
     'anesthesia',
     'api',
     'arbitration',
     'asc',
     'assist',
     'associate',
     'association',
     'auditing',
     'automating',
     'automation',
     'avoiding',
     'award',
     'awards',
     'baa',
     'baseball',
     'based',
     'batching',
     'behavioral',
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
 5: {'835',
     'above',
     'act',
     'acuity',
     'adding',
     'administrative',
     'after',
     'against',
     'agreement',
     'air',
     'ambulance',
     'amount',
     'anesthesia',
     'api',
     'arbitration',
     'asc',
     'assist',
     'associate',
     'association',
     'audit',
     'auditing',
     'automating',
     'automation',
     'avoid',
     'avoiding',
     'award',
     'awards',
     'baa',
     'baseball',
     'based',
     'batching',
     'behavioral',
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
 6: {'835',
     'above',
     'act',
     'acuity',
     'adding',
     'administrative',
     'after',
     'against',
     'agreement',
     'air',
     'ambulance',
     'amount',
     'anesthesia',
     'api',
     'arbitration',
     'asc',
     'assist',
     'associate',
     'association',
     'auditing',
     'automating',
     'automation',
     'avoiding',
     'award',
     'awards',
     'baa',
     'baseball',
     'based',
     'batching',
     'behavioral',
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
 7: {'835',
     'above',
     'act',
     'acuity',
     'adding',
     'administrative',
     'after',
     'against',
     'agreement',
     'air',
     'ambulance',
     'amount',
     'anesthesia',
     'api',
     'arbitration',
     'asc',
     'assist',
     'associate',
     'association',
     'auditing',
     'automating',
     'automation',
     'avoiding',
     'award',
     'awards',
     'baa',
     'baseball',
     'based',
     'batching',
     'behavioral',
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
 8: {'835',
     'above',
     'act',
     'acuity',
     'adding',
     'administrative',
     'after',
     'against',
     'agreement',
     'air',
     'ambulance',
     'amount',
     'anesthesia',
     'api',
     'arbitration',
     'asc',
     'assist',
     'associate',
     'association',
     'auditing',
     'automating',
     'automation',
     'avoiding',
     'award',
     'awards',
     'baa',
     'baseball',
     'based',
     'batching',
     'behavioral',
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
 9: {'835',
     'above',
     'act',
     'acuity',
     'adding',
     'administrative',
     'after',
     'against',
     'agreement',
     'air',
     'ambulance',
     'amount',
     'anesthesia',
     'api',
     'arbitration',
     'asc',
     'assist',
     'associate',
     'association',
     'auditing',
     'automating',
     'automation',
     'avoiding',
     'award',
     'awards',
     'baa',
     'baseball',
     'based',
     'batching',
     'behavioral',
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
 10: {'835',
      'above',
      'act',
      'acuity',
      'adding',
      'administrative',
      'after',
      'against',
      'agent',
      'agreement',
      'ai',
      'air',
      'ambulance',
      'amount',
      'anesthesia',
      'api',
      'arbitration',
      'asc',
      'assist',
      'associate',
      'association',
      'auditing',
      'automate',
      'automating',
      'automation',
      'avoiding',
      'award',
      'awards',
      'baa',
      'baseball',
      'based',
      'batching',
      'behavioral',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'835',
      'above',
      'act',
      'acuity',
      'adding',
      'administrative',
      'after',
      'against',
      'agreement',
      'air',
      'ambulance',
      'amount',
      'anesthesia',
      'api',
      'arbitration',
      'asc',
      'assist',
      'associate',
      'association',
      'auditing',
      'automating',
      'automation',
      'avoiding',
      'award',
      'awards',
      'baa',
      'baseball',
      'based',
      'batching',
      'behavioral',
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
 12: {'835',
      'above',
      'act',
      'action',
      'acuity',
      'adding',
      'administrative',
      'after',
      'against',
      'agreement',
      'air',
      'ambulance',
      'amount',
      'anesthesia',
      'api',
      'arbitration',
      'asc',
      'assist',
      'associate',
      'association',
      'auditing',
      'automating',
      'automation',
      'avoiding',
      'award',
      'awards',
      'baa',
      'baseball',
      'based',
      'batching',
      'behavioral',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'MedConsults',
      'channel': 'MedConsults',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:01](https://www.youtube.com/watch?v=YlcvgGZT9eQ&t=1201s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Automation and analytics are finally viable at scale. Value-based care ties '
              'reimbursement increasingly to outcomes and cost reduction. Eliminating '
              'administrative waste frees capital to reinvest in care itself.',
      'timestamp': 1201,
      'timestamp_label': '[00:20:01]',
      'timestamp_seconds': 1201,
      'tip': 'Automation and analytics are finally viable at scale. Value-based care ties '
             'reimbursement increasingly to outcomes and cost reduction. Eliminating '
             'administrative waste frees capital to reinvest in care itself.',
      'title': 'Revenue Cycle Management in Healthcare (Full Course) (MedConsults)',
      'url': 'https://www.youtube.com/watch?v=YlcvgGZT9eQ&t=1201s',
      'video_id': 'YlcvgGZT9eQ'},
     {'author': 'Radiology Partners',
      'channel': 'Radiology Partners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:01](https://www.youtube.com/watch?v=q1qFNKqrEcs&t=241s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And the first one was benchmarking. The idea of benchmarking was really, how '
              'are we going to value that service? Well, people were quickly moved off using '
              'Medicare as a benchmark. Medicare is not a market based rate, nor was it '
              'intended to be a market based rate.',
      'timestamp': 241,
      'timestamp_label': '[00:04:01]',
      'timestamp_seconds': 241,
      'tip': 'And the first one was benchmarking. The idea of benchmarking was really, how are '
             'we going to value that service? Well, people were quickly moved off using '
             'Medicare as a benchmark. Medicare is not a market based rate, nor was it '
             'intended to be a market based rate.',
      'title': 'Part 1 - Surprise Medical Billing & The No Surprises Act: More Surprises Than '
               "You'd Think (Radiology Partners)",
      'url': 'https://www.youtube.com/watch?v=q1qFNKqrEcs&t=241s',
      'video_id': 'q1qFNKqrEcs'},
     {'author': 'CMSHHSgov',
      'channel': 'CMSHHSgov',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:39](https://www.youtube.com/watch?v=Sp7aK2UsmlE&t=1479s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Geraldine Doetzer: For air ambulance services that are furnished during 2023 or '
              'a subsequent year using the service codes on the slide.',
      'timestamp': 1479,
      'timestamp_label': '[00:24:39]',
      'timestamp_seconds': 1479,
      'tip': 'Geraldine Doetzer: For air ambulance services that are furnished during 2023 or '
             'a subsequent year using the service codes on the slide.',
      'title': 'No Surprises Act: Qualifying Payment Amount Calculation Methodology '
               '(CMSHHSgov)',
      'url': 'https://www.youtube.com/watch?v=Sp7aK2UsmlE&t=1479s',
      'video_id': 'Sp7aK2UsmlE'},
     {'author': 'Apex IONM Solutions',
      'channel': 'Apex IONM Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:08](https://www.youtube.com/watch?v=QRrun6dHMIY&t=308s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re they're going to price it according to the average in network amount for "
              'that service. But then you can push back on that. You can say, "Hey, this '
              'amount is too low. " And the insurance company has to negotiate with you or be '
              'pushed into an arbitration setting.',
      'timestamp': 308,
      'timestamp_label': '[00:05:08]',
      'timestamp_seconds': 308,
      'tip': "'re they're going to price it according to the average in network amount for "
             'that service. But then you can push back on that. You can say, "Hey, this amount '
             'is too low. " And the insurance company has to negotiate with you or be pushed '
             'into an arbitration setting.',
      'title': 'Unlocking Hidden Revenue: The No Surprises Act Strategy Providers Are Missing '
               '(Apex IONM Solutions)',
      'url': 'https://www.youtube.com/watch?v=QRrun6dHMIY&t=308s',
      'video_id': 'QRrun6dHMIY'},
     {'author': 'Medical Billing Education | Behavioral Billing',
      'channel': 'Medical Billing Education | Behavioral Billing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:08](https://www.youtube.com/watch?v=yYlBBM1kBMU&t=248s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "She might have to stop coming altogether. This isn't just a client's problem. "
              "It's a threat to your practice's cash flow. Cash flow is the movement of money "
              "into and out of your business. If your clients can't afford to continue care, "
              'your income becomes unstable.',
      'timestamp': 248,
      'timestamp_label': '[00:04:08]',
      'timestamp_seconds': 248,
      'tip': "She might have to stop coming altogether. This isn't just a client's problem. "
             "It's a threat to your practice's cash flow. Cash flow is the movement of money "
             "into and out of your business. If your clients can't afford to continue care, "
             'your income becomes unstable.',
      'title': 'The Hidden Costs of Your Out-of-Network Behavioral Health Practice (Medical '
               'Billing Education | Behavioral Billing)',
      'url': 'https://www.youtube.com/watch?v=yYlBBM1kBMU&t=248s',
      'video_id': 'yYlBBM1kBMU'},
     {'author': 'Outpatient Endovascular & Interventional Society',
      'channel': 'Outpatient Endovascular & Interventional Society',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:00:05](https://www.youtube.com/watch?v=5aFK91a1KPY&t=3605s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I was talking to had no clue what value-based care was. And then higher patient '
              'satisfaction, long-term follow-up care. Many times people leave the hospital '
              'after procedure and their they may not get any follow-up. And then little '
              'things like free parking.',
      'timestamp': 3605,
      'timestamp_label': '[01:00:05]',
      'timestamp_seconds': 3605,
      'tip': 'I was talking to had no clue what value-based care was. And then higher patient '
             'satisfaction, long-term follow-up care. Many times people leave the hospital '
             'after procedure and their they may not get any follow-up. And then little things '
             'like free parking.',
      'title': 'Revenue Cycle for OBLs: Payer Contracts, 2026 Coding and Denials | OEIS Annual '
               'Meeting (Outpatient Endovascular & Interventional Society)',
      'url': 'https://www.youtube.com/watch?v=5aFK91a1KPY&t=3605s',
      'video_id': '5aFK91a1KPY'},
     {'author': 'CMSHHSgov',
      'channel': 'CMSHHSgov',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:53](https://www.youtube.com/watch?v=7lzQt8aAlG0&t=1433s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And there are specific rules that must be filed in order for a party to batch '
              'items and services together. So, the first is that they must be billed by the '
              'same provider or group of providers, or the same facility or the same provider '
              'of air ambulance service.',
      'timestamp': 1433,
      'timestamp_label': '[00:23:53]',
      'timestamp_seconds': 1433,
      'tip': 'And there are specific rules that must be filed in order for a party to batch '
             'items and services together. So, the first is that they must be billed by the '
             'same provider or group of providers, or the same facility or the same provider '
             'of air ambulance service.',
      'title': 'An Overview of the Independent Dispute Resolution Process for Disputing '
               'Parties, Part II (CMSHHSgov)',
      'url': 'https://www.youtube.com/watch?v=7lzQt8aAlG0&t=1433s',
      'video_id': '7lzQt8aAlG0'},
     {'author': 'FOX 26 Houston',
      'channel': 'FOX 26 Houston',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=9dOW3txIHG0&t=98s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Urgent care facilities are not included unless the facilities licensed for '
              'emergency care If your doctor sends your test results to an out of network lab '
              ', the lab can still balanced bill. You Also very important is ground ambulance '
              'service.',
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': 'Urgent care facilities are not included unless the facilities licensed for '
             'emergency care If your doctor sends your test results to an out of network lab , '
             'the lab can still balanced bill. You Also very important is ground ambulance '
             'service.',
      'title': 'Loopholes in No Surprises Act can leave some patients with high bills (FOX 26 '
               'Houston)',
      'url': 'https://www.youtube.com/watch?v=9dOW3txIHG0&t=98s',
      'video_id': '9dOW3txIHG0'},
     {'author': 'Reimbursify',
      'channel': 'Reimbursify',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:47](https://www.youtube.com/watch?v=of48SgwvfiI&t=647s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Not required on that type of service but if you jump down two sections here '
              'applied behavioral analysis you can see that this does require '
              'pre-authorization.',
      'timestamp': 647,
      'timestamp_label': '[00:10:47]',
      'timestamp_seconds': 647,
      'tip': 'Not required on that type of service but if you jump down two sections here '
             'applied behavioral analysis you can see that this does require '
             'pre-authorization.',
      'title': 'Benefit Verifications 101 - Let your clients check their own out-of-network '
               'coverage! (Reimbursify)',
      'url': 'https://www.youtube.com/watch?v=of48SgwvfiI&t=647s',
      'video_id': 'of48SgwvfiI'},
     {'author': 'Practical Data Solutions - Healthcare Analytics',
      'channel': 'Practical Data Solutions - Healthcare Analytics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:32](https://www.youtube.com/watch?v=4SW5Ihdk8ps&t=512s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Succeed under value-based contracts a big area that i think we're going to get "
              "into in a little bit is around the risk scoring it's around hcc capture.",
      'timestamp': 512,
      'timestamp_label': '[00:08:32]',
      'timestamp_seconds': 512,
      'tip': "Succeed under value-based contracts a big area that i think we're going to get "
             "into in a little bit is around the risk scoring it's around hcc capture.",
      'title': '5 Best Practices of Revenue Cycle Analytics and Denials Management (Practical '
               'Data Solutions - Healthcare Analytics)',
      'url': 'https://www.youtube.com/watch?v=4SW5Ihdk8ps&t=512s',
      'video_id': '4SW5Ihdk8ps'},
     {'author': 'Private Practice Skills',
      'channel': 'Private Practice Skills',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:01](https://www.youtube.com/watch?v=JT1pxEvMFxw&t=421s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Because there's no way of guaranteeing that our clients are actually going to "
              'submit that out of network super bill now once a new client or an existing.',
      'timestamp': 421,
      'timestamp_label': '[00:07:01]',
      'timestamp_seconds': 421,
      'tip': "Because there's no way of guaranteeing that our clients are actually going to "
             'submit that out of network super bill now once a new client or an existing.',
      'title': 'How the No Surprises Act Impacts your Practice | Good Faith Estimate (Private '
               'Practice Skills)',
      'url': 'https://www.youtube.com/watch?v=JT1pxEvMFxw&t=421s',
      'video_id': 'JT1pxEvMFxw'},
     {'author': 'IDR Law',
      'channel': 'IDR Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:59](https://www.youtube.com/watch?v=ikQ6l3STH18&t=479s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'As an executive will want to see what advice they gave to the client and this '
              'was one that came up recently this was in a a firm standard client care letter.',
      'timestamp': 479,
      'timestamp_label': '[00:07:59]',
      'timestamp_seconds': 479,
      'tip': 'As an executive will want to see what advice they gave to the client and this '
             'was one that came up recently this was in a a firm standard client care letter.',
      'title': 'Contentious Clinic: Executor and Administrator Removal Disputes (IDR Law)',
      'url': 'https://www.youtube.com/watch?v=ikQ6l3STH18&t=479s',
      'video_id': 'ikQ6l3STH18'},
     {'author': 'JobRath',
      'channel': 'JobRath',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:24](https://www.youtube.com/watch?v=I__wJbnhlTw&t=324s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And finally, boxes 25 to 33 contain tax ID, patient account number, total '
              'charges, amount paid, provider signature information, service facility details, '
              "and billing provider information. So, while handling denials, you don't need to "
              'read the complete CMS 1500 form.',
      'timestamp': 324,
      'timestamp_label': '[00:05:24]',
      'timestamp_seconds': 324,
      'tip': 'And finally, boxes 25 to 33 contain tax ID, patient account number, total '
             'charges, amount paid, provider signature information, service facility details, '
             "and billing provider information. So, while handling denials, you don't need to "
             'read the complete CMS 1500 form.',
      'title': 'What Is CMS-1500 Form in Medical Billing? How to Read It for Denial Handling? '
               '#medicalbilling #rcm (JobRath)',
      'url': 'https://www.youtube.com/watch?v=I__wJbnhlTw&t=324s',
      'video_id': 'I__wJbnhlTw'},
     {'author': 'Ensemble',
      'channel': 'Ensemble',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:40](https://www.youtube.com/watch?v=EREvBniyM5c&t=760s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then rule number two everybody is your neighbor very nice love it thank you '
              "thank you all right well Beth thanks for joining us today and why don't you do "
              'the outro for us sure thanks for joining us be on the lookout for additional '
              'operator insights.',
      'timestamp': 760,
      'timestamp_label': '[00:12:40]',
      'timestamp_seconds': 760,
      'tip': 'Then rule number two everybody is your neighbor very nice love it thank you '
             "thank you all right well Beth thanks for joining us today and why don't you do "
             'the outro for us sure thanks for joining us be on the lookout for additional '
             'operator insights.',
      'title': 'Healthcare Revenue Recovery | OPERATOR INSIGHTS | Healthcare Revenue Cycle '
               'Management, RCM (Ensemble)',
      'url': 'https://www.youtube.com/watch?v=EREvBniyM5c&t=760s',
      'video_id': 'EREvBniyM5c'},
     {'author': 'Patriot Group',
      'channel': 'Patriot Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:08](https://www.youtube.com/watch?v=dUdxVBDLf5w&t=968s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Adda Network providers could really maximize their revenue so um it was a '
              'pleasure speaking with you today thanks likewise merid take care have a nice '
              'day okay take care.',
      'timestamp': 968,
      'timestamp_label': '[00:16:08]',
      'timestamp_seconds': 968,
      'tip': 'Adda Network providers could really maximize their revenue so um it was a '
             'pleasure speaking with you today thanks likewise merid take care have a nice day '
             'okay take care.',
      'title': 'How to Generate Revenue for Out-of-Network Medical Claims: Insights with '
               'Thomas J. Force (Patriot Group)',
      'url': 'https://www.youtube.com/watch?v=dUdxVBDLf5w&t=968s',
      'video_id': 'dUdxVBDLf5w'}],
 2: [{'author': 'MediBill Pro',
      'channel': 'MediBill Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=JpGm6Pmzrk8&t=54s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Fixed amount patient pays at the visit. So, this is basically a fixed amount, '
              'or we can say that this is a checking fees. Whenever we are just going to visit '
              'any kind of a doctor, we are going to pay a certain fee at the time of getting '
              'service.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'Fixed amount patient pays at the visit. So, this is basically a fixed amount, or '
             'we can say that this is a checking fees. Whenever we are just going to visit any '
             'kind of a doctor, we are going to pay a certain fee at the time of getting '
             'service.',
      'title': 'Medical Billing Jobs Interview Q&A | Rejection vs Copay vs Deductible '
               'Explained (2026 Guide) (MediBill Pro)',
      'url': 'https://www.youtube.com/watch?v=JpGm6Pmzrk8&t=54s',
      'video_id': 'JpGm6Pmzrk8'},
     {'author': 'HealthWatch Wisconsin',
      'channel': 'HealthWatch Wisconsin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:47](https://www.youtube.com/watch?v=XZ1MNlkWu4Y&t=47s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Didn't fully determine how much insurers had to pay providers in this situation "
              'the original rule set a qualifying payment amount based on average.',
      'timestamp': 47,
      'timestamp_label': '[00:00:47]',
      'timestamp_seconds': 47,
      'tip': "Didn't fully determine how much insurers had to pay providers in this situation "
             'the original rule set a qualifying payment amount based on average.',
      'title': 'New Final Rule on No Surprises Act - Explained (HealthWatch Wisconsin)',
      'url': 'https://www.youtube.com/watch?v=XZ1MNlkWu4Y&t=47s',
      'video_id': 'XZ1MNlkWu4Y'},
     {'author': 'CMSHHSgov',
      'channel': 'CMSHHSgov',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:52:24](https://www.youtube.com/watch?v=RRI2VT8QiiI&t=3144s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'PPDR process to settle payment disputes with providers and facilities. HHS will '
              'assess the $25 administrative fee in 2022 on the non-prevailing party providers '
              'facilities and uninsured or self-pay individual to the PPDR process.',
      'timestamp': 3144,
      'timestamp_label': '[00:52:24]',
      'timestamp_seconds': 3144,
      'tip': 'PPDR process to settle payment disputes with providers and facilities. HHS will '
             'assess the $25 administrative fee in 2022 on the non-prevailing party providers '
             'facilities and uninsured or self-pay individual to the PPDR process.',
      'title': 'No Surprises Act: Understanding Good Faith Estimates & Patient Provider '
               'Dispute Resolution Reqs (CMSHHSgov)',
      'url': 'https://www.youtube.com/watch?v=RRI2VT8QiiI&t=3144s',
      'video_id': 'RRI2VT8QiiI'},
     {'author': 'Craft Your Practice',
      'channel': 'Craft Your Practice',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:29](https://www.youtube.com/watch?v=tkUfu8WA56U&t=209s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So let's do it once with round numbers. Say your fee is a hundred and fifty "
              'dollars. The plan decides that the allowed amount for that session is a '
              "hundred, and the client's out-of-network benefit pays sixty percent after the "
              'deductible.',
      'timestamp': 209,
      'timestamp_label': '[00:03:29]',
      'timestamp_seconds': 209,
      'tip': "So let's do it once with round numbers. Say your fee is a hundred and fifty "
             'dollars. The plan decides that the allowed amount for that session is a hundred, '
             "and the client's out-of-network benefit pays sixty percent after the deductible.",
      'title': 'Superbills for Therapists: How Out-of-Network Reimbursement Actually Works '
               '(Craft Your Practice)',
      'url': 'https://www.youtube.com/watch?v=tkUfu8WA56U&t=209s',
      'video_id': 'tkUfu8WA56U'},
     {'author': 'MD Clarity',
      'channel': 'MD Clarity',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:08](https://www.youtube.com/watch?v=wnXpxS7_cqA&t=608s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This means digitizing your contracts and fee schedules, replicating the payer's "
              'adjudication math, and comparing every payment that comes in against what the '
              'contract says it should have been at the claim line level.',
      'timestamp': 608,
      'timestamp_label': '[00:10:08]',
      'timestamp_seconds': 608,
      'tip': "This means digitizing your contracts and fee schedules, replicating the payer's "
             'adjudication math, and comparing every payment that comes in against what the '
             'contract says it should have been at the claim line level.',
      'title': 'Healthcare Underpayments Explained: Causes, Costs, and How to Recover (MD '
               'Clarity)',
      'url': 'https://www.youtube.com/watch?v=wnXpxS7_cqA&t=608s',
      'video_id': 'wnXpxS7_cqA'},
     {'author': 'Michael Roberts',
      'channel': 'Michael Roberts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:36](https://www.youtube.com/watch?v=HolIPG8-TV8&t=96s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'CO45 means $60 over the contracted fee, and the practice writes it off. PR2 is '
              '$20 of coinsurance that the patient owes. AMT B6 is the allowed amount, $140. '
              'That is what the payer says the visit is worth under your contract. 200 charged '
              '60 contractual leaves 140 allowed.',
      'timestamp': 96,
      'timestamp_label': '[00:01:36]',
      'timestamp_seconds': 96,
      'tip': 'CO45 means $60 over the contracted fee, and the practice writes it off. PR2 is '
             '$20 of coinsurance that the patient owes. AMT B6 is the allowed amount, $140. '
             'That is what the payer says the visit is worth under your contract. 200 charged '
             '60 contractual leaves 140 allowed.',
      'title': '835 ERA Line by Line    and introducing Professor Remit (Michael Roberts)',
      'url': 'https://www.youtube.com/watch?v=HolIPG8-TV8&t=96s',
      'video_id': 'HolIPG8-TV8'},
     {'author': 'Insured and Informed',
      'channel': 'Insured and Informed',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:59](https://www.youtube.com/watch?v=wySlaLru-l4&t=179s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Instead of immediately assuming you have to pay the full amount, or even before '
              "looking into asking your doctor's office for  a reduced payment, a payment.",
      'timestamp': 179,
      'timestamp_label': '[00:02:59]',
      'timestamp_seconds': 179,
      'tip': 'Instead of immediately assuming you have to pay the full amount, or even before '
             "looking into asking your doctor's office for  a reduced payment, a payment.",
      'title': 'My In-Network Doctor Sent My Labs Out-of-Network… Now I Owe $2,000? (Insured '
               'and Informed)',
      'url': 'https://www.youtube.com/watch?v=wySlaLru-l4&t=179s',
      'video_id': 'wySlaLru-l4'},
     {'author': 'InfiMed Health',
      'channel': 'InfiMed Health',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:16](https://www.youtube.com/watch?v=uO7nW5fy5Y4&t=76s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '835 remittance parser reads each payment, adjustment and reason code. ERA '
              'matching ties each remittance line to the right claim and patient account. '
              'Contract variance detection compares what was paid with what the contract '
              'allows, and flags any gap.',
      'timestamp': 76,
      'timestamp_label': '[00:01:16]',
      'timestamp_seconds': 76,
      'tip': '835 remittance parser reads each payment, adjustment and reason code. ERA '
             'matching ties each remittance line to the right claim and patient account. '
             'Contract variance detection compares what was paid with what the contract '
             'allows, and flags any gap.',
      'title': 'Payment Posting and Reconciliation Explained: From 835 to Bank Deposit '
               '(InfiMed Health)',
      'url': 'https://www.youtube.com/watch?v=uO7nW5fy5Y4&t=76s',
      'video_id': 'uO7nW5fy5Y4'},
     {'author': 'Vikash Learning',
      'channel': 'Vikash Learning',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:34](https://www.youtube.com/watch?v=MWf66u11yb8&t=334s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Control number for this specific service line this segment is vital for '
              'healthcare providers to match payments and comprehend which policy or contract '
              'is being referred to for the payment information of each service line thank you '
              'for watching.',
      'timestamp': 334,
      'timestamp_label': '[00:05:34]',
      'timestamp_seconds': 334,
      'tip': 'Control number for this specific service line this segment is vital for '
             'healthcare providers to match payments and comprehend which policy or contract '
             'is being referred to for the payment information of each service line thank you '
             'for watching.',
      'title': 'What is CARC, RARC, & 835 Healthcare Policy Identification Segment? (Vikash '
               'Learning)',
      'url': 'https://www.youtube.com/watch?v=MWf66u11yb8&t=334s',
      'video_id': 'MWf66u11yb8'},
     {'author': 'Plano Texas',
      'channel': 'Plano Texas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:55](https://www.youtube.com/watch?v=w387XkK0lkk&t=1435s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So you provided a service to that patient. The patient pays for those benefits '
              'and therefore they need to pay you according to those benefits.',
      'timestamp': 1435,
      'timestamp_label': '[00:23:55]',
      'timestamp_seconds': 1435,
      'tip': 'So you provided a service to that patient. The patient pays for those benefits '
             'and therefore they need to pay you according to those benefits.',
      'title': 'ASC Billing - The Top 5 Ways to Increase Out of Network Revenue - MediGain '
               '(Plano Texas)',
      'url': 'https://www.youtube.com/watch?v=w387XkK0lkk&t=1435s',
      'video_id': 'w387XkK0lkk'},
     {'author': 'Ask The Biller',
      'channel': 'Ask The Biller',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:45](https://www.youtube.com/watch?v=SdYPzcQPWOw&t=405s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So they pay zero dollars for the remainder of their benefit year and the '
              'insurance company is going to cover the allowed amount 100 percent so insurance '
              'reimbursement is going to be 8605 dollars.',
      'timestamp': 405,
      'timestamp_label': '[00:06:45]',
      'timestamp_seconds': 405,
      'tip': 'So they pay zero dollars for the remainder of their benefit year and the '
             'insurance company is going to cover the allowed amount 100 percent so insurance '
             'reimbursement is going to be 8605 dollars.',
      'title': 'How to Calculate Patient and Payer Responsibility (Copay vs Coinsurance vs '
               'Deductible) (Ask The Biller)',
      'url': 'https://www.youtube.com/watch?v=SdYPzcQPWOw&t=405s',
      'video_id': 'SdYPzcQPWOw'},
     {'author': 'The Medical Bill Whisperer ',
      'channel': 'The Medical Bill Whisperer ',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:58](https://www.youtube.com/watch?v=TXjn5syXueM&t=178s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Insurance would pay 100% % but it's 100% of the very low allowance and that "
              'allowance never amounts to the full amount build and that difference does.',
      'timestamp': 178,
      'timestamp_label': '[00:02:58]',
      'timestamp_seconds': 178,
      'tip': "Insurance would pay 100% % but it's 100% of the very low allowance and that "
             'allowance never amounts to the full amount build and that difference does.',
      'title': 'SHOCKING Truth: How to Get Out-of-Network Providers Paid at In-Network Rates '
               '(Legally!) (The Medical Bill Whisperer )',
      'url': 'https://www.youtube.com/watch?v=TXjn5syXueM&t=178s',
      'video_id': 'TXjn5syXueM'},
     {'author': 'Inlera University',
      'channel': 'Inlera University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:07](https://www.youtube.com/watch?v=-zx82Gn2h04&t=367s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Or CPT code $145 versus $85 so each code has its own fee Associated and I '
              'noticed I have an allowed amount so noticing the differences between a buildt '
              'amount.',
      'timestamp': 367,
      'timestamp_label': '[00:06:07]',
      'timestamp_seconds': 367,
      'tip': 'Or CPT code $145 versus $85 so each code has its own fee Associated and I '
             'noticed I have an allowed amount so noticing the differences between a buildt '
             'amount.',
      'title': 'How to Read an Explanation of Benefits (EOB) & Electronic Remittance Advice '
               '(ERA) in US Healthcare (Inlera University)',
      'url': 'https://www.youtube.com/watch?v=-zx82Gn2h04&t=367s',
      'video_id': '-zx82Gn2h04'},
     {'author': 'Medical Billing Maven',
      'channel': 'Medical Billing Maven',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:16](https://www.youtube.com/watch?v=GhRz1M9lxtc&t=76s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Insurance companies sending us information about what happened as far as the '
              "provider sending them claims we don't really pay attention to.",
      'timestamp': 76,
      'timestamp_label': '[00:01:16]',
      'timestamp_seconds': 76,
      'tip': 'Insurance companies sending us information about what happened as far as the '
             "provider sending them claims we don't really pay attention to.",
      'title': 'ELECTRONIC REMITTANCE ADVICE IN MEDICAL BILLING |WHAT ARE EOBs, RAs AND ERAs | '
               'BACK TO BASICS PART 3 (Medical Billing Maven)',
      'url': 'https://www.youtube.com/watch?v=GhRz1M9lxtc&t=76s',
      'video_id': 'GhRz1M9lxtc'},
     {'author': 'Collect Rx',
      'channel': 'Collect Rx',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:10](https://www.youtube.com/watch?v=jW7NdP3R2Lc&t=970s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Rates contracted and fee schedule rates are already fixed so out of network is '
              'the only area where you can really increase rates and improve the bottom.',
      'timestamp': 970,
      'timestamp_label': '[00:16:10]',
      'timestamp_seconds': 970,
      'tip': 'Rates contracted and fee schedule rates are already fixed so out of network is '
             'the only area where you can really increase rates and improve the bottom.',
      'title': "Collect Rx's 6 Keys to Success in Revenue Cycle Management for Out of Network "
               'Providers (Collect Rx)',
      'url': 'https://www.youtube.com/watch?v=jW7NdP3R2Lc&t=970s',
      'video_id': 'jW7NdP3R2Lc'}],
 3: [{'author': 'Top Hospitals USA',
      'channel': 'Top Hospitals USA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:39](https://www.youtube.com/watch?v=eDCqqjk5fqk&t=219s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It has closed 15,145 of them. Almost all of those, 14,799, were about the No '
              'Surprises Act. 11,417 were filed against providers, facilities, or air '
              'ambulance services.',
      'timestamp': 219,
      'timestamp_label': '[00:03:39]',
      'timestamp_seconds': 219,
      'tip': 'It has closed 15,145 of them. Almost all of those, 14,799, were about the No '
             'Surprises Act. 11,417 were filed against providers, facilities, or air ambulance '
             'services.',
      'title': 'Surprise Bills Are Illegal — So Why Did Arbitration Just Hit $15 Billion? (Top '
               'Hospitals USA)',
      'url': 'https://www.youtube.com/watch?v=eDCqqjk5fqk&t=219s',
      'video_id': 'eDCqqjk5fqk'},
     {'author': 'Vee Healthtek',
      'channel': 'Vee Healthtek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:10](https://www.youtube.com/watch?v=s3194z7bdwY&t=130s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Finally, follow the award through payment. Compare the determination with the '
              'amount received, escalate unresolved differences, and reconcile the final cash. '
              'Keep eligible dollars, submitted disputes, awards, and posted payments separate '
              'in reporting.',
      'timestamp': 130,
      'timestamp_label': '[00:02:10]',
      'timestamp_seconds': 130,
      'tip': 'Finally, follow the award through payment. Compare the determination with the '
             'amount received, escalate unresolved differences, and reconcile the final cash. '
             'Keep eligible dollars, submitted disputes, awards, and posted payments separate '
             'in reporting.',
      'title': 'How to Improve Out-of-Network Reimbursement and IDR Recovery (Vee Healthtek)',
      'url': 'https://www.youtube.com/watch?v=s3194z7bdwY&t=130s',
      'video_id': 's3194z7bdwY'},
     {'author': 'Welcome to The Patient Blueprint.',
      'channel': 'Welcome to The Patient Blueprint.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=tNSTH4Y29D8&t=118s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Surprise billing simply Since 2022, the No Surprises Act bans balance bills for '
              'emergency care, out-of-network providers at in-network facilities, and air '
              "ambulance. You owe only your in-network cost sharing. Don't pay a surprise "
              "balance bill you don't actually owe.",
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': 'Surprise billing simply Since 2022, the No Surprises Act bans balance bills for '
             'emergency care, out-of-network providers at in-network facilities, and air '
             "ambulance. You owe only your in-network cost sharing. Don't pay a surprise "
             "balance bill you don't actually owe.",
      'title': 'Surprise Billing & the No Surprises Act Explained (Welcome to The Patient '
               'Blueprint.)',
      'url': 'https://www.youtube.com/watch?v=tNSTH4Y29D8&t=118s',
      'video_id': 'tNSTH4Y29D8'},
     {'author': 'Payerset',
      'channel': 'Payerset',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:28](https://www.youtube.com/watch?v=lqE3aZxq024&t=508s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And so QPA's tend to be too low. So the starting price is too low. The flip "
              'side though is that providers and their vendors have been very effective at um '
              'at putting forth and winning arbitration awards that are much much too high.',
      'timestamp': 508,
      'timestamp_label': '[00:08:28]',
      'timestamp_seconds': 508,
      'tip': "And so QPA's tend to be too low. So the starting price is too low. The flip side "
             'though is that providers and their vendors have been very effective at um at '
             'putting forth and winning arbitration awards that are much much too high.',
      'title': 'How the No Surprises Act Impacts Employers + Navigating the IDR Payment System '
               'with Tia Goss Sawhney (Payerset)',
      'url': 'https://www.youtube.com/watch?v=lqE3aZxq024&t=508s',
      'video_id': 'lqE3aZxq024'},
     {'author': 'Coalition for Affordable Hospitals',
      'channel': 'Coalition for Affordable Hospitals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:13](https://www.youtube.com/watch?v=9SCzxZp8uAE&t=133s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t agree they go to what's a winner takes all arbitration similar to what major "
              'league baseball uses for salaries. The doctor and an the insurer each propose a '
              'price.',
      'timestamp': 133,
      'timestamp_label': '[00:02:13]',
      'timestamp_seconds': 133,
      'tip': "'t agree they go to what's a winner takes all arbitration similar to what major "
             'league baseball uses for salaries. The doctor and an the insurer each propose a '
             'price.',
      'title': 'Panel - Fixing the No Surprises Act’s Independent Dispute Resolution (IDR) '
               'Process (Coalition for Affordable Hospitals)',
      'url': 'https://www.youtube.com/watch?v=9SCzxZp8uAE&t=133s',
      'video_id': '9SCzxZp8uAE'},
     {'author': 'Law & Business',
      'channel': 'Law & Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:16](https://www.youtube.com/watch?v=88cpe80FbyY&t=376s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The California statute caps patient out-of-pocket costs at the exact rate they '
              'would pay for an equivalent in-network medical service and prohibits ambulance '
              'companies from reporting delinquent bills to credit bureaus for at least 12 '
              'months after billing.',
      'timestamp': 376,
      'timestamp_label': '[00:06:16]',
      'timestamp_seconds': 376,
      'tip': 'The California statute caps patient out-of-pocket costs at the exact rate they '
             'would pay for an equivalent in-network medical service and prohibits ambulance '
             'companies from reporting delinquent bills to credit bureaus for at least 12 '
             'months after billing.',
      'title': 'Are Ambulances Covered Under Surprise Billing Laws? (Law & Business)',
      'url': 'https://www.youtube.com/watch?v=88cpe80FbyY&t=376s',
      'video_id': '88cpe80FbyY'},
     {'author': 'Modern Healthcare Finance & RCM',
      'channel': 'Modern Healthcare Finance & RCM',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:54](https://www.youtube.com/watch?v=nQA0SW59EWQ&t=234s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re more efficient, you're getting your patients discharged sooner, which is "
              'limiting your cost and preserving your profit margin from that payment that '
              "you're getting for that patient's stay.",
      'timestamp': 234,
      'timestamp_label': '[00:03:54]',
      'timestamp_seconds': 234,
      'tip': "'re more efficient, you're getting your patients discharged sooner, which is "
             'limiting your cost and preserving your profit margin from that payment that '
             "you're getting for that patient's stay.",
      'title': 'Hospital Metrics Explained: Patient Days, ADC, ALOS, Adjusted Discharges, Case '
               'Mix Index (8 Minutes) (Modern Healthcare Finance & RCM)',
      'url': 'https://www.youtube.com/watch?v=nQA0SW59EWQ&t=234s',
      'video_id': 'nQA0SW59EWQ'},
     {'author': 'AJR Radiology',
      'channel': 'AJR Radiology',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:50](https://www.youtube.com/watch?v=rYqWvbw_kGo&t=350s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Final our study can serve as a benchmark when considering the efficacy of '
              'future IDR cost and batching rules and how they play out for the financial '
              'viability the process for clinicians.',
      'timestamp': 350,
      'timestamp_label': '[00:05:50]',
      'timestamp_seconds': 350,
      'tip': 'Final our study can serve as a benchmark when considering the efficacy of future '
             'IDR cost and batching rules and how they play out for the financial viability '
             'the process for clinicians.',
      'title': 'Financial Viability of the No Surprises Act Independent Dispute Resolution '
               'Process (AJR Radiology)',
      'url': 'https://www.youtube.com/watch?v=rYqWvbw_kGo&t=350s',
      'video_id': 'rYqWvbw_kGo'},
     {'author': 'Etactics',
      'channel': 'Etactics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:05](https://www.youtube.com/watch?v=M-Mz0m1tdrQ&t=185s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Imagine how your patients must feel offering Insight on cost estimation and '
              'coverage can prevent payment surprises and reduce the amount of bills sent to.',
      'timestamp': 185,
      'timestamp_label': '[00:03:05]',
      'timestamp_seconds': 185,
      'tip': 'Imagine how your patients must feel offering Insight on cost estimation and '
             'coverage can prevent payment surprises and reduce the amount of bills sent to.',
      'title': '[ANSWERED] What is Front-End Revenue Cycle Management? (Etactics)',
      'url': 'https://www.youtube.com/watch?v=M-Mz0m1tdrQ&t=185s',
      'video_id': 'M-Mz0m1tdrQ'},
     {'author': 'Collect Rx',
      'channel': 'Collect Rx',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:37](https://www.youtube.com/watch?v=Pqx2hpp_cLU&t=277s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Well it's important to point out here is that during John's time there he would "
              'work on cases that would act as cost containment measures for the insurance.',
      'timestamp': 277,
      'timestamp_label': '[00:04:37]',
      'timestamp_seconds': 277,
      'tip': "Well it's important to point out here is that during John's time there he would "
             'work on cases that would act as cost containment measures for the insurance.',
      'title': '6 Keys to Success in Out of Network Reimbursement (Collect Rx)',
      'url': 'https://www.youtube.com/watch?v=Pqx2hpp_cLU&t=277s',
      'video_id': 'Pqx2hpp_cLU'},
     {'author': 'Vee Healthtek',
      'channel': 'Vee Healthtek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:13](https://www.youtube.com/watch?v=GpHExH5dquQ&t=73s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The qualifying payment amount or QPA is an important reference point, but it '
              'does not provide a complete view of potential recovery. Claim evidence, the '
              'applicable recovery pathway, and collection economics still matter.',
      'timestamp': 73,
      'timestamp_label': '[00:01:13]',
      'timestamp_seconds': 73,
      'tip': 'The qualifying payment amount or QPA is an important reference point, but it '
             'does not provide a complete view of potential recovery. Claim evidence, the '
             'applicable recovery pathway, and collection economics still matter.',
      'title': 'Out-of-Network Reimbursement: Why Paid Claims Can Still Hide Lost Revenue (Vee '
               'Healthtek)',
      'url': 'https://www.youtube.com/watch?v=GpHExH5dquQ&t=73s',
      'video_id': 'GpHExH5dquQ'},
     {'author': 'Brown University Health',
      'channel': 'Brown University Health',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=g18RP2cQe_s&t=55s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Pierce] One of the exciting things we're doing at Brown, to innovate in the "
              'area of regional anesthesia, is using these nerve blocks for rib fractures.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': "Pierce] One of the exciting things we're doing at Brown, to innovate in the area "
             'of regional anesthesia, is using these nerve blocks for rib fractures.',
      'title': 'In the Emergency Department: Ultrasound-Guided Anesthetic Blocks (Brown '
               'University Health)',
      'url': 'https://www.youtube.com/watch?v=g18RP2cQe_s&t=55s',
      'video_id': 'g18RP2cQe_s'},
     {'author': 'FAIR Health',
      'channel': 'FAIR Health',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:09](https://www.youtube.com/watch?v=WuZrwo-Qxww&t=189s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Also may pay more or less than the estimates on this site review your health '
              'insurance plan documents for details on your coverage or call your insurer if '
              'you have any questions see the next video for some additional features of your '
              'cost estimate page.',
      'timestamp': 189,
      'timestamp_label': '[00:03:09]',
      'timestamp_seconds': 189,
      'tip': 'Also may pay more or less than the estimates on this site review your health '
             'insurance plan documents for details on your coverage or call your insurer if '
             'you have any questions see the next video for some additional features of your '
             'cost estimate page.',
      'title': 'Understand Your Medical Cost Estimate — FAIRHealthConsumer.org (Part 1) (FAIR '
               'Health)',
      'url': 'https://www.youtube.com/watch?v=WuZrwo-Qxww&t=189s',
      'video_id': 'WuZrwo-Qxww'},
     {'author': 'Beckers ASC',
      'channel': 'Beckers ASC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:07](https://www.youtube.com/watch?v=KkjI85NtmNE&t=67s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Forrest's has specialized in providing cost containment services to health "
              'insurers and various products and services to hospitals health systems and '
              'other health care providers previously mr.',
      'timestamp': 67,
      'timestamp_label': '[00:01:07]',
      'timestamp_seconds': 67,
      'tip': "Forrest's has specialized in providing cost containment services to health "
             'insurers and various products and services to hospitals health systems and other '
             'health care providers previously mr.',
      'title': 'Top 10 Best Practices to Maximize Complex Out-of-Network Reimbursements and '
               'More (Beckers ASC)',
      'url': 'https://www.youtube.com/watch?v=KkjI85NtmNE&t=67s',
      'video_id': 'KkjI85NtmNE'},
     {'author': 'AHealthcareZ - Healthcare Finance Explained',
      'channel': 'AHealthcareZ - Healthcare Finance Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:22](https://www.youtube.com/watch?v=NFJaCM_6M_Y&t=622s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'People are not gonna get the bills okay but as far as the behind the the scenes '
              "negotiation that has not been worked out yet and that's the point I wanted to "
              'make today thank you for watching a healthcare z.',
      'timestamp': 622,
      'timestamp_label': '[00:10:22]',
      'timestamp_seconds': 622,
      'tip': 'People are not gonna get the bills okay but as far as the behind the the scenes '
             "negotiation that has not been worked out yet and that's the point I wanted to "
             'make today thank you for watching a healthcare z.',
      'title': 'No Surprises Act Explained (AHealthcareZ - Healthcare Finance Explained)',
      'url': 'https://www.youtube.com/watch?v=NFJaCM_6M_Y&t=622s',
      'video_id': 'NFJaCM_6M_Y'}],
 4: [{'author': 'Welcome to The Patient Blueprint.',
      'channel': 'Welcome to The Patient Blueprint.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=3OCpShEAIJs&t=117s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '72 hours ahead and your informed consent. It can never be used for emergency, '
              'anesthesia, radiology, or pathology. Simply, the No Surprises Act bans balance '
              'bills for emergency care, out-of-network providers at in-network facilities, '
              'and air ambulance.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': '72 hours ahead and your informed consent. It can never be used for emergency, '
             'anesthesia, radiology, or pathology. Simply, the No Surprises Act bans balance '
             'bills for emergency care, out-of-network providers at in-network facilities, and '
             'air ambulance.',
      'title': 'Surprise Medical Bills: No Surprises Act Protections Explained (Welcome to The '
               'Patient Blueprint.)',
      'url': 'https://www.youtube.com/watch?v=3OCpShEAIJs&t=117s',
      'video_id': '3OCpShEAIJs'},
     {'author': 'Law Unpacked',
      'channel': 'Law Unpacked',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:56](https://www.youtube.com/watch?v=0NouMpFWLHI&t=176s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So what should you do if you get a surprise bill? First, don't rush to pay it. "
              "Check whether it's an emergency, an in-network facility, or an air ambulance. "
              "Second, compare it to your insurance's explanation of benefits. Your share "
              'should match your in-network costs.',
      'timestamp': 176,
      'timestamp_label': '[00:02:56]',
      'timestamp_seconds': 176,
      'tip': "So what should you do if you get a surprise bill? First, don't rush to pay it. "
             "Check whether it's an emergency, an in-network facility, or an air ambulance. "
             "Second, compare it to your insurance's explanation of benefits. Your share "
             'should match your in-network costs.',
      'title': 'Do You Have to Pay a Surprise Medical Bill? (The No Surprises Act Explained) '
               '(Law Unpacked)',
      'url': 'https://www.youtube.com/watch?v=0NouMpFWLHI&t=176s',
      'video_id': '0NouMpFWLHI'},
     {'author': 'The Medical Bill Whisperer ',
      'channel': 'The Medical Bill Whisperer ',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:54](https://www.youtube.com/watch?v=fq0_XVnPWnI&t=294s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Also covered by the no surprise act and last Air transport air ambulance is '
              'also covered under the no surprise act what to do if you get a bill call your.',
      'timestamp': 294,
      'timestamp_label': '[00:04:54]',
      'timestamp_seconds': 294,
      'tip': 'Also covered by the no surprise act and last Air transport air ambulance is also '
             'covered under the no surprise act what to do if you get a bill call your.',
      'title': 'How to Get Your Insurance to PAY for Out-of-Network Care | The Medical Bill '
               'Whisperer  (The Medical Bill Whisperer )',
      'url': 'https://www.youtube.com/watch?v=fq0_XVnPWnI&t=294s',
      'video_id': 'fq0_XVnPWnI'},
     {'author': 'Evolutio Labs',
      'channel': 'Evolutio Labs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=HwCCcS3hQls&t=21s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In 2022, a federal law called the No Surprises Act went into effect. It was '
              'designed specifically for situations like yours. If you go to an emergency '
              'room, even an out-of-network one, your insurance company cannot make you pay '
              'more than your in-network cost-sharing amount.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'In 2022, a federal law called the No Surprises Act went into effect. It was '
             'designed specifically for situations like yours. If you go to an emergency room, '
             'even an out-of-network one, your insurance company cannot make you pay more than '
             'your in-network cost-sharing amount.',
      'title': 'ER Bill Denied? Do NOT Pay Until You Watch This (The No Surprises Act) '
               '(Evolutio Labs)',
      'url': 'https://www.youtube.com/watch?v=HwCCcS3hQls&t=21s',
      'video_id': 'HwCCcS3hQls'},
     {'author': 'Holland & Hart LLP',
      'channel': 'Holland & Hart LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:44:18](https://www.youtube.com/watch?v=aaDjROGKKC0&t=2658s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t get effective consent in advance in air ambulance cases. Um of course, you "
              'may still bill and recover from the plan or the insurance for the covered '
              'services, and you may still bill self-pay patients.',
      'timestamp': 2658,
      'timestamp_label': '[00:44:18]',
      'timestamp_seconds': 2658,
      'tip': "'t get effective consent in advance in air ambulance cases. Um of course, you "
             'may still bill and recover from the plan or the insurance for the covered '
             'services, and you may still bill self-pay patients.',
      'title': 'No Surprise Billing Rules (Holland & Hart LLP)',
      'url': 'https://www.youtube.com/watch?v=aaDjROGKKC0&t=2658s',
      'video_id': 'aaDjROGKKC0'},
     {'author': 'About The Rest',
      'channel': 'About The Rest',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:54](https://www.youtube.com/watch?v=WdSfoeegaaI&t=1194s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um, I mean, that's, that's billions of dollars, uh, uh, of payments that are "
              'coming from, from the insurance companies. So, um, you know, I, I think we '
              'swung the way of No Surprises Act, which really put us all in a bad position as '
              'anesthesia providers.',
      'timestamp': 1194,
      'timestamp_label': '[00:19:54]',
      'timestamp_seconds': 1194,
      'tip': "Um, I mean, that's, that's billions of dollars, uh, uh, of payments that are "
             'coming from, from the insurance companies. So, um, you know, I, I think we swung '
             'the way of No Surprises Act, which really put us all in a bad position as '
             'anesthesia providers.',
      'title': 'Anesthesia IDR Is a Knife Fight. Who Walks Away? (About The Rest)',
      'url': 'https://www.youtube.com/watch?v=WdSfoeegaaI&t=1194s',
      'video_id': 'WdSfoeegaaI'},
     {'author': 'MediBill Pro',
      'channel': 'MediBill Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=dta7Y_d4nYA&t=30s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "80% or 90% or 70% depending on the patient's benefit plan. And rest of the 10%, "
              '20% or 30% basically is going to be paid by the patient. So, basically the '
              'percentage that the patient is going to pay after that specific deductibles is '
              'called as co-insurance amount.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': "80% or 90% or 70% depending on the patient's benefit plan. And rest of the 10%, "
             '20% or 30% basically is going to be paid by the patient. So, basically the '
             'percentage that the patient is going to pay after that specific deductibles is '
             'called as co-insurance amount.',
      'title': 'Top Medical Billing Interview Questions & Answers | Coinsurance vs Eligibility '
               'vs Preauthorization (MediBill Pro)',
      'url': 'https://www.youtube.com/watch?v=dta7Y_d4nYA&t=30s',
      'video_id': 'dta7Y_d4nYA'},
     {'author': 'Grand Rounds in Urology',
      'channel': 'Grand Rounds in Urology',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:01](https://www.youtube.com/watch?v=_42GJfeJNw4&t=121s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And the amount covered by his or her insurance often these can be large amounts '
              'of money that are a.',
      'timestamp': 121,
      'timestamp_label': '[00:02:01]',
      'timestamp_seconds': 121,
      'tip': 'And the amount covered by his or her insurance often these can be large amounts '
             'of money that are a.',
      'title': 'No More Surprises: An Overview of the No Surprises Act (Grand Rounds in '
               'Urology)',
      'url': 'https://www.youtube.com/watch?v=_42GJfeJNw4&t=121s',
      'video_id': '_42GJfeJNw4'},
     {'author': 'Kym Tolson The Traveling Therapist',
      'channel': 'Kym Tolson The Traveling Therapist',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:30](https://www.youtube.com/watch?v=FpNL1YIlvD0&t=210s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s got everything you need. It's got address, um the insurance company, the "
              "client's information. Since you already had it in there, it's going to populate "
              "that. It's got your phone number, your contact information, your NPI, your "
              'license number, tax ID.',
      'timestamp': 210,
      'timestamp_label': '[00:03:30]',
      'timestamp_seconds': 210,
      'tip': "'s got everything you need. It's got address, um the insurance company, the "
             "client's information. Since you already had it in there, it's going to populate "
             "that. It's got your phone number, your contact information, your NPI, your "
             'license number, tax ID.',
      'title': 'Out Of Network Billing Via Filing Claims Through an EHR and a Superbill (Kym '
               'Tolson The Traveling Therapist)',
      'url': 'https://www.youtube.com/watch?v=FpNL1YIlvD0&t=210s',
      'video_id': 'FpNL1YIlvD0'},
     {'author': 'PKR Vibes Career & Growth',
      'channel': 'PKR Vibes Career & Growth',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:10](https://www.youtube.com/watch?v=72PuS1BX6_s&t=730s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They are concluded that it is related to the patient. You may bill to patient '
              'or other entity. If other insurance is there okay you can bill it not otherwise '
              'then it is not related to the uh I mean it is related to the payer.',
      'timestamp': 730,
      'timestamp_label': '[00:12:10]',
      'timestamp_seconds': 730,
      'tip': 'They are concluded that it is related to the patient. You may bill to patient or '
             'other entity. If other insurance is there okay you can bill it not otherwise '
             'then it is not related to the uh I mean it is related to the payer.',
      'title': '#DENIALCODE AND REMARK CODE IN MEDICAL BILLING #ushealthcare #REMARKCODES '
               '#CARC #RARC #denialcodes (PKR Vibes Career & Growth)',
      'url': 'https://www.youtube.com/watch?v=72PuS1BX6_s&t=730s',
      'video_id': '72PuS1BX6_s'},
     {'author': 'Alicia Murray | The Therapist HQ \U0001faa9',
      'channel': 'Alicia Murray | The Therapist HQ \U0001faa9',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:32](https://www.youtube.com/watch?v=eXrZnEwRRH4&t=1052s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '" Although I have a group practice, I just use my personal NPI as the NPI for '
              "folks to check for their insurance. It doesn't bother me if they're using my "
              'NPI to check against those things.',
      'timestamp': 1052,
      'timestamp_label': '[00:17:32]',
      'timestamp_seconds': 1052,
      'tip': '" Although I have a group practice, I just use my personal NPI as the NPI for '
             "folks to check for their insurance. It doesn't bother me if they're using my NPI "
             'to check against those things.',
      'title': 'Out-of-network 101 for therapists (Alicia Murray | The Therapist HQ '
               '\U0001faa9)',
      'url': 'https://www.youtube.com/watch?v=eXrZnEwRRH4&t=1052s',
      'video_id': 'eXrZnEwRRH4'},
     {'author': 'US Healthcare Insights by Shiva',
      'channel': 'US Healthcare Insights by Shiva',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=V7EGu84Chfc&t=54s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Any authorization is needed or not which called registration and insurance '
              "verification. Next, after verification of the patient's details, the patient "
              'visits the healthcare provider and receives treatment.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'Any authorization is needed or not which called registration and insurance '
             "verification. Next, after verification of the patient's details, the patient "
             'visits the healthcare provider and receives treatment.',
      'title': "What is Revenue Cycle Management (RCM)? Complete Beginner's Guide by Shiva Rao "
               '(US Healthcare Insights by Shiva)',
      'url': 'https://www.youtube.com/watch?v=V7EGu84Chfc&t=54s',
      'video_id': 'V7EGu84Chfc'},
     {'author': 'Cedar',
      'channel': 'Cedar',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=U7ayI8K_Ggw&t=28s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Ultra focused on the insurance side of payments so what we've done is um really "
              'look at what impacts patients um and looking at Patients as consumers as well.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': "Ultra focused on the insurance side of payments so what we've done is um really "
             'look at what impacts patients um and looking at Patients as consumers as well.',
      'title': 'Insights into Healthcare Finance: PFX Benchmarks (Cedar)',
      'url': 'https://www.youtube.com/watch?v=U7ayI8K_Ggw&t=28s',
      'video_id': 'U7ayI8K_Ggw'},
     {'author': 'Inlera University',
      'channel': 'Inlera University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:55](https://www.youtube.com/watch?v=XyBNgMnFz0Y&t=355s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So you can certainly benefit from utilizing these real-time tools because if '
              'you have that patient that just walked in and you have a batch.',
      'timestamp': 355,
      'timestamp_label': '[00:05:55]',
      'timestamp_seconds': 355,
      'tip': 'So you can certainly benefit from utilizing these real-time tools because if you '
             'have that patient that just walked in and you have a batch.',
      'title': '5 Ways to verify patient Insurance Eligibility | Medical Billing Terms (Inlera '
               'University)',
      'url': 'https://www.youtube.com/watch?v=XyBNgMnFz0Y&t=355s',
      'video_id': 'XyBNgMnFz0Y'},
     {'author': 'AHealthcareZ - Healthcare Finance Explained',
      'channel': 'AHealthcareZ - Healthcare Finance Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=8NDnQoTkjb4&t=57s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Anesthesiologists and pathologists which is why many health insurance plans '
              "have what's called a wraps policy which means that these physicians even though "
              'the.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': 'Anesthesiologists and pathologists which is why many health insurance plans have '
             "what's called a wraps policy which means that these physicians even though the.",
      'title': 'Healthcare In-Network / Out-of-Network Bait and Switch (AHealthcareZ - '
               'Healthcare Finance Explained)',
      'url': 'https://www.youtube.com/watch?v=8NDnQoTkjb4&t=57s',
      'video_id': '8NDnQoTkjb4'}],
 5: [{'author': 'The Phia Group, LLC',
      'channel': 'The Phia Group, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:30](https://www.youtube.com/watch?v=ksxW878eWWk&t=690s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um just a little context and background. So, as most people here listening '
              'know, uh the No Surprises Act includes a baseball arbitration um style process. '
              'So, both parties to a dispute uh have an opportunity to submit an offer.',
      'timestamp': 690,
      'timestamp_label': '[00:11:30]',
      'timestamp_seconds': 690,
      'tip': 'Um just a little context and background. So, as most people here listening know, '
             'uh the No Surprises Act includes a baseball arbitration um style process. So, '
             'both parties to a dispute uh have an opportunity to submit an offer.',
      'title': 'Empowering Plans: P235 – The Latest No Surprises Act Developments: A 2026 '
               'Reality Check for TPAs (The Phia Group, LLC)',
      'url': 'https://www.youtube.com/watch?v=ksxW878eWWk&t=690s',
      'video_id': 'ksxW878eWWk'},
     {'author': 'Health Tech Nerds',
      'channel': 'Health Tech Nerds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:11](https://www.youtube.com/watch?v=c7whA-tTpq4&t=671s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'AEI who I had had worked with were sort of advi- explaining that arbitration '
              "had a lot of risk to it in part because it is very opaque. You you don't really "
              "know what's going to happen in the process. It risks being captured by "
              'providers.',
      'timestamp': 671,
      'timestamp_label': '[00:11:11]',
      'timestamp_seconds': 671,
      'tip': 'AEI who I had had worked with were sort of advi- explaining that arbitration had '
             "a lot of risk to it in part because it is very opaque. You you don't really know "
             "what's going to happen in the process. It risks being captured by providers.",
      'title': 'How the No Surprises Act solved balance billing but created a pricing problem '
               '| Loren Adler (Health Tech Nerds)',
      'url': 'https://www.youtube.com/watch?v=c7whA-tTpq4&t=671s',
      'video_id': 'c7whA-tTpq4'},
     {'author': 'Share My Lesson',
      'channel': 'Share My Lesson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:11](https://www.youtube.com/watch?v=Q11eG-8d-Hw&t=311s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Step four, if you're uninsured, use the $400 rule. If your bill is $400 above "
              'the good faith estimate, file a dispute. Step five, document everything. '
              "Screenshots, bills, EOBS, call logs, all of it. Healthcare shouldn't be a "
              'financial trap.',
      'timestamp': 311,
      'timestamp_label': '[00:05:11]',
      'timestamp_seconds': 311,
      'tip': "Step four, if you're uninsured, use the $400 rule. If your bill is $400 above "
             'the good faith estimate, file a dispute. Step five, document everything. '
             "Screenshots, bills, EOBS, call logs, all of it. Healthcare shouldn't be a "
             'financial trap.',
      'title': 'The No Surprises Act Explained: How to Fight Surprise Medical Bills (Share My '
               'Lesson)',
      'url': 'https://www.youtube.com/watch?v=Q11eG-8d-Hw&t=311s',
      'video_id': 'Q11eG-8d-Hw'},
     {'author': 'The Phia Group, LLC',
      'channel': 'The Phia Group, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:09](https://www.youtube.com/watch?v=8QIP4F1EGTA&t=549s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You know, we have factors that are completely detached from like the amount of '
              'money that uh that should be paid for a particular dispute or for for a '
              'particular claim. For example, I mean, you know, patient acuity or the quality '
              'of the provider or whatever.',
      'timestamp': 549,
      'timestamp_label': '[00:09:09]',
      'timestamp_seconds': 549,
      'tip': 'You know, we have factors that are completely detached from like the amount of '
             'money that uh that should be paid for a particular dispute or for for a '
             'particular claim. For example, I mean, you know, patient acuity or the quality '
             'of the provider or whatever.',
      'title': 'Empowering Plans: P254 – Fixing the No Surprises Act: Will Congress Repair '
               'IDR? (The Phia Group, LLC)',
      'url': 'https://www.youtube.com/watch?v=8QIP4F1EGTA&t=549s',
      'video_id': '8QIP4F1EGTA'},
     {'author': 'Medical Economics TV',
      'channel': 'Medical Economics TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:33](https://www.youtube.com/watch?v=K4eVTdf3xa0&t=813s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, as long as it's you know, fair and reasonable proposal in the arbitration "
              'the baseball style arbitration process that IDR provides. I think the IDR '
              'arbiters often rule in favor of the of the provider.',
      'timestamp': 813,
      'timestamp_label': '[00:13:33]',
      'timestamp_seconds': 813,
      'tip': "So, as long as it's you know, fair and reasonable proposal in the arbitration "
             'the baseball style arbitration process that IDR provides. I think the IDR '
             'arbiters often rule in favor of the of the provider.',
      'title': "S1 Ep161: The No Surprises Act's new payment dispute rule, with Anders Gilberg "
               'of MGMA (Medical Economics TV)',
      'url': 'https://www.youtube.com/watch?v=K4eVTdf3xa0&t=813s',
      'video_id': 'K4eVTdf3xa0'},
     {'author': 'Apex IONM Solutions',
      'channel': 'Apex IONM Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:26](https://www.youtube.com/watch?v=gbhlBlDLViQ&t=86s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t release the funds, then you're left with no recourse after that, cuz "
              'Congress just presumed that the insurance companies would actually follow the '
              'law. So, that that has become a significant problem.',
      'timestamp': 86,
      'timestamp_label': '[00:01:26]',
      'timestamp_seconds': 86,
      'tip': "'t release the funds, then you're left with no recourse after that, cuz Congress "
             'just presumed that the insurance companies would actually follow the law. So, '
             'that that has become a significant problem.',
      'title': 'You Won Arbitration – So Why Is the Money Still Missing? | Enforcement Push '
               'for No Surprises Act (Apex IONM Solutions)',
      'url': 'https://www.youtube.com/watch?v=gbhlBlDLViQ&t=86s',
      'video_id': 'gbhlBlDLViQ'},
     {'author': 'The On-Air Advocate',
      'channel': 'The On-Air Advocate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=1tAnAfBQ9O8&t=39s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It also protects uninsured patients by requiring a good faith estimate before '
              'you get care. And if the final bill ends up to be more than $400 above what was '
              "estimated, you have the right to dispute the charges. Now, here's something "
              'important to know.',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': 'It also protects uninsured patients by requiring a good faith estimate before '
             'you get care. And if the final bill ends up to be more than $400 above what was '
             "estimated, you have the right to dispute the charges. Now, here's something "
             'important to know.',
      'title': 'Unexpected Medical Bill? Know Your Rights Under the No Surprises Act (The '
               'On-Air Advocate)',
      'url': 'https://www.youtube.com/watch?v=1tAnAfBQ9O8&t=39s',
      'video_id': '1tAnAfBQ9O8'},
     {'author': 'The Center for Medical Education',
      'channel': 'The Center for Medical Education',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:23](https://www.youtube.com/watch?v=uqsbhH3wss0&t=563s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You know, the risks are roughly equal. Um, discuss with the patient risk '
              'benefits benefits alternatives, potential risks include, you know, uh, the '
              'potential risks of a CT to a pregnant patient. Um, discussed, uh, the risks on '
              'both sides.',
      'timestamp': 563,
      'timestamp_label': '[00:09:23]',
      'timestamp_seconds': 563,
      'tip': 'You know, the risks are roughly equal. Um, discuss with the patient risk '
             'benefits benefits alternatives, potential risks include, you know, uh, the '
             'potential risks of a CT to a pregnant patient. Um, discussed, uh, the risks on '
             'both sides.',
      'title': 'Ten Most Important Legal Questions Asked | The High Risk Emergency Medicine '
               'Course (The Center for Medical Education)',
      'url': 'https://www.youtube.com/watch?v=uqsbhH3wss0&t=563s',
      'video_id': 'uqsbhH3wss0'},
     {'author': 'One80 Physical Therapy',
      'channel': 'One80 Physical Therapy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=GVdiKSs4kvU&t=54s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And on that first visit, we're going to get to the root cause of your problem "
              'using our patented techniques and get you back to what you want to do, possibly '
              'after one visit, usually between 1 to three visits.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': "And on that first visit, we're going to get to the root cause of your problem "
             'using our patented techniques and get you back to what you want to do, possibly '
             'after one visit, usually between 1 to three visits.',
      'title': 'Insurance Pay vs Out-of-Network: Why One80 Physical Therapy is Different '
               '(One80 Physical Therapy)',
      'url': 'https://www.youtube.com/watch?v=GVdiKSs4kvU&t=54s',
      'video_id': 'GVdiKSs4kvU'},
     {'author': 'AR Specialist',
      'channel': 'AR Specialist',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:32](https://www.youtube.com/watch?v=OLFRzRe0L2A&t=332s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The sheer amount of payroll hours wasted just listening to hold music is '
              'staggering. And make no mistake, this is by design. It is meant to discourage '
              'facilities from fighting for their rightful revenue.',
      'timestamp': 332,
      'timestamp_label': '[00:05:32]',
      'timestamp_seconds': 332,
      'tip': 'The sheer amount of payroll hours wasted just listening to hold music is '
             'staggering. And make no mistake, this is by design. It is meant to discourage '
             'facilities from fighting for their rightful revenue.',
      'title': 'SCA 2027 Blueprint: Protect Out-of-Network Revenue Before It Gets Recouped (AR '
               'Specialist)',
      'url': 'https://www.youtube.com/watch?v=OLFRzRe0L2A&t=332s',
      'video_id': 'OLFRzRe0L2A'},
     {'author': 'Contempo Coding',
      'channel': 'Contempo Coding',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:25](https://www.youtube.com/watch?v=pG2R1NwUlro&t=325s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A lot of large organizations providers will capture a good amount of like '
              "office visit charges because there's just so many of them uh and the risk.",
      'timestamp': 325,
      'timestamp_label': '[00:05:25]',
      'timestamp_seconds': 325,
      'tip': 'A lot of large organizations providers will capture a good amount of like office '
             "visit charges because there's just so many of them uh and the risk.",
      'title': 'What is the Revenue Cycle in Medical Billing and Coding? (RCM Basics '
               'Explained) (Contempo Coding)',
      'url': 'https://www.youtube.com/watch?v=pG2R1NwUlro&t=325s',
      'video_id': 'pG2R1NwUlro'},
     {'author': 'Dr. Glaucomflecken',
      'channel': 'Dr. Glaucomflecken',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:37](https://www.youtube.com/watch?v=FqwonCk1DK8&t=37s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Hey anesthesia oh hey emergency hey we just had a big trauma come in can you '
              "help us out real quick oh yeah of course yeah let's go all right the tube is in "
              "I'll let you guys take it from here.",
      'timestamp': 37,
      'timestamp_label': '[00:00:37]',
      'timestamp_seconds': 37,
      'tip': 'Hey anesthesia oh hey emergency hey we just had a big trauma come in can you '
             "help us out real quick oh yeah of course yeah let's go all right the tube is in "
             "I'll let you guys take it from here.",
      'title': 'Anesthesia Helps Out Emergency Medicine (Dr. Glaucomflecken)',
      'url': 'https://www.youtube.com/watch?v=FqwonCk1DK8&t=37s',
      'video_id': 'FqwonCk1DK8'},
     {'author': 'NextChapter',
      'channel': 'NextChapter',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:37](https://www.youtube.com/watch?v=p0ekuvIETYc&t=1477s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Paid they're not going to take out FICA and taxes and Social Security so that "
              "is the risk of not using the tax return you don't get any of those later but "
              'there are other reasons.',
      'timestamp': 1477,
      'timestamp_label': '[00:24:37]',
      'timestamp_seconds': 1477,
      'tip': "Paid they're not going to take out FICA and taxes and Social Security so that is "
             "the risk of not using the tax return you don't get any of those later but there "
             'are other reasons.',
      'title': 'IDR Account Adjustment (NextChapter)',
      'url': 'https://www.youtube.com/watch?v=p0ekuvIETYc&t=1477s',
      'video_id': 'p0ekuvIETYc'},
     {'author': 'Talisman Solutions',
      'channel': 'Talisman Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:41](https://www.youtube.com/watch?v=Zf9f4f3lmAw&t=101s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That turns a static aging list into a managed action list. Book a free Talisman '
              'AR audit to turn a sample aging list into an action list.',
      'timestamp': 101,
      'timestamp_label': '[00:01:41]',
      'timestamp_seconds': 101,
      'tip': 'That turns a static aging list into a managed action list. Book a free Talisman '
             'AR audit to turn a sample aging list into an action list.',
      'title': '3 Unpaid Claims, 3 Different Next Actions | A/R Audit Walkthrough (Talisman '
               'Solutions)',
      'url': 'https://www.youtube.com/watch?v=Zf9f4f3lmAw&t=101s',
      'video_id': 'Zf9f4f3lmAw'},
     {'author': 'WFAA',
      'channel': 'WFAA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=_ofpUW91u8o&t=20s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'IT IS CALLED SURPRISE THE MIDDLE. IT IS CALLED SURPRISE MEDICAL IT IS CALLED '
              'SURPRISE MEDICAL IT IS CALLED SURPRISE MEDICAL BUILDING. EXPERT SAYS IT HAPPENS '
              'BUILDING. EXPERT SAYS IT HAPPENS TO BUILDING.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'IT IS CALLED SURPRISE THE MIDDLE. IT IS CALLED SURPRISE MEDICAL IT IS CALLED '
             'SURPRISE MEDICAL IT IS CALLED SURPRISE MEDICAL BUILDING. EXPERT SAYS IT HAPPENS '
             'BUILDING. EXPERT SAYS IT HAPPENS TO BUILDING.',
      'title': 'Surprise medical billing will be banished in Texas starting Jan. 1 (WFAA)',
      'url': 'https://www.youtube.com/watch?v=_ofpUW91u8o&t=20s',
      'video_id': '_ofpUW91u8o'}],
 6: [{'author': 'HaloMD',
      'channel': 'HaloMD',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:47:30](https://www.youtube.com/watch?v=oEWBNDsvXOQ&t=2850s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh, a great example is that if a a build charge of $1,000 uh is is first '
              'assessed and uh the arbitration award uh actually goes in in favor of the '
              "physician, but is for $800. Well, that's still an amount less than the original "
              'bill charge.',
      'timestamp': 2850,
      'timestamp_label': '[00:47:30]',
      'timestamp_seconds': 2850,
      'tip': 'Uh, a great example is that if a a build charge of $1,000 uh is is first '
             'assessed and uh the arbitration award uh actually goes in in favor of the '
             "physician, but is for $800. Well, that's still an amount less than the original "
             'bill charge.',
      'title': 'The Truth Is in the Data: Myths, Reality & What’s Next in IDR Under the NSA | '
               'Becker’s x HaloMD (HaloMD)',
      'url': 'https://www.youtube.com/watch?v=oEWBNDsvXOQ&t=2850s',
      'video_id': 'oEWBNDsvXOQ'},
     {'author': 'AS DESIGNED | Risk & Insurance Stories',
      'channel': 'AS DESIGNED | Risk & Insurance Stories',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:19](https://www.youtube.com/watch?v=w_lpas-cNkc&t=319s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That was the 6th of January. Ordinary life followed, work, school runs, the '
              'mortgage. Then, in the week of the 10th of February, two envelopes arrived in '
              'the same week, six weeks after the ambulance had gone. Start with the first of '
              'the three reasons, a list.',
      'timestamp': 319,
      'timestamp_label': '[00:05:19]',
      'timestamp_seconds': 319,
      'tip': 'That was the 6th of January. Ordinary life followed, work, school runs, the '
             'mortgage. Then, in the week of the 10th of February, two envelopes arrived in '
             'the same week, six weeks after the ambulance had gone. Start with the first of '
             'the three reasons, a list.',
      'title': 'The Law Stops Surprise Medical Bills. Why Not the Ambulance? (AS DESIGNED | '
               'Risk & Insurance Stories)',
      'url': 'https://www.youtube.com/watch?v=w_lpas-cNkc&t=319s',
      'video_id': 'w_lpas-cNkc'},
     {'author': 'Center on Health Insurance Reforms',
      'channel': 'Center on Health Insurance Reforms',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:33:47](https://www.youtube.com/watch?v=wJkWOgxZj6k&t=2027s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So 6% of claims are adding that much to healthcare trend. 5 million in IDR '
              'awards in all of 2025. It paid more than $6 million in the first half of 2026 '
              'alone and is on pace for $12 million. And all of that mostly comes from one '
              'single ER operator.',
      'timestamp': 2027,
      'timestamp_label': '[00:33:47]',
      'timestamp_seconds': 2027,
      'tip': 'So 6% of claims are adding that much to healthcare trend. 5 million in IDR '
             'awards in all of 2025. It paid more than $6 million in the first half of 2026 '
             'alone and is on pace for $12 million. And all of that mostly comes from one '
             'single ER operator.',
      'title': 'Runaway Costs: Getting the No Surprises Act Back on Track (Center on Health '
               'Insurance Reforms)',
      'url': 'https://www.youtube.com/watch?v=wJkWOgxZj6k&t=2027s',
      'video_id': 'wJkWOgxZj6k'},
     {'author': 'TopMedTalk',
      'channel': 'TopMedTalk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:37](https://www.youtube.com/watch?v=0BcGdvWG_UI&t=817s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Elevance Health to their employer sponsors in which they disclosed to their '
              "employer sponsors, apparently for the first time, it it seems, that they've "
              'been withholding payment for arbitration awards on behalf of their employer '
              'sponsors.',
      'timestamp': 817,
      'timestamp_label': '[00:13:37]',
      'timestamp_seconds': 817,
      'tip': 'Elevance Health to their employer sponsors in which they disclosed to their '
             "employer sponsors, apparently for the first time, it it seems, that they've been "
             'withholding payment for arbitration awards on behalf of their employer sponsors.',
      'title': 'ANESTHESIOLOGY 2026: No Surprises Act, IDR, and Out-of-Network Spending '
               '(TopMedTalk)',
      'url': 'https://www.youtube.com/watch?v=0BcGdvWG_UI&t=817s',
      'video_id': '0BcGdvWG_UI'},
     {'author': 'Health Weave RCM LLC',
      'channel': 'Health Weave RCM LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:19](https://www.youtube.com/watch?v=bPFE9F4Y_Y4&t=559s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'First, match the money to the explanation. The total deposited should match the '
              "total on the remittance. If it doesn't, find out why before you close the "
              'batch. Second, post each amount to the right bucket.',
      'timestamp': 559,
      'timestamp_label': '[00:09:19]',
      'timestamp_seconds': 559,
      'tip': 'First, match the money to the explanation. The total deposited should match the '
             "total on the remittance. If it doesn't, find out why before you close the batch. "
             'Second, post each amount to the right bucket.',
      'title': 'EOB vs ERA CARC RARC Codes Explained | Medical Billing Class 4 (Health Weave '
               'RCM LLC)',
      'url': 'https://www.youtube.com/watch?v=bPFE9F4Y_Y4&t=559s',
      'video_id': 'bPFE9F4Y_Y4'},
     {'author': 'RCM Mastery',
      'channel': 'RCM Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:29](https://www.youtube.com/watch?v=okx8geMd-gU&t=269s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The game is only truly won when that account balance hits zero. So after all '
              "that, what's the game plan to win? Accurate data is your absolute superpower. "
              'Always, always get approval first. Clean coding means fast cash. Think of every '
              'denial as a lesson.',
      'timestamp': 269,
      'timestamp_label': '[00:04:29]',
      'timestamp_seconds': 269,
      'tip': 'The game is only truly won when that account balance hits zero. So after all '
             "that, what's the game plan to win? Accurate data is your absolute superpower. "
             'Always, always get approval first. Clean coding means fast cash. Think of every '
             'denial as a lesson.',
      'title': 'Part 1 || Complete RCM Workflow Explained | From Patient Registration to '
               'Payment (RCM Mastery)',
      'url': 'https://www.youtube.com/watch?v=okx8geMd-gU&t=269s',
      'video_id': 'okx8geMd-gU'},
     {'author': 'CMSHHSgov',
      'channel': 'CMSHHSgov',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:11](https://www.youtube.com/watch?v=cw4MI_h6Gns&t=371s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'When selecting a batched dispute, a modal will appear with a list of criteria '
              'that will help determine if the disputes qualify for the batching process. '
              'Select Yes or No to make your selection.',
      'timestamp': 371,
      'timestamp_label': '[00:06:11]',
      'timestamp_seconds': 371,
      'tip': 'When selecting a batched dispute, a modal will appear with a list of criteria '
             'that will help determine if the disputes qualify for the batching process. '
             'Select Yes or No to make your selection.',
      'title': 'Notice of IDR Initiation Web Form Demo (CMSHHSgov)',
      'url': 'https://www.youtube.com/watch?v=cw4MI_h6Gns&t=371s',
      'video_id': 'cw4MI_h6Gns'},
     {'author': 'The Doctors Lounge',
      'channel': 'The Doctors Lounge',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:42](https://www.youtube.com/watch?v=QITUqT322Iw&t=942s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I mean there there was no prohibition. So California, like I say, in 2008 2009 '
              'was one of the first states to address it. The Supreme Court in a case called '
              'the prospect decision addressed balance billing in the context of emergency '
              'medicine.',
      'timestamp': 942,
      'timestamp_label': '[00:15:42]',
      'timestamp_seconds': 942,
      'tip': 'I mean there there was no prohibition. So California, like I say, in 2008 2009 '
             'was one of the first states to address it. The Supreme Court in a case called '
             'the prospect decision addressed balance billing in the context of emergency '
             'medicine.',
      'title': 'Ed Gaines: How Independent Physicians Finally Got Leverage Against Insurance '
               'Companies (The Doctors Lounge)',
      'url': 'https://www.youtube.com/watch?v=QITUqT322Iw&t=942s',
      'video_id': 'QITUqT322Iw'},
     {'author': 'Ryan Downs',
      'channel': 'Ryan Downs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:56](https://www.youtube.com/watch?v=0BGnlP4Q71M&t=176s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're about to get surgery. For all intents and purposes, you thought you were "
              'in network, but the anesthesiologist just happens to be out. Happens more '
              "frequently than we know. So, yeah, you're you're not getting in an air "
              'ambulance by choice.',
      'timestamp': 176,
      'timestamp_label': '[00:02:56]',
      'timestamp_seconds': 176,
      'tip': "You're about to get surgery. For all intents and purposes, you thought you were "
             'in network, but the anesthesiologist just happens to be out. Happens more '
             "frequently than we know. So, yeah, you're you're not getting in an air ambulance "
             'by choice.',
      'title': 'Mini Episode: Explaining What Accounts Qualify for the IDR Process with Adam '
               'Cartabiano (Ryan Downs)',
      'url': 'https://www.youtube.com/watch?v=0BGnlP4Q71M&t=176s',
      'video_id': '0BGnlP4Q71M'},
     {'author': 'UtreatiBill LLC',
      'channel': 'UtreatiBill LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=_0Dt6rewEvU&t=111s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Everything we do is fully HIPAA compliant, so patient data stays protected. '
              'Pricing starts at just 2% with no heavy overhead or extra staff. Find [snorts] '
              "where you're losing revenue. Book your free consultation at utreatibil.",
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': 'Everything we do is fully HIPAA compliant, so patient data stays protected. '
             'Pricing starts at just 2% with no heavy overhead or extra staff. Find [snorts] '
             "where you're losing revenue. Book your free consultation at utreatibil.",
      'title': 'Stop Losing Money! Revenue Cycle Management (UtreatiBill LLC)',
      'url': 'https://www.youtube.com/watch?v=_0Dt6rewEvU&t=111s',
      'video_id': '_0Dt6rewEvU'},
     {'author': 'MBC RCM',
      'channel': 'MBC RCM',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:45](https://www.youtube.com/watch?v=VoQc5Oh8ot4&t=405s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'First, a paid claim in the same episode of care is your absolute strongest '
              'evidence when disputing a records request. Second, your authorization and '
              'single case agreement details should be on file and cited on every call.',
      'timestamp': 405,
      'timestamp_label': '[00:06:45]',
      'timestamp_seconds': 405,
      'tip': 'First, a paid claim in the same episode of care is your absolute strongest '
             'evidence when disputing a records request. Second, your authorization and single '
             'case agreement details should be on file and cited on every call.',
      'title': 'Medical Billing Denials: The 45-Minute Strategy That Gets Results (MBC RCM)',
      'url': 'https://www.youtube.com/watch?v=VoQc5Oh8ot4&t=405s',
      'video_id': 'VoQc5Oh8ot4'},
     {'author': 'Inlera University',
      'channel': 'Inlera University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=3JOMCnMqhvI&t=75s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Company might have a full very detailed a comprehensive list of what they would '
              'pay for a service but that is only if the patients benefits actually will.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': 'Company might have a full very detailed a comprehensive list of what they would '
             'pay for a service but that is only if the patients benefits actually will.',
      'title': 'What is the Allowed Amount? | Healthcare Medical Billing (Inlera University)',
      'url': 'https://www.youtube.com/watch?v=3JOMCnMqhvI&t=75s',
      'video_id': '3JOMCnMqhvI'},
     {'author': 'Nate Page',
      'channel': 'Nate Page',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:17](https://www.youtube.com/watch?v=rdwGJdKffpI&t=497s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Exactly what to expect with payment best of luck to you in your journey as you '
              "find a therapist and please let us know if there's any way that we can help you "
              'in that process take care.',
      'timestamp': 497,
      'timestamp_label': '[00:08:17]',
      'timestamp_seconds': 497,
      'tip': 'Exactly what to expect with payment best of luck to you in your journey as you '
             "find a therapist and please let us know if there's any way that we can help you "
             'in that process take care.',
      'title': 'Out of Network Therapist | Superbills and Health Insurance (Nate Page)',
      'url': 'https://www.youtube.com/watch?v=rdwGJdKffpI&t=497s',
      'video_id': 'rdwGJdKffpI'},
     {'author': 'Amazing Charts',
      'channel': 'Amazing Charts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:03](https://www.youtube.com/watch?v=eKRUeJa5ZzQ&t=183s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The stresses off of your office and allow somebody else that this is all they '
              "do and they're experts at it to follow up on your bills to make sure that the "
              "claims get paid on the first submission so you're not chasing things.",
      'timestamp': 183,
      'timestamp_label': '[00:03:03]',
      'timestamp_seconds': 183,
      'tip': 'The stresses off of your office and allow somebody else that this is all they do '
             "and they're experts at it to follow up on your bills to make sure that the "
             "claims get paid on the first submission so you're not chasing things.",
      'title': 'Webinar: Amazing Charts Revenue Cycle Management (RCM) (Amazing Charts)',
      'url': 'https://www.youtube.com/watch?v=eKRUeJa5ZzQ&t=183s',
      'video_id': 'eKRUeJa5ZzQ'},
     {'author': 'AR Sid',
      'channel': 'AR Sid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=3ny6SM1xecc&t=15s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'फर्स्ट वीडियो एंड हियर इज दी स्टेप ऑफ आरसीएम साइकिल। इन दिस वीडियो वी आर लुकिंग '
              'फॉर दी स्टेप्स एंड दी ब्लॉक। आई मीन हम लोग इसको स्टेप्स नहीं ब्लॉक्स की.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'फर्स्ट वीडियो एंड हियर इज दी स्टेप ऑफ आरसीएम साइकिल। इन दिस वीडियो वी आर लुकिंग '
             'फॉर दी स्टेप्स एंड दी ब्लॉक। आई मीन हम लोग इसको स्टेप्स नहीं ब्लॉक्स की.',
      'title': 'Learn Complete RCM Cycle in 5 Minutes | US Healthcare | Appointment to Payment '
               '& Denials (AR Sid)',
      'url': 'https://www.youtube.com/watch?v=3ny6SM1xecc&t=15s',
      'video_id': '3ny6SM1xecc'}],
 7: [{'author': 'Ben Martin',
      'channel': 'Ben Martin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=dTrA6r3pGyE&t=35s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The new IDR process levels the playing field with binding arbitration, allowing '
              'providers to submit their own payment offers and contest rates based on factors '
              'beyond just the qualifying payment amount.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'The new IDR process levels the playing field with binding arbitration, allowing '
             'providers to submit their own payment offers and contest rates based on factors '
             'beyond just the qualifying payment amount.',
      'title': 'CoGenetix & ANS Solutions- OON IDR Webinar (Ben Martin)',
      'url': 'https://www.youtube.com/watch?v=dTrA6r3pGyE&t=35s',
      'video_id': 'dTrA6r3pGyE'},
     {'author': 'KLGatesLaw',
      'channel': 'KLGatesLaw',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:34](https://www.youtube.com/watch?v=NwapzBNojY0&t=94s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And since its implementation in 2022, out-of-network providers have submitted '
              'hundreds of thousands of claims under the current baseball style arbitration '
              'process, which is significantly higher than the agencies originally '
              'anticipated.',
      'timestamp': 94,
      'timestamp_label': '[00:01:34]',
      'timestamp_seconds': 94,
      'tip': 'And since its implementation in 2022, out-of-network providers have submitted '
             'hundreds of thousands of claims under the current baseball style arbitration '
             'process, which is significantly higher than the agencies originally anticipated.',
      'title': 'No Surprises Act Check-In: The Latest Changes to the IDR Process (KLGatesLaw)',
      'url': 'https://www.youtube.com/watch?v=NwapzBNojY0&t=94s',
      'video_id': 'NwapzBNojY0'},
     {'author': 'American Medical Association (AMA)',
      'channel': 'American Medical Association (AMA)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:08](https://www.youtube.com/watch?v=6_ODgJ97UtA&t=1748s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'ADR process is proceeding under the rule established by Texas Medical '
              'association, which is that this rule, that deference to Cuba is not on the '
              'books anymore, that the entire process will be determined based solely on the '
              'factors outlined in the statute.',
      'timestamp': 1748,
      'timestamp_label': '[00:29:08]',
      'timestamp_seconds': 1748,
      'tip': 'ADR process is proceeding under the rule established by Texas Medical '
             'association, which is that this rule, that deference to Cuba is not on the books '
             'anymore, that the entire process will be determined based solely on the factors '
             'outlined in the statute.',
      'title': 'Out-of-network payment process under the No Surprises Act (American Medical '
               'Association (AMA))',
      'url': 'https://www.youtube.com/watch?v=6_ODgJ97UtA&t=1748s',
      'video_id': '6_ODgJ97UtA'},
     {'author': 'Paragon Health Institute',
      'channel': 'Paragon Health Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:57:00](https://www.youtube.com/watch?v=PpfXacIXrAc&t=3420s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Pilgrim mentioned, this does not represent a majority of the IDR disputes. But '
              "these high award outliers are driving up costs, and they're distorting the "
              'system. And they could be an incentive for some to use arbitration as as the '
              'sort of payment of first resort.',
      'timestamp': 3420,
      'timestamp_label': '[00:57:00]',
      'timestamp_seconds': 3420,
      'tip': 'Pilgrim mentioned, this does not represent a majority of the IDR disputes. But '
             "these high award outliers are driving up costs, and they're distorting the "
             'system. And they could be an incentive for some to use arbitration as as the '
             'sort of payment of first resort.',
      'title': 'Fixing the No Surprises Act: Scaling Back and Reforming the Federal '
               'Arbitration System (Paragon Health Institute)',
      'url': 'https://www.youtube.com/watch?v=PpfXacIXrAc&t=3420s',
      'video_id': 'PpfXacIXrAc'},
     {'author': 'Staffingly, Inc',
      'channel': 'Staffingly, Inc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=ASHyX7v13Eo&t=70s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '300 times its designed capacity. Yet, wrapped inside this broken system is a '
              'mathematical reality that practice owners cannot ignore. Participating in this '
              'process yields massive financial returns. This chart compares baseline payments '
              'to arbitration outcomes.',
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': '300 times its designed capacity. Yet, wrapped inside this broken system is a '
             'mathematical reality that practice owners cannot ignore. Participating in this '
             'process yields massive financial returns. This chart compares baseline payments '
             'to arbitration outcomes.',
      'title': 'NSA IDR Dispute Filing Services for Medical Practices | Recover What Insurers '
               'Owe (Staffingly, Inc)',
      'url': 'https://www.youtube.com/watch?v=ASHyX7v13Eo&t=70s',
      'video_id': 'ASHyX7v13Eo'},
     {'author': 'Ryan Downs',
      'channel': 'Ryan Downs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:51](https://www.youtube.com/watch?v=7lqb5ev54mA&t=171s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And you have 30 days to kind of go through that settlement process. You have to '
              'go through that process because you have to show proof that you went through '
              'that process in order to get to the official arbitration step.',
      'timestamp': 171,
      'timestamp_label': '[00:02:51]',
      'timestamp_seconds': 171,
      'tip': 'And you have 30 days to kind of go through that settlement process. You have to '
             'go through that process because you have to show proof that you went through '
             'that process in order to get to the official arbitration step.',
      'title': 'Mini Episode: Breaking Down The IDR Process with Adam Cartabiano (Ryan Downs)',
      'url': 'https://www.youtube.com/watch?v=7lqb5ev54mA&t=171s',
      'video_id': '7lqb5ev54mA'},
     {'author': 'Zelis Healthcare',
      'channel': 'Zelis Healthcare',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:04](https://www.youtube.com/watch?v=D63N2KsthY8&t=304s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Talk a little bit about the technical assistant assistance later on. It looks '
              'like another layer on top of uh the R process which is not in the regulations. '
              "It's not in the statute but seems to allow for a resubmission of claims based "
              'on errors.',
      'timestamp': 304,
      'timestamp_label': '[00:05:04]',
      'timestamp_seconds': 304,
      'tip': 'Talk a little bit about the technical assistant assistance later on. It looks '
             'like another layer on top of uh the R process which is not in the regulations. '
             "It's not in the statute but seems to allow for a resubmission of claims based on "
             'errors.',
      'title': 'No Surprises Act & IDR Updates | What Healthcare Payers & Providers Need to '
               'Know (Zelis Healthcare)',
      'url': 'https://www.youtube.com/watch?v=D63N2KsthY8&t=304s',
      'video_id': 'D63N2KsthY8'},
     {'author': 'RCM Navigator',
      'channel': 'RCM Navigator',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:05](https://www.youtube.com/watch?v=ETPWERdn_jE&t=125s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Denied claims are a major financial hurdle. Reviewing and addressing denials '
              'promptly through appeal processes helps recover lost revenue. Step 10, patient '
              'billing and collections. After insurance payments, patients are build for any '
              'remaining balances.',
      'timestamp': 125,
      'timestamp_label': '[00:02:05]',
      'timestamp_seconds': 125,
      'tip': 'Denied claims are a major financial hurdle. Reviewing and addressing denials '
             'promptly through appeal processes helps recover lost revenue. Step 10, patient '
             'billing and collections. After insurance payments, patients are build for any '
             'remaining balances.',
      'title': 'Break down of 13 steps of US Medical RCM (Revenue Cycle Management) (RCM '
               'Navigator)',
      'url': 'https://www.youtube.com/watch?v=ETPWERdn_jE&t=125s',
      'video_id': 'ETPWERdn_jE'},
     {'author': 'American Medical Association (AMA)',
      'channel': 'American Medical Association (AMA)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:45](https://www.youtube.com/watch?v=Ie5ARcGEY1g&t=225s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And we'll go through each of these steps in the next slides. Step one is "
              'patient registration. And this is when the practice collects the basic patient '
              'demographic information and inputs that into the system.',
      'timestamp': 225,
      'timestamp_label': '[00:03:45]',
      'timestamp_seconds': 225,
      'tip': "And we'll go through each of these steps in the next slides. Step one is patient "
             'registration. And this is when the practice collects the basic patient '
             'demographic information and inputs that into the system.',
      'title': 'Revenue Cycle Management (American Medical Association (AMA))',
      'url': 'https://www.youtube.com/watch?v=Ie5ARcGEY1g&t=225s',
      'video_id': 'Ie5ARcGEY1g'},
     {'author': 'JobRath',
      'channel': 'JobRath',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=WCjl2ZOU1ec&t=98s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "AR aging, and revenue loss. That's why every department in the revenue cycle is "
              'connected. If one step fails, it impacts the entire reimbursement process.',
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': "AR aging, and revenue loss. That's why every department in the revenue cycle is "
             'connected. If one step fails, it impacts the entire reimbursement process.',
      'title': 'What Is Revenue Cycle Management (RCM)? Interview Answer That Gets You Hired '
               '(JobRath)',
      'url': 'https://www.youtube.com/watch?v=WCjl2ZOU1ec&t=98s',
      'video_id': 'WCjl2ZOU1ec'},
     {'author': 'Bill Fighter',
      'channel': 'Bill Fighter',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:48](https://www.youtube.com/watch?v=OWN7CBskcIQ&t=468s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Step four, get it in writing. This is huge. Before you pay one penny, get the '
              'agreement in writing, usually by email.',
      'timestamp': 468,
      'timestamp_label': '[00:07:48]',
      'timestamp_seconds': 468,
      'tip': 'Step four, get it in writing. This is huge. Before you pay one penny, get the '
             'agreement in writing, usually by email.',
      'title': 'Out-of-Network Bill Shock? Negotiate It Down 60% With This Script (Bill '
               'Fighter)',
      'url': 'https://www.youtube.com/watch?v=OWN7CBskcIQ&t=468s',
      'video_id': 'OWN7CBskcIQ'},
     {'author': 'Fulcrum Strategies',
      'channel': 'Fulcrum Strategies',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:33](https://www.youtube.com/watch?v=f9Q5ImwNeS0&t=213s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Texas Medical Association representing Physicians all over the country and some '
              'guidance that was put out by CMS.',
      'timestamp': 213,
      'timestamp_label': '[00:03:33]',
      'timestamp_seconds': 213,
      'tip': 'Texas Medical Association representing Physicians all over the country and some '
             'guidance that was put out by CMS.',
      'title': 'Ep. 61 - Breaking down the impacts of the TMA 3 ruling (Fulcrum Strategies)',
      'url': 'https://www.youtube.com/watch?v=f9Q5ImwNeS0&t=213s',
      'video_id': 'f9Q5ImwNeS0'},
     {'author': 'Dr. Tamir, MD',
      'channel': 'Dr. Tamir, MD',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=dfcTAfDPDqw&t=100s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I thought I was going to go into but eventually I changed my mind and that's "
              'really how I landed on anesthesia which is to me the perfect specialty.',
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': "I thought I was going to go into but eventually I changed my mind and that's "
             'really how I landed on anesthesia which is to me the perfect specialty.',
      'title': 'The three specialties I couldn’t do #anesthesia #doctor #medschool #medicine '
               '#premed (Dr. Tamir, MD)',
      'url': 'https://www.youtube.com/watch?v=dfcTAfDPDqw&t=100s',
      'video_id': 'dfcTAfDPDqw'},
     {'author': 'Audio Webinars',
      'channel': 'Audio Webinars',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=T6j0qhLPruk&t=77s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Uh there's going to be a lot of uh there are a lot of unanswered questions I "
              'would recommend strongly that at the end of this presentation if I cannot '
              'answer any questions uh to email me or to webinar planet and within 24 hours I '
              'will get you an answer.',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': "Uh there's going to be a lot of uh there are a lot of unanswered questions I "
             'would recommend strongly that at the end of this presentation if I cannot answer '
             'any questions uh to email me or to webinar planet and within 24 hours I will get '
             'you an answer.',
      'title': 'Federal No Surprises Act – The IDR Process, Good Faith Estimates, and What '
               'Providers Need to Know (Audio Webinars)',
      'url': 'https://www.youtube.com/watch?v=T6j0qhLPruk&t=77s',
      'video_id': 'T6j0qhLPruk'},
     {'author': 'Azeem khan Watanyar Official',
      'channel': 'Azeem khan Watanyar Official',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:00](https://www.youtube.com/watch?v=PPo7dGhm69c&t=480s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '40 مليار مطالبة رعاية صحية لأكثر من 10,000 خدمة في جميع أنحاء الولايات المتحدة. '
              '"Fair Health" معدلاً تقديرياً في الولايات المتحدة لأكثر من 10,000 خدمة.',
      'timestamp': 480,
      'timestamp_label': '[00:08:00]',
      'timestamp_seconds': 480,
      'tip': '40 مليار مطالبة رعاية صحية لأكثر من 10,000 خدمة في جميع أنحاء الولايات المتحدة. '
             '"Fair Health" معدلاً تقديرياً في الولايات المتحدة لأكثر من 10,000 خدمة.',
      'title': 'Ch # 3- What is Out-of-Network Billing | How to resolve Out-of-Network denial '
               'in medical billing (Azeem khan Watanyar Official)',
      'url': 'https://www.youtube.com/watch?v=PPo7dGhm69c&t=480s',
      'video_id': 'PPo7dGhm69c'}],
 8: [{'author': 'Long Reads, Explained',
      'channel': 'Long Reads, Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:52](https://www.youtube.com/watch?v=nJ5Tz7G_LA8&t=712s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The law does give the government a tool. It authorizes the Trump administration '
              'to fine health insurers one hundred dollars for each day they do not pay an '
              'arbitration award. So far, it has not issued a single penalty.',
      'timestamp': 712,
      'timestamp_label': '[00:11:52]',
      'timestamp_seconds': 712,
      'tip': 'The law does give the government a tool. It authorizes the Trump administration '
             'to fine health insurers one hundred dollars for each day they do not pay an '
             'arbitration award. So far, it has not issued a single penalty.',
      'title': 'No Surprises Act: Nearly 30% of Awards Unpaid by Insurers (Long Reads, '
               'Explained)',
      'url': 'https://www.youtube.com/watch?v=nJ5Tz7G_LA8&t=712s',
      'video_id': 'nJ5Tz7G_LA8'},
     {'author': 'Lido',
      'channel': 'Lido',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:54](https://www.youtube.com/watch?v=NHWPEtUOyK0&t=354s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'IDR route, we also take it through negotiation, batching, we do all the admin '
              'and operational paperwork and filing work, including pushing data and '
              'documentation to the new centralized IDR gateway, which no longer offers an API '
              'infrastructure.',
      'timestamp': 354,
      'timestamp_label': '[00:05:54]',
      'timestamp_seconds': 354,
      'tip': 'IDR route, we also take it through negotiation, batching, we do all the admin '
             'and operational paperwork and filing work, including pushing data and '
             'documentation to the new centralized IDR gateway, which no longer offers an API '
             'infrastructure.',
      'title': 'Is This Claim Eligible for IDR? How to Check Before You File (No Surprises '
               'Act) (Lido)',
      'url': 'https://www.youtube.com/watch?v=NHWPEtUOyK0&t=354s',
      'video_id': 'NHWPEtUOyK0'},
     {'author': 'HIPAA TV',
      'channel': 'HIPAA TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:44](https://www.youtube.com/watch?v=T99RB14fdY4&t=1064s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The actual amount exceeds the expected amount by 400 or more so 400 or more in '
              'excess of the good faith estimate will trigger the arbitration provision of the '
              'no surprises act.',
      'timestamp': 1064,
      'timestamp_label': '[00:17:44]',
      'timestamp_seconds': 1064,
      'tip': 'The actual amount exceeds the expected amount by 400 or more so 400 or more in '
             'excess of the good faith estimate will trigger the arbitration provision of the '
             'no surprises act.',
      'title': 'No Surprises Act  Provider Training (HIPAA TV)',
      'url': 'https://www.youtube.com/watch?v=T99RB14fdY4&t=1064s',
      'video_id': 'T99RB14fdY4'},
     {'author': 'Idea Usher',
      'channel': 'Idea Usher',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=zULb0Uazje4&t=79s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Integrated medical billing software combined with EHR systems, allowing '
              'seamless data flow between clinical and billing operations. Cloud-based billing '
              'software accessible from anywhere with automatic updates, lower upfront costs, '
              'and improved scalability.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': 'Integrated medical billing software combined with EHR systems, allowing seamless '
             'data flow between clinical and billing operations. Cloud-based billing software '
             'accessible from anywhere with automatic updates, lower upfront costs, and '
             'improved scalability.',
      'title': 'How to Build Medical Billing & Claim Software [2026] | Medical Billing '
               'Software Development (Idea Usher)',
      'url': 'https://www.youtube.com/watch?v=zULb0Uazje4&t=79s',
      'video_id': 'zULb0Uazje4'},
     {'author': 'Bill Fighter',
      'channel': 'Bill Fighter',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:08](https://www.youtube.com/watch?v=1VtIU2oIxEY&t=188s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Happens to be out-of-network, they cannot bill you at out-of-network rates. '
              'Number three,  air ambulance services.',
      'timestamp': 188,
      'timestamp_label': '[00:03:08]',
      'timestamp_seconds': 188,
      'tip': 'Happens to be out-of-network, they cannot bill you at out-of-network rates. '
             'Number three,  air ambulance services.',
      'title': 'No Surprises Act Exposed - How to Kill an $8,472 Surprise Bill (Bill Fighter)',
      'url': 'https://www.youtube.com/watch?v=1VtIU2oIxEY&t=188s',
      'video_id': '1VtIU2oIxEY'},
     {'author': 'Compliancy Group',
      'channel': 'Compliancy Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:49](https://www.youtube.com/watch?v=yI1fsZFZPwY&t=229s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Business associate agreements create a framework for secure data sharing while '
              'ensuring that Healthcare organizations take complete accountability for more '
              'information contact us at compliance e-group today.',
      'timestamp': 229,
      'timestamp_label': '[00:03:49]',
      'timestamp_seconds': 229,
      'tip': 'Business associate agreements create a framework for secure data sharing while '
             'ensuring that Healthcare organizations take complete accountability for more '
             'information contact us at compliance e-group today.',
      'title': 'What is a Business Associate Agreement (Compliancy Group)',
      'url': 'https://www.youtube.com/watch?v=yI1fsZFZPwY&t=229s',
      'video_id': 'yI1fsZFZPwY'},
     {'author': 'Xpert Billing Talk',
      'channel': 'Xpert Billing Talk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:21](https://www.youtube.com/watch?v=CwSXrQBZiOg&t=201s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "CMS didn't just lower the barriers to entry without tightening the operational "
              'screws. The workflow is actually substantially stricter now. It prevents '
              'exactly that kind of spamming. You see, the 30-day open negotiation clock now '
              'strictly starts based on portal date stamps.',
      'timestamp': 201,
      'timestamp_label': '[00:03:21]',
      'timestamp_seconds': 201,
      'tip': "CMS didn't just lower the barriers to entry without tightening the operational "
             'screws. The workflow is actually substantially stricter now. It prevents exactly '
             'that kind of spamming. You see, the 30-day open negotiation clock now strictly '
             'starts based on portal date stamps.',
      'title': 'Federal IDR Gateway Rules 2026: New Portal, Fees & Batching Changes (Xpert '
               'Billing Talk)',
      'url': 'https://www.youtube.com/watch?v=CwSXrQBZiOg&t=201s',
      'video_id': 'CwSXrQBZiOg'},
     {'author': 'HealthLeaders Media',
      'channel': 'HealthLeaders Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:38](https://www.youtube.com/watch?v=BKBNIfZ081U&t=578s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I said Epic has a tool other independent vendors have tools out there some '
              'clinical some more focused on the technical some both. Take advantage of it '
              "while you're focusing on the strategic because it is your bloodstream.",
      'timestamp': 578,
      'timestamp_label': '[00:09:38]',
      'timestamp_seconds': 578,
      'tip': 'I said Epic has a tool other independent vendors have tools out there some '
             'clinical some more focused on the technical some both. Take advantage of it '
             "while you're focusing on the strategic because it is your bloodstream.",
      'title': 'Revenue Cycle NOW: Strengthening Back-End Performance (HealthLeaders Media)',
      'url': 'https://www.youtube.com/watch?v=BKBNIfZ081U&t=578s',
      'video_id': 'BKBNIfZ081U'},
     {'author': 'RCMOpsPro',
      'channel': 'RCMOpsPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=Y-cwIjpRq9w&t=65s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If a doctor bills a CMS 1500 with an inpatient POS code, but the hospital '
              'forgets to bill the matching UB-04, the payer will flag the mismatch and deny '
              'both claims instantly. A basic data entry clerk relies on the software to catch '
              'these errors.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': 'If a doctor bills a CMS 1500 with an inpatient POS code, but the hospital '
             'forgets to bill the matching UB-04, the payer will flag the mismatch and deny '
             'both claims instantly. A basic data entry clerk relies on the software to catch '
             'these errors.',
      'title': 'CMS-1500 vs. UB-04 Explained: Mastering the Architecture of Billing | Created '
               'by Diego Samson (RCMOpsPro)',
      'url': 'https://www.youtube.com/watch?v=Y-cwIjpRq9w&t=65s',
      'video_id': 'Y-cwIjpRq9w'},
     {'author': 'The Claim Game X Practice Solutions',
      'channel': 'The Claim Game X Practice Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:09](https://www.youtube.com/watch?v=FE6Ns41GFH0&t=429s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And this brings us to the second tool. And we have this exclusive to our '
              "Hourglass members and it's called the guide to the components of an ERRA. The "
              'technical name for an ERRA is an 835 file.',
      'timestamp': 429,
      'timestamp_label': '[00:07:09]',
      'timestamp_seconds': 429,
      'tip': 'And this brings us to the second tool. And we have this exclusive to our '
             "Hourglass members and it's called the guide to the components of an ERRA. The "
             'technical name for an ERRA is an 835 file.',
      'title': 'Episode 29: Revenue Cycle Management Explained: Remittances, ERAs, and Portals '
               '(The Claim Game X Practice Solutions)',
      'url': 'https://www.youtube.com/watch?v=FE6Ns41GFH0&t=429s',
      'video_id': 'FE6Ns41GFH0'},
     {'author': 'P3Fusion',
      'channel': 'P3Fusion',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=IQXlcicB37I&t=100s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Compliant with NSA regulations and gain powerful insights through our reporting '
              'tools ready to transform your NSA dispute Management contact us today to learn '
              'how our solution can improve efficiency ensure compliance and give you full '
              'control over your dispute processes.',
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': 'Compliant with NSA regulations and gain powerful insights through our reporting '
             'tools ready to transform your NSA dispute Management contact us today to learn '
             'how our solution can improve efficiency ensure compliance and give you full '
             'control over your dispute processes.',
      'title': 'No Surprises Act Dispute Management Solution | IDR | P3Fusion (P3Fusion)',
      'url': 'https://www.youtube.com/watch?v=IQXlcicB37I&t=100s',
      'video_id': 'IQXlcicB37I'},
     {'author': 'David Hood -- Practical AI Engineering',
      'channel': 'David Hood -- Practical AI Engineering',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:31](https://www.youtube.com/watch?v=A7ARXTSHAk0&t=331s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Comes to like data processing and and data analysis and data processing means a '
              'bunch of different things you can get a 100x 10,000x the value the the.',
      'timestamp': 331,
      'timestamp_label': '[00:05:31]',
      'timestamp_seconds': 331,
      'tip': 'Comes to like data processing and and data analysis and data processing means a '
             'bunch of different things you can get a 100x 10,000x the value the the.',
      'title': 'RCM Revenue Cycle Management Medical AI LLM Case Studies (David Hood -- '
               'Practical AI Engineering)',
      'url': 'https://www.youtube.com/watch?v=A7ARXTSHAk0&t=331s',
      'video_id': 'A7ARXTSHAk0'},
     {'author': 'Athelas',
      'channel': 'Athelas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:20](https://www.youtube.com/watch?v=6p7H4Wqe_xQ&t=200s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Power your practice with healthcare's leading AI powered RCM platform and "
              'tenacious group of In-House billing experts discover how a FIS RCM can help you '
              'supercharge your workflows remove Band-Aid fixes and drive Revenue schedule a '
              'demo today.',
      'timestamp': 200,
      'timestamp_label': '[00:03:20]',
      'timestamp_seconds': 200,
      'tip': "Power your practice with healthcare's leading AI powered RCM platform and "
             'tenacious group of In-House billing experts discover how a FIS RCM can help you '
             'supercharge your workflows remove Band-Aid fixes and drive Revenue schedule a '
             'demo today.',
      'title': 'Athelas | Revenue Cycle Management Demo (Athelas)',
      'url': 'https://www.youtube.com/watch?v=6p7H4Wqe_xQ&t=200s',
      'video_id': '6p7H4Wqe_xQ'},
     {'author': 'PYA, PC',
      'channel': 'PYA, PC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:01](https://www.youtube.com/watch?v=j1DGgPw1__E&t=601s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You have to go through you would get on the other services at a waiver that is '
              'signed it has to be documented and they have to retain a copy of that notice '
              'and consent if we could have the next slide please.',
      'timestamp': 601,
      'timestamp_label': '[00:10:01]',
      'timestamp_seconds': 601,
      'tip': 'You have to go through you would get on the other services at a waiver that is '
             'signed it has to be documented and they have to retain a copy of that notice and '
             'consent if we could have the next slide please.',
      'title': '“No Surprises Act  The New Independent Dispute Resolution Process”   CPE '
               'Webinar (PYA, PC)',
      'url': 'https://www.youtube.com/watch?v=j1DGgPw1__E&t=601s',
      'video_id': 'j1DGgPw1__E'},
     {'author': "Becker's Hospital Review",
      'channel': "Becker's Hospital Review",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:55](https://www.youtube.com/watch?v=RJps0omOazk&t=655s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Time the legislator lands and comes through National Airport they're reminded "
              'of this issue so it is a front and center of everyone out in Washington DC.',
      'timestamp': 655,
      'timestamp_label': '[00:10:55]',
      'timestamp_seconds': 655,
      'tip': "Time the legislator lands and comes through National Airport they're reminded of "
             'this issue so it is a front and center of everyone out in Washington DC.',
      'title': 'Surprise Billing Legislation - Overview, Response, and Future Implications '
               "(Becker's Hospital Review)",
      'url': 'https://www.youtube.com/watch?v=RJps0omOazk&t=655s',
      'video_id': 'RJps0omOazk'}],
 9: [{'author': 'Covered USA',
      'channel': 'Covered USA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=zDmKmfxl84c&t=157s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ground ambulance services are not covered by the No Surprises Act at all. That '
              'is stated plainly in the federal guidance. So, a helicopter ride can be '
              'protected, while a ground ambulance ride may not be, depending on your state '
              'law and your plan.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': 'Ground ambulance services are not covered by the No Surprises Act at all. That '
             'is stated plainly in the federal guidance. So, a helicopter ride can be '
             'protected, while a ground ambulance ride may not be, depending on your state law '
             'and your plan.',
      'title': 'The Surprise Bill Ban: What the No Surprises Act Actually Covers — and the One '
               'Ambulance It Does Not (Covered USA)',
      'url': 'https://www.youtube.com/watch?v=zDmKmfxl84c&t=157s',
      'video_id': 'zDmKmfxl84c'},
     {'author': 'CollectionPro Services LLC',
      'channel': 'CollectionPro Services LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=Ahr00pn-Tiw&t=40s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Win, it ends when you collect. We review unpaid awards, pursue payers '
              'relentlessly, escalate compliance issues, and coordinate legal.',
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': 'Win, it ends when you collect. We review unpaid awards, pursue payers '
             'relentlessly, escalate compliance issues, and coordinate legal.',
      'title': 'Winning your IDR arbitration is only half the battle. Collecting your award is '
               'what really matters! (CollectionPro Services LLC)',
      'url': 'https://www.youtube.com/watch?v=Ahr00pn-Tiw&t=40s',
      'video_id': 'Ahr00pn-Tiw'},
     {'author': 'Problem Solved Lab',
      'channel': 'Problem Solved Lab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:41](https://www.youtube.com/watch?v=ofqIwNzp8lA&t=101s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Third, air ambulance transport. A helicopter or airplane medical flight from an '
              'out-of-network provider is covered and you owe only your in-network cost share. '
              'Now, the gaps and these matter. Ground ambulances are not covered by the '
              'federal law.',
      'timestamp': 101,
      'timestamp_label': '[00:01:41]',
      'timestamp_seconds': 101,
      'tip': 'Third, air ambulance transport. A helicopter or airplane medical flight from an '
             'out-of-network provider is covered and you owe only your in-network cost share. '
             'Now, the gaps and these matter. Ground ambulances are not covered by the federal '
             'law.',
      'title': 'The No Surprises Act Cut Your ER Bill Already — Did You Pay $1,300 Too Much? '
               '(2026) (Problem Solved Lab)',
      'url': 'https://www.youtube.com/watch?v=ofqIwNzp8lA&t=101s',
      'video_id': 'ofqIwNzp8lA'},
     {'author': 'Texas Business group on Health',
      'channel': 'Texas Business group on Health',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:39:35](https://www.youtube.com/watch?v=8zjJbZyS2j8&t=2375s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um uh but uh they're the they're not bringing claims under the federal No "
              "Surprises Act itself. They're bringing claims sort of under these using these "
              'state law theories. And courts have dealt with these claims in a couple '
              'different ways.',
      'timestamp': 2375,
      'timestamp_label': '[00:39:35]',
      'timestamp_seconds': 2375,
      'tip': "Um uh but uh they're the they're not bringing claims under the federal No "
             "Surprises Act itself. They're bringing claims sort of under these using these "
             'state law theories. And courts have dealt with these claims in a couple '
             'different ways.',
      'title': 'No Surprises Act IDR Challenge Webinar (Texas Business group on Health)',
      'url': 'https://www.youtube.com/watch?v=8zjJbZyS2j8&t=2375s',
      'video_id': '8zjJbZyS2j8'},
     {'author': 'Capital Autopsy',
      'channel': 'Capital Autopsy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:35](https://www.youtube.com/watch?v=PVUGwjJg-VI&t=575s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'To protect your family from healthcare billing arbitrage, here are three rules. '
              'Rule number one: Never pay an out-of-network emergency room, anesthesiology or '
              'air-ambulance bill at face value.',
      'timestamp': 575,
      'timestamp_label': '[00:09:35]',
      'timestamp_seconds': 575,
      'tip': 'To protect your family from healthcare billing arbitrage, here are three rules. '
             'Rule number one: Never pay an out-of-network emergency room, anesthesiology or '
             'air-ambulance bill at face value.',
      'title': 'In-Network Hospital, Out-of-Network Doctor: The Private Equity Trap (Capital '
               'Autopsy)',
      'url': 'https://www.youtube.com/watch?v=PVUGwjJg-VI&t=575s',
      'video_id': 'PVUGwjJg-VI'},
     {'author': 'Hospital Decoded',
      'channel': 'Hospital Decoded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:28](https://www.youtube.com/watch?v=kXzE5L4StBs&t=1288s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '73% of all the air ambulance helicopters in the country. Many of them are for '
              "profit. Some fly under contract to hospitals, wearing the hospital's brand. The "
              'logo on the tail then does not always tell you who owns the aircraft or who '
              'sends the bill.',
      'timestamp': 1288,
      'timestamp_label': '[00:21:28]',
      'timestamp_seconds': 1288,
      'tip': '73% of all the air ambulance helicopters in the country. Many of them are for '
             "profit. Some fly under contract to hospitals, wearing the hospital's brand. The "
             'logo on the tail then does not always tell you who owns the aircraft or who '
             'sends the bill.',
      'title': 'How Air Ambulances Actually Work (Hospital Decoded)',
      'url': 'https://www.youtube.com/watch?v=kXzE5L4StBs&t=1288s',
      'video_id': 'kXzE5L4StBs'},
     {'author': 'AHealthcareZ - Healthcare Finance Explained',
      'channel': 'AHealthcareZ - Healthcare Finance Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=6E_HRECi-t8&t=80s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '"Okay, well, what what amount are we going to pay here for you?" You know, the '
              'law didn\'t force them to be in network, but it said, "Okay, listen.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': '"Okay, well, what what amount are we going to pay here for you?" You know, the '
             'law didn\'t force them to be in network, but it said, "Okay, listen.',
      'title': 'No Surprises Act Independent Dispute Resolution Drives Up Healthcare Costs in '
               'America (AHealthcareZ - Healthcare Finance Explained)',
      'url': 'https://www.youtube.com/watch?v=6E_HRECi-t8&t=80s',
      'video_id': '6E_HRECi-t8'},
     {'author': 'IndeMed',
      'channel': 'IndeMed',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=YSVbYfiNgWE&t=21s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Been in contract with the insurance carrier. To no fault of the patient, the No '
              'Surprises Act ended  all of those concerns, ended the concerns that.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'Been in contract with the insurance carrier. To no fault of the patient, the No '
             'Surprises Act ended  all of those concerns, ended the concerns that.',
      'title': "The No Surprises Act Is Working — Here's How (IndeMed)",
      'url': 'https://www.youtube.com/watch?v=YSVbYfiNgWE&t=21s',
      'video_id': 'YSVbYfiNgWE'},
     {'author': 'Miller Johnson',
      'channel': 'Miller Johnson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:17](https://www.youtube.com/watch?v=EwlPyAVGU8k&t=257s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Federal and the state law and the answer was no and it said because the state '
              'law is going to govern state regulated plans where um.',
      'timestamp': 257,
      'timestamp_label': '[00:04:17]',
      'timestamp_seconds': 257,
      'tip': 'Federal and the state law and the answer was no and it said because the state '
             'law is going to govern state regulated plans where um.',
      'title': 'Michigan’s Surprise Billing Law:  What Providers and Health Plans Need to Know '
               '(Miller Johnson)',
      'url': 'https://www.youtube.com/watch?v=EwlPyAVGU8k&t=257s',
      'video_id': 'EwlPyAVGU8k'},
     {'author': 'RCMPRO',
      'channel': 'RCMPRO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:04](https://www.youtube.com/watch?v=6Lc5iQMx35E&t=544s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Field 27, accept assignment. Indicate whether the provider accepts assignment '
              "according to the payer's rules. Enter the total of all the service line charges "
              'from field 24. Enter any amount already paid, if applicable. Field 30, reserved '
              'for NUCC use.',
      'timestamp': 544,
      'timestamp_label': '[00:09:04]',
      'timestamp_seconds': 544,
      'tip': 'Field 27, accept assignment. Indicate whether the provider accepts assignment '
             "according to the payer's rules. Enter the total of all the service line charges "
             'from field 24. Enter any amount already paid, if applicable. Field 30, reserved '
             'for NUCC use.',
      'title': 'CMS-1500 Claim Form Explained | Complete Guide to Medical Billing | RCMPRO '
               '(RCMPRO)',
      'url': 'https://www.youtube.com/watch?v=6Lc5iQMx35E&t=544s',
      'video_id': '6Lc5iQMx35E'},
     {'author': 'KLGatesLaw',
      'channel': 'KLGatesLaw',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:30](https://www.youtube.com/watch?v=VbqFYBvnpas&t=390s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That the ACT had already established multiple factors that an arbitrator shall '
              'consider before the rules were prated those were the items that Steve.',
      'timestamp': 390,
      'timestamp_label': '[00:06:30]',
      'timestamp_seconds': 390,
      'tip': 'That the ACT had already established multiple factors that an arbitrator shall '
             'consider before the rules were prated those were the items that Steve.',
      'title': 'Navigating the Independent Dispute Resolution Process Under the No Surprises '
               'Act (KLGatesLaw)',
      'url': 'https://www.youtube.com/watch?v=VbqFYBvnpas&t=390s',
      'video_id': 'VbqFYBvnpas'},
     {'author': 'American Medical Association (AMA)',
      'channel': 'American Medical Association (AMA)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:30:50](https://www.youtube.com/watch?v=zyTkKRTBBEg&t=1850s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Voluntary compliance in the boxes there we see you know if it's an insurer "
              'issue most likely the insurance departments well in every state the insurance.',
      'timestamp': 1850,
      'timestamp_label': '[00:30:50]',
      'timestamp_seconds': 1850,
      'tip': "Voluntary compliance in the boxes there we see you know if it's an insurer issue "
             'most likely the insurance departments well in every state the insurance.',
      'title': 'AMA Advocacy Insights webinar series: Implementing the No Surprises Act '
               '(American Medical Association (AMA))',
      'url': 'https://www.youtube.com/watch?v=zyTkKRTBBEg&t=1850s',
      'video_id': 'zyTkKRTBBEg'},
     {'author': 'RCMOpsPro',
      'channel': 'RCMOpsPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=RddJn-tA3OM&t=33s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They are establishing the legal and financial framework for the entire '
              'encounter. Over 80% of all claim denials originate right here. A missed middle '
              'initial will sit silently in the system until it triggers a hard denial 30 days '
              'later.',
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': 'They are establishing the legal and financial framework for the entire '
             'encounter. Over 80% of all claim denials originate right here. A missed middle '
             'initial will sit silently in the system until it triggers a hard denial 30 days '
             'later.',
      'title': 'Revenue Cycle Management (RCM) Explained: Front, Mid & Back End | Created by '
               'Diego Samson (RCMOpsPro)',
      'url': 'https://www.youtube.com/watch?v=RddJn-tA3OM&t=33s',
      'video_id': 'RddJn-tA3OM'},
     {'author': 'Gottlieb and Greenspan, LLC',
      'channel': 'Gottlieb and Greenspan, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=HTDpgKwIfRg&t=22s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is something he proposed before back in 2019 when the parties were '
              'negotiating as to how the NSA itself would be structured.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'This is something he proposed before back in 2019 when the parties were '
             'negotiating as to how the NSA itself would be structured.',
      'title': 'No Surprises Act Update - October 2026: Pallone, Cassidy, CMS Meeting '
               '(Gottlieb and Greenspan, LLC)',
      'url': 'https://www.youtube.com/watch?v=HTDpgKwIfRg&t=22s',
      'video_id': 'HTDpgKwIfRg'},
     {'author': 'Private Practice Skills',
      'channel': 'Private Practice Skills',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:41](https://www.youtube.com/watch?v=HqCQhe8wbVM&t=341s)',
      'relevance': 'Attributed practitioner commentary on contingency out-of-network physician '
                   'underpayment recovery under the federal No Surprises Act (`42 U.S.C. § '
                   '300gg-111`), automating `30`-business-day Open Negotiation, '
                   '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                   'arbitration briefs (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Well I hope you found this video about super bills helpful and until next time '
              'from one therapist to another I wish you well but if you change your mind you '
              'can just interrupt at any point.',
      'timestamp': 341,
      'timestamp_label': '[00:05:41]',
      'timestamp_seconds': 341,
      'tip': 'Well I hope you found this video about super bills helpful and until next time '
             'from one therapist to another I wish you well but if you change your mind you '
             'can just interrupt at any point.',
      'title': 'Superbills in Private Practice | Out-of-Network Billing (Private Practice '
               'Skills)',
      'url': 'https://www.youtube.com/watch?v=HqCQhe8wbVM&t=341s',
      'video_id': 'HqCQhe8wbVM'}],
 10: [{'author': 'KandR BILLING & AI RCM SOFTWARE',
       'channel': 'KandR BILLING & AI RCM SOFTWARE',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:20](https://www.youtube.com/watch?v=-yVkokS2iaE&t=320s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The routing is system-driven and fully logged. This ensures structured '
               'workload distribution, accountability, and operational efficiency at scale. '
               'After a claim is worked, the system automatically triggers the AI quality '
               'audit agent.',
       'timestamp': 320,
       'timestamp_label': '[00:05:20]',
       'timestamp_seconds': 320,
       'tip': 'The routing is system-driven and fully logged. This ensures structured workload '
              'distribution, accountability, and operational efficiency at scale. After a '
              'claim is worked, the system automatically triggers the AI quality audit agent.',
       'title': 'RCM Software Workflow Demo | AI-Powered AR Automation for Healthcare (KandR '
                'BILLING & AI RCM SOFTWARE)',
       'url': 'https://www.youtube.com/watch?v=-yVkokS2iaE&t=320s',
       'video_id': '-yVkokS2iaE'},
      {'author': 'About The Rest',
       'channel': 'About The Rest',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=x35n4T9CppE&t=21s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And Tracy I think did a very good job of describing how their behaviors '
               'changed after these rules were promulgated. They have all this leverage and '
               "they're driving down rates. This has had a seismic impact in the anesthesia "
               'community, business community, seismic.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'And Tracy I think did a very good job of describing how their behaviors changed '
              "after these rules were promulgated. They have all this leverage and they're "
              'driving down rates. This has had a seismic impact in the anesthesia community, '
              'business community, seismic.',
       'title': 'The No Surprises Act Created a Monster (About The Rest)',
       'url': 'https://www.youtube.com/watch?v=x35n4T9CppE&t=21s',
       'video_id': 'x35n4T9CppE'},
      {'author': 'Medicalbillingz',
       'channel': 'Medicalbillingz',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:05](https://www.youtube.com/watch?v=LBZTRJRtZ54&t=65s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Happier patients with transparent billing and fewer surprises. Reduced '
               "administrative burden for providers. It's a win-win for clinics and patients "
               'alike. AI predicts claim denials before submission while automation handles '
               'repetitive tasks like coding and payment posting.',
       'timestamp': 65,
       'timestamp_label': '[00:01:05]',
       'timestamp_seconds': 65,
       'tip': 'Happier patients with transparent billing and fewer surprises. Reduced '
              "administrative burden for providers. It's a win-win for clinics and patients "
              'alike. AI predicts claim denials before submission while automation handles '
              'repetitive tasks like coding and payment posting.',
       'title': 'End to End Revenue Cycle Management in Healthcare | Full RCM Workflow '
                '(Medicalbillingz)',
       'url': 'https://www.youtube.com/watch?v=LBZTRJRtZ54&t=65s',
       'video_id': 'LBZTRJRtZ54'},
      {'author': 'Innobot Health',
       'channel': 'Innobot Health',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:54](https://www.youtube.com/watch?v=uMy2M4PPrMU&t=54s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'API connections to over 1,800 payers, agentic UI automation that navigates '
               'payer portals the way a person would, conversational AI bots that can call a '
               'payer directly, and InoChat with an optional human in the loop when needed.',
       'timestamp': 54,
       'timestamp_label': '[00:00:54]',
       'timestamp_seconds': 54,
       'tip': 'API connections to over 1,800 payers, agentic UI automation that navigates '
              'payer portals the way a person would, conversational AI bots that can call a '
              'payer directly, and InoChat with an optional human in the loop when needed.',
       'title': 'Inside IRIS: A Full Tour of the Platform That Runs Your Revenue Cycle '
                '(Innobot Health)',
       'url': 'https://www.youtube.com/watch?v=uMy2M4PPrMU&t=54s',
       'video_id': 'uMy2M4PPrMU'},
      {'author': 'Guidehouse',
       'channel': 'Guidehouse',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:09](https://www.youtube.com/watch?v=VQBtuhx0a5U&t=69s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'That will then be submitted and the agent will follow up on that to ensure '
               'that we receive a proper response and generate maximum revenue. The thing '
               "that's a little bit different about what we do than a typical reviewer one is "
               'the speed and the capacity.',
       'timestamp': 69,
       'timestamp_label': '[00:01:09]',
       'timestamp_seconds': 69,
       'tip': 'That will then be submitted and the agent will follow up on that to ensure that '
              "we receive a proper response and generate maximum revenue. The thing that's a "
              'little bit different about what we do than a typical reviewer one is the speed '
              'and the capacity.',
       'title': 'AI Agents for Revenue Cycle: Medical Necessity Appeal Agent — RCM Denial '
                'Recovery Automation (Guidehouse)',
       'url': 'https://www.youtube.com/watch?v=VQBtuhx0a5U&t=69s',
       'video_id': 'VQBtuhx0a5U'},
      {'author': 'NTT DATA North America',
       'channel': 'NTT DATA North America',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:03](https://www.youtube.com/watch?v=xJZ_wqqTQhY&t=63s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The initial authorization request is denied by insurance provider for medical '
               'necessity. Our AI appeal agent drafts an overturn letter, referencing NCCN and '
               'insurance-specific guidelines, which is reviewed by the oncologist and '
               'submitted.',
       'timestamp': 63,
       'timestamp_label': '[00:01:03]',
       'timestamp_seconds': 63,
       'tip': 'The initial authorization request is denied by insurance provider for medical '
              'necessity. Our AI appeal agent drafts an overturn letter, referencing NCCN and '
              'insurance-specific guidelines, which is reviewed by the oncologist and '
              'submitted.',
       'title': 'How 9 AI Agents Automate the Entire Revenue Cycle | RCM by NTT DATA Demo (NTT '
                'DATA North America)',
       'url': 'https://www.youtube.com/watch?v=xJZ_wqqTQhY&t=63s',
       'video_id': 'xJZ_wqqTQhY'},
      {'author': 'AGS Health',
       'channel': 'AGS Health',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:57](https://www.youtube.com/watch?v=x0zeGvoXqsc&t=237s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And so this AI agent is navigating the IVR, inputting all the right '
               'information like claim ID and others, listening to Mozart and Bach for like 35 '
               "minutes while they're there on the while it's on the whole time.",
       'timestamp': 237,
       'timestamp_label': '[00:03:57]',
       'timestamp_seconds': 237,
       'tip': 'And so this AI agent is navigating the IVR, inputting all the right information '
              'like claim ID and others, listening to Mozart and Bach for like 35 minutes '
              "while they're there on the while it's on the whole time.",
       'title': "Agentic Automation And Why It's Transforming Healthcare RCM - AGS Health (AGS "
                'Health)',
       'url': 'https://www.youtube.com/watch?v=x0zeGvoXqsc&t=237s',
       'video_id': 'x0zeGvoXqsc'},
      {'author': 'Jan Miller - Student Loan Consultant',
       'channel': 'Jan Miller - Student Loan Consultant',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:03](https://www.youtube.com/watch?v=nJ_2pYeUX80&t=123s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s been there and um you know most people don't stay at the same loan serer "
               'through the duration of their payment. So that information will likely only be '
               "at studentaid. 're the people forgive the loan after a certain amount of time "
               'anyway.',
       'timestamp': 123,
       'timestamp_label': '[00:02:03]',
       'timestamp_seconds': 123,
       'tip': "'s been there and um you know most people don't stay at the same loan serer "
              'through the duration of their payment. So that information will likely only be '
              "at studentaid. 're the people forgive the loan after a certain amount of time "
              'anyway.',
       'title': 'IDR Payment Count Hack (Jan Miller - Student Loan Consultant)',
       'url': 'https://www.youtube.com/watch?v=nJ_2pYeUX80&t=123s',
       'video_id': 'nJ_2pYeUX80'},
      {'author': "Becker's Hospital Review",
       'channel': "Becker's Hospital Review",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:23:21](https://www.youtube.com/watch?v=7h4H8g1S01E&t=1401s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Amount in this case you cannot bail two patients for the discounted amount '
               'because you have come to an agreement with a vendor but I also want to '
               'mention.',
       'timestamp': 1401,
       'timestamp_label': '[00:23:21]',
       'timestamp_seconds': 1401,
       'tip': 'Amount in this case you cannot bail two patients for the discounted amount '
              'because you have come to an agreement with a vendor but I also want to mention.',
       'title': "Out-of-Network: Frequently Asked Questions (Becker's Hospital Review)",
       'url': 'https://www.youtube.com/watch?v=7h4H8g1S01E&t=1401s',
       'video_id': '7h4H8g1S01E'},
      {'author': 'The Claim Game X Practice Solutions',
       'channel': 'The Claim Game X Practice Solutions',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:35](https://www.youtube.com/watch?v=b2mkUKtTWnE&t=455s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And in our guide to the components of an ERRA, we break down how this file '
               'differs from the paper version. The biggest difference between an electronic '
               "remittance advice and an explanation of benefits is speed. Then there's the "
               'component of automation.',
       'timestamp': 455,
       'timestamp_label': '[00:07:35]',
       'timestamp_seconds': 455,
       'tip': 'And in our guide to the components of an ERRA, we break down how this file '
              'differs from the paper version. The biggest difference between an electronic '
              "remittance advice and an explanation of benefits is speed. Then there's the "
              'component of automation.',
       'title': 'Revenue Cycle Management Explained: Remittances, ERAs, and Portals (The Claim '
                'Game X Practice Solutions)',
       'url': 'https://www.youtube.com/watch?v=b2mkUKtTWnE&t=455s',
       'video_id': 'b2mkUKtTWnE'},
      {'author': 'LandingAI',
       'channel': 'LandingAI',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:44](https://www.youtube.com/watch?v=SE4fu2hvD94&t=464s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Um the manual review burden. Uh I think we see a lot of automation pipelines '
               'where folks are still needing to do a ton of manual review. So again this '
               'comes back to um accuracy of the extraction um and then inefficiency as well.',
       'timestamp': 464,
       'timestamp_label': '[00:07:44]',
       'timestamp_seconds': 464,
       'tip': 'Um the manual review burden. Uh I think we see a lot of automation pipelines '
              'where folks are still needing to do a ton of manual review. So again this comes '
              'back to um accuracy of the extraction um and then inefficiency as well.',
       'title': 'How AI Is Transforming High-Volume Document Workflows at Scale in Healthcare '
                'RCM (LandingAI)',
       'url': 'https://www.youtube.com/watch?v=SE4fu2hvD94&t=464s',
       'video_id': 'SE4fu2hvD94'},
      {'author': 'PayerWatch',
       'channel': 'PayerWatch',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:54:58](https://www.youtube.com/watch?v=cePrn8Rhav8&t=3298s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Said there was a September study from last year that's more relevant that's "
               'what you need to be using great the next question is going to be what are your '
               'thoughts on us utilizing AI to work denials and write appeal.',
       'timestamp': 3298,
       'timestamp_label': '[00:54:58]',
       'timestamp_seconds': 3298,
       'tip': "Said there was a September study from last year that's more relevant that's "
              'what you need to be using great the next question is going to be what are your '
              'thoughts on us utilizing AI to work denials and write appeal.',
       'title': 'Revenue Cycle 101 (PayerWatch)',
       'url': 'https://www.youtube.com/watch?v=cePrn8Rhav8&t=3298s',
       'video_id': 'cePrn8Rhav8'},
      {'author': 'Jarod Carter',
       'channel': 'Jarod Carter',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:00](https://www.youtube.com/watch?v=cA7tBJf4KyY&t=240s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Needed information so again download that free template and make sure that '
               'your super bills are set up for success or setting your patients up for '
               'Success.',
       'timestamp': 240,
       'timestamp_label': '[00:04:00]',
       'timestamp_seconds': 240,
       'tip': 'Needed information so again download that free template and make sure that your '
              'super bills are set up for success or setting your patients up for Success.',
       'title': 'Top 4 Out-of-Network Billing & Superbill Tips (Jarod Carter)',
       'url': 'https://www.youtube.com/watch?v=cA7tBJf4KyY&t=240s',
       'video_id': 'cA7tBJf4KyY'},
      {'author': 'Bethel Law',
       'channel': 'Bethel Law',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:21](https://www.youtube.com/watch?v=q3heX6QnFfo&t=381s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Waters and medical billing I'm attorney Andrew bethl and I'm here to help you "
               "make sense of the laws that impact your life I'll catch you in the next video.",
       'timestamp': 381,
       'timestamp_label': '[00:06:21]',
       'timestamp_seconds': 381,
       'tip': "Waters and medical billing I'm attorney Andrew bethl and I'm here to help you "
              "make sense of the laws that impact your life I'll catch you in the next video.",
       'title': 'How the No Surprises Act is Saving You From Billing Shocks! (Bethel Law)',
       'url': 'https://www.youtube.com/watch?v=q3heX6QnFfo&t=381s',
       'video_id': 'q3heX6QnFfo'},
      {'author': 'Azeem khan Watanyar Official',
       'channel': 'Azeem khan Watanyar Official',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=RhNPFe6U8iU&t=15s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'व्हेन अ पेयर और पेशेंट पेज़ मोर देन द बिल्ट और अलाउड अमाउंट। ओवरपेमेंट क्या है? '
               'जब इंश्योरेंस या पेशेंट जो अलाउड अमाउंट होती है उनसे अगर ज्यादा अमाउंट पे.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'व्हेन अ पेयर और पेशेंट पेज़ मोर देन द बिल्ट और अलाउड अमाउंट। ओवरपेमेंट क्या है? '
              'जब इंश्योरेंस या पेशेंट जो अलाउड अमाउंट होती है उनसे अगर ज्यादा अमाउंट पे.',
       'title': 'What is the difference between overpayment and underpayment in medical '
                'billing (Azeem khan Watanyar Official)',
       'url': 'https://www.youtube.com/watch?v=RhNPFe6U8iU&t=15s',
       'video_id': 'RhNPFe6U8iU'}],
 11: [{'author': 'Xpert Billing Talk',
       'channel': 'Xpert Billing Talk',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:53](https://www.youtube.com/watch?v=g3C-DoM_9CI&t=233s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Which just proves your team actually needs a robust calendar-based tool to '
               'calculate exact business days, not manual counting. Manual counting is a '
               'recipe for disaster. And there is a secondary deadline coming up fast after '
               'this, right? Keep your eye on January 15, 2027.',
       'timestamp': 233,
       'timestamp_label': '[00:03:53]',
       'timestamp_seconds': 233,
       'tip': 'Which just proves your team actually needs a robust calendar-based tool to '
              'calculate exact business days, not manual counting. Manual counting is a recipe '
              'for disaster. And there is a secondary deadline coming up fast after this, '
              'right? Keep your eye on January 15, 2027.',
       'title': 'Federal IDR Changes Nov. 1, 2026: Radiology Batching & Deadlines (Xpert '
                'Billing Talk)',
       'url': 'https://www.youtube.com/watch?v=g3C-DoM_9CI&t=233s',
       'video_id': 'g3C-DoM_9CI'},
      {'author': 'Jentry Harris',
       'channel': 'Jentry Harris',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=LNSPlo2_U3c&t=21s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The No Surprises Act protects members from balance billing when they receive '
               'emergency care or unknowingly receive out of network services at an in-et '
               'network facility. Think ER visits, air ambulance, or an anesthesiologist at an '
               'in-et network hospital.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'The No Surprises Act protects members from balance billing when they receive '
              'emergency care or unknowingly receive out of network services at an in-et '
              'network facility. Think ER visits, air ambulance, or an anesthesiologist at an '
              'in-et network hospital.',
       'title': 'The No Surprises Act (NSA) and Independent Dispute Resolution (IDR) (Jentry '
                'Harris)',
       'url': 'https://www.youtube.com/watch?v=LNSPlo2_U3c&t=21s',
       'video_id': 'LNSPlo2_U3c'},
      {'author': 'HealthWatch Wisconsin',
       'channel': 'HealthWatch Wisconsin',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:32](https://www.youtube.com/watch?v=MsP7ttGr9OA&t=32s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re at an out-of-network facility. There is a notable exception and that is "
               'ground ambulances. The No Surprises Act included some new protections for '
               'folks getting air ambulance bills, but it did not include protection for '
               'ground ambulance bills.',
       'timestamp': 32,
       'timestamp_label': '[00:00:32]',
       'timestamp_seconds': 32,
       'tip': "'re at an out-of-network facility. There is a notable exception and that is "
              'ground ambulances. The No Surprises Act included some new protections for folks '
              'getting air ambulance bills, but it did not include protection for ground '
              'ambulance bills.',
       'title': 'Quick Take: No Surprises Act: Out of Network Charges (HealthWatch Wisconsin)',
       'url': 'https://www.youtube.com/watch?v=MsP7ttGr9OA&t=32s',
       'video_id': 'MsP7ttGr9OA'},
      {'author': 'Long Reads, Explained',
       'channel': 'Long Reads, Explained',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:17](https://www.youtube.com/watch?v=cSaC2n-3r9o&t=617s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And it says the average award is more than five times the qualifying payment '
               'amount, which is the benchmark rate used in these disputes. Individual cases '
               'make those multiples concrete.',
       'timestamp': 617,
       'timestamp_label': '[00:10:17]',
       'timestamp_seconds': 617,
       'tip': 'And it says the average award is more than five times the qualifying payment '
              'amount, which is the benchmark rate used in these disputes. Individual cases '
              'make those multiples concrete.',
       'title': 'No Surprises Act arbitration is driving 2027 premium spike (Long Reads, '
                'Explained)',
       'url': 'https://www.youtube.com/watch?v=cSaC2n-3r9o&t=617s',
       'video_id': 'cSaC2n-3r9o'},
      {'author': 'American Medical Association (AMA)',
       'channel': 'American Medical Association (AMA)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:11](https://www.youtube.com/watch?v=YJ1Bgt_KIyw&t=611s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Congress and still place a thumb on the scale in favor of health plans. So on '
               'September 22, the Texas Medical Association filed a new lawsuit in the same '
               'federal court in Texas arguing that the final rules still suffer from the same '
               'problems as the interim final rules.',
       'timestamp': 611,
       'timestamp_label': '[00:10:11]',
       'timestamp_seconds': 611,
       'tip': 'Congress and still place a thumb on the scale in favor of health plans. So on '
              'September 22, the Texas Medical Association filed a new lawsuit in the same '
              'federal court in Texas arguing that the final rules still suffer from the same '
              'problems as the interim final rules.',
       'title': 'What physicians need to know about the No Surprises Act with Emily Carroll, '
                'JD & George Cox, JD (American Medical Association (AMA))',
       'url': 'https://www.youtube.com/watch?v=YJ1Bgt_KIyw&t=611s',
       'video_id': 'YJ1Bgt_KIyw'},
      {'author': 'Apex IONM Solutions',
       'channel': 'Apex IONM Solutions',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:34](https://www.youtube.com/watch?v=EE3aFeVfLnk&t=34s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'This ignores all kinds of context. The qualified payment amount or QPA in an '
               'arbitration setting is supposed to be the median contracted rate for a given '
               "service that's identified by its billing code.",
       'timestamp': 34,
       'timestamp_label': '[00:00:34]',
       'timestamp_seconds': 34,
       'tip': 'This ignores all kinds of context. The qualified payment amount or QPA in an '
              'arbitration setting is supposed to be the median contracted rate for a given '
              "service that's identified by its billing code.",
       'title': 'Insurers Say the No Surprises Act Is Paying Providers Too Much (Apex IONM '
                'Solutions)',
       'url': 'https://www.youtube.com/watch?v=EE3aFeVfLnk&t=34s',
       'video_id': 'EE3aFeVfLnk'},
      {'author': 'OpenBots',
       'channel': 'OpenBots',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:41](https://www.youtube.com/watch?v=ZpELLvKSrF8&t=101s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So yeah, I'm very excited once again to give a quick introduction about "
               "myself. Like Gabe said, uh my name is Ronaldo Banerjee. I'm the associate "
               'director of healthcare automation solutions at Openbots.',
       'timestamp': 101,
       'timestamp_label': '[00:01:41]',
       'timestamp_seconds': 101,
       'tip': "So yeah, I'm very excited once again to give a quick introduction about myself. "
              "Like Gabe said, uh my name is Ronaldo Banerjee. I'm the associate director of "
              'healthcare automation solutions at Openbots.',
       'title': 'Eligibility Verification in Healthcare with Agentic AI | #RCM #AIinHealthcare '
                '#HealthcareAutomation (OpenBots)',
       'url': 'https://www.youtube.com/watch?v=ZpELLvKSrF8&t=101s',
       'video_id': 'ZpELLvKSrF8'},
      {'author': 'Jarod Carter',
       'channel': 'Jarod Carter',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:18](https://www.youtube.com/watch?v=heiuukmxgss&t=138s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Discount from based on our standard operating procedures you know whether it's "
               'for packages for sliding scale for mates rates for the difference between a.',
       'timestamp': 138,
       'timestamp_label': '[00:02:18]',
       'timestamp_seconds': 138,
       'tip': "Discount from based on our standard operating procedures you know whether it's "
              'for packages for sliding scale for mates rates for the difference between a.',
       'title': 'Superbill Secrets for Cash Practice Packages - Out-of-Network Billing '
                'Reimbursement Tips (Jarod Carter)',
       'url': 'https://www.youtube.com/watch?v=heiuukmxgss&t=138s',
       'video_id': 'heiuukmxgss'},
      {'author': 'CMSHHSgov',
       'channel': 'CMSHHSgov',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:32](https://www.youtube.com/watch?v=Vy31vkzfNBE&t=92s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'After reviewing the information at the top of this page, the initiating party '
               'should read this warning message and the security and privacy agreement. At '
               'the bottom of this page, select the checkbox next to the Security and Privacy '
               'Agreement.',
       'timestamp': 92,
       'timestamp_label': '[00:01:32]',
       'timestamp_seconds': 92,
       'tip': 'After reviewing the information at the top of this page, the initiating party '
              'should read this warning message and the security and privacy agreement. At the '
              'bottom of this page, select the checkbox next to the Security and Privacy '
              'Agreement.',
       'title': 'No Surprises Act: Notice of IDR Initiation - Resubmission Web Form Demo '
                '(CMSHHSgov)',
       'url': 'https://www.youtube.com/watch?v=Vy31vkzfNBE&t=92s',
       'video_id': 'Vy31vkzfNBE'},
      {'author': 'EDI PowerTools by EMS Healthcare Informatics',
       'channel': 'EDI PowerTools by EMS Healthcare Informatics',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:41](https://www.youtube.com/watch?v=JfPjIRaIz-o&t=461s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Secondary Claim by the payer so that's what that two means now let's just walk "
               'through the rest o cpo3 is the total claim charged amount on the whole claim.',
       'timestamp': 461,
       'timestamp_label': '[00:07:41]',
       'timestamp_seconds': 461,
       'tip': "Secondary Claim by the payer so that's what that two means now let's just walk "
              'through the rest o cpo3 is the total claim charged amount on the whole claim.',
       'title': 'How to read an 835 Electronic Remittance File (EDI PowerTools by EMS '
                'Healthcare Informatics)',
       'url': 'https://www.youtube.com/watch?v=JfPjIRaIz-o&t=461s',
       'video_id': 'JfPjIRaIz-o'},
      {'author': 'First Healthcare Compliance',
       'channel': 'First Healthcare Compliance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:30:56](https://www.youtube.com/watch?v=uQSw1Ucy6L4&t=1856s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Would encourage you and your clients to reach out to their mac their medicare '
               'audit contractor or a.',
       'timestamp': 1856,
       'timestamp_label': '[00:30:56]',
       'timestamp_seconds': 1856,
       'tip': 'Would encourage you and your clients to reach out to their mac their medicare '
              'audit contractor or a.',
       'title': 'The No Surprises Act - What You Need to Know (First Healthcare Compliance)',
       'url': 'https://www.youtube.com/watch?v=uQSw1Ucy6L4&t=1856s',
       'video_id': 'uQSw1Ucy6L4'},
      {'author': 'Identification and Recruitment Consortium',
       'channel': 'Identification and Recruitment Consortium',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:19:02](https://www.youtube.com/watch?v=wAiC4TUQNvs&t=1142s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Amacholi, Florida to Pit County, North Carolina on April 4th, 2026 to plant '
               'tobacco. She got work planning tobacco and after the planting season ended in '
               'June, Rosa heard of strawberry work in Tennessee and moved her family there '
               'July 12th, 2026.',
       'timestamp': 1142,
       'timestamp_label': '[00:19:02]',
       'timestamp_seconds': 1142,
       'tip': 'Amacholi, Florida to Pit County, North Carolina on April 4th, 2026 to plant '
              'tobacco. She got work planning tobacco and after the planting season ended in '
              'June, Rosa heard of strawberry work in Tennessee and moved her family there '
              'July 12th, 2026.',
       'title': 'IDR Scenarios- Title I, Part C (Identification and Recruitment Consortium)',
       'url': 'https://www.youtube.com/watch?v=wAiC4TUQNvs&t=1142s',
       'video_id': 'wAiC4TUQNvs'},
      {'author': 'Remodel Health',
       'channel': 'Remodel Health',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:36](https://www.youtube.com/watch?v=tNA4dmumP8o&t=336s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "The course of time but we wanted to make sure it's on your radar be thinking "
               "like a consumer when you're interacting with your health care because the time "
               "is now when you're going to be able to have much better choices.",
       'timestamp': 336,
       'timestamp_label': '[00:05:36]',
       'timestamp_seconds': 336,
       'tip': "The course of time but we wanted to make sure it's on your radar be thinking "
              "like a consumer when you're interacting with your health care because the time "
              "is now when you're going to be able to have much better choices.",
       'title': 'No Surprises Act: New Law to Protect Against Surprise Medical Bills (Remodel '
                'Health)',
       'url': 'https://www.youtube.com/watch?v=tNA4dmumP8o&t=336s',
       'video_id': 'tNA4dmumP8o'},
      {'author': 'The Private Practice Outsider',
       'channel': 'The Private Practice Outsider',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:32](https://www.youtube.com/watch?v=TNKYk9V0ty8&t=152s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That's when you choose not to balance bill your patient so I hope that cleared "
               'it up if you have questions I can always do this on the computer so you can '
               "see the actual numbers on a spreadsheet but best of luck I'll catch you on the "
               'next video.',
       'timestamp': 152,
       'timestamp_label': '[00:02:32]',
       'timestamp_seconds': 152,
       'tip': "That's when you choose not to balance bill your patient so I hope that cleared "
              'it up if you have questions I can always do this on the computer so you can see '
              "the actual numbers on a spreadsheet but best of luck I'll catch you on the next "
              'video.',
       'title': 'Out of Network Billing [Coinsurance plus Balance Billing] Amount Explained '
                '(The Private Practice Outsider)',
       'url': 'https://www.youtube.com/watch?v=TNKYk9V0ty8&t=152s',
       'video_id': 'TNKYk9V0ty8'},
      {'author': 'The Phia Group, LLC',
       'channel': 'The Phia Group, LLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:57](https://www.youtube.com/watch?v=ksxW878eWWk&t=717s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Um, Guardian Flight uh brought suit in federal court uh against the payor to '
               'enforce a payment award that it was granted in arbitration.',
       'timestamp': 717,
       'timestamp_label': '[00:11:57]',
       'timestamp_seconds': 717,
       'tip': 'Um, Guardian Flight uh brought suit in federal court uh against the payor to '
              'enforce a payment award that it was granted in arbitration.',
       'title': 'Empowering Plans: P235 – The Latest No Surprises Act Developments: A 2026 '
                'Reality Check for TPAs (The Phia Group, LLC)',
       'url': 'https://www.youtube.com/watch?v=ksxW878eWWk&t=717s',
       'video_id': 'ksxW878eWWk'}],
 12: [{'author': 'Inlera University',
       'channel': 'Inlera University',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:47:57](https://www.youtube.com/watch?v=RvLjKE1S1eU&t=2877s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re going to start seeing a really smooth revenue cycle if you're touching "
               "those rejections daily. So, when we're looking at reconciling, we are "
               "balancing our day, our week, and our month. We're looking at the totals of all "
               'of those things.',
       'timestamp': 2877,
       'timestamp_label': '[00:47:57]',
       'timestamp_seconds': 2877,
       'tip': "'re going to start seeing a really smooth revenue cycle if you're touching "
              "those rejections daily. So, when we're looking at reconciling, we are balancing "
              "our day, our week, and our month. We're looking at the totals of all of those "
              'things.',
       'title': 'Revenue Cycle Management & Recommended Workflow Part 3 | Medical Billers '
                'Network Live (Inlera University)',
       'url': 'https://www.youtube.com/watch?v=RvLjKE1S1eU&t=2877s',
       'video_id': 'RvLjKE1S1eU'},
      {'author': 'New Hampshire Insurance Department',
       'channel': 'New Hampshire Insurance Department',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:18:35](https://www.youtube.com/watch?v=C6hIoQuEWeA&t=1115s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You mentioned that the IDR initiation needs to take place within four days '
               'following the close of the open negotiation process or four days before the '
               'end of the open negotiation process. So you tack on those four days after the '
               '20th day you start counting.',
       'timestamp': 1115,
       'timestamp_label': '[00:18:35]',
       'timestamp_seconds': 1115,
       'tip': 'You mentioned that the IDR initiation needs to take place within four days '
              'following the close of the open negotiation process or four days before the end '
              'of the open negotiation process. So you tack on those four days after the 20th '
              'day you start counting.',
       'title': 'Explaining the Independent Dispute Resolution Process in New Hampshire (New '
                'Hampshire Insurance Department)',
       'url': 'https://www.youtube.com/watch?v=C6hIoQuEWeA&t=1115s',
       'video_id': 'C6hIoQuEWeA'},
      {'author': 'Unfiltered Money Labs',
       'channel': 'Unfiltered Money Labs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:38](https://www.youtube.com/watch?v=oP8xNI1bG3E&t=38s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Borrower A owes $40,000 and makes $35,000 a year. Borrower B also owes '
               "$40,000, but they're pulling in $90,000. Under a traditional fixed payment "
               "plan, they'd both be forced to pay the exact same amount every month based "
               'purely on the loan balance.',
       'timestamp': 38,
       'timestamp_label': '[00:00:38]',
       'timestamp_seconds': 38,
       'tip': 'Borrower A owes $40,000 and makes $35,000 a year. Borrower B also owes $40,000, '
              "but they're pulling in $90,000. Under a traditional fixed payment plan, they'd "
              'both be forced to pay the exact same amount every month based purely on the '
              'loan balance.',
       'title': 'Income-Driven Repayment Explained: How to Lower Your Student Loan Payments '
                '(2026) (Unfiltered Money Labs)',
       'url': 'https://www.youtube.com/watch?v=oP8xNI1bG3E&t=38s',
       'video_id': 'oP8xNI1bG3E'},
      {'author': 'Strategic Wealth Design',
       'channel': 'Strategic Wealth Design',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:07](https://www.youtube.com/watch?v=l05EHgbqGQ8&t=187s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "You'll get a notice July 1st. You'll start getting 90-day notices if you "
               "haven't already. When you get that, it's important to be looking at what "
               "income based repayment plan is the best for you. It's a case- byase situation.",
       'timestamp': 187,
       'timestamp_label': '[00:03:07]',
       'timestamp_seconds': 187,
       'tip': "You'll get a notice July 1st. You'll start getting 90-day notices if you "
              "haven't already. When you get that, it's important to be looking at what income "
              "based repayment plan is the best for you. It's a case- byase situation.",
       'title': 'New IDR Plans (Income-Driven Repayment) for Student Debt | Student Loan '
                'Webinar 2026 Recap (Strategic Wealth Design)',
       'url': 'https://www.youtube.com/watch?v=l05EHgbqGQ8&t=187s',
       'video_id': 'l05EHgbqGQ8'},
      {'author': 'HaloMD',
       'channel': 'HaloMD',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:53](https://www.youtube.com/watch?v=of6CD7esHY0&t=293s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '120 days after plan registry. You will not be able to rebatch any disputes '
               "moving forward if you made an error. It's something that CMS has already "
               'reported back in the day.',
       'timestamp': 293,
       'timestamp_label': '[00:04:53]',
       'timestamp_seconds': 293,
       'tip': '120 days after plan registry. You will not be able to rebatch any disputes '
              "moving forward if you made an error. It's something that CMS has already "
              'reported back in the day.',
       'title': 'Decoding The Federal IDR Operations Final Rule: Access, Process and Timing '
                '(HaloMD)',
       'url': 'https://www.youtube.com/watch?v=of6CD7esHY0&t=293s',
       'video_id': 'of6CD7esHY0'},
      {'author': 'U.S. Department of Health and Human Services',
       'channel': 'U.S. Department of Health and Human Services',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:30](https://www.youtube.com/watch?v=eKJscqVwYls&t=90s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Fourth, we are here to help. We have created a consumer-friendly complaint '
               'help desk to guide patients through the dispute process. The help desk is open '
               'from 8am - 8pm Eastern time, 7 days a week to help you with the payment '
               'arbitration process or other questions.',
       'timestamp': 90,
       'timestamp_label': '[00:01:30]',
       'timestamp_seconds': 90,
       'tip': 'Fourth, we are here to help. We have created a consumer-friendly complaint help '
              'desk to guide patients through the dispute process. The help desk is open from '
              '8am - 8pm Eastern time, 7 days a week to help you with the payment arbitration '
              'process or other questions.',
       'title': 'No More Surprise Medical Bills: 5 Things To Know about the No Surprises Act '
                'Taking Effect in 2022 (U.S. Department of Health and Human Services)',
       'url': 'https://www.youtube.com/watch?v=eKJscqVwYls&t=90s',
       'video_id': 'eKJscqVwYls'},
      {'author': 'Federal Student Aid',
       'channel': 'Federal Student Aid',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:50](https://www.youtube.com/watch?v=9TnGgGAGY8c&t=170s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'If paying the same amount every month throughout your repayment period works '
               'better for your goals, then adjustable payments on an income-driven repayment '
               'plan might not be the best choice for you. Consider instead enrolling in one '
               'of the fixed payment repayment plans.',
       'timestamp': 170,
       'timestamp_label': '[00:02:50]',
       'timestamp_seconds': 170,
       'tip': 'If paying the same amount every month throughout your repayment period works '
              'better for your goals, then adjustable payments on an income-driven repayment '
              'plan might not be the best choice for you. Consider instead enrolling in one of '
              'the fixed payment repayment plans.',
       'title': 'Intro to IDR: What To Know About Income-Driven Repayment (IDR) Plans for '
                'Student Loans (Federal Student Aid)',
       'url': 'https://www.youtube.com/watch?v=9TnGgGAGY8c&t=170s',
       'video_id': '9TnGgGAGY8c'},
      {'author': 'DAS Health',
       'channel': 'DAS Health',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:51:28](https://www.youtube.com/watch?v=e5b1ICVPSZs&t=3088s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Known its actions violated the rule or the facility or provider reimburses the '
               'health plan insurer or patient as applicable within 30 days of the violation.',
       'timestamp': 3088,
       'timestamp_label': '[00:51:28]',
       'timestamp_seconds': 3088,
       'tip': 'Known its actions violated the rule or the facility or provider reimburses the '
              'health plan insurer or patient as applicable within 30 days of the violation.',
       'title': 'Don’t Be Surprised by the No Surprises Act! (DAS Health)',
       'url': 'https://www.youtube.com/watch?v=e5b1ICVPSZs&t=3088s',
       'video_id': 'e5b1ICVPSZs'},
      {'author': 'Zelis Healthcare',
       'channel': 'Zelis Healthcare',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:59](https://www.youtube.com/watch?v=lhoUoQSpOCg&t=59s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Um at the start of 2025, more than 600,000 disputes still awaited '
               'determinations. Um, additionally, providers and payers face significant delays '
               'in that dispute resolution, um, with 69% of open disputes being more than 30 '
               "days old. Now, let's talk about outcomes.",
       'timestamp': 59,
       'timestamp_label': '[00:00:59]',
       'timestamp_seconds': 59,
       'tip': 'Um at the start of 2025, more than 600,000 disputes still awaited '
              'determinations. Um, additionally, providers and payers face significant delays '
              'in that dispute resolution, um, with 69% of open disputes being more than 30 '
              "days old. Now, let's talk about outcomes.",
       'title': 'Trends & Insights from 2024 CMS IDR Data | What’s Changing in No Surprises '
                'Act Disputes (Zelis Healthcare)',
       'url': 'https://www.youtube.com/watch?v=lhoUoQSpOCg&t=59s',
       'video_id': 'lhoUoQSpOCg'},
      {'author': 'AarkNine Healthcare',
       'channel': 'AarkNine Healthcare',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:39:47](https://www.youtube.com/watch?v=3HP5mg0UdCw&t=2387s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Another key metric they track is reduced AR days. AR stands for accounts '
               "receivable days. It's basically the average time it takes for a service to be "
               "paid for after it's been provided.",
       'timestamp': 2387,
       'timestamp_label': '[00:39:47]',
       'timestamp_seconds': 2387,
       'tip': 'Another key metric they track is reduced AR days. AR stands for accounts '
              "receivable days. It's basically the average time it takes for a service to be "
              "paid for after it's been provided.",
       'title': 'CARC & RARC Adjustment and Denial codes ll Medical claim denial & management '
                'll adjustment #rcm (AarkNine Healthcare)',
       'url': 'https://www.youtube.com/watch?v=3HP5mg0UdCw&t=2387s',
       'video_id': '3HP5mg0UdCw'},
      {'author': 'Andrea Austin',
       'channel': 'Andrea Austin',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:16](https://www.youtube.com/watch?v=8o10JCNK6n8&t=316s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re living it doing it every day. And also seeing again the the people around "
               "us enjoying their days. And that's not something a lot of us in medicine can "
               'see anymore.',
       'timestamp': 316,
       'timestamp_label': '[00:05:16]',
       'timestamp_seconds': 316,
       'tip': "'re living it doing it every day. And also seeing again the the people around "
              "us enjoying their days. And that's not something a lot of us in medicine can "
              'see anymore.',
       'title': 'Autonomy in Medicine: The Path to Fulfillment and Innovation (Andrea Austin)',
       'url': 'https://www.youtube.com/watch?v=8o10JCNK6n8&t=316s',
       'video_id': '8o10JCNK6n8'},
      {'author': 'AHealthcareZ - Healthcare Finance Explained',
       'channel': 'AHealthcareZ - Healthcare Finance Explained',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:00](https://www.youtube.com/watch?v=rqdWr9ynZ_o&t=660s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'By 365 days in a year that means on average the hospital bills out 8.2 million '
               'a day like a medium-sized hospital system.',
       'timestamp': 660,
       'timestamp_label': '[00:11:00]',
       'timestamp_seconds': 660,
       'tip': 'By 365 days in a year that means on average the hospital bills out 8.2 million '
              'a day like a medium-sized hospital system.',
       'title': 'Revenue Cycle Management in Healthcare Explained (AHealthcareZ - Healthcare '
                'Finance Explained)',
       'url': 'https://www.youtube.com/watch?v=rqdWr9ynZ_o&t=660s',
       'video_id': 'rqdWr9ynZ_o'},
      {'author': 'Dr. Lauren Baker',
       'channel': 'Dr. Lauren Baker',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:18:20](https://www.youtube.com/watch?v=zsaby8gJNmg&t=1100s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Provide really great care for kiddos so anything I can do to make your lives '
               'easier I am totally gameless have a good day guys bye.',
       'timestamp': 1100,
       'timestamp_label': '[00:18:20]',
       'timestamp_seconds': 1100,
       'tip': 'Provide really great care for kiddos so anything I can do to make your lives '
              'easier I am totally gameless have a good day guys bye.',
       'title': 'How To Fill Out A Claims Form For Out of Network Reimbursement | PT Out of '
                'Network Claim (Dr. Lauren Baker)',
       'url': 'https://www.youtube.com/watch?v=zsaby8gJNmg&t=1100s',
       'video_id': 'zsaby8gJNmg'},
      {'author': 'Orion Billing - Medical Billing Basics',
       'channel': 'Orion Billing - Medical Billing Basics',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:42](https://www.youtube.com/watch?v=_z9Vfv0D6_4&t=162s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I will make another video or two about how you can use it how to appeal those '
               'things and give some more information about erisa at Orion billing we work '
               'hard to appeal all the things that need to be appealed and get one ready in '
               'the door have an awesome day.',
       'timestamp': 162,
       'timestamp_label': '[00:02:42]',
       'timestamp_seconds': 162,
       'tip': 'I will make another video or two about how you can use it how to appeal those '
              'things and give some more information about erisa at Orion billing we work hard '
              'to appeal all the things that need to be appealed and get one ready in the door '
              'have an awesome day.',
       'title': 'ERISA explained (and Why it Matters) (Orion Billing - Medical Billing Basics)',
       'url': 'https://www.youtube.com/watch?v=_z9Vfv0D6_4&t=162s',
       'video_id': '_z9Vfv0D6_4'},
      {'author': 'Long Reads, Explained',
       'channel': 'Long Reads, Explained',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:49](https://www.youtube.com/watch?v=nJ5Tz7G_LA8&t=829s)',
       'relevance': 'Attributed practitioner commentary on contingency out-of-network '
                    'physician underpayment recovery under the federal No Surprises Act (`42 '
                    'U.S.C. § 300gg-111`), automating `30`-business-day Open Negotiation, '
                    '`4`-business-day Certified `IDR` Entity batching, and `QPA`-uplift '
                    'arbitration briefs (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'It won one thousand thirty-two arbitration cases in twenty twenty-five. Its '
               'average award was around four times what insurers typically pay. And in '
               'January, the practice had to take out a line of credit to make payroll.',
       'timestamp': 829,
       'timestamp_label': '[00:13:49]',
       'timestamp_seconds': 829,
       'tip': 'It won one thousand thirty-two arbitration cases in twenty twenty-five. Its '
              'average award was around four times what insurers typically pay. And in '
              'January, the practice had to take out a line of credit to make payroll.',
       'title': 'No Surprises Act: Nearly 30% of Awards Unpaid by Insurers (Long Reads, '
                'Explained)',
       'url': 'https://www.youtube.com/watch?v=nJ5Tz7G_LA8&t=829s',
       'video_id': 'nJ5Tz7G_LA8'}]}
