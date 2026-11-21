"""Curated 180-citation Building an SEO Empire baseline (15 per chapter across Q1-Q12) mined strictly from verified Building an SEO Empire YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'10000',
     '30x',
     '45x',
     '50k',
     'abuse',
     'ads',
     'affiliate',
     'aged',
     'ahrefs',
     'analysis',
     'api',
     'arbitrage',
     'architecture',
     'articles',
     'astro',
     'audit',
     'author',
     'authority',
     'b2b',
     'backlink',
     'backlinks',
     'barnacle',
     'breton',
     'budget',
     'building',
     'business',
     'buyer',
     'buying',
     'calculator',
     'capture',
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
 2: {'10000',
     '30x',
     '45x',
     '50k',
     'abuse',
     'ads',
     'affiliate',
     'aged',
     'ahrefs',
     'analysis',
     'api',
     'arbitrage',
     'architecture',
     'articles',
     'astro',
     'audit',
     'author',
     'authority',
     'b2b',
     'backlink',
     'backlinks',
     'barnacle',
     'breton',
     'budget',
     'building',
     'business',
     'buyer',
     'buying',
     'calculator',
     'capture',
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
 3: {'10000',
     '30x',
     '45x',
     '50k',
     'abuse',
     'ads',
     'affiliate',
     'aged',
     'ahrefs',
     'analysis',
     'api',
     'arbitrage',
     'architecture',
     'articles',
     'astro',
     'audit',
     'author',
     'authority',
     'b2b',
     'backlink',
     'backlinks',
     'barnacle',
     'breton',
     'budget',
     'building',
     'business',
     'buyer',
     'buying',
     'calculator',
     'capture',
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
 4: {'10000',
     '30x',
     '45x',
     '50k',
     'abuse',
     'ads',
     'affiliate',
     'aged',
     'ahrefs',
     'analysis',
     'api',
     'arbitrage',
     'architecture',
     'articles',
     'astro',
     'audit',
     'author',
     'authority',
     'b2b',
     'backlink',
     'backlinks',
     'barnacle',
     'breton',
     'budget',
     'building',
     'business',
     'buyer',
     'buying',
     'calculator',
     'capital',
     'capture',
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
 5: {'10000',
     '30x',
     '45x',
     '50k',
     'abuse',
     'ads',
     'affiliate',
     'aged',
     'ahrefs',
     'analysis',
     'api',
     'arbitrage',
     'architecture',
     'articles',
     'astro',
     'audit',
     'author',
     'authority',
     'avoid',
     'b2b',
     'backlink',
     'backlinks',
     'barnacle',
     'breton',
     'budget',
     'building',
     'business',
     'buyer',
     'buying',
     'calculator',
     'capture',
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
 6: {'10000',
     '30x',
     '45x',
     '50k',
     'abuse',
     'ads',
     'affiliate',
     'aged',
     'ahrefs',
     'analysis',
     'api',
     'arbitrage',
     'architecture',
     'articles',
     'astro',
     'audit',
     'author',
     'authority',
     'b2b',
     'backlink',
     'backlinks',
     'barnacle',
     'breton',
     'budget',
     'building',
     'business',
     'buyer',
     'buying',
     'calculator',
     'capture',
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
 7: {'10000',
     '30x',
     '45x',
     '50k',
     'abuse',
     'ads',
     'affiliate',
     'aged',
     'ahrefs',
     'analysis',
     'api',
     'arbitrage',
     'architecture',
     'articles',
     'astro',
     'audit',
     'author',
     'authority',
     'b2b',
     'backlink',
     'backlinks',
     'barnacle',
     'breton',
     'budget',
     'building',
     'business',
     'buyer',
     'buying',
     'calculator',
     'capture',
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
 8: {'10000',
     '30x',
     '45x',
     '50k',
     'abuse',
     'ads',
     'affiliate',
     'aged',
     'ahrefs',
     'analysis',
     'api',
     'arbitrage',
     'architecture',
     'articles',
     'astro',
     'audit',
     'author',
     'authority',
     'b2b',
     'backlink',
     'backlinks',
     'barnacle',
     'breton',
     'budget',
     'building',
     'business',
     'buyer',
     'buying',
     'calculator',
     'capture',
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
 9: {'10000',
     '30x',
     '45x',
     '50k',
     'abuse',
     'ads',
     'affiliate',
     'aged',
     'agreement',
     'ahrefs',
     'analysis',
     'api',
     'arbitrage',
     'architecture',
     'articles',
     'astro',
     'audit',
     'author',
     'authority',
     'b2b',
     'backlink',
     'backlinks',
     'barnacle',
     'breton',
     'budget',
     'building',
     'business',
     'buyer',
     'buying',
     'calculator',
     'capture',
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
 10: {'10000',
      '30x',
      '45x',
      '50k',
      'abuse',
      'ads',
      'affiliate',
      'aged',
      'agent',
      'ahrefs',
      'ai',
      'analysis',
      'api',
      'arbitrage',
      'architecture',
      'articles',
      'astro',
      'audit',
      'author',
      'authority',
      'automate',
      'automation',
      'b2b',
      'backlink',
      'backlinks',
      'barnacle',
      'breton',
      'budget',
      'building',
      'business',
      'buyer',
      'buying',
      'calculator',
      'capture',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'10000',
      '30x',
      '45x',
      '50k',
      'abuse',
      'ads',
      'affiliate',
      'aged',
      'ahrefs',
      'analysis',
      'api',
      'arbitrage',
      'architecture',
      'articles',
      'astro',
      'audit',
      'author',
      'authority',
      'b2b',
      'backlink',
      'backlinks',
      'barnacle',
      'breton',
      'budget',
      'building',
      'business',
      'buyer',
      'buying',
      'calculator',
      'capture',
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
 12: {'10000',
      '30x',
      '45x',
      '50k',
      'abuse',
      'action',
      'ads',
      'affiliate',
      'aged',
      'ahrefs',
      'analysis',
      'api',
      'arbitrage',
      'architecture',
      'articles',
      'astro',
      'audit',
      'author',
      'authority',
      'b2b',
      'backlink',
      'backlinks',
      'barnacle',
      'breton',
      'budget',
      'building',
      'business',
      'buyer',
      'buying',
      'calculator',
      'capture',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'QUANTEVO',
      'channel': 'QUANTEVO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=JEma0TFSBVU&t=62s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Use Google AdSense, direct ads, or category sponsorships, especially once you '
              'get traffic. List service providers with affiliate programs and earn '
              'commissions on clicks or sales. Membership access in niche markets. You can '
              'even charge users to access the directory.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': 'Use Google AdSense, direct ads, or category sponsorships, especially once you '
             'get traffic. List service providers with affiliate programs and earn commissions '
             'on clicks or sales. Membership access in niche markets. You can even charge '
             'users to access the directory.',
      'title': 'Directory Website Business Model Explained in 3 Minutes! (QUANTEVO)',
      'url': 'https://www.youtube.com/watch?v=JEma0TFSBVU&t=62s',
      'video_id': 'JEma0TFSBVU'},
     {'author': 'SEO Jesus',
      'channel': 'SEO Jesus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:01](https://www.youtube.com/watch?v=AGcswUV4IEA&t=301s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Best examples I've seen of this was one client in the high value Finance Niche "
              'where they had a page that was getting some rankings but not really doing.',
      'timestamp': 301,
      'timestamp_label': '[00:05:01]',
      'timestamp_seconds': 301,
      'tip': "Best examples I've seen of this was one client in the high value Finance Niche "
             'where they had a page that was getting some rankings but not really doing.',
      'title': 'How I DOUBLED My Best AI Parasite Post Ranking In 1 Week With Expired Domain '
               'Backlinks (SEO Jesus)',
      'url': 'https://www.youtube.com/watch?v=AGcswUV4IEA&t=301s',
      'video_id': 'AGcswUV4IEA'},
     {'author': 'Edward Sturm',
      'channel': 'Edward Sturm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=8DuIlUdfY_w&t=118s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, my questions are, how do you build topical authority without defaulting to '
              'blog content? Are there other practical frameworks, deliverables, or tactics '
              'that help a client build depth around a topic beyond publishing educational '
              'articles?',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': 'So, my questions are, how do you build topical authority without defaulting to '
             'blog content? Are there other practical frameworks, deliverables, or tactics '
             'that help a client build depth around a topic beyond publishing educational '
             'articles?',
      'title': 'Topical Authority Isn’t Blog Posts - It’s This (Edward Sturm)',
      'url': 'https://www.youtube.com/watch?v=8DuIlUdfY_w&t=118s',
      'video_id': '8DuIlUdfY_w'},
     {'author': 'B2BSEOio',
      'channel': 'B2BSEOio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=P-NBpi1qUEo&t=42s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "50 backlinks from medical websites with DR 60 plus. The agency's approach pairs "
              'journalist outreach with expert commentary to earn editorial mentions and '
              'backlinks. SEO and link building, so it may not be the right fit if you need a '
              'full-service PR agency.',
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': "50 backlinks from medical websites with DR 60 plus. The agency's approach pairs "
             'journalist outreach with expert commentary to earn editorial mentions and '
             'backlinks. SEO and link building, so it may not be the right fit if you need a '
             'full-service PR agency.',
      'title': '8 HARO Link Building Agencies Compared: Who’s Best for Your Brand? (B2BSEOio)',
      'url': 'https://www.youtube.com/watch?v=P-NBpi1qUEo&t=42s',
      'video_id': 'P-NBpi1qUEo'},
     {'author': 'Rank Math SEO',
      'channel': 'Rank Math SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:43](https://www.youtube.com/watch?v=5EkSj0nrCpg&t=223s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Or are you building a niche site that specifically talks about Air Fryers? So '
              'the first thing you got to be clear when drawing up your site structure or '
              'architecture is to know the goal of your site and stick with it all the way.',
      'timestamp': 223,
      'timestamp_label': '[00:03:43]',
      'timestamp_seconds': 223,
      'tip': 'Or are you building a niche site that specifically talks about Air Fryers? So '
             'the first thing you got to be clear when drawing up your site structure or '
             'architecture is to know the goal of your site and stick with it all the way.',
      'title': 'How to Make a Silo Structure? - Step-by-Step Guide To Rank No #1 (Rank Math '
               'SEO)',
      'url': 'https://www.youtube.com/watch?v=5EkSj0nrCpg&t=223s',
      'video_id': '5EkSj0nrCpg'},
     {'author': 'SEO Boardroom',
      'channel': 'SEO Boardroom',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=CVctN2LgvDQ&t=56s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "SEO was asking me um do you know what SEO is and I said nope but I'm going to "
              'Google it and so this was uh the beginning of my journey um I was starting to '
              'work there and building the the market in the German speaking uh countries.',
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': "SEO was asking me um do you know what SEO is and I said nope but I'm going to "
             'Google it and so this was uh the beginning of my journey um I was starting to '
             'work there and building the the market in the German speaking uh countries.',
      'title': 'Google is not coming to save you SEO in 2026 - canonical abuse, Parasite, '
               'Negative SEO and more (SEO Boardroom)',
      'url': 'https://www.youtube.com/watch?v=CVctN2LgvDQ&t=56s',
      'video_id': 'CVctN2LgvDQ'},
     {'author': 'Julian Goldie SEO',
      'channel': 'Julian Goldie SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=LY7IFzytdLo&t=83s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re the subject matter expert in your niche and in your field and you want to "
              "get those links coming to your site, so I'll leave the journalism portion to "
              'another channel and we can just talk about the source portion. So why is HARO '
              'useful for link building?',
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': "'re the subject matter expert in your niche and in your field and you want to "
             "get those links coming to your site, so I'll leave the journalism portion to "
             'another channel and we can just talk about the source portion. So why is HARO '
             'useful for link building?',
      'title': 'Link Building 2022: How To Use HARO For Backlinks || Link Building Strategy || '
               'Julian Goldie SEO (Julian Goldie SEO)',
      'url': 'https://www.youtube.com/watch?v=LY7IFzytdLo&t=83s',
      'video_id': 'LY7IFzytdLo'},
     {'author': 'Kate Smoothy | SEO Specialist',
      'channel': 'Kate Smoothy | SEO Specialist',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:25](https://www.youtube.com/watch?v=zS5xebRUE5Y&t=745s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm based in the UK, as I've just been talking about, and I have tried to claim "
              "several of our clients' businesses and our own on ChatGPT Business Hub and have "
              "not yet been able to. I've been put on a waitlist.",
      'timestamp': 745,
      'timestamp_label': '[00:12:25]',
      'timestamp_seconds': 745,
      'tip': "I'm based in the UK, as I've just been talking about, and I have tried to claim "
             "several of our clients' businesses and our own on ChatGPT Business Hub and have "
             "not yet been able to. I've been put on a waitlist.",
      'title': 'GOOGLE UPDATE Is Here (Nov 2026 Core Update) & AI Is Changing SERPs (Kate '
               'Smoothy | SEO Specialist)',
      'url': 'https://www.youtube.com/watch?v=zS5xebRUE5Y&t=745s',
      'video_id': 'zS5xebRUE5Y'},
     {'author': 'Koray Tuğberk GÜBÜR',
      'channel': 'Koray Tuğberk GÜBÜR',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:17](https://www.youtube.com/watch?v=mD51uM8v_bw&t=857s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'RAM there is no RAM on the market anymore they keep buying every CPU GPU and '
              'every RAM and because of that there is not even enough hardware anymore to '
              'actually check your website currently. So because of this, you should you have '
              'to make everything right in the first place.',
      'timestamp': 857,
      'timestamp_label': '[00:14:17]',
      'timestamp_seconds': 857,
      'tip': 'RAM there is no RAM on the market anymore they keep buying every CPU GPU and '
             'every RAM and because of that there is not even enough hardware anymore to '
             'actually check your website currently. So because of this, you should you have '
             'to make everything right in the first place.',
      'title': 'Topical Authority and Semantic SEO for Local Rankings (Law and Beyond) (Koray '
               'Tuğberk GÜBÜR)',
      'url': 'https://www.youtube.com/watch?v=mD51uM8v_bw&t=857s',
      'video_id': 'mD51uM8v_bw'},
     {'author': 'Alex COLLINSEO',
      'channel': 'Alex COLLINSEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=Q263PTEZCQg&t=20s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'How to actually add them the same way I do it with my clients, no secrets held. '
              'And finally, some free tools to audit your current internal linking situation '
              'in your website. There are three types of internal linking.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'How to actually add them the same way I do it with my clients, no secrets held. '
             'And finally, some free tools to audit your current internal linking situation in '
             'your website. There are three types of internal linking.',
      'title': 'How To Do Internal Linking For SEO & Google/AI Rankings (Alex COLLINSEO)',
      'url': 'https://www.youtube.com/watch?v=Q263PTEZCQg&t=20s',
      'video_id': 'Q263PTEZCQg'},
     {'author': 'Fery Kaszoni',
      'channel': 'Fery Kaszoni',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=PUlSnyUHWbU&t=89s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Effective especially when there is a breaking news or extraordinary event that '
              'is happening around the world that you can use jack for your client I hope this '
              'video is inspirational and I hope you start some google trends based link '
              'building campaigns soon.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': 'Effective especially when there is a breaking news or extraordinary event that '
             'is happening around the world that you can use jack for your client I hope this '
             'video is inspirational and I hope you start some google trends based link '
             'building campaigns soon.',
      'title': '50 High-DR Links in 2 Hours - Digital PR Link Building Case Study (Fery '
               'Kaszoni)',
      'url': 'https://www.youtube.com/watch?v=PUlSnyUHWbU&t=89s',
      'video_id': 'PUlSnyUHWbU'},
     {'author': 'BoostRoas',
      'channel': 'BoostRoas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:42:01](https://www.youtube.com/watch?v=kuSNDOAsr50&t=2521s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Follow in order to find for instance in this case application think content I '
              'would encourage you to use this solution that is already in the market.',
      'timestamp': 2521,
      'timestamp_label': '[00:42:01]',
      'timestamp_seconds': 2521,
      'tip': 'Follow in order to find for instance in this case application think content I '
             'would encourage you to use this solution that is already in the market.',
      'title': 'Python SEO: How to Improve Crawling and Indexing - Weekly SEO with Daniel '
               'Heredia (BoostRoas)',
      'url': 'https://www.youtube.com/watch?v=kuSNDOAsr50&t=2521s',
      'video_id': 'kuSNDOAsr50'},
     {'author': 'Frey Chu',
      'channel': 'Frey Chu',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:35](https://www.youtube.com/watch?v=NoUJBS6-yNQ&t=155s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Once you kind of go into the niche itself and the community and you look on '
              'Reddit you look on Tik Tok you just kind of start to do some social listening '
              'on.',
      'timestamp': 155,
      'timestamp_label': '[00:02:35]',
      'timestamp_seconds': 155,
      'tip': 'Once you kind of go into the niche itself and the community and you look on '
             'Reddit you look on Tik Tok you just kind of start to do some social listening '
             'on.',
      'title': 'Can You Really Make $200K+ With A Website Directory? My Thoughts + Answering '
               'Questions (Frey Chu)',
      'url': 'https://www.youtube.com/watch?v=NoUJBS6-yNQ&t=155s',
      'video_id': 'NoUJBS6-yNQ'},
     {'author': 'Travis Wilkie',
      'channel': 'Travis Wilkie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:15](https://www.youtube.com/watch?v=D7f-Pid5IhM&t=195s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Are some keywords we can go after here that will be on the lower range of the '
              "cosper click but maybe that's a little too low maybe we just want anything "
              "under $25 now we've got Service Plumbing.",
      'timestamp': 195,
      'timestamp_label': '[00:03:15]',
      'timestamp_seconds': 195,
      'tip': 'Are some keywords we can go after here that will be on the lower range of the '
             "cosper click but maybe that's a little too low maybe we just want anything under "
             "$25 now we've got Service Plumbing.",
      'title': 'Semrush For Finding Low CPC Keywords (Travis Wilkie)',
      'url': 'https://www.youtube.com/watch?v=D7f-Pid5IhM&t=195s',
      'video_id': 'D7f-Pid5IhM'},
     {'author': 'Contentbase',
      'channel': 'Contentbase',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=ryLlXyneZ0o&t=103s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Value what other areas are they using this strategy I see they also have an '
              'aable Universe section this targets broader categories like education.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': 'Value what other areas are they using this strategy I see they also have an '
             'aable Universe section this targets broader categories like education.',
      'title': 'Programmatic SEO Case Study - Airtable (Contentbase)',
      'url': 'https://www.youtube.com/watch?v=ryLlXyneZ0o&t=103s',
      'video_id': 'ryLlXyneZ0o'}],
 2: [{'author': 'Ahrefs',
      'channel': 'Ahrefs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:55](https://www.youtube.com/watch?v=C5ddo63kHHI&t=235s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Buying backlinks is exactly as it sounds. You pay webmasters or authors a fee '
              "and in return, they'll link back to a page on your site. Now, this is against "
              "Google's Webmaster Guidelines and can potentially result in a penalty.",
      'timestamp': 235,
      'timestamp_label': '[00:03:55]',
      'timestamp_seconds': 235,
      'tip': 'Buying backlinks is exactly as it sounds. You pay webmasters or authors a fee '
             "and in return, they'll link back to a page on your site. Now, this is against "
             "Google's Webmaster Guidelines and can potentially result in a penalty.",
      'title': 'Link Building for Beginners: Complete Guide to Get Backlinks (Ahrefs)',
      'url': 'https://www.youtube.com/watch?v=C5ddo63kHHI&t=235s',
      'video_id': 'C5ddo63kHHI'},
     {'author': 'David Kowalski',
      'channel': 'David Kowalski',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:39](https://www.youtube.com/watch?v=OzPRqoG7brI&t=579s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Every other way of making money from a website scales differently. And once you '
              'see that, ads stop being your business and start being the floor underneath it. '
              'Affiliate is the obvious next one. You get paid per decision instead of per '
              'view.',
      'timestamp': 579,
      'timestamp_label': '[00:09:39]',
      'timestamp_seconds': 579,
      'tip': 'Every other way of making money from a website scales differently. And once you '
             'see that, ads stop being your business and start being the floor underneath it. '
             'Affiliate is the obvious next one. You get paid per decision instead of per '
             'view.',
      'title': 'AdSense, Mediavine, Monumetric, Raptive.. Which Is BEST? (David Kowalski)',
      'url': 'https://www.youtube.com/watch?v=OzPRqoG7brI&t=579s',
      'video_id': 'OzPRqoG7brI'},
     {'author': 'My First Website',
      'channel': 'My First Website',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:58](https://www.youtube.com/watch?v=Z2ya7VWFvh4&t=418s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If your site is brand new, three to six months. If it's an aged site, four to "
              "eight weeks. And if it's an established site, two to four weeks. Low "
              'competition keywords rank faster because fewer backlinks needed, less authority '
              'required, and less content depth needed.',
      'timestamp': 418,
      'timestamp_label': '[00:06:58]',
      'timestamp_seconds': 418,
      'tip': "If your site is brand new, three to six months. If it's an aged site, four to "
             "eight weeks. And if it's an established site, two to four weeks. Low competition "
             'keywords rank faster because fewer backlinks needed, less authority required, '
             'and less content depth needed.',
      'title': 'Semrush Tips: Find Low Competition Keywords That Still Get Traffic (My First '
               'Website)',
      'url': 'https://www.youtube.com/watch?v=Z2ya7VWFvh4&t=418s',
      'video_id': 'Z2ya7VWFvh4'},
     {'author': 'Koray Tuğberk GÜBÜR',
      'channel': 'Koray Tuğberk GÜBÜR',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=bWjlnI4gXxo&t=77s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Every attribute in this area sometimes the mobile app customer support and '
              'security they can go in into the same page payment methods as well yeah as.',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': 'Every attribute in this area sometimes the mobile app customer support and '
             'security they can go in into the same page payment methods as well yeah as.',
      'title': 'Topical Authority and Topical Maps in 5 Minutes - Koray Tugberk GUBUR (Koray '
               'Tuğberk GÜBÜR)',
      'url': 'https://www.youtube.com/watch?v=bWjlnI4gXxo&t=77s',
      'video_id': 'bWjlnI4gXxo'},
     {'author': 'Jaume Ros',
      'channel': 'Jaume Ros',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:11](https://www.youtube.com/watch?v=Ju4Bsp8-o7I&t=191s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And here's a perfect example. They conducted a study and predicted how avid "
              "gamers could look in the next 20 years if they didn't change their lifestyle "
              'habits. 71 backlinks, 46 referring domains, and pretty solid authority score '
              'coming in. Also got picked up by some media.',
      'timestamp': 191,
      'timestamp_label': '[00:03:11]',
      'timestamp_seconds': 191,
      'tip': "And here's a perfect example. They conducted a study and predicted how avid "
             "gamers could look in the next 20 years if they didn't change their lifestyle "
             'habits. 71 backlinks, 46 referring domains, and pretty solid authority score '
             'coming in. Also got picked up by some media.',
      'title': 'What is Digital PR? (The FUTURE of Link Building?) (Jaume Ros)',
      'url': 'https://www.youtube.com/watch?v=Ju4Bsp8-o7I&t=191s',
      'video_id': 'Ju4Bsp8-o7I'},
     {'author': 'Collaborator',
      'channel': 'Collaborator',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:32](https://www.youtube.com/watch?v=CXPwDszPK7g&t=512s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In case you want the publisher to publish the website content for you, of '
              'course you should pay the publisher and the fees are openly available to you '
              'once you are exploring the platform.',
      'timestamp': 512,
      'timestamp_label': '[00:08:32]',
      'timestamp_seconds': 512,
      'tip': 'In case you want the publisher to publish the website content for you, of course '
             'you should pay the publisher and the fees are openly available to you once you '
             'are exploring the platform.',
      'title': 'How to Find High-Quality Backlinks for SEO | Artur Perrella Glukhovskyy '
               '(Collaborator)',
      'url': 'https://www.youtube.com/watch?v=CXPwDszPK7g&t=512s',
      'video_id': 'CXPwDszPK7g'},
     {'author': 'Max Kuch',
      'channel': 'Max Kuch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=kkVGjM2Fpok&t=98s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'End of June and mid of June I received the payment for April so like the April '
              'display ads would have been payable 1st of May but then net 45 pushes back to.',
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': 'End of June and mid of June I received the payment for April so like the April '
             'display ads would have been payable 1st of May but then net 45 pushes back to.',
      'title': 'RAPTIVE REVIEW: Is This THE Best Ad Network? (2024) (Max Kuch)',
      'url': 'https://www.youtube.com/watch?v=kkVGjM2Fpok&t=98s',
      'video_id': 'kkVGjM2Fpok'},
     {'author': 'BKA Content',
      'channel': 'BKA Content',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:38](https://www.youtube.com/watch?v=n68rh1s-ZdY&t=458s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'An RV park that person who has the RV is looking for certain things when they '
              'make their decision process so making sure that you have subpages that cover '
              'all of those parts of the customer.',
      'timestamp': 458,
      'timestamp_label': '[00:07:38]',
      'timestamp_seconds': 458,
      'tip': 'An RV park that person who has the RV is looking for certain things when they '
             'make their decision process so making sure that you have subpages that cover all '
             'of those parts of the customer.',
      'title': 'Is Your Website Structure Hurting Your SEO? Do this! (BKA Content)',
      'url': 'https://www.youtube.com/watch?v=n68rh1s-ZdY&t=458s',
      'video_id': 'n68rh1s-ZdY'},
     {'author': 'James Dooley',
      'channel': 'James Dooley',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:37](https://www.youtube.com/watch?v=4Ln6U3hYfwQ&t=697s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We don't own any of these sites. We just pay them or we just convince them to "
              'publish these type of articles on their sources in the way that actually can '
              'support my network as well. So prime example, like SEO Mastery Summit.',
      'timestamp': 697,
      'timestamp_label': '[00:11:37]',
      'timestamp_seconds': 697,
      'tip': "We don't own any of these sites. We just pay them or we just convince them to "
             'publish these type of articles on their sources in the way that actually can '
             'support my network as well. So prime example, like SEO Mastery Summit.',
      'title': 'External Topical Maps | 3rd Party Semantic Content Networks (James Dooley ft '
               'Koray Tuğberk Gübür) (James Dooley)',
      'url': 'https://www.youtube.com/watch?v=4Ln6U3hYfwQ&t=697s',
      'video_id': '4Ln6U3hYfwQ'},
     {'author': 'CrowdReply | Rank in AI Answers',
      'channel': 'CrowdReply | Rank in AI Answers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:25](https://www.youtube.com/watch?v=v2nAe-a8JrQ&t=445s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Optimize for backlinks, basically the same thing. And versus pages, you don't "
              'have to get into them, you can create them yourself.',
      'timestamp': 445,
      'timestamp_label': '[00:07:25]',
      'timestamp_seconds': 445,
      'tip': "Optimize for backlinks, basically the same thing. And versus pages, you don't "
             'have to get into them, you can create them yourself.',
      'title': 'Generative Engine Optimization: The Best AI Tool for GEO! 2026 (CrowdReply | '
               'Rank in AI Answers)',
      'url': 'https://www.youtube.com/watch?v=v2nAe-a8JrQ&t=445s',
      'video_id': 'v2nAe-a8JrQ'},
     {'author': 'Chris Palmer SEO',
      'channel': 'Chris Palmer SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=qLr_HlF7dKw&t=35s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'How we know that internal backlinks are important for SEO. Let me show this to '
              'you here. So, this is Lighthouse Man. One of the initial things that we did was '
              'take care of internal link build, right?',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'How we know that internal backlinks are important for SEO. Let me show this to '
             'you here. So, this is Lighthouse Man. One of the initial things that we did was '
             'take care of internal link build, right?',
      'title': 'On-Page SEO Internal Linking Tips (Chris Palmer SEO)',
      'url': 'https://www.youtube.com/watch?v=qLr_HlF7dKw&t=35s',
      'video_id': 'qLr_HlF7dKw'},
     {'author': 'Vitaliy Gershfeld',
      'channel': 'Vitaliy Gershfeld',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:34](https://www.youtube.com/watch?v=Gb-4YRsXxSk&t=154s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And when they scroll through your content longer, more ads load up, and your '
              "RPM rates will go up because they'll be staying on your website longer.",
      'timestamp': 154,
      'timestamp_label': '[00:02:34]',
      'timestamp_seconds': 154,
      'tip': 'And when they scroll through your content longer, more ads load up, and your RPM '
             "rates will go up because they'll be staying on your website longer.",
      'title': 'How To Increase Your Blog RPM (Mediavine Tips That ACTUALLY Work) (Vitaliy '
               'Gershfeld)',
      'url': 'https://www.youtube.com/watch?v=Gb-4YRsXxSk&t=154s',
      'video_id': 'Gb-4YRsXxSk'},
     {'author': 'Web Rice Studio',
      'channel': 'Web Rice Studio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=FU2y92rBoWo&t=15s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'की होने वाली है। तो भाई वीडियो को एंड तक जरूर देखना। छोटा सा इंट्रो देता हूं। '
              'मेरा नाम असीम है। मैं एक वेबसाइट डिजाइनर हूं। साथ ही साथ एसयू एक्सपर्ट हूं। '
              'चलिए.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'की होने वाली है। तो भाई वीडियो को एंड तक जरूर देखना। छोटा सा इंट्रो देता हूं। '
             'मेरा नाम असीम है। मैं एक वेबसाइट डिजाइनर हूं। साथ ही साथ एसयू एक्सपर्ट हूं। '
             'चलिए.',
      'title': '1.5 Million Traffic Without Backlinks? 😳 | Calculator Site Case Study (Web '
               'Rice Studio)',
      'url': 'https://www.youtube.com/watch?v=FU2y92rBoWo&t=15s',
      'video_id': 'FU2y92rBoWo'},
     {'author': 'OG Shubh',
      'channel': 'OG Shubh',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=dRCq6yZqqKw&t=15s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'वीडियो पे आए इस वीडियो में मैं तुमको बताऊंगा कि तुम कैसे और कहां से एकदम '
              'चीपेस्ट प्राइस में HF या सेम रस का ग्रुप बाय कर सकते हो। लाइक और भी तुमको जो '
              'भी.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'वीडियो पे आए इस वीडियो में मैं तुमको बताऊंगा कि तुम कैसे और कहां से एकदम चीपेस्ट '
             'प्राइस में HF या सेम रस का ग्रुप बाय कर सकते हो। लाइक और भी तुमको जो भी.',
      'title': 'Ahrefs & Semrush Group Buy SEO Tools (2026) | Instant Access | 100% Private & '
               'Secure (OG Shubh)',
      'url': 'https://www.youtube.com/watch?v=dRCq6yZqqKw&t=15s',
      'video_id': 'dRCq6yZqqKw'},
     {'author': 'Umar Tazkeer',
      'channel': 'Umar Tazkeer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:29](https://www.youtube.com/watch?v=uWNsW77fwSs&t=29s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'ट्रैफिक का ही ग्रोथ रेट है और यह परसेंटेज में है और यहां पर आपका प्रोजेक्टेड '
              'ट्रैफिक है तो प्रॉब्लम यह है कि अगर हमारे पास मंथ बाय मंथ कुछ ट्रैफिक.',
      'timestamp': 29,
      'timestamp_label': '[00:00:29]',
      'timestamp_seconds': 29,
      'tip': 'ट्रैफिक का ही ग्रोथ रेट है और यह परसेंटेज में है और यहां पर आपका प्रोजेक्टेड '
             'ट्रैफिक है तो प्रॉब्लम यह है कि अगर हमारे पास मंथ बाय मंथ कुछ ट्रैफिक.',
      'title': 'Small Calculator to do the SEO Traffic Forecasting - Umar Tazkeer (Umar '
               'Tazkeer)',
      'url': 'https://www.youtube.com/watch?v=uWNsW77fwSs&t=29s',
      'video_id': 'uWNsW77fwSs'}],
 3: [{'author': 'Consumer Reviews',
      'channel': 'Consumer Reviews',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:34](https://www.youtube.com/watch?v=Q0qBq0V4xC4&t=274s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, I started with RFS here to run a backlink audit and figure out where '
              'competitors were getting their traffic from. Solid data, simple filters, and I '
              'was able to spot link building opportunities. But when it was time to plan a '
              'full content strategy, I hit a wall.',
      'timestamp': 274,
      'timestamp_label': '[00:04:34]',
      'timestamp_seconds': 274,
      'tip': 'So, I started with RFS here to run a backlink audit and figure out where '
             'competitors were getting their traffic from. Solid data, simple filters, and I '
             'was able to spot link building opportunities. But when it was time to plan a '
             'full content strategy, I hit a wall.',
      'title': "Semrush vs Ahrefs: I Used Both – Here's What You Need to Know (Consumer "
               'Reviews)',
      'url': 'https://www.youtube.com/watch?v=Q0qBq0V4xC4&t=274s',
      'video_id': 'Q0qBq0V4xC4'},
     {'author': 'LinkBuilding HQ',
      'channel': 'LinkBuilding HQ',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:13](https://www.youtube.com/watch?v=3vuTHqRjxvQ&t=253s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Digital PR is all about building brand visibility and its success is measured '
              'in media mentions, brand sentiment, website traffic, social media engagement, '
              'and ultimately business leads and sales. In digital PR, backlinks are a '
              'valuable byproduct, but not the sole objective.',
      'timestamp': 253,
      'timestamp_label': '[00:04:13]',
      'timestamp_seconds': 253,
      'tip': 'Digital PR is all about building brand visibility and its success is measured in '
             'media mentions, brand sentiment, website traffic, social media engagement, and '
             'ultimately business leads and sales. In digital PR, backlinks are a valuable '
             'byproduct, but not the sole objective.',
      'title': 'Digital PR: A New Fad or the Future of SEO? (LinkBuilding HQ)',
      'url': 'https://www.youtube.com/watch?v=3vuTHqRjxvQ&t=253s',
      'video_id': '3vuTHqRjxvQ'},
     {'author': 'Ahrefs',
      'channel': 'Ahrefs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:44](https://www.youtube.com/watch?v=kpz9-QZRYn8&t=284s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Ahrefs' SEO toolbar and look at the number of referring domains to the page or "
              "use the URL rating metric which is an Ahrefs' metric that measures page-level "
              "authority. The second place to find internal link opportunities is in Ahrefs' "
              'Site Audit.',
      'timestamp': 284,
      'timestamp_label': '[00:04:44]',
      'timestamp_seconds': 284,
      'tip': "Ahrefs' SEO toolbar and look at the number of referring domains to the page or "
             "use the URL rating metric which is an Ahrefs' metric that measures page-level "
             "authority. The second place to find internal link opportunities is in Ahrefs' "
             'Site Audit.',
      'title': 'How to use Internal Links to Boost Google Rankings (Ahrefs)',
      'url': 'https://www.youtube.com/watch?v=kpz9-QZRYn8&t=284s',
      'video_id': 'kpz9-QZRYn8'},
     {'author': 'Visibility on Purpose',
      'channel': 'Visibility on Purpose',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:47](https://www.youtube.com/watch?v=B1uNyKgJlXc&t=647s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mukra or Sision, it is a fraction of the cost. So, if that is something within '
              "your budget, I think it's so recommended to do the paid plan. There are "
              'features that are just going to be really helpful when you have the paid plan '
              'versus free.',
      'timestamp': 647,
      'timestamp_label': '[00:10:47]',
      'timestamp_seconds': 647,
      'tip': 'Mukra or Sision, it is a fraction of the cost. So, if that is something within '
             "your budget, I think it's so recommended to do the paid plan. There are features "
             'that are just going to be really helpful when you have the paid plan versus '
             'free.',
      'title': 'HARO vs Qwoted — Best Platform for PR Link Building & Backlinks (Full 2025 '
               'Tutorial) (Visibility on Purpose)',
      'url': 'https://www.youtube.com/watch?v=B1uNyKgJlXc&t=647s',
      'video_id': 'B1uNyKgJlXc'},
     {'author': 'Collaborator',
      'channel': 'Collaborator',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:50](https://www.youtube.com/watch?v=7sg8dljI1yQ&t=710s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Because link building isn't about getting us more links as possible, it's about "
              'building the right backlink profile for your website.',
      'timestamp': 710,
      'timestamp_label': '[00:11:50]',
      'timestamp_seconds': 710,
      'tip': "Because link building isn't about getting us more links as possible, it's about "
             'building the right backlink profile for your website.',
      'title': 'How to Choose Quality Backlinks for SEO: DR, Traffic, Relevance & Price '
               '(Collaborator)',
      'url': 'https://www.youtube.com/watch?v=7sg8dljI1yQ&t=710s',
      'video_id': '7sg8dljI1yQ'},
     {'author': 'Topical Authority SEO | Floyi',
      'channel': 'Topical Authority SEO | Floyi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:04](https://www.youtube.com/watch?v=0XswjN-Lops&t=244s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Continue draft and edit article open the work you've already started. So silo "
              "analysis updates every time your topical authority scores recalculate or you've "
              'refreshed the SERPs. And last updated shows when the last time that happened.',
      'timestamp': 244,
      'timestamp_label': '[00:04:04]',
      'timestamp_seconds': 244,
      'tip': "Continue draft and edit article open the work you've already started. So silo "
             "analysis updates every time your topical authority scores recalculate or you've "
             'refreshed the SERPs. And last updated shows when the last time that happened.',
      'title': '14 How to Run a Competitor Content Gap Analysis by Silo (Floyi Tutorial) '
               '(Topical Authority SEO | Floyi)',
      'url': 'https://www.youtube.com/watch?v=0XswjN-Lops&t=244s',
      'video_id': '0XswjN-Lops'},
     {'author': 'Misha Manko',
      'channel': 'Misha Manko',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:59](https://www.youtube.com/watch?v=nBrto2B9RyE&t=659s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, basically with a very low crawl budget, with a low authority, your pages, '
              'your URLs will never be fully indexed. One of the indication that you have low '
              'crawl budget is if you have inside Google Search Console a lot of discovered, '
              'but not indexed status on your URLs.',
      'timestamp': 659,
      'timestamp_label': '[00:10:59]',
      'timestamp_seconds': 659,
      'tip': 'So, basically with a very low crawl budget, with a low authority, your pages, '
             'your URLs will never be fully indexed. One of the indication that you have low '
             'crawl budget is if you have inside Google Search Console a lot of discovered, '
             'but not indexed status on your URLs.',
      'title': 'Crawl Budget, Explained: What Eats It and How to Get More (Misha Manko)',
      'url': 'https://www.youtube.com/watch?v=nBrto2B9RyE&t=659s',
      'video_id': 'nBrto2B9RyE'},
     {'author': 'Edward Sturm',
      'channel': 'Edward Sturm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:50](https://www.youtube.com/watch?v=clcy9RbjrXQ&t=1250s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Especially if you're building free parasites and you still haven't made a "
              "profit, you're definitely doing something wrong. I hope you enjoyed that little "
              'presentation. My recommendation is always you test free first. You can always '
              'start Paris SEO for free.',
      'timestamp': 1250,
      'timestamp_label': '[00:20:50]',
      'timestamp_seconds': 1250,
      'tip': "Especially if you're building free parasites and you still haven't made a "
             "profit, you're definitely doing something wrong. I hope you enjoyed that little "
             'presentation. My recommendation is always you test free first. You can always '
             'start Paris SEO for free.',
      'title': 'Parasite SEO: How Charles Floate Ranks Pages on Google.com Itself (Edward '
               'Sturm)',
      'url': 'https://www.youtube.com/watch?v=clcy9RbjrXQ&t=1250s',
      'video_id': 'clcy9RbjrXQ'},
     {'author': 'Ideal Directories',
      'channel': 'Ideal Directories',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:42](https://www.youtube.com/watch?v=nrI7go1wRl0&t=162s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Free listings to local businesses to establish a relationship and build trust '
              "and then three follow up and offer your other services and that's it who would "
              'have thought that giving away listings on a business directory website could be '
              'so profitable.',
      'timestamp': 162,
      'timestamp_label': '[00:02:42]',
      'timestamp_seconds': 162,
      'tip': 'Free listings to local businesses to establish a relationship and build trust '
             "and then three follow up and offer your other services and that's it who would "
             'have thought that giving away listings on a business directory website could be '
             'so profitable.',
      'title': 'How to Profit from Giving Away Listings on Your Business Directory Website | '
               'Ideal Directories (Ideal Directories)',
      'url': 'https://www.youtube.com/watch?v=nrI7go1wRl0&t=162s',
      'video_id': 'nrI7go1wRl0'},
     {'author': 'SaaS SEO Engine',
      'channel': 'SaaS SEO Engine',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:02](https://www.youtube.com/watch?v=kBXz_ArlMVk&t=1022s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Valuable than you know from an opportunity cost pers perspective great '
              'investment of time and and resources here all right and the last example I.',
      'timestamp': 1022,
      'timestamp_label': '[00:17:02]',
      'timestamp_seconds': 1022,
      'tip': 'Valuable than you know from an opportunity cost pers perspective great '
             'investment of time and and resources here all right and the last example I.',
      'title': 'Programmatic SEO: 9 Real SaaS Success Stories (SaaS SEO Engine)',
      'url': 'https://www.youtube.com/watch?v=kBXz_ArlMVk&t=1022s',
      'video_id': 'kBXz_ArlMVk'},
     {'author': 'Empire Flippers',
      'channel': 'Empire Flippers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:47](https://www.youtube.com/watch?v=i598iDr-y8E&t=407s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Thousand dollars per month in net profit during the pandemic then click on the '
              "video here so that's all for now thanks for watching see you next time.",
      'timestamp': 407,
      'timestamp_label': '[00:06:47]',
      'timestamp_seconds': 407,
      'tip': 'Thousand dollars per month in net profit during the pandemic then click on the '
             "video here so that's all for now thanks for watching see you next time.",
      'title': 'Breaking News: Selling Foreign Content Sites (Empire Flippers)',
      'url': 'https://www.youtube.com/watch?v=i598iDr-y8E&t=407s',
      'video_id': 'i598iDr-y8E'},
     {'author': 'Koray Tuğberk GÜBÜR',
      'channel': 'Koray Tuğberk GÜBÜR',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:32](https://www.youtube.com/watch?v=X_ou1eO28gE&t=1172s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Name together with your products or together with your industry it will '
              'directly make Google think that you are a brand you are a real world business.',
      'timestamp': 1172,
      'timestamp_label': '[00:19:32]',
      'timestamp_seconds': 1172,
      'tip': 'Name together with your products or together with your industry it will directly '
             'make Google think that you are a brand you are a real world business.',
      'title': 'Exploring Holistic SEO (Semantic SEO, Topical Authority, Technical SEO) with '
               'Koray Tuğberk (Koray Tuğberk GÜBÜR)',
      'url': 'https://www.youtube.com/watch?v=X_ou1eO28gE&t=1172s',
      'video_id': 'X_ou1eO28gE'},
     {'author': 'Semrush Toolz',
      'channel': 'Semrush Toolz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:58](https://www.youtube.com/watch?v=Xo8oCdoM32I&t=298s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'यूज़ करके दिखा देता हूं। देख सकते हैं एचf जो है वो ओपन हो चुका है। यहां पे भी '
              'मैं कीवर्ड एक्सप्लोरर पे आता हूं। एंड कोई कीवर्ड जो है वह आपको सर्च करके दिखा '
              'देता हूं।.',
      'timestamp': 298,
      'timestamp_label': '[00:04:58]',
      'timestamp_seconds': 298,
      'tip': 'यूज़ करके दिखा देता हूं। देख सकते हैं एचf जो है वो ओपन हो चुका है। यहां पे भी मैं '
             'कीवर्ड एक्सप्लोरर पे आता हूं। एंड कोई कीवर्ड जो है वह आपको सर्च करके दिखा देता '
             'हूं।.',
      'title': 'Unlock Ahrefs & Semrush Premium | Budget-Friendly Method 🔥 SemrushToolz '
               '(Semrush Toolz)',
      'url': 'https://www.youtube.com/watch?v=Xo8oCdoM32I&t=298s',
      'video_id': 'Xo8oCdoM32I'},
     {'author': 'Learn From Top Rated Freelancer',
      'channel': 'Learn From Top Rated Freelancer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=zq2twCJ2wuA&t=78s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Googleুগল বোর্ড আপনার সাইটের যতগুলা ইউআরএল ক্রোল করতে চায় এবং ক্রোল করতে পারছে '
              'সেই সংখ্যাটাই মূলত ক্রোল বাজেট। বেসিক্যালি বুঝতে পারছেন?',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'Googleুগল বোর্ড আপনার সাইটের যতগুলা ইউআরএল ক্রোল করতে চায় এবং ক্রোল করতে পারছে '
             'সেই সংখ্যাটাই মূলত ক্রোল বাজেট। বেসিক্যালি বুঝতে পারছেন?',
      'title': 'Crawl Budget Optimization Explained (Technical SEO Masterclass) (Learn From '
               'Top Rated Freelancer)',
      'url': 'https://www.youtube.com/watch?v=zq2twCJ2wuA&t=78s',
      'video_id': 'zq2twCJ2wuA'},
     {'author': 'HeyRahat',
      'channel': 'HeyRahat',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:24](https://www.youtube.com/watch?v=2oU82BZ6KOU&t=204s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Method and most of our this we the hack is the shorten paragraph This is the '
              'main important part and then you need to adjust or increase the font size of '
              'your article of your website so you need to most important thing you need to '
              'make your website user.',
      'timestamp': 204,
      'timestamp_label': '[00:03:24]',
      'timestamp_seconds': 204,
      'tip': 'Method and most of our this we the hack is the shorten paragraph This is the '
             'main important part and then you need to adjust or increase the font size of '
             'your article of your website so you need to most important thing you need to '
             'make your website user.',
      'title': 'Mediavine Journey RPM Secrets: Advanced Strategies You NEED to Know (I Tested '
               '& My RPM 🚀) (HeyRahat)',
      'url': 'https://www.youtube.com/watch?v=2oU82BZ6KOU&t=204s',
      'video_id': '2oU82BZ6KOU'}],
 4: [{'author': 'Niche AI Tool',
      'channel': 'Niche AI Tool',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=r8amrelmKH0&t=35s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Both tools got a fair shake. The backlink index is the largest and most '
              'accurate in the industry. The keyword research gives you accurate volumes. The '
              "site audit surface is real, actionable fixes, and it's easier to use with a 7. "
              "5 out of 10 on ease versus Semrush's 7.",
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'Both tools got a fair shake. The backlink index is the largest and most accurate '
             'in the industry. The keyword research gives you accurate volumes. The site audit '
             "surface is real, actionable fixes, and it's easier to use with a 7. 5 out of 10 "
             "on ease versus Semrush's 7.",
      'title': 'Ahrefs vs Semrush 2026: I Tested Both for 30 Days — The Honest Winner #ahrefs '
               '#semrush #aitools (Niche AI Tool)',
      'url': 'https://www.youtube.com/watch?v=r8amrelmKH0&t=35s',
      'video_id': 'r8amrelmKH0'},
     {'author': 'Matt Diggity',
      'channel': 'Matt Diggity',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=4DgWUgtZGqQ&t=103s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The client runs a software supply chain management company. If you're building "
              'a complex piece of software with multiple tools and code languages, Their '
              'platform helps you project manage the whole thing. Their cheapest subscription '
              'starts at $4,000 a month.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': "The client runs a software supply chain management company. If you're building a "
             'complex piece of software with multiple tools and code languages, Their platform '
             'helps you project manage the whole thing. Their cheapest subscription starts at '
             '$4,000 a month.',
      'title': 'Programmatic SEO: Step-by-Step Case Study (Matt Diggity)',
      'url': 'https://www.youtube.com/watch?v=4DgWUgtZGqQ&t=103s',
      'video_id': '4DgWUgtZGqQ'},
     {'author': 'How To Mr',
      'channel': 'How To Mr',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=nIeVxkyipjw&t=80s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I also love their creator first approach. They genuinely care about your '
              'growth, offering business coaching, video monetization tools, and brand '
              'partnership opportunities beyond display ads.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': 'I also love their creator first approach. They genuinely care about your growth, '
             'offering business coaching, video monetization tools, and brand partnership '
             'opportunities beyond display ads.',
      'title': 'Raptive Review | Pros and Cons – Watch Before Using (How To Mr)',
      'url': 'https://www.youtube.com/watch?v=nIeVxkyipjw&t=80s',
      'video_id': 'nIeVxkyipjw'},
     {'author': 'The Grow and Convert Marketing Show',
      'channel': 'The Grow and Convert Marketing Show',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:46](https://www.youtube.com/watch?v=hEPMrse9c_g&t=1126s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'cause these are kind of the most important specific keywords for their "
              "business. And they didn't have as much content around just best structural "
              'design software. And BIM enabled structural design tools.',
      'timestamp': 1126,
      'timestamp_label': '[00:18:46]',
      'timestamp_seconds': 1126,
      'tip': "'cause these are kind of the most important specific keywords for their "
             "business. And they didn't have as much content around just best structural "
             'design software. And BIM enabled structural design tools.',
      'title': 'The Step-by-Step GEO Strategy to Rank in ChatGPT, Perplexity & AI Overviews '
               '(The Grow and Convert Marketing Show)',
      'url': 'https://www.youtube.com/watch?v=hEPMrse9c_g&t=1126s',
      'video_id': 'hEPMrse9c_g'},
     {'author': 'FatRank',
      'channel': 'FatRank',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:55](https://www.youtube.com/watch?v=9YOo5zDOsP8&t=475s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '\'re doing a backlink audit, instead of just shooting blind and going, "Oh, you '
              'need more links to this this page or to this the to the home page." It might be '
              "to certain category pages that's saying the server logs are not crawling this "
              'enough.',
      'timestamp': 475,
      'timestamp_label': '[00:07:55]',
      'timestamp_seconds': 475,
      'tip': '\'re doing a backlink audit, instead of just shooting blind and going, "Oh, you '
             'need more links to this this page or to this the to the home page." It might be '
             "to certain category pages that's saying the server logs are not crawling this "
             'enough.',
      'title': 'Server Log Analysis | Find and Fix SEO Errors (FatRank)',
      'url': 'https://www.youtube.com/watch?v=9YOo5zDOsP8&t=475s',
      'video_id': '9YOo5zDOsP8'},
     {'author': 'Gautam Prachi',
      'channel': 'Gautam Prachi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:33](https://www.youtube.com/watch?v=ctFRKtUiETo&t=513s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Which is stopping them to rank on Google there are so many of tools like sem '
              'Rush Uber suggest and um AI tools also which will help you audit your website '
              'now in.',
      'timestamp': 513,
      'timestamp_label': '[00:08:33]',
      'timestamp_seconds': 513,
      'tip': 'Which is stopping them to rank on Google there are so many of tools like sem '
             'Rush Uber suggest and um AI tools also which will help you audit your website '
             'now in.',
      'title': 'How to build SEO portfolio | How to make portfolio website free | How to pitch '
               'clients for SEO (Gautam Prachi)',
      'url': 'https://www.youtube.com/watch?v=ctFRKtUiETo&t=513s',
      'video_id': 'ctFRKtUiETo'},
     {'author': "Meghan's Media",
      'channel': "Meghan's Media",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:52](https://www.youtube.com/watch?v=NRcTFL8qghY&t=172s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Get approved they handle all of the setup um on your website so like with '
              'Google AdSense I know they have the auto ads um feature but I still had to '
              'tweak.',
      'timestamp': 172,
      'timestamp_label': '[00:02:52]',
      'timestamp_seconds': 172,
      'tip': 'Get approved they handle all of the setup um on your website so like with Google '
             'AdSense I know they have the auto ads um feature but I still had to tweak.',
      'title': 'Mediavine Q&A: Rate Calculations, Ad Placement Control & More - A Few of Your '
               "Questions Answered (Meghan's Media)",
      'url': 'https://www.youtube.com/watch?v=NRcTFL8qghY&t=172s',
      'video_id': 'NRcTFL8qghY'},
     {'author': "Kevin C. Roy & GreenBananaSEO's AEO / GEO Mastery",
      'channel': "Kevin C. Roy & GreenBananaSEO's AEO / GEO Mastery",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=1mZtqiAXmXs&t=56s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Gemini perplexity and more we're gonna cover things from content to "
              'architecture entity signals schema measurement and anything else that works so '
              'these videos are built as frameworks that you can copy.',
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': "Gemini perplexity and more we're gonna cover things from content to architecture "
             'entity signals schema measurement and anything else that works so these videos '
             'are built as frameworks that you can copy.',
      'title': 'Google’s 2026 Core Update: Why “Good Content” Is No Longer Enough (Kevin C. '
               "Roy & GreenBananaSEO's AEO / GEO Mastery)",
      'url': 'https://www.youtube.com/watch?v=1mZtqiAXmXs&t=56s',
      'video_id': '1mZtqiAXmXs'},
     {'author': 'Iron Goo',
      'channel': 'Iron Goo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:39](https://www.youtube.com/watch?v=Z5OwRBCX5ww&t=699s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t as helpful as it might seem. That study shows what AI tools cite, not what "
              'causes a citation, and it comes from a company that sells PR software. We dig '
              'into what AI answers count in the next episode.',
      'timestamp': 699,
      'timestamp_label': '[00:11:39]',
      'timestamp_seconds': 699,
      'tip': "'t as helpful as it might seem. That study shows what AI tools cite, not what "
             'causes a citation, and it comes from a company that sells PR software. We dig '
             'into what AI answers count in the next episode.',
      'title': 'Digital PR: earn relevant links with data only you have (Iron Goo)',
      'url': 'https://www.youtube.com/watch?v=Z5OwRBCX5ww&t=699s',
      'video_id': 'Z5OwRBCX5ww'},
     {'author': 'Julian Goldie SEO',
      'channel': 'Julian Goldie SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:30](https://www.youtube.com/watch?v=m8uR1-8CGkg&t=270s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sure that you can outsource this job you know I actually used a word calm this '
              'is a great website to outsource heron link-building to because right in how a.',
      'timestamp': 270,
      'timestamp_label': '[00:04:30]',
      'timestamp_seconds': 270,
      'tip': 'Sure that you can outsource this job you know I actually used a word calm this '
             'is a great website to outsource heron link-building to because right in how a.',
      'title': 'HARO Backlinks: Get Links In 2 Minutes (Or Less)! (Julian Goldie SEO)',
      'url': 'https://www.youtube.com/watch?v=m8uR1-8CGkg&t=270s',
      'video_id': 'm8uR1-8CGkg'},
     {'author': 'Entity Elevation',
      'channel': 'Entity Elevation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:13](https://www.youtube.com/watch?v=JMgl5UyTg7Q&t=193s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Doll companies and their CMOS and they they get access to a lot of tools but I '
              "haven't seen any comprehensive tool and even the like CMOS they would tell me "
              'Hey Stephen I like your method a lot so I knew I had something.',
      'timestamp': 193,
      'timestamp_label': '[00:03:13]',
      'timestamp_seconds': 193,
      'tip': 'Doll companies and their CMOS and they they get access to a lot of tools but I '
             "haven't seen any comprehensive tool and even the like CMOS they would tell me "
             'Hey Stephen I like your method a lot so I knew I had something.',
      'title': 'Internal Linking Framework - Steven Kang - Rank Elevation SEO Summit 2024 '
               '(Entity Elevation)',
      'url': 'https://www.youtube.com/watch?v=JMgl5UyTg7Q&t=193s',
      'video_id': 'JMgl5UyTg7Q'},
     {'author': 'Ideal Directories',
      'channel': 'Ideal Directories',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:33](https://www.youtube.com/watch?v=i6uh0q1WdLo&t=213s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Want to tell their friends and fellow business owners about how great your site '
              "is and what it does for them don't let the concern of selling listings on a "
              "site that's brand new stop you from getting started now.",
      'timestamp': 213,
      'timestamp_label': '[00:03:33]',
      'timestamp_seconds': 213,
      'tip': 'Want to tell their friends and fellow business owners about how great your site '
             "is and what it does for them don't let the concern of selling listings on a site "
             "that's brand new stop you from getting started now.",
      'title': 'How to Sell Listings on a Directory Website with Little or No Traffic (Ideal '
               'Directories)',
      'url': 'https://www.youtube.com/watch?v=i6uh0q1WdLo&t=213s',
      'video_id': 'i6uh0q1WdLo'},
     {'author': 'Koray Tuğberk GÜBÜR',
      'channel': 'Koray Tuğberk GÜBÜR',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:30:59](https://www.youtube.com/watch?v=qrDPul4eAYw&t=1859s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sectors for credits and insurance we had to actually create a kind of '
              "connection a kind of smoothing area between the topics and that's why money "
              'saving was.',
      'timestamp': 1859,
      'timestamp_label': '[00:30:59]',
      'timestamp_seconds': 1859,
      'tip': 'Sectors for credits and insurance we had to actually create a kind of connection '
             "a kind of smoothing area between the topics and that's why money saving was.",
      'title': 'Topical Authority: 15 Semantically Optimized Topical Maps for SEO (Koray '
               'Tuğberk GÜBÜR)',
      'url': 'https://www.youtube.com/watch?v=qrDPul4eAYw&t=1859s',
      'video_id': 'qrDPul4eAYw'},
     {'author': 'NSIM AI Integrated Digital Marketing Institute',
      'channel': 'NSIM AI Integrated Digital Marketing Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=UXHpsKivCGI&t=15s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'है वो समझना है। [घंटी की आवाज़] सी जब भी हम वेबसाइट के करते हैं उस पे नए पेजेस '
              'क्रिएट करते हैं, नए पोस्ट क्रिएट करते हैं तो सिर्फ वेबसाइट बनाना या सिर्फ.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'है वो समझना है। [घंटी की आवाज़] सी जब भी हम वेबसाइट के करते हैं उस पे नए पेजेस '
             'क्रिएट करते हैं, नए पोस्ट क्रिएट करते हैं तो सिर्फ वेबसाइट बनाना या सिर्फ.',
      'title': 'What is Crawl Budget in SEO? | How Google Crawls and Indexes Your Website '
               '(NSIM AI Integrated Digital Marketing Institute)',
      'url': 'https://www.youtube.com/watch?v=UXHpsKivCGI&t=15s',
      'video_id': 'UXHpsKivCGI'},
     {'author': 'Mayank Sahu SEO',
      'channel': 'Mayank Sahu SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=ThJgF8OZbDk&t=15s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'ये दो हफ्ते तक चलने वाला है। जब कोर अपडेट आता है या किसी भी तरीके का अपडेट आता '
              'है, लोग सबसे पहले क्या करना शुरू कर देते हैं? टाइटल में बदलाव करना शुरू कर.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'ये दो हफ्ते तक चलने वाला है। जब कोर अपडेट आता है या किसी भी तरीके का अपडेट आता '
             'है, लोग सबसे पहले क्या करना शुरू कर देते हैं? टाइटल में बदलाव करना शुरू कर.',
      'title': 'Google November Core Update 2026: How to Improve Rankings & Recover Traffic '
               '(Mayank Sahu SEO)',
      'url': 'https://www.youtube.com/watch?v=ThJgF8OZbDk&t=15s',
      'video_id': 'ThJgF8OZbDk'}],
 5: [{'author': 'Revenue Tactics',
      'channel': 'Revenue Tactics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:06](https://www.youtube.com/watch?v=7pZQrsYVmt4&t=606s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re buying it and you control that decision completely. Of course, paid traffic "
              'requires a testing budget and the early campaigns may not be immediately '
              'profitable in a worst-case scenario, but the nature of that risk is '
              'fundamentally different from SEO risk.',
      'timestamp': 606,
      'timestamp_label': '[00:10:06]',
      'timestamp_seconds': 606,
      'tip': "'re buying it and you control that decision completely. Of course, paid traffic "
             'requires a testing budget and the early campaigns may not be immediately '
             'profitable in a worst-case scenario, but the nature of that risk is '
             'fundamentally different from SEO risk.',
      'title': "Affiliate Blogs & SEO Are Dead In 2026 [Here's What's Working Instead] "
               '(Revenue Tactics)',
      'url': 'https://www.youtube.com/watch?v=7pZQrsYVmt4&t=606s',
      'video_id': '7pZQrsYVmt4'},
     {'author': 'MostDomain',
      'channel': 'MostDomain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:44](https://www.youtube.com/watch?v=hMnUuibx6ZU&t=224s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Those three are what you need to avoid. Remember, one backlink from a trusted '
              'site like Forbes or TechCrunch is worth way, way more than 10,000 spammy '
              'backlinks. So, if the backlink graph looks natural and stable, you are onto '
              'something.',
      'timestamp': 224,
      'timestamp_label': '[00:03:44]',
      'timestamp_seconds': 224,
      'tip': 'Those three are what you need to avoid. Remember, one backlink from a trusted '
             'site like Forbes or TechCrunch is worth way, way more than 10,000 spammy '
             'backlinks. So, if the backlink graph looks natural and stable, you are onto '
             'something.',
      'title': '7 Steps: How to Find Powerful Expired Domains for SEO in 2026 (MostDomain)',
      'url': 'https://www.youtube.com/watch?v=hMnUuibx6ZU&t=224s',
      'video_id': 'hMnUuibx6ZU'},
     {'author': 'Rank Math SEO',
      'channel': 'Rank Math SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:44](https://www.youtube.com/watch?v=2XsoKvArFjo&t=764s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you follow best practice number one we have mentioned earlier about site '
              "hierarchy, you shouldn't have a problem with this. The last mistake you should "
              'avoid about internal linking is not optimizing it for mobile devices.',
      'timestamp': 764,
      'timestamp_label': '[00:12:44]',
      'timestamp_seconds': 764,
      'tip': 'If you follow best practice number one we have mentioned earlier about site '
             "hierarchy, you shouldn't have a problem with this. The last mistake you should "
             'avoid about internal linking is not optimizing it for mobile devices.',
      'title': '6 Best Internal Linking Practices for Higher Rankings (Rank Math SEO)',
      'url': 'https://www.youtube.com/watch?v=2XsoKvArFjo&t=764s',
      'video_id': '2XsoKvArFjo'},
     {'author': 'Leonidas @ PPCBasic',
      'channel': 'Leonidas @ PPCBasic',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:44](https://www.youtube.com/watch?v=78JTZZ9dRQ8&t=284s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, the the problem that I encountered is that when trying to figure this '
              "stuff out, ultimately all of us here are affiliate marketers and we're all in "
              "the lead gen space. So, how do you make Google trust us if we're just a lead "
              'gen website?',
      'timestamp': 284,
      'timestamp_label': '[00:04:44]',
      'timestamp_seconds': 284,
      'tip': 'Now, the the problem that I encountered is that when trying to figure this stuff '
             "out, ultimately all of us here are affiliate marketers and we're all in the lead "
             "gen space. So, how do you make Google trust us if we're just a lead gen website?",
      'title': 'Programmatic SEO - Building Hyper-Targeted Landing Pages (Leonidas @ PPCBasic)',
      'url': 'https://www.youtube.com/watch?v=78JTZZ9dRQ8&t=284s',
      'video_id': '78JTZZ9dRQ8'},
     {'author': 'Brandon Aday',
      'channel': 'Brandon Aday',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=CWvcb0rGN0g&t=88s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Identify the true authority. Give every important page one clear job to do. '
              'Different fields have specific traps. Law firms struggle with duplicate city.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'Identify the true authority. Give every important page one clear job to do. '
             'Different fields have specific traps. Law firms struggle with duplicate city.',
      'title': 'AI SEO Site Architecture: Speed, Structure, and Internal Links | AI Visibility '
               'Academy (Brandon Aday)',
      'url': 'https://www.youtube.com/watch?v=CWvcb0rGN0g&t=88s',
      'video_id': 'CWvcb0rGN0g'},
     {'author': 'Grumpy SEO Guy',
      'channel': 'Grumpy SEO Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:16](https://www.youtube.com/watch?v=ez24lr3G_Mc&t=1756s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Period of time we don't want to take any chances okay we don't want to take any "
              'risks buying something that may or may not be over optimized so 10 for me.',
      'timestamp': 1756,
      'timestamp_label': '[00:29:16]',
      'timestamp_seconds': 1756,
      'tip': "Period of time we don't want to take any chances okay we don't want to take any "
             'risks buying something that may or may not be over optimized so 10 for me.',
      'title': 'How to Build Your Own Portfolio of Authoritative Websites to Rank Your '
               'Clients, Part 1:... (Grumpy SEO Guy)',
      'url': 'https://www.youtube.com/watch?v=ez24lr3G_Mc&t=1756s',
      'video_id': 'ez24lr3G_Mc'},
     {'author': 'Magic Click Partners',
      'channel': 'Magic Click Partners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:53](https://www.youtube.com/watch?v=gK31bqBOj_k&t=233s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But, you really need to fully understand the risks involved. Moderation on '
              'Reddit is quite tough. Subreddits often enforce their own specific rules, and '
              'users are very quick to spot anything that feels fake. That is why the biggest '
              'mistake is coming across as far too salesy.',
      'timestamp': 233,
      'timestamp_label': '[00:03:53]',
      'timestamp_seconds': 233,
      'tip': 'But, you really need to fully understand the risks involved. Moderation on '
             'Reddit is quite tough. Subreddits often enforce their own specific rules, and '
             'users are very quick to spot anything that feels fake. That is why the biggest '
             'mistake is coming across as far too salesy.',
      'title': 'Reddit Parasite SEO – How to Natively Rank #1 on Google (Magic Click Partners)',
      'url': 'https://www.youtube.com/watch?v=gK31bqBOj_k&t=233s',
      'video_id': 'gK31bqBOj_k'},
     {'author': 'Google Search Central',
      'channel': 'Google Search Central',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:34](https://www.youtube.com/watch?v=am4g0hXAA8Q&t=334s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Excluded section of the GSA report? Something along those lines? MARTIN SPLITT: '
              'Yeah, exactly. These things are really helpful. Sometimes you also see people '
              "are like, oh, yeah. My crawl budget is really low. And then we're like, yeah, "
              'but is that a problem?',
      'timestamp': 334,
      'timestamp_label': '[00:05:34]',
      'timestamp_seconds': 334,
      'tip': 'Excluded section of the GSA report? Something along those lines? MARTIN SPLITT: '
             'Yeah, exactly. These things are really helpful. Sometimes you also see people '
             "are like, oh, yeah. My crawl budget is really low. And then we're like, yeah, "
             'but is that a problem?',
      'title': 'Crawl Budget: SEO Mythbusting (Google Search Central)',
      'url': 'https://www.youtube.com/watch?v=am4g0hXAA8Q&t=334s',
      'video_id': 'am4g0hXAA8Q'},
     {'author': 'UltraSEOSolutions',
      'channel': 'UltraSEOSolutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=MLdjFE-yxMk&t=59s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And as you can imagine, this has kicked off a huge debate. There are two very '
              'clear sides here. On one side, you have people saying search is junk. On the '
              'other, publishers say they need this to survive. And make no mistake, this '
              "isn't just a theoretical debate.",
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': 'And as you can imagine, this has kicked off a huge debate. There are two very '
             'clear sides here. On one side, you have people saying search is junk. On the '
             "other, publishers say they need this to survive. And make no mistake, this isn't "
             'just a theoretical debate.',
      'title': "Google's CRACKDOWN on Parasite SEO: Why the EU is Probing Site Reputation "
               'Abuse (UltraSEOSolutions)',
      'url': 'https://www.youtube.com/watch?v=MLdjFE-yxMk&t=59s',
      'video_id': 'MLdjFE-yxMk'},
     {'author': 'Jaryd Krause - Buying Online Businesses',
      'channel': 'Jaryd Krause - Buying Online Businesses',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=O0q1EG7DNIc&t=65s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Content sites and with these content sites they don't actually know how to "
              'create great content or build backlinks right.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': "Content sites and with these content sites they don't actually know how to "
             'create great content or build backlinks right.',
      'title': 'Honest Empire Flippers Review   From 10 + Website Purchases (Jaryd Krause - '
               'Buying Online Businesses)',
      'url': 'https://www.youtube.com/watch?v=O0q1EG7DNIc&t=65s',
      'video_id': 'O0q1EG7DNIc'},
     {'author': 'Abdul Latif',
      'channel': 'Abdul Latif',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=pjmp4gM12iQ&t=134s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They sit buried three or four clicks deep, while the blog gets all the links '
              'and all the traffic that never buys anything. So the site looks busy, but the '
              'phone stays quiet. The owner thinks they have a traffic problem. Usually, they '
              'have a linking problem.',
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': 'They sit buried three or four clicks deep, while the blog gets all the links and '
             'all the traffic that never buys anything. So the site looks busy, but the phone '
             'stays quiet. The owner thinks they have a traffic problem. Usually, they have a '
             'linking problem.',
      'title': 'Your Best Pages Are Invisible to Google — Internal Linking Explained (2026) '
               '(Abdul Latif)',
      'url': 'https://www.youtube.com/watch?v=pjmp4gM12iQ&t=134s',
      'video_id': 'pjmp4gM12iQ'},
     {'author': 'Misha Manko',
      'channel': 'Misha Manko',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:22](https://www.youtube.com/watch?v=vcLkBQxf9Hs&t=442s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Not every page here crawl currently not indexed can be a problem. So if it's a "
              'feed filter or some kind of sorting or UTM markers here so a feed for example '
              "it's okay to have these pages here you don't want them to be actually indexed.",
      'timestamp': 442,
      'timestamp_label': '[00:07:22]',
      'timestamp_seconds': 442,
      'tip': "Not every page here crawl currently not indexed can be a problem. So if it's a "
             'feed filter or some kind of sorting or UTM markers here so a feed for example '
             "it's okay to have these pages here you don't want them to be actually indexed.",
      'title': 'Crawled - Currently Not Indexed: How to Fix It (Live Site, Real Data) (Misha '
               'Manko)',
      'url': 'https://www.youtube.com/watch?v=vcLkBQxf9Hs&t=442s',
      'video_id': 'vcLkBQxf9Hs'},
     {'author': 'Koray Tuğberk GÜBÜR',
      'channel': 'Koray Tuğberk GÜBÜR',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=ww7yHUSX5Ak&t=110s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Be showing you some API Le files here I will again be giving you different type '
              'of suggestions but before going there let me just show you this is 3 months of.',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': 'Be showing you some API Le files here I will again be giving you different type '
             'of suggestions but before going there let me just show you this is 3 months of.',
      'title': 'From 0 to 4.000 Clicks a Day: Semantic SEO for Finance - Learn Real Topical '
               'Authority (Koray Tuğberk GÜBÜR)',
      'url': 'https://www.youtube.com/watch?v=ww7yHUSX5Ak&t=110s',
      'video_id': 'ww7yHUSX5Ak'},
     {'author': 'SirLinksalot',
      'channel': 'SirLinksalot',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:25](https://www.youtube.com/watch?v=nSLIbiyP5vc&t=385s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The uh the auto match uh happened to go to the wrong post right what's cool "
              "about it is you can use both of those um together what's the name of the the "
              "one that we use for afford a similar post I don't know if we have on sir links "
              'or redirection most likely.',
      'timestamp': 385,
      'timestamp_label': '[00:06:25]',
      'timestamp_seconds': 385,
      'tip': "The uh the auto match uh happened to go to the wrong post right what's cool "
             "about it is you can use both of those um together what's the name of the the one "
             "that we use for afford a similar post I don't know if we have on sir links or "
             'redirection most likely.',
      'title': 'Should You Rebuild or Redirect EVERY Aged/Expired Domain URL? (SirLinksalot)',
      'url': 'https://www.youtube.com/watch?v=nSLIbiyP5vc&t=385s',
      'video_id': 'nSLIbiyP5vc'},
     {'author': 'Authority Hacker Podcast',
      'channel': 'Authority Hacker Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:22](https://www.youtube.com/watch?v=ePxZx_vQNFo&t=562s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Would communicate around that whereas and and same with penguin they would be '
              "like I don't think penguin they ever said they were going after links or "
              'something but it became pretty obvious.',
      'timestamp': 562,
      'timestamp_label': '[00:09:22]',
      'timestamp_seconds': 562,
      'tip': 'Would communicate around that whereas and and same with penguin they would be '
             "like I don't think penguin they ever said they were going after links or "
             'something but it became pretty obvious.',
      'title': 'Surviving Google Core Updates in 2021 (Ep. 247) (Authority Hacker Podcast)',
      'url': 'https://www.youtube.com/watch?v=ePxZx_vQNFo&t=562s',
      'video_id': 'ePxZx_vQNFo'}],
 6: [{'author': 'Ahrefs',
      'channel': 'Ahrefs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:18](https://www.youtube.com/watch?v=3tbDkc3k48E&t=198s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So I\'ll click on our buyer\'s journey guide, and do a find for "search '
              'intent." And it looks like it\'s unlinked, so it could be a perfectly good '
              'place to add an internal link. The second way is to use the Link Opportunities '
              "report in Ahrefs' Site Audit.",
      'timestamp': 198,
      'timestamp_label': '[00:03:18]',
      'timestamp_seconds': 198,
      'tip': 'So I\'ll click on our buyer\'s journey guide, and do a find for "search intent." '
             "And it looks like it's unlinked, so it could be a perfectly good place to add an "
             "internal link. The second way is to use the Link Opportunities report in Ahrefs' "
             'Site Audit.',
      'title': 'How to Use Internal Links to Rank Higher in Google (Ahrefs)',
      'url': 'https://www.youtube.com/watch?v=3tbDkc3k48E&t=198s',
      'video_id': '3tbDkc3k48E'},
     {'author': 'Tim The SEO Guru',
      'channel': 'Tim The SEO Guru',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:42](https://www.youtube.com/watch?v=cOL8sezUyEQ&t=522s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And the nice thing is Ahrefs has in backend SEO data sources already. And then '
              "you're connecting Ahrefs to your brand, to your brand assets, to your Google "
              'Search Console, to your business profile.',
      'timestamp': 522,
      'timestamp_label': '[00:08:42]',
      'timestamp_seconds': 522,
      'tip': 'And the nice thing is Ahrefs has in backend SEO data sources already. And then '
             "you're connecting Ahrefs to your brand, to your brand assets, to your Google "
             'Search Console, to your business profile.',
      'title': "Google's Core Update Is Back in a New Form. Are You Ready? (Tim The SEO Guru)",
      'url': 'https://www.youtube.com/watch?v=cOL8sezUyEQ&t=522s',
      'video_id': 'cOL8sezUyEQ'},
     {'author': 'Julian Goldie SEO',
      'channel': 'Julian Goldie SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:13](https://www.youtube.com/watch?v=HWSpTVX7qMI&t=253s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Connect your own search console and it works the same way. Agent three is the '
              'page check. A member is about to run their first AI audits for two businesses. '
              'This is the audit I would start with. Google publishes a list of questions to '
              'ask about your own content.',
      'timestamp': 253,
      'timestamp_label': '[00:04:13]',
      'timestamp_seconds': 253,
      'tip': 'Connect your own search console and it works the same way. Agent three is the '
             'page check. A member is about to run their first AI audits for two businesses. '
             'This is the audit I would start with. Google publishes a list of questions to '
             'ask about your own content.',
      'title': "Google's November 2026 Core Update Just Dropped (Do This) (Julian Goldie SEO)",
      'url': 'https://www.youtube.com/watch?v=HWSpTVX7qMI&t=253s',
      'video_id': 'HWSpTVX7qMI'},
     {'author': 'The School of Digital Marketing',
      'channel': 'The School of Digital Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=YK2cFZ61cS8&t=110s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now you can monitor queries and find out which are relevant to your business '
              'take note that you must respond to a lead quickly the emails you receive can '
              'help.',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': 'Now you can monitor queries and find out which are relevant to your business '
             'take note that you must respond to a lead quickly the emails you receive can '
             'help.',
      'title': 'How To Use HARO For Free Backlinks (The School of Digital Marketing)',
      'url': 'https://www.youtube.com/watch?v=YK2cFZ61cS8&t=110s',
      'video_id': 'YK2cFZ61cS8'},
     {'author': 'Pearl Lemon SEO',
      'channel': 'Pearl Lemon SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:07](https://www.youtube.com/watch?v=aRuxCdZQ1Yo&t=127s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Here's where you check this. First things first, you want to open Google Search "
              'Console right here. Right here in settings, you find crawl stats and you open '
              "report. So, what are we looking for here? You're looking for patterns.",
      'timestamp': 127,
      'timestamp_label': '[00:02:07]',
      'timestamp_seconds': 127,
      'tip': "Here's where you check this. First things first, you want to open Google Search "
             'Console right here. Right here in settings, you find crawl stats and you open '
             "report. So, what are we looking for here? You're looking for patterns.",
      'title': 'How to Fix Crawl Budget Issues and Improve Your SEO in 2026 (Pearl Lemon SEO)',
      'url': 'https://www.youtube.com/watch?v=aRuxCdZQ1Yo&t=127s',
      'video_id': 'aRuxCdZQ1Yo'},
     {'author': 'Koray Tuğberk GÜBÜR',
      'channel': 'Koray Tuğberk GÜBÜR',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:56](https://www.youtube.com/watch?v=DoFTx8z5X2g&t=476s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "For the first time so maybe we have because search gbt's data is different but "
              'apparently we have most of that so try to see how you are using it how many.',
      'timestamp': 476,
      'timestamp_label': '[00:07:56]',
      'timestamp_seconds': 476,
      'tip': "For the first time so maybe we have because search gbt's data is different but "
             'apparently we have most of that so try to see how you are using it how many.',
      'title': 'EEAT with SEMANTICS and Topical Authority: 4x Organic SEO Growth through '
               'Helpful Content Update (Koray Tuğberk GÜBÜR)',
      'url': 'https://www.youtube.com/watch?v=DoFTx8z5X2g&t=476s',
      'video_id': 'DoFTx8z5X2g'},
     {'author': 'Travis Wilkie',
      'channel': 'Travis Wilkie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:39](https://www.youtube.com/watch?v=0qP8UUWuBSc&t=99s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It'll show you like the potential search volume for those keywords and um for "
              'those clusters and and on and on and on, right? So, first you need to set up a '
              'list.',
      'timestamp': 99,
      'timestamp_label': '[00:01:39]',
      'timestamp_seconds': 99,
      'tip': "It'll show you like the potential search volume for those keywords and um for "
             'those clusters and and on and on and on, right? So, first you need to set up a '
             'list.',
      'title': 'How To Do Keyword Clustering Using Semrush (Travis Wilkie)',
      'url': 'https://www.youtube.com/watch?v=0qP8UUWuBSc&t=99s',
      'video_id': '0qP8UUWuBSc'},
     {'author': 'Kasra Dash',
      'channel': 'Kasra Dash',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=yzNo7jJ8WBE&t=22s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ve never done a technical SEO audit, what a technical SEO audit allows you to "
              'do is it allows you to analyze how search engines first of all crawl, render, '
              'and index your website, but then it also allows you to identify any barriers on '
              "on your website's growth.",
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "'ve never done a technical SEO audit, what a technical SEO audit allows you to "
             'do is it allows you to analyze how search engines first of all crawl, render, '
             'and index your website, but then it also allows you to identify any barriers on '
             "on your website's growth.",
      'title': 'Complete Technical SEO Guide 2026 (Fix Crawl, Index & Speed Issues) (Kasra '
               'Dash)',
      'url': 'https://www.youtube.com/watch?v=yzNo7jJ8WBE&t=22s',
      'video_id': 'yzNo7jJ8WBE'},
     {'author': 'James Dooley',
      'channel': 'James Dooley',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:41](https://www.youtube.com/watch?v=XIZhTUQmcNI&t=461s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "GPT, that is more reliant on training data, but it's still going to be sourcing "
              "through being quite a lot. So, the first thing is there's going to be "
              "differences in how being and Google rank pages. So, you're going to be ranked "
              'differently.',
      'timestamp': 461,
      'timestamp_label': '[00:07:41]',
      'timestamp_seconds': 461,
      'tip': "GPT, that is more reliant on training data, but it's still going to be sourcing "
             "through being quite a lot. So, the first thing is there's going to be "
             "differences in how being and Google rank pages. So, you're going to be ranked "
             'differently.',
      'title': 'Parasite SEO in 2026 for Third Party Corroboration (James Dooley Interviews '
               'Charles Floate) (James Dooley)',
      'url': 'https://www.youtube.com/watch?v=XIZhTUQmcNI&t=461s',
      'video_id': 'XIZhTUQmcNI'},
     {'author': 'Tutorial Stack',
      'channel': 'Tutorial Stack',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=fLGvfe6OTgc&t=118s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can just go to any keyword or ads, sorry, any keyword in here and then we '
              "I'm just going to show you exactly how to cluster up that keyword. So, simply "
              'just add your keyword and hit search.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': 'You can just go to any keyword or ads, sorry, any keyword in here and then we '
             "I'm just going to show you exactly how to cluster up that keyword. So, simply "
             'just add your keyword and hit search.',
      'title': 'How to Do Keyword Clustering in Semrush (Step-by-Step) (Tutorial Stack)',
      'url': 'https://www.youtube.com/watch?v=fLGvfe6OTgc&t=118s',
      'video_id': 'fLGvfe6OTgc'},
     {'author': 'Ahrefs Product Updates',
      'channel': 'Ahrefs Product Updates',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:58](https://www.youtube.com/watch?v=JMyPIbu7vhw&t=58s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Plus, these numbers beside the groups tell you the total search volume that '
              "includes the word or phrase in your target country. It's definitely a much "
              'quicker way to sort through all your data.',
      'timestamp': 58,
      'timestamp_label': '[00:00:58]',
      'timestamp_seconds': 58,
      'tip': 'Plus, these numbers beside the groups tell you the total search volume that '
             "includes the word or phrase in your target country. It's definitely a much "
             'quicker way to sort through all your data.',
      'title': 'New: Keyword Grouping in Keywords Explorer (Ahrefs Product Updates)',
      'url': 'https://www.youtube.com/watch?v=JMyPIbu7vhw&t=58s',
      'video_id': 'JMyPIbu7vhw'},
     {'author': 'Tutorial Stack',
      'channel': 'Tutorial Stack',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:24](https://www.youtube.com/watch?v=1Q38-qqOu3c&t=24s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is going to really help you out quite a lot. So just go and select this '
              'one. And you want to basically just enter your keyword in here and click on '
              'search and we will show you exactly how to find the better ones. So just go and '
              'add your keyword in here.',
      'timestamp': 24,
      'timestamp_label': '[00:00:24]',
      'timestamp_seconds': 24,
      'tip': 'This is going to really help you out quite a lot. So just go and select this '
             'one. And you want to basically just enter your keyword in here and click on '
             'search and we will show you exactly how to find the better ones. So just go and '
             'add your keyword in here.',
      'title': 'How to Find Low Competition Keywords in Semrush (Full Tutorial) (Tutorial '
               'Stack)',
      'url': 'https://www.youtube.com/watch?v=1Q38-qqOu3c&t=24s',
      'video_id': '1Q38-qqOu3c'},
     {'author': 'Manan Gupta',
      'channel': 'Manan Gupta',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:35](https://www.youtube.com/watch?v=_DewVbSSXe0&t=275s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Phone number. You want to list your NAP on multiple.',
      'timestamp': 275,
      'timestamp_label': '[00:04:35]',
      'timestamp_seconds': 275,
      'tip': 'Phone number. You want to list your NAP on multiple.',
      'title': 'Real Estate SEO (Complete 2025 Guide) | Rank #1 in Google (Manan Gupta)',
      'url': 'https://www.youtube.com/watch?v=_DewVbSSXe0&t=275s',
      'video_id': '_DewVbSSXe0'},
     {'author': 'Contentbase',
      'channel': 'Contentbase',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:14](https://www.youtube.com/watch?v=fetD9UtOY78&t=194s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'About combining data Automation and a focus on providing valuable information '
              "to users it's not a Magic Bullet but it can be incredibly effective that was a "
              'great discussion thanks for sharing your insights.',
      'timestamp': 194,
      'timestamp_label': '[00:03:14]',
      'timestamp_seconds': 194,
      'tip': 'About combining data Automation and a focus on providing valuable information to '
             "users it's not a Magic Bullet but it can be incredibly effective that was a "
             'great discussion thanks for sharing your insights.',
      'title': 'Programmatic SEO Case Study - Payscale (Contentbase)',
      'url': 'https://www.youtube.com/watch?v=fetD9UtOY78&t=194s',
      'video_id': 'fetD9UtOY78'},
     {'author': 'Optimist - Growth-Focused Content Marketing Agency',
      'channel': 'Optimist - Growth-Focused Content Marketing Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:00:19](https://www.youtube.com/watch?v=OvzerRoMcu8&t=3619s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Yeah thank you for having me and thank you for all the viewers as well I mean '
              'uh this is a this has been a really nice opportunity for me to share my '
              "insights as well so yeah awesome well that'll be all for today thanks again and "
              'and cheers all thanks for joining.',
      'timestamp': 3619,
      'timestamp_label': '[01:00:19]',
      'timestamp_seconds': 3619,
      'tip': 'Yeah thank you for having me and thank you for all the viewers as well I mean uh '
             'this is a this has been a really nice opportunity for me to share my insights as '
             "well so yeah awesome well that'll be all for today thanks again and and cheers "
             'all thanks for joining.',
      'title': 'Build Back Links With HARO - How To Earn Free DR90+ Links | Optimist (Optimist '
               '- Growth-Focused Content Marketing Agency)',
      'url': 'https://www.youtube.com/watch?v=OvzerRoMcu8&t=3619s',
      'video_id': 'OvzerRoMcu8'}],
 7: [{'author': 'Bill Mcintosh',
      'channel': 'Bill Mcintosh',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:05](https://www.youtube.com/watch?v=UGKO4HDAk8w&t=605s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Are the author claims and prices genuine? Did you review the AI written '
              "details? Would someone trust this business enough to take the next step? That's "
              "the old credit card question brought into [clears throat] today's AI workflow.",
      'timestamp': 605,
      'timestamp_label': '[00:10:05]',
      'timestamp_seconds': 605,
      'tip': 'Are the author claims and prices genuine? Did you review the AI written details? '
             "Would someone trust this business enough to take the next step? That's the old "
             "credit card question brought into [clears throat] today's AI workflow.",
      'title': 'Google Core Update ALERT: 3 New SEO Mistakes That Can Tank Your Traffic (Bill '
               'Mcintosh)',
      'url': 'https://www.youtube.com/watch?v=UGKO4HDAk8w&t=605s',
      'video_id': 'UGKO4HDAk8w'},
     {'author': 'Behzad Hussain',
      'channel': 'Behzad Hussain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:10](https://www.youtube.com/watch?v=NQCo-V1utn8&t=250s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Here we will process the finalized topics in step 20 we will create title tags '
              'based on serp analysis and then in step 21 we will structure URLs for each node '
              'or page. In step 22 we will create image alt texts. In step 23 we will create '
              'image name or URL.',
      'timestamp': 250,
      'timestamp_label': '[00:04:10]',
      'timestamp_seconds': 250,
      'tip': 'Here we will process the finalized topics in step 20 we will create title tags '
             'based on serp analysis and then in step 21 we will structure URLs for each node '
             'or page. In step 22 we will create image alt texts. In step 23 we will create '
             'image name or URL.',
      'title': 'Master Topical Map Authority : 26 Micro-Steps to Rank #1 (Semantic SEO Content '
               'Strategy) (Behzad Hussain)',
      'url': 'https://www.youtube.com/watch?v=NQCo-V1utn8&t=250s',
      'video_id': 'NQCo-V1utn8'},
     {'author': 'Kasra Dash',
      'channel': 'Kasra Dash',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=I26NAT6T6Gs&t=88s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Half of those sites had pages far away from what the business sells. And it '
              'usually starts with good intentions. Step one, cover your core topics before '
              'anything else. For years, we were told the more articles on your site, the '
              'better.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'Half of those sites had pages far away from what the business sells. And it '
             'usually starts with good intentions. Step one, cover your core topics before '
             'anything else. For years, we were told the more articles on your site, the '
             'better.',
      'title': 'Topical Authority Is DEAD (Do This Instead) (Kasra Dash)',
      'url': 'https://www.youtube.com/watch?v=I26NAT6T6Gs&t=88s',
      'video_id': 'I26NAT6T6Gs'},
     {'author': 'Mike Swigunski',
      'channel': 'Mike Swigunski',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=w5fG8eKka5Y&t=15s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Business you're going to want to stick around i'm going to show you the exact "
              'five-step process to buy a profitable.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Business you're going to want to stick around i'm going to show you the exact "
             'five-step process to buy a profitable.',
      'title': 'Buying and Selling Websites with Empire Flippers! 5 Step Online Business '
               'Buying Process (Mike Swigunski)',
      'url': 'https://www.youtube.com/watch?v=w5fG8eKka5Y&t=15s',
      'video_id': 'w5fG8eKka5Y'},
     {'author': 'Fery Kaszoni',
      'channel': 'Fery Kaszoni',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=BpLuK4tA5zw&t=139s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I just had to rewrite it like two or three times until I thought it was good to '
              'go. And that’s the whole execution of the campaign before the outreach. Now, '
              'let’s look at the outreach process.',
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': 'I just had to rewrite it like two or three times until I thought it was good to '
             'go. And that’s the whole execution of the campaign before the outreach. Now, '
             'let’s look at the outreach process.',
      'title': 'Digital PR Link Building - 50 Links Built in 3 Hours (Fery Kaszoni)',
      'url': 'https://www.youtube.com/watch?v=BpLuK4tA5zw&t=139s',
      'video_id': 'BpLuK4tA5zw'},
     {'author': 'Travis Wilkie',
      'channel': 'Travis Wilkie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:40](https://www.youtube.com/watch?v=wSkIVyKv2rY&t=160s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s bringing you a consistent flow of customers, right? So, that's why I created "
              'this free course where I actually walk you step by step through the whole '
              'process of setting up your online presence.',
      'timestamp': 160,
      'timestamp_label': '[00:02:40]',
      'timestamp_seconds': 160,
      'tip': "'s bringing you a consistent flow of customers, right? So, that's why I created "
             'this free course where I actually walk you step by step through the whole '
             'process of setting up your online presence.',
      'title': 'How To Do Keyword Clustering Using Ahrefs (Travis Wilkie)',
      'url': 'https://www.youtube.com/watch?v=wSkIVyKv2rY&t=160s',
      'video_id': 'wSkIVyKv2rY'},
     {'author': 'CanEye',
      'channel': 'CanEye',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:55](https://www.youtube.com/watch?v=kZ7NX7BR1X8&t=415s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Complete product survey and start shopping. So, like survey ads and make money '
              'with surveys. These are just ads that in my opinion are kind of low quality '
              "that I don't really love showing.",
      'timestamp': 415,
      'timestamp_label': '[00:06:55]',
      'timestamp_seconds': 415,
      'tip': 'Complete product survey and start shopping. So, like survey ads and make money '
             'with surveys. These are just ads that in my opinion are kind of low quality that '
             "I don't really love showing.",
      'title': 'AdSense, Mediavine and Ezoic Alternative?  Make Money Blogging in 2025! '
               '(CanEye)',
      'url': 'https://www.youtube.com/watch?v=kZ7NX7BR1X8&t=415s',
      'video_id': 'kZ7NX7BR1X8'},
     {'author': 'The Answer Lab | GEO & AEO',
      'channel': 'The Answer Lab | GEO & AEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:15](https://www.youtube.com/watch?v=yeLHXIInymI&t=315s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The top of a page. Specifics beat slogans, prices, sizes, delivery times, who '
              "it's for, and who it isn't for.  Step four, back it up. Facts.",
      'timestamp': 315,
      'timestamp_label': '[00:05:15]',
      'timestamp_seconds': 315,
      'tip': 'The top of a page. Specifics beat slogans, prices, sizes, delivery times, who '
             "it's for, and who it isn't for.  Step four, back it up. Facts.",
      'title': 'What Is GEO? Generative Engine Optimization Explained (The Answer Lab | GEO & '
               'AEO)',
      'url': 'https://www.youtube.com/watch?v=yeLHXIInymI&t=315s',
      'video_id': 'yeLHXIInymI'},
     {'author': 'James Taylor SEO',
      'channel': 'James Taylor SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:18](https://www.youtube.com/watch?v=tRq2jVJMTNQ&t=378s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Cheers for checking this one out definitely don't discount harrow from your "
              "lint building process it's such a good tool um and yeah if you have any quick "
              "wins or anything like that with it give us a shout be interested cheers I'll "
              'catch you next time.',
      'timestamp': 378,
      'timestamp_label': '[00:06:18]',
      'timestamp_seconds': 378,
      'tip': "Cheers for checking this one out definitely don't discount harrow from your lint "
             "building process it's such a good tool um and yeah if you have any quick wins or "
             "anything like that with it give us a shout be interested cheers I'll catch you "
             'next time.',
      'title': 'Link Building With HARO (Help A Reporter Out) - Overview & Guide (James Taylor '
               'SEO)',
      'url': 'https://www.youtube.com/watch?v=tRq2jVJMTNQ&t=378s',
      'video_id': 'tRq2jVJMTNQ'},
     {'author': 'Amazon SEO Consultant',
      'channel': 'Amazon SEO Consultant',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:25](https://www.youtube.com/watch?v=Knzcwbb96v8&t=565s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Experience Empire flippers delivers where it matters most in successful verify '
              'transactions thank you very much for watching we really hope this helped and '
              "we'll see you in the next video.",
      'timestamp': 565,
      'timestamp_label': '[00:09:25]',
      'timestamp_seconds': 565,
      'tip': 'Experience Empire flippers delivers where it matters most in successful verify '
             'transactions thank you very much for watching we really hope this helped and '
             "we'll see you in the next video.",
      'title': 'Empire Flippers Review - Post Purchase | Online Business Marketplace (Amazon '
               'FBA & Our Experience) (Amazon SEO Consultant)',
      'url': 'https://www.youtube.com/watch?v=Knzcwbb96v8&t=565s',
      'video_id': 'Knzcwbb96v8'},
     {'author': 'WeStudyFunnels',
      'channel': 'WeStudyFunnels',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:20](https://www.youtube.com/watch?v=PpHWPSjRYPI&t=260s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Know obviously content is going to be of varying qualities but I would guess '
              "that some of these companies are publishing some high quality content I don't "
              "know let's just see the top two.",
      'timestamp': 260,
      'timestamp_label': '[00:04:20]',
      'timestamp_seconds': 260,
      'tip': 'Know obviously content is going to be of varying qualities but I would guess '
             "that some of these companies are publishing some high quality content I don't "
             "know let's just see the top two.",
      'title': 'Where SEMRUSH and Ahrefs Keyword Difficulty Score Fails (WeStudyFunnels)',
      'url': 'https://www.youtube.com/watch?v=PpHWPSjRYPI&t=260s',
      'video_id': 'PpHWPSjRYPI'},
     {'author': 'TM Blast',
      'channel': 'TM Blast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:28](https://www.youtube.com/watch?v=1v7Wiw-ptLU&t=448s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The uh before and after but I really wanted to record this video to explain my '
              'thought process so let me know if you guys have any questions as always have a '
              'good rest of your day.',
      'timestamp': 448,
      'timestamp_label': '[00:07:28]',
      'timestamp_seconds': 448,
      'tip': 'The uh before and after but I really wanted to record this video to explain my '
             'thought process so let me know if you guys have any questions as always have a '
             'good rest of your day.',
      'title': 'Using Log File Analysis to Improve How Google Crawls My Website (TM Blast)',
      'url': 'https://www.youtube.com/watch?v=1v7Wiw-ptLU&t=448s',
      'video_id': '1v7Wiw-ptLU'},
     {'author': 'CanEye',
      'channel': 'CanEye',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:16](https://www.youtube.com/watch?v=FyVNDOxiU6o&t=376s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Keep showing you this process and continue to keep showing you my results and '
              'if you are interested in this kind of stuff then please do all those things '
              "you're supposed to do to help with Channel growth and I'll see you in the next "
              'one this guy sucks.',
      'timestamp': 376,
      'timestamp_label': '[00:06:16]',
      'timestamp_seconds': 376,
      'tip': 'Keep showing you this process and continue to keep showing you my results and if '
             "you are interested in this kind of stuff then please do all those things you're "
             "supposed to do to help with Channel growth and I'll see you in the next one this "
             'guy sucks.',
      'title': 'First full month Mediavine earnings report! [Pinterest Affiliate Marketing] '
               '(CanEye)',
      'url': 'https://www.youtube.com/watch?v=FyVNDOxiU6o&t=376s',
      'video_id': 'FyVNDOxiU6o'},
     {'author': 'Contentbase',
      'channel': 'Contentbase',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:06](https://www.youtube.com/watch?v=3Fkd3FP40iU&t=186s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Takeaway here programmatic SEO can be a GameChanger for businesses looking to '
              'increase their organic traffic but it requires planning and execution '
              "definitely it's all about strategic implementation that was a great discussion "
              'thanks for sharing your insights.',
      'timestamp': 186,
      'timestamp_label': '[00:03:06]',
      'timestamp_seconds': 186,
      'tip': 'Takeaway here programmatic SEO can be a GameChanger for businesses looking to '
             'increase their organic traffic but it requires planning and execution definitely '
             "it's all about strategic implementation that was a great discussion thanks for "
             'sharing your insights.',
      'title': 'Programmatic SEO Case Study - moveBuddha (Contentbase)',
      'url': 'https://www.youtube.com/watch?v=3Fkd3FP40iU&t=186s',
      'video_id': '3Fkd3FP40iU'},
     {'author': 'Contentbase',
      'channel': 'Contentbase',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:08](https://www.youtube.com/watch?v=hGy2v1LMEg0&t=188s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "A balancing act yeah so it's a powerful strategy but it requires careful "
              "planning and execution precisely it's not a Magic Bullet but when done right it "
              'can be incredibly effective that was a great discussion thanks for sharing your '
              'insights.',
      'timestamp': 188,
      'timestamp_label': '[00:03:08]',
      'timestamp_seconds': 188,
      'tip': "A balancing act yeah so it's a powerful strategy but it requires careful "
             "planning and execution precisely it's not a Magic Bullet but when done right it "
             'can be incredibly effective that was a great discussion thanks for sharing your '
             'insights.',
      'title': 'Programmatic SEO Case Study - G2 (Contentbase)',
      'url': 'https://www.youtube.com/watch?v=hGy2v1LMEg0&t=188s',
      'video_id': 'hGy2v1LMEg0'}],
 8: [{'author': 'Site Verdict',
      'channel': 'Site Verdict',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=tEUh8E-4D7U&t=71s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Rush provides keyword research. It also does competitor analysis. Position '
              'tracking and site audit  are core tools. Both cover essential SEO needs.',
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': 'Rush provides keyword research. It also does competitor analysis. Position '
             'tracking and site audit  are core tools. Both cover essential SEO needs.',
      'title': 'Ahrefs vs SEMrush 2026: Which Is Better? (Site Verdict)',
      'url': 'https://www.youtube.com/watch?v=tEUh8E-4D7U&t=71s',
      'video_id': 'tEUh8E-4D7U'},
     {'author': 'masudbcl',
      'channel': 'masudbcl',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:01](https://www.youtube.com/watch?v=lbSL3iPtyq8&t=121s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Prices about a daily page visit monthly page visit early page visit daily '
              'monthly and yearly revenues also I will show you a link price calculator as '
              'your tool or seo software from a small seo tools website free seo tools '
              'software section.',
      'timestamp': 121,
      'timestamp_label': '[00:02:01]',
      'timestamp_seconds': 121,
      'tip': 'Prices about a daily page visit monthly page visit early page visit daily '
             'monthly and yearly revenues also I will show you a link price calculator as your '
             'tool or seo software from a small seo tools website free seo tools software '
             'section.',
      'title': '💸 Link Price Calculator Tutorial: Essential SEO Tool for White Hat SEO | '
               '(masudbcl)',
      'url': 'https://www.youtube.com/watch?v=lbSL3iPtyq8&t=121s',
      'video_id': 'lbSL3iPtyq8'},
     {'author': 'AI Innovations With Maria Johnsen',
      'channel': 'AI Innovations With Maria Johnsen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:39](https://www.youtube.com/watch?v=8iciP8By_g4&t=939s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm not telling you their name. They offer these tool management tools, and "
              'they spend years on traditional SEO practices. The website attracted 13,000 '
              'visitors and very little traffic came from AI platform. The company decided to '
              'rethink its strategy.',
      'timestamp': 939,
      'timestamp_label': '[00:15:39]',
      'timestamp_seconds': 939,
      'tip': "I'm not telling you their name. They offer these tool management tools, and they "
             'spend years on traditional SEO practices. The website attracted 13,000 visitors '
             'and very little traffic came from AI platform. The company decided to rethink '
             'its strategy.',
      'title': 'Generative Engine Optimization (GEO) How to Rank in AI Search Engines (AI '
               'Innovations With Maria Johnsen)',
      'url': 'https://www.youtube.com/watch?v=8iciP8By_g4&t=939s',
      'video_id': '8iciP8By_g4'},
     {'author': 'FatRank',
      'channel': 'FatRank',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:09](https://www.youtube.com/watch?v=GVJrNHhAXME&t=189s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But uh there are tools out there. Um you can just download your log files and '
              'input them into something like uh Dreamy Frog has a log analyzer tool which is '
              'quite basic but will give you the data.',
      'timestamp': 189,
      'timestamp_label': '[00:03:09]',
      'timestamp_seconds': 189,
      'tip': 'But uh there are tools out there. Um you can just download your log files and '
             'input them into something like uh Dreamy Frog has a log analyzer tool which is '
             'quite basic but will give you the data.',
      'title': 'The Real Importance of Crawl Budget for SEO (FatRank)',
      'url': 'https://www.youtube.com/watch?v=GVJrNHhAXME&t=189s',
      'video_id': 'GVJrNHhAXME'},
     {'author': 'WordsAtScale',
      'channel': 'WordsAtScale',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:17](https://www.youtube.com/watch?v=mpV06kMELhI&t=137s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And that's the essence of the search gap ideology, finding low competition, "
              "flying under the radar products, and reviewing them. And I'm very happy to say "
              'that my linkbait data gap articles have started to get traction.',
      'timestamp': 137,
      'timestamp_label': '[00:02:17]',
      'timestamp_seconds': 137,
      'tip': "And that's the essence of the search gap ideology, finding low competition, "
             "flying under the radar products, and reviewing them. And I'm very happy to say "
             'that my linkbait data gap articles have started to get traction.',
      'title': "Google March 2026 Core Update: Every Site I Own Survived (Here's Why) "
               '(WordsAtScale)',
      'url': 'https://www.youtube.com/watch?v=mpV06kMELhI&t=137s',
      'video_id': 'mpV06kMELhI'},
     {'author': 'Matthew Zare',
      'channel': 'Matthew Zare',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:09](https://www.youtube.com/watch?v=HwZI5n7WwiI&t=69s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '"What\'s the best CRM for a startup?" "How do I improve my website\'s SEO?" No '
              'scrolling, no comparing 10 articles, no clicking through search results. The AI '
              "has already done the research. Here's something else that most people don't "
              'realize.',
      'timestamp': 69,
      'timestamp_label': '[00:01:09]',
      'timestamp_seconds': 69,
      'tip': '"What\'s the best CRM for a startup?" "How do I improve my website\'s SEO?" No '
             'scrolling, no comparing 10 articles, no clicking through search results. The AI '
             "has already done the research. Here's something else that most people don't "
             'realize.',
      'title': 'What Is GEO (Generative Engine Optimization)? The Complete Guide for AI Search '
               '(Matthew Zare)',
      'url': 'https://www.youtube.com/watch?v=HwZI5n7WwiI&t=69s',
      'video_id': 'HwZI5n7WwiI'},
     {'author': 'Fast Hippo Media',
      'channel': 'Fast Hippo Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=JrHxc3BMz6g&t=80s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The GEO playbook, how to shape what AI says about you. Here's the GEO playbook "
              'we use  at Fast Hippo Media. Audit your brand inside AI tools. Search.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': "The GEO playbook, how to shape what AI says about you. Here's the GEO playbook "
             'we use  at Fast Hippo Media. Audit your brand inside AI tools. Search.',
      'title': 'ChatGPT Generative Engine Optimization (GEO) Guide (Fast Hippo Media)',
      'url': 'https://www.youtube.com/watch?v=JrHxc3BMz6g&t=80s',
      'video_id': 'JrHxc3BMz6g'},
     {'author': 'Spy Opinion',
      'channel': 'Spy Opinion',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:56](https://www.youtube.com/watch?v=TdrC4IUva6k&t=176s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "SEO tools, think like this. What's the best SEO tool for beginners? People talk "
              'differently than they type. Your content should reflect that. Strategy six, '
              'generative engine optimization for social search.',
      'timestamp': 176,
      'timestamp_label': '[00:02:56]',
      'timestamp_seconds': 176,
      'tip': "SEO tools, think like this. What's the best SEO tool for beginners? People talk "
             'differently than they type. Your content should reflect that. Strategy six, '
             'generative engine optimization for social search.',
      'title': '10 Powerful Generative Engine Optimization (GEO) Strategies for 2025 | Rank #1 '
               'in AI Search (Spy Opinion)',
      'url': 'https://www.youtube.com/watch?v=TdrC4IUva6k&t=176s',
      'video_id': 'TdrC4IUva6k'},
     {'author': 'Samik Choudhury',
      'channel': 'Samik Choudhury',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=xbFsXyB1UZo&t=98s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'SEO we create one template which can be used into different blog pages. So you '
              "don't have to rewrite the UI again and again. You just get the data from your "
              'database or from anything like this one.',
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': 'SEO we create one template which can be used into different blog pages. So you '
             "don't have to rewrite the UI again and again. You just get the data from your "
             'database or from anything like this one.',
      'title': 'Programmatic SEO Tutorial ($1,175 MRR in 72 Days Case Study) (Samik Choudhury)',
      'url': 'https://www.youtube.com/watch?v=xbFsXyB1UZo&t=98s',
      'video_id': 'xbFsXyB1UZo'},
     {'author': 'BSM - A Denver SEO Company',
      'channel': 'BSM - A Denver SEO Company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=2jejTy2fWTg&t=115s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So hopefully you'll be able to join me there in Seattle. So, let's take a look "
              "at Google Search Console. If you haven't set this free Google tool up for your "
              'website yet, make sure do that right away.',
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': "So hopefully you'll be able to join me there in Seattle. So, let's take a look "
             "at Google Search Console. If you haven't set this free Google tool up for your "
             'website yet, make sure do that right away.',
      'title': 'Google’s March 2025 Core Update—How to Check If You Were Hit or Helped (BSM - '
               'A Denver SEO Company)',
      'url': 'https://www.youtube.com/watch?v=2jejTy2fWTg&t=115s',
      'video_id': '2jejTy2fWTg'},
     {'author': "Meghan's Media",
      'channel': "Meghan's Media",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:10](https://www.youtube.com/watch?v=XXTUzO1Y_1U&t=310s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "However, there's actually one thing I do like a little bit better with Raptive. "
              'Um in their dashboard, they have some really cool SEO tools. I really like '
              "their keyword research tool, which I'm starting to use as like my main tool, um "
              "and it's free for their publishers.",
      'timestamp': 310,
      'timestamp_label': '[00:05:10]',
      'timestamp_seconds': 310,
      'tip': "However, there's actually one thing I do like a little bit better with Raptive. "
             'Um in their dashboard, they have some really cool SEO tools. I really like their '
             "keyword research tool, which I'm starting to use as like my main tool, um and "
             "it's free for their publishers.",
      'title': "My REAL Blog Income (With Less Traffic) — Mediavine vs Raptive (Meghan's "
               'Media)',
      'url': 'https://www.youtube.com/watch?v=XXTUzO1Y_1U&t=310s',
      'video_id': 'XXTUzO1Y_1U'},
     {'author': 'Contentbase',
      'channel': 'Contentbase',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:23](https://www.youtube.com/watch?v=51GhDWoaU_A&t=203s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They've shown that automation could be a powerful tool for driving organic "
              "traffic absolutely it's a testament to the power of data driven decision making "
              'and a well executed strategy that was a great discussion thanks for sharing '
              'your insights my pleasure.',
      'timestamp': 203,
      'timestamp_label': '[00:03:23]',
      'timestamp_seconds': 203,
      'tip': "They've shown that automation could be a powerful tool for driving organic "
             "traffic absolutely it's a testament to the power of data driven decision making "
             'and a well executed strategy that was a great discussion thanks for sharing your '
             'insights my pleasure.',
      'title': 'Programmatic SEO Case Study - Make (Contentbase)',
      'url': 'https://www.youtube.com/watch?v=51GhDWoaU_A&t=203s',
      'video_id': '51GhDWoaU_A'},
     {'author': 'SarojTech',
      'channel': 'SarojTech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:09](https://www.youtube.com/watch?v=l0X0MgV5EP4&t=129s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'LinkedIn पेज पर किया है। इसकी ऑफिशियल वेबसाइट है सर्च कंसोल की। वहां पर हम चलते '
              'हैं। यह LinkedIn पोस्ट किया है इसने। इसके बाद हम इस पर क्लिक करते हैं। ठीक है। '
              'तो यह इसकी जो है ऑफिशियल वेबसाइट है, देखो Google की। ठीक है। search.',
      'timestamp': 129,
      'timestamp_label': '[00:02:09]',
      'timestamp_seconds': 129,
      'tip': 'LinkedIn पेज पर किया है। इसकी ऑफिशियल वेबसाइट है सर्च कंसोल की। वहां पर हम चलते '
             'हैं। यह LinkedIn पोस्ट किया है इसने। इसके बाद हम इस पर क्लिक करते हैं। ठीक है। '
             'तो यह इसकी जो है ऑफिशियल वेबसाइट है, देखो Google की। ठीक है। search.',
      'title': 'Google November 2026 Core Update Officially Released | SEO Ranking Update | '
               'SarojTech (SarojTech)',
      'url': 'https://www.youtube.com/watch?v=l0X0MgV5EP4&t=129s',
      'video_id': 'l0X0MgV5EP4'},
     {'author': 'Koray Tuğberk GÜBÜR',
      'channel': 'Koray Tuğberk GÜBÜR',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:08](https://www.youtube.com/watch?v=l_Eiy1S5MeA&t=668s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Based on the previous identity as much as possible and from there make a log '
              'file analysis for the most scrolled ones revive them resurrect them and link '
              'your.',
      'timestamp': 668,
      'timestamp_label': '[00:11:08]',
      'timestamp_seconds': 668,
      'tip': 'Based on the previous identity as much as possible and from there make a log '
             'file analysis for the most scrolled ones revive them resurrect them and link '
             'your.',
      'title': 'From Dead to Alive: Expired Domain SEO Case Study Achieves 2000X Growth (Koray '
               'Tuğberk GÜBÜR)',
      'url': 'https://www.youtube.com/watch?v=l_Eiy1S5MeA&t=668s',
      'video_id': 'l_Eiy1S5MeA'},
     {'author': 'Contentbase',
      'channel': 'Contentbase',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=oAo6faMNv24&t=15s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Programmatic SEO automation platform try content based for free today at '
              'contentbase doai ever wonder um how Trip Advisor.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Programmatic SEO automation platform try content based for free today at '
             'contentbase doai ever wonder um how Trip Advisor.',
      'title': 'Programmatic SEO Case Study - Tripadvisor (Contentbase)',
      'url': 'https://www.youtube.com/watch?v=oAo6faMNv24&t=15s',
      'video_id': 'oAo6faMNv24'}],
 9: [{'author': 'Real Estate SEO & Web Design',
      'channel': 'Real Estate SEO & Web Design',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:16](https://www.youtube.com/watch?v=xDMs5FogvQ8&t=1036s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And then you want to make sure you obviously link all of those articles to each '
              'other to build that relevance before you spend time and money trying to build '
              'external backlinks to your website from other websites to grow your authority.',
      'timestamp': 1036,
      'timestamp_label': '[00:17:16]',
      'timestamp_seconds': 1036,
      'tip': 'And then you want to make sure you obviously link all of those articles to each '
             'other to build that relevance before you spend time and money trying to build '
             'external backlinks to your website from other websites to grow your authority.',
      'title': 'SEO Hacks for Realtor Websites in 2026 (Real Estate SEO & Web Design)',
      'url': 'https://www.youtube.com/watch?v=xDMs5FogvQ8&t=1036s',
      'video_id': 'xDMs5FogvQ8'},
     {'author': 'James Dooley',
      'channel': 'James Dooley',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:23](https://www.youtube.com/watch?v=mE2Y-3fNorE&t=863s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You just mass created everything. You've not worked through your tiers. You "
              "don't have the traffic, which then builds up the authority for that topic of "
              'what you can have. And then you can then start building up other terms around '
              "it. Don't, don't be afraid of Google, right?",
      'timestamp': 863,
      'timestamp_label': '[00:14:23]',
      'timestamp_seconds': 863,
      'tip': "You just mass created everything. You've not worked through your tiers. You "
             "don't have the traffic, which then builds up the authority for that topic of "
             'what you can have. And then you can then start building up other terms around '
             "it. Don't, don't be afraid of Google, right?",
      'title': 'Building Topical Authority: How to Gain Traction For a New Topic (James Dooley '
               'ft David G Quaid) (James Dooley)',
      'url': 'https://www.youtube.com/watch?v=mE2Y-3fNorE&t=863s',
      'video_id': 'mE2Y-3fNorE'},
     {'author': 'Jacky Chou from Indexsy',
      'channel': 'Jacky Chou from Indexsy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:11](https://www.youtube.com/watch?v=m1jRNdRvtb0&t=251s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, if it's rank and rent and affiliate articles, it's okay. But if it's "
              "disclosed articles, then it's not. Let's see if this is always check rules. So "
              'undisclosed, probably illegal if this is written by CBD North, like if this is '
              'a rank and rent, you know what I mean?',
      'timestamp': 251,
      'timestamp_label': '[00:04:11]',
      'timestamp_seconds': 251,
      'tip': "So, if it's rank and rent and affiliate articles, it's okay. But if it's "
             "disclosed articles, then it's not. Let's see if this is always check rules. So "
             'undisclosed, probably illegal if this is written by CBD North, like if this is a '
             'rank and rent, you know what I mean?',
      'title': 'Google is formally targeting Parasite SEO (again) (Jacky Chou from Indexsy)',
      'url': 'https://www.youtube.com/watch?v=m1jRNdRvtb0&t=251s',
      'video_id': 'm1jRNdRvtb0'},
     {'author': 'Frey Chu',
      'channel': 'Frey Chu',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:38](https://www.youtube.com/watch?v=mHkLfhpVYqc&t=818s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t really deliver in terms of the page traffic, but assuming that you were "
              'looking at an expired domain that had the best links bring in real traffic to '
              'these old blog articles, you could go and rebuild these blogs exactly as they '
              'were with the same URL slug.',
      'timestamp': 818,
      'timestamp_label': '[00:13:38]',
      'timestamp_seconds': 818,
      'tip': "'t really deliver in terms of the page traffic, but assuming that you were "
             'looking at an expired domain that had the best links bring in real traffic to '
             'these old blog articles, you could go and rebuild these blogs exactly as they '
             'were with the same URL slug.',
      'title': 'How I Find Expired Domains with Backlink Goldmines (and When They’re Worth It) '
               '(Frey Chu)',
      'url': 'https://www.youtube.com/watch?v=mHkLfhpVYqc&t=818s',
      'video_id': 'mHkLfhpVYqc'},
     {'author': 'SirLinksalot',
      'channel': 'SirLinksalot',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:10](https://www.youtube.com/watch?v=lfCYBd5qKMk&t=130s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So uh in regards to like using them for let's say pbn building great option in "
              'regards to using them to try and uh build a new affiliate.',
      'timestamp': 130,
      'timestamp_label': '[00:02:10]',
      'timestamp_seconds': 130,
      'tip': "So uh in regards to like using them for let's say pbn building great option in "
             'regards to using them to try and uh build a new affiliate.',
      'title': 'Rebuild Expired Domains LIKE THIS (SirLinksalot)',
      'url': 'https://www.youtube.com/watch?v=lfCYBd5qKMk&t=130s',
      'video_id': 'lfCYBd5qKMk'},
     {'author': 'She Knows SEO',
      'channel': 'She Knows SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:30](https://www.youtube.com/watch?v=xRuzXK8HIFo&t=450s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'YouTube videos that you embed. I never remember the difference between these '
              'two so I just kind of lump them in together for overall ads um in terms of like '
              'video ads. Uh but you can ask them to explain that more. I did once and I have '
              'forgotten the answer.',
      'timestamp': 450,
      'timestamp_label': '[00:07:30]',
      'timestamp_seconds': 450,
      'tip': 'YouTube videos that you embed. I never remember the difference between these two '
             'so I just kind of lump them in together for overall ads um in terms of like '
             'video ads. Uh but you can ask them to explain that more. I did once and I have '
             'forgotten the answer.',
      'title': 'Raptive Review: BTS of the BEST Ad Network (She Knows SEO)',
      'url': 'https://www.youtube.com/watch?v=xRuzXK8HIFo&t=450s',
      'video_id': 'xRuzXK8HIFo'},
     {'author': 'RustyBrick Barry Schwartz Search Engine Roundtable',
      'channel': 'RustyBrick Barry Schwartz Search Engine Roundtable',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:05](https://www.youtube.com/watch?v=7eYiiLVxrOE&t=425s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Like let's all spam Barry's data. Best looking SEO in the world. Click click "
              'click click click. Well, Google has lost again to SERP API in their scraping '
              "case. So um as we've reported on in the past, the SERP API was being sued by "
              'Google for really a sort of DCMA compliance.',
      'timestamp': 425,
      'timestamp_label': '[00:07:05]',
      'timestamp_seconds': 425,
      'tip': "Like let's all spam Barry's data. Best looking SEO in the world. Click click "
             'click click click. Well, Google has lost again to SERP API in their scraping '
             "case. So um as we've reported on in the past, the SERP API was being sued by "
             'Google for really a sort of DCMA compliance.',
      'title': "It's New 11/11: Google November Core Update Unleashed, ChatGPT Click Insights, "
               'Yahoo Scout, SerpApi (RustyBrick Barry Schwartz Search Engine Roundtable)',
      'url': 'https://www.youtube.com/watch?v=7eYiiLVxrOE&t=425s',
      'video_id': '7eYiiLVxrOE'},
     {'author': 'Brandon Aday',
      'channel': 'Brandon Aday',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=a6WT80_MCZs&t=89s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Invisible to humans. Finally, you need ecosystem agreement. Your core business '
              'details must match perfectly across your website,  Google Business.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': 'Invisible to humans. Finally, you need ecosystem agreement. Your core business '
             'details must match perfectly across your website,  Google Business.',
      'title': 'What is GEO: Generative Engine Optimization Essentials | AI Visibility Academy '
               '(Brandon Aday)',
      'url': 'https://www.youtube.com/watch?v=a6WT80_MCZs&t=89s',
      'video_id': 'a6WT80_MCZs'},
     {'author': 'Casey Botticello',
      'channel': 'Casey Botticello',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:04](https://www.youtube.com/watch?v=uSKcihbY0hs&t=904s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ads and while there were a few bugs uh this is literally their beta and it '
              "works pretty well um it's much easier to set up than the normal media Vine "
              'artive.',
      'timestamp': 904,
      'timestamp_label': '[00:15:04]',
      'timestamp_seconds': 904,
      'tip': 'Ads and while there were a few bugs uh this is literally their beta and it works '
             "pretty well um it's much easier to set up than the normal media Vine artive.",
      'title': 'Mediavine vs. Raptive: A Review of Both Display Ad Networks as a Blogger '
               '(Casey Botticello)',
      'url': 'https://www.youtube.com/watch?v=uSKcihbY0hs&t=904s',
      'video_id': 'uSKcihbY0hs'},
     {'author': 'Niche Pursuits Podcast',
      'channel': 'Niche Pursuits Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:24](https://www.youtube.com/watch?v=0iNy5JybH4I&t=1104s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um Google is doing what they do when they apparently identify site reputation '
              "abuse they don't have an algorithmic solution for it the only thing they can.",
      'timestamp': 1104,
      'timestamp_label': '[00:18:24]',
      'timestamp_seconds': 1104,
      'tip': 'Um Google is doing what they do when they apparently identify site reputation '
             "abuse they don't have an algorithmic solution for it the only thing they can.",
      'title': 'Runaway Parasite SEO! Google Penalizes Forbes! (Niche Pursuits Podcast)',
      'url': 'https://www.youtube.com/watch?v=0iNy5JybH4I&t=1104s',
      'video_id': '0iNy5JybH4I'},
     {'author': 'Semrush Live',
      'channel': 'Semrush Live',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:28](https://www.youtube.com/watch?v=eelEuYoflG0&t=1468s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Doing malicious things you know you can you can think of something internally '
              'that makes the case but all those things can be validated with server log '
              "analysis it's it's you have to have it it has to be always on for most "
              'organizations of any size.',
      'timestamp': 1468,
      'timestamp_label': '[00:24:28]',
      'timestamp_seconds': 1468,
      'tip': 'Doing malicious things you know you can you can think of something internally '
             'that makes the case but all those things can be validated with server log '
             "analysis it's it's you have to have it it has to be always on for most "
             'organizations of any size.',
      'title': 'How to Leverage Insights from Your Site’s Server Logs | 5 Hours of Technical '
               'SEO (Semrush Live)',
      'url': 'https://www.youtube.com/watch?v=eelEuYoflG0&t=1468s',
      'video_id': 'eelEuYoflG0'},
     {'author': 'Koray Tuğberk GÜBÜR',
      'channel': 'Koray Tuğberk GÜBÜR',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:06](https://www.youtube.com/watch?v=WrU25krFCtk&t=366s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Domain terms and you can actually analyze the Google algorithm especially from '
              'visual semantics point of view by providing relevance and responsiveness.',
      'timestamp': 366,
      'timestamp_label': '[00:06:06]',
      'timestamp_seconds': 366,
      'tip': 'Domain terms and you can actually analyze the Google algorithm especially from '
             'visual semantics point of view by providing relevance and responsiveness.',
      'title': 'Topical Authority with 1 Page Exact Match Domain: 8,000 Clicks a Day - Learn '
               'Visual Semantics (Koray Tuğberk GÜBÜR)',
      'url': 'https://www.youtube.com/watch?v=WrU25krFCtk&t=366s',
      'video_id': 'WrU25krFCtk'},
     {'author': 'Carl Broadbent',
      'channel': 'Carl Broadbent',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:34](https://www.youtube.com/watch?v=feVaD3YiPFE&t=994s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Thumbs up if you did leave me comment do you have videos on your side are you '
              'thinking about putting them on do you hate them let me know in the comments '
              "below and I'll try and get to answering all the questions you leave so thanks "
              'again see you in the next video.',
      'timestamp': 994,
      'timestamp_label': '[00:16:34]',
      'timestamp_seconds': 994,
      'tip': 'Thumbs up if you did leave me comment do you have videos on your side are you '
             'thinking about putting them on do you hate them let me know in the comments '
             "below and I'll try and get to answering all the questions you leave so thanks "
             'again see you in the next video.',
      'title': 'See MY EARNINGS FROM VIDEO display ads with MEDIAVINE (Carl Broadbent)',
      'url': 'https://www.youtube.com/watch?v=feVaD3YiPFE&t=994s',
      'video_id': 'feVaD3YiPFE'},
     {'author': 'James Taylor SEO',
      'channel': 'James Taylor SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:13](https://www.youtube.com/watch?v=JKWFZj_AF8o&t=613s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um I'll send you an email with some free resources and I'll just be updating "
              'that sheet as and when I make new ones so yeah make sure you check it out I '
              "hope this was helpful uh any comments let me know and I'll see you in the next "
              'video.',
      'timestamp': 613,
      'timestamp_label': '[00:10:13]',
      'timestamp_seconds': 613,
      'tip': "Um I'll send you an email with some free resources and I'll just be updating "
             'that sheet as and when I make new ones so yeah make sure you check it out I hope '
             "this was helpful uh any comments let me know and I'll see you in the next video.",
      'title': 'How To Build Backlinks With Digital PR (The First Strategies To Try!) (James '
               'Taylor SEO)',
      'url': 'https://www.youtube.com/watch?v=JKWFZj_AF8o&t=613s',
      'video_id': 'JKWFZj_AF8o'},
     {'author': 'Koray Tuğberk GÜBÜR',
      'channel': 'Koray Tuğberk GÜBÜR',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:32](https://www.youtube.com/watch?v=D7P6-b1XtxE&t=152s)',
      'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                   'programmatic & topical-authority SEO, GEO citation capture, and media '
                   'exits (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And especially co- occurrence around that mention. And the last part is the '
              'claim. The claim again is like the biggest law firm or the most successful.',
      'timestamp': 152,
      'timestamp_label': '[00:02:32]',
      'timestamp_seconds': 152,
      'tip': 'And especially co- occurrence around that mention. And the last part is the '
             'claim. The claim again is like the biggest law firm or the most successful.',
      'title': 'How to Get Cited by AI: External Topical Maps Explained (Koray Tuğberk GÜBÜR)',
      'url': 'https://www.youtube.com/watch?v=D7P6-b1XtxE&t=152s',
      'video_id': 'D7P6-b1XtxE'}],
 10: [{'author': 'the digitalemania',
       'channel': 'the digitalemania',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:20](https://www.youtube.com/watch?v=ufTFZFvsEIM&t=80s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The system also supports internal link preparation, helping connect relevant '
               'articles and pages within your website. Next, create a suitable image using '
               'the guided image prompt, or we can use automation if paid API is used, and '
               'upload it to the article.',
       'timestamp': 80,
       'timestamp_label': '[00:01:20]',
       'timestamp_seconds': 80,
       'tip': 'The system also supports internal link preparation, helping connect relevant '
              'articles and pages within your website. Next, create a suitable image using the '
              'guided image prompt, or we can use automation if paid API is used, and upload '
              'it to the article.',
       'title': 'How to Create SEO Blog Posts with AI & Publish to WordPress? | Real Estate '
                'Website Demo 2026 (the digitalemania)',
       'url': 'https://www.youtube.com/watch?v=ufTFZFvsEIM&t=80s',
       'video_id': 'ufTFZFvsEIM'},
      {'author': 'brightonSEO',
       'channel': 'brightonSEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:21](https://www.youtube.com/watch?v=Q9Nkmc8Cx6I&t=801s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Um, Google does really well though with heavy pages. Um, they just will slow '
               "their rate of crawl, but the AI bots, remember, they're trying to catch up to "
               "Google at rapid speed. So, they don't have the budget. They're not rendering "
               'JavaScript.',
       'timestamp': 801,
       'timestamp_label': '[00:13:21]',
       'timestamp_seconds': 801,
       'tip': 'Um, Google does really well though with heavy pages. Um, they just will slow '
              "their rate of crawl, but the AI bots, remember, they're trying to catch up to "
              "Google at rapid speed. So, they don't have the budget. They're not rendering "
              'JavaScript.',
       'title': "Log Files Don't Lie: A 30-Day Crawl Analysis That Changed How We Prioritize "
                'Technical SEO (brightonSEO)',
       'url': 'https://www.youtube.com/watch?v=Q9Nkmc8Cx6I&t=801s',
       'video_id': 'Q9Nkmc8Cx6I'},
      {'author': 'Lorraine Pawell - SEO AEO & Content Strategy',
       'channel': 'Lorraine Pawell - SEO AEO & Content Strategy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:18](https://www.youtube.com/watch?v=HYZv8hDMBvw&t=318s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "But it fails when you're just spinning pages with AI swapping out city names "
               "or products as you there's no unique content or insight. You don't have "
               'topical authority or backlinks to support it. If your strategy is copy paste '
               "with keywords, don't bother.",
       'timestamp': 318,
       'timestamp_label': '[00:05:18]',
       'timestamp_seconds': 318,
       'tip': "But it fails when you're just spinning pages with AI swapping out city names or "
              "products as you there's no unique content or insight. You don't have topical "
              'authority or backlinks to support it. If your strategy is copy paste with '
              "keywords, don't bother.",
       'title': 'Most Programmatic SEO Fails in 2026 — Here’s How to Make It Work (Lorraine '
                'Pawell - SEO AEO & Content Strategy)',
       'url': 'https://www.youtube.com/watch?v=HYZv8hDMBvw&t=318s',
       'video_id': 'HYZv8hDMBvw'},
      {'author': "Vasco's SEO Tips",
       'channel': "Vasco's SEO Tips",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=voMel_srl_w&t=20s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I want to show you step-by-step how you can leverage this AI tech to actually '
               'build high-quality backlinks that if you build them to your site, you get '
               'higher rankings, that is you get more traffic, that is you can make more money '
               'with your products or services.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'I want to show you step-by-step how you can leverage this AI tech to actually '
              'build high-quality backlinks that if you build them to your site, you get '
              'higher rankings, that is you get more traffic, that is you can make more money '
              'with your products or services.',
       'title': 'How I Build Unlimited FREE Backlinks with AI (to rank #1 on Google and get '
                "more traffic) (Vasco's SEO Tips)",
       'url': 'https://www.youtube.com/watch?v=voMel_srl_w&t=20s',
       'video_id': 'voMel_srl_w'},
      {'author': 'ClickMinded',
       'channel': 'ClickMinded',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:28](https://www.youtube.com/watch?v=YN8hU1e3d-0&t=88s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, to accomplish this today, we're going to be using the Clickminded project "
               'agent. The Clickminded project agent is essentially a centralized place where '
               'all the information about the business lives.',
       'timestamp': 88,
       'timestamp_label': '[00:01:28]',
       'timestamp_seconds': 88,
       'tip': "So, to accomplish this today, we're going to be using the Clickminded project "
              'agent. The Clickminded project agent is essentially a centralized place where '
              'all the information about the business lives.',
       'title': '🔗 How I Boost Rankings With AI-Powered Internal Linking for SEO (in Under 5 '
                'Minutes) (ClickMinded)',
       'url': 'https://www.youtube.com/watch?v=YN8hU1e3d-0&t=88s',
       'video_id': 'YN8hU1e3d-0'},
      {'author': 'AeroIDX',
       'channel': 'AeroIDX',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:30](https://www.youtube.com/watch?v=6etBe1gPZqE&t=30s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Using content only you could write. Add a frequently asked question on every '
               'page. And add live listings plus a lead capture form. Most agent websites have '
               "only one search page. But people don't search homes for sale. They search for "
               'specific things.',
       'timestamp': 30,
       'timestamp_label': '[00:00:30]',
       'timestamp_seconds': 30,
       'tip': 'Using content only you could write. Add a frequently asked question on every '
              'page. And add live listings plus a lead capture form. Most agent websites have '
              "only one search page. But people don't search homes for sale. They search for "
              'specific things.',
       'title': '5 SEO Tips to Rank Your Real Estate Website (Real Example) - AeroIDX '
                '(AeroIDX)',
       'url': 'https://www.youtube.com/watch?v=6etBe1gPZqE&t=30s',
       'video_id': '6etBe1gPZqE'},
      {'author': 'Contentbase',
       'channel': 'Contentbase',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:32](https://www.youtube.com/watch?v=mlckmJy3BwY&t=152s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Strategy that can drive significant organic traffic exactly it's about "
               'leveraging data and automation to create high quality content at scale very '
               'efficient that was a great discussion thanks for sharing your insights I '
               'learned a lot.',
       'timestamp': 152,
       'timestamp_label': '[00:02:32]',
       'timestamp_seconds': 152,
       'tip': "Strategy that can drive significant organic traffic exactly it's about "
              'leveraging data and automation to create high quality content at scale very '
              'efficient that was a great discussion thanks for sharing your insights I '
              'learned a lot.',
       'title': 'Programmatic SEO Case Study - Nomad List (Contentbase)',
       'url': 'https://www.youtube.com/watch?v=mlckmJy3BwY&t=152s',
       'video_id': 'mlckmJy3BwY'},
      {'author': 'True SEO',
       'channel': 'True SEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:28](https://www.youtube.com/watch?v=y6yAJ9Ocl3U&t=148s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So judge Google by what it rewards, not what it says. So what did the last '
               "update reward? We asked Google's AI again. Firsthand experience, new "
               "information, not summaries of what's already out there, and less shallow AI "
               'content built at scale to game search.',
       'timestamp': 148,
       'timestamp_label': '[00:02:28]',
       'timestamp_seconds': 148,
       'tip': 'So judge Google by what it rewards, not what it says. So what did the last '
              "update reward? We asked Google's AI again. Firsthand experience, new "
              "information, not summaries of what's already out there, and less shallow AI "
              'content built at scale to game search.',
       'title': 'Google Core Update Explained (November 2026): What Google Really Rewards and '
                '8 SEO Fixes (True SEO)',
       'url': 'https://www.youtube.com/watch?v=y6yAJ9Ocl3U&t=148s',
       'video_id': 'y6yAJ9Ocl3U'},
      {'author': 'Alex Moreau | AI for Ads & SEO-GEO',
       'channel': 'Alex Moreau | AI for Ads & SEO-GEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:57](https://www.youtube.com/watch?v=Oq7qV4_5W-A&t=57s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '8% of visits with an AI summary, and 15 without. The way out is one agent that '
               "sees your SEO and AI visibility together. You'll watch one work in a candle "
               "store's workspace while we build a checklist of the key principles of GEO.",
       'timestamp': 57,
       'timestamp_label': '[00:00:57]',
       'timestamp_seconds': 57,
       'tip': '8% of visits with an AI summary, and 15 without. The way out is one agent that '
              "sees your SEO and AI visibility together. You'll watch one work in a candle "
              "store's workspace while we build a checklist of the key principles of GEO.",
       'title': 'What Is GEO? Generative Engine Optimization Explained (2026): 5 Key '
                'Principles (Alex Moreau | AI for Ads & SEO-GEO)',
       'url': 'https://www.youtube.com/watch?v=Oq7qV4_5W-A&t=57s',
       'video_id': 'Oq7qV4_5W-A'},
      {'author': 'Contentbase',
       'channel': 'Contentbase',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:50](https://www.youtube.com/watch?v=QG0qwLG-SBk&t=170s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Cley's programmatic SEO strategy is a master class in efficiency and scale "
               "it's a testament to the power of Automation and targeted content thanks for "
               'breaking it it all down for us this is a great discussion yeah thanks for '
               'being here.',
       'timestamp': 170,
       'timestamp_label': '[00:02:50]',
       'timestamp_seconds': 170,
       'tip': "Cley's programmatic SEO strategy is a master class in efficiency and scale it's "
              'a testament to the power of Automation and targeted content thanks for breaking '
              'it it all down for us this is a great discussion yeah thanks for being here.',
       'title': 'Programmatic SEO Case Study - Calendly (Contentbase)',
       'url': 'https://www.youtube.com/watch?v=QG0qwLG-SBk&t=170s',
       'video_id': 'QG0qwLG-SBk'},
      {'author': 'Hamida - Programmatic SEO Agency',
       'channel': 'Hamida - Programmatic SEO Agency',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:39](https://www.youtube.com/watch?v=FO1ASxHYnhE&t=219s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Available and the next thing to do is to create their content template for '
               "this example we'll be using the generate press element so we create new "
               'element as a block type and then start designing our content.',
       'timestamp': 219,
       'timestamp_label': '[00:03:39]',
       'timestamp_seconds': 219,
       'tip': 'Available and the next thing to do is to create their content template for this '
              "example we'll be using the generate press element so we create new element as a "
              'block type and then start designing our content.',
       'title': 'How to Create a Programmatic SEO Website for Real Estate Using WordPress '
                '(Hamida - Programmatic SEO Agency)',
       'url': 'https://www.youtube.com/watch?v=FO1ASxHYnhE&t=219s',
       'video_id': 'FO1ASxHYnhE'},
      {'author': 'Julian Goldie SEO',
       'channel': 'Julian Goldie SEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:27](https://www.youtube.com/watch?v=s_GIhK4WE18&t=147s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Created for people notice how bi people has been removed which is pretty crazy '
               'very interesting to me that signals AI content is actually more accepted now.',
       'timestamp': 147,
       'timestamp_label': '[00:02:27]',
       'timestamp_seconds': 147,
       'tip': 'Created for people notice how bi people has been removed which is pretty crazy '
              'very interesting to me that signals AI content is actually more accepted now.',
       'title': "Google Helpful Content Update 2024: I Wasn't Prepared for This!😮 (Julian "
                'Goldie SEO)',
       'url': 'https://www.youtube.com/watch?v=s_GIhK4WE18&t=147s',
       'video_id': 's_GIhK4WE18'},
      {'author': 'Unique Web School',
       'channel': 'Unique Web School',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:34](https://www.youtube.com/watch?v=3G4gPPFTYrM&t=154s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Google में क्लिक कर देता हूं। और यहां से मैं Google के अंदर लॉगिन कर लेता हूं। '
               'यहां से हम लोग ईमेल को सेलेक्ट करते हैं। कंटिन्यू बटन में क्लिक करते हैं। और '
               'हमारा जो अकाउंट है वह यहां पर क्रिएट हो चुका है। आप लोग यहां पर देख सकते हो। '
               'ठीक है?',
       'timestamp': 154,
       'timestamp_label': '[00:02:34]',
       'timestamp_seconds': 154,
       'tip': 'Google में क्लिक कर देता हूं। और यहां से मैं Google के अंदर लॉगिन कर लेता हूं। '
              'यहां से हम लोग ईमेल को सेलेक्ट करते हैं। कंटिन्यू बटन में क्लिक करते हैं। और '
              'हमारा जो अकाउंट है वह यहां पर क्रिएट हो चुका है। आप लोग यहां पर देख सकते हो। '
              'ठीक है?',
       'title': 'How to Create an SEO Portfolio Website Using AI | No Coding Required (Unique '
                'Web School)',
       'url': 'https://www.youtube.com/watch?v=3G4gPPFTYrM&t=154s',
       'video_id': '3G4gPPFTYrM'},
      {'author': '24siteshop – Website Design Agency',
       'channel': '24siteshop – Website Design Agency',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=NIRbajvpihU&t=15s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'रियलस्टेट एजेंट का वेबसाइट है। ठीक है? यहां पे आप देख सकते हो। तो, यहां पे '
               'प्रोफेशनल लाइक रियलस्टेट एजेंट है। यहां पे आपका गोरेगांव ईस्ट पे आपका ये '
               'लोकेटेड.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'रियलस्टेट एजेंट का वेबसाइट है। ठीक है? यहां पे आप देख सकते हो। तो, यहां पे '
              'प्रोफेशनल लाइक रियलस्टेट एजेंट है। यहां पे आपका गोरेगांव ईस्ट पे आपका ये '
              'लोकेटेड.',
       'title': 'We’ve Just Completed This Real Estate Agent Portfolio Website for a Client | '
                'Real Estate Agent Site (24siteshop – Website Design Agency)',
       'url': 'https://www.youtube.com/watch?v=NIRbajvpihU&t=15s',
       'video_id': 'NIRbajvpihU'},
      {'author': 'Contentbase',
       'channel': 'Contentbase',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:02](https://www.youtube.com/watch?v=1uDcX4xnqpU&t=182s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Takeaway here is that programmatic SEO when done right can generate massive '
               "organic traffic it's about combining smart keyword research with automated "
               'content creation to meet user needs effectively that was a great discussion '
               'thanks for sharing your insights.',
       'timestamp': 182,
       'timestamp_label': '[00:03:02]',
       'timestamp_seconds': 182,
       'tip': 'Takeaway here is that programmatic SEO when done right can generate massive '
              "organic traffic it's about combining smart keyword research with automated "
              'content creation to meet user needs effectively that was a great discussion '
              'thanks for sharing your insights.',
       'title': 'Programmatic SEO Case Study - Canva (Contentbase)',
       'url': 'https://www.youtube.com/watch?v=1uDcX4xnqpU&t=182s',
       'video_id': '1uDcX4xnqpU'}],
 11: [{'author': 'Ippei - Rank and Rent SEO',
       'channel': 'Ippei - Rank and Rent SEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:58](https://www.youtube.com/watch?v=uJ0bhk9MeDE&t=1078s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "11 years I've dabbled with bunch of different things like affiliate marketing "
               "or e-commerce in 2025 and this year in 2026, I've tripled down on this digital "
               'real estate business and I built 150 sites and I plan on building another 100 '
               'more sites as well.',
       'timestamp': 1078,
       'timestamp_label': '[00:17:58]',
       'timestamp_seconds': 1078,
       'tip': "11 years I've dabbled with bunch of different things like affiliate marketing "
              "or e-commerce in 2025 and this year in 2026, I've tripled down on this digital "
              'real estate business and I built 150 sites and I plan on building another 100 '
              'more sites as well.',
       'title': 'Best Digital Real Estate Investing Business for Beginners (How I made passive '
                'income for 11 Years) (Ippei - Rank and Rent SEO)',
       'url': 'https://www.youtube.com/watch?v=uJ0bhk9MeDE&t=1078s',
       'video_id': 'uJ0bhk9MeDE'},
      {'author': 'B2BSEOio',
       'channel': 'B2BSEOio',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=uI61LP8Ue30&t=20s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Your Money Your Life category and we had to build some authority, but to be '
               'honest, the on-page SEO part was handled by their in-house team, so we just '
               'was responsible for the off-page SEO, the link building part.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'Your Money Your Life category and we had to build some authority, but to be '
              'honest, the on-page SEO part was handled by their in-house team, so we just was '
              'responsible for the off-page SEO, the link building part.',
       'title': 'A Programmatic SEO Case Study: What Went Wrong for a Healthcare Brand '
                '(B2BSEOio)',
       'url': 'https://www.youtube.com/watch?v=uI61LP8Ue30&t=20s',
       'video_id': 'uI61LP8Ue30'},
      {'author': 'Google Search Central',
       'channel': 'Google Search Central',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:35](https://www.youtube.com/watch?v=LIMqmzuzpVg&t=515s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I think it comes from the fact that a few large-scale websites do have '
               'articles and blog posts where they talk about crawl budget being a thing. It '
               "is being discussed in SEO training courses, as far as I've seen. It's being "
               'discussed at conferences.',
       'timestamp': 515,
       'timestamp_label': '[00:08:35]',
       'timestamp_seconds': 515,
       'tip': 'I think it comes from the fact that a few large-scale websites do have articles '
              'and blog posts where they talk about crawl budget being a thing. It is being '
              "discussed in SEO training courses, as far as I've seen. It's being discussed at "
              'conferences.',
       'title': 'Should I worry about crawl budget? | Search Off the Record (Google Search '
                'Central)',
       'url': 'https://www.youtube.com/watch?v=LIMqmzuzpVg&t=515s',
       'video_id': 'LIMqmzuzpVg'},
      {'author': 'Pavel Klimakov',
       'channel': 'Pavel Klimakov',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:21:26](https://www.youtube.com/watch?v=9RNJrGhH7ek&t=1286s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Right and I assume if you have a salesperson</b> <b>in the team or the actual '
               'manager,</b> <b>they can probably consult you and give you these points. '
               "What's the actual user journey? Yeah, we always also ask can you give us a</b> "
               '<b>kinds of brochure about your company.',
       'timestamp': 1286,
       'timestamp_label': '[00:21:26]',
       'timestamp_seconds': 1286,
       'tip': 'Right and I assume if you have a salesperson</b> <b>in the team or the actual '
              "manager,</b> <b>they can probably consult you and give you these points. What's "
              'the actual user journey? Yeah, we always also ask can you give us a</b> '
              '<b>kinds of brochure about your company.',
       'title': 'Topical Authority With Koray Tuğberk GÜBÜR (Pavel Klimakov)',
       'url': 'https://www.youtube.com/watch?v=9RNJrGhH7ek&t=1286s',
       'video_id': '9RNJrGhH7ek'},
      {'author': 'Vitaliy Gershfeld',
       'channel': 'Vitaliy Gershfeld',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:22](https://www.youtube.com/watch?v=NwV-eO-VZe8&t=22s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Affiliate marketing is certainly a popular option. Selling your own products, '
               'services, courses is also another option, collecting an email list, but '
               "there's also the option of display ads, where you basically connect with "
               'companies that put ads on your website.',
       'timestamp': 22,
       'timestamp_label': '[00:00:22]',
       'timestamp_seconds': 22,
       'tip': 'Affiliate marketing is certainly a popular option. Selling your own products, '
              "services, courses is also another option, collecting an email list, but there's "
              'also the option of display ads, where you basically connect with companies that '
              'put ads on your website.',
       'title': 'How Much Money Can RPM ACTUALLY Make You? (Mediavine Explained) (Vitaliy '
                'Gershfeld)',
       'url': 'https://www.youtube.com/watch?v=NwV-eO-VZe8&t=22s',
       'video_id': 'NwV-eO-VZe8'},
      {'author': 'Semrush',
       'channel': 'Semrush',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:13](https://www.youtube.com/watch?v=vnkjR9TE9Ok&t=313s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "URL are updated to the new URL. Next off, since we're talking about links, "
               "let's also not forget to audit the external ones from your site. When you link "
               'to external sites, you give your authority away.',
       'timestamp': 313,
       'timestamp_label': '[00:05:13]',
       'timestamp_seconds': 313,
       'tip': "URL are updated to the new URL. Next off, since we're talking about links, "
              "let's also not forget to audit the external ones from your site. When you link "
              'to external sites, you give your authority away.',
       'title': 'Internal Linking Strategy: How to Set it Up (Semrush)',
       'url': 'https://www.youtube.com/watch?v=vnkjR9TE9Ok&t=313s',
       'video_id': 'vnkjR9TE9Ok'},
      {'author': 'Edward Sturm',
       'channel': 'Edward Sturm',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:02](https://www.youtube.com/watch?v=mKy9_UCPEVM&t=362s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "You don't need a backlink to generate authority. You can have a page that "
               'ranks for an easy keyword and that is generating authority. And now you can '
               'take that authority and channel some of it to other pages on your site that '
               'you want to rank.',
       'timestamp': 362,
       'timestamp_label': '[00:06:02]',
       'timestamp_seconds': 362,
       'tip': "You don't need a backlink to generate authority. You can have a page that ranks "
              'for an easy keyword and that is generating authority. And now you can take that '
              'authority and channel some of it to other pages on your site that you want to '
              'rank.',
       'title': 'The First Rule of Internal Linking (That Most SEOs Ignore) (Edward Sturm)',
       'url': 'https://www.youtube.com/watch?v=mKy9_UCPEVM&t=362s',
       'video_id': 'mKy9_UCPEVM'},
      {'author': 'Brendan Hufford',
       'channel': 'Brendan Hufford',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:20](https://www.youtube.com/watch?v=zSyoobG9KTY&t=320s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So for example, here's an article that I'm starting to build out, and starting "
               'to make a lot stronger. Before it was just a documentary about me building my '
               'Jujitsu eCommerce brand.',
       'timestamp': 320,
       'timestamp_label': '[00:05:20]',
       'timestamp_seconds': 320,
       'tip': "So for example, here's an article that I'm starting to build out, and starting "
              'to make a lot stronger. Before it was just a documentary about me building my '
              'Jujitsu eCommerce brand.',
       'title': 'Creating Website Architecture for SEO (2023) (Brendan Hufford)',
       'url': 'https://www.youtube.com/watch?v=zSyoobG9KTY&t=320s',
       'video_id': 'zSyoobG9KTY'},
      {'author': 'Surfside PPC',
       'channel': 'Surfside PPC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:19:29](https://www.youtube.com/watch?v=0_SAQbGnl3Y&t=1169s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'E-commerce over affil pure affiliate websites now and you know not many things '
               "that we can do if if Google's decided to Blacklist our websites.",
       'timestamp': 1169,
       'timestamp_label': '[00:19:29]',
       'timestamp_seconds': 1169,
       'tip': 'E-commerce over affil pure affiliate websites now and you know not many things '
              "that we can do if if Google's decided to Blacklist our websites.",
       'title': 'Helpful Content Update 1 Year Later and Google Core Updates Impacting SEO '
                '(Surfside PPC)',
       'url': 'https://www.youtube.com/watch?v=0_SAQbGnl3Y&t=1169s',
       'video_id': '0_SAQbGnl3Y'},
      {'author': 'Robbie Richards',
       'channel': 'Robbie Richards',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=P5ET0IvFReQ&t=15s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'To show you the new clustering tool inside the semrush keyword manager and how '
               'you can use that to Cluster existing keyword sets but also create keyword.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'To show you the new clustering tool inside the semrush keyword manager and how '
              'you can use that to Cluster existing keyword sets but also create keyword.',
       'title': 'How to Create Keyword Clusters With Semrush (New Feature) (Robbie Richards)',
       'url': 'https://www.youtube.com/watch?v=P5ET0IvFReQ&t=15s',
       'video_id': 'P5ET0IvFReQ'},
      {'author': 'RustyBrick Barry Schwartz Search Engine Roundtable',
       'channel': 'RustyBrick Barry Schwartz Search Engine Roundtable',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:10](https://www.youtube.com/watch?v=GBh1xJ3iSws&t=490s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'They removed the whole article Too Short um errors for news articles saying '
               "there's no such thing as an article Too Short anymore it used to have a word.",
       'timestamp': 490,
       'timestamp_label': '[00:08:10]',
       'timestamp_seconds': 490,
       'tip': 'They removed the whole article Too Short um errors for news articles saying '
              "there's no such thing as an article Too Short anymore it used to have a word.",
       'title': 'Google September Core Update, Helpful Content Update Done & Possible Local '
                'Search Ranking Update (RustyBrick Barry Schwartz Search Engine Roundtable)',
       'url': 'https://www.youtube.com/watch?v=GBh1xJ3iSws&t=490s',
       'video_id': 'GBh1xJ3iSws'},
      {'author': 'Contentbase',
       'channel': 'Contentbase',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:12](https://www.youtube.com/watch?v=yI2G7YcivYQ&t=192s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Power of programmatic SEO when done right it's a smart efficient way to build "
               "a substantial online presence absolutely it's a game Cher for businesses "
               'looking to scale their content creation that was a great discussion thanks for '
               'being here.',
       'timestamp': 192,
       'timestamp_label': '[00:03:12]',
       'timestamp_seconds': 192,
       'tip': "Power of programmatic SEO when done right it's a smart efficient way to build a "
              "substantial online presence absolutely it's a game Cher for businesses looking "
              'to scale their content creation that was a great discussion thanks for being '
              'here.',
       'title': 'Programmatic SEO Case Study - Failory (Contentbase)',
       'url': 'https://www.youtube.com/watch?v=yI2G7YcivYQ&t=192s',
       'video_id': 'yI2G7YcivYQ'},
      {'author': 'Umar Tazkeer',
       'channel': 'Umar Tazkeer',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=CT-KwgPNkHI&t=15s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'हैं बट हेल्प बैकिंग स्ट्रैटजी सीधा सा मतलब हेल्थ रिपोर्टर आउट अगर मैं है रोकें '
               'फुल फॉर्म की बात करूं तो यह बैकिंग स्ट्रैटजी क्या है और कहां से हमको.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'हैं बट हेल्प बैकिंग स्ट्रैटजी सीधा सा मतलब हेल्थ रिपोर्टर आउट अगर मैं है रोकें '
              'फुल फॉर्म की बात करूं तो यह बैकिंग स्ट्रैटजी क्या है और कहां से हमको.',
       'title': 'How to Create HARO - Help a Reporter Out Backlink | SEO Course | #68 (Umar '
                'Tazkeer)',
       'url': 'https://www.youtube.com/watch?v=CT-KwgPNkHI&t=15s',
       'video_id': 'CT-KwgPNkHI'},
      {'author': 'The Blueprint Training',
       'channel': 'The Blueprint Training',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:52](https://www.youtube.com/watch?v=wdldIiHzAcs&t=352s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Conversations guys this is what this is all about hey Ryan here hope you '
               'likeed that video if you want more check out these two videos right here on '
               'the screen right.',
       'timestamp': 352,
       'timestamp_label': '[00:05:52]',
       'timestamp_seconds': 352,
       'tip': 'Conversations guys this is what this is all about hey Ryan here hope you likeed '
              'that video if you want more check out these two videos right here on the screen '
              'right.',
       'title': 'SEO For Real Estate Agents in 2025 (The Blueprint Training)',
       'url': 'https://www.youtube.com/watch?v=wdldIiHzAcs&t=352s',
       'video_id': 'wdldIiHzAcs'},
      {'author': 'Consumer Reviews',
       'channel': 'Consumer Reviews',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:16](https://www.youtube.com/watch?v=Q0qBq0V4xC4&t=196s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '200 a month and adds historical data, content marketing tools, and support for '
               '15 projects. Then you got the business plan, which comes in more like 415,420 '
               'per month. And that adds API access, and team collaboration features.',
       'timestamp': 196,
       'timestamp_label': '[00:03:16]',
       'timestamp_seconds': 196,
       'tip': '200 a month and adds historical data, content marketing tools, and support for '
              '15 projects. Then you got the business plan, which comes in more like 415,420 '
              'per month. And that adds API access, and team collaboration features.',
       'title': "Semrush vs Ahrefs: I Used Both – Here's What You Need to Know (Consumer "
                'Reviews)',
       'url': 'https://www.youtube.com/watch?v=Q0qBq0V4xC4&t=196s',
       'video_id': 'Q0qBq0V4xC4'}],
 12: [{'author': 'Affiliate Credo',
       'channel': 'Affiliate Credo',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:08](https://www.youtube.com/watch?v=aQH5Bmsfr3A&t=188s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'This guide will help you to start this business Website Authority as the Key '
               'to Successful Rankings in 2022 At the same time, domains with 500 authority '
               'backlinks can bypass other sites with 800 or even 3000 backlinks.',
       'timestamp': 188,
       'timestamp_label': '[00:03:08]',
       'timestamp_seconds': 188,
       'tip': 'This guide will help you to start this business Website Authority as the Key to '
              'Successful Rankings in 2022 At the same time, domains with 500 authority '
              'backlinks can bypass other sites with 800 or even 3000 backlinks.',
       'title': 'Expired Domain SEO Case Study. Top Rankings for Thousands of Keywords '
                '(Affiliate Credo)',
       'url': 'https://www.youtube.com/watch?v=aQH5Bmsfr3A&t=188s',
       'video_id': 'aQH5Bmsfr3A'},
      {'author': 'Outgrow',
       'channel': 'Outgrow',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:02](https://www.youtube.com/watch?v=KfYMGwuZlKU&t=62s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Each question should move the user closer to a personalized result. Here are '
               'some examples to get you started. Which lifestyle change are you considering? '
               'How many cigarettes do you smoke per day? How many days per week do you plan '
               'to exercise?',
       'timestamp': 62,
       'timestamp_label': '[00:01:02]',
       'timestamp_seconds': 62,
       'tip': 'Each question should move the user closer to a personalized result. Here are '
              'some examples to get you started. Which lifestyle change are you considering? '
              'How many cigarettes do you smoke per day? How many days per week do you plan to '
              'exercise?',
       'title': 'Stop Writing Blogs. Build This Instead: Interactive Calculators for SEO '
                '(Outgrow)',
       'url': 'https://www.youtube.com/watch?v=KfYMGwuZlKU&t=62s',
       'video_id': 'KfYMGwuZlKU'},
      {'author': 'Hyper-Niche Affiliate Directories & AI Tools',
       'channel': 'Hyper-Niche Affiliate Directories & AI Tools',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:12](https://www.youtube.com/watch?v=oGsNm_jrtyw&t=312s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Anyhow, I hope this video is helpful and go there and, just if you pick a '
               "topic, just do a few every every day or every week and if you're with your "
               "consistency, you'll see how effective this strategy is for building your niche "
               'directory sites.',
       'timestamp': 312,
       'timestamp_label': '[00:05:12]',
       'timestamp_seconds': 312,
       'tip': 'Anyhow, I hope this video is helpful and go there and, just if you pick a '
              "topic, just do a few every every day or every week and if you're with your "
              "consistency, you'll see how effective this strategy is for building your niche "
              'directory sites.',
       'title': 'Build a $1750 per Month Local Directory Without Google Maps Hassles! '
                '(Hyper-Niche Affiliate Directories & AI Tools)',
       'url': 'https://www.youtube.com/watch?v=oGsNm_jrtyw&t=312s',
       'video_id': 'oGsNm_jrtyw'},
      {'author': 'MostDomain',
       'channel': 'MostDomain',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:23](https://www.youtube.com/watch?v=XdcIcYkuhCc&t=443s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So to recap, here are the four ways expired domains can boost your SEO. One, '
               'they give you instant SEO momentum. Two, you can inherit highquality '
               'backlinks. Three, it can redirect authority to your main site. Four, you can '
               'rebuild them as spool projects with a head start.',
       'timestamp': 443,
       'timestamp_label': '[00:07:23]',
       'timestamp_seconds': 443,
       'tip': 'So to recap, here are the four ways expired domains can boost your SEO. One, '
              'they give you instant SEO momentum. Two, you can inherit highquality backlinks. '
              'Three, it can redirect authority to your main site. Four, you can rebuild them '
              'as spool projects with a head start.',
       'title': 'What is an Expired Domain? And 4 Ways It Can Boost Your SEO (MostDomain)',
       'url': 'https://www.youtube.com/watch?v=XdcIcYkuhCc&t=443s',
       'video_id': 'XdcIcYkuhCc'},
      {'author': 'Edward Sturm',
       'channel': 'Edward Sturm',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:32](https://www.youtube.com/watch?v=kroDk8LuKtY&t=812s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But again, slight volatility is completely normal and you should keep '
               'building. I shared this on X a couple days ago. If you are getting some '
               'branded searches, please, for the love of God, put up two bottom ofunnel SEO '
               'landing pages each week.',
       'timestamp': 812,
       'timestamp_label': '[00:13:32]',
       'timestamp_seconds': 812,
       'tip': 'But again, slight volatility is completely normal and you should keep building. '
              'I shared this on X a couple days ago. If you are getting some branded searches, '
              'please, for the love of God, put up two bottom ofunnel SEO landing pages each '
              'week.',
       'title': 'Google’s November Core Update Is Crushing AI Content Sites (Edward Sturm)',
       'url': 'https://www.youtube.com/watch?v=kroDk8LuKtY&t=812s',
       'video_id': 'kroDk8LuKtY'},
      {'author': 'James Dooley',
       'channel': 'James Dooley',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:43](https://www.youtube.com/watch?v=cv7lfh1AjZc&t=283s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "If you've only got 28 days is a start and we can look at it. 500 errors that "
               "would be quick to jump out. But also then in the logs while we're talking "
               'about logs, things like stop wasting crawl budget.',
       'timestamp': 283,
       'timestamp_label': '[00:04:43]',
       'timestamp_seconds': 283,
       'tip': "If you've only got 28 days is a start and we can look at it. 500 errors that "
              "would be quick to jump out. But also then in the logs while we're talking about "
              'logs, things like stop wasting crawl budget.',
       'title': 'Importance of growing crawl budget (James Dooley Interviews Andrew Halliday) '
                '(James Dooley)',
       'url': 'https://www.youtube.com/watch?v=cv7lfh1AjZc&t=283s',
       'video_id': 'cv7lfh1AjZc'},
      {'author': 'Google Search Central',
       'channel': 'Google Search Central',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:02](https://www.youtube.com/watch?v=x_GoMrl6_u0&t=422s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Dig deeper into the error and fix it. If Google found at least one error on '
               'your site in the last 90 days, but it occurred more than a week ago, you will '
               'see a warning that you had problems in the past.',
       'timestamp': 422,
       'timestamp_label': '[00:07:02]',
       'timestamp_seconds': 422,
       'tip': 'Dig deeper into the error and fix it. If Google found at least one error on '
              'your site in the last 90 days, but it occurred more than a week ago, you will '
              'see a warning that you had problems in the past.',
       'title': 'Crawl Budget and the Crawl Stats report - Google Search Console Training '
                '(Google Search Central)',
       'url': 'https://www.youtube.com/watch?v=x_GoMrl6_u0&t=422s',
       'video_id': 'x_GoMrl6_u0'},
      {'author': 'Emmanuel Lao',
       'channel': 'Emmanuel Lao',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:20](https://www.youtube.com/watch?v=yTNs1XDHQIk&t=320s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Because at the end of the day in order for you to really start playing this '
               "game the barrier for entry is about a hundred posts by the way I'm saying "
               'this.',
       'timestamp': 320,
       'timestamp_label': '[00:05:20]',
       'timestamp_seconds': 320,
       'tip': 'Because at the end of the day in order for you to really start playing this '
              "game the barrier for entry is about a hundred posts by the way I'm saying this.",
       'title': 'Real Estate SEO Made Simple: A Step-by-Step Framework for Success (Emmanuel '
                'Lao)',
       'url': 'https://www.youtube.com/watch?v=yTNs1XDHQIk&t=320s',
       'video_id': 'yTNs1XDHQIk'},
      {'author': 'She Knows SEO',
       'channel': 'She Knows SEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:21](https://www.youtube.com/watch?v=dL9VBY-Gj0Y&t=261s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Money maybe you've made 15K in ads this month if you aren't at a total of a "
               "hundred thousand yet you still can't do this and I found that quite "
               'frustrating.',
       'timestamp': 261,
       'timestamp_label': '[00:04:21]',
       'timestamp_seconds': 261,
       'tip': "Money maybe you've made 15K in ads this month if you aren't at a total of a "
              "hundred thousand yet you still can't do this and I found that quite "
              'frustrating.',
       'title': 'Mediavine vs. Raptive: Which is Better for Bloggers? (She Knows SEO)',
       'url': 'https://www.youtube.com/watch?v=dL9VBY-Gj0Y&t=261s',
       'video_id': 'dL9VBY-Gj0Y'},
      {'author': 'Max Kuch',
       'channel': 'Max Kuch',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:02](https://www.youtube.com/watch?v=qQrj8xEf1Vk&t=302s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "They do require 10K page views a month minimum so obviously that's lower than "
               'the 50k required for the repti wise or the 100K for the normal repti inseller.',
       'timestamp': 302,
       'timestamp_label': '[00:05:02]',
       'timestamp_seconds': 302,
       'tip': "They do require 10K page views a month minimum so obviously that's lower than "
              'the 50k required for the repti wise or the 100K for the normal repti inseller.',
       'title': 'RAPTIVE vs MONUMETRIC: I Moved My Website And Now Earn X Times More (Max '
                'Kuch)',
       'url': 'https://www.youtube.com/watch?v=qQrj8xEf1Vk&t=302s',
       'video_id': 'qQrj8xEf1Vk'},
      {'author': 'Ahrefs',
       'channel': 'Ahrefs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:04](https://www.youtube.com/watch?v=gReszNnykpg&t=124s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'AI assistants like Chat GPT may actually use them to decide who to recommend. '
               "And it's because of how AI assistants work. When someone enters a prompt like, "
               '"Plan me a 5-day trip to Japan in November," the AI assistant fans it out into '
               'dozens of smaller longtail subqueries.',
       'timestamp': 124,
       'timestamp_label': '[00:02:04]',
       'timestamp_seconds': 124,
       'tip': 'AI assistants like Chat GPT may actually use them to decide who to recommend. '
              "And it's because of how AI assistants work. When someone enters a prompt like, "
              '"Plan me a 5-day trip to Japan in November," the AI assistant fans it out into '
              'dozens of smaller longtail subqueries.',
       'title': 'The New SEO Playbook for AI Search (Top GEO Ranking Factors) (Ahrefs)',
       'url': 'https://www.youtube.com/watch?v=gReszNnykpg&t=124s',
       'video_id': 'gReszNnykpg'},
      {'author': 'Income stream surfers',
       'channel': 'Income stream surfers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:16](https://www.youtube.com/watch?v=C6HdlbqGuF4&t=796s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Really really try with a design like that and it has a lot of searches per '
               "month and there's not a lot of competition on redbubble and no one's using "
               'exact phrase match you can potentially get on there if there are some weak '
               'websites on the server.',
       'timestamp': 796,
       'timestamp_label': '[00:13:16]',
       'timestamp_seconds': 796,
       'tip': 'Really really try with a design like that and it has a lot of searches per '
              "month and there's not a lot of competition on redbubble and no one's using "
              'exact phrase match you can potentially get on there if there are some weak '
              'websites on the server.',
       'title': 'Why I think Ahrefs and SEMrush are EASILY the Best Print On Demand SEO '
                'Keyword Methods (Income stream surfers)',
       'url': 'https://www.youtube.com/watch?v=C6HdlbqGuF4&t=796s',
       'video_id': 'C6HdlbqGuF4'},
      {'author': 'Jacob Shireman',
       'channel': 'Jacob Shireman',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:06](https://www.youtube.com/watch?v=Iktexen_-cc&t=786s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Affordable starter homes in Richmond Texas let's see what comes up so now "
               "Zillow wasn't number one as local realtor board but then we start to see fly "
               'homes.com.',
       'timestamp': 786,
       'timestamp_label': '[00:13:06]',
       'timestamp_seconds': 786,
       'tip': "Affordable starter homes in Richmond Texas let's see what comes up so now "
              "Zillow wasn't number one as local realtor board but then we start to see fly "
              'homes.com.',
       'title': 'Real Estate SEO:  How to Rank Your Website for 2025 (Jacob Shireman)',
       'url': 'https://www.youtube.com/watch?v=Iktexen_-cc&t=786s',
       'video_id': 'Iktexen_-cc'},
      {'author': 'Slickplan',
       'channel': 'Slickplan',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:14](https://www.youtube.com/watch?v=SdKSpj4c2H4&t=194s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Visitors away routine site reviews will help you steer clear of those setbacks '
               'all in all a well-planned website structure built with your audience in mind '
               "is the key to maximizing your site's potential start designing yours today "
               'with our s map Builder.',
       'timestamp': 194,
       'timestamp_label': '[00:03:14]',
       'timestamp_seconds': 194,
       'tip': 'Visitors away routine site reviews will help you steer clear of those setbacks '
              'all in all a well-planned website structure built with your audience in mind is '
              "the key to maximizing your site's potential start designing yours today with "
              'our s map Builder.',
       'title': 'Mastering website structure from A to Z: Improve UX and boost SEO (Slickplan)',
       'url': 'https://www.youtube.com/watch?v=SdKSpj4c2H4&t=194s',
       'video_id': 'SdKSpj4c2H4'},
      {'author': 'Niche AI Tool',
       'channel': 'Niche AI Tool',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:30](https://www.youtube.com/watch?v=r8amrelmKH0&t=90s)',
       'relevance': 'Attributed practitioner commentary on multi-site search portfolios, '
                    'programmatic & topical-authority SEO, GEO citation capture, and media '
                    'exits (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "A ref's wins on ease of use and backlink data. Semrush wins on keyword "
               'database size and integrations. It genuinely comes down to your workflow, not '
               'a magic score. A ref starts at $99 a month for the light tier with a $7 trial '
               'and no free plan.',
       'timestamp': 90,
       'timestamp_label': '[00:01:30]',
       'timestamp_seconds': 90,
       'tip': "A ref's wins on ease of use and backlink data. Semrush wins on keyword database "
              'size and integrations. It genuinely comes down to your workflow, not a magic '
              'score. A ref starts at $99 a month for the light tier with a $7 trial and no '
              'free plan.',
       'title': 'Ahrefs vs Semrush 2026: I Tested Both for 30 Days — The Honest Winner #ahrefs '
                '#semrush #aitools (Niche AI Tool)',
       'url': 'https://www.youtube.com/watch?v=r8amrelmKH0&t=90s',
       'video_id': 'r8amrelmKH0'}]}
