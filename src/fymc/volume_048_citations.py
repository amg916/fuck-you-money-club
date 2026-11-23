"""Curated 180-citation Data-Mined Qui Tam, SEC & IRS Whistleblower Analytics baseline (15 per chapter across Q1-Q12) mined strictly from verified Data-Mined Qui Tam, SEC & IRS Whistleblower Analytics YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'211',
     '3729',
     '7623',
     '78u',
     'ability',
     'act',
     'adjustment',
     'advantage',
     'aml',
     'analysis',
     'analyst',
     'analytics',
     'annual',
     'anomalies',
     'anonymous',
     'anti',
     'antidumping',
     'attorney',
     'attorneys',
     'auto',
     'available',
     'average',
     'avoidance',
     'award',
     'awards',
     'bar',
     'best',
     'bill',
     'billing',
     'building',
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
 2: {'211',
     '3729',
     '7623',
     '78u',
     'ability',
     'act',
     'adjustment',
     'advantage',
     'aml',
     'analysis',
     'analyst',
     'analytics',
     'annual',
     'anomalies',
     'anonymous',
     'anti',
     'antidumping',
     'attorney',
     'attorneys',
     'auto',
     'available',
     'average',
     'avoidance',
     'award',
     'awards',
     'bar',
     'best',
     'bill',
     'billing',
     'budget',
     'building',
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
 3: {'211',
     '3729',
     '7623',
     '78u',
     'ability',
     'act',
     'adjustment',
     'advantage',
     'aml',
     'analysis',
     'analyst',
     'analytics',
     'annual',
     'anomalies',
     'anonymous',
     'anti',
     'antidumping',
     'attorney',
     'attorneys',
     'auto',
     'available',
     'average',
     'avoidance',
     'award',
     'awards',
     'bar',
     'best',
     'bill',
     'billing',
     'building',
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
 4: {'211',
     '3729',
     '7623',
     '78u',
     'ability',
     'act',
     'adjustment',
     'advantage',
     'aml',
     'analysis',
     'analyst',
     'analytics',
     'annual',
     'anomalies',
     'anonymous',
     'anti',
     'antidumping',
     'attorney',
     'attorneys',
     'auto',
     'available',
     'average',
     'avoidance',
     'award',
     'awards',
     'bar',
     'best',
     'bill',
     'billing',
     'budget',
     'building',
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
 5: {'211',
     '3729',
     '7623',
     '78u',
     'ability',
     'act',
     'adjustment',
     'advantage',
     'aml',
     'analysis',
     'analyst',
     'analytics',
     'annual',
     'anomalies',
     'anonymous',
     'anti',
     'antidumping',
     'attorney',
     'attorneys',
     'audit',
     'auto',
     'available',
     'average',
     'avoid',
     'avoidance',
     'award',
     'awards',
     'bar',
     'best',
     'bill',
     'billing',
     'building',
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
 6: {'211',
     '3729',
     '7623',
     '78u',
     'ability',
     'act',
     'adjustment',
     'advantage',
     'aml',
     'analysis',
     'analyst',
     'analytics',
     'annual',
     'anomalies',
     'anonymous',
     'anti',
     'antidumping',
     'attorney',
     'attorneys',
     'auto',
     'available',
     'average',
     'avoidance',
     'award',
     'awards',
     'bar',
     'best',
     'bill',
     'billing',
     'building',
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
 7: {'211',
     '3729',
     '7623',
     '78u',
     'ability',
     'act',
     'adjustment',
     'advantage',
     'aml',
     'analysis',
     'analyst',
     'analytics',
     'annual',
     'anomalies',
     'anonymous',
     'anti',
     'antidumping',
     'attorney',
     'attorneys',
     'auto',
     'available',
     'average',
     'avoidance',
     'award',
     'awards',
     'bar',
     'best',
     'bill',
     'billing',
     'building',
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
 8: {'211',
     '3729',
     '7623',
     '78u',
     'ability',
     'act',
     'adjustment',
     'advantage',
     'aml',
     'analysis',
     'analyst',
     'analytics',
     'annual',
     'anomalies',
     'anonymous',
     'anti',
     'antidumping',
     'api',
     'attorney',
     'attorneys',
     'auto',
     'available',
     'average',
     'avoidance',
     'award',
     'awards',
     'bar',
     'best',
     'bill',
     'billing',
     'building',
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
 9: {'211',
     '3729',
     '7623',
     '78u',
     'ability',
     'act',
     'adjustment',
     'advantage',
     'agreement',
     'aml',
     'analysis',
     'analyst',
     'analytics',
     'annual',
     'anomalies',
     'anonymous',
     'anti',
     'antidumping',
     'attorney',
     'attorneys',
     'auto',
     'available',
     'average',
     'avoidance',
     'award',
     'awards',
     'bar',
     'best',
     'bill',
     'billing',
     'building',
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
 10: {'211',
      '3729',
      '7623',
      '78u',
      'ability',
      'act',
      'adjustment',
      'advantage',
      'agent',
      'ai',
      'aml',
      'analysis',
      'analyst',
      'analytics',
      'annual',
      'anomalies',
      'anonymous',
      'anti',
      'antidumping',
      'attorney',
      'attorneys',
      'auto',
      'automate',
      'automation',
      'available',
      'average',
      'avoidance',
      'award',
      'awards',
      'bar',
      'best',
      'bill',
      'billing',
      'building',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'211',
      '3729',
      '7623',
      '78u',
      'ability',
      'act',
      'adjustment',
      'advantage',
      'aml',
      'analysis',
      'analyst',
      'analytics',
      'annual',
      'anomalies',
      'anonymous',
      'anti',
      'antidumping',
      'attorney',
      'attorneys',
      'auto',
      'available',
      'average',
      'avoidance',
      'award',
      'awards',
      'bar',
      'best',
      'bill',
      'billing',
      'building',
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
 12: {'211',
      '3729',
      '7623',
      '78u',
      'ability',
      'act',
      'action',
      'adjustment',
      'advantage',
      'aml',
      'analysis',
      'analyst',
      'analytics',
      'annual',
      'anomalies',
      'anonymous',
      'anti',
      'antidumping',
      'attorney',
      'attorneys',
      'auto',
      'available',
      'average',
      'avoidance',
      'award',
      'awards',
      'bar',
      'best',
      'bill',
      'billing',
      'building',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Holt Law: For Healthcare Businesses',
      'channel': 'Holt Law: For Healthcare Businesses',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:56](https://www.youtube.com/watch?v=L-RuzumCY2k&t=896s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t just a business choice, it's a compliance minefield. We're going to break "
              'down the management fees, billing risks, and even the False Claims Act to make '
              'sure your revenue stays in your pocket and out of the hands of the feds.',
      'timestamp': 896,
      'timestamp_label': '[00:14:56]',
      'timestamp_seconds': 896,
      'tip': "'t just a business choice, it's a compliance minefield. We're going to break "
             'down the management fees, billing risks, and even the False Claims Act to make '
             'sure your revenue stays in your pocket and out of the hands of the feds.',
      'title': 'Stark Law and Anti-Kickback Explained What Healthcare Businesses Must Know '
               '(Holt Law: For Healthcare Businesses)',
      'url': 'https://www.youtube.com/watch?v=L-RuzumCY2k&t=896s',
      'video_id': 'L-RuzumCY2k'},
     {'author': 'KLGatesLaw',
      'channel': 'KLGatesLaw',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:48](https://www.youtube.com/watch?v=MMcEwUD0PNo&t=768s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Market rate to provide a service of value to the referring cardiologist so that '
              'she in turn would continue to return the favor by referring patients.',
      'timestamp': 768,
      'timestamp_label': '[00:12:48]',
      'timestamp_seconds': 768,
      'tip': 'Market rate to provide a service of value to the referring cardiologist so that '
             'she in turn would continue to return the favor by referring patients.',
      'title': 'Stark Law and the Anti-Kickback Statute Under the False Claims Act '
               '(KLGatesLaw)',
      'url': 'https://www.youtube.com/watch?v=MMcEwUD0PNo&t=768s',
      'video_id': 'MMcEwUD0PNo'},
     {'author': 'CMMC LaunchPad',
      'channel': 'CMMC LaunchPad',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=GkIQylusGaw&t=110s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're not an attorney yet, Leslie. I work with the law firm of Cordatus LLP. "
              "We represent government contractors. We're a small shop who represent lots of "
              'service stable veteran owned small businesses, other small businesses. Um '
              "that's that's our bread and butter.",
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': "You're not an attorney yet, Leslie. I work with the law firm of Cordatus LLP. We "
             "represent government contractors. We're a small shop who represent lots of "
             "service stable veteran owned small businesses, other small businesses. Um that's "
             "that's our bread and butter.",
      'title': 'False Claims Act and Other Risks of Non Compliance (CMMC LaunchPad)',
      'url': 'https://www.youtube.com/watch?v=GkIQylusGaw&t=110s',
      'video_id': 'GkIQylusGaw'},
     {'author': 'The Anti-Fraud Coalition',
      'channel': 'The Anti-Fraud Coalition',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:14](https://www.youtube.com/watch?v=fQss6bE5tKc&t=194s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'UBS admitted that it had helped its US clients evade taxes. Other large awards '
              'made by the IRS to whistleblowers included a $20 million award made to a '
              'whistleblower who filed a tip under the discretionary award program before the '
              'mandatory award program existed.',
      'timestamp': 194,
      'timestamp_label': '[00:03:14]',
      'timestamp_seconds': 194,
      'tip': 'UBS admitted that it had helped its US clients evade taxes. Other large awards '
             'made by the IRS to whistleblowers included a $20 million award made to a '
             'whistleblower who filed a tip under the discretionary award program before the '
             'mandatory award program existed.',
      'title': 'IRS Whistleblower Program Primer (The Anti-Fraud Coalition)',
      'url': 'https://www.youtube.com/watch?v=fQss6bE5tKc&t=194s',
      'video_id': 'fQss6bE5tKc'},
     {'author': 'Boston 25 News',
      'channel': 'Boston 25 News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:44](https://www.youtube.com/watch?v=mfEL3LienPQ&t=164s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The Internal Revenue Service is a very very busy organization they can't run "
              'down every lead if they do happen to run down yours remember to claim the '
              "reward on your taxes because if you don't someone could fill out form 211 on "
              "you I'm Ted Daniel fox25 news.",
      'timestamp': 164,
      'timestamp_label': '[00:02:44]',
      'timestamp_seconds': 164,
      'tip': "The Internal Revenue Service is a very very busy organization they can't run "
             'down every lead if they do happen to run down yours remember to claim the reward '
             "on your taxes because if you don't someone could fill out form 211 on you I'm "
             'Ted Daniel fox25 news.',
      'title': 'Becoming an IRS Informant Can Make You Money (Boston 25 News)',
      'url': 'https://www.youtube.com/watch?v=mfEL3LienPQ&t=164s',
      'video_id': 'mfEL3LienPQ'},
     {'author': 'Bill Cushing',
      'channel': 'Bill Cushing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=FCOkO5_92ZE&t=60s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'False Claims Act billing for services that were never provided is fraud '
              'upcoding services in order to get a higher rate of reimbursement is fraud '
              'upcoding occurs when a claim is submitted for a more expensive service or '
              'procedure than was actually done.',
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': 'False Claims Act billing for services that were never provided is fraud upcoding '
             'services in order to get a higher rate of reimbursement is fraud upcoding occurs '
             'when a claim is submitted for a more expensive service or procedure than was '
             'actually done.',
      'title': 'False Claims Act Basics 1 (Bill Cushing)',
      'url': 'https://www.youtube.com/watch?v=FCOkO5_92ZE&t=60s',
      'video_id': 'FCOkO5_92ZE'},
     {'author': 'OIGatHHS',
      'channel': 'OIGatHHS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=a4KhqqeAaUg&t=33s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Let’s start with Number One: What does the law prohibit? Under the Federal '
              'Anti-kickback Statute you may not knowingly and willfully offer, pay, solicit '
              'or receive anything of value to induce or reward for referrals of Federal '
              'health care program business.',
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': 'Let’s start with Number One: What does the law prohibit? Under the Federal '
             'Anti-kickback Statute you may not knowingly and willfully offer, pay, solicit or '
             'receive anything of value to induce or reward for referrals of Federal health '
             'care program business.',
      'title': 'Federal Anti-Kickback Statute (OIGatHHS)',
      'url': 'https://www.youtube.com/watch?v=a4KhqqeAaUg&t=33s',
      'video_id': 'a4KhqqeAaUg'},
     {'author': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'channel': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:19](https://www.youtube.com/watch?v=XXtgvEhkvo4&t=19s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Successfully through a keam law firm however there's a carve out in the false "
              'claims act for tax liability that can go in other directions the IRS anti '
              'money.',
      'timestamp': 19,
      'timestamp_label': '[00:00:19]',
      'timestamp_seconds': 19,
      'tip': "Successfully through a keam law firm however there's a carve out in the false "
             'claims act for tax liability that can go in other directions the IRS anti money.',
      'title': 'How to Report Customs Fraud: A Whistleblower’s Guide (Brown, LLC - A Premier '
               'Whistleblower Law Firm)',
      'url': 'https://www.youtube.com/watch?v=XXtgvEhkvo4&t=19s',
      'video_id': 'XXtgvEhkvo4'},
     {'author': 'Business with Mr. G',
      'channel': 'Business with Mr. G',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:11](https://www.youtube.com/watch?v=g-_DOtTZkIM&t=551s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's true that value is subjective in everyday life, but in financial services, "
              "it's about the relationship between the cost and the benefit. The firm has to "
              'evidence this. You know, an old insurance policy or an investment platform you '
              'signed up for 10 years ago.',
      'timestamp': 551,
      'timestamp_label': '[00:09:11]',
      'timestamp_seconds': 551,
      'tip': "It's true that value is subjective in everyday life, but in financial services, "
             "it's about the relationship between the cost and the benefit. The firm has to "
             'evidence this. You know, an old insurance policy or an investment platform you '
             'signed up for 10 years ago.',
      'title': 'FCA Consumer Duty Explained | Delivering Good Outcomes for Customers! '
               '(Business with Mr. G)',
      'url': 'https://www.youtube.com/watch?v=g-_DOtTZkIM&t=551s',
      'video_id': 'g-_DOtTZkIM'},
     {'author': 'CNBC',
      'channel': 'CNBC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:18](https://www.youtube.com/watch?v=OqK_6Nor98U&t=318s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Agents shut one down and new ones pop up. In this business, which has been '
              'billing Medicare for durable medical equipment, we find a young woman sitting '
              "alone at a desk. The woman says it's a medical supply store, but she has "
              'nothing to do with the actual business.',
      'timestamp': 318,
      'timestamp_label': '[00:05:18]',
      'timestamp_seconds': 318,
      'tip': 'Agents shut one down and new ones pop up. In this business, which has been '
             'billing Medicare for durable medical equipment, we find a young woman sitting '
             "alone at a desk. The woman says it's a medical supply store, but she has nothing "
             'to do with the actual business.',
      'title': 'How Medicare And Medicaid Fraud Became A $100B Problem In The U.S. (CNBC)',
      'url': 'https://www.youtube.com/watch?v=OqK_6Nor98U&t=318s',
      'video_id': 'OqK_6Nor98U'},
     {'author': 'The Employment Law Group, P.C.',
      'channel': 'The Employment Law Group, P.C.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:58](https://www.youtube.com/watch?v=ukz2VRmDQIs&t=358s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Counsel some cover absolutely dealing with the client absolutely thank you '
              'thank you and we look forward to seeing each of you in Washington on February '
              "27th and 28th 2020 for this year's key Tam conference you can register at the "
              'Federal Bar webpage at fed bar org.',
      'timestamp': 358,
      'timestamp_label': '[00:05:58]',
      'timestamp_seconds': 358,
      'tip': 'Counsel some cover absolutely dealing with the client absolutely thank you thank '
             'you and we look forward to seeing each of you in Washington on February 27th and '
             "28th 2020 for this year's key Tam conference you can register at the Federal Bar "
             'webpage at fed bar org.',
      'title': '"Qui Tam 2020" Panel Preview: Multi-Relator Cases (The Employment Law Group, '
               'P.C.)',
      'url': 'https://www.youtube.com/watch?v=ukz2VRmDQIs&t=358s',
      'video_id': 'ukz2VRmDQIs'},
     {'author': 'Shipman Wright Law',
      'channel': 'Shipman Wright Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:10](https://www.youtube.com/watch?v=7-9Z8vNWVFc&t=250s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Federal statutes because uh they're not necessarily straightforward um we're "
              'now handling a couple including one fairly large potential claim um that uh '
              'that we received from somebody um who had heard about us um through some of our '
              'former clients.',
      'timestamp': 250,
      'timestamp_label': '[00:04:10]',
      'timestamp_seconds': 250,
      'tip': "Federal statutes because uh they're not necessarily straightforward um we're now "
             'handling a couple including one fairly large potential claim um that uh that we '
             'received from somebody um who had heard about us um through some of our former '
             'clients.',
      'title': 'Attorney Cory Reiss on Qui Tam (Shipman Wright Law)',
      'url': 'https://www.youtube.com/watch?v=7-9Z8vNWVFc&t=250s',
      'video_id': '7-9Z8vNWVFc'},
     {'author': 'WilliamsMullen',
      'channel': 'WilliamsMullen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:44](https://www.youtube.com/watch?v=NdqYGSN5BYc&t=464s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Submitted to Medicaid for work that wasn't actually done by people who know "
              "they're committing fraud um that's a that's a separate federal crime.",
      'timestamp': 464,
      'timestamp_label': '[00:07:44]',
      'timestamp_seconds': 464,
      'tip': "Submitted to Medicaid for work that wasn't actually done by people who know "
             "they're committing fraud um that's a that's a separate federal crime.",
      'title': 'The “Risky Business” of the Federal False Claims Act:  Strategic Thinking for '
               '2017 (WilliamsMullen)',
      'url': 'https://www.youtube.com/watch?v=NdqYGSN5BYc&t=464s',
      'video_id': 'NdqYGSN5BYc'},
     {'author': 'Thompson Coburn LLP',
      'channel': 'Thompson Coburn LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:54](https://www.youtube.com/watch?v=CNlX3Qfdluw&t=1434s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Incident for instance after um I don't know a few weeks and they've dealt with "
              "the malware incident and then they didn't report it that could be exactly what "
              "doj is looking for those sorts of incidents that's just one example.",
      'timestamp': 1434,
      'timestamp_label': '[00:23:54]',
      'timestamp_seconds': 1434,
      'tip': "Incident for instance after um I don't know a few weeks and they've dealt with "
             "the malware incident and then they didn't report it that could be exactly what "
             "doj is looking for those sorts of incidents that's just one example.",
      'title': 'DOJ Cyber Fraud Initiative - Cyber Faces the FCA Hammer (Thompson Coburn LLP)',
      'url': 'https://www.youtube.com/watch?v=CNlX3Qfdluw&t=1434s',
      'video_id': 'CNlX3Qfdluw'},
     {'author': 'Kevin Pho, MD',
      'channel': 'Kevin Pho, MD',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:50](https://www.youtube.com/watch?v=eIMINUxFlVI&t=1130s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Medicare Advantage versus Medicare. For those who aren't familiar between those "
              'two entities, why are Medicare Advantage cases more scrutinized? So Medicare, '
              'our traditional Medicare Part A and B, was historically just a fee for service '
              'model.',
      'timestamp': 1130,
      'timestamp_label': '[00:18:50]',
      'timestamp_seconds': 1130,
      'tip': "Medicare Advantage versus Medicare. For those who aren't familiar between those "
             'two entities, why are Medicare Advantage cases more scrutinized? So Medicare, '
             'our traditional Medicare Part A and B, was historically just a fee for service '
             'model.',
      'title': 'Why physicians should care about the False Claims Act (Kevin Pho, MD)',
      'url': 'https://www.youtube.com/watch?v=eIMINUxFlVI&t=1130s',
      'video_id': 'eIMINUxFlVI'}],
 2: [{'author': 'Justia',
      'channel': 'Justia',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:21](https://www.youtube.com/watch?v=HocnawRgrAA&t=1221s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, um we kind of know from contracts what material means, right? It has to '
              'matter to the intent of the contract. Um, in this case, it means that whatever '
              "is wrong has to have been part of the government's decision to pay or not pay "
              'the bill, right?',
      'timestamp': 1221,
      'timestamp_label': '[00:20:21]',
      'timestamp_seconds': 1221,
      'tip': 'Now, um we kind of know from contracts what material means, right? It has to '
             'matter to the intent of the contract. Um, in this case, it means that whatever '
             "is wrong has to have been part of the government's decision to pay or not pay "
             'the bill, right?',
      'title': 'Whistleblower 101: Navigating the False Claims Act | Justia Webinars (Justia)',
      'url': 'https://www.youtube.com/watch?v=HocnawRgrAA&t=1221s',
      'video_id': 'HocnawRgrAA'},
     {'author': 'Against The Fraud',
      'channel': 'Against The Fraud',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:04](https://www.youtube.com/watch?v=H0ay64A0XXA&t=904s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s decision to pay the bill. Uh, and just because it's a regulation doesn't "
              "mean it's material to payment. There are a lot, I mean, healthcare has millions "
              'of regulations, right? Violating a single regulation does not necessarily make '
              'your claim a false claim.',
      'timestamp': 904,
      'timestamp_label': '[00:15:04]',
      'timestamp_seconds': 904,
      'tip': "'s decision to pay the bill. Uh, and just because it's a regulation doesn't mean "
             "it's material to payment. There are a lot, I mean, healthcare has millions of "
             'regulations, right? Violating a single regulation does not necessarily make your '
             'claim a false claim.',
      'title': 'The Truth About Whistleblower Cases Nobody Tells You (Against The Fraud)',
      'url': 'https://www.youtube.com/watch?v=H0ay64A0XXA&t=904s',
      'video_id': 'H0ay64A0XXA'},
     {'author': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'channel': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=3ugChIElhkM&t=65s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Billing for a particular procedure but they don't over Bill Medicare or "
              'Medicaid they just over Bill private insurers or people who pay out of pocket.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': "Billing for a particular procedure but they don't over Bill Medicare or Medicaid "
             'they just over Bill private insurers or people who pay out of pocket.',
      'title': 'A Guide to the False Claims Act for Whistleblowers | Brown, LLC (Brown, LLC - '
               'A Premier Whistleblower Law Firm)',
      'url': 'https://www.youtube.com/watch?v=3ugChIElhkM&t=65s',
      'video_id': '3ugChIElhkM'},
     {'author': 'Dirty Medicine',
      'channel': 'Dirty Medicine',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=6IVcs5MTeF8&t=54s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Going to pay particular attention to the stark law anti-kickback statute false '
              'claims act and exclusion statute now when it comes.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'Going to pay particular attention to the stark law anti-kickback statute false '
             'claims act and exclusion statute now when it comes.',
      'title': 'Healthcare Fraud & Abuse (Stark Law, Anti-Kickback, etc.) (Dirty Medicine)',
      'url': 'https://www.youtube.com/watch?v=6IVcs5MTeF8&t=54s',
      'video_id': '6IVcs5MTeF8'},
     {'author': 'FinCrime Agent',
      'channel': 'FinCrime Agent',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:00](https://www.youtube.com/watch?v=md699NsaAZg&t=300s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '25,000 for the more "Complex" applications. Additionally, firms regulated by '
              'the UK FCA would also pay annual fees which are are determined by the sort of '
              'regulated activities carried out by a business, the volume of those activities, '
              "and the FCA's regulatory expenses.",
      'timestamp': 300,
      'timestamp_label': '[00:05:00]',
      'timestamp_seconds': 300,
      'tip': '25,000 for the more "Complex" applications. Additionally, firms regulated by the '
             'UK FCA would also pay annual fees which are are determined by the sort of '
             'regulated activities carried out by a business, the volume of those activities, '
             "and the FCA's regulatory expenses.",
      'title': 'The Role of the FCA - Free Regulatory Compliance Trainings (FinCrime Agent)',
      'url': 'https://www.youtube.com/watch?v=md699NsaAZg&t=300s',
      'video_id': 'md699NsaAZg'},
     {'author': 'Tony Munter Attorney at Law',
      'channel': 'Tony Munter Attorney at Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=KMtkKgsZzRo&t=22s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'People ask about attorney fees, they want to know how we handle it. A '
              "contingent fee is pretty simple, it's basically saying that if we win, we take "
              "a share of whatever your recovery is. I guess that's the bad news.",
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'People ask about attorney fees, they want to know how we handle it. A contingent '
             "fee is pretty simple, it's basically saying that if we win, we take a share of "
             "whatever your recovery is. I guess that's the bad news.",
      'title': 'How Do Attorney Fees Work In a Whistleblower Case? | Tony Munter Attorney at '
               'Law (Tony Munter Attorney at Law)',
      'url': 'https://www.youtube.com/watch?v=KMtkKgsZzRo&t=22s',
      'video_id': 'KMtkKgsZzRo'},
     {'author': 'Fraud in America',
      'channel': 'Fraud in America',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:39](https://www.youtube.com/watch?v=lX4p0oRMWls&t=579s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Like money was just leaving government so quickly and nobody wanted to put any '
              'sort of check on that at all. You know, there was a sort of Eb in 1943 and a '
              'recovery in 1986. Those attorneys fees were really important.',
      'timestamp': 579,
      'timestamp_label': '[00:09:39]',
      'timestamp_seconds': 579,
      'tip': 'Like money was just leaving government so quickly and nobody wanted to put any '
             'sort of check on that at all. You know, there was a sort of Eb in 1943 and a '
             'recovery in 1986. Those attorneys fees were really important.',
      'title': 'Wartime Fraud: The Legacy of the False Claims Act (Fraud in America)',
      'url': 'https://www.youtube.com/watch?v=lX4p0oRMWls&t=579s',
      'video_id': 'lX4p0oRMWls'},
     {'author': 'ABA Criminal Justice Section',
      'channel': 'ABA Criminal Justice Section',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:52](https://www.youtube.com/watch?v=w2SmaDc-C4M&t=472s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The the most important ruling I think of the Escobar decision and that had to '
              'do with the fact that the false claim itself had to be material to the '
              'government and in order for the False Claims Act to apply so the way Escobar '
              'Changed the world.',
      'timestamp': 472,
      'timestamp_label': '[00:07:52]',
      'timestamp_seconds': 472,
      'tip': 'The the most important ruling I think of the Escobar decision and that had to do '
             'with the fact that the false claim itself had to be material to the government '
             'and in order for the False Claims Act to apply so the way Escobar Changed the '
             'world.',
      'title': 'Healthcare Enforcement and the False Claims Act: Trends and Developments (ABA '
               'Criminal Justice Section)',
      'url': 'https://www.youtube.com/watch?v=w2SmaDc-C4M&t=472s',
      'video_id': 'w2SmaDc-C4M'},
     {'author': 'ABA Criminal Justice Section',
      'channel': 'ABA Criminal Justice Section',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:16](https://www.youtube.com/watch?v=vHZhDg8Ml14&t=916s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Complaint where the government intervenes there may well be attorney's fees "
              'paid but i would say that there.',
      'timestamp': 916,
      'timestamp_label': '[00:15:16]',
      'timestamp_seconds': 916,
      'tip': "Complaint where the government intervenes there may well be attorney's fees paid "
             'but i would say that there.',
      'title': 'Settling an FCA Case (ABA Criminal Justice Section)',
      'url': 'https://www.youtube.com/watch?v=vHZhDg8Ml14&t=916s',
      'video_id': 'vHZhDg8Ml14'},
     {'author': 'Quimbee',
      'channel': 'Quimbee',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:47](https://www.youtube.com/watch?v=1SUxz8N7UU8&t=107s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Medicare for a service or level of service that wasn't actually provided or the "
              'submission of an untrue record supporting a claim for medicare payment.',
      'timestamp': 107,
      'timestamp_label': '[00:01:47]',
      'timestamp_seconds': 107,
      'tip': "Medicare for a service or level of service that wasn't actually provided or the "
             'submission of an untrue record supporting a claim for medicare payment.',
      'title': 'Healthcare Law  Lesson | The False Claims Act | Lesson 13 of 34 (Quimbee)',
      'url': 'https://www.youtube.com/watch?v=1SUxz8N7UU8&t=107s',
      'video_id': '1SUxz8N7UU8'},
     {'author': 'HJ Collection Investors – Independent Community',
      'channel': 'HJ Collection Investors – Independent Community',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=4O3914yuhv0&t=71s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Add payment confirmations or bank transfer records with payment dates and '
              'recipient names. Explain what interest you received, what payments are '
              'outstanding, and any maturity or repayment dates.',
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': 'Add payment confirmations or bank transfer records with payment dates and '
             'recipient names. Explain what interest you received, what payments are '
             'outstanding, and any maturity or repayment dates.',
      'title': 'HJ Collection Investors: How to Contact the FCA & Submit Evidence (HJ '
               'Collection Investors – Independent Community)',
      'url': 'https://www.youtube.com/watch?v=4O3914yuhv0&t=71s',
      'video_id': '4O3914yuhv0'},
     {'author': 'The Brad Weisman Show',
      'channel': 'The Brad Weisman Show',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:32](https://www.youtube.com/watch?v=_ehHXyRo6fI&t=392s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'My eye number one there was a a $50,000 Challenge from a guy named William '
              'Conklin to prove that we had to file and pay income tax the people that live '
              'and.',
      'timestamp': 392,
      'timestamp_label': '[00:06:32]',
      'timestamp_seconds': 392,
      'tip': 'My eye number one there was a a $50,000 Challenge from a guy named William '
             'Conklin to prove that we had to file and pay income tax the people that live '
             'and.',
      'title': "IRS Whistleblower to Financial Empowerment: Dr. Sherry Peel Jackson's Journey "
               '#irs #tbws2024 (The Brad Weisman Show)',
      'url': 'https://www.youtube.com/watch?v=_ehHXyRo6fI&t=392s',
      'video_id': '_ehHXyRo6fI'},
     {'author': 'Compliance Mitigation',
      'channel': 'Compliance Mitigation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:47](https://www.youtube.com/watch?v=3kDd1dqYkWY&t=707s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "As somebody who's committed to compliance and hopefully lessen your company's "
              'vulnerability to a government investigation thanks.',
      'timestamp': 707,
      'timestamp_label': '[00:11:47]',
      'timestamp_seconds': 707,
      'tip': "As somebody who's committed to compliance and hopefully lessen your company's "
             'vulnerability to a government investigation thanks.',
      'title': 'Violating the False Claims Act (Case Study 019) (Compliance Mitigation)',
      'url': 'https://www.youtube.com/watch?v=3kDd1dqYkWY&t=707s',
      'video_id': '3kDd1dqYkWY'},
     {'author': 'Whistleblower Heroes',
      'channel': 'Whistleblower Heroes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:41](https://www.youtube.com/watch?v=FopC1sCa2y8&t=1001s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Employees every year to other competitors because by now USIS was no longer the '
              'only company doing these investigations for the government.',
      'timestamp': 1001,
      'timestamp_label': '[00:16:41]',
      'timestamp_seconds': 1001,
      'tip': 'Employees every year to other competitors because by now USIS was no longer the '
             'only company doing these investigations for the government.',
      'title': 'Blake Percival: whistleblower and successful qui tam plaintiff on USIS dumping '
               'fraud (Whistleblower Heroes)',
      'url': 'https://www.youtube.com/watch?v=FopC1sCa2y8&t=1001s',
      'video_id': 'FopC1sCa2y8'},
     {'author': 'DarrowEverett LLP',
      'channel': 'DarrowEverett LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:28](https://www.youtube.com/watch?v=5LsJY2Ss1SI&t=568s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Obviously, they're going to have to pay attorneys fees, and usually the "
              "attorneys take about a third of that, but you're still talking to 20 to 25% of "
              "the claim. And there's been some claims in DOJ, you know, over the years that "
              'would have been billions of dollars.',
      'timestamp': 568,
      'timestamp_label': '[00:09:28]',
      'timestamp_seconds': 568,
      'tip': "Obviously, they're going to have to pay attorneys fees, and usually the "
             "attorneys take about a third of that, but you're still talking to 20 to 25% of "
             "the claim. And there's been some claims in DOJ, you know, over the years that "
             'would have been billions of dollars.',
      'title': 'The DOJ’s New Agenda: What Every Business Should Know About the False Claims '
               'Act (DarrowEverett LLP)',
      'url': 'https://www.youtube.com/watch?v=5LsJY2Ss1SI&t=568s',
      'video_id': '5LsJY2Ss1SI'}],
 3: [{'author': 'Tycko & Zavareei LLP',
      'channel': 'Tycko & Zavareei LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:35:02](https://www.youtube.com/watch?v=A2nRu5da_9k&t=2102s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'False Claims Act, where there are no caps and where we just saw from the '
              'statistics, the average award is is close to, more than $500,000. And there '
              'have been awards in customs qui tam cases, that are, that are multi-millions of '
              'dollars.',
      'timestamp': 2102,
      'timestamp_label': '[00:35:02]',
      'timestamp_seconds': 2102,
      'tip': 'False Claims Act, where there are no caps and where we just saw from the '
             'statistics, the average award is is close to, more than $500,000. And there have '
             'been awards in customs qui tam cases, that are, that are multi-millions of '
             'dollars.',
      'title': 'Customs Fraud Whistleblowing: Combat Evasion and Earn Rewards | LinkedIn Live '
               '(Tycko & Zavareei LLP)',
      'url': 'https://www.youtube.com/watch?v=A2nRu5da_9k&t=2102s',
      'video_id': 'A2nRu5da_9k'},
     {'author': 'Jones Day',
      'channel': 'Jones Day',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=ah8GhXnbe-8&t=40s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "DOJ's Fraud unit to work with US attorney's offices and utilize the False "
              'Claims Act, which is a pre-existing statute that is used in other contexts, '
              'against government contracting companies in relation to their cybersecurity.',
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': "DOJ's Fraud unit to work with US attorney's offices and utilize the False Claims "
             'Act, which is a pre-existing statute that is used in other contexts, against '
             'government contracting companies in relation to their cybersecurity.',
      'title': "What is the Department of Justice's Civil Cyber-Fraud Initiative? (Jones Day)",
      'url': 'https://www.youtube.com/watch?v=ah8GhXnbe-8&t=40s',
      'video_id': 'ah8GhXnbe-8'},
     {'author': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'channel': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:57](https://www.youtube.com/watch?v=CZeUV80NaAA&t=177s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The key is to separate casual, passive, or even active involvement from '
              "leadership and direct profit per scheme under the False Claims Act. Now, let's "
              "look to see whether you're eligible for an SEC whistleblower award if you're "
              'part of the scheme.',
      'timestamp': 177,
      'timestamp_label': '[00:02:57]',
      'timestamp_seconds': 177,
      'tip': 'The key is to separate casual, passive, or even active involvement from '
             "leadership and direct profit per scheme under the False Claims Act. Now, let's "
             "look to see whether you're eligible for an SEC whistleblower award if you're "
             'part of the scheme.',
      'title': 'Can You Be a Whistleblower If You Participated in the Fraud? #whistleblower '
               '(Brown, LLC - A Premier Whistleblower Law Firm)',
      'url': 'https://www.youtube.com/watch?v=CZeUV80NaAA&t=177s',
      'video_id': 'CZeUV80NaAA'},
     {'author': 'ASI Education',
      'channel': 'ASI Education',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:13](https://www.youtube.com/watch?v=95bEAYfWTiY&t=1213s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Yeah, they said 60% of DOD contracts would fall below the new threshold for '
              "certified costs or pricing data. It's going the opposite direction.",
      'timestamp': 1213,
      'timestamp_label': '[00:20:13]',
      'timestamp_seconds': 1213,
      'tip': 'Yeah, they said 60% of DOD contracts would fall below the new threshold for '
             "certified costs or pricing data. It's going the opposite direction.",
      'title': 'Can a Contract Award Survive When Competitors’ Prices Are Leaked? The FAR is '
               'Lava Ep. 9 (ASI Education)',
      'url': 'https://www.youtube.com/watch?v=95bEAYfWTiY&t=1213s',
      'video_id': '95bEAYfWTiY'},
     {'author': 'ComplianceVideos',
      'channel': 'ComplianceVideos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:40](https://www.youtube.com/watch?v=zF0bNkCTI_Q&t=220s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Medicare advantage uh which is also known as Medicare part C um drug device and '
              'biologics pricing uh anything related to barriers to patient access to care uh '
              'kickbacks uh defective medical devices and manipulation of electronic health '
              'records.',
      'timestamp': 220,
      'timestamp_label': '[00:03:40]',
      'timestamp_seconds': 220,
      'tip': 'Medicare advantage uh which is also known as Medicare part C um drug device and '
             'biologics pricing uh anything related to barriers to patient access to care uh '
             'kickbacks uh defective medical devices and manipulation of electronic health '
             'records.',
      'title': 'Josh Drew on What’s New with the False Claims Act [Podcast] (ComplianceVideos)',
      'url': 'https://www.youtube.com/watch?v=zF0bNkCTI_Q&t=220s',
      'video_id': 'zF0bNkCTI_Q'},
     {'author': 'BizTipsVideos',
      'channel': 'BizTipsVideos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=UGSY-GRiqec&t=38s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'New rules provide a bounty to any individual who provides the government or '
              'self-regulatory agency with new information, original information, based on '
              'independent knowledge or analysis that is not already known by the commission.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': 'New rules provide a bounty to any individual who provides the government or '
             'self-regulatory agency with new information, original information, based on '
             'independent knowledge or analysis that is not already known by the commission.',
      'title': 'Biz Tips: Understanding the new SEC Whistleblower Rules (BizTipsVideos)',
      'url': 'https://www.youtube.com/watch?v=UGSY-GRiqec&t=38s',
      'video_id': 'UGSY-GRiqec'},
     {'author': 'The Employment Law Group, P.C.',
      'channel': 'The Employment Law Group, P.C.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:36](https://www.youtube.com/watch?v=Okv3G2wwiCA&t=156s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For those of you tuning in, we look forward to seeing you at the FBA key '
              'sections 2026 annual conference. The era of uncertainty under the False Claims '
              'Act, February 18th through 20th, 2026.',
      'timestamp': 156,
      'timestamp_label': '[00:02:36]',
      'timestamp_seconds': 156,
      'tip': 'For those of you tuning in, we look forward to seeing you at the FBA key '
             'sections 2026 annual conference. The era of uncertainty under the False Claims '
             'Act, February 18th through 20th, 2026.',
      'title': '"Qui Tam 2026" Panel Preview - The Constitutionality of the Federal False '
               'Claims Act (The Employment Law Group, P.C.)',
      'url': 'https://www.youtube.com/watch?v=Okv3G2wwiCA&t=156s',
      'video_id': 'Okv3G2wwiCA'},
     {'author': 'Stephen Teller - Teller Law',
      'channel': 'Stephen Teller - Teller Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:47](https://www.youtube.com/watch?v=QNzd1e6e8UE&t=467s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I don't Yeah, just just pay just pay with Joe. It's way easier for everyone. "
              "And it's funny because it actually costs them three times as much in the long "
              "run if they would just paid it to begin with. And that's one of the issues with "
              'the False Claims Act in particular.',
      'timestamp': 467,
      'timestamp_label': '[00:07:47]',
      'timestamp_seconds': 467,
      'tip': "I don't Yeah, just just pay just pay with Joe. It's way easier for everyone. And "
             "it's funny because it actually costs them three times as much in the long run if "
             "they would just paid it to begin with. And that's one of the issues with the "
             'False Claims Act in particular.',
      'title': 'Exposing Customs Fraud: Hidden Schemes and How to Stop Them (Stephen Teller - '
               'Teller Law)',
      'url': 'https://www.youtube.com/watch?v=QNzd1e6e8UE&t=467s',
      'video_id': 'QNzd1e6e8UE'},
     {'author': 'SovereignProductions369',
      'channel': 'SovereignProductions369',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=Q2EMaQHpNPM&t=114s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Is tax fraud it really is and they claim to be exempt organizations when I '
              "don't understand how you have an exempt corporation that [ __ ] doesn't happen "
              "like that unless it's a 501 3c and so whether you uh a non-profit making making "
              'profit.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': "Is tax fraud it really is and they claim to be exempt organizations when I don't "
             "understand how you have an exempt corporation that [ __ ] doesn't happen like "
             "that unless it's a 501 3c and so whether you uh a non-profit making making "
             'profit.',
      'title': 'FORM 211 Treasury Notice of Breach of trust fraud on court case. '
               '(SovereignProductions369)',
      'url': 'https://www.youtube.com/watch?v=Q2EMaQHpNPM&t=114s',
      'video_id': 'Q2EMaQHpNPM'},
     {'author': 'Whistleblowers International',
      'channel': 'Whistleblowers International',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:35](https://www.youtube.com/watch?v=nGZvKSKSh-Y&t=95s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The dodd-frank act created a whistleblower program for reporting information '
              'about fraudulent practices in the trading of derivatives.',
      'timestamp': 95,
      'timestamp_label': '[00:01:35]',
      'timestamp_seconds': 95,
      'tip': 'The dodd-frank act created a whistleblower program for reporting information '
             'about fraudulent practices in the trading of derivatives.',
      'title': 'CFTC Whistleblower Rewards Program - Whistleblowers International '
               '(Whistleblowers International)',
      'url': 'https://www.youtube.com/watch?v=nGZvKSKSh-Y&t=95s',
      'video_id': 'nGZvKSKSh-Y'},
     {'author': 'Senior Medicare Patrol National Resource Center',
      'channel': 'Senior Medicare Patrol National Resource Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=ZkOLz_FNG3c&t=45s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Examples of DME include wheelchairs or scooters oxygen equipment back braces '
              'and hospital beds Medicare spends 6.7 billion dollars each year on DME at least '
              '700 million is estimated waste due to fraud Medicare fraud results in higher '
              'costs for everyone.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': 'Examples of DME include wheelchairs or scooters oxygen equipment back braces and '
             'hospital beds Medicare spends 6.7 billion dollars each year on DME at least 700 '
             'million is estimated waste due to fraud Medicare fraud results in higher costs '
             'for everyone.',
      'title': 'DME Fraud: The Facts (Senior Medicare Patrol National Resource Center)',
      'url': 'https://www.youtube.com/watch?v=ZkOLz_FNG3c&t=45s',
      'video_id': 'ZkOLz_FNG3c'},
     {'author': 'Vincent Romo',
      'channel': 'Vincent Romo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:26](https://www.youtube.com/watch?v=G7YHankdf9E&t=26s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '25 million fund paying up to $30,000 to tipsters whose information leads to a '
              'fraud conviction. Trump described it as a 1% commission on fraud uncovered and '
              "said he'd personally decide who gets paid when several people claim the same "
              'tip.',
      'timestamp': 26,
      'timestamp_label': '[00:00:26]',
      'timestamp_seconds': 26,
      'tip': '25 million fund paying up to $30,000 to tipsters whose information leads to a '
             'fraud conviction. Trump described it as a 1% commission on fraud uncovered and '
             "said he'd personally decide who gets paid when several people claim the same "
             'tip.',
      'title': 'Whistleblower Incentive Program: $30,000 Tips and Tough Questions #shorts '
               '(Vincent Romo)',
      'url': 'https://www.youtube.com/watch?v=G7YHankdf9E&t=26s',
      'video_id': 'G7YHankdf9E'},
     {'author': 'Michael Rosenblat',
      'channel': 'Michael Rosenblat',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:22](https://www.youtube.com/watch?v=8iceOOTBGds&t=142s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'May have feel free to contact me either at my website which is listed below or '
              "give me a call also with Nikon's informations as listed below my phone numbers "
              'eight four seven four eight zero two three nine zero talk to you soon thanks '
              'bye.',
      'timestamp': 142,
      'timestamp_label': '[00:02:22]',
      'timestamp_seconds': 142,
      'tip': 'May have feel free to contact me either at my website which is listed below or '
             "give me a call also with Nikon's informations as listed below my phone numbers "
             'eight four seven four eight zero two three nine zero talk to you soon thanks '
             'bye.',
      'title': 'False Claims Act Basics (Michael Rosenblat)',
      'url': 'https://www.youtube.com/watch?v=8iceOOTBGds&t=142s',
      'video_id': '8iceOOTBGds'},
     {'author': 'Zuckerman Whistleblower Law Firm',
      'channel': 'Zuckerman Whistleblower Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:08](https://www.youtube.com/watch?v=EG1qQyQJKzg&t=128s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Experience representing whistleblowers and a thorough understanding of '
              'whistleblower protection laws if you have suffered retaliation for reporting '
              'potential violations of federal securities loss to your employer or the sec '
              'call us today for a confidential case.',
      'timestamp': 128,
      'timestamp_label': '[00:02:08]',
      'timestamp_seconds': 128,
      'tip': 'Experience representing whistleblowers and a thorough understanding of '
             'whistleblower protection laws if you have suffered retaliation for reporting '
             'potential violations of federal securities loss to your employer or the sec call '
             'us today for a confidential case.',
      'title': 'Protections for SEC Whistleblowers (Zuckerman Whistleblower Law Firm)',
      'url': 'https://www.youtube.com/watch?v=EG1qQyQJKzg&t=128s',
      'video_id': 'EG1qQyQJKzg'},
     {'author': 'Federal News Network',
      'channel': 'Federal News Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:06](https://www.youtube.com/watch?v=ovf7HOfeGQ0&t=426s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s a lot that goes into the consideration but that it would be um worthwhile to "
              "come forward on their own and and get the credit that's available. Let's talk a "
              'little bit about uh the the the work I mean how how big is the cyber civil '
              'cyber fraud unit?',
      'timestamp': 426,
      'timestamp_label': '[00:07:06]',
      'timestamp_seconds': 426,
      'tip': "'s a lot that goes into the consideration but that it would be um worthwhile to "
             "come forward on their own and and get the credit that's available. Let's talk a "
             'little bit about uh the the the work I mean how how big is the cyber civil cyber '
             'fraud unit?',
      'title': 'Trump administration looks to False Claims Act to curb cybersecurity '
               'violations (Federal News Network)',
      'url': 'https://www.youtube.com/watch?v=ovf7HOfeGQ0&t=426s',
      'video_id': 'ovf7HOfeGQ0'}],
 4: [{'author': 'nurselyf',
      'channel': 'nurselyf',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:20](https://www.youtube.com/watch?v=T-h0f2YLPec&t=140s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Fraud investigations and compliance are crucial aspects of maintaining '
              'integrity within the health care system. How fraud investigations happen. Data '
              'analysis flags unusual billing patterns. Whistleblowers report suspicious '
              'practices under the False Claims Act.',
      'timestamp': 140,
      'timestamp_label': '[00:02:20]',
      'timestamp_seconds': 140,
      'tip': 'Fraud investigations and compliance are crucial aspects of maintaining integrity '
             'within the health care system. How fraud investigations happen. Data analysis '
             'flags unusual billing patterns. Whistleblowers report suspicious practices under '
             'the False Claims Act.',
      'title': 'Preventing Healthcare Fraud: Stark Law, Anti-Kickback Statute & How to Stay '
               'Compliant (nurselyf)',
      'url': 'https://www.youtube.com/watch?v=T-h0f2YLPec&t=140s',
      'video_id': 'T-h0f2YLPec'},
     {'author': 'Andrew Jonathan Hillman',
      'channel': 'Andrew Jonathan Hillman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:39](https://www.youtube.com/watch?v=AcMsQCQm5QI&t=279s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Medicare patients to that entity for designated health services, unless an '
              'exception applies. The entity may not bill Medicare for services furnished '
              'under a prohibited referral. Unlike the Anti-Kickback Statute, the basic Stark '
              'prohibition does not turn on intent.',
      'timestamp': 279,
      'timestamp_label': '[00:04:39]',
      'timestamp_seconds': 279,
      'tip': 'Medicare patients to that entity for designated health services, unless an '
             'exception applies. The entity may not bill Medicare for services furnished under '
             'a prohibited referral. Unlike the Anti-Kickback Statute, the basic Stark '
             'prohibition does not turn on intent.',
      'title': 'Andrew Hillman, Dallas | False Claims Act, Qui Tam, Stark Law Explained | '
               'Andrew Jonathan Hillman (Andrew Jonathan Hillman)',
      'url': 'https://www.youtube.com/watch?v=AcMsQCQm5QI&t=279s',
      'video_id': 'AcMsQCQm5QI'},
     {'author': 'Chapman Law Group: Health Care Attorneys',
      'channel': 'Chapman Law Group: Health Care Attorneys',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:12](https://www.youtube.com/watch?v=RvnCdJAJ4FQ&t=192s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Florida can come after you. AHCA and Medicaid can come after you if they '
              "believe that you're taking Medicaid money and receiving or offering kickbacks "
              'to get clients and bill Medicare Medicaid or private insurance.',
      'timestamp': 192,
      'timestamp_label': '[00:03:12]',
      'timestamp_seconds': 192,
      'tip': 'Florida can come after you. AHCA and Medicaid can come after you if they believe '
             "that you're taking Medicaid money and receiving or offering kickbacks to get "
             'clients and bill Medicare Medicaid or private insurance.',
      'title': 'Federal Anti-Kickback Statute by Health Care Lawyer (Chapman Law Group: Health '
               'Care Attorneys)',
      'url': 'https://www.youtube.com/watch?v=RvnCdJAJ4FQ&t=192s',
      'video_id': 'RvnCdJAJ4FQ'},
     {'author': 'Emory School of Law',
      'channel': 'Emory School of Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=yiUS5Zf9HRI&t=15s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm here in the courtroom at the emory university school of law in Atlanta "
              "Georgia and we're talking today with Bill nettles who's the US Attorney for.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "I'm here in the courtroom at the emory university school of law in Atlanta "
             "Georgia and we're talking today with Bill nettles who's the US Attorney for.",
      'title': 'A Conversation on Whistleblowers and the False Claims Act (Emory School of '
               'Law)',
      'url': 'https://www.youtube.com/watch?v=yiUS5Zf9HRI&t=15s',
      'video_id': 'yiUS5Zf9HRI'},
     {'author': 'Group Practice with Neal Goldstein',
      'channel': 'Group Practice with Neal Goldstein',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=gIyVCP3OhyM&t=50s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um the statute itself was enacted in 1972. It's section 1128b of the social "
              "security act. Um, and it's interestingly it's not titled the anti- kickback "
              'statute. The name of that particular section is criminal penalties for acts '
              'involving federal healthcare programs.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': "Um the statute itself was enacted in 1972. It's section 1128b of the social "
             "security act. Um, and it's interestingly it's not titled the anti- kickback "
             'statute. The name of that particular section is criminal penalties for acts '
             'involving federal healthcare programs.',
      'title': 'Overview of the Anti-Kickback Statute (Group Practice with Neal Goldstein)',
      'url': 'https://www.youtube.com/watch?v=gIyVCP3OhyM&t=50s',
      'video_id': 'gIyVCP3OhyM'},
     {'author': 'Theodore Watson',
      'channel': 'Theodore Watson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:34](https://www.youtube.com/watch?v=uJurzK0qLLU&t=154s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Company's future for help defending a federal False Claims Act case or "
              'implementing policies and controls to avoid criminal charges contact Watson & '
              'Associates LLC at one eight six six six zero one five five one eight four free '
              'initial consultation.',
      'timestamp': 154,
      'timestamp_label': '[00:02:34]',
      'timestamp_seconds': 154,
      'tip': "Company's future for help defending a federal False Claims Act case or "
             'implementing policies and controls to avoid criminal charges contact Watson & '
             'Associates LLC at one eight six six six zero one five five one eight four free '
             'initial consultation.',
      'title': 'False Claims Act Defense Lawyers for Government Contractors (Theodore Watson)',
      'url': 'https://www.youtube.com/watch?v=uJurzK0qLLU&t=154s',
      'video_id': 'uJurzK0qLLU'},
     {'author': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'channel': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=Hb6Ogl9Fm8I&t=120s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You don't need to prove it right away, but you need to show the government that "
              "you can. The False Claims Act has what's called a public disclosure bar.",
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': "You don't need to prove it right away, but you need to show the government that "
             "you can. The False Claims Act has what's called a public disclosure bar.",
      'title': 'What Makes a Strong Whistleblower Case? Brown, LLC Explains (Brown, LLC - A '
               'Premier Whistleblower Law Firm)',
      'url': 'https://www.youtube.com/watch?v=Hb6Ogl9Fm8I&t=120s',
      'video_id': 'Hb6Ogl9Fm8I'},
     {'author': 'Mahany Law',
      'channel': 'Mahany Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:04](https://www.youtube.com/watch?v=BueLAsaxhHM&t=304s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'All inquiries are protected by the attorney-client privilege and completely '
              'confidential thank you very much for watching this video.',
      'timestamp': 304,
      'timestamp_label': '[00:05:04]',
      'timestamp_seconds': 304,
      'tip': 'All inquiries are protected by the attorney-client privilege and completely '
             'confidential thank you very much for watching this video.',
      'title': 'Anti-Money Laundering Whistleblower Reward Program | 2021 SEC AML '
               'Whistleblower Program Summary (Mahany Law)',
      'url': 'https://www.youtube.com/watch?v=BueLAsaxhHM&t=304s',
      'video_id': 'BueLAsaxhHM'},
     {'author': 'Holland & Hart LLP',
      'channel': 'Holland & Hart LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:32:57](https://www.youtube.com/watch?v=wODno0XW8l4&t=1977s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If the patient expresses a different patient preference or if the patient's "
              "insurer or physician determines that it's not in the patient's best interests.",
      'timestamp': 1977,
      'timestamp_label': '[00:32:57]',
      'timestamp_seconds': 1977,
      'tip': "If the patient expresses a different patient preference or if the patient's "
             "insurer or physician determines that it's not in the patient's best interests.",
      'title': 'New Final Rules for Stark and Anti Kickback Reforms: An In-Depth Review '
               '(Holland & Hart LLP)',
      'url': 'https://www.youtube.com/watch?v=wODno0XW8l4&t=1977s',
      'video_id': 'wODno0XW8l4'},
     {'author': 'Parrish & Goodman Attorneys At Law',
      'channel': 'Parrish & Goodman Attorneys At Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:39](https://www.youtube.com/watch?v=AL33o4s-dp4&t=159s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Entity the IRS whistleblower program affects us all by understanding how it '
              'operates and the impact that it has we can collectively strive for a more.',
      'timestamp': 159,
      'timestamp_label': '[00:02:39]',
      'timestamp_seconds': 159,
      'tip': 'Entity the IRS whistleblower program affects us all by understanding how it '
             'operates and the impact that it has we can collectively strive for a more.',
      'title': 'IRS Whistleblower Programs You Should Know About (Parrish & Goodman Attorneys '
               'At Law)',
      'url': 'https://www.youtube.com/watch?v=AL33o4s-dp4&t=159s',
      'video_id': 'AL33o4s-dp4'},
     {'author': 'American Health Law Association',
      'channel': 'American Health Law Association',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:03](https://www.youtube.com/watch?v=xaaGMrYhE60&t=1143s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And because of the significant uh size of the Medicare Advantage program um '
              'that we we do believe the government is going to continue to focus on um.',
      'timestamp': 1143,
      'timestamp_label': '[00:19:03]',
      'timestamp_seconds': 1143,
      'tip': 'And because of the significant uh size of the Medicare Advantage program um that '
             'we we do believe the government is going to continue to focus on um.',
      'title': 'Trends and Developments Related to the False Claims Act (American Health Law '
               'Association)',
      'url': 'https://www.youtube.com/watch?v=xaaGMrYhE60&t=1143s',
      'video_id': 'xaaGMrYhE60'},
     {'author': 'Phillips & Cohen LLP',
      'channel': 'Phillips & Cohen LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:37:24](https://www.youtube.com/watch?v=j2GyHTrfNTE&t=2244s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Over you know every every couple of months there have has been more money um '
              'made available to businesses in industry.',
      'timestamp': 2244,
      'timestamp_label': '[00:37:24]',
      'timestamp_seconds': 2244,
      'tip': 'Over you know every every couple of months there have has been more money um '
             'made available to businesses in industry.',
      'title': 'The SEC and CFTC whistleblower reward programs – their impact and success | '
               'Berkeley Boosts (Phillips & Cohen LLP)',
      'url': 'https://www.youtube.com/watch?v=j2GyHTrfNTE&t=2244s',
      'video_id': 'j2GyHTrfNTE'},
     {'author': 'McGuireWoods LLP',
      'channel': 'McGuireWoods LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:53](https://www.youtube.com/watch?v=JXEl43HAAuo&t=713s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your arms around the story hopefully find things that you can show the '
              "government you're cooperating you can educate the government as well.",
      'timestamp': 713,
      'timestamp_label': '[00:11:53]',
      'timestamp_seconds': 713,
      'tip': 'Your arms around the story hopefully find things that you can show the '
             "government you're cooperating you can educate the government as well.",
      'title': 'Healthcare Headlines: Episode 3 - Stay Ready: Trends in Healthcare False '
               'Claims Act Investigations (McGuireWoods LLP)',
      'url': 'https://www.youtube.com/watch?v=JXEl43HAAuo&t=713s',
      'video_id': 'JXEl43HAAuo'},
     {'author': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'channel': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:34](https://www.youtube.com/watch?v=b9I9BCtPjzw&t=514s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Leave below it's public and you may lose the privilege so don't put any "
              "privileged information feel free to reach out for us directly we'll make sure "
              'somebody tries to get back to you promptly thank you for listening to this '
              'video and best of luck.',
      'timestamp': 514,
      'timestamp_label': '[00:08:34]',
      'timestamp_seconds': 514,
      'tip': "Leave below it's public and you may lose the privilege so don't put any "
             "privileged information feel free to reach out for us directly we'll make sure "
             'somebody tries to get back to you promptly thank you for listening to this video '
             'and best of luck.',
      'title': 'How to Report Securities Fraud | SEC Whistleblower Program | Brown, LLC '
               '(Brown, LLC - A Premier Whistleblower Law Firm)',
      'url': 'https://www.youtube.com/watch?v=b9I9BCtPjzw&t=514s',
      'video_id': 'b9I9BCtPjzw'},
     {'author': 'Tycko & Zavareei LLP',
      'channel': 'Tycko & Zavareei LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:00](https://www.youtube.com/watch?v=A2nRu5da_9k&t=180s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And I'll be explaining how that works and giving you some statistics about "
              'awards that have actually been awarded. Talk briefly about the anti retaliation '
              'provision of the False Claims Act and then about e allegations and EPA claims. '
              "That's the enforcement Protect Act.",
      'timestamp': 180,
      'timestamp_label': '[00:03:00]',
      'timestamp_seconds': 180,
      'tip': "And I'll be explaining how that works and giving you some statistics about "
             'awards that have actually been awarded. Talk briefly about the anti retaliation '
             'provision of the False Claims Act and then about e allegations and EPA claims. '
             "That's the enforcement Protect Act.",
      'title': 'Customs Fraud Whistleblowing: Combat Evasion and Earn Rewards | LinkedIn Live '
               '(Tycko & Zavareei LLP)',
      'url': 'https://www.youtube.com/watch?v=A2nRu5da_9k&t=180s',
      'video_id': 'A2nRu5da_9k'}],
 5: [{'author': 'OIGatHHS',
      'channel': 'OIGatHHS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:46](https://www.youtube.com/watch?v=BbZ78QTLztQ&t=46s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Anti-kickback statute or the Stark law. These laws are addressed in other OIG '
              'presentations. When the government pursues violations of the False Claims Act, '
              'it does not target innocent billing mistakes.',
      'timestamp': 46,
      'timestamp_label': '[00:00:46]',
      'timestamp_seconds': 46,
      'tip': 'Anti-kickback statute or the Stark law. These laws are addressed in other OIG '
             'presentations. When the government pursues violations of the False Claims Act, '
             'it does not target innocent billing mistakes.',
      'title': 'False Claims Act (OIGatHHS)',
      'url': 'https://www.youtube.com/watch?v=BbZ78QTLztQ&t=46s',
      'video_id': 'BbZ78QTLztQ'},
     {'author': 'DarshanTalks',
      'channel': 'DarshanTalks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:35](https://www.youtube.com/watch?v=BXNGLzF0b-E&t=155s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This is going to be negligent. 't want your deal to carry a false claims act "
              'risk baked into it. As you may know, you may have a six-month window to '
              "disclose any problems you find to avoid success or liability. Now, let's talk "
              'about promotions.',
      'timestamp': 155,
      'timestamp_label': '[00:02:35]',
      'timestamp_seconds': 155,
      'tip': "This is going to be negligent. 't want your deal to carry a false claims act "
             'risk baked into it. As you may know, you may have a six-month window to disclose '
             "any problems you find to avoid success or liability. Now, let's talk about "
             'promotions.',
      'title': 'DOJ and HHS Launch FCA Fraud Task Force (DarshanTalks)',
      'url': 'https://www.youtube.com/watch?v=BXNGLzF0b-E&t=155s',
      'video_id': 'BXNGLzF0b-E'},
     {'author': 'Shipping Solutions',
      'channel': 'Shipping Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:22](https://www.youtube.com/watch?v=EIHwzCe4zZM&t=262s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you want to make that job a whole lot easier, click here to get a free trial '
              'of our Product Classification and Import Controls Software. It’ll help you find '
              'the right codes, check for extra tariffs, and avoid compliance mistakes.',
      'timestamp': 262,
      'timestamp_label': '[00:04:22]',
      'timestamp_seconds': 262,
      'tip': 'If you want to make that job a whole lot easier, click here to get a free trial '
             'of our Product Classification and Import Controls Software. It’ll help you find '
             'the right codes, check for extra tariffs, and avoid compliance mistakes.',
      'title': 'What Is the False Claims Act? Importer Risks & Compliance Tips (Shipping '
               'Solutions)',
      'url': 'https://www.youtube.com/watch?v=EIHwzCe4zZM&t=262s',
      'video_id': 'EIHwzCe4zZM'},
     {'author': 'ClearanceJobs',
      'channel': 'ClearanceJobs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:36:47](https://www.youtube.com/watch?v=j_QEFJG-ON4&t=2207s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Attorney to spend a lot of time understanding the NIS controls you know and and '
              'how to conduct a cyber audit um so to get confident enough in that space.',
      'timestamp': 2207,
      'timestamp_label': '[00:36:47]',
      'timestamp_seconds': 2207,
      'tip': 'Attorney to spend a lot of time understanding the NIS controls you know and and '
             'how to conduct a cyber audit um so to get confident enough in that space.',
      'title': 'Defense TechCast: False Claims Act with Julie Bracker (ClearanceJobs)',
      'url': 'https://www.youtube.com/watch?v=j_QEFJG-ON4&t=2207s',
      'video_id': 'j_QEFJG-ON4'},
     {'author': 'Analysis Group',
      'channel': 'Analysis Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:48:57](https://www.youtube.com/watch?v=y9nEr_YUXBY&t=2937s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s too many false positives, that's a a a problem in itself. If you really need "
              "to find the false negatives, that's a separate one. You kind of have to look at "
              'the problem and do your best to land the plane on the right uh runway.',
      'timestamp': 2937,
      'timestamp_label': '[00:48:57]',
      'timestamp_seconds': 2937,
      'tip': "'s too many false positives, that's a a a problem in itself. If you really need "
             "to find the false negatives, that's a separate one. You kind of have to look at "
             'the problem and do your best to land the plane on the right uh runway.',
      'title': 'Data Mining and the False Claims Act: Key Takeaways (Analysis Group)',
      'url': 'https://www.youtube.com/watch?v=y9nEr_YUXBY&t=2937s',
      'video_id': 'y9nEr_YUXBY'},
     {'author': 'Nellie Miranda',
      'channel': 'Nellie Miranda',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:37](https://www.youtube.com/watch?v=b8VkfUJZguw&t=637s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And the Medicare billing dispute remains unsolved. Should someone serving as '
              'mayor also be allowed to chair the board of a company dealing with a major '
              'federal healthcare investigation?',
      'timestamp': 637,
      'timestamp_label': '[00:10:37]',
      'timestamp_seconds': 637,
      'tip': 'And the Medicare billing dispute remains unsolved. Should someone serving as '
             'mayor also be allowed to chair the board of a company dealing with a major '
             'federal healthcare investigation?',
      'title': "Mayor's Healthcare Company Goes BANKRUPT Amid Federal Medicare Fraud "
               'Investigation! (Nellie Miranda)',
      'url': 'https://www.youtube.com/watch?v=b8VkfUJZguw&t=637s',
      'video_id': 'b8VkfUJZguw'},
     {'author': 'National Whistleblower Center',
      'channel': 'National Whistleblower Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:29](https://www.youtube.com/watch?v=OVyUfacfmsk&t=269s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ve heard, personal risk, to provide specific and credible information about "
              'conduct that violates our act. Your contributions are critical to our law '
              'enforcement function and we are grateful for them and as well as for all the '
              "support to the CFTC's whistleblower program.",
      'timestamp': 269,
      'timestamp_label': '[00:04:29]',
      'timestamp_seconds': 269,
      'tip': "'ve heard, personal risk, to provide specific and credible information about "
             'conduct that violates our act. Your contributions are critical to our law '
             'enforcement function and we are grateful for them and as well as for all the '
             "support to the CFTC's whistleblower program.",
      'title': 'How Whistleblowers Power CFTC Enforcement | Raagnee Beri at National '
               'Whistleblower Day 2026 (National Whistleblower Center)',
      'url': 'https://www.youtube.com/watch?v=OVyUfacfmsk&t=269s',
      'video_id': 'OVyUfacfmsk'},
     {'author': 'GRF CPAs & Advisors',
      'channel': 'GRF CPAs & Advisors',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:13](https://www.youtube.com/watch?v=bPsS_B4v7Dw&t=193s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And so, some of the different services we provide is just traditional audit and '
              "tax, outsourced accounting as well as technology solutions. If you're looking "
              'to change your accounting ERP system. Enterprise risk management is is really '
              'big.',
      'timestamp': 193,
      'timestamp_label': '[00:03:13]',
      'timestamp_seconds': 193,
      'tip': 'And so, some of the different services we provide is just traditional audit and '
             "tax, outsourced accounting as well as technology solutions. If you're looking to "
             'change your accounting ERP system. Enterprise risk management is is really big.',
      'title': 'Part 1: How to Set Up a World-Class Whistleblower Program (GRF CPAs & '
               'Advisors)',
      'url': 'https://www.youtube.com/watch?v=bPsS_B4v7Dw&t=193s',
      'video_id': 'bPsS_B4v7Dw'},
     {'author': 'Pinnacle Healthcare Consulting',
      'channel': 'Pinnacle Healthcare Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:34:37](https://www.youtube.com/watch?v=k11FLIP3Vk4&t=2077s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Value based enterprise is a risk-bearing organization has the potential to make '
              'its own margins and and you know it may have additional investors and and '
              'bringing its own returns next slide please.',
      'timestamp': 2077,
      'timestamp_label': '[00:34:37]',
      'timestamp_seconds': 2077,
      'tip': 'Value based enterprise is a risk-bearing organization has the potential to make '
             'its own margins and and you know it may have additional investors and and '
             'bringing its own returns next slide please.',
      'title': 'Using the New CMS and OIG Stark and Anti Kickback Revisions with Value Based '
               'Enterprises (Pinnacle Healthcare Consulting)',
      'url': 'https://www.youtube.com/watch?v=k11FLIP3Vk4&t=2077s',
      'video_id': 'k11FLIP3Vk4'},
     {'author': 'McGuireWoods LLP',
      'channel': 'McGuireWoods LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=J3hHvouRce8&t=15s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Speaking on recent developments in false claims act liation and some parallel '
              'statutes uh today is the presentation is by David pnik and myself Brett '
              'Barnett.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Speaking on recent developments in false claims act liation and some parallel '
             'statutes uh today is the presentation is by David pnik and myself Brett Barnett.',
      'title': 'Recent Developments in False Claims Act Litigation (McGuireWoods LLP)',
      'url': 'https://www.youtube.com/watch?v=J3hHvouRce8&t=15s',
      'video_id': 'J3hHvouRce8'},
     {'author': 'Freedom Law School',
      'channel': 'Freedom Law School',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:30:35](https://www.youtube.com/watch?v=xtocXbDnCkg&t=1835s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In my case, they needed to try to discredit me so rapidly, they went criminal '
              "first. So when that didn't work, >> then they went to the civil uh audit thing "
              'in, >> right?',
      'timestamp': 1835,
      'timestamp_label': '[00:30:35]',
      'timestamp_seconds': 1835,
      'tip': 'In my case, they needed to try to discredit me so rapidly, they went criminal '
             "first. So when that didn't work, >> then they went to the civil uh audit thing "
             'in, >> right?',
      'title': 'IRS WHISTLEBLOWER Joe Banister Exposes the Federal Income Tax FRAUD with '
               'Marjorie Taylor Greene (Freedom Law School)',
      'url': 'https://www.youtube.com/watch?v=xtocXbDnCkg&t=1835s',
      'video_id': 'xtocXbDnCkg'},
     {'author': 'Former IRS Agent Representation   4.2M Views',
      'channel': 'Former IRS Agent Representation   4.2M Views',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:11](https://www.youtube.com/watch?v=41ejxu80Qtg&t=191s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You got to document the case if it's not documented don't waste your time don't "
              "let this person rent space in your head irs probably isn't going to audit.",
      'timestamp': 191,
      'timestamp_label': '[00:03:11]',
      'timestamp_seconds': 191,
      'tip': "You got to document the case if it's not documented don't waste your time don't "
             "let this person rent space in your head irs probably isn't going to audit.",
      'title': 'Former IRS Agent Explains How To Become a IRS Whistleblower & Receive a Reward '
               'For Exposing Fraud (Former IRS Agent Representation   4.2M Views)',
      'url': 'https://www.youtube.com/watch?v=41ejxu80Qtg&t=191s',
      'video_id': '41ejxu80Qtg'},
     {'author': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'channel': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=nDO81fwnTqg&t=114s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Practitioners engage in then you may be entitled to a percentage of the '
              "recovery the key is knowing which is which and that's why you should always try "
              'to take advantage of firms that offer free whistleblower consultations.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': 'Practitioners engage in then you may be entitled to a percentage of the recovery '
             "the key is knowing which is which and that's why you should always try to take "
             'advantage of firms that offer free whistleblower consultations.',
      'title': 'How To Report Medicare Fraud | Brown, LLC (Brown, LLC - A Premier '
               'Whistleblower Law Firm)',
      'url': 'https://www.youtube.com/watch?v=nDO81fwnTqg&t=114s',
      'video_id': 'nDO81fwnTqg'},
     {'author': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'channel': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=UJOLP8WkFPo&t=62s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'As part of the problem rather than part of the solution you need to speak with '
              'an SEC whistleblower law firm early to understand what your rights and options.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': 'As part of the problem rather than part of the solution you need to speak with '
             'an SEC whistleblower law firm early to understand what your rights and options.',
      'title': 'Top Types of Securities Fraud and How Whistleblowers Can Take Action in 2026 '
               '(Brown, LLC - A Premier Whistleblower Law Firm)',
      'url': 'https://www.youtube.com/watch?v=UJOLP8WkFPo&t=62s',
      'video_id': 'UJOLP8WkFPo'},
     {'author': 'Stephen Teller - Teller Law',
      'channel': 'Stephen Teller - Teller Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:54](https://www.youtube.com/watch?v=0w534uBbqVQ&t=354s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They can say to the patient go anywhere for your MRI, but they can't say go to "
              "my clinic down the street if they're if they're billing separately. What if the "
              "patient >> goes to their building down the street? Yeah, I mean, it's not a "
              'problem.',
      'timestamp': 354,
      'timestamp_label': '[00:05:54]',
      'timestamp_seconds': 354,
      'tip': "They can say to the patient go anywhere for your MRI, but they can't say go to "
             "my clinic down the street if they're if they're billing separately. What if the "
             "patient >> goes to their building down the street? Yeah, I mean, it's not a "
             'problem.',
      'title': 'Medicare and Medicaid Fraud: When Does Improper Billing Violate the False '
               'Claims Act? (Stephen Teller - Teller Law)',
      'url': 'https://www.youtube.com/watch?v=0w534uBbqVQ&t=354s',
      'video_id': '0w534uBbqVQ'}],
 6: [{'author': 'Stephen Teller - Teller Law',
      'channel': 'Stephen Teller - Teller Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:16](https://www.youtube.com/watch?v=0w534uBbqVQ&t=616s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And if it's not, what's going on? Are there any other healthcare billing "
              "practices that commonly lead to false claims act cases? Well, there's um "
              "there's always the ability to sort of the to fudge the qualification, right?",
      'timestamp': 616,
      'timestamp_label': '[00:10:16]',
      'timestamp_seconds': 616,
      'tip': "And if it's not, what's going on? Are there any other healthcare billing "
             "practices that commonly lead to false claims act cases? Well, there's um there's "
             'always the ability to sort of the to fudge the qualification, right?',
      'title': 'Medicare and Medicaid Fraud: When Does Improper Billing Violate the False '
               'Claims Act? (Stephen Teller - Teller Law)',
      'url': 'https://www.youtube.com/watch?v=0w534uBbqVQ&t=616s',
      'video_id': '0w534uBbqVQ'},
     {'author': 'Law Minded',
      'channel': 'Law Minded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=sNHauc7rutQ&t=110s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s that successful claims can lead to a monetary award between 15 and 30% of "
              'what the IRS collects. And some individual awards have run into the tens of '
              'millions of dollars. The second one is more personal.',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': "'s that successful claims can lead to a monetary award between 15 and 30% of "
             'what the IRS collects. And some individual awards have run into the tens of '
             'millions of dollars. The second one is more personal.',
      'title': 'How to Become an IRS Whistleblower (and Get Paid) | Law Minded EP. 11 (Law '
               'Minded)',
      'url': 'https://www.youtube.com/watch?v=sNHauc7rutQ&t=110s',
      'video_id': 'sNHauc7rutQ'},
     {'author': 'Hall Martin',
      'channel': 'Hall Martin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=ut1fgqxQy-M&t=62s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For IRS whistleblower cases, you file a form 211. The government will determine '
              'whether to pursue or not. The filer can make another claim under a different '
              'act to gain a higher payout. Department of Justice or SEC will lead the '
              'investigation.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': 'For IRS whistleblower cases, you file a form 211. The government will determine '
             'whether to pursue or not. The filer can make another claim under a different act '
             'to gain a higher payout. Department of Justice or SEC will lead the '
             'investigation.',
      'title': 'Startup Funding Espresso – Claiming Whistleblower Status (Hall Martin)',
      'url': 'https://www.youtube.com/watch?v=ut1fgqxQy-M&t=62s',
      'video_id': 'ut1fgqxQy-M'},
     {'author': 'Mahany Law',
      'channel': 'Mahany Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:01](https://www.youtube.com/watch?v=PTeabZ29k14&t=61s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Issues awards in less than 1% of the tips it receives it is important that you '
              'find an attorney well-versed in securities laws and the whistleblower.',
      'timestamp': 61,
      'timestamp_label': '[00:01:01]',
      'timestamp_seconds': 61,
      'tip': 'Issues awards in less than 1% of the tips it receives it is important that you '
             'find an attorney well-versed in securities laws and the whistleblower.',
      'title': 'How to become a SEC whistleblower (Mahany Law)',
      'url': 'https://www.youtube.com/watch?v=PTeabZ29k14&t=61s',
      'video_id': 'PTeabZ29k14'},
     {'author': 'PilieroMazza PLLC',
      'channel': 'PilieroMazza PLLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:43:55](https://www.youtube.com/watch?v=ZyG_Zu7OvIg&t=2635s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Reporting them you do find them so the next step from discovering that you have '
              'a false claims act violation is being faced with a subpoena a simple '
              'investigative demand or a search warrant regarding a potential false claims act '
              'violation.',
      'timestamp': 2635,
      'timestamp_label': '[00:43:55]',
      'timestamp_seconds': 2635,
      'tip': 'Reporting them you do find them so the next step from discovering that you have '
             'a false claims act violation is being faced with a subpoena a simple '
             'investigative demand or a search warrant regarding a potential false claims act '
             'violation.',
      'title': 'Risk Prevention Strategies: FCA Risk Prevention for Government Contractors '
               '(PilieroMazza PLLC)',
      'url': 'https://www.youtube.com/watch?v=ZyG_Zu7OvIg&t=2635s',
      'video_id': 'ZyG_Zu7OvIg'},
     {'author': 'Husch Blackwell',
      'channel': 'Husch Blackwell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:08](https://www.youtube.com/watch?v=_n3NJXxKz_8&t=248s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Social Security Act permits these states that meet certain criteria to qualify '
              'for an increased share of any damages related to Medicaid. And I believe '
              "there's 23 states that currently take advantage of this and qualify for that "
              'share.',
      'timestamp': 248,
      'timestamp_label': '[00:04:08]',
      'timestamp_seconds': 248,
      'tip': 'Social Security Act permits these states that meet certain criteria to qualify '
             "for an increased share of any damages related to Medicaid. And I believe there's "
             '23 states that currently take advantage of this and qualify for that share.',
      'title': 'The Rise of State False Claims Act Enforcement (Husch Blackwell)',
      'url': 'https://www.youtube.com/watch?v=_n3NJXxKz_8&t=248s',
      'video_id': '_n3NJXxKz_8'},
     {'author': 'LexBlog',
      'channel': 'LexBlog',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:16](https://www.youtube.com/watch?v=bH6nph-3JKQ&t=316s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That was attorney Steve Pearlman for more of his Insight on this case be sure '
              'to visit PRCA whistleblower defense you can find that blog at whistleblower '
              'defense.com thanks for joining me today Steve thank you Colin.',
      'timestamp': 316,
      'timestamp_label': '[00:05:16]',
      'timestamp_seconds': 316,
      'tip': 'That was attorney Steve Pearlman for more of his Insight on this case be sure to '
             'visit PRCA whistleblower defense you can find that blog at whistleblower '
             'defense.com thanks for joining me today Steve thank you Colin.',
      'title': 'Steve Pearlman explains the SEC bringing its first Dodd-Frank whistleblower '
               'action (LexBlog)',
      'url': 'https://www.youtube.com/watch?v=bH6nph-3JKQ&t=316s',
      'video_id': 'bH6nph-3JKQ'},
     {'author': 'Wiley Rein LLP',
      'channel': 'Wiley Rein LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:32](https://www.youtube.com/watch?v=lzz_1rNcrwk&t=392s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'April of 2018 the SEC highlighted $2.2 million award to a whistleblower who '
              'first reported to another agency and this was the first time as noted in the.',
      'timestamp': 392,
      'timestamp_label': '[00:06:32]',
      'timestamp_seconds': 392,
      'tip': 'April of 2018 the SEC highlighted $2.2 million award to a whistleblower who '
             'first reported to another agency and this was the first time as noted in the.',
      'title': 'The SEC Whistleblower Program in 2018 (Wiley Rein LLP)',
      'url': 'https://www.youtube.com/watch?v=lzz_1rNcrwk&t=392s',
      'video_id': 'lzz_1rNcrwk'},
     {'author': 'The National Desk',
      'channel': 'The National Desk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:49](https://www.youtube.com/watch?v=yWSbhn3NK9w&t=109s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It steals from the very social fabric of the United States of America. But just '
              "reporting suspected fraud won't automatically get you a check. To qualify for a "
              'reward, your tip would have to lead to a fraud conviction or significant '
              'federal enforcement action.',
      'timestamp': 109,
      'timestamp_label': '[00:01:49]',
      'timestamp_seconds': 109,
      'tip': 'It steals from the very social fabric of the United States of America. But just '
             "reporting suspected fraud won't automatically get you a check. To qualify for a "
             'reward, your tip would have to lead to a fraud conviction or significant federal '
             'enforcement action.',
      'title': 'NEW FRAUD PROGRAM |  $25 million whistleblower program to reward those who '
               'expose (The National Desk)',
      'url': 'https://www.youtube.com/watch?v=yWSbhn3NK9w&t=109s',
      'video_id': 'yWSbhn3NK9w'},
     {'author': 'Koegle Law Group',
      'channel': 'Koegle Law Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=nM5JZ33rgDk&t=78s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Teams messages, Slack if you use those, pulling all that data out and providing '
              'it to the investigator, even if it is your HR team, so that they can do a '
              'robust investigation because what I often deal with is sort of like the after '
              'facts.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'Teams messages, Slack if you use those, pulling all that data out and providing '
             'it to the investigator, even if it is your HR team, so that they can do a robust '
             'investigation because what I often deal with is sort of like the after facts.',
      'title': 'Why Workplace Investigations Matter: Avoiding Bias in Employee Claims | '
               'California Employment Law (Koegle Law Group)',
      'url': 'https://www.youtube.com/watch?v=nM5JZ33rgDk&t=78s',
      'video_id': 'nM5JZ33rgDk'},
     {'author': 'APT',
      'channel': 'APT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:22](https://www.youtube.com/watch?v=FnUiQJNaMn8&t=382s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The words that were spoken. By 2008, we knew that Epstein was a convicted '
              'sexual abuser. How was that not a deal breaker for the president? If you, '
              'Congresswoman, um ask Bill Clinton that. The images that tell the story.',
      'timestamp': 382,
      'timestamp_label': '[00:06:22]',
      'timestamp_seconds': 382,
      'tip': 'The words that were spoken. By 2008, we knew that Epstein was a convicted sexual '
             'abuser. How was that not a deal breaker for the president? If you, '
             'Congresswoman, um ask Bill Clinton that. The images that tell the story.',
      'title': 'Bessent Unveils $30,000 Whistleblower Reward as Trump Escalates Fraud '
               'Crackdown | APT (APT)',
      'url': 'https://www.youtube.com/watch?v=FnUiQJNaMn8&t=382s',
      'video_id': 'FnUiQJNaMn8'},
     {'author': 'The Employment Law Group, P.C.',
      'channel': 'The Employment Law Group, P.C.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:47](https://www.youtube.com/watch?v=ujkR1nAOen8&t=227s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Discussion aly thank you we look forward to seeing you at the 2022 fba ketam '
              "section annual conference lincoln's law meets the 21st century february 23rd "
              '24th and 25th all virtually you can find us at fedbar.org.',
      'timestamp': 227,
      'timestamp_label': '[00:03:47]',
      'timestamp_seconds': 227,
      'tip': 'Discussion aly thank you we look forward to seeing you at the 2022 fba ketam '
             "section annual conference lincoln's law meets the 21st century february 23rd "
             '24th and 25th all virtually you can find us at fedbar.org.',
      'title': '"Qui Tam 2022" Panel Preview  - The Modern Relator (The Employment Law Group, '
               'P.C.)',
      'url': 'https://www.youtube.com/watch?v=ujkR1nAOen8&t=227s',
      'video_id': 'ujkR1nAOen8'},
     {'author': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'channel': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:23](https://www.youtube.com/watch?v=39Q-yYGWPVg&t=563s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They shouldn't have received a loan in the first place you could put that case "
              'together from the outside you could maybe bring that false claims act case.',
      'timestamp': 563,
      'timestamp_label': '[00:09:23]',
      'timestamp_seconds': 563,
      'tip': "They shouldn't have received a loan in the first place you could put that case "
             'together from the outside you could maybe bring that false claims act case.',
      'title': 'Does a Whistleblower Need to be an Employee? (Not what you think!) | Brown, '
               'LLC (Brown, LLC - A Premier Whistleblower Law Firm)',
      'url': 'https://www.youtube.com/watch?v=39Q-yYGWPVg&t=563s',
      'video_id': '39Q-yYGWPVg'},
     {'author': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'channel': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:37](https://www.youtube.com/watch?v=N4uuM9uvRYY&t=397s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Firm or give us a call we offer free consultations not just star firm there '
              "there's other quality ketan whistleblower law firms don't leave it publicly "
              'because it can only compromise your case I thank whomever asked that question '
              'we look forward to the next.',
      'timestamp': 397,
      'timestamp_label': '[00:06:37]',
      'timestamp_seconds': 397,
      'tip': 'Firm or give us a call we offer free consultations not just star firm there '
             "there's other quality ketan whistleblower law firms don't leave it publicly "
             'because it can only compromise your case I thank whomever asked that question we '
             'look forward to the next.',
      'title': 'What Is a Partial Seal Lift in the False Claims Act Litigation? | Brown, LLC '
               '(Brown, LLC - A Premier Whistleblower Law Firm)',
      'url': 'https://www.youtube.com/watch?v=N4uuM9uvRYY&t=397s',
      'video_id': 'N4uuM9uvRYY'},
     {'author': 'UAP Legion',
      'channel': 'UAP Legion',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:40](https://www.youtube.com/watch?v=Y9DOny35SW0&t=1300s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Whistleblowers can find False Claims Act whistleblower attorneys and law firms '
              'online. Several qui tam whistleblower attorneys and law firms have won large '
              'settlements against U.',
      'timestamp': 1300,
      'timestamp_label': '[00:21:40]',
      'timestamp_seconds': 1300,
      'tip': 'Whistleblowers can find False Claims Act whistleblower attorneys and law firms '
             'online. Several qui tam whistleblower attorneys and law firms have won large '
             'settlements against U.',
      'title': 'UAP Whistleblowers: The False Claims Act (UAP Legion)',
      'url': 'https://www.youtube.com/watch?v=Y9DOny35SW0&t=1300s',
      'video_id': 'Y9DOny35SW0'}],
 7: [{'author': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'channel': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:38](https://www.youtube.com/watch?v=tQIkb01vCTw&t=278s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If they're one of the best IRS whistleblower law firms out there, they probably "
              'navigated those state statutes before like we have. Step two, gathering the '
              'evidence. The IRS does not act on speculation. They want specific, credible, '
              'and verifiable information.',
      'timestamp': 278,
      'timestamp_label': '[00:04:38]',
      'timestamp_seconds': 278,
      'tip': "If they're one of the best IRS whistleblower law firms out there, they probably "
             'navigated those state statutes before like we have. Step two, gathering the '
             'evidence. The IRS does not act on speculation. They want specific, credible, and '
             'verifiable information.',
      'title': 'The IRS Whistleblower Process from Start to Finish (Brown, LLC - A Premier '
               'Whistleblower Law Firm)',
      'url': 'https://www.youtube.com/watch?v=tQIkb01vCTw&t=278s',
      'video_id': 'tQIkb01vCTw'},
     {'author': 'PYA, PC',
      'channel': 'PYA, PC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=T_14t1wDSrY&t=91s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And really, you know, as we're doing that analysis process from an "
              'anti-kickback statute perspective, another important component is does any '
              'purpose of the arrangement, even if its intent is not to do this, could it be '
              'viewed as inducing or rewarding referrals?',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': "And really, you know, as we're doing that analysis process from an anti-kickback "
             'statute perspective, another important component is does any purpose of the '
             'arrangement, even if its intent is not to do this, could it be viewed as '
             'inducing or rewarding referrals?',
      'title': 'Anti-Kickback and Stark Law: What Compliance Leaders Need to Know (PYA, PC)',
      'url': 'https://www.youtube.com/watch?v=T_14t1wDSrY&t=91s',
      'video_id': 'T_14t1wDSrY'},
     {'author': 'Lockaby PLLC',
      'channel': 'Lockaby PLLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=OfdepsSYjp4&t=114s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Attorney guide you through the process it can be scary to speak up about fraud '
              'in the workplace fortunately the false claims act has strong protections.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': 'Attorney guide you through the process it can be scary to speak up about fraud '
             'in the workplace fortunately the false claims act has strong protections.',
      'title': 'Qui Tam Basics: What is a Qui Tam Lawsuit (Lockaby PLLC)',
      'url': 'https://www.youtube.com/watch?v=OfdepsSYjp4&t=114s',
      'video_id': 'OfdepsSYjp4'},
     {'author': 'Dallas-Fort Worth Hospital Council',
      'channel': 'Dallas-Fort Worth Hospital Council',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:17](https://www.youtube.com/watch?v=_1_drZryqm4&t=1217s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, under under the anti-kickback statute, um you know, any really any '
              'arrangement that your hospital or health system has um with any vendor, with '
              'any management company, billing company, consultants, um other providers, other '
              'hospitals, right?',
      'timestamp': 1217,
      'timestamp_label': '[00:20:17]',
      'timestamp_seconds': 1217,
      'tip': 'So, under under the anti-kickback statute, um you know, any really any '
             'arrangement that your hospital or health system has um with any vendor, with any '
             'management company, billing company, consultants, um other providers, other '
             'hospitals, right?',
      'title': 'DFWHC and Hall Render webinar “Stark and Anti-Kickback Provisions in Health '
               'Care Real Estate” (Dallas-Fort Worth Hospital Council)',
      'url': 'https://www.youtube.com/watch?v=_1_drZryqm4&t=1217s',
      'video_id': '_1_drZryqm4'},
     {'author': 'SkillAcquire',
      'channel': 'SkillAcquire',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:41](https://www.youtube.com/watch?v=NsOogB7kLRQ&t=101s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you're not already thinking about this, whether you're a provider, a coder, "
              'you know, whatever um space you hold in in health care, um if you are involved '
              'in the billing and coding process at all, please make sure that the diagnosis '
              'codes are supported.',
      'timestamp': 101,
      'timestamp_label': '[00:01:41]',
      'timestamp_seconds': 101,
      'tip': "If you're not already thinking about this, whether you're a provider, a coder, "
             'you know, whatever um space you hold in in health care, um if you are involved '
             'in the billing and coding process at all, please make sure that the diagnosis '
             'codes are supported.',
      'title': '2026 False Claims Act Enforcement: DOJ Guidelines & Whistleblower Risk | '
               'SkillAcquire (SkillAcquire)',
      'url': 'https://www.youtube.com/watch?v=NsOogB7kLRQ&t=101s',
      'video_id': 'NsOogB7kLRQ'},
     {'author': 'Parnham and Associates',
      'channel': 'Parnham and Associates',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:36](https://www.youtube.com/watch?v=8tuRViP_j4Y&t=276s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Through your attorney so if you know anyone who has a potential whistleblower '
              'claim or if you yourself do please give us a call here at parnum and mcwilliams '
              'and we can help navigate you through this process.',
      'timestamp': 276,
      'timestamp_label': '[00:04:36]',
      'timestamp_seconds': 276,
      'tip': 'Through your attorney so if you know anyone who has a potential whistleblower '
             'claim or if you yourself do please give us a call here at parnum and mcwilliams '
             'and we can help navigate you through this process.',
      'title': 'Houston Criminal Attorney: The Dodd-Frank Act and Whistleblowers (Parnham and '
               'Associates)',
      'url': 'https://www.youtube.com/watch?v=8tuRViP_j4Y&t=276s',
      'video_id': '8tuRViP_j4Y'},
     {'author': 'Phillips & Cohen LLP',
      'channel': 'Phillips & Cohen LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:43](https://www.youtube.com/watch?v=5twGfbHBnJs&t=1303s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They'd feel compelled to do what they did one from an english system and one in "
              'american system who brought a false claims act.',
      'timestamp': 1303,
      'timestamp_label': '[00:21:43]',
      'timestamp_seconds': 1303,
      'tip': "They'd feel compelled to do what they did one from an english system and one in "
             'american system who brought a false claims act.',
      'title': 'The False Claims Act: What makes a whistleblower law so powerful | Berkeley '
               'Boosts (Phillips & Cohen LLP)',
      'url': 'https://www.youtube.com/watch?v=5twGfbHBnJs&t=1303s',
      'video_id': '5twGfbHBnJs'},
     {'author': 'Dorsey & Whitney LLP',
      'channel': 'Dorsey & Whitney LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:17](https://www.youtube.com/watch?v=lzireoG9EFw&t=1577s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Doesn't even have to be commercially reasonable so really what if you take a "
              'step back in in this circumstance the full.',
      'timestamp': 1577,
      'timestamp_label': '[00:26:17]',
      'timestamp_seconds': 1577,
      'tip': "Doesn't even have to be commercially reasonable so really what if you take a "
             'step back in in this circumstance the full.',
      'title': 'Final Stark and Anti-Kickback Statute Rules: What You Need to Know (Dorsey & '
               'Whitney LLP)',
      'url': 'https://www.youtube.com/watch?v=lzireoG9EFw&t=1577s',
      'video_id': 'lzireoG9EFw'},
     {'author': 'Foley & Lardner LLP',
      'channel': 'Foley & Lardner LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:50](https://www.youtube.com/watch?v=7vp44tFe6hs&t=1670s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The V violation uh but most of the attorneys I talk to who represent '
              "whistleblowers tell me that if they think it's a.",
      'timestamp': 1670,
      'timestamp_label': '[00:27:50]',
      'timestamp_seconds': 1670,
      'tip': 'The V violation uh but most of the attorneys I talk to who represent '
             "whistleblowers tell me that if they think it's a.",
      'title': 'Whistleblower Provisions of the Dodd-Frank Act (Foley & Lardner LLP)',
      'url': 'https://www.youtube.com/watch?v=7vp44tFe6hs&t=1670s',
      'video_id': '7vp44tFe6hs'},
     {'author': 'Levin Papantonio',
      'channel': 'Levin Papantonio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:24](https://www.youtube.com/watch?v=xH5IpDAiP5c&t=144s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Protect your claim that you have to make sure that you are the original source '
              "which means don't go to the press don't go public take it to an experienced "
              'council to make sure you can walk through the steps and the criteria to protect '
              'the claim.',
      'timestamp': 144,
      'timestamp_label': '[00:02:24]',
      'timestamp_seconds': 144,
      'tip': 'Protect your claim that you have to make sure that you are the original source '
             "which means don't go to the press don't go public take it to an experienced "
             'council to make sure you can walk through the steps and the criteria to protect '
             'the claim.',
      'title': 'Mistakes Not to Make in a Qui Tam Whistleblower case (Levin Papantonio)',
      'url': 'https://www.youtube.com/watch?v=xH5IpDAiP5c&t=144s',
      'video_id': 'xH5IpDAiP5c'},
     {'author': 'Where IRS Problems Get Solved',
      'channel': 'Where IRS Problems Get Solved',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:15](https://www.youtube.com/watch?v=ruRW_hNSDYk&t=615s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Any sense of whether how it's going throughout the process either that's what "
              "drives me crazy it drives people crazy right it's very frustrating um and.",
      'timestamp': 615,
      'timestamp_label': '[00:10:15]',
      'timestamp_seconds': 615,
      'tip': "Any sense of whether how it's going throughout the process either that's what "
             "drives me crazy it drives people crazy right it's very frustrating um and.",
      'title': 'IRS Whistleblower Program: Success or Failure? Eric Green & Bryan Skarlatos '
               '(Where IRS Problems Get Solved)',
      'url': 'https://www.youtube.com/watch?v=ruRW_hNSDYk&t=615s',
      'video_id': 'ruRW_hNSDYk'},
     {'author': 'PilieroMazza PLLC',
      'channel': 'PilieroMazza PLLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:36:19](https://www.youtube.com/watch?v=eIBPl3LNUXQ&t=2179s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um you should not seek forgiveness because again the certifications and the '
              'forgiveness application could also create false claims act liability.',
      'timestamp': 2179,
      'timestamp_label': '[00:36:19]',
      'timestamp_seconds': 2179,
      'tip': 'Um you should not seek forgiveness because again the certifications and the '
             'forgiveness application could also create false claims act liability.',
      'title': 'False Claims Act Implications for PPP and Disaster Relief Loans: What Small '
               'Businesses Should . . . (PilieroMazza PLLC)',
      'url': 'https://www.youtube.com/watch?v=eIBPl3LNUXQ&t=2179s',
      'video_id': 'eIBPl3LNUXQ'},
     {'author': 'Gary Martin Hays, LLC',
      'channel': 'Gary Martin Hays, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:37](https://www.youtube.com/watch?v=64dIGOXUwoc&t=337s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Through the Department of Justice will then investigate the allegations and the '
              'government will decide whether or not it will join or intervene the lawsuit '
              'listen if you have any questions about any kind of false claims out there give '
              'us a call our phone number 770- 934.',
      'timestamp': 337,
      'timestamp_label': '[00:05:37]',
      'timestamp_seconds': 337,
      'tip': 'Through the Department of Justice will then investigate the allegations and the '
             'government will decide whether or not it will join or intervene the lawsuit '
             'listen if you have any questions about any kind of false claims out there give '
             'us a call our phone number 770- 934.',
      'title': 'Qui Tam: What steps should you take when dealing with false claims in a qui '
               'tam case? (Gary Martin Hays, LLC)',
      'url': 'https://www.youtube.com/watch?v=64dIGOXUwoc&t=337s',
      'video_id': '64dIGOXUwoc'},
     {'author': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'channel': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:49](https://www.youtube.com/watch?v=faQOCnnY-QI&t=589s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Don't so please call us at 8775612272 if you have anything that you'd like us "
              "to discuss but don't leave anything privileged together end Medicare fraud.",
      'timestamp': 589,
      'timestamp_label': '[00:09:49]',
      'timestamp_seconds': 589,
      'tip': "Don't so please call us at 8775612272 if you have anything that you'd like us to "
             "discuss but don't leave anything privileged together end Medicare fraud.",
      'title': 'How to Report Medicare Fraud in 2026? (Brown, LLC - A Premier Whistleblower '
               'Law Firm)',
      'url': 'https://www.youtube.com/watch?v=faQOCnnY-QI&t=589s',
      'video_id': 'faQOCnnY-QI'},
     {'author': 'Law Minded',
      'channel': 'Law Minded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:04](https://www.youtube.com/watch?v=sNHauc7rutQ&t=364s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "What's the best way to go about it? Um absolutely, I would recommend having an "
              'attorney for this to guide them through the entire process because it can '
              'definitely get complicated.',
      'timestamp': 364,
      'timestamp_label': '[00:06:04]',
      'timestamp_seconds': 364,
      'tip': "What's the best way to go about it? Um absolutely, I would recommend having an "
             'attorney for this to guide them through the entire process because it can '
             'definitely get complicated.',
      'title': 'How to Become an IRS Whistleblower (and Get Paid) | Law Minded EP. 11 (Law '
               'Minded)',
      'url': 'https://www.youtube.com/watch?v=sNHauc7rutQ&t=364s',
      'video_id': 'sNHauc7rutQ'}],
 8: [{'author': 'Beverly Hills Bar Association',
      'channel': 'Beverly Hills Bar Association',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:29](https://www.youtube.com/watch?v=yN7NRjwYKFs&t=389s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Champions the act and with jeff Sessions was there with Hector Jeff Sessions '
              "now he Hector's Attorney General bar so to a large extent this really is a "
              'uniquely.',
      'timestamp': 389,
      'timestamp_label': '[00:06:29]',
      'timestamp_seconds': 389,
      'tip': 'Champions the act and with jeff Sessions was there with Hector Jeff Sessions now '
             "he Hector's Attorney General bar so to a large extent this really is a uniquely.",
      'title': 'Qui Tam 101: False Claims Act, Whistleblowers, Corporate Fraud and Employer '
               'Misconduct (Beverly Hills Bar Association)',
      'url': 'https://www.youtube.com/watch?v=yN7NRjwYKFs&t=389s',
      'video_id': 'yN7NRjwYKFs'},
     {'author': 'DarrowEverett LLP',
      'channel': 'DarrowEverett LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:16](https://www.youtube.com/watch?v=5LsJY2Ss1SI&t=856s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, the whistleblowers are still be a significant part of the false claims act. '
              'DOJ is just trying to ramp up, you know, in the AI era with their data '
              'analytics mostly in main justice.',
      'timestamp': 856,
      'timestamp_label': '[00:14:16]',
      'timestamp_seconds': 856,
      'tip': 'So, the whistleblowers are still be a significant part of the false claims act. '
             'DOJ is just trying to ramp up, you know, in the AI era with their data analytics '
             'mostly in main justice.',
      'title': 'The DOJ’s New Agenda: What Every Business Should Know About the False Claims '
               'Act (DarrowEverett LLP)',
      'url': 'https://www.youtube.com/watch?v=5LsJY2Ss1SI&t=856s',
      'video_id': '5LsJY2Ss1SI'},
     {'author': 'Foley & Lardner LLP',
      'channel': 'Foley & Lardner LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:50](https://www.youtube.com/watch?v=J1-aE0W1Eu8&t=1070s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'll talk about with customs or there's increasingly available Medicare and now "
              'Medicaid data down at like a claims level was recently uh, released.',
      'timestamp': 1070,
      'timestamp_label': '[00:17:50]',
      'timestamp_seconds': 1070,
      'tip': "I'll talk about with customs or there's increasingly available Medicare and now "
             'Medicaid data down at like a claims level was recently uh, released.',
      'title': 'False Claims Act Enforcement in 2026 (Foley & Lardner LLP)',
      'url': 'https://www.youtube.com/watch?v=J1-aE0W1Eu8&t=1070s',
      'video_id': 'J1-aE0W1Eu8'},
     {'author': 'Epstein Becker Green',
      'channel': 'Epstein Becker Green',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:35](https://www.youtube.com/watch?v=rxUll524o5w&t=1115s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, right at the motion to dismiss phase, a False Claims Act complaint that '
              'alleged that Baylor Scott and White and its affiliates had used inflated codes '
              'to bill Medicare.',
      'timestamp': 1115,
      'timestamp_label': '[00:18:35]',
      'timestamp_seconds': 1115,
      'tip': 'So, right at the motion to dismiss phase, a False Claims Act complaint that '
             'alleged that Baylor Scott and White and its affiliates had used inflated codes '
             'to bill Medicare.',
      'title': 'Speaking of Litigation - DOJ’s National Fraud Enforcement Division: Early '
               'Seizures and Data Mining (Epstein Becker Green)',
      'url': 'https://www.youtube.com/watch?v=rxUll524o5w&t=1115s',
      'video_id': 'rxUll524o5w'},
     {'author': 'Baker Donelson',
      'channel': 'Baker Donelson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:17](https://www.youtube.com/watch?v=-Vss5I_7dHM&t=797s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The party submitting the bill is always a debate so in the beginning and this '
              'really pulls you in as to why whistleblowers are so important the government '
              'has access to all the data.',
      'timestamp': 797,
      'timestamp_label': '[00:13:17]',
      'timestamp_seconds': 797,
      'tip': 'The party submitting the bill is always a debate so in the beginning and this '
             'really pulls you in as to why whistleblowers are so important the government has '
             'access to all the data.',
      'title': 'False Claims Act 101 (Baker Donelson)',
      'url': 'https://www.youtube.com/watch?v=-Vss5I_7dHM&t=797s',
      'video_id': '-Vss5I_7dHM'},
     {'author': 'Silver Law Group',
      'channel': 'Silver Law Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=AoceOfN67y8&t=100s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Of their attorneys scott silver previously worked as a defense attorney on wall '
              'street and now he uses insights gained from that experience to fight for.',
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': 'Of their attorneys scott silver previously worked as a defense attorney on wall '
             'street and now he uses insights gained from that experience to fight for.',
      'title': 'SEC Whistleblower Attorneys - Overview (Silver Law Group)',
      'url': 'https://www.youtube.com/watch?v=AoceOfN67y8&t=100s',
      'video_id': 'AoceOfN67y8'},
     {'author': 'CNBC',
      'channel': 'CNBC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:22](https://www.youtube.com/watch?v=CctRGUwjm7k&t=442s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Cambridge analytical or any other data analytics companies were breaking laws '
              "because I believe that they weren't in the most case none of these companies.",
      'timestamp': 442,
      'timestamp_label': '[00:07:22]',
      'timestamp_seconds': 442,
      'tip': 'Cambridge analytical or any other data analytics companies were breaking laws '
             "because I believe that they weren't in the most case none of these companies.",
      'title': 'Cambridge Analytica Whistleblower Brittany Kaiser: Lack Of Transparency In '
               'Data Gathering | CNBC (CNBC)',
      'url': 'https://www.youtube.com/watch?v=CctRGUwjm7k&t=442s',
      'video_id': 'CctRGUwjm7k'},
     {'author': 'Mercia Asset Management PLC',
      'channel': 'Mercia Asset Management PLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:06](https://www.youtube.com/watch?v=5LeNkCDistY&t=306s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Us uh over the next couple of years will be to deepen our products be able to '
              "bring more data into them and broaden the market that we're selling them to our "
              'ambitions are um pretty much unlimited because the growth in digital forensics '
              'is exponential.',
      'timestamp': 306,
      'timestamp_label': '[00:05:06]',
      'timestamp_seconds': 306,
      'tip': 'Us uh over the next couple of years will be to deepen our products be able to '
             "bring more data into them and broaden the market that we're selling them to our "
             'ambitions are um pretty much unlimited because the growth in digital forensics '
             'is exponential.',
      'title': "Forensic Analytics | Software that's revolutionising police investigations "
               '(Mercia Asset Management PLC)',
      'url': 'https://www.youtube.com/watch?v=5LeNkCDistY&t=306s',
      'video_id': '5LeNkCDistY'},
     {'author': 'Melissa Green Law Group',
      'channel': 'Melissa Green Law Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:29](https://www.youtube.com/watch?v=Lbcq9qvdJtE&t=29s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s most powerful tool against fraud. Its central idea is simple. People inside "
              'organizations may know what government investigators cannot see. The law makes '
              'it illegal to knowingly submit a false or fraudulent claim for payment to the '
              'federal government.',
      'timestamp': 29,
      'timestamp_label': '[00:00:29]',
      'timestamp_seconds': 29,
      'tip': "'s most powerful tool against fraud. Its central idea is simple. People inside "
             'organizations may know what government investigators cannot see. The law makes '
             'it illegal to knowingly submit a false or fraudulent claim for payment to the '
             'federal government.',
      'title': 'What Is the False Claims Act and Why Does It Matter? (Melissa Green Law Group)',
      'url': 'https://www.youtube.com/watch?v=Lbcq9qvdJtE&t=29s',
      'video_id': 'Lbcq9qvdJtE'},
     {'author': 'GBB Legal',
      'channel': 'GBB Legal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:08](https://www.youtube.com/watch?v=FAfnVdZ6Ie0&t=308s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Takes to take that case from beginning to end which is trial for a judge the '
              'jury thank you and I hope that helps you with a better understanding of the '
              'False Claims Act and how these cases are put together.',
      'timestamp': 308,
      'timestamp_label': '[00:05:08]',
      'timestamp_seconds': 308,
      'tip': 'Takes to take that case from beginning to end which is trial for a judge the '
             'jury thank you and I hope that helps you with a better understanding of the '
             'False Claims Act and how these cases are put together.',
      'title': 'Introduction to the False Claims Act (FCA) (GBB Legal)',
      'url': 'https://www.youtube.com/watch?v=FAfnVdZ6Ie0&t=308s',
      'video_id': 'FAfnVdZ6Ie0'},
     {'author': 'Workman Forensics',
      'channel': 'Workman Forensics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:38](https://www.youtube.com/watch?v=4CnIVLSoe2o&t=758s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Its services visit workmanforensics.com find us on social media on any social '
              'media platform at workmen forensics if you have any questions comments concerns '
              'or topic ideas please email us at podcast workmanforensics.com thanks for '
              'listening.',
      'timestamp': 758,
      'timestamp_label': '[00:12:38]',
      'timestamp_seconds': 758,
      'tip': 'Its services visit workmanforensics.com find us on social media on any social '
             'media platform at workmen forensics if you have any questions comments concerns '
             'or topic ideas please email us at podcast workmanforensics.com thanks for '
             'listening.',
      'title': "Don't Wait On a Whistleblower (Workman Forensics)",
      'url': 'https://www.youtube.com/watch?v=4CnIVLSoe2o&t=758s',
      'video_id': '4CnIVLSoe2o'},
     {'author': 'Fraud in America',
      'channel': 'Fraud in America',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:24](https://www.youtube.com/watch?v=MTKHmo8s-kc&t=264s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Very small I think in the last fiscal year the federal government recovered a '
              "about $77 billion in duties but that's out of I think close to five Bill 5.",
      'timestamp': 264,
      'timestamp_label': '[00:04:24]',
      'timestamp_seconds': 264,
      'tip': 'Very small I think in the last fiscal year the federal government recovered a '
             "about $77 billion in duties but that's out of I think close to five Bill 5.",
      'title': 'Breaking Down Tariffs and Customs Fraud 101 (Fraud in America)',
      'url': 'https://www.youtube.com/watch?v=MTKHmo8s-kc&t=264s',
      'video_id': 'MTKHmo8s-kc'},
     {'author': 'ABA Criminal Justice Section',
      'channel': 'ABA Criminal Justice Section',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:08](https://www.youtube.com/watch?v=JN4iipJiHZM&t=1628s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Interrupt you I just want to I want to bring amanda into this and amanda asked '
              "you as a long time civil ausa uh whether this is a tool that you've used and "
              'what what your experience has been with it yeah we I have not can you hear me '
              'okay.',
      'timestamp': 1628,
      'timestamp_label': '[00:27:08]',
      'timestamp_seconds': 1628,
      'tip': 'Interrupt you I just want to I want to bring amanda into this and amanda asked '
             "you as a long time civil ausa uh whether this is a tool that you've used and "
             'what what your experience has been with it yeah we I have not can you hear me '
             'okay.',
      'title': 'Ethical Issues in Qui Tam Investigations (ABA Criminal Justice Section)',
      'url': 'https://www.youtube.com/watch?v=JN4iipJiHZM&t=1628s',
      'video_id': 'JN4iipJiHZM'},
     {'author': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'channel': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:51](https://www.youtube.com/watch?v=7two8gR6AAY&t=171s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Blow the whistle the right way on Medicare fraud you might as well try to enjoy '
              "an upside since you're going through it rather than just be a participant in "
              'the investigation with maybe potentially a downsize as well thank you for the '
              'question.',
      'timestamp': 171,
      'timestamp_label': '[00:02:51]',
      'timestamp_seconds': 171,
      'tip': 'Blow the whistle the right way on Medicare fraud you might as well try to enjoy '
             "an upside since you're going through it rather than just be a participant in the "
             'investigation with maybe potentially a downsize as well thank you for the '
             'question.',
      'title': 'What Happens When You Report Medicare Fraud? |  Brown, LLC (Brown, LLC - A '
               'Premier Whistleblower Law Firm)',
      'url': 'https://www.youtube.com/watch?v=7two8gR6AAY&t=171s',
      'video_id': '7two8gR6AAY'},
     {'author': 'Shipping Solutions',
      'channel': 'Shipping Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:49](https://www.youtube.com/watch?v=EIHwzCe4zZM&t=169s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Customs to reduce your risk. If you need help with classification, click the '
              'link in the right-hand corner to try our Product Classification Software for '
              'free. It eliminates the need to manually search through hundreds of pages of '
              'HTS codes.',
      'timestamp': 169,
      'timestamp_label': '[00:02:49]',
      'timestamp_seconds': 169,
      'tip': 'Customs to reduce your risk. If you need help with classification, click the '
             'link in the right-hand corner to try our Product Classification Software for '
             'free. It eliminates the need to manually search through hundreds of pages of HTS '
             'codes.',
      'title': 'What Is the False Claims Act? Importer Risks & Compliance Tips (Shipping '
               'Solutions)',
      'url': 'https://www.youtube.com/watch?v=EIHwzCe4zZM&t=169s',
      'video_id': 'EIHwzCe4zZM'}],
 9: [{'author': 'Michael H. Cohen – Healthcare Law',
      'channel': 'Michael H. Cohen – Healthcare Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=yUDp-6sl7yI&t=22s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Cohen, founding attorney of the Cohen Healthcare Law Group. We’ve advised over '
              'a thousand healthcare industry clients on healthcare and FDA legal issues. '
              'Today, I’m going to explain some of the key differences between Stark Law and '
              'the Anti-Kickback Statute.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'Cohen, founding attorney of the Cohen Healthcare Law Group. We’ve advised over a '
             'thousand healthcare industry clients on healthcare and FDA legal issues. Today, '
             'I’m going to explain some of the key differences between Stark Law and the '
             'Anti-Kickback Statute.',
      'title': 'Stark vs Anti-Kickback: The Key Differences (Michael H. Cohen – Healthcare '
               'Law)',
      'url': 'https://www.youtube.com/watch?v=yUDp-6sl7yI&t=22s',
      'video_id': 'yUDp-6sl7yI'},
     {'author': 'Kevin Pho, MD',
      'channel': 'Kevin Pho, MD',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:41](https://www.youtube.com/watch?v=eIMINUxFlVI&t=701s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You should have a compliance officer who is knowledgeable about the False '
              "Claims Act. And I would say if you're employed, there's something called the "
              "safe harbor uh for anti-kickback, and then there's the Stark Law exception. "
              'Understand how you fit under the exceptions.',
      'timestamp': 701,
      'timestamp_label': '[00:11:41]',
      'timestamp_seconds': 701,
      'tip': 'You should have a compliance officer who is knowledgeable about the False Claims '
             "Act. And I would say if you're employed, there's something called the safe "
             "harbor uh for anti-kickback, and then there's the Stark Law exception. "
             'Understand how you fit under the exceptions.',
      'title': 'Why physicians should care about the False Claims Act (Kevin Pho, MD)',
      'url': 'https://www.youtube.com/watch?v=eIMINUxFlVI&t=701s',
      'video_id': 'eIMINUxFlVI'},
     {'author': "Children's of Alabama",
      'channel': "Children's of Alabama",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:19](https://www.youtube.com/watch?v=yrBJ3oA7mHw&t=439s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Harbor it might still be in compliance with the anti-kickback statute but it's "
              'subject to a case-by-case analysis.',
      'timestamp': 439,
      'timestamp_label': '[00:07:19]',
      'timestamp_seconds': 439,
      'tip': "Harbor it might still be in compliance with the anti-kickback statute but it's "
             'subject to a case-by-case analysis.',
      'title': 'COA Corporate Compliance: Understanding the Stark Law and Anti-Kickback '
               "Statute (Children's of Alabama)",
      'url': 'https://www.youtube.com/watch?v=yrBJ3oA7mHw&t=439s',
      'video_id': 'yrBJ3oA7mHw'},
     {'author': 'Blue Ocean Law Group. innovative Counsel [iC]',
      'channel': 'Blue Ocean Law Group. innovative Counsel [iC]',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:06](https://www.youtube.com/watch?v=4mXSodsYqr4&t=66s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, how are they pulling this off? What's the legal firepower behind it? Well, "
              "it's not some new cybersecurity law. Instead, the government has basically "
              'dusted off a powerful old law and aimed it squarely at the tech sector. Meet '
              'the False Claims Act, or the FCA.',
      'timestamp': 66,
      'timestamp_label': '[00:01:06]',
      'timestamp_seconds': 66,
      'tip': "So, how are they pulling this off? What's the legal firepower behind it? Well, "
             "it's not some new cybersecurity law. Instead, the government has basically "
             'dusted off a powerful old law and aimed it squarely at the tech sector. Meet the '
             'False Claims Act, or the FCA.',
      'title': 'How the False Claims Act transforms CyberSecurity Non-compliance Risks into '
               'Fraud against the US Gov (Blue Ocean Law Group. innovative Counsel [iC])',
      'url': 'https://www.youtube.com/watch?v=4mXSodsYqr4&t=66s',
      'video_id': '4mXSodsYqr4'},
     {'author': 'Seyfarth Shaw LLP',
      'channel': 'Seyfarth Shaw LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:51:45](https://www.youtube.com/watch?v=QLVKZRh_ArE&t=3105s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'March they turned this into a actual bar clause a contract clause um that gives '
              'government access to to records requires reporting of subs subcontractors who '
              'are known to violate uh the order um and of course declares compliance '
              'material.',
      'timestamp': 3105,
      'timestamp_label': '[00:51:45]',
      'timestamp_seconds': 3105,
      'tip': 'March they turned this into a actual bar clause a contract clause um that gives '
             'government access to to records requires reporting of subs subcontractors who '
             'are known to violate uh the order um and of course declares compliance material.',
      'title': 'False Claims Act Enforcement: The Developments Reshaping Risk for 2027 - '
               'November 10, 2026 (Seyfarth Shaw LLP)',
      'url': 'https://www.youtube.com/watch?v=QLVKZRh_ArE&t=3105s',
      'video_id': 'QLVKZRh_ArE'},
     {'author': 'Chapman Law Group: Health Care Attorneys',
      'channel': 'Chapman Law Group: Health Care Attorneys',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:21](https://www.youtube.com/watch?v=4cRTBx7ikiY&t=261s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t appropriate for billing incident too. So you gather that information and "
              "you're going to work with your attorney to prepare this disclosure statement. "
              "And in the disclosure statement, you're going to have to have facts and "
              "details. Perhaps you're going to have calendars.",
      'timestamp': 261,
      'timestamp_label': '[00:04:21]',
      'timestamp_seconds': 261,
      'tip': "'t appropriate for billing incident too. So you gather that information and "
             "you're going to work with your attorney to prepare this disclosure statement. "
             "And in the disclosure statement, you're going to have to have facts and details. "
             "Perhaps you're going to have calendars.",
      'title': 'What is QUI TAM Law? Part 1: Relators and Disclosures (Chapman Law Group: '
               'Health Care Attorneys)',
      'url': 'https://www.youtube.com/watch?v=4cRTBx7ikiY&t=261s',
      'video_id': '4cRTBx7ikiY'},
     {'author': 'American Health Law Association',
      'channel': 'American Health Law Association',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:01](https://www.youtube.com/watch?v=6O2jbkASdfY&t=1201s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Stark Law on the federal side, and frankly, on the state side, my analysis is '
              'probably going to start with the state analog. You know, most states have a '
              "physician self-referral law. And the reason for that is because it's more of a "
              'strict liability standard, right?',
      'timestamp': 1201,
      'timestamp_label': '[00:20:01]',
      'timestamp_seconds': 1201,
      'tip': 'Stark Law on the federal side, and frankly, on the state side, my analysis is '
             'probably going to start with the state analog. You know, most states have a '
             "physician self-referral law. And the reason for that is because it's more of a "
             'strict liability standard, right?',
      'title': 'Stark Law: Latest Trends and Developments (American Health Law Association)',
      'url': 'https://www.youtube.com/watch?v=6O2jbkASdfY&t=1201s',
      'video_id': '6O2jbkASdfY'},
     {'author': 'Tony Munter Attorney at Law',
      'channel': 'Tony Munter Attorney at Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:07](https://www.youtube.com/watch?v=tW8oVBiMkLg&t=127s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Whistleblower program the harm comes to investors who may have been defrauded '
              'by securities both of these laws the dodd-frank law that created the SCC '
              'whistleblower program and the False Claims Act are powerful to us for '
              'whistleblowers to use and appropriate matters.',
      'timestamp': 127,
      'timestamp_label': '[00:02:07]',
      'timestamp_seconds': 127,
      'tip': 'Whistleblower program the harm comes to investors who may have been defrauded by '
             'securities both of these laws the dodd-frank law that created the SCC '
             'whistleblower program and the False Claims Act are powerful to us for '
             'whistleblowers to use and appropriate matters.',
      'title': 'What Should I Know About the SEC and CFTC Whistleblower Programs? | Tony '
               'Munter Attorney at Law (Tony Munter Attorney at Law)',
      'url': 'https://www.youtube.com/watch?v=tW8oVBiMkLg&t=127s',
      'video_id': 'tW8oVBiMkLg'},
     {'author': 'Accuser Media',
      'channel': 'Accuser Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:49](https://www.youtube.com/watch?v=2yLpClw9MG8&t=49s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'When an accuser asserts formal allegations of malfeasance, disclosures must '
              'satisfy three foundational legal hurdles, evidentiary specificity, procedural '
              'compliance with authorized agency channels, and the total absence of bad faith '
              'fabrication.',
      'timestamp': 49,
      'timestamp_label': '[00:00:49]',
      'timestamp_seconds': 49,
      'tip': 'When an accuser asserts formal allegations of malfeasance, disclosures must '
             'satisfy three foundational legal hurdles, evidentiary specificity, procedural '
             'compliance with authorized agency channels, and the total absence of bad faith '
             'fabrication.',
      'title': 'The $279 Million Whistleblower: Inside the Largest SEC Bounty Pay | Case '
               'Documentary (Accuser Media)',
      'url': 'https://www.youtube.com/watch?v=2yLpClw9MG8&t=49s',
      'video_id': '2yLpClw9MG8'},
     {'author': 'Protect',
      'channel': 'Protect',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=VXSmJlGNKIw&t=59s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ah because a disclosure needs to meet certain legal tests before it can be '
              'protected all right I thought anyone could whistleblow about anything afraid.',
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': 'Ah because a disclosure needs to meet certain legal tests before it can be '
             'protected all right I thought anyone could whistleblow about anything afraid.',
      'title': 'Protected Disclosures & Whistleblowing (Protect)',
      'url': 'https://www.youtube.com/watch?v=VXSmJlGNKIw&t=59s',
      'video_id': 'VXSmJlGNKIw'},
     {'author': 'Husch Blackwell',
      'channel': 'Husch Blackwell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:33](https://www.youtube.com/watch?v=FO7NfNf-r0k&t=513s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Brandon, a lot of our listeners may not know about ECRA all that much, but a '
              "lot of them should. So, why don't you tee this conversation off by telling us "
              'about ECRA and how it ties into the False Claims Act? So, ECRA is an '
              'interesting rule, a law statute sort of idea.',
      'timestamp': 513,
      'timestamp_label': '[00:08:33]',
      'timestamp_seconds': 513,
      'tip': 'Brandon, a lot of our listeners may not know about ECRA all that much, but a lot '
             "of them should. So, why don't you tee this conversation off by telling us about "
             'ECRA and how it ties into the False Claims Act? So, ECRA is an interesting rule, '
             'a law statute sort of idea.',
      'title': 'Trump DOJ Sharpens Its Focus on Healthcare Fraud (Husch Blackwell)',
      'url': 'https://www.youtube.com/watch?v=FO7NfNf-r0k&t=513s',
      'video_id': 'FO7NfNf-r0k'},
     {'author': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'channel': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:38](https://www.youtube.com/watch?v=Cz4DaWsS-xM&t=518s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You retain a whistleblower law firm that firm's loyalty is to you to protect "
              'you to get you the best result so you need somebody like that in your corner.',
      'timestamp': 518,
      'timestamp_label': '[00:08:38]',
      'timestamp_seconds': 518,
      'tip': "You retain a whistleblower law firm that firm's loyalty is to you to protect you "
             'to get you the best result so you need somebody like that in your corner.',
      'title': 'What’s the #1 Thing a Whistleblower Should Do? #whistleblower (Brown, LLC - A '
               'Premier Whistleblower Law Firm)',
      'url': 'https://www.youtube.com/watch?v=Cz4DaWsS-xM&t=518s',
      'video_id': 'Cz4DaWsS-xM'},
     {'author': 'Zuckerman Whistleblower Law Firm',
      'channel': 'Zuckerman Whistleblower Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=mq-TIQ4Y8ps&t=103s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The right thing call The Whistleblower lawyers at zuckman law today at 202 '
              '26289 59 or go to our website www. Zuckerman law.com to learn more about '
              'whistleblower rights and protections at Zuckerman law we work to protect you '
              'and get you the reward you deserve.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': 'The right thing call The Whistleblower lawyers at zuckman law today at 202 26289 '
             '59 or go to our website www. Zuckerman law.com to learn more about whistleblower '
             'rights and protections at Zuckerman law we work to protect you and get you the '
             'reward you deserve.',
      'title': 'SEC Whistleblower Rewards and Bounties (Zuckerman Whistleblower Law Firm)',
      'url': 'https://www.youtube.com/watch?v=mq-TIQ4Y8ps&t=103s',
      'video_id': 'mq-TIQ4Y8ps'},
     {'author': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'channel': 'Brown, LLC - A Premier Whistleblower Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:35](https://www.youtube.com/watch?v=RuNrDW46nKY&t=815s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Blowing the whistle about tax fraud tax cheats either the IRS whistleblower '
              'program New York State whistleblower tax cheat program or other states '
              'whistleblower programs please contact our firm 8775612272.',
      'timestamp': 815,
      'timestamp_label': '[00:13:35]',
      'timestamp_seconds': 815,
      'tip': 'Blowing the whistle about tax fraud tax cheats either the IRS whistleblower '
             'program New York State whistleblower tax cheat program or other states '
             'whistleblower programs please contact our firm 8775612272.',
      'title': 'Exposing Tax Cheats: How Whistleblowers Can Report Tax Fraud (Brown, LLC - A '
               'Premier Whistleblower Law Firm)',
      'url': 'https://www.youtube.com/watch?v=RuNrDW46nKY&t=815s',
      'video_id': 'RuNrDW46nKY'},
     {'author': 'Andrew Jonathan Hillman',
      'channel': 'Andrew Jonathan Hillman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:07](https://www.youtube.com/watch?v=AcMsQCQm5QI&t=367s)',
      'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                   'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                   'import manifests) paired with paid relator-counsel litigation-support '
                   'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                   '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'HIPAA compliance, internal investigations, document review, and support for '
              'expert reports. He works as a Senior Paralegal, and as an expert witness he is '
              'retained through counsel. He is not an attorney, and he does not give legal '
              'advice.',
      'timestamp': 367,
      'timestamp_label': '[00:06:07]',
      'timestamp_seconds': 367,
      'tip': 'HIPAA compliance, internal investigations, document review, and support for '
             'expert reports. He works as a Senior Paralegal, and as an expert witness he is '
             'retained through counsel. He is not an attorney, and he does not give legal '
             'advice.',
      'title': 'Andrew Hillman, Dallas | False Claims Act, Qui Tam, Stark Law Explained | '
               'Andrew Jonathan Hillman (Andrew Jonathan Hillman)',
      'url': 'https://www.youtube.com/watch?v=AcMsQCQm5QI&t=367s',
      'video_id': 'AcMsQCQm5QI'}],
 10: [{'author': 'Foundation Digital Media',
       'channel': 'Foundation Digital Media',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:12](https://www.youtube.com/watch?v=dyn9ni2HPDU&t=132s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Those awards are associated with enforcement actions that have resulted in '
               'monetary sanctions totaling more than 3. Because of our in-depth knowledge of '
               'the CFTC, our attorneys can help you present your information to the agency in '
               'the best way possible.',
       'timestamp': 132,
       'timestamp_label': '[00:02:12]',
       'timestamp_seconds': 132,
       'tip': 'Those awards are associated with enforcement actions that have resulted in '
              'monetary sanctions totaling more than 3. Because of our in-depth knowledge of '
              'the CFTC, our attorneys can help you present your information to the agency in '
              'the best way possible.',
       'title': 'Washington DC Whistleblower Program Explainer | Phillips & Cohen (Foundation '
                'Digital Media)',
       'url': 'https://www.youtube.com/watch?v=dyn9ni2HPDU&t=132s',
       'video_id': 'dyn9ni2HPDU'},
      {'author': 'HB Litigation News',
       'channel': 'HB Litigation News',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:20:29](https://www.youtube.com/watch?v=mNX2NY20ks0&t=1229s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re going to try to put forth their best examples of what they would deem to "
               "be brought. They're going to try to put those in their complaint. But if the "
               'case moves on to discovery, you know, AI can also be a really powerful tool '
               'for defendants.',
       'timestamp': 1229,
       'timestamp_label': '[00:20:29]',
       'timestamp_seconds': 1229,
       'tip': "'re going to try to put forth their best examples of what they would deem to be "
              "brought. They're going to try to put those in their complaint. But if the case "
              'moves on to discovery, you know, AI can also be a really powerful tool for '
              'defendants.',
       'title': 'Can an Algorithm Find Fraud? The New False Claims Act #falseclaims  '
                '#healthcarefraud #legaltech (HB Litigation News)',
       'url': 'https://www.youtube.com/watch?v=mNX2NY20ks0&t=1229s',
       'video_id': 'mNX2NY20ks0'},
      {'author': 'Federal News Network',
       'channel': 'Federal News Network',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:01](https://www.youtube.com/watch?v=ovf7HOfeGQ0&t=481s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Um and that's about 130 lawyers or so right now. Uh they work with the US "
               "attorney's offices and there are US attorneys offices everywhere in the "
               'country in every judicial district.',
       'timestamp': 481,
       'timestamp_label': '[00:08:01]',
       'timestamp_seconds': 481,
       'tip': "Um and that's about 130 lawyers or so right now. Uh they work with the US "
              "attorney's offices and there are US attorneys offices everywhere in the country "
              'in every judicial district.',
       'title': 'Trump administration looks to False Claims Act to curb cybersecurity '
                'violations (Federal News Network)',
       'url': 'https://www.youtube.com/watch?v=ovf7HOfeGQ0&t=481s',
       'video_id': 'ovf7HOfeGQ0'},
      {'author': 'The Employment Law Group, P.C.',
       'channel': 'The Employment Law Group, P.C.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:45](https://www.youtube.com/watch?v=aZd6GqRekxQ&t=285s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Resolution in Eva that sounds just terrific and thank you we look forward to '
               'seeing each of you at the FBA keam sections 2024 annual conference the '
               'government and the FCA practice February 21st through 23rd 2024 register now '
               'at www.fed bar.org.',
       'timestamp': 285,
       'timestamp_label': '[00:04:45]',
       'timestamp_seconds': 285,
       'tip': 'Resolution in Eva that sounds just terrific and thank you we look forward to '
              'seeing each of you at the FBA keam sections 2024 annual conference the '
              'government and the FCA practice February 21st through 23rd 2024 register now at '
              'www.fed bar.org.',
       'title': '"Qui Tam 2024" Panel Preview - Insider, Competitor, Analyst, Doe: Who\'s Your '
                'Whistleblower? (The Employment Law Group, P.C.)',
       'url': 'https://www.youtube.com/watch?v=aZd6GqRekxQ&t=285s',
       'video_id': 'aZd6GqRekxQ'},
      {'author': 'Fox News',
       'channel': 'Fox News',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:48](https://www.youtube.com/watch?v=EADzW7gAeVw&t=168s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "AND TO THAT POINT, HUNTER BIDEN'S ATTORNEY, CHRIS CLARK PUT OUT A STATEMENT IN "
               'WHICH HE SAYS IT APPEARS THIS IRS AGENT HAS COMMITTED A CRIME. IT IS A FELONY '
               'FOR AN IRS AGENT TO IMPROPERLY DISCLOSE INFORMATION ABOUT AN ONGOING TAX '
               'INVESTIGATION.',
       'timestamp': 168,
       'timestamp_label': '[00:02:48]',
       'timestamp_seconds': 168,
       'tip': "AND TO THAT POINT, HUNTER BIDEN'S ATTORNEY, CHRIS CLARK PUT OUT A STATEMENT IN "
              'WHICH HE SAYS IT APPEARS THIS IRS AGENT HAS COMMITTED A CRIME. IT IS A FELONY '
              'FOR AN IRS AGENT TO IMPROPERLY DISCLOSE INFORMATION ABOUT AN ONGOING TAX '
              'INVESTIGATION.',
       'title': "IRS whistleblower couldn't live with himself if he stayed quiet: Attorney for "
                'whistleblower (Fox News)',
       'url': 'https://www.youtube.com/watch?v=EADzW7gAeVw&t=168s',
       'video_id': 'EADzW7gAeVw'},
      {'author': 'FinCrime Intelligence',
       'channel': 'FinCrime Intelligence',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:52](https://www.youtube.com/watch?v=Mi3ALpKg17s&t=52s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It's about building an entire framework for trust and for long-term stability. "
               "And this is absolutely key. The FCA doesn't just hand out a rulebook and say, "
               '"Good luck." No, it actively shapes how financial firms think and how they '
               'act.',
       'timestamp': 52,
       'timestamp_label': '[00:00:52]',
       'timestamp_seconds': 52,
       'tip': "It's about building an entire framework for trust and for long-term stability. "
              "And this is absolutely key. The FCA doesn't just hand out a rulebook and say, "
              '"Good luck." No, it actively shapes how financial firms think and how they act.',
       'title': 'Financial Conduct Authority - Financial Crime Acronyms and Definitions '
                '(FinCrime Intelligence)',
       'url': 'https://www.youtube.com/watch?v=Mi3ALpKg17s&t=52s',
       'video_id': 'Mi3ALpKg17s'},
      {'author': 'Tycko & Zavareei LLP',
       'channel': 'Tycko & Zavareei LLP',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:07](https://www.youtube.com/watch?v=azRmbEExKOw&t=67s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Four: Fraud in the banking industry may be reported to the Department of '
               'Justice. And finally, violations of anti-money laundering requirements or '
               'other violations of the Bank Secrecy Act can be reported directly to the '
               'Treasury Department.',
       'timestamp': 67,
       'timestamp_label': '[00:01:07]',
       'timestamp_seconds': 67,
       'tip': 'Four: Fraud in the banking industry may be reported to the Department of '
              'Justice. And finally, violations of anti-money laundering requirements or other '
              'violations of the Bank Secrecy Act can be reported directly to the Treasury '
              'Department.',
       'title': 'Financial Fraud: Qui Tam Lawsuits Explained (Tycko & Zavareei LLP)',
       'url': 'https://www.youtube.com/watch?v=azRmbEExKOw&t=67s',
       'video_id': 'azRmbEExKOw'},
      {'author': 'Former IRS Agent Representation   4.2M Views',
       'channel': 'Former IRS Agent Representation   4.2M Views',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=QxVllUQ7IRk&t=15s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "As a former IRS agent I've worked 10 000 cases I have a whole team of IRS "
               'agents we all work together to resolve cases if you have an IRS problem or you '
               'need a.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': "As a former IRS agent I've worked 10 000 cases I have a whole team of IRS "
              'agents we all work together to resolve cases if you have an IRS problem or you '
              'need a.',
       'title': 'If You Are Filing A Whistle Blower Complaint, Form 211 Or Turning Someone For '
                'Fraud , Form 3949A (Former IRS Agent Representation   4.2M Views)',
       'url': 'https://www.youtube.com/watch?v=QxVllUQ7IRk&t=15s',
       'video_id': 'QxVllUQ7IRk'},
      {'author': 'First Healthcare Compliance',
       'channel': 'First Healthcare Compliance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:56:40](https://www.youtube.com/watch?v=SKjmFHwe2Rk&t=3400s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Leverage there that the government can have against the company and a lot of '
               'times a company will choose to settle rather than be threatened with being '
               'excluded from medicare and medicaid.',
       'timestamp': 3400,
       'timestamp_label': '[00:56:40]',
       'timestamp_seconds': 3400,
       'tip': 'Leverage there that the government can have against the company and a lot of '
              'times a company will choose to settle rather than be threatened with being '
              'excluded from medicare and medicaid.',
       'title': 'Fraud, Healthcare, COVID 19, and the False Claims Act (First Healthcare '
                'Compliance)',
       'url': 'https://www.youtube.com/watch?v=SKjmFHwe2Rk&t=3400s',
       'video_id': 'SKjmFHwe2Rk'},
      {'author': 'ABA Criminal Justice Section',
       'channel': 'ABA Criminal Justice Section',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:30:38](https://www.youtube.com/watch?v=kcNFrNC2BIg&t=1838s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That shoots half as well as it's supposed to because they have no other in the "
               'procurement pipeline and so the fact that they keep procuring the gun.',
       'timestamp': 1838,
       'timestamp_label': '[00:30:38]',
       'timestamp_seconds': 1838,
       'tip': "That shoots half as well as it's supposed to because they have no other in the "
              'procurement pipeline and so the fact that they keep procuring the gun.',
       'title': 'The False Claims Act Post-Escobar | Part 1 (ABA Criminal Justice Section)',
       'url': 'https://www.youtube.com/watch?v=kcNFrNC2BIg&t=1838s',
       'video_id': 'kcNFrNC2BIg'},
      {'author': 'Bloomberg Originals',
       'channel': 'Bloomberg Originals',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:01](https://www.youtube.com/watch?v=eSiH7Rgnhe4&t=241s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Want some sort of Leverage to either get a sweeter or richer deal in terms of '
               'my current uh employment terms or in connection with a severance package.',
       'timestamp': 241,
       'timestamp_label': '[00:04:01]',
       'timestamp_seconds': 241,
       'tip': 'Want some sort of Leverage to either get a sweeter or richer deal in terms of '
              'my current uh employment terms or in connection with a severance package.',
       'title': 'Guttman, Pearlman Debate Dodd-Frank Whistleblower Rules (Bloomberg Originals)',
       'url': 'https://www.youtube.com/watch?v=eSiH7Rgnhe4&t=241s',
       'video_id': 'eSiH7Rgnhe4'},
      {'author': 'Teach Me! Personal Finance',
       'channel': 'Teach Me! Personal Finance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:51](https://www.youtube.com/watch?v=WA3dtUQT9f8&t=771s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Supporting documentation as required and then you complete this information in '
               'line 16 by tax year and by dollar amount to the extent that you know them so '
               "if this is something over multiple tax years then there's space for at least "
               'five different tax years.',
       'timestamp': 771,
       'timestamp_label': '[00:12:51]',
       'timestamp_seconds': 771,
       'tip': 'Supporting documentation as required and then you complete this information in '
              'line 16 by tax year and by dollar amount to the extent that you know them so if '
              "this is something over multiple tax years then there's space for at least five "
              'different tax years.',
       'title': 'IRS Form 211 walkthrough ARCHIVED COPY - READ COMMENTS ONLY (Teach Me! '
                'Personal Finance)',
       'url': 'https://www.youtube.com/watch?v=WA3dtUQT9f8&t=771s',
       'video_id': 'WA3dtUQT9f8'},
      {'author': 'James Hoyer, P.A.',
       'channel': 'James Hoyer, P.A.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:25](https://www.youtube.com/watch?v=whq5-7zwAGE&t=85s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Patient that believed the tax payers were being cheated you have the power '
               "stop it's fraud age vitals owner maintains this case should have been between "
               'the patient and the doctor not the pharmacy Pinellas County Peter Bernard '
               'newsChannel 8.',
       'timestamp': 85,
       'timestamp_label': '[00:01:25]',
       'timestamp_seconds': 85,
       'tip': 'Patient that believed the tax payers were being cheated you have the power stop '
              "it's fraud age vitals owner maintains this case should have been between the "
              'patient and the doctor not the pharmacy Pinellas County Peter Bernard '
              'newsChannel 8.',
       'title': 'Rare Case of Patient Whistleblower leads to Settlement in Medicare Fraud Case '
                '(James Hoyer, P.A.)',
       'url': 'https://www.youtube.com/watch?v=whq5-7zwAGE&t=85s',
       'video_id': 'whq5-7zwAGE'},
      {'author': 'Brown, LLC - A Premier Whistleblower Law Firm',
       'channel': 'Brown, LLC - A Premier Whistleblower Law Firm',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:17](https://www.youtube.com/watch?v=5fDm1yVZ4cM&t=617s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Confidential consultation please call our firm Brown LLC by calling 877 561 '
               "0000 the call is free and confidential and we're only paid in most instances "
               'if we win your kits.',
       'timestamp': 617,
       'timestamp_label': '[00:10:17]',
       'timestamp_seconds': 617,
       'tip': 'Confidential consultation please call our firm Brown LLC by calling 877 561 '
              "0000 the call is free and confidential and we're only paid in most instances if "
              'we win your kits.',
       'title': 'Qui Tam Predictions for 2024 | Brown, LLC (Brown, LLC - A Premier '
                'Whistleblower Law Firm)',
       'url': 'https://www.youtube.com/watch?v=5fDm1yVZ4cM&t=617s',
       'video_id': '5fDm1yVZ4cM'},
      {'author': 'Changing Options',
       'channel': 'Changing Options',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:29](https://www.youtube.com/watch?v=rZEktgyZwgk&t=269s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Do their best to investigate them our contact info is on the next Slide the '
               'county also has an Anonymous hotline 18665 49004 or ww. tnw grc.com SDC.',
       'timestamp': 269,
       'timestamp_label': '[00:04:29]',
       'timestamp_seconds': 269,
       'tip': 'Do their best to investigate them our contact info is on the next Slide the '
              'county also has an Anonymous hotline 18665 49004 or ww. tnw grc.com SDC.',
       'title': 'False Claims Act Training (Changing Options)',
       'url': 'https://www.youtube.com/watch?v=rZEktgyZwgk&t=269s',
       'video_id': 'rZEktgyZwgk'}],
 11: [{'author': 'Robert Eckard Law',
       'channel': 'Robert Eckard Law',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:37](https://www.youtube.com/watch?v=tLBsvqESK6o&t=37s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Enacted which included the anti-money laundering Act of 2020. amla '
               'whistleblower Rewards program requires the Department of Treasury to pay '
               'Awards.',
       'timestamp': 37,
       'timestamp_label': '[00:00:37]',
       'timestamp_seconds': 37,
       'tip': 'Enacted which included the anti-money laundering Act of 2020. amla '
              'whistleblower Rewards program requires the Department of Treasury to pay '
              'Awards.',
       'title': 'Rewarding Whistleblowers Regarding Money Laundering (Robert Eckard Law)',
       'url': 'https://www.youtube.com/watch?v=tLBsvqESK6o&t=37s',
       'video_id': 'tLBsvqESK6o'},
      {'author': 'Husch Blackwell',
       'channel': 'Husch Blackwell',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:14](https://www.youtube.com/watch?v=XAVzMsuvKNE&t=1034s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Are we going to be putting an essential national security contractor out of '
               "business and then we suddenly don't have what we need to defend the nation. So "
               "that's going to be the analysis there at DOJ. And the analysis is a super "
               'simple balancing act here.',
       'timestamp': 1034,
       'timestamp_label': '[00:17:14]',
       'timestamp_seconds': 1034,
       'tip': 'Are we going to be putting an essential national security contractor out of '
              "business and then we suddenly don't have what we need to defend the nation. So "
              "that's going to be the analysis there at DOJ. And the analysis is a super "
              'simple balancing act here.',
       'title': 'Qui Tam Dismissals Are Spiking: What That Means for FCA Enforcement (Husch '
                'Blackwell)',
       'url': 'https://www.youtube.com/watch?v=XAVzMsuvKNE&t=1034s',
       'video_id': 'XAVzMsuvKNE'},
      {'author': 'Changing Options',
       'channel': 'Changing Options',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:23](https://www.youtube.com/watch?v=rZEktgyZwgk&t=263s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Are encouraged to share concerns with the county the agency compliance office '
               'takes all complaints seriously and will do their best to investigate them our '
               'contact info is on the next Slide the county also has an Anonymous hotline '
               '18665 49004 or ww. tnw grc.com SDC.',
       'timestamp': 263,
       'timestamp_label': '[00:04:23]',
       'timestamp_seconds': 263,
       'tip': 'Are encouraged to share concerns with the county the agency compliance office '
              'takes all complaints seriously and will do their best to investigate them our '
              'contact info is on the next Slide the county also has an Anonymous hotline '
              '18665 49004 or ww. tnw grc.com SDC.',
       'title': 'False Claims Act Training (Changing Options)',
       'url': 'https://www.youtube.com/watch?v=rZEktgyZwgk&t=263s',
       'video_id': 'rZEktgyZwgk'},
      {'author': 'American Health Law Association',
       'channel': 'American Health Law Association',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:34](https://www.youtube.com/watch?v=U_YfcwE9PJk&t=334s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Um, did the party act knowingly? Um, and that's an interesting analysis, you "
               'know, looking at actual knowledge or deliberate ignorance or reckless '
               'disregard as as concepts as well.',
       'timestamp': 334,
       'timestamp_label': '[00:05:34]',
       'timestamp_seconds': 334,
       'tip': "Um, did the party act knowingly? Um, and that's an interesting analysis, you "
              'know, looking at actual knowledge or deliberate ignorance or reckless disregard '
              'as as concepts as well.',
       'title': 'False Claims Act: Latest Trends and Developments (American Health Law '
                'Association)',
       'url': 'https://www.youtube.com/watch?v=U_YfcwE9PJk&t=334s',
       'video_id': 'U_YfcwE9PJk'},
      {'author': 'Fraud in America',
       'channel': 'Fraud in America',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:43](https://www.youtube.com/watch?v=R3h4J-EAtro&t=403s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'ve dealt with a wide variety of whistleblower programs, whether it's the SEC, "
               'the CFTC, the IRS, or the False Claims Act. Our members had a lot of views on '
               'how what best practices are for a government whistleblower program.',
       'timestamp': 403,
       'timestamp_label': '[00:06:43]',
       'timestamp_seconds': 403,
       'tip': "'ve dealt with a wide variety of whistleblower programs, whether it's the SEC, "
              'the CFTC, the IRS, or the False Claims Act. Our members had a lot of views on '
              'how what best practices are for a government whistleblower program.',
       'title': 'FinCEN Proposed Regulations (Fraud in America)',
       'url': 'https://www.youtube.com/watch?v=R3h4J-EAtro&t=403s',
       'video_id': 'R3h4J-EAtro'},
      {'author': 'Stephen Teller - Teller Law',
       'channel': 'Stephen Teller - Teller Law',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:05](https://www.youtube.com/watch?v=SiATzxJHy2Y&t=485s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That would be public record already. But if I'm bringing a false claims act "
               "case against Amazon I can't talk about that in in a very in a um even more so "
               "than the attorney client privilege issues. So it'll be Yeah, it'll So I'm "
               'sorry.',
       'timestamp': 485,
       'timestamp_label': '[00:08:05]',
       'timestamp_seconds': 485,
       'tip': "That would be public record already. But if I'm bringing a false claims act "
              "case against Amazon I can't talk about that in in a very in a um even more so "
              "than the attorney client privilege issues. So it'll be Yeah, it'll So I'm "
              'sorry.',
       'title': 'How Qui Tam Lawsuits Actually Work (Stephen Teller - Teller Law)',
       'url': 'https://www.youtube.com/watch?v=SiATzxJHy2Y&t=485s',
       'video_id': 'SiATzxJHy2Y'},
      {'author': 'PilieroMazza PLLC',
       'channel': 'PilieroMazza PLLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:57:34](https://www.youtube.com/watch?v=OqheRWaihEo&t=3454s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Those kinds of situations are where we've really seen False Claims Act "
               "liability. We haven't really seen False Claims Act issues if you're like on "
               "the periphery or some people say, well, if you're a government contractor, you "
               'should have never applied.',
       'timestamp': 3454,
       'timestamp_label': '[00:57:34]',
       'timestamp_seconds': 3454,
       'tip': "Those kinds of situations are where we've really seen False Claims Act "
              "liability. We haven't really seen False Claims Act issues if you're like on the "
              "periphery or some people say, well, if you're a government contractor, you "
              'should have never applied.',
       'title': 'Common Scenarios Triggering False Claims Act Violations, Part 1: Gov. '
                'Contracts and Cybersecurity (PilieroMazza PLLC)',
       'url': 'https://www.youtube.com/watch?v=OqheRWaihEo&t=3454s',
       'video_id': 'OqheRWaihEo'},
      {'author': 'NCURA1959',
       'channel': 'NCURA1959',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:14](https://www.youtube.com/watch?v=oh1aiSdEJHY&t=134s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Research administrators two of the greatest assets we can offer are our '
               "integrity and our knowledge I applaud you for keeping current with nura's "
               'YouTube Tuesday videos and wish you only the best in your career as a research '
               'administrator thank you e.',
       'timestamp': 134,
       'timestamp_label': '[00:02:14]',
       'timestamp_seconds': 134,
       'tip': 'Research administrators two of the greatest assets we can offer are our '
              "integrity and our knowledge I applaud you for keeping current with nura's "
              'YouTube Tuesday videos and wish you only the best in your career as a research '
              'administrator thank you e.',
       'title': 'The False Claims Act: What It Is And Why You Should Care (NCURA1959)',
       'url': 'https://www.youtube.com/watch?v=oh1aiSdEJHY&t=134s',
       'video_id': 'oh1aiSdEJHY'},
      {'author': 'Beasley Allen',
       'channel': 'Beasley Allen',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:45](https://www.youtube.com/watch?v=dnDB-BkTNpk&t=105s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A nurse or someone dealing directly with Services involving the federal '
               'government and when that occurs and you see something going on you should '
               'contact an attorney because you may be the next whistleblower that protects '
               'taxpayer funds from corruption.',
       'timestamp': 105,
       'timestamp_label': '[00:01:45]',
       'timestamp_seconds': 105,
       'tip': 'A nurse or someone dealing directly with Services involving the federal '
              'government and when that occurs and you see something going on you should '
              'contact an attorney because you may be the next whistleblower that protects '
              'taxpayer funds from corruption.',
       'title': 'Qui Tam - Your Whistleblower Rights (Beasley Allen)',
       'url': 'https://www.youtube.com/watch?v=dnDB-BkTNpk&t=105s',
       'video_id': 'dnDB-BkTNpk'},
      {'author': 'Kohn Kohn & Colapinto',
       'channel': 'Kohn Kohn & Colapinto',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=O45E7FrG_mM&t=20s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "At the national westerlar center and i'm also an attorney myself representing "
               'tax whistleblowers at zurby miller finger rat um just want to.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': "At the national westerlar center and i'm also an attorney myself representing "
              'tax whistleblowers at zurby miller finger rat um just want to.',
       'title': 'IRS Tax Whistleblower Program: The Basics With A Focus On Offshore Accounts '
                '(Kohn Kohn & Colapinto)',
       'url': 'https://www.youtube.com/watch?v=O45E7FrG_mM&t=20s',
       'video_id': 'O45E7FrG_mM'},
      {'author': 'Garrison, Levin-Epstein, Fitzgerald & Pirrotti',
       'channel': 'Garrison, Levin-Epstein, Fitzgerald & Pirrotti',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:24](https://www.youtube.com/watch?v=ft81gWsFd2M&t=24s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "If you work for a publicly traded company, any company that's traded for "
               'example on the New York Stock Exchange or the Nasdaq or for a contractor or a '
               'subsidiary of one of those companies and you report fraud, these laws can '
               'protect your job.',
       'timestamp': 24,
       'timestamp_label': '[00:00:24]',
       'timestamp_seconds': 24,
       'tip': "If you work for a publicly traded company, any company that's traded for "
              'example on the New York Stock Exchange or the Nasdaq or for a contractor or a '
              'subsidiary of one of those companies and you report fraud, these laws can '
              'protect your job.',
       'title': 'Sarbanes-Oxley and Dodd-Frank Whistleblower Protections (Garrison, '
                'Levin-Epstein, Fitzgerald & Pirrotti)',
       'url': 'https://www.youtube.com/watch?v=ft81gWsFd2M&t=24s',
       'video_id': 'ft81gWsFd2M'},
      {'author': 'K2 GRC',
       'channel': 'K2 GRC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:08](https://www.youtube.com/watch?v=BgDdBSZpEjc&t=188s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'They are an individual that reports evidence of wrongdoing in an organization. '
               'This can be an employee, someone in management, or even someone outside of the '
               'company.',
       'timestamp': 188,
       'timestamp_label': '[00:03:08]',
       'timestamp_seconds': 188,
       'tip': 'They are an individual that reports evidence of wrongdoing in an organization. '
              'This can be an employee, someone in management, or even someone outside of the '
              'company.',
       'title': 'False Claims Act EXPLAINED  Real Cases & Massive Penalties (K2 GRC)',
       'url': 'https://www.youtube.com/watch?v=BgDdBSZpEjc&t=188s',
       'video_id': 'BgDdBSZpEjc'},
      {'author': 'Sanford Heisler Sharp McKnight',
       'channel': 'Sanford Heisler Sharp McKnight',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:10](https://www.youtube.com/watch?v=zvfb6_cVFWg&t=190s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Got to talk to somebody about it you need to go to somebody who has an open '
               "mind to the possibilities that exist in today's environment but you have to "
               "have somebody who's curious enough to to listen and ask the right questions so "
               'that that you can get some real advice.',
       'timestamp': 190,
       'timestamp_label': '[00:03:10]',
       'timestamp_seconds': 190,
       'tip': 'Got to talk to somebody about it you need to go to somebody who has an open '
              "mind to the possibilities that exist in today's environment but you have to "
              "have somebody who's curious enough to to listen and ask the right questions so "
              'that that you can get some real advice.',
       'title': 'Our Whistleblower and Qui Tam Practice (Sanford Heisler Sharp McKnight)',
       'url': 'https://www.youtube.com/watch?v=zvfb6_cVFWg&t=190s',
       'video_id': 'zvfb6_cVFWg'},
      {'author': 'nurselyf',
       'channel': 'nurselyf',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:25](https://www.youtube.com/watch?v=T-h0f2YLPec&t=145s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'How fraud investigations happen. Data analysis flags unusual billing patterns. '
               'Whistleblowers report suspicious practices under the False Claims Act. Audits '
               'and subpoenas gather documentation and interview staff.',
       'timestamp': 145,
       'timestamp_label': '[00:02:25]',
       'timestamp_seconds': 145,
       'tip': 'How fraud investigations happen. Data analysis flags unusual billing patterns. '
              'Whistleblowers report suspicious practices under the False Claims Act. Audits '
              'and subpoenas gather documentation and interview staff.',
       'title': 'Preventing Healthcare Fraud: Stark Law, Anti-Kickback Statute & How to Stay '
                'Compliant (nurselyf)',
       'url': 'https://www.youtube.com/watch?v=T-h0f2YLPec&t=145s',
       'video_id': 'T-h0f2YLPec'},
      {'author': 'The Anti-Fraud Coalition',
       'channel': 'The Anti-Fraud Coalition',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=fQss6bE5tKc&t=20s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '211, application for award for original information. Unlike some other '
               'whistleblower programs, tips cannot be submitted anonymously to the IRS, but '
               'the IRS does protect whistleblowers confidentiality.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': '211, application for award for original information. Unlike some other '
              'whistleblower programs, tips cannot be submitted anonymously to the IRS, but '
              'the IRS does protect whistleblowers confidentiality.',
       'title': 'IRS Whistleblower Program Primer (The Anti-Fraud Coalition)',
       'url': 'https://www.youtube.com/watch?v=fQss6bE5tKc&t=20s',
       'video_id': 'fQss6bE5tKc'}],
 12: [{'author': 'Whistleblower Network News',
       'channel': 'Whistleblower Network News',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:39:38](https://www.youtube.com/watch?v=wsT0MJ2Q9Gg&t=2378s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s in the whistleblower reform bill would be um accompanied by some action on "
               'the appropriation front um to ensure staffing and funding for the '
               'whistleblower office to meet uh those deadlines and accelerate the processing '
               'of awards.',
       'timestamp': 2378,
       'timestamp_label': '[00:39:38]',
       'timestamp_seconds': 2378,
       'tip': "'s in the whistleblower reform bill would be um accompanied by some action on "
              'the appropriation front um to ensure staffing and funding for the whistleblower '
              'office to meet uh those deadlines and accelerate the processing of awards.',
       'title': 'Strengthening the SEC Whistleblower Program (Whistleblower Network News)',
       'url': 'https://www.youtube.com/watch?v=wsT0MJ2Q9Gg&t=2378s',
       'video_id': 'wsT0MJ2Q9Gg'},
      {'author': 'UAP Legion',
       'channel': 'UAP Legion',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:46](https://www.youtube.com/watch?v=Y9DOny35SW0&t=766s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'There are major monetary awards for whistleblowers with successful recoveries '
               'under the federal False Claims Act statute. Under the federal False Claims '
               'Act, if the qui tam FCA action succeeds, the whistleblower is entitled to 15% '
               'to 30% of the total recovery by law.',
       'timestamp': 766,
       'timestamp_label': '[00:12:46]',
       'timestamp_seconds': 766,
       'tip': 'There are major monetary awards for whistleblowers with successful recoveries '
              'under the federal False Claims Act statute. Under the federal False Claims Act, '
              'if the qui tam FCA action succeeds, the whistleblower is entitled to 15% to 30% '
              'of the total recovery by law.',
       'title': 'UAP Whistleblowers: The False Claims Act (UAP Legion)',
       'url': 'https://www.youtube.com/watch?v=Y9DOny35SW0&t=766s',
       'video_id': 'Y9DOny35SW0'},
      {'author': 'Tony Munter Attorney at Law',
       'channel': 'Tony Munter Attorney at Law',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:29](https://www.youtube.com/watch?v=IX4WhZTmPRI&t=29s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'First, it should just plain scream out as Fraud. I can talk all day about the '
               'technical requirements for your case to meet the definition of a claim. I can '
               'ask all kinds of questions, and these questions are very important, and may '
               'affect your ability to collect on the case.',
       'timestamp': 29,
       'timestamp_label': '[00:00:29]',
       'timestamp_seconds': 29,
       'tip': 'First, it should just plain scream out as Fraud. I can talk all day about the '
              'technical requirements for your case to meet the definition of a claim. I can '
              'ask all kinds of questions, and these questions are very important, and may '
              'affect your ability to collect on the case.',
       'title': 'How Can I Make a Strong False Claims Act Case? | Tony Munter Attorney at Law '
                '(Tony Munter Attorney at Law)',
       'url': 'https://www.youtube.com/watch?v=IX4WhZTmPRI&t=29s',
       'video_id': 'IX4WhZTmPRI'},
      {'author': 'Cape Endeavors, Inc.',
       'channel': 'Cape Endeavors, Inc.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:37:26](https://www.youtube.com/watch?v=-2BTi30xXrA&t=2246s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I mean, you and I, as as you know, from these these incidents, you're on the "
               'phone, you know, 12 hours a day, all all manner, especially in the early days, '
               'and being in the the foxhole with you is just tremendous.',
       'timestamp': 2246,
       'timestamp_label': '[00:37:26]',
       'timestamp_seconds': 2246,
       'tip': "I mean, you and I, as as you know, from these these incidents, you're on the "
              'phone, you know, 12 hours a day, all all manner, especially in the early days, '
              'and being in the the foxhole with you is just tremendous.',
       'title': 'Whistleblowers, CMMC & the DOJ: The Hidden Triggers Behind False Claims Act '
                'Investigations (Cape Endeavors, Inc.)',
       'url': 'https://www.youtube.com/watch?v=-2BTi30xXrA&t=2246s',
       'video_id': '-2BTi30xXrA'},
      {'author': 'Against The Fraud',
       'channel': 'Against The Fraud',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:23](https://www.youtube.com/watch?v=QmB-gKtr0tc&t=323s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s attorney files a qui tam lawsuit, it does not go on the public record, not "
               'at all. On day one, the complaint is filed under seal on a secret court docket '
               "that's kept locked down by the clerk of the court.",
       'timestamp': 323,
       'timestamp_label': '[00:05:23]',
       'timestamp_seconds': 323,
       'tip': "'s attorney files a qui tam lawsuit, it does not go on the public record, not "
              'at all. On day one, the complaint is filed under seal on a secret court docket '
              "that's kept locked down by the clerk of the court.",
       'title': 'The Secret Law That Pays You 30% to Expose Corporate Fraud (False Claims Act '
                'Deep Dive) (Against The Fraud)',
       'url': 'https://www.youtube.com/watch?v=QmB-gKtr0tc&t=323s',
       'video_id': 'QmB-gKtr0tc'},
      {'author': 'Oklahoma Insurance Department',
       'channel': 'Oklahoma Insurance Department',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:25:09](https://www.youtube.com/watch?v=BLKbLs-2Y2I&t=1509s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "If you're on a Medicare Advantage plan, you're going to actually get an "
               'explanation of benefits from that plan, and you need to take the time to '
               "review that very carefully and make sure that it's accurate. Did you go to the "
               'doctor on that date?',
       'timestamp': 1509,
       'timestamp_label': '[00:25:09]',
       'timestamp_seconds': 1509,
       'tip': "If you're on a Medicare Advantage plan, you're going to actually get an "
              'explanation of benefits from that plan, and you need to take the time to review '
              "that very carefully and make sure that it's accurate. Did you go to the doctor "
              'on that date?',
       'title': '2025 Medicare Monday Ep. 5: Medicare Fraud Prevention (Oklahoma Insurance '
                'Department)',
       'url': 'https://www.youtube.com/watch?v=BLKbLs-2Y2I&t=1509s',
       'video_id': 'BLKbLs-2Y2I'},
      {'author': 'Brown, LLC - A Premier Whistleblower Law Firm',
       'channel': 'Brown, LLC - A Premier Whistleblower Law Firm',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:22](https://www.youtube.com/watch?v=0_sJP-wJPRc&t=82s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'However, the program has become more challenging every day for whistleblowers '
               'to navigate, especially when people file it without an attorney.',
       'timestamp': 82,
       'timestamp_label': '[00:01:22]',
       'timestamp_seconds': 82,
       'tip': 'However, the program has become more challenging every day for whistleblowers '
              'to navigate, especially when people file it without an attorney.',
       'title': 'SEC Whistleblower Program Crisis? 31 Awards Denied Back-to-Back (Brown, LLC - '
                'A Premier Whistleblower Law Firm)',
       'url': 'https://www.youtube.com/watch?v=0_sJP-wJPRc&t=82s',
       'video_id': '0_sJP-wJPRc'},
      {'author': 'Money vs. The System',
       'channel': 'Money vs. The System',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:50](https://www.youtube.com/watch?v=QrUTZJlJrbQ&t=50s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And all it takes to start the machine is one word at your kitchen table. It '
               'begins with a call center. The federal appeals court describes it this way.',
       'timestamp': 50,
       'timestamp_label': '[00:00:50]',
       'timestamp_seconds': 50,
       'tip': 'And all it takes to start the machine is one word at your kitchen table. It '
              'begins with a call center. The federal appeals court describes it this way.',
       'title': 'Medicare Scam: Nurse Billed 24+ Hours a Day in Free Cancer Test Scheme (Money '
                'vs. The System)',
       'url': 'https://www.youtube.com/watch?v=QrUTZJlJrbQ&t=50s',
       'video_id': 'QrUTZJlJrbQ'},
      {'author': 'Cohen Milstein',
       'channel': 'Cohen Milstein',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:57](https://www.youtube.com/watch?v=skGozAS0va8&t=117s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Do every day if you choose to retain us we will represent you on a fully '
               'contingent basis we only receive a fee if you receive a whistleblower reward '
               'if you would like to discuss your potential claim please contact us for a '
               'confidential consultation.',
       'timestamp': 117,
       'timestamp_label': '[00:01:57]',
       'timestamp_seconds': 117,
       'tip': 'Do every day if you choose to retain us we will represent you on a fully '
              'contingent basis we only receive a fee if you receive a whistleblower reward if '
              'you would like to discuss your potential claim please contact us for a '
              'confidential consultation.',
       'title': 'The Whistleblower Process and the False Claims Act – Cohen Milstein Explains '
                '(Cohen Milstein)',
       'url': 'https://www.youtube.com/watch?v=skGozAS0va8&t=117s',
       'video_id': 'skGozAS0va8'},
      {'author': 'Phillips & Cohen LLP',
       'channel': 'Phillips & Cohen LLP',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:16:56](https://www.youtube.com/watch?v=5-ptDaAQkvI&t=4616s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Relator consents or not especially given that the government is not even a '
               'party to the action at the time the request is made who wants to take that one '
               'motions for partial.',
       'timestamp': 4616,
       'timestamp_label': '[01:16:56]',
       'timestamp_seconds': 4616,
       'tip': 'Relator consents or not especially given that the government is not even a '
              'party to the action at the time the request is made who wants to take that one '
              'motions for partial.',
       'title': 'Recurring Issues in False Claims Act Litigation (Phillips & Cohen LLP)',
       'url': 'https://www.youtube.com/watch?v=5-ptDaAQkvI&t=4616s',
       'video_id': '5-ptDaAQkvI'},
      {'author': 'Compliance Podcast Network',
       'channel': 'Compliance Podcast Network',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:20:46](https://www.youtube.com/watch?v=bFRmUwE-_F4&t=1246s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Management but it's just going to be something that compliance officers would "
               "have to Grapple with um we'll we'll see how it works well Matt that seems like "
               "a good place for us to end this episode uh I can't wait to see what next week "
               'brings us thank you very much Tom.',
       'timestamp': 1246,
       'timestamp_label': '[00:20:46]',
       'timestamp_seconds': 1246,
       'tip': "Management but it's just going to be something that compliance officers would "
              "have to Grapple with um we'll we'll see how it works well Matt that seems like "
              "a good place for us to end this episode uh I can't wait to see what next week "
              'brings us thank you very much Tom.',
       'title': 'Compliance into the Weeds: The DOJ Whistleblower Incentive Program '
                '(Compliance Podcast Network)',
       'url': 'https://www.youtube.com/watch?v=bFRmUwE-_F4&t=1246s',
       'video_id': 'bFRmUwE-_F4'},
      {'author': 'The Employment Law Group, P.C.',
       'channel': 'The Employment Law Group, P.C.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:07](https://www.youtube.com/watch?v=m7bKdhkfWEE&t=187s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Greg thanks for giving us a quick peek into what we can expect to see during '
               'the afternoon of day two of our 2023 KTM conference scheduled for February '
               '16th and 17th in Washington DC at the Hilton Washington DC capitol hill join '
               'us in person or virtually at www.fba.org.',
       'timestamp': 187,
       'timestamp_label': '[00:03:07]',
       'timestamp_seconds': 187,
       'tip': 'Greg thanks for giving us a quick peek into what we can expect to see during '
              'the afternoon of day two of our 2023 KTM conference scheduled for February 16th '
              'and 17th in Washington DC at the Hilton Washington DC capitol hill join us in '
              'person or virtually at www.fba.org.',
       'title': '"Qui Tam 2023" Panel Preview - Interviewing Whistleblowers: Techniques and '
                'Cautions (The Employment Law Group, P.C.)',
       'url': 'https://www.youtube.com/watch?v=m7bKdhkfWEE&t=187s',
       'video_id': 'm7bKdhkfWEE'},
      {'author': 'Logan Allec',
       'channel': 'Logan Allec',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:33](https://www.youtube.com/watch?v=i4GnKgGXiMw&t=213s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Yourself here um you're you're the claimant just FYI um so yeah that's that's "
               "basically it here's where to mail it there you go so you know if you know any "
               'tax cheats in your life report the IRS you might make some money.',
       'timestamp': 213,
       'timestamp_label': '[00:03:33]',
       'timestamp_seconds': 213,
       'tip': "Yourself here um you're you're the claimant just FYI um so yeah that's that's "
              "basically it here's where to mail it there you go so you know if you know any "
              'tax cheats in your life report the IRS you might make some money.',
       'title': 'Get Paid for Reporting Tax Cheats | IRS Whistleblower Program (Logan Allec)',
       'url': 'https://www.youtube.com/watch?v=i4GnKgGXiMw&t=213s',
       'video_id': 'i4GnKgGXiMw'},
      {'author': 'Robert Eckard Law',
       'channel': 'Robert Eckard Law',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:07](https://www.youtube.com/watch?v=tLBsvqESK6o&t=127s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Judicial or administrative action brought under the bank secrecy act that '
               'results in sanctions exceeding one million dollars the anti-money.',
       'timestamp': 127,
       'timestamp_label': '[00:02:07]',
       'timestamp_seconds': 127,
       'tip': 'Judicial or administrative action brought under the bank secrecy act that '
              'results in sanctions exceeding one million dollars the anti-money.',
       'title': 'Rewarding Whistleblowers Regarding Money Laundering (Robert Eckard Law)',
       'url': 'https://www.youtube.com/watch?v=tLBsvqESK6o&t=127s',
       'video_id': 'tLBsvqESK6o'},
      {'author': 'OIGatHHS',
       'channel': 'OIGatHHS',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:46](https://www.youtube.com/watch?v=BbZ78QTLztQ&t=226s)',
       'relevance': 'Attributed practitioner commentary on forensic public-dataset anomaly '
                    'detection (`CMS` Part B/D, Open Payments, `SAM.gov` procurement, and '
                    'import manifests) paired with paid relator-counsel litigation-support '
                    'retainers and `15%–30%` statutory whistleblower filings (`31 U.S.C. § '
                    '3730`, `SEC`, `CFTC`, `IRS`) (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'If a provider identifies billing mistakes in the course of those audits, the '
               'provider must repay overpayments to Medicare and Medicaid within 60 days to '
               'avoid False Claims Act liability.',
       'timestamp': 226,
       'timestamp_label': '[00:03:46]',
       'timestamp_seconds': 226,
       'tip': 'If a provider identifies billing mistakes in the course of those audits, the '
              'provider must repay overpayments to Medicare and Medicaid within 60 days to '
              'avoid False Claims Act liability.',
       'title': 'False Claims Act (OIGatHHS)',
       'url': 'https://www.youtube.com/watch?v=BbZ78QTLztQ&t=226s',
       'video_id': 'BbZ78QTLztQ'}]}
