"""Curated 180-citation High-Ticket Affiliate Marketing baseline (15 per chapter across Q1-Q12) mined strictly from verified Affiliate Marketing, SEO/GEO, Attribution, and Growth YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'affiliate',
     'b2b',
     'bounty',
     'bridge',
     'commission',
     'commissions',
     'concierge',
     'cpa',
     'fintech',
     'funnel',
     'high',
     'merchant',
     'model',
     'offer',
     'offers',
     'partner',
     'publishing',
     'recurring',
     'referral',
     'saas',
     'ticket'},
 2: {'advertiser',
     'attribution',
     'awin',
     'buyer',
     'call',
     'cj',
     'cookie',
     'cpa',
     'everflow',
     'impact',
     'lead',
     'ltv',
     'merchant',
     'network',
     'partnerstack',
     'pay',
     'payout',
     'ping',
     'post',
     'postback',
     'ringba',
     'window'},
 3: {'aov',
     'arbitrage',
     'cac',
     'chargeback',
     'clawback',
     'commission',
     'conversion',
     'cpa',
     'cpc',
     'economics',
     'epc',
     'float',
     'gross',
     'margin',
     'margins',
     'net',
     'payout',
     'profit',
     'recurring',
     'refund',
     'reversal',
     'roas',
     'scrub'},
 4: {'budget',
     'capital',
     'clickflare',
     'cloudflare',
     'domain',
     'domains',
     'edge',
     'everflow',
     'expired',
     'free',
     'hosting',
     'lander',
     'opex',
     'podcast',
     'rss',
     'serverless',
     'stack',
     'startup',
     'tracker',
     'tracking',
     'vercel',
     'voluum'},
 5: {'abuse',
     'algorithm',
     'amazon',
     'ban',
     'bidding',
     'brand',
     'clawback',
     'cookie',
     'coupon',
     'cut',
     'cuts',
     'deindex',
     'dependence',
     'fraud',
     'google',
     'hijack',
     'penalty',
     'policy',
     'reputation',
     'risk',
     'scrub',
     'stuffing',
     'trademark',
     'trap'},
 6: {'ad',
     'ads',
     'alternative',
     'comparison',
     'competitor',
     'cpc',
     'demand',
     'discover',
     'intent',
     'job',
     'keyword',
     'keywords',
     'library',
     'meta',
     'niche',
     'offers',
     'pricing',
     'query',
     'research',
     'review',
     'reviews',
     'search',
     'velocity',
     'vs'},
 7: {'ab',
     'afd',
     'attribution',
     'bridge',
     'calculator',
     'click',
     'conversion',
     'funnel',
     'lander',
     'landing',
     'lead',
     'page',
     'ping',
     'post',
     'postback',
     'presell',
     'quiz',
     'rsoc',
     's2s',
     'server',
     'subid',
     'test',
     'web2app',
     'webhook'},
 8: {'ahrefs',
     'ai',
     'analytics',
     'chatgpt',
     'chrome',
     'citation',
     'citations',
     'data',
     'extension',
     'geo',
     'llm',
     'perplexity',
     'pixel',
     'pixels',
     'plugin',
     'posthog',
     'ringba',
     'schema',
     'semrush',
     'serp',
     'tool',
     'tools',
     'tracker'},
 9: {'advertising',
     'agreement',
     'bidding',
     'brand',
     'claim',
     'claims',
     'compliance',
     'consent',
     'disclosure',
     'disclosures',
     'endorsement',
     'ftc',
     'gdpr',
     'kickback',
     'law',
     'legal',
     'medium',
     'policy',
     'privacy',
     'reddit',
     'regulation',
     'rules',
     'tcpa',
     'terms',
     'trademark'},
 10: {'arbitrage',
      'channel',
      'co',
      'coreg',
      'ctv',
      'dm',
      'email',
      'faceless',
      'loop',
      'media',
      'navboost',
      'newsletter',
      'organic',
      'paid',
      'pinterest',
      'quora',
      'reddit',
      'seo',
      'social',
      'sparkloop',
      'traffic',
      'video',
      'viral',
      'youtube'},
 11: {'acquire',
      'asset',
      'buyer',
      'content',
      'contractor',
      'contractors',
      'diversify',
      'editor',
      'empire',
      'exit',
      'flippers',
      'founder',
      'hire',
      'kpi',
      'manager',
      'media',
      'multiple',
      'multiples',
      'operations',
      'pod',
      'portfolio',
      'quiet',
      'scale',
      'scaling',
      'sop',
      'team'},
 12: {'action',
      'approve',
      'audit',
      'campaign',
      'checklist',
      'commission',
      'day',
      'days',
      'execute',
      'first',
      'funnel',
      'goal',
      'kill',
      'kpi',
      'launch',
      'milestone',
      'month',
      'offer',
      'pages',
      'plan',
      'roadmap',
      'scale',
      'sprint',
      'start',
      'steps',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Ecom Chief',
      'channel': 'Ecom Chief',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:14](https://www.youtube.com/watch?v=iVK1QrJwylk&t=74s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': 'They are platforms designed to compare, review the latest tools, and teach '
              'professional use cases. B2B SAS unit economics offer 20 to 50% commissions, '
              'yielding $50 to $500 per sale. With subscription models, one referral pays a '
              "monthly cut for the user's lifetime.",
      'timestamp': 74,
      'timestamp_label': '[00:01:14]',
      'timestamp_seconds': 74,
      'tip': 'They are platforms designed to compare, review the latest tools, and teach '
             'professional use cases. B2B SAS unit economics offer 20 to 50% commissions, '
             'yielding $50 to $500 per sale. With subscription models, one referral pays a '
             "monthly cut for the user's lifetime.",
      'title': 'How to Buy and Grow an AI Affiliate Website in 2026 (High-Ticket SaaS '
               'Commissions) (Ecom Chief)',
      'url': 'https://www.youtube.com/watch?v=iVK1QrJwylk&t=74s',
      'video_id': 'iVK1QrJwylk'},
     {'author': 'Aaron Chen',
      'channel': 'Aaron Chen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=HNlC0mNMS60&t=20s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': '26,000 here and over here selling high ticket affiliate products, somebody '
              "else's offer, $192,000. I'm going to show you right now. So the first thing "
              'that you need to understand is that there are networks out there where you can '
              'find high ticket affiliate offers.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': '26,000 here and over here selling high ticket affiliate products, somebody '
             "else's offer, $192,000. I'm going to show you right now. So the first thing that "
             'you need to understand is that there are networks out there where you can find '
             'high ticket affiliate offers.',
      'title': 'High-Ticket Affiliate Marketing Explained | How People Make $1k/Per Sale '
               '(Aaron Chen)',
      'url': 'https://www.youtube.com/watch?v=HNlC0mNMS60&t=20s',
      'video_id': 'HNlC0mNMS60'},
     {'author': 'Daniel | Tech & Data',
      'channel': 'Daniel | Tech & Data',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:55](https://www.youtube.com/watch?v=SWQet1wMMyA&t=175s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': 'You can create different reward rules depending on the business model. For '
              'example, you can offer a larger percentage for the first conversion or '
              'recurring commissions across the customer life cycle.',
      'timestamp': 175,
      'timestamp_label': '[00:02:55]',
      'timestamp_seconds': 175,
      'tip': 'You can create different reward rules depending on the business model. For '
             'example, you can offer a larger percentage for the first conversion or recurring '
             'commissions across the customer life cycle.',
      'title': 'FirstPromoter Review - 2026 | The Easiest Way to Run a SaaS Affiliate Program? '
               '(Daniel | Tech & Data)',
      'url': 'https://www.youtube.com/watch?v=SWQet1wMMyA&t=175s',
      'video_id': 'SWQet1wMMyA'},
     {'author': 'Michael Bashi',
      'channel': 'Michael Bashi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:49](https://www.youtube.com/watch?v=lh5ulbIfANU&t=409s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': "This leaves us with digital products. No, I don't mean sell online courses, "
              'high ticket coaching, or get on the phone to close high ticket clients for a '
              'large commission payout. This is unsustainable as well.',
      'timestamp': 409,
      'timestamp_label': '[00:06:49]',
      'timestamp_seconds': 409,
      'tip': "This leaves us with digital products. No, I don't mean sell online courses, high "
             'ticket coaching, or get on the phone to close high ticket clients for a large '
             'commission payout. This is unsustainable as well.',
      'title': 'The Smartest Affiliate Business Model: Recurring SaaS Commissions (Michael '
               'Bashi)',
      'url': 'https://www.youtube.com/watch?v=lh5ulbIfANU&t=409s',
      'video_id': 'lh5ulbIfANU'},
     {'author': 'Adam Enfroy',
      'channel': 'Adam Enfroy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:47](https://www.youtube.com/watch?v=rv01CKLsaY0&t=47s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': "And now, let's get into it. So, here's the fundamental difference between low "
              "ticket and high ticket affiliate marketing. With low ticket products, you're "
              'playing a volume game. So, it could be like a $50 product, 30% commission, $15 '
              'a sale.',
      'timestamp': 47,
      'timestamp_label': '[00:00:47]',
      'timestamp_seconds': 47,
      'tip': "And now, let's get into it. So, here's the fundamental difference between low "
             "ticket and high ticket affiliate marketing. With low ticket products, you're "
             'playing a volume game. So, it could be like a $50 product, 30% commission, $15 a '
             'sale.',
      'title': 'How to ACTUALLY Make Your First $1,000 with High Ticket Affiliate Marketing... '
               'Works in 2026 (Adam Enfroy)',
      'url': 'https://www.youtube.com/watch?v=rv01CKLsaY0&t=47s',
      'video_id': 'rv01CKLsaY0'},
     {'author': 'A1 Republic',
      'channel': 'A1 Republic',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:23](https://www.youtube.com/watch?v=_i_IWLtQFGM&t=23s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': 'Now, PartnerStack is not a consumer affiliate network like Amazon Associates. '
              "It's purpose-built specifically for B2B SaaS. Software companies are going to "
              'use it to manage their affiliate, reseller, and partner programs.',
      'timestamp': 23,
      'timestamp_label': '[00:00:23]',
      'timestamp_seconds': 23,
      'tip': 'Now, PartnerStack is not a consumer affiliate network like Amazon Associates. '
             "It's purpose-built specifically for B2B SaaS. Software companies are going to "
             'use it to manage their affiliate, reseller, and partner programs.',
      'title': 'Can You Make Money with Partnerstack Affiliate Marketing? (Honest Review) (A1 '
               'Republic)',
      'url': 'https://www.youtube.com/watch?v=_i_IWLtQFGM&t=23s',
      'video_id': '_i_IWLtQFGM'},
     {'author': 'Smart Capital',
      'channel': 'Smart Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:25](https://www.youtube.com/watch?v=rO96TZ7xl6A&t=145s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': 'Third, how to set up automated email sequences that nurture leads and promote '
              'affiliate offers without sounding like a sales pitch.',
      'timestamp': 145,
      'timestamp_label': '[00:02:25]',
      'timestamp_seconds': 145,
      'tip': 'Third, how to set up automated email sequences that nurture leads and promote '
             'affiliate offers without sounding like a sales pitch.',
      'title': 'B2B Affiliate Sales Funnels: High-Ticket Recurring Commissions Explained '
               '(2026) (Smart Capital)',
      'url': 'https://www.youtube.com/watch?v=rO96TZ7xl6A&t=145s',
      'video_id': 'rO96TZ7xl6A'},
     {'author': 'Kris the Entrepreneur',
      'channel': 'Kris the Entrepreneur',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=nCy55CUnfK4&t=25s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': 'So, I personally use Partners Stack a lot. And the reason why I use partner '
              'stack is because they have a lot of companies in the network that is B2B, that '
              'is tech, and is in general with higher commissions than if it was a B2C '
              'product.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': 'So, I personally use Partners Stack a lot. And the reason why I use partner '
             'stack is because they have a lot of companies in the network that is B2B, that '
             'is tech, and is in general with higher commissions than if it was a B2C product.',
      'title': "Don't Use PartnerStack Until You Watch This (Kris the Entrepreneur)",
      'url': 'https://www.youtube.com/watch?v=nCy55CUnfK4&t=25s',
      'video_id': 'nCy55CUnfK4'},
     {'author': 'Mr. Money',
      'channel': 'Mr. Money',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:41](https://www.youtube.com/watch?v=VHaXNPiHd6Q&t=341s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': 'For example, Many Chat is going to give you anywhere from $30 to $50 in '
              "recurring commissions. For example, if you go into e-commerce here, they're all "
              "going to be here and you're just going to see what they offer to you. First of "
              'all, make sure that they are in your niche.',
      'timestamp': 341,
      'timestamp_label': '[00:05:41]',
      'timestamp_seconds': 341,
      'tip': 'For example, Many Chat is going to give you anywhere from $30 to $50 in '
             "recurring commissions. For example, if you go into e-commerce here, they're all "
             "going to be here and you're just going to see what they offer to you. First of "
             'all, make sure that they are in your niche.',
      'title': 'How To Make Money With Partnerstack Affiliate Marketing in 2026 (Mr. Money)',
      'url': 'https://www.youtube.com/watch?v=VHaXNPiHd6Q&t=341s',
      'video_id': 'VHaXNPiHd6Q'},
     {'author': 'Rabbit Hole Radio',
      'channel': 'Rabbit Hole Radio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:06](https://www.youtube.com/watch?v=vvzOZL0NXKI&t=1266s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': 'Which perfectly transitions us to mistake number four. Failing to capture your '
              'audience, relying purely on a visitor clicking an affiliate link on their very '
              'first visit is a fatal error, especially for high ticket items.',
      'timestamp': 1266,
      'timestamp_label': '[00:21:06]',
      'timestamp_seconds': 1266,
      'tip': 'Which perfectly transitions us to mistake number four. Failing to capture your '
             'audience, relying purely on a visitor clicking an affiliate link on their very '
             'first visit is a fatal error, especially for high ticket items.',
      'title': 'The 2026 High Ticket Affiliate Blueprint (Rabbit Hole Radio)',
      'url': 'https://www.youtube.com/watch?v=vvzOZL0NXKI&t=1266s',
      'video_id': 'vvzOZL0NXKI'},
     {'author': 'Ecommerce Paradise | High Ticket Dropshipping',
      'channel': 'Ecommerce Paradise | High Ticket Dropshipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:28](https://www.youtube.com/watch?v=oCSQ3s1mmGQ&t=448s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': 'So, uh, you can check that out at e-commercepad. Um, I have a lifetime offer as '
              "well as monthly offers. So, choose what's best for you and what fits your "
              "budget and I'm happy to help. So, let me know if you guys have any questions.",
      'timestamp': 448,
      'timestamp_label': '[00:07:28]',
      'timestamp_seconds': 448,
      'tip': 'So, uh, you can check that out at e-commercepad. Um, I have a lifetime offer as '
             "well as monthly offers. So, choose what's best for you and what fits your budget "
             "and I'm happy to help. So, let me know if you guys have any questions.",
      'title': 'How to Build a High-Ticket Quote Funnel with GemPages and Claude (Ecommerce '
               'Paradise | High Ticket Dropshipping)',
      'url': 'https://www.youtube.com/watch?v=oCSQ3s1mmGQ&t=448s',
      'video_id': 'oCSQ3s1mmGQ'},
     {'author': 'The Infamous Joel',
      'channel': 'The Infamous Joel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:23](https://www.youtube.com/watch?v=YVPPIdIHYpo&t=503s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': "'re going to have it updated for a lifetime and you're always going to get all "
              'of my high-ticket premium recommendations, be an affiliate, and sell all this '
              'stuff. Focus on one thing at a time.',
      'timestamp': 503,
      'timestamp_label': '[00:08:23]',
      'timestamp_seconds': 503,
      'tip': "'re going to have it updated for a lifetime and you're always going to get all "
             'of my high-ticket premium recommendations, be an affiliate, and sell all this '
             'stuff. Focus on one thing at a time.',
      'title': '20 High-Ticket Affiliate Programs to Find $1K Commissions (The Infamous Joel)',
      'url': 'https://www.youtube.com/watch?v=YVPPIdIHYpo&t=503s',
      'video_id': 'YVPPIdIHYpo'},
     {'author': 'Jayant Padhi',
      'channel': 'Jayant Padhi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=wj29osNl-zE&t=30s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': 'I can show you the results right here on the screen here you can see this is '
              'what it is the model is GPT 4 so I wrote create a compelling landing page copy '
              'for a free 30 day high ticket sales course.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'I can show you the results right here on the screen here you can see this is '
             'what it is the model is GPT 4 so I wrote create a compelling landing page copy '
             'for a free 30 day high ticket sales course.',
      'title': 'I used ChatGPT4 to build a high ticket funnel (Jayant Padhi)',
      'url': 'https://www.youtube.com/watch?v=wj29osNl-zE&t=30s',
      'video_id': 'wj29osNl-zE'},
     {'author': 'Beach Bum University',
      'channel': 'Beach Bum University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:39](https://www.youtube.com/watch?v=fMKmS-H3tBg&t=399s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': 'Um, but you need Vid IQ for this. So, anyway, so it comes back, it reads '
              'through all the information and it says, "David, here\'s the full email '
              'marketing and funnel SAS stack. YouTube uh with affiliate terms, cookies, all '
              'that stuff, right?',
      'timestamp': 399,
      'timestamp_label': '[00:06:39]',
      'timestamp_seconds': 399,
      'tip': 'Um, but you need Vid IQ for this. So, anyway, so it comes back, it reads through '
             'all the information and it says, "David, here\'s the full email marketing and '
             'funnel SAS stack. YouTube uh with affiliate terms, cookies, all that stuff, '
             'right?',
      'title': "Best SaaS for Recurring Affiliate Commissions? Here's How to Find Them... "
               '(Beach Bum University)',
      'url': 'https://www.youtube.com/watch?v=fMKmS-H3tBg&t=399s',
      'video_id': 'fMKmS-H3tBg'},
     {'author': 'Jay Neyer',
      'channel': 'Jay Neyer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:51](https://www.youtube.com/watch?v=sDHZObLqdzI&t=351s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': 'And now you have a natural customer ascension ladder. You can start off with a '
              'low ticket offer, getting them coming for a birthday party celebration, use the '
              'equipment, and now you have a natural ascension path.',
      'timestamp': 351,
      'timestamp_label': '[00:05:51]',
      'timestamp_seconds': 351,
      'tip': 'And now you have a natural customer ascension ladder. You can start off with a '
             'low ticket offer, getting them coming for a birthday party celebration, use the '
             'equipment, and now you have a natural ascension path.',
      'title': 'How We Generated $211K While Building a High-Ticket Lead Funnel (Jay Neyer)',
      'url': 'https://www.youtube.com/watch?v=sDHZObLqdzI&t=351s',
      'video_id': 'sDHZObLqdzI'}],
 2: [{'author': 'Rafael Hernandez ⚡️',
      'channel': 'Rafael Hernandez ⚡️',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=A_xXkLg_0xI&t=43s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': 'Great Marketing AI, a performance marketing agency for personal injury law '
              'firm. So, what exactly is Ping Post? Most pay-per-lead agencies currently are '
              'working on a direct post where they have a specific buyer that they generate '
              "leads for. So, here's the agency owner.",
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': 'Great Marketing AI, a performance marketing agency for personal injury law firm. '
             'So, what exactly is Ping Post? Most pay-per-lead agencies currently are working '
             'on a direct post where they have a specific buyer that they generate leads for. '
             "So, here's the agency owner.",
      'title': 'The Ping Post Secret — Why PPL Agencies Are Leaving Thousands on the Table '
               '(Rafael Hernandez ⚡️)',
      'url': 'https://www.youtube.com/watch?v=A_xXkLg_0xI&t=43s',
      'video_id': 'A_xXkLg_0xI'},
     {'author': 'WordsAtScale',
      'channel': 'WordsAtScale',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:07](https://www.youtube.com/watch?v=DJFaYJ3O7aU&t=187s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': 'One network offered over $900 for buyer hazard calls. His domain was registered '
              'this February. No team, no reviews, and you can contact them on WhatsApp. A '
              "payout far above everyone else for the same call. That's bait, not a better "
              'buyer.',
      'timestamp': 187,
      'timestamp_label': '[00:03:07]',
      'timestamp_seconds': 187,
      'tip': 'One network offered over $900 for buyer hazard calls. His domain was registered '
             'this February. No team, no reviews, and you can contact them on WhatsApp. A '
             "payout far above everyone else for the same call. That's bait, not a better "
             'buyer.',
      'title': 'Pay Per Call Marketing: Sell Your Rank and Rent Calls (You Never Talk to the '
               'Business) (WordsAtScale)',
      'url': 'https://www.youtube.com/watch?v=DJFaYJ3O7aU&t=187s',
      'video_id': 'DJFaYJ3O7aU'},
     {'author': 'LeadByte',
      'channel': 'LeadByte',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:33](https://www.youtube.com/watch?v=NYSR6kFlcI8&t=153s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': "Offer and you've set up your landing page to receive the transaction ID that's "
              'generated from everflow Once the lead has been allocated to a buyer in lead '
              'bite we have set up the post back to actually fire back to everflow to record '
              'that event.',
      'timestamp': 153,
      'timestamp_label': '[00:02:33]',
      'timestamp_seconds': 153,
      'tip': "Offer and you've set up your landing page to receive the transaction ID that's "
             'generated from everflow Once the lead has been allocated to a buyer in lead bite '
             'we have set up the post back to actually fire back to everflow to record that '
             'event.',
      'title': 'Tracking Leads Sold in Everflow (LeadByte)',
      'url': 'https://www.youtube.com/watch?v=NYSR6kFlcI8&t=153s',
      'video_id': 'NYSR6kFlcI8'},
     {'author': 'ExclusiveLiveCall',
      'channel': 'ExclusiveLiveCall',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:50](https://www.youtube.com/watch?v=XKj8PVuNBOs&t=890s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': "University, I'm going to show you our lead form builder. We're going to learn "
              "how ping/post and RTB for lead forms work. We'll talk about documenting "
              'consumer consent and the consent certificate functionality built directly into '
              'Proaxis.',
      'timestamp': 890,
      'timestamp_label': '[00:14:50]',
      'timestamp_seconds': 890,
      'tip': "University, I'm going to show you our lead form builder. We're going to learn "
             "how ping/post and RTB for lead forms work. We'll talk about documenting consumer "
             'consent and the consent certificate functionality built directly into Proaxis.',
      'title': 'How to Find Pay Per Call Buyers | Build Performance Marketing Business | Pay '
               'Per Call University #9 (ExclusiveLiveCall)',
      'url': 'https://www.youtube.com/watch?v=XKj8PVuNBOs&t=890s',
      'video_id': 'XKj8PVuNBOs'},
     {'author': 'Asghar Speaks',
      'channel': 'Asghar Speaks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:01](https://www.youtube.com/watch?v=r74nmdjWZ88&t=241s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': 'Then, they hire publishers like us to take calls and forward them to the '
              'buyers. So, the role of Ringba here is simply to track the calls. Well, the '
              'company sets a fixed amount of dollars that they are going to pay out. The '
              'publisher will receive these dollars for each lead.',
      'timestamp': 241,
      'timestamp_label': '[00:04:01]',
      'timestamp_seconds': 241,
      'tip': 'Then, they hire publishers like us to take calls and forward them to the buyers. '
             'So, the role of Ringba here is simply to track the calls. Well, the company sets '
             'a fixed amount of dollars that they are going to pay out. The publisher will '
             'receive these dollars for each lead.',
      'title': 'Pay Per Call Complete Course 2026 | Ringba Tutorial | Pay Per Call  | Beginner '
               'to Advanced 2026 (Asghar Speaks)',
      'url': 'https://www.youtube.com/watch?v=r74nmdjWZ88&t=241s',
      'video_id': 'r74nmdjWZ88'},
     {'author': 'Everflow - Partner Marketing Platform',
      'channel': 'Everflow - Partner Marketing Platform',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:23](https://www.youtube.com/watch?v=qXMBHCgI3Wk&t=143s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': 'A client launching a new mobile game uses an MMP or mobile measurement partner '
              'like Singular. Since Singular handles the actual device attribution, the '
              'Everflow team is responsible for setting up the advertiser postback URL in '
              "Singular's platform.",
      'timestamp': 143,
      'timestamp_label': '[00:02:23]',
      'timestamp_seconds': 143,
      'tip': 'A client launching a new mobile game uses an MMP or mobile measurement partner '
             'like Singular. Since Singular handles the actual device attribution, the '
             'Everflow team is responsible for setting up the advertiser postback URL in '
             "Singular's platform.",
      'title': 'How to Set Up & Test Your Advertiser Postback | Everflow Mini Webinars '
               '(Everflow - Partner Marketing Platform)',
      'url': 'https://www.youtube.com/watch?v=qXMBHCgI3Wk&t=143s',
      'video_id': 'qXMBHCgI3Wk'},
     {'author': 'Rob Reece',
      'channel': 'Rob Reece',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:09](https://www.youtube.com/watch?v=5QOU-NXPWw4&t=69s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': "Picture a new local plumber needs new business. He's got a Facebook page, "
              "maybe, and he's got a contact form website, but nobody's calling. So, he calls "
              'a lead gen company, and one of the things they offer are pay per call '
              "campaigns. That's you behind the scenes.",
      'timestamp': 69,
      'timestamp_label': '[00:01:09]',
      'timestamp_seconds': 69,
      'tip': "Picture a new local plumber needs new business. He's got a Facebook page, maybe, "
             "and he's got a contact form website, but nobody's calling. So, he calls a lead "
             "gen company, and one of the things they offer are pay per call campaigns. That's "
             'you behind the scenes.',
      'title': 'RHIMS 10 Pay-Per-Call Explained (Make Money Selling Phone Calls) (Rob Reece)',
      'url': 'https://www.youtube.com/watch?v=5QOU-NXPWw4&t=69s',
      'video_id': '5QOU-NXPWw4'},
     {'author': 'ClickFlare',
      'channel': 'ClickFlare',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:02](https://www.youtube.com/watch?v=cSLdoNWYxfE&t=662s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': 'Everflow Affiliate Network and copy this post-back right here. Go to '
              'post-backs, add a new one, and you can fire a post-back on a global level or '
              "for a specific offer. So let's say I want to fire for a global level. I'm going "
              'to select the delivery method as post-back.',
      'timestamp': 662,
      'timestamp_label': '[00:11:02]',
      'timestamp_seconds': 662,
      'tip': 'Everflow Affiliate Network and copy this post-back right here. Go to post-backs, '
             'add a new one, and you can fire a post-back on a global level or for a specific '
             "offer. So let's say I want to fire for a global level. I'm going to select the "
             'delivery method as post-back.',
      'title': 'How To Track Everflow and Meta For Advanced Affiliate Marketing (ClickFlare)',
      'url': 'https://www.youtube.com/watch?v=cSLdoNWYxfE&t=662s',
      'video_id': 'cSLdoNWYxfE'},
     {'author': 'PingPost Exchange',
      'channel': 'PingPost Exchange',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:52](https://www.youtube.com/watch?v=u6fnEGbP72s&t=292s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': "Uh this screen just shows you some client campaigns and what you're going to "
              "see here is what we call I'll just draw your attention to not only the "
              'different lead types here, but the development vortex, which is real important.',
      'timestamp': 292,
      'timestamp_label': '[00:04:52]',
      'timestamp_seconds': 292,
      'tip': "Uh this screen just shows you some client campaigns and what you're going to see "
             "here is what we call I'll just draw your attention to not only the different "
             'lead types here, but the development vortex, which is real important.',
      'title': 'Ping Post Exchange Introduction - Lead Generation (PingPost Exchange)',
      'url': 'https://www.youtube.com/watch?v=u6fnEGbP72s&t=292s',
      'video_id': 'u6fnEGbP72s'},
     {'author': 'Kris the Entrepreneur',
      'channel': 'Kris the Entrepreneur',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:56](https://www.youtube.com/watch?v=JFjxGPpUYBk&t=896s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': '30-day cookie time means that the from the moment someone clicks the affiliate '
              "link that you provided, well then there's a 30-day window where if that person "
              "comes back and actually buys this product or service, well then you'll get the "
              'commission.',
      'timestamp': 896,
      'timestamp_label': '[00:14:56]',
      'timestamp_seconds': 896,
      'tip': '30-day cookie time means that the from the moment someone clicks the affiliate '
             "link that you provided, well then there's a 30-day window where if that person "
             "comes back and actually buys this product or service, well then you'll get the "
             'commission.',
      'title': 'How to Make Your First $500 on Impact (Affiliate Marketing for Beginners) '
               '(Kris the Entrepreneur)',
      'url': 'https://www.youtube.com/watch?v=JFjxGPpUYBk&t=896s',
      'video_id': 'JFjxGPpUYBk'},
     {'author': 'PingTree Systems',
      'channel': 'PingTree Systems',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=IljcLX1_Ifw&t=80s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': 'I am clicking this direct post so the diff so the all the all the campaign is '
              'uh about 95 percent same the only difference is if you see here this is pin '
              'post and here the price is 0. 00 due to this CPL so we can set the price 0.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': 'I am clicking this direct post so the diff so the all the all the campaign is uh '
             'about 95 percent same the only difference is if you see here this is pin post '
             'and here the price is 0. 00 due to this CPL so we can set the price 0.',
      'title': 'Setup Ping-Post and Direct Post Buyer (PingTree Systems)',
      'url': 'https://www.youtube.com/watch?v=IljcLX1_Ifw&t=80s',
      'video_id': 'IljcLX1_Ifw'},
     {'author': 'Atomic Funnels',
      'channel': 'Atomic Funnels',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:52](https://www.youtube.com/watch?v=g1L7iVYbiGs&t=232s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': "There are a couple drawbacks to this. Um one is that it's going to have the "
              "highest cost per booked call. So it's also going to result in the highest level "
              'of lead qualification.',
      'timestamp': 232,
      'timestamp_label': '[00:03:52]',
      'timestamp_seconds': 232,
      'tip': "There are a couple drawbacks to this. Um one is that it's going to have the "
             "highest cost per booked call. So it's also going to result in the highest level "
             'of lead qualification.',
      'title': 'Best Sales Funnel for High-Ticket Offers? 4 Types Compared (2026) (Atomic '
               'Funnels)',
      'url': 'https://www.youtube.com/watch?v=g1L7iVYbiGs&t=232s',
      'video_id': 'g1L7iVYbiGs'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:17](https://www.youtube.com/watch?v=SZ3UyKpdEjg&t=557s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': 'Sets um the one thing is that the lead price is set here at ten dollars and '
              "it's identified as a static price so in this case uh we can see here there's an "
              "html delivery uh if the lead matches these filter sets it's just going to be "
              'delivered to the to this lead buyer.',
      'timestamp': 557,
      'timestamp_label': '[00:09:17]',
      'timestamp_seconds': 557,
      'tip': "Sets um the one thing is that the lead price is set here at ten dollars and it's "
             "identified as a static price so in this case uh we can see here there's an html "
             "delivery uh if the lead matches these filter sets it's just going to be "
             'delivered to the to this lead buyer.',
      'title': 'Ping Post Basics Webinar | boberdoo Ping Post Software (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=SZ3UyKpdEjg&t=557s',
      'video_id': 'SZ3UyKpdEjg'},
     {'author': 'Beginner to 1K a Day Journey',
      'channel': 'Beginner to 1K a Day Journey',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:22](https://www.youtube.com/watch?v=lHKdHRzs75g&t=262s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': 'So I get free advertisement in almost 350 dollars. This is free money actually. '
              "So I can If I pay it, it's okay. If I pay this money, if I pay what I what I "
              'spend, so okay, you can call it okay, 250% ROI.',
      'timestamp': 262,
      'timestamp_label': '[00:04:22]',
      'timestamp_seconds': 262,
      'tip': 'So I get free advertisement in almost 350 dollars. This is free money actually. '
             "So I can If I pay it, it's okay. If I pay this money, if I pay what I what I "
             'spend, so okay, you can call it okay, 250% ROI.',
      'title': '($23k/month) 450% ROI Pay Per Call Campaign | Marketcall Case Study (Beginner '
               'to 1K a Day Journey)',
      'url': 'https://www.youtube.com/watch?v=lHKdHRzs75g&t=262s',
      'video_id': 'lHKdHRzs75g'},
     {'author': 'Listflex LLC',
      'channel': 'Listflex LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:21](https://www.youtube.com/watch?v=wv4e9QY42p8&t=201s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': 'About ping posts or high-dollar leads or the home of organ space or how this '
              'flex can kind of streamline everything and automate it for you just let us know '
              "or talk to your sales rep so thanks again and we'll talk soon.",
      'timestamp': 201,
      'timestamp_label': '[00:03:21]',
      'timestamp_seconds': 201,
      'tip': 'About ping posts or high-dollar leads or the home of organ space or how this '
             'flex can kind of streamline everything and automate it for you just let us know '
             "or talk to your sales rep so thanks again and we'll talk soon.",
      'title': 'Listflex Tip - Send or sell leads via host post ping post (Listflex LLC)',
      'url': 'https://www.youtube.com/watch?v=wv4e9QY42p8&t=201s',
      'video_id': 'wv4e9QY42p8'}],
 3: [{'author': 'Daniel | Tech & Data',
      'channel': 'Daniel | Tech & Data',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:18](https://www.youtube.com/watch?v=SWQet1wMMyA&t=378s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': 'SaaS founders and growth-focused teams. You still get full control over the '
              'affiliate dashboard experience, flexible commission structures, recurring '
              'billing attribution, and payout automation, but without going through a '
              'complicated enterprise onboarding process.',
      'timestamp': 378,
      'timestamp_label': '[00:06:18]',
      'timestamp_seconds': 378,
      'tip': 'SaaS founders and growth-focused teams. You still get full control over the '
             'affiliate dashboard experience, flexible commission structures, recurring '
             'billing attribution, and payout automation, but without going through a '
             'complicated enterprise onboarding process.',
      'title': 'FirstPromoter Review - 2026 | The Easiest Way to Run a SaaS Affiliate Program? '
               '(Daniel | Tech & Data)',
      'url': 'https://www.youtube.com/watch?v=SWQet1wMMyA&t=378s',
      'video_id': 'SWQet1wMMyA'},
     {'author': 'A1 Republic',
      'channel': 'A1 Republic',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:41](https://www.youtube.com/watch?v=_i_IWLtQFGM&t=41s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': 'So, the key thing that actually makes this different from most affiliate '
              "marketing is the fact that you're not promoting recurring software "
              'subscriptions, which means you can earn monthly recurring commission, not just '
              'a single one-time payout per sale.',
      'timestamp': 41,
      'timestamp_label': '[00:00:41]',
      'timestamp_seconds': 41,
      'tip': 'So, the key thing that actually makes this different from most affiliate '
             "marketing is the fact that you're not promoting recurring software "
             'subscriptions, which means you can earn monthly recurring commission, not just a '
             'single one-time payout per sale.',
      'title': 'Can You Make Money with Partnerstack Affiliate Marketing? (Honest Review) (A1 '
               'Republic)',
      'url': 'https://www.youtube.com/watch?v=_i_IWLtQFGM&t=41s',
      'video_id': '_i_IWLtQFGM'},
     {'author': 'Beach Bum University',
      'channel': 'Beach Bum University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=fMKmS-H3tBg&t=20s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': "I love it because it, you know, just the compounding effect. 've got all that "
              'recurring commission. Sure, you get some people that drop out, but as long as '
              "you're signing up more people than are dropping off, you're making more money "
              'all the time.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "I love it because it, you know, just the compounding effect. 've got all that "
             'recurring commission. Sure, you get some people that drop out, but as long as '
             "you're signing up more people than are dropping off, you're making more money "
             'all the time.',
      'title': "Best SaaS for Recurring Affiliate Commissions? Here's How to Find Them... "
               '(Beach Bum University)',
      'url': 'https://www.youtube.com/watch?v=fMKmS-H3tBg&t=20s',
      'video_id': 'fMKmS-H3tBg'},
     {'author': 'Kris the Entrepreneur',
      'channel': 'Kris the Entrepreneur',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:19](https://www.youtube.com/watch?v=JFjxGPpUYBk&t=499s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': "'s like some big deal or whatever or like commitment. Then another example is "
              'Hostinger. So they give you 40 to 60% commission and actually sometimes they '
              'offer recurring commission.',
      'timestamp': 499,
      'timestamp_label': '[00:08:19]',
      'timestamp_seconds': 499,
      'tip': "'s like some big deal or whatever or like commitment. Then another example is "
             'Hostinger. So they give you 40 to 60% commission and actually sometimes they '
             'offer recurring commission.',
      'title': 'How to Make Your First $500 on Impact (Affiliate Marketing for Beginners) '
               '(Kris the Entrepreneur)',
      'url': 'https://www.youtube.com/watch?v=JFjxGPpUYBk&t=499s',
      'video_id': 'JFjxGPpUYBk'},
     {'author': 'ToThePoint Guide',
      'channel': 'ToThePoint Guide',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:57](https://www.youtube.com/watch?v=fAqhUrhwABs&t=177s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': "'s also good but when you can have recurring commission not just for first year "
              "but forever is like it's so good. Like I've been in the affiliate partnership "
              'with the company. I made videos five years back. Five years back I made videos.',
      'timestamp': 177,
      'timestamp_label': '[00:02:57]',
      'timestamp_seconds': 177,
      'tip': "'s also good but when you can have recurring commission not just for first year "
             "but forever is like it's so good. Like I've been in the affiliate partnership "
             'with the company. I made videos five years back. Five years back I made videos.',
      'title': 'PartnerStack Tutorial 2026 | How to Use & Promote PartnerStack Affiliate for '
               'Beginners (ToThePoint Guide)',
      'url': 'https://www.youtube.com/watch?v=fAqhUrhwABs&t=177s',
      'video_id': 'fAqhUrhwABs'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:31](https://www.youtube.com/watch?v=SZ3UyKpdEjg&t=151s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': 'So what this would be is allows your lead seller to ping you in uh run through '
              'your ping tree and return back a dynamic price uh you can carve out a profit '
              'margin and then pass the balance back to the source so if we look into the '
              'source settings and we scroll down.',
      'timestamp': 151,
      'timestamp_label': '[00:02:31]',
      'timestamp_seconds': 151,
      'tip': 'So what this would be is allows your lead seller to ping you in uh run through '
             'your ping tree and return back a dynamic price uh you can carve out a profit '
             'margin and then pass the balance back to the source so if we look into the '
             'source settings and we scroll down.',
      'title': 'Ping Post Basics Webinar | boberdoo Ping Post Software (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=SZ3UyKpdEjg&t=151s',
      'video_id': 'SZ3UyKpdEjg'},
     {'author': 'SEO Jesus',
      'channel': 'SEO Jesus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:51](https://www.youtube.com/watch?v=fFkytpd4J_Q&t=471s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': '" I just didn\'t think straight. I wasn\'t thinking like a businessman. I '
              "wasn't thinking about profit margin or anything. And like I say, legalities and "
              'pain points and going missing.',
      'timestamp': 471,
      'timestamp_label': '[00:07:51]',
      'timestamp_seconds': 471,
      'tip': '" I just didn\'t think straight. I wasn\'t thinking like a businessman. I '
             "wasn't thinking about profit margin or anything. And like I say, legalities and "
             'pain points and going missing.',
      'title': "I Quit Affiliate SEO After 10 Years - Here's What I'm Doing Instead (SEO "
               'Jesus)',
      'url': 'https://www.youtube.com/watch?v=fFkytpd4J_Q&t=471s',
      'video_id': 'fFkytpd4J_Q'},
     {'author': 'Rafael Hernandez ⚡️',
      'channel': 'Rafael Hernandez ⚡️',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:07](https://www.youtube.com/watch?v=A_xXkLg_0xI&t=367s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': 'Best for maximizing revenue per lead. So if I go here to ping post, you can see '
              'here this shows all of my out inbound pings, outbound pings and posts. I can '
              'have different minimum profit margins. I can have different minimum profit '
              'margins, required ping fields.',
      'timestamp': 367,
      'timestamp_label': '[00:06:07]',
      'timestamp_seconds': 367,
      'tip': 'Best for maximizing revenue per lead. So if I go here to ping post, you can see '
             'here this shows all of my out inbound pings, outbound pings and posts. I can '
             'have different minimum profit margins. I can have different minimum profit '
             'margins, required ping fields.',
      'title': 'The Ping Post Secret — Why PPL Agencies Are Leaving Thousands on the Table '
               '(Rafael Hernandez ⚡️)',
      'url': 'https://www.youtube.com/watch?v=A_xXkLg_0xI&t=367s',
      'video_id': 'A_xXkLg_0xI'},
     {'author': 'Michael Bashi',
      'channel': 'Michael Bashi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:15](https://www.youtube.com/watch?v=lh5ulbIfANU&t=255s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': 'First, physical products are complicated. They have many logistical aspects to '
              'them that eats away from your commission payout by the seller. Anything '
              'physical you can think of to sell.',
      'timestamp': 255,
      'timestamp_label': '[00:04:15]',
      'timestamp_seconds': 255,
      'tip': 'First, physical products are complicated. They have many logistical aspects to '
             'them that eats away from your commission payout by the seller. Anything physical '
             'you can think of to sell.',
      'title': 'The Smartest Affiliate Business Model: Recurring SaaS Commissions (Michael '
               'Bashi)',
      'url': 'https://www.youtube.com/watch?v=lh5ulbIfANU&t=255s',
      'video_id': 'lh5ulbIfANU'},
     {'author': 'Everflow - Partner Marketing Platform',
      'channel': 'Everflow - Partner Marketing Platform',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:02](https://www.youtube.com/watch?v=BzxID19IQnM&t=542s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': "Conversion data and I'm not going to talk too much about that either because we "
              'will get into that a little bit later as well but we can go to the next slide.',
      'timestamp': 542,
      'timestamp_label': '[00:09:02]',
      'timestamp_seconds': 542,
      'tip': "Conversion data and I'm not going to talk too much about that either because we "
             'will get into that a little bit later as well but we can go to the next slide.',
      'title': 'Everflow Connect 2020 - Tracking Methods: Past, Present, and Future (Everflow '
               '- Partner Marketing Platform)',
      'url': 'https://www.youtube.com/watch?v=BzxID19IQnM&t=542s',
      'video_id': 'BzxID19IQnM'},
     {'author': 'MrOrangeDream',
      'channel': 'MrOrangeDream',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:12](https://www.youtube.com/watch?v=H5OtlkBchxU&t=432s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': "'s three ways to make money here. So the cool thing is is you like I mentioned, "
              'you make a instant you know, commission whenever you get a sale.',
      'timestamp': 432,
      'timestamp_label': '[00:07:12]',
      'timestamp_seconds': 432,
      'tip': "'s three ways to make money here. So the cool thing is is you like I mentioned, "
             'you make a instant you know, commission whenever you get a sale.',
      'title': 'Best High Ticket Affiliate Program For Beginners 2026 ($1000/Day) '
               '(MrOrangeDream)',
      'url': 'https://www.youtube.com/watch?v=H5OtlkBchxU&t=432s',
      'video_id': 'H5OtlkBchxU'},
     {'author': 'MissionMoreMoney',
      'channel': 'MissionMoreMoney',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=vd2RLWPlaqw&t=102s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': 'All right, the commission preferences section is the other thing that I wanted '
              'to talk to you about. So, when setting your commission preferences on here, '
              'choose revenue percentage over a fixed fee.',
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': 'All right, the commission preferences section is the other thing that I wanted '
             'to talk to you about. So, when setting your commission preferences on here, '
             'choose revenue percentage over a fixed fee.',
      'title': 'PartnerStack Affiliate Marketing | Basic Tutorial for Beginners '
               '(MissionMoreMoney)',
      'url': 'https://www.youtube.com/watch?v=vd2RLWPlaqw&t=102s',
      'video_id': 'vd2RLWPlaqw'},
     {'author': 'KudaOnline',
      'channel': 'KudaOnline',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=EUQ9OfMYDnw&t=65s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': 'Forect affiliate marketing laws and then the federal commission headlines there '
              'is the data protection is the gdp and best practices is for future future trend '
              'we will beat you will be looking at now let us look at an overview affiliate.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': 'Forect affiliate marketing laws and then the federal commission headlines there '
             'is the data protection is the gdp and best practices is for future future trend '
             'we will beat you will be looking at now let us look at an overview affiliate.',
      'title': 'Must-Know Affiliate Marketing Laws: FTC Guidelines, GDPR, and Disclosure Best '
               'Practices (KudaOnline)',
      'url': 'https://www.youtube.com/watch?v=EUQ9OfMYDnw&t=65s',
      'video_id': 'EUQ9OfMYDnw'},
     {'author': 'Khris Steven',
      'channel': 'Khris Steven',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:57](https://www.youtube.com/watch?v=-C4gk3OAfmk&t=417s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': 'So, you put your affiliate link and make some commission, right? So, this is '
              'you can create a content on deal versus Rippling, deal versus Gusto, deal '
              'versus Remote, you know, deal versus deal deal versus Work Workday Wise.',
      'timestamp': 417,
      'timestamp_label': '[00:06:57]',
      'timestamp_seconds': 417,
      'tip': 'So, you put your affiliate link and make some commission, right? So, this is you '
             'can create a content on deal versus Rippling, deal versus Gusto, deal versus '
             'Remote, you know, deal versus deal deal versus Work Workday Wise.',
      'title': 'PartnerStack Affiliate Walkthrough: Finding Offers + My $3K Withdrawal (Khris '
               'Steven)',
      'url': 'https://www.youtube.com/watch?v=-C4gk3OAfmk&t=417s',
      'video_id': '-C4gk3OAfmk'},
     {'author': 'Rabbit Hole Radio',
      'channel': 'Rabbit Hole Radio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:34:41](https://www.youtube.com/watch?v=vvzOZL0NXKI&t=2081s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': 'The NLP categorized disclosures as clear if they used unambiguous phrasing, '
              'such as I earn a commission or, as an Amazon associate, I earn from qualifying '
              'purchases.',
      'timestamp': 2081,
      'timestamp_label': '[00:34:41]',
      'timestamp_seconds': 2081,
      'tip': 'The NLP categorized disclosures as clear if they used unambiguous phrasing, such '
             'as I earn a commission or, as an Amazon associate, I earn from qualifying '
             'purchases.',
      'title': 'The 2026 High Ticket Affiliate Blueprint (Rabbit Hole Radio)',
      'url': 'https://www.youtube.com/watch?v=vvzOZL0NXKI&t=2081s',
      'video_id': 'vvzOZL0NXKI'}],
 4: [{'author': 'Bens Review Videos',
      'channel': 'Bens Review Videos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:40](https://www.youtube.com/watch?v=eqw-Rqw7PNY&t=220s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': 'Two more prompts write the privacy and terms pages. Hosting is free on GitHub '
              'Pages, and the companion lists the four A records for your registrar. '
              'Everything is written out here, so you can follow it with the video paused. '
              'Module five is the ten dollar call stack.',
      'timestamp': 220,
      'timestamp_label': '[00:03:40]',
      'timestamp_seconds': 220,
      'tip': 'Two more prompts write the privacy and terms pages. Hosting is free on GitHub '
             'Pages, and the companion lists the four A records for your registrar. Everything '
             'is written out here, so you can follow it with the video paused. Module five is '
             'the ten dollar call stack.',
      'title': 'RHIMS 10 Review: Pay Per Call Affiliate Marketing for Beginners, Expired '
               'Domains + 3 Bonuses (Bens Review Videos)',
      'url': 'https://www.youtube.com/watch?v=eqw-Rqw7PNY&t=220s',
      'video_id': 'eqw-Rqw7PNY'},
     {'author': 'ClickFlare',
      'channel': 'ClickFlare',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:15](https://www.youtube.com/watch?v=cSLdoNWYxfE&t=375s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': "I'll grab this tracking link right here. I'll copy it, and create it on "
              "Clickflare. So let's name it Everflow offer.",
      'timestamp': 375,
      'timestamp_label': '[00:06:15]',
      'timestamp_seconds': 375,
      'tip': "I'll grab this tracking link right here. I'll copy it, and create it on "
             "Clickflare. So let's name it Everflow offer.",
      'title': 'How To Track Everflow and Meta For Advanced Affiliate Marketing (ClickFlare)',
      'url': 'https://www.youtube.com/watch?v=cSLdoNWYxfE&t=375s',
      'video_id': 'cSLdoNWYxfE'},
     {'author': 'Jay Neyer',
      'channel': 'Jay Neyer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=sDHZObLqdzI&t=168s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': 'And so, step one was fixing the measurement. Before moving the budget around, '
              'we wanted to make sure that we can actually trust the numbers. So, we had to '
              'rebuild the conversion tracking.',
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': 'And so, step one was fixing the measurement. Before moving the budget around, we '
             'wanted to make sure that we can actually trust the numbers. So, we had to '
             'rebuild the conversion tracking.',
      'title': 'How We Generated $211K While Building a High-Ticket Lead Funnel (Jay Neyer)',
      'url': 'https://www.youtube.com/watch?v=sDHZObLqdzI&t=168s',
      'video_id': 'sDHZObLqdzI'},
     {'author': 'Everflow - Partner Marketing Platform',
      'channel': 'Everflow - Partner Marketing Platform',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:18](https://www.youtube.com/watch?v=Ni95PXMEMzE&t=318s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': 'Primary tracking domain and how to do that uh essentially the same thing with '
              "your partners so let's start at an offer so we're going to go to offers man.",
      'timestamp': 318,
      'timestamp_label': '[00:05:18]',
      'timestamp_seconds': 318,
      'tip': 'Primary tracking domain and how to do that uh essentially the same thing with '
             "your partners so let's start at an offer so we're going to go to offers man.",
      'title': 'Tracking & Conversion Domain Management | Webinars (Everflow - Partner '
               'Marketing Platform)',
      'url': 'https://www.youtube.com/watch?v=Ni95PXMEMzE&t=318s',
      'video_id': 'Ni95PXMEMzE'},
     {'author': 'SERPSUPPORT',
      'channel': 'SERPSUPPORT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=xREoSqy-pj0&t=83s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': 'Big domains have years of history, millions of backlinks, and a strong brand. A '
              'new page on that domain inherits part of that trust from day one. Compare that '
              'with a fresh site.',
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': 'Big domains have years of history, millions of backlinks, and a strong brand. A '
             'new page on that domain inherits part of that trust from day one. Compare that '
             'with a fresh site.',
      'title': "What Is Parasite SEO? Google's Crackdown Explained (SERPSUPPORT)",
      'url': 'https://www.youtube.com/watch?v=xREoSqy-pj0&t=83s',
      'video_id': 'xREoSqy-pj0'},
     {'author': 'AffiliateStrat',
      'channel': 'AffiliateStrat',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:54](https://www.youtube.com/watch?v=Z_YllaXsWGA&t=1074s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': 'IDs and sub IDs um for further tracking. So your link can be direct linking or '
              'a redirect link and everything that you need to create is just right here on '
              "this pane. Now, if we go to traffic health, I don't have the required "
              'permissions to access this field.',
      'timestamp': 1074,
      'timestamp_label': '[00:17:54]',
      'timestamp_seconds': 1074,
      'tip': 'IDs and sub IDs um for further tracking. So your link can be direct linking or a '
             'redirect link and everything that you need to create is just right here on this '
             "pane. Now, if we go to traffic health, I don't have the required permissions to "
             'access this field.',
      'title': 'Everflow Review & Guide: Full Platform Walkthrough, Pros, Cons, and Real Demos '
               '(AffiliateStrat)',
      'url': 'https://www.youtube.com/watch?v=Z_YllaXsWGA&t=1074s',
      'video_id': 'Z_YllaXsWGA'},
     {'author': 'Drew Tutorial',
      'channel': 'Drew Tutorial',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=fPXIdQyUtwQ&t=91s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': 'PayPal or Stripe, you can do that. Simple click and set up withdrawal. And from '
              "here, choose the method that you want. So, let's say I wanted to do for example "
              'PayPal. I click on that and just enter my details. PayPal to my Partner Stack '
              'account.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': 'PayPal or Stripe, you can do that. Simple click and set up withdrawal. And from '
             "here, choose the method that you want. So, let's say I wanted to do for example "
             'PayPal. I click on that and just enter my details. PayPal to my Partner Stack '
             'account.',
      'title': 'How to Use PartnerStack (Full Tutorial) | Start Earning With Affiliate '
               'Programs Fast! (Drew Tutorial)',
      'url': 'https://www.youtube.com/watch?v=fPXIdQyUtwQ&t=91s',
      'video_id': 'fPXIdQyUtwQ'},
     {'author': 'CrowdReply | Rank in AI Answers',
      'channel': 'CrowdReply | Rank in AI Answers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:43](https://www.youtube.com/watch?v=GCT2Tp-7xys&t=463s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': "That's basically parasite SEO on how it is nowadays, and it's certainly "
              "different than what it used to be. It's a bit tricky, and you can certainly do "
              'it yourself if you got the tracking software. So, head over to Crowd Reply.',
      'timestamp': 463,
      'timestamp_label': '[00:07:43]',
      'timestamp_seconds': 463,
      'tip': "That's basically parasite SEO on how it is nowadays, and it's certainly "
             "different than what it used to be. It's a bit tricky, and you can certainly do "
             'it yourself if you got the tracking software. So, head over to Crowd Reply.',
      'title': "Is Parasite SEO Dead? No. Here's the 2026 Version (230 Citations From One "
               'Page) (CrowdReply | Rank in AI Answers)',
      'url': 'https://www.youtube.com/watch?v=GCT2Tp-7xys&t=463s',
      'video_id': 'GCT2Tp-7xys'},
     {'author': 'Marcel Sattler | Leading Native Advertising Expert',
      'channel': 'Marcel Sattler | Leading Native Advertising Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:32](https://www.youtube.com/watch?v=zxw8X11thwQ&t=212s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': 'Cars now almost being given away sea prices. So it suggests you that never '
              "driven cars are almost for free. And when you're searching for a car, you "
              "definitely want to check it out because they're playing a lot of, or they're "
              'playing.',
      'timestamp': 212,
      'timestamp_label': '[00:03:32]',
      'timestamp_seconds': 212,
      'tip': 'Cars now almost being given away sea prices. So it suggests you that never '
             "driven cars are almost for free. And when you're searching for a car, you "
             "definitely want to check it out because they're playing a lot of, or they're "
             'playing.',
      'title': 'Native Ads Samples – Affiliate, Arbitrage & Performance (Taboola Sample / '
               'Outbrain Sample) (Marcel Sattler | Leading Native Advertising Expert)',
      'url': 'https://www.youtube.com/watch?v=zxw8X11thwQ&t=212s',
      'video_id': 'zxw8X11thwQ'},
     {'author': 'LeadByte',
      'channel': 'LeadByte',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=NYSR6kFlcI8&t=60s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': 'We are now just going to click on the test URL you can see here this is just a '
              'test site you can see here we decided to pass in the everflow transaction ID '
              'into the source field so when we submit a lead the source value so the '
              'transaction ID will be submitted into lead.',
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': 'We are now just going to click on the test URL you can see here this is just a '
             'test site you can see here we decided to pass in the everflow transaction ID '
             'into the source field so when we submit a lead the source value so the '
             'transaction ID will be submitted into lead.',
      'title': 'Tracking Leads Sold in Everflow (LeadByte)',
      'url': 'https://www.youtube.com/watch?v=NYSR6kFlcI8&t=60s',
      'video_id': 'NYSR6kFlcI8'},
     {'author': 'Everflow - Partner Marketing Platform',
      'channel': 'Everflow - Partner Marketing Platform',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=2Q-xY6ABqXE&t=22s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': "So, the process starts the moment a user clicks a partner's tracking link, "
              'prompting Everflow to immediately generate and store a unique identifier called '
              'the transaction ID.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "So, the process starts the moment a user clicks a partner's tracking link, "
             'prompting Everflow to immediately generate and store a unique identifier called '
             'the transaction ID.',
      'title': 'What is a Server-to-Server (S2S) Postback? | Everflow Mini Webinars (Everflow '
               '- Partner Marketing Platform)',
      'url': 'https://www.youtube.com/watch?v=2Q-xY6ABqXE&t=22s',
      'video_id': '2Q-xY6ABqXE'},
     {'author': 'Roland Bernath',
      'channel': 'Roland Bernath',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:48](https://www.youtube.com/watch?v=RbYaW3a3yCY&t=48s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': "'re the right person or you're the right company to work with them. And then "
              'basically right in the bottom of it, you have a very simple button that says '
              'get started, book a call, get a free XYZ strategy session.',
      'timestamp': 48,
      'timestamp_label': '[00:00:48]',
      'timestamp_seconds': 48,
      'tip': "'re the right person or you're the right company to work with them. And then "
             'basically right in the bottom of it, you have a very simple button that says get '
             'started, book a call, get a free XYZ strategy session.',
      'title': 'The ONLY Funnel You Need to Sell High Ticket in 2026 (Roland Bernath)',
      'url': 'https://www.youtube.com/watch?v=RbYaW3a3yCY&t=48s',
      'video_id': 'RbYaW3a3yCY'},
     {'author': 'SEO Boardroom',
      'channel': 'SEO Boardroom',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:47](https://www.youtube.com/watch?v=L6ZLGvFvaT8&t=407s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': 'Uh research, check for keywords that uh might be very good opportunities that '
              'are not that saturated. Outrank your competitors because they are simply weak. '
              'Uh especially if you have the budget. And of course, this goes to my previous '
              'point.',
      'timestamp': 407,
      'timestamp_label': '[00:06:47]',
      'timestamp_seconds': 407,
      'tip': 'Uh research, check for keywords that uh might be very good opportunities that '
             'are not that saturated. Outrank your competitors because they are simply weak. '
             'Uh especially if you have the budget. And of course, this goes to my previous '
             'point.',
      'title': 'Google Just Said Parasite SEO Is OK! (SEO Boardroom)',
      'url': 'https://www.youtube.com/watch?v=L6ZLGvFvaT8&t=407s',
      'video_id': 'L6ZLGvFvaT8'},
     {'author': 'Automate & Chill By Abhishek Sood',
      'channel': 'Automate & Chill By Abhishek Sood',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:14](https://www.youtube.com/watch?v=g7SAWXINXDo&t=74s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': "From here, you'll need to get a phone number; for example, it's for plumbing. "
              'We\'re building a plumbing website. So, go to the campaign and click on "Add '
              'Number." There are two options: toll-free and local.',
      'timestamp': 74,
      'timestamp_label': '[00:01:14]',
      'timestamp_seconds': 74,
      'tip': "From here, you'll need to get a phone number; for example, it's for plumbing. "
             'We\'re building a plumbing website. So, go to the campaign and click on "Add '
             'Number." There are two options: toll-free and local.',
      'title': 'LeadSmart Pay Per Call Affiliate Approval & How to get trackable phone number '
               'from Ringba (Automate & Chill By Abhishek Sood)',
      'url': 'https://www.youtube.com/watch?v=g7SAWXINXDo&t=74s',
      'video_id': 'g7SAWXINXDo'},
     {'author': 'A1 Republic',
      'channel': 'A1 Republic',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:42](https://www.youtube.com/watch?v=_i_IWLtQFGM&t=222s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': '12 months for each new customer that you refer. So, if some person gets the '
              "plan at $20, you're going to get $10. So, you have a free trial for customers, "
              'which has a free plan, and then discounts. So, you have give a 20% discount on '
              'annual plans.',
      'timestamp': 222,
      'timestamp_label': '[00:03:42]',
      'timestamp_seconds': 222,
      'tip': '12 months for each new customer that you refer. So, if some person gets the plan '
             "at $20, you're going to get $10. So, you have a free trial for customers, which "
             'has a free plan, and then discounts. So, you have give a 20% discount on annual '
             'plans.',
      'title': 'Can You Make Money with Partnerstack Affiliate Marketing? (Honest Review) (A1 '
               'Republic)',
      'url': 'https://www.youtube.com/watch?v=_i_IWLtQFGM&t=222s',
      'video_id': '_i_IWLtQFGM'}],
 5: [{'author': 'Edward Sturm',
      'channel': 'Edward Sturm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=NsptdY_L85A&t=64s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': 'These websites will not be penalized within Google. Google has this policy '
              "called the site reputation abuse policy. The EU's issue is that this policy may "
              'have been too broad under the digital markets act.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': 'These websites will not be penalized within Google. Google has this policy '
             "called the site reputation abuse policy. The EU's issue is that this policy may "
             'have been too broad under the digital markets act.',
      'title': "Google Just Dropped the Parasite SEO Penalty in Europe. Here's the Catch "
               '(Edward Sturm)',
      'url': 'https://www.youtube.com/watch?v=NsptdY_L85A&t=64s',
      'video_id': 'NsptdY_L85A'},
     {'author': 'SERPSUPPORT',
      'channel': 'SERPSUPPORT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:13](https://www.youtube.com/watch?v=xREoSqy-pj0&t=193s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': 'Google noticed, and it responded with a new rule. In March 2024, Google '
              'announced its site reputation abuse policy and started enforcing it with manual '
              'actions in May 2024. In November 2024, it went further.',
      'timestamp': 193,
      'timestamp_label': '[00:03:13]',
      'timestamp_seconds': 193,
      'tip': 'Google noticed, and it responded with a new rule. In March 2024, Google '
             'announced its site reputation abuse policy and started enforcing it with manual '
             'actions in May 2024. In November 2024, it went further.',
      'title': "What Is Parasite SEO? Google's Crackdown Explained (SERPSUPPORT)",
      'url': 'https://www.youtube.com/watch?v=xREoSqy-pj0&t=193s',
      'video_id': 'xREoSqy-pj0'},
     {'author': 'The Agent Workshop',
      'channel': 'The Agent Workshop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=NPtudBqceS0&t=64s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': "Google's own examples: an education site hosting payday loan reviews, a medical "
              "site hosting casino pages, a news site's coupon section run by an outside "
              'company, or a sports site hosting supplement reviews. Google added this policy '
              'in March 2024.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': "Google's own examples: an education site hosting payday loan reviews, a medical "
             "site hosting casino pages, a news site's coupon section run by an outside "
             'company, or a sports site hosting supplement reviews. Google added this policy '
             'in March 2024.',
      'title': 'Parasite SEO in 2026: What Still Works (and What Gets You Penalized) (The '
               'Agent Workshop)',
      'url': 'https://www.youtube.com/watch?v=NPtudBqceS0&t=64s',
      'video_id': 'NPtudBqceS0'},
     {'author': 'SEO Boardroom',
      'channel': 'SEO Boardroom',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:26](https://www.youtube.com/watch?v=L6ZLGvFvaT8&t=86s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': 'As of 28th of August Google is saying they will not give you manual penalty '
              'within European Union. AKA they will not punish parasite SEO practices, '
              'piggybacking practices, site abuse practices with manual penalty, which is '
              'huge, right?',
      'timestamp': 86,
      'timestamp_label': '[00:01:26]',
      'timestamp_seconds': 86,
      'tip': 'As of 28th of August Google is saying they will not give you manual penalty '
             'within European Union. AKA they will not punish parasite SEO practices, '
             'piggybacking practices, site abuse practices with manual penalty, which is huge, '
             'right?',
      'title': 'Google Just Said Parasite SEO Is OK! (SEO Boardroom)',
      'url': 'https://www.youtube.com/watch?v=L6ZLGvFvaT8&t=86s',
      'video_id': 'L6ZLGvFvaT8'},
     {'author': 'SEO Jesus',
      'channel': 'SEO Jesus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:18](https://www.youtube.com/watch?v=fFkytpd4J_Q&t=738s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': "Google don't like that anymore. And that's all there is to it. So, you know, it "
              "there's no real quick, easy to do now. You know, you need to build a brand, you "
              'need to do all of this other funky stuff.',
      'timestamp': 738,
      'timestamp_label': '[00:12:18]',
      'timestamp_seconds': 738,
      'tip': "Google don't like that anymore. And that's all there is to it. So, you know, it "
             "there's no real quick, easy to do now. You know, you need to build a brand, you "
             'need to do all of this other funky stuff.',
      'title': "I Quit Affiliate SEO After 10 Years - Here's What I'm Doing Instead (SEO "
               'Jesus)',
      'url': 'https://www.youtube.com/watch?v=fFkytpd4J_Q&t=738s',
      'video_id': 'fFkytpd4J_Q'},
     {'author': 'Aaron Chen',
      'channel': 'Aaron Chen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:26](https://www.youtube.com/watch?v=HNlC0mNMS60&t=206s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': 'So I asked Google Gemini what is the average commission rate for Amazon '
              'associates? And you can see right here that it says between 1 to 4% is most '
              'typical for physical goods. So 1% is for Amazon fresh video games, consoles, '
              'grocery, health and personal care.',
      'timestamp': 206,
      'timestamp_label': '[00:03:26]',
      'timestamp_seconds': 206,
      'tip': 'So I asked Google Gemini what is the average commission rate for Amazon '
             'associates? And you can see right here that it says between 1 to 4% is most '
             'typical for physical goods. So 1% is for Amazon fresh video games, consoles, '
             'grocery, health and personal care.',
      'title': 'High-Ticket Affiliate Marketing Explained | How People Make $1k/Per Sale '
               '(Aaron Chen)',
      'url': 'https://www.youtube.com/watch?v=HNlC0mNMS60&t=206s',
      'video_id': 'HNlC0mNMS60'},
     {'author': 'Jay Neyer',
      'channel': 'Jay Neyer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:31](https://www.youtube.com/watch?v=sDHZObLqdzI&t=211s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': 'And for that same period, the connection recorded $31,000 in conversion value. '
              "And GA4 showed over $28,000. So, about 11% more revenue from Google's bidding "
              "that we can now see. Now, let's talk about the low ticket funnel.",
      'timestamp': 211,
      'timestamp_label': '[00:03:31]',
      'timestamp_seconds': 211,
      'tip': 'And for that same period, the connection recorded $31,000 in conversion value. '
             "And GA4 showed over $28,000. So, about 11% more revenue from Google's bidding "
             "that we can now see. Now, let's talk about the low ticket funnel.",
      'title': 'How We Generated $211K While Building a High-Ticket Lead Funnel (Jay Neyer)',
      'url': 'https://www.youtube.com/watch?v=sDHZObLqdzI&t=211s',
      'video_id': 'sDHZObLqdzI'},
     {'author': 'Vasco Aires',
      'channel': 'Vasco Aires',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:38:37](https://www.youtube.com/watch?v=C2ne_saHpSs&t=2317s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': 'And then, uh, because they rely heavily on social, okay? Optimize for brand '
              'mentions across the web. Not just Google and Bing, but social media, LinkedIn, '
              'YouTube, Tik Tok. They need to know about your brand. Then, of course, be '
              'coherent, right?',
      'timestamp': 2317,
      'timestamp_label': '[00:38:37]',
      'timestamp_seconds': 2317,
      'tip': 'And then, uh, because they rely heavily on social, okay? Optimize for brand '
             'mentions across the web. Not just Google and Bing, but social media, LinkedIn, '
             'YouTube, Tik Tok. They need to know about your brand. Then, of course, be '
             'coherent, right?',
      'title': 'SaaS SEO Strategy - How I make $4,000/day with a SaaS (Vasco Aires)',
      'url': 'https://www.youtube.com/watch?v=C2ne_saHpSs&t=2317s',
      'video_id': 'C2ne_saHpSs'},
     {'author': 'Seeking Profit',
      'channel': 'Seeking Profit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:59](https://www.youtube.com/watch?v=fo-OxsDnUVQ&t=1379s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': 'The single product review like the vacuum 75 just the product is showing versus '
              "keywords in and amongst the brand page which is interesting we're also seeing.",
      'timestamp': 1379,
      'timestamp_label': '[00:22:59]',
      'timestamp_seconds': 1379,
      'tip': 'The single product review like the vacuum 75 just the product is showing versus '
             "keywords in and amongst the brand page which is interesting we're also seeing.",
      'title': 'The Formula Behind High-Converting Affiliate Articles (w/Jamie IF) (Seeking '
               'Profit)',
      'url': 'https://www.youtube.com/watch?v=fo-OxsDnUVQ&t=1379s',
      'video_id': 'fo-OxsDnUVQ'},
     {'author': 'Marcel Sattler | Leading Native Advertising Expert',
      'channel': 'Marcel Sattler | Leading Native Advertising Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:35](https://www.youtube.com/watch?v=7JPuuysCuKw&t=335s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': 'Traffic of course and maybe they have a different system so maybe they are not '
              'making the purchase straight away but maybe they are generating the email '
              "addresses additionally and afterwards like let's say you have a 30 30 day "
              'cookie.',
      'timestamp': 335,
      'timestamp_label': '[00:05:35]',
      'timestamp_seconds': 335,
      'tip': 'Traffic of course and maybe they have a different system so maybe they are not '
             'making the purchase straight away but maybe they are generating the email '
             "addresses additionally and afterwards like let's say you have a 30 30 day "
             'cookie.',
      'title': 'Affiliate Marketing + Native Ads: Make Money with this Strategy on Taboola and '
               'Outbrain (Marcel Sattler | Leading Native Advertising Expert)',
      'url': 'https://www.youtube.com/watch?v=7JPuuysCuKw&t=335s',
      'video_id': '7JPuuysCuKw'},
     {'author': 'Traffic Cardinal EN — Affiliate Press',
      'channel': 'Traffic Cardinal EN — Affiliate Press',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:35](https://www.youtube.com/watch?v=caUORKmsfnU&t=815s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': "It's it's a lot better in uh Europe than the US generally. Obviously everything "
              'is better than in the US. Uh I also heard that Google is actively fighting the '
              'abuse of website authority.',
      'timestamp': 815,
      'timestamp_label': '[00:13:35]',
      'timestamp_seconds': 815,
      'tip': "It's it's a lot better in uh Europe than the US generally. Obviously everything "
             'is better than in the US. Uh I also heard that Google is actively fighting the '
             'abuse of website authority.',
      'title': 'The SEO Strategy Google Can’t Kill — James Oliver Explains Parasite SEO '
               '(Traffic Cardinal EN — Affiliate Press)',
      'url': 'https://www.youtube.com/watch?v=caUORKmsfnU&t=815s',
      'video_id': 'caUORKmsfnU'},
     {'author': 'Julian Goldie SEO',
      'channel': 'Julian Goldie SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:31](https://www.youtube.com/watch?v=hIETDrxi-7Q&t=1291s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': "Towards them and so I think what you'll see on Twitter right now is a lot of "
              "people not really giving that much value and they're just complaining about oh.",
      'timestamp': 1291,
      'timestamp_label': '[00:21:31]',
      'timestamp_seconds': 1291,
      'tip': "Towards them and so I think what you'll see on Twitter right now is a lot of "
             "people not really giving that much value and they're just complaining about oh.",
      'title': 'Google Site Reputation Abuse Update: Is Parasite SEO OVER? 😱 (Julian Goldie '
               'SEO)',
      'url': 'https://www.youtube.com/watch?v=hIETDrxi-7Q&t=1291s',
      'video_id': 'hIETDrxi-7Q'},
     {'author': 'CrowdReply | Rank in AI Answers',
      'channel': 'CrowdReply | Rank in AI Answers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=GCT2Tp-7xys&t=104s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': "'s not necessarily looking at you, it's looking at the brand or the website "
              'that is talking about you. And in this case, that is easy to go very, very bad '
              'on. So, you have your own new website.',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': "'s not necessarily looking at you, it's looking at the brand or the website that "
             'is talking about you. And in this case, that is easy to go very, very bad on. '
             'So, you have your own new website.',
      'title': "Is Parasite SEO Dead? No. Here's the 2026 Version (230 Citations From One "
               'Page) (CrowdReply | Rank in AI Answers)',
      'url': 'https://www.youtube.com/watch?v=GCT2Tp-7xys&t=104s',
      'video_id': 'GCT2Tp-7xys'},
     {'author': 'Everflow - Partner Marketing Platform',
      'channel': 'Everflow - Partner Marketing Platform',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:55](https://www.youtube.com/watch?v=FMpj69YFsHA&t=535s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': 'Track this event in your everflow account and this event will be across all '
              'your offers that you created for this specific Advertiser in this case is '
              "Amazon so let's go back to Advertiser.",
      'timestamp': 535,
      'timestamp_label': '[00:08:55]',
      'timestamp_seconds': 535,
      'tip': 'Track this event in your everflow account and this event will be across all your '
             'offers that you created for this specific Advertiser in this case is Amazon so '
             "let's go back to Advertiser.",
      'title': 'General Advertiser & Postback set up (Everflow - Partner Marketing Platform)',
      'url': 'https://www.youtube.com/watch?v=FMpj69YFsHA&t=535s',
      'video_id': 'FMpj69YFsHA'},
     {'author': 'Ahrefs',
      'channel': 'Ahrefs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:33](https://www.youtube.com/watch?v=Sk8MAbD39Qw&t=153s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': "So, we updated at that point we'd updated 30 of the 50 that are in the "
              'portfolio. Organic traffic is up 249%. Revenue per buyers guide up 140% through '
              'the worst content downturn in a decade, while the rest of the industry was '
              'getting cut in half.',
      'timestamp': 153,
      'timestamp_label': '[00:02:33]',
      'timestamp_seconds': 153,
      'tip': "So, we updated at that point we'd updated 30 of the 50 that are in the "
             'portfolio. Organic traffic is up 249%. Revenue per buyers guide up 140% through '
             'the worst content downturn in a decade, while the rest of the industry was '
             'getting cut in half.',
      'title': 'Google Crushed Affiliate Websites. His Grew Anyway. (Ahrefs)',
      'url': 'https://www.youtube.com/watch?v=Sk8MAbD39Qw&t=153s',
      'video_id': 'Sk8MAbD39Qw'}],
 6: [{'author': 'Adam Enfroy',
      'channel': 'Adam Enfroy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:15](https://www.youtube.com/watch?v=rv01CKLsaY0&t=735s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': "So, here's how to evaluate if a niche is worth entering. So, search for these "
              "buyer intent keywords in that space. If it's all major media publications, it's "
              'probably too competitive.',
      'timestamp': 735,
      'timestamp_label': '[00:12:15]',
      'timestamp_seconds': 735,
      'tip': "So, here's how to evaluate if a niche is worth entering. So, search for these "
             "buyer intent keywords in that space. If it's all major media publications, it's "
             'probably too competitive.',
      'title': 'How to ACTUALLY Make Your First $1,000 with High Ticket Affiliate Marketing... '
               'Works in 2026 (Adam Enfroy)',
      'url': 'https://www.youtube.com/watch?v=rv01CKLsaY0&t=735s',
      'video_id': 'rv01CKLsaY0'},
     {'author': 'Ecom Chief',
      'channel': 'Ecom Chief',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:52](https://www.youtube.com/watch?v=iVK1QrJwylk&t=112s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': 'Maximizing ROI or return on investment requires active management. By '
              'continuously updating tool reviews to reflect new features and pricing, you '
              'capture high intent search traffic as the fast-moving AI market evolves.',
      'timestamp': 112,
      'timestamp_label': '[00:01:52]',
      'timestamp_seconds': 112,
      'tip': 'Maximizing ROI or return on investment requires active management. By '
             'continuously updating tool reviews to reflect new features and pricing, you '
             'capture high intent search traffic as the fast-moving AI market evolves.',
      'title': 'How to Buy and Grow an AI Affiliate Website in 2026 (High-Ticket SaaS '
               'Commissions) (Ecom Chief)',
      'url': 'https://www.youtube.com/watch?v=iVK1QrJwylk&t=112s',
      'video_id': 'iVK1QrJwylk'},
     {'author': 'Rank Math SEO',
      'channel': 'Rank Math SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:39](https://www.youtube.com/watch?v=wO28FZWmVwE&t=159s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': "If you don't understand the intent of the keyword, you can simply copy it. For "
              'example, aircon servicing Singapore. Then go to Google and search for the '
              'keyword. As you scroll down, take note of the keywords in the people also '
              'search for section.',
      'timestamp': 159,
      'timestamp_label': '[00:02:39]',
      'timestamp_seconds': 159,
      'tip': "If you don't understand the intent of the keyword, you can simply copy it. For "
             'example, aircon servicing Singapore. Then go to Google and search for the '
             'keyword. As you scroll down, take note of the keywords in the people also search '
             'for section.',
      'title': 'The 2027 SEO & GEO Checklist (What Your Site Might Be Missing) (Rank Math SEO)',
      'url': 'https://www.youtube.com/watch?v=wO28FZWmVwE&t=159s',
      'video_id': 'wO28FZWmVwE'},
     {'author': 'WordsAtScale',
      'channel': 'WordsAtScale',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:35](https://www.youtube.com/watch?v=DJFaYJ3O7aU&t=395s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': 'How members rank new pages in 24 to 48 hours. One more thing, premium members '
              'at $47 a month now get two of my own tools, the state dominator which finds '
              'demand for rank and rank niches and ICP keywords, the keyword research tool I '
              'built for myself.',
      'timestamp': 395,
      'timestamp_label': '[00:06:35]',
      'timestamp_seconds': 395,
      'tip': 'How members rank new pages in 24 to 48 hours. One more thing, premium members at '
             '$47 a month now get two of my own tools, the state dominator which finds demand '
             'for rank and rank niches and ICP keywords, the keyword research tool I built for '
             'myself.',
      'title': 'Pay Per Call Marketing: Sell Your Rank and Rent Calls (You Never Talk to the '
               'Business) (WordsAtScale)',
      'url': 'https://www.youtube.com/watch?v=DJFaYJ3O7aU&t=395s',
      'video_id': 'DJFaYJ3O7aU'},
     {'author': 'Khris Steven',
      'channel': 'Khris Steven',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:32](https://www.youtube.com/watch?v=-C4gk3OAfmk&t=512s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': 'Then you can also do Workday alternative. So, these are like content ideas for '
              'small business. You can also do for small business or you can also do um cover '
              'Deal pricing. So, you can do the pricing, you can do the Deal review.',
      'timestamp': 512,
      'timestamp_label': '[00:08:32]',
      'timestamp_seconds': 512,
      'tip': 'Then you can also do Workday alternative. So, these are like content ideas for '
             'small business. You can also do for small business or you can also do um cover '
             'Deal pricing. So, you can do the pricing, you can do the Deal review.',
      'title': 'PartnerStack Affiliate Walkthrough: Finding Offers + My $3K Withdrawal (Khris '
               'Steven)',
      'url': 'https://www.youtube.com/watch?v=-C4gk3OAfmk&t=512s',
      'video_id': '-C4gk3OAfmk'},
     {'author': 'The Grow and Convert Marketing Show',
      'channel': 'The Grow and Convert Marketing Show',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:39](https://www.youtube.com/watch?v=ZciLGXWg1uA&t=219s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': "So if you're really new to Grow and Convert, our whole thesis is that we go "
              'after. SEO keywords that are at the bottom of the funnel, meaning the act of '
              'Googling the keyword has buying intent.',
      'timestamp': 219,
      'timestamp_label': '[00:03:39]',
      'timestamp_seconds': 219,
      'tip': "So if you're really new to Grow and Convert, our whole thesis is that we go "
             'after. SEO keywords that are at the bottom of the funnel, meaning the act of '
             'Googling the keyword has buying intent.',
      'title': 'How to Create Comparison Content (Without Making Your CEO Nervous): A Data '
               'Backed Approach (The Grow and Convert Marketing Show)',
      'url': 'https://www.youtube.com/watch?v=ZciLGXWg1uA&t=219s',
      'video_id': 'ZciLGXWg1uA'},
     {'author': 'Rob Hoffman',
      'channel': 'Rob Hoffman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:07](https://www.youtube.com/watch?v=mPeQxVCunPU&t=67s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': 'And what I mean is the first type of keyword would be your competitor and then '
              'the word alternatives. The second type would be the name of your competitor and '
              'then the word review. And then the third would be your competitor versus '
              'another competitor.',
      'timestamp': 67,
      'timestamp_label': '[00:01:07]',
      'timestamp_seconds': 67,
      'tip': 'And what I mean is the first type of keyword would be your competitor and then '
             'the word alternatives. The second type would be the name of your competitor and '
             'then the word review. And then the third would be your competitor versus another '
             'competitor.',
      'title': "Copy This Al SEO Strategy, It'll Blow Up Your Business (Rob Hoffman)",
      'url': 'https://www.youtube.com/watch?v=mPeQxVCunPU&t=67s',
      'video_id': 'mPeQxVCunPU'},
     {'author': 'Beach Bum University',
      'channel': 'Beach Bum University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:52](https://www.youtube.com/watch?v=fMKmS-H3tBg&t=412s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': 'YouTube uh with affiliate terms, cookies, all that stuff, right? Um high intent '
              "keyword search worth owning. It's talking about BBU Beach University. But "
              "here's what people are searching. Go high level, Get Response, Beehive, Kit, "
              'Lead Pages, ClickFunnels, right?',
      'timestamp': 412,
      'timestamp_label': '[00:06:52]',
      'timestamp_seconds': 412,
      'tip': 'YouTube uh with affiliate terms, cookies, all that stuff, right? Um high intent '
             "keyword search worth owning. It's talking about BBU Beach University. But here's "
             'what people are searching. Go high level, Get Response, Beehive, Kit, Lead '
             'Pages, ClickFunnels, right?',
      'title': "Best SaaS for Recurring Affiliate Commissions? Here's How to Find Them... "
               '(Beach Bum University)',
      'url': 'https://www.youtube.com/watch?v=fMKmS-H3tBg&t=412s',
      'video_id': 'fMKmS-H3tBg'},
     {'author': 'Beginner to 1K a Day Journey',
      'channel': 'Beginner to 1K a Day Journey',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=HhGv4y6TrXs&t=108s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': "I'm sharing everything everything I have done so I can hit these numbers. I "
              'includes how to run ads, includes how to um to take care about the keywords, '
              "the headlines, the descriptions, everything. Everything's including this method "
              'or this strategy or this mentorship.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': "I'm sharing everything everything I have done so I can hit these numbers. I "
             'includes how to run ads, includes how to um to take care about the keywords, the '
             "headlines, the descriptions, everything. Everything's including this method or "
             'this strategy or this mentorship.',
      'title': 'HIT $5,000 EVERY WEEK FOR 24 WEEKS STRAIGHT! MARKETCALL (PAY PER CALL) '
               '(Beginner to 1K a Day Journey)',
      'url': 'https://www.youtube.com/watch?v=HhGv4y6TrXs&t=108s',
      'video_id': 'HhGv4y6TrXs'},
     {'author': 'Vasco Aires',
      'channel': 'Vasco Aires',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:01](https://www.youtube.com/watch?v=C2ne_saHpSs&t=1501s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': "'s a good thing to just not send traffic to them. Then of course optimize for "
              'alternative search terms, right? Well, what competitor one is and then in-depth '
              "alternatives uh of of all the competitors. And that's what we do as well. Here "
              'again, I showed you before, right?',
      'timestamp': 1501,
      'timestamp_label': '[00:25:01]',
      'timestamp_seconds': 1501,
      'tip': "'s a good thing to just not send traffic to them. Then of course optimize for "
             'alternative search terms, right? Well, what competitor one is and then in-depth '
             "alternatives uh of of all the competitors. And that's what we do as well. Here "
             'again, I showed you before, right?',
      'title': 'SaaS SEO Strategy - How I make $4,000/day with a SaaS (Vasco Aires)',
      'url': 'https://www.youtube.com/watch?v=C2ne_saHpSs&t=1501s',
      'video_id': 'C2ne_saHpSs'},
     {'author': 'Asghar Speaks',
      'channel': 'Asghar Speaks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:43](https://www.youtube.com/watch?v=r74nmdjWZ88&t=343s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': "Now let's talk about the publishers. See, the publishers 'job is to generate "
              'calls. Now, to generate calls, there are various sources. You can post ads '
              'there to generate calls. Facebook Meta, where you can run paid ads and generate '
              'calls. Besides that, there are websites.',
      'timestamp': 343,
      'timestamp_label': '[00:05:43]',
      'timestamp_seconds': 343,
      'tip': "Now let's talk about the publishers. See, the publishers 'job is to generate "
             'calls. Now, to generate calls, there are various sources. You can post ads there '
             'to generate calls. Facebook Meta, where you can run paid ads and generate calls. '
             'Besides that, there are websites.',
      'title': 'Pay Per Call Complete Course 2026 | Ringba Tutorial | Pay Per Call  | Beginner '
               'to Advanced 2026 (Asghar Speaks)',
      'url': 'https://www.youtube.com/watch?v=r74nmdjWZ88&t=343s',
      'video_id': 'r74nmdjWZ88'},
     {'author': 'Alex COLLINSEO',
      'channel': 'Alex COLLINSEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=MzA9HXeEoMA&t=20s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': "SEO strategy, and how to execute it step by step. The first strategy we're "
              "going to do is competitor plus alternative. It's my favorite one because we're "
              'getting traffic from competitors to our website.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "SEO strategy, and how to execute it step by step. The first strategy we're going "
             "to do is competitor plus alternative. It's my favorite one because we're getting "
             'traffic from competitors to our website.',
      'title': 'How To Outrank Your Competitors Using “Alternative” Keyword Pages (Alex '
               'COLLINSEO)',
      'url': 'https://www.youtube.com/watch?v=MzA9HXeEoMA&t=20s',
      'video_id': 'MzA9HXeEoMA'},
     {'author': 'ToolTester Pro',
      'channel': 'ToolTester Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:59](https://www.youtube.com/watch?v=boGwMjAxtuk&t=659s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': 'Do they lead with examples or with explanation? What does it give you in the '
              "first screen? This bit I wouldn't bother with. Then search that same term in "
              "Google and look what's actually being searched. What you are reading here is "
              'intent.',
      'timestamp': 659,
      'timestamp_label': '[00:10:59]',
      'timestamp_seconds': 659,
      'tip': 'Do they lead with examples or with explanation? What does it give you in the '
             "first screen? This bit I wouldn't bother with. Then search that same term in "
             "Google and look what's actually being searched. What you are reading here is "
             'intent.',
      'title': 'How to Steal Your Competitor’s SEO Strategy in 15 Minutes (Semrush Traffic & '
               'AI Audit) (ToolTester Pro)',
      'url': 'https://www.youtube.com/watch?v=boGwMjAxtuk&t=659s',
      'video_id': 'boGwMjAxtuk'},
     {'author': 'Seeking Profit',
      'channel': 'Seeking Profit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=fo-OxsDnUVQ&t=83s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': "Registered bossy Paws and we started doing keyword research and there's all "
              "these in name like does your cat have this does your cat's piss smell like wine "
              "or whatever like let's skip this one.",
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': "Registered bossy Paws and we started doing keyword research and there's all "
             "these in name like does your cat have this does your cat's piss smell like wine "
             "or whatever like let's skip this one.",
      'title': 'The Formula Behind High-Converting Affiliate Articles (w/Jamie IF) (Seeking '
               'Profit)',
      'url': 'https://www.youtube.com/watch?v=fo-OxsDnUVQ&t=83s',
      'video_id': 'fo-OxsDnUVQ'},
     {'author': 'Ecommerce Paradise | High Ticket Dropshipping',
      'channel': 'Ecommerce Paradise | High Ticket Dropshipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:19](https://www.youtube.com/watch?v=oCSQ3s1mmGQ&t=319s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': 'Um, so that you can integrate your reviews apps and your search app and all '
              'this other stuff into, you know, your affiliate program app for example into '
              'Gem Pages. Um, and they have a lot of different like conversion rate '
              'optimization resources as well in their app.',
      'timestamp': 319,
      'timestamp_label': '[00:05:19]',
      'timestamp_seconds': 319,
      'tip': 'Um, so that you can integrate your reviews apps and your search app and all this '
             'other stuff into, you know, your affiliate program app for example into Gem '
             'Pages. Um, and they have a lot of different like conversion rate optimization '
             'resources as well in their app.',
      'title': 'How to Build a High-Ticket Quote Funnel with GemPages and Claude (Ecommerce '
               'Paradise | High Ticket Dropshipping)',
      'url': 'https://www.youtube.com/watch?v=oCSQ3s1mmGQ&t=319s',
      'video_id': 'oCSQ3s1mmGQ'}],
 7: [{'author': 'Everflow - Partner Marketing Platform',
      'channel': 'Everflow - Partner Marketing Platform',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=2Q-xY6ABqXE&t=114s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': 'Server to server allows them to track delayed conversion events such as lead '
              'reaching the closed one opportunity stage in the CRM, ensuring the partner who '
              'generated the initial click weeks ago receives credit regardless of the '
              'customer browser status.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': 'Server to server allows them to track delayed conversion events such as lead '
             'reaching the closed one opportunity stage in the CRM, ensuring the partner who '
             'generated the initial click weeks ago receives credit regardless of the customer '
             'browser status.',
      'title': 'What is a Server-to-Server (S2S) Postback? | Everflow Mini Webinars (Everflow '
               '- Partner Marketing Platform)',
      'url': 'https://www.youtube.com/watch?v=2Q-xY6ABqXE&t=114s',
      'video_id': '2Q-xY6ABqXE'},
     {'author': 'Alex Cattoni',
      'channel': 'Alex Cattoni',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:11](https://www.youtube.com/watch?v=vC_LEc8pGp8&t=311s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': "And this brings me to the second page that we're talking about today, a landing "
              'page for one of my highest converting lead magnets, my subject line split test '
              'report.',
      'timestamp': 311,
      'timestamp_label': '[00:05:11]',
      'timestamp_seconds': 311,
      'tip': "And this brings me to the second page that we're talking about today, a landing "
             'page for one of my highest converting lead magnets, my subject line split test '
             'report.',
      'title': 'This Landing Page Has A 79% Conversion Rate. Here’s Why It Works… (Alex '
               'Cattoni)',
      'url': 'https://www.youtube.com/watch?v=vC_LEc8pGp8&t=311s',
      'video_id': 'vC_LEc8pGp8'},
     {'author': 'Everflow - Partner Marketing Platform',
      'channel': 'Everflow - Partner Marketing Platform',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=qXMBHCgI3Wk&t=38s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': "ID macro to advertiser's landing page or system. And two, the advertiser "
              'accurately configures the postback URL on their side. This is often found in '
              'the global postback section or specific offer settings to fire the ID back to '
              'Everflow upon conversion.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': "ID macro to advertiser's landing page or system. And two, the advertiser "
             'accurately configures the postback URL on their side. This is often found in the '
             'global postback section or specific offer settings to fire the ID back to '
             'Everflow upon conversion.',
      'title': 'How to Set Up & Test Your Advertiser Postback | Everflow Mini Webinars '
               '(Everflow - Partner Marketing Platform)',
      'url': 'https://www.youtube.com/watch?v=qXMBHCgI3Wk&t=38s',
      'video_id': 'qXMBHCgI3Wk'},
     {'author': 'Atomic Funnels',
      'channel': 'Atomic Funnels',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:50](https://www.youtube.com/watch?v=g1L7iVYbiGs&t=530s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': "And then after we're done with that, we can click and go check out the offer. "
              "So by having all four of these different customer journeys, we're able to "
              'optimize for all three of our conversion goals, serving offers, VSL view '
              'duration, and lead capture.',
      'timestamp': 530,
      'timestamp_label': '[00:08:50]',
      'timestamp_seconds': 530,
      'tip': "And then after we're done with that, we can click and go check out the offer. So "
             "by having all four of these different customer journeys, we're able to optimize "
             'for all three of our conversion goals, serving offers, VSL view duration, and '
             'lead capture.',
      'title': 'Best Sales Funnel for High-Ticket Offers? 4 Types Compared (2026) (Atomic '
               'Funnels)',
      'url': 'https://www.youtube.com/watch?v=g1L7iVYbiGs&t=530s',
      'video_id': 'g1L7iVYbiGs'},
     {'author': 'Jon McNeil',
      'channel': 'Jon McNeil',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:38](https://www.youtube.com/watch?v=U4rN7FuTQGc&t=158s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': "'re going to see your actual bridge page. So, what tends to happen when people "
              'opt in to your squeeze page, those 40 people, everybody that actually sees this '
              "bridge page here, the people that see the bridge page here don't always click "
              'on the link.',
      'timestamp': 158,
      'timestamp_label': '[00:02:38]',
      'timestamp_seconds': 158,
      'tip': "'re going to see your actual bridge page. So, what tends to happen when people "
             'opt in to your squeeze page, those 40 people, everybody that actually sees this '
             "bridge page here, the people that see the bridge page here don't always click on "
             'the link.',
      'title': 'BRIDGE PAGE FUNNEL - (HOW TO INCREASE CONVERSIONS) (Jon McNeil)',
      'url': 'https://www.youtube.com/watch?v=U4rN7FuTQGc&t=158s',
      'video_id': 'U4rN7FuTQGc'},
     {'author': 'PingPost Exchange',
      'channel': 'PingPost Exchange',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:35](https://www.youtube.com/watch?v=u6fnEGbP72s&t=335s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': 'So, as we keep going here, this is if you want to drill down on each lead '
              'itself, what was the behavior between the ping and the post, what the different '
              'buyers their bid responses are, what it sold for, you can drill down to each '
              'specific lead.',
      'timestamp': 335,
      'timestamp_label': '[00:05:35]',
      'timestamp_seconds': 335,
      'tip': 'So, as we keep going here, this is if you want to drill down on each lead '
             'itself, what was the behavior between the ping and the post, what the different '
             'buyers their bid responses are, what it sold for, you can drill down to each '
             'specific lead.',
      'title': 'Ping Post Exchange Introduction - Lead Generation (PingPost Exchange)',
      'url': 'https://www.youtube.com/watch?v=u6fnEGbP72s&t=335s',
      'video_id': 'u6fnEGbP72s'},
     {'author': 'Jayant Padhi',
      'channel': 'Jayant Padhi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:48](https://www.youtube.com/watch?v=wj29osNl-zE&t=348s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': 'That I can use in my landing page and basically we test which headline works '
              'the best and tended different headlines to put on the VSL page here as you can '
              'see Chad GPT 4 is definitely not something that you should lose out on and and '
              'if you want all the scripts.',
      'timestamp': 348,
      'timestamp_label': '[00:05:48]',
      'timestamp_seconds': 348,
      'tip': 'That I can use in my landing page and basically we test which headline works the '
             'best and tended different headlines to put on the VSL page here as you can see '
             'Chad GPT 4 is definitely not something that you should lose out on and and if '
             'you want all the scripts.',
      'title': 'I used ChatGPT4 to build a high ticket funnel (Jayant Padhi)',
      'url': 'https://www.youtube.com/watch?v=wj29osNl-zE&t=348s',
      'video_id': 'wj29osNl-zE'},
     {'author': 'boberdoo.com',
      'channel': 'boberdoo.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:08](https://www.youtube.com/watch?v=SZ3UyKpdEjg&t=128s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': 'Well which will allow them to ping into your lead distribution system now when '
              "you're in the specific settings there are several different several different "
              'options so you see we set up a test one that is for dynamic pricing so what '
              'this would be is allows.',
      'timestamp': 128,
      'timestamp_label': '[00:02:08]',
      'timestamp_seconds': 128,
      'tip': 'Well which will allow them to ping into your lead distribution system now when '
             "you're in the specific settings there are several different several different "
             'options so you see we set up a test one that is for dynamic pricing so what this '
             'would be is allows.',
      'title': 'Ping Post Basics Webinar | boberdoo Ping Post Software (boberdoo.com)',
      'url': 'https://www.youtube.com/watch?v=SZ3UyKpdEjg&t=128s',
      'video_id': 'SZ3UyKpdEjg'},
     {'author': 'vanel sylvestre',
      'channel': 'vanel sylvestre',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:01](https://www.youtube.com/watch?v=a32vgNX3Qkw&t=181s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': 'Facebook, as you can see right here. Uh I go on Facebook and I type something '
              'like American Airline complain like this. And I join some group like this and '
              'post my landing page and get paid whenever I do that. So, guys, this is how I '
              'do it. Anyone can do the same thing.',
      'timestamp': 181,
      'timestamp_label': '[00:03:01]',
      'timestamp_seconds': 181,
      'tip': 'Facebook, as you can see right here. Uh I go on Facebook and I type something '
             'like American Airline complain like this. And I join some group like this and '
             'post my landing page and get paid whenever I do that. So, guys, this is how I do '
             'it. Anyone can do the same thing.',
      'title': "I Made $14,000 With Pay Per Call Affiliate Marketing (Here's Exactly How!) "
               '(vanel sylvestre)',
      'url': 'https://www.youtube.com/watch?v=a32vgNX3Qkw&t=181s',
      'video_id': 'a32vgNX3Qkw'},
     {'author': 'Rank Math SEO',
      'channel': 'Rank Math SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:34](https://www.youtube.com/watch?v=wO28FZWmVwE&t=394s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': 'You see, these are the internal links and anchor tags it recommends. And as you '
              'click on this, the link will be added to the page. You can also utilize the '
              'related post feature to find other pages to add. Give it a while, and it will '
              'recommend some posts for you to add.',
      'timestamp': 394,
      'timestamp_label': '[00:06:34]',
      'timestamp_seconds': 394,
      'tip': 'You see, these are the internal links and anchor tags it recommends. And as you '
             'click on this, the link will be added to the page. You can also utilize the '
             'related post feature to find other pages to add. Give it a while, and it will '
             'recommend some posts for you to add.',
      'title': 'The 2027 SEO & GEO Checklist (What Your Site Might Be Missing) (Rank Math SEO)',
      'url': 'https://www.youtube.com/watch?v=wO28FZWmVwE&t=394s',
      'video_id': 'wO28FZWmVwE'},
     {'author': 'Rafael Hernandez ⚡️',
      'channel': 'Rafael Hernandez ⚡️',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=A_xXkLg_0xI&t=55s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': "So, here's the agency owner. You deliver the lead to your buyer. Buyer pays you "
              "and that's it, right? 90% of paper lead agencies have never even heard of or "
              'even dabbled in ping post.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': "So, here's the agency owner. You deliver the lead to your buyer. Buyer pays you "
             "and that's it, right? 90% of paper lead agencies have never even heard of or "
             'even dabbled in ping post.',
      'title': 'The Ping Post Secret — Why PPL Agencies Are Leaving Thousands on the Table '
               '(Rafael Hernandez ⚡️)',
      'url': 'https://www.youtube.com/watch?v=A_xXkLg_0xI&t=55s',
      'video_id': 'A_xXkLg_0xI'},
     {'author': 'LeadByte',
      'channel': 'LeadByte',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=NYSR6kFlcI8&t=64s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': 'Click on the test URL you can see here this is just a test site you can see '
              'here we decided to pass in the everflow transaction ID into the source field so '
              'when we submit a lead the source value so the transaction ID will be submitted '
              'into lead.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': 'Click on the test URL you can see here this is just a test site you can see here '
             'we decided to pass in the everflow transaction ID into the source field so when '
             'we submit a lead the source value so the transaction ID will be submitted into '
             'lead.',
      'title': 'Tracking Leads Sold in Everflow (LeadByte)',
      'url': 'https://www.youtube.com/watch?v=NYSR6kFlcI8&t=64s',
      'video_id': 'NYSR6kFlcI8'},
     {'author': 'Jamie McAdam',
      'channel': 'Jamie McAdam',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:31](https://www.youtube.com/watch?v=khf473ZL71w&t=151s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': 'So, this is page one, your opt-in page. This is where cold traffic comes and '
              "they become a lead. You're going to sell the outcome. And you're also going to "
              'hint at the mechanism.',
      'timestamp': 151,
      'timestamp_label': '[00:02:31]',
      'timestamp_seconds': 151,
      'tip': 'So, this is page one, your opt-in page. This is where cold traffic comes and '
             "they become a lead. You're going to sell the outcome. And you're also going to "
             'hint at the mechanism.',
      'title': 'The 4-Page VSL Funnel For $5K High Ticket Programs (Jamie McAdam)',
      'url': 'https://www.youtube.com/watch?v=khf473ZL71w&t=151s',
      'video_id': 'khf473ZL71w'},
     {'author': 'Carlos Corona',
      'channel': 'Carlos Corona',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:36](https://www.youtube.com/watch?v=zOQZw8jApe0&t=1776s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': 'Flow and then what you can do also is follow the guide which I posted there and '
              "if you're watching from YouTube or my Facebook page I posted there the guide "
              "but for those that want to um I can't see it the link give me a second and let "
              'me share it real quick.',
      'timestamp': 1776,
      'timestamp_label': '[00:29:36]',
      'timestamp_seconds': 1776,
      'tip': 'Flow and then what you can do also is follow the guide which I posted there and '
             "if you're watching from YouTube or my Facebook page I posted there the guide but "
             "for those that want to um I can't see it the link give me a second and let me "
             'share it real quick.',
      'title': 'Pay Per Call: How to configure your Everflow postback to track FB conversion '
               'pixels (Carlos Corona)',
      'url': 'https://www.youtube.com/watch?v=zOQZw8jApe0&t=1776s',
      'video_id': 'zOQZw8jApe0'},
     {'author': 'subscribe if i helped you :)',
      'channel': 'subscribe if i helped you :)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:56](https://www.youtube.com/watch?v=rKrC1mctap4&t=176s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': "Now, once you're on this page, you basically want to click on the sign up and "
              'start earning option. You can see you can sign up with your email, Google X, or '
              'any of these other applications.',
      'timestamp': 176,
      'timestamp_label': '[00:02:56]',
      'timestamp_seconds': 176,
      'tip': "Now, once you're on this page, you basically want to click on the sign up and "
             'start earning option. You can see you can sign up with your email, Google X, or '
             'any of these other applications.',
      'title': 'How Does Impact.com Work? | How To Make Money With Impact.com (subscribe if i '
               'helped you :))',
      'url': 'https://www.youtube.com/watch?v=rKrC1mctap4&t=176s',
      'video_id': 'rKrC1mctap4'}],
 8: [{'author': 'Rank Math SEO',
      'channel': 'Rank Math SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:16](https://www.youtube.com/watch?v=wO28FZWmVwE&t=496s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'You can also ask, what do customers always complain about your business? Find '
              'out how your business is performing on AI overview and take note of the '
              'reference sources. Go to ChatGPT, Perplexity, and Claude to ask the same '
              'question.',
      'timestamp': 496,
      'timestamp_label': '[00:08:16]',
      'timestamp_seconds': 496,
      'tip': 'You can also ask, what do customers always complain about your business? Find '
             'out how your business is performing on AI overview and take note of the '
             'reference sources. Go to ChatGPT, Perplexity, and Claude to ask the same '
             'question.',
      'title': 'The 2027 SEO & GEO Checklist (What Your Site Might Be Missing) (Rank Math SEO)',
      'url': 'https://www.youtube.com/watch?v=wO28FZWmVwE&t=496s',
      'video_id': 'wO28FZWmVwE'},
     {'author': 'The Infamous Joel',
      'channel': 'The Infamous Joel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:13](https://www.youtube.com/watch?v=YVPPIdIHYpo&t=313s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': "Everything's going AI, so everybody's selling AI stuff. And this one "
              'specifically is for for the tool called OpenClaw. Now, I did watch a little bit '
              "of what this guy's talking about. Again, I'm like, I've seen so many of these "
              'things. I watch them in the background.',
      'timestamp': 313,
      'timestamp_label': '[00:05:13]',
      'timestamp_seconds': 313,
      'tip': "Everything's going AI, so everybody's selling AI stuff. And this one "
             'specifically is for for the tool called OpenClaw. Now, I did watch a little bit '
             "of what this guy's talking about. Again, I'm like, I've seen so many of these "
             'things. I watch them in the background.',
      'title': '20 High-Ticket Affiliate Programs to Find $1K Commissions (The Infamous Joel)',
      'url': 'https://www.youtube.com/watch?v=YVPPIdIHYpo&t=313s',
      'video_id': 'YVPPIdIHYpo'},
     {'author': 'Mr. Money',
      'channel': 'Mr. Money',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:49](https://www.youtube.com/watch?v=VHaXNPiHd6Q&t=469s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'Few clicks and you scrape all the leads you need. They have free trial which '
              'you can just use right now to see whether this is for you or not. And from '
              "there, it's a onetime payment. It is basically an extension which works like "
              'this on Google Chrome.',
      'timestamp': 469,
      'timestamp_label': '[00:07:49]',
      'timestamp_seconds': 469,
      'tip': 'Few clicks and you scrape all the leads you need. They have free trial which you '
             'can just use right now to see whether this is for you or not. And from there, '
             "it's a onetime payment. It is basically an extension which works like this on "
             'Google Chrome.',
      'title': 'How To Make Money With Partnerstack Affiliate Marketing in 2026 (Mr. Money)',
      'url': 'https://www.youtube.com/watch?v=VHaXNPiHd6Q&t=469s',
      'video_id': 'VHaXNPiHd6Q'},
     {'author': 'Vasco Aires',
      'channel': 'Vasco Aires',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:01](https://www.youtube.com/watch?v=C2ne_saHpSs&t=181s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'Um, yeah, regardless, I mean, it ranks for a bunch of relevant keywords for '
              "adding subtitles to videos because that's exactly what this uh this tool does. "
              'But the most interesting thing right here is if you just remove this and go to '
              'for/tools, right?',
      'timestamp': 181,
      'timestamp_label': '[00:03:01]',
      'timestamp_seconds': 181,
      'tip': 'Um, yeah, regardless, I mean, it ranks for a bunch of relevant keywords for '
             "adding subtitles to videos because that's exactly what this uh this tool does. "
             'But the most interesting thing right here is if you just remove this and go to '
             'for/tools, right?',
      'title': 'SaaS SEO Strategy - How I make $4,000/day with a SaaS (Vasco Aires)',
      'url': 'https://www.youtube.com/watch?v=C2ne_saHpSs&t=181s',
      'video_id': 'C2ne_saHpSs'},
     {'author': 'Automate & Chill By Abhishek Sood',
      'channel': 'Automate & Chill By Abhishek Sood',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:28](https://www.youtube.com/watch?v=g7SAWXINXDo&t=208s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'From that address , you can extract the micro-niche. From that address, you can '
              'extract the neighborhood of the micro-niche and a micro-service. So, this '
              "dashboard of PaperCall, with Ringba, doesn't just provide earnings data.",
      'timestamp': 208,
      'timestamp_label': '[00:03:28]',
      'timestamp_seconds': 208,
      'tip': 'From that address , you can extract the micro-niche. From that address, you can '
             'extract the neighborhood of the micro-niche and a micro-service. So, this '
             "dashboard of PaperCall, with Ringba, doesn't just provide earnings data.",
      'title': 'LeadSmart Pay Per Call Affiliate Approval & How to get trackable phone number '
               'from Ringba (Automate & Chill By Abhishek Sood)',
      'url': 'https://www.youtube.com/watch?v=g7SAWXINXDo&t=208s',
      'video_id': 'g7SAWXINXDo'},
     {'author': 'ToolTester Pro',
      'channel': 'ToolTester Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:14](https://www.youtube.com/watch?v=boGwMjAxtuk&t=974s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'You get a set number of free searches a day for sizing up one competitor and '
              'working out where to point your next few posts, completely good with the free '
              'tool.',
      'timestamp': 974,
      'timestamp_label': '[00:16:14]',
      'timestamp_seconds': 974,
      'tip': 'You get a set number of free searches a day for sizing up one competitor and '
             'working out where to point your next few posts, completely good with the free '
             'tool.',
      'title': 'How to Steal Your Competitor’s SEO Strategy in 15 Minutes (Semrush Traffic & '
               'AI Audit) (ToolTester Pro)',
      'url': 'https://www.youtube.com/watch?v=boGwMjAxtuk&t=974s',
      'video_id': 'boGwMjAxtuk'},
     {'author': 'Alex Cattoni',
      'channel': 'Alex Cattoni',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=vC_LEc8pGp8&t=88s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'Now, I recently pulled the data for this offer specifically. And as you can see '
              'here in Google Analytics, this page has had a total of 7222 unique visitors '
              'over the last 10 months. And according to my Kajabi account, a total of 1035 '
              'sales in that exact same period.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'Now, I recently pulled the data for this offer specifically. And as you can see '
             'here in Google Analytics, this page has had a total of 7222 unique visitors over '
             'the last 10 months. And according to my Kajabi account, a total of 1035 sales in '
             'that exact same period.',
      'title': 'This Landing Page Has A 79% Conversion Rate. Here’s Why It Works… (Alex '
               'Cattoni)',
      'url': 'https://www.youtube.com/watch?v=vC_LEc8pGp8&t=88s',
      'video_id': 'vC_LEc8pGp8'},
     {'author': 'Asghar Speaks',
      'channel': 'Asghar Speaks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:11](https://www.youtube.com/watch?v=r74nmdjWZ88&t=191s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': "Now, let's talk about Ringba; what exactly is Ringba? See, it's not like you "
              'just create an account on Ringba or sign up and start earning immediately. '
              'Ringba is just a call tracker. If you go to Ringba and sign up, they have '
              'plans.',
      'timestamp': 191,
      'timestamp_label': '[00:03:11]',
      'timestamp_seconds': 191,
      'tip': "Now, let's talk about Ringba; what exactly is Ringba? See, it's not like you "
             'just create an account on Ringba or sign up and start earning immediately. '
             'Ringba is just a call tracker. If you go to Ringba and sign up, they have plans.',
      'title': 'Pay Per Call Complete Course 2026 | Ringba Tutorial | Pay Per Call  | Beginner '
               'to Advanced 2026 (Asghar Speaks)',
      'url': 'https://www.youtube.com/watch?v=r74nmdjWZ88&t=191s',
      'video_id': 'r74nmdjWZ88'},
     {'author': 'Daniel | Tech & Data',
      'channel': 'Daniel | Tech & Data',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:14](https://www.youtube.com/watch?v=SWQet1wMMyA&t=254s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'Now, something else worth mentioning here is the new AI assistant feature '
              "inside FirstPromoter. At the moment, this tool is still experimental, so it's "
              'better viewed as an early workflow assistant rather than a fully mature '
              'automation system.',
      'timestamp': 254,
      'timestamp_label': '[00:04:14]',
      'timestamp_seconds': 254,
      'tip': 'Now, something else worth mentioning here is the new AI assistant feature inside '
             "FirstPromoter. At the moment, this tool is still experimental, so it's better "
             'viewed as an early workflow assistant rather than a fully mature automation '
             'system.',
      'title': 'FirstPromoter Review - 2026 | The Easiest Way to Run a SaaS Affiliate Program? '
               '(Daniel | Tech & Data)',
      'url': 'https://www.youtube.com/watch?v=SWQet1wMMyA&t=254s',
      'video_id': 'SWQet1wMMyA'},
     {'author': 'ClickFlare',
      'channel': 'ClickFlare',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:58](https://www.youtube.com/watch?v=cSLdoNWYxfE&t=58s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'That means tracking accurate events, passing proper parameters and feeding the '
              'Meta pixel with clean, consistent data. So your pixel score improves and your '
              'campaign scale more efficiently.',
      'timestamp': 58,
      'timestamp_label': '[00:00:58]',
      'timestamp_seconds': 58,
      'tip': 'That means tracking accurate events, passing proper parameters and feeding the '
             'Meta pixel with clean, consistent data. So your pixel score improves and your '
             'campaign scale more efficiently.',
      'title': 'How To Track Everflow and Meta For Advanced Affiliate Marketing (ClickFlare)',
      'url': 'https://www.youtube.com/watch?v=cSLdoNWYxfE&t=58s',
      'video_id': 'cSLdoNWYxfE'},
     {'author': 'The Grow and Convert Marketing Show',
      'channel': 'The Grow and Convert Marketing Show',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:00](https://www.youtube.com/watch?v=ZciLGXWg1uA&t=420s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'So I just typed DocuSign Alternatives. I was not a customer of DocuSign, but I '
              "just knew them because they're the brand leader in the space. But the "
              "conversion point you're making stands, which is. I was very much at the bottom "
              'of the funnel, like we needed a tool.',
      'timestamp': 420,
      'timestamp_label': '[00:07:00]',
      'timestamp_seconds': 420,
      'tip': 'So I just typed DocuSign Alternatives. I was not a customer of DocuSign, but I '
             "just knew them because they're the brand leader in the space. But the conversion "
             "point you're making stands, which is. I was very much at the bottom of the "
             'funnel, like we needed a tool.',
      'title': 'How to Create Comparison Content (Without Making Your CEO Nervous): A Data '
               'Backed Approach (The Grow and Convert Marketing Show)',
      'url': 'https://www.youtube.com/watch?v=ZciLGXWg1uA&t=420s',
      'video_id': 'ZciLGXWg1uA'},
     {'author': 'Rob Hoffman',
      'channel': 'Rob Hoffman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:19](https://www.youtube.com/watch?v=mPeQxVCunPU&t=259s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': "And you can also see that they're ranking number one here in Google. Our client "
              "Beehive is another example where they're showing up number one right here for "
              "Kit alternatives or our client Teamwork Town who's showing up number one for "
              'Many Pixels alternatives.',
      'timestamp': 259,
      'timestamp_label': '[00:04:19]',
      'timestamp_seconds': 259,
      'tip': "And you can also see that they're ranking number one here in Google. Our client "
             "Beehive is another example where they're showing up number one right here for "
             "Kit alternatives or our client Teamwork Town who's showing up number one for "
             'Many Pixels alternatives.',
      'title': "Copy This Al SEO Strategy, It'll Blow Up Your Business (Rob Hoffman)",
      'url': 'https://www.youtube.com/watch?v=mPeQxVCunPU&t=259s',
      'video_id': 'mPeQxVCunPU'},
     {'author': 'Rob Reece',
      'channel': 'Rob Reece',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:47](https://www.youtube.com/watch?v=5QOU-NXPWw4&t=407s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'And if you want to know the words that make people actually call or buy, grab '
              'my free AI word list down below. This is Rob Reese with End the Lab. Thanks for '
              "checking out this experiment, and I'll see you next time.",
      'timestamp': 407,
      'timestamp_label': '[00:06:47]',
      'timestamp_seconds': 407,
      'tip': 'And if you want to know the words that make people actually call or buy, grab my '
             'free AI word list down below. This is Rob Reese with End the Lab. Thanks for '
             "checking out this experiment, and I'll see you next time.",
      'title': 'RHIMS 10 Pay-Per-Call Explained (Make Money Selling Phone Calls) (Rob Reece)',
      'url': 'https://www.youtube.com/watch?v=5QOU-NXPWw4&t=407s',
      'video_id': '5QOU-NXPWw4'},
     {'author': 'AffiliateStrat',
      'channel': 'AffiliateStrat',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:04](https://www.youtube.com/watch?v=Z_YllaXsWGA&t=844s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': "'s really not difficult to navigate, figure out your way in and out, figure out "
              "how to run reports and and do everything that you're going to want to do. Um, "
              "it's made as simple as possible despite being heavily data driven.",
      'timestamp': 844,
      'timestamp_label': '[00:14:04]',
      'timestamp_seconds': 844,
      'tip': "'s really not difficult to navigate, figure out your way in and out, figure out "
             "how to run reports and and do everything that you're going to want to do. Um, "
             "it's made as simple as possible despite being heavily data driven.",
      'title': 'Everflow Review & Guide: Full Platform Walkthrough, Pros, Cons, and Real Demos '
               '(AffiliateStrat)',
      'url': 'https://www.youtube.com/watch?v=Z_YllaXsWGA&t=844s',
      'video_id': 'Z_YllaXsWGA'},
     {'author': 'ToThePoint Guide',
      'channel': 'ToThePoint Guide',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:00](https://www.youtube.com/watch?v=fAqhUrhwABs&t=240s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': "And then you're going to have a like deal, hire the best 150 countries without "
              'worrying about compliance, payroll, or HR admin. So the question you can even '
              'ask AI, okay, what kind of videos I can know directly make to promote a deal?',
      'timestamp': 240,
      'timestamp_label': '[00:04:00]',
      'timestamp_seconds': 240,
      'tip': "And then you're going to have a like deal, hire the best 150 countries without "
             'worrying about compliance, payroll, or HR admin. So the question you can even '
             'ask AI, okay, what kind of videos I can know directly make to promote a deal?',
      'title': 'PartnerStack Tutorial 2026 | How to Use & Promote PartnerStack Affiliate for '
               'Beginners (ToThePoint Guide)',
      'url': 'https://www.youtube.com/watch?v=fAqhUrhwABs&t=240s',
      'video_id': 'fAqhUrhwABs'}],
 9: [{'author': 'Bens Review Videos',
      'channel': 'Bens Review Videos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:29](https://www.youtube.com/watch?v=eqw-Rqw7PNY&t=209s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'The AI rebuilds the page in the old look, with the old logo removed. It adds a '
              'sticky call banner for mobile and a disclosure that the site is independently '
              'operated. Two more prompts write the privacy and terms pages.',
      'timestamp': 209,
      'timestamp_label': '[00:03:29]',
      'timestamp_seconds': 209,
      'tip': 'The AI rebuilds the page in the old look, with the old logo removed. It adds a '
             'sticky call banner for mobile and a disclosure that the site is independently '
             'operated. Two more prompts write the privacy and terms pages.',
      'title': 'RHIMS 10 Review: Pay Per Call Affiliate Marketing for Beginners, Expired '
               'Domains + 3 Bonuses (Bens Review Videos)',
      'url': 'https://www.youtube.com/watch?v=eqw-Rqw7PNY&t=209s',
      'video_id': 'eqw-Rqw7PNY'},
     {'author': 'Smart Capital',
      'channel': 'Smart Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:25](https://www.youtube.com/watch?v=LBA0vmJPE5w&t=445s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'So, the content has to be honest, including the downsides. One approach people '
              'use is to list three genuine drawbacks of every tool they recommend. Because a '
              'review with no negatives reads like an advertisement and the law requires '
              'disclosure.',
      'timestamp': 445,
      'timestamp_label': '[00:07:25]',
      'timestamp_seconds': 445,
      'tip': 'So, the content has to be honest, including the downsides. One approach people '
             'use is to list three genuine drawbacks of every tool they recommend. Because a '
             'review with no negatives reads like an advertisement and the law requires '
             'disclosure.',
      'title': 'B2B Software Affiliate Programs: How to Earn Recurring Commissions in 2026 '
               '(Smart Capital)',
      'url': 'https://www.youtube.com/watch?v=LBA0vmJPE5w&t=445s',
      'video_id': 'LBA0vmJPE5w'},
     {'author': 'Rabbit Hole Radio',
      'channel': 'Rabbit Hole Radio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=vvzOZL0NXKI&t=21s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'It is a staggering reality check, honestly. I mean, you have this industry that '
              'is projected to hit a $17 billion global valuation by the end of 2026. And the '
              'biggest players in the space are basically building these massive empires on a '
              'foundation of legal non-compliance.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'It is a staggering reality check, honestly. I mean, you have this industry that '
             'is projected to hit a $17 billion global valuation by the end of 2026. And the '
             'biggest players in the space are basically building these massive empires on a '
             'foundation of legal non-compliance.',
      'title': 'The 2026 High Ticket Affiliate Blueprint (Rabbit Hole Radio)',
      'url': 'https://www.youtube.com/watch?v=vvzOZL0NXKI&t=21s',
      'video_id': 'vvzOZL0NXKI'},
     {'author': 'Traffic Cardinal EN — Affiliate Press',
      'channel': 'Traffic Cardinal EN — Affiliate Press',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:13](https://www.youtube.com/watch?v=caUORKmsfnU&t=613s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': "There's always like the main ones like LinkedIn, uh, Medium, Vocal Media is "
              "good and there's a new Reddit is ranking for pretty much everything which is "
              'like the the big one which everyone uses all the time.',
      'timestamp': 613,
      'timestamp_label': '[00:10:13]',
      'timestamp_seconds': 613,
      'tip': "There's always like the main ones like LinkedIn, uh, Medium, Vocal Media is good "
             "and there's a new Reddit is ranking for pretty much everything which is like the "
             'the big one which everyone uses all the time.',
      'title': 'The SEO Strategy Google Can’t Kill — James Oliver Explains Parasite SEO '
               '(Traffic Cardinal EN — Affiliate Press)',
      'url': 'https://www.youtube.com/watch?v=caUORKmsfnU&t=613s',
      'video_id': 'caUORKmsfnU'},
     {'author': 'KudaOnline',
      'channel': 'KudaOnline',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=EUQ9OfMYDnw&t=80s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'Future trend we will beat you will be looking at now let us look at an overview '
              'affiliate marketing is conffiliate you alsation why you need to have compliance '
              'et.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': 'Future trend we will beat you will be looking at now let us look at an overview '
             'affiliate marketing is conffiliate you alsation why you need to have compliance '
             'et.',
      'title': 'Must-Know Affiliate Marketing Laws: FTC Guidelines, GDPR, and Disclosure Best '
               'Practices (KudaOnline)',
      'url': 'https://www.youtube.com/watch?v=EUQ9OfMYDnw&t=80s',
      'video_id': 'EUQ9OfMYDnw'},
     {'author': 'The Agent Workshop',
      'channel': 'The Agent Workshop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=NPtudBqceS0&t=79s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'Google added this policy in March 2024. In November 2024 it went further: using '
              'third-party content this way breaks the rules no matter how much the host is '
              'involved. After that, big publishers got manual actions on those sections, as '
              'reported by Search Engine Journal.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': 'Google added this policy in March 2024. In November 2024 it went further: using '
             'third-party content this way breaks the rules no matter how much the host is '
             'involved. After that, big publishers got manual actions on those sections, as '
             'reported by Search Engine Journal.',
      'title': 'Parasite SEO in 2026: What Still Works (and What Gets You Penalized) (The '
               'Agent Workshop)',
      'url': 'https://www.youtube.com/watch?v=NPtudBqceS0&t=79s',
      'video_id': 'NPtudBqceS0'},
     {'author': 'Kasra Dash',
      'channel': 'Kasra Dash',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:30](https://www.youtube.com/watch?v=qP0qmnleojY&t=270s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'The entity way is the best CRM for accountants or a CRM for recruitment '
              'agencies. Now your brand is attached to a profession. Your page talks about '
              'what accountants actually need like client deadlines, tax season, workload, and '
              'compliance.',
      'timestamp': 270,
      'timestamp_label': '[00:04:30]',
      'timestamp_seconds': 270,
      'tip': 'The entity way is the best CRM for accountants or a CRM for recruitment '
             'agencies. Now your brand is attached to a profession. Your page talks about what '
             'accountants actually need like client deadlines, tax season, workload, and '
             'compliance.',
      'title': 'Topical Authority Is Getting Sites CRUSHED (Do This Instead) (Kasra Dash)',
      'url': 'https://www.youtube.com/watch?v=qP0qmnleojY&t=270s',
      'video_id': 'qP0qmnleojY'},
     {'author': 'Alex COLLINSEO',
      'channel': 'Alex COLLINSEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=MzA9HXeEoMA&t=110s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'And what we did here is look at the SERs and the results and there were two '
              'things that show me that we could create a page and rank. The first one was '
              'because Google was actually ranking Reddit number one as well as a YouTube '
              'video.',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': 'And what we did here is look at the SERs and the results and there were two '
             'things that show me that we could create a page and rank. The first one was '
             'because Google was actually ranking Reddit number one as well as a YouTube '
             'video.',
      'title': 'How To Outrank Your Competitors Using “Alternative” Keyword Pages (Alex '
               'COLLINSEO)',
      'url': 'https://www.youtube.com/watch?v=MzA9HXeEoMA&t=110s',
      'video_id': 'MzA9HXeEoMA'},
     {'author': 'SERPSUPPORT',
      'channel': 'SERPSUPPORT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:47](https://www.youtube.com/watch?v=xREoSqy-pj0&t=107s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'Parasite SEO tries to compress that whole journey into a few days. Parasite SEO '
              'shows up in a few common places. First, user-generated platforms. Think Medium, '
              'LinkedIn articles, Reddit, Quora, or free blogging platforms where anyone can '
              'publish under a powerful domain.',
      'timestamp': 107,
      'timestamp_label': '[00:01:47]',
      'timestamp_seconds': 107,
      'tip': 'Parasite SEO tries to compress that whole journey into a few days. Parasite SEO '
             'shows up in a few common places. First, user-generated platforms. Think Medium, '
             'LinkedIn articles, Reddit, Quora, or free blogging platforms where anyone can '
             'publish under a powerful domain.',
      'title': "What Is Parasite SEO? Google's Crackdown Explained (SERPSUPPORT)",
      'url': 'https://www.youtube.com/watch?v=xREoSqy-pj0&t=107s',
      'video_id': 'xREoSqy-pj0'},
     {'author': 'AM Days',
      'channel': 'AM Days',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:10](https://www.youtube.com/watch?v=0ELJUfzzK1M&t=430s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'In the future because they they really want to stamp out the worst of the worst '
              'practices which to me are the deceptive formats you know the fake news articles '
              'fake blogs fake review sites all right well thanks Tom sure thanks a lot.',
      'timestamp': 430,
      'timestamp_label': '[00:07:10]',
      'timestamp_seconds': 430,
      'tip': 'In the future because they they really want to stamp out the worst of the worst '
             'practices which to me are the deceptive formats you know the fake news articles '
             'fake blogs fake review sites all right well thanks Tom sure thanks a lot.',
      'title': 'FTC Affiliate Disclosure Rules and Do Not Track (AM Days)',
      'url': 'https://www.youtube.com/watch?v=0ELJUfzzK1M&t=430s',
      'video_id': '0ELJUfzzK1M'},
     {'author': 'subscribe if i helped you :)',
      'channel': 'subscribe if i helped you :)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:01](https://www.youtube.com/watch?v=rKrC1mctap4&t=61s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'Now, you can see right here if we go to the discover option and click on the '
              'find brands option, you can see right here we can search for pretty much any '
              'brand ever. You can see right here they got Target, Paramont, Walmart.',
      'timestamp': 61,
      'timestamp_label': '[00:01:01]',
      'timestamp_seconds': 61,
      'tip': 'Now, you can see right here if we go to the discover option and click on the '
             'find brands option, you can see right here we can search for pretty much any '
             'brand ever. You can see right here they got Target, Paramont, Walmart.',
      'title': 'How Does Impact.com Work? | How To Make Money With Impact.com (subscribe if i '
               'helped you :))',
      'url': 'https://www.youtube.com/watch?v=rKrC1mctap4&t=61s',
      'video_id': 'rKrC1mctap4'},
     {'author': 'Jon McNeil',
      'channel': 'Jon McNeil',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:53](https://www.youtube.com/watch?v=U4rN7FuTQGc&t=353s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': "I've tried it both different ways and conversion seems to be higher on this uh "
              "second example here, but you don't have the chance to brand yourself. So, what "
              "I've been testing out lately is kind of a new way. So, let's go ahead and start "
              'off with traffic again.',
      'timestamp': 353,
      'timestamp_label': '[00:05:53]',
      'timestamp_seconds': 353,
      'tip': "I've tried it both different ways and conversion seems to be higher on this uh "
             "second example here, but you don't have the chance to brand yourself. So, what "
             "I've been testing out lately is kind of a new way. So, let's go ahead and start "
             'off with traffic again.',
      'title': 'BRIDGE PAGE FUNNEL - (HOW TO INCREASE CONVERSIONS) (Jon McNeil)',
      'url': 'https://www.youtube.com/watch?v=U4rN7FuTQGc&t=353s',
      'video_id': 'U4rN7FuTQGc'},
     {'author': 'Marcel Sattler | Leading Native Advertising Expert',
      'channel': 'Marcel Sattler | Leading Native Advertising Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:19](https://www.youtube.com/watch?v=zxw8X11thwQ&t=919s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': "For some of them they're working better. For some of them they're working not "
              'as good as expected, but in generals are just a part which I recommend you when '
              "you have a lot of experience with native advertising cause it doesn't make "
              'sense for you when you start now in q4.',
      'timestamp': 919,
      'timestamp_label': '[00:15:19]',
      'timestamp_seconds': 919,
      'tip': "For some of them they're working better. For some of them they're working not as "
             'good as expected, but in generals are just a part which I recommend you when you '
             "have a lot of experience with native advertising cause it doesn't make sense for "
             'you when you start now in q4.',
      'title': 'Native Ads Samples – Affiliate, Arbitrage & Performance (Taboola Sample / '
               'Outbrain Sample) (Marcel Sattler | Leading Native Advertising Expert)',
      'url': 'https://www.youtube.com/watch?v=zxw8X11thwQ&t=919s',
      'video_id': 'zxw8X11thwQ'},
     {'author': 'MrOrangeDream',
      'channel': 'MrOrangeDream',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=H5OtlkBchxU&t=43s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'Would Would that give you a little bit more breathing room? If the answer is '
              'yes, then pay close attention cuz I will reveal exactly what this program is. '
              'So, this program, it is very high converting, especially for people who are '
              'brand new online.',
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': 'Would Would that give you a little bit more breathing room? If the answer is '
             'yes, then pay close attention cuz I will reveal exactly what this program is. '
             'So, this program, it is very high converting, especially for people who are '
             'brand new online.',
      'title': 'Best High Ticket Affiliate Program For Beginners 2026 ($1000/Day) '
               '(MrOrangeDream)',
      'url': 'https://www.youtube.com/watch?v=H5OtlkBchxU&t=43s',
      'video_id': 'H5OtlkBchxU'},
     {'author': 'Edward Sturm',
      'channel': 'Edward Sturm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:46](https://www.youtube.com/watch?v=NsptdY_L85A&t=106s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'Google, of course, strongly disagreed, arguing that the policy exists '
              'specifically to stop publishers from renting their authority to third parties '
              'to manipulate rankings.',
      'timestamp': 106,
      'timestamp_label': '[00:01:46]',
      'timestamp_seconds': 106,
      'tip': 'Google, of course, strongly disagreed, arguing that the policy exists '
             'specifically to stop publishers from renting their authority to third parties to '
             'manipulate rankings.',
      'title': "Google Just Dropped the Parasite SEO Penalty in Europe. Here's the Catch "
               '(Edward Sturm)',
      'url': 'https://www.youtube.com/watch?v=NsptdY_L85A&t=106s',
      'video_id': 'NsptdY_L85A'}],
 10: [{'author': 'Edward Sturm',
       'channel': 'Edward Sturm',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:05](https://www.youtube.com/watch?v=NsptdY_L85A&t=485s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': "So, if you're in SEO, you got to know about this stuff. I don't think it's "
               'going to change anything for search engine optimization within social media '
               'like Reddit or YouTube.',
       'timestamp': 485,
       'timestamp_label': '[00:08:05]',
       'timestamp_seconds': 485,
       'tip': "So, if you're in SEO, you got to know about this stuff. I don't think it's "
              'going to change anything for search engine optimization within social media '
              'like Reddit or YouTube.',
       'title': "Google Just Dropped the Parasite SEO Penalty in Europe. Here's the Catch "
                '(Edward Sturm)',
       'url': 'https://www.youtube.com/watch?v=NsptdY_L85A&t=485s',
       'video_id': 'NsptdY_L85A'},
      {'author': 'Michael Bashi',
       'channel': 'Michael Bashi',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:11](https://www.youtube.com/watch?v=lh5ulbIfANU&t=191s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': 'Can you guarantee if anyone will buy? Can you predict your future sales ratio '
               "or profit margins? It's not getting any cheaper. Rather, paid advertising "
               "keeps getting more expensive. And if you're thinking free traffic like posting "
               'on social media, well, great.',
       'timestamp': 191,
       'timestamp_label': '[00:03:11]',
       'timestamp_seconds': 191,
       'tip': 'Can you guarantee if anyone will buy? Can you predict your future sales ratio '
              "or profit margins? It's not getting any cheaper. Rather, paid advertising keeps "
              "getting more expensive. And if you're thinking free traffic like posting on "
              'social media, well, great.',
       'title': 'The Smartest Affiliate Business Model: Recurring SaaS Commissions (Michael '
                'Bashi)',
       'url': 'https://www.youtube.com/watch?v=lh5ulbIfANU&t=191s',
       'video_id': 'lh5ulbIfANU'},
      {'author': 'subscribe if i helped you :)',
       'channel': 'subscribe if i helped you :)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:50](https://www.youtube.com/watch?v=rKrC1mctap4&t=50s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': 'And you can even enter in a landing page such as a website or YouTube channel '
               "or other social media application so that brands that you're actually applying "
               'to through this website can actually increase your odds of being accepted.',
       'timestamp': 50,
       'timestamp_label': '[00:00:50]',
       'timestamp_seconds': 50,
       'tip': 'And you can even enter in a landing page such as a website or YouTube channel '
              "or other social media application so that brands that you're actually applying "
              'to through this website can actually increase your odds of being accepted.',
       'title': 'How Does Impact.com Work? | How To Make Money With Impact.com (subscribe if i '
                'helped you :))',
       'url': 'https://www.youtube.com/watch?v=rKrC1mctap4&t=50s',
       'video_id': 'rKrC1mctap4'},
      {'author': 'Smart Capital',
       'channel': 'Smart Capital',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:31](https://www.youtube.com/watch?v=LBA0vmJPE5w&t=571s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': 'One approach people use is a short email sequence, a useful guide first, a '
               'comparison second, and a trial offer third. Never a hard sell on the first '
               'email. Social media helps, but in B2B it usually the distribution channel, not '
               'the sales floor.',
       'timestamp': 571,
       'timestamp_label': '[00:09:31]',
       'timestamp_seconds': 571,
       'tip': 'One approach people use is a short email sequence, a useful guide first, a '
              'comparison second, and a trial offer third. Never a hard sell on the first '
              'email. Social media helps, but in B2B it usually the distribution channel, not '
              'the sales floor.',
       'title': 'B2B Software Affiliate Programs: How to Earn Recurring Commissions in 2026 '
                '(Smart Capital)',
       'url': 'https://www.youtube.com/watch?v=LBA0vmJPE5w&t=571s',
       'video_id': 'LBA0vmJPE5w'},
      {'author': 'Cesar O. Vlogs',
       'channel': 'Cesar O. Vlogs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[02:40:44](https://www.youtube.com/watch?v=0BMb7aXEG78&t=9644s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': 'Score that is for my YouTube channel so check this out I have I have here two '
               'options the weighted score and the unweighted I because I have the paid '
               "version I'm using the weighted score because this is for my YouTube.",
       'timestamp': 9644,
       'timestamp_label': '[02:40:44]',
       'timestamp_seconds': 9644,
       'tip': 'Score that is for my YouTube channel so check this out I have I have here two '
              'options the weighted score and the unweighted I because I have the paid version '
              "I'm using the weighted score because this is for my YouTube.",
       'title': 'High ticket affiliate marketing Ninja strategies for beginners 2024 (Cesar O. '
                'Vlogs)',
       'url': 'https://www.youtube.com/watch?v=0BMb7aXEG78&t=9644s',
       'video_id': '0BMb7aXEG78'},
      {'author': 'MrOrangeDream',
       'channel': 'MrOrangeDream',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:57](https://www.youtube.com/watch?v=H5OtlkBchxU&t=657s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': "YouTube SEO, so like videos like this that you're watching. And then the other "
               'type of traffic that I use is short-form videos with TikTok as well. And I '
               'also am going to be very soon building out a custom funnel for this exact '
               'program.',
       'timestamp': 657,
       'timestamp_label': '[00:10:57]',
       'timestamp_seconds': 657,
       'tip': "YouTube SEO, so like videos like this that you're watching. And then the other "
              'type of traffic that I use is short-form videos with TikTok as well. And I also '
              'am going to be very soon building out a custom funnel for this exact program.',
       'title': 'Best High Ticket Affiliate Program For Beginners 2026 ($1000/Day) '
                '(MrOrangeDream)',
       'url': 'https://www.youtube.com/watch?v=H5OtlkBchxU&t=657s',
       'video_id': 'H5OtlkBchxU'},
      {'author': 'Jesper Nissen SEO',
       'channel': 'Jesper Nissen SEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:34](https://www.youtube.com/watch?v=Lw3Y8hF75U8&t=214s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': 'So you get kind of like a tiered link building structure and this makes it '
               'perfect for parasite SEO And this is also one of the reasons why my social '
               'media post they rank fast and they also rank relatively high.',
       'timestamp': 214,
       'timestamp_label': '[00:03:34]',
       'timestamp_seconds': 214,
       'tip': 'So you get kind of like a tiered link building structure and this makes it '
              'perfect for parasite SEO And this is also one of the reasons why my social '
              'media post they rank fast and they also rank relatively high.',
       'title': 'The Ultimate Parasite SEO platform for fast rankings in Google (Jesper Nissen '
                'SEO)',
       'url': 'https://www.youtube.com/watch?v=Lw3Y8hF75U8&t=214s',
       'video_id': 'Lw3Y8hF75U8'},
      {'author': 'Ecom Chief',
       'channel': 'Ecom Chief',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:06](https://www.youtube.com/watch?v=iVK1QrJwylk&t=186s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': 'YouTube channel, expanded the content to include AI design tools, and created '
               'a lead generation email course. After 12 months, traffic had increased by 73%. '
               'More importantly, the monthly profit doubled and reached $4,800.',
       'timestamp': 186,
       'timestamp_label': '[00:03:06]',
       'timestamp_seconds': 186,
       'tip': 'YouTube channel, expanded the content to include AI design tools, and created a '
              'lead generation email course. After 12 months, traffic had increased by 73%. '
              'More importantly, the monthly profit doubled and reached $4,800.',
       'title': 'How to Buy and Grow an AI Affiliate Website in 2026 (High-Ticket SaaS '
                'Commissions) (Ecom Chief)',
       'url': 'https://www.youtube.com/watch?v=iVK1QrJwylk&t=186s',
       'video_id': 'iVK1QrJwylk'},
      {'author': 'Adam Enfroy',
       'channel': 'Adam Enfroy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:59](https://www.youtube.com/watch?v=rv01CKLsaY0&t=1079s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': 'You could try to spread yourself too thin doing social media and blogging and '
               "YouTube and just none of the content's good. You need really consistent output "
               "and focus on one platform. It's either a website or a YouTube channel. It's "
               'hard to do both at the same time.',
       'timestamp': 1079,
       'timestamp_label': '[00:17:59]',
       'timestamp_seconds': 1079,
       'tip': 'You could try to spread yourself too thin doing social media and blogging and '
              "YouTube and just none of the content's good. You need really consistent output "
              "and focus on one platform. It's either a website or a YouTube channel. It's "
              'hard to do both at the same time.',
       'title': 'How to ACTUALLY Make Your First $1,000 with High Ticket Affiliate '
                'Marketing... Works in 2026 (Adam Enfroy)',
       'url': 'https://www.youtube.com/watch?v=rv01CKLsaY0&t=1079s',
       'video_id': 'rv01CKLsaY0'},
      {'author': 'Ryan Mathews',
       'channel': 'Ryan Mathews',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:22](https://www.youtube.com/watch?v=mhUqtWNsZ8A&t=22s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': "The client I mentioned is getting all of his traffic from YouTube, but we're "
               'going to go through a real example right now and set it all up. And this '
               "client that we're setting it up for is going to be running Facebook ads as "
               'well as Reddit ads which is kind of unique.',
       'timestamp': 22,
       'timestamp_label': '[00:00:22]',
       'timestamp_seconds': 22,
       'tip': "The client I mentioned is getting all of his traffic from YouTube, but we're "
              'going to go through a real example right now and set it all up. And this client '
              "that we're setting it up for is going to be running Facebook ads as well as "
              'Reddit ads which is kind of unique.',
       'title': 'The ULTIMATE Funnel for Selling High Ticket Offers (Ryan Mathews)',
       'url': 'https://www.youtube.com/watch?v=mhUqtWNsZ8A&t=22s',
       'video_id': 'mhUqtWNsZ8A'},
      {'author': 'Aaron Chen',
       'channel': 'Aaron Chen',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:47](https://www.youtube.com/watch?v=HNlC0mNMS60&t=287s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': 'Facebook ads, Bing Ads, Google ads, right? Or you can do it for free, which I '
               'I prefer. So social media posts like Facebook post, Tik Tok post, YouTube '
               'post, and Instagram posts.',
       'timestamp': 287,
       'timestamp_label': '[00:04:47]',
       'timestamp_seconds': 287,
       'tip': 'Facebook ads, Bing Ads, Google ads, right? Or you can do it for free, which I I '
              'prefer. So social media posts like Facebook post, Tik Tok post, YouTube post, '
              'and Instagram posts.',
       'title': 'High-Ticket Affiliate Marketing Explained | How People Make $1k/Per Sale '
                '(Aaron Chen)',
       'url': 'https://www.youtube.com/watch?v=HNlC0mNMS60&t=287s',
       'video_id': 'HNlC0mNMS60'},
      {'author': 'Mr. Money',
       'channel': 'Mr. Money',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:52](https://www.youtube.com/watch?v=VHaXNPiHd6Q&t=172s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': 'And of course, whichever social media platform you use, you can use it. For '
               'example, I like to use Pinterest for the pet niche and some health and beauty '
               'products because first of all, Pinterest has over 1. 2 billion visits on the '
               'platform each month.',
       'timestamp': 172,
       'timestamp_label': '[00:02:52]',
       'timestamp_seconds': 172,
       'tip': 'And of course, whichever social media platform you use, you can use it. For '
              'example, I like to use Pinterest for the pet niche and some health and beauty '
              'products because first of all, Pinterest has over 1. 2 billion visits on the '
              'platform each month.',
       'title': 'How To Make Money With Partnerstack Affiliate Marketing in 2026 (Mr. Money)',
       'url': 'https://www.youtube.com/watch?v=VHaXNPiHd6Q&t=172s',
       'video_id': 'VHaXNPiHd6Q'},
      {'author': 'Kris the Entrepreneur',
       'channel': 'Kris the Entrepreneur',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:23](https://www.youtube.com/watch?v=JFjxGPpUYBk&t=623s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': "Of course, it's important that you don't spam your YouTube channel with this "
               "because it's not a sales channel. The most important thing to keep in mind is "
               'that you want to make a video that actually have value that helps people.',
       'timestamp': 623,
       'timestamp_label': '[00:10:23]',
       'timestamp_seconds': 623,
       'tip': "Of course, it's important that you don't spam your YouTube channel with this "
              "because it's not a sales channel. The most important thing to keep in mind is "
              'that you want to make a video that actually have value that helps people.',
       'title': 'How to Make Your First $500 on Impact (Affiliate Marketing for Beginners) '
                '(Kris the Entrepreneur)',
       'url': 'https://www.youtube.com/watch?v=JFjxGPpUYBk&t=623s',
       'video_id': 'JFjxGPpUYBk'},
      {'author': 'SEO Boardroom',
       'channel': 'SEO Boardroom',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:56](https://www.youtube.com/watch?v=L6ZLGvFvaT8&t=116s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': 'I was just talking about in my spam video. That these links are ranking huge '
               "because DR95, 2-3 million in traffic. Of course, they're going to outrank you "
               "if you just started or your website simply doesn't invest in building "
               'authority.',
       'timestamp': 116,
       'timestamp_label': '[00:01:56]',
       'timestamp_seconds': 116,
       'tip': 'I was just talking about in my spam video. That these links are ranking huge '
              "because DR95, 2-3 million in traffic. Of course, they're going to outrank you "
              "if you just started or your website simply doesn't invest in building "
              'authority.',
       'title': 'Google Just Said Parasite SEO Is OK! (SEO Boardroom)',
       'url': 'https://www.youtube.com/watch?v=L6ZLGvFvaT8&t=116s',
       'video_id': 'L6ZLGvFvaT8'},
      {'author': 'Rob Hoffman',
       'channel': 'Rob Hoffman',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:24:19](https://www.youtube.com/watch?v=mPeQxVCunPU&t=1459s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': 'I also have other content on my YouTube channel where I dive deeper into how '
               'to build each specific type of page. For example, how to build a best page, '
               'like best project management tool, and I go through it in depth.',
       'timestamp': 1459,
       'timestamp_label': '[00:24:19]',
       'timestamp_seconds': 1459,
       'tip': 'I also have other content on my YouTube channel where I dive deeper into how to '
              'build each specific type of page. For example, how to build a best page, like '
              'best project management tool, and I go through it in depth.',
       'title': "Copy This Al SEO Strategy, It'll Blow Up Your Business (Rob Hoffman)",
       'url': 'https://www.youtube.com/watch?v=mPeQxVCunPU&t=1459s',
       'video_id': 'mPeQxVCunPU'}],
 11: [{'author': 'MissionMoreMoney',
       'channel': 'MissionMoreMoney',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:04](https://www.youtube.com/watch?v=vd2RLWPlaqw&t=304s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': "If you work alone, you won't need to do anything here, but as soon as you hire "
               'a channel manager or an editor, this is where you safely send them an invite '
               'so they can access your portal without sharing your account password, right?',
       'timestamp': 304,
       'timestamp_label': '[00:05:04]',
       'timestamp_seconds': 304,
       'tip': "If you work alone, you won't need to do anything here, but as soon as you hire "
              'a channel manager or an editor, this is where you safely send them an invite so '
              'they can access your portal without sharing your account password, right?',
       'title': 'PartnerStack Affiliate Marketing | Basic Tutorial for Beginners '
                '(MissionMoreMoney)',
       'url': 'https://www.youtube.com/watch?v=vd2RLWPlaqw&t=304s',
       'video_id': 'vd2RLWPlaqw'},
      {'author': 'Roland Bernath',
       'channel': 'Roland Bernath',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:37](https://www.youtube.com/watch?v=RbYaW3a3yCY&t=97s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': "But if you don't segment them, they're going to waste your time and your "
               "team's time and you don't want that, right? So basically, we ask them the "
               'initial questions you would ask your ideal client. Do you already create '
               'content? Do you have an offer that actually works?',
       'timestamp': 97,
       'timestamp_label': '[00:01:37]',
       'timestamp_seconds': 97,
       'tip': "But if you don't segment them, they're going to waste your time and your team's "
              "time and you don't want that, right? So basically, we ask them the initial "
              'questions you would ask your ideal client. Do you already create content? Do '
              'you have an offer that actually works?',
       'title': 'The ONLY Funnel You Need to Sell High Ticket in 2026 (Roland Bernath)',
       'url': 'https://www.youtube.com/watch?v=RbYaW3a3yCY&t=97s',
       'video_id': 'RbYaW3a3yCY'},
      {'author': 'Ahrefs',
       'channel': 'Ahrefs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:27](https://www.youtube.com/watch?v=Sk8MAbD39Qw&t=87s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': 'Digital Media and is now AllGear Digital. It worked out in January 2021, we '
               'were acquired. They acquired iRunFar and did what every content company was '
               'doing. They created more guides, more categories, more content. Every '
               'affiliate site was running the same playbook.',
       'timestamp': 87,
       'timestamp_label': '[00:01:27]',
       'timestamp_seconds': 87,
       'tip': 'Digital Media and is now AllGear Digital. It worked out in January 2021, we '
              'were acquired. They acquired iRunFar and did what every content company was '
              'doing. They created more guides, more categories, more content. Every affiliate '
              'site was running the same playbook.',
       'title': 'Google Crushed Affiliate Websites. His Grew Anyway. (Ahrefs)',
       'url': 'https://www.youtube.com/watch?v=Sk8MAbD39Qw&t=87s',
       'video_id': 'Sk8MAbD39Qw'},
      {'author': 'Kasra Dash',
       'channel': 'Kasra Dash',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:01](https://www.youtube.com/watch?v=qP0qmnleojY&t=481s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': 'That second list is your content plan. Rank OS comes with the school group by '
               "the way. You don't buy it on its own. So, remember the site that went from 10 "
               'million visits to zero. It did the old thing at scale. Thousands of pages '
               'anyone could write, attached to nothing.',
       'timestamp': 481,
       'timestamp_label': '[00:08:01]',
       'timestamp_seconds': 481,
       'tip': 'That second list is your content plan. Rank OS comes with the school group by '
              "the way. You don't buy it on its own. So, remember the site that went from 10 "
              'million visits to zero. It did the old thing at scale. Thousands of pages '
              'anyone could write, attached to nothing.',
       'title': 'Topical Authority Is Getting Sites CRUSHED (Do This Instead) (Kasra Dash)',
       'url': 'https://www.youtube.com/watch?v=qP0qmnleojY&t=481s',
       'video_id': 'qP0qmnleojY'},
      {'author': 'Traffic Cardinal EN — Affiliate Press',
       'channel': 'Traffic Cardinal EN — Affiliate Press',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:24:13](https://www.youtube.com/watch?v=caUORKmsfnU&t=1453s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': "'t reach it then they're gone and then you hire someone else. Uh because a lot "
               'of it is you you kind of have to know you have to train the skills in in the '
               "person. So you want that person around they're an asset to the business.",
       'timestamp': 1453,
       'timestamp_label': '[00:24:13]',
       'timestamp_seconds': 1453,
       'tip': "'t reach it then they're gone and then you hire someone else. Uh because a lot "
              'of it is you you kind of have to know you have to train the skills in in the '
              "person. So you want that person around they're an asset to the business.",
       'title': 'The SEO Strategy Google Can’t Kill — James Oliver Explains Parasite SEO '
                '(Traffic Cardinal EN — Affiliate Press)',
       'url': 'https://www.youtube.com/watch?v=caUORKmsfnU&t=1453s',
       'video_id': 'caUORKmsfnU'},
      {'author': 'ExclusiveLiveCall',
       'channel': 'ExclusiveLiveCall',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:26](https://www.youtube.com/watch?v=XKj8PVuNBOs&t=506s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': "You're helping them understand what can I afford to pay to acquire a "
               'profitable customer. Once the buyer is interested, start collecting the '
               'information needed to create the campaign. Which zip codes, cities, or states? '
               'How many opportunities per day?',
       'timestamp': 506,
       'timestamp_label': '[00:08:26]',
       'timestamp_seconds': 506,
       'tip': "You're helping them understand what can I afford to pay to acquire a profitable "
              'customer. Once the buyer is interested, start collecting the information needed '
              'to create the campaign. Which zip codes, cities, or states? How many '
              'opportunities per day?',
       'title': 'How to Find Pay Per Call Buyers | Build Performance Marketing Business | Pay '
                'Per Call University #9 (ExclusiveLiveCall)',
       'url': 'https://www.youtube.com/watch?v=XKj8PVuNBOs&t=506s',
       'video_id': 'XKj8PVuNBOs'},
      {'author': 'Jamie McAdam',
       'channel': 'Jamie McAdam',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:43](https://www.youtube.com/watch?v=khf473ZL71w&t=523s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': "'t forget because no matter what a member of our team will be sitting on that "
               "call for half an hour whether you are there or not and we'd love to help you "
               'get to the desired outcome with our XYZ mechanism, okay?',
       'timestamp': 523,
       'timestamp_label': '[00:08:43]',
       'timestamp_seconds': 523,
       'tip': "'t forget because no matter what a member of our team will be sitting on that "
              "call for half an hour whether you are there or not and we'd love to help you "
              'get to the desired outcome with our XYZ mechanism, okay?',
       'title': 'The 4-Page VSL Funnel For $5K High Ticket Programs (Jamie McAdam)',
       'url': 'https://www.youtube.com/watch?v=khf473ZL71w&t=523s',
       'video_id': 'khf473ZL71w'},
      {'author': 'John Casto',
       'channel': 'John Casto',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:46](https://www.youtube.com/watch?v=WwyCibTrAlY&t=646s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': "I've watched dropshipping videos since 2019 with uh Bulletproof Scaling, "
               'right? Uh you also had the tag The Wolf of Ecom, correct? I study one, I study '
               'everything.',
       'timestamp': 646,
       'timestamp_label': '[00:10:46]',
       'timestamp_seconds': 646,
       'tip': "I've watched dropshipping videos since 2019 with uh Bulletproof Scaling, right? "
              'Uh you also had the tag The Wolf of Ecom, correct? I study one, I study '
              'everything.',
       'title': '4 Million Dollars Per Month With Pay Per Call - Zishan Manji (John Casto)',
       'url': 'https://www.youtube.com/watch?v=WwyCibTrAlY&t=646s',
       'video_id': 'WwyCibTrAlY'},
      {'author': 'Smart Capital',
       'channel': 'Smart Capital',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:11](https://www.youtube.com/watch?v=LBA0vmJPE5w&t=191s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': 'That is also why the sales cycle is longer. A business does not impulse buy a '
               "tool at midnight. It researches, trials, and gets a manager's approval. Your "
               'content has to serve that slower, careful decision.',
       'timestamp': 191,
       'timestamp_label': '[00:03:11]',
       'timestamp_seconds': 191,
       'tip': 'That is also why the sales cycle is longer. A business does not impulse buy a '
              "tool at midnight. It researches, trials, and gets a manager's approval. Your "
              'content has to serve that slower, careful decision.',
       'title': 'B2B Software Affiliate Programs: How to Earn Recurring Commissions in 2026 '
                '(Smart Capital)',
       'url': 'https://www.youtube.com/watch?v=LBA0vmJPE5w&t=191s',
       'video_id': 'LBA0vmJPE5w'},
      {'author': 'Khris Steven',
       'channel': 'Khris Steven',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:18](https://www.youtube.com/watch?v=-C4gk3OAfmk&t=318s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': 'It You know, what you need to do The first thing you need to do is, you know, '
               'do some keyword research on Deel, then create content. So, the content could '
               "be on your website, it could be on YouTube, the way I'm I'm shooting this "
               'video right now.',
       'timestamp': 318,
       'timestamp_label': '[00:05:18]',
       'timestamp_seconds': 318,
       'tip': 'It You know, what you need to do The first thing you need to do is, you know, '
              'do some keyword research on Deel, then create content. So, the content could be '
              "on your website, it could be on YouTube, the way I'm I'm shooting this video "
              'right now.',
       'title': 'PartnerStack Affiliate Walkthrough: Finding Offers + My $3K Withdrawal (Khris '
                'Steven)',
       'url': 'https://www.youtube.com/watch?v=-C4gk3OAfmk&t=318s',
       'video_id': '-C4gk3OAfmk'},
      {'author': 'ToThePoint Guide',
       'channel': 'ToThePoint Guide',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:21](https://www.youtube.com/watch?v=fAqhUrhwABs&t=81s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': 'So there are many ways how you can do it. Then you can have the content '
               "marketplace. So unlock new revenue streams with your content. Let's start by "
               "content property. So you're going to like edit, right?",
       'timestamp': 81,
       'timestamp_label': '[00:01:21]',
       'timestamp_seconds': 81,
       'tip': 'So there are many ways how you can do it. Then you can have the content '
              "marketplace. So unlock new revenue streams with your content. Let's start by "
              "content property. So you're going to like edit, right?",
       'title': 'PartnerStack Tutorial 2026 | How to Use & Promote PartnerStack Affiliate for '
                'Beginners (ToThePoint Guide)',
       'url': 'https://www.youtube.com/watch?v=fAqhUrhwABs&t=81s',
       'video_id': 'fAqhUrhwABs'},
      {'author': 'Drew Tutorial',
       'channel': 'Drew Tutorial',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:47](https://www.youtube.com/watch?v=fPXIdQyUtwQ&t=227s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': "I want to see more, click on explore all and it's taking me all over here to "
               'taking me over where I can see all those 17 different programs available on '
               "partner stock as it relates to the social media niche. Now, I'm going to show "
               "you what's here as well.",
       'timestamp': 227,
       'timestamp_label': '[00:03:47]',
       'timestamp_seconds': 227,
       'tip': "I want to see more, click on explore all and it's taking me all over here to "
              'taking me over where I can see all those 17 different programs available on '
              "partner stock as it relates to the social media niche. Now, I'm going to show "
              "you what's here as well.",
       'title': 'How to Use PartnerStack (Full Tutorial) | Start Earning With Affiliate '
                'Programs Fast! (Drew Tutorial)',
       'url': 'https://www.youtube.com/watch?v=fPXIdQyUtwQ&t=227s',
       'video_id': 'fPXIdQyUtwQ'},
      {'author': 'Jesper Nissen SEO',
       'channel': 'Jesper Nissen SEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:32](https://www.youtube.com/watch?v=Lw3Y8hF75U8&t=32s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': "So, I didn't include the outgoing link here in the comment because I don't "
               'want to you insert too many links in the body of the body content of the post '
               'because some platforms like X, they do sometimes throttle down your reach if '
               'you do include links.',
       'timestamp': 32,
       'timestamp_label': '[00:00:32]',
       'timestamp_seconds': 32,
       'tip': "So, I didn't include the outgoing link here in the comment because I don't want "
              'to you insert too many links in the body of the body content of the post '
              'because some platforms like X, they do sometimes throttle down your reach if '
              'you do include links.',
       'title': 'The Ultimate Parasite SEO platform for fast rankings in Google (Jesper Nissen '
                'SEO)',
       'url': 'https://www.youtube.com/watch?v=Lw3Y8hF75U8&t=32s',
       'video_id': 'Lw3Y8hF75U8'},
      {'author': 'Kris the Entrepreneur',
       'channel': 'Kris the Entrepreneur',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:35](https://www.youtube.com/watch?v=nCy55CUnfK4&t=35s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': 'And if you make content that is more towards B2C, you know, more easier '
               'subjects, not tutorials guys and all, well then maybe other networks will be '
               'more relevant because talking about some tech software might not be the right '
               'fit for your channel.',
       'timestamp': 35,
       'timestamp_label': '[00:00:35]',
       'timestamp_seconds': 35,
       'tip': 'And if you make content that is more towards B2C, you know, more easier '
              'subjects, not tutorials guys and all, well then maybe other networks will be '
              'more relevant because talking about some tech software might not be the right '
              'fit for your channel.',
       'title': "Don't Use PartnerStack Until You Watch This (Kris the Entrepreneur)",
       'url': 'https://www.youtube.com/watch?v=nCy55CUnfK4&t=35s',
       'video_id': 'nCy55CUnfK4'},
      {'author': 'Ryan Mathews',
       'channel': 'Ryan Mathews',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:55](https://www.youtube.com/watch?v=mhUqtWNsZ8A&t=535s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': "I actually forget this cuz I don't actually personally design funnels anymore. "
               "I have somebody on my team who's far better than me. Within high level, one "
               'nice thing is you can actually change these settings specific for mobile.',
       'timestamp': 535,
       'timestamp_label': '[00:08:55]',
       'timestamp_seconds': 535,
       'tip': "I actually forget this cuz I don't actually personally design funnels anymore. "
              "I have somebody on my team who's far better than me. Within high level, one "
              'nice thing is you can actually change these settings specific for mobile.',
       'title': 'The ULTIMATE Funnel for Selling High Ticket Offers (Ryan Mathews)',
       'url': 'https://www.youtube.com/watch?v=mhUqtWNsZ8A&t=535s',
       'video_id': 'mhUqtWNsZ8A'}],
 12: [{'author': 'Ecommerce Paradise | High Ticket Dropshipping',
       'channel': 'Ecommerce Paradise | High Ticket Dropshipping',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:34](https://www.youtube.com/watch?v=oCSQ3s1mmGQ&t=94s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': "And with Gem Pages, it's uh, you know, only 29 bucks a month to create "
               'multiple landing pages. But for the free plan, you can create at least one '
               'landing page. You can create a high ticket quote request funnel for example or '
               'maybe a design service that fits your niche.',
       'timestamp': 94,
       'timestamp_label': '[00:01:34]',
       'timestamp_seconds': 94,
       'tip': "And with Gem Pages, it's uh, you know, only 29 bucks a month to create multiple "
              'landing pages. But for the free plan, you can create at least one landing page. '
              'You can create a high ticket quote request funnel for example or maybe a design '
              'service that fits your niche.',
       'title': 'How to Build a High-Ticket Quote Funnel with GemPages and Claude (Ecommerce '
                'Paradise | High Ticket Dropshipping)',
       'url': 'https://www.youtube.com/watch?v=oCSQ3s1mmGQ&t=94s',
       'video_id': 'oCSQ3s1mmGQ'},
      {'author': 'Ryan Mathews',
       'channel': 'Ryan Mathews',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:05](https://www.youtube.com/watch?v=mhUqtWNsZ8A&t=185s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': "'ll start building out these steps. So, again, the the first page here is the "
               'video page. And actually already started building this. I recorded this video '
               "once and my camera died. So, we're going to just get a little bit of a head "
               'start here.',
       'timestamp': 185,
       'timestamp_label': '[00:03:05]',
       'timestamp_seconds': 185,
       'tip': "'ll start building out these steps. So, again, the the first page here is the "
              'video page. And actually already started building this. I recorded this video '
              "once and my camera died. So, we're going to just get a little bit of a head "
              'start here.',
       'title': 'The ULTIMATE Funnel for Selling High Ticket Offers (Ryan Mathews)',
       'url': 'https://www.youtube.com/watch?v=mhUqtWNsZ8A&t=185s',
       'video_id': 'mhUqtWNsZ8A'},
      {'author': 'Jayant Padhi',
       'channel': 'Jayant Padhi',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:34](https://www.youtube.com/watch?v=wj29osNl-zE&t=154s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': "I'll personally record your sales process identify in a bottlenecks and help "
               'you create a personalized action plan to start closing more high ticket deals '
               'with ease so which is amazing.',
       'timestamp': 154,
       'timestamp_label': '[00:02:34]',
       'timestamp_seconds': 154,
       'tip': "I'll personally record your sales process identify in a bottlenecks and help "
              'you create a personalized action plan to start closing more high ticket deals '
              'with ease so which is amazing.',
       'title': 'I used ChatGPT4 to build a high ticket funnel (Jayant Padhi)',
       'url': 'https://www.youtube.com/watch?v=wj29osNl-zE&t=154s',
       'video_id': 'wj29osNl-zE'},
      {'author': 'vanel sylvestre',
       'channel': 'vanel sylvestre',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:05](https://www.youtube.com/watch?v=a32vgNX3Qkw&t=125s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': '" So, I use a website called Hostinger to create a multiple landing page and I '
               'create a website on my name, Vano Sylvestri, and I create landing page for '
               "each offer. So, you're going to pay only $4 per month with this company. But, "
               'I will suggest you to pay a yearly plan.',
       'timestamp': 125,
       'timestamp_label': '[00:02:05]',
       'timestamp_seconds': 125,
       'tip': '" So, I use a website called Hostinger to create a multiple landing page and I '
              'create a website on my name, Vano Sylvestri, and I create landing page for each '
              "offer. So, you're going to pay only $4 per month with this company. But, I will "
              'suggest you to pay a yearly plan.',
       'title': "I Made $14,000 With Pay Per Call Affiliate Marketing (Here's Exactly How!) "
                '(vanel sylvestre)',
       'url': 'https://www.youtube.com/watch?v=a32vgNX3Qkw&t=125s',
       'video_id': 'a32vgNX3Qkw'},
      {'author': 'Eric Beer',
       'channel': 'Eric Beer',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:53](https://www.youtube.com/watch?v=-V2ponSNAm8&t=173s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': 'Grand a month and then something and then you start building your list and '
               'building your asset so you can sell this bad boy one day later on in life so '
               "with that said boys and girls love you all I'm out later.",
       'timestamp': 173,
       'timestamp_label': '[00:02:53]',
       'timestamp_seconds': 173,
       'tip': 'Grand a month and then something and then you start building your list and '
              'building your asset so you can sell this bad boy one day later on in life so '
              "with that said boys and girls love you all I'm out later.",
       'title': 'How to make MILLIONS with affiliate marketing and lead gen arbitrage (Eric '
                'Beer)',
       'url': 'https://www.youtube.com/watch?v=-V2ponSNAm8&t=173s',
       'video_id': '-V2ponSNAm8'},
      {'author': 'Bens Review Videos',
       'channel': 'Bens Review Videos',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:54](https://www.youtube.com/watch?v=eqw-Rqw7PNY&t=294s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': 'The Case Files are the part I read twice. JayKay shows his own walk-in tub '
               'funnel in Marion County, Florida. Domain nine ninety-nine, NumberBarn six '
               'ninety-nine a month. In the first fourteen days: four calls, two pressed one, '
               'one voicemail.',
       'timestamp': 294,
       'timestamp_label': '[00:04:54]',
       'timestamp_seconds': 294,
       'tip': 'The Case Files are the part I read twice. JayKay shows his own walk-in tub '
              'funnel in Marion County, Florida. Domain nine ninety-nine, NumberBarn six '
              'ninety-nine a month. In the first fourteen days: four calls, two pressed one, '
              'one voicemail.',
       'title': 'RHIMS 10 Review: Pay Per Call Affiliate Marketing for Beginners, Expired '
                'Domains + 3 Bonuses (Bens Review Videos)',
       'url': 'https://www.youtube.com/watch?v=eqw-Rqw7PNY&t=294s',
       'video_id': 'eqw-Rqw7PNY'},
      {'author': 'Beginner to 1K a Day Journey',
       'channel': 'Beginner to 1K a Day Journey',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=lHKdHRzs75g&t=21s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': 'Before we start today today not today yesterday and 2nd of July are the best '
               "two days for me since I've started. So, this is no longer a journey. This is "
               "no longer something I wish I could reach. It's already it's a present right "
               "now. It's happening as we talking.",
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'Before we start today today not today yesterday and 2nd of July are the best '
              "two days for me since I've started. So, this is no longer a journey. This is no "
              "longer something I wish I could reach. It's already it's a present right now. "
              "It's happening as we talking.",
       'title': '($23k/month) 450% ROI Pay Per Call Campaign | Marketcall Case Study (Beginner '
                'to 1K a Day Journey)',
       'url': 'https://www.youtube.com/watch?v=lHKdHRzs75g&t=21s',
       'video_id': 'lHKdHRzs75g'},
      {'author': 'The Infamous Joel',
       'channel': 'The Infamous Joel',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:02](https://www.youtube.com/watch?v=YVPPIdIHYpo&t=542s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': '"Oh, I made three thousand in a week. I made five thousand my first month." '
               "They didn't do anything different. All they did was change what they were "
               'selling. They came to me and they were like, "Oh, I\'ve only made $50 with '
               'this thing."',
       'timestamp': 542,
       'timestamp_label': '[00:09:02]',
       'timestamp_seconds': 542,
       'tip': '"Oh, I made three thousand in a week. I made five thousand my first month." '
              "They didn't do anything different. All they did was change what they were "
              'selling. They came to me and they were like, "Oh, I\'ve only made $50 with this '
              'thing."',
       'title': '20 High-Ticket Affiliate Programs to Find $1K Commissions (The Infamous Joel)',
       'url': 'https://www.youtube.com/watch?v=YVPPIdIHYpo&t=542s',
       'video_id': 'YVPPIdIHYpo'},
      {'author': 'Ahrefs',
       'channel': 'Ahrefs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:51](https://www.youtube.com/watch?v=Sk8MAbD39Qw&t=591s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': 'So, it could just run every week, every month, every day if you wanted to. '
               'Have it email you a report. If you have Slack, it can send a message in a '
               'Slack channel. Like, you can connect whichever applications you want. And '
               "then, >> you're able to do that here.",
       'timestamp': 591,
       'timestamp_label': '[00:09:51]',
       'timestamp_seconds': 591,
       'tip': 'So, it could just run every week, every month, every day if you wanted to. Have '
              'it email you a report. If you have Slack, it can send a message in a Slack '
              'channel. Like, you can connect whichever applications you want. And then, >> '
              "you're able to do that here.",
       'title': 'Google Crushed Affiliate Websites. His Grew Anyway. (Ahrefs)',
       'url': 'https://www.youtube.com/watch?v=Sk8MAbD39Qw&t=591s',
       'video_id': 'Sk8MAbD39Qw'},
      {'author': 'Alex Cattoni',
       'channel': 'Alex Cattoni',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:11](https://www.youtube.com/watch?v=vC_LEc8pGp8&t=71s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': "Let's start with the sales page, 365 day inbox income, so this page sells my "
               '$27 email marketing mini course, 365 day inbox income, which helps marketers '
               'and business owners plan their email marketing calendar for an entire year.',
       'timestamp': 71,
       'timestamp_label': '[00:01:11]',
       'timestamp_seconds': 71,
       'tip': "Let's start with the sales page, 365 day inbox income, so this page sells my "
              '$27 email marketing mini course, 365 day inbox income, which helps marketers '
              'and business owners plan their email marketing calendar for an entire year.',
       'title': 'This Landing Page Has A 79% Conversion Rate. Here’s Why It Works… (Alex '
                'Cattoni)',
       'url': 'https://www.youtube.com/watch?v=vC_LEc8pGp8&t=71s',
       'video_id': 'vC_LEc8pGp8'},
      {'author': 'The Agent Workshop',
       'channel': 'The Agent Workshop',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:12](https://www.youtube.com/watch?v=NPtudBqceS0&t=192s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': "And casino, payday loan, or coupon pages on sites that aren't about that. On "
               'the other side, Google says wire stories, forum posts, closely edited content, '
               "and clearly labeled ads are fine. Here's a safe version you can start today, "
               'in five steps.',
       'timestamp': 192,
       'timestamp_label': '[00:03:12]',
       'timestamp_seconds': 192,
       'tip': "And casino, payday loan, or coupon pages on sites that aren't about that. On "
              'the other side, Google says wire stories, forum posts, closely edited content, '
              "and clearly labeled ads are fine. Here's a safe version you can start today, in "
              'five steps.',
       'title': 'Parasite SEO in 2026: What Still Works (and What Gets You Penalized) (The '
                'Agent Workshop)',
       'url': 'https://www.youtube.com/watch?v=NPtudBqceS0&t=192s',
       'video_id': 'NPtudBqceS0'},
      {'author': 'John Casto',
       'channel': 'John Casto',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:30](https://www.youtube.com/watch?v=WwyCibTrAlY&t=330s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': 'And that was a golden tip that we did during Q4 last year that took us from '
               '120k a day to 260k a day in like 4 or 5 days. You destroyed you crushed ACA. I '
               'mean, I had a lot of great contacts, great friends, and I had great teachers.',
       'timestamp': 330,
       'timestamp_label': '[00:05:30]',
       'timestamp_seconds': 330,
       'tip': 'And that was a golden tip that we did during Q4 last year that took us from '
              '120k a day to 260k a day in like 4 or 5 days. You destroyed you crushed ACA. I '
              'mean, I had a lot of great contacts, great friends, and I had great teachers.',
       'title': '4 Million Dollars Per Month With Pay Per Call - Zishan Manji (John Casto)',
       'url': 'https://www.youtube.com/watch?v=WwyCibTrAlY&t=330s',
       'video_id': 'WwyCibTrAlY'},
      {'author': 'Atomic Funnels',
       'channel': 'Atomic Funnels',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:27](https://www.youtube.com/watch?v=g1L7iVYbiGs&t=87s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': 'Fox, CBS, NBC, Bloomberg, Market Watch, 300 other media outlets. We as we go '
               'down the page, we take our outcome and we diffuse it a little bit into three '
               'steps. How is it that we arrive at that outcome? Then we get into offer '
               'presentation.',
       'timestamp': 87,
       'timestamp_label': '[00:01:27]',
       'timestamp_seconds': 87,
       'tip': 'Fox, CBS, NBC, Bloomberg, Market Watch, 300 other media outlets. We as we go '
              'down the page, we take our outcome and we diffuse it a little bit into three '
              'steps. How is it that we arrive at that outcome? Then we get into offer '
              'presentation.',
       'title': 'Best Sales Funnel for High-Ticket Offers? 4 Types Compared (2026) (Atomic '
                'Funnels)',
       'url': 'https://www.youtube.com/watch?v=g1L7iVYbiGs&t=87s',
       'video_id': 'g1L7iVYbiGs'},
      {'author': 'Jon McNeil',
       'channel': 'Jon McNeil',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:43](https://www.youtube.com/watch?v=U4rN7FuTQGc&t=463s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': "'ll make another video about that for another day. 're going to get onto your "
               'autoresponder, so in this first email, you want to introduce yourself, right?',
       'timestamp': 463,
       'timestamp_label': '[00:07:43]',
       'timestamp_seconds': 463,
       'tip': "'ll make another video about that for another day. 're going to get onto your "
              'autoresponder, so in this first email, you want to introduce yourself, right?',
       'title': 'BRIDGE PAGE FUNNEL - (HOW TO INCREASE CONVERSIONS) (Jon McNeil)',
       'url': 'https://www.youtube.com/watch?v=U4rN7FuTQGc&t=463s',
       'video_id': 'U4rN7FuTQGc'},
      {'author': 'Alex COLLINSEO',
       'channel': 'Alex COLLINSEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:40](https://www.youtube.com/watch?v=MzA9HXeEoMA&t=340s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': "'t offer but you are relevant to it or smart alternative that the first "
               "example you can offer that so they don't want what you offer exactly but you "
               'do offer also the alternative.',
       'timestamp': 340,
       'timestamp_label': '[00:05:40]',
       'timestamp_seconds': 340,
       'tip': "'t offer but you are relevant to it or smart alternative that the first example "
              "you can offer that so they don't want what you offer exactly but you do offer "
              'also the alternative.',
       'title': 'How To Outrank Your Competitors Using “Alternative” Keyword Pages (Alex '
                'COLLINSEO)',
       'url': 'https://www.youtube.com/watch?v=MzA9HXeEoMA&t=340s',
       'video_id': 'MzA9HXeEoMA'}]}
