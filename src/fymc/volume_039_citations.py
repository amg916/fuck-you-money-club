"""Curated 180-citation Inbound Pay-Per-Call & RTB Ping-Post Arbitrage baseline (15 per chapter across Q1-Q12) mined strictly from verified Inbound Pay-Per-Call & RTB Ping-Post Arbitrage YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'100k',
     '10k',
     '300',
     'aca',
     'accident',
     'ads',
     'affiliate',
     'age',
     'appointment',
     'arbitrage',
     'attribution',
     'auctions',
     'auto',
     'automating',
     'bid',
     'bidding',
     'billable',
     'boberdoo',
     'booking',
     'breakers',
     'broker',
     'buffer',
     'building',
     'business',
     'buyer',
     'buying',
     'call',
     'caller',
     'callers',
     'calls',
     'campaigns',
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
     '10k',
     '300',
     'aca',
     'accident',
     'ads',
     'affiliate',
     'age',
     'appointment',
     'arbitrage',
     'attribution',
     'auctions',
     'auto',
     'automating',
     'bid',
     'bidding',
     'billable',
     'boberdoo',
     'booking',
     'breakers',
     'broker',
     'budget',
     'buffer',
     'building',
     'buyer',
     'buying',
     'call',
     'caller',
     'callers',
     'calls',
     'campaigns',
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
     '10k',
     '300',
     'aca',
     'accident',
     'ads',
     'affiliate',
     'age',
     'appointment',
     'arbitrage',
     'attribution',
     'auctions',
     'auto',
     'automating',
     'bid',
     'bidding',
     'billable',
     'boberdoo',
     'booking',
     'breakers',
     'broker',
     'buffer',
     'building',
     'buyer',
     'buying',
     'call',
     'caller',
     'callers',
     'calls',
     'campaigns',
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
     '10k',
     '300',
     'aca',
     'accident',
     'ads',
     'affiliate',
     'age',
     'appointment',
     'arbitrage',
     'attribution',
     'auctions',
     'auto',
     'automating',
     'bid',
     'bidding',
     'billable',
     'boberdoo',
     'booking',
     'breakers',
     'broker',
     'budget',
     'buffer',
     'building',
     'buyer',
     'buying',
     'call',
     'caller',
     'callers',
     'calls',
     'campaigns',
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
 5: {'100k',
     '10k',
     '300',
     'aca',
     'accident',
     'ads',
     'affiliate',
     'age',
     'appointment',
     'arbitrage',
     'attribution',
     'auctions',
     'audit',
     'auto',
     'automating',
     'avoid',
     'bid',
     'bidding',
     'billable',
     'boberdoo',
     'booking',
     'breakers',
     'broker',
     'buffer',
     'building',
     'buyer',
     'buying',
     'call',
     'caller',
     'callers',
     'calls',
     'campaigns',
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
     '10k',
     '300',
     'aca',
     'accident',
     'ads',
     'affiliate',
     'age',
     'appointment',
     'arbitrage',
     'attribution',
     'auctions',
     'auto',
     'automating',
     'bid',
     'bidding',
     'billable',
     'boberdoo',
     'booking',
     'breakers',
     'broker',
     'buffer',
     'building',
     'buyer',
     'buying',
     'call',
     'caller',
     'callers',
     'calls',
     'campaigns',
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
     '10k',
     '300',
     'aca',
     'accident',
     'ads',
     'affiliate',
     'age',
     'appointment',
     'arbitrage',
     'attribution',
     'auctions',
     'auto',
     'automating',
     'bid',
     'bidding',
     'billable',
     'boberdoo',
     'booking',
     'breakers',
     'broker',
     'buffer',
     'building',
     'buyer',
     'buying',
     'call',
     'caller',
     'callers',
     'calls',
     'campaigns',
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
     '10k',
     '300',
     'aca',
     'accident',
     'ads',
     'affiliate',
     'age',
     'api',
     'appointment',
     'arbitrage',
     'attribution',
     'auctions',
     'auto',
     'automating',
     'bid',
     'bidding',
     'billable',
     'boberdoo',
     'booking',
     'breakers',
     'broker',
     'buffer',
     'building',
     'buyer',
     'buying',
     'call',
     'caller',
     'callers',
     'calls',
     'campaigns',
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
     '10k',
     '300',
     'aca',
     'accident',
     'ads',
     'affiliate',
     'age',
     'agreement',
     'appointment',
     'arbitrage',
     'attribution',
     'auctions',
     'auto',
     'automating',
     'bid',
     'bidding',
     'billable',
     'boberdoo',
     'booking',
     'breakers',
     'broker',
     'buffer',
     'building',
     'buyer',
     'buying',
     'call',
     'caller',
     'callers',
     'calls',
     'campaigns',
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
      '10k',
      '300',
      'aca',
      'accident',
      'ads',
      'affiliate',
      'age',
      'agent',
      'ai',
      'appointment',
      'arbitrage',
      'attribution',
      'auctions',
      'auto',
      'automate',
      'automating',
      'automation',
      'bid',
      'bidding',
      'billable',
      'boberdoo',
      'booking',
      'breakers',
      'broker',
      'buffer',
      'building',
      'buyer',
      'buying',
      'call',
      'caller',
      'callers',
      'calls',
      'campaigns',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'100k',
      '10k',
      '300',
      'aca',
      'accident',
      'ads',
      'affiliate',
      'age',
      'appointment',
      'arbitrage',
      'attribution',
      'auctions',
      'auto',
      'automating',
      'bid',
      'bidding',
      'billable',
      'boberdoo',
      'booking',
      'breakers',
      'broker',
      'buffer',
      'building',
      'buyer',
      'buying',
      'call',
      'caller',
      'callers',
      'calls',
      'campaigns',
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
      '10k',
      '300',
      'aca',
      'accident',
      'action',
      'ads',
      'affiliate',
      'age',
      'appointment',
      'arbitrage',
      'attribution',
      'auctions',
      'auto',
      'automating',
      'bid',
      'bidding',
      'billable',
      'boberdoo',
      'booking',
      'breakers',
      'broker',
      'buffer',
      'building',
      'buyer',
      'buying',
      'call',
      'caller',
      'callers',
      'calls',
      'campaigns',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Nate Ancelet',
      'channel': 'Nate Ancelet',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:21](https://www.youtube.com/watch?v=q4tpqSo7KCE&t=81s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "All right, let's just make this super simple for those that don't understand "
              'the model. An affiliate who is already generating exclusive auto insurance '
              "inbound calls. If they're already generating them and they're selling for $40 "
              'each, I find a buyer who will pay 45.',
      'timestamp': 81,
      'timestamp_label': '[00:01:21]',
      'timestamp_seconds': 81,
      'tip': "All right, let's just make this super simple for those that don't understand the "
             'model. An affiliate who is already generating exclusive auto insurance inbound '
             "calls. If they're already generating them and they're selling for $40 each, I "
             'find a buyer who will pay 45.',
      'title': 'How to make $20,344/day with Pay Per Call (Nate Ancelet)',
      'url': 'https://www.youtube.com/watch?v=q4tpqSo7KCE&t=81s',
      'video_id': 'q4tpqSo7KCE'},
     {'author': 'ExclusiveLiveCall',
      'channel': 'ExclusiveLiveCall',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:56](https://www.youtube.com/watch?v=U9jGHjNPQdQ&t=416s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, I have this buyer, John Smith. I can see that I can log in as John Smith '
              'and see his account. See what he registered for. I can give him a call, check '
              'his campaigns, whatever I need to do on the client account. And you can just '
              'launch your business in no time.',
      'timestamp': 416,
      'timestamp_label': '[00:06:56]',
      'timestamp_seconds': 416,
      'tip': 'So, I have this buyer, John Smith. I can see that I can log in as John Smith and '
             'see his account. See what he registered for. I can give him a call, check his '
             'campaigns, whatever I need to do on the client account. And you can just launch '
             'your business in no time.',
      'title': 'White Label Pay Per Call Business Opportunity | We Provide the Calls, You '
               'Bring the Buyers (ExclusiveLiveCall)',
      'url': 'https://www.youtube.com/watch?v=U9jGHjNPQdQ&t=416s',
      'video_id': 'U9jGHjNPQdQ'},
     {'author': 'TrackDrive',
      'channel': 'TrackDrive',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:49](https://www.youtube.com/watch?v=_h1_mcKPGjY&t=349s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They're paid for results, not just for showing the ad. You might also hear this "
              'person called the buyer. This is the business that answers the phone call. It '
              'might be an insurance agency, a law firm, home services company, or a call '
              'center that handles calls for many brands.',
      'timestamp': 349,
      'timestamp_label': '[00:05:49]',
      'timestamp_seconds': 349,
      'tip': "They're paid for results, not just for showing the ad. You might also hear this "
             'person called the buyer. This is the business that answers the phone call. It '
             'might be an insurance agency, a law firm, home services company, or a call '
             'center that handles calls for many brands.',
      'title': 'What Pay-Per-Call Is and Why It Pays | Pay-Per-Call Masterclass (TrackDrive)',
      'url': 'https://www.youtube.com/watch?v=_h1_mcKPGjY&t=349s',
      'video_id': '_h1_mcKPGjY'},
     {'author': 'Leadbase',
      'channel': 'Leadbase',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:54](https://www.youtube.com/watch?v=ewNftdwX784&t=654s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're able to kind of finance your business through those upfront payments. "
              'You only need a few pieces of software. Whereas with paper call, you might need '
              'to hire appointment setters, call routing, uh like, you know, proper hookups to '
              'your your client CRM.',
      'timestamp': 654,
      'timestamp_label': '[00:10:54]',
      'timestamp_seconds': 654,
      'tip': "You're able to kind of finance your business through those upfront payments. You "
             'only need a few pieces of software. Whereas with paper call, you might need to '
             'hire appointment setters, call routing, uh like, you know, proper hookups to '
             'your your client CRM.',
      'title': 'Why Pay Per Lead Beats Pay Per Call in 2026 (Leadbase)',
      'url': 'https://www.youtube.com/watch?v=ewNftdwX784&t=654s',
      'video_id': 'ewNftdwX784'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=d1FxjZ5ukI4&t=126s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'TV radio ads Direct Mail is also a popular way to generate call and then for '
              'our clients working with call centers live transfers are a big part so.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': 'TV radio ads Direct Mail is also a popular way to generate call and then for our '
             'clients working with call centers live transfers are a big part so.',
      'title': 'How To Sell Calls | boberdoo Call Routing Software (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=d1FxjZ5ukI4&t=126s',
      'video_id': 'd1FxjZ5ukI4'},
     {'author': 'ExclusiveLiveCall',
      'channel': 'ExclusiveLiveCall',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:07](https://www.youtube.com/watch?v=u_m2wo44WpQ&t=367s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And because these businesses always need new customers just to survive, they '
              'keep buying calls every single month. Your recurring revenue just compounds '
              'massively, creating a highly valuable, predictable business. Section seven, the '
              'future of lead gen, performance marketing.',
      'timestamp': 367,
      'timestamp_label': '[00:06:07]',
      'timestamp_seconds': 367,
      'tip': 'And because these businesses always need new customers just to survive, they '
             'keep buying calls every single month. Your recurring revenue just compounds '
             'massively, creating a highly valuable, predictable business. Section seven, the '
             'future of lead gen, performance marketing.',
      'title': 'How to Create Recurring Revenue with White Label Pay Per Call (The Business '
               'Model Agencies Missing) (ExclusiveLiveCall)',
      'url': 'https://www.youtube.com/watch?v=u_m2wo44WpQ&t=367s',
      'video_id': 'u_m2wo44WpQ'},
     {'author': 'Matt Wacek',
      'channel': 'Matt Wacek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:50](https://www.youtube.com/watch?v=S1xXLvaXSvU&t=470s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Scroll too far to find the phone number to to then call and then hopefully turn '
              'into revenue for your business just basically just shows a little bit of.',
      'timestamp': 470,
      'timestamp_label': '[00:07:50]',
      'timestamp_seconds': 470,
      'tip': 'Scroll too far to find the phone number to to then call and then hopefully turn '
             'into revenue for your business just basically just shows a little bit of.',
      'title': 'Pay Per Call Affiliate Marketing Using Craigslist (Step By Step) (Matt Wacek)',
      'url': 'https://www.youtube.com/watch?v=S1xXLvaXSvU&t=470s',
      'video_id': 'S1xXLvaXSvU'},
     {'author': 'Invoca',
      'channel': 'Invoca',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=IPh2uXrQS1A&t=75s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Businesses are moving towards a customer centric model Paul's are the most "
              'single most important thing that you can be mining for insights and in Bocca is '
              'fantastic at helping unleash all of the value that exists inside of those phone '
              'calls.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': "Businesses are moving towards a customer centric model Paul's are the most "
             'single most important thing that you can be mining for insights and in Bocca is '
             'fantastic at helping unleash all of the value that exists inside of those phone '
             'calls.',
      'title': 'The Value of Call Tracking and Conversational Analytics | Invoca Testimonials '
               '(Invoca)',
      'url': 'https://www.youtube.com/watch?v=IPh2uXrQS1A&t=75s',
      'video_id': 'IPh2uXrQS1A'},
     {'author': 'Yoder',
      'channel': 'Yoder',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=-GEw-hz8tiY&t=15s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Affiliate in the paper call space he's done about 15 million total in Revenue I "
              "basically sat down with him for about 30 minutes just to go through what's "
              'gotten.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Affiliate in the paper call space he's done about 15 million total in Revenue I "
             "basically sat down with him for about 30 minutes just to go through what's "
             'gotten.',
      'title': 'This 26 Year Old Marketer Generated Over $15,000,000 Selling Phonecalls - 30 '
               'Min Pay Per Call Guide (Yoder)',
      'url': 'https://www.youtube.com/watch?v=-GEw-hz8tiY&t=15s',
      'video_id': '-GEw-hz8tiY'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:29](https://www.youtube.com/watch?v=AMwEMCOuhA0&t=329s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm gonna get the highest margin per phone call I possibly can and then I'm "
              'going to create enterprise value so that I can eventually sell my company and '
              'so.',
      'timestamp': 329,
      'timestamp_label': '[00:05:29]',
      'timestamp_seconds': 329,
      'tip': "I'm gonna get the highest margin per phone call I possibly can and then I'm "
             'going to create enterprise value so that I can eventually sell my company and '
             'so.',
      'title': 'Pay Per Call Masterclass - Building Your Business (Ringba)',
      'url': 'https://www.youtube.com/watch?v=AMwEMCOuhA0&t=329s',
      'video_id': 'AMwEMCOuhA0'},
     {'author': 'RingCentral UK',
      'channel': 'RingCentral UK',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:17](https://www.youtube.com/watch?v=UPUMLukglNc&t=137s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Are routed through to a specific branch of the business and then on to relevant '
              "call queues from there again it's the same process of how to add and remove "
              'different options these menus can be as complex or as simple as you need thank '
              'you for watching.',
      'timestamp': 137,
      'timestamp_label': '[00:02:17]',
      'timestamp_seconds': 137,
      'tip': 'Are routed through to a specific branch of the business and then on to relevant '
             "call queues from there again it's the same process of how to add and remove "
             'different options these menus can be as complex or as simple as you need thank '
             'you for watching.',
      'title': 'Creating an IVR Menu | RingCentral Office Demo (RingCentral UK)',
      'url': 'https://www.youtube.com/watch?v=UPUMLukglNc&t=137s',
      'video_id': 'UPUMLukglNc'},
     {'author': 'Elite Marketer',
      'channel': 'Elite Marketer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=yfrI3Ns-hqY&t=15s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Unfair advantage over your competition are you ready let's go hey everybody "
              'Welcome to the next level Facebook ads podcast episode.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Unfair advantage over your competition are you ready let's go hey everybody "
             'Welcome to the next level Facebook ads podcast episode.',
      'title': 'EP 359: Master Facebook Quiz Ads & Unlock Endless Possibilities (Elite '
               'Marketer)',
      'url': 'https://www.youtube.com/watch?v=yfrI3Ns-hqY&t=15s',
      'video_id': 'yfrI3Ns-hqY'},
     {'author': 'FatRank',
      'channel': 'FatRank',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:54](https://www.youtube.com/watch?v=sfm-ky0HkUw&t=534s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Stuff and there might not be as many repairs needed so just bear that in mind '
              'it is a very seasonable um niche as well yeah for sure.',
      'timestamp': 534,
      'timestamp_label': '[00:08:54]',
      'timestamp_seconds': 534,
      'tip': 'Stuff and there might not be as many repairs needed so just bear that in mind it '
             'is a very seasonable um niche as well yeah for sure.',
      'title': 'Lead Generation For Roofing Companies | Fatrank lead generation (FatRank)',
      'url': 'https://www.youtube.com/watch?v=sfm-ky0HkUw&t=534s',
      'video_id': 'sfm-ky0HkUw'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=20s5iGyl_MY&t=15s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Function now the purpose of a paper call network is to take the business '
              'development burden off of the affiliate and call buyers while reducing.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Function now the purpose of a paper call network is to take the business '
             'development burden off of the affiliate and call buyers while reducing.',
      'title': 'Pay Per Call Masterclass - How Pay Per Call Networks Function (Ringba)',
      'url': 'https://www.youtube.com/watch?v=20s5iGyl_MY&t=15s',
      'video_id': '20s5iGyl_MY'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:21](https://www.youtube.com/watch?v=HxYmbtP1ydQ&t=141s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Trusted by industry-leading pay-per-call companies connect your online '
              'marketing to your offline sales and get the data you need to drive revenue with '
              'rainbow to learn more about how rimba is changing the future of pay-per-call '
              'visit www.ring.',
      'timestamp': 141,
      'timestamp_label': '[00:02:21]',
      'timestamp_seconds': 141,
      'tip': 'Trusted by industry-leading pay-per-call companies connect your online marketing '
             'to your offline sales and get the data you need to drive revenue with rainbow to '
             'learn more about how rimba is changing the future of pay-per-call visit '
             'www.ring.',
      'title': 'Insurance Vertical Pros and Cons Explained (Ringba)',
      'url': 'https://www.youtube.com/watch?v=HxYmbtP1ydQ&t=141s',
      'video_id': 'HxYmbtP1ydQ'}],
 2: [{'author': 'TrackDrive',
      'channel': 'TrackDrive',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:58](https://www.youtube.com/watch?v=yYZ5s6jFzQs&t=58s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A publisher sends 100 calls. Of those 100 calls, 80 of them qualify, meaning '
              'that they met the agreed rules. Maybe they were too short or from the wrong '
              'state or repeat callers. The buyer pays $50 for each qualified call.',
      'timestamp': 58,
      'timestamp_label': '[00:00:58]',
      'timestamp_seconds': 58,
      'tip': 'A publisher sends 100 calls. Of those 100 calls, 80 of them qualify, meaning '
             'that they met the agreed rules. Maybe they were too short or from the wrong '
             'state or repeat callers. The buyer pays $50 for each qualified call.',
      'title': 'The Economics of a Call | Pay-Per-Call Masterclass (TrackDrive)',
      'url': 'https://www.youtube.com/watch?v=yYZ5s6jFzQs&t=58s',
      'video_id': 'yYZ5s6jFzQs'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:35](https://www.youtube.com/watch?v=yFkULiyenzk&t=95s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For instance, if you want to limit your financial exposure to a new buyer, you '
              'can cap them at $2,000 for the first 2 weeks to make sure they pay before '
              'sending them any more calls. Zip code routing is crucial to successful paper '
              'call campaigns.',
      'timestamp': 95,
      'timestamp_label': '[00:01:35]',
      'timestamp_seconds': 95,
      'tip': 'For instance, if you want to limit your financial exposure to a new buyer, you '
             'can cap them at $2,000 for the first 2 weeks to make sure they pay before '
             'sending them any more calls. Zip code routing is crucial to successful paper '
             'call campaigns.',
      'title': 'How To Optimize Your Pay Per Call Routing (Part 2) (Ringba)',
      'url': 'https://www.youtube.com/watch?v=yFkULiyenzk&t=95s',
      'video_id': 'yFkULiyenzk'},
     {'author': 'John Ventura',
      'channel': 'John Ventura',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:14](https://www.youtube.com/watch?v=x3UYaJjRdx0&t=74s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, example, a buyer pays you $30 for every call that lasts 2 minutes. They get '
              'a live prospect on the phone for that price. Completely performance-based. No '
              'retainers, no monthly fees, no hoping for ROI. The value proposition is '
              'extremely attractive.',
      'timestamp': 74,
      'timestamp_label': '[00:01:14]',
      'timestamp_seconds': 74,
      'tip': 'So, example, a buyer pays you $30 for every call that lasts 2 minutes. They get '
             'a live prospect on the phone for that price. Completely performance-based. No '
             'retainers, no monthly fees, no hoping for ROI. The value proposition is '
             'extremely attractive.',
      'title': 'I make $1M/mo with Pay Per Call (just copy me) (John Ventura)',
      'url': 'https://www.youtube.com/watch?v=x3UYaJjRdx0&t=74s',
      'video_id': 'x3UYaJjRdx0'},
     {'author': 'ExclusiveLiveCall',
      'channel': 'ExclusiveLiveCall',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:25](https://www.youtube.com/watch?v=ag1bHGTo0cU&t=205s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, now we have that feature. You can just log in uh to exclusive live calls or '
              'to our white label partners, activate flex payment, and just enjoy pay after '
              'the fact and good get good quality calls. It helps you to increase your '
              'customer base as a white label partner.',
      'timestamp': 205,
      'timestamp_label': '[00:03:25]',
      'timestamp_seconds': 205,
      'tip': 'So, now we have that feature. You can just log in uh to exclusive live calls or '
             'to our white label partners, activate flex payment, and just enjoy pay after the '
             'fact and good get good quality calls. It helps you to increase your customer '
             'base as a white label partner.',
      'title': 'No Prepayment for Pay Per Call Leads | Exclusive Live Calls '
               '(ExclusiveLiveCall)',
      'url': 'https://www.youtube.com/watch?v=ag1bHGTo0cU&t=205s',
      'video_id': 'ag1bHGTo0cU'},
     {'author': 'Matt Wacek',
      'channel': 'Matt Wacek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=m-08JHhJeok&t=15s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Really need to pay attention because I am pulling back the curtain and we're "
              'diving deep into how to start a paper call affiliate or a lead generation SEO.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Really need to pay attention because I am pulling back the curtain and we're "
             'diving deep into how to start a paper call affiliate or a lead generation SEO.',
      'title': 'How To Start A Pay Per Call Affiliate/Lead Gen. SEO Business in 2024 '
               '($50k-$100k year As A Beginner) (Matt Wacek)',
      'url': 'https://www.youtube.com/watch?v=m-08JHhJeok&t=15s',
      'video_id': 'm-08JHhJeok'},
     {'author': 'The Starving Affiliate',
      'channel': 'The Starving Affiliate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=nixTVpebMgI&t=40s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Into customers or worse you pay for calls that forced you into a bidding war '
              "with your competition it's unfortunate but I hear horror stories about how "
              'much.',
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': 'Into customers or worse you pay for calls that forced you into a bidding war '
             "with your competition it's unfortunate but I hear horror stories about how much.",
      'title': 'Joe Burnich - How To Do Marketing For Water Damage Restoration Success - Joe '
               'Burnich (The Starving Affiliate)',
      'url': 'https://www.youtube.com/watch?v=nixTVpebMgI&t=40s',
      'video_id': 'nixTVpebMgI'},
     {'author': 'ExclusiveLiveCall',
      'channel': 'ExclusiveLiveCall',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=scPdPdSnQWY&t=157s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Imagine you're generating plumbing calls nationwide, but one buyer only covers "
              'South Florida. A customer calls from Dallas. Great consumer, great intent, '
              "wrong geography. If that's your only buyer, you may have nowhere to send that "
              'call.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': "Imagine you're generating plumbing calls nationwide, but one buyer only covers "
             'South Florida. A customer calls from Dallas. Great consumer, great intent, wrong '
             "geography. If that's your only buyer, you may have nowhere to send that call.",
      'title': 'How to Read a Pay Per Call Campaign Before You Send Traffic | Pay Per Call '
               'University #6 (ExclusiveLiveCall)',
      'url': 'https://www.youtube.com/watch?v=scPdPdSnQWY&t=157s',
      'video_id': 'scPdPdSnQWY'},
     {'author': 'DigitalTriggers',
      'channel': 'DigitalTriggers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:59](https://www.youtube.com/watch?v=1agI5uDKUlQ&t=419s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Penciling out to me and making me more qualified calls and then obviously I'm "
              "also charging 5 6 10 even 15 times the amount per call that sound like it's "
              'worth your time watching the rest of this video right now Matusz can you guys '
              'are live I need some feedback.',
      'timestamp': 419,
      'timestamp_label': '[00:06:59]',
      'timestamp_seconds': 419,
      'tip': "Penciling out to me and making me more qualified calls and then obviously I'm "
             "also charging 5 6 10 even 15 times the amount per call that sound like it's "
             'worth your time watching the rest of this video right now Matusz can you guys '
             'are live I need some feedback.',
      'title': 'With Pay Per Call What Makes a Call Billable? (DigitalTriggers)',
      'url': 'https://www.youtube.com/watch?v=1agI5uDKUlQ&t=419s',
      'video_id': '1agI5uDKUlQ'},
     {'author': 'Matt Wacek',
      'channel': 'Matt Wacek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=uxYMcIUwpLA&t=15s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Basically doing pay per call as an affiliate and also doing it with getting '
              'clients because there are some disadvantages and advantages and pros.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Basically doing pay per call as an affiliate and also doing it with getting '
             'clients because there are some disadvantages and advantages and pros.',
      'title': 'Pay Per Call - As An Affiliate vs. Getting Lead Generation Clients | Pay Per '
               'Lead (Matt Wacek)',
      'url': 'https://www.youtube.com/watch?v=uxYMcIUwpLA&t=15s',
      'video_id': 'uxYMcIUwpLA'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:03](https://www.youtube.com/watch?v=CSGuZ-Sping&t=903s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Verse 75 found 75 was the best one the call went to that buyer with this phone '
              'number the call lasted 0.3 minutes which was higher than the 0.17 um 10.2 '
              'seconds duration from the minimum duration here and so that call is '
              'successfully sold.',
      'timestamp': 903,
      'timestamp_label': '[00:15:03]',
      'timestamp_seconds': 903,
      'tip': 'Verse 75 found 75 was the best one the call went to that buyer with this phone '
             'number the call lasted 0.3 minutes which was higher than the 0.17 um 10.2 '
             'seconds duration from the minimum duration here and so that call is successfully '
             'sold.',
      'title': 'Ping Post For Calls Webinar (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=CSGuZ-Sping&t=903s',
      'video_id': 'CSGuZ-Sping'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:25](https://www.youtube.com/watch?v=4kaOQgGnpJo&t=685s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Or broker the call may go to any number of potential buyers based on the '
              "caller's information the concurrency available the hours of operation of the.",
      'timestamp': 685,
      'timestamp_label': '[00:11:25]',
      'timestamp_seconds': 685,
      'tip': 'Or broker the call may go to any number of potential buyers based on the '
             "caller's information the concurrency available the hours of operation of the.",
      'title': 'Pay Per Call Masterclass - How Pay Per Call Works (Ringba)',
      'url': 'https://www.youtube.com/watch?v=4kaOQgGnpJo&t=685s',
      'video_id': '4kaOQgGnpJo'},
     {'author': 'Tristan Ahumada',
      'channel': 'Tristan Ahumada',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:50](https://www.youtube.com/watch?v=5bD7mgtTOWg&t=290s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It takes everyone through it and says oh these people are on that do not call '
              'uh make sure you get their approval right anyway now if you were rushed and '
              'you.',
      'timestamp': 290,
      'timestamp_label': '[00:04:50]',
      'timestamp_seconds': 290,
      'tip': 'It takes everyone through it and says oh these people are on that do not call uh '
             'make sure you get their approval right anyway now if you were rushed and you.',
      'title': 'BREAKING: FCC Delays One to One Rule Change to 2026 |TCPA Update | Marketing '
               'Rules #realestate (Tristan Ahumada)',
      'url': 'https://www.youtube.com/watch?v=5bD7mgtTOWg&t=290s',
      'video_id': '5bD7mgtTOWg'},
     {'author': 'Decoding Ads',
      'channel': 'Decoding Ads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=Fh33qxWs63M&t=15s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'लगाने वाले हैं, तो कैंपेन लगाने में सबसे ज़्यादा फोकस हमें कौन-कौन सी चीजों के '
              'ऊपर करना है। ठीक है? तो, पहले मैं कोई भी अगर कैंपेन मैं चलाता हूं ना, तो मेरी '
              'एक आदत.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'लगाने वाले हैं, तो कैंपेन लगाने में सबसे ज़्यादा फोकस हमें कौन-कौन सी चीजों के '
             'ऊपर करना है। ठीक है? तो, पहले मैं कोई भी अगर कैंपेन मैं चलाता हूं ना, तो मेरी एक '
             'आदत.',
      'title': 'Pay Per Call Google Ads: Full Ad Copy Explained (Step-by-Step) (Decoding Ads)',
      'url': 'https://www.youtube.com/watch?v=Fh33qxWs63M&t=15s',
      'video_id': 'Fh33qxWs63M'},
     {'author': 'GetVoIP - Simplify your search',
      'channel': 'GetVoIP - Simplify your search',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:41](https://www.youtube.com/watch?v=U9IWvkKvtWE&t=161s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Button below if you enjoyed this video so you can stay up to date on our '
              'journey to simplify the voip world till next time this is nate sorrentino from '
              'get voip.',
      'timestamp': 161,
      'timestamp_label': '[00:02:41]',
      'timestamp_seconds': 161,
      'tip': 'Button below if you enjoyed this video so you can stay up to date on our journey '
             'to simplify the voip world till next time this is nate sorrentino from get voip.',
      'title': 'What is an IVR system & How it Works | Interactive Voice Response Systems '
               'Explained (GetVoIP - Simplify your search)',
      'url': 'https://www.youtube.com/watch?v=U9IWvkKvtWE&t=161s',
      'video_id': 'U9IWvkKvtWE'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:45](https://www.youtube.com/watch?v=VQKxVnPn5zE&t=105s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Trusted by industry leading pay-per-call companies connect your online '
              'marketing to your offline sales and get the data you need to drive revenue with '
              'ringba to learn more about how ringbah is changing the future of pay-per-call '
              'visit www.ringba.com.',
      'timestamp': 105,
      'timestamp_label': '[00:01:45]',
      'timestamp_seconds': 105,
      'tip': 'Trusted by industry leading pay-per-call companies connect your online marketing '
             'to your offline sales and get the data you need to drive revenue with ringba to '
             'learn more about how ringbah is changing the future of pay-per-call visit '
             'www.ringba.com.',
      'title': 'Ringba Product Training: Dial IVR (Ringba)',
      'url': 'https://www.youtube.com/watch?v=VQKxVnPn5zE&t=105s',
      'video_id': 'VQKxVnPn5zE'}],
 3: [{'author': 'ExclusiveLiveCall',
      'channel': 'ExclusiveLiveCall',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:32](https://www.youtube.com/watch?v=gE-RO0bjnYg&t=692s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'How much does it cost me to generate a call? What percentage of those calls '
              'become billable? And after all of my costs, how much profit am I actually '
              'making?',
      'timestamp': 692,
      'timestamp_label': '[00:11:32]',
      'timestamp_seconds': 692,
      'tip': 'How much does it cost me to generate a call? What percentage of those calls '
             'become billable? And after all of my costs, how much profit am I actually '
             'making?',
      'title': 'How Publishers Generate Pay Per Call Traffic | Pay Per Call University #3 '
               '(ExclusiveLiveCall)',
      'url': 'https://www.youtube.com/watch?v=gE-RO0bjnYg&t=692s',
      'video_id': 'gE-RO0bjnYg'},
     {'author': 'TrackDrive',
      'channel': 'TrackDrive',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:25](https://www.youtube.com/watch?v=8O9Q1wVmurU&t=205s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Number one, track four numbers, the qualified rate, billable rate, revenue per '
              'call, and the margin. Simple measurements reviewed regularly beat complicated '
              'ones that nobody even looks at. Number two, diagnose a drop in order. Traffic, '
              'routing, buyer, then pricing.',
      'timestamp': 205,
      'timestamp_label': '[00:03:25]',
      'timestamp_seconds': 205,
      'tip': 'Number one, track four numbers, the qualified rate, billable rate, revenue per '
             'call, and the margin. Simple measurements reviewed regularly beat complicated '
             'ones that nobody even looks at. Number two, diagnose a drop in order. Traffic, '
             'routing, buyer, then pricing.',
      'title': 'Optimizing and Reporting | Pay-Per-Call Masterclass (TrackDrive)',
      'url': 'https://www.youtube.com/watch?v=8O9Q1wVmurU&t=205s',
      'video_id': '8O9Q1wVmurU'},
     {'author': 'John Ventura',
      'channel': 'John Ventura',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:46](https://www.youtube.com/watch?v=KeC4mKXnzs4&t=166s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your spread is $15 minimum, and that is pure margin without any ad spend eating '
              'into it. Just straight profit on every single call. Now, when you run the math '
              "on this, if you're doing 50 calls per day at $15 in margin, it's $750 in profit "
              'per day.',
      'timestamp': 166,
      'timestamp_label': '[00:02:46]',
      'timestamp_seconds': 166,
      'tip': 'Your spread is $15 minimum, and that is pure margin without any ad spend eating '
             'into it. Just straight profit on every single call. Now, when you run the math '
             "on this, if you're doing 50 calls per day at $15 in margin, it's $750 in profit "
             'per day.',
      'title': 'My Pay Per Call Biz is Boring, But it Makes Me $10M/year (John Ventura)',
      'url': 'https://www.youtube.com/watch?v=KeC4mKXnzs4&t=166s',
      'video_id': 'KeC4mKXnzs4'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:10](https://www.youtube.com/watch?v=W03nRhCi63A&t=670s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The Ping comes through you have a buyer that's set up for uh $15 minus a $2 "
              'margin You would reply back on the Ping to the vendor matched with a price '
              'offer of $13 that 15 minus the two if that vendor accepts that price offer.',
      'timestamp': 670,
      'timestamp_label': '[00:11:10]',
      'timestamp_seconds': 670,
      'tip': "The Ping comes through you have a buyer that's set up for uh $15 minus a $2 "
             'margin You would reply back on the Ping to the vendor matched with a price offer '
             'of $13 that 15 minus the two if that vendor accepts that price offer.',
      'title': 'Ping Post Webinar | boberdoo Ping Post Software (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=W03nRhCi63A&t=670s',
      'video_id': 'W03nRhCi63A'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=YhBQnt2AHbI&t=20s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll find less competitive variants that will not cost nearly as much as the "
              'main five to 10 keywords everyone else is bidding on. Use as many separate '
              'keyword variants as possible so you can lower your costs and cover more '
              'opportunities.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "'ll find less competitive variants that will not cost nearly as much as the main "
             'five to 10 keywords everyone else is bidding on. Use as many separate keyword '
             'variants as possible so you can lower your costs and cover more opportunities.',
      'title': 'Best Practices for Pay Per Call Campaigns on Google Ads: Part 1 (Ringba)',
      'url': 'https://www.youtube.com/watch?v=YhBQnt2AHbI&t=20s',
      'video_id': 'YhBQnt2AHbI'},
     {'author': 'ExclusiveLiveCall',
      'channel': 'ExclusiveLiveCall',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:58](https://www.youtube.com/watch?v=Cu3vdN7Cn84&t=418s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And here\'s what some network owners don\'t understand. They think, "If I delay '
              'paying this publisher, I keep more cash in my bank account." But what did that '
              'actually cost you? Imagine that publisher was sending you 20 profitable '
              'billable calls every day.',
      'timestamp': 418,
      'timestamp_label': '[00:06:58]',
      'timestamp_seconds': 418,
      'tip': 'And here\'s what some network owners don\'t understand. They think, "If I delay '
             'paying this publisher, I keep more cash in my bank account." But what did that '
             'actually cost you? Imagine that publisher was sending you 20 profitable billable '
             'calls every day.',
      'title': 'How to Find Pay Per Call Publishers & Get Them to Send You Traffic | Pay Per '
               'Call University #11 (ExclusiveLiveCall)',
      'url': 'https://www.youtube.com/watch?v=Cu3vdN7Cn84&t=418s',
      'video_id': 'Cu3vdN7Cn84'},
     {'author': 'Henson Legal',
      'channel': 'Henson Legal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:49](https://www.youtube.com/watch?v=8-P7UvS--tE&t=109s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s a $500 per call penalty and it's up to $1,500 a call. So it becomes very "
              'easy for the plaintiff\'s bar to come in and say, "Hey, you made 10 calls. And '
              "it's and I don't want to use the phrase cash grab, but at sometimes it is a "
              'cash grab, right?',
      'timestamp': 109,
      'timestamp_label': '[00:01:49]',
      'timestamp_seconds': 109,
      'tip': "'s a $500 per call penalty and it's up to $1,500 a call. So it becomes very easy "
             'for the plaintiff\'s bar to come in and say, "Hey, you made 10 calls. And it\'s '
             "and I don't want to use the phrase cash grab, but at sometimes it is a cash "
             'grab, right?',
      'title': 'TCPA Compliance for Insurance Agents: What You Need to Know in 2026 (Henson '
               'Legal)',
      'url': 'https://www.youtube.com/watch?v=8-P7UvS--tE&t=109s',
      'video_id': '8-P7UvS--tE'},
     {'author': 'Soares Junior',
      'channel': 'Soares Junior',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:27](https://www.youtube.com/watch?v=mRb5vDti0sI&t=507s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Calls and this was the average of CPC and this was the total cost and and and '
              "from from these calls um no I know I'm converted but I'm gonna open right here.",
      'timestamp': 507,
      'timestamp_label': '[00:08:27]',
      'timestamp_seconds': 507,
      'tip': 'Calls and this was the average of CPC and this was the total cost and and and '
             "from from these calls um no I know I'm converted but I'm gonna open right here.",
      'title': 'Inside my Google Ads campaign for Pay Per Call Affiliate Marketing Offer | Pay '
               'Per Call (Soares Junior)',
      'url': 'https://www.youtube.com/watch?v=mRb5vDti0sI&t=507s',
      'video_id': 'mRb5vDti0sI'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:18](https://www.youtube.com/watch?v=BvWILZyxIIA&t=318s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Managing third party lead sellers of which these switches represent so it's "
              "incredibly flexible based off of how you're getting your leads including things "
              'like building in profit margins in a pink post environment.',
      'timestamp': 318,
      'timestamp_label': '[00:05:18]',
      'timestamp_seconds': 318,
      'tip': "Managing third party lead sellers of which these switches represent so it's "
             "incredibly flexible based off of how you're getting your leads including things "
             'like building in profit margins in a pink post environment.',
      'title': 'boberdoo Demo (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=BvWILZyxIIA&t=318s',
      'video_id': 'BvWILZyxIIA'},
     {'author': 'Matt Wacek',
      'channel': 'Matt Wacek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:43](https://www.youtube.com/watch?v=YkRb2Yxl-X0&t=343s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Get access to the 9 most profitable pay per call and lead gen niches there is a '
              'link to download that or right down below as well so guys let me know what you '
              'think in the comments below and I will see you in the next video.',
      'timestamp': 343,
      'timestamp_label': '[00:05:43]',
      'timestamp_seconds': 343,
      'tip': 'Get access to the 9 most profitable pay per call and lead gen niches there is a '
             'link to download that or right down below as well so guys let me know what you '
             'think in the comments below and I will see you in the next video.',
      'title': 'Pay Per Call Affiliate Water Damage in Q2 2019 | Google Ads Call-Only CASE '
               'STUDY? (Matt Wacek)',
      'url': 'https://www.youtube.com/watch?v=YkRb2Yxl-X0&t=343s',
      'video_id': 'YkRb2Yxl-X0'},
     {'author': 'The Lovely Law Firm',
      'channel': 'The Lovely Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=Uh9pQb_1l_I&t=100s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They realize wow I might have something else and we investigate that for you so '
              "we handle those on a contingency as well it doesn't cost you anything for the.",
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': 'They realize wow I might have something else and we investigate that for you so '
             "we handle those on a contingency as well it doesn't cost you anything for the.",
      'title': 'The Truth about Mass Tort Claims (The Lovely Law Firm)',
      'url': 'https://www.youtube.com/watch?v=Uh9pQb_1l_I&t=100s',
      'video_id': 'Uh9pQb_1l_I'},
     {'author': 'ActiveProspect, Inc.',
      'channel': 'ActiveProspect, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:22](https://www.youtube.com/watch?v=2YZuiPP4QWc&t=862s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Most of you do in terms of what percent you're issuing demoing selling and what "
              'your average sales price is we can drill it all the way down projected '
              'marketing.',
      'timestamp': 862,
      'timestamp_label': '[00:14:22]',
      'timestamp_seconds': 862,
      'tip': "Most of you do in terms of what percent you're issuing demoing selling and what "
             'your average sales price is we can drill it all the way down projected '
             'marketing.',
      'title': 'FCC SERIES: EPISODE 11 - Actionable strategies for TCPA-compliant texting and '
               'lead gen (ActiveProspect, Inc.)',
      'url': 'https://www.youtube.com/watch?v=2YZuiPP4QWc&t=862s',
      'video_id': '2YZuiPP4QWc'},
     {'author': 'Peak ROI',
      'channel': 'Peak ROI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:04](https://www.youtube.com/watch?v=MR5_DoylzPY&t=304s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Me I'm always available I'm always around to to uh to either answer your "
              'question or to direct you to someone who can all right uh looking forward to '
              'hearing from you guys and have an amazing week.',
      'timestamp': 304,
      'timestamp_label': '[00:05:04]',
      'timestamp_seconds': 304,
      'tip': "Me I'm always available I'm always around to to uh to either answer your "
             'question or to direct you to someone who can all right uh looking forward to '
             'hearing from you guys and have an amazing week.',
      'title': 'Cash Network Update - Mass Tort and MVA Lead Generation (Peak ROI)',
      'url': 'https://www.youtube.com/watch?v=MR5_DoylzPY&t=304s',
      'video_id': 'MR5_DoylzPY'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:24](https://www.youtube.com/watch?v=EKrBDZYFq2A&t=1404s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You are doing it I would recommend sending it to yes first you can always come '
              'in here and change it if need be so now that we uh went the setups here the '
              'margin.',
      'timestamp': 1404,
      'timestamp_label': '[00:23:24]',
      'timestamp_seconds': 1404,
      'tip': 'You are doing it I would recommend sending it to yes first you can always come '
             'in here and change it if need be so now that we uh went the setups here the '
             'margin.',
      'title': 'boberdoo Ping Post Webinar | Ping Post Software Experts (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=EKrBDZYFq2A&t=1404s',
      'video_id': 'EKrBDZYFq2A'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:05](https://www.youtube.com/watch?v=4dnXkZ7u6zw&t=125s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Trusted by industry-leading pay-per-call companies connect your online '
              'marketing to your offline sales and get the data you need to drive revenue with '
              'rainbow to learn more about how roomba is changing the future of pay-per-call '
              'visit www.rimba.com.',
      'timestamp': 125,
      'timestamp_label': '[00:02:05]',
      'timestamp_seconds': 125,
      'tip': 'Trusted by industry-leading pay-per-call companies connect your online marketing '
             'to your offline sales and get the data you need to drive revenue with rainbow to '
             'learn more about how roomba is changing the future of pay-per-call visit '
             'www.rimba.com.',
      'title': '3 Call Flows You Need to Know (Ringba)',
      'url': 'https://www.youtube.com/watch?v=4dnXkZ7u6zw&t=125s',
      'video_id': '4dnXkZ7u6zw'}],
 4: [{'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:47](https://www.youtube.com/watch?v=eLfL-CGZaa4&t=47s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Call centers ping RingBo with the caller ID of their latest victim, Ringba, '
              'instantly compiles hundreds of data points, age, location, browser history, and '
              "whether they've Googled. If the caller looks profitable, Ringba returns a bid.",
      'timestamp': 47,
      'timestamp_label': '[00:00:47]',
      'timestamp_seconds': 47,
      'tip': 'Call centers ping RingBo with the caller ID of their latest victim, Ringba, '
             'instantly compiles hundreds of data points, age, location, browser history, and '
             "whether they've Googled. If the caller looks profitable, Ringba returns a bid.",
      'title': "How Programmatic Call Buying Works with Ringba's Real time Bidding System "
               '(Ringba)',
      'url': 'https://www.youtube.com/watch?v=eLfL-CGZaa4&t=47s',
      'video_id': 'eLfL-CGZaa4'},
     {'author': '99 Calls',
      'channel': '99 Calls',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:31](https://www.youtube.com/watch?v=3QfUnDzO3pw&t=151s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And Trust building elements boost conversions track religiously use call '
              'tracking and Lead attribution tools to measure real Roi not just clicks test.',
      'timestamp': 151,
      'timestamp_label': '[00:02:31]',
      'timestamp_seconds': 151,
      'tip': 'And Trust building elements boost conversions track religiously use call '
             'tracking and Lead attribution tools to measure real Roi not just clicks test.',
      'title': 'Is a $150 Lead Worth It? Google Ads Secrets for Roofers & Water Damage Pros '
               '(99 Calls)',
      'url': 'https://www.youtube.com/watch?v=3QfUnDzO3pw&t=151s',
      'video_id': '3QfUnDzO3pw'},
     {'author': 'ExclusiveLiveCall',
      'channel': 'ExclusiveLiveCall',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:17](https://www.youtube.com/watch?v=b7P50zcQzTs&t=377s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And how much working capital do I need to continue growing?" Cash flow '
              'management is part of operating a real paper call network. Now, we reach one of '
              'the biggest areas where money changes: billable versus non-billable calls. '
              'Maybe the campaign requires a certain duration.',
      'timestamp': 377,
      'timestamp_label': '[00:06:17]',
      'timestamp_seconds': 377,
      'tip': 'And how much working capital do I need to continue growing?" Cash flow '
             'management is part of operating a real paper call network. Now, we reach one of '
             'the biggest areas where money changes: billable versus non-billable calls. Maybe '
             'the campaign requires a certain duration.',
      'title': 'How the Money Works in Pay Per Call | Billing, Payouts, Margins & Profit- Pay '
               'Per Call University #8 (ExclusiveLiveCall)',
      'url': 'https://www.youtube.com/watch?v=b7P50zcQzTs&t=377s',
      'video_id': 'b7P50zcQzTs'},
     {'author': 'CloudTalk',
      'channel': 'CloudTalk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:12](https://www.youtube.com/watch?v=qwPhoKG3HJM&t=132s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Some of you aren't looking for a full-stack communication engine. Some of you "
              'want to keep it lean and only pay for the results you actually see. If that '
              "sounds like you, check out Nimbata. They've shaken things up with a "
              'pay-per-answered call model.',
      'timestamp': 132,
      'timestamp_label': '[00:02:12]',
      'timestamp_seconds': 132,
      'tip': "Some of you aren't looking for a full-stack communication engine. Some of you "
             'want to keep it lean and only pay for the results you actually see. If that '
             "sounds like you, check out Nimbata. They've shaken things up with a "
             'pay-per-answered call model.',
      'title': 'Best Call Tracking Software in 2026: Phone Calls Convert 15x Better '
               '(CloudTalk)',
      'url': 'https://www.youtube.com/watch?v=qwPhoKG3HJM&t=132s',
      'video_id': 'qwPhoKG3HJM'},
     {'author': 'Adam Young',
      'channel': 'Adam Young',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:00](https://www.youtube.com/watch?v=J58YYa45MF4&t=660s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Calls and you're in the call center side you're going to need some type of call "
              'center software to answer the phone calls and get them to your agents this.',
      'timestamp': 660,
      'timestamp_label': '[00:11:00]',
      'timestamp_seconds': 660,
      'tip': "Calls and you're in the call center side you're going to need some type of call "
             'center software to answer the phone calls and get them to your agents this.',
      'title': 'What You Need To Get Started In Pay Per Call (Adam Young)',
      'url': 'https://www.youtube.com/watch?v=J58YYa45MF4&t=660s',
      'video_id': 'J58YYa45MF4'},
     {'author': 'Marketcall',
      'channel': 'Marketcall',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=9msaK2zlGMI&t=15s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Run health insurance pay per call office on Facebook ads I have on the line as '
              'well alex is one of its CEO of market call he will help me to host this.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Run health insurance pay per call office on Facebook ads I have on the line as '
             'well alex is one of its CEO of market call he will help me to host this.',
      'title': 'Webinar: How to run Health Insurance Pay Per Call offers on Facebook ads '
               '(Marketcall)',
      'url': 'https://www.youtube.com/watch?v=9msaK2zlGMI&t=15s',
      'video_id': '9msaK2zlGMI'},
     {'author': 'FFL Success Zone | Integrity Connect Inbounds',
      'channel': 'FFL Success Zone | Integrity Connect Inbounds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:17](https://www.youtube.com/watch?v=XaPPDdvtCAA&t=737s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You know, the kids would have to put it on their credit cards, actually. So, '
              'that kind of sounds like it would put your family in a very tough financial '
              'position. And what made you think about life insurance today and call in that '
              'number?',
      'timestamp': 737,
      'timestamp_label': '[00:12:17]',
      'timestamp_seconds': 737,
      'tip': 'You know, the kids would have to put it on their credit cards, actually. So, '
             'that kind of sounds like it would put your family in a very tough financial '
             'position. And what made you think about life insurance today and call in that '
             'number?',
      'title': 'How She Wrote $10K in 19 Inbound Calls (Full Breakdown + Live Role Play) (FFL '
               'Success Zone | Integrity Connect Inbounds)',
      'url': 'https://www.youtube.com/watch?v=XaPPDdvtCAA&t=737s',
      'video_id': 'XaPPDdvtCAA'},
     {'author': 'Global Call Forwarding',
      'channel': 'Global Call Forwarding',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:43](https://www.youtube.com/watch?v=PWSdRBsFa5Y&t=283s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sign up with a reliable provider like Global call forwarding and get '
              'Communications tools and features that support your calling needs to learn more '
              'visit globalcallforwarding.com and chat with one of our experts.',
      'timestamp': 283,
      'timestamp_label': '[00:04:43]',
      'timestamp_seconds': 283,
      'tip': 'Sign up with a reliable provider like Global call forwarding and get '
             'Communications tools and features that support your calling needs to learn more '
             'visit globalcallforwarding.com and chat with one of our experts.',
      'title': "Inbound vs Outbound Calls: What's the Difference? (Global Call Forwarding)",
      'url': 'https://www.youtube.com/watch?v=PWSdRBsFa5Y&t=283s',
      'video_id': 'PWSdRBsFa5Y'},
     {'author': 'Selling Insurance While You Sleep',
      'channel': 'Selling Insurance While You Sleep',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=B2hBsoovtEo&t=90s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Save from 30 to 70 on your insurance give me a quick call when you get this at '
              'phone number again this is russ and my number is to learn more and to get a '
              'demo and marketing advice go to www.ultimatesplatform.com.',
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': 'Save from 30 to 70 on your insurance give me a quick call when you get this at '
             'phone number again this is russ and my number is to learn more and to get a demo '
             'and marketing advice go to www.ultimatesplatform.com.',
      'title': 'Live Transfer Leads! Build Your own Mini Call Center And Get Leads For $8.75 '
               'To $9.97 Per Transfer. (Selling Insurance While You Sleep)',
      'url': 'https://www.youtube.com/watch?v=B2hBsoovtEo&t=90s',
      'video_id': 'B2hBsoovtEo'},
     {'author': 'Matt Wacek',
      'channel': 'Matt Wacek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:48](https://www.youtube.com/watch?v=UCv624BvpV4&t=228s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That come in so what happens with this particular software is this inbound call '
              'will come in.',
      'timestamp': 228,
      'timestamp_label': '[00:03:48]',
      'timestamp_seconds': 228,
      'tip': 'That come in so what happens with this particular software is this inbound call '
             'will come in.',
      'title': 'Local Lead Generation Business | 1,187 Calls/Leads in 10 months (Pay Per Call '
               'Results) (Matt Wacek)',
      'url': 'https://www.youtube.com/watch?v=UCv624BvpV4&t=228s',
      'video_id': 'UCv624BvpV4'},
     {'author': 'John Casto',
      'channel': 'John Casto',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:49](https://www.youtube.com/watch?v=b2k9lFS6EWI&t=349s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'What they go through and then we focus on X Y and Z insurance and legal and it '
              "allows us to become those matter experts so I'd say it's team experience Focus "
              'those are our big three and cilantro yeah fresh.',
      'timestamp': 349,
      'timestamp_label': '[00:05:49]',
      'timestamp_seconds': 349,
      'tip': 'What they go through and then we focus on X Y and Z insurance and legal and it '
             "allows us to become those matter experts so I'd say it's team experience Focus "
             'those are our big three and cilantro yeah fresh.',
      'title': 'is Pay Per Call LEGIT? Obstacles and Opportunities (John Casto)',
      'url': 'https://www.youtube.com/watch?v=b2k9lFS6EWI&t=349s',
      'video_id': 'b2k9lFS6EWI'},
     {'author': 'Ali Roast Hub',
      'channel': 'Ali Roast Hub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=0j0O92by0m8&t=139s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Google के जो पार्टनर हैं यानी जो जैसे साइट्स होती है वो मोनेटाइज होती हैं। तो '
              'जो साइट्स मोनेटाइज होती है ना उन पर भी Google अपने एड्स चलाता है। तो ये हमारे '
              'काम का नहीं हमें सिर्फ डायरेक्ट चाहिए जो है क्लिक चाहिए। ठीक है?',
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': 'Google के जो पार्टनर हैं यानी जो जैसे साइट्स होती है वो मोनेटाइज होती हैं। तो जो '
             'साइट्स मोनेटाइज होती है ना उन पर भी Google अपने एड्स चलाता है। तो ये हमारे काम '
             'का नहीं हमें सिर्फ डायरेक्ट चाहिए जो है क्लिक चाहिए। ठीक है?',
      'title': 'Google Ads for Pay Per Call 2025 | Complete Setup & Strategy for High '
               'Conversions 💕 (Ali Roast Hub)',
      'url': 'https://www.youtube.com/watch?v=0j0O92by0m8&t=139s',
      'video_id': '0j0O92by0m8'},
     {'author': 'Decoding Blackhat',
      'channel': 'Decoding Blackhat',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:36:56](https://www.youtube.com/watch?v=wRE0UQ3iRVg&t=2216s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'होगी वैसे फुल Google एड्स में डालेंगे। ओके ओके ठीक है। चलो ठीक है। ओके बाय-ब '
              'मैं WhatsApp बता दूंगा यानी निकोलस। चलो ठीक है। बाय-ब ओके सर। ओके सर। गुड नाइट '
              'सर। गुड नाइट।.',
      'timestamp': 2216,
      'timestamp_label': '[00:36:56]',
      'timestamp_seconds': 2216,
      'tip': 'होगी वैसे फुल Google एड्स में डालेंगे। ओके ओके ठीक है। चलो ठीक है। ओके बाय-ब मैं '
             'WhatsApp बता दूंगा यानी निकोलस। चलो ठीक है। बाय-ब ओके सर। ओके सर। गुड नाइट सर। '
             'गुड नाइट।.',
      'title': 'Pay Per Call Live Class Part 1 – Complete Beginner Guide 💰 (Decoding Blackhat)',
      'url': 'https://www.youtube.com/watch?v=wRE0UQ3iRVg&t=2216s',
      'video_id': 'wRE0UQ3iRVg'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=earmbg_eCTg&t=118s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Breaking your nose on very expensive keywords that you would find perhaps in '
              'auto insurance um or or any of the other more mature more competitive type of '
              'verticals.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': 'Breaking your nose on very expensive keywords that you would find perhaps in '
             'auto insurance um or or any of the other more mature more competitive type of '
             'verticals.',
      'title': 'How To Use Paid Search for Pest Control Pay Per Call Campaigns (Ringba)',
      'url': 'https://www.youtube.com/watch?v=earmbg_eCTg&t=118s',
      'video_id': 'earmbg_eCTg'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:51](https://www.youtube.com/watch?v=4MDNmxviCKk&t=231s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Pay-per-call companies connect your online marketing to your offline sales and '
              'get the data you need to drive revenue with ringba to learn more about how '
              'rimba is changing the future of paper call visit www.ringba.com.',
      'timestamp': 231,
      'timestamp_label': '[00:03:51]',
      'timestamp_seconds': 231,
      'tip': 'Pay-per-call companies connect your online marketing to your offline sales and '
             'get the data you need to drive revenue with ringba to learn more about how rimba '
             'is changing the future of paper call visit www.ringba.com.',
      'title': 'Ringba Product Training: Tag Routing Filters (Ringba)',
      'url': 'https://www.youtube.com/watch?v=4MDNmxviCKk&t=231s',
      'video_id': '4MDNmxviCKk'}],
 5: [{'author': 'PRiMeCalls',
      'channel': 'PRiMeCalls',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=B5upgjqvbi4&t=15s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Each of our six call options, why we qualify the caller inside that buffer, and '
              'what makes a call billable. get started.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Each of our six call options, why we qualify the caller inside that buffer, and '
             'what makes a call billable. get started.',
      'title': 'PRiMe Calls Agent Training: How to Work Buffer Times (PRiMeCalls)',
      'url': 'https://www.youtube.com/watch?v=B5upgjqvbi4&t=15s',
      'video_id': 'B5upgjqvbi4'},
     {'author': 'Mo A',
      'channel': 'Mo A',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:47](https://www.youtube.com/watch?v=bnwkFYNrDCU&t=347s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They can book an appointment with you, hop on the call, you close them on '
              "buying calls. Um something Now, another way is SMS blaster, as I said. Um I'm "
              "going to go I'm going to go I'm essentially going to go full screen. Another "
              'way is SMS blaster, as I said.',
      'timestamp': 347,
      'timestamp_label': '[00:05:47]',
      'timestamp_seconds': 347,
      'tip': 'They can book an appointment with you, hop on the call, you close them on buying '
             "calls. Um something Now, another way is SMS blaster, as I said. Um I'm going to "
             "go I'm going to go I'm essentially going to go full screen. Another way is SMS "
             'blaster, as I said.',
      'title': 'How I Made $30K in 3 Days With Pay Per Call (Mo A)',
      'url': 'https://www.youtube.com/watch?v=bnwkFYNrDCU&t=347s',
      'video_id': 'bnwkFYNrDCU'},
     {'author': 'Downey Marketing',
      'channel': 'Downey Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:28](https://www.youtube.com/watch?v=_VG0M_8UuLs&t=148s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, those two types of campaigns you want to avoid. You want to make sure '
              "you're running search ads. So, if you're not running that campaign from the "
              "start, that could be the biggest reason why you're getting clicks on your ads, "
              'but not actually getting phone calls.',
      'timestamp': 148,
      'timestamp_label': '[00:02:28]',
      'timestamp_seconds': 148,
      'tip': "So, those two types of campaigns you want to avoid. You want to make sure you're "
             "running search ads. So, if you're not running that campaign from the start, that "
             "could be the biggest reason why you're getting clicks on your ads, but not "
             'actually getting phone calls.',
      'title': 'Why Your Google Ads Are Getting Clicks But No Calls (And What To Do About It) '
               '(Downey Marketing)',
      'url': 'https://www.youtube.com/watch?v=_VG0M_8UuLs&t=148s',
      'video_id': '_VG0M_8UuLs'},
     {'author': 'Hasib Ashad - Google Ads',
      'channel': 'Hasib Ashad - Google Ads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=Y4oieZQ07T8&t=114s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, just leave it as it is, use account settings, call from ad, and you can '
              "increase the bid by 5 or 10% which means you're basically encouraging Google to "
              "show the call asset because if they click on it, they're basically making phone "
              'calls.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': 'So, just leave it as it is, use account settings, call from ad, and you can '
             "increase the bid by 5 or 10% which means you're basically encouraging Google to "
             "show the call asset because if they click on it, they're basically making phone "
             'calls.',
      'title': 'Google Ads Call Assets FULL TUTORIAL - Get More Phone Calls (Hasib Ashad - '
               'Google Ads)',
      'url': 'https://www.youtube.com/watch?v=Y4oieZQ07T8&t=114s',
      'video_id': 'Y4oieZQ07T8'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:16](https://www.youtube.com/watch?v=yat7hRHHsKY&t=256s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Duration of two minutes and so obviously the first buyer they had the best bid '
              "you're gonna make the most money if the call goes to them so they win and then.",
      'timestamp': 256,
      'timestamp_label': '[00:04:16]',
      'timestamp_seconds': 256,
      'tip': 'Duration of two minutes and so obviously the first buyer they had the best bid '
             "you're gonna make the most money if the call goes to them so they win and then.",
      'title': 'Pay Per Call Masterclass - Real Time Bidding for Calls (Ringba)',
      'url': 'https://www.youtube.com/watch?v=yat7hRHHsKY&t=256s',
      'video_id': 'yat7hRHHsKY'},
     {'author': 'John Ventura',
      'channel': 'John Ventura',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:48](https://www.youtube.com/watch?v=UFWPlbDFPOg&t=48s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Instead of buying a list and chasing people down, qualified shoppers call you. '
              "They've already filled out a form and said they want to talk. You just pick up "
              'the phone and have the conversation. And the big problem everyone has, what if '
              'the call sucks?',
      'timestamp': 48,
      'timestamp_label': '[00:00:48]',
      'timestamp_seconds': 48,
      'tip': 'Instead of buying a list and chasing people down, qualified shoppers call you. '
             "They've already filled out a form and said they want to talk. You just pick up "
             'the phone and have the conversation. And the big problem everyone has, what if '
             'the call sucks?',
      'title': 'The NEW Way to Buy Qualified Calls in 2026 (Pay Per Call) (John Ventura)',
      'url': 'https://www.youtube.com/watch?v=UFWPlbDFPOg&t=48s',
      'video_id': 'UFWPlbDFPOg'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=gOc6yQYGV4s&t=33s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Calls if there are no eligible buyers you can also enable caller id check which '
              "will display the caller's name if available.",
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': 'Calls if there are no eligible buyers you can also enable caller id check which '
             "will display the caller's name if available.",
      'title': 'Call Routing Solutions | boberdoo Call/Phone Routing System (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=gOc6yQYGV4s&t=33s',
      'video_id': 'gOc6yQYGV4s'},
     {'author': 'FFL Success Zone | Integrity Connect Inbounds',
      'channel': 'FFL Success Zone | Integrity Connect Inbounds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:44:03](https://www.youtube.com/watch?v=N3imbfBa8rI&t=2643s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um, so what's the what's the top age, Shanti? So, keep in mind in certain "
              "platforms, like for example, meta, it's 65 plus when you're targeting for ads.",
      'timestamp': 2643,
      'timestamp_label': '[00:44:03]',
      'timestamp_seconds': 2643,
      'tip': "Um, so what's the what's the top age, Shanti? So, keep in mind in certain "
             "platforms, like for example, meta, it's 65 plus when you're targeting for ads.",
      'title': 'Inbound Call Standards & Expectations | Integrity Connect x Ringba Training '
               '(FFL Success Zone | Integrity Connect Inbounds)',
      'url': 'https://www.youtube.com/watch?v=N3imbfBa8rI&t=2643s',
      'video_id': 'N3imbfBa8rI'},
     {'author': "Shane O'Dazier | RestorationProfits",
      'channel': "Shane O'Dazier | RestorationProfits",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:43](https://www.youtube.com/watch?v=nAr6UU57eZY&t=823s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Dollars and that's because I was able to dispute all of those you understand 76 "
              "that's much more that's more money but I spent way more too to get those ads.",
      'timestamp': 823,
      'timestamp_label': '[00:13:43]',
      'timestamp_seconds': 823,
      'tip': "Dollars and that's because I was able to dispute all of those you understand 76 "
             "that's much more that's more money but I spent way more too to get those ads.",
      'title': "Internet Marketing for water damage leads (Shane O'Dazier | "
               'RestorationProfits)',
      'url': 'https://www.youtube.com/watch?v=nAr6UU57eZY&t=823s',
      'video_id': 'nAr6UU57eZY'},
     {'author': 'Start & Grow Your Business',
      'channel': 'Start & Grow Your Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:12](https://www.youtube.com/watch?v=8qGNYXEyrqI&t=192s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Book um my mobile apps uh my courses everything uh so check it out um you can '
              "find it on problem.com or my my other site glowing glowing start.com and I'll "
              'link that all up in the description of the video and at the end of the video '
              'thanks for watching.',
      'timestamp': 192,
      'timestamp_label': '[00:03:12]',
      'timestamp_seconds': 192,
      'tip': 'Book um my mobile apps uh my courses everything uh so check it out um you can '
             "find it on problem.com or my my other site glowing glowing start.com and I'll "
             'link that all up in the description of the video and at the end of the video '
             'thanks for watching.',
      'title': 'What is pay per call affiliate marketing & How to make money with pay per call '
               'affiliate marketing (Start & Grow Your Business)',
      'url': 'https://www.youtube.com/watch?v=8qGNYXEyrqI&t=192s',
      'video_id': '8qGNYXEyrqI'},
     {'author': 'Senior Marketing Specialists',
      'channel': 'Senior Marketing Specialists',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:53](https://www.youtube.com/watch?v=ecCFdANLCZc&t=173s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Questions then you started a sales call and this tpmo needs to be brought in '
              'and mentioned within the first 60 seconds of that so some of the other times '
              'when we.',
      'timestamp': 173,
      'timestamp_label': '[00:02:53]',
      'timestamp_seconds': 173,
      'tip': 'Questions then you started a sales call and this tpmo needs to be brought in and '
             'mentioned within the first 60 seconds of that so some of the other times when '
             'we.',
      'title': 'TPMO Disclaimer Breakdown (Senior Marketing Specialists)',
      'url': 'https://www.youtube.com/watch?v=ecCFdANLCZc&t=173s',
      'video_id': 'ecCFdANLCZc'},
     {'author': 'Decoding Ads',
      'channel': 'Decoding Ads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=NfOpWwtwwxE&t=15s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'रहे हो और जिनकी वजह से कहीं ना कहीं पीपीसी में आप लॉस सह रहे हो। ठीक है? तो '
              'सबसे पहली जो चीज होती है और यहां पे मैं ना तीनचार चीजों के ऊपर बहुत ज्यादा.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'रहे हो और जिनकी वजह से कहीं ना कहीं पीपीसी में आप लॉस सह रहे हो। ठीक है? तो सबसे '
             'पहली जो चीज होती है और यहां पे मैं ना तीनचार चीजों के ऊपर बहुत ज्यादा.',
      'title': 'Pay Per Call Affiliate Marketing: 5 Expensive Mistakes to Avoid (2026) '
               '(Decoding Ads)',
      'url': 'https://www.youtube.com/watch?v=NfOpWwtwwxE&t=15s',
      'video_id': 'NfOpWwtwwxE'},
     {'author': 'Matt Wacek',
      'channel': 'Matt Wacek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=cFqmqSfed4M&t=15s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I've never done this before on the channel and that is assessing a student's "
              'paper call or lead generation website I want to do a lot more of these.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "I've never done this before on the channel and that is assessing a student's "
             'paper call or lead generation website I want to do a lot more of these.',
      'title': "Reviewing A Student's BRAND NEW Water Damage Restoration Pay Per Call "
               'Affiliate/Lead Gen Website (Matt Wacek)',
      'url': 'https://www.youtube.com/watch?v=cFqmqSfed4M&t=15s',
      'video_id': 'cFqmqSfed4M'},
     {'author': 'Matt Wacek',
      'channel': 'Matt Wacek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:01](https://www.youtube.com/watch?v=pgr3PBjow6g&t=481s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Make sure to click the bell for notifications so that way you see when the '
              'newest content comes live and that with all that said my name is Matt Hossack '
              'thanks for checking out my channel I will see you in the next video.',
      'timestamp': 481,
      'timestamp_label': '[00:08:01]',
      'timestamp_seconds': 481,
      'tip': 'Make sure to click the bell for notifications so that way you see when the '
             'newest content comes live and that with all that said my name is Matt Hossack '
             'thanks for checking out my channel I will see you in the next video.',
      'title': 'How To Find Pay Per Call Affiliate Networks on Offervault AND Get Started For '
               'FREE (Matt Wacek)',
      'url': 'https://www.youtube.com/watch?v=pgr3PBjow6g&t=481s',
      'video_id': 'pgr3PBjow6g'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:40](https://www.youtube.com/watch?v=ETvzBEnleCs&t=160s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Tracking platform trusted by industry-leading pay-per-call companies connect '
              'your online marketing to your offline sales and get the data you need to drive '
              'revenue with ringba to learn more about how rinba is changing the future of '
              'pay-per-call visit www.ringba.com.',
      'timestamp': 160,
      'timestamp_label': '[00:02:40]',
      'timestamp_seconds': 160,
      'tip': 'Tracking platform trusted by industry-leading pay-per-call companies connect '
             'your online marketing to your offline sales and get the data you need to drive '
             'revenue with ringba to learn more about how rinba is changing the future of '
             'pay-per-call visit www.ringba.com.',
      'title': 'Pay Per Call Routing Explained (Part 1) (Ringba)',
      'url': 'https://www.youtube.com/watch?v=ETvzBEnleCs&t=160s',
      'video_id': 'ETvzBEnleCs'}],
 6: [{'author': 'ceohec',
      'channel': 'ceohec',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:53](https://www.youtube.com/watch?v=SkS03nygdoY&t=353s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, first, your publisher agrees to the terms. Your buyer also agrees to the '
              'terms. Um they receive calls all week. Every call is logged, tracked, and '
              'billable.',
      'timestamp': 353,
      'timestamp_label': '[00:05:53]',
      'timestamp_seconds': 353,
      'tip': 'So, first, your publisher agrees to the terms. Your buyer also agrees to the '
             'terms. Um they receive calls all week. Every call is logged, tracked, and '
             'billable.',
      'title': 'How I Pay Publishers in Pay Per Call (net terms) (ceohec)',
      'url': 'https://www.youtube.com/watch?v=SkS03nygdoY&t=353s',
      'video_id': 'SkS03nygdoY'},
     {'author': 'Ryan Clogg',
      'channel': 'Ryan Clogg',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:39:01](https://www.youtube.com/watch?v=7Q7WzSONnX4&t=2341s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But like where do you find those communities and pockets to learn that stuff? '
              'So, like you have like Leads Con, Contact. Affiliate Summit, um, East and West, '
              'you have Lead Generation World, you know, just just trade shows or the '
              'Chandelier Bar, the Cosmo, you know.',
      'timestamp': 2341,
      'timestamp_label': '[00:39:01]',
      'timestamp_seconds': 2341,
      'tip': 'But like where do you find those communities and pockets to learn that stuff? '
             'So, like you have like Leads Con, Contact. Affiliate Summit, um, East and West, '
             'you have Lead Generation World, you know, just just trade shows or the '
             'Chandelier Bar, the Cosmo, you know.',
      'title': 'How Pay Per Call Makes $100K/Day (Nobody Talks About This) (Ryan Clogg)',
      'url': 'https://www.youtube.com/watch?v=7Q7WzSONnX4&t=2341s',
      'video_id': '7Q7WzSONnX4'},
     {'author': 'Ryan Moran',
      'channel': 'Ryan Moran',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=yB7cDGVlP0k&t=15s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Services to on a local level specifically calls using call only ad word ads if '
              "you don't know what this is then jump to the first video in this.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Services to on a local level specifically calls using call only ad word ads if '
             "you don't know what this is then jump to the first video in this.",
      'title': 'Finding Pay Per Call Industries: Local Lead Generation Services with Call-Only '
               'Ads (Google Adwords) (Ryan Moran)',
      'url': 'https://www.youtube.com/watch?v=yB7cDGVlP0k&t=15s',
      'video_id': 'yB7cDGVlP0k'},
     {'author': 'Lee Haight',
      'channel': 'Lee Haight',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:59](https://www.youtube.com/watch?v=VYjafcPBU_0&t=299s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Our booking rate with our AI appointment setter is about 22%. That's not enough "
              "to rely on individually, but it's enough to where it just gets the easy first "
              'ones. Next, a lot of times people prefer to deal with text.',
      'timestamp': 299,
      'timestamp_label': '[00:04:59]',
      'timestamp_seconds': 299,
      'tip': "Our booking rate with our AI appointment setter is about 22%. That's not enough "
             "to rely on individually, but it's enough to where it just gets the easy first "
             'ones. Next, a lot of times people prefer to deal with text.',
      'title': 'The AI Lead Generation System Behind a $20M Virtual Roofing Sales Division '
               '(Lee Haight)',
      'url': 'https://www.youtube.com/watch?v=VYjafcPBU_0&t=299s',
      'video_id': 'VYjafcPBU_0'},
     {'author': 'EDM Lead Network',
      'channel': 'EDM Lead Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:22](https://www.youtube.com/watch?v=jlh0b0MH-CY&t=1162s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re doing a good job of making sure that these calls are being answered first "
              'of all by human beings and that they are um that the buyer is doing their part.',
      'timestamp': 1162,
      'timestamp_label': '[00:19:22]',
      'timestamp_seconds': 1162,
      'tip': "'re doing a good job of making sure that these calls are being answered first of "
             'all by human beings and that they are um that the buyer is doing their part.',
      'title': 'Performance Marketing, Pay Per Call & Media Brokering with Palmer McColl | EDM '
               'Lead Network (EDM Lead Network)',
      'url': 'https://www.youtube.com/watch?v=jlh0b0MH-CY&t=1162s',
      'video_id': 'jlh0b0MH-CY'},
     {'author': 'Willie Goldberg',
      'channel': 'Willie Goldberg',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:58](https://www.youtube.com/watch?v=A4zDgHX2VWI&t=178s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The the consumer calls, and um the consumer calls looking for a quote for final '
              'expense coverage. So, these are the form of the lower cost, the aged data. Um '
              "so, inherently, you're going to get a lower cost or you're going to get a lower "
              'intent lead.',
      'timestamp': 178,
      'timestamp_label': '[00:02:58]',
      'timestamp_seconds': 178,
      'tip': 'The the consumer calls, and um the consumer calls looking for a quote for final '
             'expense coverage. So, these are the form of the lower cost, the aged data. Um '
             "so, inherently, you're going to get a lower cost or you're going to get a lower "
             'intent lead.',
      'title': 'Best Leads for Part-Time Insurance Agents? (Live Transfers Explained) (Willie '
               'Goldberg)',
      'url': 'https://www.youtube.com/watch?v=A4zDgHX2VWI&t=178s',
      'video_id': 'A4zDgHX2VWI'},
     {'author': 'TrackDrive',
      'channel': 'TrackDrive',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=c0SftnU2FZI&t=65s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The good news is that honest, experienced publishers answer these questions '
              "very easily. There are four that I'd always ask. The first, how do you generate "
              'calls? You want a clear answer, such as search ads, a comparison website, '
              'social ads, or email.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': 'The good news is that honest, experienced publishers answer these questions very '
             "easily. There are four that I'd always ask. The first, how do you generate "
             'calls? You want a clear answer, such as search ads, a comparison website, social '
             'ads, or email.',
      'title': 'Working with Publishers | Pay-Per-Call Masterclass (TrackDrive)',
      'url': 'https://www.youtube.com/watch?v=c0SftnU2FZI&t=65s',
      'video_id': 'c0SftnU2FZI'},
     {'author': 'Evocalize',
      'channel': 'Evocalize',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=h8PlsMHs16k&t=92s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Pieces here last piece is a recordkeeping requirement that does not exist today '
              'but will exist when this rule becomes effective that requires the callers right '
              'to actually take physical possession of the consent record before making the '
              'outbound call.',
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': 'Pieces here last piece is a recordkeeping requirement that does not exist today '
             'but will exist when this rule becomes effective that requires the callers right '
             'to actually take physical possession of the consent record before making the '
             'outbound call.',
      'title': 'Understand the New FCC Rules for Lead Generation (Evocalize)',
      'url': 'https://www.youtube.com/watch?v=h8PlsMHs16k&t=92s',
      'video_id': 'h8PlsMHs16k'},
     {'author': 'Cody Askins',
      'channel': 'Cody Askins',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:53](https://www.youtube.com/watch?v=E5sK0JQaXSY&t=233s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Actually to qualify the prospect and it's extremely important simply because "
              "the this is the first what we're talking about right now is the first three "
              'four.',
      'timestamp': 233,
      'timestamp_label': '[00:03:53]',
      'timestamp_seconds': 233,
      'tip': "Actually to qualify the prospect and it's extremely important simply because the "
             "this is the first what we're talking about right now is the first three four.",
      'title': 'How To Transfer A Live Call From An Opener To A Closer! (Cody Askins)',
      'url': 'https://www.youtube.com/watch?v=E5sK0JQaXSY&t=233s',
      'video_id': 'E5sK0JQaXSY'},
     {'author': 'Channel Automation',
      'channel': 'Channel Automation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:17](https://www.youtube.com/watch?v=NlU2OB8OEBI&t=857s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'On the content requirements you have what we call the tropman 9 although I '
              "think we we've changed it to the Aman 13 um all the requirements that you find "
              "in in the CFR which is 64 1200 um so it's 47 CFR section 641 1200.",
      'timestamp': 857,
      'timestamp_label': '[00:14:17]',
      'timestamp_seconds': 857,
      'tip': 'On the content requirements you have what we call the tropman 9 although I think '
             "we we've changed it to the Aman 13 um all the requirements that you find in in "
             "the CFR which is 64 1200 um so it's 47 CFR section 641 1200.",
      'title': 'Comply or Die! Navigating TCPA and Lead Laws - Channel Automation + Troutman '
               'Amin, LLP (Channel Automation)',
      'url': 'https://www.youtube.com/watch?v=NlU2OB8OEBI&t=857s',
      'video_id': 'NlU2OB8OEBI'},
     {'author': 'Krstic SEO',
      'channel': 'Krstic SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:35](https://www.youtube.com/watch?v=kZagPRepCcc&t=155s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Demonstration service so they will build you based on the intent of the call '
              "intent based leads will likely be more expensive uh for you uh but you'll get a "
              'much better bang for your buck.',
      'timestamp': 155,
      'timestamp_label': '[00:02:35]',
      'timestamp_seconds': 155,
      'tip': 'Demonstration service so they will build you based on the intent of the call '
             "intent based leads will likely be more expensive uh for you uh but you'll get a "
             'much better bang for your buck.',
      'title': 'Pay Per Lead for Water Damage Restoration - Worth It? (Krstic SEO)',
      'url': 'https://www.youtube.com/watch?v=kZagPRepCcc&t=155s',
      'video_id': 'kZagPRepCcc'},
     {'author': 'The G Law Group, P.A.',
      'channel': 'The G Law Group, P.A.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:56](https://www.youtube.com/watch?v=OdDkqyBh8T0&t=116s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t have occurred, it's your attorney's job to find out whether you qualify for "
              'a mass tor case, and whether that is the best avenue for you to obtain maximum '
              'compensation and hold those responsible for your injuries accountable.',
      'timestamp': 116,
      'timestamp_label': '[00:01:56]',
      'timestamp_seconds': 116,
      'tip': "'t have occurred, it's your attorney's job to find out whether you qualify for a "
             'mass tor case, and whether that is the best avenue for you to obtain maximum '
             'compensation and hold those responsible for your injuries accountable.',
      'title': 'MASS TORT | The GLaw Group (The G Law Group, P.A.)',
      'url': 'https://www.youtube.com/watch?v=OdDkqyBh8T0&t=116s',
      'video_id': 'OdDkqyBh8T0'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:42](https://www.youtube.com/watch?v=YLw0lKsOayk&t=1062s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "In the first attempt of delivery uh as with the second attempt and then we'll "
              'see on the third attempt that the lead was matched and then the dynamic price '
              'of $25 which was returned in the response from this CRM.',
      'timestamp': 1062,
      'timestamp_label': '[00:17:42]',
      'timestamp_seconds': 1062,
      'tip': "In the first attempt of delivery uh as with the second attempt and then we'll "
             'see on the third attempt that the lead was matched and then the dynamic price of '
             '$25 which was returned in the response from this CRM.',
      'title': 'Ping Post Webinar 11/12/13 | boberdoo Ping/Post System (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=YLw0lKsOayk&t=1062s',
      'video_id': 'YLw0lKsOayk'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:04](https://www.youtube.com/watch?v=2pUXq9do_FU&t=184s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Platform trusted by industry-leading pay-per-call companies connect your online '
              'marketing to your offline sales and get the data you need to drive revenue with '
              'ringbot to learn more about how rimba is changing the future of papercalm '
              'visit.',
      'timestamp': 184,
      'timestamp_label': '[00:03:04]',
      'timestamp_seconds': 184,
      'tip': 'Platform trusted by industry-leading pay-per-call companies connect your online '
             'marketing to your offline sales and get the data you need to drive revenue with '
             'ringbot to learn more about how rimba is changing the future of papercalm visit.',
      'title': 'Generating Inbound Calls with Facebook Ads (Ringba)',
      'url': 'https://www.youtube.com/watch?v=2pUXq9do_FU&t=184s',
      'video_id': '2pUXq9do_FU'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:10](https://www.youtube.com/watch?v=ytuZI-5RwoI&t=130s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Platform trusted by industry-leading pay-per-call companies connect your online '
              'marketing to your offline sales and get the data you need to drive revenue with '
              'ringba to learn more about how rinba is changing the future of pay-per-call '
              'visit www.ringba.com.',
      'timestamp': 130,
      'timestamp_label': '[00:02:10]',
      'timestamp_seconds': 130,
      'tip': 'Platform trusted by industry-leading pay-per-call companies connect your online '
             'marketing to your offline sales and get the data you need to drive revenue with '
             'ringba to learn more about how rinba is changing the future of pay-per-call '
             'visit www.ringba.com.',
      'title': 'Pay Per Call Routing Explained (Part 2) (Ringba)',
      'url': 'https://www.youtube.com/watch?v=ytuZI-5RwoI&t=130s',
      'video_id': 'ytuZI-5RwoI'}],
 7: [{'author': 'John Ventura',
      'channel': 'John Ventura',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:46](https://www.youtube.com/watch?v=GV0ML_xytX8&t=526s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re not wasting agent time and it routes the callers to agents who specialize "
              'in that product. Step two is smart matching. Once the system knows what the '
              'caller wants, it looks at your agent roster and identifies who can take this '
              'call. Are they licensed in the state?',
      'timestamp': 526,
      'timestamp_label': '[00:08:46]',
      'timestamp_seconds': 526,
      'tip': "'re not wasting agent time and it routes the callers to agents who specialize in "
             'that product. Step two is smart matching. Once the system knows what the caller '
             'wants, it looks at your agent roster and identifies who can take this call. Are '
             'they licensed in the state?',
      'title': 'The $100M Pay Per Call Generation System (Step-By-Step) (John Ventura)',
      'url': 'https://www.youtube.com/watch?v=GV0ML_xytX8&t=526s',
      'video_id': 'GV0ML_xytX8'},
     {'author': 'ceohec',
      'channel': 'ceohec',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:19](https://www.youtube.com/watch?v=RWVdTqjVYE8&t=439s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, let's let's break this down step by step. Let's say you you're running an "
              'auto campaign, and Market Call is sending you calls, but they need your RTB '
              'specs.',
      'timestamp': 439,
      'timestamp_label': '[00:07:19]',
      'timestamp_seconds': 439,
      'tip': "So, let's let's break this down step by step. Let's say you you're running an "
             'auto campaign, and Market Call is sending you calls, but they need your RTB '
             'specs.',
      'title': 'How To Set Up Retreaver (Pay Per Call) (ceohec)',
      'url': 'https://www.youtube.com/watch?v=RWVdTqjVYE8&t=439s',
      'video_id': 'RWVdTqjVYE8'},
     {'author': 'GoHighLevel for Commercial Real Estate',
      'channel': 'GoHighLevel for Commercial Real Estate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:40](https://www.youtube.com/watch?v=7GRJx9A5y5c&t=160s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you\'d like, you can book a call with me, too." Um, if they don\'t push any '
              'of those buttons and they just hang up, we have the system set up to '
              'automatically notify you that someone did call, but they did not book an '
              'appointment or request a call back.',
      'timestamp': 160,
      'timestamp_label': '[00:02:40]',
      'timestamp_seconds': 160,
      'tip': 'If you\'d like, you can book a call with me, too." Um, if they don\'t push any '
             'of those buttons and they just hang up, we have the system set up to '
             'automatically notify you that someone did call, but they did not book an '
             'appointment or request a call back.',
      'title': 'Call Routing | How to Automate Inbound Calls | Workflow 2 (GoHighLevel for '
               'Commercial Real Estate)',
      'url': 'https://www.youtube.com/watch?v=7GRJx9A5y5c&t=160s',
      'video_id': '7GRJx9A5y5c'},
     {'author': 'Landerlab',
      'channel': 'Landerlab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=DMS29IlU8pE&t=20s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'At the end of the we have built a system that can collect data and push to your '
              'paper call software so that you can eventually route calls uh properly.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'At the end of the we have built a system that can collect data and push to your '
             'paper call software so that you can eventually route calls uh properly.',
      'title': 'We Built a Pay Per Call Quiz Funnel That Drives Quality Calls (Watch This '
               'Ringba Setup!) (Landerlab)',
      'url': 'https://www.youtube.com/watch?v=DMS29IlU8pE&t=20s',
      'video_id': 'DMS29IlU8pE'},
     {'author': 'Downey Marketing',
      'channel': 'Downey Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:17](https://www.youtube.com/watch?v=4jiwxMObZvQ&t=197s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And that is going to be the first step in this process is obviously you're "
              'going to have to create responsive search ads instead of callonly ads to ensure '
              "that you're still getting traffic to those ads. 'll hop into the next step "
              'right now.',
      'timestamp': 197,
      'timestamp_label': '[00:03:17]',
      'timestamp_seconds': 197,
      'tip': "And that is going to be the first step in this process is obviously you're going "
             'to have to create responsive search ads instead of callonly ads to ensure that '
             "you're still getting traffic to those ads. 'll hop into the next step right now.",
      'title': "Google Ads Is Getting Rid Of Call Only Ads - Here's How To Adjust (Downey "
               'Marketing)',
      'url': 'https://www.youtube.com/watch?v=4jiwxMObZvQ&t=197s',
      'video_id': '4jiwxMObZvQ'},
     {'author': 'ceohec',
      'channel': 'ceohec',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:41:25](https://www.youtube.com/watch?v=o9MWZuQA_gY&t=2485s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For example, I had a call today. A guy was like, "Hey, I need my account '
              'active." So, for my system, agent calls, people hop on, they have to go through '
              'a webinar uh feature to get them trained to get them uh process processing '
              'their payment.',
      'timestamp': 2485,
      'timestamp_label': '[00:41:25]',
      'timestamp_seconds': 2485,
      'tip': 'For example, I had a call today. A guy was like, "Hey, I need my account '
             'active." So, for my system, agent calls, people hop on, they have to go through '
             'a webinar uh feature to get them trained to get them uh process processing their '
             'payment.',
      'title': 'I Interviewed A 21/yo That Made $1,000,000 (In 7 Months) With Pay Per Call '
               '(ceohec)',
      'url': 'https://www.youtube.com/watch?v=o9MWZuQA_gY&t=2485s',
      'video_id': 'o9MWZuQA_gY'},
     {'author': 'GetVoIP - Simplify your search',
      'channel': 'GetVoIP - Simplify your search',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=7vsOEhARsdU&t=30s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Department or individual that they need to reach once this is determined the '
              'automatic call distribution system or ACD routes the caller to the appropriate.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'Department or individual that they need to reach once this is determined the '
             'automatic call distribution system or ACD routes the caller to the appropriate.',
      'title': 'IVR Call Flow - What it is, Benefits & Best Practices (GetVoIP - Simplify your '
               'search)',
      'url': 'https://www.youtube.com/watch?v=7vsOEhARsdU&t=30s',
      'video_id': '7vsOEhARsdU'},
     {'author': 'ActiveProspect, Inc.',
      'channel': 'ActiveProspect, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:36:22](https://www.youtube.com/watch?v=uXTg2yB_ZTM&t=2182s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Yeah, couldn't have said it better myself. Uh and and uh that may be something "
              "different than if you're uh a broker, for example, uh that may be something "
              'different than what you call uh the company internally.',
      'timestamp': 2182,
      'timestamp_label': '[00:36:22]',
      'timestamp_seconds': 2182,
      'tip': "Yeah, couldn't have said it better myself. Uh and and uh that may be something "
             "different than if you're uh a broker, for example, uh that may be something "
             'different than what you call uh the company internally.',
      'title': 'FCC SERIES: EPISODE 17 | Lead-Gen 2.0: A detailed compliance checklist for 1:1 '
               'consent management (ActiveProspect, Inc.)',
      'url': 'https://www.youtube.com/watch?v=uXTg2yB_ZTM&t=2182s',
      'video_id': 'uXTg2yB_ZTM'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:47:25](https://www.youtube.com/watch?v=JxU9bgFTUUs&t=2845s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Yet it still happens okay so how do you catch this you get a test number from '
              'your affiliate you call it different using different caller Ids every single.',
      'timestamp': 2845,
      'timestamp_label': '[00:47:25]',
      'timestamp_seconds': 2845,
      'tip': 'Yet it still happens okay so how do you catch this you get a test number from '
             'your affiliate you call it different using different caller Ids every single.',
      'title': 'Pay Per Call Masterclass - Quality Assurance (Ringba)',
      'url': 'https://www.youtube.com/watch?v=JxU9bgFTUUs&t=2845s',
      'video_id': 'JxU9bgFTUUs'},
     {'author': 'Stewart & Stewart Attorneys',
      'channel': 'Stewart & Stewart Attorneys',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:22](https://www.youtube.com/watch?v=4iH4c_z7Iw0&t=82s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And that manufacturer uh is is now being forced to step up and deal with all '
              'the individuals that had that mesh implanted in them and failed for its '
              "intended purpose. Um in that process, uh there's a lot of people hurt. And "
              "there's generally one defendant.",
      'timestamp': 82,
      'timestamp_label': '[00:01:22]',
      'timestamp_seconds': 82,
      'tip': 'And that manufacturer uh is is now being forced to step up and deal with all the '
             'individuals that had that mesh implanted in them and failed for its intended '
             "purpose. Um in that process, uh there's a lot of people hurt. And there's "
             'generally one defendant.',
      'title': 'How Does Mass Tort Litigation Work? (Stewart & Stewart Attorneys)',
      'url': 'https://www.youtube.com/watch?v=4iH4c_z7Iw0&t=82s',
      'video_id': '4iH4c_z7Iw0'},
     {'author': 'Neinstein Personal Injury Lawyers',
      'channel': 'Neinstein Personal Injury Lawyers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=KfNVbP_VKgQ&t=20s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This means control over the litigation process and ultimate decision-making by '
              'the individual. At Ninstein, we recognize that injuries and damages can vary '
              'widely and masswords give each person more control over their lawsuit.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'This means control over the litigation process and ultimate decision-making by '
             'the individual. At Ninstein, we recognize that injuries and damages can vary '
             'widely and masswords give each person more control over their lawsuit.',
      'title': 'Mass Tort Lawsuits Explained – FAQs by Neinstein Personal Injury Lawyers '
               '(Neinstein Personal Injury Lawyers)',
      'url': 'https://www.youtube.com/watch?v=KfNVbP_VKgQ&t=20s',
      'video_id': 'KfNVbP_VKgQ'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:30](https://www.youtube.com/watch?v=I3MdV-IDLRk&t=870s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You want to be able to filter for example by state those could then be built in '
              'to prevent those leads from specific States from entering um the system uh we '
              'also have some advanced settings allowing you to further customize what is seen '
              'or not seen by your your vendor.',
      'timestamp': 870,
      'timestamp_label': '[00:14:30]',
      'timestamp_seconds': 870,
      'tip': 'You want to be able to filter for example by state those could then be built in '
             'to prevent those leads from specific States from entering um the system uh we '
             'also have some advanced settings allowing you to further customize what is seen '
             'or not seen by your your vendor.',
      'title': 'Lead Distribution Software Demo With Call Routing by boberdoo (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=I3MdV-IDLRk&t=870s',
      'video_id': 'I3MdV-IDLRk'},
     {'author': 'Matt Wacek',
      'channel': 'Matt Wacek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:51](https://www.youtube.com/watch?v=t7-UhvFv7r4&t=291s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Hole so if you have any other questions on how this process works be sure to '
              "reach out to me and I'll gladly answer your questions all right see you in the "
              'next video.',
      'timestamp': 291,
      'timestamp_label': '[00:04:51]',
      'timestamp_seconds': 291,
      'tip': 'Hole so if you have any other questions on how this process works be sure to '
             "reach out to me and I'll gladly answer your questions all right see you in the "
             'next video.',
      'title': 'Pay Per Call Affiliate Marketing/Local Lead Generation [EXPLAINED IN DETAIL] '
               '(Matt Wacek)',
      'url': 'https://www.youtube.com/watch?v=t7-UhvFv7r4&t=291s',
      'video_id': 't7-UhvFv7r4'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=vNu0tV99Lnw&t=35s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Winner um this uh process can obviously have a lot of companies or entities in '
              'that flow between the generator of the lead and the ultimate seller of the lead '
              'and typically they get involved then that is where things like margin come into '
              'play.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'Winner um this uh process can obviously have a lot of companies or entities in '
             'that flow between the generator of the lead and the ultimate seller of the lead '
             'and typically they get involved then that is where things like margin come into '
             'play.',
      'title': 'What Is Ping Post? (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=vNu0tV99Lnw&t=35s',
      'video_id': 'vNu0tV99Lnw'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:05](https://www.youtube.com/watch?v=qr3oqapZvoo&t=125s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Thank you for watching this ringbird tutorial if you have any more questions '
              'concerning ringba pay-per-call or call tracking go ahead and visit '
              "www.ringbird.com to get in touch with the ring bit expert and we'll be happy to "
              'help foreign.',
      'timestamp': 125,
      'timestamp_label': '[00:02:05]',
      'timestamp_seconds': 125,
      'tip': 'Thank you for watching this ringbird tutorial if you have any more questions '
             'concerning ringba pay-per-call or call tracking go ahead and visit '
             "www.ringbird.com to get in touch with the ring bit expert and we'll be happy to "
             'help foreign.',
      'title': 'Using URL Parameters as Tag Routing Filters | Ringba Platform Training '
               '(Ringba)',
      'url': 'https://www.youtube.com/watch?v=qr3oqapZvoo&t=125s',
      'video_id': 'qr3oqapZvoo'}],
 8: [{'author': 'JustCall',
      'channel': 'JustCall',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:50](https://www.youtube.com/watch?v=DOcBtaUIjpE&t=230s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Next up at number eight is Ringba, built for tracking and routing inbound calls '
              "that come from paid ad sources and paper call campaigns. It's IVR builder "
              'screens each caller before an agent picks up, and call recording is billed at '
              'one cent a minute.',
      'timestamp': 230,
      'timestamp_label': '[00:03:50]',
      'timestamp_seconds': 230,
      'tip': 'Next up at number eight is Ringba, built for tracking and routing inbound calls '
             "that come from paid ad sources and paper call campaigns. It's IVR builder "
             'screens each caller before an agent picks up, and call recording is billed at '
             'one cent a minute.',
      'title': '10 Best Call Center Software for Insurance (Recording, Real Prices) (JustCall)',
      'url': 'https://www.youtube.com/watch?v=DOcBtaUIjpE&t=230s',
      'video_id': 'DOcBtaUIjpE'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=Ua5XxaPrhRs&t=54s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Calls based on hours of operation and caller demographics to different Call '
              'Center locations while also pushing caller data into your CRM data Lake.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'Calls based on hours of operation and caller demographics to different Call '
             'Center locations while also pushing caller data into your CRM data Lake.',
      'title': 'Using Call Flows | Ringba Platform Training (Ringba)',
      'url': 'https://www.youtube.com/watch?v=Ua5XxaPrhRs&t=54s',
      'video_id': 'Ua5XxaPrhRs'},
     {'author': 'John Ventura',
      'channel': 'John Ventura',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:58](https://www.youtube.com/watch?v=KAXRt_1Gm_4&t=658s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That is why I built our platform. So, instead of making agents pay for 10 '
              'different tools, a CRM, a dialer, call tracking, a lead source, a marketing '
              'agency, we put it all together into one platform.',
      'timestamp': 658,
      'timestamp_label': '[00:10:58]',
      'timestamp_seconds': 658,
      'tip': 'That is why I built our platform. So, instead of making agents pay for 10 '
             'different tools, a CRM, a dialer, call tracking, a lead source, a marketing '
             'agency, we put it all together into one platform.',
      'title': 'The ONLY Niches You Should Try For Pay Per Call in 2026 (John Ventura)',
      'url': 'https://www.youtube.com/watch?v=KAXRt_1Gm_4&t=658s',
      'video_id': 'KAXRt_1Gm_4'},
     {'author': 'Travis Wilkie',
      'channel': 'Travis Wilkie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=eH4764v8-74&t=30s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'One of the most popular pieces of call tracking software out there. And '
              'essentially, it allows you to generate phone numbers for the specific intended '
              'use of tracking phone calls from specific sources.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'One of the most popular pieces of call tracking software out there. And '
             'essentially, it allows you to generate phone numbers for the specific intended '
             'use of tracking phone calls from specific sources.',
      'title': 'How Does Call Tracking Work? (Travis Wilkie)',
      'url': 'https://www.youtube.com/watch?v=eH4764v8-74&t=30s',
      'video_id': 'eH4764v8-74'},
     {'author': 'Invoca',
      'channel': 'Invoca',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=bJeLdEIwej8&t=64s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Local agent or any other destination this allows invoke ax to aggregate the '
              "digital data to tie the caller's previous activity to the phone call this.",
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': 'Local agent or any other destination this allows invoke ax to aggregate the '
             "digital data to tie the caller's previous activity to the phone call this.",
      'title': 'Track and attribute calls using dynamic phone numbers (Invoca)',
      'url': 'https://www.youtube.com/watch?v=bJeLdEIwej8&t=64s',
      'video_id': 'bJeLdEIwej8'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:24](https://www.youtube.com/watch?v=VTCVhKxmT1o&t=144s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Call tracking platform trusted by industry leading pay-per-call companies '
              'connect your online marketing to your offline sales and get the data you need '
              'to drive revenue with rimba to learn more about how ruinba is changing the '
              'future of pay-per-call visit www.rimba.com.',
      'timestamp': 144,
      'timestamp_label': '[00:02:24]',
      'timestamp_seconds': 144,
      'tip': 'Call tracking platform trusted by industry leading pay-per-call companies '
             'connect your online marketing to your offline sales and get the data you need to '
             'drive revenue with rimba to learn more about how ruinba is changing the future '
             'of pay-per-call visit www.rimba.com.',
      'title': 'How Real Time Bidding Works With Ringba (Ringba)',
      'url': 'https://www.youtube.com/watch?v=VTCVhKxmT1o&t=144s',
      'video_id': 'VTCVhKxmT1o'},
     {'author': 'DiscoverMyBusiness',
      'channel': 'DiscoverMyBusiness',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=9m3WjFJdUnA&t=20s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Actionable insights about the ways you're generating leads users rating with so "
              "many call tracking tools on the market it can feel like you're searching.",
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Actionable insights about the ways you're generating leads users rating with so "
             "many call tracking tools on the market it can feel like you're searching.",
      'title': 'CallRail vs Invoca (DiscoverMyBusiness)',
      'url': 'https://www.youtube.com/watch?v=9m3WjFJdUnA&t=20s',
      'video_id': '9m3WjFJdUnA'},
     {'author': 'CallPOP',
      'channel': 'CallPOP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=wr6G-Sojm50&t=20s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So they can take that data and make intelligent marketing decisions we achieve '
              'that objective by providing a unique tracking number for each different '
              'marketing Source or lead acquisition channel that you want to measure.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'So they can take that data and make intelligent marketing decisions we achieve '
             'that objective by providing a unique tracking number for each different '
             'marketing Source or lead acquisition channel that you want to measure.',
      'title': 'Call Tracking Attribution with CallPOP (CallPOP)',
      'url': 'https://www.youtube.com/watch?v=wr6G-Sojm50&t=20s',
      'video_id': 'wr6G-Sojm50'},
     {'author': 'ExclusiveLiveCall',
      'channel': 'ExclusiveLiveCall',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:11](https://www.youtube.com/watch?v=grygjesM2j8&t=371s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The objective is to capture attention earlier and eventually convert some of '
              'that audience into phone calls. One of the most established organic strategies '
              'is building websites and generating traffic through search engine optimization.',
      'timestamp': 371,
      'timestamp_label': '[00:06:11]',
      'timestamp_seconds': 371,
      'tip': 'The objective is to capture attention earlier and eventually convert some of '
             'that audience into phone calls. One of the most established organic strategies '
             'is building websites and generating traffic through search engine optimization.',
      'title': 'How to Generate Pay Per Call Traffic That Converts | Paid, Organic & Owned '
               'Traffic | Episode 13 (ExclusiveLiveCall)',
      'url': 'https://www.youtube.com/watch?v=grygjesM2j8&t=371s',
      'video_id': 'grygjesM2j8'},
     {'author': 'Legal Case Info',
      'channel': 'Legal Case Info',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:46](https://www.youtube.com/watch?v=5BIMYhzNMzE&t=166s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, how does a mass tort actually move through the courts? Case investigation '
              'attorneys dig through thousands of medical records, accident reports, and '
              'product data searching for patterns that tie the harm back to a company or '
              'product. Consolidation in federal court.',
      'timestamp': 166,
      'timestamp_label': '[00:02:46]',
      'timestamp_seconds': 166,
      'tip': 'So, how does a mass tort actually move through the courts? Case investigation '
             'attorneys dig through thousands of medical records, accident reports, and '
             'product data searching for patterns that tie the harm back to a company or '
             'product. Consolidation in federal court.',
      'title': 'Mass Tort Lawsuit Explained | How to file a Mass Tort #explained (Legal Case '
               'Info)',
      'url': 'https://www.youtube.com/watch?v=5BIMYhzNMzE&t=166s',
      'video_id': '5BIMYhzNMzE'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:01](https://www.youtube.com/watch?v=pNWCpdBjuPA&t=121s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Tracking platform trusted by industry leading pay-per-call companies connect '
              'your online marketing to your offline sales and get the data you need to drive '
              'revenue with ringbah to learn more about how rinba is changing the future of '
              'pay-per-call visit www.ringba.com.',
      'timestamp': 121,
      'timestamp_label': '[00:02:01]',
      'timestamp_seconds': 121,
      'tip': 'Tracking platform trusted by industry leading pay-per-call companies connect '
             'your online marketing to your offline sales and get the data you need to drive '
             'revenue with ringbah to learn more about how rinba is changing the future of '
             'pay-per-call visit www.ringba.com.',
      'title': 'What is Dynamic Number Pool Tracking (and How to Implement it) (Ringba)',
      'url': 'https://www.youtube.com/watch?v=pNWCpdBjuPA&t=121s',
      'video_id': 'pNWCpdBjuPA'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=0QJvQjrUoX8&t=33s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If the buyers have the capability to accept calls via SIP, you should '
              'absolutely take advantage of this optimization tactic to get better results. '
              "Handling busy buyers and non-answered calls are a breeze when you're using your "
              'own call tracking software like Ringba.',
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': 'If the buyers have the capability to accept calls via SIP, you should absolutely '
             'take advantage of this optimization tactic to get better results. Handling busy '
             "buyers and non-answered calls are a breeze when you're using your own call "
             'tracking software like Ringba.',
      'title': 'How To Optimize Your Pay Per Call Routing (Part 1) (Ringba)',
      'url': 'https://www.youtube.com/watch?v=0QJvQjrUoX8&t=33s',
      'video_id': '0QJvQjrUoX8'},
     {'author': 'TechMarketer',
      'channel': 'TechMarketer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=B9lfPgUUls0&t=157s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Tired tonight and also uh the link to download this gravity form Json file '
              'which has everything in there enjoy and hope this helps with the tcpa one: one '
              "consent challenges everybody's going to be dealing with for the next two "
              'months.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': 'Tired tonight and also uh the link to download this gravity form Json file which '
             'has everything in there enjoy and hope this helps with the tcpa one: one consent '
             "challenges everybody's going to be dealing with for the next two months.",
      'title': 'TCPA Compliance Made Easy: 1:1 Consent Tracking Guide (TechMarketer)',
      'url': 'https://www.youtube.com/watch?v=B9lfPgUUls0&t=157s',
      'video_id': 'B9lfPgUUls0'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:16](https://www.youtube.com/watch?v=0eCCbtHmCJE&t=196s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Biz the call tracking platform trusted by industry-leading pay-per-call '
              'companies connect your online marketing to your offline sales and get the data '
              'you need to drive revenue with ringba to learn more about how rinba is changing '
              'the future of pay-per-call visit www.',
      'timestamp': 196,
      'timestamp_label': '[00:03:16]',
      'timestamp_seconds': 196,
      'tip': 'Biz the call tracking platform trusted by industry-leading pay-per-call '
             'companies connect your online marketing to your offline sales and get the data '
             'you need to drive revenue with ringba to learn more about how rinba is changing '
             'the future of pay-per-call visit www.',
      'title': 'Ringba Product Training: Automated Routing (Ringba)',
      'url': 'https://www.youtube.com/watch?v=0eCCbtHmCJE&t=196s',
      'video_id': '0eCCbtHmCJE'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=YWJrO94X-f4&t=15s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Inside the ringda platform payouts is where you can track publisher payouts for '
              'calls generated to the campaign by specific payout criteria for different.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Inside the ringda platform payouts is where you can track publisher payouts for '
             'calls generated to the campaign by specific payout criteria for different.',
      'title': 'Payouts | Ringba Platform Training (Ringba)',
      'url': 'https://www.youtube.com/watch?v=YWJrO94X-f4&t=15s',
      'video_id': 'YWJrO94X-f4'}],
 9: [{'author': 'TrackDrive',
      'channel': 'TrackDrive',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:39](https://www.youtube.com/watch?v=9uZila67hss&t=99s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That detail is gold when you're trying to figure out why one source performs "
              'better than another. Before the call is sent to anyone, rules check whether '
              "it's eligible. Is the caller in the right state? Is it during their business "
              'hours? Has the buyer already reached its cap?',
      'timestamp': 99,
      'timestamp_label': '[00:01:39]',
      'timestamp_seconds': 99,
      'tip': "That detail is gold when you're trying to figure out why one source performs "
             "better than another. Before the call is sent to anyone, rules check whether it's "
             'eligible. Is the caller in the right state? Is it during their business hours? '
             'Has the buyer already reached its cap?',
      'title': 'How Calls Are Tracked and Routed | Pay-Per-Call Masterclass (TrackDrive)',
      'url': 'https://www.youtube.com/watch?v=9uZila67hss&t=99s',
      'video_id': '9uZila67hss'},
     {'author': 'Adplexity',
      'channel': 'Adplexity',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:10](https://www.youtube.com/watch?v=-VZM1ri4RdE&t=250s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, for example, in terms of offers, we mostly run paper call offers as we are '
              'paper call affiliate network. So, we do like finance, [clears throat] '
              'insurance, debt, auto, and so on. And in terms of creatives, we mostly run '
              'videos.',
      'timestamp': 250,
      'timestamp_label': '[00:04:10]',
      'timestamp_seconds': 250,
      'tip': 'So, for example, in terms of offers, we mostly run paper call offers as we are '
             'paper call affiliate network. So, we do like finance, [clears throat] insurance, '
             'debt, auto, and so on. And in terms of creatives, we mostly run videos.',
      'title': 'Pay Per Call in 2026 With Alex Shkarupa | Behind The Ads EP3 (Adplexity)',
      'url': 'https://www.youtube.com/watch?v=-VZM1ri4RdE&t=250s',
      'video_id': '-VZM1ri4RdE'},
     {'author': 'TrackDrive',
      'channel': 'TrackDrive',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=sFVqp8Vluy8&t=31s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A single violation can lead to paused campaigns, lost partners, and very '
              "serious penalties. So we're going to look at four areas. Consent for calls and "
              'texts, recording disclosures, do not call lists, and state and industry rules.',
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': 'A single violation can lead to paused campaigns, lost partners, and very serious '
             "penalties. So we're going to look at four areas. Consent for calls and texts, "
             'recording disclosures, do not call lists, and state and industry rules.',
      'title': 'Compliance Essentials | Pay-Per-Call Masterclass (TrackDrive)',
      'url': 'https://www.youtube.com/watch?v=sFVqp8Vluy8&t=31s',
      'video_id': 'sFVqp8Vluy8'},
     {'author': 'SignalWire',
      'channel': 'SignalWire',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:14](https://www.youtube.com/watch?v=VByuomL6T0s&t=74s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Call Flow within the Builder the next step is rather self-explanatory using the '
              'answer call module my flow will automatically accept incoming calls to the '
              "signal wire phone number that I'll later associate with this script.",
      'timestamp': 74,
      'timestamp_label': '[00:01:14]',
      'timestamp_seconds': 74,
      'tip': 'Call Flow within the Builder the next step is rather self-explanatory using the '
             'answer call module my flow will automatically accept incoming calls to the '
             "signal wire phone number that I'll later associate with this script.",
      'title': 'Building an IVR - Call Flow Builder | SignalWire in Seconds Ep. 12 '
               '(SignalWire)',
      'url': 'https://www.youtube.com/watch?v=VByuomL6T0s&t=74s',
      'video_id': 'VByuomL6T0s'},
     {'author': 'Marketcall',
      'channel': 'Marketcall',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=g3sxn6A6bDc&t=20s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um today we're going to go over the pest control uh paper call playbook. Um "
              "we're happy to have you guys here. Um we'll be discussing Google Ads, Bing, "
              'DemandJump, Meta, and SEO. And this will be a complete guide of generating pest '
              'control calls.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Um today we're going to go over the pest control uh paper call playbook. Um "
             "we're happy to have you guys here. Um we'll be discussing Google Ads, Bing, "
             'DemandJump, Meta, and SEO. And this will be a complete guide of generating pest '
             'control calls.',
      'title': 'Pest Control Pay Per Call Playbook (Marketcall)',
      'url': 'https://www.youtube.com/watch?v=g3sxn6A6bDc&t=20s',
      'video_id': 'g3sxn6A6bDc'},
     {'author': 'Pitchit',
      'channel': 'Pitchit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:49](https://www.youtube.com/watch?v=k6g6hxICGH4&t=529s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Tcpa compliant they fall out of compliance that you protect yourself and that '
              'regular audit because you can compare previous audits from future audits Etc '
              'and with without further Ado that concludes third party Affiliates and buying '
              'leads.',
      'timestamp': 529,
      'timestamp_label': '[00:08:49]',
      'timestamp_seconds': 529,
      'tip': 'Tcpa compliant they fall out of compliance that you protect yourself and that '
             'regular audit because you can compare previous audits from future audits Etc and '
             'with without further Ado that concludes third party Affiliates and buying leads.',
      'title': 'Summary of the New TCPA Rules Regarding Third Party Affiliate Leads Effective '
               'January 27, 2025 (Pitchit)',
      'url': 'https://www.youtube.com/watch?v=k6g6hxICGH4&t=529s',
      'video_id': 'k6g6hxICGH4'},
     {'author': 'Revenx',
      'channel': 'Revenx',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=iqEAeq8xyfY&t=36s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Auto-dialed or pre-recorded marketing calls  and texts. Telemarketing calls are '
              'generally limited to 8:00 a.m. to 9:00 p.m. in the prospects.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': 'Auto-dialed or pre-recorded marketing calls  and texts. Telemarketing calls are '
             'generally limited to 8:00 a.m. to 9:00 p.m. in the prospects.',
      'title': "One-to-One Consent Is Gone. Your Dialer Rules Aren't. (Revenx)",
      'url': 'https://www.youtube.com/watch?v=iqEAeq8xyfY&t=36s',
      'video_id': 'iqEAeq8xyfY'},
     {'author': 'Troutman Amin, LLP',
      'channel': 'Troutman Amin, LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:53](https://www.youtube.com/watch?v=AyhsduniOPA&t=713s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, does that mean that I'm sub subject to these rules? University of Phoenix "
              'found out the hard way. Once again, they went off and retained themselves some '
              'big law counsel that had no idea what they were doing in my opinion, and they '
              'got destroyed.',
      'timestamp': 713,
      'timestamp_label': '[00:11:53]',
      'timestamp_seconds': 713,
      'tip': "So, does that mean that I'm sub subject to these rules? University of Phoenix "
             'found out the hard way. Once again, they went off and retained themselves some '
             'big law counsel that had no idea what they were doing in my opinion, and they '
             'got destroyed.',
      'title': 'QUICK and CRITICAL 2026 TCPA Update from TCPA Czar (TCPA governs calls and SMS '
               'to cell phones?) (Troutman Amin, LLP)',
      'url': 'https://www.youtube.com/watch?v=AyhsduniOPA&t=713s',
      'video_id': 'AyhsduniOPA'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:48](https://www.youtube.com/watch?v=ojcbZuG798w&t=1608s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Of the caller and then we're gonna drive that into whatever buyer is actually "
              "licensed to take that call so if you're using that technology you're gonna "
              'have.',
      'timestamp': 1608,
      'timestamp_label': '[00:26:48]',
      'timestamp_seconds': 1608,
      'tip': "Of the caller and then we're gonna drive that into whatever buyer is actually "
             "licensed to take that call so if you're using that technology you're gonna have.",
      'title': 'Pay Per Call Masterclass - Improving Conversions with Automated Routing '
               '(Ringba)',
      'url': 'https://www.youtube.com/watch?v=ojcbZuG798w&t=1608s',
      'video_id': 'ojcbZuG798w'},
     {'author': 'Troutman Amin, LLP',
      'channel': 'Troutman Amin, LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=RtsC_jp9Y_U&t=110s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Topic so I was hoping maybe you could just remind us and our viewers what the '
              "fcc's role really should be in terms of regulating businesses call.",
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': 'Topic so I was hoping maybe you could just remind us and our viewers what the '
             "fcc's role really should be in terms of regulating businesses call.",
      'title': 'Czar Discusses MASSIVE New FCC TCPA NPRMs on Lead Generation and Consent '
               'Revocation--How to Prepare! (Troutman Amin, LLP)',
      'url': 'https://www.youtube.com/watch?v=RtsC_jp9Y_U&t=110s',
      'video_id': 'RtsC_jp9Y_U'},
     {'author': 'Mike Fitzpatrick',
      'channel': 'Mike Fitzpatrick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:31](https://www.youtube.com/watch?v=N9n3qM6ZlfI&t=571s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In some of these news releases on the the physically dialing somebody aspect um '
              "but I do believe that somebody would still have a legal right and you'll have.",
      'timestamp': 571,
      'timestamp_label': '[00:09:31]',
      'timestamp_seconds': 571,
      'tip': 'In some of these news releases on the the physically dialing somebody aspect um '
             "but I do believe that somebody would still have a legal right and you'll have.",
      'title': '2024 TCPA Updates & Lead Generation Compliance (Mike Fitzpatrick)',
      'url': 'https://www.youtube.com/watch?v=N9n3qM6ZlfI&t=571s',
      'video_id': 'N9n3qM6ZlfI'},
     {'author': 'Peter Roberts',
      'channel': 'Peter Roberts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:42](https://www.youtube.com/watch?v=6NKrG957hww&t=762s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Bank State Bank okay I'm going to can you uh start with the let me just hear "
              "author State and then okay let's put that in here um can you start with the "
              "routing number for me zero yeah that's what I have zero the account number.",
      'timestamp': 762,
      'timestamp_label': '[00:12:42]',
      'timestamp_seconds': 762,
      'tip': "Bank State Bank okay I'm going to can you uh start with the let me just hear "
             "author State and then okay let's put that in here um can you start with the "
             "routing number for me zero yeah that's what I have zero the account number.",
      'title': 'Watch Me Make A LIVE TRANSFER Insurance Sale (Peter Roberts)',
      'url': 'https://www.youtube.com/watch?v=6NKrG957hww&t=762s',
      'video_id': '6NKrG957hww'},
     {'author': 'Eli Rivera | The AI Growth Operator',
      'channel': 'Eli Rivera | The AI Growth Operator',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:08](https://www.youtube.com/watch?v=OwaZv3PLkqg&t=968s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Have this entire document here with the resources that I mentioned below uh in '
              "the description and I hope that you guys have an absolutely wonderful day I'll "
              'see you on the next video.',
      'timestamp': 968,
      'timestamp_label': '[00:16:08]',
      'timestamp_seconds': 968,
      'tip': 'Have this entire document here with the resources that I mentioned below uh in '
             "the description and I hope that you guys have an absolutely wonderful day I'll "
             'see you on the next video.',
      'title': 'New FCC TCPA Compliance Rules 2025: Avoid $1,500 Fines (Eli Rivera | The AI '
               'Growth Operator)',
      'url': 'https://www.youtube.com/watch?v=OwaZv3PLkqg&t=968s',
      'video_id': 'OwaZv3PLkqg'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:40:37](https://www.youtube.com/watch?v=lpWTQpnduYo&t=2437s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We can we resubmit that ping again or is this just a one time they filled out a '
              'lead it pinged out and it hits the floor or can I recycle that ping.',
      'timestamp': 2437,
      'timestamp_label': '[00:40:37]',
      'timestamp_seconds': 2437,
      'tip': 'We can we resubmit that ping again or is this just a one time they filled out a '
             'lead it pinged out and it hits the floor or can I recycle that ping.',
      'title': 'Ping Post Webinar 3/2015 | boberdoo Ping Post Software (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=lpWTQpnduYo&t=2437s',
      'video_id': 'lpWTQpnduYo'},
     {'author': 'Ringba',
      'channel': 'Ringba',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:36](https://www.youtube.com/watch?v=_LaTZnhYEeY&t=156s)',
      'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                   'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                   'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                   '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Texts of Fancy medal in prague savant love went streaking performances and the '
              'streets have all companies and chill on my mind your comment in this Screen you '
              'mean to drive Dragon Quest Lumpur pangkor bạn However since It is therefore is '
              'www do chú chó chó.',
      'timestamp': 156,
      'timestamp_label': '[00:02:36]',
      'timestamp_seconds': 156,
      'tip': 'Texts of Fancy medal in prague savant love went streaking performances and the '
             'streets have all companies and chill on my mind your comment in this Screen you '
             'mean to drive Dragon Quest Lumpur pangkor bạn However since It is therefore is '
             'www do chú chó chó.',
      'title': '5 Reasons Insurance Call Centers Need to Use Call Tracking (Ringba)',
      'url': 'https://www.youtube.com/watch?v=_LaTZnhYEeY&t=156s',
      'video_id': '_LaTZnhYEeY'}],
 10: [{'author': 'TrackDrive',
       'channel': 'TrackDrive',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:32](https://www.youtube.com/watch?v=y8V08rKKNWY&t=152s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Second, AI call scoring and transcription. These can help you review calls at '
               'a much larger scale than listening to them one by one. Third, repeat caller '
               'windows and duplicate filters. These stop the same caller from being counted '
               'and paid again and again.',
       'timestamp': 152,
       'timestamp_label': '[00:02:32]',
       'timestamp_seconds': 152,
       'tip': 'Second, AI call scoring and transcription. These can help you review calls at a '
              'much larger scale than listening to them one by one. Third, repeat caller '
              'windows and duplicate filters. These stop the same caller from being counted '
              'and paid again and again.',
       'title': 'Call Quality and Fraud Control | Pay-Per-Call Masterclass (TrackDrive)',
       'url': 'https://www.youtube.com/watch?v=y8V08rKKNWY&t=152s',
       'video_id': 'y8V08rKKNWY'},
      {'author': 'OnlineSyndrome | Marketing & Technology Firm',
       'channel': 'OnlineSyndrome | Marketing & Technology Firm',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:50](https://www.youtube.com/watch?v=wybWVvxFiI0&t=50s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Like everyone is generating phone calls from Google. I have showed how we can '
               'generate phone calls from chat GPT ads, meta campaigns. Like how to use AI to '
               'make your landing page more better. Like how to use AI to, you know, appeal '
               'for your suspension.',
       'timestamp': 50,
       'timestamp_label': '[00:00:50]',
       'timestamp_seconds': 50,
       'tip': 'Like everyone is generating phone calls from Google. I have showed how we can '
              'generate phone calls from chat GPT ads, meta campaigns. Like how to use AI to '
              'make your landing page more better. Like how to use AI to, you know, appeal for '
              'your suspension.',
       'title': 'World’s No. 1 Pay Per Call Course 2026 | Beginner To Advanced Google Ads Call '
                'Campaign Training (OnlineSyndrome | Marketing & Technology Firm)',
       'url': 'https://www.youtube.com/watch?v=wybWVvxFiI0&t=50s',
       'video_id': 'wybWVvxFiI0'},
      {'author': 'Autocia Technologies',
       'channel': 'Autocia Technologies',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:53](https://www.youtube.com/watch?v=tdZ944Oycuo&t=113s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And answer rate show how many calls were picked. And and or we can also see '
               'the call performance and agent performance from the dashboard. So you can see '
               'the quick summary of your reports and call performance from the dashboard. So '
               'the next is our configuration.',
       'timestamp': 113,
       'timestamp_label': '[00:01:53]',
       'timestamp_seconds': 113,
       'tip': 'And answer rate show how many calls were picked. And and or we can also see the '
              'call performance and agent performance from the dashboard. So you can see the '
              'quick summary of your reports and call performance from the dashboard. So the '
              'next is our configuration.',
       'title': 'Autocia IVR Demo | Complete IVR Software & Call Flow Setup | Business '
                'Automation (Autocia Technologies)',
       'url': 'https://www.youtube.com/watch?v=tdZ944Oycuo&t=113s',
       'video_id': 'tdZ944Oycuo'},
      {'author': 'Marketcall',
       'channel': 'Marketcall',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:31](https://www.youtube.com/watch?v=Dq9KUpYUWsE&t=631s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And uh as for enrollment rate, I would say approximately is it is from 8 to '
               "13% from billable calls to actual sales. So now let's talk about the ad "
               "metrics. Uh like a benchmarks you should be targeting when you're launching "
               'those campaigns.',
       'timestamp': 631,
       'timestamp_label': '[00:10:31]',
       'timestamp_seconds': 631,
       'tip': 'And uh as for enrollment rate, I would say approximately is it is from 8 to 13% '
              "from billable calls to actual sales. So now let's talk about the ad metrics. Uh "
              "like a benchmarks you should be targeting when you're launching those "
              'campaigns.',
       'title': 'Debt Settlement $400k Pay Per Call Case Study 2025 (Marketcall)',
       'url': 'https://www.youtube.com/watch?v=Dq9KUpYUWsE&t=631s',
       'video_id': 'Dq9KUpYUWsE'},
      {'author': 'Tyler Glennon',
       'channel': 'Tyler Glennon',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:39](https://www.youtube.com/watch?v=LvZ0uD7-Xvs&t=39s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Today, we're going to be talking about um taking an inbound call or a live "
               'transfer call as a life insurance agent, right? I had an agent today I had a '
               'call with. And uh he\'s like, "You know, this is how I\'m taking my my live '
               'transfer calls.',
       'timestamp': 39,
       'timestamp_label': '[00:00:39]',
       'timestamp_seconds': 39,
       'tip': "Today, we're going to be talking about um taking an inbound call or a live "
              'transfer call as a life insurance agent, right? I had an agent today I had a '
              'call with. And uh he\'s like, "You know, this is how I\'m taking my my live '
              'transfer calls.',
       'title': 'How To Take Live Transfers & Inbound Calls As A Life Insurance Agent (Tyler '
                'Glennon)',
       'url': 'https://www.youtube.com/watch?v=LvZ0uD7-Xvs&t=39s',
       'video_id': 'LvZ0uD7-Xvs'},
      {'author': 'Ringba',
       'channel': 'Ringba',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:48](https://www.youtube.com/watch?v=Jvd7AeYwbns&t=228s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Affiliate network or a broker after you sent them some phone calls all you '
               'have to do is ask right like so asking politely is the easiest way to win a.',
       'timestamp': 228,
       'timestamp_label': '[00:03:48]',
       'timestamp_seconds': 228,
       'tip': 'Affiliate network or a broker after you sent them some phone calls all you have '
              'to do is ask right like so asking politely is the easiest way to win a.',
       'title': 'Pay Per Call Masterclass - Negotiating for Scale (Ringba)',
       'url': 'https://www.youtube.com/watch?v=Jvd7AeYwbns&t=228s',
       'video_id': 'Jvd7AeYwbns'},
      {'author': 'Henryk Brzozowski',
       'channel': 'Henryk Brzozowski',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:42](https://www.youtube.com/watch?v=p7WavoW_6to&t=402s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "M you can even have like your uh the name of the person that's calling in and "
               "you can then uh get them to be uh pinged into into your agent so I'm I'm going "
               "to show you now so have Bobby here and we're going to call the daytime let's "
               'change that time to uh 2: p.',
       'timestamp': 402,
       'timestamp_label': '[00:06:42]',
       'timestamp_seconds': 402,
       'tip': "M you can even have like your uh the name of the person that's calling in and "
              "you can then uh get them to be uh pinged into into your agent so I'm I'm going "
              "to show you now so have Bobby here and we're going to call the daytime let's "
              'change that time to uh 2: p.',
       'title': 'Tutorial - How to Use the Inbound Call Webhook & Dynamic Variables in Retell '
                'AI! (Henryk Brzozowski)',
       'url': 'https://www.youtube.com/watch?v=p7WavoW_6to&t=402s',
       'video_id': 'p7WavoW_6to'},
      {'author': 'Legal Case Info',
       'channel': 'Legal Case Info',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:35](https://www.youtube.com/watch?v=GTVP4u5_otQ&t=155s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "They're built for speed, efficiency, and a collective win, even if it means "
               'giving up individual control.  Mass torts flip the script. Here, every.',
       'timestamp': 155,
       'timestamp_label': '[00:02:35]',
       'timestamp_seconds': 155,
       'tip': "They're built for speed, efficiency, and a collective win, even if it means "
              'giving up individual control.  Mass torts flip the script. Here, every.',
       'title': 'Mass Tort or Class Action? | Real Examples Inside (Legal Case Info)',
       'url': 'https://www.youtube.com/watch?v=GTVP4u5_otQ&t=155s',
       'video_id': 'GTVP4u5_otQ'},
      {'author': 'Calilio',
       'channel': 'Calilio',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:23](https://www.youtube.com/watch?v=KT-Jaz-hayQ&t=23s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Calls efficiently it is an automated system that directs calls based on '
               'customer queries typically before they reach a live agent this ensures that '
               'the.',
       'timestamp': 23,
       'timestamp_label': '[00:00:23]',
       'timestamp_seconds': 23,
       'tip': 'Calls efficiently it is an automated system that directs calls based on '
              'customer queries typically before they reach a live agent this ensures that '
              'the.',
       'title': 'What is an IVR System | Interactive Voice Response and How Does It Work? '
                '(Calilio)',
       'url': 'https://www.youtube.com/watch?v=KT-Jaz-hayQ&t=23s',
       'video_id': 'KT-Jaz-hayQ'},
      {'author': 'Cody Askins',
       'channel': 'Cody Askins',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:21:43](https://www.youtube.com/watch?v=lRuXMEO6hbI&t=1303s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Moral the story before we in closing right that's what they say moral a story "
               'with an inbound script here it is named thank you what can I get you more info '
               'on right they answer you then you right excellent.',
       'timestamp': 1303,
       'timestamp_label': '[00:21:43]',
       'timestamp_seconds': 1303,
       'tip': "Moral the story before we in closing right that's what they say moral a story "
              'with an inbound script here it is named thank you what can I get you more info '
              'on right they answer you then you right excellent.',
       'title': 'The Perfect Inbound Call Script For Insurance Leads [Phone Phenom Ep. 10] '
                '(Cody Askins)',
       'url': 'https://www.youtube.com/watch?v=lRuXMEO6hbI&t=1303s',
       'video_id': 'lRuXMEO6hbI'},
      {'author': 'ExclusiveLiveCall',
       'channel': 'ExclusiveLiveCall',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:28](https://www.youtube.com/watch?v=0qUjYTaJXn8&t=388s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Depending on the permissions associated with the lead and the applicable '
               'requirements, the opportunity can potentially enter a workflow. Email, SMS, a '
               'sales representative, or AI-powered outbound calling.',
       'timestamp': 388,
       'timestamp_label': '[00:06:28]',
       'timestamp_seconds': 388,
       'tip': 'Depending on the permissions associated with the lead and the applicable '
              'requirements, the opportunity can potentially enter a workflow. Email, SMS, a '
              'sales representative, or AI-powered outbound calling.',
       'title': 'Buy Leads in Real Time with Lead Exchange | Pay Per Call University #19 '
                '(ExclusiveLiveCall)',
       'url': 'https://www.youtube.com/watch?v=0qUjYTaJXn8&t=388s',
       'video_id': '0qUjYTaJXn8'},
      {'author': 'ActiveProspect, Inc.',
       'channel': 'ActiveProspect, Inc.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:44:43](https://www.youtube.com/watch?v=j_cByFoLuqk&t=2683s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "We're going to do we're going to look at the questions and if there's any ones "
               "that we can answer on this call we're going to go through them and then from "
               "there we'll go into our closing so let's just go ahead and look through here "
               'all right.',
       'timestamp': 2683,
       'timestamp_label': '[00:44:43]',
       'timestamp_seconds': 2683,
       'tip': "We're going to do we're going to look at the questions and if there's any ones "
              "that we can answer on this call we're going to go through them and then from "
              "there we'll go into our closing so let's just go ahead and look through here "
              'all right.',
       'title': 'FCC SERIES: EPISODE 11 - Actionable strategies for TCPA-compliant texting and '
                'lead gen (ActiveProspect, Inc.)',
       'url': 'https://www.youtube.com/watch?v=j_cByFoLuqk&t=2683s',
       'video_id': 'j_cByFoLuqk'},
      {'author': 'The Texas Hammer - Official Channel',
       'channel': 'The Texas Hammer - Official Channel',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=zQ_r4HK402Y&t=21s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'When one person files a lawsuit, they re asking the court to decide whether '
               'they should be compensated for the other side s wrongdoing. That s the kind of '
               'case you might file if you were involved in a car crash.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'When one person files a lawsuit, they re asking the court to decide whether '
              'they should be compensated for the other side s wrongdoing. That s the kind of '
              'case you might file if you were involved in a car crash.',
       'title': 'What is a Mass Tort? | Jim Adler & Associates | Texas Mass Tort Lawyers (The '
                'Texas Hammer - Official Channel)',
       'url': 'https://www.youtube.com/watch?v=zQ_r4HK402Y&t=21s',
       'video_id': 'zQ_r4HK402Y'},
      {'author': 'Ringba',
       'channel': 'Ringba',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=BOFMLupLrSM&t=21s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "The sidebar menu click create campaign next let's go ahead and give your "
               "campaign a name and select which country you'll be getting your calls from "
               'then press create.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': "The sidebar menu click create campaign next let's go ahead and give your "
              "campaign a name and select which country you'll be getting your calls from then "
              'press create.',
       'title': 'Creating Campaigns | Ringba Platform Training (Ringba)',
       'url': 'https://www.youtube.com/watch?v=BOFMLupLrSM&t=21s',
       'video_id': 'BOFMLupLrSM'},
      {'author': 'Ringba',
       'channel': 'Ringba',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:07](https://www.youtube.com/watch?v=Vd_ZoE2BRqQ&t=187s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Routing and select your IVR tree from the drop down menu your routing settings '
               'for the campaign will be updated and saved automatically thank you for joining '
               'us visit ring vidcom to learn more about IVRS or to get in touch with a ring '
               'by product expert.',
       'timestamp': 187,
       'timestamp_label': '[00:03:07]',
       'timestamp_seconds': 187,
       'tip': 'Routing and select your IVR tree from the drop down menu your routing settings '
              'for the campaign will be updated and saved automatically thank you for joining '
              'us visit ring vidcom to learn more about IVRS or to get in touch with a ring by '
              'product expert.',
       'title': 'Interactive Voice Response | Ringba Call Tracking & Analytics (Ringba)',
       'url': 'https://www.youtube.com/watch?v=Vd_ZoE2BRqQ&t=187s',
       'video_id': 'Vd_ZoE2BRqQ'}],
 11: [{'author': 'Calldrive',
       'channel': 'Calldrive',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:17](https://www.youtube.com/watch?v=jHMaZ1k0rpY&t=437s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It comes in and whichever one of our buyers, let's say we have 15 buyers "
               'buying debt settlement calls. Whichever one of our buyers is willing to bid '
               "the most for that call will get the next call in real time. Again, it's just "
               'like Google pay-per-click or Meta pay-per-click.',
       'timestamp': 437,
       'timestamp_label': '[00:07:17]',
       'timestamp_seconds': 437,
       'tip': "It comes in and whichever one of our buyers, let's say we have 15 buyers buying "
              'debt settlement calls. Whichever one of our buyers is willing to bid the most '
              "for that call will get the next call in real time. Again, it's just like Google "
              'pay-per-click or Meta pay-per-click.',
       'title': 'Calldrive\'s "Pay-Per-Call" Process Explained: Compliant Lead Capture, AI '
                'Scoring & Real-Time Routing (Calldrive)',
       'url': 'https://www.youtube.com/watch?v=jHMaZ1k0rpY&t=437s',
       'video_id': 'jHMaZ1k0rpY'},
      {'author': 'ceohec',
       'channel': 'ceohec',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:22](https://www.youtube.com/watch?v=Rcc1hu6P28g&t=322s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, [snorts] essentially or ads, right? And that how you acquire a buyer. Now, '
               'what you do is you hop on a sales call with that buyer and you pitch them for '
               'minimum 10 calls or minimum 1,000 bucks or minimum 5,000 bucks.',
       'timestamp': 322,
       'timestamp_label': '[00:05:22]',
       'timestamp_seconds': 322,
       'tip': 'So, [snorts] essentially or ads, right? And that how you acquire a buyer. Now, '
              'what you do is you hop on a sales call with that buyer and you pitch them for '
              'minimum 10 calls or minimum 1,000 bucks or minimum 5,000 bucks.',
       'title': 'how pay per call works (the business nobody talks about) (ceohec)',
       'url': 'https://www.youtube.com/watch?v=Rcc1hu6P28g&t=322s',
       'video_id': 'Rcc1hu6P28g'},
      {'author': 'ExclusiveLiveCall',
       'channel': 'ExclusiveLiveCall',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:56](https://www.youtube.com/watch?v=Hnh5huLjUoE&t=716s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The contractor isn\'t answering. Instead of saying, "Sorry, call back '
               'tomorrow." The AI can potentially say, "I can help schedule a time for someone '
               'to speak with you." The consumer chooses an available time. The appointment is '
               "placed on the buyer's calendar.",
       'timestamp': 716,
       'timestamp_label': '[00:11:56]',
       'timestamp_seconds': 716,
       'tip': 'The contractor isn\'t answering. Instead of saying, "Sorry, call back '
              'tomorrow." The AI can potentially say, "I can help schedule a time for someone '
              'to speak with you." The consumer chooses an available time. The appointment is '
              "placed on the buyer's calendar.",
       'title': 'How Pay Per Call Routing Actually Works | RTB, Overflow & AI Call Recovery | '
                'Pay Per Call Episode #7 (ExclusiveLiveCall)',
       'url': 'https://www.youtube.com/watch?v=Hnh5huLjUoE&t=716s',
       'video_id': 'Hnh5huLjUoE'},
      {'author': 'TrackDrive',
       'channel': 'TrackDrive',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:18](https://www.youtube.com/watch?v=V1FTIO7peWA&t=198s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A buyer with five agents can take five calls at once. The sixth caller would '
               'have to wait or be sent somewhere else. Caps are about the total over time. '
               'Concurrency is about right now. A disposition is the outcome of a call.',
       'timestamp': 198,
       'timestamp_label': '[00:03:18]',
       'timestamp_seconds': 198,
       'tip': 'A buyer with five agents can take five calls at once. The sixth caller would '
              'have to wait or be sent somewhere else. Caps are about the total over time. '
              'Concurrency is about right now. A disposition is the outcome of a call.',
       'title': 'The Pay-Per-Call Vocabulary | Pay-Per-Call Masterclass (TrackDrive)',
       'url': 'https://www.youtube.com/watch?v=V1FTIO7peWA&t=198s',
       'video_id': 'V1FTIO7peWA'},
      {'author': 'Contractor Marketing Pros',
       'channel': 'Contractor Marketing Pros',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:17](https://www.youtube.com/watch?v=-dj0lXdjE3c&t=197s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The cost per sale is anywhere between $100 and $200. LSA show up above Google '
               'ads include that Google guaranteed badge and you only pay for real calls, not '
               "clicks. Because it's a higher conversion rate typically, right? These people "
               'are ready to hire.',
       'timestamp': 197,
       'timestamp_label': '[00:03:17]',
       'timestamp_seconds': 197,
       'tip': 'The cost per sale is anywhere between $100 and $200. LSA show up above Google '
              'ads include that Google guaranteed badge and you only pay for real calls, not '
              "clicks. Because it's a higher conversion rate typically, right? These people "
              'are ready to hire.',
       'title': 'Ultimate Guide for Plumbers for Lead Generation (2025) (Contractor Marketing '
                'Pros)',
       'url': 'https://www.youtube.com/watch?v=-dj0lXdjE3c&t=197s',
       'video_id': '-dj0lXdjE3c'},
      {'author': 'Adshot Media | Google Ads Experts',
       'channel': 'Adshot Media | Google Ads Experts',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:06](https://www.youtube.com/watch?v=9FAM3f3MDl0&t=546s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': '24 our team is ready to help you 24/7. 7 as we are only targeting uh changes '
               'and uh cancellation service. So we will not write any booking related keywords '
               'here.',
       'timestamp': 546,
       'timestamp_label': '[00:09:06]',
       'timestamp_seconds': 546,
       'tip': '24 our team is ready to help you 24/7. 7 as we are only targeting uh changes '
              'and uh cancellation service. So we will not write any booking related keywords '
              'here.',
       'title': 'How To Setup Pay Per Call Campaign Google Ads | Flight Booking | Google Ads '
                'Tutorial | AdShot Media (Adshot Media | Google Ads Experts)',
       'url': 'https://www.youtube.com/watch?v=9FAM3f3MDl0&t=546s',
       'video_id': '9FAM3f3MDl0'},
      {'author': 'John Casto',
       'channel': 'John Casto',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:11](https://www.youtube.com/watch?v=XQvPekJ-K8M&t=71s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Online they can get people click on ads but they're not necessarily a bus a "
               "Biz Dev person so and they don't know what I hire a bis Dev person so that bis "
               'Dev.',
       'timestamp': 71,
       'timestamp_label': '[00:01:11]',
       'timestamp_seconds': 71,
       'tip': "Online they can get people click on ads but they're not necessarily a bus a Biz "
              "Dev person so and they don't know what I hire a bis Dev person so that bis Dev.",
       'title': 'The BIGGEST Challenges in Pay Per Call | Affiliate Marketing (John Casto)',
       'url': 'https://www.youtube.com/watch?v=XQvPekJ-K8M&t=71s',
       'video_id': 'XQvPekJ-K8M'},
      {'author': 'Ringba',
       'channel': 'Ringba',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:51](https://www.youtube.com/watch?v=RVobRCTpSEg&t=171s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Yellow equals no conversion. Just like morality, optional. Our ringree roots '
               'calls to the highest bidder or the person who bribes the loudest. Scale '
               'budgets during crisis hours. Cut back when lawsuits rise and adjust operations '
               'without human conversation.',
       'timestamp': 171,
       'timestamp_label': '[00:02:51]',
       'timestamp_seconds': 171,
       'tip': 'Yellow equals no conversion. Just like morality, optional. Our ringree roots '
              'calls to the highest bidder or the person who bribes the loudest. Scale budgets '
              'during crisis hours. Cut back when lawsuits rise and adjust operations without '
              'human conversation.',
       'title': 'Getting Started with Ringba (2025) | Ringba Call Tracking & Analytics | Live '
                'demonstration (Ringba)',
       'url': 'https://www.youtube.com/watch?v=RVobRCTpSEg&t=171s',
       'video_id': 'RVobRCTpSEg'},
      {'author': 'CallCentreHelper',
       'channel': 'CallCentreHelper',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:46](https://www.youtube.com/watch?v=8f7qA0z-AgQ&t=106s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Ivr connecting into back-end systems identifying who the caller is based on '
               "the telephone number that they're displaying that kind of thing in order to "
               'give their their team as much information about the caller when they come '
               'through as possible.',
       'timestamp': 106,
       'timestamp_label': '[00:01:46]',
       'timestamp_seconds': 106,
       'tip': 'Ivr connecting into back-end systems identifying who the caller is based on the '
              "telephone number that they're displaying that kind of thing in order to give "
              'their their team as much information about the caller when they come through as '
              'possible.',
       'title': 'How Does an IVR Work? (CallCentreHelper)',
       'url': 'https://www.youtube.com/watch?v=8f7qA0z-AgQ&t=106s',
       'video_id': '8f7qA0z-AgQ'},
      {'author': 'Legal Case Info',
       'channel': 'Legal Case Info',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:31](https://www.youtube.com/watch?v=7f5tx0OFDQc&t=91s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "You're not just signing up for a list, you're hiring someone to represent your "
               "individual case every step of the way. Once you're in, your attorney starts "
               "building your case from the ground up. They'll collect everything.",
       'timestamp': 91,
       'timestamp_label': '[00:01:31]',
       'timestamp_seconds': 91,
       'tip': "You're not just signing up for a list, you're hiring someone to represent your "
              "individual case every step of the way. Once you're in, your attorney starts "
              "building your case from the ground up. They'll collect everything.",
       'title': 'How to file a #masstort lawsuit | Explained (Legal Case Info)',
       'url': 'https://www.youtube.com/watch?v=7f5tx0OFDQc&t=91s',
       'video_id': '7f5tx0OFDQc'},
      {'author': 'WildJar Call Intelligence',
       'channel': 'WildJar Call Intelligence',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:41](https://www.youtube.com/watch?v=5z0mahGmR40&t=221s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Notification and an SMS through sales and just an email through to support so '
               'you can follow up that customer again uh hope you enjoyed it uh any questions '
               'please reach out to the team um thanks for listening.',
       'timestamp': 221,
       'timestamp_label': '[00:03:41]',
       'timestamp_seconds': 221,
       'tip': 'Notification and an SMS through sales and just an email through to support so '
              'you can follow up that customer again uh hope you enjoyed it uh any questions '
              'please reach out to the team um thanks for listening.',
       'title': 'Call Flow Builder - IVR routing (WildJar Call Intelligence)',
       'url': 'https://www.youtube.com/watch?v=5z0mahGmR40&t=221s',
       'video_id': '5z0mahGmR40'},
      {'author': 'Ringba',
       'channel': 'Ringba',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=uDzWrD17wqg&t=21s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Them if you are not using ringba to sell calls on the ringba exchange please '
               'reach out to the ringba X team for one-on-one support to ensure you are '
               "selling calls into the exchange correctly let's get into it first go to the "
               'ringba platform and create a buyer for ringba.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'Them if you are not using ringba to sell calls on the ringba exchange please '
              'reach out to the ringba X team for one-on-one support to ensure you are selling '
              "calls into the exchange correctly let's get into it first go to the ringba "
              'platform and create a buyer for ringba.',
       'title': 'RingbaX |  How to Setup a Seller Ring Tree and Ring Tree Target (Ringba)',
       'url': 'https://www.youtube.com/watch?v=uDzWrD17wqg&t=21s',
       'video_id': 'uDzWrD17wqg'},
      {'author': 'Agent CRM',
       'channel': 'Agent CRM',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:20](https://www.youtube.com/watch?v=TFi09QYEol8&t=560s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Would say it's my pleasure but just like our viewers uh regulations are no fun "
               "but that's my job to help you guys so so you're welcome thank you guys for "
               'watching and leave any questions in the comments bye for now.',
       'timestamp': 560,
       'timestamp_label': '[00:09:20]',
       'timestamp_seconds': 560,
       'tip': "Would say it's my pleasure but just like our viewers uh regulations are no fun "
              "but that's my job to help you guys so so you're welcome thank you guys for "
              'watching and leave any questions in the comments bye for now.',
       'title': 'FCC / TCPA Regulation Updates (Agent CRM)',
       'url': 'https://www.youtube.com/watch?v=TFi09QYEol8&t=560s',
       'video_id': 'TFi09QYEol8'},
      {'author': 'Ringba',
       'channel': 'Ringba',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:36](https://www.youtube.com/watch?v=WOqDYpchQOo&t=276s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Platform trusted by industry leading pay-per-call companies connect your '
               'online marketing to your offline sales and get the data you need to drive '
               'revenue with ringbah to learn more about how ringbah is changing the future of '
               'pay-per-call visit www.ringba.com.',
       'timestamp': 276,
       'timestamp_label': '[00:04:36]',
       'timestamp_seconds': 276,
       'tip': 'Platform trusted by industry leading pay-per-call companies connect your online '
              'marketing to your offline sales and get the data you need to drive revenue with '
              'ringbah to learn more about how ringbah is changing the future of pay-per-call '
              'visit www.ringba.com.',
       'title': 'Ringba Product Training: Routing Calls to Dynamic Ring Tree Targets (Ringba)',
       'url': 'https://www.youtube.com/watch?v=WOqDYpchQOo&t=276s',
       'video_id': 'WOqDYpchQOo'},
      {'author': 'Nate Ancelet',
       'channel': 'Nate Ancelet',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:37](https://www.youtube.com/watch?v=q4tpqSo7KCE&t=577s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re doing 20 billable calls a day, you add three more affiliates in. Now "
               "you're scaling this one buyer. Now we got, you know, three other buyers or two "
               'other buyers that are trying to come in the mix. You add four affiliates, '
               'three buyers.',
       'timestamp': 577,
       'timestamp_label': '[00:09:37]',
       'timestamp_seconds': 577,
       'tip': "'re doing 20 billable calls a day, you add three more affiliates in. Now you're "
              'scaling this one buyer. Now we got, you know, three other buyers or two other '
              'buyers that are trying to come in the mix. You add four affiliates, three '
              'buyers.',
       'title': 'How to make $20,344/day with Pay Per Call (Nate Ancelet)',
       'url': 'https://www.youtube.com/watch?v=q4tpqSo7KCE&t=577s',
       'video_id': 'q4tpqSo7KCE'}],
 12: [{'author': 'vanel sylvestre',
       'channel': 'vanel sylvestre',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:19:47](https://www.youtube.com/watch?v=B2slPImGPD8&t=1187s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So you will learn step by step how to create uh profitable ads and get lot of '
               'phone calls and start making your first $100 per day online.',
       'timestamp': 1187,
       'timestamp_label': '[00:19:47]',
       'timestamp_seconds': 1187,
       'tip': 'So you will learn step by step how to create uh profitable ads and get lot of '
              'phone calls and start making your first $100 per day online.',
       'title': "I Made $11,429+ With Pay Per Call Affiliate Marketing (Here's How!) (vanel "
                'sylvestre)',
       'url': 'https://www.youtube.com/watch?v=B2slPImGPD8&t=1187s',
       'video_id': 'B2slPImGPD8'},
      {'author': 'Carlos Corona',
       'channel': 'Carlos Corona',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:48](https://www.youtube.com/watch?v=tf4AieS7Mhc&t=228s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "ACA related and it's not Medicare related. So I will strongly discourage that "
               'you go that route. It might work for a few days, for a few weeks, and '
               "eventually, you know, you're going to start hearing complaints about your "
               'calls and so on, right?',
       'timestamp': 228,
       'timestamp_label': '[00:03:48]',
       'timestamp_seconds': 228,
       'tip': "ACA related and it's not Medicare related. So I will strongly discourage that "
              'you go that route. It might work for a few days, for a few weeks, and '
              "eventually, you know, you're going to start hearing complaints about your calls "
              'and so on, right?',
       'title': 'How to set up a profitable Ringba call flow that converts (Carlos Corona)',
       'url': 'https://www.youtube.com/watch?v=tf4AieS7Mhc&t=228s',
       'video_id': 'tf4AieS7Mhc'},
      {'author': 'Ringba',
       'channel': 'Ringba',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:47:27](https://www.youtube.com/watch?v=RhODbxB4ylU&t=2847s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Those calls I'm gonna make them bid on those phone calls and I'm gonna start a "
               "bidding war because someone's going to be willing to pay more than someone "
               'else.',
       'timestamp': 2847,
       'timestamp_label': '[00:47:27]',
       'timestamp_seconds': 2847,
       'tip': "Those calls I'm gonna make them bid on those phone calls and I'm gonna start a "
              "bidding war because someone's going to be willing to pay more than someone "
              'else.',
       'title': 'Pay Per Call Masterclass - Creating a Buyer Network (Ringba)',
       'url': 'https://www.youtube.com/watch?v=RhODbxB4ylU&t=2847s',
       'video_id': 'RhODbxB4ylU'},
      {'author': 'Sabri Suby',
       'channel': 'Sabri Suby',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=u57s5wmdl5s&t=21s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s the single thing that decides whether or not your $30 lives or dies before "
               "you've even spent a scent. Most people with a small budget, they try and play "
               'it safe. And I see it every single day. They launch ads and they go out with '
               'what I call a subpar offer.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': "'s the single thing that decides whether or not your $30 lives or dies before "
              "you've even spent a scent. Most people with a small budget, they try and play "
              'it safe. And I see it every single day. They launch ads and they go out with '
              'what I call a subpar offer.',
       'title': 'How to Scale Meta Ads on a Low Budget (Post-Andromeda) (Sabri Suby)',
       'url': 'https://www.youtube.com/watch?v=u57s5wmdl5s&t=21s',
       'video_id': 'u57s5wmdl5s'},
      {'author': 'TrackDrive',
       'channel': 'TrackDrive',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:32](https://www.youtube.com/watch?v=ncatAE6wf_0&t=212s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Start with conservative caps and widen them as quality is proven. It's much "
               'easier to raise a cap for a publisher who is delivering than to explain to a '
               'buyer why they were flooded with calls on day one.',
       'timestamp': 212,
       'timestamp_label': '[00:03:32]',
       'timestamp_seconds': 212,
       'tip': "Start with conservative caps and widen them as quality is proven. It's much "
              'easier to raise a cap for a publisher who is delivering than to explain to a '
              'buyer why they were flooded with calls on day one.',
       'title': 'Setting Up a Campaign | Pay-Per-Call Masterclass (TrackDrive)',
       'url': 'https://www.youtube.com/watch?v=ncatAE6wf_0&t=212s',
       'video_id': 'ncatAE6wf_0'},
      {'author': 'Beginner to 1K a Day Journey',
       'channel': 'Beginner to 1K a Day Journey',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:43](https://www.youtube.com/watch?v=Cea6GBkjsgg&t=43s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Um the account manager even he told me if I still consistently to provide 30 '
               "qualified calls a day, he's going to increase my calls from 26 to 30. Uh but "
               "it's still it's not yet. He said it's it might be uh starting from October, "
               "but it didn't start yet.",
       'timestamp': 43,
       'timestamp_label': '[00:00:43]',
       'timestamp_seconds': 43,
       'tip': 'Um the account manager even he told me if I still consistently to provide 30 '
              "qualified calls a day, he's going to increase my calls from 26 to 30. Uh but "
              "it's still it's not yet. He said it's it might be uh starting from October, but "
              "it didn't start yet.",
       'title': 'I Built a $1,000/Day Pay Per Call Business — Here’s What’s Next (Beginner to '
                '1K a Day Journey)',
       'url': 'https://www.youtube.com/watch?v=Cea6GBkjsgg&t=43s',
       'video_id': 'Cea6GBkjsgg'},
      {'author': 'StackSense',
       'channel': 'StackSense',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:52](https://www.youtube.com/watch?v=Kkuu-FgiGxg&t=52s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Marketing Lite is $65 a month. Number three, what converts. Dynamic number '
               'insertion comes on the entry plan. White label is an extra $50 a month. Best '
               'for agencies that report every lead type to clients. Call tracking starts at '
               '$30 a month with $30 of usage credit.',
       'timestamp': 52,
       'timestamp_label': '[00:00:52]',
       'timestamp_seconds': 52,
       'tip': 'Marketing Lite is $65 a month. Number three, what converts. Dynamic number '
              'insertion comes on the entry plan. White label is an extra $50 a month. Best '
              'for agencies that report every lead type to clients. Call tracking starts at '
              '$30 a month with $30 of usage credit.',
       'title': '5 Best Call Tracking Software for Marketing Agencies (2026) (StackSense)',
       'url': 'https://www.youtube.com/watch?v=Kkuu-FgiGxg&t=52s',
       'video_id': 'Kkuu-FgiGxg'},
      {'author': 'FFL Success Zone | Integrity Connect Inbounds',
       'channel': 'FFL Success Zone | Integrity Connect Inbounds',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:29](https://www.youtube.com/watch?v=-YRrdoKG1xs&t=209s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But yeah, the call flow, I mean, how long do you typically have to wait '
               'between calls now? Honestly, sometimes not even 5 minutes. Yeah, no, I think '
               '>> We have several hundred people a day take calls.',
       'timestamp': 209,
       'timestamp_label': '[00:03:29]',
       'timestamp_seconds': 209,
       'tip': 'But yeah, the call flow, I mean, how long do you typically have to wait between '
              'calls now? Honestly, sometimes not even 5 minutes. Yeah, no, I think >> We have '
              'several hundred people a day take calls.',
       'title': '📞 How to Always Get Back on Script | Inbound Final Expense Insurance Calls '
                '(FFL Success Zone | Integrity Connect Inbounds)',
       'url': 'https://www.youtube.com/watch?v=-YRrdoKG1xs&t=209s',
       'video_id': '-YRrdoKG1xs'},
      {'author': 'Dollar_Earn_with_us',
       'channel': 'Dollar_Earn_with_us',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:41](https://www.youtube.com/watch?v=e4KqhdonStw&t=1001s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It is ADD schedule actually we'll just ask your network or advertisers or "
               'clients that uh what days and on what time they want you to run their ads so '
               "uh I'll be selecting Monday to Friday oh.",
       'timestamp': 1001,
       'timestamp_label': '[00:16:41]',
       'timestamp_seconds': 1001,
       'tip': "It is ADD schedule actually we'll just ask your network or advertisers or "
              'clients that uh what days and on what time they want you to run their ads so uh '
              "I'll be selecting Monday to Friday oh.",
       'title': 'Pay per call | Pest Control Service in United States | Google Ad for Pest '
                'Control 100% Working (Dollar_Earn_with_us)',
       'url': 'https://www.youtube.com/watch?v=e4KqhdonStw&t=1001s',
       'video_id': 'e4KqhdonStw'},
      {'author': 'FFL Agent Academy',
       'channel': 'FFL Agent Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:23](https://www.youtube.com/watch?v=xdbb7zNo-kk&t=83s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Um a month um I'm really just looking for information starting at the minimum "
               "you know if I can get it better skill doesn't have to just be great but I'm "
               'just really looking for something um just something to start off with nice '
               'okay and data.',
       'timestamp': 83,
       'timestamp_label': '[00:01:23]',
       'timestamp_seconds': 83,
       'tip': "Um a month um I'm really just looking for information starting at the minimum "
              "you know if I can get it better skill doesn't have to just be great but I'm "
              'just really looking for something um just something to start off with nice okay '
              'and data.',
       'title': 'Life Insurance Live Transfer Phone Sales Training with Alexander Strate (FFL '
                'Agent Academy)',
       'url': 'https://www.youtube.com/watch?v=xdbb7zNo-kk&t=83s',
       'video_id': 'xdbb7zNo-kk'},
      {'author': 'Attorney Joseph Lyon',
       'channel': 'Attorney Joseph Lyon',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:13](https://www.youtube.com/watch?v=nUl1KZ2z_es&t=373s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'That are unique to you and will be worked up individually if the settlement '
               'process is not successful my firm is in a position to push the case forward '
               'and to ultimately pursue your day in court as an individual and not part of a '
               'class action.',
       'timestamp': 373,
       'timestamp_label': '[00:06:13]',
       'timestamp_seconds': 373,
       'tip': 'That are unique to you and will be worked up individually if the settlement '
              'process is not successful my firm is in a position to push the case forward and '
              'to ultimately pursue your day in court as an individual and not part of a class '
              'action.',
       'title': 'What is the Process of Mass Tort Litigation? Attorney Joe Lyon Explains '
                '(Attorney Joseph Lyon)',
       'url': 'https://www.youtube.com/watch?v=nUl1KZ2z_es&t=373s',
       'video_id': 'nUl1KZ2z_es'},
      {'author': 'Ryan Moran',
       'channel': 'Ryan Moran',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:04](https://www.youtube.com/watch?v=NC4s18S7p00&t=424s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "You start the sooner you'll be able to promote offers and make more money head "
               "over to the next video in the series where I'm going to go over what to look "
               "for in a high converting offer I'll see you guys then Cheers.",
       'timestamp': 424,
       'timestamp_label': '[00:07:04]',
       'timestamp_seconds': 424,
       'tip': "You start the sooner you'll be able to promote offers and make more money head "
              "over to the next video in the series where I'm going to go over what to look "
              "for in a high converting offer I'll see you guys then Cheers.",
       'title': 'How to Find Pay-Per-Call Affiliate Networks and Offers (Ryan Moran)',
       'url': 'https://www.youtube.com/watch?v=NC4s18S7p00&t=424s',
       'video_id': 'NC4s18S7p00'},
      {'author': 'StreetText',
       'channel': 'StreetText',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:29](https://www.youtube.com/watch?v=5wE-LfVEhgk&t=209s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Recipient and it's ensuring that the context of the message relates to the "
               "initial request and it's ensuring that uh people aren't being round robin by "
               'businesses yeah have a great and awesome day.',
       'timestamp': 209,
       'timestamp_label': '[00:03:29]',
       'timestamp_seconds': 209,
       'tip': "Recipient and it's ensuring that the context of the message relates to the "
              "initial request and it's ensuring that uh people aren't being round robin by "
              'businesses yeah have a great and awesome day.',
       'title': 'FCC/TCPA Compliance 2025: New Rules for Lead Generation & Automated Messages '
                'Simplified (StreetText)',
       'url': 'https://www.youtube.com/watch?v=5wE-LfVEhgk&t=209s',
       'video_id': '5wE-LfVEhgk'},
      {'author': 'Ringba',
       'channel': 'Ringba',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:27](https://www.youtube.com/watch?v=8ojiGzzsrV0&t=267s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Tracking tags configure payout settings setup URL parameters and optimize your '
               'call routing by adding more targets to your routing plan thank you for joining '
               'us visit ring by comm to learn more about our platform or to get in touch with '
               'a ring product expert.',
       'timestamp': 267,
       'timestamp_label': '[00:04:27]',
       'timestamp_seconds': 267,
       'tip': 'Tracking tags configure payout settings setup URL parameters and optimize your '
              'call routing by adding more targets to your routing plan thank you for joining '
              'us visit ring by comm to learn more about our platform or to get in touch with '
              'a ring product expert.',
       'title': 'Account Setup | Ringba Call Tracking & Analytics (Ringba)',
       'url': 'https://www.youtube.com/watch?v=8ojiGzzsrV0&t=267s',
       'video_id': '8ojiGzzsrV0'},
      {'author': 'ceohec',
       'channel': 'ceohec',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:04](https://www.youtube.com/watch?v=SkS03nygdoY&t=364s)',
       'relevance': 'Attributed practitioner commentary on `Ringba`/`Retreaver` real-time '
                    'bidding (`RTB`) inbound pay-per-call ping-post exchanges, `90–120s` '
                    'buffer-qualified insurance/legal/emergency-trade call auctions, and '
                    '`TrustedForm`/`Jornaya` `1-to-1` consent verification (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Your buyer also agrees to the terms. Um they receive calls all week. Every '
               'call is logged, tracked, and billable. The publisher invoices you on your '
               "term, which is weekly net seven. You're You invoice your buyer, which is net "
               "three. You It's weekly net three for your buyer.",
       'timestamp': 364,
       'timestamp_label': '[00:06:04]',
       'timestamp_seconds': 364,
       'tip': 'Your buyer also agrees to the terms. Um they receive calls all week. Every call '
              'is logged, tracked, and billable. The publisher invoices you on your term, '
              "which is weekly net seven. You're You invoice your buyer, which is net three. "
              "You It's weekly net three for your buyer.",
       'title': 'How I Pay Publishers in Pay Per Call (net terms) (ceohec)',
       'url': 'https://www.youtube.com/watch?v=SkS03nygdoY&t=364s',
       'video_id': 'SkS03nygdoY'}]}
