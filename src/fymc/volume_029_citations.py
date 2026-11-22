"""Curated 180-citation Insurance Restoration baseline (15 per chapter across Q1-Q12) mined strictly from verified Insurance Restoration YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'accounts',
     'adjuster',
     'administrator',
     'alacrity',
     'anti',
     'aob',
     'asbestos',
     'assignment',
     'benefits',
     'billing',
     'boundary',
     'business',
     'call',
     'check',
     'claims',
     'cleaning',
     'client',
     'clients',
     'commercial',
     'company',
     'connection',
     'contents',
     'contractor',
     'crew',
     'damage',
     'deductible',
     'desk',
     'direction',
     'dispatch',
     'documentation',
     'downward',
     'drying',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'accounts',
     'adjuster',
     'administrator',
     'alacrity',
     'anti',
     'aob',
     'asbestos',
     'assignment',
     'benefits',
     'billing',
     'boundary',
     'budget',
     'business',
     'buyer',
     'call',
     'check',
     'claims',
     'cleaning',
     'commercial',
     'company',
     'connection',
     'contents',
     'contract',
     'contractor',
     'crew',
     'customer',
     'damage',
     'decision',
     'deductible',
     'desk',
     'direction',
     'dispatch',
     'documentation',
     'downward',
     'drying',
     'escrow',
     'fee',
     'fees',
     'invoice',
     'pay',
     'payment',
     'pays',
     'retainer'},
 3: {'accounts',
     'adjuster',
     'administrator',
     'alacrity',
     'anti',
     'aob',
     'asbestos',
     'assignment',
     'benefits',
     'billing',
     'boundary',
     'business',
     'call',
     'cash',
     'cashflow',
     'check',
     'claims',
     'cleaning',
     'commercial',
     'commission',
     'company',
     'connection',
     'contents',
     'contractor',
     'cost',
     'costs',
     'crew',
     'damage',
     'deductible',
     'desk',
     'direction',
     'dispatch',
     'documentation',
     'downward',
     'drying',
     'economics',
     'margin',
     'margins',
     'price',
     'pricing',
     'profit',
     'roi',
     'unit'},
 4: {'accounts',
     'adjuster',
     'administrator',
     'alacrity',
     'anti',
     'aob',
     'asbestos',
     'assignment',
     'benefits',
     'billing',
     'boundary',
     'budget',
     'business',
     'call',
     'capital',
     'check',
     'claims',
     'cleaning',
     'commercial',
     'company',
     'connection',
     'contents',
     'contractor',
     'crew',
     'damage',
     'deductible',
     'desk',
     'direction',
     'dispatch',
     'documentation',
     'downward',
     'drying',
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
 5: {'accounts',
     'adjuster',
     'administrator',
     'alacrity',
     'anti',
     'aob',
     'asbestos',
     'assignment',
     'audit',
     'avoid',
     'benefits',
     'billing',
     'boundary',
     'business',
     'call',
     'check',
     'claims',
     'clawback',
     'cleaning',
     'commercial',
     'company',
     'connection',
     'contents',
     'contractor',
     'crew',
     'damage',
     'deductible',
     'desk',
     'direction',
     'dispatch',
     'dispute',
     'documentation',
     'downward',
     'drying',
     'edge',
     'fail',
     'mistake',
     'mistakes',
     'problem',
     'risk',
     'risks',
     'trap',
     'traps'},
 6: {'accounts',
     'adjuster',
     'administrator',
     'alacrity',
     'anti',
     'aob',
     'asbestos',
     'assignment',
     'benefits',
     'billing',
     'boundary',
     'business',
     'call',
     'check',
     'claims',
     'cleaning',
     'client',
     'commercial',
     'company',
     'connection',
     'contents',
     'contractor',
     'crew',
     'damage',
     'data',
     'deal',
     'deductible',
     'desk',
     'direction',
     'dispatch',
     'documentation',
     'downward',
     'drying',
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
 7: {'accounts',
     'adjuster',
     'administrator',
     'alacrity',
     'anti',
     'aob',
     'asbestos',
     'assignment',
     'benefits',
     'billing',
     'boundary',
     'business',
     'call',
     'check',
     'checklist',
     'claims',
     'cleaning',
     'commercial',
     'company',
     'connection',
     'contents',
     'contractor',
     'crew',
     'damage',
     'deductible',
     'delivery',
     'desk',
     'direction',
     'dispatch',
     'documentation',
     'downward',
     'drying',
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
 8: {'accounts',
     'adjuster',
     'administrator',
     'alacrity',
     'anti',
     'aob',
     'api',
     'asbestos',
     'assignment',
     'benefits',
     'billing',
     'boundary',
     'business',
     'call',
     'check',
     'claims',
     'cleaning',
     'commercial',
     'company',
     'connection',
     'contents',
     'contractor',
     'crew',
     'crm',
     'damage',
     'data',
     'database',
     'deductible',
     'desk',
     'direction',
     'dispatch',
     'documentation',
     'downward',
     'drying',
     'platform',
     'portal',
     'scraper',
     'search',
     'software',
     'tool',
     'tools',
     'tracking'},
 9: {'accounts',
     'adjuster',
     'administrator',
     'agreement',
     'alacrity',
     'anti',
     'aob',
     'asbestos',
     'assignment',
     'benefits',
     'billing',
     'boundary',
     'business',
     'call',
     'check',
     'claims',
     'cleaning',
     'commercial',
     'company',
     'compliance',
     'connection',
     'contents',
     'contract',
     'contractor',
     'crew',
     'damage',
     'deductible',
     'desk',
     'direction',
     'disclosure',
     'dispatch',
     'documentation',
     'downward',
     'drying',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'accounts',
      'adjuster',
      'administrator',
      'agent',
      'ai',
      'alacrity',
      'anti',
      'aob',
      'asbestos',
      'assignment',
      'automate',
      'automation',
      'benefits',
      'billing',
      'boundary',
      'business',
      'call',
      'check',
      'claims',
      'cleaning',
      'commercial',
      'company',
      'connection',
      'contents',
      'contractor',
      'crew',
      'damage',
      'dashboard',
      'deductible',
      'desk',
      'direction',
      'dispatch',
      'documentation',
      'downward',
      'drying',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'accounts',
      'adjuster',
      'administrator',
      'alacrity',
      'anti',
      'aob',
      'asbestos',
      'assignment',
      'benefits',
      'billing',
      'boundary',
      'business',
      'call',
      'check',
      'claims',
      'cleaning',
      'commercial',
      'company',
      'connection',
      'contents',
      'contractor',
      'crew',
      'damage',
      'deductible',
      'desk',
      'direction',
      'dispatch',
      'documentation',
      'downward',
      'drying',
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
 12: {'accounts',
      'action',
      'adjuster',
      'administrator',
      'alacrity',
      'anti',
      'aob',
      'asbestos',
      'assignment',
      'benefits',
      'billing',
      'boundary',
      'business',
      'call',
      'check',
      'claims',
      'cleaning',
      'commercial',
      'company',
      'connection',
      'contents',
      'contractor',
      'crew',
      'damage',
      'day',
      'days',
      'deductible',
      'desk',
      'direction',
      'dispatch',
      'documentation',
      'downward',
      'drying',
      'launch',
      'milestone',
      'month',
      'plan',
      'roadmap',
      'sprint',
      'start',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Butler Legal',
      'channel': 'Butler Legal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:24](https://www.youtube.com/watch?v=rxahzd6qaCw&t=84s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'When the contractor comes in to ensure that he or she gets paid, the contractor '
              'will have either the homeowner or the commercial business owner execute the '
              'assignment of benefits. The insured typically will say the scope of the damage '
              "that they'd like repaired.",
      'timestamp': 84,
      'timestamp_label': '[00:01:24]',
      'timestamp_seconds': 84,
      'tip': 'When the contractor comes in to ensure that he or she gets paid, the contractor '
             'will have either the homeowner or the commercial business owner execute the '
             'assignment of benefits. The insured typically will say the scope of the damage '
             "that they'd like repaired.",
      'title': 'Handling of Assignment of Benefit ("AOB") Claims (Butler Legal)',
      'url': 'https://www.youtube.com/watch?v=rxahzd6qaCw&t=84s',
      'video_id': 'rxahzd6qaCw'},
     {'author': 'Roofing Insights',
      'channel': 'Roofing Insights',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:54](https://www.youtube.com/watch?v=Qv99F8pvYNU&t=1434s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And if if out here it\'s my client, I call them up and say, "You should have '
              'paid this." Write them a check immediately and tell them, "You\'re sorry." If '
              'it\'s over here on the fraud side, I call the insurance company and say, "This '
              'is going to be fun.',
      'timestamp': 1434,
      'timestamp_label': '[00:23:54]',
      'timestamp_seconds': 1434,
      'tip': 'And if if out here it\'s my client, I call them up and say, "You should have '
             'paid this." Write them a check immediately and tell them, "You\'re sorry." If '
             'it\'s over here on the fraud side, I call the insurance company and say, "This '
             'is going to be fun.',
      'title': 'Insurance Lawyer vs Public Adjuster: Who Really Protects Homeowners? (Roofing '
               'Insights)',
      'url': 'https://www.youtube.com/watch?v=Qv99F8pvYNU&t=1434s',
      'video_id': 'Qv99F8pvYNU'},
     {'author': 'Learn To Restore',
      'channel': 'Learn To Restore',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:57](https://www.youtube.com/watch?v=i4RGAC2VwaY&t=297s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And if you are going to be doing carpet cleaning for clients, then you should '
              "have in your company and know the S100. If you're doing upholstery cleaning, "
              "you should have the S300. If you're doing water damage, you should have and "
              'know the S500.',
      'timestamp': 297,
      'timestamp_label': '[00:04:57]',
      'timestamp_seconds': 297,
      'tip': 'And if you are going to be doing carpet cleaning for clients, then you should '
             "have in your company and know the S100. If you're doing upholstery cleaning, you "
             "should have the S300. If you're doing water damage, you should have and know the "
             'S500.',
      'title': 'Intro to the IICRC S500 for Water Damage Restoration (Learn To Restore)',
      'url': 'https://www.youtube.com/watch?v=i4RGAC2VwaY&t=297s',
      'video_id': 'i4RGAC2VwaY'},
     {'author': 'Restoration Roofing',
      'channel': 'Restoration Roofing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:47](https://www.youtube.com/watch?v=t6BiCluK7GY&t=47s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Law so let me give you a little scenario real quick let's say you have a roof "
              'claim and the replacement value is twenty thousand dollars so this is what the '
              'insurance company is saying they are valuing the roof at so you have a two '
              'thousand dollar deductible.',
      'timestamp': 47,
      'timestamp_label': '[00:00:47]',
      'timestamp_seconds': 47,
      'tip': "Law so let me give you a little scenario real quick let's say you have a roof "
             'claim and the replacement value is twenty thousand dollars so this is what the '
             'insurance company is saying they are valuing the roof at so you have a two '
             'thousand dollar deductible.',
      'title': 'Is it illegal for my roofer to waive my deductible? | #Insurancedeductible '
               '(Restoration Roofing)',
      'url': 'https://www.youtube.com/watch?v=t6BiCluK7GY&t=47s',
      'video_id': 't6BiCluK7GY'},
     {'author': 'MaprBot',
      'channel': 'MaprBot',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:45](https://www.youtube.com/watch?v=wQbjMlmo1Bg&t=105s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'It can help with planning, but it does not establish that hail is falling at a '
              'particular property. Check current National Weather Service warnings for '
              'immediate decisions. Bottom line, these are reported hail locations, not a '
              'complete damage survey.',
      'timestamp': 105,
      'timestamp_label': '[00:01:45]',
      'timestamp_seconds': 105,
      'tip': 'It can help with planning, but it does not establish that hail is falling at a '
             'particular property. Check current National Weather Service warnings for '
             'immediate decisions. Bottom line, these are reported hail locations, not a '
             'complete damage survey.',
      'title': 'Mid-Atlantic Hail Recap: 34 Reports, Storms Move Offshore | November 12, 2026 '
               '(MaprBot)',
      'url': 'https://www.youtube.com/watch?v=wQbjMlmo1Bg&t=105s',
      'video_id': 'wQbjMlmo1Bg'},
     {'author': 'The DYOJO (The DYOJO)',
      'channel': 'The DYOJO (The DYOJO)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:01](https://www.youtube.com/watch?v=onSDIprTeAU&t=1321s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um no no I I think that I I how do I say this best? I think that if um if a '
              "business isn't approaching multiple models um at some point they are going to "
              'run into a model interrupt.',
      'timestamp': 1321,
      'timestamp_label': '[00:22:01]',
      'timestamp_seconds': 1321,
      'tip': 'Um no no I I think that I I how do I say this best? I think that if um if a '
             "business isn't approaching multiple models um at some point they are going to "
             'run into a model interrupt.',
      'title': 'How do you win the insurance claims TPA game (Contractor Connections & '
               'Alacrity)? TDP 58 (PVJ 012) (The DYOJO (The DYOJO))',
      'url': 'https://www.youtube.com/watch?v=onSDIprTeAU&t=1321s',
      'video_id': 'onSDIprTeAU'},
     {'author': 'Chad Michael - The Practitioner',
      'channel': 'Chad Michael - The Practitioner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:43](https://www.youtube.com/watch?v=Op9Qkl-qW58&t=763s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You see, you can't really you can't you're not allowed if you're a contractor "
              "in most states anyway, you're not allowed to tell the client to file a claim or "
              'how to file a claim, steer them towards the claim.',
      'timestamp': 763,
      'timestamp_label': '[00:12:43]',
      'timestamp_seconds': 763,
      'tip': "You see, you can't really you can't you're not allowed if you're a contractor in "
             "most states anyway, you're not allowed to tell the client to file a claim or how "
             'to file a claim, steer them towards the claim.',
      'title': 'Commercial Roof Coating | Hail Damage (Chad Michael - The Practitioner)',
      'url': 'https://www.youtube.com/watch?v=Op9Qkl-qW58&t=763s',
      'video_id': 'Op9Qkl-qW58'},
     {'author': 'Octagon Cleaning and Restoration',
      'channel': 'Octagon Cleaning and Restoration',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:07](https://www.youtube.com/watch?v=WTz841eMFkk&t=67s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Or the mold or the asbestos I like the relationship with the client the '
              "customer they tend to be a little bigger jobs don't they they are they're "
              'larger.',
      'timestamp': 67,
      'timestamp_label': '[00:01:07]',
      'timestamp_seconds': 67,
      'tip': 'Or the mold or the asbestos I like the relationship with the client the customer '
             "they tend to be a little bigger jobs don't they they are they're larger.",
      'title': 'Inside Fire Damage Restoration: A Project Manager’s Perspective (Octagon '
               'Cleaning and Restoration)',
      'url': 'https://www.youtube.com/watch?v=WTz841eMFkk&t=67s',
      'video_id': 'WTz841eMFkk'},
     {'author': 'Dustin Taylor',
      'channel': 'Dustin Taylor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:14](https://www.youtube.com/watch?v=gtsj3GY7D8c&t=254s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And then emergency service call like that. And then I'll go like this. And I'll "
              'just call it a 10 by 20 like that. So that gets rid of that portion. And I '
              "think I'm going to go like this. And I'll get to this in a second. So, I'm not "
              'going to resolve that yet.',
      'timestamp': 254,
      'timestamp_label': '[00:04:14]',
      'timestamp_seconds': 254,
      'tip': "And then emergency service call like that. And then I'll go like this. And I'll "
             'just call it a 10 by 20 like that. So that gets rid of that portion. And I think '
             "I'm going to go like this. And I'll get to this in a second. So, I'm not going "
             'to resolve that yet.',
      'title': 'Writing Xactimate Roofing Supplement - Texas (Dustin Taylor)',
      'url': 'https://www.youtube.com/watch?v=gtsj3GY7D8c&t=254s',
      'video_id': 'gtsj3GY7D8c'},
     {'author': 'Restoration Success Strategies | Albi',
      'channel': 'Restoration Success Strategies | Albi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:05](https://www.youtube.com/watch?v=Fj9S8rNJ5d4&t=1205s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "If if your not if your immediate instinct isn't to talk them out of it then "
              "they have to go then then they need to go right then. Because they're not "
              "they're not they're just keeping them around they're not really adding value to "
              'your business.',
      'timestamp': 1205,
      'timestamp_label': '[00:20:05]',
      'timestamp_seconds': 1205,
      'tip': "If if your not if your immediate instinct isn't to talk them out of it then they "
             "have to go then then they need to go right then. Because they're not they're not "
             "they're just keeping them around they're not really adding value to your "
             'business.',
      'title': 'How Restoration Companies Get Water Damage Jobs (The Plumber Referral '
               'Playbook) (Restoration Success Strategies | Albi)',
      'url': 'https://www.youtube.com/watch?v=Fj9S8rNJ5d4&t=1205s',
      'video_id': 'Fj9S8rNJ5d4'},
     {'author': 'FirehouseEducation',
      'channel': 'FirehouseEducation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:35](https://www.youtube.com/watch?v=Appti0ctcGA&t=335s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Perfect example of how you while your client blow their mind take care of their '
              "contents and don't wind up having damages at the hand of your employees so.",
      'timestamp': 335,
      'timestamp_label': '[00:05:35]',
      'timestamp_seconds': 335,
      'tip': 'Perfect example of how you while your client blow their mind take care of their '
             "contents and don't wind up having damages at the hand of your employees so.",
      'title': 'How To Packout A Fire Restoration Job Without Damage To Contents '
               '(FirehouseEducation)',
      'url': 'https://www.youtube.com/watch?v=Appti0ctcGA&t=335s',
      'video_id': 'Appti0ctcGA'},
     {'author': 'Contractor Talk Podcast',
      'channel': 'Contractor Talk Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:43:22](https://www.youtube.com/watch?v=Tg526FvHOmY&t=2602s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Auto it went into medical went into life as well um it really affected Florida '
              'Insurance market so what to expect if you have a a loss on your property in '
              "Florida now in 2024 you don't want to miss this podcast.",
      'timestamp': 2602,
      'timestamp_label': '[00:43:22]',
      'timestamp_seconds': 2602,
      'tip': 'Auto it went into medical went into life as well um it really affected Florida '
             'Insurance market so what to expect if you have a a loss on your property in '
             "Florida now in 2024 you don't want to miss this podcast.",
      'title': 'Shifting Sands: The Move from AOB to Direction to Pay in Florida Restoration '
               'Contracting (Contractor Talk Podcast)',
      'url': 'https://www.youtube.com/watch?v=Tg526FvHOmY&t=2602s',
      'video_id': 'Tg526FvHOmY'},
     {'author': 'Holmes Drafting Services',
      'channel': 'Holmes Drafting Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:37](https://www.youtube.com/watch?v=zzzZPeokDUk&t=97s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Homeowner now you have an open claim on your insurance you have a lien on your '
              'house and you have a lawsuit against an insurance carrier those three things '
              "are the the most major uh concern of you know that's the worst case scenario of "
              'that of that scenario.',
      'timestamp': 97,
      'timestamp_label': '[00:01:37]',
      'timestamp_seconds': 97,
      'tip': 'Homeowner now you have an open claim on your insurance you have a lien on your '
             'house and you have a lawsuit against an insurance carrier those three things are '
             "the the most major uh concern of you know that's the worst case scenario of that "
             'of that scenario.',
      'title': 'What is Assignment of Benefits (AOB)? (Holmes Drafting Services)',
      'url': 'https://www.youtube.com/watch?v=zzzZPeokDUk&t=97s',
      'video_id': 'zzzZPeokDUk'},
     {'author': 'News4JAX The Local Station',
      'channel': 'News4JAX The Local Station',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=hB0EZGfpw4I&t=98s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Get regulated they probably don't have the educational training they probably "
              "don't have the financial ability to to train their people and mold so "
              'absolutely I think you get rid of them tarek minor channel for the local '
              'station.',
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': "Get regulated they probably don't have the educational training they probably "
             "don't have the financial ability to to train their people and mold so absolutely "
             'I think you get rid of them tarek minor channel for the local station.',
      'title': "Florida lawmakers seek 'assignment of benefits' solution (News4JAX The Local "
               'Station)',
      'url': 'https://www.youtube.com/watch?v=hB0EZGfpw4I&t=98s',
      'video_id': 'hB0EZGfpw4I'},
     {'author': 'Adjuster TV',
      'channel': 'Adjuster TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:26](https://www.youtube.com/watch?v=nHMaLQmm8nw&t=386s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Other questions ad free as well as get access to a members only segment '
              'question and answer head on over to adjustertvplus.com and become a member '
              'right now.',
      'timestamp': 386,
      'timestamp_label': '[00:06:26]',
      'timestamp_seconds': 386,
      'tip': 'Other questions ad free as well as get access to a members only segment question '
             'and answer head on over to adjustertvplus.com and become a member right now.',
      'title': 'How to ACTUALLY work as a remote desk adjuster (Adjuster TV)',
      'url': 'https://www.youtube.com/watch?v=nHMaLQmm8nw&t=386s',
      'video_id': 'nHMaLQmm8nw'}],
 2: [{'author': 'Long Term Care Law Office',
      'channel': 'Long Term Care Law Office',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:16](https://www.youtube.com/watch?v=4AHP633shFk&t=256s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Pay their own attorney fees to go after their customer client so for all those '
              "reasons the assignment is a it's a critical part of the process of facilitating "
              'care and facilitating payment for the care with the assignment we with the '
              'assignment.',
      'timestamp': 256,
      'timestamp_label': '[00:04:16]',
      'timestamp_seconds': 256,
      'tip': 'Pay their own attorney fees to go after their customer client so for all those '
             "reasons the assignment is a it's a critical part of the process of facilitating "
             'care and facilitating payment for the care with the assignment we with the '
             'assignment.',
      'title': 'Healthcare Law, Steve Dunn   Assignment of Benefits (Long Term Care Law '
               'Office)',
      'url': 'https://www.youtube.com/watch?v=4AHP633shFk&t=256s',
      'video_id': '4AHP633shFk'},
     {'author': 'The Fine Print',
      'channel': 'The Fine Print',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=UxKcyrt-VS0&t=103s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And when the insurer refused to pay the full 22,000, the contractor did exactly '
              'what the form allowed. It filed a lawsuit against the insurance company, naming '
              "the homeowner's policy, seeking the disputed amount plus attorney fees. Why "
              'would a contractor want to sue?',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': 'And when the insurer refused to pay the full 22,000, the contractor did exactly '
             'what the form allowed. It filed a lawsuit against the insurance company, naming '
             "the homeowner's policy, seeking the disputed amount plus attorney fees. Why "
             'would a contractor want to sue?',
      'title': 'He Signed One Form at His Front Door and Lost Control of His Own Claim | '
               'Assignment of Benefits (The Fine Print)',
      'url': 'https://www.youtube.com/watch?v=UxKcyrt-VS0&t=103s',
      'video_id': 'UxKcyrt-VS0'},
     {'author': 'CCK Law Long-Term Disability',
      'channel': 'CCK Law Long-Term Disability',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:53](https://www.youtube.com/watch?v=lnhw4pYCOFU&t=53s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'TPA, not an insurance company. They manage LTD claims for major employers and '
              'insurers. Their role is to evaluate your claim and recommend an approval or a '
              'denial, but they do not pay benefits directly.',
      'timestamp': 53,
      'timestamp_label': '[00:00:53]',
      'timestamp_seconds': 53,
      'tip': 'TPA, not an insurance company. They manage LTD claims for major employers and '
             'insurers. Their role is to evaluate your claim and recommend an approval or a '
             'denial, but they do not pay benefits directly.',
      'title': 'How Sedgwick Handles LTD Claims and Why Denials Happen (CCK Law Long-Term '
               'Disability)',
      'url': 'https://www.youtube.com/watch?v=lnhw4pYCOFU&t=53s',
      'video_id': 'lnhw4pYCOFU'},
     {'author': 'Medicalbillingz',
      'channel': 'Medicalbillingz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:24](https://www.youtube.com/watch?v=HC1u-rGDBKc&t=144s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Promptly consider o versus self-payment based on your needs and preferences '
              'informed decision- making on a ob and medical billing is crucial while it '
              'offers advantages through understanding and adherence to precautions ensure '
              'data protection.',
      'timestamp': 144,
      'timestamp_label': '[00:02:24]',
      'timestamp_seconds': 144,
      'tip': 'Promptly consider o versus self-payment based on your needs and preferences '
             'informed decision- making on a ob and medical billing is crucial while it offers '
             'advantages through understanding and adherence to precautions ensure data '
             'protection.',
      'title': 'Assignment of Benefits (AOB) in Medical Billing: Your Comprehensive Guide '
               '(Medicalbillingz)',
      'url': 'https://www.youtube.com/watch?v=HC1u-rGDBKc&t=144s',
      'video_id': 'HC1u-rGDBKc'},
     {'author': 'TheIICRC',
      'channel': 'TheIICRC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:46](https://www.youtube.com/watch?v=tPPswF112gY&t=46s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Be sure to pay your non-refundable and non-transferable MRS application and '
              'examination fees. Both need to be paid in full before you will obtain access to '
              'the exam. Upon your initial application submission, you will pay the $150 '
              'application fee.',
      'timestamp': 46,
      'timestamp_label': '[00:00:46]',
      'timestamp_seconds': 46,
      'tip': 'Be sure to pay your non-refundable and non-transferable MRS application and '
             'examination fees. Both need to be paid in full before you will obtain access to '
             'the exam. Upon your initial application submission, you will pay the $150 '
             'application fee.',
      'title': 'IICRC Mold Remediation Specialist (MRS) - Handbook (TheIICRC)',
      'url': 'https://www.youtube.com/watch?v=tPPswF112gY&t=46s',
      'video_id': 'tPPswF112gY'},
     {'author': 'Digital Roofing Innovations',
      'channel': 'Digital Roofing Innovations',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:50](https://www.youtube.com/watch?v=tVMI8UScmmE&t=170s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "They don't want you to uh venmo business them or paypal business they want to "
              'get a check okay and because they pay a lot of their guys.',
      'timestamp': 170,
      'timestamp_label': '[00:02:50]',
      'timestamp_seconds': 170,
      'tip': "They don't want you to uh venmo business them or paypal business they want to "
             'get a check okay and because they pay a lot of their guys.',
      'title': 'How to Pay Your Roofing Subcontractors - Ch 4 Vd 14 (Digital Roofing '
               'Innovations)',
      'url': 'https://www.youtube.com/watch?v=tVMI8UScmmE&t=170s',
      'video_id': 'tVMI8UScmmE'},
     {'author': 'Grossman PA LLC',
      'channel': 'Grossman PA LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=diiBgujlZF0&t=77s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I know I've done them a hundred times. Sure, there's unforeseen conditions. You "
              'can explain them, document them, and issue a justified change order. When '
              "carriers question your invoice, you scream they're lowballing me. Did you "
              'actually know insurance companies pay claims?',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': "I know I've done them a hundred times. Sure, there's unforeseen conditions. You "
             'can explain them, document them, and issue a justified change order. When '
             "carriers question your invoice, you scream they're lowballing me. Did you "
             'actually know insurance companies pay claims?',
      'title': 'One Question That Will Shake the Billion-Dollar Insurance Restoration Industry '
               '(Grossman PA LLC)',
      'url': 'https://www.youtube.com/watch?v=diiBgujlZF0&t=77s',
      'video_id': 'diiBgujlZF0'},
     {'author': 'Chris Zimmerman',
      'channel': 'Chris Zimmerman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:17](https://www.youtube.com/watch?v=9A5QEe9xxXk&t=257s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So, yes, I think the analogy is is good. I just think there's a much easier "
              'path. So, let\'s try another one here. This says, "I am an adjuster. If I '
              'assign this task to a third-party administrator, then I expect to pay a bill '
              'for them for requested services.".',
      'timestamp': 257,
      'timestamp_label': '[00:04:17]',
      'timestamp_seconds': 257,
      'tip': "So, yes, I think the analogy is is good. I just think there's a much easier "
             'path. So, let\'s try another one here. This says, "I am an adjuster. If I assign '
             'this task to a third-party administrator, then I expect to pay a bill for them '
             'for requested services.".',
      'title': 'Watch This BEFORE You Do Everything Your Insurance Adjuster Says (Chris '
               'Zimmerman)',
      'url': 'https://www.youtube.com/watch?v=9A5QEe9xxXk&t=257s',
      'video_id': '9A5QEe9xxXk'},
     {'author': "Shane O'Dazier | RestorationProfits",
      'channel': "Shane O'Dazier | RestorationProfits",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:04](https://www.youtube.com/watch?v=72Qh6dRR94U&t=604s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'To pay for decontamination so just call it a restock fee and put it on there '
              'they pay it all right so this is an example of what our estimate was like.',
      'timestamp': 604,
      'timestamp_label': '[00:10:04]',
      'timestamp_seconds': 604,
      'tip': 'To pay for decontamination so just call it a restock fee and put it on there '
             'they pay it all right so this is an example of what our estimate was like.',
      'title': 'Water Restoration Business - Estimates (Maximize Self-Pay & Insurance Payouts) '
               "(Shane O'Dazier | RestorationProfits)",
      'url': 'https://www.youtube.com/watch?v=72Qh6dRR94U&t=604s',
      'video_id': '72Qh6dRR94U'},
     {'author': 'PushLeads',
      'channel': 'PushLeads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:46](https://www.youtube.com/watch?v=9FnufX3pXj4&t=646s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Get your free search terms audit by reaching out to us on here on YouTube or '
              "LinkedIn or one or online or just call us We'll show exactly what clicks you're "
              "wasting We'll show you exactly what clicks are wasting your budget and playing "
              'English.',
      'timestamp': 646,
      'timestamp_label': '[00:10:46]',
      'timestamp_seconds': 646,
      'tip': 'Get your free search terms audit by reaching out to us on here on YouTube or '
             "LinkedIn or one or online or just call us We'll show exactly what clicks you're "
             "wasting We'll show you exactly what clicks are wasting your budget and playing "
             'English.',
      'title': 'How do you set up Google Ads for emergency contractors in 2026? (PushLeads)',
      'url': 'https://www.youtube.com/watch?v=9FnufX3pXj4&t=646s',
      'video_id': '9FnufX3pXj4'},
     {'author': 'Roof Sales Mastery',
      'channel': 'Roof Sales Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:53](https://www.youtube.com/watch?v=jj-GWZEtOc0&t=1133s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Sometimes they're just gonna pay for half of it and that's all you're gonna get "
              "and sometimes you're gonna have a really tough insurance company like.",
      'timestamp': 1133,
      'timestamp_label': '[00:18:53]',
      'timestamp_seconds': 1133,
      'tip': "Sometimes they're just gonna pay for half of it and that's all you're gonna get "
             "and sometimes you're gonna have a really tough insurance company like.",
      'title': 'Best Way to Learn Roof Supplementing & Xactimate (Roof Sales Mastery)',
      'url': 'https://www.youtube.com/watch?v=jj-GWZEtOc0&t=1133s',
      'video_id': 'jj-GWZEtOc0'},
     {'author': 'Hook Agency',
      'channel': 'Hook Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:21](https://www.youtube.com/watch?v=BCYwigE5kQU&t=81s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "24-to-48-hour verification review. Don't make big profile changes right before "
              "or during your migration window. Second, your budget structure changes. You're "
              'moving from a weekly budget to a daily budget, using a standard 30.',
      'timestamp': 81,
      'timestamp_label': '[00:01:21]',
      'timestamp_seconds': 81,
      'tip': "24-to-48-hour verification review. Don't make big profile changes right before "
             "or during your migration window. Second, your budget structure changes. You're "
             'moving from a weekly budget to a daily budget, using a standard 30.',
      'title': 'Google Just Killed the LSAs: What Every Contractor Needs to Know (August 2026) '
               '(Hook Agency)',
      'url': 'https://www.youtube.com/watch?v=BCYwigE5kQU&t=81s',
      'video_id': 'BCYwigE5kQU'},
     {'author': 'magicplan',
      'channel': 'magicplan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:03](https://www.youtube.com/watch?v=irpHqZ46CG8&t=363s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Down to your report PDF all you do is click on report PDF and after a moment '
              "you'll have a file that you can easily share and that you can view with your "
              'customer on site all from the convenience of your mobile device.',
      'timestamp': 363,
      'timestamp_label': '[00:06:03]',
      'timestamp_seconds': 363,
      'tip': 'Down to your report PDF all you do is click on report PDF and after a moment '
             "you'll have a file that you can easily share and that you can view with your "
             'customer on site all from the convenience of your mobile device.',
      'title': 'How to Document Water Damage Restoration Like a Pro (magicplan)',
      'url': 'https://www.youtube.com/watch?v=irpHqZ46CG8&t=363s',
      'video_id': 'irpHqZ46CG8'},
     {'author': "Shane O'Dazier | RestorationProfits",
      'channel': "Shane O'Dazier | RestorationProfits",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:44](https://www.youtube.com/watch?v=m97k7TBcJgY&t=404s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Crew for two days it was $3,400 like yo I put that in there and they paid it '
              "these examples were paid in full estimates now they don't always pay.",
      'timestamp': 404,
      'timestamp_label': '[00:06:44]',
      'timestamp_seconds': 404,
      'tip': 'Crew for two days it was $3,400 like yo I put that in there and they paid it '
             "these examples were paid in full estimates now they don't always pay.",
      'title': "Estimates for Water Damage Restoration: Advanced Tips (Shane O'Dazier | "
               'RestorationProfits)',
      'url': 'https://www.youtube.com/watch?v=m97k7TBcJgY&t=404s',
      'video_id': 'm97k7TBcJgY'},
     {'author': 'Roof Sales Mastery',
      'channel': 'Roof Sales Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:32](https://www.youtube.com/watch?v=sICOGLUjsao&t=1172s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Customer identified for the things that they should be indemnified for and to '
              'make sure that you guys can put the right things on the roof and you get paid '
              'for the work that you do everybody gets taken care of correctly.',
      'timestamp': 1172,
      'timestamp_label': '[00:19:32]',
      'timestamp_seconds': 1172,
      'tip': 'Customer identified for the things that they should be indemnified for and to '
             'make sure that you guys can put the right things on the roof and you get paid '
             'for the work that you do everybody gets taken care of correctly.',
      'title': 'The Basic Process of Supplementing Insurance Claims for Roofers (Roof Sales '
               'Mastery)',
      'url': 'https://www.youtube.com/watch?v=sICOGLUjsao&t=1172s',
      'video_id': 'sICOGLUjsao'}],
 3: [{'author': "Shane O'Dazier | RestorationProfits",
      'channel': "Shane O'Dazier | RestorationProfits",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:52](https://www.youtube.com/watch?v=PqL0m54Gjb4&t=412s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'t know, I help people just like you grow and scale your water damage "
              'restoration business. If you are interested in me helping you grow and scale '
              "your company, go to workwithshane. We hop on a 15-minute call to see if we're a "
              "good fit. Now, let's go back to the video.",
      'timestamp': 412,
      'timestamp_label': '[00:06:52]',
      'timestamp_seconds': 412,
      'tip': "'t know, I help people just like you grow and scale your water damage "
             'restoration business. If you are interested in me helping you grow and scale '
             "your company, go to workwithshane. We hop on a 15-minute call to see if we're a "
             "good fit. Now, let's go back to the video.",
      'title': 'The biggest mistake contractors make when billing insurance for water damage '
               "claims (Shane O'Dazier | RestorationProfits)",
      'url': 'https://www.youtube.com/watch?v=PqL0m54Gjb4&t=412s',
      'video_id': 'PqL0m54Gjb4'},
     {'author': 'RoofCoach',
      'channel': 'RoofCoach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=gLFs8l5O0j4&t=146s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Do I have your attention now? Markup only adds the percentage to cost. Margin '
              'math figures out what the selling price needs to be to ensure that you have the '
              "gross profit dollars left over after you've done the job that will cover your "
              'overhead and net profit.',
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': 'Do I have your attention now? Markup only adds the percentage to cost. Margin '
             'math figures out what the selling price needs to be to ensure that you have the '
             "gross profit dollars left over after you've done the job that will cover your "
             'overhead and net profit.',
      'title': 'How to Price Roofing Jobs for Profit (Without Losing Clients) (RoofCoach)',
      'url': 'https://www.youtube.com/watch?v=gLFs8l5O0j4&t=146s',
      'video_id': 'gLFs8l5O0j4'},
     {'author': 'George Gabriel',
      'channel': 'George Gabriel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:57](https://www.youtube.com/watch?v=KnWhJDOPsTc&t=297s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Then after that, as you can see, it's going to check that the whole thing adds "
              'back to the actual contract price. And it shows the plan cost and the plan '
              'margin in dollars as a percent of the price. Now look at this line because it '
              'says not priced.',
      'timestamp': 297,
      'timestamp_label': '[00:04:57]',
      'timestamp_seconds': 297,
      'tip': "Then after that, as you can see, it's going to check that the whole thing adds "
             'back to the actual contract price. And it shows the plan cost and the plan '
             'margin in dollars as a percent of the price. Now look at this line because it '
             'says not priced.',
      'title': 'Why Contractors Lose Margin After the Job Is Sold (George Gabriel)',
      'url': 'https://www.youtube.com/watch?v=KnWhJDOPsTc&t=297s',
      'video_id': 'KnWhJDOPsTc'},
     {'author': 'Water Damage Restoration Coach - Jon Schoen',
      'channel': 'Water Damage Restoration Coach - Jon Schoen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:16](https://www.youtube.com/watch?v=HFcU3Nls6fM&t=256s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Call doesn't cost you anything let's have a conversation about what I can do to "
              'help you grow your business and make more money and get more jobs thanks a lot '
              'and thanks for watching invest in your financial future.',
      'timestamp': 256,
      'timestamp_label': '[00:04:16]',
      'timestamp_seconds': 256,
      'tip': "Call doesn't cost you anything let's have a conversation about what I can do to "
             'help you grow your business and make more money and get more jobs thanks a lot '
             'and thanks for watching invest in your financial future.',
      'title': '3 Ways to get more water damage jobs from plumbers (Water Damage Restoration '
               'Coach - Jon Schoen)',
      'url': 'https://www.youtube.com/watch?v=HFcU3Nls6fM&t=256s',
      'video_id': 'HFcU3Nls6fM'},
     {'author': 'Roofing Insights',
      'channel': 'Roofing Insights',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:26](https://www.youtube.com/watch?v=ppn4akh1gPo&t=26s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'That could literally make or break your business profit margin and markup a lot '
              "of contractors don't understand the difference and if you get it wrong it.",
      'timestamp': 26,
      'timestamp_label': '[00:00:26]',
      'timestamp_seconds': 26,
      'tip': 'That could literally make or break your business profit margin and markup a lot '
             "of contractors don't understand the difference and if you get it wrong it.",
      'title': "How To price a Job? Profit Margin Vs Markup: Most Roofing Contractors don't "
               'know this (Roofing Insights)',
      'url': 'https://www.youtube.com/watch?v=ppn4akh1gPo&t=26s',
      'video_id': 'ppn4akh1gPo'},
     {'author': 'Restoration Success Strategies | Albi',
      'channel': 'Restoration Success Strategies | Albi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:22](https://www.youtube.com/watch?v=MDZLPIkMaI8&t=322s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Insurance company is able to save some costs and kind of regulate the claims '
              "process and that's a very small percentage of the industry probably.",
      'timestamp': 322,
      'timestamp_label': '[00:05:22]',
      'timestamp_seconds': 322,
      'tip': 'Insurance company is able to save some costs and kind of regulate the claims '
             "process and that's a very small percentage of the industry probably.",
      'title': 'The Ultimate Guide To Water Damage Restoration: Everything You Need To Know '
               '(Restoration Success Strategies | Albi)',
      'url': 'https://www.youtube.com/watch?v=MDZLPIkMaI8&t=322s',
      'video_id': 'MDZLPIkMaI8'},
     {'author': 'Estimate Mastery',
      'channel': 'Estimate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:24](https://www.youtube.com/watch?v=q6R8Iom5Uz8&t=144s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "It's great to rope them in on the overhead and profit conversation. As far as "
              "the specifics of the estimate, it was written in May of 2024. So, that's the "
              "price list we're dealing with. So, we've got some outdated pricing on our "
              'hands.',
      'timestamp': 144,
      'timestamp_label': '[00:02:24]',
      'timestamp_seconds': 144,
      'tip': "It's great to rope them in on the overhead and profit conversation. As far as "
             "the specifics of the estimate, it was written in May of 2024. So, that's the "
             "price list we're dealing with. So, we've got some outdated pricing on our hands.",
      'title': 'Estimate Review - Supplementing in Xactimate (Estimate Mastery)',
      'url': 'https://www.youtube.com/watch?v=q6R8Iom5Uz8&t=144s',
      'video_id': 'q6R8Iom5Uz8'},
     {'author': 'American Roof Supplements',
      'channel': 'American Roof Supplements',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:28](https://www.youtube.com/watch?v=TkCEjbO6vQs&t=448s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Good documentation does not guarantee approval, but poor documentation makes a '
              'legitimate request much harder to evaluate. A supplement cannot rewrite the '
              'insurance policy. It cannot turn actual cash value coverage into replacement '
              'cost value coverage.',
      'timestamp': 448,
      'timestamp_label': '[00:07:28]',
      'timestamp_seconds': 448,
      'tip': 'Good documentation does not guarantee approval, but poor documentation makes a '
             'legitimate request much harder to evaluate. A supplement cannot rewrite the '
             'insurance policy. It cannot turn actual cash value coverage into replacement '
             'cost value coverage.',
      'title': 'Xactimate 101 How Roofing Supplements Actually Work (Beginner’s Guide) '
               '(American Roof Supplements)',
      'url': 'https://www.youtube.com/watch?v=TkCEjbO6vQs&t=448s',
      'video_id': 'TkCEjbO6vQs'},
     {'author': 'Roofing Insights',
      'channel': 'Roofing Insights',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:36:15](https://www.youtube.com/watch?v=uykTx34p0Js&t=2175s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, he keeps following up nonstop. So, we have a a door knocker public '
              'adjuster. On paper, it sounds like a win-win. I get a new roof at no cost. The '
              "only loser seems like an insurance company, but I'm suspicious. What's his real "
              'incentive and should I be concerned?',
      'timestamp': 2175,
      'timestamp_label': '[00:36:15]',
      'timestamp_seconds': 2175,
      'tip': 'Now, he keeps following up nonstop. So, we have a a door knocker public '
             'adjuster. On paper, it sounds like a win-win. I get a new roof at no cost. The '
             "only loser seems like an insurance company, but I'm suspicious. What's his real "
             'incentive and should I be concerned?',
      'title': 'Public Adjusters: Scam or Savior? 5 Key Questions Every Homeowner Must Ask '
               '(Roofing Insights)',
      'url': 'https://www.youtube.com/watch?v=uykTx34p0Js&t=2175s',
      'video_id': 'uykTx34p0Js'},
     {'author': 'Chris Zimmerman',
      'channel': 'Chris Zimmerman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:01](https://www.youtube.com/watch?v=LwNOcenSP_c&t=361s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re all on the same page, that the adjuster, you the contractor, and the "
              'homeowner have all heard the same information and are aware of where we are. '
              'Preferred to get that recorded so that we have an accurate record of what '
              'actually happened.',
      'timestamp': 361,
      'timestamp_label': '[00:06:01]',
      'timestamp_seconds': 361,
      'tip': "'re all on the same page, that the adjuster, you the contractor, and the "
             'homeowner have all heard the same information and are aware of where we are. '
             'Preferred to get that recorded so that we have an accurate record of what '
             'actually happened.',
      'title': 'How to Get More Out of Your First Insurance Adjuster Meeting (Chris Zimmerman)',
      'url': 'https://www.youtube.com/watch?v=LwNOcenSP_c&t=361s',
      'video_id': 'LwNOcenSP_c'},
     {'author': 'Estimate Mastery',
      'channel': 'Estimate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=WNR0K0ubIoI&t=36s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Where you're going to lose the money? First of all, low E is a big deal. Then "
              'right here, the window material price reflects the cost of a standard modular '
              'size window.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': "Where you're going to lose the money? First of all, low E is a big deal. Then "
             'right here, the window material price reflects the cost of a standard modular '
             'size window.',
      'title': 'Make More Money on Your Next Insurance Job With This Xactimate Tip for '
               'Windows! (Estimate Mastery)',
      'url': 'https://www.youtube.com/watch?v=WNR0K0ubIoI&t=36s',
      'video_id': 'WNR0K0ubIoI'},
     {'author': 'Restorex Disaster Restoration',
      'channel': 'Restorex Disaster Restoration',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=nFvUl2Kjwjs&t=89s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Out the red carpet offer the white cup service to the plumbers customers we '
              'want to make that customers so happy that they are responding back thank you '
              'thank you thank you for referring storix in the meantime a little cash in your '
              'pocket.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': 'Out the red carpet offer the white cup service to the plumbers customers we want '
             'to make that customers so happy that they are responding back thank you thank '
             'you thank you for referring storix in the meantime a little cash in your pocket.',
      'title': 'Plumber Referral Program for Indianapolis Plumbers | Restorex Disaster '
               'Restoration (Restorex Disaster Restoration)',
      'url': 'https://www.youtube.com/watch?v=nFvUl2Kjwjs&t=89s',
      'video_id': 'nFvUl2Kjwjs'},
     {'author': 'FirehouseEducation',
      'channel': 'FirehouseEducation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=rAAR3Zmm80c&t=57s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Packing like items together improperly so we don't have damage then please do "
              'that the more items that you have packed and concealed in a box the less '
              'chance.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': "Packing like items together improperly so we don't have damage then please do "
             'that the more items that you have packed and concealed in a box the less chance.',
      'title': 'How To Packout For Sucess On Contents Restoration Jobs (FirehouseEducation)',
      'url': 'https://www.youtube.com/watch?v=rAAR3Zmm80c&t=57s',
      'video_id': 'rAAR3Zmm80c'},
     {'author': 'Chad Michael - The Practitioner',
      'channel': 'Chad Michael - The Practitioner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=DmesIP8hcak&t=20s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Deductible right mine has a deductible problems like they're trying to get you "
              "to waive the deductible right or cover that it up and why is that they're "
              'trying to do that because everybody else is doing it right.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Deductible right mine has a deductible problems like they're trying to get you "
             "to waive the deductible right or cover that it up and why is that they're trying "
             'to do that because everybody else is doing it right.',
      'title': 'How to Legally COVER The Deductible (Chad Michael - The Practitioner)',
      'url': 'https://www.youtube.com/watch?v=DmesIP8hcak&t=20s',
      'video_id': 'DmesIP8hcak'},
     {'author': 'FirehouseEducation',
      'channel': 'FirehouseEducation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:37](https://www.youtube.com/watch?v=GhZSitNz6aQ&t=397s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I believe that's in other news I I can't remember suddenly on the video anyway "
              'so you can catch up and catch all the videos and I thank you so much for '
              'watching and until then I will see you on the next video.',
      'timestamp': 397,
      'timestamp_label': '[00:06:37]',
      'timestamp_seconds': 397,
      'tip': "I believe that's in other news I I can't remember suddenly on the video anyway "
             'so you can catch up and catch all the videos and I thank you so much for '
             'watching and until then I will see you on the next video.',
      'title': 'What Is a Public Adjuster and what is their role in Restoration? '
               '(FirehouseEducation)',
      'url': 'https://www.youtube.com/watch?v=GhZSitNz6aQ&t=397s',
      'video_id': 'GhZSitNz6aQ'}],
 4: [{'author': 'Homeowner Explained',
      'channel': 'Homeowner Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:37](https://www.youtube.com/watch?v=MPSOkm3YFak&t=457s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Sometimes it's an assignment of benefits that hands your claim, and your "
              "insurance check, to them. Never sign anything you haven't read, and never sign "
              'under pressure. Red flag four: no local address, no reviews, and no license '
              'where your state requires one.',
      'timestamp': 457,
      'timestamp_label': '[00:07:37]',
      'timestamp_seconds': 457,
      'tip': "Sometimes it's an assignment of benefits that hands your claim, and your "
             "insurance check, to them. Never sign anything you haven't read, and never sign "
             'under pressure. Red flag four: no local address, no reviews, and no license '
             'where your state requires one.',
      'title': 'Did the Hail Really Damage Your Roof? Check This First (Homeowner Explained)',
      'url': 'https://www.youtube.com/watch?v=MPSOkm3YFak&t=457s',
      'video_id': 'MPSOkm3YFak'},
     {'author': 'PuroClean of Central Southwest Houston',
      'channel': 'PuroClean of Central Southwest Houston',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=HHLnyMyxcpQ&t=36s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The very first step is documentation. This is critical for the insurance '
              'compliance. We use our company phones to capture photos and everything, '
              'moisture readings, close-up of damage, damage items, even 3D scans with Docky '
              'Sketch.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': 'The very first step is documentation. This is critical for the insurance '
             'compliance. We use our company phones to capture photos and everything, moisture '
             'readings, close-up of damage, damage items, even 3D scans with Docky Sketch.',
      'title': 'The Water Damage Mitigation Process Step by Step by PuroClean (PuroClean of '
               'Central Southwest Houston)',
      'url': 'https://www.youtube.com/watch?v=HHLnyMyxcpQ&t=36s',
      'video_id': 'HHLnyMyxcpQ'},
     {'author': 'Be A Claims Adjuster',
      'channel': 'Be A Claims Adjuster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=u947iwIhI7A&t=54s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sedwick is a third-party administrator, TPA. They handle claims on behalf of '
              "other businesses, but don't sell insurance policies themselves. Employment "
              'structure, State Farm. You work for the insurance company itself.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'Sedwick is a third-party administrator, TPA. They handle claims on behalf of '
             "other businesses, but don't sell insurance policies themselves. Employment "
             'structure, State Farm. You work for the insurance company itself.',
      'title': 'State Farm vs Sedgwick: Which is Better for New Claims Adjusters? (Be A Claims '
               'Adjuster)',
      'url': 'https://www.youtube.com/watch?v=u947iwIhI7A&t=54s',
      'video_id': 'u947iwIhI7A'},
     {'author': 'Chad Michael - The Practitioner',
      'channel': 'Chad Michael - The Practitioner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:05](https://www.youtube.com/watch?v=vkrXTVQcVQQ&t=1505s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Of it in terms of insurance claims like whenever there's new evidence brought "
              "forth then it's like we can it's new damage new damage like Dam not not.",
      'timestamp': 1505,
      'timestamp_label': '[00:25:05]',
      'timestamp_seconds': 1505,
      'tip': "Of it in terms of insurance claims like whenever there's new evidence brought "
             "forth then it's like we can it's new damage new damage like Dam not not.",
      'title': 'When the Contractor and the Insurance Adjuster Disagree | Effective Methods To '
               'Unlock Stalemate (Chad Michael - The Practitioner)',
      'url': 'https://www.youtube.com/watch?v=vkrXTVQcVQQ&t=1505s',
      'video_id': 'vkrXTVQcVQQ'},
     {'author': 'Claims Underground Podcast',
      'channel': 'Claims Underground Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=bPBmUaKay2w&t=20s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The runaround and ready to find out what's really going on then let's get down "
              'to business and learn from the insurance claims experts Corey Locke and Troy '
              'Willis foreign.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "The runaround and ready to find out what's really going on then let's get down "
             'to business and learn from the insurance claims experts Corey Locke and Troy '
             'Willis foreign.',
      'title': 'Claims Underground Podcast: Mastering Assignment of Benefits with Top Public '
               'Adjusters (Claims Underground Podcast)',
      'url': 'https://www.youtube.com/watch?v=bPBmUaKay2w&t=20s',
      'video_id': 'bPBmUaKay2w'},
     {'author': 'The STRONG Roofer w/ Adam Bensman',
      'channel': 'The STRONG Roofer w/ Adam Bensman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:28](https://www.youtube.com/watch?v=zxGa72oAf0w&t=448s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Software that the insurance company needs we submit that to them on your behalf '
              "to say hey guess what guys you missed x y and z here's all the.",
      'timestamp': 448,
      'timestamp_label': '[00:07:28]',
      'timestamp_seconds': 448,
      'tip': 'Software that the insurance company needs we submit that to them on your behalf '
             "to say hey guess what guys you missed x y and z here's all the.",
      'title': 'Explaining Supplements to Homeowners: How Roof Insurance Claim Supplements '
               'Work (The STRONG Roofer w/ Adam Bensman)',
      'url': 'https://www.youtube.com/watch?v=zxGa72oAf0w&t=448s',
      'video_id': 'zxGa72oAf0w'},
     {'author': 'MN Labor and Industry',
      'channel': 'MN Labor and Industry',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=xXGIjQfUG4s&t=22s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You can see I'm a part of a few groups here. I'm going to look at Up North "
              'Insurance. So, if I simply wanted to view the claims on my entity details page, '
              'I would want to look for a few things. So, first off, I see that I have global '
              'claim access permissions.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "You can see I'm a part of a few groups here. I'm going to look at Up North "
             'Insurance. So, if I simply wanted to view the claims on my entity details page, '
             'I would want to look for a few things. So, first off, I see that I have global '
             'claim access permissions.',
      'title': 'Claim access for insurers and third-party administrators (MN Labor and '
               'Industry)',
      'url': 'https://www.youtube.com/watch?v=xXGIjQfUG4s&t=22s',
      'video_id': 'xXGIjQfUG4s'},
     {'author': 'The Claim Squad Public Adjusters',
      'channel': 'The Claim Squad Public Adjusters',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:18](https://www.youtube.com/watch?v=h_W9kUbadMM&t=438s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Don't know let's say 20 000. now they're thinking they can save this and now "
              'this is 10 bucks this is how the insurance company works this is what you get '
              'when you use an insurance company contractor cutting corners going on the cheap '
              'and you as a homeowner have no idea.',
      'timestamp': 438,
      'timestamp_label': '[00:07:18]',
      'timestamp_seconds': 438,
      'tip': "Don't know let's say 20 000. now they're thinking they can save this and now "
             'this is 10 bucks this is how the insurance company works this is what you get '
             'when you use an insurance company contractor cutting corners going on the cheap '
             'and you as a homeowner have no idea.',
      'title': '5 Reasons Not to Use Your Insurance Company Contractor: Water Mitigation or '
               'Restoration Company (The Claim Squad Public Adjusters)',
      'url': 'https://www.youtube.com/watch?v=h_W9kUbadMM&t=438s',
      'video_id': 'h_W9kUbadMM'},
     {'author': 'yourEadvisor.com',
      'channel': 'yourEadvisor.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:36](https://www.youtube.com/watch?v=On3xbq5nLqk&t=276s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Us I hope this helps it's a very basic understanding check out our Facebook "
              'page for more information on homeowners insurance and some of this stuff '
              'because we do post as we kind of here stuff with the Florida Legislature thanks '
              'look for it in the next video.',
      'timestamp': 276,
      'timestamp_label': '[00:04:36]',
      'timestamp_seconds': 276,
      'tip': "Us I hope this helps it's a very basic understanding check out our Facebook page "
             'for more information on homeowners insurance and some of this stuff because we '
             'do post as we kind of here stuff with the Florida Legislature thanks look for it '
             'in the next video.',
      'title': 'Assignment of Benefits (AOB) (yourEadvisor.com)',
      'url': 'https://www.youtube.com/watch?v=On3xbq5nLqk&t=276s',
      'video_id': 'On3xbq5nLqk'},
     {'author': 'Richard Levisee',
      'channel': 'Richard Levisee',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:37](https://www.youtube.com/watch?v=VFWDHse67ws&t=457s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Think I've already went over the contractor's waiver of lean they got the their "
              "own form in there they want you to fill out let's see here the tax.",
      'timestamp': 457,
      'timestamp_label': '[00:07:37]',
      'timestamp_seconds': 457,
      'tip': "Think I've already went over the contractor's waiver of lean they got the their "
             "own form in there they want you to fill out let's see here the tax.",
      'title': 'Insurance check has my mortgage company on it. What do I do? (Richard Levisee)',
      'url': 'https://www.youtube.com/watch?v=VFWDHse67ws&t=457s',
      'video_id': 'VFWDHse67ws'},
     {'author': 'AARP Florida - The Sunshine State!',
      'channel': 'AARP Florida - The Sunshine State!',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:41](https://www.youtube.com/watch?v=vscXMMen_rc&t=101s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I think is a challenge that you really have to watch self not necessarily '
              'always self but the fraud part and your loss and if you turn your insurance.',
      'timestamp': 101,
      'timestamp_label': '[00:01:41]',
      'timestamp_seconds': 101,
      'tip': 'I think is a challenge that you really have to watch self not necessarily always '
             'self but the fraud part and your loss and if you turn your insurance.',
      'title': 'Barbara Day Assignment of Benefits (AOB) on insurance claims (AARP Florida - '
               'The Sunshine State!)',
      'url': 'https://www.youtube.com/watch?v=vscXMMen_rc&t=101s',
      'video_id': 'vscXMMen_rc'},
     {'author': 'Canei Adjusting',
      'channel': 'Canei Adjusting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=Z7kbWUDeX6A&t=75s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And you could change that by going here and changing the floor protection. '
              'Insurance companies are going to want to use that. Now, the company that I had '
              'this macro for, they want to use a primitive floor plus 17.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': 'And you could change that by going here and changing the floor protection. '
             'Insurance companies are going to want to use that. Now, the company that I had '
             'this macro for, they want to use a primitive floor plus 17.',
      'title': 'WALL XACTIMATE LINE ITEMS (Canei Adjusting)',
      'url': 'https://www.youtube.com/watch?v=Z7kbWUDeX6A&t=75s',
      'video_id': 'Z7kbWUDeX6A'},
     {'author': "Shane O'Dazier | RestorationProfits",
      'channel': "Shane O'Dazier | RestorationProfits",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=NyqgMvKRX14&t=15s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'To look at five different things that you can do to fight off the insurance '
              'company when they try to whittle down your estimate or your invoice if you own.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'To look at five different things that you can do to fight off the insurance '
             'company when they try to whittle down your estimate or your invoice if you own.',
      'title': 'How to avoid insurance reductions on estimates for water damage restoration '
               "(Shane O'Dazier | RestorationProfits)",
      'url': 'https://www.youtube.com/watch?v=NyqgMvKRX14&t=15s',
      'video_id': 'NyqgMvKRX14'},
     {'author': 'Coach8',
      'channel': 'Coach8',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:48:34](https://www.youtube.com/watch?v=7gZTdFWoHgs&t=2914s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'It is recommended that a specialized excerpt expert be consulted prior to '
              "determining the appropriate repair so it's recommended we get a specialized "
              "expertise now I'd encourage you to have a look at the definition of a "
              'specialized expert within this new document.',
      'timestamp': 2914,
      'timestamp_label': '[00:48:34]',
      'timestamp_seconds': 2914,
      'tip': 'It is recommended that a specialized excerpt expert be consulted prior to '
             "determining the appropriate repair so it's recommended we get a specialized "
             "expertise now I'd encourage you to have a look at the definition of a "
             'specialized expert within this new document.',
      'title': 'Reviewing the ANSI/IICRC S500 2021 Standard for Professional Water Damage '
               'Restoration, 5th Edition (Coach8)',
      'url': 'https://www.youtube.com/watch?v=7gZTdFWoHgs&t=2914s',
      'video_id': '7gZTdFWoHgs'},
     {'author': 'Chad Michael - The Practitioner',
      'channel': 'Chad Michael - The Practitioner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:14](https://www.youtube.com/watch?v=tYSY3Eo_nvA&t=254s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "We're being paid properly because you don't know your guys going in to remove "
              "that stuff and Gao sorry to remove that stuff if they're not properly protected "
              "with the personal protection equipment masks etc we'll get in that stuff later "
              'on the training course.',
      'timestamp': 254,
      'timestamp_label': '[00:04:14]',
      'timestamp_seconds': 254,
      'tip': "We're being paid properly because you don't know your guys going in to remove "
             "that stuff and Gao sorry to remove that stuff if they're not properly protected "
             "with the personal protection equipment masks etc we'll get in that stuff later "
             'on the training course.',
      'title': 'Insurance Adjusters Use Wrong Xactimate Estimate Items | Wet Drywall (Chad '
               'Michael - The Practitioner)',
      'url': 'https://www.youtube.com/watch?v=tYSY3Eo_nvA&t=254s',
      'video_id': 'tYSY3Eo_nvA'}],
 5: [{'author': 'Happy Adjuster',
      'channel': 'Happy Adjuster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:41](https://www.youtube.com/watch?v=hqbiodyd1gc&t=41s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s overpriced, unnecessary, or even never completed. Once you've signed an AOB, "
              'you could be cut out of the conversation entirely. And in some cases, you may '
              'end up in the middle of a legal dispute between the contractor and your '
              'insurance company.',
      'timestamp': 41,
      'timestamp_label': '[00:00:41]',
      'timestamp_seconds': 41,
      'tip': "'s overpriced, unnecessary, or even never completed. Once you've signed an AOB, "
             'you could be cut out of the conversation entirely. And in some cases, you may '
             'end up in the middle of a legal dispute between the contractor and your '
             'insurance company.',
      'title': 'What Is an Assignment of Benefits (AOB)? | Should You Sign One After a '
               'Property Damage Claim? (Happy Adjuster)',
      'url': 'https://www.youtube.com/watch?v=hqbiodyd1gc&t=41s',
      'video_id': 'hqbiodyd1gc'},
     {'author': 'Avner Gat, Inc. - Public Insurance Adjusters',
      'channel': 'Avner Gat, Inc. - Public Insurance Adjusters',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=8x3Gfr6Uyr8&t=92s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Materials and  allow the restoration company to come back and finish the '
              'drying. If the asbestos testing results coming  negative.',
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': 'Materials and  allow the restoration company to come back and finish the drying. '
             'If the asbestos testing results coming  negative.',
      'title': 'Ask Avner Deep Dive: Restoration Companies vs Insurance Claims (Avner Gat, '
               'Inc. - Public Insurance Adjusters)',
      'url': 'https://www.youtube.com/watch?v=8x3Gfr6Uyr8&t=92s',
      'video_id': '8x3Gfr6Uyr8'},
     {'author': 'State Farm Insurance',
      'channel': 'State Farm Insurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=bNL46sw5_5c&t=79s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Dispute arbitration is an option for most subrogation claims where a major '
              'insurance company is involved.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': 'Dispute arbitration is an option for most subrogation claims where a major '
             'insurance company is involved.',
      'title': 'Auto Claims Subrogation/Deductible Refund Process | State Farm (State Farm '
               'Insurance)',
      'url': 'https://www.youtube.com/watch?v=bNL46sw5_5c&t=79s',
      'video_id': 'bNL46sw5_5c'},
     {'author': 'Crossroads Insurance Recovery',
      'channel': 'Crossroads Insurance Recovery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:35](https://www.youtube.com/watch?v=iKLGuESx4po&t=155s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then release funds as the repairs are completed at each state doing a direct '
              'assignment of benefits to a contractor removes that possibility for the.',
      'timestamp': 155,
      'timestamp_label': '[00:02:35]',
      'timestamp_seconds': 155,
      'tip': 'Then release funds as the repairs are completed at each state doing a direct '
             'assignment of benefits to a contractor removes that possibility for the.',
      'title': 'Assignment of Benefits in Your Insurance Claim (Crossroads Insurance Recovery)',
      'url': 'https://www.youtube.com/watch?v=iKLGuESx4po&t=155s',
      'video_id': 'iKLGuESx4po'},
     {'author': "Shane O'Dazier | RestorationProfits",
      'channel': "Shane O'Dazier | RestorationProfits",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:23](https://www.youtube.com/watch?v=3xfQ7PdL-AA&t=563s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Information we get on a call and see how we can help you grow your company '
              "lastly there'll be some other videos right here here if you want to watch more "
              'content about growing your Restoration company check out one of these videos '
              "we'll see you guys on the next one.",
      'timestamp': 563,
      'timestamp_label': '[00:09:23]',
      'timestamp_seconds': 563,
      'tip': 'Information we get on a call and see how we can help you grow your company '
             "lastly there'll be some other videos right here here if you want to watch more "
             'content about growing your Restoration company check out one of these videos '
             "we'll see you guys on the next one.",
      'title': "How to negotiate with adjusters | restoration company (Shane O'Dazier | "
               'RestorationProfits)',
      'url': 'https://www.youtube.com/watch?v=3xfQ7PdL-AA&t=563s',
      'video_id': '3xfQ7PdL-AA'},
     {'author': 'Roof Sales Mastery',
      'channel': 'Roof Sales Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=q63afBPc6eY&t=62s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Items all the time rigin I call it the basic BS it's like rigin starter "
              'overhead and profit flashings drip edge ice of water shield mismeasurements on.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': "Items all the time rigin I call it the basic BS it's like rigin starter overhead "
             'and profit flashings drip edge ice of water shield mismeasurements on.',
      'title': 'How to Supplement Insurance Roofing Claims with Xactimate (Roof Sales Mastery)',
      'url': 'https://www.youtube.com/watch?v=q63afBPc6eY&t=62s',
      'video_id': 'q63afBPc6eY'},
     {'author': 'claimhelpme',
      'channel': 'claimhelpme',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:40](https://www.youtube.com/watch?v=2WVlG5yPBTU&t=220s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And this is where estimating matters. A weak estimate creates a weak starting '
              'point. A weak carrier estimate that nobody challenges becomes the number '
              'everybody starts negotiating from. That is what I call a baseline problem.',
      'timestamp': 220,
      'timestamp_label': '[00:03:40]',
      'timestamp_seconds': 220,
      'tip': 'And this is where estimating matters. A weak estimate creates a weak starting '
             'point. A weak carrier estimate that nobody challenges becomes the number '
             'everybody starts negotiating from. That is what I call a baseline problem.',
      'title': 'What Does a Public Adjuster Actually Do? Insurance Estimates, Settlements & '
               'Your Rights (claimhelpme)',
      'url': 'https://www.youtube.com/watch?v=2WVlG5yPBTU&t=220s',
      'video_id': '2WVlG5yPBTU'},
     {'author': 'Balanced Building Biology',
      'channel': 'Balanced Building Biology',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:00](https://www.youtube.com/watch?v=YdUmzaa5wO0&t=480s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "It's just a basic quality check performed by the remediator, essentially "
              "checking their own work. That's fine for simple, low-risk jobs. But a PRV, "
              'post-remediation verification, that is your independent guarantee.',
      'timestamp': 480,
      'timestamp_label': '[00:08:00]',
      'timestamp_seconds': 480,
      'tip': "It's just a basic quality check performed by the remediator, essentially "
             "checking their own work. That's fine for simple, low-risk jobs. But a PRV, "
             'post-remediation verification, that is your independent guarantee.',
      'title': 'Mould Remediation Done Right: The Official IICRC S520 Homeowner Guide '
               '(Balanced Building Biology)',
      'url': 'https://www.youtube.com/watch?v=YdUmzaa5wO0&t=480s',
      'video_id': 'YdUmzaa5wO0'},
     {'author': 'Daly & Black, P.C.',
      'channel': 'Daly & Black, P.C.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:30](https://www.youtube.com/watch?v=jaGktNyKvE4&t=150s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Don't to pay you and the result is you get left holding the bag so if you've "
              "got questions about whether or not you're engaged in a process that is against "
              'the law in your stay talk to somebody before you put yourself at risk call '
              'someone who knows.',
      'timestamp': 150,
      'timestamp_label': '[00:02:30]',
      'timestamp_seconds': 150,
      'tip': "Don't to pay you and the result is you get left holding the bag so if you've got "
             "questions about whether or not you're engaged in a process that is against the "
             'law in your stay talk to somebody before you put yourself at risk call someone '
             'who knows.',
      'title': 'Unauthorized Practice of Public Adjusting (UPPA) (Daly & Black, P.C.)',
      'url': 'https://www.youtube.com/watch?v=jaGktNyKvE4&t=150s',
      'video_id': 'jaGktNyKvE4'},
     {'author': 'American Roof Supplements',
      'channel': 'American Roof Supplements',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=HpoMhPz1KfU&t=52s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Measurements, shingles, tear off, underlayment, ridge, a few accessories, nice '
              "clean PDF, very official. And that's why you still need to check the details. "
              'Because the biggest problem is rarely a giant red line that says we forgot half '
              'the roof.',
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': 'Measurements, shingles, tear off, underlayment, ridge, a few accessories, nice '
             "clean PDF, very official. And that's why you still need to check the details. "
             'Because the biggest problem is rarely a giant red line that says we forgot half '
             'the roof.',
      'title': 'How to Prove an Insurance Estimate Wrong — Line by Line in Xactimate (American '
               'Roof Supplements)',
      'url': 'https://www.youtube.com/watch?v=HpoMhPz1KfU&t=52s',
      'video_id': 'HpoMhPz1KfU'},
     {'author': 'Roofing Insights',
      'channel': 'Roofing Insights',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:23](https://www.youtube.com/watch?v=FqdbOCycivo&t=563s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Are not using all in-house crews and you know that I wouldn't went to business "
              "school 15 years ago lord knows where I'd be right now so the kids definitely "
              'need that but as far as fixing our problem to get these bigger companies and '
              'say hey.',
      'timestamp': 563,
      'timestamp_label': '[00:09:23]',
      'timestamp_seconds': 563,
      'tip': "Are not using all in-house crews and you know that I wouldn't went to business "
             "school 15 years ago lord knows where I'd be right now so the kids definitely "
             'need that but as far as fixing our problem to get these bigger companies and say '
             'hey.',
      'title': 'Roofer on Roofing Subcontractors | Illegal Roofers | Kareem Hunter (Roofing '
               'Insights)',
      'url': 'https://www.youtube.com/watch?v=FqdbOCycivo&t=563s',
      'video_id': 'FqdbOCycivo'},
     {'author': 'Chris Hatcher',
      'channel': 'Chris Hatcher',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:07](https://www.youtube.com/watch?v=i4kOEeFrMaI&t=307s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Button and click on it machine's going to do a self check make sure there's no "
              "duplications I'm just going to go with the final draft with or without removal "
              'of depreciation and click on view.',
      'timestamp': 307,
      'timestamp_label': '[00:05:07]',
      'timestamp_seconds': 307,
      'tip': "Button and click on it machine's going to do a self check make sure there's no "
             "duplications I'm just going to go with the final draft with or without removal "
             'of depreciation and click on view.',
      'title': 'TopAdjuster.com Xactimate tutorial - Mitigation and Restoration total pages '
               'from one estimate (Chris Hatcher)',
      'url': 'https://www.youtube.com/watch?v=i4kOEeFrMaI&t=307s',
      'video_id': 'i4kOEeFrMaI'},
     {'author': 'TheIICRC',
      'channel': 'TheIICRC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:59](https://www.youtube.com/watch?v=0HzVwvOo2Ww&t=179s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Submit as your work documentation how much experience is required and what '
              'kinds of documents you should provide click on the ad button to begin uploading '
              'job information and fill out the page click.',
      'timestamp': 179,
      'timestamp_label': '[00:02:59]',
      'timestamp_seconds': 179,
      'tip': 'Submit as your work documentation how much experience is required and what kinds '
             'of documents you should provide click on the ad button to begin uploading job '
             'information and fill out the page click.',
      'title': 'IICRC Mold Remediation Specialist (MRS) Application Guide (TheIICRC)',
      'url': 'https://www.youtube.com/watch?v=0HzVwvOo2Ww&t=179s',
      'video_id': '0HzVwvOo2Ww'},
     {'author': 'Restoration Technical Institute',
      'channel': 'Restoration Technical Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:09](https://www.youtube.com/watch?v=XMpZ-8ZsSW8&t=69s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Back however the extraction point is in the front this nylon squeegee bar right '
              "here is the compression point and it's also the extraction point so when you "
              'ride this you want to keep your weight to the front.',
      'timestamp': 69,
      'timestamp_label': '[00:01:09]',
      'timestamp_seconds': 69,
      'tip': 'Back however the extraction point is in the front this nylon squeegee bar right '
             "here is the compression point and it's also the extraction point so when you "
             'ride this you want to keep your weight to the front.',
      'title': 'POV: Applied Structural Drying with RTI | IICRC ASD Course with Destry '
               'Ransdell (Restoration Technical Institute)',
      'url': 'https://www.youtube.com/watch?v=XMpZ-8ZsSW8&t=69s',
      'video_id': 'XMpZ-8ZsSW8'},
     {'author': "Shane O'Dazier | RestorationProfits",
      'channel': "Shane O'Dazier | RestorationProfits",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:01](https://www.youtube.com/watch?v=D4BavFC6d1E&t=301s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Knowing what they want second problem assuming you know what they want right '
              "you can't treat them all the same these are relationships all right.",
      'timestamp': 301,
      'timestamp_label': '[00:05:01]',
      'timestamp_seconds': 301,
      'tip': 'Knowing what they want second problem assuming you know what they want right you '
             "can't treat them all the same these are relationships all right.",
      'title': 'How to get referrals for a water damage restoration business - plumbers (Shane '
               "O'Dazier | RestorationProfits)",
      'url': 'https://www.youtube.com/watch?v=D4BavFC6d1E&t=301s',
      'video_id': 'D4BavFC6d1E'}],
 6: [{'author': 'Integrity Roofing and Painting',
      'channel': 'Integrity Roofing and Painting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=Mi6XZq4h6yo&t=40s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'To follow a protocol of your mortgage company in order to get that insurance '
              'check endorsed what we recommend is to first call your branch to find out what.',
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': 'To follow a protocol of your mortgage company in order to get that insurance '
             'check endorsed what we recommend is to first call your branch to find out what.',
      'title': 'Mortgage Company Insurance Check Endorsement (Integrity Roofing and Painting)',
      'url': 'https://www.youtube.com/watch?v=Mi6XZq4h6yo&t=40s',
      'video_id': 'Mi6XZq4h6yo'},
     {'author': 'Encircle',
      'channel': 'Encircle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:30](https://www.youtube.com/watch?v=uy09gaqf4AU&t=390s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So describing that damage is the first step that then feeds into a detailed '
              'scope, and now that feeds into the Xactimate estimate. Encircle Scope to '
              'Xactimate Estimate is the straightest line from field documentation to a '
              'defensible estimate that you will find.',
      'timestamp': 390,
      'timestamp_label': '[00:06:30]',
      'timestamp_seconds': 390,
      'tip': 'So describing that damage is the first step that then feeds into a detailed '
             'scope, and now that feeds into the Xactimate estimate. Encircle Scope to '
             'Xactimate Estimate is the straightest line from field documentation to a '
             'defensible estimate that you will find.',
      'title': 'A New Era of Estimating | Your Data, Your Expertise, From Scope to Estimate '
               '—\xa0Webinar (Encircle)',
      'url': 'https://www.youtube.com/watch?v=uy09gaqf4AU&t=390s',
      'video_id': 'uy09gaqf4AU'},
     {'author': 'AnnePullen',
      'channel': 'AnnePullen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=tLwSSUZ6Awc&t=104s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'A contractor who offers to make your deductible disappear is usually planning '
              "to inflate the estimate to absorb it. That's insurance fraud with your name on "
              "the paperwork and it's illegal in most states. If a company offers you that "
              "deal, that's not generosity.",
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': 'A contractor who offers to make your deductible disappear is usually planning to '
             "inflate the estimate to absorb it. That's insurance fraud with your name on the "
             "paperwork and it's illegal in most states. If a company offers you that deal, "
             "that's not generosity.",
      'title': 'Your Insurance Deductible After a Claim: What Nobody Tells You (AnnePullen)',
      'url': 'https://www.youtube.com/watch?v=tLwSSUZ6Awc&t=104s',
      'video_id': 'tLwSSUZ6Awc'},
     {'author': 'Restoration Made Simple',
      'channel': 'Restoration Made Simple',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=8nQyv3vEI6A&t=21s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Um you could be $300, $500, $800. I'm hearing in some parts of the country "
              'right now a water damage lead through a lead source or a lead generation '
              'company can be $1,500, $1,600, okay?',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "Um you could be $300, $500, $800. I'm hearing in some parts of the country right "
             'now a water damage lead through a lead source or a lead generation company can '
             'be $1,500, $1,600, okay?',
      'title': 'Close More Water Damage Restoration Leads - Call Conversion Tips (Restoration '
               'Made Simple)',
      'url': 'https://www.youtube.com/watch?v=8nQyv3vEI6A&t=21s',
      'video_id': '8nQyv3vEI6A'},
     {'author': 'Verisk Property and Restoration Solutions',
      'channel': 'Verisk Property and Restoration Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=wTueMQ06kvA&t=40s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The first step is to add on your sketch where you intend to put any containment '
              'barriers, essentially, creating drying chambers or divisions in the home. To '
              'add a barrier, sketch a missing wall that surrounds the water damage in the '
              'living room.',
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': 'The first step is to add on your sketch where you intend to put any containment '
             'barriers, essentially, creating drying chambers or divisions in the home. To add '
             'a barrier, sketch a missing wall that surrounds the water damage in the living '
             'room.',
      'title': 'Xactimate Xpert Tip: Starting a Water Mitigation in Estimate in XactScope '
               '(Verisk Property and Restoration Solutions)',
      'url': 'https://www.youtube.com/watch?v=wTueMQ06kvA&t=40s',
      'video_id': 'wTueMQ06kvA'},
     {'author': 'The Restoration Advisors Group',
      'channel': 'The Restoration Advisors Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:20](https://www.youtube.com/watch?v=qQzYZWLmaSI&t=140s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mind and I can contrl f search something that is related to it and find what I '
              'wrote for find what somebody else in our company had wrote for and and just go.',
      'timestamp': 140,
      'timestamp_label': '[00:02:20]',
      'timestamp_seconds': 140,
      'tip': 'Mind and I can contrl f search something that is related to it and find what I '
             'wrote for find what somebody else in our company had wrote for and and just go.',
      'title': 'Ultimate Xactimate Cheat Sheet & How I built a chatbot to help write my '
               'estimates (The Restoration Advisors Group)',
      'url': 'https://www.youtube.com/watch?v=qQzYZWLmaSI&t=140s',
      'video_id': 'qQzYZWLmaSI'},
     {'author': "Shane O'Dazier | RestorationProfits",
      'channel': "Shane O'Dazier | RestorationProfits",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:31](https://www.youtube.com/watch?v=xXe9Z763dDc&t=1171s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '80% of the time that never happens. But, in the 20% of the time that they do '
              'find a winner, the minute that that guy walks out to go start his own company, '
              'all your business left with him, bro. All of your business left with him.',
      'timestamp': 1171,
      'timestamp_label': '[00:19:31]',
      'timestamp_seconds': 1171,
      'tip': '80% of the time that never happens. But, in the 20% of the time that they do '
             'find a winner, the minute that that guy walks out to go start his own company, '
             'all your business left with him, bro. All of your business left with him.',
      'title': "How to get consistent water damage jobs without storms (Shane O'Dazier | "
               'RestorationProfits)',
      'url': 'https://www.youtube.com/watch?v=xXe9Z763dDc&t=1171s',
      'video_id': 'xXe9Z763dDc'},
     {'author': 'Xactimate Training by Crest LLC',
      'channel': 'Xactimate Training by Crest LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:05](https://www.youtube.com/watch?v=ZY8afiQROiI&t=605s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So I'm going to recommend that you actually put the contractor's name in there "
              "now how do you do that first thing we're going to do is we're going to add one "
              'of these guys in here so just click right here where it says add.',
      'timestamp': 605,
      'timestamp_label': '[00:10:05]',
      'timestamp_seconds': 605,
      'tip': "So I'm going to recommend that you actually put the contractor's name in there "
             "now how do you do that first thing we're going to do is we're going to add one "
             'of these guys in here so just click right here where it says add.',
      'title': 'Xactimate - Global Depreciation, Bid Item (from the "Desk Adjuster" course) '
               '(Xactimate Training by Crest LLC)',
      'url': 'https://www.youtube.com/watch?v=ZY8afiQROiI&t=605s',
      'video_id': 'ZY8afiQROiI'},
     {'author': 'EstimateTV',
      'channel': 'EstimateTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=sSaHviAzZ6w&t=78s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "There's a little drop down. If you click on that, it'll bring back the search. "
              'If I hit paint and then hit the return key or hit the search button, we want to '
              'go to the item search results, which is the first 100 matching items.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': "There's a little drop down. If you click on that, it'll bring back the search. "
             'If I hit paint and then hit the return key or hit the search button, we want to '
             'go to the item search results, which is the first 100 matching items.',
      'title': 'How to find materials and repairs in Xactimate | Line Items and Search '
               '(EstimateTV)',
      'url': 'https://www.youtube.com/watch?v=sSaHviAzZ6w&t=78s',
      'video_id': 'sSaHviAzZ6w'},
     {'author': 'Water Damage Restoration Marketing - Vinnie Mac',
      'channel': 'Water Damage Restoration Marketing - Vinnie Mac',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:26](https://www.youtube.com/watch?v=2akNGTmJry8&t=206s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'SEO or Maps uh Google Business Profile lead volume and then the the gray column '
              'uh the fourth column over are PPC results and then the summary on the '
              'right-hand column.',
      'timestamp': 206,
      'timestamp_label': '[00:03:26]',
      'timestamp_seconds': 206,
      'tip': 'SEO or Maps uh Google Business Profile lead volume and then the the gray column '
             'uh the fourth column over are PPC results and then the summary on the right-hand '
             'column.',
      'title': 'Google Local Service Ads For Water Damage Restoration Companies Everything You '
               'Need To Know In 2026 (Water Damage Restoration Marketing - Vinnie Mac)',
      'url': 'https://www.youtube.com/watch?v=2akNGTmJry8&t=206s',
      'video_id': '2akNGTmJry8'},
     {'author': 'TheIICRC',
      'channel': 'TheIICRC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:57](https://www.youtube.com/watch?v=JOiWfXdUwjM&t=1437s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Lead remediator to Hey listen I check this place out I I consider this PO '
              "mediation evaluation I say it's okay and good to go for that must be done in "
              "every case so it's a good thing to have to to be able to do that see how all "
              'jobs get to be verified by an IEP.',
      'timestamp': 1437,
      'timestamp_label': '[00:23:57]',
      'timestamp_seconds': 1437,
      'tip': 'Lead remediator to Hey listen I check this place out I I consider this PO '
             "mediation evaluation I say it's okay and good to go for that must be done in "
             "every case so it's a good thing to have to to be able to do that see how all "
             'jobs get to be verified by an IEP.',
      'title': 'IICRC June Webinar: S520 2024 Standard (TheIICRC)',
      'url': 'https://www.youtube.com/watch?v=JOiWfXdUwjM&t=1437s',
      'video_id': 'JOiWfXdUwjM'},
     {'author': 'James Poon',
      'channel': 'James Poon',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:33:43](https://www.youtube.com/watch?v=r1JeD2hb2jM&t=2023s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "That's separate to the restore remediator this is normally a larger area of "
              'damage or contamination that impacts multiple zones or rooms the area of water '
              'damage or contamination is often greater than 10 square m.',
      'timestamp': 2023,
      'timestamp_label': '[00:33:43]',
      'timestamp_seconds': 2023,
      'tip': "That's separate to the restore remediator this is normally a larger area of "
             'damage or contamination that impacts multiple zones or rooms the area of water '
             'damage or contamination is often greater than 10 square m.',
      'title': 'AS-IICRC S520-2024 Nicole Bijlsma (James Poon)',
      'url': 'https://www.youtube.com/watch?v=r1JeD2hb2jM&t=2023s',
      'video_id': 'r1JeD2hb2jM'},
     {'author': 'Chad Michael - The Practitioner',
      'channel': 'Chad Michael - The Practitioner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:37](https://www.youtube.com/watch?v=Lh586v6HcYw&t=1477s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You know but like I said I like to keep some things in my back pocket bedroom '
              'two master bedroom office living room so a lot of interior damage right general '
              'conditions.',
      'timestamp': 1477,
      'timestamp_label': '[00:24:37]',
      'timestamp_seconds': 1477,
      'tip': 'You know but like I said I like to keep some things in my back pocket bedroom '
             'two master bedroom office living room so a lot of interior damage right general '
             'conditions.',
      'title': 'Xactimate Estimate Tips | Handling Insurance Adjusters (Chad Michael - The '
               'Practitioner)',
      'url': 'https://www.youtube.com/watch?v=Lh586v6HcYw&t=1477s',
      'video_id': 'Lh586v6HcYw'},
     {'author': 'American Roof Supplements',
      'channel': 'American Roof Supplements',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:40](https://www.youtube.com/watch?v=wi2YpyR1was&t=340s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Is supplements and estimates this is what we do guys we're xactimate "
              "specialists so the first one's on the house completely and totally free we have "
              'a 72-hour turnaround.',
      'timestamp': 340,
      'timestamp_label': '[00:05:40]',
      'timestamp_seconds': 340,
      'tip': "Is supplements and estimates this is what we do guys we're xactimate specialists "
             "so the first one's on the house completely and totally free we have a 72-hour "
             'turnaround.',
      'title': 'Supplement Training: Step by Step Instructions for Roofing Contractors '
               '(American Roof Supplements)',
      'url': 'https://www.youtube.com/watch?v=wi2YpyR1was&t=340s',
      'video_id': 'wi2YpyR1was'},
     {'author': "Shane O'Dazier | RestorationProfits",
      'channel': "Shane O'Dazier | RestorationProfits",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:36](https://www.youtube.com/watch?v=Rcmd8gVFzB8&t=816s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'That helpful if you have any questions on it drop a comment below do let me '
              "know and tag me share this video on social media tag me in it and we'll catch "
              'you guys in the next one.',
      'timestamp': 816,
      'timestamp_label': '[00:13:36]',
      'timestamp_seconds': 816,
      'tip': 'That helpful if you have any questions on it drop a comment below do let me know '
             "and tag me share this video on social media tag me in it and we'll catch you "
             'guys in the next one.',
      'title': "How to get leads for water damage restoration (Shane O'Dazier | "
               'RestorationProfits)',
      'url': 'https://www.youtube.com/watch?v=Rcmd8gVFzB8&t=816s',
      'video_id': 'Rcmd8gVFzB8'}],
 7: [{'author': 'Restoration Success Strategies | Albi',
      'channel': 'Restoration Success Strategies | Albi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:05](https://www.youtube.com/watch?v=3PlUwHvZkxE&t=785s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And those TPAs like Contractor Connection and Alacrity, I think it's called "
              'Altimeter now, like strongly favor the top-end contractors and they have these '
              'assignment algorithms that assign work to them specifically.',
      'timestamp': 785,
      'timestamp_label': '[00:13:05]',
      'timestamp_seconds': 785,
      'tip': "And those TPAs like Contractor Connection and Alacrity, I think it's called "
             'Altimeter now, like strongly favor the top-end contractors and they have these '
             'assignment algorithms that assign work to them specifically.',
      'title': 'How to Start a Water Damage Restoration Company in 2026 (Restoration Success '
               'Strategies | Albi)',
      'url': 'https://www.youtube.com/watch?v=3PlUwHvZkxE&t=785s',
      'video_id': '3PlUwHvZkxE'},
     {'author': 'Tyro Health',
      'channel': 'Tyro Health',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:39](https://www.youtube.com/watch?v=CbZ5Nrxx8Xw&t=219s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "If they select no, the claim doesn't proceed because assignment is required for "
              'bulk billing. So, the key benefit here is that assignment of benefit is '
              'captured seamlessly as part of the claiming process without needing a separate '
              'steps.',
      'timestamp': 219,
      'timestamp_label': '[00:03:39]',
      'timestamp_seconds': 219,
      'tip': "If they select no, the claim doesn't proceed because assignment is required for "
             'bulk billing. So, the key benefit here is that assignment of benefit is captured '
             'seamlessly as part of the claiming process without needing a separate steps.',
      'title': 'Webinar: Assignment of Benefit (AoB) Changes - What You Need to Know (Tyro '
               'Health)',
      'url': 'https://www.youtube.com/watch?v=CbZ5Nrxx8Xw&t=219s',
      'video_id': 'CbZ5Nrxx8Xw'},
     {'author': 'Regulatory Joe',
      'channel': 'Regulatory Joe',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:57](https://www.youtube.com/watch?v=kR0zavFV0HU&t=597s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So far too often, payers are delegating to TPAs at the 11th hour where they '
              'will participate and where claims will need to be processed, but have that '
              'conversation up front. And finally, step three, building a centralized '
              'implementation plan and codified business process.',
      'timestamp': 597,
      'timestamp_label': '[00:09:57]',
      'timestamp_seconds': 597,
      'tip': 'So far too often, payers are delegating to TPAs at the 11th hour where they will '
             'participate and where claims will need to be processed, but have that '
             'conversation up front. And finally, step three, building a centralized '
             'implementation plan and codified business process.',
      'title': 'TPA Licensure 101: What Every Third-Party Administrator Needs to Know '
               '(Regulatory Joe)',
      'url': 'https://www.youtube.com/watch?v=kR0zavFV0HU&t=597s',
      'video_id': 'kR0zavFV0HU'},
     {'author': 'ReconSmart Solutions LLC',
      'channel': 'ReconSmart Solutions LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:43](https://www.youtube.com/watch?v=3DF6Xf4wlIg&t=463s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And listen, this translation process only flows in one direction. Step one, the '
              'physical loss conditions dictate the field activity. Step two, that field '
              'activity generates the documentation and the quantities of materials and labor.',
      'timestamp': 463,
      'timestamp_label': '[00:07:43]',
      'timestamp_seconds': 463,
      'tip': 'And listen, this translation process only flows in one direction. Step one, the '
             'physical loss conditions dictate the field activity. Step two, that field '
             'activity generates the documentation and the quantities of materials and labor.',
      'title': 'Understanding Water Mitigation: From the Loss to the Estimate | ReconSmart '
               '(ReconSmart Solutions LLC)',
      'url': 'https://www.youtube.com/watch?v=3DF6Xf4wlIg&t=463s',
      'video_id': '3DF6Xf4wlIg'},
     {'author': 'Water Damage Restoration Marketing - Vinnie Mac',
      'channel': 'Water Damage Restoration Marketing - Vinnie Mac',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:35](https://www.youtube.com/watch?v=O0STLVhCL2c&t=635s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And you'll typically have a higher lead quality because it's actually a phone "
              "call happening. Um, similar to other ads platforms, but it's it's an a big "
              "advantage of the system. Let's talk about verification.",
      'timestamp': 635,
      'timestamp_label': '[00:10:35]',
      'timestamp_seconds': 635,
      'tip': "And you'll typically have a higher lead quality because it's actually a phone "
             "call happening. Um, similar to other ads platforms, but it's it's an a big "
             "advantage of the system. Let's talk about verification.",
      'title': 'Water Damage Google Local Services Ads - Everything You Need To Know - '
               'Restoration Marketing (Water Damage Restoration Marketing - Vinnie Mac)',
      'url': 'https://www.youtube.com/watch?v=O0STLVhCL2c&t=635s',
      'video_id': 'O0STLVhCL2c'},
     {'author': 'Public Adjuster Show with Vince Perri',
      'channel': 'Public Adjuster Show with Vince Perri',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:51](https://www.youtube.com/watch?v=RRn3mzn9xCw&t=231s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "To talk about first number one let's talk about the actual claims process and "
              "the role of the public adjuster i'm going to put up this definition right.",
      'timestamp': 231,
      'timestamp_label': '[00:03:51]',
      'timestamp_seconds': 231,
      'tip': "To talk about first number one let's talk about the actual claims process and "
             "the role of the public adjuster i'm going to put up this definition right.",
      'title': 'Roofers Vs Public Adjuster - Fight to the Death - Public Adjuster Training '
               '(Public Adjuster Show with Vince Perri)',
      'url': 'https://www.youtube.com/watch?v=RRn3mzn9xCw&t=231s',
      'video_id': 'RRn3mzn9xCw'},
     {'author': 'Chris Zimmerman',
      'channel': 'Chris Zimmerman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:09](https://www.youtube.com/watch?v=1quXRyfkTgo&t=129s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'ve completed all this work for the insurance company to release any money "
              "that's being withheld. Usually that's called depreciation. So these are all "
              "steps that are involved in the insurance restoration process that wouldn't be "
              'involved in the retail process.',
      'timestamp': 129,
      'timestamp_label': '[00:02:09]',
      'timestamp_seconds': 129,
      'tip': "'ve completed all this work for the insurance company to release any money "
             "that's being withheld. Usually that's called depreciation. So these are all "
             "steps that are involved in the insurance restoration process that wouldn't be "
             'involved in the retail process.',
      'title': "What is Insurance Restoration Roofing? (Beginner's Guide) (Chris Zimmerman)",
      'url': 'https://www.youtube.com/watch?v=1quXRyfkTgo&t=129s',
      'video_id': '1quXRyfkTgo'},
     {'author': 'Claim Daddy',
      'channel': 'Claim Daddy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[02:28:32](https://www.youtube.com/watch?v=Qu-NqEwWWPk&t=8912s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Those are our line items right there we're going to uh seal or mask the lower "
              'wall detach and reset the baseboard and paint the baseboard floor system '
              "there's no water damage so we're just going to use the standard line items.",
      'timestamp': 8912,
      'timestamp_label': '[02:28:32]',
      'timestamp_seconds': 8912,
      'tip': "Those are our line items right there we're going to uh seal or mask the lower "
             "wall detach and reset the baseboard and paint the baseboard floor system there's "
             "no water damage so we're just going to use the standard line items.",
      'title': 'Xactimate Scoping and Estimating Training | Adjuster University (Claim Daddy)',
      'url': 'https://www.youtube.com/watch?v=Qu-NqEwWWPk&t=8912s',
      'video_id': 'Qu-NqEwWWPk'},
     {'author': 'The STRONG Roofer w/ Adam Bensman',
      'channel': 'The STRONG Roofer w/ Adam Bensman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:12](https://www.youtube.com/watch?v=-aZHNsY5qIY&t=192s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The name of the guy from the insurance company they're either paid by the "
              'insurance coming themselves or a third party claims company and these guys '
              'come.',
      'timestamp': 192,
      'timestamp_label': '[00:03:12]',
      'timestamp_seconds': 192,
      'tip': "The name of the guy from the insurance company they're either paid by the "
             'insurance coming themselves or a third party claims company and these guys come.',
      'title': 'Selling Hail-Damaged Roofs: The Hail Sales Process From Start to Finish (The '
               'STRONG Roofer w/ Adam Bensman)',
      'url': 'https://www.youtube.com/watch?v=-aZHNsY5qIY&t=192s',
      'video_id': '-aZHNsY5qIY'},
     {'author': 'Chris Hamilton',
      'channel': 'Chris Hamilton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:35](https://www.youtube.com/watch?v=LEzohuG5ykg&t=95s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'That so I think the more that we can do as far as helping these employees as '
              'far as navigating the Healthcare System the better so that would be a first '
              'question.',
      'timestamp': 95,
      'timestamp_label': '[00:01:35]',
      'timestamp_seconds': 95,
      'tip': 'That so I think the more that we can do as far as helping these employees as far '
             'as navigating the Healthcare System the better so that would be a first '
             'question.',
      'title': 'What does a TPA or third party administrator do for my company benefits plan? '
               '(Chris Hamilton)',
      'url': 'https://www.youtube.com/watch?v=LEzohuG5ykg&t=95s',
      'video_id': 'LEzohuG5ykg'},
     {'author': 'American Roof Supplements',
      'channel': 'American Roof Supplements',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:21](https://www.youtube.com/watch?v=DR03Zlogfe0&t=621s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "After that, it's a flat fee. 50 for an estimate, 150 for a supplement, and less "
              "if we wrote the estimate. No percentage, no monthly fee. If you're newer to "
              "insurance work, we'll walk you through your first five claims so you learn the "
              'process.',
      'timestamp': 621,
      'timestamp_label': '[00:10:21]',
      'timestamp_seconds': 621,
      'tip': "After that, it's a flat fee. 50 for an estimate, 150 for a supplement, and less "
             "if we wrote the estimate. No percentage, no monthly fee. If you're newer to "
             "insurance work, we'll walk you through your first five claims so you learn the "
             'process.',
      'title': 'Roofer Explains Roofing Terms: 12 Roof Components That Matter in Xactimate '
               '(American Roof Supplements)',
      'url': 'https://www.youtube.com/watch?v=DR03Zlogfe0&t=621s',
      'video_id': 'DR03Zlogfe0'},
     {'author': "Shane O'Dazier | RestorationProfits",
      'channel': "Shane O'Dazier | RestorationProfits",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:38](https://www.youtube.com/watch?v=5CbcT0WZWts&t=398s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Before you get any of this material we have to get on a call with you and '
              "verify you are who you say you are and we've had to kick a few people out and.",
      'timestamp': 398,
      'timestamp_label': '[00:06:38]',
      'timestamp_seconds': 398,
      'tip': 'Before you get any of this material we have to get on a call with you and verify '
             "you are who you say you are and we've had to kick a few people out and.",
      'title': 'How a restoration contractor should write an estimate for water mitigation '
               "(Shane O'Dazier | RestorationProfits)",
      'url': 'https://www.youtube.com/watch?v=5CbcT0WZWts&t=398s',
      'video_id': '5CbcT0WZWts'},
     {'author': 'Adjuster TV',
      'channel': 'Adjuster TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:58:34](https://www.youtube.com/watch?v=6084H_VeZTA&t=3514s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The storm chaser and the uh for the adjuster who let me let's be honest what "
              "kind of storm chasers if we're doing catwork right.",
      'timestamp': 3514,
      'timestamp_label': '[00:58:34]',
      'timestamp_seconds': 3514,
      'tip': "The storm chaser and the uh for the adjuster who let me let's be honest what "
             "kind of storm chasers if we're doing catwork right.",
      'title': 'HAIL CLAIM WALKTHROUGH | Xactimate X1 roof claim (Adjuster TV)',
      'url': 'https://www.youtube.com/watch?v=6084H_VeZTA&t=3514s',
      'video_id': '6084H_VeZTA'},
     {'author': 'APPALeadership',
      'channel': 'APPALeadership',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:42:04](https://www.youtube.com/watch?v=cPAFOZbMKQE&t=2524s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "It's the same for 3 & 4 for different reasons class 3 a lot of evaporation "
              'taking place class poor not a lot of evaporation taking place so I need to '
              "lower what's called my vapor pressure differential to pull those materials the "
              'moisture out of those materials.',
      'timestamp': 2524,
      'timestamp_label': '[00:42:04]',
      'timestamp_seconds': 2524,
      'tip': "It's the same for 3 & 4 for different reasons class 3 a lot of evaporation "
             'taking place class poor not a lot of evaporation taking place so I need to lower '
             "what's called my vapor pressure differential to pull those materials the "
             'moisture out of those materials.',
      'title': '2019 08 29 12 51 IICRC S500 Standard   Water Damage Principles   Recovery '
               '(APPALeadership)',
      'url': 'https://www.youtube.com/watch?v=cPAFOZbMKQE&t=2524s',
      'video_id': 'cPAFOZbMKQE'},
     {'author': "Shane O'Dazier | RestorationProfits",
      'channel': "Shane O'Dazier | RestorationProfits",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:05](https://www.youtube.com/watch?v=b1-Dcqk4F9g&t=425s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "It's a steal so let's take a look at the work authorization so you got to make "
              'a copy of it and this is what it does here so the the three day um equipment '
              "rule so let's go to where I put this guy in right here.",
      'timestamp': 425,
      'timestamp_label': '[00:07:05]',
      'timestamp_seconds': 425,
      'tip': "It's a steal so let's take a look at the work authorization so you got to make a "
             'copy of it and this is what it does here so the the three day um equipment rule '
             "so let's go to where I put this guy in right here.",
      'title': "Contractor Contracts vs Restoration Contracts (Shane O'Dazier | "
               'RestorationProfits)',
      'url': 'https://www.youtube.com/watch?v=b1-Dcqk4F9g&t=425s',
      'video_id': 'b1-Dcqk4F9g'}],
 8: [{'author': 'PushLeads',
      'channel': 'PushLeads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=wnVxHv3JM28&t=55s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Here is the core distinction. A restoration company handles emergency '
              'mitigation, stopping active damage, drying the structure, and removing '
              'contaminants. A general contractor handles reconstruction, putting the property '
              'back together after the environment is stabilized.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'Here is the core distinction. A restoration company handles emergency '
             'mitigation, stopping active damage, drying the structure, and removing '
             'contaminants. A general contractor handles reconstruction, putting the property '
             'back together after the environment is stabilized.',
      'title': "Restoration Company vs General Contractor: What's the Difference? (PushLeads)",
      'url': 'https://www.youtube.com/watch?v=wnVxHv3JM28&t=55s',
      'video_id': 'wnVxHv3JM28'},
     {'author': 'magicplan',
      'channel': 'magicplan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:39](https://www.youtube.com/watch?v=F4WLuIxWd-Q&t=339s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Of using that tool of the assignment of benefits as efficient and as kind of '
              "like smooth as possible yeah yeah um that's a it's a tough question to answer.",
      'timestamp': 339,
      'timestamp_label': '[00:05:39]',
      'timestamp_seconds': 339,
      'tip': 'Of using that tool of the assignment of benefits as efficient and as kind of '
             "like smooth as possible yeah yeah um that's a it's a tough question to answer.",
      'title': 'When Does Assignment of Benefits (AOB) Work Best? Tips for Restorers (w/Josh '
               'Ehmke) (magicplan)',
      'url': 'https://www.youtube.com/watch?v=F4WLuIxWd-Q&t=339s',
      'video_id': 'F4WLuIxWd-Q'},
     {'author': 'American Roof Supplements',
      'channel': 'American Roof Supplements',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:09](https://www.youtube.com/watch?v=zDKvQs0viSI&t=129s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Not every claim needs a public adjuster, but complicated disputes may. Now the '
              'crew is on the roof and opinions have to give way to evidence. A dark spot '
              "isn't automatically hail damage.",
      'timestamp': 129,
      'timestamp_label': '[00:02:09]',
      'timestamp_seconds': 129,
      'tip': 'Not every claim needs a public adjuster, but complicated disputes may. Now the '
             "crew is on the roof and opinions have to give way to evidence. A dark spot isn't "
             'automatically hail damage.',
      'title': '7 Levels of Public Adjusters: Simple Claims to Total Chaos (American Roof '
               'Supplements)',
      'url': 'https://www.youtube.com/watch?v=zDKvQs0viSI&t=129s',
      'video_id': 'zDKvQs0viSI'},
     {'author': 'Self Insured Reporting',
      'channel': 'Self Insured Reporting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=7lU917xnSRE&t=157s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "But it's we have all the api's built in our platform already show you a couple "
              'of other things when the claims and enrollment come in into the system we.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': "But it's we have all the api's built in our platform already show you a couple "
             'of other things when the claims and enrollment come in into the system we.',
      'title': 'Third Party Administrators (Self Insured Reporting)',
      'url': 'https://www.youtube.com/watch?v=7lU917xnSRE&t=157s',
      'video_id': '7lU917xnSRE'},
     {'author': 'Adjuster TV',
      'channel': 'Adjuster TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:21](https://www.youtube.com/watch?v=86mEe0yHwiw&t=1881s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Property or auto claims ia including many more videos free tutorials and '
              'webinars with best gear and software for claims and industry news and I a '
              'weather reports head on over to adjuster tv.com and as always thank you so much '
              'for watching and have a great storm.',
      'timestamp': 1881,
      'timestamp_label': '[00:31:21]',
      'timestamp_seconds': 1881,
      'tip': 'Property or auto claims ia including many more videos free tutorials and '
             'webinars with best gear and software for claims and industry news and I a '
             'weather reports head on over to adjuster tv.com and as always thank you so much '
             'for watching and have a great storm.',
      'title': 'Matterport Demo and Walkthrough (Adjuster TV)',
      'url': 'https://www.youtube.com/watch?v=86mEe0yHwiw&t=1881s',
      'video_id': '86mEe0yHwiw'},
     {'author': 'On-Site Adjusting',
      'channel': 'On-Site Adjusting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:06](https://www.youtube.com/watch?v=oEc6cQdcK6I&t=66s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You know, you you're about to jump in with a uh restoration company who's going "
              "to bring in uh uh mitigation equipment. They're going to dry everything up and "
              "then your adjuster is going to show up and he's gonna, you know, it's just "
              'gonna be all dry.',
      'timestamp': 66,
      'timestamp_label': '[00:01:06]',
      'timestamp_seconds': 66,
      'tip': "You know, you you're about to jump in with a uh restoration company who's going "
             "to bring in uh uh mitigation equipment. They're going to dry everything up and "
             "then your adjuster is going to show up and he's gonna, you know, it's just gonna "
             'be all dry.',
      'title': 'Don’t Let the Insurance Company’s Contractor Ruin Your Claim 😳 | Public '
               'Adjuster Explains (On-Site Adjusting)',
      'url': 'https://www.youtube.com/watch?v=oEc6cQdcK6I&t=66s',
      'video_id': 'oEc6cQdcK6I'},
     {'author': 'Water Damage Restoration Coach - Jon Schoen',
      'channel': 'Water Damage Restoration Coach - Jon Schoen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:09](https://www.youtube.com/watch?v=-0hAYhkhJaw&t=429s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Software um but you know the mic documentation is a lot and um you know so '
              "you're going to end up having to put somebody on that.",
      'timestamp': 429,
      'timestamp_label': '[00:07:09]',
      'timestamp_seconds': 429,
      'tip': 'Software um but you know the mic documentation is a lot and um you know so '
             "you're going to end up having to put somebody on that.",
      'title': "How to Get on Insurance Restoration Third Party Administrator's TPA's Lists "
               '(Water Damage Restoration Coach - Jon Schoen)',
      'url': 'https://www.youtube.com/watch?v=-0hAYhkhJaw&t=429s',
      'video_id': '-0hAYhkhJaw'},
     {'author': 'Actionable',
      'channel': 'Actionable',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:20](https://www.youtube.com/watch?v=s4xCprLX1Yw&t=920s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Added text to the note field of replaced definition to clarify contractor will '
              'generally have and use standard ladder jacks and plank scaffolding as part of '
              'their normal equipment tool set.',
      'timestamp': 920,
      'timestamp_label': '[00:15:20]',
      'timestamp_seconds': 920,
      'tip': 'Added text to the note field of replaced definition to clarify contractor will '
             'generally have and use standard ladder jacks and plank scaffolding as part of '
             'their normal equipment tool set.',
      'title': '🚨 23 NEW XACTIMATE LINE ITEMS! (Actionable)',
      'url': 'https://www.youtube.com/watch?v=s4xCprLX1Yw&t=920s',
      'video_id': 's4xCprLX1Yw'},
     {'author': 'TheIICRC',
      'channel': 'TheIICRC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:46](https://www.youtube.com/watch?v=bcid0F9jRTI&t=1186s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Conditions and historical data and other published sources are available and '
              "how it's all put together so we may use one or many or all of these but they're "
              'all uh opportunities for us to establish our drying goal without just saying '
              'what is a dry standard.',
      'timestamp': 1186,
      'timestamp_label': '[00:19:46]',
      'timestamp_seconds': 1186,
      'tip': 'Conditions and historical data and other published sources are available and how '
             "it's all put together so we may use one or many or all of these but they're all "
             'uh opportunities for us to establish our drying goal without just saying what is '
             'a dry standard.',
      'title': 'ANSI/IICRC S500: 2021 Edition (TheIICRC)',
      'url': 'https://www.youtube.com/watch?v=bcid0F9jRTI&t=1186s',
      'video_id': 'bcid0F9jRTI'},
     {'author': "Shane O'Dazier | RestorationProfits",
      'channel': "Shane O'Dazier | RestorationProfits",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:43](https://www.youtube.com/watch?v=MLuoMdYemWU&t=643s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I mean, talk about not dancing with the one that brought you. Guys, if you '
              "didn't already know, the two biggest problems you're going to have in owning a "
              'restoration company are this. Number one, getting consistent water damage jobs '
              'coming in the door.',
      'timestamp': 643,
      'timestamp_label': '[00:10:43]',
      'timestamp_seconds': 643,
      'tip': 'I mean, talk about not dancing with the one that brought you. Guys, if you '
             "didn't already know, the two biggest problems you're going to have in owning a "
             'restoration company are this. Number one, getting consistent water damage jobs '
             'coming in the door.',
      'title': 'Creative Ways To Get Consistent Water Restoration Business Leads (Shane '
               "O'Dazier | RestorationProfits)",
      'url': 'https://www.youtube.com/watch?v=MLuoMdYemWU&t=643s',
      'video_id': 'MLuoMdYemWU'},
     {'author': "Builder's Perspective Public Adjusting",
      'channel': "Builder's Perspective Public Adjusting",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:58](https://www.youtube.com/watch?v=kWxJ6PIkM-M&t=838s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You some advice so feel free to give us a call 888-830 bppa 888-830-2772 send '
              'us a message on Facebook and we will be happy to get back with you thanks.',
      'timestamp': 838,
      'timestamp_label': '[00:13:58]',
      'timestamp_seconds': 838,
      'tip': 'You some advice so feel free to give us a call 888-830 bppa 888-830-2772 send us '
             'a message on Facebook and we will be happy to get back with you thanks.',
      'title': "Reading Xactimate Estimate (Builder's Perspective Public Adjusting)",
      'url': 'https://www.youtube.com/watch?v=kWxJ6PIkM-M&t=838s',
      'video_id': 'kWxJ6PIkM-M'},
     {'author': 'Water Damage Restoration Marketing - Vinnie Mac',
      'channel': 'Water Damage Restoration Marketing - Vinnie Mac',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:23](https://www.youtube.com/watch?v=KYZjCfsaWhs&t=203s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'We also made a connection to Sunbelt and they we were providing power for us as '
              'well for our equipment and then I also made connections to our other office in.',
      'timestamp': 203,
      'timestamp_label': '[00:03:23]',
      'timestamp_seconds': 203,
      'tip': 'We also made a connection to Sunbelt and they we were providing power for us as '
             'well for our equipment and then I also made connections to our other office in.',
      'title': 'Water Damage Marketing | How To Generate Water Damage Leads (Water Damage '
               'Restoration Marketing - Vinnie Mac)',
      'url': 'https://www.youtube.com/watch?v=KYZjCfsaWhs&t=203s',
      'video_id': 'KYZjCfsaWhs'},
     {'author': 'Estimate Mastery',
      'channel': 'Estimate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=fdW0W_-MR-s&t=15s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "What I'm going to share here in this video there's a way to do what I like to "
              "call oneclick estimating and I'm going to show you how this works in Xactimate.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "What I'm going to share here in this video there's a way to do what I like to "
             "call oneclick estimating and I'm going to show you how this works in Xactimate.",
      'title': '1 Click Secret - Write a roof & siding estimate in 15 minutes using this one '
               'tool in Xactimate (Estimate Mastery)',
      'url': 'https://www.youtube.com/watch?v=fdW0W_-MR-s&t=15s',
      'video_id': 'fdW0W_-MR-s'},
     {'author': "Shane O'Dazier | RestorationProfits",
      'channel': "Shane O'Dazier | RestorationProfits",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:38](https://www.youtube.com/watch?v=CV0x51fC7pw&t=338s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re a fit like you've probably got enough data at that point. Does that make "
              'sense >> to call it? Like how long do you need to look at the flatline before '
              'you call in dead?',
      'timestamp': 338,
      'timestamp_label': '[00:05:38]',
      'timestamp_seconds': 338,
      'tip': "'re a fit like you've probably got enough data at that point. Does that make "
             'sense >> to call it? Like how long do you need to look at the flatline before '
             'you call in dead?',
      'title': "How to Get Plumbers Sending You $60K Water Jobs (Shane O'Dazier | "
               'RestorationProfits)',
      'url': 'https://www.youtube.com/watch?v=CV0x51fC7pw&t=338s',
      'video_id': 'CV0x51fC7pw'},
     {'author': 'Happy Adjuster',
      'channel': 'Happy Adjuster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:48](https://www.youtube.com/watch?v=hqbiodyd1gc&t=48s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Once you've signed an AOB, you could be cut out of the conversation entirely. "
              'And in some cases, you may end up in the middle of a legal dispute between the '
              "contractor and your insurance company. An AOB means you won't have to deal "
              'directly with the insurance company.',
      'timestamp': 48,
      'timestamp_label': '[00:00:48]',
      'timestamp_seconds': 48,
      'tip': "Once you've signed an AOB, you could be cut out of the conversation entirely. "
             'And in some cases, you may end up in the middle of a legal dispute between the '
             "contractor and your insurance company. An AOB means you won't have to deal "
             'directly with the insurance company.',
      'title': 'What Is an Assignment of Benefits (AOB)? | Should You Sign One After a '
               'Property Damage Claim? (Happy Adjuster)',
      'url': 'https://www.youtube.com/watch?v=hqbiodyd1gc&t=48s',
      'video_id': 'hqbiodyd1gc'}],
 9: [{'author': 'American Roof Supplements',
      'channel': 'American Roof Supplements',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:04](https://www.youtube.com/watch?v=GK_Was-iK98&t=484s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'There is also a legal and compliance side to this. Public adjuster rules vary '
              'by state. Some states have specific requirements around contracts, fees, '
              'disclosures, third-party services, record keeping, or who can perform certain '
              'claim-related activities.',
      'timestamp': 484,
      'timestamp_label': '[00:08:04]',
      'timestamp_seconds': 484,
      'tip': 'There is also a legal and compliance side to this. Public adjuster rules vary by '
             'state. Some states have specific requirements around contracts, fees, '
             'disclosures, third-party services, record keeping, or who can perform certain '
             'claim-related activities.',
      'title': 'Public Adjusters: Stop Wasting Hours Building Xactimate Estimates (American '
               'Roof Supplements)',
      'url': 'https://www.youtube.com/watch?v=GK_Was-iK98&t=484s',
      'video_id': 'GK_Was-iK98'},
     {'author': 'flanewscapitol',
      'channel': 'flanewscapitol',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=7-KaOK5zk7g&t=90s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Recover full costs and ensures consumers repairs are up to standard Florida's "
              'ranked the state with the fifth worst legal climate in the country insurers say '
              'assignment of benefits fraud is a major factor in the ranking in Tallahassee '
              "I'm Jake stofan.",
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': "Recover full costs and ensures consumers repairs are up to standard Florida's "
             'ranked the state with the fifth worst legal climate in the country insurers say '
             "assignment of benefits fraud is a major factor in the ranking in Tallahassee I'm "
             'Jake stofan.',
      'title': 'Insurers Call for Assignment of Benefits Reform (flanewscapitol)',
      'url': 'https://www.youtube.com/watch?v=7-KaOK5zk7g&t=90s',
      'video_id': '7-KaOK5zk7g'},
     {'author': 'Building Experts Institute',
      'channel': 'Building Experts Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=RmjqTZJ3II0&t=45s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re going to perform this, which is a dollar amount, not just a hand over the "
              'benefits of a policy. And if you live in a state where there is no assignment '
              'of benefits, a contingency contract in many ways is an assignment of benefits '
              'form.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': "'re going to perform this, which is a dollar amount, not just a hand over the "
             'benefits of a policy. And if you live in a state where there is no assignment of '
             'benefits, a contingency contract in many ways is an assignment of benefits form.',
      'title': 'Contingency contracts may violate UPPA (Building Experts Institute)',
      'url': 'https://www.youtube.com/watch?v=RmjqTZJ3II0&t=45s',
      'video_id': 'RmjqTZJ3II0'},
     {'author': 'Accountancy Students Hub',
      'channel': 'Accountancy Students Hub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:58](https://www.youtube.com/watch?v=-mzjb7XSisY&t=298s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "They have to pay interest at twice the legal rate, plus attorney's fees and "
              'damages. The law literally does not mess around when it comes to delayed '
              'payouts. Next up is section four, the rules of prescription.',
      'timestamp': 298,
      'timestamp_label': '[00:04:58]',
      'timestamp_seconds': 298,
      'tip': "They have to pay interest at twice the legal rate, plus attorney's fees and "
             'damages. The law literally does not mess around when it comes to delayed '
             'payouts. Next up is section four, the rules of prescription.',
      'title': 'RFBT Insurance 05: Special Classes of Insurance, Claims Settlement, '
               'Prescription, and Subrogation (Accountancy Students Hub)',
      'url': 'https://www.youtube.com/watch?v=-mzjb7XSisY&t=298s',
      'video_id': '-mzjb7XSisY'},
     {'author': 'The Deductible',
      'channel': 'The Deductible',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:21](https://www.youtube.com/watch?v=A4K6Yt2bnWk&t=561s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'One last thing, and I mean this, this video is education, not advice. Rates, '
              'surcharge rules, and deductibles vary by state, by company, and by policy. Read '
              'your own policy or talk to a licensed agent in your state before you change '
              'anything.',
      'timestamp': 561,
      'timestamp_label': '[00:09:21]',
      'timestamp_seconds': 561,
      'tip': 'One last thing, and I mean this, this video is education, not advice. Rates, '
             'surcharge rules, and deductibles vary by state, by company, and by policy. Read '
             'your own policy or talk to a licensed agent in your state before you change '
             'anything.',
      'title': 'Deductibles Explained: The Math That Decides If a Claim Is Worth Filing (The '
               'Deductible)',
      'url': 'https://www.youtube.com/watch?v=A4K6Yt2bnWk&t=561s',
      'video_id': 'A4K6Yt2bnWk'},
     {'author': 'Relentless Health Value',
      'channel': 'Relentless Health Value',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:34:59](https://www.youtube.com/watch?v=pNIYu-t990E&t=2099s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So trying to rely on their internal processes to make sure that your contract '
              'is adequately adjudicated as per the terms of the contract, you can see how '
              "that might be an issue. Even with the best of intention. So they're committed "
              "to it, but you're right.",
      'timestamp': 2099,
      'timestamp_label': '[00:34:59]',
      'timestamp_seconds': 2099,
      'tip': 'So trying to rely on their internal processes to make sure that your contract is '
             'adequately adjudicated as per the terms of the contract, you can see how that '
             "might be an issue. Even with the best of intention. So they're committed to it, "
             "but you're right.",
      'title': 'Running a TPA (Third Party Administrator) RFP Process That Is Less of a Wild '
               'West Fiduciary Shootout (Relentless Health Value)',
      'url': 'https://www.youtube.com/watch?v=pNIYu-t990E&t=2099s',
      'video_id': 'pNIYu-t990E'},
     {'author': "Time's Dark Captains",
      'channel': "Time's Dark Captains",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:24](https://www.youtube.com/watch?v=y00Yi4bnLx4&t=1284s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Doing an assessment on looking at whether it's in normal fungal ecology now "
              'this is where the state of texas rules come in go like yeah.',
      'timestamp': 1284,
      'timestamp_label': '[00:21:24]',
      'timestamp_seconds': 1284,
      'tip': "Doing an assessment on looking at whether it's in normal fungal ecology now this "
             'is where the state of texas rules come in go like yeah.',
      'title': "Texas Mold Remediation:  IICRC S520/R520, IICRC S500 and the TMARR (Time's "
               'Dark Captains)',
      'url': 'https://www.youtube.com/watch?v=y00Yi4bnLx4&t=1284s',
      'video_id': 'y00Yi4bnLx4'},
     {'author': 'RestoreMasters',
      'channel': 'RestoreMasters',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:34](https://www.youtube.com/watch?v=rw8dEal_Ppk&t=34s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Us to see the direction of the storm but not necessarily do you see the damage '
              "on top of the TV oh so we felt around different spots where there's.",
      'timestamp': 34,
      'timestamp_label': '[00:00:34]',
      'timestamp_seconds': 34,
      'tip': 'Us to see the direction of the storm but not necessarily do you see the damage '
             "on top of the TV oh so we felt around different spots where there's.",
      'title': 'RestoreMasters TPO Roof Inspections (Property Damage Assessments) | Hail '
               'Damage (RestoreMasters)',
      'url': 'https://www.youtube.com/watch?v=rw8dEal_Ppk&t=34s',
      'video_id': 'rw8dEal_Ppk'},
     {'author': 'Marketing Ninjas',
      'channel': 'Marketing Ninjas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=n7ECptsaJTQ&t=35s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ask questions like, are you already working with a mitigation company, or '
              "multiple mitigation companies? What's gone well with them? How do you usually "
              'decide who to send a job to? What do you need most from a restoration partner? '
              'These kinds of questions flip the script.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'Ask questions like, are you already working with a mitigation company, or '
             "multiple mitigation companies? What's gone well with them? How do you usually "
             'decide who to send a job to? What do you need most from a restoration partner? '
             'These kinds of questions flip the script.',
      'title': 'How to Get Plumbers to Actually Send You Mitigation Jobs (Marketing Ninjas)',
      'url': 'https://www.youtube.com/watch?v=n7ECptsaJTQ&t=35s',
      'video_id': 'n7ECptsaJTQ'},
     {'author': 'Claims Adjuster of the Year',
      'channel': 'Claims Adjuster of the Year',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=EDF71IxtN5w&t=117s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Were working and you put in the policy dates again we've got to make sure it's "
              'active and then you put in the deductible okay see please explain how the '
              'deductible works in regards to uh so the so the deductible is not actually '
              'something.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': "Were working and you put in the policy dates again we've got to make sure it's "
             'active and then you put in the deductible okay see please explain how the '
             'deductible works in regards to uh so the so the deductible is not actually '
             'something.',
      'title': 'How to Use Xactimate for Training as an Adjuster | Training for beginners 🔥 '
               'Claims Adjuster (Claims Adjuster of the Year)',
      'url': 'https://www.youtube.com/watch?v=EDF71IxtN5w&t=117s',
      'video_id': 'EDF71IxtN5w'},
     {'author': 'Omegasonics',
      'channel': 'Omegasonics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:46](https://www.youtube.com/watch?v=3UmvqUcOFDc&t=106s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Exact item your insured is looking for without having to scroll through '
              'hundreds of photos for more information on proper packout procedures give us a '
              'call or visit our website at omegas sonics.com you can also connect with us on '
              'Facebook and Twitter.',
      'timestamp': 106,
      'timestamp_label': '[00:01:46]',
      'timestamp_seconds': 106,
      'tip': 'Exact item your insured is looking for without having to scroll through hundreds '
             'of photos for more information on proper packout procedures give us a call or '
             'visit our website at omegas sonics.com you can also connect with us on Facebook '
             'and Twitter.',
      'title': 'Tips for Proper Restoration Packout (Omegasonics)',
      'url': 'https://www.youtube.com/watch?v=3UmvqUcOFDc&t=106s',
      'video_id': '3UmvqUcOFDc'},
     {'author': 'Claim Toolkit',
      'channel': 'Claim Toolkit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:34](https://www.youtube.com/watch?v=LQ4DKKitI6o&t=1294s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Outdated information so we're going to scroll down you'll see we can "
              'essentially do a comparison between states for the applicable law I am '
              'researching.',
      'timestamp': 1294,
      'timestamp_label': '[00:21:34]',
      'timestamp_seconds': 1294,
      'tip': "Outdated information so we're going to scroll down you'll see we can essentially "
             'do a comparison between states for the applicable law I am researching.',
      'title': 'Claim Toolkit Training - 06/17/2021 (Sedgwick) (Claim Toolkit)',
      'url': 'https://www.youtube.com/watch?v=LQ4DKKitI6o&t=1294s',
      'video_id': 'LQ4DKKitI6o'},
     {'author': 'TheIICRC',
      'channel': 'TheIICRC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:29](https://www.youtube.com/watch?v=6CI2NAsooLw&t=629s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Compliant with the global harmonization system so we've included International "
              "measurements and other information we've enhanced the rules for negative "
              'pressure containments used in sensitive environments such as Retirement Homes '
              'hospitals day care centers Etc.',
      'timestamp': 629,
      'timestamp_label': '[00:10:29]',
      'timestamp_seconds': 629,
      'tip': "Compliant with the global harmonization system so we've included International "
             "measurements and other information we've enhanced the rules for negative "
             'pressure containments used in sensitive environments such as Retirement Homes '
             'hospitals day care centers Etc.',
      'title': 'Newly-Revised ANSI/IICRC S520: 2015 - What You Need to Know (TheIICRC)',
      'url': 'https://www.youtube.com/watch?v=6CI2NAsooLw&t=629s',
      'video_id': '6CI2NAsooLw'},
     {'author': 'Navigating the Business of Medicine',
      'channel': 'Navigating the Business of Medicine',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:46](https://www.youtube.com/watch?v=z0-3oV0C8EU&t=406s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Something wrong no I'm kidding but don't feel bad if you're confused often or "
              'you get frustrated it is common across the board for most of us take care of '
              "yourselves and we'll talk to you soon bye-bye.",
      'timestamp': 406,
      'timestamp_label': '[00:06:46]',
      'timestamp_seconds': 406,
      'tip': "Something wrong no I'm kidding but don't feel bad if you're confused often or "
             'you get frustrated it is common across the board for most of us take care of '
             "yourselves and we'll talk to you soon bye-bye.",
      'title': 'Understanding Third-Party Administrators (TPAs) in Healthcare Insurance '
               '(Navigating the Business of Medicine)',
      'url': 'https://www.youtube.com/watch?v=z0-3oV0C8EU&t=406s',
      'video_id': 'z0-3oV0C8EU'},
     {'author': 'Butler Legal',
      'channel': 'Butler Legal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:59](https://www.youtube.com/watch?v=rxahzd6qaCw&t=179s)',
      'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                   'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                   'supplements, and UPPA-safe collections (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Florida law is clear that that assignment anti-assignment provision does not '
              'apply to post-loss assignment of insurance benefits.',
      'timestamp': 179,
      'timestamp_label': '[00:02:59]',
      'timestamp_seconds': 179,
      'tip': 'Florida law is clear that that assignment anti-assignment provision does not '
             'apply to post-loss assignment of insurance benefits.',
      'title': 'Handling of Assignment of Benefit ("AOB") Claims (Butler Legal)',
      'url': 'https://www.youtube.com/watch?v=rxahzd6qaCw&t=179s',
      'video_id': 'rxahzd6qaCw'}],
 10: [{'author': 'One Claim Solution',
       'channel': 'One Claim Solution',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:08](https://www.youtube.com/watch?v=wq1z-Qyyws8&t=68s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "There's a reason that hospitals and doctors’ offices use this, in their "
               'everyday billing practices. You know, how often have you ever seen a bill come '
               "to you from your health insurance company? You know, I've never gotten the "
               'check from the health insurance company.',
       'timestamp': 68,
       'timestamp_label': '[00:01:08]',
       'timestamp_seconds': 68,
       'tip': "There's a reason that hospitals and doctors’ offices use this, in their "
              'everyday billing practices. You know, how often have you ever seen a bill come '
              "to you from your health insurance company? You know, I've never gotten the "
              'check from the health insurance company.',
       'title': 'OCS: Assignment Of Benefits (One Claim Solution)',
       'url': 'https://www.youtube.com/watch?v=wq1z-Qyyws8&t=68s',
       'video_id': 'wq1z-Qyyws8'},
      {'author': 'CandiMentor',
       'channel': 'CandiMentor',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:37:07](https://www.youtube.com/watch?v=AVAVGkoZuK0&t=2227s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'They can also create opportunities for intentional abuse. Common indicators '
               'include stage damage, inflated contents lists, duplicate claims, and altered '
               'photographs or documents. These are warning signs, not conclusions.',
       'timestamp': 2227,
       'timestamp_label': '[00:37:07]',
       'timestamp_seconds': 2227,
       'tip': 'They can also create opportunities for intentional abuse. Common indicators '
              'include stage damage, inflated contents lists, duplicate claims, and altered '
              'photographs or documents. These are warning signs, not conclusions.',
       'title': 'Adjuster Exam: Salvage, Subrogation, Fraud, Ethics, Fair Claims Practices & '
                'Catastrophe Claims (CandiMentor)',
       'url': 'https://www.youtube.com/watch?v=AVAVGkoZuK0&t=2227s',
       'video_id': 'AVAVGkoZuK0'},
      {'author': 'Chris Zimmerman',
       'channel': 'Chris Zimmerman',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:12](https://www.youtube.com/watch?v=esg8I0BJFLM&t=72s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'An independent adjuster is a licensed adjuster who is hired by the insurance '
               'company as a third party. So they work for an independent adjuster firm and '
               'they might do claims for several different insurance companies.',
       'timestamp': 72,
       'timestamp_label': '[00:01:12]',
       'timestamp_seconds': 72,
       'tip': 'An independent adjuster is a licensed adjuster who is hired by the insurance '
              'company as a third party. So they work for an independent adjuster firm and '
              'they might do claims for several different insurance companies.',
       'title': 'What All Roofing Contractors Need to Know About Adjusters (Chris Zimmerman)',
       'url': 'https://www.youtube.com/watch?v=esg8I0BJFLM&t=72s',
       'video_id': 'esg8I0BJFLM'},
      {'author': 'Collision Crash Course',
       'channel': 'Collision Crash Course',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:41](https://www.youtube.com/watch?v=jcrOa0gm--g&t=101s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'I was hit by an underinsured motorist, so I did use my policy for the repair. '
               'I did have to pay my deductible to MGA, and I did get my deductible back. So '
               "every claim is different, every insurance company's speed is different, but "
               "that's just my experience.",
       'timestamp': 101,
       'timestamp_label': '[00:01:41]',
       'timestamp_seconds': 101,
       'tip': 'I was hit by an underinsured motorist, so I did use my policy for the repair. I '
              'did have to pay my deductible to MGA, and I did get my deductible back. So '
              "every claim is different, every insurance company's speed is different, but "
              "that's just my experience.",
       'title': "Do You Have to Pay Your Deductible If the Accident Wasn't Your Fault? "
                '(Collision Crash Course)',
       'url': 'https://www.youtube.com/watch?v=jcrOa0gm--g&t=101s',
       'video_id': 'jcrOa0gm--g'},
      {'author': 'FirehouseEducation',
       'channel': 'FirehouseEducation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:42](https://www.youtube.com/watch?v=MkCNqNRsk04&t=522s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Hepa vacuuming it, and then doing a steam cleaning on that mattress. And then '
               'I end it with a um running it through my hydroxal drying chamber. So, your '
               'fifth question, Sam, was cleaning of clothing and bedding.',
       'timestamp': 522,
       'timestamp_label': '[00:08:42]',
       'timestamp_seconds': 522,
       'tip': 'Hepa vacuuming it, and then doing a steam cleaning on that mattress. And then I '
              'end it with a um running it through my hydroxal drying chamber. So, your fifth '
              'question, Sam, was cleaning of clothing and bedding.',
       'title': 'How to Clean Smoke-Damaged Contents After a Wildfire | Ask Annissa '
                '(FirehouseEducation)',
       'url': 'https://www.youtube.com/watch?v=MkCNqNRsk04&t=522s',
       'video_id': 'MkCNqNRsk04'},
      {'author': 'Magentus | Practice Management',
       'channel': 'Magentus | Practice Management',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=kY8cf-6-nlQ&t=15s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Medicare's assignment of benefit requirements. These changes apply to both "
               'bulk billing and inpatient simplified billing.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': "Medicare's assignment of benefit requirements. These changes apply to both bulk "
              'billing and inpatient simplified billing.',
       'title': 'Medicare Assignment of Benefit (AoB) in Gentu (Magentus | Practice '
                'Management)',
       'url': 'https://www.youtube.com/watch?v=kY8cf-6-nlQ&t=15s',
       'video_id': 'kY8cf-6-nlQ'},
      {'author': 'Daughtry Construction Group',
       'channel': 'Daughtry Construction Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:45](https://www.youtube.com/watch?v=HLwvN9mF1R0&t=345s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Go over anything that we miss cleaning and this is charged by the square foot '
               'again commercial right now is about 29 cents a square foot in residential '
               "right now it's about 37 cents a square foot.",
       'timestamp': 345,
       'timestamp_label': '[00:05:45]',
       'timestamp_seconds': 345,
       'tip': 'Go over anything that we miss cleaning and this is charged by the square foot '
              'again commercial right now is about 29 cents a square foot in residential right '
              "now it's about 37 cents a square foot.",
       'title': 'Xactimate Line Item Cheat Sheet (Daughtry Construction Group)',
       'url': 'https://www.youtube.com/watch?v=HLwvN9mF1R0&t=345s',
       'video_id': 'HLwvN9mF1R0'},
      {'author': 'EstimateHub — PDF to ESX converter for Xactimate',
       'channel': 'EstimateHub — PDF to ESX converter for Xactimate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:08](https://www.youtube.com/watch?v=KeJzOY4eZHU&t=68s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Uh you can set your company header here. So an insurance carrier is going to '
               "set their header or contractor is going to set their header, so it's going to "
               'be a logo and their details.',
       'timestamp': 68,
       'timestamp_label': '[00:01:08]',
       'timestamp_seconds': 68,
       'tip': 'Uh you can set your company header here. So an insurance carrier is going to '
              "set their header or contractor is going to set their header, so it's going to "
              'be a logo and their details.',
       'title': 'Xactimate Estimate Example (EstimateHub — PDF to ESX converter for Xactimate)',
       'url': 'https://www.youtube.com/watch?v=KeJzOY4eZHU&t=68s',
       'video_id': 'KeJzOY4eZHU'},
      {'author': 'Adjuster TV',
       'channel': 'Adjuster TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:56](https://www.youtube.com/watch?v=zOFPOUrXGw4&t=356s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Lowest possible deductible that they may have is 500 bucks or ,000 bucks right '
               'unfortunately sometimes we have to say no on claims learn about exclusions in '
               'this next video right here.',
       'timestamp': 356,
       'timestamp_label': '[00:05:56]',
       'timestamp_seconds': 356,
       'tip': 'Lowest possible deductible that they may have is 500 bucks or ,000 bucks right '
              'unfortunately sometimes we have to say no on claims learn about exclusions in '
              'this next video right here.',
       'title': 'Insurance Deductibles 101: When, Why, and How They Apply (Adjuster TV)',
       'url': 'https://www.youtube.com/watch?v=zOFPOUrXGw4&t=356s',
       'video_id': 'zOFPOUrXGw4'},
      {'author': 'Self-Funded',
       'channel': 'Self-Funded',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:51](https://www.youtube.com/watch?v=nBqdaYbbpKg&t=51s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Essentially just adjudicate claims eligibility management and try to implement '
               'and run every.',
       'timestamp': 51,
       'timestamp_label': '[00:00:51]',
       'timestamp_seconds': 51,
       'tip': 'Essentially just adjudicate claims eligibility management and try to implement '
              'and run every.',
       'title': 'Life at Third Party Administrator - Owen Paradis - JP Farley - True Captive '
                'Summit (Self-Funded)',
       'url': 'https://www.youtube.com/watch?v=nBqdaYbbpKg&t=51s',
       'video_id': 'nBqdaYbbpKg'},
      {'author': 'Testudo LLC',
       'channel': 'Testudo LLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:55](https://www.youtube.com/watch?v=4NKJ6zuVvTY&t=715s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'The work area each cell requires its own wipe and each counter tab can be '
               'wiped in its entirety unless it is over 40 square feet you use a long-handled '
               'mop and wipe no more than 40 square feet per wipe compare each wipe to the '
               'cleaning verification.',
       'timestamp': 715,
       'timestamp_label': '[00:11:55]',
       'timestamp_seconds': 715,
       'tip': 'The work area each cell requires its own wipe and each counter tab can be wiped '
              'in its entirety unless it is over 40 square feet you use a long-handled mop and '
              'wipe no more than 40 square feet per wipe compare each wipe to the cleaning '
              'verification.',
       'title': 'Lead Safe Renovator Training - Interior Work Practices (Testudo LLC)',
       'url': 'https://www.youtube.com/watch?v=4NKJ6zuVvTY&t=715s',
       'video_id': '4NKJ6zuVvTY'},
      {'author': 'Canei Adjusting',
       'channel': 'Canei Adjusting',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:40](https://www.youtube.com/watch?v=BQZjEuyEaq4&t=700s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Ceiling fans, there are good things, extra features. If there's any in the "
               'room that might need to be, especially if the damage is close to it and that '
               "panel needs come down, then you might want to detach and reset Reese's lights "
               'as well.',
       'timestamp': 700,
       'timestamp_label': '[00:11:40]',
       'timestamp_seconds': 700,
       'tip': "Ceiling fans, there are good things, extra features. If there's any in the room "
              'that might need to be, especially if the damage is close to it and that panel '
              "needs come down, then you might want to detach and reset Reese's lights as "
              'well.',
       'title': 'CEILING XACTIMATE LINE ITEMS (Canei Adjusting)',
       'url': 'https://www.youtube.com/watch?v=BQZjEuyEaq4&t=700s',
       'video_id': 'BQZjEuyEaq4'},
      {'author': 'Chad Michael - The Practitioner',
       'channel': 'Chad Michael - The Practitioner',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:20:10](https://www.youtube.com/watch?v=4dhIe6HGIs0&t=1210s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Common things that they resist on right but some but sometimes it's like the "
               'insurance company they prove the whole thing right they prove a bunch of '
               "things they give you this great thing like how come all of them can't be that "
               'way.',
       'timestamp': 1210,
       'timestamp_label': '[00:20:10]',
       'timestamp_seconds': 1210,
       'tip': "Common things that they resist on right but some but sometimes it's like the "
              'insurance company they prove the whole thing right they prove a bunch of things '
              "they give you this great thing like how come all of them can't be that way.",
       'title': 'The Ultimate Insurance Claim Supplement (Chad Michael - The Practitioner)',
       'url': 'https://www.youtube.com/watch?v=4dhIe6HGIs0&t=1210s',
       'video_id': '4dhIe6HGIs0'},
      {'author': 'ProLine',
       'channel': 'ProLine',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:49](https://www.youtube.com/watch?v=g3I-8o2x140&t=949s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Add we can try we's try this one is this going to have your face in it well "
               "that one's muted maybe we'll add both and see what happens but you are muted.",
       'timestamp': 949,
       'timestamp_label': '[00:15:49]',
       'timestamp_seconds': 949,
       'tip': "Add we can try we's try this one is this going to have your face in it well "
              "that one's muted maybe we'll add both and see what happens but you are muted.",
       'title': 'Roofing subcrews, profit, markup, and repair work | Roofer2Roofer 002 '
                '(ProLine)',
       'url': 'https://www.youtube.com/watch?v=g3I-8o2x140&t=949s',
       'video_id': 'g3I-8o2x140'},
      {'author': 'PushLeads',
       'channel': 'PushLeads',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:23](https://www.youtube.com/watch?v=wnVxHv3JM28&t=503s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q10 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'For most significant insurance claims, you need both. For small losses with '
               'limited material removal, the restoration company alone may handle it. For '
               'purely structural repairs with no environmental concerns, a general contractor '
               'is the right call from the start.',
       'timestamp': 503,
       'timestamp_label': '[00:08:23]',
       'timestamp_seconds': 503,
       'tip': 'For most significant insurance claims, you need both. For small losses with '
              'limited material removal, the restoration company alone may handle it. For '
              'purely structural repairs with no environmental concerns, a general contractor '
              'is the right call from the start.',
       'title': "Restoration Company vs General Contractor: What's the Difference? (PushLeads)",
       'url': 'https://www.youtube.com/watch?v=wnVxHv3JM28&t=503s',
       'video_id': 'wnVxHv3JM28'}],
 11: [{'author': 'Tampa Bay 28',
       'channel': 'Tampa Bay 28',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:52](https://www.youtube.com/watch?v=1DrEImX-sYU&t=52s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Her contractor also asked her to approve an assignment of benefits you said '
               "I'll take care of everything for years the i-team exposed the abuse of the.",
       'timestamp': 52,
       'timestamp_label': '[00:00:52]',
       'timestamp_seconds': 52,
       'tip': 'Her contractor also asked her to approve an assignment of benefits you said '
              "I'll take care of everything for years the i-team exposed the abuse of the.",
       'title': "Stopping 'Assignment of Benefits' Abuse (Tampa Bay 28)",
       'url': 'https://www.youtube.com/watch?v=1DrEImX-sYU&t=52s',
       'video_id': '1DrEImX-sYU'},
      {'author': "The Adjuster's Roundtable",
       'channel': "The Adjuster's Roundtable",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:33](https://www.youtube.com/watch?v=_wmRAji2ZmI&t=333s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'I was able to develop not only with their senior level desk adjusters but the '
               'next level above that, you know, the big time decision makers, you know the '
               'director of the claims operations.',
       'timestamp': 333,
       'timestamp_label': '[00:05:33]',
       'timestamp_seconds': 333,
       'tip': 'I was able to develop not only with their senior level desk adjusters but the '
              'next level above that, you know, the big time decision makers, you know the '
              'director of the claims operations.',
       'title': 'How he Overturned a Denied Insurance Claim | Public Adjuster Case Study & '
                "Expert Tips (The Adjuster's Roundtable)",
       'url': 'https://www.youtube.com/watch?v=_wmRAji2ZmI&t=333s',
       'video_id': '_wmRAji2ZmI'},
      {'author': 'Phill McGurk',
       'channel': 'Phill McGurk',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:25](https://www.youtube.com/watch?v=Dl8DpDk97_A&t=325s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'It avoids that whole conflict of interest of having the company grade its own '
               "homework. So, let's just boil this all down into your personal hiring "
               'checklist. Before you sign any contract, make sure you can check these four '
               'boxes.',
       'timestamp': 325,
       'timestamp_label': '[00:05:25]',
       'timestamp_seconds': 325,
       'tip': 'It avoids that whole conflict of interest of having the company grade its own '
              "homework. So, let's just boil this all down into your personal hiring "
              'checklist. Before you sign any contract, make sure you can check these four '
              'boxes.',
       'title': 'IICRC S520 - Core Principle of Mould Remediation (Phill McGurk)',
       'url': 'https://www.youtube.com/watch?v=Dl8DpDk97_A&t=325s',
       'video_id': 'Dl8DpDk97_A'},
      {'author': "Shane O'Dazier | RestorationProfits",
       'channel': "Shane O'Dazier | RestorationProfits",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:05](https://www.youtube.com/watch?v=SK7KHGnvQ6Y&t=725s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'In your information we get on a call and see how we can help you grow your '
               "company lastly there'll be some other videos right here if you want to watch "
               'more content about growing your Restoration company check out one of these '
               "videos we'll see you guys on the next one.",
       'timestamp': 725,
       'timestamp_label': '[00:12:05]',
       'timestamp_seconds': 725,
       'tip': 'In your information we get on a call and see how we can help you grow your '
              "company lastly there'll be some other videos right here if you want to watch "
              'more content about growing your Restoration company check out one of these '
              "videos we'll see you guys on the next one.",
       'title': "The ugly truth about Xactimate and the restoration industry (Shane O'Dazier | "
                'RestorationProfits)',
       'url': 'https://www.youtube.com/watch?v=SK7KHGnvQ6Y&t=725s',
       'video_id': 'SK7KHGnvQ6Y'},
      {'author': 'Fred McCutcheon Jr.',
       'channel': 'Fred McCutcheon Jr.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:19](https://www.youtube.com/watch?v=yrUY61hcioM&t=79s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Your insurance company to coordinate your claim and help you get your life '
               'back on track our fire damage reconstruction experts work quickly to restore '
               'the property to pre-fire conditions thank you from all of us at catastrophy '
               'services and serving your property.',
       'timestamp': 79,
       'timestamp_label': '[00:01:19]',
       'timestamp_seconds': 79,
       'tip': 'Your insurance company to coordinate your claim and help you get your life back '
              'on track our fire damage reconstruction experts work quickly to restore the '
              'property to pre-fire conditions thank you from all of us at catastrophy '
              'services and serving your property.',
       'title': 'Fire Damage Contents Pack Outs (Fred McCutcheon Jr.)',
       'url': 'https://www.youtube.com/watch?v=yrUY61hcioM&t=79s',
       'video_id': 'yrUY61hcioM'},
      {'author': 'FirehouseEducation',
       'channel': 'FirehouseEducation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:41](https://www.youtube.com/watch?v=w85_KBcX690&t=101s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "So, really the the way we determine what what we're going to do is the degree "
               'of the damage to the items, do we have to use ultrasonic, how intense is our '
               'cleaning situation, and then how damaged if any, is our structure.',
       'timestamp': 101,
       'timestamp_label': '[00:01:41]',
       'timestamp_seconds': 101,
       'tip': "So, really the the way we determine what what we're going to do is the degree "
              'of the damage to the items, do we have to use ultrasonic, how intense is our '
              'cleaning situation, and then how damaged if any, is our structure.',
       'title': 'When Do You Packout or Clean In Place A Contents Restoration Job? '
                '(FirehouseEducation)',
       'url': 'https://www.youtube.com/watch?v=w85_KBcX690&t=101s',
       'video_id': 'w85_KBcX690'},
      {'author': 'Roof Sales Mastery',
       'channel': 'Roof Sales Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:20](https://www.youtube.com/watch?v=rui1iBgQxWY&t=200s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "So, simplify your business. Make sure that you're delegating tasks to people "
               'and make them responsible for the one thing that they should really be good '
               "at. That's why your production manager just focuses on production.",
       'timestamp': 200,
       'timestamp_label': '[00:03:20]',
       'timestamp_seconds': 200,
       'tip': "So, simplify your business. Make sure that you're delegating tasks to people "
              'and make them responsible for the one thing that they should really be good at. '
              "That's why your production manager just focuses on production.",
       'title': 'Should You Designate an In-House Supplementer for Roof Claims? (Roof Sales '
                'Mastery)',
       'url': 'https://www.youtube.com/watch?v=rui1iBgQxWY&t=200s',
       'video_id': 'rui1iBgQxWY'},
      {'author': 'State Restoration Services',
       'channel': 'State Restoration Services',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:35](https://www.youtube.com/watch?v=06ChGuOZCto&t=35s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': '20,000 into 50/50, half of it now, half of it after you build the roof. '
               'Deductible is not something that insurance company will ever take from you. '
               "You don't have to ever, ever, under no circumstances, they will ask you to "
               'send the money to them, all right?',
       'timestamp': 35,
       'timestamp_label': '[00:00:35]',
       'timestamp_seconds': 35,
       'tip': '20,000 into 50/50, half of it now, half of it after you build the roof. '
              'Deductible is not something that insurance company will ever take from you. You '
              "don't have to ever, ever, under no circumstances, they will ask you to send the "
              'money to them, all right?',
       'title': 'Insurance Deductible Explained What It Means for Your Roof Claim (State '
                'Restoration Services)',
       'url': 'https://www.youtube.com/watch?v=06ChGuOZCto&t=35s',
       'video_id': '06ChGuOZCto'},
      {'author': 'Chad Michael - The Practitioner',
       'channel': 'Chad Michael - The Practitioner',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:31:58](https://www.youtube.com/watch?v=bVX2IRINNSM&t=1918s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'On all sake but State Farm so what was one with this call them give another '
               "thing that we're asking 1453 and when the team 53 answers that adjusts with.",
       'timestamp': 1918,
       'timestamp_label': '[00:31:58]',
       'timestamp_seconds': 1918,
       'tip': 'On all sake but State Farm so what was one with this call them give another '
              "thing that we're asking 1453 and when the team 53 answers that adjusts with.",
       'title': 'Who To Send Xactimate Estimate To? | Roof Claim Supplement (Chad Michael - '
                'The Practitioner)',
       'url': 'https://www.youtube.com/watch?v=bVX2IRINNSM&t=1918s',
       'video_id': 'bVX2IRINNSM'},
      {'author': 'Andrew Melrose',
       'channel': 'Andrew Melrose',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:00](https://www.youtube.com/watch?v=iQ4PIKW3sEc&t=120s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "Effectively and uh there's a science of drying it really is extracting its "
               "fans its dehumidifiers it's assessing the different materials um and then "
               "we're.",
       'timestamp': 120,
       'timestamp_label': '[00:02:00]',
       'timestamp_seconds': 120,
       'tip': "Effectively and uh there's a science of drying it really is extracting its fans "
              "its dehumidifiers it's assessing the different materials um and then we're.",
       'title': 'Only Hire Certified Professionals! - (Water Restoration/IICRC s500 VS. Mold '
                'Remediation/IICRC s520) (Andrew Melrose)',
       'url': 'https://www.youtube.com/watch?v=iQ4PIKW3sEc&t=120s',
       'video_id': 'iQ4PIKW3sEc'},
      {'author': 'Adjusterpedia',
       'channel': 'Adjusterpedia',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:38](https://www.youtube.com/watch?v=4EdiIO_RCX0&t=218s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Check mark so you get the idea through here or does it have pipe jacks yes or '
               'whatever do I have valley metal W check mark yes how many pipe jacks do I '
               'have.',
       'timestamp': 218,
       'timestamp_label': '[00:03:38]',
       'timestamp_seconds': 218,
       'tip': 'Check mark so you get the idea through here or does it have pipe jacks yes or '
              'whatever do I have valley metal W check mark yes how many pipe jacks do I have.',
       'title': 'Why and How to use Scope Sheets - Tutorial (Adjusterpedia)',
       'url': 'https://www.youtube.com/watch?v=4EdiIO_RCX0&t=218s',
       'video_id': '4EdiIO_RCX0'},
      {'author': 'Xactimate Training by Crest LLC',
       'channel': 'Xactimate Training by Crest LLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:51](https://www.youtube.com/watch?v=CFVMi9HmVcM&t=51s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'I just wanted to put a little bit of everything in there. You can see here '
               "I've got removing some wet non-s salvageable carpet, some carpet pad, tear out "
               '2 ft of drywall, tear out baseboard, and tear out one cabinet just as an '
               "example. So, I'm going to save and exit.",
       'timestamp': 51,
       'timestamp_label': '[00:00:51]',
       'timestamp_seconds': 51,
       'tip': "I just wanted to put a little bit of everything in there. You can see here I've "
              'got removing some wet non-s salvageable carpet, some carpet pad, tear out 2 ft '
              'of drywall, tear out baseboard, and tear out one cabinet just as an example. '
              "So, I'm going to save and exit.",
       'title': 'Xactimate - Water Mitigation to Rebuild Estimate Tool (Xactimate Training by '
                'Crest LLC)',
       'url': 'https://www.youtube.com/watch?v=CFVMi9HmVcM&t=51s',
       'video_id': 'CFVMi9HmVcM'},
      {'author': 'Adjuster TV',
       'channel': 'Adjuster TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:47](https://www.youtube.com/watch?v=lIyYVIMZa0s&t=527s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'My industry Partners to help you be a great adjuster so that you can serve our '
               'industry and make a great living doing it and as always thank you so much for '
               'watching and have a great storm.',
       'timestamp': 527,
       'timestamp_label': '[00:08:47]',
       'timestamp_seconds': 527,
       'tip': 'My industry Partners to help you be a great adjuster so that you can serve our '
              'industry and make a great living doing it and as always thank you so much for '
              'watching and have a great storm.',
       'title': 'How to write a roof repair estimate in Xactimate X1 (Adjuster TV)',
       'url': 'https://www.youtube.com/watch?v=lIyYVIMZa0s&t=527s',
       'video_id': 'lIyYVIMZa0s'},
      {'author': 'Encircle',
       'channel': 'Encircle',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:58:09](https://www.youtube.com/watch?v=33iGNdZ6fyE&t=3489s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Your strongest argument your second strongest argument would be then I need to '
               'know what chemicals to use to clean it if it can be cleaned or do I have to '
               "remove the material that' be your next strongest.",
       'timestamp': 3489,
       'timestamp_label': '[00:58:09]',
       'timestamp_seconds': 3489,
       'tip': 'Your strongest argument your second strongest argument would be then I need to '
              'know what chemicals to use to clean it if it can be cleaned or do I have to '
              "remove the material that' be your next strongest.",
       'title': 'Fire & Smoke Restoration Bootcamp - Webinar (Encircle)',
       'url': 'https://www.youtube.com/watch?v=33iGNdZ6fyE&t=3489s',
       'video_id': '33iGNdZ6fyE'},
      {'author': 'Homeowner Explained',
       'channel': 'Homeowner Explained',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:39](https://www.youtube.com/watch?v=MPSOkm3YFak&t=579s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q11 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Read your deductible, roof coverage, and deadline before you call. Be there '
               "for the adjuster, and don't sign anything at your front door. And know your "
               'options if the payout falls short. Grab the free Wind and Hail Claim Checklist '
               'at homeownerexplained.',
       'timestamp': 579,
       'timestamp_label': '[00:09:39]',
       'timestamp_seconds': 579,
       'tip': 'Read your deductible, roof coverage, and deadline before you call. Be there for '
              "the adjuster, and don't sign anything at your front door. And know your options "
              'if the payout falls short. Grab the free Wind and Hail Claim Checklist at '
              'homeownerexplained.',
       'title': 'Did the Hail Really Damage Your Roof? Check This First (Homeowner Explained)',
       'url': 'https://www.youtube.com/watch?v=MPSOkm3YFak&t=579s',
       'video_id': 'MPSOkm3YFak'}],
 12: [{'author': "Shane O'Dazier | RestorationProfits",
       'channel': "Shane O'Dazier | RestorationProfits",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:32](https://www.youtube.com/watch?v=roHp-ZzbYvs&t=452s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Instead of just billing for three days or 4 days I started using half day '
               'Roundup billing so if it sat there for 3 days and a few hours start charging '
               '3.4.',
       'timestamp': 452,
       'timestamp_label': '[00:07:32]',
       'timestamp_seconds': 452,
       'tip': 'Instead of just billing for three days or 4 days I started using half day '
              'Roundup billing so if it sat there for 3 days and a few hours start charging '
              '3.4.',
       'title': "Top 5 Xactimate hacks for water damage estimates (Shane O'Dazier | "
                'RestorationProfits)',
       'url': 'https://www.youtube.com/watch?v=roHp-ZzbYvs&t=452s',
       'video_id': 'roHp-ZzbYvs'},
      {'author': 'Restoration Growth Co',
       'channel': 'Restoration Growth Co',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:46](https://www.youtube.com/watch?v=zkR_04H9hBQ&t=586s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': '30 more water damage jobs in your first 90 days, not 30 leads, 30 jobs. And if '
               "the number isn't there at day 90, we keep working and you stop paying until it "
               'is. Only one restoration company per market.',
       'timestamp': 586,
       'timestamp_label': '[00:09:46]',
       'timestamp_seconds': 586,
       'tip': '30 more water damage jobs in your first 90 days, not 30 leads, 30 jobs. And if '
              "the number isn't there at day 90, we keep working and you stop paying until it "
              'is. Only one restoration company per market.',
       'title': 'The Hidden Cost of Water Damage Google Ads (And How to Stop It!) (Restoration '
                'Growth Co)',
       'url': 'https://www.youtube.com/watch?v=zkR_04H9hBQ&t=586s',
       'video_id': 'zkR_04H9hBQ'},
      {'author': 'claimhelpme',
       'channel': 'claimhelpme',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:26](https://www.youtube.com/watch?v=eLQHV7yIGx8&t=146s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'And homeowners, do you notice the difference? One contractor promises to start '
               'tomorrow, the other explains what happens when the insurance company '
               'disagrees, how the scope will be reviewed, and needs to be done before the '
               'construction begins. One demonstrated knowledge.',
       'timestamp': 146,
       'timestamp_label': '[00:02:26]',
       'timestamp_seconds': 146,
       'tip': 'And homeowners, do you notice the difference? One contractor promises to start '
              'tomorrow, the other explains what happens when the insurance company disagrees, '
              'how the scope will be reviewed, and needs to be done before the construction '
              'begins. One demonstrated knowledge.',
       'title': 'Restoration Contractors: Stop Selling From Weakness! Insurance Claims Done '
                'Right (claimhelpme)',
       'url': 'https://www.youtube.com/watch?v=eLQHV7yIGx8&t=146s',
       'video_id': 'eLQHV7yIGx8'},
      {'author': 'Canei Adjusting',
       'channel': 'Canei Adjusting',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:11](https://www.youtube.com/watch?v=Sk9blhK0GiU&t=251s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "So let's say we receive the claim on the 23rd if you're a contractor, the day "
               'that you signed the contract with the insured day that you contacted the '
               "insured, you received on the 23rd, but they didn't give you permission to call "
               'until the 24th.',
       'timestamp': 251,
       'timestamp_label': '[00:04:11]',
       'timestamp_seconds': 251,
       'tip': "So let's say we receive the claim on the 23rd if you're a contractor, the day "
              'that you signed the contract with the insured day that you contacted the '
              "insured, you received on the 23rd, but they didn't give you permission to call "
              'until the 24th.',
       'title': 'XACTIMATE CLAIM INFORMATION (Canei Adjusting)',
       'url': 'https://www.youtube.com/watch?v=Sk9blhK0GiU&t=251s',
       'video_id': 'Sk9blhK0GiU'},
      {'author': 'Tradeforge CRM',
       'channel': 'Tradeforge CRM',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:24](https://www.youtube.com/watch?v=Kiez0kPNuRk&t=384s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "14-day trial, no credit card needed. If you don't love it, dead stop, you "
               "know, after 14 days. If you do love it, pick a plan. You know, we're always "
               'going to be updating the system.',
       'timestamp': 384,
       'timestamp_label': '[00:06:24]',
       'timestamp_seconds': 384,
       'tip': "14-day trial, no credit card needed. If you don't love it, dead stop, you know, "
              "after 14 days. If you do love it, pick a plan. You know, we're always going to "
              'be updating the system.',
       'title': 'Roof Measurement → Supplement → Signed Contract in One Workflow | TradeForge '
                'for Roofers (Tradeforge CRM)',
       'url': 'https://www.youtube.com/watch?v=Kiez0kPNuRk&t=384s',
       'video_id': 'Kiez0kPNuRk'},
      {'author': 'Marketing Ninjas',
       'channel': 'Marketing Ninjas',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:34](https://www.youtube.com/watch?v=5Ibyq8oHR7Y&t=214s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Clear tiers, clear benefits, easy to engage. So, why does this approach work '
               "so well long term? 's paying for their leads and start being the company that "
               "all the plumbers are bragging about. Well, this works because it's not about "
               'gimmicks.',
       'timestamp': 214,
       'timestamp_label': '[00:03:34]',
       'timestamp_seconds': 214,
       'tip': 'Clear tiers, clear benefits, easy to engage. So, why does this approach work so '
              "well long term? 's paying for their leads and start being the company that all "
              "the plumbers are bragging about. Well, this works because it's not about "
              'gimmicks.',
       'title': 'How to Generate 7 Figures for Your Restoration Company From Plumbers '
                '(Marketing Ninjas)',
       'url': 'https://www.youtube.com/watch?v=5Ibyq8oHR7Y&t=214s',
       'video_id': '5Ibyq8oHR7Y'},
      {'author': 'Restoration Made Simple',
       'channel': 'Restoration Made Simple',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:17](https://www.youtube.com/watch?v=aBQA1Wn_LNQ&t=377s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Again, you can adapt it to your area, but I would print these for my guys in '
               'Colorado and also for a company in Utah. And they were closing between three '
               'to five more self-paid jobs a month with just this sheet. And you can get '
               'that, okay?',
       'timestamp': 377,
       'timestamp_label': '[00:06:17]',
       'timestamp_seconds': 377,
       'tip': 'Again, you can adapt it to your area, but I would print these for my guys in '
              'Colorado and also for a company in Utah. And they were closing between three to '
              'five more self-paid jobs a month with just this sheet. And you can get that, '
              'okay?',
       'title': 'Restoration Made Simple - How to start a water damage business (Restoration '
                'Made Simple)',
       'url': 'https://www.youtube.com/watch?v=aBQA1Wn_LNQ&t=377s',
       'video_id': 'aBQA1Wn_LNQ'},
      {'author': 'Overhead And Profit',
       'channel': 'Overhead And Profit',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:09](https://www.youtube.com/watch?v=A7SLk2mjCXU&t=249s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Money on the table for more on this please go to www. overhead andpractices '
               'writing services and invoicing supplementing and billing thank you so much for '
               "watching hope you're having a great day.",
       'timestamp': 249,
       'timestamp_label': '[00:04:09]',
       'timestamp_seconds': 249,
       'tip': 'Money on the table for more on this please go to www. overhead andpractices '
              'writing services and invoicing supplementing and billing thank you so much for '
              "watching hope you're having a great day.",
       'title': 'Xactimate and Insurance Prices Change Every Month; Do You Know How Much? '
                '(Overhead And Profit)',
       'url': 'https://www.youtube.com/watch?v=A7SLk2mjCXU&t=249s',
       'video_id': 'A7SLk2mjCXU'},
      {'author': 'Claim Daddy',
       'channel': 'Claim Daddy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:19](https://www.youtube.com/watch?v=yytgxtBGSF8&t=799s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "So, if we're here underneath the project, we would be under parameters, and "
               'this price listing should be the month that you are completing the assignment.',
       'timestamp': 799,
       'timestamp_label': '[00:13:19]',
       'timestamp_seconds': 799,
       'tip': "So, if we're here underneath the project, we would be under parameters, and "
              'this price listing should be the month that you are completing the assignment.',
       'title': '🏠🎯 Master Hail Claim Xactimate Estimating | Pro Adjuster Training (Claim '
                'Daddy)',
       'url': 'https://www.youtube.com/watch?v=yytgxtBGSF8&t=799s',
       'video_id': 'yytgxtBGSF8'},
      {'author': 'ISSA Media',
       'channel': 'ISSA Media',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:39](https://www.youtube.com/watch?v=jFMj8u8OsU4&t=99s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'S520 was uh basically brought into being. Uh we have to first start with the '
               'S500 which was the uh standard that came out for the water damage restoration '
               'industry. But the S500 did not really address anything with mold.',
       'timestamp': 99,
       'timestamp_label': '[00:01:39]',
       'timestamp_seconds': 99,
       'tip': 'S520 was uh basically brought into being. Uh we have to first start with the '
              'S500 which was the uh standard that came out for the water damage restoration '
              'industry. But the S500 did not really address anything with mold.',
       'title': 'Inside the S520: The Standard That Changed Mold Remediation (ISSA Media)',
       'url': 'https://www.youtube.com/watch?v=jFMj8u8OsU4&t=99s',
       'video_id': 'jFMj8u8OsU4'},
      {'author': 'Estimate Mastery',
       'channel': 'Estimate Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:18:02](https://www.youtube.com/watch?v=Vj-mEgtLqUw&t=1082s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Visually so if you want to go in the bedroom here you can start to hover and '
               "learn what exactly make calls all these different wall finishes they don't "
               'call.',
       'timestamp': 1082,
       'timestamp_label': '[00:18:02]',
       'timestamp_seconds': 1082,
       'tip': 'Visually so if you want to go in the bedroom here you can start to hover and '
              "learn what exactly make calls all these different wall finishes they don't "
              'call.',
       'title': 'Xactimate 101 - Free Beginner Training in Xactimate (Estimate Mastery)',
       'url': 'https://www.youtube.com/watch?v=Vj-mEgtLqUw&t=1082s',
       'video_id': 'Vj-mEgtLqUw'},
      {'author': 'Adjuster TV',
       'channel': 'Adjuster TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:48](https://www.youtube.com/watch?v=dtHSqRxkHLA&t=348s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'Property adjuster head on over to adjust your tv.com start right now and get '
               'instant access to a totally free video training anyway that does it for me '
               'thank you so much for watching and have a great storm.',
       'timestamp': 348,
       'timestamp_label': '[00:05:48]',
       'timestamp_seconds': 348,
       'tip': 'Property adjuster head on over to adjust your tv.com start right now and get '
              'instant access to a totally free video training anyway that does it for me '
              'thank you so much for watching and have a great storm.',
       'title': '5 MIND BLOWING Xactimate Mobile Hacks in 5 Minutes 💥 (Adjuster TV)',
       'url': 'https://www.youtube.com/watch?v=dtHSqRxkHLA&t=348s',
       'video_id': 'dtHSqRxkHLA'},
      {'author': 'Roof Sales Mastery',
       'channel': 'Roof Sales Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:08](https://www.youtube.com/watch?v=Jvj3So17gtA&t=128s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': "That's important so we're going to go into that in that same module right "
               'there perfect module module 10 now this is where I start getting away from '
               'estimating and more into sketching and I need to know if this is something '
               'that you think is useful.',
       'timestamp': 128,
       'timestamp_label': '[00:02:08]',
       'timestamp_seconds': 128,
       'tip': "That's important so we're going to go into that in that same module right there "
              'perfect module module 10 now this is where I start getting away from estimating '
              'and more into sketching and I need to know if this is something that you think '
              'is useful.',
       'title': 'Maxing Out Roof Only Claims (Roof Sales Mastery)',
       'url': 'https://www.youtube.com/watch?v=Jvj3So17gtA&t=128s',
       'video_id': 'Jvj3So17gtA'},
      {'author': 'Water Damage Restoration Marketing - Vinnie Mac',
       'channel': 'Water Damage Restoration Marketing - Vinnie Mac',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:30](https://www.youtube.com/watch?v=IDqwheOOgb0&t=150s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'It how to sign up for it how to optimize it how to get the best results and if '
               "things are stuck I'm going to give you some pointers on how to take a look at "
               'that as well um so let me share my screen here and we will get started.',
       'timestamp': 150,
       'timestamp_label': '[00:02:30]',
       'timestamp_seconds': 150,
       'tip': 'It how to sign up for it how to optimize it how to get the best results and if '
              "things are stuck I'm going to give you some pointers on how to take a look at "
              'that as well um so let me share my screen here and we will get started.',
       'title': 'Water Damage Google Local Services Ads: Everything You Need to Know (Water '
                'Damage Restoration Marketing - Vinnie Mac)',
       'url': 'https://www.youtube.com/watch?v=IDqwheOOgb0&t=150s',
       'video_id': 'IDqwheOOgb0'},
      {'author': 'Restoration Success Strategies | Albi',
       'channel': 'Restoration Success Strategies | Albi',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:46](https://www.youtube.com/watch?v=3PlUwHvZkxE&t=646s)',
       'relevance': 'Attributed practitioner commentary on water/fire/mold mitigation & storm '
                    'insurance restoration, `IICRC` psychrometric documentation, `Xactimate` '
                    'supplements, and UPPA-safe collections (Chapter Q12 operational '
                    'verification).',
       'source_type': 'video_pro_tip',
       'text': 'RAA conference a couple months ago and I was on a panel talking where an '
               'insurance adjuster lady was on on stage and she was like, "Oh, you know, if '
               "contractors were to document better and give us better drying logs, we'd be "
               'able to pay out claims better.".',
       'timestamp': 646,
       'timestamp_label': '[00:10:46]',
       'timestamp_seconds': 646,
       'tip': 'RAA conference a couple months ago and I was on a panel talking where an '
              'insurance adjuster lady was on on stage and she was like, "Oh, you know, if '
              "contractors were to document better and give us better drying logs, we'd be "
              'able to pay out claims better.".',
       'title': 'How to Start a Water Damage Restoration Company in 2026 (Restoration Success '
                'Strategies | Albi)',
       'url': 'https://www.youtube.com/watch?v=3PlUwHvZkxE&t=646s',
       'video_id': '3PlUwHvZkxE'}]}
