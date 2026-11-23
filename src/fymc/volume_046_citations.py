"""Curated 180-citation Mass-Tort Case Acquisition, HITECH Record Triage & Law-Firm MSOs baseline (15 per chapter across Q1-Q12) mined strictly from verified Mass-Tort Case Acquisition, HITECH Record Triage & Law-Firm MSOs YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'164',
     '524',
     '702',
     'aba',
     'abs',
     'accident',
     'acquisition',
     'act',
     'administrative',
     'ads',
     'advertising',
     'afff',
     'agencies',
     'alternative',
     'api',
     'arizona',
     'auditing',
     'automation',
     'bankrupt',
     'bar',
     'bellwethers',
     'bot',
     'building',
     'business',
     'buyers',
     'call',
     'case',
     'cashflow',
     'causation',
     'center',
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
 2: {'164',
     '524',
     '702',
     'aba',
     'abs',
     'accident',
     'acquisition',
     'act',
     'administrative',
     'ads',
     'advertising',
     'afff',
     'agencies',
     'alternative',
     'api',
     'arizona',
     'auditing',
     'automation',
     'bankrupt',
     'bar',
     'bellwethers',
     'bot',
     'budget',
     'building',
     'business',
     'buyer',
     'buyers',
     'call',
     'case',
     'cashflow',
     'causation',
     'center',
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
 3: {'164',
     '524',
     '702',
     'aba',
     'abs',
     'accident',
     'acquisition',
     'act',
     'administrative',
     'ads',
     'advertising',
     'afff',
     'agencies',
     'alternative',
     'api',
     'arizona',
     'auditing',
     'automation',
     'bankrupt',
     'bar',
     'bellwethers',
     'bot',
     'building',
     'business',
     'buyers',
     'call',
     'case',
     'cash',
     'cashflow',
     'causation',
     'center',
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
 4: {'164',
     '524',
     '702',
     'aba',
     'abs',
     'accident',
     'acquisition',
     'act',
     'administrative',
     'ads',
     'advertising',
     'afff',
     'agencies',
     'alternative',
     'api',
     'arizona',
     'auditing',
     'automation',
     'bankrupt',
     'bar',
     'bellwethers',
     'bot',
     'budget',
     'building',
     'business',
     'buyers',
     'call',
     'capital',
     'case',
     'cashflow',
     'causation',
     'center',
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
 5: {'164',
     '524',
     '702',
     'aba',
     'abs',
     'accident',
     'acquisition',
     'act',
     'administrative',
     'ads',
     'advertising',
     'afff',
     'agencies',
     'alternative',
     'api',
     'arizona',
     'audit',
     'auditing',
     'automation',
     'avoid',
     'bankrupt',
     'bar',
     'bellwethers',
     'bot',
     'building',
     'business',
     'buyers',
     'call',
     'case',
     'cashflow',
     'causation',
     'center',
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
 6: {'164',
     '524',
     '702',
     'aba',
     'abs',
     'accident',
     'acquisition',
     'act',
     'administrative',
     'ads',
     'advertising',
     'afff',
     'agencies',
     'alternative',
     'api',
     'arizona',
     'auditing',
     'automation',
     'bankrupt',
     'bar',
     'bellwethers',
     'bot',
     'building',
     'business',
     'buyers',
     'call',
     'case',
     'cashflow',
     'causation',
     'center',
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
 7: {'164',
     '524',
     '702',
     'aba',
     'abs',
     'accident',
     'acquisition',
     'act',
     'administrative',
     'ads',
     'advertising',
     'afff',
     'agencies',
     'alternative',
     'api',
     'arizona',
     'auditing',
     'automation',
     'bankrupt',
     'bar',
     'bellwethers',
     'bot',
     'building',
     'business',
     'buyers',
     'call',
     'case',
     'cashflow',
     'causation',
     'center',
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
 8: {'164',
     '524',
     '702',
     'aba',
     'abs',
     'accident',
     'acquisition',
     'act',
     'administrative',
     'ads',
     'advertising',
     'afff',
     'agencies',
     'alternative',
     'api',
     'arizona',
     'auditing',
     'automation',
     'bankrupt',
     'bar',
     'bellwethers',
     'bot',
     'building',
     'business',
     'buyers',
     'call',
     'case',
     'cashflow',
     'causation',
     'center',
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
 9: {'164',
     '524',
     '702',
     'aba',
     'abs',
     'accident',
     'acquisition',
     'act',
     'administrative',
     'ads',
     'advertising',
     'afff',
     'agencies',
     'agreement',
     'alternative',
     'api',
     'arizona',
     'auditing',
     'automation',
     'bankrupt',
     'bar',
     'bellwethers',
     'bot',
     'building',
     'business',
     'buyers',
     'call',
     'case',
     'cashflow',
     'causation',
     'center',
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
 10: {'164',
      '524',
      '702',
      'aba',
      'abs',
      'accident',
      'acquisition',
      'act',
      'administrative',
      'ads',
      'advertising',
      'afff',
      'agencies',
      'agent',
      'ai',
      'alternative',
      'api',
      'arizona',
      'auditing',
      'automate',
      'automation',
      'bankrupt',
      'bar',
      'bellwethers',
      'bot',
      'building',
      'business',
      'buyers',
      'call',
      'case',
      'cashflow',
      'causation',
      'center',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'164',
      '524',
      '702',
      'aba',
      'abs',
      'accident',
      'acquisition',
      'act',
      'administrative',
      'ads',
      'advertising',
      'afff',
      'agencies',
      'alternative',
      'api',
      'arizona',
      'auditing',
      'automation',
      'bankrupt',
      'bar',
      'bellwethers',
      'bot',
      'building',
      'business',
      'buyers',
      'call',
      'case',
      'cashflow',
      'causation',
      'center',
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
 12: {'164',
      '524',
      '702',
      'aba',
      'abs',
      'accident',
      'acquisition',
      'act',
      'action',
      'administrative',
      'ads',
      'advertising',
      'afff',
      'agencies',
      'alternative',
      'api',
      'arizona',
      'auditing',
      'automation',
      'bankrupt',
      'bar',
      'bellwethers',
      'bot',
      'building',
      'business',
      'buyers',
      'call',
      'case',
      'cashflow',
      'causation',
      'center',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'The Heart of Law Podcast',
      'channel': 'The Heart of Law Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:48](https://www.youtube.com/watch?v=OdPOa3osKC0&t=768s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s practicing law, still being very careful about how you're doing client "
              'intake and having appropriate communication with the clients and not having in '
              "the case of one of the ABS's that was discipline, an office manager who was "
              'signing clients.',
      'timestamp': 768,
      'timestamp_label': '[00:12:48]',
      'timestamp_seconds': 768,
      'tip': "'s practicing law, still being very careful about how you're doing client intake "
             'and having appropriate communication with the clients and not having in the case '
             "of one of the ABS's that was discipline, an office manager who was signing "
             'clients.',
      'title': 'Alternative Business Structures: Updates from Arizona’s Legal Frontier (The '
               'Heart of Law Podcast)',
      'url': 'https://www.youtube.com/watch?v=OdPOa3osKC0&t=768s',
      'video_id': 'OdPOa3osKC0'},
     {'author': 'Optimize My Firm',
      'channel': 'Optimize My Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:36](https://www.youtube.com/watch?v=lgURVgZL9IY&t=1176s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh, and figuring out, as you said, what your niche is, continuing to make those '
              "personal connections within your market. Uh, there's space for everybody and "
              'good business models will survive as long as you are providing a great service.',
      'timestamp': 1176,
      'timestamp_label': '[00:19:36]',
      'timestamp_seconds': 1176,
      'tip': 'Uh, and figuring out, as you said, what your niche is, continuing to make those '
             "personal connections within your market. Uh, there's space for everybody and "
             'good business models will survive as long as you are providing a great service.',
      'title': 'MSOs, Your Market, And Your Choice - PIMM 151 (Optimize My Firm)',
      'url': 'https://www.youtube.com/watch?v=lgURVgZL9IY&t=1176s',
      'video_id': 'lgURVgZL9IY'},
     {'author': 'Tort Experts',
      'channel': 'Tort Experts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:36:10](https://www.youtube.com/watch?v=AyY5OoT74DQ&t=2170s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You uh institute policies uh firm policies. You institute uh uh tickers. I used '
              'we used to call them that uh every so often the uh client is is contacted.',
      'timestamp': 2170,
      'timestamp_label': '[00:36:10]',
      'timestamp_seconds': 2170,
      'tip': 'You uh institute policies uh firm policies. You institute uh uh tickers. I used '
             'we used to call them that uh every so often the uh client is is contacted.',
      'title': 'Ben Martin & Sebastian Westerby | Depo-Provera Litigation, Mass Torts, and '
               'Case Acquisition Reality (Tort Experts)',
      'url': 'https://www.youtube.com/watch?v=AyY5OoT74DQ&t=2170s',
      'video_id': 'AyY5OoT74DQ'},
     {'author': 'Jon and Marc',
      'channel': 'Jon and Marc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=NHmq2W3F_do&t=22s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Because if the answer is internal margins or shareholder expectations, that '
              'changes how strategy gets built. Our RR Digital stays independent so we can '
              'optimize around one thing, law firm growth. That means cases, clients, and '
              'revenue.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'Because if the answer is internal margins or shareholder expectations, that '
             'changes how strategy gets built. Our RR Digital stays independent so we can '
             'optimize around one thing, law firm growth. That means cases, clients, and '
             'revenue.',
      'title': 'Navigating Mass Tort Settlements: The 95% Participation Threshold & '
               'Depo-Provera Rules (Jon and Marc)',
      'url': 'https://www.youtube.com/watch?v=NHmq2W3F_do&t=22s',
      'video_id': 'NHmq2W3F_do'},
     {'author': 'Fleming, Nolen & Jez',
      'channel': 'Fleming, Nolen & Jez',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:27](https://www.youtube.com/watch?v=qOnM2bNh01E&t=207s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Tell you how many clients that I have call up and say what's happening with my "
              "case what's going on with my case and and we'll tell them well here's what's.",
      'timestamp': 207,
      'timestamp_label': '[00:03:27]',
      'timestamp_seconds': 207,
      'tip': "Tell you how many clients that I have call up and say what's happening with my "
             "case what's going on with my case and and we'll tell them well here's what's.",
      'title': 'Why is a Bellwether Trial Important? (Fleming, Nolen & Jez)',
      'url': 'https://www.youtube.com/watch?v=qOnM2bNh01E&t=207s',
      'video_id': 'qOnM2bNh01E'},
     {'author': 'The Future Is Bright Podcast',
      'channel': 'The Future Is Bright Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:38](https://www.youtube.com/watch?v=CdJKmwCQvOw&t=1298s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh, we are, you know, in that case, they may come into the US and and do '
              "business here. We are free to make other MSO investments. We're free to make "
              "other law firm investments. Obviously, in the US, however, they'd have to be "
              'made through MSOs.',
      'timestamp': 1298,
      'timestamp_label': '[00:21:38]',
      'timestamp_seconds': 1298,
      'tip': 'Uh, we are, you know, in that case, they may come into the US and and do '
             "business here. We are free to make other MSO investments. We're free to make "
             "other law firm investments. Obviously, in the US, however, they'd have to be "
             'made through MSOs.',
      'title': 'David Perla on Litigation Finance, Law Firm Investment, and the Future of '
               'Legal Talent (The Future Is Bright Podcast)',
      'url': 'https://www.youtube.com/watch?v=CdJKmwCQvOw&t=1298s',
      'video_id': 'CdJKmwCQvOw'},
     {'author': 'Ten Golden Rules Internet Marketing for Law Firms',
      'channel': 'Ten Golden Rules Internet Marketing for Law Firms',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:18](https://www.youtube.com/watch?v=I4F5OYZQJuU&t=1698s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You cannot offshore to China. But some of these finance bros, you know, they '
              "just think they know everything and that they walk on water. It's knocking us "
              'all out of our chair here. Others have said things to us like once we control '
              'client intake, then we control the firm.',
      'timestamp': 1698,
      'timestamp_label': '[00:28:18]',
      'timestamp_seconds': 1698,
      'tip': 'You cannot offshore to China. But some of these finance bros, you know, they '
             "just think they know everything and that they walk on water. It's knocking us "
             'all out of our chair here. Others have said things to us like once we control '
             'client intake, then we control the firm.',
      'title': 'Legal MSOs: Managed Service Organizations & the Future of Law Firms | MSO '
               'Advisor Frederick Shelton (Ten Golden Rules Internet Marketing for Law Firms)',
      'url': 'https://www.youtube.com/watch?v=I4F5OYZQJuU&t=1698s',
      'video_id': 'I4F5OYZQJuU'},
     {'author': 'McGuireWoods LLP',
      'channel': 'McGuireWoods LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:21](https://www.youtube.com/watch?v=tBtb3Kmq3ZA&t=861s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Reliable model of that market a model that included both supply side factors '
              'and demand side factors and as part of the supply side factors that the expert.',
      'timestamp': 861,
      'timestamp_label': '[00:14:21]',
      'timestamp_seconds': 861,
      'tip': 'Reliable model of that market a model that included both supply side factors and '
             'demand side factors and as part of the supply side factors that the expert.',
      'title': 'Expert Testimony and the New Rule 702: Strategy and Implications (McGuireWoods '
               'LLP)',
      'url': 'https://www.youtube.com/watch?v=tBtb3Kmq3ZA&t=861s',
      'video_id': 'tBtb3Kmq3ZA'},
     {'author': 'TownCenter Partners Litigation Finance',
      'channel': 'TownCenter Partners Litigation Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=Bb96l6seoxI&t=108s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'This new competitive challenge but overall this development is good for clients '
              'and for the justice system as a whole if you need help with litigation funding '
              'call me at seven oh three five seven oh five two six four or email me at Roni '
              'at your TCP com.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': 'This new competitive challenge but overall this development is good for clients '
             'and for the justice system as a whole if you need help with litigation funding '
             'call me at seven oh three five seven oh five two six four or email me at Roni at '
             'your TCP com.',
      'title': 'Litigation finance Changes the Law Firm Landscape (TownCenter Partners '
               'Litigation Finance)',
      'url': 'https://www.youtube.com/watch?v=Bb96l6seoxI&t=108s',
      'video_id': 'Bb96l6seoxI'},
     {'author': 'Alt Funds Network',
      'channel': 'Alt Funds Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:21](https://www.youtube.com/watch?v=FQLjhMdShl0&t=741s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Call it as a litigation finance company if I'm able to charge 15 for my client "
              "maybe I'm able to pass along 12 at a bottom line or whatever that may be.",
      'timestamp': 741,
      'timestamp_label': '[00:12:21]',
      'timestamp_seconds': 741,
      'tip': "Call it as a litigation finance company if I'm able to charge 15 for my client "
             "maybe I'm able to pass along 12 at a bottom line or whatever that may be.",
      'title': 'Litigation Finance Demystified: Investment Trends & Future Outlook | Interview '
               'with Sean Campbell (Alt Funds Network)',
      'url': 'https://www.youtube.com/watch?v=FQLjhMdShl0&t=741s',
      'video_id': 'FQLjhMdShl0'},
     {'author': 'Case Works',
      'channel': 'Case Works',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=voWGMGOyvtQ&t=77s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "They always help the clients and this new service they're offering I'm actually "
              'working with them on a new settlement I have so really looking.',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': "They always help the clients and this new service they're offering I'm actually "
             'working with them on a new settlement I have so really looking.',
      'title': 'Huge NEC Verdict, Bellwether Trials Coming for AFFF & Zantac, and CPAP '
               'Settlement Matrix Updates 🙌🏻 (Case Works)',
      'url': 'https://www.youtube.com/watch?v=voWGMGOyvtQ&t=77s',
      'video_id': 'voWGMGOyvtQ'},
     {'author': 'Slarskey LLC',
      'channel': 'Slarskey LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:27](https://www.youtube.com/watch?v=l-KmnCtiBMg&t=687s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Credit um perspective and lender perspective you can certainly look at the '
              'Historical revenue and expenses of the business and you can look at um you.',
      'timestamp': 687,
      'timestamp_label': '[00:11:27]',
      'timestamp_seconds': 687,
      'tip': 'Credit um perspective and lender perspective you can certainly look at the '
             'Historical revenue and expenses of the business and you can look at um you.',
      'title': 'Litigation Funding Pt.1: The Investor Perspective (Slarskey LLC)',
      'url': 'https://www.youtube.com/watch?v=l-KmnCtiBMg&t=687s',
      'video_id': 'l-KmnCtiBMg'},
     {'author': "Legal Lead Sharks Podcast | K'Lee Terrazas",
      'channel': "Legal Lead Sharks Podcast | K'Lee Terrazas",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:32](https://www.youtube.com/watch?v=sehjNBEeVbw&t=212s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I've got some good value here for the viewers and listeners today. So, we we "
              "deal at Legal Lead Sharks, obviously, we work with law firms, right? 're "
              'talking certain niches, especially personal injury, probably the most expensive '
              'niche.',
      'timestamp': 212,
      'timestamp_label': '[00:03:32]',
      'timestamp_seconds': 212,
      'tip': "I've got some good value here for the viewers and listeners today. So, we we "
             "deal at Legal Lead Sharks, obviously, we work with law firms, right? 're talking "
             'certain niches, especially personal injury, probably the most expensive niche.',
      'title': "What Bad Google Ads Agencies Don't Want Lawyers to Know From a 7-Figure Ad "
               "Agency Owner (Legal Lead Sharks Podcast | K'Lee Terrazas)",
      'url': 'https://www.youtube.com/watch?v=sehjNBEeVbw&t=212s',
      'video_id': 'sehjNBEeVbw'},
     {'author': 'Jon and Marc',
      'channel': 'Jon and Marc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=LaXcjMiTQWI&t=20s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'RR Digital stays independent. So, we can optimize around one thing, law firm '
              "growth. That means cases, clients, and revenue. If you're rethinking your "
              'marketing partner, visit rrdigitalmedia.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'RR Digital stays independent. So, we can optimize around one thing, law firm '
             "growth. That means cases, clients, and revenue. If you're rethinking your "
             'marketing partner, visit rrdigitalmedia.',
      'title': '2026 Mass Tort Power Rankings: Who Claimed the #1 Spot? (Jon and Marc)',
      'url': 'https://www.youtube.com/watch?v=LaXcjMiTQWI&t=20s',
      'video_id': 'LaXcjMiTQWI'},
     {'author': 'Miller & Zois, Attorneys at Law',
      'channel': 'Miller & Zois, Attorneys at Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=ZSUxJOy6C54&t=114s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Same we still believe that elmer on cases in the highest settlement tiers will '
              'have a potential value range of three hundred thousand to six hundred thousand '
              'cases in the next tier down could be worth around seventy five thousand to two '
              'hundred and fifty thousand.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': 'Same we still believe that elmer on cases in the highest settlement tiers will '
             'have a potential value range of three hundred thousand to six hundred thousand '
             'cases in the next tier down could be worth around seventy five thousand to two '
             'hundred and fifty thousand.',
      'title': 'Elmiron Lawsuit (Miller & Zois, Attorneys at Law)',
      'url': 'https://www.youtube.com/watch?v=ZSUxJOy6C54&t=114s',
      'video_id': 'ZSUxJOy6C54'}],
 2: [{'author': 'Holt Law: For Healthcare Businesses',
      'channel': 'Holt Law: For Healthcare Businesses',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:44](https://www.youtube.com/watch?v=DNk78wbKy5s&t=224s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s really important not to get MSOs mixed up with something called alternative "
              "business structures or ABS. An ABS, which you'll find in places like Arizona "
              'and Utah, is a formally licensed entity that actually does allow non-awyer '
              'ownership.',
      'timestamp': 224,
      'timestamp_label': '[00:03:44]',
      'timestamp_seconds': 224,
      'tip': "'s really important not to get MSOs mixed up with something called alternative "
             "business structures or ABS. An ABS, which you'll find in places like Arizona and "
             'Utah, is a formally licensed entity that actually does allow non-awyer '
             'ownership.',
      'title': 'Law Firm Growth: Avoiding Management Services Organization ("MSO") Model Fee '
               'Traps (Holt Law: For Healthcare Businesses)',
      'url': 'https://www.youtube.com/watch?v=DNk78wbKy5s&t=224s',
      'video_id': 'DNk78wbKy5s'},
     {'author': 'Nexus Legal Group',
      'channel': 'Nexus Legal Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=4LdL5Q6T7ds&t=45s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Multiply that across hundreds of claims, and you can see why so many firms are '
              'tying up capital and inventory that never pays it back. Nexus Legal Group built '
              'its mass tort and complex litigation case acquisition program to fix that at '
              'the source.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': 'Multiply that across hundreds of claims, and you can see why so many firms are '
             'tying up capital and inventory that never pays it back. Nexus Legal Group built '
             'its mass tort and complex litigation case acquisition program to fix that at the '
             'source.',
      'title': "Signed Isn't Settlement Ready Building Mass Tort Inventory That Holds Up "
               '(Nexus Legal Group)',
      'url': 'https://www.youtube.com/watch?v=4LdL5Q6T7ds&t=45s',
      'video_id': '4LdL5Q6T7ds'},
     {'author': 'Mattern LLC',
      'channel': 'Mattern LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:07](https://www.youtube.com/watch?v=8wwcTCIWOXM&t=367s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'MSO is going to be providing all of the administrative resources and '
              'intellectual property necessary for the practice to function. In exchange for '
              'that, the law firm is going to pay to the MSO a monthly service fee.',
      'timestamp': 367,
      'timestamp_label': '[00:06:07]',
      'timestamp_seconds': 367,
      'tip': 'MSO is going to be providing all of the administrative resources and '
             'intellectual property necessary for the practice to function. In exchange for '
             'that, the law firm is going to pay to the MSO a monthly service fee.',
      'title': 'Law Firm MSOs 101: How Private Equity and Managed Services Drive Legal Growth '
               '(Mattern LLC)',
      'url': 'https://www.youtube.com/watch?v=8wwcTCIWOXM&t=367s',
      'video_id': '8wwcTCIWOXM'},
     {'author': 'Dolman Law Group',
      'channel': 'Dolman Law Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:44:17](https://www.youtube.com/watch?v=g66VtR5b5gQ&t=2657s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'t this isn't groups of firms that are just out there looking to settle a case "
              'to to cash a check on their fees. These are firms that rather go to trial '
              'because they know they could get a better decision.',
      'timestamp': 2657,
      'timestamp_label': '[00:44:17]',
      'timestamp_seconds': 2657,
      'tip': "'t this isn't groups of firms that are just out there looking to settle a case "
             'to to cash a check on their fees. These are firms that rather go to trial '
             'because they know they could get a better decision.',
      'title': 'Lawyers Explain Litigation Finance | How Lawsuit Funding Levels the Playing '
               'Field in PI Cases (Dolman Law Group)',
      'url': 'https://www.youtube.com/watch?v=g66VtR5b5gQ&t=2657s',
      'video_id': 'g66VtR5b5gQ'},
     {'author': 'Drugwatch',
      'channel': 'Drugwatch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:52](https://www.youtube.com/watch?v=y_Jf3JpGO8Y&t=172s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'These attorneys typically work on a contingency basis. That means you usually '
              'pay nothing unless you win your case. However, you may have to pay certain fees '
              "such as court costs. It's important to ask the attorney about any out-of-pocket "
              'costs.',
      'timestamp': 172,
      'timestamp_label': '[00:02:52]',
      'timestamp_seconds': 172,
      'tip': 'These attorneys typically work on a contingency basis. That means you usually '
             'pay nothing unless you win your case. However, you may have to pay certain fees '
             "such as court costs. It's important to ask the attorney about any out-of-pocket "
             'costs.',
      'title': 'Hernia Mesh Lawsuit 2026 Update | How to File a Hernia Mesh Lawsuit '
               '(Drugwatch)',
      'url': 'https://www.youtube.com/watch?v=y_Jf3JpGO8Y&t=172s',
      'video_id': 'y_Jf3JpGO8Y'},
     {'author': 'Certum Group',
      'channel': 'Certum Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:28](https://www.youtube.com/watch?v=-8_noUd4xgs&t=928s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And all of those expenses are incurred long before any clients ever see a '
              'recovery. So the way that we the way that our firm works, we have a contingency '
              "fee arrangement. Clients don't pay attorney fees upfront.",
      'timestamp': 928,
      'timestamp_label': '[00:15:28]',
      'timestamp_seconds': 928,
      'tip': 'And all of those expenses are incurred long before any clients ever see a '
             'recovery. So the way that we the way that our firm works, we have a contingency '
             "fee arrangement. Clients don't pay attorney fees upfront.",
      'title': 'Inside Mass Torts with Lacey Lewis from Trial Lawyers United (Certum Group)',
      'url': 'https://www.youtube.com/watch?v=-8_noUd4xgs&t=928s',
      'video_id': '-8_noUd4xgs'},
     {'author': 'The Federalist Society',
      'channel': 'The Federalist Society',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:45:07](https://www.youtube.com/watch?v=LVcpWtomEvU&t=2707s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You can't just pay the uh your fee and and get yourself a judge and uh you're "
              "in business. Um I think uh Professor McGovern was here earlier. I don't know "
              "whether he's still here, but he has a a phrase that he calls it uh if you if "
              'you build it, they will come.',
      'timestamp': 2707,
      'timestamp_label': '[00:45:07]',
      'timestamp_seconds': 2707,
      'tip': "You can't just pay the uh your fee and and get yourself a judge and uh you're in "
             "business. Um I think uh Professor McGovern was here earlier. I don't know "
             "whether he's still here, but he has a a phrase that he calls it uh if you if you "
             'build it, they will come.',
      'title': 'Eliminating Meritless Claims [Multidistrict Litigation (MDL) Conference] (The '
               'Federalist Society)',
      'url': 'https://www.youtube.com/watch?v=LVcpWtomEvU&t=2707s',
      'video_id': 'LVcpWtomEvU'},
     {'author': 'Cut to the Chase Network',
      'channel': 'Cut to the Chase Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:05](https://www.youtube.com/watch?v=JlBWnsNpbyc&t=605s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Bard claimants, but it pays out over the next 2 years. So, that that's the "
              'number one by market share. Very close behind that is Medtronic Covidien. So, '
              "that's the case I just tried.",
      'timestamp': 605,
      'timestamp_label': '[00:10:05]',
      'timestamp_seconds': 605,
      'tip': "Bard claimants, but it pays out over the next 2 years. So, that that's the "
             'number one by market share. Very close behind that is Medtronic Covidien. So, '
             "that's the case I just tried.",
      'title': 'Hernia Mesh Lawsuit Update: Covidien Verdict, Bard Settlement, and What Comes '
               "Next | Timothy O'Brien (Cut to the Chase Network)",
      'url': 'https://www.youtube.com/watch?v=JlBWnsNpbyc&t=605s',
      'video_id': 'JlBWnsNpbyc'},
     {'author': 'Sara Shikhman, Esq.',
      'channel': 'Sara Shikhman, Esq.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:51](https://www.youtube.com/watch?v=JadIHn9B3vk&t=231s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And it also details the management fee that is paid to the MSO. And the '
              'management fee is a way for the MSO owner to get some of the revenues of the '
              'medical spa entity. And speaking of fees, what kind of fees typically paid to '
              'the professional entity or the doctor?',
      'timestamp': 231,
      'timestamp_label': '[00:03:51]',
      'timestamp_seconds': 231,
      'tip': 'And it also details the management fee that is paid to the MSO. And the '
             'management fee is a way for the MSO owner to get some of the revenues of the '
             'medical spa entity. And speaking of fees, what kind of fees typically paid to '
             'the professional entity or the doctor?',
      'title': 'What is an MSO (Management Services Organization)? (Sara Shikhman, Esq.)',
      'url': 'https://www.youtube.com/watch?v=JadIHn9B3vk&t=231s',
      'video_id': 'JadIHn9B3vk'},
     {'author': 'Answering Legal, Inc.',
      'channel': 'Answering Legal, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=_OyhC_G4cFw&t=70s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Gina made sure to politely ask all of the information regarding Alyssa's case "
              'and will now try to reach Tom lawyer she will let him know who is calling the '
              'details of the case and will ask him if he would like to take the call this is '
              'Tom lawyer hi mr.',
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': "Gina made sure to politely ask all of the information regarding Alyssa's case "
             'and will now try to reach Tom lawyer she will let him know who is calling the '
             'details of the case and will ask him if he would like to take the call this is '
             'Tom lawyer hi mr.',
      'title': 'Legal Intake Receptionist - Attorney Not Able to Take the Call (Answering '
               'Legal, Inc.)',
      'url': 'https://www.youtube.com/watch?v=_OyhC_G4cFw&t=70s',
      'video_id': '_OyhC_G4cFw'},
     {'author': 'Michael Stanisci',
      'channel': 'Michael Stanisci',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:23](https://www.youtube.com/watch?v=_qBek9AFPiI&t=23s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So there's not going to be any payments to the plaintiffs in 26, none in 27. "
              "Generally, my rule of thumb is in a mass tort settlement, you won't receive a a "
              'payment, actual funds, until at least a year and a half from the time of the '
              'settlement.',
      'timestamp': 23,
      'timestamp_label': '[00:00:23]',
      'timestamp_seconds': 23,
      'tip': "So there's not going to be any payments to the plaintiffs in 26, none in 27. "
             "Generally, my rule of thumb is in a mass tort settlement, you won't receive a a "
             'payment, actual funds, until at least a year and a half from the time of the '
             'settlement.',
      'title': 'When can I expect my PFAS/AFFF 3M settlement? (Michael Stanisci)',
      'url': 'https://www.youtube.com/watch?v=_qBek9AFPiI&t=23s',
      'video_id': '_qBek9AFPiI'},
     {'author': 'The New York Injury & Malpractice Law Firm, P.C.',
      'channel': 'The New York Injury & Malpractice Law Firm, P.C.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:30](https://www.youtube.com/watch?v=uJITvDxd4jA&t=210s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Because no one does anything about it. Now, another thing that you can do and '
              "what we do in some cases, let's say the hospital is completely stonewalling "
              'you. "And we\'re not going to give you the records. You\'re going to have to '
              'pay $5,000.".',
      'timestamp': 210,
      'timestamp_label': '[00:03:30]',
      'timestamp_seconds': 210,
      'tip': 'Because no one does anything about it. Now, another thing that you can do and '
             "what we do in some cases, let's say the hospital is completely stonewalling you. "
             '"And we\'re not going to give you the records. You\'re going to have to pay '
             '$5,000.".',
      'title': 'Lawyer Secrets to Getting Medical Records FAST (The New York Injury & '
               'Malpractice Law Firm, P.C.)',
      'url': 'https://www.youtube.com/watch?v=uJITvDxd4jA&t=210s',
      'video_id': 'uJITvDxd4jA'},
     {'author': 'Jon and Marc',
      'channel': 'Jon and Marc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:14](https://www.youtube.com/watch?v=ql3WYzhinZk&t=494s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So, obviously our side says no. Every case so far that's been decided "
              "individually, the court let those claims proceed, but we're going to have a "
              'decision here in a probably the early next year, which is going to have a huge '
              'impact on all of these cases.',
      'timestamp': 494,
      'timestamp_label': '[00:08:14]',
      'timestamp_seconds': 494,
      'tip': "So, obviously our side says no. Every case so far that's been decided "
             "individually, the court let those claims proceed, but we're going to have a "
             'decision here in a probably the early next year, which is going to have a huge '
             'impact on all of these cases.',
      'title': 'Year-End Mass Tort Settlement Watch: Hair Relaxer, Camp Lejeune, Uber & '
               'Roundup Updates (Jon and Marc)',
      'url': 'https://www.youtube.com/watch?v=ql3WYzhinZk&t=494s',
      'video_id': 'ql3WYzhinZk'},
     {'author': 'Lawsuit Tracker',
      'channel': 'Lawsuit Tracker',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:53](https://www.youtube.com/watch?v=orLyLTC8fiA&t=113s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re just trying to look for those, surgical reports. So usually medical records "
              "get purged every 7 to 10 years. Sometimes that's not the case. And sometimes "
              'surgical reports are kept a little bit longer.',
      'timestamp': 113,
      'timestamp_label': '[00:01:53]',
      'timestamp_seconds': 113,
      'tip': "'re just trying to look for those, surgical reports. So usually medical records "
             "get purged every 7 to 10 years. Sometimes that's not the case. And sometimes "
             'surgical reports are kept a little bit longer.',
      'title': 'What you need to KNOW about Hernia Mesh Lawsuits (Lawsuit Tracker)',
      'url': 'https://www.youtube.com/watch?v=orLyLTC8fiA&t=113s',
      'video_id': 'orLyLTC8fiA'},
     {'author': 'Jon and Marc',
      'channel': 'Jon and Marc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:10](https://www.youtube.com/watch?v=J0vh1lrcwJk&t=1270s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'It looks like the first bellweather trial is not going to kick off probably '
              'until April or May of next year. So I think you have this six to eightmonth '
              "window to get cases. We'll see what the defendants do here. Again, it's it's "
              'going to be a business decision.',
      'timestamp': 1270,
      'timestamp_label': '[00:21:10]',
      'timestamp_seconds': 1270,
      'tip': 'It looks like the first bellweather trial is not going to kick off probably '
             'until April or May of next year. So I think you have this six to eightmonth '
             "window to get cases. We'll see what the defendants do here. Again, it's it's "
             'going to be a business decision.',
      'title': 'Pre-MTMP Mass Tort Power Rankings: Top 10 Litigations to Watch in 2026 (Jon '
               'and Marc)',
      'url': 'https://www.youtube.com/watch?v=J0vh1lrcwJk&t=1270s',
      'video_id': 'J0vh1lrcwJk'}],
 3: [{'author': 'ResTech Solutions',
      'channel': 'ResTech Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:59](https://www.youtube.com/watch?v=fTOe5KR6QSE&t=479s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '100,000 on this project, but they have that $9. 9 million that they otherwise '
              'would have spent on legal fees across the case to go invest in their business '
              'and and make whatever their profit margin is on on on their usual business.',
      'timestamp': 479,
      'timestamp_label': '[00:07:59]',
      'timestamp_seconds': 479,
      'tip': '100,000 on this project, but they have that $9. 9 million that they otherwise '
             'would have spent on legal fees across the case to go invest in their business '
             'and and make whatever their profit margin is on on on their usual business.',
      'title': 'How Litigation Finance Is Reshaping Law Firms (Capital, Risk & 10X Returns '
               'Explained) (ResTech Solutions)',
      'url': 'https://www.youtube.com/watch?v=fTOe5KR6QSE&t=479s',
      'video_id': 'fTOe5KR6QSE'},
     {'author': 'Kayse AI',
      'channel': 'Kayse AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=kjUaKK45Ahg&t=31s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '>> Without Case, we would be looking at a large call center. We would be using '
              'significantly more human resources. The investment to those human resources.',
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': '>> Without Case, we would be looking at a large call center. We would be using '
             'significantly more human resources. The investment to those human resources.',
      'title': 'Why Aylstock Witkin Kreis & Overholtz, a Top Mass Tort Firm Runs on Kayse | '
               'Maury Goldstein (Kayse AI)',
      'url': 'https://www.youtube.com/watch?v=kjUaKK45Ahg&t=31s',
      'video_id': 'kjUaKK45Ahg'},
     {'author': 'Holt Law: For Healthcare Businesses',
      'channel': 'Holt Law: For Healthcare Businesses',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:06](https://www.youtube.com/watch?v=bXO6V29iXPs&t=426s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And in my mind, I think is a no-brainer for anyone who doesn't have an NBA or "
              "didn't go into building a medical spa to become a business owner and marketer. "
              'So essential for growth, but also maybe case specific.',
      'timestamp': 426,
      'timestamp_label': '[00:07:06]',
      'timestamp_seconds': 426,
      'tip': "And in my mind, I think is a no-brainer for anyone who doesn't have an NBA or "
             "didn't go into building a medical spa to become a business owner and marketer. "
             'So essential for growth, but also maybe case specific.',
      'title': 'How the MSO Model Helps Healthcare Businesses (Holt Law: For Healthcare '
               'Businesses)',
      'url': 'https://www.youtube.com/watch?v=bXO6V29iXPs&t=426s',
      'video_id': 'bXO6V29iXPs'},
     {'author': 'Logan Mayer LLP',
      'channel': 'Logan Mayer LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:24](https://www.youtube.com/watch?v=fMKPM7zg2OI&t=864s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And often times people are talking in terms of what's the cost of defense? Uh "
              "is that a reasonable metric on which to settle a case? Because we're going to "
              'have to spend this money anyway on our own attorneys to get a good result.',
      'timestamp': 864,
      'timestamp_label': '[00:14:24]',
      'timestamp_seconds': 864,
      'tip': "And often times people are talking in terms of what's the cost of defense? Uh is "
             "that a reasonable metric on which to settle a case? Because we're going to have "
             'to spend this money anyway on our own attorneys to get a good result.',
      'title': 'Mass Tort Litigation: How Companies Defend Claims Involving Multiple '
               'Plaintiffs (Logan Mayer LLP)',
      'url': 'https://www.youtube.com/watch?v=fMKPM7zg2OI&t=864s',
      'video_id': 'fMKPM7zg2OI'},
     {'author': 'The Nomberg Law Firm',
      'channel': 'The Nomberg Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:27](https://www.youtube.com/watch?v=_9ZPWIgPW14&t=27s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Well the high tech act was passed several years ago and it's supposed to help "
              'alleviate some of those costs that gives some ground rules and some.',
      'timestamp': 27,
      'timestamp_label': '[00:00:27]',
      'timestamp_seconds': 27,
      'tip': "Well the high tech act was passed several years ago and it's supposed to help "
             'alleviate some of those costs that gives some ground rules and some.',
      'title': 'What is the HITECH Act? (The Nomberg Law Firm)',
      'url': 'https://www.youtube.com/watch?v=_9ZPWIgPW14&t=27s',
      'video_id': '_9ZPWIgPW14'},
     {'author': 'Addleshaw Goddard',
      'channel': 'Addleshaw Goddard',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:41](https://www.youtube.com/watch?v=22mFLcrQrE8&t=101s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So if you get it wrong, if you're unsuccessful in your claim, generally, you "
              "will have to pay a large portion of your opponent's costs, as well. The ability "
              'to shift that cost burden onto a litigation funder is really important in the '
              'context of a class action.',
      'timestamp': 101,
      'timestamp_label': '[00:01:41]',
      'timestamp_seconds': 101,
      'tip': "So if you get it wrong, if you're unsuccessful in your claim, generally, you "
             "will have to pay a large portion of your opponent's costs, as well. The ability "
             'to shift that cost burden onto a litigation funder is really important in the '
             'context of a class action.',
      'title': 'Litigation Finance - The class action perspective (Addleshaw Goddard)',
      'url': 'https://www.youtube.com/watch?v=22mFLcrQrE8&t=101s',
      'video_id': '22mFLcrQrE8'},
     {'author': 'Bill Hauser with SMB Team',
      'channel': 'Bill Hauser with SMB Team',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:43](https://www.youtube.com/watch?v=mr9VmqdCZ6M&t=223s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'National all of the united states campaign your cost-per-click is going to be '
              "low you're probably going to be one of the only people advertising for it let's "
              "see Gordon folding knives lawsuit let's see if there's any people bidding on "
              'this keyword.',
      'timestamp': 223,
      'timestamp_label': '[00:03:43]',
      'timestamp_seconds': 223,
      'tip': 'National all of the united states campaign your cost-per-click is going to be '
             "low you're probably going to be one of the only people advertising for it let's "
             "see Gordon folding knives lawsuit let's see if there's any people bidding on "
             'this keyword.',
      'title': 'Mass Tort Marketing | How To Use The CPSC to Get Product Liability & Mass Tort '
               'Cases Online (Bill Hauser with SMB Team)',
      'url': 'https://www.youtube.com/watch?v=mr9VmqdCZ6M&t=223s',
      'video_id': 'mr9VmqdCZ6M'},
     {'author': 'Oregon Law Lab',
      'channel': 'Oregon Law Lab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:40](https://www.youtube.com/watch?v=TyGsfcYU1dw&t=520s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'There that do but the big ones the ones that are staying in business the ones '
              'that are have been around for multiple years they are not looking for the uh '
              "case right they're looking for something that more likely than not they think "
              'is going to win.',
      'timestamp': 520,
      'timestamp_label': '[00:08:40]',
      'timestamp_seconds': 520,
      'tip': 'There that do but the big ones the ones that are staying in business the ones '
             'that are have been around for multiple years they are not looking for the uh '
             "case right they're looking for something that more likely than not they think is "
             'going to win.',
      'title': '9 Questions about 3rd Party Litigation Funding in 9 Minutes | Oregon Law Lab '
               '(Oregon Law Lab)',
      'url': 'https://www.youtube.com/watch?v=TyGsfcYU1dw&t=520s',
      'video_id': 'TyGsfcYU1dw'},
     {'author': 'Bloomberg Law',
      'channel': 'Bloomberg Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:09](https://www.youtube.com/watch?v=zyULl2H1mh8&t=129s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Cost only bearers of bad news and big costs to instead having them go into '
              "client's offices and create value deliver a financial solution that the client "
              "possibly hadn't thought of before even if that Financial solution doesn't "
              'involve paying the legal.',
      'timestamp': 129,
      'timestamp_label': '[00:02:09]',
      'timestamp_seconds': 129,
      'tip': 'Cost only bearers of bad news and big costs to instead having them go into '
             "client's offices and create value deliver a financial solution that the client "
             "possibly hadn't thought of before even if that Financial solution doesn't "
             'involve paying the legal.',
      'title': 'Litigation Finance Explained, Part 1 (Bloomberg Law)',
      'url': 'https://www.youtube.com/watch?v=zyULl2H1mh8&t=129s',
      'video_id': 'zyULl2H1mh8'},
     {'author': 'Jon and Marc',
      'channel': 'Jon and Marc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:28](https://www.youtube.com/watch?v=YItGL_4J9i4&t=448s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I would say now is is a decent time for you to evaluate getting involved before '
              'it gets too tough to really get a good case in at a decent price. Coming in at '
              'number five, we have weight loss drugs. So, this is moving up one spot in the '
              'rankings to number five.',
      'timestamp': 448,
      'timestamp_label': '[00:07:28]',
      'timestamp_seconds': 448,
      'tip': 'I would say now is is a decent time for you to evaluate getting involved before '
             'it gets too tough to really get a good case in at a decent price. Coming in at '
             'number five, we have weight loss drugs. So, this is moving up one spot in the '
             'rankings to number five.',
      'title': 'The August 2026 Mass Tort Power Rankings: What to Acquire, What to Watch, and '
               'What Is Settling (Jon and Marc)',
      'url': 'https://www.youtube.com/watch?v=YItGL_4J9i4&t=448s',
      'video_id': 'YItGL_4J9i4'},
     {'author': 'Ron Lasorsa',
      'channel': 'Ron Lasorsa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=mmpH5piuvUk&t=91s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You how much it costs to generate that lead so if you haven't been able to "
              'answer yes to those three questions I just asked you need to have a '
              'conversation with me please contact me at local magnet calls.com thank you for '
              'your time.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': "You how much it costs to generate that lead so if you haven't been able to "
             'answer yes to those three questions I just asked you need to have a conversation '
             'with me please contact me at local magnet calls.com thank you for your time.',
      'title': 'Local Magnet Mass Tort Lead Generation Services (Ron Lasorsa)',
      'url': 'https://www.youtube.com/watch?v=mmpH5piuvUk&t=91s',
      'video_id': 'mmpH5piuvUk'},
     {'author': 'Tesorb',
      'channel': 'Tesorb',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:45](https://www.youtube.com/watch?v=lhOaUXVR9JY&t=165s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Among other things. On September 28th, a federal judge in California refused to '
              "move one of those cases to  Texas as SpaceX's AI unit had asked. The judge.",
      'timestamp': 165,
      'timestamp_label': '[00:02:45]',
      'timestamp_seconds': 165,
      'tip': 'Among other things. On September 28th, a federal judge in California refused to '
             "move one of those cases to  Texas as SpaceX's AI unit had asked. The judge.",
      'title': "Grok's Image Lawsuits Explained: 13 Cases and One Panel Hearing on Dec. 3 "
               '(Tesorb)',
      'url': 'https://www.youtube.com/watch?v=lhOaUXVR9JY&t=165s',
      'video_id': 'lhOaUXVR9JY'},
     {'author': 'Bloomberg Television',
      'channel': 'Bloomberg Television',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:27](https://www.youtube.com/watch?v=dg6Bt8bmJmQ&t=447s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Number of unnecessary cases with without Merit um without a clear injury for '
              'the plaintiffs their lawyers and their funders Justice is a verdict in their '
              'favor or a settlement a cash settlement.',
      'timestamp': 447,
      'timestamp_label': '[00:07:27]',
      'timestamp_seconds': 447,
      'tip': 'Number of unnecessary cases with without Merit um without a clear injury for the '
             'plaintiffs their lawyers and their funders Justice is a verdict in their favor '
             'or a settlement a cash settlement.',
      'title': 'Billion Dollar Lawsuits: When Litigation Finance Met Mass Torts (Bloomberg '
               'Television)',
      'url': 'https://www.youtube.com/watch?v=dg6Bt8bmJmQ&t=447s',
      'video_id': 'dg6Bt8bmJmQ'},
     {'author': 'TownCenter Partners Litigation Finance',
      'channel': 'TownCenter Partners Litigation Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:01](https://www.youtube.com/watch?v=1Xs5nnkcuL4&t=121s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Agreement since money is only paid back if there is a favorable outcome there '
              'for litigation financing can be a good option for a lot of different people and '
              'for many different types of claims if you need help with litigation finance '
              'call or email me today.',
      'timestamp': 121,
      'timestamp_label': '[00:02:01]',
      'timestamp_seconds': 121,
      'tip': 'Agreement since money is only paid back if there is a favorable outcome there '
             'for litigation financing can be a good option for a lot of different people and '
             'for many different types of claims if you need help with litigation finance call '
             'or email me today.',
      'title': 'Types of Litigation Finance Cases (TownCenter Partners Litigation Finance)',
      'url': 'https://www.youtube.com/watch?v=1Xs5nnkcuL4&t=121s',
      'video_id': '1Xs5nnkcuL4'},
     {'author': 'Slarskey LLC',
      'channel': 'Slarskey LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:31](https://www.youtube.com/watch?v=gdDT2WSKYs0&t=1231s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Would have saved everything so there's nothing I can do about it and like you "
              "know so it's sort of like stuff like that sort of the inside baseball uh is "
              'really kind of what I offer.',
      'timestamp': 1231,
      'timestamp_label': '[00:20:31]',
      'timestamp_seconds': 1231,
      'tip': "Would have saved everything so there's nothing I can do about it and like you "
             "know so it's sort of like stuff like that sort of the inside baseball uh is "
             'really kind of what I offer.',
      'title': 'Hot Topics in Litigation Funding Pt.1: A Conversation with Evan Fried and Ted '
               'Farrell on Mass Torts (Slarskey LLC)',
      'url': 'https://www.youtube.com/watch?v=gdDT2WSKYs0&t=1231s',
      'video_id': 'gdDT2WSKYs0'}],
 4: [{'author': 'Law Leaders',
      'channel': 'Law Leaders',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=Tvn12qG9i5s&t=15s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Joining me today to talk about updates to Arizona's alternative business "
              'structure and referral fee reforms is Linda Shey of the Sheely Law Firm Linda.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Joining me today to talk about updates to Arizona's alternative business "
             'structure and referral fee reforms is Linda Shey of the Sheely Law Firm Linda.',
      'title': "Arizona's Alternative Business Structure (ABS): 3 Year Update & What We Have "
               'Learned So Far... (Law Leaders)',
      'url': 'https://www.youtube.com/watch?v=Tvn12qG9i5s&t=15s',
      'video_id': 'Tvn12qG9i5s'},
     {'author': 'Mohr Marketing',
      'channel': 'Mohr Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=agO8HeUx95E&t=59s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'This shifts the burden entirely to your intake and acquisition strategy. Right '
              'now, the only barred cases worth your acquisition budget are what we call tier '
              '1 late discovery claims.',
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': 'This shifts the burden entirely to your intake and acquisition strategy. Right '
             'now, the only barred cases worth your acquisition budget are what we call tier 1 '
             'late discovery claims.',
      'title': 'The Sign and Hold era for Bard Hernia Mesh is over  Here is the new playbook '
               'for 2026 (Mohr Marketing)',
      'url': 'https://www.youtube.com/watch?v=agO8HeUx95E&t=59s',
      'video_id': 'agO8HeUx95E'},
     {'author': 'lawofmedicine',
      'channel': 'lawofmedicine',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:54](https://www.youtube.com/watch?v=n3wWlYBSpfg&t=174s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Number three, business associate agreements. Previously, business associates '
              'were required to comply with HIPPA related privacy laws through a contract with '
              'a covered entity, but they were not responsible for HIPPA compliance.',
      'timestamp': 174,
      'timestamp_label': '[00:02:54]',
      'timestamp_seconds': 174,
      'tip': 'Number three, business associate agreements. Previously, business associates '
             'were required to comply with HIPPA related privacy laws through a contract with '
             'a covered entity, but they were not responsible for HIPPA compliance.',
      'title': 'HITECH ACT - 2010 Changes in HIPAA Law (lawofmedicine)',
      'url': 'https://www.youtube.com/watch?v=n3wWlYBSpfg&t=174s',
      'video_id': 'n3wWlYBSpfg'},
     {'author': 'Filevine',
      'channel': 'Filevine',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=TxRqadYVM2E&t=108s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Filevine is a legal work platform like you've never seen. Other software makes "
              'you work their way. With FileVine, you can customize the whole system to work '
              'your way. Set up custom phases to track the status of every case and '
              'automatically assign certain tasks to your team.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': "Filevine is a legal work platform like you've never seen. Other software makes "
             'you work their way. With FileVine, you can customize the whole system to work '
             'your way. Set up custom phases to track the status of every case and '
             'automatically assign certain tasks to your team.',
      'title': 'Your Complete Legal Tech Stack | Filevine (Filevine)',
      'url': 'https://www.youtube.com/watch?v=TxRqadYVM2E&t=108s',
      'video_id': 'TxRqadYVM2E'},
     {'author': 'The Heart of Law Podcast',
      'channel': 'The Heart of Law Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:53](https://www.youtube.com/watch?v=poe1CAsUc4U&t=1793s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'They want to partner with a lawyer in Arizona is it the entity or is it an '
              'individual a hedge fund that typically goes on the application yes.',
      'timestamp': 1793,
      'timestamp_label': '[00:29:53]',
      'timestamp_seconds': 1793,
      'tip': 'They want to partner with a lawyer in Arizona is it the entity or is it an '
             'individual a hedge fund that typically goes on the application yes.',
      'title': 'Navigating the Arizona ABS Program: Rule Changes and Rising Opportunities (The '
               'Heart of Law Podcast)',
      'url': 'https://www.youtube.com/watch?v=poe1CAsUc4U&t=1793s',
      'video_id': 'poe1CAsUc4U'},
     {'author': 'Infodash',
      'channel': 'Infodash',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:33](https://www.youtube.com/watch?v=_P68fUIZN48&t=513s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "MSO you can't own a law firm. And that's the big difference between the two. Um "
              'as time went on, the investors who like to move really quickly realized that '
              "ABS has a lot of regulatory oversight. It's not easy to get a license. There's "
              'a lot of uh scrutiny.',
      'timestamp': 513,
      'timestamp_label': '[00:08:33]',
      'timestamp_seconds': 513,
      'tip': "MSO you can't own a law firm. And that's the big difference between the two. Um "
             'as time went on, the investors who like to move really quickly realized that ABS '
             "has a lot of regulatory oversight. It's not easy to get a license. There's a lot "
             'of uh scrutiny.',
      'title': 'Episode 138: Traditional Law Firm Ownership Is Becoming a Competitive '
               'Disadvantage with Andy Kvesic (Infodash)',
      'url': 'https://www.youtube.com/watch?v=_P68fUIZN48&t=513s',
      'video_id': '_P68fUIZN48'},
     {'author': 'Moore Injury Funding',
      'channel': 'Moore Injury Funding',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:42](https://www.youtube.com/watch?v=hZFw0Dvtfuk&t=1122s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Justice Department, because the Justice Department is getting involved in this. '
              'Um you know, the False Claims Act, you have many uh insurance companies that '
              'are now filing RICO claims against uh personal injury law firms for staged uh '
              'personal injury um claims.',
      'timestamp': 1122,
      'timestamp_label': '[00:18:42]',
      'timestamp_seconds': 1122,
      'tip': 'Justice Department, because the Justice Department is getting involved in this. '
             'Um you know, the False Claims Act, you have many uh insurance companies that are '
             'now filing RICO claims against uh personal injury law firms for staged uh '
             'personal injury um claims.',
      'title': 'Volume Over Verification: The Hidden Economics of Mass-Tort Litigation - Ron '
               'Lasorsa - S8, Ep.#4 (Moore Injury Funding)',
      'url': 'https://www.youtube.com/watch?v=hZFw0Dvtfuk&t=1122s',
      'video_id': 'hZFw0Dvtfuk'},
     {'author': 'Answering Legal, Inc.',
      'channel': 'Answering Legal, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=B8jUBO9DY0k&t=88s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Hold on one moment please Jana got all the pertinent information regarding '
              "Tiffany's case and is now going to try and reach Tom lawyer she will let him "
              'know who is calling and what they are calling about so that Tom can decide if '
              "he wants to take the call let's watch.",
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'Hold on one moment please Jana got all the pertinent information regarding '
             "Tiffany's case and is now going to try and reach Tom lawyer she will let him "
             'know who is calling and what they are calling about so that Tom can decide if he '
             "wants to take the call let's watch.",
      'title': 'Legal Intake Receptionist Call Patching (Answering Legal, Inc.)',
      'url': 'https://www.youtube.com/watch?v=B8jUBO9DY0k&t=88s',
      'video_id': 'B8jUBO9DY0k'},
     {'author': 'TownCenter Partners Litigation Finance',
      'channel': 'TownCenter Partners Litigation Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:11](https://www.youtube.com/watch?v=5XWpCPDxugc&t=131s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'When a funder does decide to invest the amount of the investment is often '
              'limited typically funders offer claim holders about 10 percent of the expected '
              'recovery although that percentage may vary depending upon the size of the '
              'litigation budget for the case.',
      'timestamp': 131,
      'timestamp_label': '[00:02:11]',
      'timestamp_seconds': 131,
      'tip': 'When a funder does decide to invest the amount of the investment is often '
             'limited typically funders offer claim holders about 10 percent of the expected '
             'recovery although that percentage may vary depending upon the size of the '
             'litigation budget for the case.',
      'title': 'Understanding Litigation Finance Underwriting, Part I (TownCenter Partners '
               'Litigation Finance)',
      'url': 'https://www.youtube.com/watch?v=5XWpCPDxugc&t=131s',
      'video_id': '5XWpCPDxugc'},
     {'author': 'Jon and Marc',
      'channel': 'Jon and Marc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:51](https://www.youtube.com/watch?v=P4L_OgCBmDc&t=591s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, again, this case is focusing on the infection, which was the initial '
              "bellwether trial which resulted in the hung jury. So, we're going to see if we "
              'can win this one, but the judge is doing what we love to see. The the next '
              'bellwethers are stacked.',
      'timestamp': 591,
      'timestamp_label': '[00:09:51]',
      'timestamp_seconds': 591,
      'tip': 'So, again, this case is focusing on the infection, which was the initial '
             "bellwether trial which resulted in the hung jury. So, we're going to see if we "
             'can win this one, but the judge is doing what we love to see. The the next '
             'bellwethers are stacked.',
      'title': 'Camp Lejeune Bellwethers Kick Off, Meta Drops Out, & Bard PowerPort Surges '
               '(Jon and Marc)',
      'url': 'https://www.youtube.com/watch?v=P4L_OgCBmDc&t=591s',
      'video_id': 'P4L_OgCBmDc'},
     {'author': 'The Heart of Law Podcast',
      'channel': 'The Heart of Law Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:32:00](https://www.youtube.com/watch?v=Zz1HlCrfQPY&t=1920s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I think um is why Rocade and and seasoned capital sources understand and don't "
              'hold it against them. They kind of get all of that in order because you '
              'understand these are not business people. These are attorneys and attorneys '
              "didn't go to law school to run a business.",
      'timestamp': 1920,
      'timestamp_label': '[00:32:00]',
      'timestamp_seconds': 1920,
      'tip': "I think um is why Rocade and and seasoned capital sources understand and don't "
             'hold it against them. They kind of get all of that in order because you '
             'understand these are not business people. These are attorneys and attorneys '
             "didn't go to law school to run a business.",
      'title': 'Funding the Fight: Inside Litigation Funding with Rocade Capital (The Heart of '
               'Law Podcast)',
      'url': 'https://www.youtube.com/watch?v=Zz1HlCrfQPY&t=1920s',
      'video_id': 'Zz1HlCrfQPY'},
     {'author': 'Justinian & Associates PLLC',
      'channel': 'Justinian & Associates PLLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=_YA0HVm1udc&t=90s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And unreasonable conduct and in a typical personal injury lawsuit negligence is '
              'the principal claim that is raised but in a pharmaceutical case.',
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': 'And unreasonable conduct and in a typical personal injury lawsuit negligence is '
             'the principal claim that is raised but in a pharmaceutical case.',
      'title': 'Mass Tort Law - Pharmaceuticals Pt. 1 - Strict Liability vs. Negligence - '
               'Whiteboard Series (Justinian & Associates PLLC)',
      'url': 'https://www.youtube.com/watch?v=_YA0HVm1udc&t=90s',
      'video_id': '_YA0HVm1udc'},
     {'author': 'Nigh Goldenberg Raso & Vaughn PLLC',
      'channel': 'Nigh Goldenberg Raso & Vaughn PLLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=AxtNAnlfdLI&t=20s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So if that if that's in federal court, it's the process that we call "
              "multi-district litigation where there'll be a filing for that to occur. The "
              'cases then get consolidated.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "So if that if that's in federal court, it's the process that we call "
             "multi-district litigation where there'll be a filing for that to occur. The "
             'cases then get consolidated.',
      'title': 'What Are the Stages of a Lawsuit in an MDL? Part 1 (Explained for Clients) '
               '(Nigh Goldenberg Raso & Vaughn PLLC)',
      'url': 'https://www.youtube.com/watch?v=AxtNAnlfdLI&t=20s',
      'video_id': 'AxtNAnlfdLI'},
     {'author': 'Case Works',
      'channel': 'Case Works',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:17](https://www.youtube.com/watch?v=AVLtP9ONXaY&t=977s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Defendants what is a compensable case and with the court's help we would figure "
              'this all out together okay now.',
      'timestamp': 977,
      'timestamp_label': '[00:16:17]',
      'timestamp_seconds': 977,
      'tip': "Defendants what is a compensable case and with the court's help we would figure "
             'this all out together okay now.',
      'title': 'Tips to Successfully Handling a High Volume of Mass Tort Cases W/ Bill '
               'Barfield (Case Works)',
      'url': 'https://www.youtube.com/watch?v=AVLtP9ONXaY&t=977s',
      'video_id': 'AVLtP9ONXaY'},
     {'author': 'The New York Injury & Malpractice Law Firm, P.C.',
      'channel': 'The New York Injury & Malpractice Law Firm, P.C.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:37](https://www.youtube.com/watch?v=JdDeicrkI-o&t=277s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "A little bill that goes right next to the subscription click that and you'll "
              'get notified every single time I do a video and I do these videos for lawyers '
              "once a day I'll see you tomorrow thanks bye bye.",
      'timestamp': 277,
      'timestamp_label': '[00:04:37]',
      'timestamp_seconds': 277,
      'tip': "A little bill that goes right next to the subscription click that and you'll get "
             'notified every single time I do a video and I do these videos for lawyers once a '
             "day I'll see you tomorrow thanks bye bye.",
      'title': 'How to get Medical Records at (almost) No Expense (The New York Injury & '
               'Malpractice Law Firm, P.C.)',
      'url': 'https://www.youtube.com/watch?v=JdDeicrkI-o&t=277s',
      'video_id': 'JdDeicrkI-o'}],
 5: [{'author': 'Denton Peterson Dunn, PLLC',
      'channel': 'Denton Peterson Dunn, PLLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:44](https://www.youtube.com/watch?v=5NeidO5OU60&t=44s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The State Bar of Arizona is especially concerned that attorneys could be '
              'pressured to make decisions that could compromise their professional judgment. '
              "It's really important that ABS's follow a core principle of attorney "
              'independence to avoid ethical violations.',
      'timestamp': 44,
      'timestamp_label': '[00:00:44]',
      'timestamp_seconds': 44,
      'tip': 'The State Bar of Arizona is especially concerned that attorneys could be '
             'pressured to make decisions that could compromise their professional judgment. '
             "It's really important that ABS's follow a core principle of attorney "
             'independence to avoid ethical violations.',
      'title': '5 Major Risks Facing Arizona ABS Law Firms And How to Manage Them | Denton '
               'Peterson Dunn (Denton Peterson Dunn, PLLC)',
      'url': 'https://www.youtube.com/watch?v=5NeidO5OU60&t=44s',
      'video_id': '5NeidO5OU60'},
     {'author': 'LexHive Podcast (Formerly- The Legal Growth Lab)',
      'channel': 'LexHive Podcast (Formerly- The Legal Growth Lab)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:11](https://www.youtube.com/watch?v=Ytmnnu5SPIg&t=191s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Dolbert hearing and and we end up winning and our experts go through, that's "
              'really where the the risk is minimal. Um there still have to prove the specific '
              'causation. Each case is going to be different, but generally we know this '
              'theory sound.',
      'timestamp': 191,
      'timestamp_label': '[00:03:11]',
      'timestamp_seconds': 191,
      'tip': "Dolbert hearing and and we end up winning and our experts go through, that's "
             'really where the the risk is minimal. Um there still have to prove the specific '
             'causation. Each case is going to be different, but generally we know this theory '
             'sound.',
      'title': 'Why does timing matter more than case strength in mass tort underwriting? Joe '
               'Fantini explains. \n'
               'You (LexHive Podcast (Formerly- The Legal Growth Lab))',
      'url': 'https://www.youtube.com/watch?v=Ytmnnu5SPIg&t=191s',
      'video_id': 'Ytmnnu5SPIg'},
     {'author': 'Nigh Goldenberg Raso & Vaughn PLLC',
      'channel': 'Nigh Goldenberg Raso & Vaughn PLLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=b_t0BzdDfl8&t=92s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Had I known that there was a there was a this problem with this drug, I either '
              'would not have prescribed it or I would have made sure that as part of my '
              'consultation with my patient, I would have made sure that they knew about the '
              'risk and benefits of this drug.',
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': 'Had I known that there was a there was a this problem with this drug, I either '
             'would not have prescribed it or I would have made sure that as part of my '
             'consultation with my patient, I would have made sure that they knew about the '
             'risk and benefits of this drug.',
      'title': 'What Are the Stages of a Lawsuit in an MDL? Part 2 (Bellwethers) (Nigh '
               'Goldenberg Raso & Vaughn PLLC)',
      'url': 'https://www.youtube.com/watch?v=b_t0BzdDfl8&t=92s',
      'video_id': 'b_t0BzdDfl8'},
     {'author': 'Ray Klingenberg',
      'channel': 'Ray Klingenberg',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:48](https://www.youtube.com/watch?v=cyaL9riQdMA&t=48s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Utah has implemented a seven-year regulatory sandbox pilot program Ram to '
              'experiment with alternative business structures California Michigan North '
              'Carolina and Washington D.',
      'timestamp': 48,
      'timestamp_label': '[00:00:48]',
      'timestamp_seconds': 48,
      'tip': 'Utah has implemented a seven-year regulatory sandbox pilot program Ram to '
             'experiment with alternative business structures California Michigan North '
             'Carolina and Washington D.',
      'title': 'Non-lawyer ownership of law firms – law firm marketing (Ray Klingenberg)',
      'url': 'https://www.youtube.com/watch?v=cyaL9riQdMA&t=48s',
      'video_id': 'cyaL9riQdMA'},
     {'author': 'Bloomberg Law',
      'channel': 'Bloomberg Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=z3Bd4lWO460&t=59s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Worth money but there's risk the case is only worth money if you win in court "
              'so if you lose the investment firm is out all their money now having anyone '
              'other.',
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': "Worth money but there's risk the case is only worth money if you win in court so "
             'if you lose the investment firm is out all their money now having anyone other.',
      'title': 'Making Millions Off Other People’s Lawsuits: How Litigation Finance Works '
               '(Bloomberg Law)',
      'url': 'https://www.youtube.com/watch?v=z3Bd4lWO460&t=59s',
      'video_id': 'z3Bd4lWO460'},
     {'author': 'Global Economic Press',
      'channel': 'Global Economic Press',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=t8pdtQfiTLM&t=126s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The defendants moved the case to federal court, where it was consolidated with '
              'other implanted port catheter cases in multi-district litigation number 381, '
              'assigned to Judge David G. Campbell in the United States District Court for the '
              'District of Arizona.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': 'The defendants moved the case to federal court, where it was consolidated with '
             'other implanted port catheter cases in multi-district litigation number 381, '
             'assigned to Judge David G. Campbell in the United States District Court for the '
             'District of Arizona.',
      'title': 'Jury Awards $40 Million to Plaintiff in Bellwether Verdict in Bard Implanted '
               'Port Catheter MDL (Global Economic Press)',
      'url': 'https://www.youtube.com/watch?v=t8pdtQfiTLM&t=126s',
      'video_id': 't8pdtQfiTLM'},
     {'author': 'Dyer, Garofalo, Mann & Schultz',
      'channel': 'Dyer, Garofalo, Mann & Schultz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:50](https://www.youtube.com/watch?v=N689ZxCIKNY&t=170s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Know if they have a mass tour case that they should call our office or contact '
              'our office what would they do and how would they go about contacting us.',
      'timestamp': 170,
      'timestamp_label': '[00:02:50]',
      'timestamp_seconds': 170,
      'tip': 'Know if they have a mass tour case that they should call our office or contact '
             'our office what would they do and how would they go about contacting us.',
      'title': 'What is a Mass Tort Lawsuit? (Dyer, Garofalo, Mann & Schultz)',
      'url': 'https://www.youtube.com/watch?v=N689ZxCIKNY&t=170s',
      'video_id': 'N689ZxCIKNY'},
     {'author': 'Fleming, Nolen & Jez',
      'channel': 'Fleming, Nolen & Jez',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:45](https://www.youtube.com/watch?v=YHzG4RIk3g8&t=105s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Knowledge of course you talk to experts before the mdl is formed and and while '
              "you're building your case because you need to know that there is one but when.",
      'timestamp': 105,
      'timestamp_label': '[00:01:45]',
      'timestamp_seconds': 105,
      'tip': 'Knowledge of course you talk to experts before the mdl is formed and and while '
             "you're building your case because you need to know that there is one but when.",
      'title': "Kelsey Stokes discusses what it's like to be in leadership on a MDL case "
               '(Fleming, Nolen & Jez)',
      'url': 'https://www.youtube.com/watch?v=YHzG4RIk3g8&t=105s',
      'video_id': 'YHzG4RIk3g8'},
     {'author': 'Case Works',
      'channel': 'Case Works',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:37](https://www.youtube.com/watch?v=flwkUvC50CU&t=217s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And that would avoid the types of injuries that we're seeing in this "
              'consolidated group of lawsuits. Thank you for that, Shannon. And would you '
              'share a little bit about, Berger Montague, their role in this case?',
      'timestamp': 217,
      'timestamp_label': '[00:03:37]',
      'timestamp_seconds': 217,
      'tip': "And that would avoid the types of injuries that we're seeing in this "
             'consolidated group of lawsuits. Thank you for that, Shannon. And would you share '
             'a little bit about, Berger Montague, their role in this case?',
      'title': 'March 2024 Bard PowerPort Litigation Updates with Berger Montague (Case Works)',
      'url': 'https://www.youtube.com/watch?v=flwkUvC50CU&t=217s',
      'video_id': 'flwkUvC50CU'},
     {'author': 'Jon and Marc',
      'channel': 'Jon and Marc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:11](https://www.youtube.com/watch?v=2lQbSEVsxgE&t=551s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "They've settled out on individual cases, they've now settled out with the DOJ. "
              "I think that TikTok's new owner inherited known risk, and they are trying to "
              'get out of these cases in any way possible to avoid the like massive potential, '
              'obviously, bad PR, nuclear verdicts.',
      'timestamp': 551,
      'timestamp_label': '[00:09:11]',
      'timestamp_seconds': 551,
      'tip': "They've settled out on individual cases, they've now settled out with the DOJ. I "
             "think that TikTok's new owner inherited known risk, and they are trying to get "
             'out of these cases in any way possible to avoid the like massive potential, '
             'obviously, bad PR, nuclear verdicts.',
      'title': 'Inside Abbott’s $675 Million NEC Deal and Meta’s High-Stakes Trials (Jon and '
               'Marc)',
      'url': 'https://www.youtube.com/watch?v=2lQbSEVsxgE&t=551s',
      'video_id': '2lQbSEVsxgE'},
     {'author': 'LexHive Podcast (Formerly- The Legal Growth Lab)',
      'channel': 'LexHive Podcast (Formerly- The Legal Growth Lab)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:53](https://www.youtube.com/watch?v=DQ8EXxoteKo&t=833s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'t actually know the process to go through, the criteria, what to do, they "
              'could potentially, you know, mishandle a litigation or a case and that puts you '
              'and your family at risk.',
      'timestamp': 833,
      'timestamp_label': '[00:13:53]',
      'timestamp_seconds': 833,
      'tip': "'t actually know the process to go through, the criteria, what to do, they could "
             'potentially, you know, mishandle a litigation or a case and that puts you and '
             'your family at risk.',
      'title': '$375M Social Media Verdict + $6M Trial: What Mass Tort Lawyers Need to Know '
               '(2026 Update) (LexHive Podcast (Formerly- The Legal Growth Lab))',
      'url': 'https://www.youtube.com/watch?v=DQ8EXxoteKo&t=833s',
      'video_id': 'DQ8EXxoteKo'},
     {'author': 'LawShelf',
      'channel': 'LawShelf',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:31](https://www.youtube.com/watch?v=sozfq7mjvKE&t=811s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Bellwether cases may show the parties their potential risks and benefits and '
              'facilitate settlement in our next module we will discuss many of the ways in '
              'which MDL procedures and class-action procedures are combined in mass tort '
              'actions.',
      'timestamp': 811,
      'timestamp_label': '[00:13:31]',
      'timestamp_seconds': 811,
      'tip': 'Bellwether cases may show the parties their potential risks and benefits and '
             'facilitate settlement in our next module we will discuss many of the ways in '
             'which MDL procedures and class-action procedures are combined in mass tort '
             'actions.',
      'title': 'Multidistrict Litigation: Module 3 of 5 (LawShelf)',
      'url': 'https://www.youtube.com/watch?v=sozfq7mjvKE&t=811s',
      'video_id': 'sozfq7mjvKE'},
     {'author': 'Drugwatch',
      'channel': 'Drugwatch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=Gr0hwiqZSYs&t=52s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'This could bring much needed relief to more victims nationwide. In 2021, '
              'Syngenta and Chevron set aside $187. In July 2025, Syngenta settled a key '
              'lawsuit in Philadelphia right before that case was set for trial.',
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': 'This could bring much needed relief to more victims nationwide. In 2021, '
             'Syngenta and Chevron set aside $187. In July 2025, Syngenta settled a key '
             'lawsuit in Philadelphia right before that case was set for trial.',
      'title': 'Paraquat Lawsuits & Settlements: Fall 2025 Updates (Drugwatch)',
      'url': 'https://www.youtube.com/watch?v=Gr0hwiqZSYs&t=52s',
      'video_id': 'Gr0hwiqZSYs'},
     {'author': "Legal Lead Sharks Podcast | K'Lee Terrazas",
      'channel': "Legal Lead Sharks Podcast | K'Lee Terrazas",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:10](https://www.youtube.com/watch?v=zELnyJbIEGM&t=370s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re going to cheat somewhere else in your case. And that's what it is, just "
              "cheating. But because the punishment used to be $10,000, why wouldn't you do "
              "it? And in some of these cases, Kayleigh, you've seen, you can settle a case "
              'for 25, 50 million dollars.',
      'timestamp': 370,
      'timestamp_label': '[00:06:10]',
      'timestamp_seconds': 370,
      'tip': "'re going to cheat somewhere else in your case. And that's what it is, just "
             "cheating. But because the punishment used to be $10,000, why wouldn't you do it? "
             "And in some of these cases, Kayleigh, you've seen, you can settle a case for 25, "
             '50 million dollars.',
      'title': 'Personal Injury Law’s Dark Side Mass Tort Reform & Barratry Exposed | Lawyer '
               "Up the Next Generation (Legal Lead Sharks Podcast | K'Lee Terrazas)",
      'url': 'https://www.youtube.com/watch?v=zELnyJbIEGM&t=370s',
      'video_id': 'zELnyJbIEGM'},
     {'author': 'Vineskills',
      'channel': 'Vineskills',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:37:02](https://www.youtube.com/watch?v=YtXAzduQ3PE&t=2222s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Questions and we gotta tell it again what the project type is and what section '
              'we want to um create that item in and once we do that uh there will be '
              "additional fields that appear um that we can populate uh so we're going to do "
              'my workers.',
      'timestamp': 2222,
      'timestamp_label': '[00:37:02]',
      'timestamp_seconds': 2222,
      'tip': 'Questions and we gotta tell it again what the project type is and what section '
             'we want to um create that item in and once we do that uh there will be '
             "additional fields that appear um that we can populate uh so we're going to do my "
             'workers.',
      'title': 'Free Help Wednesdays: Workato and Filevine (Vineskills)',
      'url': 'https://www.youtube.com/watch?v=YtXAzduQ3PE&t=2222s',
      'video_id': 'YtXAzduQ3PE'}],
 6: [{'author': 'Saad Khan | AI Automation',
      'channel': 'Saad Khan | AI Automation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:09](https://www.youtube.com/watch?v=ZkN7hMCBwmQ&t=69s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Let me walk you through each one. The moment a prospect clicks on your ads and '
              'submits the information, the system catches it instantly through event-driven '
              'injection. In milliseconds, not minutes, a signal is sent to initiate an '
              'outbound call.',
      'timestamp': 69,
      'timestamp_label': '[00:01:09]',
      'timestamp_seconds': 69,
      'tip': 'Let me walk you through each one. The moment a prospect clicks on your ads and '
             'submits the information, the system catches it instantly through event-driven '
             'injection. In milliseconds, not minutes, a signal is sent to initiate an '
             'outbound call.',
      'title': 'How Mass Tort Law Firms save $30,000+ / month Using AI Voice Agents | '
               'Blueprint Explained (Saad Khan | AI Automation)',
      'url': 'https://www.youtube.com/watch?v=ZkN7hMCBwmQ&t=69s',
      'video_id': 'ZkN7hMCBwmQ'},
     {'author': 'The Leads Warehouse',
      'channel': 'The Leads Warehouse',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:41](https://www.youtube.com/watch?v=FlPOncTNHp0&t=41s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mass tort lead generation generally falls into three major categories: signed '
              'case or full intake campaigns, long-form leads, and co-registration real-time '
              'leads.',
      'timestamp': 41,
      'timestamp_label': '[00:00:41]',
      'timestamp_seconds': 41,
      'tip': 'Mass tort lead generation generally falls into three major categories: signed '
             'case or full intake campaigns, long-form leads, and co-registration real-time '
             'leads.',
      'title': 'How AI Is Changing Mass Tort Lead Generation (The Leads Warehouse)',
      'url': 'https://www.youtube.com/watch?v=FlPOncTNHp0&t=41s',
      'video_id': 'FlPOncTNHp0'},
     {'author': 'TownCenter Partners Litigation Finance',
      'channel': 'TownCenter Partners Litigation Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=yYpZT2DR1fE&t=21s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'But a closer look at litigation funding reveals it offers significant '
              'advantages for building a better law practice. First, litigation funding '
              'increases demand for legal services. Lawyers will have more business if there '
              'are more parties pursuing legal claims.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'But a closer look at litigation funding reveals it offers significant advantages '
             'for building a better law practice. First, litigation funding increases demand '
             'for legal services. Lawyers will have more business if there are more parties '
             'pursuing legal claims.',
      'title': 'How Litigation Finance Can Help Lawyers and Law Firms (TownCenter Partners '
               'Litigation Finance)',
      'url': 'https://www.youtube.com/watch?v=yYpZT2DR1fE&t=21s',
      'video_id': 'yYpZT2DR1fE'},
     {'author': 'The National Law Review',
      'channel': 'The National Law Review',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:30:34](https://www.youtube.com/watch?v=9teRv9eFpEc&t=1834s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s first call might be to the the transactional lawyer who helped them on the "
              'agreement, who helped them on the deal.',
      'timestamp': 1834,
      'timestamp_label': '[00:30:34]',
      'timestamp_seconds': 1834,
      'tip': "'s first call might be to the the transactional lawyer who helped them on the "
             'agreement, who helped them on the deal.',
      'title': 'Litigation Finance Market Process (The National Law Review)',
      'url': 'https://www.youtube.com/watch?v=9teRv9eFpEc&t=1834s',
      'video_id': '9teRv9eFpEc'},
     {'author': 'The Good Law Group',
      'channel': 'The Good Law Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:16](https://www.youtube.com/watch?v=qhkL5vZ-1Ps&t=76s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '50,000 to $500,000 per case. It is hard to say what each person can expect. '
              'These numbers are just estimates and hopefully we will find out soon when the '
              'bellwethers begin in 2021 what the settlements are going to be for everybody '
              "that's been harmed by these products.",
      'timestamp': 76,
      'timestamp_label': '[00:01:16]',
      'timestamp_seconds': 76,
      'tip': '50,000 to $500,000 per case. It is hard to say what each person can expect. '
             'These numbers are just estimates and hopefully we will find out soon when the '
             'bellwethers begin in 2021 what the settlements are going to be for everybody '
             "that's been harmed by these products.",
      'title': 'How Is Compensation Awarded in a Hernia Mesh Lawsuit? | The Good Law Group '
               '(The Good Law Group)',
      'url': 'https://www.youtube.com/watch?v=qhkL5vZ-1Ps&t=76s',
      'video_id': 'qhkL5vZ-1Ps'},
     {'author': "Legal Lead Sharks Podcast | K'Lee Terrazas",
      'channel': "Legal Lead Sharks Podcast | K'Lee Terrazas",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:37](https://www.youtube.com/watch?v=XcpDdsuGoEY&t=217s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "28% of calls that came from the law firm's GBP went missed on the first "
              'attempt. I promise you guys, they are not going to leave a voicemail. They are '
              'going to call the next person on their list.',
      'timestamp': 217,
      'timestamp_label': '[00:03:37]',
      'timestamp_seconds': 217,
      'tip': "28% of calls that came from the law firm's GBP went missed on the first attempt. "
             'I promise you guys, they are not going to leave a voicemail. They are going to '
             'call the next person on their list.',
      'title': 'Intake EQ For Law Firms Because a Missed Call is a Missed Case! Live Demo.... '
               "(Legal Lead Sharks Podcast | K'Lee Terrazas)",
      'url': 'https://www.youtube.com/watch?v=XcpDdsuGoEY&t=217s',
      'video_id': 'XcpDdsuGoEY'},
     {'author': 'Jon and Marc',
      'channel': 'Jon and Marc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:22](https://www.youtube.com/watch?v=8CBO3CgHLvA&t=82s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Stop chasing vanity metrics and get more cases. Let's get back to the episode. "
              "We work on the exact opposite end of the business that we work. We're on the "
              'front end on the lead and case generation side.',
      'timestamp': 82,
      'timestamp_label': '[00:01:22]',
      'timestamp_seconds': 82,
      'tip': "Stop chasing vanity metrics and get more cases. Let's get back to the episode. "
             "We work on the exact opposite end of the business that we work. We're on the "
             'front end on the lead and case generation side.',
      'title': 'The Hidden Process That Delays Every Mass Tort Payout (Jon and Marc)',
      'url': 'https://www.youtube.com/watch?v=8CBO3CgHLvA&t=82s',
      'video_id': '8CBO3CgHLvA'},
     {'author': 'Miller & Zois, Attorneys at Law',
      'channel': 'Miller & Zois, Attorneys at Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=awXMQE40aro&t=20s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'If the jury resolved Institute in favor of the plaintiff it could pave the way '
              'for a multi-billion dollar settlement the city of Stuart case is the first.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'If the jury resolved Institute in favor of the plaintiff it could pave the way '
             'for a multi-billion dollar settlement the city of Stuart case is the first.',
      'title': 'AFFF Firefighting Foam MDL - 1st Bellwether Trial (Miller & Zois, Attorneys at '
               'Law)',
      'url': 'https://www.youtube.com/watch?v=awXMQE40aro&t=20s',
      'video_id': 'awXMQE40aro'},
     {'author': 'Napoli Shkolnik',
      'channel': 'Napoli Shkolnik',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:19](https://www.youtube.com/watch?v=S1VC15_WonY&t=19s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Individual personal injury claims. When the AFFF litigation first began, the '
              'focus was very site-specific.  We were looking at contamination tied to.',
      'timestamp': 19,
      'timestamp_label': '[00:00:19]',
      'timestamp_seconds': 19,
      'tip': 'Individual personal injury claims. When the AFFF litigation first began, the '
             'focus was very site-specific.  We were looking at contamination tied to.',
      'title': "PFAS Litigation's Next Chapter: The Rise of Individual Personal Injury Claims "
               '(Napoli Shkolnik)',
      'url': 'https://www.youtube.com/watch?v=S1VC15_WonY&t=19s',
      'video_id': 'S1VC15_WonY'},
     {'author': 'OfferVault',
      'channel': 'OfferVault',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:49](https://www.youtube.com/watch?v=dlxuHtoqmYw&t=289s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Vessel for how clever we are and how cheaply we can get these leads for them '
              "that's the whole exchange basic stuff get a cheap lead make sure it works out.",
      'timestamp': 289,
      'timestamp_label': '[00:04:49]',
      'timestamp_seconds': 289,
      'tip': 'Vessel for how clever we are and how cheaply we can get these leads for them '
             "that's the whole exchange basic stuff get a cheap lead make sure it works out.",
      'title': 'The Affiliate Marketing Show - Ep. 37 - Mast Tort, SMS, Compliance, Paying it '
               'Forward, TXTRIA.net (OfferVault)',
      'url': 'https://www.youtube.com/watch?v=dlxuHtoqmYw&t=289s',
      'video_id': 'dlxuHtoqmYw'},
     {'author': 'Levinson and Stefani Injury Lawyers',
      'channel': 'Levinson and Stefani Injury Lawyers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:57](https://www.youtube.com/watch?v=TrEm-Mk2jeQ&t=657s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'This report automatically sent to you on a weekly basis and they get that '
              "report and it's an Excel file and it's a list of every provider within every "
              'case.',
      'timestamp': 657,
      'timestamp_label': '[00:10:57]',
      'timestamp_seconds': 657,
      'tip': 'This report automatically sent to you on a weekly basis and they get that report '
             "and it's an Excel file and it's a list of every provider within every case.",
      'title': 'How to Use Filevine to Track Medicals (UPDATED!!!) (Levinson and Stefani '
               'Injury Lawyers)',
      'url': 'https://www.youtube.com/watch?v=TrEm-Mk2jeQ&t=657s',
      'video_id': 'TrEm-Mk2jeQ'},
     {'author': 'Cut to the Chase Network',
      'channel': 'Cut to the Chase Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:07](https://www.youtube.com/watch?v=IHvCfh-WJ6E&t=1027s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '"Okay, now we want to look at this mass tort thing." So, with that being said, '
              "there are all kinds of what you call lead vendors out there. So, let's say I "
              "want to get into mass torts, I'm going to go to a conference, I'm going to meet "
              'somebody.',
      'timestamp': 1027,
      'timestamp_label': '[00:17:07]',
      'timestamp_seconds': 1027,
      'tip': '"Okay, now we want to look at this mass tort thing." So, with that being said, '
             "there are all kinds of what you call lead vendors out there. So, let's say I "
             "want to get into mass torts, I'm going to go to a conference, I'm going to meet "
             'somebody.',
      'title': 'Mass Tort Update 2026: Roundup Settlement, PFAS Litigation & Uber Cases | '
               'Steve Smith (Cut to the Chase Network)',
      'url': 'https://www.youtube.com/watch?v=IHvCfh-WJ6E&t=1027s',
      'video_id': 'IHvCfh-WJ6E'},
     {'author': 'Cut to the Chase Network',
      'channel': 'Cut to the Chase Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:33](https://www.youtube.com/watch?v=-H3O5pPP-XA&t=513s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And there's pressure points to have a deal announced soon. I feel confident "
              'that they will reach a global resolution this year. The judge can in fact force '
              'a date for the next bellwether case, and that date would trigger a resolution.',
      'timestamp': 513,
      'timestamp_label': '[00:08:33]',
      'timestamp_seconds': 513,
      'tip': "And there's pressure points to have a deal announced soon. I feel confident that "
             'they will reach a global resolution this year. The judge can in fact force a '
             'date for the next bellwether case, and that date would trigger a resolution.',
      'title': 'Mass Tort Update 2026: Camp Lejeune, PFAS, NEC Baby Formula & Depo-Provera | '
               'Steve Smith Pt. 2 (Cut to the Chase Network)',
      'url': 'https://www.youtube.com/watch?v=-H3O5pPP-XA&t=513s',
      'video_id': '-H3O5pPP-XA'},
     {'author': 'Alert Communications',
      'channel': 'Alert Communications',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:30](https://www.youtube.com/watch?v=PJEVefyQCxA&t=1650s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Time of the intake and the quality of that intake is actually shortened so that '
              'first impression really matters to conversions as well.',
      'timestamp': 1650,
      'timestamp_label': '[00:27:30]',
      'timestamp_seconds': 1650,
      'tip': 'Time of the intake and the quality of that intake is actually shortened so that '
             'first impression really matters to conversions as well.',
      'title': 'Alert Communications Webinar - Converting Mass Tort Leads - May 2020 (Alert '
               'Communications)',
      'url': 'https://www.youtube.com/watch?v=PJEVefyQCxA&t=1650s',
      'video_id': 'PJEVefyQCxA'},
     {'author': 'Jon and Marc',
      'channel': 'Jon and Marc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:28](https://www.youtube.com/watch?v=IPkB5-wL-oY&t=508s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re working on that, Kelsey, what what do you guys have going on in MDL? First "
              "of all, what's the every time we have a a case management conference, the judge "
              'says, "These just keep coming. They get get filed every day. When is this going '
              'to stop?".',
      'timestamp': 508,
      'timestamp_label': '[00:08:28]',
      'timestamp_seconds': 508,
      'tip': "'re working on that, Kelsey, what what do you guys have going on in MDL? First "
             "of all, what's the every time we have a a case management conference, the judge "
             'says, "These just keep coming. They get get filed every day. When is this going '
             'to stop?".',
      'title': 'What’s Next for Hernia Mesh Litigation? With Kelsey Stokes & David Hobbs (Jon '
               'and Marc)',
      'url': 'https://www.youtube.com/watch?v=IPkB5-wL-oY&t=508s',
      'video_id': 'IPkB5-wL-oY'}],
 7: [{'author': 'SelectHub',
      'channel': 'SelectHub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=BBsBjTLqlDI&t=28s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Filevine is a legal case management and workflow platform built for law firms, '
              'corporate legal departments, and government agencies. Teams manage cases, '
              'contracts, documents, deadlines, billing, and client communication all in one '
              'centralized system.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': 'Filevine is a legal case management and workflow platform built for law firms, '
             'corporate legal departments, and government agencies. Teams manage cases, '
             'contracts, documents, deadlines, billing, and client communication all in one '
             'centralized system.',
      'title': 'Ultimate Filevine Review 2026: Legal Case Management + AI Intelligence '
               '(SelectHub)',
      'url': 'https://www.youtube.com/watch?v=BBsBjTLqlDI&t=28s',
      'video_id': 'BBsBjTLqlDI'},
     {'author': 'Tech Help Man',
      'channel': 'Tech Help Man',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:07](https://www.youtube.com/watch?v=g6KQDADEgmI&t=667s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The value of AI is strongest when it removes repetitive administration while '
              "keeping source material and responsibility clear. Litify say it's AI operates "
              'with case context and can support both recommendations and workflow execution.',
      'timestamp': 667,
      'timestamp_label': '[00:11:07]',
      'timestamp_seconds': 667,
      'tip': 'The value of AI is strongest when it removes repetitive administration while '
             "keeping source material and responsibility clear. Litify say it's AI operates "
             'with case context and can support both recommendations and workflow execution.',
      'title': 'Litify Tutorial for Beginners | Step by step Legal Practice Management Guide '
               '(Tech Help Man)',
      'url': 'https://www.youtube.com/watch?v=g6KQDADEgmI&t=667s',
      'video_id': 'g6KQDADEgmI'},
     {'author': 'The Federalist Society',
      'channel': 'The Federalist Society',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:30](https://www.youtube.com/watch?v=vk0M8TfTG9g&t=1410s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I'll call big picture or process, uh, type lessons and then the second is more "
              'sort of granular practice type lessons. Um, and and bellwethers, which is '
              'really the focus of our conversation, falls into the former, uh, which is the '
              'big picture lessons.',
      'timestamp': 1410,
      'timestamp_label': '[00:23:30]',
      'timestamp_seconds': 1410,
      'tip': "I'll call big picture or process, uh, type lessons and then the second is more "
             'sort of granular practice type lessons. Um, and and bellwethers, which is really '
             'the focus of our conversation, falls into the former, uh, which is the big '
             'picture lessons.',
      'title': 'Trying Cases and Settlement [Multidistrict Litigation (MDL) Conference] (The '
               'Federalist Society)',
      'url': 'https://www.youtube.com/watch?v=vk0M8TfTG9g&t=1410s',
      'video_id': 'vk0M8TfTG9g'},
     {'author': 'Sullivan & Cromwell LLP',
      'channel': 'Sullivan & Cromwell LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=X7eQYHQmnm8&t=79s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Since Congress passed the Multidistrict Litigation Act in 1968 and created the '
              'MDL process, there haven’t been any specific rules dictating how judges should '
              'manage MDLs, beyond the Federal Rules of Civil Procedure that apply in every '
              'federal civil case.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': 'Since Congress passed the Multidistrict Litigation Act in 1968 and created the '
             'MDL process, there haven’t been any specific rules dictating how judges should '
             'manage MDLs, beyond the Federal Rules of Civil Procedure that apply in every '
             'federal civil case.',
      'title': 'The New Proposed Federal Rule 16.1 and Its Implications for Multidistrict '
               'Litigation (Sullivan & Cromwell LLP)',
      'url': 'https://www.youtube.com/watch?v=X7eQYHQmnm8&t=79s',
      'video_id': 'X7eQYHQmnm8'},
     {'author': 'King Law',
      'channel': 'King Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:59](https://www.youtube.com/watch?v=aOm5hBG6t9s&t=119s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Since that time, we had another case management order, Case Management Order '
              '37, which talked about the deficiency process. Defendants have long maintained '
              'that there are not quality cases or not quality lawsuits filed in this '
              'litigation.',
      'timestamp': 119,
      'timestamp_label': '[00:01:59]',
      'timestamp_seconds': 119,
      'tip': 'Since that time, we had another case management order, Case Management Order 37, '
             'which talked about the deficiency process. Defendants have long maintained that '
             'there are not quality cases or not quality lawsuits filed in this litigation.',
      'title': 'PFAS Lawsuit Update (June 2026) - Settlements Anticipated (King Law)',
      'url': 'https://www.youtube.com/watch?v=aOm5hBG6t9s&t=119s',
      'video_id': 'aOm5hBG6t9s'},
     {'author': 'Profit with Law (Moshe Amsel)',
      'channel': 'Profit with Law (Moshe Amsel)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:58](https://www.youtube.com/watch?v=tjuCUb5CKVY&t=538s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So if we have one claimant that's injured, right, one plaintiff in a case, they "
              'have their own lawsuit, it goes through all the steps of, you know, the '
              'discovery process, depositions, all of these things for that one person based '
              'on their one case, right?',
      'timestamp': 538,
      'timestamp_label': '[00:08:58]',
      'timestamp_seconds': 538,
      'tip': "So if we have one claimant that's injured, right, one plaintiff in a case, they "
             'have their own lawsuit, it goes through all the steps of, you know, the '
             'discovery process, depositions, all of these things for that one person based on '
             'their one case, right?',
      'title': 'How to Make a Return on Investing in Mass Tort Cases (Profit with Law (Moshe '
               'Amsel))',
      'url': 'https://www.youtube.com/watch?v=tjuCUb5CKVY&t=538s',
      'video_id': 'tjuCUb5CKVY'},
     {'author': 'Drop In, A Parambil Podcast',
      'channel': 'Drop In, A Parambil Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=yCOD2nZqkok&t=20s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'But each person still has an individual case with their own causation and '
              'damages. Few people understand that system better than Toby Milrod. Toby has '
              'spent more than 25 years in pharmaceutical, medical device, and complex injury '
              'litigation.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'But each person still has an individual case with their own causation and '
             'damages. Few people understand that system better than Toby Milrod. Toby has '
             'spent more than 25 years in pharmaceutical, medical device, and complex injury '
             'litigation.',
      'title': 'How mass torts are won, from hormone therapy to Roundup | Tobi Millrood (Drop '
               'In, A Parambil Podcast)',
      'url': 'https://www.youtube.com/watch?v=yCOD2nZqkok&t=20s',
      'video_id': 'yCOD2nZqkok'},
     {'author': 'Optimize My Firm',
      'channel': 'Optimize My Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:25](https://www.youtube.com/watch?v=My1QKQ-hGSw&t=1165s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And if you can bring those two together, then you can just you've got a very "
              'reliable system and it should function. Now you have to check it all the time. '
              "That's something we added this year was quality assurance because we had "
              'awesome people.',
      'timestamp': 1165,
      'timestamp_label': '[00:19:25]',
      'timestamp_seconds': 1165,
      'tip': "And if you can bring those two together, then you can just you've got a very "
             'reliable system and it should function. Now you have to check it all the time. '
             "That's something we added this year was quality assurance because we had awesome "
             'people.',
      'title': 'Litigation to Leadership: Moving from The Courtroom to Business Development - '
               'PIMM 163@fellerwendt (Optimize My Firm)',
      'url': 'https://www.youtube.com/watch?v=My1QKQ-hGSw&t=1165s',
      'video_id': 'My1QKQ-hGSw'},
     {'author': 'LexHive Podcast (Formerly- The Legal Growth Lab)',
      'channel': 'LexHive Podcast (Formerly- The Legal Growth Lab)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:52](https://www.youtube.com/watch?v=jn6XvG1gC9w&t=952s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So instead what we do is we go through this bellweather process where the idea '
              'is to take representative cases of the entire inventory which has the facts, '
              'the science and the issue that applies to every case.',
      'timestamp': 952,
      'timestamp_label': '[00:15:52]',
      'timestamp_seconds': 952,
      'tip': 'So instead what we do is we go through this bellweather process where the idea '
             'is to take representative cases of the entire inventory which has the facts, the '
             'science and the issue that applies to every case.',
      'title': 'Underwriting Mass Torts: A Risk Framework for PI firms (LexHive Podcast '
               '(Formerly- The Legal Growth Lab))',
      'url': 'https://www.youtube.com/watch?v=jn6XvG1gC9w&t=952s',
      'video_id': 'jn6XvG1gC9w'},
     {'author': 'Searcy Law Video',
      'channel': 'Searcy Law Video',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:54](https://www.youtube.com/watch?v=yIQ0NYXRsmQ&t=294s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So, in some respects, that's one of the benefits of the MDL process is having a "
              'single judge who is committed to making certain that the case moves as quickly '
              'as possible.',
      'timestamp': 294,
      'timestamp_label': '[00:04:54]',
      'timestamp_seconds': 294,
      'tip': "So, in some respects, that's one of the benefits of the MDL process is having a "
             'single judge who is committed to making certain that the case moves as quickly '
             'as possible.',
      'title': 'What is a Multidistrict Litigation, or MDL? (Searcy Law Video)',
      'url': 'https://www.youtube.com/watch?v=yIQ0NYXRsmQ&t=294s',
      'video_id': 'yIQ0NYXRsmQ'},
     {'author': 'Business Box',
      'channel': 'Business Box',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=ET5Xa_RCeM8&t=64s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Centralizes the process simplifying tasks like evidence collection and witness '
              'deposition now after pre-trial each case proceeds individually ensuring '
              'failured outcomes based on specific circum circumstances then we have '
              'individualized damage.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': 'Centralizes the process simplifying tasks like evidence collection and witness '
             'deposition now after pre-trial each case proceeds individually ensuring failured '
             'outcomes based on specific circum circumstances then we have individualized '
             'damage.',
      'title': "Mass Torts VS Class Action | What's The Difference Between Them ? (Business "
               'Box)',
      'url': 'https://www.youtube.com/watch?v=ET5Xa_RCeM8&t=64s',
      'video_id': 'ET5Xa_RCeM8'},
     {'author': 'Jackson LLP Healthcare Lawyers',
      'channel': 'Jackson LLP Healthcare Lawyers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:22](https://www.youtube.com/watch?v=4niOtoceEKc&t=142s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'But if you are operating in any of the states in which our attorneys are '
              "licensed, we're able to help you navigate this process and get your business or "
              'practice either expanded or up and running.',
      'timestamp': 142,
      'timestamp_label': '[00:02:22]',
      'timestamp_seconds': 142,
      'tip': 'But if you are operating in any of the states in which our attorneys are '
             "licensed, we're able to help you navigate this process and get your business or "
             'practice either expanded or up and running.',
      'title': 'Top 3 Reasons to Establish a Management Services Organization (MSO) | Jackson '
               'LLP Healthcare Lawyers (Jackson LLP Healthcare Lawyers)',
      'url': 'https://www.youtube.com/watch?v=4niOtoceEKc&t=142s',
      'video_id': '4niOtoceEKc'},
     {'author': 'Center for Litigation and Courts',
      'channel': 'Center for Litigation and Courts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:50](https://www.youtube.com/watch?v=ZZ-JHbBTjyw&t=590s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Process takes a while um and so if we want to sort of you know prioritize '
              'getting recovery into the hands of injured victims as quickly as possible it '
              'could be that some of these alternatives are better.',
      'timestamp': 590,
      'timestamp_label': '[00:09:50]',
      'timestamp_seconds': 590,
      'tip': 'Process takes a while um and so if we want to sort of you know prioritize '
             'getting recovery into the hands of injured victims as quickly as possible it '
             'could be that some of these alternatives are better.',
      'title': 'Episode 9: "How Does Litigation Resolve Mass Torts?" (Center for Litigation '
               'and Courts)',
      'url': 'https://www.youtube.com/watch?v=ZZ-JHbBTjyw&t=590s',
      'video_id': 'ZZ-JHbBTjyw'},
     {'author': 'Faces of Lawsuit Abuse',
      'channel': 'Faces of Lawsuit Abuse',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:47](https://www.youtube.com/watch?v=hBSeW8fizPA&t=107s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Information prohibits full social security numbers from being released and so '
              'forth less information than even lawsuits publicly disclose says mckenna until '
              'congress acts unscrupulous lawyers will continue to game the system at the '
              'expense of real victims.',
      'timestamp': 107,
      'timestamp_label': '[00:01:47]',
      'timestamp_seconds': 107,
      'tip': 'Information prohibits full social security numbers from being released and so '
             'forth less information than even lawsuits publicly disclose says mckenna until '
             'congress acts unscrupulous lawyers will continue to game the system at the '
             'expense of real victims.',
      'title': 'Deterring Fraud in the Longest Running Mass Tort in History (Faces of Lawsuit '
               'Abuse)',
      'url': 'https://www.youtube.com/watch?v=hBSeW8fizPA&t=107s',
      'video_id': 'hBSeW8fizPA'},
     {'author': 'LawShelf',
      'channel': 'LawShelf',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:09](https://www.youtube.com/watch?v=5S5cU4oj7oA&t=669s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'That must be resolved for all individual plaintiffs in the MDL either through '
              'motion settlement or trial however the resolution of these issues covered by '
              'the class often makes the negotiation of settlements for the residual '
              'individual claims easier and more likely.',
      'timestamp': 669,
      'timestamp_label': '[00:11:09]',
      'timestamp_seconds': 669,
      'tip': 'That must be resolved for all individual plaintiffs in the MDL either through '
             'motion settlement or trial however the resolution of these issues covered by the '
             'class often makes the negotiation of settlements for the residual individual '
             'claims easier and more likely.',
      'title': 'Interplay Between Class Actions with Multidistrict Litigation: Module 4 of 5 '
               '(LawShelf)',
      'url': 'https://www.youtube.com/watch?v=5S5cU4oj7oA&t=669s',
      'video_id': '5S5cU4oj7oA'}],
 8: [{'author': 'Lunch Hour Legal Marketing',
      'channel': 'Lunch Hour Legal Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:58](https://www.youtube.com/watch?v=9AejH9lLg90&t=1198s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'ve done with Lead Docket passing the data into FileVine. It actually all goes "
              "into the project immediately when it's created. We have a direct integration "
              "that no other case management platform has with Lead Docket. It's Lead Docket "
              'and File Vine directly integrate.',
      'timestamp': 1198,
      'timestamp_label': '[00:19:58]',
      'timestamp_seconds': 1198,
      'tip': "'ve done with Lead Docket passing the data into FileVine. It actually all goes "
             "into the project immediately when it's created. We have a direct integration "
             "that no other case management platform has with Lead Docket. It's Lead Docket "
             'and File Vine directly integrate.',
      'title': 'How Filevine Is Transforming Intake, CRM, & Client Communication (Lunch Hour '
               'Legal Marketing)',
      'url': 'https://www.youtube.com/watch?v=9AejH9lLg90&t=1198s',
      'video_id': '9AejH9lLg90'},
     {'author': 'SelectHub',
      'channel': 'SelectHub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:15](https://www.youtube.com/watch?v=RE04OZvO3RQ&t=375s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Filevine offers firm-wide operational reporting, matter progress, team '
              'productivity, billable hours, case outcomes, revenue tracking, and custom '
              'dashboards. Harvey reports on AI usage and compliance. Filevine reports on '
              'business performance and operations.',
      'timestamp': 375,
      'timestamp_label': '[00:06:15]',
      'timestamp_seconds': 375,
      'tip': 'Filevine offers firm-wide operational reporting, matter progress, team '
             'productivity, billable hours, case outcomes, revenue tracking, and custom '
             'dashboards. Harvey reports on AI usage and compliance. Filevine reports on '
             'business performance and operations.',
      'title': 'Harvey AI vs. Filevine: Which Legal AI Platform Is Right For Your Firm in '
               '2026? (SelectHub)',
      'url': 'https://www.youtube.com/watch?v=RE04OZvO3RQ&t=375s',
      'video_id': 'RE04OZvO3RQ'},
     {'author': 'The LegalTech Fund',
      'channel': 'The LegalTech Fund',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=_HuCGlH6Wyw&t=21s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'For those who may not be familiar with Pattern Data, what exactly do you do? '
              'Who do you serve and where does where does Pattern fit into the industry? '
              'Pattern is an AI-first software platform.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'For those who may not be familiar with Pattern Data, what exactly do you do? Who '
             'do you serve and where does where does Pattern fit into the industry? Pattern is '
             'an AI-first software platform.',
      'title': 'In Studio with Pattern Data | Mass Tort Rebuilt | AI, Expertise, and the '
               'Future of Litigation | 2026 (The LegalTech Fund)',
      'url': 'https://www.youtube.com/watch?v=_HuCGlH6Wyw&t=21s',
      'video_id': '_HuCGlH6Wyw'},
     {'author': 'Sagar Pratap Singh',
      'channel': 'Sagar Pratap Singh',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:28](https://www.youtube.com/watch?v=mCa47xGWbys&t=268s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'It built for that workflow first in depth. It also followed the case back to '
              'the front door. By 2022 it had bought lead docket, a lead tracking and intake '
              'tool. So a form intake could sit in the same system as it cases.',
      'timestamp': 268,
      'timestamp_label': '[00:04:28]',
      'timestamp_seconds': 268,
      'tip': 'It built for that workflow first in depth. It also followed the case back to the '
             'front door. By 2022 it had bought lead docket, a lead tracking and intake tool. '
             'So a form intake could sit in the same system as it cases.',
      'title': 'How Filevine, MyCase and Smokeball Won Small Law Firms | Ep 4 (Sagar Pratap '
               'Singh)',
      'url': 'https://www.youtube.com/watch?v=mCa47xGWbys&t=268s',
      'video_id': 'mCa47xGWbys'},
     {'author': 'Jon and Marc',
      'channel': 'Jon and Marc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:35:54](https://www.youtube.com/watch?v=U2xFBBUm_IU&t=2154s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s from their referrals or from repeat cases. They're just trying to acquire "
              "it, data, market share. Tactically, what we've seen is it's something's very "
              'very very interesting. Google Ads, search ads used to be the dominant way for '
              'firms to acquire cases, right?',
      'timestamp': 2154,
      'timestamp_label': '[00:35:54]',
      'timestamp_seconds': 2154,
      'tip': "'s from their referrals or from repeat cases. They're just trying to acquire it, "
             "data, market share. Tactically, what we've seen is it's something's very very "
             'very interesting. Google Ads, search ads used to be the dominant way for firms '
             'to acquire cases, right?',
      'title': 'The Private Equity Shift: Turning Your Law Firm From a Founder-Led Practice to '
               'a Scalable Asset (Jon and Marc)',
      'url': 'https://www.youtube.com/watch?v=U2xFBBUm_IU&t=2154s',
      'video_id': 'U2xFBBUm_IU'},
     {'author': 'LawAccounting',
      'channel': 'LawAccounting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=dqv7XkRgaQQ&t=38s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, quick note on the tech side. Case cube and law accounting are both built '
              "natively on Salesforce, the world's leading CRM system. So that gives us "
              'enterprise level security, deep customization, and a single source of truth for '
              'both case management and trust accounting.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': 'So, quick note on the tech side. Case cube and law accounting are both built '
             "natively on Salesforce, the world's leading CRM system. So that gives us "
             'enterprise level security, deep customization, and a single source of truth for '
             'both case management and trust accounting.',
      'title': 'How Mass Tort Law Firms Can Manage Intake, Matters, Documents, Billing & '
               'Accounting (LawAccounting)',
      'url': 'https://www.youtube.com/watch?v=dqv7XkRgaQQ&t=38s',
      'video_id': 'dqv7XkRgaQQ'},
     {'author': 'Pattern Data',
      'channel': 'Pattern Data',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=PjzhkF1x4xI&t=20s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'CRM, some of the data in spreadsheets. And when it kind time to do something '
              'with the information, you need to grab somebody to kind of stitch it together, '
              're-review the cases, modify the data structures.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'CRM, some of the data in spreadsheets. And when it kind time to do something '
             'with the information, you need to grab somebody to kind of stitch it together, '
             're-review the cases, modify the data structures.',
      'title': 'How Mass Tort Firms Manage Cases from Intake to Settlement | Matt Francis '
               '(Pattern Data)',
      'url': 'https://www.youtube.com/watch?v=PjzhkF1x4xI&t=20s',
      'video_id': 'PjzhkF1x4xI'},
     {'author': 'LawNext',
      'channel': 'LawNext',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:59](https://www.youtube.com/watch?v=Yq68SC86WTQ&t=1559s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I ask him how he and his firm have incorporated the platform more broadly into '
              'their workflows. Tell you talked about this this one case with with the infant '
              "in the NICU. I don't know if that was that the Abbott Lab. I read about you "
              'being work on an Abbott Labs case.',
      'timestamp': 1559,
      'timestamp_label': '[00:25:59]',
      'timestamp_seconds': 1559,
      'tip': 'I ask him how he and his firm have incorporated the platform more broadly into '
             'their workflows. Tell you talked about this this one case with with the infant '
             "in the NICU. I don't know if that was that the Abbott Lab. I read about you "
             'being work on an Abbott Labs case.',
      'title': 'Ep 295 - How One Mass Tort Firm Uses Supio, the AI Platform for PI Lawyers '
               '(LawNext)',
      'url': 'https://www.youtube.com/watch?v=Yq68SC86WTQ&t=1559s',
      'video_id': 'Yq68SC86WTQ'},
     {'author': 'Vineskills',
      'channel': 'Vineskills',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:35](https://www.youtube.com/watch?v=XAU9uhQg6nk&t=755s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, with some things in Filevine, um you can get uh you can kind of undo those '
              'actions, particularly in the PDF editor tool or like with DocGens, redactions '
              'might be the one and only time that that is not the case.',
      'timestamp': 755,
      'timestamp_label': '[00:12:35]',
      'timestamp_seconds': 755,
      'tip': 'So, with some things in Filevine, um you can get uh you can kind of undo those '
             'actions, particularly in the PDF editor tool or like with DocGens, redactions '
             'might be the one and only time that that is not the case.',
      'title': 'Free Help Wednesdays: Filevine Tips for Paralegals (Vineskills)',
      'url': 'https://www.youtube.com/watch?v=XAU9uhQg6nk&t=755s',
      'video_id': 'XAU9uhQg6nk'},
     {'author': 'Blue Sky Legal',
      'channel': 'Blue Sky Legal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=n9AQhSIMkNg&t=51s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "CPM goes up, and your CPA can double. Early tors where no one's running ads "
              'yet. CPA could be $300 to $1,800. But once an MDL is formed, science titans, '
              'firms flood the space, CPA hits 4K plus. Camp Llejun, we saw top six grand in '
              'late 2023.',
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': "CPM goes up, and your CPA can double. Early tors where no one's running ads yet. "
             'CPA could be $300 to $1,800. But once an MDL is formed, science titans, firms '
             'flood the space, CPA hits 4K plus. Camp Llejun, we saw top six grand in late '
             '2023.',
      'title': 'Mass Tort Cost Per Acquisition Breakdown: What You’re Doing Wrong (And How to '
               'Fix It) (Blue Sky Legal)',
      'url': 'https://www.youtube.com/watch?v=n9AQhSIMkNg&t=51s',
      'video_id': 'n9AQhSIMkNg'},
     {'author': 'Upchurch Watson White & Max Mediation Group',
      'channel': 'Upchurch Watson White & Max Mediation Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:22](https://www.youtube.com/watch?v=10ygaMXLKfM&t=142s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Behalf of your clients how do you estimate settlement values what are the tools '
              'that you use how do you tackle such a an unwieldy Beast how do we get to '
              'settlement already what happened to everything else.',
      'timestamp': 142,
      'timestamp_label': '[00:02:22]',
      'timestamp_seconds': 142,
      'tip': 'Behalf of your clients how do you estimate settlement values what are the tools '
             'that you use how do you tackle such a an unwieldy Beast how do we get to '
             'settlement already what happened to everything else.',
      'title': 'Utilizing MDL (Multi-District Litigation) to Resolve Class and Mass Actions '
               '(Upchurch Watson White & Max Mediation Group)',
      'url': 'https://www.youtube.com/watch?v=10ygaMXLKfM&t=142s',
      'video_id': '10ygaMXLKfM'},
     {'author': 'CERIS Health',
      'channel': 'CERIS Health',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:44:51](https://www.youtube.com/watch?v=Coka2u38__k&t=2691s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Out what technology is available to centralize the mrr process for the him '
              'department janie well of course the chartfast platform.',
      'timestamp': 2691,
      'timestamp_label': '[00:44:51]',
      'timestamp_seconds': 2691,
      'tip': 'Out what technology is available to centralize the mrr process for the him '
             'department janie well of course the chartfast platform.',
      'title': 'The Challenges of Medical Record Retrieval - AHIMA Fireside Chat (CERIS '
               'Health)',
      'url': 'https://www.youtube.com/watch?v=Coka2u38__k&t=2691s',
      'video_id': 'Coka2u38__k'},
     {'author': 'Justinian & Associates PLLC',
      'channel': 'Justinian & Associates PLLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:07](https://www.youtube.com/watch?v=mIB8iIDsWhY&t=67s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Everybody to work up those cases on their own for each case to be handled in a '
              "vacuum or in a box by itself because you'd end up spending lots of money.",
      'timestamp': 67,
      'timestamp_label': '[00:01:07]',
      'timestamp_seconds': 67,
      'tip': 'Everybody to work up those cases on their own for each case to be handled in a '
             "vacuum or in a box by itself because you'd end up spending lots of money.",
      'title': 'Multi-District Litigation (MDLs) (Justinian & Associates PLLC)',
      'url': 'https://www.youtube.com/watch?v=mIB8iIDsWhY&t=67s',
      'video_id': 'mIB8iIDsWhY'},
     {'author': 'Case Works',
      'channel': 'Case Works',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=My_I0OLHPXc&t=118s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The research that you Rec put together is really valuable and that people '
              'should definitely seek out that white paper one of the key data points you had.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': 'The research that you Rec put together is really valuable and that people should '
             'definitely seek out that white paper one of the key data points you had.',
      'title': 'Mastering Mass Torts: True Cost, Feedback Loops and Vendor Relationships '
               'featuring Devin Downey (Case Works)',
      'url': 'https://www.youtube.com/watch?v=My_I0OLHPXc&t=118s',
      'video_id': 'My_I0OLHPXc'},
     {'author': 'Jon and Marc',
      'channel': 'Jon and Marc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:26](https://www.youtube.com/watch?v=IUAtVEe81NI&t=446s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, this will keep rising, I think, as well in 2026. What is going on at number '
              "five with Roundup? The Power Rangers darling has fallen. It's coming in at "
              "number five. It's not to say, you know, people don't believe in this case. We "
              'still think this is a winner.',
      'timestamp': 446,
      'timestamp_label': '[00:07:26]',
      'timestamp_seconds': 446,
      'tip': 'So, this will keep rising, I think, as well in 2026. What is going on at number '
             "five with Roundup? The Power Rangers darling has fallen. It's coming in at "
             "number five. It's not to say, you know, people don't believe in this case. We "
             'still think this is a winner.',
      'title': 'Top 10 Mass Torts to Watch in 2026 | Power Rankings for Plaintiff Firms (Jon '
               'and Marc)',
      'url': 'https://www.youtube.com/watch?v=IUAtVEe81NI&t=446s',
      'video_id': 'IUAtVEe81NI'}],
 9: [{'author': "Legal Lead Sharks Podcast | K'Lee Terrazas",
      'channel': "Legal Lead Sharks Podcast | K'Lee Terrazas",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:10](https://www.youtube.com/watch?v=j80F3HgdRAw&t=190s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'It works for any legal vertical, but a missed call is a missed case. And when '
              "you're spending money on SEO, ads, marketing, branding, Google put out a report "
              "last year that said 28% of calls that came from the law firm's GBP went missed "
              'on the first attempt.',
      'timestamp': 190,
      'timestamp_label': '[00:03:10]',
      'timestamp_seconds': 190,
      'tip': 'It works for any legal vertical, but a missed call is a missed case. And when '
             "you're spending money on SEO, ads, marketing, branding, Google put out a report "
             "last year that said 28% of calls that came from the law firm's GBP went missed "
             'on the first attempt.',
      'title': 'Law Firms & Attorneys A Missed Call = A Missed Case. This AI Agent Fixes That '
               "(LIVE Demo) (Legal Lead Sharks Podcast | K'Lee Terrazas)",
      'url': 'https://www.youtube.com/watch?v=j80F3HgdRAw&t=190s',
      'video_id': 'j80F3HgdRAw'},
     {'author': 'Jackson LLP Healthcare Lawyers',
      'channel': 'Jackson LLP Healthcare Lawyers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:02](https://www.youtube.com/watch?v=wUqthLNx6Ro&t=122s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The management service agreement will be mindful of all the laws that apply to '
              'you, including things like Stark Law, Anti-Kickback Statute, False Claims Act, '
              'state fee-splitting provisions, and state Corporate Practice of Medicine '
              'doctrine.',
      'timestamp': 122,
      'timestamp_label': '[00:02:02]',
      'timestamp_seconds': 122,
      'tip': 'The management service agreement will be mindful of all the laws that apply to '
             'you, including things like Stark Law, Anti-Kickback Statute, False Claims Act, '
             'state fee-splitting provisions, and state Corporate Practice of Medicine '
             'doctrine.',
      'title': 'MSO (Management Services Organization) Basics | Jackson LLP Healthcare '
               'Attorneys (Jackson LLP Healthcare Lawyers)',
      'url': 'https://www.youtube.com/watch?v=wUqthLNx6Ro&t=122s',
      'video_id': 'wUqthLNx6Ro'},
     {'author': 'Confido Legal',
      'channel': 'Confido Legal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:57](https://www.youtube.com/watch?v=5TjsKzLtyc4&t=897s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'ABA, but are adopted on a state-by-state level by the Supreme Court of each '
              'particular state. Um and so each Supreme Court looks at the rules, you know, '
              'adopts them in whole or in part or with modifications.',
      'timestamp': 897,
      'timestamp_label': '[00:14:57]',
      'timestamp_seconds': 897,
      'tip': 'ABA, but are adopted on a state-by-state level by the Supreme Court of each '
             'particular state. Um and so each Supreme Court looks at the rules, you know, '
             'adopts them in whole or in part or with modifications.',
      'title': 'Ep 70 - Private Equity, MSOs, and the Ethics of Law Firm Ownership (Confido '
               'Legal)',
      'url': 'https://www.youtube.com/watch?v=5TjsKzLtyc4&t=897s',
      'video_id': '5TjsKzLtyc4'},
     {'author': 'Dike Law Group | Texas Healthcare Law',
      'channel': 'Dike Law Group | Texas Healthcare Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:27](https://www.youtube.com/watch?v=aZDpDRV6-KA&t=147s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Really really interested in starting a healthcare organization give me a call '
              "I'll be glad to help you I'll walk you through your State's corporate practice "
              "and Medicine statutes and I'll draft you an MSO that will buy by your state law "
              'thanks so much bye.',
      'timestamp': 147,
      'timestamp_label': '[00:02:27]',
      'timestamp_seconds': 147,
      'tip': 'Really really interested in starting a healthcare organization give me a call '
             "I'll be glad to help you I'll walk you through your State's corporate practice "
             "and Medicine statutes and I'll draft you an MSO that will buy by your state law "
             'thanks so much bye.',
      'title': 'Management Services Organization(MSO) w/ Texas Healthcare Business Attorney. '
               '(Dike Law Group | Texas Healthcare Law)',
      'url': 'https://www.youtube.com/watch?v=aZDpDRV6-KA&t=147s',
      'video_id': 'aZDpDRV6-KA'},
     {'author': 'Lawsuit Tracker',
      'channel': 'Lawsuit Tracker',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=tVouqZmWW5I&t=72s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I listed first are the only injuries that we can file in federal court for this '
              'case. Some law firms are still taking tier 2 injuries, especially prostate '
              'cancer. Many legal experts believe that this is the next injury the judge will '
              'allow to be added.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': 'I listed first are the only injuries that we can file in federal court for this '
             'case. Some law firms are still taking tier 2 injuries, especially prostate '
             'cancer. Many legal experts believe that this is the next injury the judge will '
             'allow to be added.',
      'title': 'MILITARY WATER CONTAMINATION LAWSUIT AKA AFFF MDL OVERVIEW (Lawsuit Tracker)',
      'url': 'https://www.youtube.com/watch?v=tVouqZmWW5I&t=72s',
      'video_id': 'tVouqZmWW5I'},
     {'author': 'LegalTechLIVE',
      'channel': 'LegalTechLIVE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:53](https://www.youtube.com/watch?v=ajveDNkk7dg&t=1433s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Singular laws is in good standing with the state bar you know all that sort of '
              "thing so that's our promise to the customer.",
      'timestamp': 1433,
      'timestamp_label': '[00:23:53]',
      'timestamp_seconds': 1433,
      'tip': 'Singular laws is in good standing with the state bar you know all that sort of '
             "thing so that's our promise to the customer.",
      'title': 'Allen Rodriguez President of Arizona ABS Law Firm Singular Law Group - '
               'LegalTechLIVE - Ep. 131 (LegalTechLIVE)',
      'url': 'https://www.youtube.com/watch?v=ajveDNkk7dg&t=1433s',
      'video_id': 'ajveDNkk7dg'},
     {'author': 'Holt Law: For Healthcare Businesses',
      'channel': 'Holt Law: For Healthcare Businesses',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:41](https://www.youtube.com/watch?v=Oa-6OBD0Gak&t=281s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "From a legal perspective, there's this big contract called the management "
              'service agreement. It essentially outlines the responsibility of the two '
              'entities. So, it\'s saying, "Hey, medical practice, you\'re going to stick to '
              'doing clinical things.',
      'timestamp': 281,
      'timestamp_label': '[00:04:41]',
      'timestamp_seconds': 281,
      'tip': "From a legal perspective, there's this big contract called the management "
             'service agreement. It essentially outlines the responsibility of the two '
             'entities. So, it\'s saying, "Hey, medical practice, you\'re going to stick to '
             'doing clinical things.',
      'title': 'Understanding MSOs: The Structure Behind Modern Clinics (Holt Law: For '
               'Healthcare Businesses)',
      'url': 'https://www.youtube.com/watch?v=Oa-6OBD0Gak&t=281s',
      'video_id': 'Oa-6OBD0Gak'},
     {'author': 'OffshoreAlert',
      'channel': 'OffshoreAlert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:40:44](https://www.youtube.com/watch?v=rQPZlRgHcfE&t=2444s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Case I think it would be an odd thing for a judge to own stock in Burford but '
              'you know clearly there should be you know the purpose that we have in the US '
              'for disclosure yes exactly.',
      'timestamp': 2444,
      'timestamp_label': '[00:40:44]',
      'timestamp_seconds': 2444,
      'tip': 'Case I think it would be an odd thing for a judge to own stock in Burford but '
             'you know clearly there should be you know the purpose that we have in the US for '
             'disclosure yes exactly.',
      'title': 'How Litigation Funding Is Shaking Up The Legal Industry (OffshoreAlert)',
      'url': 'https://www.youtube.com/watch?v=rQPZlRgHcfE&t=2444s',
      'video_id': 'rQPZlRgHcfE'},
     {'author': 'Jersey Justice Podcast',
      'channel': 'Jersey Justice Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:07](https://www.youtube.com/watch?v=HrjoNgJuhLU&t=427s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'All it means is every case filed in the state of New Jersey gets assigned to '
              'one judge >> Yeah. Just like in federal court, every case filed in any district '
              'in the country gets sent to one judge. In pelvic mesh it was a judge in the '
              'Southern District of West Virginia.',
      'timestamp': 427,
      'timestamp_label': '[00:07:07]',
      'timestamp_seconds': 427,
      'tip': 'All it means is every case filed in the state of New Jersey gets assigned to one '
             'judge >> Yeah. Just like in federal court, every case filed in any district in '
             'the country gets sent to one judge. In pelvic mesh it was a judge in the '
             'Southern District of West Virginia.',
      'title': 'Jersey Justice w/ Adam M. Slater, Esq. | Episode 75 | Taking On Giants: Mass '
               'Torts, Trial Law, & AI (Jersey Justice Podcast)',
      'url': 'https://www.youtube.com/watch?v=HrjoNgJuhLU&t=427s',
      'video_id': 'HrjoNgJuhLU'},
     {'author': 'The Future Is Bright Podcast',
      'channel': 'The Future Is Bright Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:23](https://www.youtube.com/watch?v=wXttJe-HCVM&t=23s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Do they comply with the ABA rule 5. So, welcome everyone to the Future is '
              'Bright podcast. My name is Chris Bats and my co-host Howard Rosenberg. Howard '
              'and I are at the epicenter of law firm talent and strategic growth here in New '
              'York City and the UK.',
      'timestamp': 23,
      'timestamp_label': '[00:00:23]',
      'timestamp_seconds': 23,
      'tip': 'Do they comply with the ABA rule 5. So, welcome everyone to the Future is Bright '
             'podcast. My name is Chris Bats and my co-host Howard Rosenberg. Howard and I are '
             'at the epicenter of law firm talent and strategic growth here in New York City '
             'and the UK.',
      'title': 'Law Firms, PE, and MSOs: A Legal Ethics Conversation with Lucian Pera (The '
               'Future Is Bright Podcast)',
      'url': 'https://www.youtube.com/watch?v=wXttJe-HCVM&t=23s',
      'video_id': 'wXttJe-HCVM'},
     {'author': 'The Brandi Law Firm',
      'channel': 'The Brandi Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=luVb2J9MsQk&t=40s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s still an individual lawsuit filed on behalf of each one. But because there's "
              'so many, and because they have similar information that needs to be disclosed '
              'in each case all the cases from around the state are put into the same '
              "courtroom, it's for efficiency purposes.",
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': "'s still an individual lawsuit filed on behalf of each one. But because there's "
             'so many, and because they have similar information that needs to be disclosed in '
             'each case all the cases from around the state are put into the same courtroom, '
             "it's for efficiency purposes.",
      'title': 'What Is The Difference Between A Class Action, Mass Tort, and Individual '
               'Personal Injury Action? (The Brandi Law Firm)',
      'url': 'https://www.youtube.com/watch?v=luVb2J9MsQk&t=40s',
      'video_id': 'luVb2J9MsQk'},
     {'author': 'Milestone',
      'channel': 'Milestone',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=1O2RKMH06LU&t=15s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "To unravel the world of AI and to discuss it'll affect the legal profession "
              'today I am joined with Carol wall an attorney and partner at the law.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "To unravel the world of AI and to discuss it'll affect the legal profession "
             'today I am joined with Carol wall an attorney and partner at the law.',
      'title': 'AI Lawyers and the Evolution of Mass Torts feat. Cara Wall | Law, AI & Money '
               'Ep. 12 (Milestone)',
      'url': 'https://www.youtube.com/watch?v=1O2RKMH06LU&t=15s',
      'video_id': '1O2RKMH06LU'},
     {'author': 'Case Works',
      'channel': 'Case Works',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:26](https://www.youtube.com/watch?v=oc04hOYvUBA&t=26s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Calls legal calls are case Originators who specialize detailed interviews of '
              'potential claimants including documentation and medical record.',
      'timestamp': 26,
      'timestamp_label': '[00:00:26]',
      'timestamp_seconds': 26,
      'tip': 'Calls legal calls are case Originators who specialize detailed interviews of '
             'potential claimants including documentation and medical record.',
      'title': '💰Global Settlement for Bard Hernia Mesh, AFF lawsuit updates and another new '
               'MDL on the horizon? (Case Works)',
      'url': 'https://www.youtube.com/watch?v=oc04hOYvUBA&t=26s',
      'video_id': 'oc04hOYvUBA'},
     {'author': 'Jon and Marc',
      'channel': 'Jon and Marc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=3Qxw8dtCCns&t=35s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'t really operate that way. We build acquisition systems while staying tactic "
              "agnostic about how they get there. So, we're not going to force your law firm "
              'into whatever the agency happens to sell.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': "'t really operate that way. We build acquisition systems while staying tactic "
             "agnostic about how they get there. So, we're not going to force your law firm "
             'into whatever the agency happens to sell.',
      'title': 'The 4 Mass Tort Developments Plaintiff Firms Should Be Watching | Tort Talk '
               '(Jon and Marc)',
      'url': 'https://www.youtube.com/watch?v=3Qxw8dtCCns&t=35s',
      'video_id': '3Qxw8dtCCns'},
     {'author': 'Case Works',
      'channel': 'Case Works',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=or3TWPA-tro&t=21s)',
      'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                   'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                   'co-ventures, paid-media plaintiff intake, and automated `45 CFR § 164.524` '
                   'HITECH electronic medical-record (`EMR`) triage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'We are continuing our series talking to thought leaders in the legal space '
              'today being joined by susan barfield ceo of caseworks and chris princess vp of '
              'sales at consumer attorney marketing group thank you both for joining us today '
              'thank you john thanks jim.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'We are continuing our series talking to thought leaders in the legal space today '
             'being joined by susan barfield ceo of caseworks and chris princess vp of sales '
             'at consumer attorney marketing group thank you both for joining us today thank '
             'you john thanks jim.',
      'title': 'Three Optimal Moments To Seek Mass Tort Clients (Case Works)',
      'url': 'https://www.youtube.com/watch?v=or3TWPA-tro&t=21s',
      'video_id': 'or3TWPA-tro'}],
 10: [{'author': 'tortshark',
       'channel': 'tortshark',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:42](https://www.youtube.com/watch?v=7Jbuob_1a-Y&t=42s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': '10,000 signed cases under his belt. We realized if we combined the best of '
               "both worlds, we could create something that's never been done before. A "
               "category of one, an AI first, best-in-class case acquisition engine that's "
               'unmatched in the industry.',
       'timestamp': 42,
       'timestamp_label': '[00:00:42]',
       'timestamp_seconds': 42,
       'tip': '10,000 signed cases under his belt. We realized if we combined the best of both '
              "worlds, we could create something that's never been done before. A category of "
              "one, an AI first, best-in-class case acquisition engine that's unmatched in the "
              'industry.',
       'title': 'TortShark Mass Tort Marketing Explainer Video (tortshark)',
       'url': 'https://www.youtube.com/watch?v=7Jbuob_1a-Y&t=42s',
       'video_id': '7Jbuob_1a-Y'},
      {'author': 'The PE Podcast',
       'channel': 'The PE Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:47](https://www.youtube.com/watch?v=R60PdSP1C24&t=47s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s making it all change is also the thing that's creating all of the value "
               'here. So, first of all, the cost of firms are being reduced 80-90% plus right '
               'now as we speak due to AI workflow automation.',
       'timestamp': 47,
       'timestamp_label': '[00:00:47]',
       'timestamp_seconds': 47,
       'tip': "'s making it all change is also the thing that's creating all of the value "
              'here. So, first of all, the cost of firms are being reduced 80-90% plus right '
              'now as we speak due to AI workflow automation.',
       'title': 'What is a law firm MSO? | Joe Prencipe (The PE Podcast)',
       'url': 'https://www.youtube.com/watch?v=R60PdSP1C24&t=47s',
       'video_id': 'R60PdSP1C24'},
      {'author': "Legal Lead Sharks Podcast | K'Lee Terrazas",
       'channel': "Legal Lead Sharks Podcast | K'Lee Terrazas",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:10](https://www.youtube.com/watch?v=e67Bx9d5FBc&t=70s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'No matter how many times I had worked with call centers to try to train them '
               'on the intake cadence that we needed for Google ads and converting those, we '
               'always just got okay service. One of the big benefits to the AI agents outside '
               'of the fact that they can work 24/7.',
       'timestamp': 70,
       'timestamp_label': '[00:01:10]',
       'timestamp_seconds': 70,
       'tip': 'No matter how many times I had worked with call centers to try to train them on '
              'the intake cadence that we needed for Google ads and converting those, we '
              'always just got okay service. One of the big benefits to the AI agents outside '
              'of the fact that they can work 24/7.',
       'title': 'Why Traditional Call Centers Are Failing Law Firms 2026 (Legal Lead Sharks '
                "Podcast | K'Lee Terrazas)",
       'url': 'https://www.youtube.com/watch?v=e67Bx9d5FBc&t=70s',
       'video_id': 'e67Bx9d5FBc'},
      {'author': 'Business Solution',
       'channel': 'Business Solution',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:18:59](https://www.youtube.com/watch?v=zTi3ftvnsY0&t=1139s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Now, as a little bit of a teaser trailer here, you might notice these lovely, '
               'I like to call them lilac stars. These are for our AI capabilities within '
               'Filevine.',
       'timestamp': 1139,
       'timestamp_label': '[00:18:59]',
       'timestamp_seconds': 1139,
       'tip': 'Now, as a little bit of a teaser trailer here, you might notice these lovely, I '
              'like to call them lilac stars. These are for our AI capabilities within '
              'Filevine.',
       'title': 'Filevine Demo & Tutorial: #1 Case Management Software for Legal Teams '
                '(Business Solution)',
       'url': 'https://www.youtube.com/watch?v=zTi3ftvnsY0&t=1139s',
       'video_id': 'zTi3ftvnsY0'},
      {'author': 'Daya Naef',
       'channel': 'Daya Naef',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:16](https://www.youtube.com/watch?v=1QCGIBQ7PQI&t=616s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Well within Excel um so various ways I can look at this another way that kind '
               "of our AI fields and of course I'm going to call out these items exist within.",
       'timestamp': 616,
       'timestamp_label': '[00:10:16]',
       'timestamp_seconds': 616,
       'tip': 'Well within Excel um so various ways I can look at this another way that kind '
              "of our AI fields and of course I'm going to call out these items exist within.",
       'title': 'Filevine AI Demo: Revolutionizing Legal Case Management with AI-Powered Tools '
                '(Daya Naef)',
       'url': 'https://www.youtube.com/watch?v=1QCGIBQ7PQI&t=616s',
       'video_id': '1QCGIBQ7PQI'},
      {'author': 'Vineskills',
       'channel': 'Vineskills',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:50:03](https://www.youtube.com/watch?v=oNoHY7832hw&t=3003s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Um, definitely reach out to us if you have more questions and um, you know, '
               "book a discovery call and and show us what you're into, what you're interested "
               "in building and um, we'll give you ideas and we can um, we can hopefully help.",
       'timestamp': 3003,
       'timestamp_label': '[00:50:03]',
       'timestamp_seconds': 3003,
       'tip': 'Um, definitely reach out to us if you have more questions and um, you know, '
              "book a discovery call and and show us what you're into, what you're interested "
              "in building and um, we'll give you ideas and we can um, we can hopefully help.",
       'title': '[Webinar Replay] From Manual to Automated: Real Filevine + Zapier Workflows '
                'for Legal Teams (Vineskills)',
       'url': 'https://www.youtube.com/watch?v=oNoHY7832hw&t=3003s',
       'video_id': 'oNoHY7832hw'},
      {'author': 'The Law Firm Brand Builders',
       'channel': 'The Law Firm Brand Builders',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:46](https://www.youtube.com/watch?v=73xfuxsKsEM&t=766s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So the Lit Portal that's the is that the patented AI technology that >> Yeah, "
               'yeah, it is. Yeah, Lit Portal is a patented AI technology. It serves as our '
               "business engine. It's actually running our work behind the scenes.",
       'timestamp': 766,
       'timestamp_label': '[00:12:46]',
       'timestamp_seconds': 766,
       'tip': "So the Lit Portal that's the is that the patented AI technology that >> Yeah, "
              'yeah, it is. Yeah, Lit Portal is a patented AI technology. It serves as our '
              "business engine. It's actually running our work behind the scenes.",
       'title': 'Healthcare Liens Explained: Resolving Complex Mass Tort Settlements | Ft. '
                'Michelle Prince (The Law Firm Brand Builders)',
       'url': 'https://www.youtube.com/watch?v=73xfuxsKsEM&t=766s',
       'video_id': '73xfuxsKsEM'},
      {'author': 'King Law',
       'channel': 'King Law',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:47](https://www.youtube.com/watch?v=Is4DHXZ5JIM&t=107s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So it's not like a car accident case where you reach a settlement and you're "
               'going to get $100,000. You sign the release two weeks later, you get the '
               "check. This is a little different than that. And that's because you're dealing "
               'with thousands of people at once.',
       'timestamp': 107,
       'timestamp_label': '[00:01:47]',
       'timestamp_seconds': 107,
       'tip': "So it's not like a car accident case where you reach a settlement and you're "
              'going to get $100,000. You sign the release two weeks later, you get the check. '
              "This is a little different than that. And that's because you're dealing with "
              'thousands of people at once.',
       'title': 'Hernia Mesh Lawsuit Update (February 2025) (King Law)',
       'url': 'https://www.youtube.com/watch?v=Is4DHXZ5JIM&t=107s',
       'video_id': 'Is4DHXZ5JIM'},
      {'author': 'Answering Legal, Inc.',
       'channel': 'Answering Legal, Inc.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:15](https://www.youtube.com/watch?v=2az9KaozXKQ&t=255s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Like why do how can firms start the process of putting an intake script and '
               'like form and just whole process in place. So what you really have to do is '
               'take each call and identify the goals, right?',
       'timestamp': 255,
       'timestamp_label': '[00:04:15]',
       'timestamp_seconds': 255,
       'tip': 'Like why do how can firms start the process of putting an intake script and '
              'like form and just whole process in place. So what you really have to do is '
              'take each call and identify the goals, right?',
       'title': 'Legal Intake 101: Scripts, Strategy & Sales You’re Ignoring (Answering Legal, '
                'Inc.)',
       'url': 'https://www.youtube.com/watch?v=2az9KaozXKQ&t=255s',
       'video_id': '2az9KaozXKQ'},
      {'author': 'Advanced Affiliate',
       'channel': 'Advanced Affiliate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:36:07](https://www.youtube.com/watch?v=Tt2FvNxVuCs&t=2167s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Everyone's like oh I'm so excited I'm jumping on a call with a rep I'm like "
               "you're probably going to be let down they're going to tell you some [ __ ].",
       'timestamp': 2167,
       'timestamp_label': '[00:36:07]',
       'timestamp_seconds': 2167,
       'tip': "Everyone's like oh I'm so excited I'm jumping on a call with a rep I'm like "
              "you're probably going to be let down they're going to tell you some [ __ ].",
       'title': 'EP 117: Mass Tort Exposed! How To Scale Legal Lead Generation With John Casto '
                '(Advanced Affiliate)',
       'url': 'https://www.youtube.com/watch?v=Tt2FvNxVuCs&t=2167s',
       'video_id': 'Tt2FvNxVuCs'},
      {'author': 'Jon and Marc',
       'channel': 'Jon and Marc',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:21](https://www.youtube.com/watch?v=7TfOtDaTez8&t=741s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I hope to see in my lifetime and I hope this is a positive trend towards that. '
               'All right, moving on to number three. Depo-Provera, cracking the top three. '
               'The rocket docket, as we call it, is moving full speed ahead to the Daubert '
               'hearing at the end of June.',
       'timestamp': 741,
       'timestamp_label': '[00:12:21]',
       'timestamp_seconds': 741,
       'tip': 'I hope to see in my lifetime and I hope this is a positive trend towards that. '
              'All right, moving on to number three. Depo-Provera, cracking the top three. The '
              'rocket docket, as we call it, is moving full speed ahead to the Daubert hearing '
              'at the end of June.',
       'title': 'Mass Tort Power Rankings: The "Rocket Docket" Surges & A Game-Changing $27M '
                'Precedent (Jon and Marc)',
       'url': 'https://www.youtube.com/watch?v=7TfOtDaTez8&t=741s',
       'video_id': '7TfOtDaTez8'},
      {'author': 'CorporateAttorneysCA',
       'channel': 'CorporateAttorneysCA',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:26](https://www.youtube.com/watch?v=cTWDG8n6ks0&t=146s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Following physician-owned MSO non-physician owned MSO and hybrid MSO which is '
               'owned by both physician and non-physician hospitals or larger Healthcare '
               'Systems may also own msos to provide centralized administrative support to '
               'their Affiliated.',
       'timestamp': 146,
       'timestamp_label': '[00:02:26]',
       'timestamp_seconds': 146,
       'tip': 'Following physician-owned MSO non-physician owned MSO and hybrid MSO which is '
              'owned by both physician and non-physician hospitals or larger Healthcare '
              'Systems may also own msos to provide centralized administrative support to '
              'their Affiliated.',
       'title': 'Exploring the Role of MSO in Healthcare: What is MSO in Healthcare in '
                'California? (CorporateAttorneysCA)',
       'url': 'https://www.youtube.com/watch?v=cTWDG8n6ks0&t=146s',
       'video_id': 'cTWDG8n6ks0'},
      {'author': 'Dolman Law Group',
       'channel': 'Dolman Law Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:05](https://www.youtube.com/watch?v=qGQGuFYFCF8&t=65s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And based on the outcomes of those verdicts, you typically will reach a '
               'settlement matrix. So at the end of the day, a settlement matrix takes into '
               'account all of the various different factors that people think go into valuing '
               'a particular multid-district litigation case.',
       'timestamp': 65,
       'timestamp_label': '[00:01:05]',
       'timestamp_seconds': 65,
       'tip': 'And based on the outcomes of those verdicts, you typically will reach a '
              'settlement matrix. So at the end of the day, a settlement matrix takes into '
              'account all of the various different factors that people think go into valuing '
              'a particular multid-district litigation case.',
       'title': 'Mass tort cases are decided by a single trial with all victims (Dolman Law '
                'Group)',
       'url': 'https://www.youtube.com/watch?v=qGQGuFYFCF8&t=65s',
       'video_id': 'qGQGuFYFCF8'},
      {'author': 'Schuler, Weisser, Zoeller, Overbeck & Baxter P.A.',
       'channel': 'Schuler, Weisser, Zoeller, Overbeck & Baxter P.A.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:52](https://www.youtube.com/watch?v=zCygMrcjoOQ&t=112s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Fit within the grid the people in those cases that weren't tried if they opt "
               'into the settlement then they have to fit into a grid and depending on where '
               "they fit in that grid that's how much money they're going to get so it's not "
               'as individualized.',
       'timestamp': 112,
       'timestamp_label': '[00:01:52]',
       'timestamp_seconds': 112,
       'tip': "Fit within the grid the people in those cases that weren't tried if they opt "
              'into the settlement then they have to fit into a grid and depending on where '
              "they fit in that grid that's how much money they're going to get so it's not as "
              'individualized.',
       'title': 'How are plaintiffs compensated in a mass tort case? (Schuler, Weisser, '
                'Zoeller, Overbeck & Baxter P.A.)',
       'url': 'https://www.youtube.com/watch?v=zCygMrcjoOQ&t=112s',
       'video_id': 'zCygMrcjoOQ'},
      {'author': 'Saad Khan | AI Automation',
       'channel': 'Saad Khan | AI Automation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:41](https://www.youtube.com/watch?v=ZkN7hMCBwmQ&t=41s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'We shift your firm from passive software to a fully agentic AI workflow. The '
               'result, zero speed to lead response times. Instead of your team scrambling to '
               'call back during business hours, the system operates 24/7/365.',
       'timestamp': 41,
       'timestamp_label': '[00:00:41]',
       'timestamp_seconds': 41,
       'tip': 'We shift your firm from passive software to a fully agentic AI workflow. The '
              'result, zero speed to lead response times. Instead of your team scrambling to '
              'call back during business hours, the system operates 24/7/365.',
       'title': 'How Mass Tort Law Firms save $30,000+ / month Using AI Voice Agents | '
                'Blueprint Explained (Saad Khan | AI Automation)',
       'url': 'https://www.youtube.com/watch?v=ZkN7hMCBwmQ&t=41s',
       'video_id': 'ZkN7hMCBwmQ'}],
 11: [{'author': "Legal Lead Sharks Podcast | K'Lee Terrazas",
       'channel': "Legal Lead Sharks Podcast | K'Lee Terrazas",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:22:53](https://www.youtube.com/watch?v=lW3uPdauQrA&t=1373s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "You know, you'll be hearing from our legal team within 24 hours. So they first "
               'speak with the pre-litigation parallegal, which some firms call a case '
               "manager, and then within 48 hours, they'll hear from the pre-suit attorney.",
       'timestamp': 1373,
       'timestamp_label': '[00:22:53]',
       'timestamp_seconds': 1373,
       'tip': "You know, you'll be hearing from our legal team within 24 hours. So they first "
              'speak with the pre-litigation parallegal, which some firms call a case manager, '
              "and then within 48 hours, they'll hear from the pre-suit attorney.",
       'title': 'Scaling a Personal Injury Law Firm with Systems, Intake, and $38M in Wins | '
                "Lawyer Up (Legal Lead Sharks Podcast | K'Lee Terrazas)",
       'url': 'https://www.youtube.com/watch?v=lW3uPdauQrA&t=1373s',
       'video_id': 'lW3uPdauQrA'},
      {'author': 'How to Simple',
       'channel': 'How to Simple',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:51](https://www.youtube.com/watch?v=3bh0rzq79u8&t=111s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Measuring and improving their operations so if we click on this what is L by '
               'question it should give us a nice most uh video or uh what do you call this '
               'introduction video about litify so you can see litify demo a powerful legal '
               'operating solution and business.',
       'timestamp': 111,
       'timestamp_label': '[00:01:51]',
       'timestamp_seconds': 111,
       'tip': 'Measuring and improving their operations so if we click on this what is L by '
              'question it should give us a nice most uh video or uh what do you call this '
              'introduction video about litify so you can see litify demo a powerful legal '
              'operating solution and business.',
       'title': 'Litify Tutorial for Beginners | Legal Practice Management 2025 (How to '
                'Simple)',
       'url': 'https://www.youtube.com/watch?v=3bh0rzq79u8&t=111s',
       'video_id': '3bh0rzq79u8'},
      {'author': 'On The Docket with Napoli Shkolnik',
       'channel': 'On The Docket with Napoli Shkolnik',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:24](https://www.youtube.com/watch?v=p519y7c1was&t=564s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Um this uh in environmental law, the it's very science-driven. So so you have "
               "to be you have to be sure that you're able to prove causation and that the "
               'science has evolved sufficiently in order for you to be able to prove a case.',
       'timestamp': 564,
       'timestamp_label': '[00:09:24]',
       'timestamp_seconds': 564,
       'tip': "Um this uh in environmental law, the it's very science-driven. So so you have "
              "to be you have to be sure that you're able to prove causation and that the "
              'science has evolved sufficiently in order for you to be able to prove a case.',
       'title': 'Inside the Making of A Mass Tort  | Coral M. Odiot-Rivera & Silvino John Diaz '
                '(On The Docket with Napoli Shkolnik)',
       'url': 'https://www.youtube.com/watch?v=p519y7c1was&t=564s',
       'video_id': 'p519y7c1was'},
      {'author': 'CaptureBilling',
       'channel': 'CaptureBilling',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:25](https://www.youtube.com/watch?v=GzeUKKWvC0o&t=25s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Contained within it's pages is new legislation known as the Health Information "
               "Technology for Economic and Clinical Help Act That's a mouthful so we'll just "
               'call it the HITECH Act. So what exactly is the HITECH Act; and how does it '
               'affect you, a physician?',
       'timestamp': 25,
       'timestamp_label': '[00:00:25]',
       'timestamp_seconds': 25,
       'tip': "Contained within it's pages is new legislation known as the Health Information "
              "Technology for Economic and Clinical Help Act That's a mouthful so we'll just "
              'call it the HITECH Act. So what exactly is the HITECH Act; and how does it '
              'affect you, a physician?',
       'title': 'The HITECH Act: Electronic Health Records and Meaningful Use (CaptureBilling)',
       'url': 'https://www.youtube.com/watch?v=GzeUKKWvC0o&t=25s',
       'video_id': 'GzeUKKWvC0o'},
      {'author': 'LF Advisers - All Things Litigation Funding',
       'channel': 'LF Advisers - All Things Litigation Funding',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:21:57](https://www.youtube.com/watch?v=4PHHiyG2S5k&t=1317s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "All right, now let's talk about um I want to talk about that case because "
               'people would probably watch this and say, "Oh, this hedge fund manager is '
               'trying to get rich off this money, blah blah blah blah.".',
       'timestamp': 1317,
       'timestamp_label': '[00:21:57]',
       'timestamp_seconds': 1317,
       'tip': "All right, now let's talk about um I want to talk about that case because "
              'people would probably watch this and say, "Oh, this hedge fund manager is '
              'trying to get rich off this money, blah blah blah blah.".',
       'title': 'James Koutoulas - Juris Trade (LF Advisers - All Things Litigation Funding)',
       'url': 'https://www.youtube.com/watch?v=4PHHiyG2S5k&t=1317s',
       'video_id': '4PHHiyG2S5k'},
      {'author': 'Chaffin Luhana LLP Injury Lawyers',
       'channel': 'Chaffin Luhana LLP Injury Lawyers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:37](https://www.youtube.com/watch?v=5cou1UWhrYw&t=37s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'That team is with lawyers paralegals assistants who you know will work on your '
               "case we get to know your story we want to know what's happened to you what are "
               'your injuries what are the extent of those injuries and really how has that '
               'impacted your life.',
       'timestamp': 37,
       'timestamp_label': '[00:00:37]',
       'timestamp_seconds': 37,
       'tip': 'That team is with lawyers paralegals assistants who you know will work on your '
              "case we get to know your story we want to know what's happened to you what are "
              'your injuries what are the extent of those injuries and really how has that '
              'impacted your life.',
       'title': 'What happens during my Mass Tort case? | Chaffin Luhana (Chaffin Luhana LLP '
                'Injury Lawyers)',
       'url': 'https://www.youtube.com/watch?v=5cou1UWhrYw&t=37s',
       'video_id': '5cou1UWhrYw'},
      {'author': 'Modern Legal Ops | Building a tech forward firm',
       'channel': 'Modern Legal Ops | Building a tech forward firm',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:16](https://www.youtube.com/watch?v=jycz9TsdE9w&t=76s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And ultimately, that's what led to our our our slowdown. Now that we're able "
               "to track that, we're able to measure that, we're able to respond accordingly. "
               'Work with your intake team, look at your internal operations and determine '
               'what are the things that we need to measure.',
       'timestamp': 76,
       'timestamp_label': '[00:01:16]',
       'timestamp_seconds': 76,
       'tip': "And ultimately, that's what led to our our our slowdown. Now that we're able to "
              "track that, we're able to measure that, we're able to respond accordingly. Work "
              'with your intake team, look at your internal operations and determine what are '
              'the things that we need to measure.',
       'title': 'The Intake Bottleneck We Were Missing #legaloperations #lawfirmmarketing '
                '(Modern Legal Ops | Building a tech forward firm)',
       'url': 'https://www.youtube.com/watch?v=jycz9TsdE9w&t=76s',
       'video_id': 'jycz9TsdE9w'},
      {'author': 'Brown Rudnick LLP',
       'channel': 'Brown Rudnick LLP',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:26:02](https://www.youtube.com/watch?v=QpKDhqASBqM&t=1562s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'That in order to fund cases that may not otherwise be fundable at that stage '
               'as Chris mentioned start new business lines hire new people open new offices '
               'all of.',
       'timestamp': 1562,
       'timestamp_label': '[00:26:02]',
       'timestamp_seconds': 1562,
       'tip': 'That in order to fund cases that may not otherwise be fundable at that stage as '
              'Chris mentioned start new business lines hire new people open new offices all '
              'of.',
       'title': 'Portfolio and Law Firm Financing - European Litigation Funding Conference '
                '2023 (Brown Rudnick LLP)',
       'url': 'https://www.youtube.com/watch?v=QpKDhqASBqM&t=1562s',
       'video_id': 'QpKDhqASBqM'},
      {'author': 'Carlton Fields',
       'channel': 'Carlton Fields',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:28](https://www.youtube.com/watch?v=ieQJBTxA0z4&t=268s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'That can be adopted from the habits of really good team members and '
               'implemented on a broader scale so those are very important and one thing.',
       'timestamp': 268,
       'timestamp_label': '[00:04:28]',
       'timestamp_seconds': 268,
       'tip': 'That can be adopted from the habits of really good team members and implemented '
              'on a broader scale so those are very important and one thing.',
       'title': 'Tips and Strategies for Successful Mass Tort Management (Carlton Fields)',
       'url': 'https://www.youtube.com/watch?v=ieQJBTxA0z4&t=268s',
       'video_id': 'ieQJBTxA0z4'},
      {'author': 'Milestone',
       'channel': 'Milestone',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:23:04](https://www.youtube.com/watch?v=Y7FbfNp9_X4&t=1384s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Back to your team or or your whoever is your I.T provider or your case '
               'management system and say hey I heard this great idea could we do that here.',
       'timestamp': 1384,
       'timestamp_label': '[00:23:04]',
       'timestamp_seconds': 1384,
       'tip': 'Back to your team or or your whoever is your I.T provider or your case '
              'management system and say hey I heard this great idea could we do that here.',
       'title': 'Work Smarter Not Harder: Leveraging Tech to Modernize Your Mass Tort Practice '
                '(Milestone)',
       'url': 'https://www.youtube.com/watch?v=Y7FbfNp9_X4&t=1384s',
       'video_id': 'Y7FbfNp9_X4'},
      {'author': 'Errol Janusz',
       'channel': 'Errol Janusz',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:00](https://www.youtube.com/watch?v=mfKVI7JPrYc&t=60s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And the reason for this is when you come in and you complete your task and '
               "then you add a subsequent task. So, I've completed my test task here and I "
               'want to subtask Ivan on my team to now do something else. That task is now '
               'transferred.',
       'timestamp': 60,
       'timestamp_label': '[00:01:00]',
       'timestamp_seconds': 60,
       'tip': 'And the reason for this is when you come in and you complete your task and then '
              "you add a subsequent task. So, I've completed my test task here and I want to "
              'subtask Ivan on my team to now do something else. That task is now transferred.',
       'title': 'Filevine Demo for Law Offices (2026 Edition) (Errol Janusz)',
       'url': 'https://www.youtube.com/watch?v=mfKVI7JPrYc&t=60s',
       'video_id': 'mfKVI7JPrYc'},
      {'author': 'NYU School of Law',
       'channel': 'NYU School of Law',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:45](https://www.youtube.com/watch?v=tAaeP6Z-hK0&t=585s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'There is an article by Judith Resnik, one of our graduates, also, who argues '
               'that the class action is, in effect, a public subsidy for certain kinds of '
               'litigation because it lowers the transaction cost of creating the benefits and '
               'scale. This is going one step further.',
       'timestamp': 585,
       'timestamp_label': '[00:09:45]',
       'timestamp_seconds': 585,
       'tip': 'There is an article by Judith Resnik, one of our graduates, also, who argues '
              'that the class action is, in effect, a public subsidy for certain kinds of '
              'litigation because it lowers the transaction cost of creating the benefits and '
              'scale. This is going one step further.',
       'title': '2015 Fall Conference: Litigation Funding: Panel 3 (NYU School of Law)',
       'url': 'https://www.youtube.com/watch?v=tAaeP6Z-hK0&t=585s',
       'video_id': 'tAaeP6Z-hK0'},
      {'author': 'Vineskills',
       'channel': 'Vineskills',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:42:31](https://www.youtube.com/watch?v=9_hNat-thXA&t=2551s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Answer your questions you all have uh some amazing knowledge on automation so '
               'thanks for sharing it with us here today um and again if you all need anything '
               'feel free to reach out thanks perect have a good one bye-bye.',
       'timestamp': 2551,
       'timestamp_label': '[00:42:31]',
       'timestamp_seconds': 2551,
       'tip': 'Answer your questions you all have uh some amazing knowledge on automation so '
              'thanks for sharing it with us here today um and again if you all need anything '
              'feel free to reach out thanks perect have a good one bye-bye.',
       'title': 'Free Help Wednesdays: Filevine Automations (Vineskills)',
       'url': 'https://www.youtube.com/watch?v=9_hNat-thXA&t=2551s',
       'video_id': '9_hNat-thXA'},
      {'author': 'Consultwebs',
       'channel': 'Consultwebs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:22:26](https://www.youtube.com/watch?v=n2icO1gMkN8&t=1346s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "There's a mentoring moment that you would like my thoughts on um I I'm always "
               'looking for post ideas so I would love to hear from anybody who wants to reach '
               'out thanks again for joining the show thanks Tanner.',
       'timestamp': 1346,
       'timestamp_label': '[00:22:26]',
       'timestamp_seconds': 1346,
       'tip': "There's a mentoring moment that you would like my thoughts on um I I'm always "
              'looking for post ideas so I would love to hear from anybody who wants to reach '
              'out thanks again for joining the show thanks Tanner.',
       'title': 'Leading the Way in Mass Tort Litigation Management (Consultwebs)',
       'url': 'https://www.youtube.com/watch?v=n2icO1gMkN8&t=1346s',
       'video_id': 'n2icO1gMkN8'},
      {'author': 'The Heart of Law Podcast',
       'channel': 'The Heart of Law Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:02](https://www.youtube.com/watch?v=OdPOa3osKC0&t=182s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'t know what is an alternative business structure and how does it work? So an "
               'alternative business structure law firm or an ABS law firm is one that has '
               "some non-awyer ownership. That's that's the easiest description.",
       'timestamp': 182,
       'timestamp_label': '[00:03:02]',
       'timestamp_seconds': 182,
       'tip': "'t know what is an alternative business structure and how does it work? So an "
              'alternative business structure law firm or an ABS law firm is one that has some '
              "non-awyer ownership. That's that's the easiest description.",
       'title': 'Alternative Business Structures: Updates from Arizona’s Legal Frontier (The '
                'Heart of Law Podcast)',
       'url': 'https://www.youtube.com/watch?v=OdPOa3osKC0&t=182s',
       'video_id': 'OdPOa3osKC0'}],
 12: [{'author': 'Michael Stanisci',
       'channel': 'Michael Stanisci',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:48](https://www.youtube.com/watch?v=9fbIhuuhgGE&t=108s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So after a fact discovery wraps up in March, which is next month, the court '
               'will pick bellwether case trials probably to start around 2027. So this is '
               'definitely a marathon, not a sprint.',
       'timestamp': 108,
       'timestamp_label': '[00:01:48]',
       'timestamp_seconds': 108,
       'tip': 'So after a fact discovery wraps up in March, which is next month, the court '
              'will pick bellwether case trials probably to start around 2027. So this is '
              'definitely a marathon, not a sprint.',
       'title': 'Hair Relaxer MDL (Uterine Cancer Litigation) (Michael Stanisci)',
       'url': 'https://www.youtube.com/watch?v=9fbIhuuhgGE&t=108s',
       'video_id': '9fbIhuuhgGE'},
      {'author': 'Case Works',
       'channel': 'Case Works',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:33](https://www.youtube.com/watch?v=UP0ve0ms-ik&t=333s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And I'm hopeful before that May 24 deadline when the judge indicated there "
               "could start being some remands that will have a settlement. We'll keep you "
               "updated, of course, every week here on tort talk, if there's a settlement "
               'reach in the next couple of days.',
       'timestamp': 333,
       'timestamp_label': '[00:05:33]',
       'timestamp_seconds': 333,
       'tip': "And I'm hopeful before that May 24 deadline when the judge indicated there "
              "could start being some remands that will have a settlement. We'll keep you "
              "updated, of course, every week here on tort talk, if there's a settlement reach "
              'in the next couple of days.',
       'title': 'Big News for CPAP, J&J Talc Powder, AFFF and Bard Hernia Mesh Plaintiffs This '
                'Week! (Case Works)',
       'url': 'https://www.youtube.com/watch?v=UP0ve0ms-ik&t=333s',
       'video_id': 'UP0ve0ms-ik'},
      {'author': 'emedikon',
       'channel': 'emedikon',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:32](https://www.youtube.com/watch?v=CuDhCaHyZnI&t=212s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Mass General and then of course they had to do a corrective action plan and '
               'they had to basically do a whole comprehensive set of policy and procedure '
               'adjustments to protected PHI because this is not in the actual business '
               'practices of the organization.',
       'timestamp': 212,
       'timestamp_label': '[00:03:32]',
       'timestamp_seconds': 212,
       'tip': 'Mass General and then of course they had to do a corrective action plan and '
              'they had to basically do a whole comprehensive set of policy and procedure '
              'adjustments to protected PHI because this is not in the actual business '
              'practices of the organization.',
       'title': 'MPT Podcast 8: HIPAA - Changes in HITECH and the Impact on Your Practice '
                '(emedikon)',
       'url': 'https://www.youtube.com/watch?v=CuDhCaHyZnI&t=212s',
       'video_id': 'CuDhCaHyZnI'},
      {'author': 'TALKSONLAW',
       'channel': 'TALKSONLAW',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=1kAfGIkF10g&t=21s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I call generational conflict that law firms often experience. I should have '
               'known that you were on top of this from the start. Well, we have the perfect '
               'guest today. We have someone who I think is at the center of, if not part of '
               'the origination of it as a asset class.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'I call generational conflict that law firms often experience. I should have '
              'known that you were on top of this from the start. Well, we have the perfect '
              'guest today. We have someone who I think is at the center of, if not part of '
              'the origination of it as a asset class.',
       'title': 'Is a Lawsuit a Financial Asset? Inside Litigation Finance (TALKSONLAW)',
       'url': 'https://www.youtube.com/watch?v=1kAfGIkF10g&t=21s',
       'video_id': '1kAfGIkF10g'},
      {'author': 'Jon and Marc',
       'channel': 'Jon and Marc',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=08ES8nUZRYk&t=20s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Bard Power Port litigation, and an update on Camp Lejeune. Let's start off "
               'with uh yet another resolution. We had AFFF result in a huge settlement last '
               'week. Joe, you texted it to me as soon as you heard the news.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': "Bard Power Port litigation, and an update on Camp Lejeune. Let's start off with "
              'uh yet another resolution. We had AFFF result in a huge settlement last week. '
              'Joe, you texted it to me as soon as you heard the news.',
       'title': 'Could the Year of the Settlement Have One More in Store? (Jon and Marc)',
       'url': 'https://www.youtube.com/watch?v=08ES8nUZRYk&t=20s',
       'video_id': '08ES8nUZRYk'},
      {'author': 'CW33 (KDAF)',
       'channel': 'CW33 (KDAF)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:39](https://www.youtube.com/watch?v=hSl_yaMfnv0&t=159s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'PRODUCT BASED WE WE WILL WILL DO WE DO THOSE CASES. WE HAVE THE EXPERTS TO DO '
               'IT. YOU TELL US A LITTLE BIT ABOUT THE MASS TORTS. NEW STATED, HOW MIGHT THE '
               'CONSUMER KNOW IF THEIR CASE IS ELIGIBLE? YOU KNOW, THAT IS SO SO KEY. A LOT OF '
               'THESE MASS TORTS REALLY START INDIVIDUAL.',
       'timestamp': 159,
       'timestamp_label': '[00:02:39]',
       'timestamp_seconds': 159,
       'tip': 'PRODUCT BASED WE WE WILL WILL DO WE DO THOSE CASES. WE HAVE THE EXPERTS TO DO '
              'IT. YOU TELL US A LITTLE BIT ABOUT THE MASS TORTS. NEW STATED, HOW MIGHT THE '
              'CONSUMER KNOW IF THEIR CASE IS ELIGIBLE? YOU KNOW, THAT IS SO SO KEY. A LOT OF '
              'THESE MASS TORTS REALLY START INDIVIDUAL.',
       'title': 'What is the Difference Between Mass Tort and Class Action? Cochran Firm Texas '
                'Explains (CW33 (KDAF))',
       'url': 'https://www.youtube.com/watch?v=hSl_yaMfnv0&t=159s',
       'video_id': 'hSl_yaMfnv0'},
      {'author': 'ReelLawyers',
       'channel': 'ReelLawyers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=Kez8eHItKyc&t=15s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Will confuse the two a class action is a single case in which one person is '
               'representing the interests of a larger group of people sometimes hundreds or.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Will confuse the two a class action is a single case in which one person is '
              'representing the interests of a larger group of people sometimes hundreds or.',
       'title': 'What is the difference between multidistrict litigation and class action '
                'litigation? | Graham Newman (ReelLawyers)',
       'url': 'https://www.youtube.com/watch?v=Kez8eHItKyc&t=15s',
       'video_id': 'Kez8eHItKyc'},
      {'author': 'Randell C. Roberts',
       'channel': 'Randell C. Roberts',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:30](https://www.youtube.com/watch?v=ErJCmvkCs0o&t=150s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'We at Roberts and Roberts recommend that when you have the option that you go '
               'with the multi-district litigation or the individual case as opposed to a '
               'class action to be sure that you receive the individual attention and '
               'compensation that you deserve.',
       'timestamp': 150,
       'timestamp_label': '[00:02:30]',
       'timestamp_seconds': 150,
       'tip': 'We at Roberts and Roberts recommend that when you have the option that you go '
              'with the multi-district litigation or the individual case as opposed to a class '
              'action to be sure that you receive the individual attention and compensation '
              'that you deserve.',
       'title': 'What is the difference between mass tort, class action, and a MDL? (Randell '
                'C. Roberts)',
       'url': 'https://www.youtube.com/watch?v=ErJCmvkCs0o&t=150s',
       'video_id': 'ErJCmvkCs0o'},
      {'author': 'Salenger, Sack, Kimmel & Bavaro, LLP',
       'channel': 'Salenger, Sack, Kimmel & Bavaro, LLP',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:28](https://www.youtube.com/watch?v=ch5IVo6DOos&t=148s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The judge is not a doctor and is not a scientist. So these experts are brought '
               "in on science day and they really just educate the judge on the science that's "
               'involved in the case so the judge can better oversee the trial when it '
               'happens.',
       'timestamp': 148,
       'timestamp_label': '[00:02:28]',
       'timestamp_seconds': 148,
       'tip': 'The judge is not a doctor and is not a scientist. So these experts are brought '
              "in on science day and they really just educate the judge on the science that's "
              'involved in the case so the judge can better oversee the trial when it happens.',
       'title': 'Hair Relaxer Lawsuit Update: Bellwether Trials, Cancer Claims & What Comes '
                'Next (Salenger, Sack, Kimmel & Bavaro, LLP)',
       'url': 'https://www.youtube.com/watch?v=ch5IVo6DOos&t=148s',
       'video_id': 'ch5IVo6DOos'},
      {'author': 'The Ben Martin Law Group',
       'channel': 'The Ben Martin Law Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:39](https://www.youtube.com/watch?v=Hgo9gx4KBwk&t=99s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You know, cases are settled sometimes based upon what happens with a '
               'bellwether case. Bellwether is something that the particular sheep was called '
               'in the old days, hundreds of years ago.',
       'timestamp': 99,
       'timestamp_label': '[00:01:39]',
       'timestamp_seconds': 99,
       'tip': 'You know, cases are settled sometimes based upon what happens with a bellwether '
              'case. Bellwether is something that the particular sheep was called in the old '
              'days, hundreds of years ago.',
       'title': 'Depo-Provera Lawsuit Updates: Bellwether Cases Explained (The Ben Martin Law '
                'Group)',
       'url': 'https://www.youtube.com/watch?v=Hgo9gx4KBwk&t=99s',
       'video_id': 'Hgo9gx4KBwk'},
      {'author': 'Roberts & Roberts Law Firm',
       'channel': 'Roberts & Roberts Law Firm',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:32](https://www.youtube.com/watch?v=XubmYzsLJEw&t=152s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'When you have the option that you go with the multi-district litigation or the '
               'individual case as opposed to a class action to be sure that you receive the '
               'individual attention and compensation that you deserve.',
       'timestamp': 152,
       'timestamp_label': '[00:02:32]',
       'timestamp_seconds': 152,
       'tip': 'When you have the option that you go with the multi-district litigation or the '
              'individual case as opposed to a class action to be sure that you receive the '
              'individual attention and compensation that you deserve.',
       'title': 'What is the difference between mass tort, class action and a MDL (Roberts & '
                'Roberts Law Firm)',
       'url': 'https://www.youtube.com/watch?v=XubmYzsLJEw&t=152s',
       'video_id': 'XubmYzsLJEw'},
      {'author': 'Lawsuit Tracker',
       'channel': 'Lawsuit Tracker',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:40](https://www.youtube.com/watch?v=WmvLnQq2ZuY&t=40s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "At that point, once you're filed, you're good and nothing's really happening "
               'with your specific case. The bellweather trials will likely be scheduled and '
               "happen um different science days, but that's for again everyone involved.",
       'timestamp': 40,
       'timestamp_label': '[00:00:40]',
       'timestamp_seconds': 40,
       'tip': "At that point, once you're filed, you're good and nothing's really happening "
              'with your specific case. The bellweather trials will likely be scheduled and '
              "happen um different science days, but that's for again everyone involved.",
       'title': "You won't hear much from your lawyer in an MDL and here's why (Lawsuit "
                'Tracker)',
       'url': 'https://www.youtube.com/watch?v=WmvLnQq2ZuY&t=40s',
       'video_id': 'WmvLnQq2ZuY'},
      {'author': 'Litify',
       'channel': 'Litify',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:51:07](https://www.youtube.com/watch?v=5eCAkl3wUBg&t=3067s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Connections group um connections at litify decom and otherwise we will post '
               'this recording in a couple days on the community so you can revisit it and '
               'thank you all so much for joining thanks Amanda thank you so much everyone '
               'bye.',
       'timestamp': 3067,
       'timestamp_label': '[00:51:07]',
       'timestamp_seconds': 3067,
       'tip': 'Connections group um connections at litify decom and otherwise we will post '
              'this recording in a couple days on the community so you can revisit it and '
              'thank you all so much for joining thanks Amanda thank you so much everyone bye.',
       'title': 'Litify Intake Training: Manage Leads, Questionnaires, and Case Qualification '
                '(Litify)',
       'url': 'https://www.youtube.com/watch?v=5eCAkl3wUBg&t=3067s',
       'video_id': '5eCAkl3wUBg'},
      {'author': 'LawShelf',
       'channel': 'LawShelf',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:18](https://www.youtube.com/watch?v=9kniD1-Jx8E&t=618s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Are resolved by settlement or pre-trial motion despite the heavy emphasis on '
               'settlement from asked torts whether part of a class action or an MDL some need '
               'to be tried the trial process is where MDL s and class actions take very '
               'different paths.',
       'timestamp': 618,
       'timestamp_label': '[00:10:18]',
       'timestamp_seconds': 618,
       'tip': 'Are resolved by settlement or pre-trial motion despite the heavy emphasis on '
              'settlement from asked torts whether part of a class action or an MDL some need '
              'to be tried the trial process is where MDL s and class actions take very '
              'different paths.',
       'title': 'Settlement and Trials of Mass Torts: Module 5 of 5 (LawShelf)',
       'url': 'https://www.youtube.com/watch?v=9kniD1-Jx8E&t=618s',
       'video_id': '9kniD1-Jx8E'},
      {'author': 'Nexus Legal Group',
       'channel': 'Nexus Legal Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:57](https://www.youtube.com/watch?v=4LdL5Q6T7ds&t=57s)',
       'relevance': 'Attributed practitioner commentary on ABA Rule `5.4`-compliant Law-Firm '
                    'Management Services Organizations (`MSOs`), licensed Arizona `ABS` '
                    'co-ventures, paid-media plaintiff intake, and automated `45 CFR § '
                    '164.524` HITECH electronic medical-record (`EMR`) triage (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Nexus Legal Group built its mass tort and complex litigation case acquisition '
               "program to fix that at the source. We don't start with our criteria.",
       'timestamp': 57,
       'timestamp_label': '[00:00:57]',
       'timestamp_seconds': 57,
       'tip': 'Nexus Legal Group built its mass tort and complex litigation case acquisition '
              "program to fix that at the source. We don't start with our criteria.",
       'title': "Signed Isn't Settlement Ready Building Mass Tort Inventory That Holds Up "
                '(Nexus Legal Group)',
       'url': 'https://www.youtube.com/watch?v=4LdL5Q6T7ds&t=57s',
       'video_id': '4LdL5Q6T7ds'}]}
