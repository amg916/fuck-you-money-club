"""Curated 180-citation Productized AI Agencies baseline (15 per chapter across Q1-Q12) mined strictly from verified Productized AI Agencies YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'15000',
     '30k',
     '5000',
     '50k',
     'aaa',
     'ada',
     'agency',
     'agent',
     'api',
     'appointment',
     'audit',
     'automated',
     'automation',
     'b2b',
     'base',
     'based',
     'bland',
     'booking',
     'bots',
     'brett',
     'building',
     'business',
     'case',
     'churn',
     'claude',
     'clay',
     'client',
     'clients',
     'cold',
     'com',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'15000',
     '30k',
     '5000',
     '50k',
     'aaa',
     'ada',
     'agency',
     'agent',
     'api',
     'appointment',
     'audit',
     'automated',
     'automation',
     'b2b',
     'base',
     'based',
     'bland',
     'booking',
     'bots',
     'brett',
     'budget',
     'building',
     'business',
     'buyer',
     'case',
     'churn',
     'claude',
     'clay',
     'client',
     'clients',
     'cold',
     'com',
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
 3: {'15000',
     '30k',
     '5000',
     '50k',
     'aaa',
     'ada',
     'agency',
     'agent',
     'api',
     'appointment',
     'audit',
     'automated',
     'automation',
     'b2b',
     'base',
     'based',
     'bland',
     'booking',
     'bots',
     'brett',
     'building',
     'business',
     'case',
     'cash',
     'cashflow',
     'churn',
     'claude',
     'clay',
     'client',
     'clients',
     'cold',
     'com',
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
 4: {'15000',
     '30k',
     '5000',
     '50k',
     'aaa',
     'ada',
     'agency',
     'agent',
     'api',
     'appointment',
     'audit',
     'automated',
     'automation',
     'b2b',
     'base',
     'based',
     'bland',
     'booking',
     'bots',
     'brett',
     'budget',
     'building',
     'business',
     'capital',
     'case',
     'churn',
     'claude',
     'clay',
     'client',
     'clients',
     'cold',
     'com',
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
 5: {'15000',
     '30k',
     '5000',
     '50k',
     'aaa',
     'ada',
     'agency',
     'agent',
     'api',
     'appointment',
     'audit',
     'automated',
     'automation',
     'avoid',
     'b2b',
     'base',
     'based',
     'bland',
     'booking',
     'bots',
     'brett',
     'building',
     'business',
     'case',
     'churn',
     'claude',
     'clawback',
     'clay',
     'client',
     'clients',
     'cold',
     'com',
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
 6: {'15000',
     '30k',
     '5000',
     '50k',
     'aaa',
     'ada',
     'agency',
     'agent',
     'api',
     'appointment',
     'audit',
     'automated',
     'automation',
     'b2b',
     'base',
     'based',
     'bland',
     'booking',
     'bots',
     'brett',
     'building',
     'business',
     'case',
     'churn',
     'claude',
     'clay',
     'client',
     'clients',
     'cold',
     'com',
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
 7: {'15000',
     '30k',
     '5000',
     '50k',
     'aaa',
     'ada',
     'agency',
     'agent',
     'api',
     'appointment',
     'audit',
     'automated',
     'automation',
     'b2b',
     'base',
     'based',
     'bland',
     'booking',
     'bots',
     'brett',
     'building',
     'business',
     'case',
     'checklist',
     'churn',
     'claude',
     'clay',
     'client',
     'clients',
     'cold',
     'com',
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
 8: {'15000',
     '30k',
     '5000',
     '50k',
     'aaa',
     'ada',
     'agency',
     'agent',
     'api',
     'appointment',
     'audit',
     'automated',
     'automation',
     'b2b',
     'base',
     'based',
     'bland',
     'booking',
     'bots',
     'brett',
     'building',
     'business',
     'case',
     'churn',
     'claude',
     'clay',
     'client',
     'clients',
     'cold',
     'com',
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
 9: {'15000',
     '30k',
     '5000',
     '50k',
     'aaa',
     'ada',
     'agency',
     'agent',
     'agreement',
     'api',
     'appointment',
     'audit',
     'automated',
     'automation',
     'b2b',
     'base',
     'based',
     'bland',
     'booking',
     'bots',
     'brett',
     'building',
     'business',
     'case',
     'churn',
     'claude',
     'clay',
     'client',
     'clients',
     'cold',
     'com',
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
 10: {'15000',
      '30k',
      '5000',
      '50k',
      'aaa',
      'ada',
      'agency',
      'agent',
      'ai',
      'api',
      'appointment',
      'audit',
      'automate',
      'automated',
      'automation',
      'b2b',
      'base',
      'based',
      'bland',
      'booking',
      'bots',
      'brett',
      'building',
      'business',
      'case',
      'churn',
      'claude',
      'clay',
      'client',
      'clients',
      'cold',
      'com',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'15000',
      '30k',
      '5000',
      '50k',
      'aaa',
      'ada',
      'agency',
      'agent',
      'api',
      'appointment',
      'audit',
      'automated',
      'automation',
      'b2b',
      'base',
      'based',
      'bland',
      'booking',
      'bots',
      'brett',
      'building',
      'business',
      'case',
      'churn',
      'claude',
      'clay',
      'client',
      'clients',
      'cold',
      'com',
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
 12: {'15000',
      '30k',
      '5000',
      '50k',
      'aaa',
      'action',
      'ada',
      'agency',
      'agent',
      'api',
      'appointment',
      'audit',
      'automated',
      'automation',
      'b2b',
      'base',
      'based',
      'bland',
      'booking',
      'bots',
      'brett',
      'building',
      'business',
      'case',
      'churn',
      'claude',
      'clay',
      'client',
      'clients',
      'cold',
      'com',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Jordan Platten',
      'channel': 'Jordan Platten',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:22](https://www.youtube.com/watch?v=kDt9J3oinVs&t=142s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I made in the early stages. You never want to send cold email from your '
              "business domain. Okay, so let's say you're an agency business like me or you're "
              "some kind of service-based business. You're probably speaking to clients via a "
              'core email address.',
      'timestamp': 142,
      'timestamp_label': '[00:02:22]',
      'timestamp_seconds': 142,
      'tip': 'I made in the early stages. You never want to send cold email from your business '
             "domain. Okay, so let's say you're an agency business like me or you're some kind "
             "of service-based business. You're probably speaking to clients via a core email "
             'address.',
      'title': 'How I Send 3,000+ Cold Emails Every Day Using Instantly AI (Full Setup) '
               '(Jordan Platten)',
      'url': 'https://www.youtube.com/watch?v=kDt9J3oinVs&t=142s',
      'video_id': 'kDt9J3oinVs'},
     {'author': 'Sean Standberry',
      'channel': 'Sean Standberry',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:18](https://www.youtube.com/watch?v=5558JLgLk50&t=558s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This is what makes your service worth $1,000 per month. You're not just "
              "creating content. You're building a complete system that turns social media "
              'attention into real revenue for the client.',
      'timestamp': 558,
      'timestamp_label': '[00:09:18]',
      'timestamp_seconds': 558,
      'tip': "This is what makes your service worth $1,000 per month. You're not just creating "
             "content. You're building a complete system that turns social media attention "
             'into real revenue for the client.',
      'title': "NEW AI Agency Business Model I'm Using to Make $474,996/mo (Sean Standberry)",
      'url': 'https://www.youtube.com/watch?v=5558JLgLk50&t=558s',
      'video_id': '5558JLgLk50'},
     {'author': 'Nick Saraev Daily',
      'channel': 'Nick Saraev Daily',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:12](https://www.youtube.com/watch?v=Z5rSDEbn7wU&t=1332s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I have the rest of my day available obviously to service my my uh pre-existing '
              'client base for the agency stuff but also just to like focus on cool other '
              'stuff. Yeah, like like average workday the average person does eight hours a '
              "day, right? Like that's not that crazy.",
      'timestamp': 1332,
      'timestamp_label': '[00:22:12]',
      'timestamp_seconds': 1332,
      'tip': 'I have the rest of my day available obviously to service my my uh pre-existing '
             'client base for the agency stuff but also just to like focus on cool other '
             'stuff. Yeah, like like average workday the average person does eight hours a '
             "day, right? Like that's not that crazy.",
      'title': 'AI Automation Agency Retainer Model Explained (Nick Saraev Daily)',
      'url': 'https://www.youtube.com/watch?v=Z5rSDEbn7wU&t=1332s',
      'video_id': 'Z5rSDEbn7wU'},
     {'author': 'Jeff Sauer - Service Stacking',
      'channel': 'Jeff Sauer - Service Stacking',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=afaXZkksQs0&t=111s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So you keep track of these developments every day, but your clients are not in '
              "the weeds of the technology. They are busy building a business. They don't know "
              "the changes coming and going, and they're not reading Anthropic's model "
              'announcements.',
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': 'So you keep track of these developments every day, but your clients are not in '
             "the weeds of the technology. They are busy building a business. They don't know "
             "the changes coming and going, and they're not reading Anthropic's model "
             'announcements.',
      'title': 'Turn Your AI Skills Into Long-Term Clients (The 90-Day Method) (Jeff Sauer - '
               'Service Stacking)',
      'url': 'https://www.youtube.com/watch?v=afaXZkksQs0&t=111s',
      'video_id': 'afaXZkksQs0'},
     {'author': 'Andrew Dunn | AI Consulting',
      'channel': 'Andrew Dunn | AI Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:08](https://www.youtube.com/watch?v=LSmxwtNHu4k&t=428s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You have head head count and full org chart, right? You have every role that '
              'exists, marketing through to delivery, right? You have the current uh tool '
              'stack. You have the revenue model, how the business actually makes money, how '
              'they get clients, all that stuff.',
      'timestamp': 428,
      'timestamp_label': '[00:07:08]',
      'timestamp_seconds': 428,
      'tip': 'You have head head count and full org chart, right? You have every role that '
             'exists, marketing through to delivery, right? You have the current uh tool '
             'stack. You have the revenue model, how the business actually makes money, how '
             'they get clients, all that stuff.',
      'title': "I've Completed 200+ AI Audits, Copy This 7 Step Process (Andrew Dunn | AI "
               'Consulting)',
      'url': 'https://www.youtube.com/watch?v=LSmxwtNHu4k&t=428s',
      'video_id': 'LSmxwtNHu4k'},
     {'author': 'Ventra Technologies',
      'channel': 'Ventra Technologies',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=b5pi4BcdrKk&t=55s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s day, and solving it creates a massive B2B service opportunity. A business "
              'owner might think they can solve this by simply plugging a raw AI model '
              'directly into their website and letting it talk to customers. But raw AI models '
              'lack specific internal context.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': "'s day, and solving it creates a massive B2B service opportunity. A business "
             'owner might think they can solve this by simply plugging a raw AI model directly '
             'into their website and letting it talk to customers. But raw AI models lack '
             'specific internal context.',
      'title': 'How to Build an AI Customer Support Business (Ventra Technologies)',
      'url': 'https://www.youtube.com/watch?v=b5pi4BcdrKk&t=55s',
      'video_id': 'b5pi4BcdrKk'},
     {'author': 'Creative Crew with Brad Hussey',
      'channel': 'Creative Crew with Brad Hussey',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=o-UR3rkPgJ4&t=88s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I knew that I probably had a better chance of succeeding in that way than the '
              "other form of, you know, being a designer. So that's yeah, I was really just "
              "out of necessity to stand out. Who are design Joy's typical like target "
              'clients. I mean, the software as a service base.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'I knew that I probably had a better chance of succeeding in that way than the '
             "other form of, you know, being a designer. So that's yeah, I was really just out "
             "of necessity to stand out. Who are design Joy's typical like target clients. I "
             'mean, the software as a service base.',
      'title': 'This is How You Run a Profitable Design Service | Brett from DesignJoy '
               '(Creative Crew with Brad Hussey)',
      'url': 'https://www.youtube.com/watch?v=o-UR3rkPgJ4&t=88s',
      'video_id': 'o-UR3rkPgJ4'},
     {'author': 'company in progress',
      'channel': 'company in progress',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:44](https://www.youtube.com/watch?v=fSAazWLuDyQ&t=284s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It could be we've automated these five manual tasks or we've brought in this "
              "custom agent to help with customer support. So it's those types of things that "
              'we provide value in the platform itself. Um, meetings and collaboration.',
      'timestamp': 284,
      'timestamp_label': '[00:04:44]',
      'timestamp_seconds': 284,
      'tip': "It could be we've automated these five manual tasks or we've brought in this "
             "custom agent to help with customer support. So it's those types of things that "
             'we provide value in the platform itself. Um, meetings and collaboration.',
      'title': 'I Built an AI Audit That Replaces a $50,000 Consultant (company in progress)',
      'url': 'https://www.youtube.com/watch?v=fSAazWLuDyQ&t=284s',
      'video_id': 'fSAazWLuDyQ'},
     {'author': 'Jackson Rose | AI',
      'channel': 'Jackson Rose | AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:35](https://www.youtube.com/watch?v=OsFhqXe8aLI&t=335s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So I'm using a document about my business. And this is truly a document that "
              "I'm using for my actual business and running my AI automation consultant firm. "
              'I had spent a lot of time refining this document.',
      'timestamp': 335,
      'timestamp_label': '[00:05:35]',
      'timestamp_seconds': 335,
      'tip': "So I'm using a document about my business. And this is truly a document that I'm "
             'using for my actual business and running my AI automation consultant firm. I had '
             'spent a lot of time refining this document.',
      'title': 'I Built an AI Sales Agent that Sends 1,000+ Personalized Emails (Full '
               'Tutorial) (Jackson Rose | AI)',
      'url': 'https://www.youtube.com/watch?v=OsFhqXe8aLI&t=335s',
      'video_id': 'OsFhqXe8aLI'},
     {'author': 'Cresco International',
      'channel': 'Cresco International',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:41](https://www.youtube.com/watch?v=4Vt8Rgxszb4&t=161s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Second, it gives AI access to your private business knowledge without '
              'retraining the model. Third, updating information becomes dramatically faster. '
              'Instead of spending days or weeks retraining a model, organizations simply '
              'update their knowledge base.',
      'timestamp': 161,
      'timestamp_label': '[00:02:41]',
      'timestamp_seconds': 161,
      'tip': 'Second, it gives AI access to your private business knowledge without retraining '
             'the model. Third, updating information becomes dramatically faster. Instead of '
             'spending days or weeks retraining a model, organizations simply update their '
             'knowledge base.',
      'title': 'Everything You Need to Know About Retrieval-Augmented Generation (RAG) | '
               'Enterprise AI Explained (Cresco International)',
      'url': 'https://www.youtube.com/watch?v=4Vt8Rgxszb4&t=161s',
      'video_id': '4Vt8Rgxszb4'},
     {'author': 'WNT',
      'channel': 'WNT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:43](https://www.youtube.com/watch?v=A0tzwuw-nEg&t=403s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If your prompts are payment for service, then OpenAI's failure to quantify the "
              'value of that data or offer alternatives constitutes unfair business practice.',
      'timestamp': 403,
      'timestamp_label': '[00:06:43]',
      'timestamp_seconds': 403,
      'tip': "If your prompts are payment for service, then OpenAI's failure to quantify the "
             'value of that data or offer alternatives constitutes unfair business practice.',
      'title': "AI Reads OpenAI's Privacy Policy, Finds Data Trap | WNT #lawyer #openai (WNT)",
      'url': 'https://www.youtube.com/watch?v=A0tzwuw-nEg&t=403s',
      'video_id': 'A0tzwuw-nEg'},
     {'author': 'Cole Medin',
      'channel': 'Cole Medin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:26](https://www.youtube.com/watch?v=tLMViADvSNE&t=686s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For example, you might have a use case where you want the similarity to be '
              'based more on the sentiment versus the semantic similarity of the text. So for '
              'a pre-trained embedding model, my order was late is going to be similar to '
              'shipping was fast, right?',
      'timestamp': 686,
      'timestamp_label': '[00:11:26]',
      'timestamp_seconds': 686,
      'tip': 'For example, you might have a use case where you want the similarity to be based '
             'more on the sentiment versus the semantic similarity of the text. So for a '
             'pre-trained embedding model, my order was late is going to be similar to '
             'shipping was fast, right?',
      'title': 'Every RAG Strategy Explained in 13 Minutes (No Fluff) (Cole Medin)',
      'url': 'https://www.youtube.com/watch?v=tLMViADvSNE&t=686s',
      'video_id': 'tLMViADvSNE'},
     {'author': 'Everyday AI Automation',
      'channel': 'Everyday AI Automation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:37](https://www.youtube.com/watch?v=SrWNK0955xw&t=337s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Is this a high value opportunity? What category does the lead belong to? In N8N '
              'we might start with a form submission or another trigger. Then connect Google '
              'Sheets or another database. Send the lead information to the model.',
      'timestamp': 337,
      'timestamp_label': '[00:05:37]',
      'timestamp_seconds': 337,
      'tip': 'Is this a high value opportunity? What category does the lead belong to? In N8N '
             'we might start with a form submission or another trigger. Then connect Google '
             'Sheets or another database. Send the lead information to the model.',
      'title': 'Zapier vs Make vs n8n vs UiPath: What You Need to Know in 2026 (Everyday AI '
               'Automation)',
      'url': 'https://www.youtube.com/watch?v=SrWNK0955xw&t=337s',
      'video_id': 'SrWNK0955xw'},
     {'author': 'AI Automation Society',
      'channel': 'AI Automation Society',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=3XIdI6vcGz0&t=43s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Like, it's to me, it's more about like definitely above five, because at five "
              "you would have had to like actually build systems, right? It's more about the "
              'infrastructure of the business than it is like the head count or the revenue.',
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': "Like, it's to me, it's more about like definitely above five, because at five "
             "you would have had to like actually build systems, right? It's more about the "
             'infrastructure of the business than it is like the head count or the revenue.',
      'title': 'The Scope Creep Mistake That Can Wreck AI Projects (AI Automation Society)',
      'url': 'https://www.youtube.com/watch?v=3XIdI6vcGz0&t=43s',
      'video_id': '3XIdI6vcGz0'},
     {'author': 'Sabrina Ramonov 🍄',
      'channel': 'Sabrina Ramonov 🍄',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:26](https://www.youtube.com/watch?v=I1NSFLOBQvc&t=446s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Don't be sold on the dream of making 300,000 per month with an AI automation "
              'agency because I personally have not met one. So, maybe they exist out there, '
              "but they're certainly not solo, meaning revenue per employee is probably not as "
              'efficient as other business models.',
      'timestamp': 446,
      'timestamp_label': '[00:07:26]',
      'timestamp_seconds': 446,
      'tip': "Don't be sold on the dream of making 300,000 per month with an AI automation "
             'agency because I personally have not met one. So, maybe they exist out there, '
             "but they're certainly not solo, meaning revenue per employee is probably not as "
             'efficient as other business models.',
      'title': 'What Nobody Tells You About Selling AI Automations (Sabrina Ramonov 🍄)',
      'url': 'https://www.youtube.com/watch?v=I1NSFLOBQvc&t=446s',
      'video_id': 'I1NSFLOBQvc'}],
 2: [{'author': 'Automate AI Consulting',
      'channel': 'Automate AI Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:57](https://www.youtube.com/watch?v=m9wI5V0nSe0&t=477s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Something like building an AI lead qualification system for a real estate '
              'agent. Or setting up automated follow-up sequences for a coaching business. Or '
              'creating a customer intake workflow for a home services company. You build it, '
              'they pay you, done.',
      'timestamp': 477,
      'timestamp_label': '[00:07:57]',
      'timestamp_seconds': 477,
      'tip': 'Something like building an AI lead qualification system for a real estate agent. '
             'Or setting up automated follow-up sequences for a coaching business. Or creating '
             'a customer intake workflow for a home services company. You build it, they pay '
             'you, done.',
      'title': 'One-Time Projects vs Retainers: Which Gets You to $10K/Month? (Automate AI '
               'Consulting)',
      'url': 'https://www.youtube.com/watch?v=m9wI5V0nSe0&t=477s',
      'video_id': 'm9wI5V0nSe0'},
     {'author': 'Simply Contact',
      'channel': 'Simply Contact',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:02](https://www.youtube.com/watch?v=DcDfJRzuZNI&t=242s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It includes an AI agent for customer inquiries, an assistant for human agents, '
              'multilingual support, and advanced analytics. Pricing is performance-based, '
              'with a cost per resolved case and an additional monthly platform fee.',
      'timestamp': 242,
      'timestamp_label': '[00:04:02]',
      'timestamp_seconds': 242,
      'tip': 'It includes an AI agent for customer inquiries, an assistant for human agents, '
             'multilingual support, and advanced analytics. Pricing is performance-based, with '
             'a cost per resolved case and an additional monthly platform fee.',
      'title': 'Top 10 AI Customer Service Companies (Simply Contact)',
      'url': 'https://www.youtube.com/watch?v=DcDfJRzuZNI&t=242s',
      'video_id': 'DcDfJRzuZNI'},
     {'author': 'Rocket Research',
      'channel': 'Rocket Research',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=swIGkbLXEdM&t=70s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Zenesk offers annual plans starting at $19 per agent per month with monthly '
              'rates higher at $25. AI agents are included in suite and support plans, but '
              'come with usage based fees of about $1. 50 to $2 per automated resolution.',
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': 'Zenesk offers annual plans starting at $19 per agent per month with monthly '
             'rates higher at $25. AI agents are included in suite and support plans, but come '
             'with usage based fees of about $1. 50 to $2 per automated resolution.',
      'title': 'How Much Should a Small Business Budget for AI Customer Support in 2026? '
               '(Rocket Research)',
      'url': 'https://www.youtube.com/watch?v=swIGkbLXEdM&t=70s',
      'video_id': 'swIGkbLXEdM'},
     {'author': 'Automate AI Consulting',
      'channel': 'Automate AI Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:15](https://www.youtube.com/watch?v=91lw5ubtLMc&t=135s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They just want you to handle it all. In that case, you host the workflow in '
              'your account and just charge a monthly maintenance fee. This usually happens '
              "with retainer clients, the ones where you're building and improving workflows "
              'month over month.',
      'timestamp': 135,
      'timestamp_label': '[00:02:15]',
      'timestamp_seconds': 135,
      'tip': 'They just want you to handle it all. In that case, you host the workflow in your '
             'account and just charge a monthly maintenance fee. This usually happens with '
             "retainer clients, the ones where you're building and improving workflows month "
             'over month.',
      'title': 'How To Deliver Your N8N Automation To Clients Like An Expert (Automate AI '
               'Consulting)',
      'url': 'https://www.youtube.com/watch?v=91lw5ubtLMc&t=135s',
      'video_id': '91lw5ubtLMc'},
     {'author': 'Noah Epstein',
      'channel': 'Noah Epstein',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:49](https://www.youtube.com/watch?v=fMdUS6amki0&t=289s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, if you are struggling, please go in there. I'm more than happy to help and "
              "I'm looking forward to helping. So, it's as simple as that. Find a business "
              'willing to pay, get the money, and go about building the automation.',
      'timestamp': 289,
      'timestamp_label': '[00:04:49]',
      'timestamp_seconds': 289,
      'tip': "So, if you are struggling, please go in there. I'm more than happy to help and "
             "I'm looking forward to helping. So, it's as simple as that. Find a business "
             'willing to pay, get the money, and go about building the automation.',
      'title': 'How I made $150k last month selling AI automations (Noah Epstein)',
      'url': 'https://www.youtube.com/watch?v=fMdUS6amki0&t=289s',
      'video_id': 'fMdUS6amki0'},
     {'author': 'Nick Saraev Daily',
      'channel': 'Nick Saraev Daily',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:39](https://www.youtube.com/watch?v=0QI9KoizfH8&t=99s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For example, do I have to pay monthly for NA and others for each client I have? '
              'Whereas, if the client is the one paying, how would the specifics work, for an '
              'example, a client buys it and how they trust me to handle it with their payment '
              'details, etc.',
      'timestamp': 99,
      'timestamp_label': '[00:01:39]',
      'timestamp_seconds': 99,
      'tip': 'For example, do I have to pay monthly for NA and others for each client I have? '
             'Whereas, if the client is the one paying, how would the specifics work, for an '
             'example, a client buys it and how they trust me to handle it with their payment '
             'details, etc.',
      'title': 'Building a profitable AI agency cold email campaign in 40min (Nick Saraev '
               'Daily)',
      'url': 'https://www.youtube.com/watch?v=0QI9KoizfH8&t=99s',
      'video_id': '0QI9KoizfH8'},
     {'author': 'Kelsey Hastie',
      'channel': 'Kelsey Hastie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=cqaukVEOmJ4&t=59s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Do not expose an insecure learning setup to the internet. Our example is a '
              'website audit request. The output is a reviewed internal draft, not a quote, '
              'contract, or automatic customer reply. Section 2, capture and validate the '
              'request.',
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': 'Do not expose an insecure learning setup to the internet. Our example is a '
             'website audit request. The output is a reviewed internal draft, not a quote, '
             'contract, or automatic customer reply. Section 2, capture and validate the '
             'request.',
      'title': 'n8n Beginner Tutorial: AI Lead Intake Automation (Free Self-Hosted Option) '
               '(Kelsey Hastie)',
      'url': 'https://www.youtube.com/watch?v=cqaukVEOmJ4&t=59s',
      'video_id': 'cqaukVEOmJ4'},
     {'author': 'Global Technology Industry Association (GTIA)',
      'channel': 'Global Technology Industry Association (GTIA)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:15](https://www.youtube.com/watch?v=TtU19Z-ASZk&t=195s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Like no one understands that every project is kind of on its way to some sort '
              'of hiccup. And so, bad dates unfortunately contaminate the entire business '
              'intelligence pipeline for their business, their customer communications, their '
              'scheduling, scheduling churn.',
      'timestamp': 195,
      'timestamp_label': '[00:03:15]',
      'timestamp_seconds': 195,
      'tip': 'Like no one understands that every project is kind of on its way to some sort of '
             'hiccup. And so, bad dates unfortunately contaminate the entire business '
             'intelligence pipeline for their business, their customer communications, their '
             'scheduling, scheduling churn.',
      'title': 'Project Risk, Scope Creep, and AI Automation for MSPs (Global Technology '
               'Industry Association (GTIA))',
      'url': 'https://www.youtube.com/watch?v=TtU19Z-ASZk&t=195s',
      'video_id': 'TtU19Z-ASZk'},
     {'author': 'Tom Hartnell',
      'channel': 'Tom Hartnell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=WFW7vb6wXZM&t=51s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '"We\'ve done this AI audit, and now it makes it a really easy decision for them '
              'to go into development." Let\'s look into the reasons of why we actually want '
              "to do an AI audit. So, if you're coming from the perspective of an AI agency, "
              "there's a few different reasons.",
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': '"We\'ve done this AI audit, and now it makes it a really easy decision for them '
             'to go into development." Let\'s look into the reasons of why we actually want to '
             "do an AI audit. So, if you're coming from the perspective of an AI agency, "
             "there's a few different reasons.",
      'title': 'How to Perform an AI Audit in 2026 (Step-by-Step Framework) (Tom Hartnell)',
      'url': 'https://www.youtube.com/watch?v=WFW7vb6wXZM&t=51s',
      'video_id': 'WFW7vb6wXZM'},
     {'author': 'Stewart Gauld',
      'channel': 'Stewart Gauld',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:03](https://www.youtube.com/watch?v=nMMWXxBsH2o&t=123s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Think about an AI agent as a customer service representative for your business '
              'that works 24/7 to enhance your customers experiences across your different '
              'channels. The great thing is you can launch your AI agents in just a few '
              'minutes with Zenesk.',
      'timestamp': 123,
      'timestamp_label': '[00:02:03]',
      'timestamp_seconds': 123,
      'tip': 'Think about an AI agent as a customer service representative for your business '
             'that works 24/7 to enhance your customers experiences across your different '
             'channels. The great thing is you can launch your AI agents in just a few minutes '
             'with Zenesk.',
      'title': 'How to use ZenDesk AI Agents | Supercharge Customer Service with AI in 2026 '
               '(Stewart Gauld)',
      'url': 'https://www.youtube.com/watch?v=nMMWXxBsH2o&t=123s',
      'video_id': 'nMMWXxBsH2o'},
     {'author': 'Zendesk',
      'channel': 'Zendesk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=mnFYeyoS2r8&t=21s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "These aren't your typical bots. AI agents don't just provide quick responses to "
              'customer questions. They actually resolve customer issues from end to end '
              'without the help of a live agent, handling both simple and complex queries with '
              'ease.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "These aren't your typical bots. AI agents don't just provide quick responses to "
             'customer questions. They actually resolve customer issues from end to end '
             'without the help of a live agent, handling both simple and complex queries with '
             'ease.',
      'title': 'AI Agents: The next generation of AI-powered bots | Zendesk (Zendesk)',
      'url': 'https://www.youtube.com/watch?v=mnFYeyoS2r8&t=21s',
      'video_id': 'mnFYeyoS2r8'},
     {'author': 'Innovative Compass Consulting',
      'channel': 'Innovative Compass Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:42](https://www.youtube.com/watch?v=DIfo9jAMZYY&t=222s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s right for what you're doing, especially before you go and publish something "
              "or make a big decision based on it. This one's huge and it's all about "
              "transparency. You can't pass off AI generated content as if it were written by "
              'a person.',
      'timestamp': 222,
      'timestamp_label': '[00:03:42]',
      'timestamp_seconds': 222,
      'tip': "'s right for what you're doing, especially before you go and publish something "
             "or make a big decision based on it. This one's huge and it's all about "
             "transparency. You can't pass off AI generated content as if it were written by a "
             'person.',
      'title': "OpenAI's Policies Explained: EU Privacy, Security, Safety, and Your Data "
               'Rights (ChatGPT, Sora,API) (Innovative Compass Consulting)',
      'url': 'https://www.youtube.com/watch?v=DIfo9jAMZYY&t=222s',
      'video_id': 'DIfo9jAMZYY'},
     {'author': "Owner's Bot Lab",
      'channel': "Owner's Bot Lab",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:29](https://www.youtube.com/watch?v=EtiRX0GduSI&t=29s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Only one of them was actually easy. Here's the job in plain English. Our test "
              "business is Brightside Plumbing and Drain. It's made up, same as last video. A "
              'customer fills out the quote form.',
      'timestamp': 29,
      'timestamp_label': '[00:00:29]',
      'timestamp_seconds': 29,
      'tip': "Only one of them was actually easy. Here's the job in plain English. Our test "
             "business is Brightside Plumbing and Drain. It's made up, same as last video. A "
             'customer fills out the quote form.',
      'title': 'I Built the Same AI Lead Responder in Zapier, Make and n8n (Only One Was Easy) '
               "(Owner's Bot Lab)",
      'url': 'https://www.youtube.com/watch?v=EtiRX0GduSI&t=29s',
      'video_id': 'EtiRX0GduSI'},
     {'author': 'Serop | AI Automation',
      'channel': 'Serop | AI Automation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=u-qrX9uP_t4&t=38s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So here in my case, I'm on the free membership, so it's fine because I'm not "
              'using any proprietary data, And now the people are mentioning like, is this an '
              'isolated issue that happened to this person or this is a widespread behavior?',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': "So here in my case, I'm on the free membership, so it's fine because I'm not "
             'using any proprietary data, And now the people are mentioning like, is this an '
             'isolated issue that happened to this person or this is a widespread behavior?',
      'title': "OpenAI's Secret Data Training: What You Need To Know (Serop | AI Automation)",
      'url': 'https://www.youtube.com/watch?v=u-qrX9uP_t4&t=38s',
      'video_id': 'u-qrX9uP_t4'},
     {'author': 'Austin Reed',
      'channel': 'Austin Reed',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:12](https://www.youtube.com/watch?v=mw1V2GoYHsk&t=132s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In that case, you can deploy a server under your own hosting account and charge '
              'them a monthly maintenance fee to keep that server alive. Usually, this '
              "scenario happens when you have a monthly retainer client, where you're "
              'constantly building and improving new workflows.',
      'timestamp': 132,
      'timestamp_label': '[00:02:12]',
      'timestamp_seconds': 132,
      'tip': 'In that case, you can deploy a server under your own hosting account and charge '
             'them a monthly maintenance fee to keep that server alive. Usually, this scenario '
             "happens when you have a monthly retainer client, where you're constantly "
             'building and improving new workflows.',
      'title': 'How to Deliver Your n8n Project to Clients Like a PRO! (Austin Reed)',
      'url': 'https://www.youtube.com/watch?v=mw1V2GoYHsk&t=132s',
      'video_id': 'mw1V2GoYHsk'}],
 3: [{'author': 'The AI Blueprint',
      'channel': 'The AI Blueprint',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:42](https://www.youtube.com/watch?v=1mZ0bWq9y-M&t=162s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Full end-to-end CRM and customer support automation for $3,000 setup and $1,500 '
              'per month. Just five active clients puts you at $7,500 in predictable monthly '
              'cash flow. To get your first paying client in under 10 days, you do not need '
              'cold calls or paid ads.',
      'timestamp': 162,
      'timestamp_label': '[00:02:42]',
      'timestamp_seconds': 162,
      'tip': 'Full end-to-end CRM and customer support automation for $3,000 setup and $1,500 '
             'per month. Just five active clients puts you at $7,500 in predictable monthly '
             'cash flow. To get your first paying client in under 10 days, you do not need '
             'cold calls or paid ads.',
      'title': 'How to Build an AI Automation Agency with n8n and AI Agents (2026 Masterclass) '
               '(The AI Blueprint)',
      'url': 'https://www.youtube.com/watch?v=1mZ0bWq9y-M&t=162s',
      'video_id': '1mZ0bWq9y-M'},
     {'author': 'ArriSse Corp',
      'channel': 'ArriSse Corp',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=XKoGenFWVHs&t=56s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Without an operational layer dictating the terms of engagement, an agency '
              'effectively surrenders its profit margins to the unpredictable behavioral '
              'quirks of every new client. In high-ticket B2B engagements, client excitement '
              'does not peak during project delivery.',
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': 'Without an operational layer dictating the terms of engagement, an agency '
             'effectively surrenders its profit margins to the unpredictable behavioral quirks '
             'of every new client. In high-ticket B2B engagements, client excitement does not '
             'peak during project delivery.',
      'title': 'The Exact System Boutique Agencies Use to Stop Scope Creep & Close $5k/mo '
               'Retainers (ArriSse Corp)',
      'url': 'https://www.youtube.com/watch?v=XKoGenFWVHs&t=56s',
      'video_id': 'XKoGenFWVHs'},
     {'author': 'LearnAI Today',
      'channel': 'LearnAI Today',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:01](https://www.youtube.com/watch?v=Pd96DxQ36U8&t=181s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Make's integrations page lists more than 3,000 apps plus an HTTP module for "
              'connecting to almost any service with an API. On AI, Make offers Make AI agents '
              "on all plans plus integrations for OpenAI, Google Gemini, and Anthropic's "
              'Claude. Pricing is based on credits.',
      'timestamp': 181,
      'timestamp_label': '[00:03:01]',
      'timestamp_seconds': 181,
      'tip': "Make's integrations page lists more than 3,000 apps plus an HTTP module for "
             'connecting to almost any service with an API. On AI, Make offers Make AI agents '
             "on all plans plus integrations for OpenAI, Google Gemini, and Anthropic's "
             'Claude. Pricing is based on credits.',
      'title': 'Zapier vs Make vs n8n (2026): Which Automation Tool Should You Use? (LearnAI '
               'Today)',
      'url': 'https://www.youtube.com/watch?v=Pd96DxQ36U8&t=181s',
      'video_id': 'Pd96DxQ36U8'},
     {'author': 'Whizz AI',
      'channel': 'Whizz AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:43](https://www.youtube.com/watch?v=Pz3jLYQwsX4&t=223s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The catch with Make is that the price depends on how many modules you use. A '
              'long scenario costs more on every run, because every module counts. Pick Make '
              'if you want a visual builder, a low monthly cost, and you are building '
              'workflows with several steps that run often.',
      'timestamp': 223,
      'timestamp_label': '[00:03:43]',
      'timestamp_seconds': 223,
      'tip': 'The catch with Make is that the price depends on how many modules you use. A '
             'long scenario costs more on every run, because every module counts. Pick Make if '
             'you want a visual builder, a low monthly cost, and you are building workflows '
             'with several steps that run often.',
      'title': 'n8n vs Zapier vs Make (2026): Which AI Automation Tool Is Actually Worth It? '
               '(Whizz AI)',
      'url': 'https://www.youtube.com/watch?v=Pz3jLYQwsX4&t=223s',
      'video_id': 'Pz3jLYQwsX4'},
     {'author': 'Anthony Shoosh',
      'channel': 'Anthony Shoosh',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:23](https://www.youtube.com/watch?v=S5UwzzP_Qec&t=563s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Go into the knowledgeb section and select the knowledge base that you have '
              'configured for that business. Moving down to audio, this is one of my favorite '
              'sections because this provides so much naturalness to the phone call. Bland '
              'lets you add background audio.',
      'timestamp': 563,
      'timestamp_label': '[00:09:23]',
      'timestamp_seconds': 563,
      'tip': 'Go into the knowledgeb section and select the knowledge base that you have '
             'configured for that business. Moving down to audio, this is one of my favorite '
             'sections because this provides so much naturalness to the phone call. Bland lets '
             'you add background audio.',
      'title': 'Bland AI Basics: Everything You Need to Start Building Voice Agents (Anthony '
               'Shoosh)',
      'url': 'https://www.youtube.com/watch?v=S5UwzzP_Qec&t=563s',
      'video_id': 'S5UwzzP_Qec'},
     {'author': 'Liam Ottley',
      'channel': 'Liam Ottley',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:09](https://www.youtube.com/watch?v=oB7gia1kC_g&t=369s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "All right, so let's talk about what we're going to be building here. It's an AI "
              'receptionist for our friend Sarah that does three things. Firstly, answers '
              "questions about the business. It's going to be pricing, location, hours, "
              'services.',
      'timestamp': 369,
      'timestamp_label': '[00:06:09]',
      'timestamp_seconds': 369,
      'tip': "All right, so let's talk about what we're going to be building here. It's an AI "
             'receptionist for our friend Sarah that does three things. Firstly, answers '
             "questions about the business. It's going to be pricing, location, hours, "
             'services.',
      'title': 'From Zero to Your First AI Voice Agent in 18 Minutes (No Coding) (Liam Ottley)',
      'url': 'https://www.youtube.com/watch?v=oB7gia1kC_g&t=369s',
      'video_id': 'oB7gia1kC_g'},
     {'author': 'Alejo Pijuan',
      'channel': 'Alejo Pijuan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:14](https://www.youtube.com/watch?v=6Fal62hzEs8&t=254s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t just cost money, they destroy client relationships. Because a lot of the "
              "times these platform failures aren't the voice agent said a word that it "
              "shouldn't have that you can fix with your prompt. You can give your client a "
              'solution.',
      'timestamp': 254,
      'timestamp_label': '[00:04:14]',
      'timestamp_seconds': 254,
      'tip': "'t just cost money, they destroy client relationships. Because a lot of the "
             "times these platform failures aren't the voice agent said a word that it "
             "shouldn't have that you can fix with your prompt. You can give your client a "
             'solution.',
      'title': 'The Best Platform for your Voice AI Agency: Retell vs Vapi (Alejo Pijuan)',
      'url': 'https://www.youtube.com/watch?v=6Fal62hzEs8&t=254s',
      'video_id': '6Fal62hzEs8'},
     {'author': 'Venture Harbour',
      'channel': 'Venture Harbour',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:19](https://www.youtube.com/watch?v=ZVSDm5siKr4&t=739s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So depending on what's important to you for your use case, you can have a bit "
              'of a play around and see if you can reduce cost, reduce latency, or improve '
              "quality depending what you're noticing is kind of lacking with your agent.",
      'timestamp': 739,
      'timestamp_label': '[00:12:19]',
      'timestamp_seconds': 739,
      'tip': "So depending on what's important to you for your use case, you can have a bit of "
             'a play around and see if you can reduce cost, reduce latency, or improve quality '
             "depending what you're noticing is kind of lacking with your agent.",
      'title': 'Build a Voice Agent in 15 Minutes Using VAPI (Easiest Tutorial) (Venture '
               'Harbour)',
      'url': 'https://www.youtube.com/watch?v=ZVSDm5siKr4&t=739s',
      'video_id': 'ZVSDm5siKr4'},
     {'author': 'Andrew Dunn | AI Consulting',
      'channel': 'Andrew Dunn | AI Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:27](https://www.youtube.com/watch?v=HPGSE4LXaQA&t=447s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '15,000 feel like an absolute bargain to the correct client. The secret to '
              "premium pricing isn't justifying the time investment. It's quantifying the "
              'business impact and risk mitigation to the end client.',
      'timestamp': 447,
      'timestamp_label': '[00:07:27]',
      'timestamp_seconds': 447,
      'tip': '15,000 feel like an absolute bargain to the correct client. The secret to '
             "premium pricing isn't justifying the time investment. It's quantifying the "
             'business impact and risk mitigation to the end client.',
      'title': "Don't Sell AI Workflows, Sell AI Audits (Massive Opportunity) (Andrew Dunn | "
               'AI Consulting)',
      'url': 'https://www.youtube.com/watch?v=HPGSE4LXaQA&t=447s',
      'video_id': 'HPGSE4LXaQA'},
     {'author': 'ToThePoint Guide',
      'channel': 'ToThePoint Guide',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=pMdWgl-3ihA&t=36s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's cost effective for the pricing plans when you're going to find here. 07 "
              "per minute, but it uses 11 laps. So that's something that you have to be aware "
              'of. And it offers like $2 a month for phone numbers.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': "It's cost effective for the pricing plans when you're going to find here. 07 per "
             "minute, but it uses 11 laps. So that's something that you have to be aware of. "
             'And it offers like $2 a month for phone numbers.',
      'title': 'Best AI Voice Agent 2025: Retell vs Vapi vs Bland vs Synthflow vs ElevenLabs '
               'vs Play AI vs Air AI vs (ToThePoint Guide)',
      'url': 'https://www.youtube.com/watch?v=pMdWgl-3ihA&t=36s',
      'video_id': 'pMdWgl-3ihA'},
     {'author': 'Bryan Taylor',
      'channel': 'Bryan Taylor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:33](https://www.youtube.com/watch?v=yLxvwa45vR8&t=213s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And for them, maybe 30,000 is not a lot of money, but the the the creep of that '
              'was was huge in in relation to what we thought we were building, right? Cuz we '
              "thought, well, we're going to give this away. It's not going to cost anything.",
      'timestamp': 213,
      'timestamp_label': '[00:03:33]',
      'timestamp_seconds': 213,
      'tip': 'And for them, maybe 30,000 is not a lot of money, but the the the creep of that '
             'was was huge in in relation to what we thought we were building, right? Cuz we '
             "thought, well, we're going to give this away. It's not going to cost anything.",
      'title': 'Custom Software Development Pitfalls: Scope Creep, AI Dependence, and Uncapped '
               'API Costs (Bryan Taylor)',
      'url': 'https://www.youtube.com/watch?v=yLxvwa45vR8&t=213s',
      'video_id': 'yLxvwa45vR8'},
     {'author': 'WPTuts',
      'channel': 'WPTuts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=UgtrG88EDhU&t=72s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now this could be possible based upon technical limitations different pricing '
              "limitations Or the fact you just don't have the time to add in new features "
              'right now This thing gives you the ability to be flexible, but also do you tell '
              'the person where possible?',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': 'Now this could be possible based upon technical limitations different pricing '
             "limitations Or the fact you just don't have the time to add in new features "
             'right now This thing gives you the ability to be flexible, but also do you tell '
             'the person where possible?',
      'title': 'How to Handle Scope Creep in Client Projects (WPTuts)',
      'url': 'https://www.youtube.com/watch?v=UgtrG88EDhU&t=72s',
      'video_id': 'UgtrG88EDhU'},
     {'author': 'freeCodeCamp.org',
      'channel': 'freeCodeCamp.org',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[03:24:57](https://www.youtube.com/watch?v=mHxLXzYjQRE&t=12297s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'PG uh Vector managed about 35, PG vector self is about $20. Very uh similar '
              'price range. Now look what happens when we go to 5 million. Now things are '
              'starting to change a little bit. You can see that in this case $400 for Pine '
              'Cone.',
      'timestamp': 12297,
      'timestamp_label': '[03:24:57]',
      'timestamp_seconds': 12297,
      'tip': 'PG uh Vector managed about 35, PG vector self is about $20. Very uh similar '
             'price range. Now look what happens when we go to 5 million. Now things are '
             'starting to change a little bit. You can see that in this case $400 for Pine '
             'Cone.',
      'title': 'Production RAG with LangChain & Vector Databases – Full Course '
               '(freeCodeCamp.org)',
      'url': 'https://www.youtube.com/watch?v=mHxLXzYjQRE&t=12297s',
      'video_id': 'mHxLXzYjQRE'},
     {'author': 'I Make it Simple',
      'channel': 'I Make it Simple',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=uSh76GAmtwM&t=111s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'One, sell a product, not your time. A clear price, a clear process, a clear '
              'result. Two, start cheap and raise the price while demand keeps saying yes. No '
              "calls, no meetings, no contracts. But be honest with yourself. Christo's "
              'warning was simple.',
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': 'One, sell a product, not your time. A clear price, a clear process, a clear '
             'result. Two, start cheap and raise the price while demand keeps saying yes. No '
             "calls, no meetings, no contracts. But be honest with yourself. Christo's warning "
             'was simple.',
      'title': 'This Designer Makes $2M a Year With ZERO Employees (Designjoy Explained '
               'Simply) (I Make it Simple)',
      'url': 'https://www.youtube.com/watch?v=uSh76GAmtwM&t=111s',
      'video_id': 'uSh76GAmtwM'},
     {'author': 'Rocket Research',
      'channel': 'Rocket Research',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=swIGkbLXEdM&t=83s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '50 to $2 per automated resolution. Additional AI features like Copilot add '
              'about $50 per agent monthly. This combination of seat and per resolution '
              'pricing can increase costs quickly for growing teams with high AI usage.',
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': '50 to $2 per automated resolution. Additional AI features like Copilot add about '
             '$50 per agent monthly. This combination of seat and per resolution pricing can '
             'increase costs quickly for growing teams with high AI usage.',
      'title': 'How Much Should a Small Business Budget for AI Customer Support in 2026? '
               '(Rocket Research)',
      'url': 'https://www.youtube.com/watch?v=swIGkbLXEdM&t=83s',
      'video_id': 'swIGkbLXEdM'}],
 4: [{'author': 'Johnny',
      'channel': 'Johnny',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=MlJ3XSy3k7A&t=100s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And guys, the the interesting thing is that I got this client through this '
              'system that I run in my own business. This is the second case study I want to '
              'break down for you. He owns an AI automation agency. Now this guy is selling '
              'this using it if that makes sense.',
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': 'And guys, the the interesting thing is that I got this client through this '
             'system that I run in my own business. This is the second case study I want to '
             'break down for you. He owns an AI automation agency. Now this guy is selling '
             'this using it if that makes sense.',
      'title': 'How To Book Sales Calls For Your Agency With AI Cold Email Outreach (Johnny)',
      'url': 'https://www.youtube.com/watch?v=MlJ3XSy3k7A&t=100s',
      'video_id': 'MlJ3XSy3k7A'},
     {'author': 'Bo Sar',
      'channel': 'Bo Sar',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:36](https://www.youtube.com/watch?v=pba8FIkOilY&t=96s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Don't give the client a recruitment dashboard. Give them a hired employee. "
              "Don't give them like billing software, give them a resolved insurance claim. "
              'Don\'t give them an automation workflow, give them the results.".',
      'timestamp': 96,
      'timestamp_label': '[00:01:36]',
      'timestamp_seconds': 96,
      'tip': "Don't give the client a recruitment dashboard. Give them a hired employee. Don't "
             "give them like billing software, give them a resolved insurance claim. Don't "
             'give them an automation workflow, give them the results.".',
      'title': 'The AI-First Agency Model YC Just Revealed (6 services to sell) (Bo Sar)',
      'url': 'https://www.youtube.com/watch?v=pba8FIkOilY&t=96s',
      'video_id': 'pba8FIkOilY'},
     {'author': 'Nate Herk | AI Automation',
      'channel': 'Nate Herk | AI Automation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:23](https://www.youtube.com/watch?v=xxARTGo_Oqg&t=143s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So if you're doing client work, this is what I recommend pretty much all the "
              'time. Option two is you host nitn but only for your own agency. So in this '
              'setup you run nitn on your own server but nobody else sees it except for your '
              'business.',
      'timestamp': 143,
      'timestamp_label': '[00:02:23]',
      'timestamp_seconds': 143,
      'tip': "So if you're doing client work, this is what I recommend pretty much all the "
             'time. Option two is you host nitn but only for your own agency. So in this setup '
             'you run nitn on your own server but nobody else sees it except for your '
             'business.',
      'title': 'How to Actually Deliver AI Projects (APIs, Hosting & Handover Explained) (Nate '
               'Herk | AI Automation)',
      'url': 'https://www.youtube.com/watch?v=xxARTGo_Oqg&t=143s',
      'video_id': 'xxARTGo_Oqg'},
     {'author': 'Mert Yerlikaya',
      'channel': 'Mert Yerlikaya',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:05](https://www.youtube.com/watch?v=1leregs81ik&t=605s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'AI tools to selling high value business outcome, a transformation. This is how '
              "we have scaled Mong AI group and it's how you can build incredible value. "
              "Whether you're implementing AI in your own company or building an AI agency, "
              'now you have two paths from here.',
      'timestamp': 605,
      'timestamp_label': '[00:10:05]',
      'timestamp_seconds': 605,
      'tip': 'AI tools to selling high value business outcome, a transformation. This is how '
             "we have scaled Mong AI group and it's how you can build incredible value. "
             "Whether you're implementing AI in your own company or building an AI agency, now "
             'you have two paths from here.',
      'title': 'How I Sell $10,000 AI Audits (Our EXACT 5-Step Process) (Mert Yerlikaya)',
      'url': 'https://www.youtube.com/watch?v=1leregs81ik&t=605s',
      'video_id': '1leregs81ik'},
     {'author': 'Just Kristers',
      'channel': 'Just Kristers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:39](https://www.youtube.com/watch?v=G1O3xtJW6hY&t=159s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Zenesk setup and customer touch points. Make your selections carefully based on '
              "where you want automated support to be available. After you've chosen the "
              'appropriate locations, click publish AI agent. Your chatbot is now live and '
              'ready to assist your customers automatically.',
      'timestamp': 159,
      'timestamp_label': '[00:02:39]',
      'timestamp_seconds': 159,
      'tip': 'Zenesk setup and customer touch points. Make your selections carefully based on '
             "where you want automated support to be available. After you've chosen the "
             'appropriate locations, click publish AI agent. Your chatbot is now live and '
             'ready to assist your customers automatically.',
      'title': 'How To Set Up Zendesk AI Chatbot (Tutorial 2026) (Just Kristers)',
      'url': 'https://www.youtube.com/watch?v=G1O3xtJW6hY&t=159s',
      'video_id': 'G1O3xtJW6hY'},
     {'author': 'Voice AI Decoded',
      'channel': 'Voice AI Decoded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:55](https://www.youtube.com/watch?v=HFuJC6Bi11o&t=415s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'API keys and pay them directly rather than it will go through Vappy. So here '
              'just as an example, we got five kind of leading voice AI platforms. This is '
              'based on 3,000 call minutes per month on a typical stack. 1, Deepseek, Nova or '
              'Deepseek Flux and 11 Labs Turbo V2.',
      'timestamp': 415,
      'timestamp_label': '[00:06:55]',
      'timestamp_seconds': 415,
      'tip': 'API keys and pay them directly rather than it will go through Vappy. So here '
             'just as an example, we got five kind of leading voice AI platforms. This is '
             'based on 3,000 call minutes per month on a typical stack. 1, Deepseek, Nova or '
             'Deepseek Flux and 11 Labs Turbo V2.',
      'title': 'VAPI vs Bland AI – I built the same voice agent on both (Voice AI Decoded)',
      'url': 'https://www.youtube.com/watch?v=HFuJC6Bi11o&t=415s',
      'video_id': 'HFuJC6Bi11o'},
     {'author': 'Jacob Kaz',
      'channel': 'Jacob Kaz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:32](https://www.youtube.com/watch?v=agtVZpDDGmU&t=632s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, anyh who, following that, the next steps are very easy as well. You have '
              'the onboarding calls, the campaign setup, the AI agent setup, AI caller. All '
              'these things take a com like maybe combined like 10 20 minutes.',
      'timestamp': 632,
      'timestamp_label': '[00:10:32]',
      'timestamp_seconds': 632,
      'tip': 'So, anyh who, following that, the next steps are very easy as well. You have the '
             'onboarding calls, the campaign setup, the AI agent setup, AI caller. All these '
             'things take a com like maybe combined like 10 20 minutes.',
      'title': 'How i built an AI Agency that makes me 100k/mo with no money (with proof) '
               '(Jacob Kaz)',
      'url': 'https://www.youtube.com/watch?v=agtVZpDDGmU&t=632s',
      'video_id': 'agtVZpDDGmU'},
     {'author': 'The Workbench',
      'channel': 'The Workbench',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:15](https://www.youtube.com/watch?v=NT0JXm1lCyE&t=555s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We do a lot of scraping through different proxies to get lists but what what's "
              'your tech stack Ian? How how do you stand up outbound for your for your uh your '
              "clients? So it's actually a lot of proprietary tools that we use. So we "
              'actually developed a lot.',
      'timestamp': 555,
      'timestamp_label': '[00:09:15]',
      'timestamp_seconds': 555,
      'tip': "We do a lot of scraping through different proxies to get lists but what what's "
             'your tech stack Ian? How how do you stand up outbound for your for your uh your '
             "clients? So it's actually a lot of proprietary tools that we use. So we actually "
             'developed a lot.',
      'title': 'How Cold Email Landed $60k Home Service Deals | The Workbench (The Workbench)',
      'url': 'https://www.youtube.com/watch?v=NT0JXm1lCyE&t=555s',
      'video_id': 'NT0JXm1lCyE'},
     {'author': 'Andrew Dunn | AI Consulting',
      'channel': 'Andrew Dunn | AI Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:57](https://www.youtube.com/watch?v=AG_L5ecwXkU&t=297s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, we are grouping together the processes. So, in this case, we've got lead "
              "generation capture. We've got qualification, discovery, and closing. We then go "
              'to delivery, which is pre-delivery setup, strategy, production, '
              'post-production, client delivery.',
      'timestamp': 297,
      'timestamp_label': '[00:04:57]',
      'timestamp_seconds': 297,
      'tip': "So, we are grouping together the processes. So, in this case, we've got lead "
             "generation capture. We've got qualification, discovery, and closing. We then go "
             'to delivery, which is pre-delivery setup, strategy, production, post-production, '
             'client delivery.',
      'title': 'How to Perform a $15,000 AI Audit (Beginner’s Guide) (Andrew Dunn | AI '
               'Consulting)',
      'url': 'https://www.youtube.com/watch?v=AG_L5ecwXkU&t=297s',
      'video_id': 'AG_L5ecwXkU'},
     {'author': 'CX Foundation',
      'channel': 'CX Foundation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:21](https://www.youtube.com/watch?v=-j4XDojlGLc&t=81s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, what brings you to the wonderful world of Bland AI today? Are you looking '
              'to build something cool or just checking things out? Well, I actually had a '
              "question. I'm interested in buying, um, but here's the thing. I have a pretty "
              'tight budget and a pretty strict timeline.',
      'timestamp': 81,
      'timestamp_label': '[00:01:21]',
      'timestamp_seconds': 81,
      'tip': 'So, what brings you to the wonderful world of Bland AI today? Are you looking to '
             'build something cool or just checking things out? Well, I actually had a '
             "question. I'm interested in buying, um, but here's the thing. I have a pretty "
             'tight budget and a pretty strict timeline.',
      'title': 'We Tested Bland AI’s Voice Agent. Here’s What Happened (CX Foundation)',
      'url': 'https://www.youtube.com/watch?v=-j4XDojlGLc&t=81s',
      'video_id': '-j4XDojlGLc'},
     {'author': 'Bland',
      'channel': 'Bland',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=W1Y3bHct_e0&t=30s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, in this case, right, we want the agent to first, obviously, absolutely make '
              "sure that the user is okay, um that there's no, you know, immediate urgency, "
              "like we should call 911, things like that. Um we've got some global nodes set "
              'up here.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'So, in this case, right, we want the agent to first, obviously, absolutely make '
             "sure that the user is okay, um that there's no, you know, immediate urgency, "
             "like we should call 911, things like that. Um we've got some global nodes set up "
             'here.',
      'title': 'How to automate FNOL insurance calls using AI voice agents (Bland)',
      'url': 'https://www.youtube.com/watch?v=W1Y3bHct_e0&t=30s',
      'video_id': 'W1Y3bHct_e0'},
     {'author': 'Matt Williams',
      'channel': 'Matt Williams',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=KeqxPxb_sak&t=33s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Ollama, and today I'm going to show you how to swap in local models, so your "
              'most private data never leaves your machine. The setup is almost the same as '
              'the Claude desktop integration that I showed recently, but with one weird quirk '
              'in how you pick your models.',
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': "Ollama, and today I'm going to show you how to swap in local models, so your "
             'most private data never leaves your machine. The setup is almost the same as the '
             'Claude desktop integration that I showed recently, but with one weird quirk in '
             'how you pick your models.',
      'title': "Stop Sending Your Private Data to OpenAI's Servers (Matt Williams)",
      'url': 'https://www.youtube.com/watch?v=KeqxPxb_sak&t=33s',
      'video_id': 'KeqxPxb_sak'},
     {'author': 'Pavlo',
      'channel': 'Pavlo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:21](https://www.youtube.com/watch?v=GCChOuvd7Sg&t=981s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Are all doing it and now I'm bringing it to you if you want to see more on how "
              'we actually get clients and turn them into pain customers you can check out '
              'this video next.',
      'timestamp': 981,
      'timestamp_label': '[00:16:21]',
      'timestamp_seconds': 981,
      'tip': "Are all doing it and now I'm bringing it to you if you want to see more on how "
             'we actually get clients and turn them into pain customers you can check out this '
             'video next.',
      'title': 'Cold Calling AI Agency Script That Gets 7 Meetings/day (Pavlo)',
      'url': 'https://www.youtube.com/watch?v=GCChOuvd7Sg&t=981s',
      'video_id': 'GCChOuvd7Sg'},
     {'author': 'IBM Technology',
      'channel': 'IBM Technology',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:26](https://www.youtube.com/watch?v=T-D1OfcDW1M&t=326s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If the user's question cannot be reliably answered based on your data store, "
              'the model should say, "I don\'t know," instead of making up something that is '
              'believable and may mislead the user.',
      'timestamp': 326,
      'timestamp_label': '[00:05:26]',
      'timestamp_seconds': 326,
      'tip': "If the user's question cannot be reliably answered based on your data store, the "
             'model should say, "I don\'t know," instead of making up something that is '
             'believable and may mislead the user.',
      'title': 'What is Retrieval-Augmented Generation (RAG)? (IBM Technology)',
      'url': 'https://www.youtube.com/watch?v=T-D1OfcDW1M&t=326s',
      'video_id': 'T-D1OfcDW1M'},
     {'author': 'Jonas | AI Tools & Automation',
      'channel': 'Jonas | AI Tools & Automation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:34](https://www.youtube.com/watch?v=4imOFZeP7nk&t=394s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Because it's a whole lot cheaper and you get a lot more freedom and executions "
              'with this method. Now, building an automation is easy, but building one that '
              "doesn't break when a real client uses it is pretty different.",
      'timestamp': 394,
      'timestamp_label': '[00:06:34]',
      'timestamp_seconds': 394,
      'tip': "Because it's a whole lot cheaper and you get a lot more freedom and executions "
             'with this method. Now, building an automation is easy, but building one that '
             "doesn't break when a real client uses it is pretty different.",
      'title': 'I Run My AI Automation Business for $0 in Software (Zapier vs Make vs n8n) '
               '(Jonas | AI Tools & Automation)',
      'url': 'https://www.youtube.com/watch?v=4imOFZeP7nk&t=394s',
      'video_id': '4imOFZeP7nk'}],
 5: [{'author': 'Austin Reed',
      'channel': 'Austin Reed',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:48](https://www.youtube.com/watch?v=mw1V2GoYHsk&t=228s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In that case, the only thing you might want to do is put the JSON file in a '
              "Notion page with a little bit of documentation handed to the client, and you're "
              "good to go. Now let's talk about API keys. Generally, while you're building, "
              'you would like to use test credentials.',
      'timestamp': 228,
      'timestamp_label': '[00:03:48]',
      'timestamp_seconds': 228,
      'tip': 'In that case, the only thing you might want to do is put the JSON file in a '
             "Notion page with a little bit of documentation handed to the client, and you're "
             "good to go. Now let's talk about API keys. Generally, while you're building, you "
             'would like to use test credentials.',
      'title': 'How to Deliver Your n8n Project to Clients Like a PRO! (Austin Reed)',
      'url': 'https://www.youtube.com/watch?v=mw1V2GoYHsk&t=228s',
      'video_id': 'mw1V2GoYHsk'},
     {'author': 'Daniel | Tech & Data',
      'channel': 'Daniel | Tech & Data',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:15](https://www.youtube.com/watch?v=PgrkNMNc_Cw&t=375s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'After I pointed out the mistake, the agent corrected it and confirmed the '
              'updated information without restarting the entire booking process. The call '
              'ended with a complete appointment summary that included the vehicle issue and '
              "the customer's contact details.",
      'timestamp': 375,
      'timestamp_label': '[00:06:15]',
      'timestamp_seconds': 375,
      'tip': 'After I pointed out the mistake, the agent corrected it and confirmed the '
             'updated information without restarting the entire booking process. The call '
             'ended with a complete appointment summary that included the vehicle issue and '
             "the customer's contact details.",
      'title': 'Retell AI Review (2026): Create AI Voice Agents in Under 10 Minutes (Daniel | '
               'Tech & Data)',
      'url': 'https://www.youtube.com/watch?v=PgrkNMNc_Cw&t=375s',
      'video_id': 'PgrkNMNc_Cw'},
     {'author': 'Nomad Life Success',
      'channel': 'Nomad Life Success',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:55](https://www.youtube.com/watch?v=KdD-2pmdFZI&t=355s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The shield is flexible by design. The three biggest mistakes I see nomads make. '
              'Mistake one, being too rigid. If you send a change order for every tiny tweak, '
              'clients will feel nickel and dimed and might leave. The shield is for scope '
              'creep, not for building a wall.',
      'timestamp': 355,
      'timestamp_label': '[00:05:55]',
      'timestamp_seconds': 355,
      'tip': 'The shield is flexible by design. The three biggest mistakes I see nomads make. '
             'Mistake one, being too rigid. If you send a change order for every tiny tweak, '
             'clients will feel nickel and dimed and might leave. The shield is for scope '
             'creep, not for building a wall.',
      'title': "The AI Scope-Creep Shield: How to Turn 'One More Request' into a Premium "
               'Change-Order That Pays Y... (Nomad Life Success)',
      'url': 'https://www.youtube.com/watch?v=KdD-2pmdFZI&t=355s',
      'video_id': 'KdD-2pmdFZI'},
     {'author': 'Michael Saruggia - GTM Engineering',
      'channel': 'Michael Saruggia - GTM Engineering',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:08](https://www.youtube.com/watch?v=DHX8uoA53OI&t=188s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Most of the times it's a recurring problem. And moreover, if you're actually "
              "able to identify these job changes, there is an amazing pipeline use case. 's "
              "say that you are in touch and you're working with 100 1,000 active clients, "
              'active accounts.',
      'timestamp': 188,
      'timestamp_label': '[00:03:08]',
      'timestamp_seconds': 188,
      'tip': "Most of the times it's a recurring problem. And moreover, if you're actually "
             "able to identify these job changes, there is an amazing pipeline use case. 's "
             "say that you are in touch and you're working with 100 1,000 active clients, "
             'active accounts.',
      'title': 'Fix Your CRM Data With Clay.Com (Job Changes Problem) (Michael Saruggia - GTM '
               'Engineering)',
      'url': 'https://www.youtube.com/watch?v=DHX8uoA53OI&t=188s',
      'video_id': 'DHX8uoA53OI'},
     {'author': 'My Web Audit',
      'channel': 'My Web Audit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:51](https://www.youtube.com/watch?v=tT1dV4_aC0M&t=1251s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Michael, It, I just had to give it four or five variables. It pulled up the '
              "prompts, and in this case, there's 20 prompts. A note to the client that says, "
              '"Hey, our audit only includes 10," and identify which 10 here work best.',
      'timestamp': 1251,
      'timestamp_label': '[00:20:51]',
      'timestamp_seconds': 1251,
      'tip': 'Michael, It, I just had to give it four or five variables. It pulled up the '
             "prompts, and in this case, there's 20 prompts. A note to the client that says, "
             '"Hey, our audit only includes 10," and identify which 10 here work best.',
      'title': 'How to sell AI visibility audits and turn them into recurring revenue for your '
               'agency (My Web Audit)',
      'url': 'https://www.youtube.com/watch?v=tT1dV4_aC0M&t=1251s',
      'video_id': 'tT1dV4_aC0M'},
     {'author': 'Zimri Mayfield',
      'channel': 'Zimri Mayfield',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:42](https://www.youtube.com/watch?v=Z7hn_pkhIxM&t=342s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Brett's nearly $2 million business is no accident. It has nothing to do with "
              'luck, but rather some very smart decisions he made while building his business. '
              'Okay, you see this channel called Starter Story? I look look at their look at '
              'the content.',
      'timestamp': 342,
      'timestamp_label': '[00:05:42]',
      'timestamp_seconds': 342,
      'tip': "Brett's nearly $2 million business is no accident. It has nothing to do with "
             'luck, but rather some very smart decisions he made while building his business. '
             'Okay, you see this channel called Starter Story? I look look at their look at '
             'the content.',
      'title': 'DesignJoy has to be a scam (Zimri Mayfield)',
      'url': 'https://www.youtube.com/watch?v=Z7hn_pkhIxM&t=342s',
      'video_id': 'Z7hn_pkhIxM'},
     {'author': 'The AI Architects | Tom Crawshaw',
      'channel': 'The AI Architects | Tom Crawshaw',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:33](https://www.youtube.com/watch?v=ofC4OeNjDx8&t=213s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're not just connecting nodes anymore. You're building fast, reliable "
              "automations that actually work. But even knowing that timeline won't save you "
              "if you're making these three mistakes that kill most people's progress. So "
              'mistake number one is tutorial addiction.',
      'timestamp': 213,
      'timestamp_label': '[00:03:33]',
      'timestamp_seconds': 213,
      'tip': "You're not just connecting nodes anymore. You're building fast, reliable "
             "automations that actually work. But even knowing that timeline won't save you if "
             "you're making these three mistakes that kill most people's progress. So mistake "
             'number one is tutorial addiction.',
      'title': 'Seriously, please watch this before you start learning n8n (The AI Architects '
               '| Tom Crawshaw)',
      'url': 'https://www.youtube.com/watch?v=ofC4OeNjDx8&t=213s',
      'video_id': 'ofC4OeNjDx8'},
     {'author': 'AI Engineering with Kaushal',
      'channel': 'AI Engineering with Kaushal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:47](https://www.youtube.com/watch?v=cxGMp3DBkMk&t=1127s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So it just does does not mandatory everyone will use agentic rag. It's based on "
              "your business. It's based on your problem. So what do if your problem can be "
              'solved just in simple naive rag means classic rag why you go for agentic?',
      'timestamp': 1127,
      'timestamp_label': '[00:18:47]',
      'timestamp_seconds': 1127,
      'tip': "So it just does does not mandatory everyone will use agentic rag. It's based on "
             "your business. It's based on your problem. So what do if your problem can be "
             'solved just in simple naive rag means classic rag why you go for agentic?',
      'title': 'RAG Explained: Why LLMs Hallucinate Without a Knowledge Layer (AI Engineering '
               'with Kaushal)',
      'url': 'https://www.youtube.com/watch?v=cxGMp3DBkMk&t=1127s',
      'video_id': 'cxGMp3DBkMk'},
     {'author': 'AI Tool Lab',
      'channel': 'AI Tool Lab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:05](https://www.youtube.com/watch?v=9wewuc4s038&t=365s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Chap base builds the model request, not the answer. Every meter in this video '
              "charges for something other than a solved problem, except the winner's free "
              'tier, which charges nothing at all to start, and even the winner has a sharp '
              'trap.',
      'timestamp': 365,
      'timestamp_label': '[00:06:05]',
      'timestamp_seconds': 365,
      'tip': 'Chap base builds the model request, not the answer. Every meter in this video '
             "charges for something other than a solved problem, except the winner's free "
             'tier, which charges nothing at all to start, and even the winner has a sharp '
             'trap.',
      'title': 'I Tested 5 AI Customer Support Chatbots — Ranked Worst to Best (2026) (AI Tool '
               'Lab)',
      'url': 'https://www.youtube.com/watch?v=9wewuc4s038&t=365s',
      'video_id': '9wewuc4s038'},
     {'author': 'Carly Meyers',
      'channel': 'Carly Meyers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:32](https://www.youtube.com/watch?v=stoZ9wFob2E&t=1292s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I think there is definitely a great place for it. It's not the the easiest "
              'business model. The problem is you spend loads of time on discovery calls when '
              'really you should be promoting.',
      'timestamp': 1292,
      'timestamp_label': '[00:21:32]',
      'timestamp_seconds': 1292,
      'tip': "I think there is definitely a great place for it. It's not the the easiest "
             'business model. The problem is you spend loads of time on discovery calls when '
             'really you should be promoting.',
      'title': 'Ditch the Broken Agency Model and Start Selling AI Audits (Part 1) (Carly '
               'Meyers)',
      'url': 'https://www.youtube.com/watch?v=stoZ9wFob2E&t=1292s',
      'video_id': 'stoZ9wFob2E'},
     {'author': 'Alex Leischow',
      'channel': 'Alex Leischow',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=8yIHmsMHMYc&t=43s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re working with like a blue-collar company uh that does like, I don't know, "
              "plumbing, um you know, renovations and services and stuff like that. So, we're "
              "we're going to be building a inbound voice agent for a plumbing company.",
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': "'re working with like a blue-collar company uh that does like, I don't know, "
             "plumbing, um you know, renovations and services and stuff like that. So, we're "
             "we're going to be building a inbound voice agent for a plumbing company.",
      'title': 'How to Build an AI Voice Agent That Calls Every Lead in 60 Seconds (VAPI '
               'Tutorial) (Alex Leischow)',
      'url': 'https://www.youtube.com/watch?v=8yIHmsMHMYc&t=43s',
      'video_id': '8yIHmsMHMYc'},
     {'author': 'The Contractor AI | AI Systems for Contractors',
      'channel': 'The Contractor AI | AI Systems for Contractors',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:17](https://www.youtube.com/watch?v=J5BBjGKyoUE&t=1097s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I want to I want to keep things on track. If I have to stop my crews, '
              "reorganize, lose days, lose production, like that's the problem. And I find "
              "that most guys they do these things as favors when they're really they really "
              'are, you know, a business mechanism.',
      'timestamp': 1097,
      'timestamp_label': '[00:18:17]',
      'timestamp_seconds': 1097,
      'tip': 'I want to I want to keep things on track. If I have to stop my crews, '
             "reorganize, lose days, lose production, like that's the problem. And I find that "
             "most guys they do these things as favors when they're really they really are, "
             'you know, a business mechanism.',
      'title': 'The $12.4K Scope Creep Killing Your Best Jobs (Fix Inside) (The Contractor AI '
               '| AI Systems for Contractors)',
      'url': 'https://www.youtube.com/watch?v=J5BBjGKyoUE&t=1097s',
      'video_id': 'J5BBjGKyoUE'},
     {'author': 'Tyler Gillespie',
      'channel': 'Tyler Gillespie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:42:15](https://www.youtube.com/watch?v=0IHziP_l6cc&t=2535s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Where you get access to kind of see a full breakdown of essentially yeah how we '
              'think about productizing services etc so definitely head over to '
              'productizedplaybook.com.',
      'timestamp': 2535,
      'timestamp_label': '[00:42:15]',
      'timestamp_seconds': 2535,
      'tip': 'Where you get access to kind of see a full breakdown of essentially yeah how we '
             'think about productizing services etc so definitely head over to '
             'productizedplaybook.com.',
      'title': '[PS #0009] How Brett Williams Runs a Successful Productized Design Service '
               '(Tyler Gillespie)',
      'url': 'https://www.youtube.com/watch?v=0IHziP_l6cc&t=2535s',
      'video_id': '0IHziP_l6cc'},
     {'author': 'Chris Prouty',
      'channel': 'Chris Prouty',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:54](https://www.youtube.com/watch?v=8yepbhYel-Q&t=234s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Might not be the only thing you need right now YouTube thinks this video is '
              'going to help you so you should probably check that out but before you do you '
              'click on my face so that you get first access to every new training I create.',
      'timestamp': 234,
      'timestamp_label': '[00:03:54]',
      'timestamp_seconds': 234,
      'tip': 'Might not be the only thing you need right now YouTube thinks this video is '
             'going to help you so you should probably check that out but before you do you '
             'click on my face so that you get first access to every new training I create.',
      'title': 'B2B LinkedIn Content Marketing - How To Get B2B Clients From LinkedIn (Chris '
               'Prouty)',
      'url': 'https://www.youtube.com/watch?v=8yepbhYel-Q&t=234s',
      'video_id': '8yepbhYel-Q'},
     {'author': 'Sean Standberry',
      'channel': 'Sean Standberry',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:58](https://www.youtube.com/watch?v=5558JLgLk50&t=538s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, when someone fills out a form but doesn't book an appointment, they "
              'automatically get a follow-up text message the next day asking if they still '
              'need help with their plumbing problem or whatever service the business offers.',
      'timestamp': 538,
      'timestamp_label': '[00:08:58]',
      'timestamp_seconds': 538,
      'tip': "So, when someone fills out a form but doesn't book an appointment, they "
             'automatically get a follow-up text message the next day asking if they still '
             'need help with their plumbing problem or whatever service the business offers.',
      'title': "NEW AI Agency Business Model I'm Using to Make $474,996/mo (Sean Standberry)",
      'url': 'https://www.youtube.com/watch?v=5558JLgLk50&t=538s',
      'video_id': '5558JLgLk50'}],
 6: [{'author': 'Nick Saraev',
      'channel': 'Nick Saraev',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:30](https://www.youtube.com/watch?v=oAWe5wFwHlo&t=1650s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, the first two leads in this list were obviously um the same company, '
              "Hathan Co. Didn't do that in this case cuz I actually think that it makes sense "
              'to pitch two people on an individual business.',
      'timestamp': 1650,
      'timestamp_label': '[00:27:30]',
      'timestamp_seconds': 1650,
      'tip': 'Now, the first two leads in this list were obviously um the same company, Hathan '
             "Co. Didn't do that in this case cuz I actually think that it makes sense to "
             'pitch two people on an individual business.',
      'title': 'I Deep-Personalized 1000+ Cold Emails Using THIS AI System (FREE TEMPLATE) '
               '(Nick Saraev)',
      'url': 'https://www.youtube.com/watch?v=oAWe5wFwHlo&t=1650s',
      'video_id': 'oAWe5wFwHlo'},
     {'author': 'Shabbir Noor AI',
      'channel': 'Shabbir Noor AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:50](https://www.youtube.com/watch?v=nGTJIZki9Ck&t=890s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'First on LinkedIn, it needs to stay up to date with the latest developments in '
              "AI, specifically what's relevant to my ICP. Now, obviously, because I have a AI "
              'agency, you would switch this up to whatever your business is through the Grock '
              'agent and using web search.',
      'timestamp': 890,
      'timestamp_label': '[00:14:50]',
      'timestamp_seconds': 890,
      'tip': 'First on LinkedIn, it needs to stay up to date with the latest developments in '
             "AI, specifically what's relevant to my ICP. Now, obviously, because I have a AI "
             'agency, you would switch this up to whatever your business is through the Grock '
             'agent and using web search.',
      'title': 'I Asked OpenClaw to Do Cold Email Outreach For 24 Hours (Shabbir Noor AI)',
      'url': 'https://www.youtube.com/watch?v=nGTJIZki9Ck&t=890s',
      'video_id': 'nGTJIZki9Ck'},
     {'author': 'Aaron Shepherd | GrowthFlare',
      'channel': 'Aaron Shepherd | GrowthFlare',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:44](https://www.youtube.com/watch?v=RQg5jgraVg8&t=284s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, I'm going to start with a few here. All right, so prospect level search is "
              'done. We have 4,000 records at the founder level, 3,200 at the marketing level, '
              'and 3,500 at the business development level. Brings us to 10,000 total leads.',
      'timestamp': 284,
      'timestamp_label': '[00:04:44]',
      'timestamp_seconds': 284,
      'tip': "So, I'm going to start with a few here. All right, so prospect level search is "
             'done. We have 4,000 records at the founder level, 3,200 at the marketing level, '
             'and 3,500 at the business development level. Brings us to 10,000 total leads.',
      'title': 'I Tried Using Claude Code To Send 250,000 Cold Emails in 7 Days (Aaron '
               'Shepherd | GrowthFlare)',
      'url': 'https://www.youtube.com/watch?v=RQg5jgraVg8&t=284s',
      'video_id': 'RQg5jgraVg8'},
     {'author': 'NoCode with Sam Oluwagbami',
      'channel': 'NoCode with Sam Oluwagbami',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=xQf-khf_CWE&t=21s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "B2B outbound sales automation, right? So, we're about to build a B2B outbound "
              'sales automation platform. A B2B outbound sales automation platform. Basically, '
              "if you're a B2B business, you you get customers, you send them emails, some of "
              'them reply, right?',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "B2B outbound sales automation, right? So, we're about to build a B2B outbound "
             'sales automation platform. A B2B outbound sales automation platform. Basically, '
             "if you're a B2B business, you you get customers, you send them emails, some of "
             'them reply, right?',
      'title': 'Cold Email is Dead — I Built an AI Outreach System That Does Everything for '
               'You (Lead to Meeting) (NoCode with Sam Oluwagbami)',
      'url': 'https://www.youtube.com/watch?v=xQf-khf_CWE&t=21s',
      'video_id': 'xQf-khf_CWE'},
     {'author': 'Ben Greening-James',
      'channel': 'Ben Greening-James',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=Lw2iBa2oM44&t=20s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, with that being said, let's get straight into it. So when I first started "
              "to do LinkedIn and I just thought, okay, I'm just going to find a lead list of "
              'people and basically just go and try and sell people straight away.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "So, with that being said, let's get straight into it. So when I first started to "
             "do LinkedIn and I just thought, okay, I'm just going to find a lead list of "
             'people and basically just go and try and sell people straight away.',
      'title': 'How I Sell B2B Services on LinkedIn (Step-by-Step) (Ben Greening-James)',
      'url': 'https://www.youtube.com/watch?v=Lw2iBa2oM44&t=20s',
      'video_id': 'Lw2iBa2oM44'},
     {'author': 'RevPartners - RevOps + GTM Engineering on HubSpot',
      'channel': 'RevPartners - RevOps + GTM Engineering on HubSpot',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:11](https://www.youtube.com/watch?v=jV1Kp0j9lp0&t=1211s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s very time consuming and bringing it back into Clay as very structured data "
              'points. The other use case for AI within Clay is creating either custom data '
              'points or um drafting outbound content.',
      'timestamp': 1211,
      'timestamp_label': '[00:20:11]',
      'timestamp_seconds': 1211,
      'tip': "'s very time consuming and bringing it back into Clay as very structured data "
             'points. The other use case for AI within Clay is creating either custom data '
             'points or um drafting outbound content.',
      'title': 'Revolutionize Your Sales: Automated AI Prospecting with HubSpot & Clay '
               '(RevPartners - RevOps + GTM Engineering on HubSpot)',
      'url': 'https://www.youtube.com/watch?v=jV1Kp0j9lp0&t=1211s',
      'video_id': 'jV1Kp0j9lp0'},
     {'author': 'Automate with Marc | AI Automation',
      'channel': 'Automate with Marc | AI Automation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:54](https://www.youtube.com/watch?v=syCqaV7N73s&t=174s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So it's got the first name, last name of people who are inbound leads or maybe "
              'a lead list that you have to go after in terms of outreach.',
      'timestamp': 174,
      'timestamp_label': '[00:02:54]',
      'timestamp_seconds': 174,
      'tip': "So it's got the first name, last name of people who are inbound leads or maybe a "
             'lead list that you have to go after in terms of outreach.',
      'title': 'The difference between Zapier, Make and n8n (2026) (Automate with Marc | AI '
               'Automation)',
      'url': 'https://www.youtube.com/watch?v=syCqaV7N73s&t=174s',
      'video_id': 'syCqaV7N73s'},
     {'author': 'Danny Peregrine',
      'channel': 'Danny Peregrine',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:04](https://www.youtube.com/watch?v=49rzug0GIOY&t=544s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The first client I ever got was on Fiverr and it's so crazy because I've never "
              'been on Fiverr. I always think of Fiverr as like a $5 thing, cheap work, '
              'whatever. But it was when OpenClaw was coming out which was like a new agent '
              "harness. It's a very new technology.",
      'timestamp': 544,
      'timestamp_label': '[00:09:04]',
      'timestamp_seconds': 544,
      'tip': "The first client I ever got was on Fiverr and it's so crazy because I've never "
             'been on Fiverr. I always think of Fiverr as like a $5 thing, cheap work, '
             'whatever. But it was when OpenClaw was coming out which was like a new agent '
             "harness. It's a very new technology.",
      'title': 'How to build a $100K/Month AI Agency in 2027 (Full Breakdown) (Danny '
               'Peregrine)',
      'url': 'https://www.youtube.com/watch?v=49rzug0GIOY&t=544s',
      'video_id': '49rzug0GIOY'},
     {'author': 'Adam Holmgren',
      'channel': 'Adam Holmgren',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:10](https://www.youtube.com/watch?v=qy4FW_qglNo&t=310s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It doesn't have to be harder than that with cold targeting. Then of course, the "
              'ideal state, you would have some sort of third party data vendor where you can '
              'get account list and so on. But we are a startup and we have to start '
              'somewhere.',
      'timestamp': 310,
      'timestamp_label': '[00:05:10]',
      'timestamp_seconds': 310,
      'tip': "It doesn't have to be harder than that with cold targeting. Then of course, the "
             'ideal state, you would have some sort of third party data vendor where you can '
             'get account list and so on. But we are a startup and we have to start somewhere.',
      'title': 'LinkedIn Ads Strategy for B2B: The Exact Campaigns That Took Us from 0 to 200 '
               'Customers (Adam Holmgren)',
      'url': 'https://www.youtube.com/watch?v=qy4FW_qglNo&t=310s',
      'video_id': 'qy4FW_qglNo'},
     {'author': 'AIMS Consulting Services',
      'channel': 'AIMS Consulting Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=fk7OXnsQu-o&t=30s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'CSV, find the missing details and re-upload that data. And that sort of even '
              "leads to a lot of data loss. And to avoid this manual work, what I'm going to "
              "do is I'm going to show you how we can automate this entire process using Cloud "
              'Code, Mold Sets and HubSpot.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'CSV, find the missing details and re-upload that data. And that sort of even '
             "leads to a lot of data loss. And to avoid this manual work, what I'm going to do "
             "is I'm going to show you how we can automate this entire process using Cloud "
             'Code, Mold Sets and HubSpot.',
      'title': 'Auto-Enrich 1,000+ CRM Contacts Using Claude Code + MoltSets (AIMS Consulting '
               'Services)',
      'url': 'https://www.youtube.com/watch?v=fk7OXnsQu-o&t=30s',
      'video_id': 'fk7OXnsQu-o'},
     {'author': 'Youri van Hofwegen',
      'channel': 'Youri van Hofwegen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:34](https://www.youtube.com/watch?v=zqtx1Soeq5E&t=214s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "To show you how this works, let's import a prebuilt AI automation template. "
              'This is the fastest way to get started since the n8n community has already '
              "created hundreds of working automations. First, let's go to the n8n website to "
              'find a template.',
      'timestamp': 214,
      'timestamp_label': '[00:03:34]',
      'timestamp_seconds': 214,
      'tip': "To show you how this works, let's import a prebuilt AI automation template. This "
             'is the fastest way to get started since the n8n community has already created '
             "hundreds of working automations. First, let's go to the n8n website to find a "
             'template.',
      'title': 'How to Use N8N for FREE - n8n Self Hosting Set Up Guide (Youri van Hofwegen)',
      'url': 'https://www.youtube.com/watch?v=zqtx1Soeq5E&t=214s',
      'video_id': 'zqtx1Soeq5E'},
     {'author': 'Expandi',
      'channel': 'Expandi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:37](https://www.youtube.com/watch?v=IqCv6BL9r6o&t=277s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But in this case, we're going to be doing a smart omni channel campaign with "
              "multiple touch points that works across any niche. For the first step, we're "
              "going to visit the lead's profile.",
      'timestamp': 277,
      'timestamp_label': '[00:04:37]',
      'timestamp_seconds': 277,
      'tip': "But in this case, we're going to be doing a smart omni channel campaign with "
             "multiple touch points that works across any niche. For the first step, we're "
             "going to visit the lead's profile.",
      'title': 'The Best LinkedIn Outreach Strategy for 2026 (Expandi)',
      'url': 'https://www.youtube.com/watch?v=IqCv6BL9r6o&t=277s',
      'video_id': 'IqCv6BL9r6o'},
     {'author': 'AI Engineer',
      'channel': 'AI Engineer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:53](https://www.youtube.com/watch?v=XNneh6-eyPg&t=713s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'CRM where you already have customer clients uh and and leads in your knowledge '
              'graph but then you want to enrich this with for instance uh protocols from call '
              'transcripts and then you basically connect this to your existing structured '
              'data as well.',
      'timestamp': 713,
      'timestamp_label': '[00:11:53]',
      'timestamp_seconds': 713,
      'tip': 'CRM where you already have customer clients uh and and leads in your knowledge '
             'graph but then you want to enrich this with for instance uh protocols from call '
             'transcripts and then you basically connect this to your existing structured data '
             'as well.',
      'title': 'Practical GraphRAG: Making LLMs smarter with Knowledge Graphs — Michael, '
               'Jesus, and Stephen, Neo4j (AI Engineer)',
      'url': 'https://www.youtube.com/watch?v=XNneh6-eyPg&t=713s',
      'video_id': 'XNneh6-eyPg'},
     {'author': 'neomanex',
      'channel': 'neomanex',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:40](https://www.youtube.com/watch?v=wOkT9r5iVME&t=520s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then let every step read the same list. If you want to build like this, join '
              'inside New Manics. We help builders set up their own.',
      'timestamp': 520,
      'timestamp_label': '[00:08:40]',
      'timestamp_seconds': 520,
      'tip': 'Then let every step read the same list. If you want to build like this, join '
             'inside New Manics. We help builders set up their own.',
      'title': 'Stop AI Agent Scope Creep: Frozen Requirements and a Done When List (neomanex)',
      'url': 'https://www.youtube.com/watch?v=wOkT9r5iVME&t=520s',
      'video_id': 'wOkT9r5iVME'},
     {'author': 'AI Hustle Lab',
      'channel': 'AI Hustle Lab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:01](https://www.youtube.com/watch?v=6FS1eyS2agI&t=481s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So I put in the term AI automation. It also asks for an email and I put in '
              'nicholas@gmail. From here we have a number of things that occur. The first is '
              'we actually feed an open AI call using the web search API that goes and it '
              'finds outlines of content on AI and automation.',
      'timestamp': 481,
      'timestamp_label': '[00:08:01]',
      'timestamp_seconds': 481,
      'tip': 'So I put in the term AI automation. It also asks for an email and I put in '
             'nicholas@gmail. From here we have a number of things that occur. The first is we '
             'actually feed an open AI call using the web search API that goes and it finds '
             'outlines of content on AI and automation.',
      'title': 'Sell These 3 Simple AI Automations for $1.7K to B2B Agencies (AI Hustle Lab)',
      'url': 'https://www.youtube.com/watch?v=6FS1eyS2agI&t=481s',
      'video_id': '6FS1eyS2agI'}],
 7: [{'author': 'ProfitPilot',
      'channel': 'ProfitPilot',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:29](https://www.youtube.com/watch?v=d8w8FHZJpdY&t=149s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "On n8n, it's one execution per run, whether the workflow has five steps or "
              "fifty. These counts assume every step runs every time. That's a worst case, and "
              "it's our calculation from the published rules, not a measured test. Now the "
              'costs, at three volumes.',
      'timestamp': 149,
      'timestamp_label': '[00:02:29]',
      'timestamp_seconds': 149,
      'tip': "On n8n, it's one execution per run, whether the workflow has five steps or "
             "fifty. These counts assume every step runs every time. That's a worst case, and "
             "it's our calculation from the published rules, not a measured test. Now the "
             'costs, at three volumes.',
      'title': 'Zapier vs Make vs n8n: What One AI Workflow Really Costs (2026 Pricing) '
               '(ProfitPilot)',
      'url': 'https://www.youtube.com/watch?v=d8w8FHZJpdY&t=149s',
      'video_id': 'd8w8FHZJpdY'},
     {'author': "Lobo Brother's | AI Systems for Business Owners",
      'channel': "Lobo Brother's | AI Systems for Business Owners",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:47](https://www.youtube.com/watch?v=dqDWqV07r6M&t=167s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's break it down with an example. And I'm using a hypothetical business that "
              'I made up over here to keep real client names and numbers private, but the '
              'process and the audit breakdown is exactly the same for how we run it for our '
              'clients.',
      'timestamp': 167,
      'timestamp_label': '[00:02:47]',
      'timestamp_seconds': 167,
      'tip': "Let's break it down with an example. And I'm using a hypothetical business that "
             'I made up over here to keep real client names and numbers private, but the '
             'process and the audit breakdown is exactly the same for how we run it for our '
             'clients.',
      'title': "I Audited A $5M Business For AI. Here's What I Found (Lobo Brother's | AI "
               'Systems for Business Owners)',
      'url': 'https://www.youtube.com/watch?v=dqDWqV07r6M&t=167s',
      'video_id': 'dqDWqV07r6M'},
     {'author': 'Mirketa Inc',
      'channel': 'Mirketa Inc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:57](https://www.youtube.com/watch?v=8N3k2qP_0SY&t=1437s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And imagine a support agent receives a case. It retrieves similar cases and '
              "relevant knowledge. Then it decides, I need to verify this customer's "
              "subscription, so it will call an API. Then I should check whether there's a "
              'known outage. It calls the monitoring system.',
      'timestamp': 1437,
      'timestamp_label': '[00:23:57]',
      'timestamp_seconds': 1437,
      'tip': 'And imagine a support agent receives a case. It retrieves similar cases and '
             "relevant knowledge. Then it decides, I need to verify this customer's "
             "subscription, so it will call an API. Then I should check whether there's a "
             'known outage. It calls the monitoring system.',
      'title': 'Beyond the Case | Episode 6: RAG, AI Agents & Vector Databases — Without the '
               'Hype (Mirketa Inc)',
      'url': 'https://www.youtube.com/watch?v=8N3k2qP_0SY&t=1437s',
      'video_id': '8N3k2qP_0SY'},
     {'author': 'Lily Latzo | AI Automation',
      'channel': 'Lily Latzo | AI Automation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:53](https://www.youtube.com/watch?v=NjvNF17_97w&t=113s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re going to do it, they're going to be interested. So the first step is the "
              "offer one pager. So this pretty much forces clarity and that's what businesses "
              "want to buy. So we're going to build an automation for a repetitive workflow "
              'inside of the business in 30 days.',
      'timestamp': 113,
      'timestamp_label': '[00:01:53]',
      'timestamp_seconds': 113,
      'tip': "'re going to do it, they're going to be interested. So the first step is the "
             "offer one pager. So this pretty much forces clarity and that's what businesses "
             "want to buy. So we're going to build an automation for a repetitive workflow "
             'inside of the business in 30 days.',
      'title': 'How I Landed 3 AI Automation Clients in 7 Days | Simple Outreach System That '
               'Works (Lily Latzo | AI Automation)',
      'url': 'https://www.youtube.com/watch?v=NjvNF17_97w&t=113s',
      'video_id': 'NjvNF17_97w'},
     {'author': 'Scott Bartnick',
      'channel': 'Scott Bartnick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:12](https://www.youtube.com/watch?v=d9zqCrUn7mY&t=432s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t know how to use it, if you have this video, send it to a freelancer, have "
              'them do it for you. You can build out the workflow and you can use the '
              'checklist down below of the different steps. So, this order comes in, the '
              'client does their onboarding.',
      'timestamp': 432,
      'timestamp_label': '[00:07:12]',
      'timestamp_seconds': 432,
      'tip': "'t know how to use it, if you have this video, send it to a freelancer, have "
             'them do it for you. You can build out the workflow and you can use the checklist '
             'down below of the different steps. So, this order comes in, the client does '
             'their onboarding.',
      'title': 'The Client Handoff System That Stops Scope Creep and Dropped Balls (Scott '
               'Bartnick)',
      'url': 'https://www.youtube.com/watch?v=d9zqCrUn7mY&t=432s',
      'video_id': 'd9zqCrUn7mY'},
     {'author': 'AI Money Math',
      'channel': 'AI Money Math',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:23](https://www.youtube.com/watch?v=VZQaUF7kKNw&t=23s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "One automation, one type of business, one city, seven steps in order. You don't "
              "need to code, you don't need an agency, a website, or a logo. You need a "
              'working demo on your phone and the nerve to show it to 30 business owners.',
      'timestamp': 23,
      'timestamp_label': '[00:00:23]',
      'timestamp_seconds': 23,
      'tip': "One automation, one type of business, one city, seven steps in order. You don't "
             "need to code, you don't need an agency, a website, or a logo. You need a working "
             'demo on your phone and the nerve to show it to 30 business owners.',
      'title': 'How to Sell AI Automations to Local Businesses (Beginner Guide) (AI Money '
               'Math)',
      'url': 'https://www.youtube.com/watch?v=VZQaUF7kKNw&t=23s',
      'video_id': 'VZQaUF7kKNw'},
     {'author': 'Aitoolnavio',
      'channel': 'Aitoolnavio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:30:02](https://www.youtube.com/watch?v=vtK1xbj-tD8&t=1802s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Every plan has unlimited users, workflows, and steps. And startups can get '
              'Business at half price. This is where n8n is different. One execution is one '
              'full run of a workflow, whether it has two steps or two hundred.',
      'timestamp': 1802,
      'timestamp_label': '[00:30:02]',
      'timestamp_seconds': 1802,
      'tip': 'Every plan has unlimited users, workflows, and steps. And startups can get '
             'Business at half price. This is where n8n is different. One execution is one '
             'full run of a workflow, whether it has two steps or two hundred.',
      'title': 'n8n Tutorial 2026: AI Agents, Self-Hosting & Pricing (Beginner to Pro) '
               '(Aitoolnavio)',
      'url': 'https://www.youtube.com/watch?v=vtK1xbj-tD8&t=1802s',
      'video_id': 'vtK1xbj-tD8'},
     {'author': 'Zendesk',
      'channel': 'Zendesk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:27](https://www.youtube.com/watch?v=vxbipxTJGgw&t=147s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t limited to one type of business. They can adapt to unique needs of each "
              'sector. In software and subscription businesses, an AI agent can troubleshoot '
              'issues, verify account details, surface the right support content, and guide '
              'customers through resolution steps.',
      'timestamp': 147,
      'timestamp_label': '[00:02:27]',
      'timestamp_seconds': 147,
      'tip': "'t limited to one type of business. They can adapt to unique needs of each "
             'sector. In software and subscription businesses, an AI agent can troubleshoot '
             'issues, verify account details, surface the right support content, and guide '
             'customers through resolution steps.',
      'title': 'What are AI Agents for customer service? Zendesk AI explained (Zendesk)',
      'url': 'https://www.youtube.com/watch?v=vxbipxTJGgw&t=147s',
      'video_id': 'vxbipxTJGgw'},
     {'author': 'SaaS Master',
      'channel': 'SaaS Master',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:33](https://www.youtube.com/watch?v=TdMeBa69Y8Y&t=333s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "N8N, which is an automation system that's going to be working open source free "
              'for me, and then just use the AI right here with a little small fee. I think '
              "it's cost me like 9 cents or 8 cents to run this, which for this highly complex "
              'workflow is nothing.',
      'timestamp': 333,
      'timestamp_label': '[00:05:33]',
      'timestamp_seconds': 333,
      'tip': "N8N, which is an automation system that's going to be working open source free "
             'for me, and then just use the AI right here with a little small fee. I think '
             "it's cost me like 9 cents or 8 cents to run this, which for this highly complex "
             'workflow is nothing.',
      'title': 'n8n Self Hosted With Claude MCP - Let AI Build Your Workflows (SaaS Master)',
      'url': 'https://www.youtube.com/watch?v=TdMeBa69Y8Y&t=333s',
      'video_id': 'TdMeBa69Y8Y'},
     {'author': 'Jeff Su',
      'channel': 'Jeff Su',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:17](https://www.youtube.com/watch?v=FwOTs4UxQS4&t=197s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I added more steps into the workflow by allowing the LM to access the weather '
              'via an API and then just for fun use a text to audio model to speak the answer. '
              'The weather forecast for seeing Elon Husky is sunny with a chance of being a '
              'good boy.',
      'timestamp': 197,
      'timestamp_label': '[00:03:17]',
      'timestamp_seconds': 197,
      'tip': 'I added more steps into the workflow by allowing the LM to access the weather '
             'via an API and then just for fun use a text to audio model to speak the answer. '
             'The weather forecast for seeing Elon Husky is sunny with a chance of being a '
             'good boy.',
      'title': 'AI Agents, Clearly Explained (Jeff Su)',
      'url': 'https://www.youtube.com/watch?v=FwOTs4UxQS4&t=197s',
      'video_id': 'FwOTs4UxQS4'},
     {'author': 'Augusto Digital',
      'channel': 'Augusto Digital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=VzBpfD_Dcq8&t=72s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We're also going to explore this single scope rule that actually holds the "
              "line. And then we'll break down the five-step checklist we actually use in our "
              "client engagements to guarantee a shipped product. So, let's start with the the "
              'root of the problem, right?',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': "We're also going to explore this single scope rule that actually holds the line. "
             "And then we'll break down the five-step checklist we actually use in our client "
             "engagements to guarantee a shipped product. So, let's start with the the root of "
             'the problem, right?',
      'title': 'Ep. 17: Stopping AI Scope Creep | Augusto Podcast (Augusto Digital)',
      'url': 'https://www.youtube.com/watch?v=VzBpfD_Dcq8&t=72s',
      'video_id': 'VzBpfD_Dcq8'},
     {'author': 'Unstructured',
      'channel': 'Unstructured',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:17](https://www.youtube.com/watch?v=ruilmyfVgrI&t=857s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh so within this one um before you write any code you really want to '
              'understand what the security model needs to be for the system. So, this is '
              'going to often be use case specific.',
      'timestamp': 857,
      'timestamp_label': '[00:14:17]',
      'timestamp_seconds': 857,
      'tip': 'Uh so within this one um before you write any code you really want to understand '
             'what the security model needs to be for the system. So, this is going to often '
             'be use case specific.',
      'title': 'Webinar: How to Build Enterprise-Ready RAG Systems (Unstructured)',
      'url': 'https://www.youtube.com/watch?v=ruilmyfVgrI&t=857s',
      'video_id': 'ruilmyfVgrI'},
     {'author': 'The Futur',
      'channel': 'The Futur',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:01:18](https://www.youtube.com/watch?v=8vwgUwgH2Js&t=3678s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Right thing at the right time in the right place so I wish you continued '
              'success thank you very much Brett for coming on the show today thank you man '
              "it's been a dream appreciate it foreign.",
      'timestamp': 3678,
      'timestamp_label': '[01:01:18]',
      'timestamp_seconds': 3678,
      'tip': 'Right thing at the right time in the right place so I wish you continued success '
             "thank you very much Brett for coming on the show today thank you man it's been a "
             'dream appreciate it foreign.',
      'title': 'Secret to Running a $1 Million Solo Design Agency (The Futur)',
      'url': 'https://www.youtube.com/watch?v=8vwgUwgH2Js&t=3678s',
      'video_id': '8vwgUwgH2Js'},
     {'author': 'The AI Blueprint',
      'channel': 'The AI Blueprint',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=1mZ0bWq9y-M&t=168s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Just five active clients puts you at $7,500 in predictable monthly cash flow. '
              'To get your first paying client in under 10 days, you do not need cold calls or '
              'paid ads. Step one, pick one specific industry like commercial real estate '
              'brokers or accounting firms.',
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': 'Just five active clients puts you at $7,500 in predictable monthly cash flow. To '
             'get your first paying client in under 10 days, you do not need cold calls or '
             'paid ads. Step one, pick one specific industry like commercial real estate '
             'brokers or accounting firms.',
      'title': 'How to Build an AI Automation Agency with n8n and AI Agents (2026 Masterclass) '
               '(The AI Blueprint)',
      'url': 'https://www.youtube.com/watch?v=1mZ0bWq9y-M&t=168s',
      'video_id': '1mZ0bWq9y-M'},
     {'author': 'ArriSse Corp',
      'channel': 'ArriSse Corp',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:58](https://www.youtube.com/watch?v=XKoGenFWVHs&t=358s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Step two triggers at day 45 with the quarterly business review. The QBR is used '
              'to pivot the relationship dynamic from deliverable execution to ongoing growth '
              'advisory by presenting an evidence-based gap analysis.',
      'timestamp': 358,
      'timestamp_label': '[00:05:58]',
      'timestamp_seconds': 358,
      'tip': 'Step two triggers at day 45 with the quarterly business review. The QBR is used '
             'to pivot the relationship dynamic from deliverable execution to ongoing growth '
             'advisory by presenting an evidence-based gap analysis.',
      'title': 'The Exact System Boutique Agencies Use to Stop Scope Creep & Close $5k/mo '
               'Retainers (ArriSse Corp)',
      'url': 'https://www.youtube.com/watch?v=XKoGenFWVHs&t=358s',
      'video_id': 'XKoGenFWVHs'}],
 8: [{'author': 'Stephanie Nyarko',
      'channel': 'Stephanie Nyarko',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:44](https://www.youtube.com/watch?v=J8C_262TFUU&t=944s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If they need something custom, if they want to integrate it with their CRM, per '
              "se, or let's say they want to route calls differently based on the time of day. "
              "If I'm building something for an agency to resell or customize for their "
              "clients, then I'll use Vapi.",
      'timestamp': 944,
      'timestamp_label': '[00:15:44]',
      'timestamp_seconds': 944,
      'tip': 'If they need something custom, if they want to integrate it with their CRM, per '
             "se, or let's say they want to route calls differently based on the time of day. "
             "If I'm building something for an agency to resell or customize for their "
             "clients, then I'll use Vapi.",
      'title': 'ElevenLabs vs Vapi vs Retell AI: I Built the Same AI Receptionist on All 3 '
               '(Stephanie Nyarko)',
      'url': 'https://www.youtube.com/watch?v=J8C_262TFUU&t=944s',
      'video_id': 'J8C_262TFUU'},
     {'author': 'Protecto',
      'channel': 'Protecto',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=e8kcLoVVX_A&t=104s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Agent workflows need this at every step. Database queries, tool results, every '
              "one of them. So before you trust a provider's promise, ask these questions. Is "
              'my content excluded from training? Is my use case eligible for zero data '
              'retention? And what are the exceptions?',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': 'Agent workflows need this at every step. Database queries, tool results, every '
             "one of them. So before you trust a provider's promise, ask these questions. Is "
             'my content excluded from training? Is my use case eligible for zero data '
             'retention? And what are the exceptions?',
      'title': 'Zero Data Retention Is Not Enough for AI Security (3 Controls Explained) #ai '
               '#aisecurity (Protecto)',
      'url': 'https://www.youtube.com/watch?v=e8kcLoVVX_A&t=104s',
      'video_id': 'e8kcLoVVX_A'},
     {'author': 'Belt Course',
      'channel': 'Belt Course',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:55](https://www.youtube.com/watch?v=YaFtlj9qXQc&t=235s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Apollo instantly, LinkedIn automation tools, a CRM and n for automations and '
              'they were happy. After after 90 days, they had two new clients at 10K MR and a '
              '45K pipeline.',
      'timestamp': 235,
      'timestamp_label': '[00:03:55]',
      'timestamp_seconds': 235,
      'tip': 'Apollo instantly, LinkedIn automation tools, a CRM and n for automations and '
             'they were happy. After after 90 days, they had two new clients at 10K MR and a '
             '45K pipeline.',
      'title': 'How to Sell AI Services with a Paid AI Business Audit (Step-by-Step Framework) '
               '(Belt Course)',
      'url': 'https://www.youtube.com/watch?v=YaFtlj9qXQc&t=235s',
      'video_id': 'YaFtlj9qXQc'},
     {'author': 'Sonny Sangha',
      'channel': 'Sonny Sangha',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:03](https://www.youtube.com/watch?v=JSYOZvtkAx4&t=1203s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, if we go into the booking, you can actually see there are going to be two '
              'tool calls over inside the booking. So if we go to tools, I have a book '
              'appointment and a check availability. So both of these were created both all '
              'from norm. So just by chatting with Norm.',
      'timestamp': 1203,
      'timestamp_label': '[00:20:03]',
      'timestamp_seconds': 1203,
      'tip': 'Now, if we go into the booking, you can actually see there are going to be two '
             'tool calls over inside the booking. So if we go to tools, I have a book '
             'appointment and a check availability. So both of these were created both all '
             'from norm. So just by chatting with Norm.',
      'title': 'I Built an AI Voice Agent That Actually Works (AI Receptionist Full Beginner '
               'Tutorial) (Sonny Sangha)',
      'url': 'https://www.youtube.com/watch?v=JSYOZvtkAx4&t=1203s',
      'video_id': 'JSYOZvtkAx4'},
     {'author': 'DataSnipper',
      'channel': 'DataSnipper',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:03](https://www.youtube.com/watch?v=fabs_LzN3oI&t=1083s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's part of the process that we build within Data Scraper to keep you as a "
              'user in the loop. And once the agent performs a task, you will see that all the '
              'information has been fully extracted verbatim because in this case we did ask '
              'the agent to do it verbatim.',
      'timestamp': 1083,
      'timestamp_label': '[00:18:03]',
      'timestamp_seconds': 1083,
      'tip': "That's part of the process that we build within Data Scraper to keep you as a "
             'user in the loop. And once the agent performs a task, you will see that all the '
             'information has been fully extracted verbatim because in this case we did ask '
             'the agent to do it verbatim.',
      'title': 'AI Use Cases for Internal Audit, External Audit, Compliance | NYC Connect 226 '
               '(DataSnipper)',
      'url': 'https://www.youtube.com/watch?v=fabs_LzN3oI&t=1083s',
      'video_id': 'fabs_LzN3oI'},
     {'author': 'Cuebic AI',
      'channel': 'Cuebic AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=BxxP4kEqOdg&t=120s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We can also configure the Brave search API key if we want to give the AI access '
              "to web search capabilities. I'll enable AI agents as well, and we can also "
              "enable the agent's knowledge base. At this point, our main AI configuration is "
              'ready.',
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': 'We can also configure the Brave search API key if we want to give the AI access '
             "to web search capabilities. I'll enable AI agents as well, and we can also "
             "enable the agent's knowledge base. At this point, our main AI configuration is "
             'ready.',
      'title': 'n8n AI Assistant & AI Agents on Self-Hosted n8n (Cuebic AI)',
      'url': 'https://www.youtube.com/watch?v=BxxP4kEqOdg&t=120s',
      'video_id': 'BxxP4kEqOdg'},
     {'author': 'Fireship',
      'channel': 'Fireship',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=bS9R6aCVEzw&t=28s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In fact, that\'s exactly what this guy was doing until he said, "Screw it. I\'m '
              'building my own Zapier from scratch." The end result was a platform called N8N, '
              "which is an open-source self-hostable automation tool. And no, it's not the "
              'sponsor of this video.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': 'In fact, that\'s exactly what this guy was doing until he said, "Screw it. I\'m '
             'building my own Zapier from scratch." The end result was a platform called N8N, '
             "which is an open-source self-hostable automation tool. And no, it's not the "
             'sponsor of this video.',
      'title': 'n8n will change your life as a developer... (Fireship)',
      'url': 'https://www.youtube.com/watch?v=bS9R6aCVEzw&t=28s',
      'video_id': 'bS9R6aCVEzw'},
     {'author': 'Indie Bites',
      'channel': 'Indie Bites',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=FpPgkqEoNDY&t=65s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Trying out ahrefs webmaster tools for free you'll see what keywords your pages "
              'are ranking for understand how google sees your content and discover what '
              'changes you need to make to improve your search ranking to try out hrs head to '
              'hrefs.com awt.ahrefs.com.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': "Trying out ahrefs webmaster tools for free you'll see what keywords your pages "
             'are ranking for understand how google sees your content and discover what '
             'changes you need to make to improve your search ranking to try out hrs head to '
             'hrefs.com awt.ahrefs.com.',
      'title': 'A solo $130k MRR productized design service - Brett Williams, Designjoy (Indie '
               'Bites)',
      'url': 'https://www.youtube.com/watch?v=FpPgkqEoNDY&t=65s',
      'video_id': 'FpPgkqEoNDY'},
     {'author': "Jake's Tech Lab",
      'channel': "Jake's Tech Lab",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:27](https://www.youtube.com/watch?v=vSmuuzicQUU&t=27s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ticketing and help desk, AI and automation, reporting and analytics, multi- '
              'channelannel messaging, pricing, security and compliance, and CRM and sales '
              "tools. We'll cruise through each one. And oh, I'm definitely calling out the "
              'quirks and highlights.',
      'timestamp': 27,
      'timestamp_label': '[00:00:27]',
      'timestamp_seconds': 27,
      'tip': 'Ticketing and help desk, AI and automation, reporting and analytics, multi- '
             'channelannel messaging, pricing, security and compliance, and CRM and sales '
             "tools. We'll cruise through each one. And oh, I'm definitely calling out the "
             'quirks and highlights.',
      'title': 'Zendesk vs Intercom Comparison 2025 | Which Customer Support Platform is Best? '
               "(Jake's Tech Lab)",
      'url': 'https://www.youtube.com/watch?v=vSmuuzicQUU&t=27s',
      'video_id': 'vSmuuzicQUU'},
     {'author': 'AI Engineer',
      'channel': 'AI Engineer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:34](https://www.youtube.com/watch?v=XlAIgmi_Vow&t=574s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So again we went back and and thought about like what is our team's expertise "
              'in and what can we do and so what we did was instead we stored the data points '
              'as JSON in a lucine based search engine.',
      'timestamp': 574,
      'timestamp_label': '[00:09:34]',
      'timestamp_seconds': 574,
      'tip': "So again we went back and and thought about like what is our team's expertise in "
             'and what can we do and so what we did was instead we stored the data points as '
             'JSON in a lucine based search engine.',
      'title': 'When Vectors Break Down: Graph-Based RAG for Dense Enterprise Knowledge - Sam '
               'Julien, Writer (AI Engineer)',
      'url': 'https://www.youtube.com/watch?v=XlAIgmi_Vow&t=574s',
      'video_id': 'XlAIgmi_Vow'},
     {'author': 'KodeKloud',
      'channel': 'KodeKloud',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:02](https://www.youtube.com/watch?v=_HQ2H_0Ayy0&t=362s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Explore this question by yourself to get a real feel for the data set. In the '
              "following question, we're asked to initialize our vector database. I spin up "
              'Chromma DB locally using a persistent client and create a collection named tech '
              'corpse_docs.',
      'timestamp': 362,
      'timestamp_label': '[00:06:02]',
      'timestamp_seconds': 362,
      'tip': 'Explore this question by yourself to get a real feel for the data set. In the '
             "following question, we're asked to initialize our vector database. I spin up "
             'Chromma DB locally using a persistent client and create a collection named tech '
             'corpse_docs.',
      'title': 'RAG Explained For Beginners (KodeKloud)',
      'url': 'https://www.youtube.com/watch?v=_HQ2H_0Ayy0&t=362s',
      'video_id': '_HQ2H_0Ayy0'},
     {'author': 'AIWealthPath',
      'channel': 'AIWealthPath',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=JKmSoDIpfdI&t=90s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Step three, pick a support AI tool that fits your size, not the biggest one on '
              "the market. If you're a small business, look at tools like Intercom Fin, "
              'Zendesk AI, or Freshdesk Freddy.',
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': 'Step three, pick a support AI tool that fits your size, not the biggest one on '
             "the market. If you're a small business, look at tools like Intercom Fin, Zendesk "
             'AI, or Freshdesk Freddy.',
      'title': 'How to Automate Your Customer Support With AI in 2026 — Full Beginner Guide '
               '(AIWealthPath)',
      'url': 'https://www.youtube.com/watch?v=JKmSoDIpfdI&t=90s',
      'video_id': 'JKmSoDIpfdI'},
     {'author': 'Cloud in',
      'channel': 'Cloud in',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:42](https://www.youtube.com/watch?v=ZE-vxHSGB7w&t=1302s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'When using organizations, AWS organizations, you can control, you know, have '
              'SCPs that pinpoint onto your platform. So, it is it is giving you an extra '
              'layer of security, as well as, you know, keeping mind of what a data actually '
              'is implemented onto your AWS account.',
      'timestamp': 1302,
      'timestamp_label': '[00:21:42]',
      'timestamp_seconds': 1302,
      'tip': 'When using organizations, AWS organizations, you can control, you know, have '
             'SCPs that pinpoint onto your platform. So, it is it is giving you an extra layer '
             'of security, as well as, you know, keeping mind of what a data actually is '
             'implemented onto your AWS account.',
      'title': 'Securing SMB GenAI Pipelines  Guardrails, Data Privacy & ISO SOC2 Compliance '
               'on AWS (Cloud in)',
      'url': 'https://www.youtube.com/watch?v=ZE-vxHSGB7w&t=1302s',
      'video_id': 'ZE-vxHSGB7w'},
     {'author': 'Simply Contact',
      'channel': 'Simply Contact',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:22](https://www.youtube.com/watch?v=DcDfJRzuZNI&t=82s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Its AI suite includes chatbots, agent assistance, automated ticketing, voice '
              'support, a knowledge base, and detailed analytics. Pricing starts at 19 dollars '
              'per agent per month. Users often highlight Zendesk’s solid automation, smooth '
              'workflows, and strong CRM integrations.',
      'timestamp': 82,
      'timestamp_label': '[00:01:22]',
      'timestamp_seconds': 82,
      'tip': 'Its AI suite includes chatbots, agent assistance, automated ticketing, voice '
             'support, a knowledge base, and detailed analytics. Pricing starts at 19 dollars '
             'per agent per month. Users often highlight Zendesk’s solid automation, smooth '
             'workflows, and strong CRM integrations.',
      'title': 'Top 10 AI Customer Service Companies (Simply Contact)',
      'url': 'https://www.youtube.com/watch?v=DcDfJRzuZNI&t=82s',
      'video_id': 'DcDfJRzuZNI'},
     {'author': 'Michael Saruggia - GTM Engineering',
      'channel': 'Michael Saruggia - GTM Engineering',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:36](https://www.youtube.com/watch?v=DHX8uoA53OI&t=336s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So there will be an automated way to actually get new data. You don't have to "
              "manually update it. Basically, you're pulling all the data from, in this case, "
              'Salesforce into different clay tables. Into the clay tables, you actually have '
              'a couple of column.',
      'timestamp': 336,
      'timestamp_label': '[00:05:36]',
      'timestamp_seconds': 336,
      'tip': "So there will be an automated way to actually get new data. You don't have to "
             "manually update it. Basically, you're pulling all the data from, in this case, "
             'Salesforce into different clay tables. Into the clay tables, you actually have a '
             'couple of column.',
      'title': 'Fix Your CRM Data With Clay.Com (Job Changes Problem) (Michael Saruggia - GTM '
               'Engineering)',
      'url': 'https://www.youtube.com/watch?v=DHX8uoA53OI&t=336s',
      'video_id': 'DHX8uoA53OI'}],
 9: [{'author': 'Mikey No Code',
      'channel': 'Mikey No Code',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:49:42](https://www.youtube.com/watch?v=i4z0kCcByY8&t=2982s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The timeline for this model should also stay realistic. During the first month, '
              'focus on choosing the niche, building the three working base 44 super agent '
              'demos, and beginning direct outreach.',
      'timestamp': 2982,
      'timestamp_label': '[00:49:42]',
      'timestamp_seconds': 2982,
      'tip': 'The timeline for this model should also stay realistic. During the first month, '
             'focus on choosing the niche, building the three working base 44 super agent '
             'demos, and beginning direct outreach.',
      'title': 'How to Start an AI Automation Agency in 2026 (Step by Step) (Mikey No Code)',
      'url': 'https://www.youtube.com/watch?v=i4z0kCcByY8&t=2982s',
      'video_id': 'i4z0kCcByY8'},
     {'author': 'Travis Wardrop',
      'channel': 'Travis Wardrop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:37](https://www.youtube.com/watch?v=CDVbVmBQVyc&t=37s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's lost money, lost clients, and massive frustration. But with this one "
              "automation, an AI agent instantly picks up any calls that don't get answered, "
              "keeps the conversation going, and even books appointments on the business's "
              'calendar automatically.',
      'timestamp': 37,
      'timestamp_label': '[00:00:37]',
      'timestamp_seconds': 37,
      'tip': "That's lost money, lost clients, and massive frustration. But with this one "
             "automation, an AI agent instantly picks up any calls that don't get answered, "
             "keeps the conversation going, and even books appointments on the business's "
             'calendar automatically.',
      'title': 'How to Sell AI Automation to Local Businesses (Beginner Guide) (Travis '
               'Wardrop)',
      'url': 'https://www.youtube.com/watch?v=CDVbVmBQVyc&t=37s',
      'video_id': 'CDVbVmBQVyc'},
     {'author': 'Quiet Client',
      'channel': 'Quiet Client',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:21](https://www.youtube.com/watch?v=csELc0aBrp4&t=261s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Max starts higher if you live in Claude all day. You own tone, facts, and the '
              'send. Never invent a client approval. This is not legal or contract advice. '
              'Estimate or invoice the approved add-on, then you send.',
      'timestamp': 261,
      'timestamp_label': '[00:04:21]',
      'timestamp_seconds': 261,
      'tip': 'Max starts higher if you live in Claude all day. You own tone, facts, and the '
             'send. Never invent a client approval. This is not legal or contract advice. '
             'Estimate or invoice the approved add-on, then you send.',
      'title': 'Stop eating scope creep for free — AI stack that drafts change orders (you '
               'still send) (2026) (Quiet Client)',
      'url': 'https://www.youtube.com/watch?v=csELc0aBrp4&t=261s',
      'video_id': 'csELc0aBrp4'},
     {'author': 'Tom Gaddis | Smart AI Operators',
      'channel': 'Tom Gaddis | Smart AI Operators',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:42](https://www.youtube.com/watch?v=A_LppzjgUi0&t=1062s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In the business details, you can see right here it says that this this business '
              'has no chat widget on their website. That means they are not taking advantage '
              'of an AI agent to li lighten the load of their people and answering calls, '
              'answering questions, booking appointments.',
      'timestamp': 1062,
      'timestamp_label': '[00:17:42]',
      'timestamp_seconds': 1062,
      'tip': 'In the business details, you can see right here it says that this this business '
             'has no chat widget on their website. That means they are not taking advantage of '
             'an AI agent to li lighten the load of their people and answering calls, '
             'answering questions, booking appointments.',
      'title': 'This AI Prospecting Update Just Made Cold Outreach Obsolete (500 Leads in '
               'Minutes) (Tom Gaddis | Smart AI Operators)',
      'url': 'https://www.youtube.com/watch?v=A_LppzjgUi0&t=1062s',
      'video_id': 'A_LppzjgUi0'},
     {'author': 'ProtaSystem',
      'channel': 'ProtaSystem',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:26](https://www.youtube.com/watch?v=6l0a6If9Oyk&t=326s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'These automated ready-to-send responses give freelancers the exact phrasing '
              'needed to push back and establish firm legal boundaries without alienating '
              'clients or destroying the relationship.',
      'timestamp': 326,
      'timestamp_label': '[00:05:26]',
      'timestamp_seconds': 326,
      'tip': 'These automated ready-to-send responses give freelancers the exact phrasing '
             'needed to push back and establish firm legal boundaries without alienating '
             'clients or destroying the relationship.',
      'title': 'Uncapped Indemnity & Scope Creep: The Contract Traps Every Freelancer Faces '
               '(ProtaSystem)',
      'url': 'https://www.youtube.com/watch?v=6l0a6If9Oyk&t=326s',
      'video_id': '6l0a6If9Oyk'},
     {'author': 'Alex Berman',
      'channel': 'Alex Berman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=Kjfkoa15cNU&t=139s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "George is doing, founder at Link Lemon. I don't care about Link Lemon. I don't "
              'care about founder. AI and automation for B2B businesses. If his was instead '
              "using AI to save agency owners 20,000 a month. That's what Jorge here should "
              'write.',
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': "George is doing, founder at Link Lemon. I don't care about Link Lemon. I don't "
             'care about founder. AI and automation for B2B businesses. If his was instead '
             "using AI to save agency owners 20,000 a month. That's what Jorge here should "
             'write.',
      'title': 'How I Do LinkedIn Outreach in 2026 (Alex Berman)',
      'url': 'https://www.youtube.com/watch?v=Kjfkoa15cNU&t=139s',
      'video_id': 'Kjfkoa15cNU'},
     {'author': 'Cleverly | #1 B2B Lead Generation Agency',
      'channel': 'Cleverly | #1 B2B Lead Generation Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:53](https://www.youtube.com/watch?v=h66nRoG6w0E&t=593s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh Cleverly has automation, obviously, so you can uh license that from us. We '
              'also have done-for-you services if you need help with this advanced targeting '
              'copy. And you want this 100% managed for you with an appointment setter. But, '
              "it's pretty straightforward.",
      'timestamp': 593,
      'timestamp_label': '[00:09:53]',
      'timestamp_seconds': 593,
      'tip': 'Uh Cleverly has automation, obviously, so you can uh license that from us. We '
             'also have done-for-you services if you need help with this advanced targeting '
             'copy. And you want this 100% managed for you with an appointment setter. But, '
             "it's pretty straightforward.",
      'title': 'The Only LinkedIn Outreach Strategy You Need in 2026 (Cleverly | #1 B2B Lead '
               'Generation Agency)',
      'url': 'https://www.youtube.com/watch?v=h66nRoG6w0E&t=593s',
      'video_id': 'h66nRoG6w0E'},
     {'author': 'Micah Johnson',
      'channel': 'Micah Johnson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=lBhO8Q-MxYI&t=39s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's a completely different agreement. So, if you're building anything with "
              'sensitive or proprietary data, the API is 100% the way to go. Next thing we got '
              'to learn about is ads have arrived. The updated policy introduces advertising '
              'for free and go-tier users.',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': "That's a completely different agreement. So, if you're building anything with "
             'sensitive or proprietary data, the API is 100% the way to go. Next thing we got '
             'to learn about is ads have arrived. The updated policy introduces advertising '
             'for free and go-tier users.',
      'title': "OpenAI's New Privacy Policy: What Every Business Owner Needs to Know (Micah "
               'Johnson)',
      'url': 'https://www.youtube.com/watch?v=lBhO8Q-MxYI&t=39s',
      'video_id': 'lBhO8Q-MxYI'},
     {'author': 'SecureCyberGates',
      'channel': 'SecureCyberGates',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:20](https://www.youtube.com/watch?v=TcAbiyEqBFM&t=260s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So we have some kind of shedding procedure here. So shedding script is runs '
              'against a client in which needs to be removed. So we may have a sharing script. '
              'Uh it runs automatically as a housekeeping jobs. So this automated backup auto '
              'backup files roll back in 35 days.',
      'timestamp': 260,
      'timestamp_label': '[00:04:20]',
      'timestamp_seconds': 260,
      'tip': 'So we have some kind of shedding procedure here. So shedding script is runs '
             'against a client in which needs to be removed. So we may have a sharing script. '
             'Uh it runs automatically as a housekeeping jobs. So this automated backup auto '
             'backup files roll back in 35 days.',
      'title': '23-[5.16] SOC2 – Data Retention Policy (SecureCyberGates)',
      'url': 'https://www.youtube.com/watch?v=TcAbiyEqBFM&t=260s',
      'video_id': 'TcAbiyEqBFM'},
     {'author': 'Nate Herk | AI Automation',
      'channel': 'Nate Herk | AI Automation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:16](https://www.youtube.com/watch?v=XB2xmX3USUI&t=1516s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I said it was like a beauty salon and stuff like that, they'd probably "
              'immediately disqualify themselves in their brain. And so I said, "Hey, I put '
              "together something uh I think you'd find interesting. It's basically a intent "
              'based email scraping and outreach system.',
      'timestamp': 1516,
      'timestamp_label': '[00:25:16]',
      'timestamp_seconds': 1516,
      'tip': "I said it was like a beauty salon and stuff like that, they'd probably "
             'immediately disqualify themselves in their brain. And so I said, "Hey, I put '
             "together something uh I think you'd find interesting. It's basically a intent "
             'based email scraping and outreach system.',
      'title': 'How a College Student Made $500k with Cold Email (Exact Framework) (Nate Herk '
               '| AI Automation)',
      'url': 'https://www.youtube.com/watch?v=XB2xmX3USUI&t=1516s',
      'video_id': 'XB2xmX3USUI'},
     {'author': 'Josue AI',
      'channel': 'Josue AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:53](https://www.youtube.com/watch?v=57vMJTMbsSc&t=113s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So you're going to paste your API key in there. And then we need a base URL and "
              'basically this is just going to be the URL that you see up here up to where it '
              'says cloud slash.',
      'timestamp': 113,
      'timestamp_label': '[00:01:53]',
      'timestamp_seconds': 113,
      'tip': "So you're going to paste your API key in there. And then we need a base URL and "
             'basically this is just going to be the URL that you see up here up to where it '
             'says cloud slash.',
      'title': 'Migrate All Your n8n Workflows in Minutes (Cloud/Self-Hosted) (Josue AI)',
      'url': 'https://www.youtube.com/watch?v=57vMJTMbsSc&t=113s',
      'video_id': '57vMJTMbsSc'},
     {'author': 'IBM Technology',
      'channel': 'IBM Technology',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:19](https://www.youtube.com/watch?v=UabBYexBD4k&t=619s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So where does this leave us? Well, if your problem involves a bounded data set '
              'and requires complex global reasoning like analyzing a specific legal contract '
              'or summarizing a book, I think long context is the way to go. It simplifies the '
              'stack and it improves the reasoning.',
      'timestamp': 619,
      'timestamp_label': '[00:10:19]',
      'timestamp_seconds': 619,
      'tip': 'So where does this leave us? Well, if your problem involves a bounded data set '
             'and requires complex global reasoning like analyzing a specific legal contract '
             'or summarizing a book, I think long context is the way to go. It simplifies the '
             'stack and it improves the reasoning.',
      'title': 'Is RAG Still Needed? Choosing the Best Approach for LLMs (IBM Technology)',
      'url': 'https://www.youtube.com/watch?v=UabBYexBD4k&t=619s',
      'video_id': 'UabBYexBD4k'},
     {'author': 'HubSpot Marketing',
      'channel': 'HubSpot Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:07](https://www.youtube.com/watch?v=uPo9D-wZv6s&t=667s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re empowering others by celebrating the success of maybe your clients and "
              'beyond. Screenshots of success, results, etc. One of the things that you want '
              'to do is identify a few content pillars.',
      'timestamp': 667,
      'timestamp_label': '[00:11:07]',
      'timestamp_seconds': 667,
      'tip': "'re empowering others by celebrating the success of maybe your clients and "
             'beyond. Screenshots of success, results, etc. One of the things that you want to '
             'do is identify a few content pillars.',
      'title': 'The Latest LinkedIn Lead Generation Strategies That Generated $2M+ (No Cold '
               'InMails) (HubSpot Marketing)',
      'url': 'https://www.youtube.com/watch?v=uPo9D-wZv6s&t=667s',
      'video_id': 'uPo9D-wZv6s'},
     {'author': 'Bo Sar',
      'channel': 'Bo Sar',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=pba8FIkOilY&t=21s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'AI to produce custom design work for clients up front to win the business '
              'before the contract is even signed. Or an ad agency that uses AI to create '
              'stunning video ads without the time and expense of setting up a physical shoot.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'AI to produce custom design work for clients up front to win the business before '
             'the contract is even signed. Or an ad agency that uses AI to create stunning '
             'video ads without the time and expense of setting up a physical shoot.',
      'title': 'The AI-First Agency Model YC Just Revealed (6 services to sell) (Bo Sar)',
      'url': 'https://www.youtube.com/watch?v=pba8FIkOilY&t=21s',
      'video_id': 'pba8FIkOilY'},
     {'author': 'NoCode with Sam Oluwagbami',
      'channel': 'NoCode with Sam Oluwagbami',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=xQf-khf_CWE&t=90s)',
      'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                   'fixed-scope workflow sprints, and managed automation retainers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So this is what the B2B sales automation platform is about. So it's a platform "
              'that puts in all of all of your several hs puts them together in one h. So, '
              "we're going to be building that app.",
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': "So this is what the B2B sales automation platform is about. So it's a platform "
             'that puts in all of all of your several hs puts them together in one h. So, '
             "we're going to be building that app.",
      'title': 'Cold Email is Dead — I Built an AI Outreach System That Does Everything for '
               'You (Lead to Meeting) (NoCode with Sam Oluwagbami)',
      'url': 'https://www.youtube.com/watch?v=xQf-khf_CWE&t=90s',
      'video_id': 'xQf-khf_CWE'}],
 10: [{'author': 'Cole Medin',
       'channel': 'Cole Medin',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:59](https://www.youtube.com/watch?v=p0FERNkpyHE&t=359s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'SQL database into what can act as a vector database we have fast API for '
               'building our agent API in Python and then finally the AI coding assistant that '
               'I used to help me build This entire agent is claude code which is an absolute '
               'beast of an AI coding assistant.',
       'timestamp': 359,
       'timestamp_label': '[00:05:59]',
       'timestamp_seconds': 359,
       'tip': 'SQL database into what can act as a vector database we have fast API for '
              'building our agent API in Python and then finally the AI coding assistant that '
              'I used to help me build This entire agent is claude code which is an absolute '
              'beast of an AI coding assistant.',
       'title': 'Introducing RAG 2.0: Agentic RAG + Knowledge Graphs (FREE Template) (Cole '
                'Medin)',
       'url': 'https://www.youtube.com/watch?v=p0FERNkpyHE&t=359s',
       'video_id': 'p0FERNkpyHE'},
      {'author': 'Nick Saraev',
       'channel': 'Nick Saraev',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:26](https://www.youtube.com/watch?v=T9diMzLIpqQ&t=146s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Our solution as an AI automation agency is going to be an automated workflow '
               "that captures form submissions, scores, leads, and then updates the CRM. I'm "
               "going to paste the scope. I'm going to paste in the cost. And then I'm also "
               'going to paste in the how soon.',
       'timestamp': 146,
       'timestamp_label': '[00:02:26]',
       'timestamp_seconds': 146,
       'tip': 'Our solution as an AI automation agency is going to be an automated workflow '
              "that captures form submissions, scores, leads, and then updates the CRM. I'm "
              "going to paste the scope. I'm going to paste in the cost. And then I'm also "
              'going to paste in the how soon.',
       'title': 'Sell These 3 Simple AI Automations for $1.7K to B2B Agencies (Nick Saraev)',
       'url': 'https://www.youtube.com/watch?v=T9diMzLIpqQ&t=146s',
       'video_id': 'T9diMzLIpqQ'},
      {'author': 'Jonas | AI Tools & Automation',
       'channel': 'Jonas | AI Tools & Automation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:43](https://www.youtube.com/watch?v=4imOFZeP7nk&t=43s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Today, I'm going to show you how I run my AI automation business for free. "
               'This is my automation dashboard, as you can see here. There are over 100 '
               'workflows in here. Everything from WhatsApp bots to payment syncs, lead '
               'follow-ups.',
       'timestamp': 43,
       'timestamp_label': '[00:00:43]',
       'timestamp_seconds': 43,
       'tip': "Today, I'm going to show you how I run my AI automation business for free. This "
              'is my automation dashboard, as you can see here. There are over 100 workflows '
              'in here. Everything from WhatsApp bots to payment syncs, lead follow-ups.',
       'title': 'I Run My AI Automation Business for $0 in Software (Zapier vs Make vs n8n) '
                '(Jonas | AI Tools & Automation)',
       'url': 'https://www.youtube.com/watch?v=4imOFZeP7nk&t=43s',
       'video_id': '4imOFZeP7nk'},
      {'author': 'AI Hustle Lab',
       'channel': 'AI Hustle Lab',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:26](https://www.youtube.com/watch?v=6FS1eyS2agI&t=146s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Our solution as an A automation agency is going to be an automated workflow '
               "that captures form submissions, scores, leads, and then updates the CRM. I'm "
               "going to paste the scope. I'm going to paste in the cost. And then I'm also "
               'going to paste in the how soon.',
       'timestamp': 146,
       'timestamp_label': '[00:02:26]',
       'timestamp_seconds': 146,
       'tip': 'Our solution as an A automation agency is going to be an automated workflow '
              "that captures form submissions, scores, leads, and then updates the CRM. I'm "
              "going to paste the scope. I'm going to paste in the cost. And then I'm also "
              'going to paste in the how soon.',
       'title': 'Sell These 3 Simple AI Automations for $1.7K to B2B Agencies (AI Hustle Lab)',
       'url': 'https://www.youtube.com/watch?v=6FS1eyS2agI&t=146s',
       'video_id': '6FS1eyS2agI'},
      {'author': 'Voice AI Decoded',
       'channel': 'Voice AI Decoded',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:29](https://www.youtube.com/watch?v=UiKoEHbio38&t=569s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, if you're nontechnical, if you like building in no code, and you don't "
               'want to be in the weeds building voice agents via an API, Retail for me is '
               "about as good as it gets. So, next up, let's have a look at Bland AI.",
       'timestamp': 569,
       'timestamp_label': '[00:09:29]',
       'timestamp_seconds': 569,
       'tip': "So, if you're nontechnical, if you like building in no code, and you don't want "
              'to be in the weeds building voice agents via an API, Retail for me is about as '
              "good as it gets. So, next up, let's have a look at Bland AI.",
       'title': "Retell AI vs Bland AI (Don't choose WRONG!) (Voice AI Decoded)",
       'url': 'https://www.youtube.com/watch?v=UiKoEHbio38&t=569s',
       'video_id': 'UiKoEHbio38'},
      {'author': 'Sean Malone | Close Bigger Deals',
       'channel': 'Sean Malone | Close Bigger Deals',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:23](https://www.youtube.com/watch?v=fXrfPpcs7fw&t=263s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Instead, try something like, your practice seems awesome, name, but when '
               'someone calls after 5, does anyone pick up? No AI, no agent, no automation, '
               'just the hole in their business. Asked as a question that they can answer in '
               "one line. But Sean, I haven't talked to them yet.",
       'timestamp': 263,
       'timestamp_label': '[00:04:23]',
       'timestamp_seconds': 263,
       'tip': 'Instead, try something like, your practice seems awesome, name, but when '
              'someone calls after 5, does anyone pick up? No AI, no agent, no automation, '
              'just the hole in their business. Asked as a question that they can answer in '
              "one line. But Sean, I haven't talked to them yet.",
       'title': 'How to Sell AI Automation Services (Without Pitching AI) (Sean Malone | Close '
                'Bigger Deals)',
       'url': 'https://www.youtube.com/watch?v=fXrfPpcs7fw&t=263s',
       'video_id': 'fXrfPpcs7fw'},
      {'author': 'Nick Puru | AI Automation',
       'channel': 'Nick Puru | AI Automation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:21:17](https://www.youtube.com/watch?v=7UpuiFHBvec&t=1277s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re building an AI agency or just implementing automation into your company or "
               'AI into your company in whatever sense, we offer one-on-one help where we walk '
               'you through everything.',
       'timestamp': 1277,
       'timestamp_label': '[00:21:17]',
       'timestamp_seconds': 1277,
       'tip': "'re building an AI agency or just implementing automation into your company or "
              'AI into your company in whatever sense, we offer one-on-one help where we walk '
              'you through everything.',
       'title': 'How to Perform $100,000 AI Audits For Businesses (Complete Guide) (Nick Puru '
                '| AI Automation)',
       'url': 'https://www.youtube.com/watch?v=7UpuiFHBvec&t=1277s',
       'video_id': '7UpuiFHBvec'},
      {'author': 'Liam Ottley',
       'channel': 'Liam Ottley',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:36](https://www.youtube.com/watch?v=2CdNLDttOSg&t=96s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, we have been building Moni Groups since October 2023. Throughout our AI '
               'agency journey, we have successfully completed over 50 AI projects working '
               'with clients from all around the world with across 10 more than 10 industries.',
       'timestamp': 96,
       'timestamp_label': '[00:01:36]',
       'timestamp_seconds': 96,
       'tip': 'So, we have been building Moni Groups since October 2023. Throughout our AI '
              'agency journey, we have successfully completed over 50 AI projects working with '
              'clients from all around the world with across 10 more than 10 industries.',
       'title': 'How Two 19-Year-Olds Made $320K in 6 Months Selling AI Audits (Full '
                'Breakdown) (Liam Ottley)',
       'url': 'https://www.youtube.com/watch?v=2CdNLDttOSg&t=96s',
       'video_id': '2CdNLDttOSg'},
      {'author': 'Carson Reed',
       'channel': 'Carson Reed',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:31:21](https://www.youtube.com/watch?v=L1LsEN_iuIc&t=1881s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'t want the error of one hurting a client's reputation or to just AI slop "
               'being incorrect to that to that, you know, uh question they have. Um now, when '
               'you use automation on LinkedIn, and you got to make sure that your LinkedIn '
               'account, your profile, is older than 1 year.',
       'timestamp': 1881,
       'timestamp_label': '[00:31:21]',
       'timestamp_seconds': 1881,
       'tip': "'t want the error of one hurting a client's reputation or to just AI slop being "
              'incorrect to that to that, you know, uh question they have. Um now, when you '
              'use automation on LinkedIn, and you got to make sure that your LinkedIn '
              'account, your profile, is older than 1 year.',
       'title': 'How To Sign AI Agency Clients Using Outreach in 2026 (Carson Reed)',
       'url': 'https://www.youtube.com/watch?v=L1LsEN_iuIc&t=1881s',
       'video_id': 'L1LsEN_iuIc'},
      {'author': 'Nate Herk | AI Automation',
       'channel': 'Nate Herk | AI Automation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=SAerRtQLD0I&t=21s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "1,200 LinkedIn agent, I did not sell the agent itself. I didn't get it on a "
               'call and say, "Hey, here\'s this workflow. Here\'s how many nodes it has. " '
               'None of that matters to the business owner. What I actually sold was the idea, '
               'the outcome.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': "1,200 LinkedIn agent, I did not sell the agent itself. I didn't get it on a "
              'call and say, "Hey, here\'s this workflow. Here\'s how many nodes it has. " '
              'None of that matters to the business owner. What I actually sold was the idea, '
              'the outcome.',
       'title': 'The TRUTH About Selling AI Automations to Businesses (Nate Herk | AI '
                'Automation)',
       'url': 'https://www.youtube.com/watch?v=SAerRtQLD0I&t=21s',
       'video_id': 'SAerRtQLD0I'},
      {'author': 'Cognitive Capital',
       'channel': 'Cognitive Capital',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:55](https://www.youtube.com/watch?v=j2Bqq0VTv0o&t=415s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'To make this totally concrete, think about workflow products that collect '
               'super sensitive user data. Take something like the Side Hustle Command Center. '
               "It's an AI-driven educational template that collects people's personal budgets "
               'and financial goals.',
       'timestamp': 415,
       'timestamp_label': '[00:06:55]',
       'timestamp_seconds': 415,
       'tip': 'To make this totally concrete, think about workflow products that collect super '
              "sensitive user data. Take something like the Side Hustle Command Center. It's "
              "an AI-driven educational template that collects people's personal budgets and "
              'financial goals.',
       'title': 'OpenAI Privacy Filter: Redact PII Locally (AI Workflow Explained) (Cognitive '
                'Capital)',
       'url': 'https://www.youtube.com/watch?v=j2Bqq0VTv0o&t=415s',
       'video_id': 'j2Bqq0VTv0o'},
      {'author': 'Michael Reimer | HighLevel & AI Systems',
       'channel': 'Michael Reimer | HighLevel & AI Systems',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:33](https://www.youtube.com/watch?v=IWNNb6VOVz8&t=93s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'If trust is weak, recommend reputation management. If website traffic is '
               'coming but no leads, recommend website optimization. The key is to sell the '
               'first measurable workflow, not a giant AI transformation.',
       'timestamp': 93,
       'timestamp_label': '[00:01:33]',
       'timestamp_seconds': 93,
       'tip': 'If trust is weak, recommend reputation management. If website traffic is coming '
              'but no leads, recommend website optimization. The key is to sell the first '
              'measurable workflow, not a giant AI transformation.',
       'title': 'The Exact Script to Close AI Agency Clients on a Discovery Call (Michael '
                'Reimer | HighLevel & AI Systems)',
       'url': 'https://www.youtube.com/watch?v=IWNNb6VOVz8&t=93s',
       'video_id': 'IWNNb6VOVz8'},
      {'author': 'The AI Architects | Tom Crawshaw',
       'channel': 'The AI Architects | Tom Crawshaw',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:43](https://www.youtube.com/watch?v=HMo8ixMd4ts&t=343s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Pick one, become the expert, and learn their problems. And you could even take '
               'the skills that you learn building workflows to build your own pipeline and '
               'potentially offer that as a service.',
       'timestamp': 343,
       'timestamp_label': '[00:05:43]',
       'timestamp_seconds': 343,
       'tip': 'Pick one, become the expert, and learn their problems. And you could even take '
              'the skills that you learn building workflows to build your own pipeline and '
              'potentially offer that as a service.',
       'title': "Don't Sell AI Automations Before You Watch THIS Video (The AI Architects | "
                'Tom Crawshaw)',
       'url': 'https://www.youtube.com/watch?v=HMo8ixMd4ts&t=343s',
       'video_id': 'HMo8ixMd4ts'},
      {'author': 'Mikey No Code',
       'channel': 'Mikey No Code',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:20:32](https://www.youtube.com/watch?v=i4z0kCcByY8&t=1232s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So now let's return to base 44. Open up agents from the left sidebar and "
               'create a new super agent. Go to general and then open up the AI model section. '
               'Make sure both the chat model and the automated task model are all still set '
               'to Opus 4.',
       'timestamp': 1232,
       'timestamp_label': '[00:20:32]',
       'timestamp_seconds': 1232,
       'tip': "So now let's return to base 44. Open up agents from the left sidebar and create "
              'a new super agent. Go to general and then open up the AI model section. Make '
              'sure both the chat model and the automated task model are all still set to Opus '
              '4.',
       'title': 'How to Start an AI Automation Agency in 2026 (Step by Step) (Mikey No Code)',
       'url': 'https://www.youtube.com/watch?v=i4z0kCcByY8&t=1232s',
       'video_id': 'i4z0kCcByY8'},
      {'author': 'Belt Course',
       'channel': 'Belt Course',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:06](https://www.youtube.com/watch?v=YaFtlj9qXQc&t=126s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Basically, the highest leverage AI and automation opportunities and a 90-day '
               'prioritized road map that turns into implementation projects. The most '
               'important thing is the outcome. Your client knows exactly where automation or '
               'AI deserves a budget and what returns to expect.',
       'timestamp': 126,
       'timestamp_label': '[00:02:06]',
       'timestamp_seconds': 126,
       'tip': 'Basically, the highest leverage AI and automation opportunities and a 90-day '
              'prioritized road map that turns into implementation projects. The most '
              'important thing is the outcome. Your client knows exactly where automation or '
              'AI deserves a budget and what returns to expect.',
       'title': 'How to Sell AI Services with a Paid AI Business Audit (Step-by-Step '
                'Framework) (Belt Course)',
       'url': 'https://www.youtube.com/watch?v=YaFtlj9qXQc&t=126s',
       'video_id': 'YaFtlj9qXQc'}],
 11: [{'author': 'Sabrina Ramonov 🍄',
       'channel': 'Sabrina Ramonov 🍄',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:13](https://www.youtube.com/watch?v=I1NSFLOBQvc&t=373s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re going to be able to scale to. At least not without hiring a team and "
               'putting all of your full-time efforts into it. Like, I have a technical '
               "background. I'm not an amazing coder by any stretch of imagination, but even I "
               'personally would not start an AI automation agency.',
       'timestamp': 373,
       'timestamp_label': '[00:06:13]',
       'timestamp_seconds': 373,
       'tip': "'re going to be able to scale to. At least not without hiring a team and "
              'putting all of your full-time efforts into it. Like, I have a technical '
              "background. I'm not an amazing coder by any stretch of imagination, but even I "
              'personally would not start an AI automation agency.',
       'title': 'What Nobody Tells You About Selling AI Automations (Sabrina Ramonov 🍄)',
       'url': 'https://www.youtube.com/watch?v=I1NSFLOBQvc&t=373s',
       'video_id': 'I1NSFLOBQvc'},
      {'author': 'Paired Recruiting',
       'channel': 'Paired Recruiting',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:10](https://www.youtube.com/watch?v=TdMOpd_cG0A&t=250s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "The trade-off is that it takes a bit more time to learn. You're not just "
               "connecting apps, you're actually building logic, but once it clicks, you get "
               "much more control. Pricing also tends to scale better since it's based more on "
               'operations instead of every single step.',
       'timestamp': 250,
       'timestamp_label': '[00:04:10]',
       'timestamp_seconds': 250,
       'tip': "The trade-off is that it takes a bit more time to learn. You're not just "
              "connecting apps, you're actually building logic, but once it clicks, you get "
              "much more control. Pricing also tends to scale better since it's based more on "
              'operations instead of every single step.',
       'title': 'Zapier vs Make vs n8n: Which Automation Tool Is Best for Your Team? (HONEST '
                'REVIEW) (Paired Recruiting)',
       'url': 'https://www.youtube.com/watch?v=TdMOpd_cG0A&t=250s',
       'video_id': 'TdMOpd_cG0A'},
      {'author': 'Brendan Jowett',
       'channel': 'Brendan Jowett',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:08](https://www.youtube.com/watch?v=Ky2Z6kGp1Vk&t=188s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "24/7, I've got something for you. My team at Inflate AI builds inbound and "
               'outbound calling systems to automate voice conversations across your business. '
               "We're talking 24/7 receptionists, speedtole outbound callers, appointment "
               'booking, whatever your business needs.',
       'timestamp': 188,
       'timestamp_label': '[00:03:08]',
       'timestamp_seconds': 188,
       'tip': "24/7, I've got something for you. My team at Inflate AI builds inbound and "
              'outbound calling systems to automate voice conversations across your business. '
              "We're talking 24/7 receptionists, speedtole outbound callers, appointment "
              'booking, whatever your business needs.',
       'title': 'The Darkside of AI Voice Agents (The Truth) (Brendan Jowett)',
       'url': 'https://www.youtube.com/watch?v=Ky2Z6kGp1Vk&t=188s',
       'video_id': 'Ky2Z6kGp1Vk'},
      {'author': 'LaunchFast with Bal Sieber',
       'channel': 'LaunchFast with Bal Sieber',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:10](https://www.youtube.com/watch?v=rI1y1OsDxdw&t=70s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Hey, I'm Ba, a designer with over 20 years of experience. I spent 15 of those "
               'in the agency world before going solo and building a oneperson business that '
               'runs on systems, not chaos.',
       'timestamp': 70,
       'timestamp_label': '[00:01:10]',
       'timestamp_seconds': 70,
       'tip': "Hey, I'm Ba, a designer with over 20 years of experience. I spent 15 of those "
              'in the agency world before going solo and building a oneperson business that '
              'runs on systems, not chaos.',
       'title': 'Brett From DesignJoy Did It. Why Can’t You? (LaunchFast with Bal Sieber)',
       'url': 'https://www.youtube.com/watch?v=rI1y1OsDxdw&t=70s',
       'video_id': 'rI1y1OsDxdw'},
      {'author': 'Nick Saraev Daily',
       'channel': 'Nick Saraev Daily',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:50](https://www.youtube.com/watch?v=LjJGh4J1eqM&t=50s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I\'ll double-check after the the stream. Hamda says, "Hey Nick, really '
               "appreciate all the value you've been sharing. I'm building an email automation "
               "system for a client and using it for myself, too. I've run into an issue with "
               'the 45-minute timeout.',
       'timestamp': 50,
       'timestamp_label': '[00:00:50]',
       'timestamp_seconds': 50,
       'tip': 'I\'ll double-check after the the stream. Hamda says, "Hey Nick, really '
              "appreciate all the value you've been sharing. I'm building an email automation "
              "system for a client and using it for myself, too. I've run into an issue with "
              'the 45-minute timeout.',
       'title': '3 AI Agency Retainer Options You Can Steal Today (Nick Saraev Daily)',
       'url': 'https://www.youtube.com/watch?v=LjJGh4J1eqM&t=50s',
       'video_id': 'LjJGh4J1eqM'},
      {'author': 'Starter Story',
       'channel': 'Starter Story',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:50](https://www.youtube.com/watch?v=vedkm3ZmHIE&t=650s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Him to work less and probably sleep better at night but what I love about '
               "Brett is that he doesn't just sell courses he continues to build his business "
               'serve clients and put in the Reps on design.',
       'timestamp': 650,
       'timestamp_label': '[00:10:50]',
       'timestamp_seconds': 650,
       'tip': 'Him to work less and probably sleep better at night but what I love about Brett '
              "is that he doesn't just sell courses he continues to build his business serve "
              'clients and put in the Reps on design.',
       'title': 'The $1.8M Solopreneur Playbook (Starter Story)',
       'url': 'https://www.youtube.com/watch?v=vedkm3ZmHIE&t=650s',
       'video_id': 'vedkm3ZmHIE'},
      {'author': 'Hey sidG',
       'channel': 'Hey sidG',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:02](https://www.youtube.com/watch?v=r4hp_y9_V3w&t=122s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A user asks something, the system zips over to the knowledge base to retrieve '
               'the right context, and it uses that context to spit out a fact-based answer. '
               'Retrieve, augment, generate. Simple, clean, and really, really effective. And '
               'the impacts on the business?',
       'timestamp': 122,
       'timestamp_label': '[00:02:02]',
       'timestamp_seconds': 122,
       'tip': 'A user asks something, the system zips over to the knowledge base to retrieve '
              'the right context, and it uses that context to spit out a fact-based answer. '
              'Retrieve, augment, generate. Simple, clean, and really, really effective. And '
              'the impacts on the business?',
       'title': 'The Future of Enterprise AI: RAG vs. Agentic Workflows (Hey sidG)',
       'url': 'https://www.youtube.com/watch?v=r4hp_y9_V3w&t=122s',
       'video_id': 'r4hp_y9_V3w'},
      {'author': 'Sales Feed',
       'channel': 'Sales Feed',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:37](https://www.youtube.com/watch?v=3_RnVI6UFkA&t=697s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '"Hey, looks like your website is hosted on Shopify. Are you happy with the '
               'conversions over there? Are you happy with its conversion rate?" Or if you\'re '
               'a recruiter, you might say, "Looks like you\'re hiring for a senior business '
               'development manager.',
       'timestamp': 697,
       'timestamp_label': '[00:11:37]',
       'timestamp_seconds': 697,
       'tip': '"Hey, looks like your website is hosted on Shopify. Are you happy with the '
              'conversions over there? Are you happy with its conversion rate?" Or if you\'re '
              'a recruiter, you might say, "Looks like you\'re hiring for a senior business '
              'development manager.',
       'title': 'The Best LinkedIn Lead Generation Strategy for 2026 (Sales Feed)',
       'url': 'https://www.youtube.com/watch?v=3_RnVI6UFkA&t=697s',
       'video_id': '3_RnVI6UFkA'},
      {'author': 'Nick Saraev Unfiltered',
       'channel': 'Nick Saraev Unfiltered',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:05](https://www.youtube.com/watch?v=J6tKdJPDJiw&t=65s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And it\'s like, "Man, but onboarding is starting to take a really long while. '
               '" Then we build some onboarding automations. And it\'s like, "Oh my goodness, '
               'the onboarding is awesome, but now we just have so much client work. " Then '
               'you start building fulfillment automations.',
       'timestamp': 65,
       'timestamp_label': '[00:01:05]',
       'timestamp_seconds': 65,
       'tip': 'And it\'s like, "Man, but onboarding is starting to take a really long while. " '
              'Then we build some onboarding automations. And it\'s like, "Oh my goodness, the '
              'onboarding is awesome, but now we just have so much client work. " Then you '
              'start building fulfillment automations.',
       'title': 'Why AI automation agency is a great business model (Nick Saraev Unfiltered)',
       'url': 'https://www.youtube.com/watch?v=J6tKdJPDJiw&t=65s',
       'video_id': 'J6tKdJPDJiw'},
      {'author': 'Harry Roper',
       'channel': 'Harry Roper',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:16](https://www.youtube.com/watch?v=rO0i7sGwhCU&t=316s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Journey um we're already at a thousand MRI with the agency and now it's just "
               'about trying to grow a bit more so if you want to learn more about how to '
               'organize your business in psychoda so you can follow my journey as well I '
               'would watch this video next.',
       'timestamp': 316,
       'timestamp_label': '[00:05:16]',
       'timestamp_seconds': 316,
       'tip': "Journey um we're already at a thousand MRI with the agency and now it's just "
              'about trying to grow a bit more so if you want to learn more about how to '
              'organize your business in psychoda so you can follow my journey as well I would '
              'watch this video next.',
       'title': 'How I made $5K A Month Using The Design Joy Model (Harry Roper)',
       'url': 'https://www.youtube.com/watch?v=rO0i7sGwhCU&t=316s',
       'video_id': 'rO0i7sGwhCU'},
      {'author': 'Liam Ottley',
       'channel': 'Liam Ottley',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:20:19](https://www.youtube.com/watch?v=noivN2hIXLY&t=1219s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'This has taken that to another level. Just really building that trust and '
               'understanding of the business to make the development off the back so much '
               'easier.',
       'timestamp': 1219,
       'timestamp_label': '[00:20:19]',
       'timestamp_seconds': 1219,
       'tip': 'This has taken that to another level. Just really building that trust and '
              'understanding of the business to make the development off the back so much '
              'easier.',
       'title': 'How to Perform a $60,000 AI Audit (Beginner’s Guide) (Liam Ottley)',
       'url': 'https://www.youtube.com/watch?v=noivN2hIXLY&t=1219s',
       'video_id': 'noivN2hIXLY'},
      {'author': 'Nate Herk | AI Automation',
       'channel': 'Nate Herk | AI Automation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:49](https://www.youtube.com/watch?v=t1PTmpas0bg&t=109s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I just have to paste in the API key right here. Now, the other thing you are '
               "going to have to do is you're going to have to grab your base URL from up "
               "here. And you probably can't see it on my screen right now.",
       'timestamp': 109,
       'timestamp_label': '[00:01:49]',
       'timestamp_seconds': 109,
       'tip': 'I just have to paste in the API key right here. Now, the other thing you are '
              "going to have to do is you're going to have to grab your base URL from up here. "
              "And you probably can't see it on my screen right now.",
       'title': 'Easiest Way to Migrate n8n Workflows Between Accounts (cloud to self-hosted) '
                '(Nate Herk | AI Automation)',
       'url': 'https://www.youtube.com/watch?v=t1PTmpas0bg&t=109s',
       'video_id': 't1PTmpas0bg'},
      {'author': 'Demandflow',
       'channel': 'Demandflow',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:23](https://www.youtube.com/watch?v=w9gOdSLVu14&t=803s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "What the client is getting and ultimately if they're actually happy with your "
               "service as always thank you very much for watching watching and I'll catch you "
               'in the next one.',
       'timestamp': 803,
       'timestamp_label': '[00:13:23]',
       'timestamp_seconds': 803,
       'tip': "What the client is getting and ultimately if they're actually happy with your "
              "service as always thank you very much for watching watching and I'll catch you "
              'in the next one.',
       'title': 'how to actually build a sustainable productized service ($20k+) (Demandflow)',
       'url': 'https://www.youtube.com/watch?v=w9gOdSLVu14&t=803s',
       'video_id': 'w9gOdSLVu14'},
      {'author': 'Hyperautomation Labs',
       'channel': 'Hyperautomation Labs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:25](https://www.youtube.com/watch?v=Bm9fbVEZvHc&t=565s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '3 hours on, drops to about 4 minutes. Once Claude has the right context file '
               'and skill file, the agent reviews, tweaks the headline, sends a weekly client '
               'report for a marketing agency.',
       'timestamp': 565,
       'timestamp_label': '[00:09:25]',
       'timestamp_seconds': 565,
       'tip': '3 hours on, drops to about 4 minutes. Once Claude has the right context file '
              'and skill file, the agent reviews, tweaks the headline, sends a weekly client '
              'report for a marketing agency.',
       'title': 'How to Build & Sell AI Automations That Make $10K/mo (Full 6-Phase Playbook) '
                '(Hyperautomation Labs)',
       'url': 'https://www.youtube.com/watch?v=Bm9fbVEZvHc&t=565s',
       'video_id': 'Bm9fbVEZvHc'},
      {'author': 'Automate AI Consulting',
       'channel': 'Automate AI Consulting',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:14](https://www.youtube.com/watch?v=91lw5ubtLMc&t=194s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Where do they find their API keys? You're writing this so that if you were to "
               'disappear from the face of the earth, they or anyone that they hire can '
               "troubleshoot their own system. Once in a blue moon, you'll get a technical "
               'client that just wants the JSON file.',
       'timestamp': 194,
       'timestamp_label': '[00:03:14]',
       'timestamp_seconds': 194,
       'tip': "Where do they find their API keys? You're writing this so that if you were to "
              'disappear from the face of the earth, they or anyone that they hire can '
              "troubleshoot their own system. Once in a blue moon, you'll get a technical "
              'client that just wants the JSON file.',
       'title': 'How To Deliver Your N8N Automation To Clients Like An Expert (Automate AI '
                'Consulting)',
       'url': 'https://www.youtube.com/watch?v=91lw5ubtLMc&t=194s',
       'video_id': '91lw5ubtLMc'}],
 12: [{'author': 'Hyperautomation Labs',
       'channel': 'Hyperautomation Labs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:28](https://www.youtube.com/watch?v=Bm9fbVEZvHc&t=388s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '30 days of post-launch support. Pricing, and this is the part most people get '
               'wrong, is based on value, not hours. If your automation saves a client 10 '
               'hours a week at a $75 billing rate, that is $3,000 a month in value.',
       'timestamp': 388,
       'timestamp_label': '[00:06:28]',
       'timestamp_seconds': 388,
       'tip': '30 days of post-launch support. Pricing, and this is the part most people get '
              'wrong, is based on value, not hours. If your automation saves a client 10 hours '
              'a week at a $75 billing rate, that is $3,000 a month in value.',
       'title': 'How to Build & Sell AI Automations That Make $10K/mo (Full 6-Phase Playbook) '
                '(Hyperautomation Labs)',
       'url': 'https://www.youtube.com/watch?v=Bm9fbVEZvHc&t=388s',
       'video_id': 'Bm9fbVEZvHc'},
      {'author': 'Milan Tahliani',
       'channel': 'Milan Tahliani',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:27](https://www.youtube.com/watch?v=2goNKtgnIKg&t=207s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "ROI backed implementation plan for a given business's um AI infrastructure and "
               'AI um roadmap. So how do you as an AI agency owner actually go ahead and '
               'position the audit? Um so you want to frame the audit as value creation, '
               'right?',
       'timestamp': 207,
       'timestamp_label': '[00:03:27]',
       'timestamp_seconds': 207,
       'tip': "ROI backed implementation plan for a given business's um AI infrastructure and "
              'AI um roadmap. So how do you as an AI agency owner actually go ahead and '
              'position the audit? Um so you want to frame the audit as value creation, right?',
       'title': 'Why ALL AI Agencies Should Run AI Audits (And How To Do Them Properly!) '
                '(Milan Tahliani)',
       'url': 'https://www.youtube.com/watch?v=2goNKtgnIKg&t=207s',
       'video_id': '2goNKtgnIKg'},
      {'author': 'AI Tools for Business',
       'channel': 'AI Tools for Business',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:15](https://www.youtube.com/watch?v=T6Ij8zqR4Bo&t=315s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Tidio charges a flat $39 a month for 50 Lyro conversations. For a free start, '
               'Tidio wins easily. A real free plan against two 14-day trials. For AI on a '
               'budget, Tidio starter plus Lyro at about $68 a month is the cheapest way to '
               'have an AI agent answering.',
       'timestamp': 315,
       'timestamp_label': '[00:05:15]',
       'timestamp_seconds': 315,
       'tip': 'Tidio charges a flat $39 a month for 50 Lyro conversations. For a free start, '
              'Tidio wins easily. A real free plan against two 14-day trials. For AI on a '
              'budget, Tidio starter plus Lyro at about $68 a month is the cheapest way to '
              'have an AI agent answering.',
       'title': '3 AI Customer Support Tools for US Small Businesses in 2026 — Intercom vs '
                'Zendesk vs Tidio (AI Tools for Business)',
       'url': 'https://www.youtube.com/watch?v=T6Ij8zqR4Bo&t=315s',
       'video_id': 'T6Ij8zqR4Bo'},
      {'author': 'Jack',
       'channel': 'Jack',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:48](https://www.youtube.com/watch?v=4RYnbUHayhM&t=168s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '2-week warm-up period, still running LinkedIn automation, but we want to warm '
               'up those email inboxes, and then, based on what we see working well, we flow '
               "into a 6-week first month, where we get very tangible results on what's going "
               'to work within our outbound.',
       'timestamp': 168,
       'timestamp_label': '[00:02:48]',
       'timestamp_seconds': 168,
       'tip': '2-week warm-up period, still running LinkedIn automation, but we want to warm '
              'up those email inboxes, and then, based on what we see working well, we flow '
              "into a 6-week first month, where we get very tangible results on what's going "
              'to work within our outbound.',
       'title': 'How to Get B2B Clients on LinkedIn in 2026 (Intent-Based Outreach System) '
                '(Jack)',
       'url': 'https://www.youtube.com/watch?v=4RYnbUHayhM&t=168s',
       'video_id': '4RYnbUHayhM'},
      {'author': 'Zubair Trabzada | AI Workshop',
       'channel': 'Zubair Trabzada | AI Workshop',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:03](https://www.youtube.com/watch?v=XUYvDbAv1IA&t=123s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "The AI automation agency field is incredible and there's a lot of "
               'opportunities in it. But please please be aware this is not a joke. This is '
               "not some easy thing that you're going to jump in and you're going to start to "
               'make $50,000 on your first month.',
       'timestamp': 123,
       'timestamp_label': '[00:02:03]',
       'timestamp_seconds': 123,
       'tip': "The AI automation agency field is incredible and there's a lot of opportunities "
              'in it. But please please be aware this is not a joke. This is not some easy '
              "thing that you're going to jump in and you're going to start to make $50,000 on "
              'your first month.',
       'title': 'The TRUTH About Selling AI Automations to Businesses (Zubair Trabzada | AI '
                'Workshop)',
       'url': 'https://www.youtube.com/watch?v=XUYvDbAv1IA&t=123s',
       'video_id': 'XUYvDbAv1IA'},
      {'author': 'Stefan | AI',
       'channel': 'Stefan | AI',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:51](https://www.youtube.com/watch?v=NFQnvr9xNf8&t=531s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Talk with the people doing this work that needs to be automated. And then week '
               'two, we actually design the solution and in a 90-day implementation road map '
               'which shows a clear ROI that needs to be hit with in those 90 days.',
       'timestamp': 531,
       'timestamp_label': '[00:08:51]',
       'timestamp_seconds': 531,
       'tip': 'Talk with the people doing this work that needs to be automated. And then week '
              'two, we actually design the solution and in a 90-day implementation road map '
              'which shows a clear ROI that needs to be hit with in those 90 days.',
       'title': 'How to Execute $200K AI Audits for Businesses (Complete Framework) (Stefan | '
                'AI)',
       'url': 'https://www.youtube.com/watch?v=NFQnvr9xNf8&t=531s',
       'video_id': 'NFQnvr9xNf8'},
      {'author': 'Daniel Davidson',
       'channel': 'Daniel Davidson',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:16](https://www.youtube.com/watch?v=GYTt2lhl7Ms&t=136s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'From routing tickets to the appropriate team to trigger-based conversations '
               'closure. Now, oftentimes the real kicker when it comes to choosing a platform '
               'like this is set up time and pricing. And on Sparrow desk, paid plans start at '
               '$16 per agent per month, billed annually.',
       'timestamp': 136,
       'timestamp_label': '[00:02:16]',
       'timestamp_seconds': 136,
       'tip': 'From routing tickets to the appropriate team to trigger-based conversations '
              'closure. Now, oftentimes the real kicker when it comes to choosing a platform '
              'like this is set up time and pricing. And on Sparrow desk, paid plans start at '
              '$16 per agent per month, billed annually.',
       'title': '5 Best AI Customer Support Platforms (2026) - Top 5 Ranked (Daniel Davidson)',
       'url': 'https://www.youtube.com/watch?v=GYTt2lhl7Ms&t=136s',
       'video_id': 'GYTt2lhl7Ms'},
      {'author': 'Nick Saraev',
       'channel': 'Nick Saraev',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:00](https://www.youtube.com/watch?v=RmYTguzXrVM&t=120s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "You actually have a stable base. You don't start from zero every month. What "
               'you do is, sure, you might have a little bit of churn.',
       'timestamp': 120,
       'timestamp_label': '[00:02:00]',
       'timestamp_seconds': 120,
       'tip': "You actually have a stable base. You don't start from zero every month. What "
              'you do is, sure, you might have a little bit of churn.',
       'title': 'How I Turn One AI Project Into $5K Monthly Retainers (Nick Saraev)',
       'url': 'https://www.youtube.com/watch?v=RmYTguzXrVM&t=120s',
       'video_id': 'RmYTguzXrVM'},
      {'author': 'Chris Koerner on The Koerner Office Podcast',
       'channel': 'Chris Koerner on The Koerner Office Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:22](https://www.youtube.com/watch?v=bAzg8BugEVY&t=502s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And so now I have a very easy life. I work less than a full-time designer. So '
               'what were you charging per month per client those first few years? So, I '
               'started out at a measly $449 a month day one. That increased to $849 a month.',
       'timestamp': 502,
       'timestamp_label': '[00:08:22]',
       'timestamp_seconds': 502,
       'tip': 'And so now I have a very easy life. I work less than a full-time designer. So '
              'what were you charging per month per client those first few years? So, I '
              'started out at a measly $449 a month day one. That increased to $849 a month.',
       'title': "The Most Profitable Solo Business You've Never Heard Of (Chris Koerner on The "
                'Koerner Office Podcast)',
       'url': 'https://www.youtube.com/watch?v=bAzg8BugEVY&t=502s',
       'video_id': 'bAzg8BugEVY'},
      {'author': 'Metics Media',
       'channel': 'Metics Media',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:55](https://www.youtube.com/watch?v=oRI0lA-ZQ3w&t=55s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The downside is cost and flexibility. Their starter plan runs around $20 a '
               'month, billed annually, or $24 monthly, and it scales up from there based on '
               'usage. The other option is self hosting.',
       'timestamp': 55,
       'timestamp_label': '[00:00:55]',
       'timestamp_seconds': 55,
       'tip': 'The downside is cost and flexibility. Their starter plan runs around $20 a '
              'month, billed annually, or $24 monthly, and it scales up from there based on '
              'usage. The other option is self hosting.',
       'title': 'How to Use n8n for FREE in 2026 - n8n Self Hosting Setup (Metics Media)',
       'url': 'https://www.youtube.com/watch?v=oRI0lA-ZQ3w&t=55s',
       'video_id': 'oRI0lA-ZQ3w'},
      {'author': 'Tommy Clark',
       'channel': 'Tommy Clark',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:30](https://www.youtube.com/watch?v=MXBaHCO4WI8&t=390s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "We've helped 50 plus early stage SAS and service founders launch and scale "
               "founder content over the past one and a half years. It's been 3 years and "
               "we've done it for over a hundred. I also make a quick call to action that I "
               'write my newsletter every single week.',
       'timestamp': 390,
       'timestamp_label': '[00:06:30]',
       'timestamp_seconds': 390,
       'tip': "We've helped 50 plus early stage SAS and service founders launch and scale "
              "founder content over the past one and a half years. It's been 3 years and we've "
              'done it for over a hundred. I also make a quick call to action that I write my '
              'newsletter every single week.',
       'title': 'The Best LinkedIn Lead Generation Strategy for 2026 (Tommy Clark)',
       'url': 'https://www.youtube.com/watch?v=MXBaHCO4WI8&t=390s',
       'video_id': 'MXBaHCO4WI8'},
      {'author': 'Starter Story',
       'channel': 'Starter Story',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:36](https://www.youtube.com/watch?v=dXKzST0FE-A&t=36s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Lot of people say it's like the Netflix of design in this video he shares "
               'everything how he launched in 24 hours how he got his first client and how '
               "anyone can build a life-changing business while still working your day job I'm "
               'Pat walls and this is starter.',
       'timestamp': 36,
       'timestamp_label': '[00:00:36]',
       'timestamp_seconds': 36,
       'tip': "Lot of people say it's like the Netflix of design in this video he shares "
              'everything how he launched in 24 hours how he got his first client and how '
              "anyone can build a life-changing business while still working your day job I'm "
              'Pat walls and this is starter.',
       'title': 'I Make $1.3M/Year With One Skill (Starter Story)',
       'url': 'https://www.youtube.com/watch?v=dXKzST0FE-A&t=36s',
       'video_id': 'dXKzST0FE-A'},
      {'author': 'Privado AI',
       'channel': 'Privado AI',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:21](https://www.youtube.com/watch?v=3wH9U_IzNn8&t=681s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Fingerprinting specifically but it's interesting that they have come against "
               "come out against this move quite proactively so thanks so much that's all from "
               "me this week hope to see you at Prado ai's Bridge Summit next month and uh "
               "I'll see you next time.",
       'timestamp': 681,
       'timestamp_label': '[00:11:21]',
       'timestamp_seconds': 681,
       'tip': "Fingerprinting specifically but it's interesting that they have come against "
              "come out against this move quite proactively so thanks so much that's all from "
              "me this week hope to see you at Prado ai's Bridge Summit next month and uh I'll "
              'see you next time.',
       'title': 'Italian DPA fines OpenAI €15M, CPPA settles with data brokers, and Google '
                'allows fingerprinting. (Privado AI)',
       'url': 'https://www.youtube.com/watch?v=3wH9U_IzNn8&t=681s',
       'video_id': '3wH9U_IzNn8'},
      {'author': 'Lily Latzo | AI Automation',
       'channel': 'Lily Latzo | AI Automation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:09](https://www.youtube.com/watch?v=NjvNF17_97w&t=549s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That is five people booking in a call. If you close at 60%, that's three "
               'clients. And if your, you know, three clients are paying you 3K a month, '
               "that's 9K a month in MR from just one simple 7day sprint.",
       'timestamp': 549,
       'timestamp_label': '[00:09:09]',
       'timestamp_seconds': 549,
       'tip': "That is five people booking in a call. If you close at 60%, that's three "
              "clients. And if your, you know, three clients are paying you 3K a month, that's "
              '9K a month in MR from just one simple 7day sprint.',
       'title': 'How I Landed 3 AI Automation Clients in 7 Days | Simple Outreach System That '
                'Works (Lily Latzo | AI Automation)',
       'url': 'https://www.youtube.com/watch?v=NjvNF17_97w&t=549s',
       'video_id': 'NjvNF17_97w'},
      {'author': 'Noah Epstein',
       'channel': 'Noah Epstein',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:01](https://www.youtube.com/watch?v=fMdUS6amki0&t=241s)',
       'relevance': 'Attributed practitioner commentary on productized B2B AI implementation, '
                    'fixed-scope workflow sprints, and managed automation retainers (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So that's how I'd recommend doing about going about it. Find a business that's "
               'willing to pay. Then maybe a few days down the line, you say, "I\'ve got a '
               'solution for you or you\'re willing to pay." You get the money and then you '
               'start building. Or not even start building.',
       'timestamp': 241,
       'timestamp_label': '[00:04:01]',
       'timestamp_seconds': 241,
       'tip': "So that's how I'd recommend doing about going about it. Find a business that's "
              'willing to pay. Then maybe a few days down the line, you say, "I\'ve got a '
              'solution for you or you\'re willing to pay." You get the money and then you '
              'start building. Or not even start building.',
       'title': 'How I made $150k last month selling AI automations (Noah Epstein)',
       'url': 'https://www.youtube.com/watch?v=fMdUS6amki0&t=241s',
       'video_id': 'fMdUS6amki0'}]}
