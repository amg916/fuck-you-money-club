"""Curated 180-citation Commercial Lead Generation baseline (15 per chapter across Q1-Q12) mined strictly from verified Commercial Lead Generation YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'365',
     '50k',
     'ads',
     'agency',
     'apollo',
     'appointment',
     'appointments',
     'attribution',
     'automated',
     'automation',
     'b2b',
     'based',
     'bear',
     'boberdoo',
     'booked',
     'building',
     'business',
     'call',
     'calling',
     'campaigns',
     'can',
     'case',
     'clay',
     'cleaning',
     'client',
     'clients',
     'cold',
     'com',
     'commercial',
     'compliance',
     'consent',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'365',
     '50k',
     'ads',
     'agency',
     'apollo',
     'appointment',
     'appointments',
     'attribution',
     'automated',
     'automation',
     'b2b',
     'based',
     'bear',
     'boberdoo',
     'booked',
     'budget',
     'building',
     'business',
     'buyer',
     'call',
     'calling',
     'campaigns',
     'can',
     'case',
     'clay',
     'cleaning',
     'client',
     'cold',
     'com',
     'commercial',
     'compliance',
     'consent',
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
 3: {'365',
     '50k',
     'ads',
     'agency',
     'apollo',
     'appointment',
     'appointments',
     'attribution',
     'automated',
     'automation',
     'b2b',
     'based',
     'bear',
     'boberdoo',
     'booked',
     'building',
     'business',
     'call',
     'calling',
     'campaigns',
     'can',
     'case',
     'cash',
     'cashflow',
     'clay',
     'cleaning',
     'client',
     'cold',
     'com',
     'commercial',
     'commission',
     'compliance',
     'consent',
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
 4: {'365',
     '50k',
     'ads',
     'agency',
     'apollo',
     'appointment',
     'appointments',
     'attribution',
     'automated',
     'automation',
     'b2b',
     'based',
     'bear',
     'boberdoo',
     'booked',
     'budget',
     'building',
     'business',
     'call',
     'calling',
     'campaigns',
     'can',
     'capital',
     'case',
     'clay',
     'cleaning',
     'client',
     'cold',
     'com',
     'commercial',
     'compliance',
     'consent',
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
 5: {'365',
     '50k',
     'ads',
     'agency',
     'apollo',
     'appointment',
     'appointments',
     'attribution',
     'audit',
     'automated',
     'automation',
     'avoid',
     'b2b',
     'based',
     'bear',
     'boberdoo',
     'booked',
     'building',
     'business',
     'call',
     'calling',
     'campaigns',
     'can',
     'case',
     'clawback',
     'clay',
     'cleaning',
     'client',
     'cold',
     'com',
     'commercial',
     'compliance',
     'consent',
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
 6: {'365',
     '50k',
     'ads',
     'agency',
     'apollo',
     'appointment',
     'appointments',
     'attribution',
     'automated',
     'automation',
     'b2b',
     'based',
     'bear',
     'boberdoo',
     'booked',
     'building',
     'business',
     'call',
     'calling',
     'campaigns',
     'can',
     'case',
     'clay',
     'cleaning',
     'client',
     'cold',
     'com',
     'commercial',
     'compliance',
     'consent',
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
 7: {'365',
     '50k',
     'ads',
     'agency',
     'apollo',
     'appointment',
     'appointments',
     'attribution',
     'automated',
     'automation',
     'b2b',
     'based',
     'bear',
     'boberdoo',
     'booked',
     'building',
     'business',
     'call',
     'calling',
     'campaigns',
     'can',
     'case',
     'checklist',
     'clay',
     'cleaning',
     'client',
     'cold',
     'com',
     'commercial',
     'compliance',
     'consent',
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
 8: {'365',
     '50k',
     'ads',
     'agency',
     'api',
     'apollo',
     'appointment',
     'appointments',
     'attribution',
     'automated',
     'automation',
     'b2b',
     'based',
     'bear',
     'boberdoo',
     'booked',
     'building',
     'business',
     'call',
     'calling',
     'campaigns',
     'can',
     'case',
     'clay',
     'cleaning',
     'client',
     'cold',
     'com',
     'commercial',
     'compliance',
     'consent',
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
 9: {'365',
     '50k',
     'ads',
     'agency',
     'agreement',
     'apollo',
     'appointment',
     'appointments',
     'attribution',
     'automated',
     'automation',
     'b2b',
     'based',
     'bear',
     'boberdoo',
     'booked',
     'building',
     'business',
     'call',
     'calling',
     'campaigns',
     'can',
     'case',
     'clay',
     'cleaning',
     'client',
     'cold',
     'com',
     'commercial',
     'compliance',
     'consent',
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
 10: {'365',
      '50k',
      'ads',
      'agency',
      'agent',
      'ai',
      'apollo',
      'appointment',
      'appointments',
      'attribution',
      'automate',
      'automated',
      'automation',
      'b2b',
      'based',
      'bear',
      'boberdoo',
      'booked',
      'building',
      'business',
      'call',
      'calling',
      'campaigns',
      'can',
      'case',
      'clay',
      'cleaning',
      'client',
      'cold',
      'com',
      'commercial',
      'compliance',
      'consent',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'365',
      '50k',
      'ads',
      'agency',
      'apollo',
      'appointment',
      'appointments',
      'attribution',
      'automated',
      'automation',
      'b2b',
      'based',
      'bear',
      'boberdoo',
      'booked',
      'building',
      'business',
      'call',
      'calling',
      'campaigns',
      'can',
      'case',
      'clay',
      'cleaning',
      'client',
      'cold',
      'com',
      'commercial',
      'compliance',
      'consent',
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
 12: {'365',
      '50k',
      'action',
      'ads',
      'agency',
      'apollo',
      'appointment',
      'appointments',
      'attribution',
      'automated',
      'automation',
      'b2b',
      'based',
      'bear',
      'boberdoo',
      'booked',
      'building',
      'business',
      'call',
      'calling',
      'campaigns',
      'can',
      'case',
      'clay',
      'cleaning',
      'client',
      'cold',
      'com',
      'commercial',
      'compliance',
      'consent',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'AJ Cassata',
      'channel': 'AJ Cassata',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=6l8CThrSJEY&t=21s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re new if you're new here, I'm AJ Cassata, co-founder of Revenue Boost. We are "
              'a outbound agency that generates leads and demos for our clients via cold '
              'email, LinkedIn, and cold calling as well.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "'re new if you're new here, I'm AJ Cassata, co-founder of Revenue Boost. We are "
             'a outbound agency that generates leads and demos for our clients via cold email, '
             'LinkedIn, and cold calling as well.',
      'title': 'How to Get Unlimited Leads Using Clay Enrichment Waterfall | clay.com Tutorial '
               '(AJ Cassata)',
      'url': 'https://www.youtube.com/watch?v=6l8CThrSJEY&t=21s',
      'video_id': '6l8CThrSJEY'},
     {'author': 'Prospeo',
      'channel': 'Prospeo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:13](https://www.youtube.com/watch?v=QnSW0B2oztg&t=193s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This lets you narrow down your search by the company's business model, so you "
              'can target B2B, SaaS, BTC, e-commerce, retail. For my case, I will select SaaS '
              'and B2B.',
      'timestamp': 193,
      'timestamp_label': '[00:03:13]',
      'timestamp_seconds': 193,
      'tip': "This lets you narrow down your search by the company's business model, so you "
             'can target B2B, SaaS, BTC, e-commerce, retail. For my case, I will select SaaS '
             'and B2B.',
      'title': 'How to Use Apollo.io (2026) – Full B2B Lead Generation Tutorial (Prospeo)',
      'url': 'https://www.youtube.com/watch?v=QnSW0B2oztg&t=193s',
      'video_id': 'QnSW0B2oztg'},
     {'author': 'Rafael Hernandez ⚡️',
      'channel': 'Rafael Hernandez ⚡️',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=ngsR38BAFbc&t=110s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So again, just think about that. This business model, the lead gen agency '
              "business model, this is your product. You're delivering a lead, you're "
              "delivering a call, you're delivering an appointment.",
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': 'So again, just think about that. This business model, the lead gen agency '
             "business model, this is your product. You're delivering a lead, you're "
             "delivering a call, you're delivering an appointment.",
      'title': 'Is a Lead Gen Agency Still Worth It in 2026? (Rafael Hernandez ⚡️)',
      'url': 'https://www.youtube.com/watch?v=ngsR38BAFbc&t=110s',
      'video_id': 'ngsR38BAFbc'},
     {'author': 'ItsKeaton',
      'channel': 'ItsKeaton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:23](https://www.youtube.com/watch?v=d2krWJWz2iM&t=323s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '300 to $500 clients, helping local businesses improve their Google business '
              'profile without cold calling, without paid ads, and without needing any SEO '
              'background.',
      'timestamp': 323,
      'timestamp_label': '[00:05:23]',
      'timestamp_seconds': 323,
      'tip': '300 to $500 clients, helping local businesses improve their Google business '
             'profile without cold calling, without paid ads, and without needing any SEO '
             'background.',
      'title': 'Make $500/Month Optimizing Google Business Profiles Using GoHighLevel '
               '(Step-by-Step) (ItsKeaton)',
      'url': 'https://www.youtube.com/watch?v=d2krWJWz2iM&t=323s',
      'video_id': 'd2krWJWz2iM'},
     {'author': 'Portable Entrepreneur',
      'channel': 'Portable Entrepreneur',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:13](https://www.youtube.com/watch?v=AmnzAjTjXDM&t=73s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Google automatically, they will be able to turn off their local service ads and '
              'save that money every single month. Now, the next option for finding more '
              'Google Business Profile clients is through partnerships.',
      'timestamp': 73,
      'timestamp_label': '[00:01:13]',
      'timestamp_seconds': 73,
      'tip': 'Google automatically, they will be able to turn off their local service ads and '
             'save that money every single month. Now, the next option for finding more Google '
             'Business Profile clients is through partnerships.',
      'title': '3 Client-Finding Hacks for Google Business Profile (GBP) Services (in 5 '
               'Minutes) (Portable Entrepreneur)',
      'url': 'https://www.youtube.com/watch?v=AmnzAjTjXDM&t=73s',
      'video_id': 'AmnzAjTjXDM'},
     {'author': 'Billy Robinson',
      'channel': 'Billy Robinson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=NStq42nosUk&t=62s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's the trap of the retainer model. And if you're in it right now, you "
              "already know exactly what I mean. You're capped by how many clients you can "
              'physically handle, and every new client just adds more complexity, not '
              'leverage.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': "That's the trap of the retainer model. And if you're in it right now, you "
             "already know exactly what I mean. You're capped by how many clients you can "
             'physically handle, and every new client just adds more complexity, not leverage.',
      'title': 'How I Built a $250K/Month Pay-Per-Lead Business (Full System) (Billy Robinson)',
      'url': 'https://www.youtube.com/watch?v=NStq42nosUk&t=62s',
      'video_id': 'NStq42nosUk'},
     {'author': 'Digital Real Estate Secrets',
      'channel': 'Digital Real Estate Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:24](https://www.youtube.com/watch?v=cSXYPhrwhwo&t=624s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Clients or how do I get customers to you know buy my service but a lot of them '
              "think like there's some push button system and what I'm saying this is a real "
              "business model it works there's.",
      'timestamp': 624,
      'timestamp_label': '[00:10:24]',
      'timestamp_seconds': 624,
      'tip': 'Clients or how do I get customers to you know buy my service but a lot of them '
             "think like there's some push button system and what I'm saying this is a real "
             "business model it works there's.",
      'title': 'How To Sell leads To Local Businesses (Rank And Rent Method) (Digital Real '
               'Estate Secrets)',
      'url': 'https://www.youtube.com/watch?v=cSXYPhrwhwo&t=624s',
      'video_id': 'cSXYPhrwhwo'},
     {'author': 'HeyReach',
      'channel': 'HeyReach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:29](https://www.youtube.com/watch?v=5JAMkYMtvhw&t=149s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'One of our clients who runs a lead gen agency built his whole list out of '
              'people engaging with posts on specific topics like cold email and cold calling '
              'because those are relevant for what he sells. Then he splits them by topic, so '
              'each group got its own messaging.',
      'timestamp': 149,
      'timestamp_label': '[00:02:29]',
      'timestamp_seconds': 149,
      'tip': 'One of our clients who runs a lead gen agency built his whole list out of people '
             'engaging with posts on specific topics like cold email and cold calling because '
             'those are relevant for what he sells. Then he splits them by topic, so each '
             'group got its own messaging.',
      'title': 'The Laziest Way to Book Meetings on LinkedIn (HeyReach)',
      'url': 'https://www.youtube.com/watch?v=5JAMkYMtvhw&t=149s',
      'video_id': '5JAMkYMtvhw'},
     {'author': 'Saravanan Ganesh',
      'channel': 'Saravanan Ganesh',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:01](https://www.youtube.com/watch?v=GHgraINYcOU&t=301s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And it's giving so much other detail. And then it says recommends what sub "
              'niche I should it says drain cleaning clogged drains should be pretty much what '
              'is prioritizing. The revenue is low, but it says that the combination is drain '
              'cleaning plus sewer line, right?',
      'timestamp': 301,
      'timestamp_label': '[00:05:01]',
      'timestamp_seconds': 301,
      'tip': "And it's giving so much other detail. And then it says recommends what sub niche "
             'I should it says drain cleaning clogged drains should be pretty much what is '
             'prioritizing. The revenue is low, but it says that the combination is drain '
             'cleaning plus sewer line, right?',
      'title': 'How to Find Rank-and-Rent Niches: Exact-Match Domains, Pay-Per-Call Buyers and '
               'AI Follow-Up (Saravanan Ganesh)',
      'url': 'https://www.youtube.com/watch?v=GHgraINYcOU&t=301s',
      'video_id': 'GHgraINYcOU'},
     {'author': 'Steve Hunsaker | Home Service Accelerator',
      'channel': 'Steve Hunsaker | Home Service Accelerator',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:45](https://www.youtube.com/watch?v=wdo4cRHVxXA&t=825s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm smarter than every other successful business in my market and all the "
              "business owners that are at the stage that I want to be. So, I don't think that "
              'I\'m going to do automation because I just I do things differently.".',
      'timestamp': 825,
      'timestamp_label': '[00:13:45]',
      'timestamp_seconds': 825,
      'tip': "I'm smarter than every other successful business in my market and all the "
             "business owners that are at the stage that I want to be. So, I don't think that "
             'I\'m going to do automation because I just I do things differently.".',
      'title': 'Complete Google Maps Lead Generation Guide for Home Service Businesses (100% '
               'FREE) (Steve Hunsaker | Home Service Accelerator)',
      'url': 'https://www.youtube.com/watch?v=wdo4cRHVxXA&t=825s',
      'video_id': 'wdo4cRHVxXA'},
     {'author': 'LeadCaptureIO',
      'channel': 'LeadCaptureIO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:15](https://www.youtube.com/watch?v=WXqAR94YqtU&t=255s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We need to create a hidden field to capture the unique certificate value that '
              'is created when the form is loaded so to do that go to a contact form type of '
              "step in your lead form in this case we'll just go to the actual contact form "
              'step.',
      'timestamp': 255,
      'timestamp_label': '[00:04:15]',
      'timestamp_seconds': 255,
      'tip': 'We need to create a hidden field to capture the unique certificate value that is '
             'created when the form is loaded so to do that go to a contact form type of step '
             "in your lead form in this case we'll just go to the actual contact form step.",
      'title': 'How to Setup ActiveProspect TrustedForm With Your LeadForm to Certify Your '
               'Lead’s Consent (LeadCaptureIO)',
      'url': 'https://www.youtube.com/watch?v=WXqAR94YqtU&t=255s',
      'video_id': 'WXqAR94YqtU'},
     {'author': 'Lead Prosper',
      'channel': 'Lead Prosper',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=gX0fjRlg1lg&t=168s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Content-Type is the only header per the API spec. Content-Type would be the key '
              'and application/json would be the value. This is automatically filled out here '
              'based on the payload type selected above. Finally for the ping set up, we have '
              'our response mapping.',
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': 'Content-Type is the only header per the API spec. Content-Type would be the key '
             'and application/json would be the value. This is automatically filled out here '
             'based on the payload type selected above. Finally for the ping set up, we have '
             'our response mapping.',
      'title': 'Lead Prosper Ping Post Buyer Setup (Lead Prosper)',
      'url': 'https://www.youtube.com/watch?v=gX0fjRlg1lg&t=168s',
      'video_id': 'gX0fjRlg1lg'},
     {'author': 'Leadbase',
      'channel': 'Leadbase',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:10](https://www.youtube.com/watch?v=4k3C9lrziIY&t=430s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Questions and it's relevant for everybody so that's going to wrap up this video "
              "guys and uh hopefully that's helpful hopefully that eases or calms your nerves "
              "a little bit we'll see you in the next video.",
      'timestamp': 430,
      'timestamp_label': '[00:07:10]',
      'timestamp_seconds': 430,
      'tip': "Questions and it's relevant for everybody so that's going to wrap up this video "
             "guys and uh hopefully that's helpful hopefully that eases or calms your nerves a "
             "little bit we'll see you in the next video.",
      'title': "This Is The End Of Lead Gen. New FCC's 1-to-1 Consent Rule Will Kill Your "
               'Agency (Leadbase)',
      'url': 'https://www.youtube.com/watch?v=4k3C9lrziIY&t=430s',
      'video_id': '4k3C9lrziIY'},
     {'author': 'ViB',
      'channel': 'ViB',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:20](https://www.youtube.com/watch?v=w2J3Ou1jTR4&t=260s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This way you can test their ability to deliver high quality appointments before '
              "committing to a larger investment. If you're in the B2B tech space, you're in "
              'luck. Because at ViB, we can work with you to build a custom trial to our pay '
              'per appointment service.',
      'timestamp': 260,
      'timestamp_label': '[00:04:20]',
      'timestamp_seconds': 260,
      'tip': 'This way you can test their ability to deliver high quality appointments before '
             "committing to a larger investment. If you're in the B2B tech space, you're in "
             'luck. Because at ViB, we can work with you to build a custom trial to our pay '
             'per appointment service.',
      'title': 'Pay Per Appointment: The RIGHT Way To Do It For B2B Lead Generation (ViB)',
      'url': 'https://www.youtube.com/watch?v=w2J3Ou1jTR4&t=260s',
      'video_id': 'w2J3Ou1jTR4'},
     {'author': 'Benjamin Bjørnholt',
      'channel': 'Benjamin Bjørnholt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:05](https://www.youtube.com/watch?v=d7ES0xh_MqI&t=365s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm not saying I'm making 100K from a client, but I'm I I've been making "
              'upwards to $15,000 from one client. And I have several clients paying me 4K, '
              "6K, 7K a month because it's a performance-based model.",
      'timestamp': 365,
      'timestamp_label': '[00:06:05]',
      'timestamp_seconds': 365,
      'tip': "I'm not saying I'm making 100K from a client, but I'm I I've been making upwards "
             'to $15,000 from one client. And I have several clients paying me 4K, 6K, 7K a '
             "month because it's a performance-based model.",
      'title': 'Pay-Per-Appointment vs Retainer: The Truth About Agency Pricing (Benjamin '
               'Bjørnholt)',
      'url': 'https://www.youtube.com/watch?v=d7ES0xh_MqI&t=365s',
      'video_id': 'd7ES0xh_MqI'}],
 2: [{'author': 'ViB',
      'channel': 'ViB',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=w2J3Ou1jTR4&t=100s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you've looked into appointment setting vendors or contractors before, you "
              'know the usual setup, big onboarding fees, longterm contracts, and a lot of '
              'cold calling. Providers charged by the hour or on a monthly retainer regardless '
              'of results.',
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': "If you've looked into appointment setting vendors or contractors before, you "
             'know the usual setup, big onboarding fees, longterm contracts, and a lot of cold '
             'calling. Providers charged by the hour or on a monthly retainer regardless of '
             'results.',
      'title': 'Pay Per Appointment: The RIGHT Way To Do It For B2B Lead Generation (ViB)',
      'url': 'https://www.youtube.com/watch?v=w2J3Ou1jTR4&t=100s',
      'video_id': 'w2J3Ou1jTR4'},
     {'author': 'Benjamin Bjørnholt',
      'channel': 'Benjamin Bjørnholt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:50](https://www.youtube.com/watch?v=d7ES0xh_MqI&t=230s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Hey, we're going to run your ads. 're going to prove a appointment setter "
              'inside your business that are going to call all of these leads and book them '
              'into appointment for you. You only pay per shown appointment.',
      'timestamp': 230,
      'timestamp_label': '[00:03:50]',
      'timestamp_seconds': 230,
      'tip': "Hey, we're going to run your ads. 're going to prove a appointment setter inside "
             'your business that are going to call all of these leads and book them into '
             'appointment for you. You only pay per shown appointment.',
      'title': 'Pay-Per-Appointment vs Retainer: The Truth About Agency Pricing (Benjamin '
               'Bjørnholt)',
      'url': 'https://www.youtube.com/watch?v=d7ES0xh_MqI&t=230s',
      'video_id': 'd7ES0xh_MqI'},
     {'author': 'Cold Pipeline',
      'channel': 'Cold Pipeline',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:46](https://www.youtube.com/watch?v=tfCx05hBH78&t=46s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '10 days after someone asked to stop, and the opt-out mechanism itself has to '
              'work without charging a fee or demanding extra personal information. CAN-SPAM '
              'was written for a world of cold commercial email by design.',
      'timestamp': 46,
      'timestamp_label': '[00:00:46]',
      'timestamp_seconds': 46,
      'tip': '10 days after someone asked to stop, and the opt-out mechanism itself has to '
             'work without charging a fee or demanding extra personal information. CAN-SPAM '
             'was written for a world of cold commercial email by design.',
      'title': 'Cold Email Compliance: What the Law Actually Requires (Cold Pipeline)',
      'url': 'https://www.youtube.com/watch?v=tfCx05hBH78&t=46s',
      'video_id': 'tfCx05hBH78'},
     {'author': 'reachmarketingllc',
      'channel': 'reachmarketingllc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:09](https://www.youtube.com/watch?v=M0v6X1EjkRM&t=129s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The budget model begins with the total allowable customer acquisition cost, the '
              'absolute maximum the business can spend to acquire one paying customer. This '
              'vertical waterfall chart illustrates the first deduction. We start with a '
              'hypothetical $6,000 allowance.',
      'timestamp': 129,
      'timestamp_label': '[00:02:09]',
      'timestamp_seconds': 129,
      'tip': 'The budget model begins with the total allowable customer acquisition cost, the '
             'absolute maximum the business can spend to acquire one paying customer. This '
             'vertical waterfall chart illustrates the first deduction. We start with a '
             'hypothetical $6,000 allowance.',
      'title': 'B2B PPC Lead Generation: How to Set CPL, Bids & Budget for ROI '
               '(reachmarketingllc)',
      'url': 'https://www.youtube.com/watch?v=M0v6X1EjkRM&t=129s',
      'video_id': 'M0v6X1EjkRM'},
     {'author': 'Leadbase',
      'channel': 'Leadbase',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:07](https://www.youtube.com/watch?v=4npGl2BQhgg&t=487s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And the cool thing about the lead gen business, too, is, you know, we had um we '
              'have these clients here. This this client was a retainer client that I was '
              'like, "Hey, how about we try, you know, hybrid modeling this a little bit and '
              'we\'ll sell you some leads.".',
      'timestamp': 487,
      'timestamp_label': '[00:08:07]',
      'timestamp_seconds': 487,
      'tip': 'And the cool thing about the lead gen business, too, is, you know, we had um we '
             'have these clients here. This this client was a retainer client that I was like, '
             '"Hey, how about we try, you know, hybrid modeling this a little bit and we\'ll '
             'sell you some leads.".',
      'title': 'Pay Per Lead vs Retainer Agency: Which Makes More Money? (Leadbase)',
      'url': 'https://www.youtube.com/watch?v=4npGl2BQhgg&t=487s',
      'video_id': '4npGl2BQhgg'},
     {'author': 'American WeatherStar',
      'channel': 'American WeatherStar',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:17](https://www.youtube.com/watch?v=sY92btEz6VQ&t=137s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, you don’t get ahold of the customer—leave a message on the phone. Call and '
              'leave another message. If you’ve left a couple of messages, maybe don’t '
              'continue to leave messages, but keep on calling. Send an email, another point '
              'of contact.',
      'timestamp': 137,
      'timestamp_label': '[00:02:17]',
      'timestamp_seconds': 137,
      'tip': 'So, you don’t get ahold of the customer—leave a message on the phone. Call and '
             'leave another message. If you’ve left a couple of messages, maybe don’t continue '
             'to leave messages, but keep on calling. Send an email, another point of contact.',
      'title': 'Lead Generation with Chris Bohn - Commercial Roofing (American WeatherStar)',
      'url': 'https://www.youtube.com/watch?v=sY92btEz6VQ&t=137s',
      'video_id': 'sY92btEz6VQ'},
     {'author': 'Steve Hunsaker | Home Service Accelerator',
      'channel': 'Steve Hunsaker | Home Service Accelerator',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:46](https://www.youtube.com/watch?v=PlZ43ZKMk34&t=166s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They're trying to run YouTube ads. They're trying to maybe pay Angie. They're "
              'trying to do yard sign campaigns, direct mailers, all this other stuff.',
      'timestamp': 166,
      'timestamp_label': '[00:02:46]',
      'timestamp_seconds': 166,
      'tip': "They're trying to run YouTube ads. They're trying to maybe pay Angie. They're "
             'trying to do yard sign campaigns, direct mailers, all this other stuff.',
      'title': 'How to Optimize Your Google Business Profile to Outrank 99% of Local '
               'Businesses on Google (Steve Hunsaker | Home Service Accelerator)',
      'url': 'https://www.youtube.com/watch?v=PlZ43ZKMk34&t=166s',
      'video_id': 'PlZ43ZKMk34'},
     {'author': 'The STRONG Roofer w/ Adam Bensman',
      'channel': 'The STRONG Roofer w/ Adam Bensman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:38](https://www.youtube.com/watch?v=eQNS1yN6pQM&t=638s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, you take that three, five, $10,000 per month test budget, and you say, '
              '"I\'m going to put this into local service ads, pay-per-click, okay, and some '
              'SEO, and I\'m going to see what works. I\'m going to track everything.".',
      'timestamp': 638,
      'timestamp_label': '[00:10:38]',
      'timestamp_seconds': 638,
      'tip': 'So, you take that three, five, $10,000 per month test budget, and you say, "I\'m '
             'going to put this into local service ads, pay-per-click, okay, and some SEO, and '
             'I\'m going to see what works. I\'m going to track everything.".',
      'title': 'STOP Wasting Money on Marketing! The ONLY 4 Ways to Get Roofing Leads (The '
               'STRONG Roofer w/ Adam Bensman)',
      'url': 'https://www.youtube.com/watch?v=eQNS1yN6pQM&t=638s',
      'video_id': 'eQNS1yN6pQM'},
     {'author': 'Lead Prosper',
      'channel': 'Lead Prosper',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=_1N3fncM-Ss&t=21s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ping portion of the buyer set up. You’ll then select the post method and '
              'payload type. As you can see here POST or GET are supported, yet Post is '
              'strongly recommended. Pay special attention to which fields are required on the '
              'ping.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'Ping portion of the buyer set up. You’ll then select the post method and payload '
             'type. As you can see here POST or GET are supported, yet Post is strongly '
             'recommended. Pay special attention to which fields are required on the ping.',
      'title': 'LeadsPedia Ping Post Buyer Setup (Lead Prosper)',
      'url': 'https://www.youtube.com/watch?v=_1N3fncM-Ss&t=21s',
      'video_id': '_1N3fncM-Ss'},
     {'author': 'Ippei - Rank and Rent SEO',
      'channel': 'Ippei - Rank and Rent SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:32](https://www.youtube.com/watch?v=0G_j4pX14MI&t=272s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And then after two, three free leads, we can have this guy just pay us in '
              'commissions. And then eventually, we can enclose this guy on a flat fee rental.',
      'timestamp': 272,
      'timestamp_label': '[00:04:32]',
      'timestamp_seconds': 272,
      'tip': 'And then after two, three free leads, we can have this guy just pay us in '
             'commissions. And then eventually, we can enclose this guy on a flat fee rental.',
      'title': "The Simple Way I'm Making Money Online Renting Websites (Ippei - Rank and Rent "
               'SEO)',
      'url': 'https://www.youtube.com/watch?v=0G_j4pX14MI&t=272s',
      'video_id': '0G_j4pX14MI'},
     {'author': 'Lead Prosper',
      'channel': 'Lead Prosper',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=Ma1kH51odZ0&t=92s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For a successful ping response, the Condition will be key equal with, the Key '
              'will be /response/status, and the Value will be Matched If the buyer system '
              'returns the real time price, you can choose to have Lead Prosper track it when '
              'storing analytics.',
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': 'For a successful ping response, the Condition will be key equal with, the Key '
             'will be /response/status, and the Value will be Matched If the buyer system '
             'returns the real time price, you can choose to have Lead Prosper track it when '
             'storing analytics.',
      'title': 'Boberdoo Ping Post Buyer Setup (Lead Prosper)',
      'url': 'https://www.youtube.com/watch?v=Ma1kH51odZ0&t=92s',
      'video_id': 'Ma1kH51odZ0'},
     {'author': 'DatatoLeads - B2B and B2C Wholesale Data and Leads',
      'channel': 'DatatoLeads - B2B and B2C Wholesale Data and Leads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=1zvwOs0qmmg&t=157s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Loopholes if you got sued let's just say let's just say Hyundai get sued for "
              'call center activities for soliciting or tcpa violations um traditionally they '
              'would go to court and they would say well your honor I ran the DNC list I did '
              'my absolute best.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': "Loopholes if you got sued let's just say let's just say Hyundai get sued for "
             'call center activities for soliciting or tcpa violations um traditionally they '
             'would go to court and they would say well your honor I ran the DNC list I did my '
             'absolute best.',
      'title': 'What is a Lead? TCPA Consent Guide to Opt in Leads - FCC Telemarketing Laws & '
               'Do Not Call List Rule (DatatoLeads - B2B and B2C Wholesale Data and Leads)',
      'url': 'https://www.youtube.com/watch?v=1zvwOs0qmmg&t=157s',
      'video_id': '1zvwOs0qmmg'},
     {'author': 'Local SEO Made Easy',
      'channel': 'Local SEO Made Easy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[03:04:56](https://www.youtube.com/watch?v=sR3EiME-Sy8&t=11096s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Google रिफ्यूज हां सही है। मैं इसको सेलेक्ट करता हूं और इंसर्ट करता हूं तो ये '
              'देखो मेरा इसने यह बना बनाया इसको वो डाल दिया। ठीक है?',
      'timestamp': 11096,
      'timestamp_label': '[03:04:56]',
      'timestamp_seconds': 11096,
      'tip': 'Google रिफ्यूज हां सही है। मैं इसको सेलेक्ट करता हूं और इंसर्ट करता हूं तो ये '
             'देखो मेरा इसने यह बना बनाया इसको वो डाल दिया। ठीक है?',
      'title': 'Master Class Part 2 - Pay Per call Workshop By Paris Qureshi (Local SEO Made '
               'Easy)',
      'url': 'https://www.youtube.com/watch?v=sR3EiME-Sy8&t=11096s',
      'video_id': 'sR3EiME-Sy8'},
     {'author': 'Alex Vacca',
      'channel': 'Alex Vacca',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:13](https://www.youtube.com/watch?v=Ouq5ayjDmmI&t=253s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Google map scraper is your main tool. You can build a list of any local '
              "business in any city in minutes. If you're in a B2B legion agency prospecting "
              'companies and decision makers, LinkedIn scrapers at what you need. VPs, head of '
              "marketing, whatever title you're targeting.",
      'timestamp': 253,
      'timestamp_label': '[00:04:13]',
      'timestamp_seconds': 253,
      'tip': 'Google map scraper is your main tool. You can build a list of any local business '
             "in any city in minutes. If you're in a B2B legion agency prospecting companies "
             'and decision makers, LinkedIn scrapers at what you need. VPs, head of marketing, '
             "whatever title you're targeting.",
      'title': 'Apify Tutorial | How to Scrape Leads 2026 (Alex Vacca)',
      'url': 'https://www.youtube.com/watch?v=Ouq5ayjDmmI&t=253s',
      'video_id': 'Ouq5ayjDmmI'},
     {'author': 'Smart Capital',
      'channel': 'Smart Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:24](https://www.youtube.com/watch?v=ozWkxUTBug4&t=204s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Not every local business is a good client, and choosing well is half the job. '
              'The best clients share three traits. Each new customer is worth a lot to them. '
              'They already spend money trying to find customers, and they can actually take '
              'more work.',
      'timestamp': 204,
      'timestamp_label': '[00:03:24]',
      'timestamp_seconds': 204,
      'tip': 'Not every local business is a good client, and choosing well is half the job. '
             'The best clients share three traits. Each new customer is worth a lot to them. '
             'They already spend money trying to find customers, and they can actually take '
             'more work.',
      'title': 'B2B Lead Generation Services for Local Businesses: How Agencies Get Clients in '
               '2026 (Smart Capital)',
      'url': 'https://www.youtube.com/watch?v=ozWkxUTBug4&t=204s',
      'video_id': 'ozWkxUTBug4'}],
 3: [{'author': 'reachmarketingllc',
      'channel': 'reachmarketingllc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=klDqIDgOt58&t=126s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It does not prove commercial outcomes. This brings us to acquisition economics '
              'and the dangerous illusion of cost per lead or CPL. According to metadata '
              'advertising platform findings, a B2B lead costs $202 on LinkedIn compared to '
              '$524 on Google Ads.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': 'It does not prove commercial outcomes. This brings us to acquisition economics '
             'and the dangerous illusion of cost per lead or CPL. According to metadata '
             'advertising platform findings, a B2B lead costs $202 on LinkedIn compared to '
             '$524 on Google Ads.',
      'title': 'B2B Lead Generation Statistics & Benchmarks 2026: Cost Per Lead, MQL-to-SQL & '
               'Buyer Data (reachmarketingllc)',
      'url': 'https://www.youtube.com/watch?v=klDqIDgOt58&t=126s',
      'video_id': 'klDqIDgOt58'},
     {'author': 'Smart Capital',
      'channel': 'Smart Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=ozWkxUTBug4&t=60s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A qualified lead is often priced at $25 to $500, and one booked appointment '
              'typically costs $150 to $600. 10 appointments a month at $300 each is $3,000 a '
              'month. Three clients at that level is $9,000 a month.',
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': 'A qualified lead is often priced at $25 to $500, and one booked appointment '
             'typically costs $150 to $600. 10 appointments a month at $300 each is $3,000 a '
             'month. Three clients at that level is $9,000 a month.',
      'title': 'B2B Lead Generation Services for Local Businesses: How Agencies Get Clients in '
               '2026 (Smart Capital)',
      'url': 'https://www.youtube.com/watch?v=ozWkxUTBug4&t=60s',
      'video_id': 'ozWkxUTBug4'},
     {'author': 'Cameron England',
      'channel': 'Cameron England',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:19](https://www.youtube.com/watch?v=yRgel0EBz2s&t=979s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's say I charge $300 for appointment. I'm already up 1K net on the front "
              'end. I can reinvest that back into ads. Everything after that on the LTV game '
              "is just free cash flow. So again, to recap, I'm not saying the paper lead model "
              "isn't good.",
      'timestamp': 979,
      'timestamp_label': '[00:16:19]',
      'timestamp_seconds': 979,
      'tip': "Let's say I charge $300 for appointment. I'm already up 1K net on the front end. "
             'I can reinvest that back into ads. Everything after that on the LTV game is just '
             "free cash flow. So again, to recap, I'm not saying the paper lead model isn't "
             'good.',
      'title': 'Why Pay Per Lead Models Are Broken (The Truth Nobody Tells You) (Cameron '
               'England)',
      'url': 'https://www.youtube.com/watch?v=yRgel0EBz2s&t=979s',
      'video_id': 'yRgel0EBz2s'},
     {'author': 'Smartlead',
      'channel': 'Smartlead',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=_lMStnTXkVM&t=35s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'From the big strategy down to the tiny details that make campaigns actually '
              'work. At the beginning, even reaching 10K per month felt impossible. It was a '
              'number we thought was out of reach. But after building our system with clay at '
              'Smartly, everything changed.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'From the big strategy down to the tiny details that make campaigns actually '
             'work. At the beginning, even reaching 10K per month felt impossible. It was a '
             'number we thought was out of reach. But after building our system with clay at '
             'Smartly, everything changed.',
      'title': 'How to Start a Cold Email Agency in 2026 (Make $100,000/Month) (Smartlead)',
      'url': 'https://www.youtube.com/watch?v=_lMStnTXkVM&t=35s',
      'video_id': '_lMStnTXkVM'},
     {'author': 'Belkins',
      'channel': 'Belkins',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=RZgWzmwugYU&t=21s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And one says they only win when you win. So you do what any sensible person '
              'does and you look for the cheapest cost per meeting. In year one, they all cost '
              "about the same. For mid-market and enterprise B2B, that's $3,000 to $5,000 for "
              'every meeting booked.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'And one says they only win when you win. So you do what any sensible person does '
             'and you look for the cheapest cost per meeting. In year one, they all cost about '
             "the same. For mid-market and enterprise B2B, that's $3,000 to $5,000 for every "
             'meeting booked.',
      'title': 'B2B Appointment Setting Cost: Complete Pricing Breakdown (Belkins)',
      'url': 'https://www.youtube.com/watch?v=RZgWzmwugYU&t=21s',
      'video_id': 'RZgWzmwugYU'},
     {'author': 'Hunter Ceroy',
      'channel': 'Hunter Ceroy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:05](https://www.youtube.com/watch?v=0Cfp-Fc0sag&t=245s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "There's a lot of material in here. You made like $10,000 in profit, which is "
              'awesome. But the client might have to make a little bit more. So, you either '
              'have to lower that price maybe to like a 1. So, it would be $175, not 200 to '
              'get them over that 2x rorowaz.',
      'timestamp': 245,
      'timestamp_label': '[00:04:05]',
      'timestamp_seconds': 245,
      'tip': "There's a lot of material in here. You made like $10,000 in profit, which is "
             'awesome. But the client might have to make a little bit more. So, you either '
             'have to lower that price maybe to like a 1. So, it would be $175, not 200 to get '
             'them over that 2x rorowaz.',
      'title': 'Pay Per Lead Pricing in 8 Minutes (Simple Math) (Hunter Ceroy)',
      'url': 'https://www.youtube.com/watch?v=0Cfp-Fc0sag&t=245s',
      'video_id': '0Cfp-Fc0sag'},
     {'author': 'Ippei - Rank and Rent SEO',
      'channel': 'Ippei - Rank and Rent SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:37](https://www.youtube.com/watch?v=Lr9XDVpYZ8M&t=277s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And this is by far going to have the greatest ROI for your efforts. Now, if '
              'you\'re somebody that\'s saying, "Oh, I\'m just kind of limited on time." I '
              'have a few different options as well. My team can build these sites for you at '
              'some cost.',
      'timestamp': 277,
      'timestamp_label': '[00:04:37]',
      'timestamp_seconds': 277,
      'tip': 'And this is by far going to have the greatest ROI for your efforts. Now, if '
             'you\'re somebody that\'s saying, "Oh, I\'m just kind of limited on time." I have '
             'a few different options as well. My team can build these sites for you at some '
             'cost.',
      'title': 'The Best Way to Generate More Leads for Your Service Business in 2026 (Ippei - '
               'Rank and Rent SEO)',
      'url': 'https://www.youtube.com/watch?v=Lr9XDVpYZ8M&t=277s',
      'video_id': 'Lr9XDVpYZ8M'},
     {'author': 'Woodpecker.co',
      'channel': 'Woodpecker.co',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:18](https://www.youtube.com/watch?v=57A2YLV9BY8&t=138s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s not story about us no one sat in European commission or any other country in "
              "the world actually saying let's do a legal act about cold emails a bit not true "
              "for the states where we have can spam act but that's that's a different story.",
      'timestamp': 138,
      'timestamp_label': '[00:02:18]',
      'timestamp_seconds': 138,
      'tip': "'s not story about us no one sat in European commission or any other country in "
             "the world actually saying let's do a legal act about cold emails a bit not true "
             "for the states where we have can spam act but that's that's a different story.",
      'title': 'Is cold emailing illegal? (GDPR explained) (Woodpecker.co)',
      'url': 'https://www.youtube.com/watch?v=57A2YLV9BY8&t=138s',
      'video_id': '57A2YLV9BY8'},
     {'author': 'Lead Gen PH',
      'channel': 'Lead Gen PH',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=i-oQ5e48OF8&t=43s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s a lot of other people also using Apollo, for example. So, if you can be more "
              "creative in the way you're getting leads, they're more fresh, they're more new, "
              "there's less people contacting them, you're going to get a lot better results.",
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': "'s a lot of other people also using Apollo, for example. So, if you can be more "
             "creative in the way you're getting leads, they're more fresh, they're more new, "
             "there's less people contacting them, you're going to get a lot better results.",
      'title': 'How to Source B2B Leads for Cold Email [Google Maps & LinkedIn] (Lead Gen PH)',
      'url': 'https://www.youtube.com/watch?v=i-oQ5e48OF8&t=43s',
      'video_id': 'i-oQ5e48OF8'},
     {'author': 'Lauro Herrera',
      'channel': 'Lauro Herrera',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:34](https://www.youtube.com/watch?v=tRO0J70WjKA&t=94s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Known CCPA was enacted in 1991 the dcpa was designed to Shield consumers from '
              'unsolicited telemarketing calls and faxes over the years it has evolved to '
              'Encompass regulations around text messaging and automated calls playing a '
              'critical role in protecting consumers price.',
      'timestamp': 94,
      'timestamp_label': '[00:01:34]',
      'timestamp_seconds': 94,
      'tip': 'Known CCPA was enacted in 1991 the dcpa was designed to Shield consumers from '
             'unsolicited telemarketing calls and faxes over the years it has evolved to '
             'Encompass regulations around text messaging and automated calls playing a '
             'critical role in protecting consumers price.',
      'title': 'Breaking Down #TCPA 1-to-1 Consent: Handling Leads Safely January '
               '27,2025!📲🤯🔥✅🇺🇸 (Lauro Herrera)',
      'url': 'https://www.youtube.com/watch?v=tRO0J70WjKA&t=94s',
      'video_id': 'tRO0J70WjKA'},
     {'author': 'Lead Prosper',
      'channel': 'Lead Prosper',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:58](https://www.youtube.com/watch?v=Pzlk50aGkUg&t=58s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For the response mapping the condition will be key equal with, the key will be '
              'status, and the value will be continue If your buyer returns the real time '
              'price you can choose to have Lead Prosper track it when storing analytics.',
      'timestamp': 58,
      'timestamp_label': '[00:00:58]',
      'timestamp_seconds': 58,
      'tip': 'For the response mapping the condition will be key equal with, the key will be '
             'status, and the value will be continue If your buyer returns the real time price '
             'you can choose to have Lead Prosper track it when storing analytics.',
      'title': 'Phonexa Ping Post Buyer Set Up (Lead Prosper)',
      'url': 'https://www.youtube.com/watch?v=Pzlk50aGkUg&t=58s',
      'video_id': 'Pzlk50aGkUg'},
     {'author': 'Billy Robinson',
      'channel': 'Billy Robinson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:56](https://www.youtube.com/watch?v=fsKaAe_lO6M&t=236s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Cost yeah so that's essentially the paper lead model works and that's a really "
              "high level overview but in another video I'll cover stuff like distribution "
              'software how to set that up and how to how to get clients thanks for watching '
              "I'll see you soon.",
      'timestamp': 236,
      'timestamp_label': '[00:03:56]',
      'timestamp_seconds': 236,
      'tip': "Cost yeah so that's essentially the paper lead model works and that's a really "
             "high level overview but in another video I'll cover stuff like distribution "
             'software how to set that up and how to how to get clients thanks for watching '
             "I'll see you soon.",
      'title': 'The $3M Pay-Per-Lead Agency Model Explained (Billy Robinson)',
      'url': 'https://www.youtube.com/watch?v=fsKaAe_lO6M&t=236s',
      'video_id': 'fsKaAe_lO6M'},
     {'author': 'AUTOMATED AF',
      'channel': 'AUTOMATED AF',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:57](https://www.youtube.com/watch?v=apGqiy7nBZs&t=417s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Another related question to answer about this subject matter and connect soon '
              'so thank you a lot thank you very much Alex any time all right Crum take care '
              'bye.',
      'timestamp': 417,
      'timestamp_label': '[00:06:57]',
      'timestamp_seconds': 417,
      'tip': 'Another related question to answer about this subject matter and connect soon so '
             'thank you a lot thank you very much Alex any time all right Crum take care bye.',
      'title': 'How GDPR affects cold emailing (AUTOMATED AF)',
      'url': 'https://www.youtube.com/watch?v=apGqiy7nBZs&t=417s',
      'video_id': 'apGqiy7nBZs'},
     {'author': 'Misar AI',
      'channel': 'Misar AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:23](https://www.youtube.com/watch?v=gz6GYKesDk4&t=1403s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And the audience matters too, right? B2B is usually treated differently from '
              'B2C. So, business contacts can often rely on legitimate interest while consumer '
              'contacts generally need consent. Soul traders and freelancers sit closer to the '
              'consumer side.',
      'timestamp': 1403,
      'timestamp_label': '[00:23:23]',
      'timestamp_seconds': 1403,
      'tip': 'And the audience matters too, right? B2B is usually treated differently from '
             'B2C. So, business contacts can often rely on legitimate interest while consumer '
             'contacts generally need consent. Soul traders and freelancers sit closer to the '
             'consumer side.',
      'title': 'Cold Email GDPR Compliance Guide 2026 for B2B Sales Teams (Misar AI)',
      'url': 'https://www.youtube.com/watch?v=gz6GYKesDk4&t=1403s',
      'video_id': 'gz6GYKesDk4'},
     {'author': 'Cold Pipeline',
      'channel': 'Cold Pipeline',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:54](https://www.youtube.com/watch?v=tfCx05hBH78&t=174s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'PO box, or a commercial mail receiving agency address all satisfy it, but the '
              "address can't be missing entirely and this practice treats a bare PO box as the "
              "weaker option even where it's technically allowed.",
      'timestamp': 174,
      'timestamp_label': '[00:02:54]',
      'timestamp_seconds': 174,
      'tip': 'PO box, or a commercial mail receiving agency address all satisfy it, but the '
             "address can't be missing entirely and this practice treats a bare PO box as the "
             "weaker option even where it's technically allowed.",
      'title': 'Cold Email Compliance: What the Law Actually Requires (Cold Pipeline)',
      'url': 'https://www.youtube.com/watch?v=tfCx05hBH78&t=174s',
      'video_id': 'tfCx05hBH78'}],
 4: [{'author': 'Billy Robinson',
      'channel': 'Billy Robinson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:28](https://www.youtube.com/watch?v=-_uHG2CwBjA&t=688s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So wrapping all this up this is a lean, simple business model. One client, one '
              'avatar, one offer, one funnel. And every new client you add just means slightly '
              "increasing your campaign budget and setting up one more GHL account. You're not "
              'building a complex agency.',
      'timestamp': 688,
      'timestamp_label': '[00:11:28]',
      'timestamp_seconds': 688,
      'tip': 'So wrapping all this up this is a lean, simple business model. One client, one '
             'avatar, one offer, one funnel. And every new client you add just means slightly '
             "increasing your campaign budget and setting up one more GHL account. You're not "
             'building a complex agency.',
      'title': 'The Pay Per Lead Model Quietly Printing $75K/Month for Agencies in 2026 (Billy '
               'Robinson)',
      'url': 'https://www.youtube.com/watch?v=-_uHG2CwBjA&t=688s',
      'video_id': '-_uHG2CwBjA'},
     {'author': 'Sendable',
      'channel': 'Sendable',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:33](https://www.youtube.com/watch?v=BWyoFA5VHTE&t=273s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'LinkedIn outreach from A to Z, from finding high-intent leads to contact them '
              'to book sales call on autopilot. So if your current stack for outbound is Sales '
              'Navigator, Clay, Apollo, and HeyReach, you can all replace them with Sendable.',
      'timestamp': 273,
      'timestamp_label': '[00:04:33]',
      'timestamp_seconds': 273,
      'tip': 'LinkedIn outreach from A to Z, from finding high-intent leads to contact them to '
             'book sales call on autopilot. So if your current stack for outbound is Sales '
             'Navigator, Clay, Apollo, and HeyReach, you can all replace them with Sendable.',
      'title': 'The Best Heyreach Alternatives for LinkedIn Outreach Automation (2026) '
               '(Sendable)',
      'url': 'https://www.youtube.com/watch?v=BWyoFA5VHTE&t=273s',
      'video_id': 'BWyoFA5VHTE'},
     {'author': 'Local SEO Made Easy',
      'channel': 'Local SEO Made Easy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:47:53](https://www.youtube.com/watch?v=Bu_9XhXpDSs&t=2873s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So from this dialer, you can call any number yourself from the same number you '
              "put on your website. Let's say we don't have renters or buyers right now. To "
              'find them, we either send emails or make cold calls. And for cold calling, you '
              "don't need a long setup.",
      'timestamp': 2873,
      'timestamp_label': '[00:47:53]',
      'timestamp_seconds': 2873,
      'tip': 'So from this dialer, you can call any number yourself from the same number you '
             "put on your website. Let's say we don't have renters or buyers right now. To "
             'find them, we either send emails or make cold calls. And for cold calling, you '
             "don't need a long setup.",
      'title': 'Callvane Full Demo | Call Tracking, Routing, Recordings & More (Local SEO Made '
               'Easy)',
      'url': 'https://www.youtube.com/watch?v=Bu_9XhXpDSs&t=2873s',
      'video_id': 'Bu_9XhXpDSs'},
     {'author': 'George Vlasyev',
      'channel': 'George Vlasyev',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:57](https://www.youtube.com/watch?v=S8imkVkGoZw&t=537s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, choose SmartLead if you run an agency or manage multiple client accounts. '
              'Its workspace separation, white-label features, advanced compliance tools, IP '
              'rotation, and flexible integrations are designed for scaled operations.',
      'timestamp': 537,
      'timestamp_label': '[00:08:57]',
      'timestamp_seconds': 537,
      'tip': 'Now, choose SmartLead if you run an agency or manage multiple client accounts. '
             'Its workspace separation, white-label features, advanced compliance tools, IP '
             'rotation, and flexible integrations are designed for scaled operations.',
      'title': 'Instantly AI vs Smartlead 2026: Which Cold Email Tool Is Right for You? '
               '(George Vlasyev)',
      'url': 'https://www.youtube.com/watch?v=S8imkVkGoZw&t=537s',
      'video_id': 'S8imkVkGoZw'},
     {'author': 'Smartlead',
      'channel': 'Smartlead',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:08](https://www.youtube.com/watch?v=dTLQCIO7Tf0&t=668s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can go here, click on setup button, and then click schedule campaigns. The '
              'sending schedule I use is Monday to Friday during of course business hours. For '
              "example, let's say that uh our ICP or the people that we are contacting, they "
              'are from Madrid.',
      'timestamp': 668,
      'timestamp_label': '[00:11:08]',
      'timestamp_seconds': 668,
      'tip': 'You can go here, click on setup button, and then click schedule campaigns. The '
             'sending schedule I use is Monday to Friday during of course business hours. For '
             "example, let's say that uh our ICP or the people that we are contacting, they "
             'are from Madrid.',
      'title': 'How to Start Cold Email in 2026: What I Would Do First (Smartlead)',
      'url': 'https://www.youtube.com/watch?v=dTLQCIO7Tf0&t=668s',
      'video_id': 'dTLQCIO7Tf0'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:54:03](https://www.youtube.com/watch?v=yCAVYNpSdZI&t=3243s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But now that we have this benchmark or framework established, I think we can '
              'jump on shorter, more scenario-based demos uh, or screen shares from here out '
              'and and dig into how the system would address your your specific business '
              'processes.',
      'timestamp': 3243,
      'timestamp_label': '[00:54:03]',
      'timestamp_seconds': 3243,
      'tip': 'But now that we have this benchmark or framework established, I think we can '
             'jump on shorter, more scenario-based demos uh, or screen shares from here out '
             'and and dig into how the system would address your your specific business '
             'processes.',
      'title': 'Ping Post Lead Distribution | boberdoo Ping Post Software (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=yCAVYNpSdZI&t=3243s',
      'video_id': 'yCAVYNpSdZI'},
     {'author': 'Nato Guajardo | Insurance Agency Growth',
      'channel': 'Nato Guajardo | Insurance Agency Growth',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:24](https://www.youtube.com/watch?v=VSivqJQ89ow&t=564s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You cannot do that you can't do a lot of those things any anymore on Facebook. "
              'So the way to target someone is by building these videos and in the video '
              "calling out exactly who you're looking for and in the ad copy.",
      'timestamp': 564,
      'timestamp_label': '[00:09:24]',
      'timestamp_seconds': 564,
      'tip': "You cannot do that you can't do a lot of those things any anymore on Facebook. "
             'So the way to target someone is by building these videos and in the video '
             "calling out exactly who you're looking for and in the ad copy.",
      'title': 'The Unlimited Insurance Lead System (Step-by-Step) (Nato Guajardo | Insurance '
               'Agency Growth)',
      'url': 'https://www.youtube.com/watch?v=VSivqJQ89ow&t=564s',
      'video_id': 'VSivqJQ89ow'},
     {'author': 'Best Lifetime Deal',
      'channel': 'Best Lifetime Deal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=4N2eWwb-eo4&t=42s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can connect up to 50 mailboxes with a 99. 4% inbox rate across the board. '
              "Once your inbox is warmed up, you're ready to launch. Head into the campaign "
              'section to see your active campaigns and how each email sequence is performing.',
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': 'You can connect up to 50 mailboxes with a 99. 4% inbox rate across the board. '
             "Once your inbox is warmed up, you're ready to launch. Head into the campaign "
             'section to see your active campaigns and how each email sequence is performing.',
      'title': 'The Best Cold Email Setup: SPF, DKIM, DMARC & Inbox Warmup Explained (Best '
               'Lifetime Deal)',
      'url': 'https://www.youtube.com/watch?v=4N2eWwb-eo4&t=42s',
      'video_id': '4N2eWwb-eo4'},
     {'author': 'Lead Assassin',
      'channel': 'Lead Assassin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:37](https://www.youtube.com/watch?v=oGhWIQAGHbo&t=457s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Generator because this has been really Uh helpful for me so It Might also help '
              'you in building your own clay tables so just going to select this all right and '
              "then let's try to run it for for 10 rs okay.",
      'timestamp': 457,
      'timestamp_label': '[00:07:37]',
      'timestamp_seconds': 457,
      'tip': 'Generator because this has been really Uh helpful for me so It Might also help '
             'you in building your own clay tables so just going to select this all right and '
             "then let's try to run it for for 10 rs okay.",
      'title': 'Clay.com Tutorial #3 - Enrich & Research Data with Claygent (Lead Assassin)',
      'url': 'https://www.youtube.com/watch?v=oGhWIQAGHbo&t=457s',
      'video_id': 'oGhWIQAGHbo'},
     {'author': 'Kidous Mahteme - Inframail Cold Email Inboxes',
      'channel': 'Kidous Mahteme - Inframail Cold Email Inboxes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:17](https://www.youtube.com/watch?v=EN_hwXy6LyU&t=377s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We'll do the free setup you know free onboarding for you and uh yeah enjoy the "
              "rest of your day I hope this made your life a lot easier let's get started book "
              "a call below I'll see you guys talk soon.",
      'timestamp': 377,
      'timestamp_label': '[00:06:17]',
      'timestamp_seconds': 377,
      'tip': "We'll do the free setup you know free onboarding for you and uh yeah enjoy the "
             "rest of your day I hope this made your life a lot easier let's get started book "
             "a call below I'll see you guys talk soon.",
      'title': 'Cold Email Setup: SPF, DKIM, and DMARC (2 minute setup for 10+ inboxes) '
               '(Kidous Mahteme - Inframail Cold Email Inboxes)',
      'url': 'https://www.youtube.com/watch?v=EN_hwXy6LyU&t=377s',
      'video_id': 'EN_hwXy6LyU'},
     {'author': 'Austin Parker',
      'channel': 'Austin Parker',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:45](https://www.youtube.com/watch?v=BVNOmeAp7mg&t=705s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Customers that live in the north suburb should review the north listing, '
              "ideally. The ones across town can review the one that's closest to them. Now, "
              "obviously if you don't have the setup, as long as they're in the same "
              "metroplex, it's usually okay.",
      'timestamp': 705,
      'timestamp_label': '[00:11:45]',
      'timestamp_seconds': 705,
      'tip': 'Customers that live in the north suburb should review the north listing, '
             "ideally. The ones across town can review the one that's closest to them. Now, "
             "obviously if you don't have the setup, as long as they're in the same metroplex, "
             "it's usually okay.",
      'title': 'If You’re Trying to Set Up Multiple Google Business Profiles in 2026, Watch '
               'This First (Austin Parker)',
      'url': 'https://www.youtube.com/watch?v=BVNOmeAp7mg&t=705s',
      'video_id': 'BVNOmeAp7mg'},
     {'author': 'Chris The Insurance Guy',
      'channel': 'Chris The Insurance Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:19](https://www.youtube.com/watch?v=pqWJ1kzSAQc&t=379s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Processes you need to learn how things you know the the coverages work and what '
              "these guys need because there's filings that are needed H Francisco albl Chris "
              'the Adelphia insurance fr.',
      'timestamp': 379,
      'timestamp_label': '[00:06:19]',
      'timestamp_seconds': 379,
      'tip': 'Processes you need to learn how things you know the the coverages work and what '
             "these guys need because there's filings that are needed H Francisco albl Chris "
             'the Adelphia insurance fr.',
      'title': 'LIVE Cold Calling Commercial Insurance Leads (Trucking) (Chris The Insurance '
               'Guy)',
      'url': 'https://www.youtube.com/watch?v=pqWJ1kzSAQc&t=379s',
      'video_id': 'pqWJ1kzSAQc'},
     {'author': 'Max Conversion',
      'channel': 'Max Conversion',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:45](https://www.youtube.com/watch?v=bR17wETzk0c&t=465s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Help you guys increase your performance and improve it and and just get better '
              'so again thanks you guys for watching take care.',
      'timestamp': 465,
      'timestamp_label': '[00:07:45]',
      'timestamp_seconds': 465,
      'tip': 'Help you guys increase your performance and improve it and and just get better '
             'so again thanks you guys for watching take care.',
      'title': 'How We Generated 100+ Truck Insurance Leads in 1 Month (Max Conversion)',
      'url': 'https://www.youtube.com/watch?v=bR17wETzk0c&t=465s',
      'video_id': 'bR17wETzk0c'},
     {'author': 'AJ Cassata',
      'channel': 'AJ Cassata',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:15](https://www.youtube.com/watch?v=12s-u4y1VF0&t=195s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They're more smaller local businesses that are more brick and mortar and you "
              "can't find them through their typical B2B database. So you need tools to scrape "
              "Google Maps. And there's other databases that are just based off Google Maps, "
              'right?',
      'timestamp': 195,
      'timestamp_label': '[00:03:15]',
      'timestamp_seconds': 195,
      'tip': "They're more smaller local businesses that are more brick and mortar and you "
             "can't find them through their typical B2B database. So you need tools to scrape "
             "Google Maps. And there's other databases that are just based off Google Maps, "
             'right?',
      'title': 'The Top 3 Ways We Use Clay.com + AI To Get Leads & Clients [Tutorial] (AJ '
               'Cassata)',
      'url': 'https://www.youtube.com/watch?v=12s-u4y1VF0&t=195s',
      'video_id': '12s-u4y1VF0'},
     {'author': 'Romain Osman Lead Generation',
      'channel': 'Romain Osman Lead Generation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:29](https://www.youtube.com/watch?v=RodU66qhDeY&t=389s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And so as you can see here, when there is no email, it's running Prospero. "
              "We're not doing any water for enrichment right now because we found that "
              "Prospero has very good coverage and so we don't need to use other tools. In our "
              "case, it doesn't necessarily make sense.",
      'timestamp': 389,
      'timestamp_label': '[00:06:29]',
      'timestamp_seconds': 389,
      'tip': "And so as you can see here, when there is no email, it's running Prospero. We're "
             'not doing any water for enrichment right now because we found that Prospero has '
             "very good coverage and so we don't need to use other tools. In our case, it "
             "doesn't necessarily make sense.",
      'title': 'Clay.com Tutorial - Best Workflow For Your Outbound Campaign (Romain Osman '
               'Lead Generation)',
      'url': 'https://www.youtube.com/watch?v=RodU66qhDeY&t=389s',
      'video_id': 'RodU66qhDeY'}],
 5: [{'author': 'Misar AI',
      'channel': 'Misar AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:47](https://www.youtube.com/watch?v=gz6GYKesDk4&t=1367s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And that's different from CAN SPAM, where unsolicited email is allowed as long "
              'as the opt out rules are followed. Under GDPR, you usually rely on legitimate '
              'interest for B2B cold email because getting prior consent for that first '
              'business contact is often not realistic.',
      'timestamp': 1367,
      'timestamp_label': '[00:22:47]',
      'timestamp_seconds': 1367,
      'tip': "And that's different from CAN SPAM, where unsolicited email is allowed as long "
             'as the opt out rules are followed. Under GDPR, you usually rely on legitimate '
             'interest for B2B cold email because getting prior consent for that first '
             'business contact is often not realistic.',
      'title': 'Cold Email GDPR Compliance Guide 2026 for B2B Sales Teams (Misar AI)',
      'url': 'https://www.youtube.com/watch?v=gz6GYKesDk4&t=1367s',
      'video_id': 'gz6GYKesDk4'},
     {'author': 'Matt Lucero',
      'channel': 'Matt Lucero',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:27](https://www.youtube.com/watch?v=jEkDgA8hPmo&t=327s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Campaigns, you can run cold email campaigns through Clay. I believe this is '
              'just a white label of Smart Lead. So, if I press add email account here, it '
              'says your credentials are shared with our email integration partner Smart Lead.',
      'timestamp': 327,
      'timestamp_label': '[00:05:27]',
      'timestamp_seconds': 327,
      'tip': 'Campaigns, you can run cold email campaigns through Clay. I believe this is just '
             'a white label of Smart Lead. So, if I press add email account here, it says your '
             'credentials are shared with our email integration partner Smart Lead.',
      'title': 'FREE Clay.com Crash Course For 2026 (Matt Lucero)',
      'url': 'https://www.youtube.com/watch?v=jEkDgA8hPmo&t=327s',
      'video_id': 'jEkDgA8hPmo'},
     {'author': 'Saleshandy',
      'channel': 'Saleshandy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=lcLenYgem-Q&t=20s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Fail to comply and you risk hefty penalties and fines. So, if you want to avoid '
              'that, you need to watch this video till the end. If you target prospects in the '
              'US country, then you must comply with the CAN-SPAM Act 2003.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'Fail to comply and you risk hefty penalties and fines. So, if you want to avoid '
             'that, you need to watch this video till the end. If you target prospects in the '
             'US country, then you must comply with the CAN-SPAM Act 2003.',
      'title': 'Is Cold Emailing Illegal in the USA? (Saleshandy)',
      'url': 'https://www.youtube.com/watch?v=lcLenYgem-Q&t=20s',
      'video_id': 'lcLenYgem-Q'},
     {'author': 'Romain Osman Lead Generation',
      'channel': 'Romain Osman Lead Generation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:25](https://www.youtube.com/watch?v=RodU66qhDeY&t=265s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We want to do that because there are some providers that we don't want to "
              'contact. In my case here, I avoid contacting Microsoft 365 providers because we '
              'notice that we have low deliverability on those mailboxes.',
      'timestamp': 265,
      'timestamp_label': '[00:04:25]',
      'timestamp_seconds': 265,
      'tip': "We want to do that because there are some providers that we don't want to "
             'contact. In my case here, I avoid contacting Microsoft 365 providers because we '
             'notice that we have low deliverability on those mailboxes.',
      'title': 'Clay.com Tutorial - Best Workflow For Your Outbound Campaign (Romain Osman '
               'Lead Generation)',
      'url': 'https://www.youtube.com/watch?v=RodU66qhDeY&t=265s',
      'video_id': 'RodU66qhDeY'},
     {'author': 'Genesys Digital',
      'channel': 'Genesys Digital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:25](https://www.youtube.com/watch?v=I-riwAqQ3us&t=205s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I continue is that these three questions are 100% customizable based on '
              'whatever specific questions that you would like to ask your client, okay? Just '
              "for simplicity sake, I've decided to ask you these three specific questions, "
              'but really they can be whatever you want, okay?',
      'timestamp': 205,
      'timestamp_label': '[00:03:25]',
      'timestamp_seconds': 205,
      'tip': 'I continue is that these three questions are 100% customizable based on whatever '
             'specific questions that you would like to ask your client, okay? Just for '
             "simplicity sake, I've decided to ask you these three specific questions, but "
             'really they can be whatever you want, okay?',
      'title': 'Mortgage Broker AI Appointment setter - Get Qualified Appointments On '
               'Autopilot (Genesys Digital)',
      'url': 'https://www.youtube.com/watch?v=I-riwAqQ3us&t=205s',
      'video_id': 'I-riwAqQ3us'},
     {'author': 'Surge Digital Marketing',
      'channel': 'Surge Digital Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:16](https://www.youtube.com/watch?v=pZ9P9Hmof3g&t=496s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Fourth, your photos and callouts. Go to campaigns and then assets, and that's "
              'where your six callouts go, the ones replacing the BBB badge. You can also '
              'upload up to 100 business photos there. Fifth, no lead notifications. Go to '
              'admin, then notifications.',
      'timestamp': 496,
      'timestamp_label': '[00:08:16]',
      'timestamp_seconds': 496,
      'tip': "Fourth, your photos and callouts. Go to campaigns and then assets, and that's "
             'where your six callouts go, the ones replacing the BBB badge. You can also '
             'upload up to 100 business photos there. Fifth, no lead notifications. Go to '
             'admin, then notifications.',
      'title': 'Google Local Service Ads Just Changed Forever! (2026 Update) (Surge Digital '
               'Marketing)',
      'url': 'https://www.youtube.com/watch?v=pZ9P9Hmof3g&t=496s',
      'video_id': 'pZ9P9Hmof3g'},
     {'author': 'Ethan Fleming Marketing',
      'channel': 'Ethan Fleming Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:27](https://www.youtube.com/watch?v=TB1PQrXx5s8&t=1227s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Gmail or Outlook or Apple sending so that regular customers are not getting '
              "your emails, which would be really bad. If you're sending less than 50 cold "
              'emails per day, you can use go high level. People who are doing cold email '
              'campaigns send out thousands per day.',
      'timestamp': 1227,
      'timestamp_label': '[00:20:27]',
      'timestamp_seconds': 1227,
      'tip': 'Gmail or Outlook or Apple sending so that regular customers are not getting your '
             "emails, which would be really bad. If you're sending less than 50 cold emails "
             'per day, you can use go high level. People who are doing cold email campaigns '
             'send out thousands per day.',
      'title': 'GoHighLevel Email Deliverability 2025: SPF, DKIM, DMARC + Warmup (No Spam) '
               '(Ethan Fleming Marketing)',
      'url': 'https://www.youtube.com/watch?v=TB1PQrXx5s8&t=1227s',
      'video_id': 'TB1PQrXx5s8'},
     {'author': 'Sell Better',
      'channel': 'Sell Better',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:28](https://www.youtube.com/watch?v=3Y7sW7ob3hY&t=388s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "For example, let's say you cold call a prospect and they were pleasant with "
              "you, but simply didn't have a problem. So there was no reason to book the "
              'meeting. Still add this person to your list and connect with them on LinkedIn.',
      'timestamp': 388,
      'timestamp_label': '[00:06:28]',
      'timestamp_seconds': 388,
      'tip': "For example, let's say you cold call a prospect and they were pleasant with you, "
             "but simply didn't have a problem. So there was no reason to book the meeting. "
             'Still add this person to your list and connect with them on LinkedIn.',
      'title': 'How to Use LinkedIn Sales Navigator For Lead Generation (2025 Update) (Sell '
               'Better)',
      'url': 'https://www.youtube.com/watch?v=3Y7sW7ob3hY&t=388s',
      'video_id': '3Y7sW7ob3hY'},
     {'author': 'Andy Walker',
      'channel': 'Andy Walker',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=FcZZMpjLVNo&t=43s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '"roofer near me", they will never see you, no matter how good you are. Most '
              'owners just think business is slow. The real problem is that Google can only '
              'find them in one small corner of their city. So, the solution to this is having '
              'multiple Google Business Profiles.',
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': '"roofer near me", they will never see you, no matter how good you are. Most '
             'owners just think business is slow. The real problem is that Google can only '
             'find them in one small corner of their city. So, the solution to this is having '
             'multiple Google Business Profiles.',
      'title': '10x Your Leads Overnight With Multiple Google Business Profiles (Andy Walker)',
      'url': 'https://www.youtube.com/watch?v=FcZZMpjLVNo&t=43s',
      'video_id': 'FcZZMpjLVNo'},
     {'author': 'CRMOZ',
      'channel': 'CRMOZ',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:55](https://www.youtube.com/watch?v=T9cn3UyRkR8&t=235s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re tracking your score, but your domain still end up in spam. And the mistake "
              "number one is that you're mixing your cold outreach with your main brand "
              'domain. If you send 5,000 cold marketing emails from your company.',
      'timestamp': 235,
      'timestamp_label': '[00:03:55]',
      'timestamp_seconds': 235,
      'tip': "'re tracking your score, but your domain still end up in spam. And the mistake "
             "number one is that you're mixing your cold outreach with your main brand domain. "
             'If you send 5,000 cold marketing emails from your company.',
      'title': 'SPF DKIM DMARC Setup + 5 Mistakes Killing Your Deliverability (CRMOZ)',
      'url': 'https://www.youtube.com/watch?v=T9cn3UyRkR8&t=235s',
      'video_id': 'T9cn3UyRkR8'},
     {'author': 'Seasalt AI',
      'channel': 'Seasalt AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:40:27](https://www.youtube.com/watch?v=KBFaRW7QmVQ&t=2427s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Using the form uh we will get in touch and then uh and then work work with you '
              "on everything tcpa yeah um I'm GNA leave the page here um for people to scam "
              'but uh Eric and I can now take uh questions uh and then do a little Q&A session '
              'right.',
      'timestamp': 2427,
      'timestamp_label': '[00:40:27]',
      'timestamp_seconds': 2427,
      'tip': 'Using the form uh we will get in touch and then uh and then work work with you '
             "on everything tcpa yeah um I'm GNA leave the page here um for people to scam but "
             'uh Eric and I can now take uh questions uh and then do a little Q&A session '
             'right.',
      'title': '(UPDATE 1/21/2025) New One-to-One Consent Rules: TCPA Compliance w/ TCPAWorld '
               'Troutman & Seasalt.ai (Seasalt AI)',
      'url': 'https://www.youtube.com/watch?v=KBFaRW7QmVQ&t=2427s',
      'video_id': 'KBFaRW7QmVQ'},
     {'author': 'LeadCaptureIO',
      'channel': 'LeadCaptureIO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:36](https://www.youtube.com/watch?v=FQR1fK6va5I&t=396s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You submit a demo or reach out to me and I'm more than happy to discuss tcpa "
              'compliance with you to help you get all set up without any hassles or having to '
              "bang your head against the wall like I did for two months that's all thank you "
              'for your time.',
      'timestamp': 396,
      'timestamp_label': '[00:06:36]',
      'timestamp_seconds': 396,
      'tip': "You submit a demo or reach out to me and I'm more than happy to discuss tcpa "
             'compliance with you to help you get all set up without any hassles or having to '
             "bang your head against the wall like I did for two months that's all thank you "
             'for your time.',
      'title': 'How to capture TCPA one-to-one consent in your lead capture forms '
               '(LeadCaptureIO)',
      'url': 'https://www.youtube.com/watch?v=FQR1fK6va5I&t=396s',
      'video_id': 'FQR1fK6va5I'},
     {'author': 'Smartlead',
      'channel': 'Smartlead',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=DIUObYQih3s&t=89s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If your mail and Outlook doesn't trust you, nothing else matters. That's where "
              'the warm-up process comes in. And when you start from a new domain, you can go '
              'all from day one. As I just said, you need to build credibility gradually.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': "If your mail and Outlook doesn't trust you, nothing else matters. That's where "
             'the warm-up process comes in. And when you start from a new domain, you can go '
             'all from day one. As I just said, you need to build credibility gradually.',
      'title': 'The Ultimate Guide to Cold Email Deliverability in 2026 (Smartlead)',
      'url': 'https://www.youtube.com/watch?v=DIUObYQih3s&t=89s',
      'video_id': 'DIUObYQih3s'},
     {'author': 'Local SEO Made Easy',
      'channel': 'Local SEO Made Easy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:49:27](https://www.youtube.com/watch?v=Bu_9XhXpDSs&t=2967s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Then for the first two, three, four calls that come in, you'll have the "
              'tracking too. You can show him, "Look, I sent this call, here\'s its '
              'recording." So you don\'t need a separate setup for cold calling either. Just '
              'come to the dialer in Callvane, enter the number and call.',
      'timestamp': 2967,
      'timestamp_label': '[00:49:27]',
      'timestamp_seconds': 2967,
      'tip': "Then for the first two, three, four calls that come in, you'll have the tracking "
             'too. You can show him, "Look, I sent this call, here\'s its recording." So you '
             "don't need a separate setup for cold calling either. Just come to the dialer in "
             'Callvane, enter the number and call.',
      'title': 'Callvane Full Demo | Call Tracking, Routing, Recordings & More (Local SEO Made '
               'Easy)',
      'url': 'https://www.youtube.com/watch?v=Bu_9XhXpDSs&t=2967s',
      'video_id': 'Bu_9XhXpDSs'},
     {'author': 'Ippei - Rank and Rent SEO',
      'channel': 'Ippei - Rank and Rent SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:50](https://www.youtube.com/watch?v=wU1OKeR3fvI&t=830s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s no shortage of business owners that you can literally just cold call all day "
              'long all across the country, all from different niches. I recently closed a '
              'deep tissue massage therapist in Illinois and that is like a brickandmortar '
              'business.',
      'timestamp': 830,
      'timestamp_label': '[00:13:50]',
      'timestamp_seconds': 830,
      'tip': "'s no shortage of business owners that you can literally just cold call all day "
             'long all across the country, all from different niches. I recently closed a deep '
             'tissue massage therapist in Illinois and that is like a brickandmortar business.',
      'title': 'Rank and Rent - Fastest Path to 10K Per month (Ippei - Rank and Rent SEO)',
      'url': 'https://www.youtube.com/watch?v=wU1OKeR3fvI&t=830s',
      'video_id': 'wU1OKeR3fvI'}],
 6: [{'author': 'Snovio',
      'channel': 'Snovio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:06](https://www.youtube.com/watch?v=MmWpOeG5GW4&t=306s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'There can be panic at first, but the solution is in your hands. Use the agency '
              "you're building to book yourself. Pick 200 prospects in your niche. Use Snovio "
              'to find their emails, send them an offer using multiple channels. It can be '
              'your first case study, by the way.',
      'timestamp': 306,
      'timestamp_label': '[00:05:06]',
      'timestamp_seconds': 306,
      'tip': 'There can be panic at first, but the solution is in your hands. Use the agency '
             "you're building to book yourself. Pick 200 prospects in your niche. Use Snovio "
             'to find their emails, send them an offer using multiple channels. It can be your '
             'first case study, by the way.',
      'title': 'Starting a Lead Generation Agency Is Easy in 2026! (Snovio)',
      'url': 'https://www.youtube.com/watch?v=MmWpOeG5GW4&t=306s',
      'video_id': 'MmWpOeG5GW4'},
     {'author': 'Software Scope',
      'channel': 'Software Scope',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:04](https://www.youtube.com/watch?v=00esG7HsVNs&t=124s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'AI personalization and smart adjust. So, it adjusts flows automatically based '
              'on how leads respond to avoid burning accounts. It has strong API and '
              'integrations. So it integrates for for example HubSpot, lead magic, outbound '
              'sync, clay and list kit.',
      'timestamp': 124,
      'timestamp_label': '[00:02:04]',
      'timestamp_seconds': 124,
      'tip': 'AI personalization and smart adjust. So, it adjusts flows automatically based on '
             'how leads respond to avoid burning accounts. It has strong API and integrations. '
             'So it integrates for for example HubSpot, lead magic, outbound sync, clay and '
             'list kit.',
      'title': 'Smartlead Vs Instantly (2026) | Which Cold Email Tool Is Better? (Software '
               'Scope)',
      'url': 'https://www.youtube.com/watch?v=00esG7HsVNs&t=124s',
      'video_id': '00esG7HsVNs'},
     {'author': 'The AI Ops Guy',
      'channel': 'The AI Ops Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=nRh4F859Xjo&t=80s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll use Clay to build a list of US companies that match our ideal customer "
              'profile, our ICP. Then we will use the topic intent signals to identify '
              'companies actively researching things like Salesforce consulting, CRM data, '
              'data quality, and lead routing automation.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': "'ll use Clay to build a list of US companies that match our ideal customer "
             'profile, our ICP. Then we will use the topic intent signals to identify '
             'companies actively researching things like Salesforce consulting, CRM data, data '
             'quality, and lead routing automation.',
      'title': 'How to Find High-Intent B2B Leads with Clay | Topic Intent + Claygent Tutorial '
               '(The AI Ops Guy)',
      'url': 'https://www.youtube.com/watch?v=nRh4F859Xjo&t=80s',
      'video_id': 'nRh4F859Xjo'},
     {'author': 'Agency Performance Partners',
      'channel': 'Agency Performance Partners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:34](https://www.youtube.com/watch?v=Y0_RWqy9tFM&t=154s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'People get grumpy cold calling, and outbound calls is a mindset. And if the '
              "phones aren't you're saying, changed up to drop-bys. Take that same list and "
              'just drop by saying hello. Meet people, but this is a huge way to benefit '
              'business.',
      'timestamp': 154,
      'timestamp_label': '[00:02:34]',
      'timestamp_seconds': 154,
      'tip': 'People get grumpy cold calling, and outbound calls is a mindset. And if the '
             "phones aren't you're saying, changed up to drop-bys. Take that same list and "
             'just drop by saying hello. Meet people, but this is a huge way to benefit '
             'business.',
      'title': 'Find Commercial Insurance Clients with These 10 Lead Generation Tactics '
               '(Agency Performance Partners)',
      'url': 'https://www.youtube.com/watch?v=Y0_RWqy9tFM&t=154s',
      'video_id': 'Y0_RWqy9tFM'},
     {'author': 'Smartlead',
      'channel': 'Smartlead',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=BRZJjgou7ic&t=120s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But then also we need to be thinking about the data quality as well, too. Most '
              'list building is can be based off of either LinkedIn data scraping or Google '
              'Maps scraping.',
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': 'But then also we need to be thinking about the data quality as well, too. Most '
             'list building is can be based off of either LinkedIn data scraping or Google '
             'Maps scraping.',
      'title': 'The BEST Way to Build Lead Lists for Cold Email in 2026 | Cold To Close : '
               'Episode 1 (Smartlead)',
      'url': 'https://www.youtube.com/watch?v=BRZJjgou7ic&t=120s',
      'video_id': 'BRZJjgou7ic'},
     {'author': 'Mark Colgan | Outbound & Pipeline for B2B SaaS',
      'channel': 'Mark Colgan | Outbound & Pipeline for B2B SaaS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:26](https://www.youtube.com/watch?v=N-15SMLSc3c&t=26s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s exactly what waterfall enrichment allows you to do. So in this particular "
              "example of finding a work email, what Clay is going to enable you to do is it's "
              "going to first try find email and then when it can't find the email on find "
              'email, it will move on to lead magic.',
      'timestamp': 26,
      'timestamp_label': '[00:00:26]',
      'timestamp_seconds': 26,
      'tip': "'s exactly what waterfall enrichment allows you to do. So in this particular "
             "example of finding a work email, what Clay is going to enable you to do is it's "
             "going to first try find email and then when it can't find the email on find "
             'email, it will move on to lead magic.',
      'title': 'What Does "Waterfall Enrichment" Even Mean?  (Clay.com For Non-Technical '
               'Users) (Mark Colgan | Outbound & Pipeline for B2B SaaS)',
      'url': 'https://www.youtube.com/watch?v=N-15SMLSc3c&t=26s',
      'video_id': 'N-15SMLSc3c'},
     {'author': 'Aimfox',
      'channel': 'Aimfox',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=O8VBEriCr60&t=108s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We can go ahead and go over to our campaigns and actually start our first '
              'campaign. Now the first you want to actually do here is to create our own lead '
              'list to figure out who we actually want to target for these campaigns.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': 'We can go ahead and go over to our campaigns and actually start our first '
             'campaign. Now the first you want to actually do here is to create our own lead '
             'list to figure out who we actually want to target for these campaigns.',
      'title': 'The LinkedIn DM System That Gets Paying Clients in 2026 (Full Tutorial) '
               '(Aimfox)',
      'url': 'https://www.youtube.com/watch?v=O8VBEriCr60&t=108s',
      'video_id': 'O8VBEriCr60'},
     {'author': 'Sales Feed',
      'channel': 'Sales Feed',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=Z9xzPDRrQHw&t=32s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Import build lead lists, enrich your leads with over 100 data providers. We've "
              'got a free trial here. I guess I will just do that. Uh, create your first table '
              'in clay.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': "Import build lead lists, enrich your leads with over 100 data providers. We've "
             'got a free trial here. I guess I will just do that. Uh, create your first table '
             'in clay.',
      'title': 'Did This AI Tool Just Change Sales Forever? (Clay AI Review) (Sales Feed)',
      'url': 'https://www.youtube.com/watch?v=Z9xzPDRrQHw&t=32s',
      'video_id': 'Z9xzPDRrQHw'},
     {'author': 'Matt Lucero',
      'channel': 'Matt Lucero',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[02:53:50](https://www.youtube.com/watch?v=_iGjRSCPXuA&t=10430s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is where you can add a global block list. You can also import CSV files if '
              'you want to do this in mass. You can also export the leads and I believe you '
              'can call this with an API as well in the API help docs.',
      'timestamp': 10430,
      'timestamp_label': '[02:53:50]',
      'timestamp_seconds': 10430,
      'tip': 'This is where you can add a global block list. You can also import CSV files if '
             'you want to do this in mass. You can also export the leads and I believe you can '
             'call this with an API as well in the API help docs.',
      'title': 'How To Use Smartlead.ai 2026 - Full Cold Email Tutorial (Matt Lucero)',
      'url': 'https://www.youtube.com/watch?v=_iGjRSCPXuA&t=10430s',
      'video_id': '_iGjRSCPXuA'},
     {'author': 'DatatoLeads - B2B and B2C Wholesale Data and Leads',
      'channel': 'DatatoLeads - B2B and B2C Wholesale Data and Leads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:58](https://www.youtube.com/watch?v=DrbAXLpA1wI&t=418s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Every lead has a cell phone so it's going to remove anything that has na where "
              "mobile one is so this indicates there's no cell phone when we flip that switch "
              'hit search.',
      'timestamp': 418,
      'timestamp_label': '[00:06:58]',
      'timestamp_seconds': 418,
      'tip': "Every lead has a cell phone so it's going to remove anything that has na where "
             "mobile one is so this indicates there's no cell phone when we flip that switch "
             'hit search.',
      'title': 'What is a Lead? TCPA Consent Guide to Opt in Leads - FCC Telemarketing Laws & '
               'Do Not Call List Rule (DatatoLeads - B2B and B2C Wholesale Data and Leads)',
      'url': 'https://www.youtube.com/watch?v=DrbAXLpA1wI&t=418s',
      'video_id': 'DrbAXLpA1wI'},
     {'author': 'Smartlead',
      'channel': 'Smartlead',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:12](https://www.youtube.com/watch?v=C2lkX09G4h4&t=672s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Finder let's click and reaching leads individually is fine when you need a few "
              'hundred but nobody is doing that 35,000 times. So this is a smart prospect the '
              'lead database built into Smart Lead and I will show you some filters you can '
              'make right here.',
      'timestamp': 672,
      'timestamp_label': '[00:11:12]',
      'timestamp_seconds': 672,
      'tip': "Finder let's click and reaching leads individually is fine when you need a few "
             'hundred but nobody is doing that 35,000 times. So this is a smart prospect the '
             'lead database built into Smart Lead and I will show you some filters you can '
             'make right here.',
      'title': "If I Wanted to Send 100,000 Cold Emails, I'd Do This (Tutorial) (Smartlead)",
      'url': 'https://www.youtube.com/watch?v=C2lkX09G4h4&t=672s',
      'video_id': 'C2lkX09G4h4'},
     {'author': 'Patrick Spychalski',
      'channel': 'Patrick Spychalski',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:07](https://www.youtube.com/watch?v=YLXzWpknuJk&t=787s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Example if I go to find people let's just say I want to find Founders and CEOs "
              "that are in New York um just to keep it simple so we'll go to job titles we "
              "type in founder and then we'll go CEO and then we'll scroll down to location "
              "and we'll put in New York.",
      'timestamp': 787,
      'timestamp_label': '[00:13:07]',
      'timestamp_seconds': 787,
      'tip': "Example if I go to find people let's just say I want to find Founders and CEOs "
             "that are in New York um just to keep it simple so we'll go to job titles we type "
             "in founder and then we'll go CEO and then we'll scroll down to location and "
             "we'll put in New York.",
      'title': 'How to Use Clay.com (1 Hour Tutorial) (Patrick Spychalski)',
      'url': 'https://www.youtube.com/watch?v=YLXzWpknuJk&t=787s',
      'video_id': 'YLXzWpknuJk'},
     {'author': 'Smartlead',
      'channel': 'Smartlead',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=GYd8Y73SCGE&t=139s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Boox and SMTP by mail Reef so uh let's look at the Journey of uh uh Google "
              "account we as soon as you're going to click on that you will be redirected to a "
              'domain name screen search for uh any domain name uh for now we can go ahead '
              'with smart lead.',
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': "Boox and SMTP by mail Reef so uh let's look at the Journey of uh uh Google "
             "account we as soon as you're going to click on that you will be redirected to a "
             'domain name screen search for uh any domain name uh for now we can go ahead with '
             'smart lead.',
      'title': 'SmartSenders Full Demo : Setting up Cold Email Infrastructure in Seconds '
               'within Smartlead (Smartlead)',
      'url': 'https://www.youtube.com/watch?v=GYd8Y73SCGE&t=139s',
      'video_id': 'GYd8Y73SCGE'},
     {'author': 'Vincent Robin',
      'channel': 'Vincent Robin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=7Sq3Ger8D3A&t=114s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And now what we want to do is to have a process to find leads that we can '
              'directly import in smart lead. If you want to find leads you can use Apollo '
              'Clay or you can use LinkedIn say navigator.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': 'And now what we want to do is to have a process to find leads that we can '
             'directly import in smart lead. If you want to find leads you can use Apollo Clay '
             'or you can use LinkedIn say navigator.',
      'title': 'How To Setup Your Smartlead.ai Cold Email Campaign (Vincent Robin)',
      'url': 'https://www.youtube.com/watch?v=7Sq3Ger8D3A&t=114s',
      'video_id': '7Sq3Ger8D3A'},
     {'author': 'Xavier Caffrey GTM',
      'channel': 'Xavier Caffrey GTM',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:53](https://www.youtube.com/watch?v=UpSWlkeuUqs&t=473s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's it's using a bunch of data providers to find the phone number of these "
              'leads. So, now you can empower your team to reach out via a cold email uh via '
              'LinkedIn and phone number as well. Now, chapter three is we have the '
              'information.',
      'timestamp': 473,
      'timestamp_label': '[00:07:53]',
      'timestamp_seconds': 473,
      'tip': "It's it's using a bunch of data providers to find the phone number of these "
             'leads. So, now you can empower your team to reach out via a cold email uh via '
             'LinkedIn and phone number as well. Now, chapter three is we have the '
             'information.',
      'title': 'The Fastest Way To Get B2B Clients In 2025 [Clay.com Tutorial] (Xavier Caffrey '
               'GTM)',
      'url': 'https://www.youtube.com/watch?v=UpSWlkeuUqs&t=473s',
      'video_id': 'UpSWlkeuUqs'}],
 7: [{'author': 'Michael Nadalin | Google Ads & Paid Ads Lead Gen',
      'channel': 'Michael Nadalin | Google Ads & Paid Ads Lead Gen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:23](https://www.youtube.com/watch?v=g88QMH5r_8M&t=143s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Can they actually purchase or invest in this case? And then when are they '
              'actually looking to do it? Now, so many times with advertising campaigns is you '
              "could do the first step, get 100 leads a month, and then you wouldn't even know "
              'the quality of the leads.',
      'timestamp': 143,
      'timestamp_label': '[00:02:23]',
      'timestamp_seconds': 143,
      'tip': 'Can they actually purchase or invest in this case? And then when are they '
             'actually looking to do it? Now, so many times with advertising campaigns is you '
             "could do the first step, get 100 leads a month, and then you wouldn't even know "
             'the quality of the leads.',
      'title': 'How To Get High Ticket/B2B Leads with Ads & Reduce Cost Per Lead (With 3 REAL '
               'Examples) (Michael Nadalin | Google Ads & Paid Ads Lead Gen)',
      'url': 'https://www.youtube.com/watch?v=g88QMH5r_8M&t=143s',
      'video_id': 'g88QMH5r_8M'},
     {'author': 'LeadLoft',
      'channel': 'LeadLoft',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=bAri9HF705I&t=102s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Of course you can see there's bounce shield which can verify emails that are "
              "unverifiable or catch all emails. And of course, there's email steps. And if "
              'you want to run cold calling, you can run that as well.',
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': "Of course you can see there's bounce shield which can verify emails that are "
             "unverifiable or catch all emails. And of course, there's email steps. And if you "
             'want to run cold calling, you can run that as well.',
      'title': 'How to Scrape LinkedIn Sales Navigator? Sales Navigator Scraper (Guide) '
               '(LeadLoft)',
      'url': 'https://www.youtube.com/watch?v=bAri9HF705I&t=102s',
      'video_id': 'bAri9HF705I'},
     {'author': 'Marcus Chan',
      'channel': 'Marcus Chan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=HL8AeTPufLU&t=21s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm going to show you my exact workflow. The same system I've used to generate "
              'millions of pipeline using sales navigator, Apollo, and chat GPT. This is the '
              'actual step-by-step process I use every single week along with my team.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "I'm going to show you my exact workflow. The same system I've used to generate "
             'millions of pipeline using sales navigator, Apollo, and chat GPT. This is the '
             'actual step-by-step process I use every single week along with my team.',
      'title': 'UPDATED 2026: LinkedIn Sales Navigator Lead Gen with AI & Apollo '
               '(Step-by-Step) (Marcus Chan)',
      'url': 'https://www.youtube.com/watch?v=HL8AeTPufLU&t=21s',
      'video_id': 'HL8AeTPufLU'},
     {'author': 'Jakub Jablonsky',
      'channel': 'Jakub Jablonsky',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:08](https://www.youtube.com/watch?v=SygbkYDB3iM&t=488s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'AI over text which is not ideal. There will a lot of drop off but there are a '
              'lot of options that can be implemented. Now that you understand what type of '
              "buyers you want to work with, let's talk about the second part which is "
              'building a system to generate quality leads.',
      'timestamp': 488,
      'timestamp_label': '[00:08:08]',
      'timestamp_seconds': 488,
      'tip': 'AI over text which is not ideal. There will a lot of drop off but there are a '
             'lot of options that can be implemented. Now that you understand what type of '
             "buyers you want to work with, let's talk about the second part which is building "
             'a system to generate quality leads.',
      'title': 'How to make $500,000 per month with a lead generation business (Step-by-Step) '
               '(Jakub Jablonsky)',
      'url': 'https://www.youtube.com/watch?v=SygbkYDB3iM&t=488s',
      'video_id': 'SygbkYDB3iM'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:38:22](https://www.youtube.com/watch?v=DSbDVWpyXUI&t=2302s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then to process those call center verification leads uploaded too you can see '
              'here this lead went unmatched this lead went unmatched due to a delivery '
              'failure these leads are held in manual review meaning.',
      'timestamp': 2302,
      'timestamp_label': '[00:38:22]',
      'timestamp_seconds': 2302,
      'tip': 'Then to process those call center verification leads uploaded too you can see '
             'here this lead went unmatched this lead went unmatched due to a delivery failure '
             'these leads are held in manual review meaning.',
      'title': 'boberdoo.com Overview Demo With Ping Post | Lead Software (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=DSbDVWpyXUI&t=2302s',
      'video_id': 'DSbDVWpyXUI'},
     {'author': 'Local View',
      'channel': 'Local View',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:29](https://www.youtube.com/watch?v=bzWbX2kyAhg&t=149s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The second thing that can help you rank higher is rating your leads. When you '
              'mark leads as booked, completed, or not relevant, it helps Google system learn '
              'what kind of leads are good for your business.',
      'timestamp': 149,
      'timestamp_label': '[00:02:29]',
      'timestamp_seconds': 149,
      'tip': 'The second thing that can help you rank higher is rating your leads. When you '
             'mark leads as booked, completed, or not relevant, it helps Google system learn '
             'what kind of leads are good for your business.',
      'title': "How To Rank Higher On Google's Local Services Ads - Local View (Local View)",
      'url': 'https://www.youtube.com/watch?v=bzWbX2kyAhg&t=149s',
      'video_id': 'bzWbX2kyAhg'},
     {'author': 'Harry Long',
      'channel': 'Harry Long',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=DgzklijTLzE&t=38s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, it's just five simple steps to get your LinkedIn automated DM campaign out "
              'there and live. But before I get into that five-step system, I want to quickly '
              "show you what's the outcome is, what you're going to have at the end of this "
              'video.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': "Now, it's just five simple steps to get your LinkedIn automated DM campaign out "
             'there and live. But before I get into that five-step system, I want to quickly '
             "show you what's the outcome is, what you're going to have at the end of this "
             'video.',
      'title': 'How I Automate My LinkedIn DM Outreach (Step By Step) (Harry Long)',
      'url': 'https://www.youtube.com/watch?v=DgzklijTLzE&t=38s',
      'video_id': 'DgzklijTLzE'},
     {'author': 'PushLeads',
      'channel': 'PushLeads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:39](https://www.youtube.com/watch?v=vWdPlgxdJUA&t=399s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Step four is building a review system that generates content, not just stars. '
              "Send your review requests within 24 hours of job completion. The customer's "
              'experience is clearest right after the job ends. Give them one sentence of '
              'guidance.',
      'timestamp': 399,
      'timestamp_label': '[00:06:39]',
      'timestamp_seconds': 399,
      'tip': 'Step four is building a review system that generates content, not just stars. '
             "Send your review requests within 24 hours of job completion. The customer's "
             'experience is clearest right after the job ends. Give them one sentence of '
             'guidance.',
      'title': 'How do contractors optimize Google Business Profile for better leads? '
               '(PushLeads)',
      'url': 'https://www.youtube.com/watch?v=vWdPlgxdJUA&t=399s',
      'video_id': 'vWdPlgxdJUA'},
     {'author': 'Matt Harriman',
      'channel': 'Matt Harriman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=hm5isqC1d74&t=146s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But, let's just for this case, we'll just go to the owner, right? So, CEO, "
              'owner, founder, managing partner, managing director. Geography is United '
              "States, industry staffing recruiting. And there's another step that I usually "
              'go through called Clay, right?',
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': "But, let's just for this case, we'll just go to the owner, right? So, CEO, "
             'owner, founder, managing partner, managing director. Geography is United States, '
             "industry staffing recruiting. And there's another step that I usually go through "
             'called Clay, right?',
      'title': 'The LinkedIn Outbound System That Actually Books Meetings (2026) (Matt '
               'Harriman)',
      'url': 'https://www.youtube.com/watch?v=hm5isqC1d74&t=146s',
      'video_id': 'hm5isqC1d74'},
     {'author': 'Surfside PPC',
      'channel': 'Surfside PPC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:46](https://www.youtube.com/watch?v=Eg42cdAsCqw&t=106s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um we have our hours and then any additional information here. So, that's going "
              'to be your first step always is fill all this information out and then from '
              "there it's like, okay, how do we know we're doing everything we can to rank our "
              'Google Business Profile high?',
      'timestamp': 106,
      'timestamp_label': '[00:01:46]',
      'timestamp_seconds': 106,
      'tip': "Um we have our hours and then any additional information here. So, that's going "
             'to be your first step always is fill all this information out and then from '
             "there it's like, okay, how do we know we're doing everything we can to rank our "
             'Google Business Profile high?',
      'title': 'Local SEO Google Business Profile Best Practices 2026 (Surfside PPC)',
      'url': 'https://www.youtube.com/watch?v=Eg42cdAsCqw&t=106s',
      'video_id': 'Eg42cdAsCqw'},
     {'author': 'LeadCaptureIO',
      'channel': 'LeadCaptureIO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:30](https://www.youtube.com/watch?v=4hypirM3lEg&t=870s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Setting up the template and then also posting it into your system with the web '
              "hook now the next thing that I'll show you let me move this to the bottom real.",
      'timestamp': 870,
      'timestamp_label': '[00:14:30]',
      'timestamp_seconds': 870,
      'tip': 'Setting up the template and then also posting it into your system with the web '
             "hook now the next thing that I'll show you let me move this to the bottom real.",
      'title': 'TCPA 1:1 Consent Made Simple With LeadCapture.io TCPA Templates, Tagging, and '
               'Compliance Workflow (LeadCaptureIO)',
      'url': 'https://www.youtube.com/watch?v=4hypirM3lEg&t=870s',
      'video_id': '4hypirM3lEg'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:07](https://www.youtube.com/watch?v=CLgSYIHZ_GY&t=127s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Simply copy and paste the text and send it as a text document or a PDF and that '
              'way you can modify it to include their unique credentials thanks for watching '
              'the next video will walk you through adding a new partner into your system.',
      'timestamp': 127,
      'timestamp_label': '[00:02:07]',
      'timestamp_seconds': 127,
      'tip': 'Simply copy and paste the text and send it as a text document or a PDF and that '
             'way you can modify it to include their unique credentials thanks for watching '
             'the next video will walk you through adding a new partner into your system.',
      'title': 'How To Ping Post Specifications | boberdoo Ping Post Software (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=CLgSYIHZ_GY&t=127s',
      'video_id': 'CLgSYIHZ_GY'},
     {'author': 'Stewart Gauld',
      'channel': 'Stewart Gauld',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:58](https://www.youtube.com/watch?v=fsZaEce18FE&t=358s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That I've added down in the description now it's important that we do need to "
              'change some of this content so over here next to mail 2 we want to add your '
              'email so my email is stewart cindyo.co.nz.',
      'timestamp': 358,
      'timestamp_label': '[00:05:58]',
      'timestamp_seconds': 358,
      'tip': "That I've added down in the description now it's important that we do need to "
             'change some of this content so over here next to mail 2 we want to add your '
             'email so my email is stewart cindyo.co.nz.',
      'title': 'How To Set Up Google Workspace SPF, DKIM & DMARC | Improve Email '
               'Deliverability (Stewart Gauld)',
      'url': 'https://www.youtube.com/watch?v=fsZaEce18FE&t=358s',
      'video_id': 'fsZaEce18FE'},
     {'author': 'Ruben Frederic',
      'channel': 'Ruben Frederic',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:50](https://www.youtube.com/watch?v=B6M6968u10c&t=1250s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So if you're able to sell on appointments or on a package, you can act like EPL "
              "might it's very it's very arguably close to pay per appointment in quality "
              'trend and all that stuff. The only thing is that with pay per appointment very '
              'easy to close.',
      'timestamp': 1250,
      'timestamp_label': '[00:20:50]',
      'timestamp_seconds': 1250,
      'tip': "So if you're able to sell on appointments or on a package, you can act like EPL "
             "might it's very it's very arguably close to pay per appointment in quality trend "
             'and all that stuff. The only thing is that with pay per appointment very easy to '
             'close.',
      'title': 'Pay Per Lead vs Pay Per Appointment for Lead Gen Agency (Ruben Frederic)',
      'url': 'https://www.youtube.com/watch?v=B6M6968u10c&t=1250s',
      'video_id': 'B6M6968u10c'},
     {'author': 'Brayden Bass',
      'channel': 'Brayden Bass',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:38](https://www.youtube.com/watch?v=QnqQKoCeYa8&t=518s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Your follow up turns that into booked jobs. Now you're pushing leads into a "
              'system that converts them. Paid ads without the first four steps are just a '
              'fast way to lose money.',
      'timestamp': 518,
      'timestamp_label': '[00:08:38]',
      'timestamp_seconds': 518,
      'tip': "Your follow up turns that into booked jobs. Now you're pushing leads into a "
             'system that converts them. Paid ads without the first four steps are just a fast '
             'way to lose money.',
      'title': 'How to Get Local Service Leads in 2026 (Without Buying Shared Leads) (Brayden '
               'Bass)',
      'url': 'https://www.youtube.com/watch?v=QnqQKoCeYa8&t=518s',
      'video_id': 'QnqQKoCeYa8'}],
 8: [{'author': 'Ippei - Rank and Rent SEO',
      'channel': 'Ippei - Rank and Rent SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:18](https://www.youtube.com/watch?v=JuyXW9x-QMs&t=318s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And my call tracking can API connect to a CRM Go High Level. At that point, '
              "you've now just created an automated commission deal where you just have to "
              "focus on what you're good at, which is just generating more and more leads, "
              'building more of these rank and rent sites.',
      'timestamp': 318,
      'timestamp_label': '[00:05:18]',
      'timestamp_seconds': 318,
      'tip': 'And my call tracking can API connect to a CRM Go High Level. At that point, '
             "you've now just created an automated commission deal where you just have to "
             "focus on what you're good at, which is just generating more and more leads, "
             'building more of these rank and rent sites.',
      'title': '6 ways to monetize Rank and Rent Websites (Ippei - Rank and Rent SEO)',
      'url': 'https://www.youtube.com/watch?v=JuyXW9x-QMs&t=318s',
      'video_id': 'JuyXW9x-QMs'},
     {'author': 'Alex Vacca',
      'channel': 'Alex Vacca',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=Ouq5ayjDmmI&t=60s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But first, let me explain how API works so you understand the foundation before '
              'we get into the specific workflows. API is a platform with pre-built scrapers. '
              'They call each scraper an actor. Think of it like an app store, but for data '
              'extraction tools.',
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': 'But first, let me explain how API works so you understand the foundation before '
             'we get into the specific workflows. API is a platform with pre-built scrapers. '
             'They call each scraper an actor. Think of it like an app store, but for data '
             'extraction tools.',
      'title': 'Apify Tutorial | How to Scrape Leads 2026 (Alex Vacca)',
      'url': 'https://www.youtube.com/watch?v=Ouq5ayjDmmI&t=60s',
      'video_id': 'Ouq5ayjDmmI'},
     {'author': 'Xavier Caffrey GTM',
      'channel': 'Xavier Caffrey GTM',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:48](https://www.youtube.com/watch?v=kY5E4wl8wlA&t=1728s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, let me search LinkedIn LinkedIn profile. So, for this case, I'm just going "
              "to use Clay's credit system to run this just to show you. But again, if you "
              'click on account, if you click on account, you can add your own API key.',
      'timestamp': 1728,
      'timestamp_label': '[00:28:48]',
      'timestamp_seconds': 1728,
      'tip': "So, let me search LinkedIn LinkedIn profile. So, for this case, I'm just going "
             "to use Clay's credit system to run this just to show you. But again, if you "
             'click on account, if you click on account, you can add your own API key.',
      'title': 'The ONLY Clay Tutorial You Need in 2025 (For Beginners) (Xavier Caffrey GTM)',
      'url': 'https://www.youtube.com/watch?v=kY5E4wl8wlA&t=1728s',
      'video_id': 'kY5E4wl8wlA'},
     {'author': 'Will Butler',
      'channel': 'Will Butler',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:57](https://www.youtube.com/watch?v=FJ2CA-mGueY&t=357s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Apify, through Clay or another enrichment tool to actually find the contact '
              "information such as the emails and phone numbers, but I'm going to go ahead and "
              'turn on the business leads enrichment uh just so you can see how it all works '
              'inside of Apify.',
      'timestamp': 357,
      'timestamp_label': '[00:05:57]',
      'timestamp_seconds': 357,
      'tip': 'Apify, through Clay or another enrichment tool to actually find the contact '
             "information such as the emails and phone numbers, but I'm going to go ahead and "
             'turn on the business leads enrichment uh just so you can see how it all works '
             'inside of Apify.',
      'title': 'Apollo & ZoomInfo Are Missing These B2B Leads (Here’s How to Find Them) (Will '
               'Butler)',
      'url': 'https://www.youtube.com/watch?v=FJ2CA-mGueY&t=357s',
      'video_id': 'FJ2CA-mGueY'},
     {'author': 'Sales Feed',
      'channel': 'Sales Feed',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:01](https://www.youtube.com/watch?v=nWnc3cZ1nFs&t=61s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'CRM, a trade show attendee list, Google Maps, Google, LinkedIn, wherever it may '
              'be. You can then add to that data and manipulate it in any way you want. So, '
              'you can use AI, publicly available information, and third party tools to enrich '
              'the data.',
      'timestamp': 61,
      'timestamp_label': '[00:01:01]',
      'timestamp_seconds': 61,
      'tip': 'CRM, a trade show attendee list, Google Maps, Google, LinkedIn, wherever it may '
             'be. You can then add to that data and manipulate it in any way you want. So, you '
             'can use AI, publicly available information, and third party tools to enrich the '
             'data.',
      'title': "I Tried Clay AI for 9 Months, Here’s What I Learned (Beginner's Guide) (Sales "
               'Feed)',
      'url': 'https://www.youtube.com/watch?v=nWnc3cZ1nFs&t=61s',
      'video_id': 'nWnc3cZ1nFs'},
     {'author': 'HeyReach',
      'channel': 'HeyReach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:37](https://www.youtube.com/watch?v=3o3gecljGlE&t=37s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can go for LinkedIn free search. You also have LinkedIn groups, events, '
              'posts, importing CSVs, whatever you prefer. If you want to integrate Hage with '
              'Clay, RB2B, Trigify, your Hopspot CRM, we have a lot of native integrations '
              'that are available to you if you click here.',
      'timestamp': 37,
      'timestamp_label': '[00:00:37]',
      'timestamp_seconds': 37,
      'tip': 'You can go for LinkedIn free search. You also have LinkedIn groups, events, '
             'posts, importing CSVs, whatever you prefer. If you want to integrate Hage with '
             'Clay, RB2B, Trigify, your Hopspot CRM, we have a lot of native integrations that '
             'are available to you if you click here.',
      'title': '10x Your LinkedIn Outbound With HeyReach [Demo Video] (HeyReach)',
      'url': 'https://www.youtube.com/watch?v=3o3gecljGlE&t=37s',
      'video_id': '3o3gecljGlE'},
     {'author': 'Coldbot',
      'channel': 'Coldbot',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:19](https://www.youtube.com/watch?v=fM-ywBq8yoU&t=199s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Warmup tools simulate engagement patterns inside their networks, but warmup is '
              'not a force field. A warmed inbox can still be damaged by bad data, complaints, '
              'sudden volume spikes or terrible sending behavior. And there is no magic number '
              'of days that guarantees safety.',
      'timestamp': 199,
      'timestamp_label': '[00:03:19]',
      'timestamp_seconds': 199,
      'tip': 'Warmup tools simulate engagement patterns inside their networks, but warmup is '
             'not a force field. A warmed inbox can still be damaged by bad data, complaints, '
             'sudden volume spikes or terrible sending behavior. And there is no magic number '
             'of days that guarantees safety.',
      'title': 'Cold Email Infrastructure 2026: Domains, DNS, Mailboxes & Warmup (Coldbot)',
      'url': 'https://www.youtube.com/watch?v=fM-ywBq8yoU&t=199s',
      'video_id': 'fM-ywBq8yoU'},
     {'author': 'Mac Creator Workflow',
      'channel': 'Mac Creator Workflow',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=kRxM5oUoNno&t=21s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'AI to write the perfect cold email sequence to convert them into paying '
              'clients. First, we need to extract our targets. Open the Chrome Web Store and '
              'download a free extension called Instant Data Scraper. Next, head over to '
              'Google Maps.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'AI to write the perfect cold email sequence to convert them into paying clients. '
             'First, we need to extract our targets. Open the Chrome Web Store and download a '
             'free extension called Instant Data Scraper. Next, head over to Google Maps.',
      'title': 'How to Scrape 1,000+ B2B Leads for FREE (Google Maps + AI Hack) (Mac Creator '
               'Workflow)',
      'url': 'https://www.youtube.com/watch?v=kRxM5oUoNno&t=21s',
      'video_id': 'kRxM5oUoNno'},
     {'author': 'Smartlead',
      'channel': 'Smartlead',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[02:39:21](https://www.youtube.com/watch?v=J8lvEnIHcLk&t=9561s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um you can take all of these and throw it in there and that way for you less '
              'technical folk, you can get something done with this. But in any case, this is '
              'where you can find all the many many many different API endpoints inside of '
              'Smart Lead.',
      'timestamp': 9561,
      'timestamp_label': '[02:39:21]',
      'timestamp_seconds': 9561,
      'tip': 'Um you can take all of these and throw it in there and that way for you less '
             'technical folk, you can get something done with this. But in any case, this is '
             'where you can find all the many many many different API endpoints inside of '
             'Smart Lead.',
      'title': 'Full Smartlead.ai Tutorial 2026 (Best Cold Email Software) (Smartlead)',
      'url': 'https://www.youtube.com/watch?v=J8lvEnIHcLk&t=9561s',
      'video_id': 'J8lvEnIHcLk'},
     {'author': 'SalesBlink',
      'channel': 'SalesBlink',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:16](https://www.youtube.com/watch?v=8sprCYGSnpI&t=76s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Back in Google, click Start authentication. Using Microsoft 365 or Outlook? '
              'Pick it under Steps shown for, and the steps change to match. Your SPF value '
              'now includes spf. And for DKIM, the steps point to the Microsoft Defender '
              'portal, not the Google Admin console.',
      'timestamp': 76,
      'timestamp_label': '[00:01:16]',
      'timestamp_seconds': 76,
      'tip': 'Back in Google, click Start authentication. Using Microsoft 365 or Outlook? Pick '
             'it under Steps shown for, and the steps change to match. Your SPF value now '
             'includes spf. And for DKIM, the steps point to the Microsoft Defender portal, '
             'not the Google Admin console.',
      'title': 'SPF, DKIM and DMARC Setup for Cold Email (Google Workspace & Microsoft 365) | '
               'SalesBlink (SalesBlink)',
      'url': 'https://www.youtube.com/watch?v=8sprCYGSnpI&t=76s',
      'video_id': '8sprCYGSnpI'},
     {'author': 'B2B Hero',
      'channel': 'B2B Hero',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:28](https://www.youtube.com/watch?v=qbyg7plwqnM&t=688s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Shouldn't ignore so if you found that useful check out some other videos I have "
              'which should be popping up right now about cold email and some cody mochi '
              'tools.',
      'timestamp': 688,
      'timestamp_label': '[00:11:28]',
      'timestamp_seconds': 688,
      'tip': "Shouldn't ignore so if you found that useful check out some other videos I have "
             'which should be popping up right now about cold email and some cody mochi tools.',
      'title': 'Is Cold Email Illegal (GDPR Explained) (B2B Hero)',
      'url': 'https://www.youtube.com/watch?v=qbyg7plwqnM&t=688s',
      'video_id': 'qbyg7plwqnM'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=o5v8ME_4M_M&t=134s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Commonly used in Home Improvement auto finance and all kinds of insurance but '
              'it can easily work with anywhere to go thanks for watching and remember to '
              'check out our ping post pages to see how you can benefit from utilizing a Baro '
              'ping post solution.',
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': 'Commonly used in Home Improvement auto finance and all kinds of insurance but it '
             'can easily work with anywhere to go thanks for watching and remember to check '
             'out our ping post pages to see how you can benefit from utilizing a Baro ping '
             'post solution.',
      'title': 'How To Ping Post Basics | boberdoo Lead Distribution Software (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=o5v8ME_4M_M&t=134s',
      'video_id': 'o5v8ME_4M_M'},
     {'author': 'LeadCaptureIO',
      'channel': 'LeadCaptureIO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:24](https://www.youtube.com/watch?v=Hd19AToxex4&t=384s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The whole idea is this, that the lead is willing to click the little box before '
              "they hit submit, then they're going to be more likely to pick up the phone.",
      'timestamp': 384,
      'timestamp_label': '[00:06:24]',
      'timestamp_seconds': 384,
      'tip': 'The whole idea is this, that the lead is willing to click the little box before '
             "they hit submit, then they're going to be more likely to pick up the phone.",
      'title': 'Why Lead Sellers Shouldn’t Fear TCPA Compliance (It’s a Competitive Advantage) '
               '(LeadCaptureIO)',
      'url': 'https://www.youtube.com/watch?v=Hd19AToxex4&t=384s',
      'video_id': 'Hd19AToxex4'},
     {'author': 'AJ Cassata',
      'channel': 'AJ Cassata',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:54](https://www.youtube.com/watch?v=6l8CThrSJEY&t=774s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "API key and then in that case, you won't spend any Clay credits. You can use "
              "the cheaper Clay plans. Uh, and then you're just basically pinging your credits "
              "from these tools that you're already using, right?",
      'timestamp': 774,
      'timestamp_label': '[00:12:54]',
      'timestamp_seconds': 774,
      'tip': "API key and then in that case, you won't spend any Clay credits. You can use the "
             "cheaper Clay plans. Uh, and then you're just basically pinging your credits from "
             "these tools that you're already using, right?",
      'title': 'How to Get Unlimited Leads Using Clay Enrichment Waterfall | clay.com Tutorial '
               '(AJ Cassata)',
      'url': 'https://www.youtube.com/watch?v=6l8CThrSJEY&t=774s',
      'video_id': '6l8CThrSJEY'},
     {'author': 'The AI Ops Guy',
      'channel': 'The AI Ops Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:08](https://www.youtube.com/watch?v=nRh4F859Xjo&t=1028s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'AI to to more data to search for in in the person like the title may be not '
              'sufficient but you can actually add a summary over here uh and that will give '
              'AI to do more research on the person. So basically you can create another '
              'client to research a person.',
      'timestamp': 1028,
      'timestamp_label': '[00:17:08]',
      'timestamp_seconds': 1028,
      'tip': 'AI to to more data to search for in in the person like the title may be not '
             'sufficient but you can actually add a summary over here uh and that will give AI '
             'to do more research on the person. So basically you can create another client to '
             'research a person.',
      'title': 'How to Find High-Intent B2B Leads with Clay | Topic Intent + Claygent Tutorial '
               '(The AI Ops Guy)',
      'url': 'https://www.youtube.com/watch?v=nRh4F859Xjo&t=1028s',
      'video_id': 'nRh4F859Xjo'}],
 9: [{'author': 'Misar AI',
      'channel': 'Misar AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=_bfiWvgegAM&t=54s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, if consent isn't the go-to for cold outreach, why do most B2B marketers "
              'lean on legitimate interest instead? How does that actually work under GDPR? '
              "Because the prospect hasn't opted in, you can't rely on consent.",
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': "So, if consent isn't the go-to for cold outreach, why do most B2B marketers lean "
             'on legitimate interest instead? How does that actually work under GDPR? Because '
             "the prospect hasn't opted in, you can't rely on consent.",
      'title': 'Is Cold Email Legal Under GDPR? A 2026 Compliance Guide for B2B Sales Teams '
               '(Misar AI)',
      'url': 'https://www.youtube.com/watch?v=_bfiWvgegAM&t=54s',
      'video_id': '_bfiWvgegAM'},
     {'author': 'mailmark',
      'channel': 'mailmark',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:01](https://www.youtube.com/watch?v=hpYC1CZASG4&t=61s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Implied consent can apply when someone publishes their business address and '
              'your email relates to their role. Again, these summaries leave out details that '
              'matter. Check the rules for each country you email and get proper advice if you '
              'are unsure.',
      'timestamp': 61,
      'timestamp_label': '[00:01:01]',
      'timestamp_seconds': 61,
      'tip': 'Implied consent can apply when someone publishes their business address and your '
             'email relates to their role. Again, these summaries leave out details that '
             'matter. Check the rules for each country you email and get proper advice if you '
             'are unsure.',
      'title': 'Is Cold Email Legal? CAN-SPAM, GDPR and CASL for B2B Outreach (mailmark)',
      'url': 'https://www.youtube.com/watch?v=hpYC1CZASG4&t=61s',
      'video_id': 'hpYC1CZASG4'},
     {'author': 'Harry Latos',
      'channel': 'Harry Latos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:00](https://www.youtube.com/watch?v=z85zvw9drj8&t=660s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You basically want to find signals that indicate this company would benefit '
              'from your service. Once again, we use tools like these, Deep Line, Clay, Cold '
              'IQ to do this. Then you can create outreach which is substantially more '
              'heavy-hitting, right?',
      'timestamp': 660,
      'timestamp_label': '[00:11:00]',
      'timestamp_seconds': 660,
      'tip': 'You basically want to find signals that indicate this company would benefit from '
             'your service. Once again, we use tools like these, Deep Line, Clay, Cold IQ to '
             'do this. Then you can create outreach which is substantially more heavy-hitting, '
             'right?',
      'title': 'B2B Lead Generation: How to Win More Clients in 2026 (Harry Latos)',
      'url': 'https://www.youtube.com/watch?v=z85zvw9drj8&t=660s',
      'video_id': 'z85zvw9drj8'},
     {'author': 'Kyle Banks',
      'channel': 'Kyle Banks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:07](https://www.youtube.com/watch?v=VnnBAIAnf54&t=1027s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And that is super important. And so, this is a very pivotal case here in terms '
              "of the wording, a business holding it up to the public and I'll show you some "
              'more examples of that as well.',
      'timestamp': 1027,
      'timestamp_label': '[00:17:07]',
      'timestamp_seconds': 1027,
      'tip': 'And that is super important. And so, this is a very pivotal case here in terms '
             "of the wording, a business holding it up to the public and I'll show you some "
             'more examples of that as well.',
      'title': 'Is B2B Cold Texting Legal? Every Law & Court Case Explained (1991–2026) (Kyle '
               'Banks)',
      'url': 'https://www.youtube.com/watch?v=VnnBAIAnf54&t=1027s',
      'video_id': 'VnnBAIAnf54'},
     {'author': 'lemlist',
      'channel': 'lemlist',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=-LtGmHnpioI&t=118s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Is it dangerous to run LinkedIn outreach automation? According to LinkedIn's "
              'terms of service, using bots or automation to script data or send messages is '
              "not allowed. Most LinkedIn tools are tolerated as long as they don't mess up "
              'the user experience.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': "Is it dangerous to run LinkedIn outreach automation? According to LinkedIn's "
             'terms of service, using bots or automation to script data or send messages is '
             "not allowed. Most LinkedIn tools are tolerated as long as they don't mess up the "
             'user experience.',
      'title': 'The Only LinkedIn Outreach Video You Will Ever Need (lemlist)',
      'url': 'https://www.youtube.com/watch?v=-LtGmHnpioI&t=118s',
      'video_id': '-LtGmHnpioI'},
     {'author': 'TechSales',
      'channel': 'TechSales',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:05](https://www.youtube.com/watch?v=aa7B2gisZdU&t=545s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'On top of that, each country has its own rules for marketing email under the '
              'e-privacy rules, and they differ for business addresses. Some countries allow '
              'cold email to companies with an easy opt-out. Others, like Germany, are much '
              'stricter.',
      'timestamp': 545,
      'timestamp_label': '[00:09:05]',
      'timestamp_seconds': 545,
      'tip': 'On top of that, each country has its own rules for marketing email under the '
             'e-privacy rules, and they differ for business addresses. Some countries allow '
             'cold email to companies with an easy opt-out. Others, like Germany, are much '
             'stricter.',
      'title': 'Cold Email Infrastructure: Domains, SPF, DKIM, DMARC and Warm Up | Cold '
               'Outreach Academy 03 (TechSales)',
      'url': 'https://www.youtube.com/watch?v=aa7B2gisZdU&t=545s',
      'video_id': 'aa7B2gisZdU'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:46](https://www.youtube.com/watch?v=Dktb23hf-d8&t=166s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Restricted to us calls there are also several switches from duration and buffer '
              'to geo segmentation which you can use to customize what calls the client can '
              'receive we can also do custom ivrs and you can build your own phone campaigns '
              'for further routing options.',
      'timestamp': 166,
      'timestamp_label': '[00:02:46]',
      'timestamp_seconds': 166,
      'tip': 'Restricted to us calls there are also several switches from duration and buffer '
             'to geo segmentation which you can use to customize what calls the client can '
             'receive we can also do custom ivrs and you can build your own phone campaigns '
             'for further routing options.',
      'title': 'Demo Part 3 Distributing Leads | boberdoo Lead Distribution Software '
               '(boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=Dktb23hf-d8&t=166s',
      'video_id': 'Dktb23hf-d8'},
     {'author': 'Smartlead',
      'channel': 'Smartlead',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:55](https://www.youtube.com/watch?v=GZEdhosrYRc&t=295s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I mean by that is, let's say your main domain is coca-cola. In that case, by "
              'sending cold outreach from any mailboxes, any inboxes that are at coca-cola.',
      'timestamp': 295,
      'timestamp_label': '[00:04:55]',
      'timestamp_seconds': 295,
      'tip': "I mean by that is, let's say your main domain is coca-cola. In that case, by "
             'sending cold outreach from any mailboxes, any inboxes that are at coca-cola.',
      'title': 'The New Rules of Cold Email Deliverability in 2026 (Smartlead)',
      'url': 'https://www.youtube.com/watch?v=GZEdhosrYRc&t=295s',
      'video_id': 'GZEdhosrYRc'},
     {'author': 'Namit Jindal | Aerosend',
      'channel': 'Namit Jindal | Aerosend',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:23](https://www.youtube.com/watch?v=OhSoUY7K_dU&t=443s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "People are more likely to sue you but I'm not really sure I don't have hard "
              'data on that and yeah let me know if you guys have any other questions happy '
              'cold emailing and for legal reasons this is not any legal advice purely meant '
              'for informational purposes or parity.',
      'timestamp': 443,
      'timestamp_label': '[00:07:23]',
      'timestamp_seconds': 443,
      'tip': "People are more likely to sue you but I'm not really sure I don't have hard data "
             'on that and yeah let me know if you guys have any other questions happy cold '
             'emailing and for legal reasons this is not any legal advice purely meant for '
             'informational purposes or parity.',
      'title': 'CAN-SPAM Act Cold Email Rules: Can You Actually Go to Jail? (Namit Jindal | '
               'Aerosend)',
      'url': 'https://www.youtube.com/watch?v=OhSoUY7K_dU&t=443s',
      'video_id': 'OhSoUY7K_dU'},
     {'author': 'Cleverly | #1 B2B Lead Generation Agency',
      'channel': 'Cleverly | #1 B2B Lead Generation Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=VXChXeJuEhI&t=88s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Like Charles for example click email it'll show me his email um I can also "
              "select all the same way I did inside of Apollo and it'll scrape everything for "
              'me that is really how easy it is to build qualified email lists using Apollo.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': "Like Charles for example click email it'll show me his email um I can also "
             "select all the same way I did inside of Apollo and it'll scrape everything for "
             'me that is really how easy it is to build qualified email lists using Apollo.',
      'title': 'How To Use Apollo IO and LinkedIn Sales Navigator To Build Emails Lists '
               '(Cleverly | #1 B2B Lead Generation Agency)',
      'url': 'https://www.youtube.com/watch?v=VXChXeJuEhI&t=88s',
      'video_id': 'VXChXeJuEhI'},
     {'author': 'HeyReach',
      'channel': 'HeyReach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:45](https://www.youtube.com/watch?v=RYTMEUD8-FQ&t=225s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'From there, it checks every single lead against that on its own and gives each '
              'one a score with reason attached. So, you can see why someone made the cut. You '
              'set those rules once and every new batch of leads is run through the same '
              'filter automatically.',
      'timestamp': 225,
      'timestamp_label': '[00:03:45]',
      'timestamp_seconds': 225,
      'tip': 'From there, it checks every single lead against that on its own and gives each '
             'one a score with reason attached. So, you can see why someone made the cut. You '
             'set those rules once and every new batch of leads is run through the same filter '
             'automatically.',
      'title': 'The Best AI LinkedIn Lead Generation Strategy for 2026 (HeyReach)',
      'url': 'https://www.youtube.com/watch?v=RYTMEUD8-FQ&t=225s',
      'video_id': 'RYTMEUD8-FQ'},
     {'author': 'Luke Weiler',
      'channel': 'Luke Weiler',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:37](https://www.youtube.com/watch?v=zR0U-wv3Bh8&t=397s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Except on this you can literally do it for free so yeah I mean that pretty much '
              'wraps up the videos and I hope this helps some people out and uh yeah have a '
              'good day.',
      'timestamp': 397,
      'timestamp_label': '[00:06:37]',
      'timestamp_seconds': 397,
      'tip': 'Except on this you can literally do it for free so yeah I mean that pretty much '
             'wraps up the videos and I hope this helps some people out and uh yeah have a '
             'good day.',
      'title': 'How to scrape LinkedIn Sales Navigator without using PhantomBuster (2024) '
               '(Luke Weiler)',
      'url': 'https://www.youtube.com/watch?v=zR0U-wv3Bh8&t=397s',
      'video_id': 'zR0U-wv3Bh8'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:52](https://www.youtube.com/watch?v=mGQoVCLseTU&t=112s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Email once your new notification is saved you will be able to change the rules '
              'which apply to it uh which means you have the ability to include or exclude '
              'individual Partners or sources or even whole lead types from the notification.',
      'timestamp': 112,
      'timestamp_label': '[00:01:52]',
      'timestamp_seconds': 112,
      'tip': 'Email once your new notification is saved you will be able to change the rules '
             'which apply to it uh which means you have the ability to include or exclude '
             'individual Partners or sources or even whole lead types from the notification.',
      'title': 'How To Notification Manager | boberdoo Lead Distribution System (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=mGQoVCLseTU&t=112s',
      'video_id': 'mGQoVCLseTU'},
     {'author': 'Sendable',
      'channel': 'Sendable',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:03](https://www.youtube.com/watch?v=BWyoFA5VHTE&t=183s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sendable is a LinkedIn outreach automation tool that allows you to find leads, '
              'then contact them. And HeyReach is a pure LinkedIn outreach tool so you can '
              'shoot campaigns, but you absolutely need other tools to find the leads.',
      'timestamp': 183,
      'timestamp_label': '[00:03:03]',
      'timestamp_seconds': 183,
      'tip': 'Sendable is a LinkedIn outreach automation tool that allows you to find leads, '
             'then contact them. And HeyReach is a pure LinkedIn outreach tool so you can '
             'shoot campaigns, but you absolutely need other tools to find the leads.',
      'title': 'The Best Heyreach Alternatives for LinkedIn Outreach Automation (2026) '
               '(Sendable)',
      'url': 'https://www.youtube.com/watch?v=BWyoFA5VHTE&t=183s',
      'video_id': 'BWyoFA5VHTE'},
     {'author': 'MoreMozi',
      'channel': 'MoreMozi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=94mDeuLH24c&t=42s)',
      'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                   'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                   'call routing (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I mean LinkedIn will for sure murder for what you're looking for. Like I mean "
              "you're looking for executives who want severance packages. Um cold outreach I "
              'mean I would I would do LinkedIn if I had to do this in order, I would one I '
              "wouldn't turn off from it ads.",
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': "I mean LinkedIn will for sure murder for what you're looking for. Like I mean "
             "you're looking for executives who want severance packages. Um cold outreach I "
             'mean I would I would do LinkedIn if I had to do this in order, I would one I '
             "wouldn't turn off from it ads.",
      'title': 'Helping a B2B Lead Gen Agency Improve Lead Quality (MoreMozi)',
      'url': 'https://www.youtube.com/watch?v=94mDeuLH24c&t=42s',
      'video_id': '94mDeuLH24c'}],
 10: [{'author': 'AJ Cassata',
       'channel': 'AJ Cassata',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:20](https://www.youtube.com/watch?v=12s-u4y1VF0&t=320s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Because AI um which is executed within Clay allows you to check the things '
               "that the filters can't see. So in our case, you know, we want to sell to B2B "
               'companies because we do B 2 B marketing at Revenue Boost, right?',
       'timestamp': 320,
       'timestamp_label': '[00:05:20]',
       'timestamp_seconds': 320,
       'tip': 'Because AI um which is executed within Clay allows you to check the things that '
              "the filters can't see. So in our case, you know, we want to sell to B2B "
              'companies because we do B 2 B marketing at Revenue Boost, right?',
       'title': 'The Top 3 Ways We Use Clay.com + AI To Get Leads & Clients [Tutorial] (AJ '
                'Cassata)',
       'url': 'https://www.youtube.com/watch?v=12s-u4y1VF0&t=320s',
       'video_id': '12s-u4y1VF0'},
      {'author': 'Ippei - Rank and Rent SEO',
       'channel': 'Ippei - Rank and Rent SEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:07](https://www.youtube.com/watch?v=wU1OKeR3fvI&t=127s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re going to get to 10K a month without fail, without any doubt because we can "
               "leverage the law of numbers in this business. And I'm going to show you "
               'exactly how in this video. Okay, AI automation very complex.',
       'timestamp': 127,
       'timestamp_label': '[00:02:07]',
       'timestamp_seconds': 127,
       'tip': "'re going to get to 10K a month without fail, without any doubt because we can "
              "leverage the law of numbers in this business. And I'm going to show you exactly "
              'how in this video. Okay, AI automation very complex.',
       'title': 'Rank and Rent - Fastest Path to 10K Per month (Ippei - Rank and Rent SEO)',
       'url': 'https://www.youtube.com/watch?v=wU1OKeR3fvI&t=127s',
       'video_id': 'wU1OKeR3fvI'},
      {'author': 'Xavier Caffrey GTM',
       'channel': 'Xavier Caffrey GTM',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:42](https://www.youtube.com/watch?v=UpSWlkeuUqs&t=42s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Um and also I want to highlight something that Clay added recently that I'm a "
               "big fan of is these AI filters. I absolutely love this and I can't believe "
               "that they offered this for free. So I'll tell you the biggest one is business "
               'types.',
       'timestamp': 42,
       'timestamp_label': '[00:00:42]',
       'timestamp_seconds': 42,
       'tip': "Um and also I want to highlight something that Clay added recently that I'm a "
              "big fan of is these AI filters. I absolutely love this and I can't believe that "
              "they offered this for free. So I'll tell you the biggest one is business types.",
       'title': 'The Fastest Way To Get B2B Clients In 2025 [Clay.com Tutorial] (Xavier '
                'Caffrey GTM)',
       'url': 'https://www.youtube.com/watch?v=UpSWlkeuUqs&t=42s',
       'video_id': 'UpSWlkeuUqs'},
      {'author': 'Michael Saruggia - GTM Engineering',
       'channel': 'Michael Saruggia - GTM Engineering',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=qWuvWm5Zcz0&t=21s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Luckily, we are in the age of AI and I have a genius copy strategy that we can '
               'actually leverage to send 50,000 cold emails per month being very cheap and '
               'only taking literally maybe 1 hour per week.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'Luckily, we are in the age of AI and I have a genius copy strategy that we can '
              'actually leverage to send 50,000 cold emails per month being very cheap and '
              'only taking literally maybe 1 hour per week.',
       'title': 'How I Am Sending 50K Cold Emails Per Month with Smartlead AI (Full Guide) '
                '(Michael Saruggia - GTM Engineering)',
       'url': 'https://www.youtube.com/watch?v=qWuvWm5Zcz0&t=21s',
       'video_id': 'qWuvWm5Zcz0'},
      {'author': 'Justin Davis',
       'channel': 'Justin Davis',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:54](https://www.youtube.com/watch?v=35rkCLq5LC4&t=54s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Lately, I've been using Instantly. It's coste effective for the number of "
               'emails it can reliably send, and it makes it easy to schedule your email '
               'sequences and automate your link building campaigns.',
       'timestamp': 54,
       'timestamp_label': '[00:00:54]',
       'timestamp_seconds': 54,
       'tip': "Lately, I've been using Instantly. It's coste effective for the number of "
              'emails it can reliably send, and it makes it easy to schedule your email '
              'sequences and automate your link building campaigns.',
       'title': 'SPF, DKIM and DMARC Explained for Link Building Outreach Email Deliverability '
                '(Justin Davis)',
       'url': 'https://www.youtube.com/watch?v=35rkCLq5LC4&t=54s',
       'video_id': '35rkCLq5LC4'},
      {'author': 'Brayden Bass',
       'channel': 'Brayden Bass',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:54](https://www.youtube.com/watch?v=QnqQKoCeYa8&t=294s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Send the link in the moment and automate if you have to. You can have the best '
               'reviews in town and still lose the call because of two words that are on '
               'almost every service business website.',
       'timestamp': 294,
       'timestamp_label': '[00:04:54]',
       'timestamp_seconds': 294,
       'tip': 'Send the link in the moment and automate if you have to. You can have the best '
              'reviews in town and still lose the call because of two words that are on almost '
              'every service business website.',
       'title': 'How to Get Local Service Leads in 2026 (Without Buying Shared Leads) (Brayden '
                'Bass)',
       'url': 'https://www.youtube.com/watch?v=QnqQKoCeYa8&t=294s',
       'video_id': 'QnqQKoCeYa8'},
      {'author': 'Tommy Chryst',
       'channel': 'Tommy Chryst',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:30](https://www.youtube.com/watch?v=YQbr_FhZTo8&t=90s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Then you'll see me connect it to the client dashboard as well as creating "
               "another automation to connect it to Google Sheets. And then finally, we'll "
               "actually get to test everything live which is what you're actually going to "
               'see a sneak peek of in a second.',
       'timestamp': 90,
       'timestamp_label': '[00:01:30]',
       'timestamp_seconds': 90,
       'tip': "Then you'll see me connect it to the client dashboard as well as creating "
              "another automation to connect it to Google Sheets. And then finally, we'll "
              "actually get to test everything live which is what you're actually going to see "
              'a sneak peek of in a second.',
       'title': 'RAW Build: Complete AI Voice Agent Speed-to-Lead System (Tommy Chryst)',
       'url': 'https://www.youtube.com/watch?v=YQbr_FhZTo8&t=90s',
       'video_id': 'YQbr_FhZTo8'},
      {'author': 'James Ranks',
       'channel': 'James Ranks',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:56](https://www.youtube.com/watch?v=PACpsGjR7Es&t=356s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, you need to have a Google Business Profile to really get uh recommended '
               "well within Google's like AI mode. So, this can give you a head start. But, "
               "regardless, otherwise, you're looking at an exact match domain.",
       'timestamp': 356,
       'timestamp_label': '[00:05:56]',
       'timestamp_seconds': 356,
       'tip': 'So, you need to have a Google Business Profile to really get uh recommended '
              "well within Google's like AI mode. So, this can give you a head start. But, "
              "regardless, otherwise, you're looking at an exact match domain.",
       'title': 'How To Find Your Rank & Rent Niche (Complete Guide + 2 Hidden Gems) (James '
                'Ranks)',
       'url': 'https://www.youtube.com/watch?v=PACpsGjR7Es&t=356s',
       'video_id': 'PACpsGjR7Es'},
      {'author': 'Zenscape',
       'channel': 'Zenscape',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:07](https://www.youtube.com/watch?v=HeluxMYTT0o&t=127s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Minds our programs tailored for different businesses what kind of business are '
               "you running I'd love to hear more about it so good we're determining what sort "
               "of business we have so let's let's just say I'm a real estate agent okay I'm a "
               'realtor in the Dallas.',
       'timestamp': 127,
       'timestamp_label': '[00:02:07]',
       'timestamp_seconds': 127,
       'tip': 'Minds our programs tailored for different businesses what kind of business are '
              "you running I'd love to hear more about it so good we're determining what sort "
              "of business we have so let's let's just say I'm a real estate agent okay I'm a "
              'realtor in the Dallas.',
       'title': 'AI Appointment Setting   The Future of Lead Gen for Marketing Agencies '
                '(Zenscape)',
       'url': 'https://www.youtube.com/watch?v=HeluxMYTT0o&t=127s',
       'video_id': 'HeluxMYTT0o'},
      {'author': 'Frankee Muryan',
       'channel': 'Frankee Muryan',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:03](https://www.youtube.com/watch?v=YWsrDI9jLXk&t=543s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "SMS and AI automations for your e-commerce and online brand. If that's you, if "
               "you're running ads and spending thousands of dollars and just need to find "
               'more ways to make revenue, regrow your email and SMS revenue by at least 20% '
               'or your money back.',
       'timestamp': 543,
       'timestamp_label': '[00:09:03]',
       'timestamp_seconds': 543,
       'tip': "SMS and AI automations for your e-commerce and online brand. If that's you, if "
              "you're running ads and spending thousands of dollars and just need to find more "
              'ways to make revenue, regrow your email and SMS revenue by at least 20% or your '
              'money back.',
       'title': 'How To Setup SPF DKIM DMARC Super Easy 2025 (Frankee Muryan)',
       'url': 'https://www.youtube.com/watch?v=YWsrDI9jLXk&t=543s',
       'video_id': 'YWsrDI9jLXk'},
      {'author': 'Georgey Tishin',
       'channel': 'Georgey Tishin',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:43](https://www.youtube.com/watch?v=p1rfyeLoS2s&t=163s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I'm going to download the CSV real quick just to show you guys an example of "
               "how that looks I'm going to open it up in Google Sheets uh here let's open it "
               'up right here I think I can just drag it in for from here.',
       'timestamp': 163,
       'timestamp_label': '[00:02:43]',
       'timestamp_seconds': 163,
       'tip': "I'm going to download the CSV real quick just to show you guys an example of "
              "how that looks I'm going to open it up in Google Sheets uh here let's open it "
              'up right here I think I can just drag it in for from here.',
       'title': 'How To Scrape UNLIMITED Local Business Leads Using Google Maps for FREE. '
                '(Georgey Tishin)',
       'url': 'https://www.youtube.com/watch?v=p1rfyeLoS2s&t=163s',
       'video_id': 'p1rfyeLoS2s'},
      {'author': 'boberdoo.com',
       'channel': 'boberdoo.com',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:01](https://www.youtube.com/watch?v=P79C92BNJHs&t=121s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Example which contains the posting url to be used for get post requests and '
               'when you need to send these specs to your vendors simply copy and paste the '
               'text and send it as a text document or a pdf that way you can modify it to '
               'include their unique credentials.',
       'timestamp': 121,
       'timestamp_label': '[00:02:01]',
       'timestamp_seconds': 121,
       'tip': 'Example which contains the posting url to be used for get post requests and '
              'when you need to send these specs to your vendors simply copy and paste the '
              'text and send it as a text document or a pdf that way you can modify it to '
              'include their unique credentials.',
       'title': 'How To Ping Post Specifications | boberdoo Ping/Post Software (boberdoo.com)',
       'url': 'https://www.youtube.com/watch?v=P79C92BNJHs&t=121s',
       'video_id': 'P79C92BNJHs'},
      {'author': 'Thelaywala',
       'channel': 'Thelaywala',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:47](https://www.youtube.com/watch?v=KocD1S0Auvo&t=47s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, in this case, it's like a painting business and as an example, immediately "
               'you would like customer customer should be engaged and immediately an '
               'appointment is booked for the newest nearest availability.',
       'timestamp': 47,
       'timestamp_label': '[00:00:47]',
       'timestamp_seconds': 47,
       'tip': "So, in this case, it's like a painting business and as an example, immediately "
              'you would like customer customer should be engaged and immediately an '
              'appointment is booked for the newest nearest availability.',
       'title': 'Set Up AI Agents for Faster Appointments (Thelaywala)',
       'url': 'https://www.youtube.com/watch?v=KocD1S0Auvo&t=47s',
       'video_id': 'KocD1S0Auvo'},
      {'author': 'Rafael Hernandez ⚡️',
       'channel': 'Rafael Hernandez ⚡️',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:17](https://www.youtube.com/watch?v=ngsR38BAFbc&t=77s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So that's not gonna change. AI doesn't make that go away. Every business still "
               "needs leads, calls, customers, appointments. Because without leads, you can't "
               'make sales.',
       'timestamp': 77,
       'timestamp_label': '[00:01:17]',
       'timestamp_seconds': 77,
       'tip': "So that's not gonna change. AI doesn't make that go away. Every business still "
              "needs leads, calls, customers, appointments. Because without leads, you can't "
              'make sales.',
       'title': 'Is a Lead Gen Agency Still Worth It in 2026? (Rafael Hernandez ⚡️)',
       'url': 'https://www.youtube.com/watch?v=ngsR38BAFbc&t=77s',
       'video_id': 'ngsR38BAFbc'},
      {'author': 'LeadLoft',
       'channel': 'LeadLoft',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:53](https://www.youtube.com/watch?v=bAri9HF705I&t=113s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And of course, there's email steps. And if you want to run cold calling, you "
               "can run that as well. For now, let's get rid of the cold calling because I "
               "know some of you probably don't want to be cold calling here. I'm going to "
               'automate as much of this as possible.',
       'timestamp': 113,
       'timestamp_label': '[00:01:53]',
       'timestamp_seconds': 113,
       'tip': "And of course, there's email steps. And if you want to run cold calling, you "
              "can run that as well. For now, let's get rid of the cold calling because I know "
              "some of you probably don't want to be cold calling here. I'm going to automate "
              'as much of this as possible.',
       'title': 'How to Scrape LinkedIn Sales Navigator? Sales Navigator Scraper (Guide) '
                '(LeadLoft)',
       'url': 'https://www.youtube.com/watch?v=bAri9HF705I&t=113s',
       'video_id': 'bAri9HF705I'}],
 11: [{'author': 'Caleb Harris',
       'channel': 'Caleb Harris',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:32](https://www.youtube.com/watch?v=TNZJNdxQvsM&t=1052s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'People actually call this model the one-man agency, because with all these '
               'automations these days, you can scale this to 50k a month without adding a '
               'single team member.',
       'timestamp': 1052,
       'timestamp_label': '[00:17:32]',
       'timestamp_seconds': 1052,
       'tip': 'People actually call this model the one-man agency, because with all these '
              'automations these days, you can scale this to 50k a month without adding a '
              'single team member.',
       'title': 'How I Make $221,217/Month With Pay Per Lead (Step-by-Step) (Caleb Harris)',
       'url': 'https://www.youtube.com/watch?v=TNZJNdxQvsM&t=1052s',
       'video_id': 'TNZJNdxQvsM'},
      {'author': 'Ruben Frederic',
       'channel': 'Ruben Frederic',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:30](https://www.youtube.com/watch?v=B6M6968u10c&t=990s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Clients can blame the lead provider for weak sales, follow, slow response '
               'time, poor closing or mis calls. So, at least with appointments, your team is '
               'calling.',
       'timestamp': 990,
       'timestamp_label': '[00:16:30]',
       'timestamp_seconds': 990,
       'tip': 'Clients can blame the lead provider for weak sales, follow, slow response time, '
              'poor closing or mis calls. So, at least with appointments, your team is '
              'calling.',
       'title': 'Pay Per Lead vs Pay Per Appointment for Lead Gen Agency (Ruben Frederic)',
       'url': 'https://www.youtube.com/watch?v=B6M6968u10c&t=990s',
       'video_id': 'B6M6968u10c'},
      {'author': 'MoreMozi',
       'channel': 'MoreMozi',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:48](https://www.youtube.com/watch?v=94mDeuLH24c&t=168s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Vegas to learn how we scale. It's where my team spends two days with you to "
               "identify the thing that's holding your business back. And so if that sounds "
               "interesting, click book a call and if you're a fit, we'd love to potentially "
               'see you out here in Vegas.',
       'timestamp': 168,
       'timestamp_label': '[00:02:48]',
       'timestamp_seconds': 168,
       'tip': "Vegas to learn how we scale. It's where my team spends two days with you to "
              "identify the thing that's holding your business back. And so if that sounds "
              "interesting, click book a call and if you're a fit, we'd love to potentially "
              'see you out here in Vegas.',
       'title': 'Helping a B2B Lead Gen Agency Improve Lead Quality (MoreMozi)',
       'url': 'https://www.youtube.com/watch?v=94mDeuLH24c&t=168s',
       'video_id': '94mDeuLH24c'},
      {'author': 'Melvin Mendoza',
       'channel': 'Melvin Mendoza',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:02](https://www.youtube.com/watch?v=OJFNkb_PwS4&t=422s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And an easy offer that you can run, guys, is hey, I'm charging $250 to a "
               "roofing contractor for an appointment, and I'm just literally charging them "
               "for $250 straight up. And my offer right now, and to increase urgency, is I'm "
               'giving them $250 worth of free appointments.',
       'timestamp': 422,
       'timestamp_label': '[00:07:02]',
       'timestamp_seconds': 422,
       'tip': "And an easy offer that you can run, guys, is hey, I'm charging $250 to a "
              "roofing contractor for an appointment, and I'm just literally charging them for "
              "$250 straight up. And my offer right now, and to increase urgency, is I'm "
              'giving them $250 worth of free appointments.',
       'title': 'How To Build A Low Ticket Sales Team (pay per appointment) (Melvin Mendoza)',
       'url': 'https://www.youtube.com/watch?v=OJFNkb_PwS4&t=422s',
       'video_id': 'OJFNkb_PwS4'},
      {'author': 'Jason Grossman',
       'channel': 'Jason Grossman',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:27:43](https://www.youtube.com/watch?v=Ot93upK_YX4&t=1663s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Get in the trenches, then hire some team, put the SOPs, and then we can layer '
               "in the automation, right? So what we do best is definitely sales. So, here's "
               'an event funnel. If you click on register, you got the four details.',
       'timestamp': 1663,
       'timestamp_label': '[00:27:43]',
       'timestamp_seconds': 1663,
       'tip': 'Get in the trenches, then hire some team, put the SOPs, and then we can layer '
              "in the automation, right? So what we do best is definitely sales. So, here's an "
              'event funnel. If you click on register, you got the four details.',
       'title': 'Create an AI Powered Lead Generation Machine Using GoHighLevel! (Jason '
                'Grossman)',
       'url': 'https://www.youtube.com/watch?v=Ot93upK_YX4&t=1663s',
       'video_id': 'Ot93upK_YX4'},
      {'author': 'TradeOps Consulting',
       'channel': 'TradeOps Consulting',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:05](https://www.youtube.com/watch?v=dUeSNisWyGc&t=125s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Implementation strategy is pretty that easy. Ideally, you should have a human '
               "rep or answering services to respond to calls that you don't pick. But, worst "
               'case, have an automated system like Go HighLevel to automatically send a '
               'message to each missed call or missed message.',
       'timestamp': 125,
       'timestamp_label': '[00:02:05]',
       'timestamp_seconds': 125,
       'tip': 'Implementation strategy is pretty that easy. Ideally, you should have a human '
              "rep or answering services to respond to calls that you don't pick. But, worst "
              'case, have an automated system like Go HighLevel to automatically send a '
              'message to each missed call or missed message.',
       'title': 'The 5-Hack Lead Generation Blueprint Every HVAC & Plumbing Owner Needs to See '
                'in 2026 (TradeOps Consulting)',
       'url': 'https://www.youtube.com/watch?v=dUeSNisWyGc&t=125s',
       'video_id': 'dUeSNisWyGc'},
      {'author': 'Hook Agency',
       'channel': 'Hook Agency',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:19](https://www.youtube.com/watch?v=WkliDsQi_qI&t=679s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I can't commend Hook Agency enough on just the experience. We're talking about "
               "plumbing experience, but the experience we've had overall working with your "
               'team members on this uh project.',
       'timestamp': 679,
       'timestamp_label': '[00:11:19]',
       'timestamp_seconds': 679,
       'tip': "I can't commend Hook Agency enough on just the experience. We're talking about "
              "plumbing experience, but the experience we've had overall working with your "
              'team members on this uh project.',
       'title': 'HVAC Lead Generation 2026 (Hook Agency)',
       'url': 'https://www.youtube.com/watch?v=WkliDsQi_qI&t=679s',
       'video_id': 'WkliDsQi_qI'},
      {'author': 'Smartlead',
       'channel': 'Smartlead',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:48](https://www.youtube.com/watch?v=CAJAVLQEQ88&t=108s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And based on this, we'll then be able to find a good list of contacts that fit "
               "our ideal client profile, in which case it's basically any partners that work "
               'at consulting firms.',
       'timestamp': 108,
       'timestamp_label': '[00:01:48]',
       'timestamp_seconds': 108,
       'tip': "And based on this, we'll then be able to find a good list of contacts that fit "
              "our ideal client profile, in which case it's basically any partners that work "
              'at consulting firms.',
       'title': 'How I Send 200,000+ Cold Emails Per Month With AI (Smartlead)',
       'url': 'https://www.youtube.com/watch?v=CAJAVLQEQ88&t=108s',
       'video_id': 'CAJAVLQEQ88'},
      {'author': 'Nav Constructs',
       'channel': 'Nav Constructs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:09](https://www.youtube.com/watch?v=ONw0mbljquQ&t=609s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "As you can see, I have so many This is proof that I've been able to do this "
               'many times, right? I have location-based and all this. Um but pretty much what '
               "you're going to do is you're going to create your profile. Now, you're going "
               'to put in Be very careful here, okay?',
       'timestamp': 609,
       'timestamp_label': '[00:10:09]',
       'timestamp_seconds': 609,
       'tip': "As you can see, I have so many This is proof that I've been able to do this "
              'many times, right? I have location-based and all this. Um but pretty much what '
              "you're going to do is you're going to create your profile. Now, you're going to "
              'put in Be very careful here, okay?',
       'title': 'How to verify google business profiles WITHOUT video verification (online '
                'construction) (Nav Constructs)',
       'url': 'https://www.youtube.com/watch?v=ONw0mbljquQ&t=609s',
       'video_id': 'ONw0mbljquQ'},
      {'author': 'Ippei - Rank and Rent SEO',
       'channel': 'Ippei - Rank and Rent SEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=raunmaNfU1o&t=20s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And every call that comes through is recorded, and anytime my client closes '
               'any job that comes from my sites, I get paid a commission. So, this was a '
               '$28,000 job that I got paid $1,000 in commission. For this one client, they '
               'paid me $8,346 last month.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'And every call that comes through is recorded, and anytime my client closes any '
              'job that comes from my sites, I get paid a commission. So, this was a $28,000 '
              'job that I got paid $1,000 in commission. For this one client, they paid me '
              '$8,346 last month.',
       'title': '21 Niche Service Businesses (Low Competition) – Make Money with Leads (Ippei '
                '- Rank and Rent SEO)',
       'url': 'https://www.youtube.com/watch?v=raunmaNfU1o&t=20s',
       'video_id': 'raunmaNfU1o'},
      {'author': 'Dekker the Marketer',
       'channel': 'Dekker the Marketer',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:18](https://www.youtube.com/watch?v=ZXT4QpFi6yY&t=258s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Publicly available so when we're doing cold emails uh it's it's not some "
               "illegal Shady activity that we're doing particularly when we're not spamming "
               "and I don't advise that you take a Spam approach to cold email.",
       'timestamp': 258,
       'timestamp_label': '[00:04:18]',
       'timestamp_seconds': 258,
       'tip': "Publicly available so when we're doing cold emails uh it's it's not some "
              "illegal Shady activity that we're doing particularly when we're not spamming "
              "and I don't advise that you take a Spam approach to cold email.",
       'title': 'Cold Email Marketing & GDPR Legal Compliance (Dekker the Marketer)',
       'url': 'https://www.youtube.com/watch?v=ZXT4QpFi6yY&t=258s',
       'video_id': 'ZXT4QpFi6yY'},
      {'author': 'boberdoo.com',
       'channel': 'boberdoo.com',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:30](https://www.youtube.com/watch?v=SxFdDGaaQiM&t=150s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Overview of current Source settings and the plus sign on the far left so stay '
               'tuned for the next video which will explain how each Source can be customized '
               'using various setup options.',
       'timestamp': 150,
       'timestamp_label': '[00:02:30]',
       'timestamp_seconds': 150,
       'tip': 'Overview of current Source settings and the plus sign on the far left so stay '
              'tuned for the next video which will explain how each Source can be customized '
              'using various setup options.',
       'title': 'How To Manage Sources Part 1 | boberdoo Lead Distribution System '
                '(boberdoo.com)',
       'url': 'https://www.youtube.com/watch?v=SxFdDGaaQiM&t=150s',
       'video_id': 'SxFdDGaaQiM'},
      {'author': 'Misar AI',
       'channel': 'Misar AI',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:37](https://www.youtube.com/watch?v=_bfiWvgegAM&t=217s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Finally, look at the protections you've added, such as easy opt-out options. "
               "If the recipient's data protection rights outweigh your business interest, you "
               "can't claim legitimate interest. So, if I'm sending a cold email to a "
               'potential corporate client.',
       'timestamp': 217,
       'timestamp_label': '[00:03:37]',
       'timestamp_seconds': 217,
       'tip': "Finally, look at the protections you've added, such as easy opt-out options. If "
              "the recipient's data protection rights outweigh your business interest, you "
              "can't claim legitimate interest. So, if I'm sending a cold email to a potential "
              'corporate client.',
       'title': 'Is Cold Email Legal Under GDPR? A 2026 Compliance Guide for B2B Sales Teams '
                '(Misar AI)',
       'url': 'https://www.youtube.com/watch?v=_bfiWvgegAM&t=217s',
       'video_id': '_bfiWvgegAM'},
      {'author': 'George Vlasyev',
       'channel': 'George Vlasyev',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:06](https://www.youtube.com/watch?v=S8imkVkGoZw&t=66s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'These features are especially useful when managing many campaigns, separating '
               'client data, limiting team access, and delivering branded reports. Instantly '
               'removes steps for simplicity. SmartLead adds structure and control for scale. '
               'They just serve different workflows.',
       'timestamp': 66,
       'timestamp_label': '[00:01:06]',
       'timestamp_seconds': 66,
       'tip': 'These features are especially useful when managing many campaigns, separating '
              'client data, limiting team access, and delivering branded reports. Instantly '
              'removes steps for simplicity. SmartLead adds structure and control for scale. '
              'They just serve different workflows.',
       'title': 'Instantly AI vs Smartlead 2026: Which Cold Email Tool Is Right for You? '
                '(George Vlasyev)',
       'url': 'https://www.youtube.com/watch?v=S8imkVkGoZw&t=66s',
       'video_id': 'S8imkVkGoZw'},
      {'author': 'reachmarketingllc',
       'channel': 'reachmarketingllc',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:43](https://www.youtube.com/watch?v=klDqIDgOt58&t=403s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Reach Marketing provides comprehensive capabilities from B2B list building, '
               'email marketing, and content syndication to highly targeted MBI AI programs. '
               'They even provide SQL appointment setting, placing qualified meetings directly '
               "onto your sales team's calendar.",
       'timestamp': 403,
       'timestamp_label': '[00:06:43]',
       'timestamp_seconds': 403,
       'tip': 'Reach Marketing provides comprehensive capabilities from B2B list building, '
              'email marketing, and content syndication to highly targeted MBI AI programs. '
              'They even provide SQL appointment setting, placing qualified meetings directly '
              "onto your sales team's calendar.",
       'title': 'B2B Lead Generation Statistics & Benchmarks 2026: Cost Per Lead, MQL-to-SQL & '
                'Buyer Data (reachmarketingllc)',
       'url': 'https://www.youtube.com/watch?v=klDqIDgOt58&t=403s',
       'video_id': 'klDqIDgOt58'}],
 12: [{'author': 'Thelaywala',
       'channel': 'Thelaywala',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:15](https://www.youtube.com/watch?v=KocD1S0Auvo&t=255s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'What the action that would be. You can add, you know, like a book appointment '
               'booking. The same thing we talk about. And you can click the free train '
               'extreme match and you actually start web call and start talking to and see how '
               'it is responding.',
       'timestamp': 255,
       'timestamp_label': '[00:04:15]',
       'timestamp_seconds': 255,
       'tip': 'What the action that would be. You can add, you know, like a book appointment '
              'booking. The same thing we talk about. And you can click the free train extreme '
              'match and you actually start web call and start talking to and see how it is '
              'responding.',
       'title': 'Set Up AI Agents for Faster Appointments (Thelaywala)',
       'url': 'https://www.youtube.com/watch?v=KocD1S0Auvo&t=255s',
       'video_id': 'KocD1S0Auvo'},
      {'author': 'Vincent Robin',
       'channel': 'Vincent Robin',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:24](https://www.youtube.com/watch?v=7Sq3Ger8D3A&t=744s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So in my case it's New York. Then you can select the days you want to send "
               'your cold emails. So Monday to Friday is perfect. Time period between '
               'sequences from 9 to 5. And finally max number of new leads reach per day per '
               'campaign.',
       'timestamp': 744,
       'timestamp_label': '[00:12:24]',
       'timestamp_seconds': 744,
       'tip': "So in my case it's New York. Then you can select the days you want to send your "
              'cold emails. So Monday to Friday is perfect. Time period between sequences from '
              '9 to 5. And finally max number of new leads reach per day per campaign.',
       'title': 'How To Setup Your Smartlead.ai Cold Email Campaign (Vincent Robin)',
       'url': 'https://www.youtube.com/watch?v=7Sq3Ger8D3A&t=744s',
       'video_id': '7Sq3Ger8D3A'},
      {'author': 'Commercial Cleaning CEO',
       'channel': 'Commercial Cleaning CEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:31](https://www.youtube.com/watch?v=AfGI7vom6uw&t=571s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Day and if you want my personal help building your business then check out the '
               "links down below I'm Matt your commercial cleaning CEO thanks for watching and "
               'until next time keep building.',
       'timestamp': 571,
       'timestamp_label': '[00:09:31]',
       'timestamp_seconds': 571,
       'tip': 'Day and if you want my personal help building your business then check out the '
              "links down below I'm Matt your commercial cleaning CEO thanks for watching and "
              'until next time keep building.',
       'title': 'How To Get 1K Commercial Cleaning Leads in Minutes (Commercial Cleaning CEO)',
       'url': 'https://www.youtube.com/watch?v=AfGI7vom6uw&t=571s',
       'video_id': 'AfGI7vom6uw'},
      {'author': 'Digitellix',
       'channel': 'Digitellix',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:47](https://www.youtube.com/watch?v=iM8vOv1pK8g&t=347s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Put together, here's a 30-day plan. Days 1 to 7, choose your sending service, "
               'add the records on a subdomain, import and clean your consented list, and '
               'write a three-email welcome series. Days 8 to 14, week one of the warm-up and '
               'turn on the welcome automation.',
       'timestamp': 347,
       'timestamp_label': '[00:05:47]',
       'timestamp_seconds': 347,
       'tip': "Put together, here's a 30-day plan. Days 1 to 7, choose your sending service, "
              'add the records on a subdomain, import and clean your consented list, and write '
              'a three-email welcome series. Days 8 to 14, week one of the warm-up and turn on '
              'the welcome automation.',
       'title': 'Email Deliverability for Small Businesses: SPF, DKIM, DMARC + Warm-Up '
                '(Digitellix)',
       'url': 'https://www.youtube.com/watch?v=iM8vOv1pK8g&t=347s',
       'video_id': 'iM8vOv1pK8g'},
      {'author': 'Kirke Männik',
       'channel': 'Kirke Männik',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:22](https://www.youtube.com/watch?v=2OJzjgoV9mo&t=142s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '$143,000 in less than 90 days for them using this killer cold email blueprint '
               'that I broke down in this 5 minute video I also exposed the exact subject line '
               "and copy we used to add $28,000 to Danny's smma and 82 sales calls a week for "
               'this other client.',
       'timestamp': 142,
       'timestamp_label': '[00:02:22]',
       'timestamp_seconds': 142,
       'tip': '$143,000 in less than 90 days for them using this killer cold email blueprint '
              'that I broke down in this 5 minute video I also exposed the exact subject line '
              "and copy we used to add $28,000 to Danny's smma and 82 sales calls a week for "
              'this other client.',
       'title': 'How to scrape unlimited Apollo leads for free (2 mins) (Kirke Männik)',
       'url': 'https://www.youtube.com/watch?v=2OJzjgoV9mo&t=142s',
       'video_id': '2OJzjgoV9mo'},
      {'author': 'Smartlead',
       'channel': 'Smartlead',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:05:53](https://www.youtube.com/watch?v=doR2rhof6CM&t=3953s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'In my case, the favorite kind of call to action that I love to start off with '
               'for most of our clients is literally saying, "Hey, would you like desired '
               'outcome? In this case, would you like to attend our summit?".',
       'timestamp': 3953,
       'timestamp_label': '[01:05:53]',
       'timestamp_seconds': 3953,
       'tip': 'In my case, the favorite kind of call to action that I love to start off with '
              'for most of our clients is literally saying, "Hey, would you like desired '
              'outcome? In this case, would you like to attend our summit?".',
       'title': 'Complete B2B Cold Email Copywriting Course Using AI (2026) (Smartlead)',
       'url': 'https://www.youtube.com/watch?v=doR2rhof6CM&t=3953s',
       'video_id': 'doR2rhof6CM'},
      {'author': 'Kyle Dickson',
       'channel': 'Kyle Dickson',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:51](https://www.youtube.com/watch?v=drsocawArfo&t=231s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Ramp-up in the cold emails, which I talked about right here. So, what this '
               "means is when you start sending cold emails after 14 to 21 days, you're not "
               "going to start sending 20 cold emails a day off the bat. You're going to ramp "
               'it up, same thing.',
       'timestamp': 231,
       'timestamp_label': '[00:03:51]',
       'timestamp_seconds': 231,
       'tip': 'Ramp-up in the cold emails, which I talked about right here. So, what this '
              "means is when you start sending cold emails after 14 to 21 days, you're not "
              "going to start sending 20 cold emails a day off the bat. You're going to ramp "
              'it up, same thing.',
       'title': 'Cold Email Deliverability MASTERCLASS – Inbox Every Time! (Full Guide) (Kyle '
                'Dickson)',
       'url': 'https://www.youtube.com/watch?v=drsocawArfo&t=231s',
       'video_id': 'drsocawArfo'},
      {'author': 'Israel Saucedo | Get Bizzy LLC',
       'channel': 'Israel Saucedo | Get Bizzy LLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:49](https://www.youtube.com/watch?v=Rp1Up2fDgPg&t=49s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Google business profile that you probably already have set up, maybe sitting '
               'dormant for a long time, and how you can start using it to generate 20, 30, '
               '40, sometimes even more leads than that just by use utilizing that Google '
               'business profile correctly.',
       'timestamp': 49,
       'timestamp_label': '[00:00:49]',
       'timestamp_seconds': 49,
       'tip': 'Google business profile that you probably already have set up, maybe sitting '
              'dormant for a long time, and how you can start using it to generate 20, 30, 40, '
              'sometimes even more leads than that just by use utilizing that Google business '
              'profile correctly.',
       'title': 'How to Turn Your Google Business Profile Into 30+ Leads a Month (Israel '
                'Saucedo | Get Bizzy LLC)',
       'url': 'https://www.youtube.com/watch?v=Rp1Up2fDgPg&t=49s',
       'video_id': 'Rp1Up2fDgPg'},
      {'author': 'Insight Carrier',
       'channel': 'Insight Carrier',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:41](https://www.youtube.com/watch?v=DG-DCGF3xHk&t=161s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The loss runs are emailed to you in three to five business days. Taking over '
               'an account, the BOR builder writes a broker of record letter in seconds for '
               'any state, too. Find the lead, make contact, start the application and the '
               'loss runs all in one place.',
       'timestamp': 161,
       'timestamp_label': '[00:02:41]',
       'timestamp_seconds': 161,
       'tip': 'The loss runs are emailed to you in three to five business days. Taking over an '
              'account, the BOR builder writes a broker of record letter in seconds for any '
              'state, too. Find the lead, make contact, start the application and the loss '
              'runs all in one place.',
       'title': 'This Trucking Insurance Application Fills Itself (Works in Any State) '
                '(Insight Carrier)',
       'url': 'https://www.youtube.com/watch?v=DG-DCGF3xHk&t=161s',
       'video_id': 'DG-DCGF3xHk'},
      {'author': 'Smartlead',
       'channel': 'Smartlead',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:12](https://www.youtube.com/watch?v=NWEL3WNYDhg&t=132s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Now, here's the entire goal of the challenge. I want to send about 20,000 cold "
               "emails in 30 days. So, give or take, that's about 1,000 emails a day. The "
               'reason why I want to send 20,000 cold email is from just running a cold email '
               'agency for the past 4 years now.',
       'timestamp': 132,
       'timestamp_label': '[00:02:12]',
       'timestamp_seconds': 132,
       'tip': "Now, here's the entire goal of the challenge. I want to send about 20,000 cold "
              "emails in 30 days. So, give or take, that's about 1,000 emails a day. The "
              'reason why I want to send 20,000 cold email is from just running a cold email '
              'agency for the past 4 years now.',
       'title': 'I Sent 20,000 Cold Emails With Claude Code in 30 Days (Results) (Smartlead)',
       'url': 'https://www.youtube.com/watch?v=NWEL3WNYDhg&t=132s',
       'video_id': 'NWEL3WNYDhg'},
      {'author': 'The Roofing Marketer',
       'channel': 'The Roofing Marketer',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:32](https://www.youtube.com/watch?v=CLPZaVvxwQk&t=92s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Like drop a comment DM me you can connect with us on social media but this is '
               "real stuff guys I hope you're having a great day and a great weekend I'm super "
               'excited to share this stuff with you as you can tell thank you so much for '
               'watching this video talk to you soon.',
       'timestamp': 92,
       'timestamp_label': '[00:01:32]',
       'timestamp_seconds': 92,
       'tip': 'Like drop a comment DM me you can connect with us on social media but this is '
              "real stuff guys I hope you're having a great day and a great weekend I'm super "
              'excited to share this stuff with you as you can tell thank you so much for '
              'watching this video talk to you soon.',
       'title': 'Roofing Lead Gen | Marketing for Roofers | Solar Lead Gen | Roofing PPC | The '
                'Roofing Marketer (The Roofing Marketer)',
       'url': 'https://www.youtube.com/watch?v=CLPZaVvxwQk&t=92s',
       'video_id': 'CLPZaVvxwQk'},
      {'author': 'Contact Center Compliance',
       'channel': 'Contact Center Compliance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:33:30](https://www.youtube.com/watch?v=_EAk_fw9kZk&t=2010s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "There and you know that's probably 45 minutes of masterclass for you another "
               "day but it's it's good to just know that there'll be some developments this "
               'year in that front that will help a little bit with the reassigned numbers '
               'piece.',
       'timestamp': 2010,
       'timestamp_label': '[00:33:30]',
       'timestamp_seconds': 2010,
       'tip': "There and you know that's probably 45 minutes of masterclass for you another "
              "day but it's it's good to just know that there'll be some developments this "
              'year in that front that will help a little bit with the reassigned numbers '
              'piece.',
       'title': 'TCPA Marketing Consent Masterclass Series Part 1 (Contact Center Compliance)',
       'url': 'https://www.youtube.com/watch?v=_EAk_fw9kZk&t=2010s',
       'video_id': '_EAk_fw9kZk'},
      {'author': 'Snovio',
       'channel': 'Snovio',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=MmWpOeG5GW4&t=21s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Imagine it's 3 months is from now. You have three clients paying you $2,500 "
               'per month. Your campaigns are running, meetings are booked. You spend more '
               "time replying to interested prospects than hunting for work. That's the "
               "business we're building in this video.",
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': "Imagine it's 3 months is from now. You have three clients paying you $2,500 per "
              'month. Your campaigns are running, meetings are booked. You spend more time '
              "replying to interested prospects than hunting for work. That's the business "
              "we're building in this video.",
       'title': 'Starting a Lead Generation Agency Is Easy in 2026! (Snovio)',
       'url': 'https://www.youtube.com/watch?v=MmWpOeG5GW4&t=21s',
       'video_id': 'MmWpOeG5GW4'},
      {'author': 'Billy Robinson',
       'channel': 'Billy Robinson',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:43](https://www.youtube.com/watch?v=-_uHG2CwBjA&t=583s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s a lot, but when you look at the numbers it really is a good investment. So "
               '200 a day on ads leads to six leads, three sales calls and one closed client. '
               "So you're collecting about 3,750 a day which is five clients a week or 18,750 "
               'a week which is 75K a month.',
       'timestamp': 583,
       'timestamp_label': '[00:09:43]',
       'timestamp_seconds': 583,
       'tip': "'s a lot, but when you look at the numbers it really is a good investment. So "
              '200 a day on ads leads to six leads, three sales calls and one closed client. '
              "So you're collecting about 3,750 a day which is five clients a week or 18,750 a "
              'week which is 75K a month.',
       'title': 'The Pay Per Lead Model Quietly Printing $75K/Month for Agencies in 2026 '
                '(Billy Robinson)',
       'url': 'https://www.youtube.com/watch?v=-_uHG2CwBjA&t=583s',
       'video_id': '-_uHG2CwBjA'},
      {'author': 'Melvin Mendoza',
       'channel': 'Melvin Mendoza',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:20:38](https://www.youtube.com/watch?v=OJFNkb_PwS4&t=1238s)',
       'relevance': 'Attributed practitioner commentary on B2B commercial lead generation, '
                    'multi-inbox outbound infrastructure, and pay-per-qualified-appointment / '
                    'call routing (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s say, four appointments, it's a very easy sale. You can probably make at "
               'least three sales a week. I know that the top performers are making a sale a '
               'day. Now the culture comes down to sending out a scoreboard, right?',
       'timestamp': 1238,
       'timestamp_label': '[00:20:38]',
       'timestamp_seconds': 1238,
       'tip': "'s say, four appointments, it's a very easy sale. You can probably make at "
              'least three sales a week. I know that the top performers are making a sale a '
              'day. Now the culture comes down to sending out a scoreboard, right?',
       'title': 'How To Build A Low Ticket Sales Team (pay per appointment) (Melvin Mendoza)',
       'url': 'https://www.youtube.com/watch?v=OJFNkb_PwS4&t=1238s',
       'video_id': 'OJFNkb_PwS4'}]}
