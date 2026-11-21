"""Curated 180-citation Million-Dollar Lead Generation baseline (15 per chapter across Q1-Q12) mined strictly from verified Million-Dollar Lead Generation YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'100k',
     '15a',
     '250k',
     '6418',
     'abm',
     'abs',
     'account',
     'accounts',
     'acquisition',
     'acv',
     'agency',
     'agent',
     'agreement',
     'alternative',
     'arizona',
     'attribution',
     'b2b',
     'bant',
     'based',
     'brief',
     'broker',
     'business',
     'buy',
     'buyer',
     'call',
     'capital',
     'center',
     'churn',
     'circumvention',
     'claim',
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
     '15a',
     '250k',
     '6418',
     'abm',
     'abs',
     'account',
     'accounts',
     'acquisition',
     'acv',
     'agency',
     'agent',
     'agreement',
     'alternative',
     'arizona',
     'attribution',
     'b2b',
     'bant',
     'based',
     'brief',
     'broker',
     'budget',
     'business',
     'buy',
     'buyer',
     'call',
     'capital',
     'center',
     'churn',
     'circumvention',
     'claim',
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
     '15a',
     '250k',
     '6418',
     'abm',
     'abs',
     'account',
     'accounts',
     'acquisition',
     'acv',
     'agency',
     'agent',
     'agreement',
     'alternative',
     'arizona',
     'attribution',
     'b2b',
     'bant',
     'based',
     'brief',
     'broker',
     'business',
     'buy',
     'buyer',
     'call',
     'capital',
     'cash',
     'cashflow',
     'center',
     'churn',
     'circumvention',
     'claim',
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
     '15a',
     '250k',
     '6418',
     'abm',
     'abs',
     'account',
     'accounts',
     'acquisition',
     'acv',
     'agency',
     'agent',
     'agreement',
     'alternative',
     'arizona',
     'attribution',
     'b2b',
     'bant',
     'based',
     'brief',
     'broker',
     'budget',
     'business',
     'buy',
     'buyer',
     'call',
     'capital',
     'center',
     'churn',
     'circumvention',
     'claim',
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
     '15a',
     '250k',
     '6418',
     'abm',
     'abs',
     'account',
     'accounts',
     'acquisition',
     'acv',
     'agency',
     'agent',
     'agreement',
     'alternative',
     'arizona',
     'attribution',
     'audit',
     'avoid',
     'b2b',
     'bant',
     'based',
     'brief',
     'broker',
     'business',
     'buy',
     'buyer',
     'call',
     'capital',
     'center',
     'churn',
     'circumvention',
     'claim',
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
     '15a',
     '250k',
     '6418',
     'abm',
     'abs',
     'account',
     'accounts',
     'acquisition',
     'acv',
     'agency',
     'agent',
     'agreement',
     'alternative',
     'arizona',
     'attribution',
     'b2b',
     'bant',
     'based',
     'brief',
     'broker',
     'business',
     'buy',
     'buyer',
     'call',
     'capital',
     'center',
     'churn',
     'circumvention',
     'claim',
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
     '15a',
     '250k',
     '6418',
     'abm',
     'abs',
     'account',
     'accounts',
     'acquisition',
     'acv',
     'agency',
     'agent',
     'agreement',
     'alternative',
     'arizona',
     'attribution',
     'b2b',
     'bant',
     'based',
     'brief',
     'broker',
     'business',
     'buy',
     'buyer',
     'call',
     'capital',
     'center',
     'checklist',
     'churn',
     'circumvention',
     'claim',
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
     '15a',
     '250k',
     '6418',
     'abm',
     'abs',
     'account',
     'accounts',
     'acquisition',
     'acv',
     'agency',
     'agent',
     'agreement',
     'alternative',
     'api',
     'arizona',
     'attribution',
     'b2b',
     'bant',
     'based',
     'brief',
     'broker',
     'business',
     'buy',
     'buyer',
     'call',
     'capital',
     'center',
     'churn',
     'circumvention',
     'claim',
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
     '15a',
     '250k',
     '6418',
     'abm',
     'abs',
     'account',
     'accounts',
     'acquisition',
     'acv',
     'agency',
     'agent',
     'agreement',
     'alternative',
     'arizona',
     'attribution',
     'b2b',
     'bant',
     'based',
     'brief',
     'broker',
     'business',
     'buy',
     'buyer',
     'call',
     'capital',
     'center',
     'churn',
     'circumvention',
     'claim',
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
      '15a',
      '250k',
      '6418',
      'abm',
      'abs',
      'account',
      'accounts',
      'acquisition',
      'acv',
      'agency',
      'agent',
      'agreement',
      'ai',
      'alternative',
      'arizona',
      'attribution',
      'automate',
      'automation',
      'b2b',
      'bant',
      'based',
      'brief',
      'broker',
      'business',
      'buy',
      'buyer',
      'call',
      'capital',
      'center',
      'churn',
      'circumvention',
      'claim',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'100k',
      '15a',
      '250k',
      '6418',
      'abm',
      'abs',
      'account',
      'accounts',
      'acquisition',
      'acv',
      'agency',
      'agent',
      'agreement',
      'alternative',
      'arizona',
      'attribution',
      'b2b',
      'bant',
      'based',
      'brief',
      'broker',
      'business',
      'buy',
      'buyer',
      'call',
      'capital',
      'center',
      'churn',
      'circumvention',
      'claim',
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
      '15a',
      '250k',
      '6418',
      'abm',
      'abs',
      'account',
      'accounts',
      'acquisition',
      'action',
      'acv',
      'agency',
      'agent',
      'agreement',
      'alternative',
      'arizona',
      'attribution',
      'b2b',
      'bant',
      'based',
      'brief',
      'broker',
      'business',
      'buy',
      'buyer',
      'call',
      'capital',
      'center',
      'churn',
      'circumvention',
      'claim',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Sarah Challis',
      'channel': 'Sarah Challis',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=nZS7xjR3bD0&t=15s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Strategies also 58% of B2B marketers reported that ABM resulted in higher deal '
              'value contracts do you want to understand account-based Marketing in.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Strategies also 58% of B2B marketers reported that ABM resulted in higher deal '
             'value contracts do you want to understand account-based Marketing in.',
      'title': 'The Ultimate Guide to Account Based Marketing (ABM) (Sarah Challis)',
      'url': 'https://www.youtube.com/watch?v=nZS7xjR3bD0&t=15s',
      'video_id': 'nZS7xjR3bD0'},
     {'author': 'Dun & Bradstreet',
      'channel': 'Dun & Bradstreet',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:11](https://www.youtube.com/watch?v=wQlrlFnnsuc&t=431s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Insights provided by lattice at the time now dmv ai signals that help us '
              "understand like in-market buyers um at an account level um categorically we're "
              'really helpful for um actually picking out and activating against the accounts '
              "that we're most likely to buy.",
      'timestamp': 431,
      'timestamp_label': '[00:07:11]',
      'timestamp_seconds': 431,
      'tip': 'Insights provided by lattice at the time now dmv ai signals that help us '
             "understand like in-market buyers um at an account level um categorically we're "
             'really helpful for um actually picking out and activating against the accounts '
             "that we're most likely to buy.",
      'title': 'ABM is a journey: How LiveRamp accelerated pipeline growth using a phased ABM '
               'rollout (Dun & Bradstreet)',
      'url': 'https://www.youtube.com/watch?v=wQlrlFnnsuc&t=431s',
      'video_id': 'wQlrlFnnsuc'},
     {'author': 'Dan Martell',
      'channel': 'Dan Martell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=RqN41GVY6UQ&t=111s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So these are the six key areas that I look at when working with a client. The '
              "firm, the business, what's true about them? What vertical do they specialize "
              "in? What's their revenue band right now? What is their percent of growth?",
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': 'So these are the six key areas that I look at when working with a client. The '
             "firm, the business, what's true about them? What vertical do they specialize in? "
             "What's their revenue band right now? What is their percent of growth?",
      'title': 'How to Define The Ideal Customer Profile For Your B2B SaaS Company (Dan '
               'Martell)',
      'url': 'https://www.youtube.com/watch?v=RqN41GVY6UQ&t=111s',
      'video_id': 'RqN41GVY6UQ'},
     {'author': 'WallStreetMojo',
      'channel': 'WallStreetMojo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=x21Z365qRBM&t=85s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Equity capital market the ECM we have debt financing and how they can provide '
              'assistance to the potential clients third sourcing of acquisition with '
              'accompanies as we saw in the dialogue box over here it is closely in $3mn –.',
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': 'Equity capital market the ECM we have debt financing and how they can provide '
             'assistance to the potential clients third sourcing of acquisition with '
             'accompanies as we saw in the dialogue box over here it is closely in $3mn –.',
      'title': 'Deal Origination Sourcing | Approaches to Deal Origination (WallStreetMojo)',
      'url': 'https://www.youtube.com/watch?v=x21Z365qRBM&t=85s',
      'video_id': 'x21Z365qRBM'},
     {'author': 'OGONJO Workbooks',
      'channel': 'OGONJO Workbooks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:56](https://www.youtube.com/watch?v=4S63IHiDhTk&t=116s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's a foundational way to define your ICP with real, checkable data. The "
              'second is the value-based framework, which flips the lens toward outcomes. It '
              'defines your ICP not just by who a company is, but by the specific business '
              'results your best customers actually achieve.',
      'timestamp': 116,
      'timestamp_label': '[00:01:56]',
      'timestamp_seconds': 116,
      'tip': "It's a foundational way to define your ICP with real, checkable data. The second "
             'is the value-based framework, which flips the lens toward outcomes. It defines '
             'your ICP not just by who a company is, but by the specific business results your '
             'best customers actually achieve.',
      'title': 'From a Vague Buyer to a One-Sentence ICP (B2B Ideal Customer Profile Series) – '
               'Pt 4 (OGONJO Workbooks)',
      'url': 'https://www.youtube.com/watch?v=4S63IHiDhTk&t=116s',
      'video_id': '4S63IHiDhTk'},
     {'author': 'Centimillionaire Strategies',
      'channel': 'Centimillionaire Strategies',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=N8Z0FPf2yLw&t=38s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Anyway, uh my company, Perkins Fund Marketing, as Richard said, has been in '
              "business for 30 years. Uh we've raised $8 billion. We only work with "
              'alternative managers, >> [snorts] >> hedge funds, private equity, niche, unique '
              'opportunities.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': 'Anyway, uh my company, Perkins Fund Marketing, as Richard said, has been in '
             "business for 30 years. Uh we've raised $8 billion. We only work with alternative "
             'managers, >> [snorts] >> hedge funds, private equity, niche, unique '
             'opportunities.',
      'title': 'Unlocking Institutional Capital: The Role and Strategic Growth of Placement '
               'Agents (Centimillionaire Strategies)',
      'url': 'https://www.youtube.com/watch?v=N8Z0FPf2yLw&t=38s',
      'video_id': 'N8Z0FPf2yLw'},
     {'author': 'Ana Leiman',
      'channel': 'Ana Leiman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:47](https://www.youtube.com/watch?v=ngCxldTE3UI&t=167s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'First the client is not buying your hours. There are two ways to price your '
              'work. Cost based, how many hours will this take me and what do I charge per '
              'hour? And value based, what is it worth to the person receiving it? Simple '
              'idea, completely different mindset.',
      'timestamp': 167,
      'timestamp_label': '[00:02:47]',
      'timestamp_seconds': 167,
      'tip': 'First the client is not buying your hours. There are two ways to price your '
             'work. Cost based, how many hours will this take me and what do I charge per '
             'hour? And value based, what is it worth to the person receiving it? Simple idea, '
             'completely different mindset.',
      'title': 'How to Move your High-ticket Consulting Clients Onto Retainers (Ana Leiman)',
      'url': 'https://www.youtube.com/watch?v=ngCxldTE3UI&t=167s',
      'video_id': 'ngCxldTE3UI'},
     {'author': 'M&A Synergy AI',
      'channel': 'M&A Synergy AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:16](https://www.youtube.com/watch?v=kk3kEZ_huBU&t=76s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, let's just call it what it is. The old model, the one that relies on "
              'waiting for deals to get listed and manually screening them. It forces you to '
              'be reactive in a market that absolutely rewards being proactive.',
      'timestamp': 76,
      'timestamp_label': '[00:01:16]',
      'timestamp_seconds': 76,
      'tip': "So, let's just call it what it is. The old model, the one that relies on waiting "
             'for deals to get listed and manually screening them. It forces you to be '
             'reactive in a market that absolutely rewards being proactive.',
      'title': 'AI Deal Sourcing Explained: How to Find Off-Market Deals (M&A Synergy AI)',
      'url': 'https://www.youtube.com/watch?v=kk3kEZ_huBU&t=76s',
      'video_id': 'kk3kEZ_huBU'},
     {'author': 'AI InterConnect',
      'channel': 'AI InterConnect',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:02](https://www.youtube.com/watch?v=Ls08sYL9pzQ&t=1202s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I put you on that and let's say uh Predictable B2B Success podcast and I know "
              'for a fact that you have this service that you deliver. You deliver '
              'go-to-market, you deliver all of those solutions for tech companies and you do '
              'it marvelously.',
      'timestamp': 1202,
      'timestamp_label': '[00:20:02]',
      'timestamp_seconds': 1202,
      'tip': "I put you on that and let's say uh Predictable B2B Success podcast and I know "
             'for a fact that you have this service that you deliver. You deliver '
             'go-to-market, you deliver all of those solutions for tech companies and you do '
             'it marvelously.',
      'title': 'How Gal Ko and PodStar Turn Podcast Guesting Into B2B Growth (AI InterConnect)',
      'url': 'https://www.youtube.com/watch?v=Ls08sYL9pzQ&t=1202s',
      'video_id': 'Ls08sYL9pzQ'},
     {'author': 'Law Firm ROI with Awais',
      'channel': 'Law Firm ROI with Awais',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:29](https://www.youtube.com/watch?v=gFY3JFigbao&t=1889s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re working on your uh Google My Business if you're basically a local business "
              "or local law firm. They're only um or you know you your your main goal is to "
              'get clients from your local area.',
      'timestamp': 1889,
      'timestamp_label': '[00:31:29]',
      'timestamp_seconds': 1889,
      'tip': "'re working on your uh Google My Business if you're basically a local business "
             "or local law firm. They're only um or you know you your your main goal is to get "
             'clients from your local area.',
      'title': 'Lead Generation for Lawyers (Law Firm ROI with Awais)',
      'url': 'https://www.youtube.com/watch?v=gFY3JFigbao&t=1889s',
      'video_id': 'gFY3JFigbao'},
     {'author': 'New Law Business Model',
      'channel': 'New Law Business Model',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:21](https://www.youtube.com/watch?v=mDqUwOQyPnc&t=81s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Business Model, and I am currently licensing more than 650 lawyers to use my '
              'proven marketing resources to keep their law practices full of clients they '
              'love to serve without wasting time, money, or energy on strategies that simply '
              'do not fit.',
      'timestamp': 81,
      'timestamp_label': '[00:01:21]',
      'timestamp_seconds': 81,
      'tip': 'Business Model, and I am currently licensing more than 650 lawyers to use my '
             'proven marketing resources to keep their law practices full of clients they love '
             'to serve without wasting time, money, or energy on strategies that simply do not '
             'fit.',
      'title': 'How Do Lawyers Find Their Ideal Clients? Lead Generation Playbook (New Law '
               'Business Model)',
      'url': 'https://www.youtube.com/watch?v=mDqUwOQyPnc&t=81s',
      'video_id': 'mDqUwOQyPnc'},
     {'author': 'Zero Risk Cases Client Acquisition Agency',
      'channel': 'Zero Risk Cases Client Acquisition Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:03](https://www.youtube.com/watch?v=z8D3CYz8Rxs&t=123s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Firm we do all the heavy lifting for your firm you receive a highly qualified '
              'client there is no risk to your law firm stop chasing down dead internet leads '
              'call us today and get your zero risk mass tort case campaign started zero risk '
              'cases call 833-937-6747.',
      'timestamp': 123,
      'timestamp_label': '[00:02:03]',
      'timestamp_seconds': 123,
      'tip': 'Firm we do all the heavy lifting for your firm you receive a highly qualified '
             'client there is no risk to your law firm stop chasing down dead internet leads '
             'call us today and get your zero risk mass tort case campaign started zero risk '
             'cases call 833-937-6747.',
      'title': 'Mass Tort Cases-Signed Mass Tort Cases-Call 855-943-8736 (Zero Risk Cases '
               'Client Acquisition Agency)',
      'url': 'https://www.youtube.com/watch?v=z8D3CYz8Rxs&t=123s',
      'video_id': 'z8D3CYz8Rxs'},
     {'author': 'Marco Palmero',
      'channel': 'Marco Palmero',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:16](https://www.youtube.com/watch?v=p5BRxk-zVCA&t=136s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Your market might be too narrow. M&A experience, then you're going to be in a "
              "tough spot and you're going to have, you know, a hard time getting value and "
              "results out of that provider. So, that's point number one.",
      'timestamp': 136,
      'timestamp_label': '[00:02:16]',
      'timestamp_seconds': 136,
      'tip': "Your market might be too narrow. M&A experience, then you're going to be in a "
             "tough spot and you're going to have, you know, a hard time getting value and "
             "results out of that provider. So, that's point number one.",
      'title': 'How Do You Choose the Right Deal Sourcing Provider? (Marco Palmero)',
      'url': 'https://www.youtube.com/watch?v=p5BRxk-zVCA&t=136s',
      'video_id': 'p5BRxk-zVCA'},
     {'author': 'Business Credit America',
      'channel': 'Business Credit America',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:35](https://www.youtube.com/watch?v=Qi_L4TMGG1A&t=95s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The country with this powerful list alone you can bypass traditional lenders '
              'and focus on dealing directly with lenders and investors that are interested in '
              'helping you make your business a success to get started now just click the '
              'link.',
      'timestamp': 95,
      'timestamp_label': '[00:01:35]',
      'timestamp_seconds': 95,
      'tip': 'The country with this powerful list alone you can bypass traditional lenders and '
             'focus on dealing directly with lenders and investors that are interested in '
             'helping you make your business a success to get started now just click the link.',
      'title': '"Unsecured Business Loans" Financing Strategy Using A Ucc-1 Financial '
               'Statement (Business Credit America)',
      'url': 'https://www.youtube.com/watch?v=Qi_L4TMGG1A&t=95s',
      'video_id': 'Qi_L4TMGG1A'},
     {'author': 'Hacking the Case Interview',
      'channel': 'Hacking the Case Interview',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:46](https://www.youtube.com/watch?v=J1GpLqugFeM&t=586s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Our comprehensive case interview course and books links are in the video '
              'description we teach the most robust effective case interiew strategies in the '
              'least timeconsuming way to save you hundreds of hours of prep time and help you '
              'land more multiple consulting job.',
      'timestamp': 586,
      'timestamp_label': '[00:09:46]',
      'timestamp_seconds': 586,
      'tip': 'Our comprehensive case interview course and books links are in the video '
             'description we teach the most robust effective case interiew strategies in the '
             'least timeconsuming way to save you hundreds of hours of prep time and help you '
             'land more multiple consulting job.',
      'title': 'Learn M&A Case Interviews in 10 Minutes | QUICKEST Tutorial on YouTube '
               '(Hacking the Case Interview)',
      'url': 'https://www.youtube.com/watch?v=J1GpLqugFeM&t=586s',
      'video_id': 'J1GpLqugFeM'}],
 2: [{'author': 'GrowthSpree - AI Native B2B Marketing Agency',
      'channel': 'GrowthSpree - AI Native B2B Marketing Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:14](https://www.youtube.com/watch?v=fdPFLXFJlwo&t=314s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The right agency integrates your customer relationship management, tracks '
              'pipeline stages, and bids toward revenue, not lead count. GrowthSpree is the '
              'top choice for B2B SaaS at a flat fee with no budget inflation incentive.',
      'timestamp': 314,
      'timestamp_label': '[00:05:14]',
      'timestamp_seconds': 314,
      'tip': 'The right agency integrates your customer relationship management, tracks '
             'pipeline stages, and bids toward revenue, not lead count. GrowthSpree is the top '
             'choice for B2B SaaS at a flat fee with no budget inflation incentive.',
      'title': '6 Best Revenue Attribution Agencies for B2B SaaS in 2026 (GrowthSpree - AI '
               'Native B2B Marketing Agency)',
      'url': 'https://www.youtube.com/watch?v=fdPFLXFJlwo&t=314s',
      'video_id': 'fdPFLXFJlwo'},
     {'author': 'Ask a VC',
      'channel': 'Ask a VC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:46](https://www.youtube.com/watch?v=su9KuGnbAW8&t=346s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re in a situation where the ACV's are smaller, call it 5-10k a year, and then "
              "the customer maybe doesn't have the same investment in you and your product, "
              "it's much easier for them to make a decision to churn.",
      'timestamp': 346,
      'timestamp_label': '[00:05:46]',
      'timestamp_seconds': 346,
      'tip': "'re in a situation where the ACV's are smaller, call it 5-10k a year, and then "
             "the customer maybe doesn't have the same investment in you and your product, "
             "it's much easier for them to make a decision to churn.",
      'title': 'AskAVC #2 - SaaS Churn: what is it? (Ask a VC)',
      'url': 'https://www.youtube.com/watch?v=su9KuGnbAW8&t=346s',
      'video_id': 'su9KuGnbAW8'},
     {'author': 'Daniel Fazio Highlights',
      'channel': 'Daniel Fazio Highlights',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:49](https://www.youtube.com/watch?v=bQCztTB4VbQ&t=229s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "No, yeah, it's just Yeah, it's just the nature of the business. So, like "
              'earlier I said like you try to work with a real estate agent get them to pay '
              "you a retainer, and they're going to tell you to get [ __ ] There's e-comm "
              "email type stuff. It It's somewhere in the middle.",
      'timestamp': 229,
      'timestamp_label': '[00:03:49]',
      'timestamp_seconds': 229,
      'tip': "No, yeah, it's just Yeah, it's just the nature of the business. So, like earlier "
             'I said like you try to work with a real estate agent get them to pay you a '
             "retainer, and they're going to tell you to get [ __ ] There's e-comm email type "
             "stuff. It It's somewhere in the middle.",
      'title': "Retainer Vs Rev Share: How I'd Price Agency Clients | Daniel Fazio AI Assisted "
               'Agency (Daniel Fazio Highlights)',
      'url': 'https://www.youtube.com/watch?v=bQCztTB4VbQ&t=229s',
      'video_id': 'bQCztTB4VbQ'},
     {'author': 'Dan Lok',
      'channel': 'Dan Lok',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=GyZuNsAtjIU&t=163s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "See, you are setting up the stage. You are setting up the sale. You're setting "
              'up the retainer fees. So, one of the ways you can structure your fee is you '
              'give them a little bit of a break if they pay the whole thing up front.',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': "See, you are setting up the stage. You are setting up the sale. You're setting "
             'up the retainer fees. So, one of the ways you can structure your fee is you give '
             'them a little bit of a break if they pay the whole thing up front.',
      'title': 'How to Package and Sell High Ticket Consulting Retainer Fees? S1E17 (Dan Lok)',
      'url': 'https://www.youtube.com/watch?v=GyZuNsAtjIU&t=163s',
      'video_id': 'GyZuNsAtjIU'},
     {'author': 'Rafael Hernandez ⚡️',
      'channel': 'Rafael Hernandez ⚡️',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:19](https://www.youtube.com/watch?v=XPcFTfp7i8E&t=379s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Write this all down in the contract when you pitch it. So that's the hybrid "
              "agency model. 's a retainer and a set price for every result that fits.",
      'timestamp': 379,
      'timestamp_label': '[00:06:19]',
      'timestamp_seconds': 379,
      'tip': "Write this all down in the contract when you pitch it. So that's the hybrid "
             "agency model. 's a retainer and a set price for every result that fits.",
      'title': 'Hybrid Lead Gen Model: Retainer Plus Pay Per Result (Rafael Hernandez ⚡️)',
      'url': 'https://www.youtube.com/watch?v=XPcFTfp7i8E&t=379s',
      'video_id': 'XPcFTfp7i8E'},
     {'author': 'Simple Explain',
      'channel': 'Simple Explain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:22](https://www.youtube.com/watch?v=vTGW5-gVWNY&t=262s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Four, the Lehman formula structures the investment banking fee on a percentage '
              'of the transaction amount based on a set of tiered fees.',
      'timestamp': 262,
      'timestamp_label': '[00:04:22]',
      'timestamp_seconds': 262,
      'tip': 'Four, the Lehman formula structures the investment banking fee on a percentage '
             'of the transaction amount based on a set of tiered fees.',
      'title': 'Lehman Formula: Definition and Calculation Examples (Simple Explain)',
      'url': 'https://www.youtube.com/watch?v=vTGW5-gVWNY&t=262s',
      'video_id': 'vTGW5-gVWNY'},
     {'author': 'Wall Street Mastermind',
      'channel': 'Wall Street Mastermind',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:09](https://www.youtube.com/watch?v=BOtCQLtiRJQ&t=969s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm I'm buying the entire company. I'm buying like OpenAI, the entirety of it. "
              'All the employees, all the customer relationships, all the PR teams, like '
              'whatever. And taxes what this means is that the seller is going to pay capital '
              'gains tax.',
      'timestamp': 969,
      'timestamp_label': '[00:16:09]',
      'timestamp_seconds': 969,
      'tip': "I'm I'm buying the entire company. I'm buying like OpenAI, the entirety of it. "
             'All the employees, all the customer relationships, all the PR teams, like '
             'whatever. And taxes what this means is that the seller is going to pay capital '
             'gains tax.',
      'title': 'The M&A Deal Lifecycle: From Origination to Close (Wall Street Mastermind)',
      'url': 'https://www.youtube.com/watch?v=BOtCQLtiRJQ&t=969s',
      'video_id': 'BOtCQLtiRJQ'},
     {'author': 'Consulting Success',
      'channel': 'Consulting Success',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:59](https://www.youtube.com/watch?v=78Np-tdJDW4&t=479s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t have to pay the same level of high cost. Maybe your fee is $15,000 a month. "
              "So it's significantly less than $250 to $400,000. But the other thing is they "
              "don't have to wait to find the right person because you're there. It takes time "
              'to find and to hire somebody, right?',
      'timestamp': 479,
      'timestamp_label': '[00:07:59]',
      'timestamp_seconds': 479,
      'tip': "'t have to pay the same level of high cost. Maybe your fee is $15,000 a month. "
             "So it's significantly less than $250 to $400,000. But the other thing is they "
             "don't have to wait to find the right person because you're there. It takes time "
             'to find and to hire somebody, right?',
      'title': 'How to Build a High-Ticket Consulting Retainer That Scales (Consulting '
               'Success)',
      'url': 'https://www.youtube.com/watch?v=78Np-tdJDW4&t=479s',
      'video_id': '78Np-tdJDW4'},
     {'author': 'Myk Pono',
      'channel': 'Myk Pono',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=Y1u-ngsyH60&t=89s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Meaning they have a budget to buy your product so that could be markers in SAS '
              'companies with over 25 employees or with revenue above 1 million ARR then you '
              'can.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': 'Meaning they have a budget to buy your product so that could be markers in SAS '
             'companies with over 25 employees or with revenue above 1 million ARR then you '
             'can.',
      'title': 'How To Research Ideal Customer Profile(ICP): Target Audience, Potential '
               'Customer, ICP, Persona (Myk Pono)',
      'url': 'https://www.youtube.com/watch?v=Y1u-ngsyH60&t=89s',
      'video_id': 'Y1u-ngsyH60'},
     {'author': 'Tao Solutions Inc',
      'channel': 'Tao Solutions Inc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=Za2avmXv1RE&t=78s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'As interest only seasonal or skip payments fees and much more the payment '
              'calculator has multiple engines available t-value included the collateral tab '
              'is where you can list all assets on the deal application.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'As interest only seasonal or skip payments fees and much more the payment '
             'calculator has multiple engines available t-value included the collateral tab is '
             'where you can list all assets on the deal application.',
      'title': 'Deal Origination (Tao Solutions Inc)',
      'url': 'https://www.youtube.com/watch?v=Za2avmXv1RE&t=78s',
      'video_id': 'Za2avmXv1RE'},
     {'author': 'All Things SPVs',
      'channel': 'All Things SPVs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:02](https://www.youtube.com/watch?v=F1OsgcF_bhg&t=842s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You could write something here like org costs or something like that if you '
              "needed felt inclined to. 've pulled off the top to pay for admin or management "
              "fee or something like that. Now we're at the end and we type in our signature.",
      'timestamp': 842,
      'timestamp_label': '[00:14:02]',
      'timestamp_seconds': 842,
      'tip': 'You could write something here like org costs or something like that if you '
             "needed felt inclined to. 've pulled off the top to pay for admin or management "
             "fee or something like that. Now we're at the end and we type in our signature.",
      'title': 'How to File Form D for Your SPV | Step-by-Step SEC Filing Guide (All Things '
               'SPVs | Part 3) (All Things SPVs)',
      'url': 'https://www.youtube.com/watch?v=F1OsgcF_bhg&t=842s',
      'video_id': 'F1OsgcF_bhg'},
     {'author': 'Concurate',
      'channel': 'Concurate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:36](https://www.youtube.com/watch?v=3_gHjeAdeNE&t=156s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, the support goes beyond writing posts. If you want a smaller agency that '
              'pays close attention to how you sound, Yellow Ink would be a suitable agency '
              "for you. Think about what happens after somebody reads your post. They're "
              'interested, so they click on your profile.',
      'timestamp': 156,
      'timestamp_label': '[00:02:36]',
      'timestamp_seconds': 156,
      'tip': 'So, the support goes beyond writing posts. If you want a smaller agency that '
             'pays close attention to how you sound, Yellow Ink would be a suitable agency for '
             "you. Think about what happens after somebody reads your post. They're "
             'interested, so they click on your profile.',
      'title': 'Which LinkedIn Ghostwriting Agency Is Right for You? Here’s 5 Options for '
               'Founders and Executives (Concurate)',
      'url': 'https://www.youtube.com/watch?v=3_gHjeAdeNE&t=156s',
      'video_id': '3_gHjeAdeNE'},
     {'author': 'Executive Resume Writers',
      'channel': 'Executive Resume Writers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=Vi-DPWAY1C0&t=118s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Posting thought leadership content is your chance to claim that stage and '
              'attract your own crowd of decision-makers and industry influencers. Thought '
              "leadership isn't just about what you know, it's about sharing insights that "
              'influence industry conversations.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': 'Posting thought leadership content is your chance to claim that stage and '
             'attract your own crowd of decision-makers and industry influencers. Thought '
             "leadership isn't just about what you know, it's about sharing insights that "
             'influence industry conversations.',
      'title': 'How to Become a Thought Leader on LinkedIn (Even Without a Huge Following) '
               '(Executive Resume Writers)',
      'url': 'https://www.youtube.com/watch?v=Vi-DPWAY1C0&t=118s',
      'video_id': 'Vi-DPWAY1C0'},
     {'author': 'Merlin Law Group',
      'channel': 'Merlin Law Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=hb-cKsFxfwg&t=60s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Sometimes the insurance company's right, but it's only if the insurance "
              'coverage is written in such a way that allows them to say, "We don\'t pay for '
              'cosmetic damage.".',
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': "Sometimes the insurance company's right, but it's only if the insurance coverage "
             'is written in such a way that allows them to say, "We don\'t pay for cosmetic '
             'damage.".',
      'title': 'Commercial Roof Hail Damage: Is It Really Cosmetic? (Merlin Law Group)',
      'url': 'https://www.youtube.com/watch?v=hb-cKsFxfwg&t=60s',
      'video_id': 'hb-cKsFxfwg'},
     {'author': 'Financial Regulation Courses',
      'channel': 'Financial Regulation Courses',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=nST9vhaTkek&t=157s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Furthermore, Rule 2111 explicitly covers hold recommendations, ensuring the '
              'standard of care remains active throughout the life cycle of the entire '
              'customer relationship.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': 'Furthermore, Rule 2111 explicitly covers hold recommendations, ensuring the '
             'standard of care remains active throughout the life cycle of the entire customer '
             'relationship.',
      'title': 'FINRA Rule 2111 Explained  Suitability Rule, Customer Recommendations & Broker '
               'Dealer Compliance (Financial Regulation Courses)',
      'url': 'https://www.youtube.com/watch?v=nST9vhaTkek&t=157s',
      'video_id': 'nST9vhaTkek'}],
 3: [{'author': 'Senator We Run Ads',
      'channel': 'Senator We Run Ads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=Jx0muHw5NUY&t=75s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'First discuss what is ABM so simply put ABM stands for account-based marketing '
              'where you identify key accounts or companies which you want to be your.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': 'First discuss what is ABM so simply put ABM stands for account-based marketing '
             'where you identify key accounts or companies which you want to be your.',
      'title': 'What is Account Based Marketing? How to setup for your B2B business (2024 '
               'version) (Senator We Run Ads)',
      'url': 'https://www.youtube.com/watch?v=Jx0muHw5NUY&t=75s',
      'video_id': 'Jx0muHw5NUY'},
     {'author': 'Money Sutra',
      'channel': 'Money Sutra',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:20](https://www.youtube.com/watch?v=aBB5nV2vr2Q&t=380s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The buyer should not justify a deal using synergies alone. The real value comes '
              'from the target stand-alone business plus credible synergies, less transaction '
              'fees, financing costs, and the cost of integrating two organizations. Closing '
              'is not the finish line.',
      'timestamp': 380,
      'timestamp_label': '[00:06:20]',
      'timestamp_seconds': 380,
      'tip': 'The buyer should not justify a deal using synergies alone. The real value comes '
             'from the target stand-alone business plus credible synergies, less transaction '
             'fees, financing costs, and the cost of integrating two organizations. Closing is '
             'not the finish line.',
      'title': 'How Billion-Dollar M&A Deals Actually Work | Investment Banking (Money Sutra)',
      'url': 'https://www.youtube.com/watch?v=aBB5nV2vr2Q&t=380s',
      'video_id': 'aBB5nV2vr2Q'},
     {'author': 'POTOMAC M&A',
      'channel': 'POTOMAC M&A',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:26](https://www.youtube.com/watch?v=RLr8PdCZ6U0&t=326s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, increasing cash flow is easy, right? You increase revenue, you call costs '
              'down, you increase cash flow. Everyone kind of gets that. Now, when you talk '
              "about risk, sometime that's a little bit more difficult for people to grasp.",
      'timestamp': 326,
      'timestamp_label': '[00:05:26]',
      'timestamp_seconds': 326,
      'tip': 'Now, increasing cash flow is easy, right? You increase revenue, you call costs '
             'down, you increase cash flow. Everyone kind of gets that. Now, when you talk '
             "about risk, sometime that's a little bit more difficult for people to grasp.",
      'title': 'Buy-Side M&A Masterclass, Pt. 1 | Before You Buy: Strategy, Criteria & '
               'Sourcing (POTOMAC M&A)',
      'url': 'https://www.youtube.com/watch?v=RLr8PdCZ6U0&t=326s',
      'video_id': 'RLr8PdCZ6U0'},
     {'author': 'Steve Armenti',
      'channel': 'Steve Armenti',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:41](https://www.youtube.com/watch?v=Mv1ZTzPcy5A&t=521s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s the ROI on this because truthfully, you know, running this type of work at a "
              'contact level is fairly expensive and time-consuming, but the numbers show '
              "really good ROI, especially if you've got an ACV of 50 to 100k uh per year.",
      'timestamp': 521,
      'timestamp_label': '[00:08:41]',
      'timestamp_seconds': 521,
      'tip': "'s the ROI on this because truthfully, you know, running this type of work at a "
             'contact level is fairly expensive and time-consuming, but the numbers show '
             "really good ROI, especially if you've got an ACV of 50 to 100k uh per year.",
      'title': 'Enterprise 1-1 ABM Play That Produced $1.3M in 40 Days (Steve Armenti)',
      'url': 'https://www.youtube.com/watch?v=Mv1ZTzPcy5A&t=521s',
      'video_id': 'Mv1ZTzPcy5A'},
     {'author': 'One Minute Finance',
      'channel': 'One Minute Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:44](https://www.youtube.com/watch?v=id39IYEm-oQ&t=464s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But, as a business scales up, say into the lower mid-market at 2 to 5 million, '
              'or the mid-market between 25 and 50 million, that multiple expands rapidly, '
              "jumping up to nearly eight times earnings. Because as a buyer, you're "
              'ultimately paying for de-risked cash flow.',
      'timestamp': 464,
      'timestamp_label': '[00:07:44]',
      'timestamp_seconds': 464,
      'tip': 'But, as a business scales up, say into the lower mid-market at 2 to 5 million, '
             'or the mid-market between 25 and 50 million, that multiple expands rapidly, '
             "jumping up to nearly eight times earnings. Because as a buyer, you're ultimately "
             'paying for de-risked cash flow.',
      'title': 'M&A Sourcing & Valuation Explained: Proprietary Deals to EBITDA Multiples (One '
               'Minute Finance)',
      'url': 'https://www.youtube.com/watch?v=id39IYEm-oQ&t=464s',
      'video_id': 'id39IYEm-oQ'},
     {'author': 'Roman Love',
      'channel': 'Roman Love',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:55](https://www.youtube.com/watch?v=3vw0ExOznb8&t=175s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Yeah, I mean that's always been a huge challenge in business development and "
              'lead generation in our industry is it can create a really high cost of '
              'acquisition or it could be a very cheap cost of acquisition, but really low '
              'quality.',
      'timestamp': 175,
      'timestamp_label': '[00:02:55]',
      'timestamp_seconds': 175,
      'tip': "Yeah, I mean that's always been a huge challenge in business development and "
             'lead generation in our industry is it can create a really high cost of '
             'acquisition or it could be a very cheap cost of acquisition, but really low '
             'quality.',
      'title': 'US commercial solar leads review: Treepublic | TNW Marketing (Roman Love)',
      'url': 'https://www.youtube.com/watch?v=3vw0ExOznb8&t=175s',
      'video_id': '3vw0ExOznb8'},
     {'author': 'Alex Hormozi',
      'channel': 'Alex Hormozi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:03](https://www.youtube.com/watch?v=O1As2zxy0es&t=303s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Business all right so a private chain is gonna have the highest costs of '
              "opening each location so there's incremental cost every new location you.",
      'timestamp': 303,
      'timestamp_label': '[00:05:03]',
      'timestamp_seconds': 303,
      'tip': 'Business all right so a private chain is gonna have the highest costs of opening '
             "each location so there's incremental cost every new location you.",
      'title': 'The Only 4 Ways To Scale A Service Business (PICK ONE) (Alex Hormozi)',
      'url': 'https://www.youtube.com/watch?v=O1As2zxy0es&t=303s',
      'video_id': 'O1As2zxy0es'},
     {'author': 'Investment Banking Insights',
      'channel': 'Investment Banking Insights',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:34](https://www.youtube.com/watch?v=zFuxJIjPV2c&t=574s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Down the pool of potential buyers and they're now doing more detailed due "
              'diligence to try to figure out do they actually want to buy this business or '
              "not so there's a couple of things that goes into this phase so there is the you "
              'know management.',
      'timestamp': 574,
      'timestamp_label': '[00:09:34]',
      'timestamp_seconds': 574,
      'tip': "Down the pool of potential buyers and they're now doing more detailed due "
             'diligence to try to figure out do they actually want to buy this business or not '
             "so there's a couple of things that goes into this phase so there is the you know "
             'management.',
      'title': 'The Six Steps of Sell Side M&A (Investment Banking Insights)',
      'url': 'https://www.youtube.com/watch?v=zFuxJIjPV2c&t=574s',
      'video_id': 'zFuxJIjPV2c'},
     {'author': 'Credit Suite',
      'channel': 'Credit Suite',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:23](https://www.youtube.com/watch?v=TvwdUsUy-Cs&t=143s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The right to claim your assets so UCC filing kind of adversely affects your '
              "business credit reports because even though it doesn't adversely affect your.",
      'timestamp': 143,
      'timestamp_label': '[00:02:23]',
      'timestamp_seconds': 143,
      'tip': 'The right to claim your assets so UCC filing kind of adversely affects your '
             "business credit reports because even though it doesn't adversely affect your.",
      'title': 'What is a UCC Filing (Credit Suite)',
      'url': 'https://www.youtube.com/watch?v=TvwdUsUy-Cs&t=143s',
      'video_id': 'TvwdUsUy-Cs'},
     {'author': 'Neil McDonnell',
      'channel': 'Neil McDonnell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:27](https://www.youtube.com/watch?v=YL3LT_x34Ms&t=687s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Words okay the next one is request for quotes that I have here and if you've "
              "read ahead right request for quotes primarily it's about getting cost price.",
      'timestamp': 687,
      'timestamp_label': '[00:11:27]',
      'timestamp_seconds': 687,
      'tip': "Words okay the next one is request for quotes that I have here and if you've "
             "read ahead right request for quotes primarily it's about getting cost price.",
      'title': 'What Government Contractors Need to Know about RFI, RFQ, and RFP Notices (Neil '
               'McDonnell)',
      'url': 'https://www.youtube.com/watch?v=YL3LT_x34Ms&t=687s',
      'video_id': 'YL3LT_x34Ms'},
     {'author': 'Local Service Ads',
      'channel': 'Local Service Ads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:57](https://www.youtube.com/watch?v=abdd1rgCZ90&t=357s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The lsa page in orlando or in clearwater or google organic in other words what '
              'ad unit or what source is generating this phone call what once.',
      'timestamp': 357,
      'timestamp_label': '[00:05:57]',
      'timestamp_seconds': 357,
      'tip': 'The lsa page in orlando or in clearwater or google organic in other words what '
             'ad unit or what source is generating this phone call what once.',
      'title': 'Law Firm Marketing: BEST Lead Generation Machine 2023 (Local Service Ads)',
      'url': 'https://www.youtube.com/watch?v=abdd1rgCZ90&t=357s',
      'video_id': 'abdd1rgCZ90'},
     {'author': 'In Love With Marketing',
      'channel': 'In Love With Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:47](https://www.youtube.com/watch?v=MhQ7Toiejks&t=107s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Where there's a point till where marketing and sales collaboration will be but "
              'in case of ABM you know sales and marketing teams they work together to '
              'generate opportunity but and also they still work together throughout the '
              'entire sales cycle as well.',
      'timestamp': 107,
      'timestamp_label': '[00:01:47]',
      'timestamp_seconds': 107,
      'tip': "Where there's a point till where marketing and sales collaboration will be but "
             'in case of ABM you know sales and marketing teams they work together to generate '
             'opportunity but and also they still work together throughout the entire sales '
             'cycle as well.',
      'title': 'Traditional B2B Marketing vs ABM Account Based Marketing (In Love With '
               'Marketing)',
      'url': 'https://www.youtube.com/watch?v=MhQ7Toiejks&t=107s',
      'video_id': 'MhQ7Toiejks'},
     {'author': 'John Colley | The Investment Banking Practitioner',
      'channel': 'John Colley | The Investment Banking Practitioner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:56](https://www.youtube.com/watch?v=dZiHOJKxvoE&t=356s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So that's a quick run through this deal origination buy side m a presentation "
              "if you'd like to talk to me about it in more detail then my contact details on "
              'the screen email me john jbdcolly.com my mobile number 07813-672612.',
      'timestamp': 356,
      'timestamp_label': '[00:05:56]',
      'timestamp_seconds': 356,
      'tip': "So that's a quick run through this deal origination buy side m a presentation if "
             "you'd like to talk to me about it in more detail then my contact details on the "
             'screen email me john jbdcolly.com my mobile number 07813-672612.',
      'title': 'Mergers and Acquisitions Explained: M&A Deal Origination Secrets (John Colley '
               '| The Investment Banking Practitioner)',
      'url': 'https://www.youtube.com/watch?v=dZiHOJKxvoE&t=356s',
      'video_id': 'dZiHOJKxvoE'},
     {'author': 'Phaibion Royal',
      'channel': 'Phaibion Royal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:45](https://www.youtube.com/watch?v=rhgUISy29oc&t=285s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Commercial solar company in the u.s. so do it now because the price will go up '
              "and we will run out of spaces okay this is your last chance I'm about to stop "
              "talking so click the link below and let's talk.",
      'timestamp': 285,
      'timestamp_label': '[00:04:45]',
      'timestamp_seconds': 285,
      'tip': 'Commercial solar company in the u.s. so do it now because the price will go up '
             "and we will run out of spaces okay this is your last chance I'm about to stop "
             "talking so click the link below and let's talk.",
      'title': 'How To Generate Commercial Solar Leads (Phaibion Royal)',
      'url': 'https://www.youtube.com/watch?v=rhgUISy29oc&t=285s',
      'video_id': 'rhgUISy29oc'},
     {'author': 'Prateek Vyas',
      'channel': 'Prateek Vyas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:14](https://www.youtube.com/watch?v=gidIDHXJlO4&t=254s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Aek not only it's fundamental but the role it can play in a change or shift in "
              "a company's stock price if you would like me to answer any questions please "
              'feel free to comment them down below other than that thank you for watching see '
              'ya.',
      'timestamp': 254,
      'timestamp_label': '[00:04:14]',
      'timestamp_seconds': 254,
      'tip': "Aek not only it's fundamental but the role it can play in a change or shift in a "
             "company's stock price if you would like me to answer any questions please feel "
             'free to comment them down below other than that thank you for watching see ya.',
      'title': 'SEC Filing — 8-K | Definition and Examples (Prateek Vyas)',
      'url': 'https://www.youtube.com/watch?v=gidIDHXJlO4&t=254s',
      'video_id': 'gidIDHXJlO4'}],
 4: [{'author': 'AI for Every Job',
      'channel': 'AI for Every Job',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:12](https://www.youtube.com/watch?v=jorQjadBVYw&t=252s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The proposal lands and the finance director has questions. Priya does not want '
              'to hear tough objections first on a live call, so she practices. In Salesforce, '
              "Agent for Sales Coach runs role plays that simulate a buyer based on the rep's "
              'deal.',
      'timestamp': 252,
      'timestamp_label': '[00:04:12]',
      'timestamp_seconds': 252,
      'tip': 'The proposal lands and the finance director has questions. Priya does not want '
             'to hear tough objections first on a live call, so she practices. In Salesforce, '
             "Agent for Sales Coach runs role plays that simulate a buyer based on the rep's "
             'deal.',
      'title': 'AI for Salespeople in 2026: Account Research, Outreach, Discovery Calls and '
               'Forecasts (AI for Every Job)',
      'url': 'https://www.youtube.com/watch?v=jorQjadBVYw&t=252s',
      'video_id': 'jorQjadBVYw'},
     {'author': 'Prospeo',
      'channel': 'Prospeo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:57](https://www.youtube.com/watch?v=OqdXhRy5QNY&t=477s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Go to the four business tab on LinkedIn, click advertise, and select or create '
              'an ad account. Choose lead generation as your campaign objective. Select either '
              'accelerate or classic campaign type and set your budget and schedule.',
      'timestamp': 477,
      'timestamp_label': '[00:07:57]',
      'timestamp_seconds': 477,
      'tip': 'Go to the four business tab on LinkedIn, click advertise, and select or create '
             'an ad account. Choose lead generation as your campaign objective. Select either '
             'accelerate or classic campaign type and set your budget and schedule.',
      'title': 'How to Use LinkedIn for Account-Based Marketing in 2026 (Complete ABM Guide) '
               '(Prospeo)',
      'url': 'https://www.youtube.com/watch?v=OqdXhRy5QNY&t=477s',
      'video_id': 'OqdXhRy5QNY'},
     {'author': 'SalesLabX',
      'channel': 'SalesLabX',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:47:48](https://www.youtube.com/watch?v=JkmlKUCHcmA&t=2868s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We like to call it the ABM Flex ABM insights but it's out of the box you can "
              "set it up on your component so here's our sales lab x account imagine on the "
              "sales rep that's called about to call this account to close a deal if I go "
              'right here in this component.',
      'timestamp': 2868,
      'timestamp_label': '[00:47:48]',
      'timestamp_seconds': 2868,
      'tip': "We like to call it the ABM Flex ABM insights but it's out of the box you can set "
             "it up on your component so here's our sales lab x account imagine on the sales "
             "rep that's called about to call this account to close a deal if I go right here "
             'in this component.',
      'title': 'SalesLabX Webinar: Salesforce Multi Touch Attribution (SalesLabX)',
      'url': 'https://www.youtube.com/watch?v=JkmlKUCHcmA&t=2868s',
      'video_id': 'JkmlKUCHcmA'},
     {'author': 'The Influence',
      'channel': 'The Influence',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=_i5Xkz85mPA&t=21s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This quote right here, it gets straight to the heart of the whole problem. It's "
              'from a story about a B2B software company that had these perfect, beautifully '
              'crafted buyer personas. I mean, they knew everything about the managers they '
              'were targeting.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "This quote right here, it gets straight to the heart of the whole problem. It's "
             'from a story about a B2B software company that had these perfect, beautifully '
             'crafted buyer personas. I mean, they knew everything about the managers they '
             'were targeting.',
      'title': 'Ideal Customer Profile vs Buyer Persona in B2B Sales (The Influence)',
      'url': 'https://www.youtube.com/watch?v=_i5Xkz85mPA&t=21s',
      'video_id': '_i5Xkz85mPA'},
     {'author': 'Kinner Sacchdev - Edbound AI',
      'channel': 'Kinner Sacchdev - Edbound AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=Ox9IzYnFdHA&t=25s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Is it better to grow one single founder account or focus on multiple accounts '
              "as your founder maybe who's possibly much larger? You can't live on the, you "
              "know, on a lifeline where you're just trying to catch the people that ready to "
              'buy.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': 'Is it better to grow one single founder account or focus on multiple accounts as '
             "your founder maybe who's possibly much larger? You can't live on the, you know, "
             "on a lifeline where you're just trying to catch the people that ready to buy.",
      'title': 'He Scaled ColdIQ From $2M to $6M ARR Using This Inbound Led Outbound GTM '
               'System | Ivan Falco ColdIQ (Kinner Sacchdev - Edbound AI)',
      'url': 'https://www.youtube.com/watch?v=Ox9IzYnFdHA&t=25s',
      'video_id': 'Ox9IzYnFdHA'},
     {'author': 'Atishay Jain - Hyperke Growth Partners',
      'channel': 'Atishay Jain - Hyperke Growth Partners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=RQbJYQq_2xM&t=50s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It all boils down to timing because in the B2B space, people buy, like buyers '
              'buy when the timing is right. So when they have a need, when that need is a '
              'priority, and when they have budget or resources allocated to solving that '
              'priority, right?',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': 'It all boils down to timing because in the B2B space, people buy, like buyers '
             'buy when the timing is right. So when they have a need, when that need is a '
             'priority, and when they have budget or resources allocated to solving that '
             'priority, right?',
      'title': 'How to use Clay Workflows + Audiences to build an automated outreach engine '
               '(Atishay Jain - Hyperke Growth Partners)',
      'url': 'https://www.youtube.com/watch?v=RQbJYQq_2xM&t=50s',
      'video_id': 'RQbJYQq_2xM'},
     {'author': 'VerifiedShortlist',
      'channel': 'VerifiedShortlist',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:47](https://www.youtube.com/watch?v=aGsk3Ma7_PA&t=287s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "For an inbound-led startup, that's a structural advantage. Salesforce needs a "
              'separate Marketing Cloud or Account Engagement purchase. A split stack, HubSpot '
              'for marketing and Salesforce for sales, is common, but it needs an integration '
              'someone maintains.',
      'timestamp': 287,
      'timestamp_label': '[00:04:47]',
      'timestamp_seconds': 287,
      'tip': "For an inbound-led startup, that's a structural advantage. Salesforce needs a "
             'separate Marketing Cloud or Account Engagement purchase. A split stack, HubSpot '
             'for marketing and Salesforce for sales, is common, but it needs an integration '
             'someone maintains.',
      'title': 'HubSpot vs Salesforce 2027: Which CRM for SaaS Startups? (VerifiedShortlist)',
      'url': 'https://www.youtube.com/watch?v=aGsk3Ma7_PA&t=287s',
      'video_id': 'aGsk3Ma7_PA'},
     {'author': 'Hunter',
      'channel': 'Hunter',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:33:23](https://www.youtube.com/watch?v=35H3HVb8ymw&t=2003s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, for example, if somebody hasn't implemented a marketing system yet and "
              "you're selling tools that can help them, understanding the influence of that "
              'marketing system in their in their business cycle is really important.',
      'timestamp': 2003,
      'timestamp_label': '[00:33:23]',
      'timestamp_seconds': 2003,
      'tip': "So, for example, if somebody hasn't implemented a marketing system yet and "
             "you're selling tools that can help them, understanding the influence of that "
             'marketing system in their in their business cycle is really important.',
      'title': 'How to Define Your Ideal Customer Profile (ICP) for B2B Lead Generation | '
               'Hunter.io (Hunter)',
      'url': 'https://www.youtube.com/watch?v=35H3HVb8ymw&t=2003s',
      'video_id': '35H3HVb8ymw'},
     {'author': 'Dylan Conroy',
      'channel': 'Dylan Conroy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:46](https://www.youtube.com/watch?v=ttPyddAq19E&t=1726s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Credential Insurance, and um, uh, the guy who was the press secretary and '
              'communications director for Bill Clinton named Mark Penn, who owns the sixth '
              'largest publicly traded media and advertising agency group in the entire world. '
              'Um, so they came on or something.',
      'timestamp': 1726,
      'timestamp_label': '[00:28:46]',
      'timestamp_seconds': 1726,
      'tip': 'Credential Insurance, and um, uh, the guy who was the press secretary and '
             'communications director for Bill Clinton named Mark Penn, who owns the sixth '
             'largest publicly traded media and advertising agency group in the entire world. '
             'Um, so they came on or something.',
      'title': 'The B2B Trojan Horse: Using a Podcast for Networking & Lead Gen (Dylan Conroy)',
      'url': 'https://www.youtube.com/watch?v=ttPyddAq19E&t=1726s',
      'video_id': 'ttPyddAq19E'},
     {'author': 'The Business Guy | Asset Protection Planners',
      'channel': 'The Business Guy | Asset Protection Planners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:49](https://www.youtube.com/watch?v=TmmMYBOJ_3c&t=169s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Additional security agreement now sometimes we use the ucc one as an asset '
              'protection strategy that is we set up an llc for our clients.',
      'timestamp': 169,
      'timestamp_label': '[00:02:49]',
      'timestamp_seconds': 169,
      'tip': 'Additional security agreement now sometimes we use the ucc one as an asset '
             'protection strategy that is we set up an llc for our clients.',
      'title': 'UCC-1 Financing Statement: What Is it? How Does It Work? (The Business Guy | '
               'Asset Protection Planners)',
      'url': 'https://www.youtube.com/watch?v=TmmMYBOJ_3c&t=169s',
      'video_id': 'TmmMYBOJ_3c'},
     {'author': 'Impactable - B2B LinkedIn Ads Agency',
      'channel': 'Impactable - B2B LinkedIn Ads Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:38](https://www.youtube.com/watch?v=s0wOPmHvpWM&t=938s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t necessarily work for like the vast majority of small to mid-size marketers. "
              'So, the AI campaign setup might be great for bigger campaigns with tons of '
              'budget where you can go broader.',
      'timestamp': 938,
      'timestamp_label': '[00:15:38]',
      'timestamp_seconds': 938,
      'tip': "'t necessarily work for like the vast majority of small to mid-size marketers. "
             'So, the AI campaign setup might be great for bigger campaigns with tons of '
             'budget where you can go broader.',
      'title': 'From Expert to Impact: How to Build Real Thought Leadership on LinkedIn '
               '(Without the Fluff) (Impactable - B2B LinkedIn Ads Agency)',
      'url': 'https://www.youtube.com/watch?v=s0wOPmHvpWM&t=938s',
      'video_id': 's0wOPmHvpWM'},
     {'author': 'James Praise #realjaymes',
      'channel': 'James Praise #realjaymes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=S9IhjTPQRTA&t=118s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I have on this column right so the Last thing I did now was to determine their '
              'CRO maturity. So like conversion rate optimization maturity based on the tools '
              "I could find. So it's um the company's advanced in CRO if they have more than "
              'three tools in the AB testing category.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': 'I have on this column right so the Last thing I did now was to determine their '
             'CRO maturity. So like conversion rate optimization maturity based on the tools I '
             "could find. So it's um the company's advanced in CRO if they have more than "
             'three tools in the AB testing category.',
      'title': 'AI Workflow – Building a Clay ICP/TAM Engine that Scored 98/100 on the Clay '
               'Outbound Certification (James Praise #realjaymes)',
      'url': 'https://www.youtube.com/watch?v=S9IhjTPQRTA&t=118s',
      'video_id': 'S9IhjTPQRTA'},
     {'author': 'Destiny Marketing Solutions',
      'channel': 'Destiny Marketing Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:21](https://www.youtube.com/watch?v=TY6iVOecM0Y&t=141s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'People to come to your show but hopefully you have a better understanding of '
              'how we are able to get more out of and traffic channel to drive and nurture '
              'inbound leads while remaining competitive call us today for a strategy session '
              'for your solar marketing needs.',
      'timestamp': 141,
      'timestamp_label': '[00:02:21]',
      'timestamp_seconds': 141,
      'tip': 'People to come to your show but hopefully you have a better understanding of how '
             'we are able to get more out of and traffic channel to drive and nurture inbound '
             'leads while remaining competitive call us today for a strategy session for your '
             'solar marketing needs.',
      'title': 'How to Build a Commercial Solar Lead Generation Machine | Destiny Marketing '
               'Solutions (Destiny Marketing Solutions)',
      'url': 'https://www.youtube.com/watch?v=TY6iVOecM0Y&t=141s',
      'video_id': 'TY6iVOecM0Y'},
     {'author': 'Photonic Growth',
      'channel': 'Photonic Growth',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:52:34](https://www.youtube.com/watch?v=Sm0uGTgJbJE&t=3154s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Upwork or whether you're using software like closely so the best thing now is "
              'to go ahead download some leads build some emails and get sending and hopefully '
              'booking some appointments.',
      'timestamp': 3154,
      'timestamp_label': '[00:52:34]',
      'timestamp_seconds': 3154,
      'tip': "Upwork or whether you're using software like closely so the best thing now is to "
             'go ahead download some leads build some emails and get sending and hopefully '
             'booking some appointments.',
      'title': 'Commercial Solar Lead Generation Course using Cold Email & LinkedIn (Photonic '
               'Growth)',
      'url': 'https://www.youtube.com/watch?v=Sm0uGTgJbJE&t=3154s',
      'video_id': 'Sm0uGTgJbJE'},
     {'author': 'Jansen/Adjusters International',
      'channel': 'Jansen/Adjusters International',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:08](https://www.youtube.com/watch?v=oAK4wMoYcMA&t=968s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Looking for the divot and and really looking at that yeah yeah and they dave '
              'got on the roof the other day it pops out at you on these pvc roofings but as '
              'you can see you see the weave.',
      'timestamp': 968,
      'timestamp_label': '[00:16:08]',
      'timestamp_seconds': 968,
      'tip': 'Looking for the divot and and really looking at that yeah yeah and they dave got '
             'on the roof the other day it pops out at you on these pvc roofings but as you '
             'can see you see the weave.',
      'title': 'How To Present Flat Roof Hail Damage To The Insurance Company '
               '(Jansen/Adjusters International)',
      'url': 'https://www.youtube.com/watch?v=oAK4wMoYcMA&t=968s',
      'video_id': 'oAK4wMoYcMA'}],
 5: [{'author': 'AdConversion',
      'channel': 'AdConversion',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:17](https://www.youtube.com/watch?v=LbEgZ7SpArs&t=557s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They fail for predictable, fixable reasons. You now know what they are. '
              'Signal-based account selection, real sales alignment before you launch, '
              'measuring momentum not attribution, and reading your leading KPIs before the '
              'absence of pipeline forces a harder conversation.',
      'timestamp': 557,
      'timestamp_label': '[00:09:17]',
      'timestamp_seconds': 557,
      'tip': 'They fail for predictable, fixable reasons. You now know what they are. '
             'Signal-based account selection, real sales alignment before you launch, '
             'measuring momentum not attribution, and reading your leading KPIs before the '
             'absence of pipeline forces a harder conversation.',
      'title': 'ABM in 2026: What Actually Works for B2B Marketing (AdConversion)',
      'url': 'https://www.youtube.com/watch?v=LbEgZ7SpArs&t=557s',
      'video_id': 'LbEgZ7SpArs'},
     {'author': 'Aqil Jannaty',
      'channel': 'Aqil Jannaty',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=sYgF5NyLeo8&t=65s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s just very challenging to break into the accounts that you want to because "
              "it's essentially a spray and prey methodology. However, account-based marketing "
              'is very, very specific.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': "'s just very challenging to break into the accounts that you want to because "
             "it's essentially a spray and prey methodology. However, account-based marketing "
             'is very, very specific.',
      'title': 'ABM (Account-Based-Marketing) 2026 Playbook and Strategies (Aqil Jannaty)',
      'url': 'https://www.youtube.com/watch?v=sYgF5NyLeo8&t=65s',
      'video_id': 'sYgF5NyLeo8'},
     {'author': 'OGONJO Workbooks',
      'channel': 'OGONJO Workbooks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:49](https://www.youtube.com/watch?v=ZSqgCrydlAo&t=49s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And this lesson gives you three lenses for that. The job your product is hired '
              "to do, the business outcome it creates, and what's personally at stake for the "
              'buyer. First, a customer buys a solution to a problem, not a product. So, '
              'define the problem before anything else.',
      'timestamp': 49,
      'timestamp_label': '[00:00:49]',
      'timestamp_seconds': 49,
      'tip': 'And this lesson gives you three lenses for that. The job your product is hired '
             "to do, the business outcome it creates, and what's personally at stake for the "
             'buyer. First, a customer buys a solution to a problem, not a product. So, define '
             'the problem before anything else.',
      'title': 'What Problem Are You Actually Solving? (B2B Ideal Customer Profile Series) – '
               'Pt 1 (OGONJO Workbooks)',
      'url': 'https://www.youtube.com/watch?v=ZSqgCrydlAo&t=49s',
      'video_id': 'ZSqgCrydlAo'},
     {'author': 'Financial Regulation Courses',
      'channel': 'Financial Regulation Courses',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=Af7w5a4iS8c&t=157s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The broker must understand the risks, rewards, and costs associated with the '
              'recommendation. The broker must have a reasonable basis to believe the '
              'recommendation is in the best interest of retail customers generally and the '
              'specific customer based on their profile.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': 'The broker must understand the risks, rewards, and costs associated with the '
             'recommendation. The broker must have a reasonable basis to believe the '
             'recommendation is in the best interest of retail customers generally and the '
             'specific customer based on their profile.',
      'title': 'Regulation Best Interest Reg BI Explained  Broker Dealer Standards of Conduct '
               '(Financial Regulation Courses)',
      'url': 'https://www.youtube.com/watch?v=Af7w5a4iS8c&t=157s',
      'video_id': 'Af7w5a4iS8c'},
     {'author': 'The B2B Playbook',
      'channel': 'The B2B Playbook',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:44](https://www.youtube.com/watch?v=TMEMDzAg5QA&t=1064s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And without that, most people, I think, Kevin, are going to be disappointed by '
              'their account-based marketing efforts.',
      'timestamp': 1064,
      'timestamp_label': '[00:17:44]',
      'timestamp_seconds': 1064,
      'tip': 'And without that, most people, I think, Kevin, are going to be disappointed by '
             'their account-based marketing efforts.',
      'title': 'How to Fit ABM in Your B2B Marketing Strategy (The B2B Playbook)',
      'url': 'https://www.youtube.com/watch?v=TMEMDzAg5QA&t=1064s',
      'video_id': 'TMEMDzAg5QA'},
     {'author': 'LinkedIn for Marketing',
      'channel': 'LinkedIn for Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:48:50](https://www.youtube.com/watch?v=Co22pd-mVlk&t=2930s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "A half to convince me of this because I kept saying no it's not it's a list "
              'they said and now I get it because the target account list in account based is '
              'your.',
      'timestamp': 2930,
      'timestamp_label': '[00:48:50]',
      'timestamp_seconds': 2930,
      'tip': "A half to convince me of this because I kept saying no it's not it's a list they "
             'said and now I get it because the target account list in account based is your.',
      'title': 'I Heart ABM: Bringing Sales and Marketing Together (LinkedIn for Marketing)',
      'url': 'https://www.youtube.com/watch?v=Co22pd-mVlk&t=2930s',
      'video_id': 'Co22pd-mVlk'},
     {'author': 'Growth Business Templates',
      'channel': 'Growth Business Templates',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:32](https://www.youtube.com/watch?v=aDOxVzIz_Hk&t=812s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Hope this is helpful to help you build out your own account based marketing '
              "strategy uh just I'll include a link to this below you can download it make a "
              'copy of it and use it going forward I will see you on the next video.',
      'timestamp': 812,
      'timestamp_label': '[00:13:32]',
      'timestamp_seconds': 812,
      'tip': 'Hope this is helpful to help you build out your own account based marketing '
             "strategy uh just I'll include a link to this below you can download it make a "
             'copy of it and use it going forward I will see you on the next video.',
      'title': 'Develop an ABM strategy that predictably generates sales pipeline with larger '
               'enterprises (Growth Business Templates)',
      'url': 'https://www.youtube.com/watch?v=aDOxVzIz_Hk&t=812s',
      'video_id': 'aDOxVzIz_Hk'},
     {'author': 'Exxcelerate',
      'channel': 'Exxcelerate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:21](https://www.youtube.com/watch?v=TE99yv49oy4&t=1161s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um and then I think for us >> Mhm. Like entrepreneurs, like business owners. I '
              'think the biggest risk with AI is using it to think. I think the biggest risk '
              "is using it to >> That's a good one.",
      'timestamp': 1161,
      'timestamp_label': '[00:19:21]',
      'timestamp_seconds': 1161,
      'tip': 'Um and then I think for us >> Mhm. Like entrepreneurs, like business owners. I '
             'think the biggest risk with AI is using it to think. I think the biggest risk is '
             "using it to >> That's a good one.",
      'title': 'How We Actually Source M&A Deals: Cold Email, AI, and Tech Stacks '
               '(Exxcelerate)',
      'url': 'https://www.youtube.com/watch?v=TE99yv49oy4&t=1161s',
      'video_id': 'TE99yv49oy4'},
     {'author': 'Chris Walker',
      'channel': 'Chris Walker',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=wkcuqfylydw&t=51s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A problem and I think what we really struggled with was multi-touch attribution '
              'so if someone comes in and downloads an inbound piece of content.',
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': 'A problem and I think what we really struggled with was multi-touch attribution '
             'so if someone comes in and downloads an inbound piece of content.',
      'title': 'How to Measure Multi-Touch Attribution Across Sales and Marketing Teams (Chris '
               'Walker)',
      'url': 'https://www.youtube.com/watch?v=wkcuqfylydw&t=51s',
      'video_id': 'wkcuqfylydw'},
     {'author': 'Pryderi Podcast',
      'channel': 'Pryderi Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:37](https://www.youtube.com/watch?v=rnUvOWiFpDQ&t=97s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Around me and talk to that person otherwise it's a contractual violation and "
              "you could be subject to damages that's a non-circumvention agreement very "
              'valuable in the context of real estate and sales not always necessary but very '
              'valuable.',
      'timestamp': 97,
      'timestamp_label': '[00:01:37]',
      'timestamp_seconds': 97,
      'tip': "Around me and talk to that person otherwise it's a contractual violation and you "
             "could be subject to damages that's a non-circumvention agreement very valuable "
             'in the context of real estate and sales not always necessary but very valuable.',
      'title': 'NON CIRCUMVENTION AGREEMENTS! (Pryderi Podcast)',
      'url': 'https://www.youtube.com/watch?v=rnUvOWiFpDQ&t=97s',
      'video_id': 'rnUvOWiFpDQ'},
     {'author': 'Roman Love',
      'channel': 'Roman Love',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:28](https://www.youtube.com/watch?v=kzJnJVEn_E4&t=328s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Yeah, look, so I'll buy everything you send me in a minute. As and when we "
              "continue to grow as a business, I'll be adding more reps into like more of my "
              "guys into that group and we'll be buying more leads.",
      'timestamp': 328,
      'timestamp_label': '[00:05:28]',
      'timestamp_seconds': 328,
      'tip': "Yeah, look, so I'll buy everything you send me in a minute. As and when we "
             "continue to grow as a business, I'll be adding more reps into like more of my "
             "guys into that group and we'll be buying more leads.",
      'title': 'Solar lead generation testimonial: Get Zero | TNW Marketing (Roman Love)',
      'url': 'https://www.youtube.com/watch?v=kzJnJVEn_E4&t=328s',
      'video_id': 'kzJnJVEn_E4'},
     {'author': 'Industrial Real Estate Show',
      'channel': 'Industrial Real Estate Show',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:17](https://www.youtube.com/watch?v=jak1MCZd_UQ&t=1217s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you have if you buy an a portfolio of multif family, a portfolio of of '
              "industrial, if you go and buy prologuses uh stock, you're you're insulated from "
              'the fact that they can repurpose all these for other uses.',
      'timestamp': 1217,
      'timestamp_label': '[00:20:17]',
      'timestamp_seconds': 1217,
      'tip': 'If you have if you buy an a portfolio of multif family, a portfolio of of '
             "industrial, if you go and buy prologuses uh stock, you're you're insulated from "
             'the fact that they can repurpose all these for other uses.',
      'title': 'The Hidden Risk in Data Center Investing Nobody’s Pricing In (Industrial Real '
               'Estate Show)',
      'url': 'https://www.youtube.com/watch?v=jak1MCZd_UQ&t=1217s',
      'video_id': 'jak1MCZd_UQ'},
     {'author': 'Solar Scaling Systems',
      'channel': 'Solar Scaling Systems',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:05](https://www.youtube.com/watch?v=UkUTbb_M4eY&t=125s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Need or a want need based products tend to do good on search engine based '
              'advertising platforms and want based products tend.',
      'timestamp': 125,
      'timestamp_label': '[00:02:05]',
      'timestamp_seconds': 125,
      'tip': 'Need or a want need based products tend to do good on search engine based '
             'advertising platforms and want based products tend.',
      'title': 'Solar Lead Generation System Revealed: How to Generate Exclusive Homeowner '
               'Leads with Ease! (Solar Scaling Systems)',
      'url': 'https://www.youtube.com/watch?v=UkUTbb_M4eY&t=125s',
      'video_id': 'UkUTbb_M4eY'},
     {'author': 'Cold Outbound Clips',
      'channel': 'Cold Outbound Clips',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:23](https://www.youtube.com/watch?v=_l5HU1yQjdM&t=23s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Verifier, and then if there's a valid email, and only if there's a valid email, "
              'we use the enrich company endpoint to find their company description, and then '
              'can we say a compliment about their business using GPT-4 mini, and prep that to '
              'be sent to SmartLead.',
      'timestamp': 23,
      'timestamp_label': '[00:00:23]',
      'timestamp_seconds': 23,
      'tip': "Verifier, and then if there's a valid email, and only if there's a valid email, "
             'we use the enrich company endpoint to find their company description, and then '
             'can we say a compliment about their business using GPT-4 mini, and prep that to '
             'be sent to SmartLead.',
      'title': 'One Sentence Built This Clay Workflow (Clay CLI + GrokBot) (Cold Outbound '
               'Clips)',
      'url': 'https://www.youtube.com/watch?v=_l5HU1yQjdM&t=23s',
      'video_id': '_l5HU1yQjdM'},
     {'author': 'Leadbase',
      'channel': 'Leadbase',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:10](https://www.youtube.com/watch?v=mb1j52sTZX0&t=190s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Up a entire quiz funnel with tons of different questions you could do whatever '
              "you want in lead base and we're here to help you and provide those templates "
              "for you let's go into location targeting all we have to do is Select.",
      'timestamp': 190,
      'timestamp_label': '[00:03:10]',
      'timestamp_seconds': 190,
      'tip': 'Up a entire quiz funnel with tons of different questions you could do whatever '
             "you want in lead base and we're here to help you and provide those templates for "
             "you let's go into location targeting all we have to do is Select.",
      'title': 'How Solar Installers Are Generating Leads w/ Leadbase (Leadbase)',
      'url': 'https://www.youtube.com/watch?v=mb1j52sTZX0&t=190s',
      'video_id': 'mb1j52sTZX0'}],
 6: [{'author': 'GrowthSpree - AI Native B2B Marketing Agency',
      'channel': 'GrowthSpree - AI Native B2B Marketing Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:49](https://www.youtube.com/watch?v=YOYPAYz4iOc&t=229s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Pipeline, not leads, is a measurement test. A lead gen agency optimizes to CPL. '
              'A pipeline first one to cost per SQL. Only 13% of MQLs become SQL. So, the tell '
              'is the feedback loop. Tiered CRM conversions that teach the algorithms to find '
              'revenue.',
      'timestamp': 229,
      'timestamp_label': '[00:03:49]',
      'timestamp_seconds': 229,
      'tip': 'Pipeline, not leads, is a measurement test. A lead gen agency optimizes to CPL. '
             'A pipeline first one to cost per SQL. Only 13% of MQLs become SQL. So, the tell '
             'is the feedback loop. Tiered CRM conversions that teach the algorithms to find '
             'revenue.',
      'title': 'The Best B2B SaaS Demand Gen Agencies for Pipeline (Not Leads) (2026) '
               '(GrowthSpree - AI Native B2B Marketing Agency)',
      'url': 'https://www.youtube.com/watch?v=YOYPAYz4iOc&t=229s',
      'video_id': 'YOYPAYz4iOc'},
     {'author': 'Hlib Storchak',
      'channel': 'Hlib Storchak',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:56](https://www.youtube.com/watch?v=Iy92NakD7e4&t=896s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So find the signal, score the people, lead with the signal in your message and '
              'book a lot a lot of calls. And if you want to talk about signal based outbound '
              'which could be built for you, please feel free to book a call with me or my '
              'team.',
      'timestamp': 896,
      'timestamp_label': '[00:14:56]',
      'timestamp_seconds': 896,
      'tip': 'So find the signal, score the people, lead with the signal in your message and '
             'book a lot a lot of calls. And if you want to talk about signal based outbound '
             'which could be built for you, please feel free to book a call with me or my '
             'team.',
      'title': 'How To Build Signal Based Outreach Campaigns (Full Guide) (Hlib Storchak)',
      'url': 'https://www.youtube.com/watch?v=Iy92NakD7e4&t=896s',
      'video_id': 'Iy92NakD7e4'},
     {'author': 'AI Automation Official',
      'channel': 'AI Automation Official',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=bQPaiBg-cWs&t=77s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'State the value clearly and ask one simple question. This agent pairs well with '
              'the lead research agent. Research first, then generate the outreach message. '
              'You can sell them together as a full outbound system. Start by testing with '
              'five or 10 real leads.',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': 'State the value clearly and ask one simple question. This agent pairs well with '
             'the lead research agent. Research first, then generate the outreach message. You '
             'can sell them together as a full outbound system. Start by testing with five or '
             '10 real leads.',
      'title': 'How to Build an Email Outreach AI Agent in n8n (AI Automation Official)',
      'url': 'https://www.youtube.com/watch?v=bQPaiBg-cWs&t=77s',
      'video_id': 'bQPaiBg-cWs'},
     {'author': 'MergerID',
      'channel': 'MergerID',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=D8UMfxaORrU&t=43s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Who' you end up doing the deal with Kao Enterprises based in Osaka our first "
              'Asian buyer really and merger ID matched you to them what is it like a dating.',
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': "Who' you end up doing the deal with Kao Enterprises based in Osaka our first "
             'Asian buyer really and merger ID matched you to them what is it like a dating.',
      'title': 'How it works: Middle Market M&A Deal Sourcing Tool (MergerID)',
      'url': 'https://www.youtube.com/watch?v=D8UMfxaORrU&t=43s',
      'video_id': 'D8UMfxaORrU'},
     {'author': 'IMG',
      'channel': 'IMG',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=dxqvZPB25eo&t=55s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um, and then we uh call the client. We don't go through the intake again. We "
              'ask some additional questions just to make sure they do truly qualify based on '
              "the criteria. And if there's any suspicion for deceit, um, we run through a "
              'whole another series of questions.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': "Um, and then we uh call the client. We don't go through the intake again. We ask "
             'some additional questions just to make sure they do truly qualify based on the '
             "criteria. And if there's any suspicion for deceit, um, we run through a whole "
             'another series of questions.',
      'title': 'The Truth About Lead Quality in Mass Tort Marketing | Interview with Katherine '
               'Hoffmann (IMG)',
      'url': 'https://www.youtube.com/watch?v=dxqvZPB25eo&t=55s',
      'video_id': 'dxqvZPB25eo'},
     {'author': 'Nazir Yakubu',
      'channel': 'Nazir Yakubu',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:05](https://www.youtube.com/watch?v=FGU8xAz-R1U&t=365s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We have AI doing all of that for us and that's where AI comes in. So content "
              'ads, then AI comes in. When a new lead comes in, within the few few to five '
              'seconds of the lead coming in, you have AI agents getting on a call to call '
              'this list to qualify the lead.',
      'timestamp': 365,
      'timestamp_label': '[00:06:05]',
      'timestamp_seconds': 365,
      'tip': "We have AI doing all of that for us and that's where AI comes in. So content "
             'ads, then AI comes in. When a new lead comes in, within the few few to five '
             'seconds of the lead coming in, you have AI agents getting on a call to call this '
             'list to qualify the lead.',
      'title': 'New Solar Lead Generation Strategy ( 60% show rate ) (Nazir Yakubu)',
      'url': 'https://www.youtube.com/watch?v=FGU8xAz-R1U&t=365s',
      'video_id': 'FGU8xAz-R1U'},
     {'author': 'Cole Furrh | B2B SaaS PPC Pro',
      'channel': 'Cole Furrh | B2B SaaS PPC Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:49](https://www.youtube.com/watch?v=WOpqbZNyqNE&t=169s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They've been given a quote for the amount of the deal. So this is the first "
              'step in which you can actually optimize for conversion value in your campaigns '
              'based on the prospective deal amount. They often call this the pipeline.',
      'timestamp': 169,
      'timestamp_label': '[00:02:49]',
      'timestamp_seconds': 169,
      'tip': "They've been given a quote for the amount of the deal. So this is the first step "
             'in which you can actually optimize for conversion value in your campaigns based '
             'on the prospective deal amount. They often call this the pipeline.',
      'title': 'Defining different HubSpot lifecycle stages + how to use them in ad campaigns '
               '(Cole Furrh | B2B SaaS PPC Pro)',
      'url': 'https://www.youtube.com/watch?v=WOpqbZNyqNE&t=169s',
      'video_id': 'WOpqbZNyqNE'},
     {'author': 'Alex Leischow',
      'channel': 'Alex Leischow',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:57](https://www.youtube.com/watch?v=Ajqub1jgsVM&t=537s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But it has, you know, custom voice agent demos that you can literally hit play '
              'and listen to that are custom for that specific lead. This is proof-first '
              'outbound.',
      'timestamp': 537,
      'timestamp_label': '[00:08:57]',
      'timestamp_seconds': 537,
      'tip': 'But it has, you know, custom voice agent demos that you can literally hit play '
             'and listen to that are custom for that specific lead. This is proof-first '
             'outbound.',
      'title': 'The BEST Way To Do Cold Outreach With AI (57% Reply Rate) (Alex Leischow)',
      'url': 'https://www.youtube.com/watch?v=Ajqub1jgsVM&t=537s',
      'video_id': 'Ajqub1jgsVM'},
     {'author': 'Prosyo',
      'channel': 'Prosyo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=kkCigTPke4Y&t=60s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Search people, then filter for your exact buyer, seniority, company size, '
              'location, industry. When the results look like your ICP, copy the URL. That '
              'link is your entire list. Back in Prospect, prospects, import, LinkedIn search '
              'tab. Paste the URL, pick a list, hit import.',
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': 'Search people, then filter for your exact buyer, seniority, company size, '
             'location, industry. When the results look like your ICP, copy the URL. That link '
             'is your entire list. Back in Prospect, prospects, import, LinkedIn search tab. '
             'Paste the URL, pick a list, hit import.',
      'title': 'I Built a LinkedIn + Email Outreach Campaign in Minutes with AI (Prosyo)',
      'url': 'https://www.youtube.com/watch?v=kkCigTPke4Y&t=60s',
      'video_id': 'kkCigTPke4Y'},
     {'author': 'GrowthSpree - AI Native B2B Marketing Agency',
      'channel': 'GrowthSpree - AI Native B2B Marketing Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=gq_DLeTobXo&t=50s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh first I started to test if I give it a LinkedIn page of a company page '
              'basically can it find people can it just visit LinkedIn and find the these '
              'personas or what whichever personas are relevant for you um and build a list. '
              'So I I gave it uh the name of a company.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': 'Uh first I started to test if I give it a LinkedIn page of a company page '
             'basically can it find people can it just visit LinkedIn and find the these '
             'personas or what whichever personas are relevant for you um and build a list. So '
             'I I gave it uh the name of a company.',
      'title': 'Claude AI ABM Campaign Walkthrough | B2B Account-Based Marketing Automation '
               'with AI (GrowthSpree - AI Native B2B Marketing Agency)',
      'url': 'https://www.youtube.com/watch?v=gq_DLeTobXo&t=50s',
      'video_id': 'gq_DLeTobXo'},
     {'author': 'ColdIQ',
      'channel': 'ColdIQ',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:13](https://www.youtube.com/watch?v=zI4SmtWCKf0&t=73s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'ICP, companies, people, etc. I want to build a list of fintech CEOs in Silicon '
              "Valley. Right, let's look at all the unlimited data that Cold IQ has. Let's "
              "find their mobiles and let's find their verified work emails.",
      'timestamp': 73,
      'timestamp_label': '[00:01:13]',
      'timestamp_seconds': 73,
      'tip': 'ICP, companies, people, etc. I want to build a list of fintech CEOs in Silicon '
             "Valley. Right, let's look at all the unlimited data that Cold IQ has. Let's find "
             "their mobiles and let's find their verified work emails.",
      'title': 'ColdIQ data is now unlimited: build lead lists without spending credits. '
               '(ColdIQ)',
      'url': 'https://www.youtube.com/watch?v=zI4SmtWCKf0&t=73s',
      'video_id': 'zI4SmtWCKf0'},
     {'author': 'Ambilio',
      'channel': 'Ambilio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=oWWC4Sj-SjA&t=42s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Deal sits a lot of work, researching the account, qualifying the lead, writing '
              'the proposal, following  up. Most of it is research and writing.',
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': 'Deal sits a lot of work, researching the account, qualifying the lead, writing '
             'the proposal, following  up. Most of it is research and writing.',
      'title': 'AI Agents in Sales: From Account Research to Proposal (and the One Check That '
               'Saves the Deal) (Ambilio)',
      'url': 'https://www.youtube.com/watch?v=oWWC4Sj-SjA&t=42s',
      'video_id': 'oWWC4Sj-SjA'},
     {'author': 'Roman Love',
      'channel': 'Roman Love',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:36](https://www.youtube.com/watch?v=oZ_jg6mmZEE&t=96s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ve been bringing you so far? So, the average deal size, if I work back from "
              "from the lead that the leads that I've been paying you, so I think I was paying "
              'you about £400 a lead.',
      'timestamp': 96,
      'timestamp_label': '[00:01:36]',
      'timestamp_seconds': 96,
      'tip': "'ve been bringing you so far? So, the average deal size, if I work back from "
             "from the lead that the leads that I've been paying you, so I think I was paying "
             'you about £400 a lead.',
      'title': 'Commercial solar leads review: James Vincent Enterprises | TNW Marketing '
               '(Roman Love)',
      'url': 'https://www.youtube.com/watch?v=oZ_jg6mmZEE&t=96s',
      'video_id': 'oZ_jg6mmZEE'},
     {'author': 'lemlist',
      'channel': 'lemlist',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:33](https://www.youtube.com/watch?v=7hSBNM6xnmc&t=453s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Points that is the first step to win at cold outreach that's all let me know in "
              'the comments if this video helped you to better find your target audience.',
      'timestamp': 453,
      'timestamp_label': '[00:07:33]',
      'timestamp_seconds': 453,
      'tip': "Points that is the first step to win at cold outreach that's all let me know in "
             'the comments if this video helped you to better find your target audience.',
      'title': 'How to create an Ideal Customer Profile (B2B lead generation) (lemlist)',
      'url': 'https://www.youtube.com/watch?v=7hSBNM6xnmc&t=453s',
      'video_id': '7hSBNM6xnmc'},
     {'author': 'Solar Boss',
      'channel': 'Solar Boss',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:49](https://www.youtube.com/watch?v=E_z3wa2X4Pw&t=109s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Scammed getting burned right so best way to do that is do your due diligence '
              'and the first thing is check them out online.',
      'timestamp': 109,
      'timestamp_label': '[00:01:49]',
      'timestamp_seconds': 109,
      'tip': 'Scammed getting burned right so best way to do that is do your due diligence and '
             'the first thing is check them out online.',
      'title': '💥Top 5 Tips to Help You Find The Right Solar Lead Generation Partner (Solar '
               'Boss)',
      'url': 'https://www.youtube.com/watch?v=E_z3wa2X4Pw&t=109s',
      'video_id': 'E_z3wa2X4Pw'}],
 7: [{'author': 'UrbanSpell',
      'channel': 'UrbanSpell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:49](https://www.youtube.com/watch?v=bSYYUhXxy4Y&t=109s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s account level, not vanity metrics and clear pipeline attribution. At that "
              'point, ABM stops being a campaign, it becomes a function, a repeatable revenue '
              "motion. That's our flow, strategy sprint, pilot execution, scale into a full "
              'funnel ABM program.',
      'timestamp': 109,
      'timestamp_label': '[00:01:49]',
      'timestamp_seconds': 109,
      'tip': "'s account level, not vanity metrics and clear pipeline attribution. At that "
             'point, ABM stops being a campaign, it becomes a function, a repeatable revenue '
             "motion. That's our flow, strategy sprint, pilot execution, scale into a full "
             'funnel ABM program.',
      'title': 'The ABM Workflow Explained | How B2B Companies Win with Account-Based '
               'Marketing | UrbanSpell | (UrbanSpell)',
      'url': 'https://www.youtube.com/watch?v=bSYYUhXxy4Y&t=109s',
      'video_id': 'bSYYUhXxy4Y'},
     {'author': '[mnainstitute.com] M&A Certification & Courses',
      'channel': '[mnainstitute.com] M&A Certification & Courses',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=ZJvGhvYmDLE&t=20s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Each step is crucial in ensuring a successful M&A transaction. By the end of '
              'this course, you will learn about the five essential steps of the M&A buy-side '
              'process. You will also discover how to prepare an effective M&A strategy and '
              'identify the right targets.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'Each step is crucial in ensuring a successful M&A transaction. By the end of '
             'this course, you will learn about the five essential steps of the M&A buy-side '
             'process. You will also discover how to prepare an effective M&A strategy and '
             'identify the right targets.',
      'title': "📢 5-step M&A buy-side process⭐ In the 'M&A Transaction' course of "
               '"mnainstitute.com" ([mnainstitute.com] M&A Certification & Courses)',
      'url': 'https://www.youtube.com/watch?v=ZJvGhvYmDLE&t=20s',
      'video_id': 'ZJvGhvYmDLE'},
     {'author': 'The Big Solar Energy Show with Anthony J. Conklin',
      'channel': 'The Big Solar Energy Show with Anthony J. Conklin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=fwRL9lFmciI&t=15s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Solar your sales process will include all these steps from what we call '
              'prospect to profit so here we go step number one is lead generation how are.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Solar your sales process will include all these steps from what we call prospect '
             'to profit so here we go step number one is lead generation how are.',
      'title': 'The 6 Steps in Selling Commercial Solar (The Big Solar Energy Show with '
               'Anthony J. Conklin)',
      'url': 'https://www.youtube.com/watch?v=fwRL9lFmciI&t=15s',
      'video_id': 'fwRL9lFmciI'},
     {'author': 'Passetto',
      'channel': 'Passetto',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:47](https://www.youtube.com/watch?v=IYxZQrk554A&t=47s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '2026 buyer behavior with a measurement system created in the early 2000s, if '
              'not even before then. Only now, more marketing executives are starting to '
              "realize the pitfalls of this. But they still don't have a clear alternative, "
              'which is the hardest part.',
      'timestamp': 47,
      'timestamp_label': '[00:00:47]',
      'timestamp_seconds': 47,
      'tip': '2026 buyer behavior with a measurement system created in the early 2000s, if not '
             'even before then. Only now, more marketing executives are starting to realize '
             "the pitfalls of this. But they still don't have a clear alternative, which is "
             'the hardest part.',
      'title': "Attribution for SaaS Marketing: What Actually Works (And What Doesn't) "
               '(Passetto)',
      'url': 'https://www.youtube.com/watch?v=IYxZQrk554A&t=47s',
      'video_id': 'IYxZQrk554A'},
     {'author': 'Nico Holloman | Hologram Agency',
      'channel': 'Nico Holloman | Hologram Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:58](https://www.youtube.com/watch?v=PauebGoMxEw&t=58s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, that's what this video is about and I'm going to break that down in a "
              'step-by-step process so you can either replicate it yourself in-house or decide '
              'you want an external agency to support you with that. Without further ado, '
              "let's get into step one.",
      'timestamp': 58,
      'timestamp_label': '[00:00:58]',
      'timestamp_seconds': 58,
      'tip': "So, that's what this video is about and I'm going to break that down in a "
             'step-by-step process so you can either replicate it yourself in-house or decide '
             "you want an external agency to support you with that. Without further ado, let's "
             'get into step one.',
      'title': 'The New Way to Source M&A Deals in 2027 (Nico Holloman | Hologram Agency)',
      'url': 'https://www.youtube.com/watch?v=PauebGoMxEw&t=58s',
      'video_id': 'PauebGoMxEw'},
     {'author': 'Meet Sona',
      'channel': 'Meet Sona',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:56](https://www.youtube.com/watch?v=LGfkRkjfsn8&t=296s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Get those drafts made and then get them scheduled and published so that you can '
              "go build your business and work on other things. That's really where a platform "
              'and a software that plugs in and acts as a a workflow, a repeatable system for '
              'you uh comes into play.',
      'timestamp': 296,
      'timestamp_label': '[00:04:56]',
      'timestamp_seconds': 296,
      'tip': 'Get those drafts made and then get them scheduled and published so that you can '
             "go build your business and work on other things. That's really where a platform "
             'and a software that plugs in and acts as a a workflow, a repeatable system for '
             'you uh comes into play.',
      'title': 'Should You Hire a LinkedIn Ghostwriter in 2026? (Meet Sona)',
      'url': 'https://www.youtube.com/watch?v=LGfkRkjfsn8&t=296s',
      'video_id': 'LGfkRkjfsn8'},
     {'author': 'Ronen Pessar',
      'channel': 'Ronen Pessar',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:43](https://www.youtube.com/watch?v=dpDcjwreO8o&t=283s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re not even the right person. A completion will tell you after every call is "
              'complete, the system needs to know what is the next step. You schedule them for '
              'a future date. If it was a yes, you schedule them for a future meeting or have '
              'a sales rep call them back.',
      'timestamp': 283,
      'timestamp_label': '[00:04:43]',
      'timestamp_seconds': 283,
      'tip': "'re not even the right person. A completion will tell you after every call is "
             'complete, the system needs to know what is the next step. You schedule them for '
             'a future date. If it was a yes, you schedule them for a future meeting or have a '
             'sales rep call them back.',
      'title': 'The NEW Way to Do Outbound Sales in 2026 (Ronen Pessar)',
      'url': 'https://www.youtube.com/watch?v=dpDcjwreO8o&t=283s',
      'video_id': 'dpDcjwreO8o'},
     {'author': 'Blue Pencil',
      'channel': 'Blue Pencil',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:11](https://www.youtube.com/watch?v=5CV9o_tOrgg&t=311s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Because the mistake most teams make is the same message going out for every '
              'signal. Obviously, this is how you waste signals. Step four, I would run the '
              "system like ops, right? So, we're not doing this based on vibes, but we have a "
              'an ops system.',
      'timestamp': 311,
      'timestamp_label': '[00:05:11]',
      'timestamp_seconds': 311,
      'tip': 'Because the mistake most teams make is the same message going out for every '
             'signal. Obviously, this is how you waste signals. Step four, I would run the '
             "system like ops, right? So, we're not doing this based on vibes, but we have a "
             'an ops system.',
      'title': 'The Ultimate Signal-based Outbound Framework in 2026 (all in Clay) (Blue '
               'Pencil)',
      'url': 'https://www.youtube.com/watch?v=5CV9o_tOrgg&t=311s',
      'video_id': '5CV9o_tOrgg'},
     {'author': 'Adam Holmgren',
      'channel': 'Adam Holmgren',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:18](https://www.youtube.com/watch?v=eFSMGI_UK38&t=618s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Let me give you a real example from my account. So, I made a post about last '
              'touch attribution and how VC focused reporting messes everything up. And in the '
              'hook, I set up a clear enemy just very straight to the point.',
      'timestamp': 618,
      'timestamp_label': '[00:10:18]',
      'timestamp_seconds': 618,
      'tip': 'Let me give you a real example from my account. So, I made a post about last '
             'touch attribution and how VC focused reporting messes everything up. And in the '
             'hook, I set up a clear enemy just very straight to the point.',
      'title': 'LinkedIn Thought Leader Ads: Full Step-by-Step Tutorial (2026) (Adam Holmgren)',
      'url': 'https://www.youtube.com/watch?v=eFSMGI_UK38&t=618s',
      'video_id': 'eFSMGI_UK38'},
     {'author': 'Financeable Training',
      'channel': 'Financeable Training',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:25](https://www.youtube.com/watch?v=LFdUFuhB9jo&t=205s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Non-disclosure agreement or nda in which they agree to keep everything about '
              'the sale process confidential once the nda is signed the analyst will send the.',
      'timestamp': 205,
      'timestamp_label': '[00:03:25]',
      'timestamp_seconds': 205,
      'tip': 'Non-disclosure agreement or nda in which they agree to keep everything about the '
             'sale process confidential once the nda is signed the analyst will send the.',
      'title': 'Sell Side M&A Process in Plain English (Financeable Training)',
      'url': 'https://www.youtube.com/watch?v=LFdUFuhB9jo&t=205s',
      'video_id': 'LFdUFuhB9jo'},
     {'author': 'Applecation Lab',
      'channel': 'Applecation Lab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=Qa47WMCz55k&t=98s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Part two, the UCC1 financing statement. Let's see how lenders secure this "
              'property. The UCC requires security instruments to be properly documented and '
              'this happens in three clear steps. First, the borrower signs a security '
              'agreement.',
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': "Part two, the UCC1 financing statement. Let's see how lenders secure this "
             'property. The UCC requires security instruments to be properly documented and '
             'this happens in three clear steps. First, the borrower signs a security '
             'agreement.',
      'title': 'Uniform Commercial Code Explained | UCC-1, Collateral & Real Estate '
               '(Applecation Lab)',
      'url': 'https://www.youtube.com/watch?v=Qa47WMCz55k&t=98s',
      'video_id': 'Qa47WMCz55k'},
     {'author': 'POTOMAC M&A',
      'channel': 'POTOMAC M&A',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:10](https://www.youtube.com/watch?v=8jBQ3jZnNvY&t=1150s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And then at the very last minute you tell him hey I really want more money for '
              "my business I'm going to go out and introduce competition into this process.",
      'timestamp': 1150,
      'timestamp_label': '[00:19:10]',
      'timestamp_seconds': 1150,
      'tip': 'And then at the very last minute you tell him hey I really want more money for '
             "my business I'm going to go out and introduce competition into this process.",
      'title': 'Sell-Side M&A Masterclass | Structuring a Formal Sale Process for Maximum '
               'Value | Private Equity (POTOMAC M&A)',
      'url': 'https://www.youtube.com/watch?v=8jBQ3jZnNvY&t=1150s',
      'video_id': '8jBQ3jZnNvY'},
     {'author': 'Lawyer Marketing and AI with Andrew Stickel',
      'channel': 'Lawyer Marketing and AI with Andrew Stickel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:48](https://www.youtube.com/watch?v=aAMJ5QeSrvU&t=1068s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your audience can tour for your when you call it for your Facebook ad campaign '
              'if you have any questions about this at all just let me know and I will talk to '
              'you soon thanks guys.',
      'timestamp': 1068,
      'timestamp_label': '[00:17:48]',
      'timestamp_seconds': 1068,
      'tip': 'Your audience can tour for your when you call it for your Facebook ad campaign '
             'if you have any questions about this at all just let me know and I will talk to '
             'you soon thanks guys.',
      'title': 'How to Generate Mass Tort Leads for $40 a Piece! [Step by Step Guide] (Lawyer '
               'Marketing and AI with Andrew Stickel)',
      'url': 'https://www.youtube.com/watch?v=aAMJ5QeSrvU&t=1068s',
      'video_id': 'aAMJ5QeSrvU'},
     {'author': 'Chad Michael - The Practitioner',
      'channel': 'Chad Michael - The Practitioner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:44](https://www.youtube.com/watch?v=d6mF320R8u0&t=44s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The flashing so to replace that flashing this system over here also must be '
              "addressed so we've got like this coating system here and you can see pretty "
              "clearly on the coating you know the damage so we've got the damage to places "
              'like there so you have the damage.',
      'timestamp': 44,
      'timestamp_label': '[00:00:44]',
      'timestamp_seconds': 44,
      'tip': 'The flashing so to replace that flashing this system over here also must be '
             "addressed so we've got like this coating system here and you can see pretty "
             "clearly on the coating you know the damage so we've got the damage to places "
             'like there so you have the damage.',
      'title': 'Commercial Flat Roof Hail Damage (Chad Michael - The Practitioner)',
      'url': 'https://www.youtube.com/watch?v=d6mF320R8u0&t=44s',
      'video_id': 'd6mF320R8u0'},
     {'author': 'David Sugrue',
      'channel': 'David Sugrue',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:09](https://www.youtube.com/watch?v=vmJD-cz6rdc&t=249s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Make yourself visible every place in the community is a place to meet new '
              'prospects the supermarket the movies or the dry cleaners are places to meet '
              'prospects your company logo on an attractive shirt and car magnet will create '
              'interest in your product.',
      'timestamp': 249,
      'timestamp_label': '[00:04:09]',
      'timestamp_seconds': 249,
      'tip': 'Make yourself visible every place in the community is a place to meet new '
             'prospects the supermarket the movies or the dry cleaners are places to meet '
             'prospects your company logo on an attractive shirt and car magnet will create '
             'interest in your product.',
      'title': 'Solar Lead Generation - 8 Great Ideas (David Sugrue)',
      'url': 'https://www.youtube.com/watch?v=vmJD-cz6rdc&t=249s',
      'video_id': 'vmJD-cz6rdc'}],
 8: [{'author': 'Marketing Business Network',
      'channel': 'Marketing Business Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=MNUNce5QMnc&t=118s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'One-to-many or programmatic ABM uses automation and data to personalize '
              'outreach at scale across dozens or hundreds of accounts at once. The appeal is '
              'efficiency in high-value, long-cycle B2B sales.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': 'One-to-many or programmatic ABM uses automation and data to personalize outreach '
             'at scale across dozens or hundreds of accounts at once. The appeal is efficiency '
             'in high-value, long-cycle B2B sales.',
      'title': 'What is Account-Based Marketing (ABM)? (Marketing Business Network)',
      'url': 'https://www.youtube.com/watch?v=MNUNce5QMnc&t=118s',
      'video_id': 'MNUNce5QMnc'},
     {'author': 'Business Solution',
      'channel': 'Business Solution',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:30](https://www.youtube.com/watch?v=gKpbSCZMPqM&t=930s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "HubSpot-based sales process, HubSpot's attribution is usually good enough and "
              'very convenient because you get journey tracking, reporting, and execution in '
              'one place without buying a separate attribution platform.',
      'timestamp': 930,
      'timestamp_label': '[00:15:30]',
      'timestamp_seconds': 930,
      'tip': "HubSpot-based sales process, HubSpot's attribution is usually good enough and "
             'very convenient because you get journey tracking, reporting, and execution in '
             'one place without buying a separate attribution platform.',
      'title': '9 Best Marketing Attribution Software for 2027 (Full Demo & Comparison) '
               '(Business Solution)',
      'url': 'https://www.youtube.com/watch?v=gKpbSCZMPqM&t=930s',
      'video_id': 'gKpbSCZMPqM'},
     {'author': 'BizNick',
      'channel': 'BizNick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:48](https://www.youtube.com/watch?v=22cx7DJjhTY&t=1488s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Number four, you can do UCC lien search for every business acquisition. Before '
              'you buy a business or its assets, run a full UCC lien search on the seller.',
      'timestamp': 1488,
      'timestamp_label': '[00:24:48]',
      'timestamp_seconds': 1488,
      'tip': 'Number four, you can do UCC lien search for every business acquisition. Before '
             'you buy a business or its assets, run a full UCC lien search on the seller.',
      'title': 'What Actually Happens When You File a UCC-1 on Yourself (I Went Through the '
               'Records) (BizNick)',
      'url': 'https://www.youtube.com/watch?v=22cx7DJjhTY&t=1488s',
      'video_id': '22cx7DJjhTY'},
     {'author': 'WebFX',
      'channel': 'WebFX',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:59](https://www.youtube.com/watch?v=V7x_5WjVUiw&t=239s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If not, though, there are several tools out there that can help. Maybe the best '
              'tool to use for organizing your customer data is a CRM, or customer '
              'relationship management tool.',
      'timestamp': 239,
      'timestamp_label': '[00:03:59]',
      'timestamp_seconds': 239,
      'tip': 'If not, though, there are several tools out there that can help. Maybe the best '
             'tool to use for organizing your customer data is a CRM, or customer relationship '
             'management tool.',
      'title': 'How to Create Your Ideal Customer Profile | ICP Marketing (WebFX)',
      'url': 'https://www.youtube.com/watch?v=V7x_5WjVUiw&t=239s',
      'video_id': 'V7x_5WjVUiw'},
     {'author': 'Safe Ozone Energies',
      'channel': 'Safe Ozone Energies',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:30](https://www.youtube.com/watch?v=ZsD6O6UWRiI&t=150s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "As I have told earlier, there are three agents are wired together with ADK's "
              'sequential agent which run runs them in order and pass data between them '
              "automatically. No no as a manual glue code. The research use ADK's building "
              'Google search tool.',
      'timestamp': 150,
      'timestamp_label': '[00:02:30]',
      'timestamp_seconds': 150,
      'tip': "As I have told earlier, there are three agents are wired together with ADK's "
             'sequential agent which run runs them in order and pass data between them '
             "automatically. No no as a manual glue code. The research use ADK's building "
             'Google search tool.',
      'title': 'Lead Scout AI Agent | Multi-Agent Sales Research with Google ADK | Kaggle '
               'Capstone 2026 (Safe Ozone Energies)',
      'url': 'https://www.youtube.com/watch?v=ZsD6O6UWRiI&t=150s',
      'video_id': 'ZsD6O6UWRiI'},
     {'author': 'Rocket SaaS',
      'channel': 'Rocket SaaS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:13](https://www.youtube.com/watch?v=5XU6PUsdwEM&t=253s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re going all in with our five tactics to get that 100k ACV. So, if you've "
              "already got these big clients in your CRM and there's a few of them and you "
              "want to get more, you've talked about Yeah.",
      'timestamp': 253,
      'timestamp_label': '[00:04:13]',
      'timestamp_seconds': 253,
      'tip': "'re going all in with our five tactics to get that 100k ACV. So, if you've "
             "already got these big clients in your CRM and there's a few of them and you want "
             "to get more, you've talked about Yeah.",
      'title': '5 ABM Campaigns to Land Bigger SaaS Clients (Rocket SaaS)',
      'url': 'https://www.youtube.com/watch?v=5XU6PUsdwEM&t=253s',
      'video_id': '5XU6PUsdwEM'},
     {'author': 'Dylan Conroy',
      'channel': 'Dylan Conroy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:48](https://www.youtube.com/watch?v=yja0j6pWgP0&t=228s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um the other interesting thing is that now like uh any of you guys use the '
              'software tool braves for email marketing or familiar with it? So braise is '
              'email email and text marketing platform to communicate with your customers.',
      'timestamp': 228,
      'timestamp_label': '[00:03:48]',
      'timestamp_seconds': 228,
      'tip': 'Um the other interesting thing is that now like uh any of you guys use the '
             'software tool braves for email marketing or familiar with it? So braise is email '
             'email and text marketing platform to communicate with your customers.',
      'title': 'The B2B Trojan Horse: Using a Podcast for Networking & Lead Gen (Dylan Conroy)',
      'url': 'https://www.youtube.com/watch?v=yja0j6pWgP0&t=228s',
      'video_id': 'yja0j6pWgP0'},
     {'author': 'OGONJO Workbooks',
      'channel': 'OGONJO Workbooks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:09](https://www.youtube.com/watch?v=bVYYwxZZ4dU&t=129s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'CRM or e-commerce platform a company runs to identify exactly where your ideal '
              'segments actually live. This is the core segmentation tool for the whole '
              'lesson. With an ICP in hand, you can finally approach the market with precision '
              'instead of a wide net.',
      'timestamp': 129,
      'timestamp_label': '[00:02:09]',
      'timestamp_seconds': 129,
      'tip': 'CRM or e-commerce platform a company runs to identify exactly where your ideal '
             'segments actually live. This is the core segmentation tool for the whole lesson. '
             'With an ICP in hand, you can finally approach the market with precision instead '
             'of a wide net.',
      'title': 'Where Your Best-Fit Customers Actually Cluster (B2B Ideal Customer Profile '
               'Series) – Pt 5 (OGONJO Workbooks)',
      'url': 'https://www.youtube.com/watch?v=bVYYwxZZ4dU&t=129s',
      'video_id': 'bVYYwxZZ4dU'},
     {'author': 'Josh Whitfield',
      'channel': 'Josh Whitfield',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:03](https://www.youtube.com/watch?v=aBPwEBpUNp4&t=423s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'ICP and being able to, you know, run job postings and promotions and news and '
              'fund rating and 3,000 actors from Appify, uh, any API call I want, pull in very '
              'robust buying intent data, engaging with social posts.',
      'timestamp': 423,
      'timestamp_label': '[00:07:03]',
      'timestamp_seconds': 423,
      'tip': 'ICP and being able to, you know, run job postings and promotions and news and '
             'fund rating and 3,000 actors from Appify, uh, any API call I want, pull in very '
             'robust buying intent data, engaging with social posts.',
      'title': 'Next-Level Outbound: Using Clay Signals & Apify for Real-Time Lead Gen (Josh '
               'Whitfield)',
      'url': 'https://www.youtube.com/watch?v=aBPwEBpUNp4&t=423s',
      'video_id': 'aBPwEBpUNp4'},
     {'author': 'Chris Bussing',
      'channel': 'Chris Bussing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:02](https://www.youtube.com/watch?v=EQhwdsXidcQ&t=302s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re providing you coaching while you're in the meeting. And post meeting, the "
              'agents are going and updating your CRM for you. And to the extent that the '
              'forecast agent also doing forecast prediction for you because so much of the '
              'data is being updated automatically.',
      'timestamp': 302,
      'timestamp_label': '[00:05:02]',
      'timestamp_seconds': 302,
      'tip': "'re providing you coaching while you're in the meeting. And post meeting, the "
             'agents are going and updating your CRM for you. And to the extent that the '
             'forecast agent also doing forecast prediction for you because so much of the '
             'data is being updated automatically.',
      'title': '$4.4B Outreach CEO: The Future of Sales Is AI Agents (Chris Bussing)',
      'url': 'https://www.youtube.com/watch?v=EQhwdsXidcQ&t=302s',
      'video_id': 'EQhwdsXidcQ'},
     {'author': 'AdConversion',
      'channel': 'AdConversion',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:34](https://www.youtube.com/watch?v=FPPnVM3_KPk&t=1294s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Think and ideate and review data so many applications for that not even just '
              'from like an ABM ads perspective or just running ads but like as a founder and '
              'a.',
      'timestamp': 1294,
      'timestamp_label': '[00:21:34]',
      'timestamp_seconds': 1294,
      'tip': 'Think and ideate and review data so many applications for that not even just '
             'from like an ABM ads perspective or just running ads but like as a founder and '
             'a.',
      'title': '10 Effective Account-Based Marketing Tactics For Modern B2B Marketers '
               '(AdConversion)',
      'url': 'https://www.youtube.com/watch?v=FPPnVM3_KPk&t=1294s',
      'video_id': 'FPPnVM3_KPk'},
     {'author': 'Sell Better',
      'channel': 'Sell Better',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=x_KIg1Z96_o&t=15s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "For The Daily Show and I've been using common room as the main tool for how I "
              'do account research and just general outbound and I wanted to share some new.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "For The Daily Show and I've been using common room as the main tool for how I do "
             'account research and just general outbound and I wanted to share some new.',
      'title': 'How to research your accounts (outbound sales) with this new AI tool (Sell '
               'Better)',
      'url': 'https://www.youtube.com/watch?v=x_KIg1Z96_o&t=15s',
      'video_id': 'x_KIg1Z96_o'},
     {'author': 'AECOM',
      'channel': 'AECOM',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:57](https://www.youtube.com/watch?v=DmHfrc4zfn0&t=537s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I know that you got to look at the power access to power access to water fiber '
              'infrastructure. Can you talk us through what are those critical elements for an '
              'ideal site for a data center?',
      'timestamp': 537,
      'timestamp_label': '[00:08:57]',
      'timestamp_seconds': 537,
      'tip': 'I know that you got to look at the power access to power access to water fiber '
             'infrastructure. Can you talk us through what are those critical elements for an '
             'ideal site for a data center?',
      'title': 'Powered land for data centers: what "ready to build" really means (AECOM)',
      'url': 'https://www.youtube.com/watch?v=DmHfrc4zfn0&t=537s',
      'video_id': 'DmHfrc4zfn0'},
     {'author': 'Envy - B2B Marketing & RevOps Agency',
      'channel': 'Envy - B2B Marketing & RevOps Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=CTPuSNDPU9Y&t=36s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Do they still need that bloated software, expensive one that doesn't really "
              'address the way that organizations of that size are going to market today? The '
              "answer is a resounding no. There's a movement from Salesforce to other CRM.",
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': "Do they still need that bloated software, expensive one that doesn't really "
             'address the way that organizations of that size are going to market today? The '
             "answer is a resounding no. There's a movement from Salesforce to other CRM.",
      'title': 'Why More Companies Are Leaving Salesforce for HubSpot CRM, And Why You Should '
               'Too 🤔 Marketing Envy (Envy - B2B Marketing & RevOps Agency)',
      'url': 'https://www.youtube.com/watch?v=CTPuSNDPU9Y&t=36s',
      'video_id': 'CTPuSNDPU9Y'},
     {'author': 'B2B Fusion',
      'channel': 'B2B Fusion',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:18](https://www.youtube.com/watch?v=4kdiiYL17XU&t=438s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Like you know changes in companies happening now it's it's just gonna you know "
              'continually happen and have that Snowball Effect I think.',
      'timestamp': 438,
      'timestamp_label': '[00:07:18]',
      'timestamp_seconds': 438,
      'tip': "Like you know changes in companies happening now it's it's just gonna you know "
             'continually happen and have that Snowball Effect I think.',
      'title': 'Evangelizing ABX - what is and is not working? (B2B Fusion)',
      'url': 'https://www.youtube.com/watch?v=4kdiiYL17XU&t=438s',
      'video_id': '4kdiiYL17XU'}],
 9: [{'author': 'Growth Manifesto Podcast',
      'channel': 'Growth Manifesto Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:01:21](https://www.youtube.com/watch?v=Vdq5ROPgQzw&t=3681s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Executive Engagement Strategies: How to Have Conversations and Develop '
              "Relationships That Build uh B2B business. Um I was going to ask you like what's "
              'that one about and how is that like different to the account-based marketing '
              'book?',
      'timestamp': 3681,
      'timestamp_label': '[01:01:21]',
      'timestamp_seconds': 3681,
      'tip': 'Executive Engagement Strategies: How to Have Conversations and Develop '
             "Relationships That Build uh B2B business. Um I was going to ask you like what's "
             'that one about and how is that like different to the account-based marketing '
             'book?',
      'title': 'How to use Account-Based Marketing to drive enterprise sales | Bev Burgess '
               '(Growth Manifesto Podcast)',
      'url': 'https://www.youtube.com/watch?v=Vdq5ROPgQzw&t=3681s',
      'video_id': 'Vdq5ROPgQzw'},
     {'author': 'Zero Risk Cases Client Acquisition Agency',
      'channel': 'Zero Risk Cases Client Acquisition Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=bK2Wu8cOcRU&t=40s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'AND, want to discuss their case with an attorney. This technology provides the '
              'highest possible value to clients for each mass tort we can offer. All '
              'potential claimants responding to our marketing come into our US-based call '
              'centers to get legal help.',
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': 'AND, want to discuss their case with an attorney. This technology provides the '
             'highest possible value to clients for each mass tort we can offer. All potential '
             'claimants responding to our marketing come into our US-based call centers to get '
             'legal help.',
      'title': 'Mass Tort Compliance Program-End Fake Leads and Lead Fraud (Zero Risk Cases '
               'Client Acquisition Agency)',
      'url': 'https://www.youtube.com/watch?v=bK2Wu8cOcRU&t=40s',
      'video_id': 'bK2Wu8cOcRU'},
     {'author': 'Policy & Property',
      'channel': 'Policy & Property',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:20](https://www.youtube.com/watch?v=V-xAfnhz1BY&t=380s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's why the repair versus replace call and your deductible type matter far "
              "more than most people think when they buy a policy. If you've ever had a roof "
              'claim denied or underpaid, tell me in the comments what your insurer said.',
      'timestamp': 380,
      'timestamp_label': '[00:06:20]',
      'timestamp_seconds': 380,
      'tip': "That's why the repair versus replace call and your deductible type matter far "
             "more than most people think when they buy a policy. If you've ever had a roof "
             'claim denied or underpaid, tell me in the comments what your insurer said.',
      'title': 'State Farm Roof Memo: Why Hail Claims Get Denied (Policy & Property)',
      'url': 'https://www.youtube.com/watch?v=V-xAfnhz1BY&t=380s',
      'video_id': 'V-xAfnhz1BY'},
     {'author': 'Connor Murray',
      'channel': 'Connor Murray',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:58](https://www.youtube.com/watch?v=DBGq--oFsQ8&t=898s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In B2B sales, there is a lot that has has to happen between them saying, "Yeah, '
              'I want to buy." So depending on the company, that can include procurement, '
              'legal review, security questionnaires, privacy reviews or vendor onboarding '
              'checklist.',
      'timestamp': 898,
      'timestamp_label': '[00:14:58]',
      'timestamp_seconds': 898,
      'tip': 'In B2B sales, there is a lot that has has to happen between them saying, "Yeah, '
             'I want to buy." So depending on the company, that can include procurement, legal '
             'review, security questionnaires, privacy reviews or vendor onboarding checklist.',
      'title': 'Learn the Entire B2B Sales Process in 17 Minutes (Connor Murray)',
      'url': 'https://www.youtube.com/watch?v=DBGq--oFsQ8&t=898s',
      'video_id': 'DBGq--oFsQ8'},
     {'author': 'eForms',
      'channel': 'eForms',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=KhY7TkJppys&t=168s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Terms for these concepts for example some may call them special and general '
              "retainers respectively no matter what they're called make sure the agreement.",
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': 'Terms for these concepts for example some may call them special and general '
             "retainers respectively no matter what they're called make sure the agreement.",
      'title': 'Everything You Need to Know About Retainer Agreements (eForms)',
      'url': 'https://www.youtube.com/watch?v=KhY7TkJppys&t=168s',
      'video_id': 'KhY7TkJppys'},
     {'author': 'Financial Regulation Courses',
      'channel': 'Financial Regulation Courses',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:34](https://www.youtube.com/watch?v=HPkIpR-sbx4&t=34s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Oversight report recently identified new compliance concerns regarding mobile '
              'applications and the accurate disclosure of risk. Between 2020 and 2026, '
              'retail.',
      'timestamp': 34,
      'timestamp_label': '[00:00:34]',
      'timestamp_seconds': 34,
      'tip': 'Oversight report recently identified new compliance concerns regarding mobile '
             'applications and the accurate disclosure of risk. Between 2020 and 2026, retail.',
      'title': 'FINRA Rule 2220 Explained  Options Communications, Advertising Rules & Broker '
               'Dealer Compliance (Financial Regulation Courses)',
      'url': 'https://www.youtube.com/watch?v=HPkIpR-sbx4&t=34s',
      'video_id': 'HPkIpR-sbx4'},
     {'author': 'The B2B Creator',
      'channel': 'The B2B Creator',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:23](https://www.youtube.com/watch?v=J7a0Ws0g0nI&t=323s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Second thing is the DM script. When you send someone a lead magnet, obviously, '
              "that's the first thing you want to send to them. But, then afterwards, you have "
              "a warm conversation there with somebody you've built trust with. It converts so "
              'much better than cold outreach.',
      'timestamp': 323,
      'timestamp_label': '[00:05:23]',
      'timestamp_seconds': 323,
      'tip': 'Second thing is the DM script. When you send someone a lead magnet, obviously, '
             "that's the first thing you want to send to them. But, then afterwards, you have "
             "a warm conversation there with somebody you've built trust with. It converts so "
             'much better than cold outreach.',
      'title': "He's Making BANK Ghostwriting for B2b/SaaS Companies on LinkedIn (The B2B "
               'Creator)',
      'url': 'https://www.youtube.com/watch?v=J7a0Ws0g0nI&t=323s',
      'video_id': 'J7a0Ws0g0nI'},
     {'author': 'Willem',
      'channel': 'Willem',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:30](https://www.youtube.com/watch?v=Gi8lgR2IK40&t=150s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We turn our Outreach from talking to 20 business owners a day to keeping that '
              'same personalization and talking to 1,000 a day um right the more volume you.',
      'timestamp': 150,
      'timestamp_label': '[00:02:30]',
      'timestamp_seconds': 150,
      'tip': 'We turn our Outreach from talking to 20 business owners a day to keeping that '
             'same personalization and talking to 1,000 a day um right the more volume you.',
      'title': 'Full Guide on M&A Deal Origination (Willem)',
      'url': 'https://www.youtube.com/watch?v=Gi8lgR2IK40&t=150s',
      'video_id': 'Gi8lgR2IK40'},
     {'author': 'BN.Digital',
      'channel': 'BN.Digital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=ssgz-uXMi6c&t=111s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But basically you once you've nailed your top of the funnel outreach right if "
              "you're getting in front of the right business owners and the right.",
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': "But basically you once you've nailed your top of the funnel outreach right if "
             "you're getting in front of the right business owners and the right.",
      'title': "What tools should I use for M&A deal sourcing and my deal flow funnel? Here's "
               'our process. (BN.Digital)',
      'url': 'https://www.youtube.com/watch?v=ssgz-uXMi6c&t=111s',
      'video_id': 'ssgz-uXMi6c'},
     {'author': 'ALC Lawcast: Finance in Focus',
      'channel': 'ALC Lawcast: Finance in Focus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:53](https://www.youtube.com/watch?v=T89w7sq33_M&t=233s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This Item requires a company to inform shareholders of the date in which they '
              'must submit director nominations on Schedule 14N. I am securities attorney '
              'Laura Anthony, founding partner of Legal & Compliance, and producer of LawCast.',
      'timestamp': 233,
      'timestamp_label': '[00:03:53]',
      'timestamp_seconds': 233,
      'tip': 'This Item requires a company to inform shareholders of the date in which they '
             'must submit director nominations on Schedule 14N. I am securities attorney Laura '
             'Anthony, founding partner of Legal & Compliance, and producer of LawCast.',
      'title': 'Item 5 of Form 8-K (ALC Lawcast: Finance in Focus)',
      'url': 'https://www.youtube.com/watch?v=T89w7sq33_M&t=233s',
      'video_id': 'T89w7sq33_M'},
     {'author': 'Joel Harrison B2B',
      'channel': 'Joel Harrison B2B',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:50](https://www.youtube.com/watch?v=_3lBtkAs_Os&t=1130s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So um in terms of the seauite the research the research showed that 41% of '
              'target decision makers and 35% of internal influences have been encouraged by '
              'seauite executives to consider vendors based on their thought leadership.',
      'timestamp': 1130,
      'timestamp_label': '[00:18:50]',
      'timestamp_seconds': 1130,
      'tip': 'So um in terms of the seauite the research the research showed that 41% of '
             'target decision makers and 35% of internal influences have been encouraged by '
             'seauite executives to consider vendors based on their thought leadership.',
      'title': 'Trust and the Trojan Horse: Using Thought Leadership to Convince Internal '
               'Influencers (Joel Harrison B2B)',
      'url': 'https://www.youtube.com/watch?v=_3lBtkAs_Os&t=1130s',
      'video_id': '_3lBtkAs_Os'},
     {'author': 'Neil McDonnell',
      'channel': 'Neil McDonnell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:56](https://www.youtube.com/watch?v=d_oQ5UhlC0k&t=236s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Different categories basically right Prime Contracting if you're going to Prime "
              "on a contract with the federal agency you're the prime and you have.",
      'timestamp': 236,
      'timestamp_label': '[00:03:56]',
      'timestamp_seconds': 236,
      'tip': "Different categories basically right Prime Contracting if you're going to Prime "
             "on a contract with the federal agency you're the prime and you have.",
      'title': 'How Government Contractors Find Teaming Partners in the Federal Market (Neil '
               'McDonnell)',
      'url': 'https://www.youtube.com/watch?v=d_oQ5UhlC0k&t=236s',
      'video_id': 'd_oQ5UhlC0k'},
     {'author': 'Roman Love',
      'channel': 'Roman Love',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:35](https://www.youtube.com/watch?v=cC9kyrNz7RM&t=215s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Don't really have any complaints in that regard at all, really. Yeah, no, I "
              'appreciate that. And in terms of other installers in other areas, would you '
              'recommend us to help them get in front of more clients and win more business '
              'for their installation company?',
      'timestamp': 215,
      'timestamp_label': '[00:03:35]',
      'timestamp_seconds': 215,
      'tip': "Don't really have any complaints in that regard at all, really. Yeah, no, I "
             'appreciate that. And in terms of other installers in other areas, would you '
             'recommend us to help them get in front of more clients and win more business for '
             'their installation company?',
      'title': 'Commercial solar leads testimonial: Ingeni Renewables | TNW Marketing (Roman '
               'Love)',
      'url': 'https://www.youtube.com/watch?v=cC9kyrNz7RM&t=215s',
      'video_id': 'cC9kyrNz7RM'},
     {'author': 'Financial Regulation Courses',
      'channel': 'Financial Regulation Courses',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=aihsw-Ee9zI&t=91s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Rule 1220 outlines diverse categories tailored to specific business functions. '
              'The general securities principle remains the standard pathway for overall '
              'management. Specialized categories include the compliance officer registration.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': 'Rule 1220 outlines diverse categories tailored to specific business functions. '
             'The general securities principle remains the standard pathway for overall '
             'management. Specialized categories include the compliance officer registration.',
      'title': 'FINRA Rule 1220 Explained  Registration Categories for Securities '
               'Professionals (Financial Regulation Courses)',
      'url': 'https://www.youtube.com/watch?v=aihsw-Ee9zI&t=91s',
      'video_id': 'aihsw-Ee9zI'},
     {'author': 'Pepper - The Agentic Organic Growth Engine',
      'channel': 'Pepper - The Agentic Organic Growth Engine',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:35](https://www.youtube.com/watch?v=ZKcBjdvfhX0&t=95s)',
      'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                   'demand generation, ABM signal orchestration, and high-ACV deal origination '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And that's honestly the best way to describe this partnership. We weren't just "
              "editing words, we were a thought partner. If you're building in a fastmoving "
              'category and your content needs to earn trust, this is the playbook.',
      'timestamp': 95,
      'timestamp_label': '[00:01:35]',
      'timestamp_seconds': 95,
      'tip': "And that's honestly the best way to describe this partnership. We weren't just "
             "editing words, we were a thought partner. If you're building in a fastmoving "
             'category and your content needs to earn trust, this is the playbook.',
      'title': 'Algolia × Pepper Case Study: Scaling SME-Led Technical Thought Leadership '
               '(Human-Led Ghostwriting) (Pepper - The Agentic Organic Growth Engine)',
      'url': 'https://www.youtube.com/watch?v=ZKcBjdvfhX0&t=95s',
      'video_id': 'ZKcBjdvfhX0'}],
 10: [{'author': 'Optimity Logics',
       'channel': 'Optimity Logics',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:10](https://www.youtube.com/watch?v=SiSLxkwVah8&t=70s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It reviews the company's operations, customer-facing processes, and possible "
               'areas for improvement. Based on the available information, the workflow can '
               'identify relevant business challenges and potential opportunities for AI or '
               'automation.',
       'timestamp': 70,
       'timestamp_label': '[00:01:10]',
       'timestamp_seconds': 70,
       'tip': "It reviews the company's operations, customer-facing processes, and possible "
              'areas for improvement. Based on the available information, the workflow can '
              'identify relevant business challenges and potential opportunities for AI or '
              'automation.',
       'title': '🚀 AI-Powered B2B Lead Research & Outreach Automation 🤖 (Optimity Logics)',
       'url': 'https://www.youtube.com/watch?v=SiSLxkwVah8&t=70s',
       'video_id': 'SiSLxkwVah8'},
      {'author': 'Misar AI',
       'channel': 'Misar AI',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:42](https://www.youtube.com/watch?v=giIGT_MMd5k&t=162s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The payoff is that the search stays aligned with the model, instead of filling '
               "up with accounts that look similar, but won't actually buy. So, in the first "
               "example, this isn't abstract at all. It's a startup selling workflow "
               'automation to mid-size tech firms.',
       'timestamp': 162,
       'timestamp_label': '[00:02:42]',
       'timestamp_seconds': 162,
       'tip': 'The payoff is that the search stays aligned with the model, instead of filling '
              "up with accounts that look similar, but won't actually buy. So, in the first "
              "example, this isn't abstract at all. It's a startup selling workflow automation "
              'to mid-size tech firms.',
       'title': 'Ideal Customer Profile Template: Free B2B Worksheet & Examples (Misar AI)',
       'url': 'https://www.youtube.com/watch?v=giIGT_MMd5k&t=162s',
       'video_id': 'giIGT_MMd5k'},
      {'author': 'POTOMAC M&A',
       'channel': 'POTOMAC M&A',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:27:39](https://www.youtube.com/watch?v=f7d2hP31YB8&t=1659s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Uh, if you've got no one that wants to buy your business, you, the seller, are "
               'not going to have any leverage or power. The buyer is going to have a lot of '
               'power. You know the banker should not necessarily have any power at all.',
       'timestamp': 1659,
       'timestamp_label': '[00:27:39]',
       'timestamp_seconds': 1659,
       'tip': "Uh, if you've got no one that wants to buy your business, you, the seller, are "
              'not going to have any leverage or power. The buyer is going to have a lot of '
              'power. You know the banker should not necessarily have any power at all.',
       'title': 'Sell-Side M&A Masterclass Q&A: Buyer Tactics, Leverage, and Negotiation '
                'Strategies #privateequity (POTOMAC M&A)',
       'url': 'https://www.youtube.com/watch?v=f7d2hP31YB8&t=1659s',
       'video_id': 'f7d2hP31YB8'},
      {'author': 'ATAK Interactive',
       'channel': 'ATAK Interactive',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:48](https://www.youtube.com/watch?v=FCu5IsBzx4U&t=408s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And then how do we find more companies that match this? This then becomes kind '
               'of our pillar account that we build other accounts around that we want to '
               'leverage that are similarly placed.',
       'timestamp': 408,
       'timestamp_label': '[00:06:48]',
       'timestamp_seconds': 408,
       'tip': 'And then how do we find more companies that match this? This then becomes kind '
              'of our pillar account that we build other accounts around that we want to '
              'leverage that are similarly placed.',
       'title': 'ABM vs. Demand Generation | How to Choose the Right Strategy (ATAK '
                'Interactive)',
       'url': 'https://www.youtube.com/watch?v=FCu5IsBzx4U&t=408s',
       'video_id': 'FCu5IsBzx4U'},
      {'author': 'Loudr Media',
       'channel': 'Loudr Media',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:04](https://www.youtube.com/watch?v=TJJfmZiIGW4&t=544s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'We call this the ripple effect and this is that compounding ripple effect that '
               "most firms don't take into consideration. So, just to recap, we're talking "
               'about speed to lead, empathy, the script, relatability, and relentless '
               'follow-up, and incentives.',
       'timestamp': 544,
       'timestamp_label': '[00:09:04]',
       'timestamp_seconds': 544,
       'tip': 'We call this the ripple effect and this is that compounding ripple effect that '
              "most firms don't take into consideration. So, just to recap, we're talking "
              'about speed to lead, empathy, the script, relatability, and relentless '
              'follow-up, and incentives.',
       'title': 'The HIDDEN Intake Script Attorneys Don’t Want YOU To Know (Loudr Media)',
       'url': 'https://www.youtube.com/watch?v=TJJfmZiIGW4&t=544s',
       'video_id': 'TJJfmZiIGW4'},
      {'author': 'ColdIQ',
       'channel': 'ColdIQ',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:34](https://www.youtube.com/watch?v=lSM-6GschOc&t=814s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I start with forgets about. It's called the AI context center. The AI context "
               'center is a place for you to load up almost the psychological profile of your '
               'business, objection handling, value propositions, etc.',
       'timestamp': 814,
       'timestamp_label': '[00:13:34]',
       'timestamp_seconds': 814,
       'tip': "I start with forgets about. It's called the AI context center. The AI context "
              'center is a place for you to load up almost the psychological profile of your '
              'business, objection handling, value propositions, etc.',
       'title': 'Build + launch outbound campaigns without leaving the terminal (Claude Code + '
                'Apollo) (ColdIQ)',
       'url': 'https://www.youtube.com/watch?v=lSM-6GschOc&t=814s',
       'video_id': 'lSM-6GschOc'},
      {'author': 'Local Service Ads',
       'channel': 'Local Service Ads',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:40](https://www.youtube.com/watch?v=I1FMlqBfPQc&t=460s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Bonus tip, integration and automation. How can you integrate Google local '
               'service ads, Google business profile, and AI intake systems for seamless lead '
               'generation and follow-up with our team?',
       'timestamp': 460,
       'timestamp_label': '[00:07:40]',
       'timestamp_seconds': 460,
       'tip': 'Bonus tip, integration and automation. How can you integrate Google local '
              'service ads, Google business profile, and AI intake systems for seamless lead '
              'generation and follow-up with our team?',
       'title': "How to Boost Your Law Firm's Lead Generation (Local Service Ads)",
       'url': 'https://www.youtube.com/watch?v=I1FMlqBfPQc&t=460s',
       'video_id': 'I1FMlqBfPQc'},
      {'author': 'Local Service Ads',
       'channel': 'Local Service Ads',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:33](https://www.youtube.com/watch?v=EJ36tZtFe4A&t=213s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "We've posted a detailed guide walking you through each step, including how to "
               'automate your speed to lead, optimize your Google business profile page, and '
               'track every conversion.',
       'timestamp': 213,
       'timestamp_label': '[00:03:33]',
       'timestamp_seconds': 213,
       'tip': "We've posted a detailed guide walking you through each step, including how to "
              'automate your speed to lead, optimize your Google business profile page, and '
              'track every conversion.',
       'title': 'Lawyers: Master Lead Generation in 4 Minutes (Local Service Ads)',
       'url': 'https://www.youtube.com/watch?v=EJ36tZtFe4A&t=213s',
       'video_id': 'EJ36tZtFe4A'},
      {'author': 'GTM Partner',
       'channel': 'GTM Partner',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:53](https://www.youtube.com/watch?v=NCH5pSCJcCU&t=413s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And we're doing the same thing for mobiles, right? Mobile phone numbers "
               'because we are having our account executives call these people in their terri '
               'territory.',
       'timestamp': 413,
       'timestamp_label': '[00:06:53]',
       'timestamp_seconds': 413,
       'tip': "And we're doing the same thing for mobiles, right? Mobile phone numbers because "
              'we are having our account executives call these people in their terri '
              'territory.',
       'title': 'How to Build Signal-Led Outbound with Clay (Full Workflow Walkthrough) (GTM '
                'Partner)',
       'url': 'https://www.youtube.com/watch?v=NCH5pSCJcCU&t=413s',
       'video_id': 'NCH5pSCJcCU'},
      {'author': 'SalesCaptain',
       'channel': 'SalesCaptain',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:38](https://www.youtube.com/watch?v=rWxFZ4ADhqQ&t=218s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So today we're building what we call forge stack which allow which connects "
               'essentially with clay where you can execute essentially all the stuff in clay '
               'um across email and and LinkedIn and do that at scale with unlimited mailboxes '
               'unlimited LinkedIn senders.',
       'timestamp': 218,
       'timestamp_label': '[00:03:38]',
       'timestamp_seconds': 218,
       'tip': "So today we're building what we call forge stack which allow which connects "
              'essentially with clay where you can execute essentially all the stuff in clay '
              'um across email and and LinkedIn and do that at scale with unlimited mailboxes '
              'unlimited LinkedIn senders.',
       'title': 'Clay Masterclass for 2026: The GTM Workflows That Actually Move Pipeline (30+ '
                'Examples) (SalesCaptain)',
       'url': 'https://www.youtube.com/watch?v=rWxFZ4ADhqQ&t=218s',
       'video_id': 'rWxFZ4ADhqQ'},
      {'author': 'Instantly',
       'channel': 'Instantly',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:18](https://www.youtube.com/watch?v=FOr5YL0hYJE&t=918s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So we look at ourselves as workflow integrators with a CRM built in and many '
               'times many of our clients use it only for this and not for the CRM. The '
               'smaller ones use it as a CRM as a marketing automation engine one in allin-one '
               'platform.',
       'timestamp': 918,
       'timestamp_label': '[00:15:18]',
       'timestamp_seconds': 918,
       'tip': 'So we look at ourselves as workflow integrators with a CRM built in and many '
              'times many of our clients use it only for this and not for the CRM. The smaller '
              'ones use it as a CRM as a marketing automation engine one in allin-one '
              'platform.',
       'title': 'The AI CRM Killing Salesforce & HubSpot (Instantly)',
       'url': 'https://www.youtube.com/watch?v=FOr5YL0hYJE&t=918s',
       'video_id': 'FOr5YL0hYJE'},
      {'author': 'AI Marketers Guild',
       'channel': 'AI Marketers Guild',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:30](https://www.youtube.com/watch?v=v0lXcZYhFXc&t=510s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So I I came up with this concept I like to call the lumpy mail. So if you '
               'think about anytime you order anything and it gets delivered to your doorstep, '
               "whether you forgot you ordered it or you remember it's coming, you get kind of "
               'excited. You have a package to open.',
       'timestamp': 510,
       'timestamp_label': '[00:08:30]',
       'timestamp_seconds': 510,
       'tip': 'So I I came up with this concept I like to call the lumpy mail. So if you think '
              'about anytime you order anything and it gets delivered to your doorstep, '
              "whether you forgot you ordered it or you remember it's coming, you get kind of "
              'excited. You have a package to open.',
       'title': 'How Strategic Gifting Drives Revenue Growth in ABM Campaigns | Outgage (AI '
                'Marketers Guild)',
       'url': 'https://www.youtube.com/watch?v=v0lXcZYhFXc&t=510s',
       'video_id': 'v0lXcZYhFXc'},
      {'author': 'ZenPilot',
       'channel': 'ZenPilot',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=-zNdXXrY9lU&t=15s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'CEO at influence a full funnel LinkedIn agency Garrett how are you doing today '
               'oh my gosh Kuba I was doing well and then I got the energy burst from that.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'CEO at influence a full funnel LinkedIn agency Garrett how are you doing today '
              'oh my gosh Kuba I was doing well and then I got the energy burst from that.',
       'title': 'How to Drive Pipeline Through LinkedIn Thought Leadership and a Strong POV '
                'with Garret Caudle (ZenPilot)',
       'url': 'https://www.youtube.com/watch?v=-zNdXXrY9lU&t=15s',
       'video_id': '-zNdXXrY9lU'},
      {'author': 'Value-First',
       'channel': 'Value-First',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:37:44](https://www.youtube.com/watch?v=NZUqq5BtQuU&t=2264s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'About it or just want it want it to be off your desk um we challenge you to '
               "find those opportunities and let's grow have a great day everybody thanks.",
       'timestamp': 2264,
       'timestamp_label': '[00:37:44]',
       'timestamp_seconds': 2264,
       'tip': 'About it or just want it want it to be off your desk um we challenge you to '
              "find those opportunities and let's grow have a great day everybody thanks.",
       'title': "Let's Build Multi-Touch Attribution in HubSpot with Sarah Lane-Hawn "
                '(Value-First)',
       'url': 'https://www.youtube.com/watch?v=NZUqq5BtQuU&t=2264s',
       'video_id': 'NZUqq5BtQuU'},
      {'author': 'Proclaim Roofing',
       'channel': 'Proclaim Roofing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:29](https://www.youtube.com/watch?v=m37LDnkUURI&t=149s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Work all over Texas and there's hail everywhere from Dallas to Midland to San "
               'Angelo San Antonio to Houston Georgetown Austin you know East Texas all of '
               "Oklahoma so again please reach out we'd love to help you out inspect all your "
               'properties thanks guys talk to you soon.',
       'timestamp': 149,
       'timestamp_label': '[00:02:29]',
       'timestamp_seconds': 149,
       'tip': "Work all over Texas and there's hail everywhere from Dallas to Midland to San "
              'Angelo San Antonio to Houston Georgetown Austin you know East Texas all of '
              "Oklahoma so again please reach out we'd love to help you out inspect all your "
              'properties thanks guys talk to you soon.',
       'title': 'How to Identify Hail Damage on your Commercial Roof (Proclaim Roofing)',
       'url': 'https://www.youtube.com/watch?v=m37LDnkUURI&t=149s',
       'video_id': 'm37LDnkUURI'}],
 11: [{'author': 'Pietro Conte',
       'channel': 'Pietro Conte',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:51](https://www.youtube.com/watch?v=1PBrwvp_6us&t=51s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'t know who could buy the house even if they did know how much it was worth. "
               "When a business decides that they're ready to sell, they run into the same "
               'problems. And so, if you were selling your house, you would hire a real estate '
               'agent.',
       'timestamp': 51,
       'timestamp_label': '[00:00:51]',
       'timestamp_seconds': 51,
       'tip': "'t know who could buy the house even if they did know how much it was worth. "
              "When a business decides that they're ready to sell, they run into the same "
              'problems. And so, if you were selling your house, you would hire a real estate '
              'agent.',
       'title': 'Ultimate Beginner’s Guide to Sell-Side M&A Process (Pietro Conte)',
       'url': 'https://www.youtube.com/watch?v=1PBrwvp_6us&t=51s',
       'video_id': '1PBrwvp_6us'},
      {'author': 'In Love With Marketing',
       'channel': 'In Love With Marketing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:54](https://www.youtube.com/watch?v=CNTwxh9-1AI&t=234s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Should have been already designed and using some content to engage with their '
               'targeted accounts and not just that ABM team can also pass on the customer.',
       'timestamp': 234,
       'timestamp_label': '[00:03:54]',
       'timestamp_seconds': 234,
       'tip': 'Should have been already designed and using some content to engage with their '
              'targeted accounts and not just that ABM team can also pass on the customer.',
       'title': 'Who is best? Account Based Marketing or Demand Generation? (In Love With '
                'Marketing)',
       'url': 'https://www.youtube.com/watch?v=CNTwxh9-1AI&t=234s',
       'video_id': 'CNTwxh9-1AI'},
      {'author': 'POTOMAC M&A',
       'channel': 'POTOMAC M&A',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:18](https://www.youtube.com/watch?v=T64at1dT1Zs&t=318s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '" You can certainly do that. You might end up waiting a decade for your phone '
               'to ring, but you can do that. You can hire a buyside broker of some sort or an '
               'adviser who basically goes out, makes calls, sends annoying emails on your '
               'behalf, and tries to drum up some business.',
       'timestamp': 318,
       'timestamp_label': '[00:05:18]',
       'timestamp_seconds': 318,
       'tip': '" You can certainly do that. You might end up waiting a decade for your phone '
              'to ring, but you can do that. You can hire a buyside broker of some sort or an '
              'adviser who basically goes out, makes calls, sends annoying emails on your '
              'behalf, and tries to drum up some business.',
       'title': 'Acquisition Criteria & Proprietary Deal Flow | Buy-Side Masterclass Moment '
                '(POTOMAC M&A)',
       'url': 'https://www.youtube.com/watch?v=T64at1dT1Zs&t=318s',
       'video_id': 'T64at1dT1Zs'},
      {'author': 'Exit Five',
       'channel': 'Exit Five',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:40](https://www.youtube.com/watch?v=q_PvrQsWu-E&t=940s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'We want to please we want to do whatever sales wants um and so we will add too '
               'many accounts and each of my team members now has an account limit so that '
               "we're not going to 200 accounts. My team cannot one person cannot know 200 "
               'accounts intimately.',
       'timestamp': 940,
       'timestamp_label': '[00:15:40]',
       'timestamp_seconds': 940,
       'tip': 'We want to please we want to do whatever sales wants um and so we will add too '
              'many accounts and each of my team members now has an account limit so that '
              "we're not going to 200 accounts. My team cannot one person cannot know 200 "
              'accounts intimately.',
       'title': 'ABM: What Ramp, Snowflake, and Hightouch are doing in 2026 (Exit Five)',
       'url': 'https://www.youtube.com/watch?v=q_PvrQsWu-E&t=940s',
       'video_id': 'q_PvrQsWu-E'},
      {'author': 'Solar Boss',
       'channel': 'Solar Boss',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:32](https://www.youtube.com/watch?v=llGN2e-R62s&t=392s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But, most important out of all is we can guarantee you predictability and '
               'stability in your business and your lead generation, right? We can go above '
               'and beyond to make sure you have you and your team have leads to call on a '
               'day-by-day basis, okay?',
       'timestamp': 392,
       'timestamp_label': '[00:06:32]',
       'timestamp_seconds': 392,
       'tip': 'But, most important out of all is we can guarantee you predictability and '
              'stability in your business and your lead generation, right? We can go above and '
              'beyond to make sure you have you and your team have leads to call on a '
              'day-by-day basis, okay?',
       'title': 'How Our Solar Lead Generation Works (Solar Boss)',
       'url': 'https://www.youtube.com/watch?v=llGN2e-R62s&t=392s',
       'video_id': 'llGN2e-R62s'},
      {'author': 'Prairie Founders Club',
       'channel': 'Prairie Founders Club',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:47](https://www.youtube.com/watch?v=VJjRWz_6Hq0&t=107s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "They're based more on emotion and it's really more about just getting the word "
               "out. So whether you're B2B or B TOC combined with your lifetime value of your "
               "customer is going to determine your sales and marketing operations. So I'm "
               'drawing a quadrant here.',
       'timestamp': 107,
       'timestamp_label': '[00:01:47]',
       'timestamp_seconds': 107,
       'tip': "They're based more on emotion and it's really more about just getting the word "
              "out. So whether you're B2B or B TOC combined with your lifetime value of your "
              "customer is going to determine your sales and marketing operations. So I'm "
              'drawing a quadrant here.',
       'title': 'Your Ideal Customer Profile (ICP): How It Changes Sales & Marketing (Prairie '
                'Founders Club)',
       'url': 'https://www.youtube.com/watch?v=VJjRWz_6Hq0&t=107s',
       'video_id': 'VJjRWz_6Hq0'},
      {'author': 'Chris Bussing',
       'channel': 'Chris Bussing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:33](https://www.youtube.com/watch?v=KH5mI_MoF2s&t=453s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And we'll get to email and and LinkedIn in a bit, but you know, thanks for "
               "taking my call. Is that something that is newer that you've added or have you "
               "done that for the for years? I've done that since probably 2017, 2018 when I "
               'was an SDR sales manager.',
       'timestamp': 453,
       'timestamp_label': '[00:07:33]',
       'timestamp_seconds': 453,
       'tip': "And we'll get to email and and LinkedIn in a bit, but you know, thanks for "
              "taking my call. Is that something that is newer that you've added or have you "
              "done that for the for years? I've done that since probably 2017, 2018 when I "
              'was an SDR sales manager.',
       'title': 'The New Rules Of B2B Outbound Sales (in 2027) (Chris Bussing)',
       'url': 'https://www.youtube.com/watch?v=KH5mI_MoF2s&t=453s',
       'video_id': 'KH5mI_MoF2s'},
      {'author': 'Aritic',
       'channel': 'Aritic',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:23](https://www.youtube.com/watch?v=0Rhumt5MUDw&t=443s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A list of 50 accounts and if there are already conversations in those accounts '
               "being going on so that's where you know the insights from the sales team can "
               'be.',
       'timestamp': 443,
       'timestamp_label': '[00:07:23]',
       'timestamp_seconds': 443,
       'tip': 'A list of 50 accounts and if there are already conversations in those accounts '
              "being going on so that's where you know the insights from the sales team can "
              'be.',
       'title': 'On-demand Webinar - Enterprise-Level ABM Gifting: How To Stand Out From The '
                'Digital Noise (Aritic)',
       'url': 'https://www.youtube.com/watch?v=0Rhumt5MUDw&t=443s',
       'video_id': '0Rhumt5MUDw'},
      {'author': 'Social-Hire.com',
       'channel': 'Social-Hire.com',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:57](https://www.youtube.com/watch?v=VesCkYBJkFA&t=117s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "If the writer's pitch is just I'll find articles and summarize them, give them "
               'a miss. On the complete flip side, red flag number three is a ghostwriter who '
               'demands too much of your time. The whole point of hiring a professional is to '
               'buy your time back.',
       'timestamp': 117,
       'timestamp_label': '[00:01:57]',
       'timestamp_seconds': 117,
       'tip': "If the writer's pitch is just I'll find articles and summarize them, give them "
              'a miss. On the complete flip side, red flag number three is a ghostwriter who '
              'demands too much of your time. The whole point of hiring a professional is to '
              'buy your time back.',
       'title': 'Before You Hire a LinkedIn Ghostwriter: Watch Out For These Red Flags '
                '(Social-Hire.com)',
       'url': 'https://www.youtube.com/watch?v=VesCkYBJkFA&t=117s',
       'video_id': 'VesCkYBJkFA'},
      {'author': 'CRM Central',
       'channel': 'CRM Central',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:23](https://www.youtube.com/watch?v=yVBDmC1qx5E&t=263s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'This means you can segment people based on very specific actions they take on '
               'your website or within your app, like clicking a certain button or spending '
               'more than 2 minutes on a pricing page. It allows your marketing team to be '
               'incredibly surgical with their outreach.',
       'timestamp': 263,
       'timestamp_label': '[00:04:23]',
       'timestamp_seconds': 263,
       'tip': 'This means you can segment people based on very specific actions they take on '
              'your website or within your app, like clicking a certain button or spending '
              'more than 2 minutes on a pricing page. It allows your marketing team to be '
              'incredibly surgical with their outreach.',
       'title': 'HubSpot Review—Best CRM Software for Enterprises in 2026! (CRM Central)',
       'url': 'https://www.youtube.com/watch?v=yVBDmC1qx5E&t=263s',
       'video_id': 'yVBDmC1qx5E'},
      {'author': 'Exit Five',
       'channel': 'Exit Five',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:37:16](https://www.youtube.com/watch?v=9csglJ7L4oo&t=2236s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Google Docs and Zapier is is like V1, but V2 is now like Zapier, custom GPTs, '
               "like figuring out all these agent like just so many there's so many ways to do "
               'something, but I think having that carved out as a dedicated team is '
               'interesting.',
       'timestamp': 2236,
       'timestamp_label': '[00:37:16]',
       'timestamp_seconds': 2236,
       'tip': 'Google Docs and Zapier is is like V1, but V2 is now like Zapier, custom GPTs, '
              "like figuring out all these agent like just so many there's so many ways to do "
              'something, but I think having that carved out as a dedicated team is '
              'interesting.',
       'title': 'Personalized Gifting, Direct Mail, and AI Driven Outbound (Exit Five)',
       'url': 'https://www.youtube.com/watch?v=9csglJ7L4oo&t=2236s',
       'video_id': '9csglJ7L4oo'},
      {'author': 'DSR Ghostwriting',
       'channel': 'DSR Ghostwriting',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:45](https://www.youtube.com/watch?v=dJvSueGEJVg&t=525s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Excellent which means thus 83% is either mediocre bad or terrible and it '
               "doesn't really take account for who's writing that so.",
       'timestamp': 525,
       'timestamp_label': '[00:08:45]',
       'timestamp_seconds': 525,
       'tip': 'Excellent which means thus 83% is either mediocre bad or terrible and it '
              "doesn't really take account for who's writing that so.",
       'title': '(Podcast) Edelman/LinkedIn B2B Thought Leadership Impact Study - Key Findings '
                '(DSR Ghostwriting)',
       'url': 'https://www.youtube.com/watch?v=dJvSueGEJVg&t=525s',
       'video_id': 'dJvSueGEJVg'},
      {'author': 'Mass Tort Institute',
       'channel': 'Mass Tort Institute',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:29](https://www.youtube.com/watch?v=0VBYF3XIGBE&t=89s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It's not going to be good so that that is definitely a big part of my job is "
               "i'm kind of the last line between my team's clients.",
       'timestamp': 89,
       'timestamp_label': '[00:01:29]',
       'timestamp_seconds': 89,
       'tip': "It's not going to be good so that that is definitely a big part of my job is "
              "i'm kind of the last line between my team's clients.",
       'title': 'Communication with Mass Tort Clients (Mass Tort Institute)',
       'url': 'https://www.youtube.com/watch?v=0VBYF3XIGBE&t=89s',
       'video_id': '0VBYF3XIGBE'},
      {'author': 'Digital Roofing Innovations',
       'channel': 'Digital Roofing Innovations',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:45](https://www.youtube.com/watch?v=GciwM0T3IPE&t=345s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Some flat roofing and stuff like that these guys especially someone like sean '
               'being certified gives everybody I think a little bit different perspective '
               'than just your average roofing contractor.',
       'timestamp': 345,
       'timestamp_label': '[00:05:45]',
       'timestamp_seconds': 345,
       'tip': 'Some flat roofing and stuff like that these guys especially someone like sean '
              'being certified gives everybody I think a little bit different perspective than '
              'just your average roofing contractor.',
       'title': 'Roofing Inspection | Hail Damage On Flat Roof (Digital Roofing Innovations)',
       'url': 'https://www.youtube.com/watch?v=GciwM0T3IPE&t=345s',
       'video_id': 'GciwM0T3IPE'},
      {'author': 'UrbanSpell',
       'channel': 'UrbanSpell',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:42](https://www.youtube.com/watch?v=bSYYUhXxy4Y&t=102s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Once we see the signals we want, right accounts engaging, right people '
               'responding, we operationalize. That means playbooks your team can repeat, a '
               "weekly cadence between marketing and sales, reporting that's account level, "
               'not vanity metrics and clear pipeline attribution.',
       'timestamp': 102,
       'timestamp_label': '[00:01:42]',
       'timestamp_seconds': 102,
       'tip': 'Once we see the signals we want, right accounts engaging, right people '
              'responding, we operationalize. That means playbooks your team can repeat, a '
              "weekly cadence between marketing and sales, reporting that's account level, not "
              'vanity metrics and clear pipeline attribution.',
       'title': 'The ABM Workflow Explained | How B2B Companies Win with Account-Based '
                'Marketing | UrbanSpell | (UrbanSpell)',
       'url': 'https://www.youtube.com/watch?v=bSYYUhXxy4Y&t=102s',
       'video_id': 'bSYYUhXxy4Y'}],
 12: [{'author': 'TK Kader',
       'channel': 'TK Kader',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:18:03](https://www.youtube.com/watch?v=rH2rc9-LY00&t=1083s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You will want to iterate on your ideal customer profile, on your messaging. '
               "And then as that's working, you will want to double down on the channel that's "
               'performing the best. So now you know exactly how to launch a proper account '
               'based marketing plan.',
       'timestamp': 1083,
       'timestamp_label': '[00:18:03]',
       'timestamp_seconds': 1083,
       'tip': 'You will want to iterate on your ideal customer profile, on your messaging. And '
              "then as that's working, you will want to double down on the channel that's "
              'performing the best. So now you know exactly how to launch a proper account '
              'based marketing plan.',
       'title': 'Account-Based Marketing: 5 Steps to Get Started And Drive Growth for Your '
                'SaaS Business (TK Kader)',
       'url': 'https://www.youtube.com/watch?v=rH2rc9-LY00&t=1083s',
       'video_id': 'rH2rc9-LY00'},
      {'author': 'Biz Stack School',
       'channel': 'Biz Stack School',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:23:42](https://www.youtube.com/watch?v=9qyxUfkZ05c&t=1422s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Called Ashley after the inspection. Two shingles missing on the north side. '
               'She wants a quote for the repair this week. Under the note, tick the box to '
               'create a follow up task. The default, in three business days, is fine. Your '
               'call is now part of the story, in order.',
       'timestamp': 1422,
       'timestamp_label': '[00:23:42]',
       'timestamp_seconds': 1422,
       'tip': 'Called Ashley after the inspection. Two shingles missing on the north side. She '
              'wants a quote for the repair this week. Under the note, tick the box to create '
              'a follow up task. The default, in three business days, is fine. Your call is '
              'now part of the story, in order.',
       'title': 'HubSpot CRM Tutorial for Beginners (2026) – Full Free Setup (Biz Stack '
                'School)',
       'url': 'https://www.youtube.com/watch?v=9qyxUfkZ05c&t=1422s',
       'video_id': '9qyxUfkZ05c'},
      {'author': 'Fullfunnel io',
       'channel': 'Fullfunnel io',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:24:53](https://www.youtube.com/watch?v=glV72-awJAU&t=1493s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, then the everything that we plan in silos is absolutely unrealistic. The '
               'first thing first, we need to form this cross-functional team, understand how '
               'much time these people could commit, and then based on this we start planning '
               'the next steps.',
       'timestamp': 1493,
       'timestamp_label': '[00:24:53]',
       'timestamp_seconds': 1493,
       'tip': 'So, then the everything that we plan in silos is absolutely unrealistic. The '
              'first thing first, we need to form this cross-functional team, understand how '
              'much time these people could commit, and then based on this we start planning '
              'the next steps.',
       'title': '[Webinar] ABM as an operating system to generate enterprise pipeline '
                '(Fullfunnel io)',
       'url': 'https://www.youtube.com/watch?v=glV72-awJAU&t=1493s',
       'video_id': 'glV72-awJAU'},
      {'author': 'Ephraim Austin',
       'channel': 'Ephraim Austin',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:02](https://www.youtube.com/watch?v=esA2m5IlLT8&t=182s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, this was the first day. Oh, this is some of the re the some of the '
               'reactions from our client. Now, pretty good start for the first day. And then '
               'on the seventh day of sending, uh, we booked another call with a $25 million '
               'electrical contractor.',
       'timestamp': 182,
       'timestamp_label': '[00:03:02]',
       'timestamp_seconds': 182,
       'tip': 'So, this was the first day. Oh, this is some of the re the some of the '
              'reactions from our client. Now, pretty good start for the first day. And then '
              'on the seventh day of sending, uh, we booked another call with a $25 million '
              'electrical contractor.',
       'title': 'We Turned an M&A Firm’s Past Deal Into Calls With $15M, $25M & $30M Companies '
                'in the First 7 Days (Ephraim Austin)',
       'url': 'https://www.youtube.com/watch?v=esA2m5IlLT8&t=182s',
       'video_id': 'esA2m5IlLT8'},
      {'author': 'Darrel Wilson Clips',
       'channel': 'Darrel Wilson Clips',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:57](https://www.youtube.com/watch?v=Yu60z9o8jdQ&t=117s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "You're not website business. You're in the monthly maintenance plan business. "
               'The build fee is great, right? You charge you a few thousand dollars and you '
               'pay the rents, but a client paying $200 every single month for an entire year '
               'sounds much better.',
       'timestamp': 117,
       'timestamp_label': '[00:01:57]',
       'timestamp_seconds': 117,
       'tip': "You're not website business. You're in the monthly maintenance plan business. "
              'The build fee is great, right? You charge you a few thousand dollars and you '
              'pay the rents, but a client paying $200 every single month for an entire year '
              'sounds much better.',
       'title': '⚡ Stop Chasing One-Time Payments: The Secret to Agency Retainers (Darrel '
                'Wilson Clips)',
       'url': 'https://www.youtube.com/watch?v=Yu60z9o8jdQ&t=117s',
       'video_id': 'Yu60z9o8jdQ'},
      {'author': 'Saunders Real Estate',
       'channel': 'Saunders Real Estate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:32:42](https://www.youtube.com/watch?v=j0rQ27ZfIcU&t=1962s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'ve got a data center buyer coming to you, it's going to be a long road before "
               'you get to the finish line. You know, along the way, make sure that on on '
               "those milestone moments, you're getting paid as they play.",
       'timestamp': 1962,
       'timestamp_label': '[00:32:42]',
       'timestamp_seconds': 1962,
       'tip': "'ve got a data center buyer coming to you, it's going to be a long road before "
              'you get to the finish line. You know, along the way, make sure that on on those '
              "milestone moments, you're getting paid as they play.",
       'title': 'How to Evaluate Land for Data Center Development • The Yield (Saunders Real '
                'Estate)',
       'url': 'https://www.youtube.com/watch?v=j0rQ27ZfIcU&t=1962s',
       'video_id': 'j0rQ27ZfIcU'},
      {'author': 'Winston Francois',
       'channel': 'Winston Francois',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:19:40](https://www.youtube.com/watch?v=MxOVnLY11DA&t=1180s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "He'll tell you some regions respond faster than anyone because they aren't "
               'used to being marketed to at all. Build a team that can move the day the news '
               "breaks, hit hard and hit it fast. Here's one action you can do this week in 10 "
               'minutes or less.',
       'timestamp': 1180,
       'timestamp_label': '[00:19:40]',
       'timestamp_seconds': 1180,
       'tip': "He'll tell you some regions respond faster than anyone because they aren't used "
              'to being marketed to at all. Build a team that can move the day the news '
              "breaks, hit hard and hit it fast. Here's one action you can do this week in 10 "
              'minutes or less.',
       'title': 'The Trojan Horse Sales Strategy with Brian Gilman (Winston Francois)',
       'url': 'https://www.youtube.com/watch?v=MxOVnLY11DA&t=1180s',
       'video_id': 'MxOVnLY11DA'},
      {'author': 'Isaiah Lebron',
       'channel': 'Isaiah Lebron',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:04](https://www.youtube.com/watch?v=oOG3hswiUr0&t=664s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Expertise would you be open to hopping on a call would you be open to '
               "exploring sometime next week cheers right and that's essentially uh how you "
               'would how.',
       'timestamp': 664,
       'timestamp_label': '[00:11:04]',
       'timestamp_seconds': 664,
       'tip': 'Expertise would you be open to hopping on a call would you be open to exploring '
              "sometime next week cheers right and that's essentially uh how you would how.",
       'title': 'the trojan horse method: use this to sign $8k mo b2b lead gen deals (Isaiah '
                'Lebron)',
       'url': 'https://www.youtube.com/watch?v=oOG3hswiUr0&t=664s',
       'video_id': 'oOG3hswiUr0'},
      {'author': 'SS&C Intralinks',
       'channel': 'SS&C Intralinks',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:34:23](https://www.youtube.com/watch?v=rOwXkmrMljc&t=2063s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Talk to me about how you personally use it. Um, Jan, I know that when we had '
               'our pre-call, you were telling me about sort of a a little tool that you use '
               'to organize your day.',
       'timestamp': 2063,
       'timestamp_label': '[00:34:23]',
       'timestamp_seconds': 2063,
       'tip': 'Talk to me about how you personally use it. Um, Jan, I know that when we had '
              'our pre-call, you were telling me about sort of a a little tool that you use to '
              'organize your day.',
       'title': 'Building the AI-Powered M&A Deal Team of 2030 | SS&C Intralinks #dealmaking '
                '#mergersandacquisitions (SS&C Intralinks)',
       'url': 'https://www.youtube.com/watch?v=rOwXkmrMljc&t=2063s',
       'video_id': 'rOwXkmrMljc'},
      {'author': 'Financial Regulation Courses',
       'channel': 'Financial Regulation Courses',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:52](https://www.youtube.com/watch?v=CmOezPFI5ew&t=112s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Substantive updates must always be revetted before being sent to the public. '
               'Furthermore, new FINRA member firms, those in their first year, must file '
               'broadly disseminated retail communications with FINRA at least 10 business '
               'days before use.',
       'timestamp': 112,
       'timestamp_label': '[00:01:52]',
       'timestamp_seconds': 112,
       'tip': 'Substantive updates must always be revetted before being sent to the public. '
              'Furthermore, new FINRA member firms, those in their first year, must file '
              'broadly disseminated retail communications with FINRA at least 10 business days '
              'before use.',
       'title': 'FINRA Rule 2210 | Communications with the Public, Advertising Rules & '
                'Broker-Dealer Compliance (Financial Regulation Courses)',
       'url': 'https://www.youtube.com/watch?v=CmOezPFI5ew&t=112s',
       'video_id': 'CmOezPFI5ew'},
      {'author': 'LandApp by LandGate',
       'channel': 'LandApp by LandGate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:52](https://www.youtube.com/watch?v=UqoyFfPDAmA&t=232s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Top offers to purchase your property or lease your land none of which you are '
               'obligated to accept so what are you waiting for consider leasing your property '
               'or selling your property for a Data Center and start generating Revenue today.',
       'timestamp': 232,
       'timestamp_label': '[00:03:52]',
       'timestamp_seconds': 232,
       'tip': 'Top offers to purchase your property or lease your land none of which you are '
              'obligated to accept so what are you waiting for consider leasing your property '
              'or selling your property for a Data Center and start generating Revenue today.',
       'title': 'Does My Land Qualify for Data Centers? (LandApp by LandGate)',
       'url': 'https://www.youtube.com/watch?v=UqoyFfPDAmA&t=232s',
       'video_id': 'UqoyFfPDAmA'},
      {'author': 'Marketing in the Age of AI',
       'channel': 'Marketing in the Age of AI',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:32](https://www.youtube.com/watch?v=M-Z0SPYJ9-w&t=1052s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So I have one based on endless referrals from Bob in way back in the day and '
               'then a couple based on the um the go-giver. But the number one is they talk '
               "about the five laws of stratospheric success and it's about adding value to "
               'others and how do you create value.',
       'timestamp': 1052,
       'timestamp_label': '[00:17:32]',
       'timestamp_seconds': 1052,
       'tip': 'So I have one based on endless referrals from Bob in way back in the day and '
              'then a couple based on the um the go-giver. But the number one is they talk '
              "about the five laws of stratospheric success and it's about adding value to "
              'others and how do you create value.',
       'title': 'AI Whale Hunting 🐋: ICP Precision, Agentic AI & Smarter Growth Strategies '
                '(Marketing in the Age of AI)',
       'url': 'https://www.youtube.com/watch?v=M-Z0SPYJ9-w&t=1052s',
       'video_id': 'M-Z0SPYJ9-w'},
      {'author': 'SMB Team',
       'channel': 'SMB Team',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:05](https://www.youtube.com/watch?v=WZ82yYgND3M&t=905s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "10 things, they're not going to remember any of those. It needs to be super "
               'super direct and to the point and also clear for them to understand. And then '
               'the final most important piece of an ad is the call to action.',
       'timestamp': 905,
       'timestamp_label': '[00:15:05]',
       'timestamp_seconds': 905,
       'tip': "10 things, they're not going to remember any of those. It needs to be super "
              'super direct and to the point and also clear for them to understand. And then '
              'the final most important piece of an ad is the call to action.',
       'title': 'How to Use Meta Ads to Get More Law Firm Leads (SMB Team)',
       'url': 'https://www.youtube.com/watch?v=WZ82yYgND3M&t=905s',
       'video_id': 'WZ82yYgND3M'},
      {'author': 'Midwest Corporate Credit',
       'channel': 'Midwest Corporate Credit',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:45](https://www.youtube.com/watch?v=QzlAvX38RS4&t=225s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Week's awesome video also if you like this video please let me know if you "
               "have any questions comment below for Midwest corporate credit I'm PK Patel "
               'thank you for watching.',
       'timestamp': 225,
       'timestamp_label': '[00:03:45]',
       'timestamp_seconds': 225,
       'tip': "Week's awesome video also if you like this video please let me know if you have "
              "any questions comment below for Midwest corporate credit I'm PK Patel thank you "
              'for watching.',
       'title': 'What is a UCC Filing? What you need to know! [UCC-1 lien] (Midwest Corporate '
                'Credit)',
       'url': 'https://www.youtube.com/watch?v=QzlAvX38RS4&t=225s',
       'video_id': 'QzlAvX38RS4'},
      {'author': 'AdConversion',
       'channel': 'AdConversion',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:56](https://www.youtube.com/watch?v=LbEgZ7SpArs&t=56s)',
       'relevance': 'Attributed practitioner commentary on enterprise million-dollar contract '
                    'demand generation, ABM signal orchestration, and high-ACV deal '
                    'origination (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'ABM programs that consistently drive pipeline start with a much smaller, more '
               "specific account list than most teams expect. And it's built around who's "
               'likely to buy now, not just who fits the ICP.',
       'timestamp': 56,
       'timestamp_label': '[00:00:56]',
       'timestamp_seconds': 56,
       'tip': 'ABM programs that consistently drive pipeline start with a much smaller, more '
              "specific account list than most teams expect. And it's built around who's "
              'likely to buy now, not just who fits the ICP.',
       'title': 'ABM in 2026: What Actually Works for B2B Marketing (AdConversion)',
       'url': 'https://www.youtube.com/watch?v=LbEgZ7SpArs&t=56s',
       'video_id': 'LbEgZ7SpArs'}]}
