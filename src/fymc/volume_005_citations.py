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
     {'author': 'Smart Affiliate',
      'channel': 'Smart Affiliate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:30](https://www.youtube.com/watch?v=WVmpPW1fJPQ&t=690s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': "Digistore24, all these other affiliate programs. But you're not just paying for "
              'the affiliate link. Yes, you have the potential to earn 80% commissions, '
              'including recurring and one-time high-ticket payouts.',
      'timestamp': 690,
      'timestamp_label': '[00:11:30]',
      'timestamp_seconds': 690,
      'tip': "Digistore24, all these other affiliate programs. But you're not just paying for "
             'the affiliate link. Yes, you have the potential to earn 80% commissions, '
             'including recurring and one-time high-ticket payouts.',
      'title': 'Done-For-You Affiliate Marketing: Recurring + High Ticket (Smart Affiliate)',
      'url': 'https://www.youtube.com/watch?v=WVmpPW1fJPQ&t=690s',
      'video_id': 'WVmpPW1fJPQ'},
     {'author': 'Adam Enfroy',
      'channel': 'Adam Enfroy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:09](https://www.youtube.com/watch?v=N7nyWQc6E1c&t=129s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': "Now, that's not typical, but VPNs is quite an interesting affiliate model that "
              "way. Okay, so those are recurring. Let's get to part two, which is high ticket "
              'programs. So, these are great if you want like fewer needed customers but '
              'bigger payouts.',
      'timestamp': 129,
      'timestamp_label': '[00:02:09]',
      'timestamp_seconds': 129,
      'tip': "Now, that's not typical, but VPNs is quite an interesting affiliate model that "
             "way. Okay, so those are recurring. Let's get to part two, which is high ticket "
             'programs. So, these are great if you want like fewer needed customers but bigger '
             'payouts.',
      'title': '13 Best Affiliate Programs You NEED to Join in 2026 (High Paying for '
               'Beginners) (Adam Enfroy)',
      'url': 'https://www.youtube.com/watch?v=N7nyWQc6E1c&t=129s',
      'video_id': 'N7nyWQc6E1c'},
     {'author': 'affiliatemarketingmc',
      'channel': 'affiliatemarketingmc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:18](https://www.youtube.com/watch?v=iPXqbbPxjHQ&t=258s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': 'It pays $15 a lead, and in order to get that, I would go over to eLocal and '
              "sign up. It's an affiliate network, much like MaxBounty, even like Commission "
              "Junction. These are all networks that have lots of offers, and that's where I "
              'would go if I wanted this offer.',
      'timestamp': 258,
      'timestamp_label': '[00:04:18]',
      'timestamp_seconds': 258,
      'tip': 'It pays $15 a lead, and in order to get that, I would go over to eLocal and sign '
             "up. It's an affiliate network, much like MaxBounty, even like Commission "
             "Junction. These are all networks that have lots of offers, and that's where I "
             'would go if I wanted this offer.',
      'title': 'Pay Per Lead Affiliate Programs - Full Training - $800 Per Lead? '
               '(affiliatemarketingmc)',
      'url': 'https://www.youtube.com/watch?v=iPXqbbPxjHQ&t=258s',
      'video_id': 'iPXqbbPxjHQ'},
     {'author': 'Kris the Entrepreneur',
      'channel': 'Kris the Entrepreneur',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=C-RMQqTVMOE&t=75s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': 'PartnerStack partnerships that I do. And as I mentioned, PartnerStack is '
              "focused on B2B, so it's a lot of SaaS companies again that offer higher "
              'commissions.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': 'PartnerStack partnerships that I do. And as I mentioned, PartnerStack is focused '
             "on B2B, so it's a lot of SaaS companies again that offer higher commissions.",
      'title': 'PartnerStack for Beginners: (2026 Step-by-Step Tutorial) (Kris the '
               'Entrepreneur)',
      'url': 'https://www.youtube.com/watch?v=C-RMQqTVMOE&t=75s',
      'video_id': 'C-RMQqTVMOE'},
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
     {'author': 'Jamie McAdam',
      'channel': 'Jamie McAdam',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:16](https://www.youtube.com/watch?v=Ck6CfmXv244&t=196s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': 'I used the low ticket to warm [snorts] them up to the high ticket, right? So, '
              'what I did was a two-step funnel with a third optional step, okay? So, it was '
              'laid out a little bit in the same way that I lay out our VSL funnels when I '
              'draw them on this board, right?',
      'timestamp': 196,
      'timestamp_label': '[00:03:16]',
      'timestamp_seconds': 196,
      'tip': 'I used the low ticket to warm [snorts] them up to the high ticket, right? So, '
             'what I did was a two-step funnel with a third optional step, okay? So, it was '
             'laid out a little bit in the same way that I lay out our VSL funnels when I draw '
             'them on this board, right?',
      'title': 'Can a $27 Low-Ticket Offer Really Sell a $5,000 Programme? (Jamie McAdam)',
      'url': 'https://www.youtube.com/watch?v=Ck6CfmXv244&t=196s',
      'video_id': 'Ck6CfmXv244'},
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
     {'author': 'ODi Productions',
      'channel': 'ODi Productions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:37](https://www.youtube.com/watch?v=mv0_WM_IIrU&t=817s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': 'Also, unlike traditional affiliate networks, Tik Tok shop brands often offer '
              'higher commission rates of 10 to 30%, which really encourages creators to '
              'showcase these products in their short form videos and live streams.',
      'timestamp': 817,
      'timestamp_label': '[00:13:37]',
      'timestamp_seconds': 817,
      'tip': 'Also, unlike traditional affiliate networks, Tik Tok shop brands often offer '
             'higher commission rates of 10 to 30%, which really encourages creators to '
             'showcase these products in their short form videos and live streams.',
      'title': 'Highest Paying Affiliate Programs in 2026: The Ultimate List (ODi Productions)',
      'url': 'https://www.youtube.com/watch?v=mv0_WM_IIrU&t=817s',
      'video_id': 'mv0_WM_IIrU'},
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
     {'author': 'Smart Capital',
      'channel': 'Smart Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:28](https://www.youtube.com/watch?v=GCv_2yM5JtI&t=148s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': 'Some marketers consider the cookie length just as important as the commission '
              'rate because premium products have long decision cycles. Real industries, real '
              'programs, reported commission ranges you can verify. First, web hosting, the '
              'classic high-ticket niche.',
      'timestamp': 148,
      'timestamp_label': '[00:02:28]',
      'timestamp_seconds': 148,
      'tip': 'Some marketers consider the cookie length just as important as the commission '
             'rate because premium products have long decision cycles. Real industries, real '
             'programs, reported commission ranges you can verify. First, web hosting, the '
             'classic high-ticket niche.',
      'title': 'High-Ticket Affiliate Marketing for Beginners: 5-Step System & Costly Mistakes '
               '(Smart Capital)',
      'url': 'https://www.youtube.com/watch?v=GCv_2yM5JtI&t=148s',
      'video_id': 'GCv_2yM5JtI'},
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
     {'author': 'Eric Beer',
      'channel': 'Eric Beer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:12](https://www.youtube.com/watch?v=hgYi_edLti8&t=432s)',
      'relevance': 'Attributed practitioner commentary on high-ticket recurring B2B SaaS, '
                   'fintech bounty, and concierge CPA referral models versus low-margin retail '
                   'links.',
      'source_type': 'video_pro_tip',
      'text': 'Person making one million dollars the fastest was the person that sold their '
              "shovels to all the people looking for the gold all right guys appreciate y'all "
              'be well talk to you soon.',
      'timestamp': 432,
      'timestamp_label': '[00:07:12]',
      'timestamp_seconds': 432,
      'tip': 'Person making one million dollars the fastest was the person that sold their '
             "shovels to all the people looking for the gold all right guys appreciate y'all "
             'be well talk to you soon.',
      'title': 'How to ARBITRAGE Affiliate Offers with PAID Traffic [complete breakdown] (Eric '
               'Beer)',
      'url': 'https://www.youtube.com/watch?v=hgYi_edLti8&t=432s',
      'video_id': 'hgYi_edLti8'},
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
      'video_id': 'lh5ulbIfANU'}],
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
     {'author': 'Decoding Ads',
      'channel': 'Decoding Ads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=OFst3KoUCj0&t=38s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': '" So, should we use a number from any pay-per-call network directly? I always '
              'advise against it. You should use your own number and route it accordingly. And '
              'through what can you do that routing? You can do that routing entirely through '
              'Ringba.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': '" So, should we use a number from any pay-per-call network directly? I always '
             'advise against it. You should use your own number and route it accordingly. And '
             'through what can you do that routing? You can do that routing entirely through '
             'Ringba.',
      'title': 'Ringba Setup Tutorial 2026 🔥 | Complete Pay Per Call Tracking Setup (Decoding '
               'Ads)',
      'url': 'https://www.youtube.com/watch?v=OFst3KoUCj0&t=38s',
      'video_id': 'OFst3KoUCj0'},
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
     {'author': 'PingPost Exchange',
      'channel': 'PingPost Exchange',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:35](https://www.youtube.com/watch?v=u6fnEGbP72s&t=335s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
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
     {'author': 'Everflow - Partner Marketing Platform',
      'channel': 'Everflow - Partner Marketing Platform',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:41](https://www.youtube.com/watch?v=q6vkJhEncx0&t=341s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': "Where you can find that Global Advertiser postback that's going to be found in "
              "your everflow dashboard so I'm going to stop sharing and let's share the "
              'everflow.',
      'timestamp': 341,
      'timestamp_label': '[00:05:41]',
      'timestamp_seconds': 341,
      'tip': "Where you can find that Global Advertiser postback that's going to be found in "
             "your everflow dashboard so I'm going to stop sharing and let's share the "
             'everflow.',
      'title': 'Postbacks 101 With Everflow (Everflow - Partner Marketing Platform)',
      'url': 'https://www.youtube.com/watch?v=q6vkJhEncx0&t=341s',
      'video_id': 'q6vkJhEncx0'},
     {'author': 'George Helgesen',
      'channel': 'George Helgesen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:52](https://www.youtube.com/watch?v=pbmgkJeKEGc&t=1792s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': "'ve been living in a world for the last 10, 20 years where you could just get "
              'people for free. You could go post on social or you could go write an article '
              "and get discovered in search and people would come and you wouldn't have to pay "
              'for them, right?',
      'timestamp': 1792,
      'timestamp_label': '[00:29:52]',
      'timestamp_seconds': 1792,
      'tip': "'ve been living in a world for the last 10, 20 years where you could just get "
             'people for free. You could go post on social or you could go write an article '
             "and get discovered in search and people would come and you wouldn't have to pay "
             'for them, right?',
      'title': '$1M with 1,000 Subscribers, Acquisition, Free Traffic is OVER | Louis '
               'Nicholls, SparkLoop Co-Founder (George Helgesen)',
      'url': 'https://www.youtube.com/watch?v=pbmgkJeKEGc&t=1792s',
      'video_id': 'pbmgkJeKEGc'},
     {'author': 'affiliatemarketingmc',
      'channel': 'affiliatemarketingmc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=-vgLc6H8Nac&t=21s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': "'s going to make the most money possible. So, instead of promoting something on "
              "Amazon that pays 2%, we're going to be looking at programs that pay as much as "
              '$30 a lead and some keywords where advertisers are paying upwards of $50 or '
              'more for one click to their website.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "'s going to make the most money possible. So, instead of promoting something on "
             "Amazon that pays 2%, we're going to be looking at programs that pay as much as "
             '$30 a lead and some keywords where advertisers are paying upwards of $50 or more '
             'for one click to their website.',
      'title': 'Pay Per Lead Affiliate Programs + CRAZY Directory Site Business Model! '
               '(affiliatemarketingmc)',
      'url': 'https://www.youtube.com/watch?v=-vgLc6H8Nac&t=21s',
      'video_id': '-vgLc6H8Nac'},
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
      'video_id': 'wv4e9QY42p8'},
     {'author': 'Everflow - Partner Marketing Platform',
      'channel': 'Everflow - Partner Marketing Platform',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:28](https://www.youtube.com/watch?v=NSernIgs5XQ&t=328s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': "Said your partner will give you a postback for their system and I'm going to "
              'show you exactly how you can Implement that so I going to stop sharing my '
              'screen real.',
      'timestamp': 328,
      'timestamp_label': '[00:05:28]',
      'timestamp_seconds': 328,
      'tip': "Said your partner will give you a postback for their system and I'm going to "
             'show you exactly how you can Implement that so I going to stop sharing my screen '
             'real.',
      'title': 'Partner and Advertiser Postback 101 (Everflow - Partner Marketing Platform)',
      'url': 'https://www.youtube.com/watch?v=NSernIgs5XQ&t=328s',
      'video_id': 'NSernIgs5XQ'},
     {'author': 'Everflow - Partner Marketing Platform',
      'channel': 'Everflow - Partner Marketing Platform',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:08](https://www.youtube.com/watch?v=qXMBHCgI3Wk&t=128s)',
      'relevance': 'Attributed practitioner commentary on merchant CAC economics, '
                   'PartnerStack/Impact/Everflow networks, pay-per-call switches, and '
                   'attribution windows.',
      'source_type': 'video_pro_tip',
      'text': "Or if they're using email attribution, they can do that as well to correctly "
              "credit the partner who generated the initial lead 2 weeks earlier. Okay, let's "
              'look at another example. A client launching a new mobile game uses an MMP or '
              'mobile measurement partner like Singular.',
      'timestamp': 128,
      'timestamp_label': '[00:02:08]',
      'timestamp_seconds': 128,
      'tip': "Or if they're using email attribution, they can do that as well to correctly "
             "credit the partner who generated the initial lead 2 weeks earlier. Okay, let's "
             'look at another example. A client launching a new mobile game uses an MMP or '
             'mobile measurement partner like Singular.',
      'title': 'How to Set Up & Test Your Advertiser Postback | Everflow Mini Webinars '
               '(Everflow - Partner Marketing Platform)',
      'url': 'https://www.youtube.com/watch?v=qXMBHCgI3Wk&t=128s',
      'video_id': 'qXMBHCgI3Wk'}],
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
     {'author': 'Kris the Entrepreneur',
      'channel': 'Kris the Entrepreneur',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:57](https://www.youtube.com/watch?v=Pk230wGiiVY&t=237s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': "And I would also in general say it's better to look at other companies where "
              "there's higher commission than some of these consumer products or like for "
              "example example Target. 't have so much of a margin and for that reason they "
              "can't offer much of a commission here.",
      'timestamp': 237,
      'timestamp_label': '[00:03:57]',
      'timestamp_seconds': 237,
      'tip': "And I would also in general say it's better to look at other companies where "
             "there's higher commission than some of these consumer products or like for "
             "example example Target. 't have so much of a margin and for that reason they "
             "can't offer much of a commission here.",
      'title': 'Impact Affiliate Program Tutorial (How To Make Money For Beginners) (Kris the '
               'Entrepreneur)',
      'url': 'https://www.youtube.com/watch?v=Pk230wGiiVY&t=237s',
      'video_id': 'Pk230wGiiVY'},
     {'author': 'Rafael Hernandez ⚡️',
      'channel': 'Rafael Hernandez ⚡️',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=UGKIfB-aGpg&t=30s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': "Neil Patel's NP Digital and Ubersuggest, and I spent 5 years as a software "
              "engineer at Microsoft before building my agency Great Marketing AI. So, let's "
              "jump right into it. We'll go over the diagram in a little bit, but lead "
              'arbitrage.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': "Neil Patel's NP Digital and Ubersuggest, and I spent 5 years as a software "
             "engineer at Microsoft before building my agency Great Marketing AI. So, let's "
             "jump right into it. We'll go over the diagram in a little bit, but lead "
             'arbitrage.',
      'title': 'Lead Arbitrage: How To Turn A $2 Click Into $45 Profit (Rafael Hernandez ⚡️)',
      'url': 'https://www.youtube.com/watch?v=UGKIfB-aGpg&t=30s',
      'video_id': 'UGKIfB-aGpg'},
     {'author': 'John Casto',
      'channel': 'John Casto',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:34](https://www.youtube.com/watch?v=WwyCibTrAlY&t=1174s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': "You are not the biggest shark. You You aren't the smartest person. There is a "
              "kid that's 18 doing 300k a day profit. It's a big smack in the face being 26 "
              "and nowhere even close to that. But it grounds you because trust me, there's "
              'always a bigger shark.',
      'timestamp': 1174,
      'timestamp_label': '[00:19:34]',
      'timestamp_seconds': 1174,
      'tip': "You are not the biggest shark. You You aren't the smartest person. There is a "
             "kid that's 18 doing 300k a day profit. It's a big smack in the face being 26 and "
             "nowhere even close to that. But it grounds you because trust me, there's always "
             'a bigger shark.',
      'title': '4 Million Dollars Per Month With Pay Per Call - Zishan Manji (John Casto)',
      'url': 'https://www.youtube.com/watch?v=WwyCibTrAlY&t=1174s',
      'video_id': 'WwyCibTrAlY'},
     {'author': 'Marcel Sattler | Leading Native Advertising Expert',
      'channel': 'Marcel Sattler | Leading Native Advertising Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:33](https://www.youtube.com/watch?v=zxw8X11thwQ&t=153s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': 'So what we see here is, Here in E-bike. Um, here, a little bit of arbitrage '
              "content usually. I will just open different taps here to see what's the, what's "
              "the case here? This is cool because what you see here that's, uh, kind of "
              'performance at or, or search arbitrage.',
      'timestamp': 153,
      'timestamp_label': '[00:02:33]',
      'timestamp_seconds': 153,
      'tip': 'So what we see here is, Here in E-bike. Um, here, a little bit of arbitrage '
             "content usually. I will just open different taps here to see what's the, what's "
             "the case here? This is cool because what you see here that's, uh, kind of "
             'performance at or, or search arbitrage.',
      'title': 'Native Ads Samples – Affiliate, Arbitrage & Performance (Taboola Sample / '
               'Outbrain Sample) (Marcel Sattler | Leading Native Advertising Expert)',
      'url': 'https://www.youtube.com/watch?v=zxw8X11thwQ&t=153s',
      'video_id': 'zxw8X11thwQ'},
     {'author': 'Find Your Influence',
      'channel': 'Find Your Influence',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:42:49](https://www.youtube.com/watch?v=Hq1UDKzazVQ&t=2569s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': 'Staff or the commission is written um but some of these fly by the answer '
              "applied by the answers such as you know complementary stay I mean I'm kind of "
              'this is my own.',
      'timestamp': 2569,
      'timestamp_label': '[00:42:49]',
      'timestamp_seconds': 2569,
      'tip': 'Staff or the commission is written um but some of these fly by the answer '
             "applied by the answers such as you know complementary stay I mean I'm kind of "
             'this is my own.',
      'title': 'New FTC Guidelines & Disclosures that Brands, Agencies and Influencers Need to '
               'Know (Find Your Influence)',
      'url': 'https://www.youtube.com/watch?v=Hq1UDKzazVQ&t=2569s',
      'video_id': 'Hq1UDKzazVQ'},
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
     {'author': 'Eric Beer',
      'channel': 'Eric Beer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:42](https://www.youtube.com/watch?v=lI1fQGR95XA&t=462s)',
      'relevance': 'Attributed practitioner commentary on earnings-per-click (EPC), recurring '
                   'commission waterfalls, reversal/clawback reserves, and net-60 cashflow.',
      'source_type': 'video_pro_tip',
      'text': "Just be outside my head and like take this bad boy for a drive uh yeah that's "
              "it guys um hey man I'm gonna go grab some lunch right now but I want to come on "
              'just tell you guys that quickly and uh wishing you guys well.',
      'timestamp': 462,
      'timestamp_label': '[00:07:42]',
      'timestamp_seconds': 462,
      'tip': "Just be outside my head and like take this bad boy for a drive uh yeah that's it "
             "guys um hey man I'm gonna go grab some lunch right now but I want to come on "
             'just tell you guys that quickly and uh wishing you guys well.',
      'title': 'How to find leads for your offer... LEAD GEN ARBITRAGE (Eric Beer)',
      'url': 'https://www.youtube.com/watch?v=lI1fQGR95XA&t=462s',
      'video_id': 'lI1fQGR95XA'},
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
      'video_id': 'A_xXkLg_0xI'}],
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
     {'author': 'GuideToEverything',
      'channel': 'GuideToEverything',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=YSLKEXHh_xI&t=21s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': 'It offers comprehensive partner management capabilities, including affiliate '
              'tracking, referral management, and influencer recruitment. Users have praised '
              'partner stack for its ease of use, quick setup, and responsive customer '
              'support.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'It offers comprehensive partner management capabilities, including affiliate '
             'tracking, referral management, and influencer recruitment. Users have praised '
             'partner stack for its ease of use, quick setup, and responsive customer support.',
      'title': 'PartnerStack vs Impact.com: Best Affiliate Platform for 2026? '
               '(GuideToEverything)',
      'url': 'https://www.youtube.com/watch?v=YSLKEXHh_xI&t=21s',
      'video_id': 'YSLKEXHh_xI'},
     {'author': 'Rankso SEO',
      'channel': 'Rankso SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:58](https://www.youtube.com/watch?v=gGfsCEiyizs&t=358s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': 'Category searches ask for the best time tracking software for freelancers. '
              'Alternative searches ask what to use instead of a platform tracker. Comparison '
              'searches weigh two tools. Problem searches ask how to show a client where the '
              'hours went.',
      'timestamp': 358,
      'timestamp_label': '[00:05:58]',
      'timestamp_seconds': 358,
      'tip': 'Category searches ask for the best time tracking software for freelancers. '
             'Alternative searches ask what to use instead of a platform tracker. Comparison '
             'searches weigh two tools. Problem searches ask how to show a client where the '
             'hours went.',
      'title': 'Parasite Reddit SEO: Find Google Traffic With This Workflow (Rankso SEO)',
      'url': 'https://www.youtube.com/watch?v=gGfsCEiyizs&t=358s',
      'video_id': 'gGfsCEiyizs'},
     {'author': 'Pixel Setup GTM Expert',
      'channel': 'Pixel Setup GTM Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:52](https://www.youtube.com/watch?v=HBs0vkiWarc&t=412s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': "Cloudflare, the problem is they just don't know how to set it up. If someone "
              'sets it up properly, the data will definitely go through. And if someone cannot '
              'set it up properly, they will naturally say, that server-side tracking cannot '
              'be done with Cloudflare .',
      'timestamp': 412,
      'timestamp_label': '[00:06:52]',
      'timestamp_seconds': 412,
      'tip': "Cloudflare, the problem is they just don't know how to set it up. If someone "
             'sets it up properly, the data will definitely go through. And if someone cannot '
             'set it up properly, they will naturally say, that server-side tracking cannot be '
             'done with Cloudflare .',
      'title': 'Cloudflare Server Side Tracking Setup | GTM + Meta CAPI | Cloudflare pixel | '
               'Live Tracking Dashboard (Pixel Setup GTM Expert)',
      'url': 'https://www.youtube.com/watch?v=HBs0vkiWarc&t=412s',
      'video_id': 'HBs0vkiWarc'},
     {'author': 'Jyll Saskin Gales | Google Ads Coach',
      'channel': 'Jyll Saskin Gales | Google Ads Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:21](https://www.youtube.com/watch?v=hv2uV4hfAQE&t=201s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': "Like, what what's the big issue here? And again, as part of that, target-based "
              "bid strategies are not designed to be limited by budget. I've spoken on this "
              'podcast before about how being limited by budget actually hinders performance.',
      'timestamp': 201,
      'timestamp_label': '[00:03:21]',
      'timestamp_seconds': 201,
      'tip': "Like, what what's the big issue here? And again, as part of that, target-based "
             "bid strategies are not designed to be limited by budget. I've spoken on this "
             'podcast before about how being limited by budget actually hinders performance.',
      'title': 'The Truth About Google\'s New Target Bidding "Update" [Inside Google Ads '
               'Episode 130] (Jyll Saskin Gales | Google Ads Coach)',
      'url': 'https://www.youtube.com/watch?v=hv2uV4hfAQE&t=201s',
      'video_id': 'hv2uV4hfAQE'},
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
     {'author': 'Everflow - Partner Marketing Platform',
      'channel': 'Everflow - Partner Marketing Platform',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:32](https://www.youtube.com/watch?v=_VC3Wol9b0c&t=332s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': 'Instead of all available offers the generated tracking links can be exported in '
              'CSV or a Json n format you can now generate tracking links from three different '
              'places utilizing various options within your everflow.',
      'timestamp': 332,
      'timestamp_label': '[00:05:32]',
      'timestamp_seconds': 332,
      'tip': 'Instead of all available offers the generated tracking links can be exported in '
             'CSV or a Json n format you can now generate tracking links from three different '
             'places utilizing various options within your everflow.',
      'title': 'How To Generate Tracking Links | Everflow Mini Webinars (Everflow - Partner '
               'Marketing Platform)',
      'url': 'https://www.youtube.com/watch?v=_VC3Wol9b0c&t=332s',
      'video_id': '_VC3Wol9b0c'},
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
     {'author': 'SEO Affiliate Domination',
      'channel': 'SEO Affiliate Domination',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:00](https://www.youtube.com/watch?v=cjhrLqpWHc0&t=360s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': 'So you almost had to learn it from like masterminds and buy courses and things '
              'like that. Now you can learn a lot of great stuff for free, but still the stuff '
              "that you're, learning, you're not a hundred percent sure that it will work if "
              "you don't have any context and stuff.",
      'timestamp': 360,
      'timestamp_label': '[00:06:00]',
      'timestamp_seconds': 360,
      'tip': 'So you almost had to learn it from like masterminds and buy courses and things '
             'like that. Now you can learn a lot of great stuff for free, but still the stuff '
             "that you're, learning, you're not a hundred percent sure that it will work if "
             "you don't have any context and stuff.",
      'title': 'Kajabi Review: FreshLearn vs Kajabi Comparison and Strategy (SEO Affiliate '
               'Domination)',
      'url': 'https://www.youtube.com/watch?v=cjhrLqpWHc0&t=360s',
      'video_id': 'cjhrLqpWHc0'},
     {'author': 'Traffic Systems Affiliate',
      'channel': 'Traffic Systems Affiliate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:49](https://www.youtube.com/watch?v=SpYPdy4dbsY&t=169s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': 'But once you have the right message or the market match, for example, you have '
              "someone like me, steak lovers, yes, even if you offer it for free, I'll take "
              "it, of course, or if even if I had to pay a lot of money. So, that's how it "
              'works, right?',
      'timestamp': 169,
      'timestamp_label': '[00:02:49]',
      'timestamp_seconds': 169,
      'tip': 'But once you have the right message or the market match, for example, you have '
             "someone like me, steak lovers, yes, even if you offer it for free, I'll take it, "
             "of course, or if even if I had to pay a lot of money. So, that's how it works, "
             'right?',
      'title': 'How I Made $2,100 in One Day With Google Ads Affiliate Marketing (Traffic '
               'Systems Affiliate)',
      'url': 'https://www.youtube.com/watch?v=SpYPdy4dbsY&t=169s',
      'video_id': 'SpYPdy4dbsY'},
     {'author': 'SparkLoop',
      'channel': 'SparkLoop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:52:24](https://www.youtube.com/watch?v=i_xgpz4ZZB8&t=3144s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless edge hosting, '
                   'server-side click trackers, and expired authority/podcast asset reuse.',
      'source_type': 'video_pro_tip',
      'text': "Have questions then obviously you're very free to reach out to our support and "
              "we're always happy to take a look and to help and see what we can do foreign.",
      'timestamp': 3144,
      'timestamp_label': '[00:52:24]',
      'timestamp_seconds': 3144,
      'tip': "Have questions then obviously you're very free to reach out to our support and "
             "we're always happy to take a look and to help and see what we can do foreign.",
      'title': 'Explode Newsletter Growth with a Partner Program - newsletter growth '
               'masterclass (SparkLoop)',
      'url': 'https://www.youtube.com/watch?v=i_xgpz4ZZB8&t=3144s',
      'video_id': 'i_xgpz4ZZB8'},
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
      'video_id': 'xREoSqy-pj0'}],
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
     {'author': 'Alek Borisov',
      'channel': 'Alek Borisov',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:30](https://www.youtube.com/watch?v=BF1KHGKUa78&t=150s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': "One, Google's own pages carry so much trust that they get found and indexed "
              'fast. Two, Google has eased off one kind of enforcement. By the end of August, '
              'Google stopped applying the manual penalties for what it calls site reputation '
              'abuse for searchers in Europe.',
      'timestamp': 150,
      'timestamp_label': '[00:02:30]',
      'timestamp_seconds': 150,
      'tip': "One, Google's own pages carry so much trust that they get found and indexed "
             'fast. Two, Google has eased off one kind of enforcement. By the end of August, '
             'Google stopped applying the manual penalties for what it calls site reputation '
             'abuse for searchers in Europe.',
      'title': 'The New Parasite SEO Loophole Hiding Inside Google (Alek Borisov)',
      'url': 'https://www.youtube.com/watch?v=BF1KHGKUa78&t=150s',
      'video_id': 'BF1KHGKUa78'},
     {'author': 'Max Crakanthorp',
      'channel': 'Max Crakanthorp',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:37](https://www.youtube.com/watch?v=Q3nMwUqzuq8&t=517s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': 'This is the campaign that allows you to feed data into the Google algorithm. It '
              'protects your brand from competitors and it boosts your SER ratings if your SEO '
              "is poor. So, if you're a brand new company, you may have really poor SEO.",
      'timestamp': 517,
      'timestamp_label': '[00:08:37]',
      'timestamp_seconds': 517,
      'tip': 'This is the campaign that allows you to feed data into the Google algorithm. It '
             'protects your brand from competitors and it boosts your SER ratings if your SEO '
             "is poor. So, if you're a brand new company, you may have really poor SEO.",
      'title': 'How To Run Google Ads For High Ticket Products [2026] (Max Crakanthorp)',
      'url': 'https://www.youtube.com/watch?v=Q3nMwUqzuq8&t=517s',
      'video_id': 'Q3nMwUqzuq8'},
     {'author': 'Guaranteed PPC',
      'channel': 'Guaranteed PPC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:17](https://www.youtube.com/watch?v=ceHQ0dOvobM&t=137s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': "'s going to cost me to show up on Google for those terms. And you could tell "
              "affiliates, by the way, don't actually bid on my brand terms. People are going "
              'to do it anyway. It is pretty hard to police.',
      'timestamp': 137,
      'timestamp_label': '[00:02:17]',
      'timestamp_seconds': 137,
      'tip': "'s going to cost me to show up on Google for those terms. And you could tell "
             "affiliates, by the way, don't actually bid on my brand terms. People are going "
             'to do it anyway. It is pretty hard to police.',
      'title': "💸 Brand Bidding On Google ADs - What People Don't Know About This That Loses "
               'Them Money! 🔍 (Guaranteed PPC)',
      'url': 'https://www.youtube.com/watch?v=ceHQ0dOvobM&t=137s',
      'video_id': 'ceHQ0dOvobM'},
     {'author': 'Amanda Agostinho',
      'channel': 'Amanda Agostinho',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:21](https://www.youtube.com/watch?v=8XBelBHfIXE&t=201s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': 'Então o que que eu faço aqui? Então, affiliates are allowed to advertise in our '
              'product, ou seja, os afiliados são permitidos sim anunciar é através do Google '
              'Ads. However, que é, no entanto, não é permitido usar o brand name ou em '
              'qualquer material que de divulgação.',
      'timestamp': 201,
      'timestamp_label': '[00:03:21]',
      'timestamp_seconds': 201,
      'tip': 'Então o que que eu faço aqui? Então, affiliates are allowed to advertise in our '
             'product, ou seja, os afiliados são permitidos sim anunciar é através do Google '
             'Ads. However, que é, no entanto, não é permitido usar o brand name ou em '
             'qualquer material que de divulgação.',
      'title': 'Como Anunciar Produtos Proibidos (NO BRAND BIDDING)\xa0- FAÇA ISSO! [AFILIADO '
               'NA GRINGA] - GOOGLE ADS (Amanda Agostinho)',
      'url': 'https://www.youtube.com/watch?v=8XBelBHfIXE&t=201s',
      'video_id': '8XBelBHfIXE'},
     {'author': 'Affiliate Credo',
      'channel': 'Affiliate Credo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=d5gBmVpAghM&t=54s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': 'You can also download this presentation as a PDF file for your management or '
              'personal use. The link is in the description. Because you can promote a brand, '
              'a person, services or products. What Google calls an entity. An entity becomes '
              'visible when it has connections.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'You can also download this presentation as a PDF file for your management or '
             'personal use. The link is in the description. Because you can promote a brand, a '
             'person, services or products. What Google calls an entity. An entity becomes '
             'visible when it has connections.',
      'title': 'Free Traffic from Google in 2026 for your Brand/Person: Parasite SEO Strategy '
               '(Affiliate Credo)',
      'url': 'https://www.youtube.com/watch?v=d5gBmVpAghM&t=54s',
      'video_id': 'd5gBmVpAghM'},
     {'author': 'Vitor Lisboa',
      'channel': 'Vitor Lisboa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=gYellXXL3Vk&t=20s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': 'Vai aprender o que é o no Brand Beating, como saber se o produto é proibido, '
              'porque alguns produtores permitem tu anunciar pro nome e outros não. Quais '
              'cuidados tu precisa ter ao escolher esses produtos? Quais são as punições se tu '
              'decidir anunciar eles?',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'Vai aprender o que é o no Brand Beating, como saber se o produto é proibido, '
             'porque alguns produtores permitem tu anunciar pro nome e outros não. Quais '
             'cuidados tu precisa ter ao escolher esses produtos? Quais são as punições se tu '
             'decidir anunciar eles?',
      'title': '🔴[NO BRAND BIDDING] Como Anunciar PRODUTOS PROIBIDOS no Google Ads (Vitor '
               'Lisboa)',
      'url': 'https://www.youtube.com/watch?v=gYellXXL3Vk&t=20s',
      'video_id': 'gYellXXL3Vk'},
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
     {'author': 'Ivan Mana',
      'channel': 'Ivan Mana',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:24](https://www.youtube.com/watch?v=HRjV85omYRA&t=504s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': "Cases and yes they won't reinstate you so something for you guys to just keep "
              'in mind okay and yeah hope this video was helpful I will see you in the next '
              'one.',
      'timestamp': 504,
      'timestamp_label': '[00:08:24]',
      'timestamp_seconds': 504,
      'tip': "Cases and yes they won't reinstate you so something for you guys to just keep in "
             'mind okay and yeah hope this video was helpful I will see you in the next one.',
      'title': 'BRAND BIDDING... How It Is Allowed?? (Ivan Mana)',
      'url': 'https://www.youtube.com/watch?v=HRjV85omYRA&t=504s',
      'video_id': 'HRjV85omYRA'},
     {'author': 'Analytics Playbook: Learn Marketing Analytics',
      'channel': 'Analytics Playbook: Learn Marketing Analytics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:46](https://www.youtube.com/watch?v=HMW_yXXlRPs&t=46s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': "You technically can use a competitor's name in your ad copy until they file a "
              'complaint. Recently, Google updated its trademark policy.',
      'timestamp': 46,
      'timestamp_label': '[00:00:46]',
      'timestamp_seconds': 46,
      'tip': "You technically can use a competitor's name in your ad copy until they file a "
             'complaint. Recently, Google updated its trademark policy.',
      'title': 'Can You Bid on Competitor Brand Names in Google Ads? (Analytics Playbook: '
               'Learn Marketing Analytics)',
      'url': 'https://www.youtube.com/watch?v=HMW_yXXlRPs&t=46s',
      'video_id': 'HMW_yXXlRPs'},
     {'author': 'Paul Rooney',
      'channel': 'Paul Rooney',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=91G7BkMV6A8&t=157s)',
      'relevance': 'Attributed practitioner commentary on Google Site Reputation Abuse sweeps, '
                   'mid-funnel commission cuts, TM+ brand-bidding bans, and scrub traps.',
      'source_type': 'video_pro_tip',
      'text': 'So, what we recommend is looking at uh the auction insights to see if anyone is '
              'bidding on your brand terms, and if brand protection is warranted, or even just '
              'searching your brand organically and seeing if anyone is going after your '
              'terms.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': 'So, what we recommend is looking at uh the auction insights to see if anyone is '
             'bidding on your brand terms, and if brand protection is warranted, or even just '
             'searching your brand organically and seeing if anyone is going after your terms.',
      'title': 'Should You Bid on Your Own Brand Name in Google Ads? (Paul Rooney)',
      'url': 'https://www.youtube.com/watch?v=91G7BkMV6A8&t=157s',
      'video_id': '91G7BkMV6A8'}],
 6: [{'author': 'Analytics Playbook: Learn Marketing Analytics',
      'channel': 'Analytics Playbook: Learn Marketing Analytics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=HMW_yXXlRPs&t=22s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': "It should be a strategic decision. If you're in a niche or lower competition "
              'industry, the search volume might not be there. Also competitor keywords almost '
              "always have a higher cost per click because Google knows you're not the "
              'competitor being searched.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "It should be a strategic decision. If you're in a niche or lower competition "
             'industry, the search volume might not be there. Also competitor keywords almost '
             "always have a higher cost per click because Google knows you're not the "
             'competitor being searched.',
      'title': 'Can You Bid on Competitor Brand Names in Google Ads? (Analytics Playbook: '
               'Learn Marketing Analytics)',
      'url': 'https://www.youtube.com/watch?v=HMW_yXXlRPs&t=22s',
      'video_id': 'HMW_yXXlRPs'},
     {'author': 'Adam Enfroy',
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
     {'author': 'Nuvela',
      'channel': 'Nuvela',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:02](https://www.youtube.com/watch?v=oumcg9JUhzE&t=542s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': "'re researching products, don't just search randomly based on your mood. Search "
              "using real keyword data. We've already explained exactly how to find keywords "
              "and how to research them. So, make sure you check those videos. Now, let's go "
              'back to analytics.',
      'timestamp': 542,
      'timestamp_label': '[00:09:02]',
      'timestamp_seconds': 542,
      'tip': "'re researching products, don't just search randomly based on your mood. Search "
             "using real keyword data. We've already explained exactly how to find keywords "
             "and how to research them. So, make sure you check those videos. Now, let's go "
             'back to analytics.',
      'title': 'How to Get More Outbound Clicks on Pinterest | Affiliate Marketing for '
               'Beginners (Nuvela)',
      'url': 'https://www.youtube.com/watch?v=oumcg9JUhzE&t=542s',
      'video_id': 'oumcg9JUhzE'},
     {'author': 'Aldo Gomes',
      'channel': 'Aldo Gomes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:02](https://www.youtube.com/watch?v=rc7rwCDzbg4&t=182s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': '1 top of page bid on the high range, which is very cheap for a keyword with '
              'such high intent. And so this is how you escape fierce competition while still '
              'navigating buyers territory on Google. But good keywords do not save ads that '
              'are destined to fail.',
      'timestamp': 182,
      'timestamp_label': '[00:03:02]',
      'timestamp_seconds': 182,
      'tip': '1 top of page bid on the high range, which is very cheap for a keyword with such '
             'high intent. And so this is how you escape fierce competition while still '
             'navigating buyers territory on Google. But good keywords do not save ads that '
             'are destined to fail.',
      'title': '$57 Affiliate Payouts With $35 Google Ads CPA (Full Funnel Breakdown) (Aldo '
               'Gomes)',
      'url': 'https://www.youtube.com/watch?v=rc7rwCDzbg4&t=182s',
      'video_id': 'rc7rwCDzbg4'},
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
     {'author': 'The SEO Desk',
      'channel': 'The SEO Desk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=DyyeBcHNuHU&t=100s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': 'And you can usually see the gap for yourself. Search the comparison and look at '
              'what ranks. Vendor pages and thin lists, a forum thread or two, some posts with '
              'pricing from 2 years ago. Three strong, recent, detailed, independent '
              'comparisons pick a different pair.',
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': 'And you can usually see the gap for yourself. Search the comparison and look at '
             'what ranks. Vendor pages and thin lists, a forum thread or two, some posts with '
             'pricing from 2 years ago. Three strong, recent, detailed, independent '
             'comparisons pick a different pair.',
      'title': 'Comparison And Alternative Queries For Small Sites (2026) (The SEO Desk)',
      'url': 'https://www.youtube.com/watch?v=DyyeBcHNuHU&t=100s',
      'video_id': 'DyyeBcHNuHU'},
     {'author': 'SEO Affiliate Domination',
      'channel': 'SEO Affiliate Domination',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=yGAUu-eFDOM&t=104s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': "'t, aren't listed on either, either of the different platforms, and so I've "
              'already made most of the videos that you see here, most of the review videos, '
              "and the main reason I'm doing this is because these are buyer intent, keyword "
              'searches.',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': "'t, aren't listed on either, either of the different platforms, and so I've "
             'already made most of the videos that you see here, most of the review videos, '
             "and the main reason I'm doing this is because these are buyer intent, keyword "
             'searches.',
      'title': 'Kajabi Review: Kajabi vs LearnDash Affiliate SEO Strategy (SEO Affiliate '
               'Domination)',
      'url': 'https://www.youtube.com/watch?v=yGAUu-eFDOM&t=104s',
      'video_id': 'yGAUu-eFDOM'},
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
     {'author': 'Rock The Rankings: B2B SaaS GEO & SEO Agency',
      'channel': 'Rock The Rankings: B2B SaaS GEO & SEO Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:05](https://www.youtube.com/watch?v=DXrqf5Xqpd4&t=305s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': "You've not already built competitor comparison Pages they can be extremely "
              'beneficial for allowing you to control that narrative rather than G2 or capture '
              'to control it for you and allow you to position yourself in your particular '
              'Market.',
      'timestamp': 305,
      'timestamp_label': '[00:05:05]',
      'timestamp_seconds': 305,
      'tip': "You've not already built competitor comparison Pages they can be extremely "
             'beneficial for allowing you to control that narrative rather than G2 or capture '
             'to control it for you and allow you to position yourself in your particular '
             'Market.',
      'title': 'SaaS Competitor Comparison Pages: Why you NEED to Build them (Rock The '
               'Rankings: B2B SaaS GEO & SEO Agency)',
      'url': 'https://www.youtube.com/watch?v=DXrqf5Xqpd4&t=305s',
      'video_id': 'DXrqf5Xqpd4'},
     {'author': 'Everflow - Partner Marketing Platform',
      'channel': 'Everflow - Partner Marketing Platform',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:55](https://www.youtube.com/watch?v=FMpj69YFsHA&t=535s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
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
     {'author': 'Affiliate Marketing How To',
      'channel': 'Affiliate Marketing How To',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:17](https://www.youtube.com/watch?v=H6zM2ZJJCzk&t=317s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': "Here you will see he's got three posts only showing in this homepage he's got "
              "absolutely no navigation apart from that okay there's no site map to be found "
              'here but if I come in here and I do site colon what was it sonya artwork.com '
              "let's take that part.",
      'timestamp': 317,
      'timestamp_label': '[00:05:17]',
      'timestamp_seconds': 317,
      'tip': "Here you will see he's got three posts only showing in this homepage he's got "
             "absolutely no navigation apart from that okay there's no site map to be found "
             'here but if I come in here and I do site colon what was it sonya artwork.com '
             "let's take that part.",
      'title': "Clickfunnels Affiliate 'Mass Page Building' SEO Campaign Ranks For 763 "
               'Keywords! (Affiliate Marketing How To)',
      'url': 'https://www.youtube.com/watch?v=H6zM2ZJJCzk&t=317s',
      'video_id': 'H6zM2ZJJCzk'},
     {'author': '🔥 TOP Digital Products 🔥',
      'channel': '🔥 TOP Digital Products 🔥',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=J_fDLt9cLEg&t=60s)',
      'relevance': "Attributed practitioner commentary on '[Competitor] alternative/pricing' "
                   'buyer intent, Ad-Library spend-velocity mining, and private CPA bumps.',
      'source_type': 'video_pro_tip',
      'text': "For example, in the analytics section, we've got prompts here. There's some "
              'YouTube growth strategy section, YouTube keyword research results, YouTube '
              "video ranking services. As you can see, we've got lots of different options "
              'here, which is super cool.',
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': "For example, in the analytics section, we've got prompts here. There's some "
             'YouTube growth strategy section, YouTube keyword research results, YouTube video '
             "ranking services. As you can see, we've got lots of different options here, "
             'which is super cool.',
      'title': 'Profound Alternative: ZeroRank AI Review & Comparison 2026 (🔥 TOP Digital '
               'Products 🔥)',
      'url': 'https://www.youtube.com/watch?v=J_fDLt9cLEg&t=60s',
      'video_id': 'J_fDLt9cLEg'}],
 7: [{'author': 'Traffic Systems Affiliate',
      'channel': 'Traffic Systems Affiliate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:47](https://www.youtube.com/watch?v=A9oSfj8vCXE&t=47s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': 'I have had only 129 people click on my quiz funnel on my landing page okay and '
              'out of 129 people I have had 22 sales 22 actions basically 22 people decided '
              "they're going to buy okay and because I'm affiliate. You can see I have made "
              '€1,279.',
      'timestamp': 47,
      'timestamp_label': '[00:00:47]',
      'timestamp_seconds': 47,
      'tip': 'I have had only 129 people click on my quiz funnel on my landing page okay and '
             'out of 129 people I have had 22 sales 22 actions basically 22 people decided '
             "they're going to buy okay and because I'm affiliate. You can see I have made "
             '€1,279.',
      'title': 'How I Made $1,527+ in One Day with CPA Affiliate Marketing Using Google Ads '
               '(2026 Strategy!) (Traffic Systems Affiliate)',
      'url': 'https://www.youtube.com/watch?v=A9oSfj8vCXE&t=47s',
      'video_id': 'A9oSfj8vCXE'},
     {'author': 'Everflow - Partner Marketing Platform',
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
     {'author': 'Local Media HQ',
      'channel': 'Local Media HQ',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:35](https://www.youtube.com/watch?v=SFCvA5RqbgU&t=1355s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': 'And just so people are qu are clear, the way the assist does it is they take '
              "people through a quiz and then they'll show them some welcome offers on their "
              'thank you page. And to redeem those welcome offers, you have to go through and '
              'click and visit another site.',
      'timestamp': 1355,
      'timestamp_label': '[00:22:35]',
      'timestamp_seconds': 1355,
      'tip': 'And just so people are qu are clear, the way the assist does it is they take '
             "people through a quiz and then they'll show them some welcome offers on their "
             'thank you page. And to redeem those welcome offers, you have to go through and '
             'click and visit another site.',
      'title': 'How to Monetize Subscribers in the First 7 Days (Local Media HQ)',
      'url': 'https://www.youtube.com/watch?v=SFCvA5RqbgU&t=1355s',
      'video_id': 'SFCvA5RqbgU'},
     {'author': 'SparkLoop',
      'channel': 'SparkLoop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:52](https://www.youtube.com/watch?v=wW2Mpe3uxT8&t=1612s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': 'The growth the Growth Ax weekly or from the desk of Marketing Max now. This '
              'landing page converts roughly 35 to 40% on all channels. 70% on my on my '
              "Twitter bio, on my Instagram bio. Meta lowers it down, um but I've AB tested "
              'more than 200 variations of this page.',
      'timestamp': 1612,
      'timestamp_label': '[00:26:52]',
      'timestamp_seconds': 1612,
      'tip': 'The growth the Growth Ax weekly or from the desk of Marketing Max now. This '
             'landing page converts roughly 35 to 40% on all channels. 70% on my on my Twitter '
             "bio, on my Instagram bio. Meta lowers it down, um but I've AB tested more than "
             '200 variations of this page.',
      'title': 'How to Increase Newsletter Conversions From 7% to 35% | Marketing Max | Send & '
               'Grow 2.0 Ep. 7 (SparkLoop)',
      'url': 'https://www.youtube.com/watch?v=wW2Mpe3uxT8&t=1612s',
      'video_id': 'wW2Mpe3uxT8'},
     {'author': 'Eran Bucai',
      'channel': 'Eran Bucai',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:56](https://www.youtube.com/watch?v=zOMjnVrk_pQ&t=656s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': "Is actually recording the video and and uh all that good stuff so now that I've "
              "shown you all this uh I'll move on to the next step of uploading the video and "
              'setting up the thank you page so you can see how it fits as part of the funnel.',
      'timestamp': 656,
      'timestamp_label': '[00:10:56]',
      'timestamp_seconds': 656,
      'tip': "Is actually recording the video and and uh all that good stuff so now that I've "
             "shown you all this uh I'll move on to the next step of uploading the video and "
             'setting up the thank you page so you can see how it fits as part of the funnel.',
      'title': 'How to Record a Bridge Page Sales Video for Your Affiliate Funnel (Eran Bucai)',
      'url': 'https://www.youtube.com/watch?v=zOMjnVrk_pQ&t=656s',
      'video_id': 'zOMjnVrk_pQ'},
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
     {'author': 'Sell Your Service',
      'channel': 'Sell Your Service',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:28](https://www.youtube.com/watch?v=nNr0jVmba9w&t=448s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': 'Page maybe you work with like like Fitness coaches or something and your opin '
              'page with something along the lines of like lose 5K belly fat you know within '
              'six weeks or whatever it is the offer is basically this again.',
      'timestamp': 448,
      'timestamp_label': '[00:07:28]',
      'timestamp_seconds': 448,
      'tip': 'Page maybe you work with like like Fitness coaches or something and your opin '
             'page with something along the lines of like lose 5K belly fat you know within '
             'six weeks or whatever it is the offer is basically this again.',
      'title': "THE most valuable funnel training you'll ever watch (10,000 hours experience) "
               '(Sell Your Service)',
      'url': 'https://www.youtube.com/watch?v=nNr0jVmba9w&t=448s',
      'video_id': 'nNr0jVmba9w'},
     {'author': 'Jay Neyer',
      'channel': 'Jay Neyer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:51](https://www.youtube.com/watch?v=sDHZObLqdzI&t=291s)',
      'relevance': 'Attributed practitioner commentary on pre-sell comparison bridge pages, '
                   'interactive calculators, S2S postback deduplication, and ping-post/RSOC '
                   'flows.',
      'source_type': 'video_pro_tip',
      'text': "517 verified five-star reviews and first-time visitors weren't really seeing "
              "them. They don't always come through your homepage. They often come through a "
              'side door. Could be a collection page, could be a blog post, could be going '
              'directly to the product page.',
      'timestamp': 291,
      'timestamp_label': '[00:04:51]',
      'timestamp_seconds': 291,
      'tip': "517 verified five-star reviews and first-time visitors weren't really seeing "
             "them. They don't always come through your homepage. They often come through a "
             'side door. Could be a collection page, could be a blog post, could be going '
             'directly to the product page.',
      'title': 'How We Generated $211K While Building a High-Ticket Lead Funnel (Jay Neyer)',
      'url': 'https://www.youtube.com/watch?v=sDHZObLqdzI&t=291s',
      'video_id': 'sDHZObLqdzI'},
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
      'video_id': 'wj29osNl-zE'}],
 8: [{'author': 'Vendasta',
      'channel': 'Vendasta',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:57](https://www.youtube.com/watch?v=VGI3TKBcH6A&t=477s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'Audit your brand visibility. So ask ChatGpt or Perplexity what it knows about '
              'you. You want to add structured data like FAQs, reviews, and local schema to '
              'key pages. You want to match full question intent across your content.',
      'timestamp': 477,
      'timestamp_label': '[00:07:57]',
      'timestamp_seconds': 477,
      'tip': 'Audit your brand visibility. So ask ChatGpt or Perplexity what it knows about '
             'you. You want to add structured data like FAQs, reviews, and local schema to key '
             'pages. You want to match full question intent across your content.',
      'title': "Generative Engine Optimization (GEO) Explained Like You're 5 (Vendasta)",
      'url': 'https://www.youtube.com/watch?v=VGI3TKBcH6A&t=477s',
      'video_id': 'VGI3TKBcH6A'},
     {'author': 'trendos',
      'channel': 'trendos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=WBhqyUPJOro&t=25s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'The ones you get from ChatGPT, Perplexity, Gemini, Google AI overviews and '
              'Claude. To do GEO well, you need to know where AI actually gets its '
              'information. This is the most important idea in this whole video. AI has two '
              'sources and they work very differently.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': 'The ones you get from ChatGPT, Perplexity, Gemini, Google AI overviews and '
             'Claude. To do GEO well, you need to know where AI actually gets its information. '
             'This is the most important idea in this whole video. AI has two sources and they '
             'work very differently.',
      'title': 'What Is GEO? Generative Engine Optimization & How to Rank in AI Search '
               '(trendos)',
      'url': 'https://www.youtube.com/watch?v=WBhqyUPJOro&t=25s',
      'video_id': 'WBhqyUPJOro'},
     {'author': 'Chipp',
      'channel': 'Chipp',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:50](https://www.youtube.com/watch?v=Pw5w2kXNRyw&t=1190s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': "Now let's talk about grading our GEO and then I'm going to give you a tool to "
              'run this on yourself. So most sites are actually blocking AI by accident. So '
              'like Google will send scrapers around the web to get information.',
      'timestamp': 1190,
      'timestamp_label': '[00:19:50]',
      'timestamp_seconds': 1190,
      'tip': "Now let's talk about grading our GEO and then I'm going to give you a tool to "
             'run this on yourself. So most sites are actually blocking AI by accident. So '
             'like Google will send scrapers around the web to get information.',
      'title': 'GEO - AI SEO Workshop - Rank on ChatGPT, Claude, Google Gemini, Perplexity '
               'with Full Playbook (Chipp)',
      'url': 'https://www.youtube.com/watch?v=Pw5w2kXNRyw&t=1190s',
      'video_id': 'Pw5w2kXNRyw'},
     {'author': 'Marouane RHAFLI',
      'channel': 'Marouane RHAFLI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=H3cOFc-TX8I&t=21s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'The way now people search for information is changing. Instead of typing '
              'keywords now on Google, millions of people are using AI like ChatGPT, Gemini, '
              "Claude, or any other AI tool. That doesn't mean SEO has disappeared.",
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'The way now people search for information is changing. Instead of typing '
             'keywords now on Google, millions of people are using AI like ChatGPT, Gemini, '
             "Claude, or any other AI tool. That doesn't mean SEO has disappeared.",
      'title': 'How to Rank in AI Search Engines Using GEO - SEO course EP 11 (Marouane '
               'RHAFLI)',
      'url': 'https://www.youtube.com/watch?v=H3cOFc-TX8I&t=21s',
      'video_id': 'H3cOFc-TX8I'},
     {'author': 'Surfer Academy',
      'channel': 'Surfer Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:48](https://www.youtube.com/watch?v=bhTo8fDmr5I&t=708s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'Google supports, making sure that any of the relevant tags are applied to your '
              'pages. More often than not, these are the same types of schema that AI tools '
              'are using to identify your content.',
      'timestamp': 708,
      'timestamp_label': '[00:11:48]',
      'timestamp_seconds': 708,
      'tip': 'Google supports, making sure that any of the relevant tags are applied to your '
             'pages. More often than not, these are the same types of schema that AI tools are '
             'using to identify your content.',
      'title': 'How to Dominate AI Search Results in 2026 (ChatGPT, AI Overviews & More) '
               '(Surfer Academy)',
      'url': 'https://www.youtube.com/watch?v=bhTo8fDmr5I&t=708s',
      'video_id': 'bhTo8fDmr5I'},
     {'author': 'Da Hoang',
      'channel': 'Da Hoang',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:22](https://www.youtube.com/watch?v=44ifmL6JCs8&t=82s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'Below it, a data table: power, top speed, cabin noise. Then human proof: a '
              'quote from the technical director, and a test-drive video. Then real '
              'maintenance costs, and five FAQs marked up as schema. AI drafts the outline, '
              'the translations, and the table code.',
      'timestamp': 82,
      'timestamp_label': '[00:01:22]',
      'timestamp_seconds': 82,
      'tip': 'Below it, a data table: power, top speed, cabin noise. Then human proof: a quote '
             'from the technical director, and a test-drive video. Then real maintenance '
             'costs, and five FAQs marked up as schema. AI drafts the outline, the '
             'translations, and the table code.',
      'title': 'Generative Engine Optimization: The 5-Part GEO Playbook (Da Hoang)',
      'url': 'https://www.youtube.com/watch?v=44ifmL6JCs8&t=82s',
      'video_id': '44ifmL6JCs8'},
     {'author': 'SEO Affiliate Domination',
      'channel': 'SEO Affiliate Domination',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:51](https://www.youtube.com/watch?v=Kol8N2k5VQw&t=171s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'So I just want to show this to you in Google and then YouTube because there are '
              'a bunch of SEO tools out there that you can use for like keyword research, like '
              "Ahrefs and SEMrush. And then there's a whole bunch of other, uh, lesser "
              'expensive ones.',
      'timestamp': 171,
      'timestamp_label': '[00:02:51]',
      'timestamp_seconds': 171,
      'tip': 'So I just want to show this to you in Google and then YouTube because there are '
             'a bunch of SEO tools out there that you can use for like keyword research, like '
             "Ahrefs and SEMrush. And then there's a whole bunch of other, uh, lesser "
             'expensive ones.',
      'title': 'Kajabi Review: Kajabi vs Gumroad, Plus SEO Strategy (SEO Affiliate Domination)',
      'url': 'https://www.youtube.com/watch?v=Kol8N2k5VQw&t=171s',
      'video_id': 'Kol8N2k5VQw'},
     {'author': '🔥 TOP Digital Products 🔥',
      'channel': '🔥 TOP Digital Products 🔥',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:40](https://www.youtube.com/watch?v=J_fDLt9cLEg&t=160s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': "Now, there's visibility and tracking across actually 17 different AI engines, "
              "which is absolutely cool to know as well. So, of course, you've got your "
              "ChatGPT, you've got your Claude, Gemini, Perplexity, Google AI Overviews, we've "
              'got Grok, as well as Bing Copilot as well.',
      'timestamp': 160,
      'timestamp_label': '[00:02:40]',
      'timestamp_seconds': 160,
      'tip': "Now, there's visibility and tracking across actually 17 different AI engines, "
             "which is absolutely cool to know as well. So, of course, you've got your "
             "ChatGPT, you've got your Claude, Gemini, Perplexity, Google AI Overviews, we've "
             'got Grok, as well as Bing Copilot as well.',
      'title': 'Profound Alternative: ZeroRank AI Review & Comparison 2026 (🔥 TOP Digital '
               'Products 🔥)',
      'url': 'https://www.youtube.com/watch?v=J_fDLt9cLEg&t=160s',
      'video_id': 'J_fDLt9cLEg'},
     {'author': 'E-commerce Berlin Expo',
      'channel': 'E-commerce Berlin Expo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:48](https://www.youtube.com/watch?v=ELiV_0RMFr4&t=1068s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'So the LLM is not being able to answer your question just from their training '
              'data. Then they will reach out and enhance their information with the '
              'information they can find on the web.',
      'timestamp': 1068,
      'timestamp_label': '[00:17:48]',
      'timestamp_seconds': 1068,
      'tip': 'So the LLM is not being able to answer your question just from their training '
             'data. Then they will reach out and enhance their information with the '
             'information they can find on the web.',
      'title': 'Generative Engine Optimization: How to Build Visibility in AI Searches like '
               'ChatGPT and Perplexity (E-commerce Berlin Expo)',
      'url': 'https://www.youtube.com/watch?v=ELiV_0RMFr4&t=1068s',
      'video_id': 'ELiV_0RMFr4'},
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
     {'author': 'SparkLoop',
      'channel': 'SparkLoop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:16](https://www.youtube.com/watch?v=u87gia-3VVo&t=136s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'Into our beehive account and then under settings website analytics we are going '
              "to paste this tag manager pixel ID and we'll hit save there from there we'll be "
              "brought back to this page and we'll verify that our tracking script is working "
              'properly once everything is set.',
      'timestamp': 136,
      'timestamp_label': '[00:02:16]',
      'timestamp_seconds': 136,
      'tip': 'Into our beehive account and then under settings website analytics we are going '
             "to paste this tag manager pixel ID and we'll hit save there from there we'll be "
             "brought back to this page and we'll verify that our tracking script is working "
             'properly once everything is set.',
      'title': 'Connecting SparkLoop to Beehiiv: Get paid to recommend top newsletters to your '
               'audience (SparkLoop)',
      'url': 'https://www.youtube.com/watch?v=u87gia-3VVo&t=136s',
      'video_id': 'u87gia-3VVo'},
     {'author': 'Everflow - Partner Marketing Platform',
      'channel': 'Everflow - Partner Marketing Platform',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:52](https://www.youtube.com/watch?v=kLc_7B0eexA&t=172s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': "Um, and if you have uh a person like a head of data, then you're ready to use "
              'something like the Everflow Fire Hose to pipe that data into Snowflake or Domo '
              'for executive highle reporting. Additionally, you could use the customer value '
              'tool.',
      'timestamp': 172,
      'timestamp_label': '[00:02:52]',
      'timestamp_seconds': 172,
      'tip': "Um, and if you have uh a person like a head of data, then you're ready to use "
             'something like the Everflow Fire Hose to pipe that data into Snowflake or Domo '
             'for executive highle reporting. Additionally, you could use the customer value '
             'tool.',
      'title': 'Connect Everflow to Your CRM: Pay on Quality, Not Just Quantity | Everflow '
               'Mini Webinars (Everflow - Partner Marketing Platform)',
      'url': 'https://www.youtube.com/watch?v=kLc_7B0eexA&t=172s',
      'video_id': 'kLc_7B0eexA'},
     {'author': 'OfferVault',
      'channel': 'OfferVault',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:36](https://www.youtube.com/watch?v=rsmZ9FBIPks&t=1536s)',
      'relevance': 'Attributed practitioner commentary on S2S attribution stacks, contextual '
                   'Chrome extensions, first-party identity pixels, and AI-Overview/GEO '
                   'citations.',
      'source_type': 'video_pro_tip',
      'text': 'Watching this thank you to brother and enjoy the rest of the weather out there '
              "in California we'll see you soon all right yes thank you so much I'll see you "
              'sooner than later all right.',
      'timestamp': 1536,
      'timestamp_label': '[00:25:36]',
      'timestamp_seconds': 1536,
      'tip': 'Watching this thank you to brother and enjoy the rest of the weather out there '
             "in California we'll see you soon all right yes thank you so much I'll see you "
             'sooner than later all right.',
      'title': 'Earnings Per Call: Melissa Lai, Senior Business Development Manager at Ringba '
               '(OfferVault)',
      'url': 'https://www.youtube.com/watch?v=rsmZ9FBIPks&t=1536s',
      'video_id': 'rsmZ9FBIPks'},
     {'author': 'Rank Math SEO',
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
      'video_id': 'boGwMjAxtuk'}],
 9: [{'author': 'Rabbit Hole Radio',
      'channel': 'Rabbit Hole Radio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:45:15](https://www.youtube.com/watch?v=MIx20-uBG6s&t=2715s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'As soon as you begin facilitating financial transactions based on your '
              'recommendations you enter the crosshairs of federal regulation. The rules of '
              'the game trust in FTC compliance.',
      'timestamp': 2715,
      'timestamp_label': '[00:45:15]',
      'timestamp_seconds': 2715,
      'tip': 'As soon as you begin facilitating financial transactions based on your '
             'recommendations you enter the crosshairs of federal regulation. The rules of the '
             'game trust in FTC compliance.',
      'title': '2026 High Ticket Affiliate Marketing Blueprint [Deep Dive] (Rabbit Hole Radio)',
      'url': 'https://www.youtube.com/watch?v=MIx20-uBG6s&t=2715s',
      'video_id': 'MIx20-uBG6s'},
     {'author': 'Hustle Audit',
      'channel': 'Hustle Audit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:40](https://www.youtube.com/watch?v=3FcVWGZ_SGY&t=160s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'You still owe your own clear disclosure on top of it. Second, the definition of '
              'an endorsement was widened to explicitly capture fake reviews, paid for star '
              'ratings, and even tags of a brand in a photo. A tag can be an endorsement.',
      'timestamp': 160,
      'timestamp_label': '[00:02:40]',
      'timestamp_seconds': 160,
      'tip': 'You still owe your own clear disclosure on top of it. Second, the definition of '
             'an endorsement was widened to explicitly capture fake reviews, paid for star '
             'ratings, and even tags of a brand in a photo. A tag can be an endorsement.',
      'title': 'What The FTC Actually Requires You To Disclose As An Affiliate (Hustle Audit)',
      'url': 'https://www.youtube.com/watch?v=3FcVWGZ_SGY&t=160s',
      'video_id': '3FcVWGZ_SGY'},
     {'author': 'eternalsoulwriter',
      'channel': 'eternalsoulwriter',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:41](https://www.youtube.com/watch?v=5myKyThXemw&t=821s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': "'s why I always encourage reading official documentation instead of relying "
              'only on YouTube videos including mine. So I will leave the links to the '
              'official Amazon policy and the FTC disclosure guide in the description box '
              'below so you can read them for yourself.',
      'timestamp': 821,
      'timestamp_label': '[00:13:41]',
      'timestamp_seconds': 821,
      'tip': "'s why I always encourage reading official documentation instead of relying only "
             'on YouTube videos including mine. So I will leave the links to the official '
             'Amazon policy and the FTC disclosure guide in the description box below so you '
             'can read them for yourself.',
      'title': 'FTC & Amazon Affiliate Disclosures Explained (Avoid These Costly Mistakes) '
               '#amazoninfluencer (eternalsoulwriter)',
      'url': 'https://www.youtube.com/watch?v=5myKyThXemw&t=821s',
      'video_id': '5myKyThXemw'},
     {'author': 'Alston Godbolt',
      'channel': 'Alston Godbolt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:21](https://www.youtube.com/watch?v=TpYEmQ9njyk&t=201s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'Influencers must make disclosures clear and conspicuous so if you have an '
              'agreement in place with a brand with a company you need to notify that '
              'somewhere you need to list that somewhere now.',
      'timestamp': 201,
      'timestamp_label': '[00:03:21]',
      'timestamp_seconds': 201,
      'tip': 'Influencers must make disclosures clear and conspicuous so if you have an '
             'agreement in place with a brand with a company you need to notify that somewhere '
             'you need to list that somewhere now.',
      'title': 'New FTC Guidelines For Affiliate & Influencer MarketerS Must Watch Before '
               'Making Your Next Video (Alston Godbolt)',
      'url': 'https://www.youtube.com/watch?v=TpYEmQ9njyk&t=201s',
      'video_id': 'TpYEmQ9njyk'},
     {'author': 'Digital Trailblazer',
      'channel': 'Digital Trailblazer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=EJWC8jVfIko&t=21s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': "'s going to be there, and you don't get in trouble with the FTC. Now, the FTC "
              'governs folks here in America, the Federal Trade Commission, it sets up the '
              "rules and laws that we need to follow whenever we're advertising online, "
              'offline, wherever.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "'s going to be there, and you don't get in trouble with the FTC. Now, the FTC "
             'governs folks here in America, the Federal Trade Commission, it sets up the '
             "rules and laws that we need to follow whenever we're advertising online, "
             'offline, wherever.',
      'title': 'FTC Compliant | How To Play It Safe for Beginner Affiliate Marketing (Digital '
               'Trailblazer)',
      'url': 'https://www.youtube.com/watch?v=EJWC8jVfIko&t=21s',
      'video_id': 'EJWC8jVfIko'},
     {'author': 'Paul Rooney',
      'channel': 'Paul Rooney',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:22](https://www.youtube.com/watch?v=91G7BkMV6A8&t=82s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'The first reason is if competitors are bidding on your terms and just generally '
              "across the board, we're finding that Google is expanding more and more search "
              'terms to actually bid on different competitors, different brand names.',
      'timestamp': 82,
      'timestamp_label': '[00:01:22]',
      'timestamp_seconds': 82,
      'tip': 'The first reason is if competitors are bidding on your terms and just generally '
             "across the board, we're finding that Google is expanding more and more search "
             'terms to actually bid on different competitors, different brand names.',
      'title': 'Should You Bid on Your Own Brand Name in Google Ads? (Paul Rooney)',
      'url': 'https://www.youtube.com/watch?v=91G7BkMV6A8&t=82s',
      'video_id': '91G7BkMV6A8'},
     {'author': 'Justin Moore',
      'channel': 'Justin Moore',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:48](https://www.youtube.com/watch?v=oQhn2MkCyK4&t=228s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': "If you thought the product was terrible, You can't say it's great. And you "
              "can't make up claims about a product that would require proof that The brand "
              "doesn't have like it cures these eight diseases or something.",
      'timestamp': 228,
      'timestamp_label': '[00:03:48]',
      'timestamp_seconds': 228,
      'tip': "If you thought the product was terrible, You can't say it's great. And you can't "
             "make up claims about a product that would require proof that The brand doesn't "
             'have like it cures these eight diseases or something.',
      'title': 'FTC Disclosures 101 for Social Media Influencers & Creators (Justin Moore)',
      'url': 'https://www.youtube.com/watch?v=oQhn2MkCyK4&t=228s',
      'video_id': 'oQhn2MkCyK4'},
     {'author': 'Jennings Strouss',
      'channel': 'Jennings Strouss',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:33](https://www.youtube.com/watch?v=zMHcPlc6Nvc&t=153s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'How do you make the proper disclosures in that? You know, you can have somebody '
              'uh issue a tweet that says, "I\'ve lost, you know, four 40 pounds on this diet '
              'pill. I\'ve taken one one day a week for two days." Well, that that\'s an '
              'endorsement.',
      'timestamp': 153,
      'timestamp_label': '[00:02:33]',
      'timestamp_seconds': 153,
      'tip': 'How do you make the proper disclosures in that? You know, you can have somebody '
             'uh issue a tweet that says, "I\'ve lost, you know, four 40 pounds on this diet '
             'pill. I\'ve taken one one day a week for two days." Well, that that\'s an '
             'endorsement.',
      'title': 'Updated FTC Guidelines on Internet Advertising & Marketing (Jennings Strouss)',
      'url': 'https://www.youtube.com/watch?v=zMHcPlc6Nvc&t=153s',
      'video_id': 'zMHcPlc6Nvc'},
     {'author': 'Venable LLP',
      'channel': 'Venable LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:33:34](https://www.youtube.com/watch?v=BY7l2XbdWPc&t=2014s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': 'Respect to these types of disclosures that in and of themselves create '
              'deception before we move on we want to give the cle password because we always '
              'forget to give it and that password or for the cle credit is endorsement 2022 '
              'endorsement 2022.',
      'timestamp': 2014,
      'timestamp_label': '[00:33:34]',
      'timestamp_seconds': 2014,
      'tip': 'Respect to these types of disclosures that in and of themselves create deception '
             'before we move on we want to give the cle password because we always forget to '
             'give it and that password or for the cle credit is endorsement 2022 endorsement '
             '2022.',
      'title': 'What You Need to Know About FTC’s Proposed Changes to Its Endorsement Guides '
               '(Venable LLP)',
      'url': 'https://www.youtube.com/watch?v=BY7l2XbdWPc&t=2014s',
      'video_id': 'BY7l2XbdWPc'},
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
     {'author': 'Seeking Profit',
      'channel': 'Seeking Profit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:59](https://www.youtube.com/watch?v=fo-OxsDnUVQ&t=1379s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
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
     {'author': 'Bens Review Videos',
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
     {'author': 'Cheryl Phan',
      'channel': 'Cheryl Phan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:10](https://www.youtube.com/watch?v=fnCkagoHXx0&t=250s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': "That's all that's all about so anyway I hope that was helpful and if you have "
              "any questions please reach out and let me know I'm here to help you and do you "
              'all have a blessed day bye-bye.',
      'timestamp': 250,
      'timestamp_label': '[00:04:10]',
      'timestamp_seconds': 250,
      'tip': "That's all that's all about so anyway I hope that was helpful and if you have "
             "any questions please reach out and let me know I'm here to help you and do you "
             'all have a blessed day bye-bye.',
      'title': 'Affiliate Link Disclosure Rules for FTC (Cheryl Phan)',
      'url': 'https://www.youtube.com/watch?v=fnCkagoHXx0&t=250s',
      'video_id': 'fnCkagoHXx0'},
     {'author': 'Guaranteed PPC',
      'channel': 'Guaranteed PPC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:41](https://www.youtube.com/watch?v=ceHQ0dOvobM&t=461s)',
      'relevance': 'Attributed practitioner commentary on FTC 16 CFR Part 255 disclosures, '
                   'authorized brand-bidding riders, TCPA one-to-one consent, and regulated '
                   'niches.',
      'source_type': 'video_pro_tip',
      'text': "'t have four ads above it now. I've even seen people bitching about this that "
              "are not even in the advertising industry anymore because there's a term called "
              'enshittification.',
      'timestamp': 461,
      'timestamp_label': '[00:07:41]',
      'timestamp_seconds': 461,
      'tip': "'t have four ads above it now. I've even seen people bitching about this that "
             "are not even in the advertising industry anymore because there's a term called "
             'enshittification.',
      'title': "💸 Brand Bidding On Google ADs - What People Don't Know About This That Loses "
               'Them Money! 🔍 (Guaranteed PPC)',
      'url': 'https://www.youtube.com/watch?v=ceHQ0dOvobM&t=461s',
      'video_id': 'ceHQ0dOvobM'}],
 10: [{'author': 'Michael Bashi',
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
      {'author': 'Powerhouse Affiliate',
       'channel': 'Powerhouse Affiliate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:00](https://www.youtube.com/watch?v=hI7Wb7R-89g&t=480s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': 'Now once you find a video, you can either be the person in the video. You can '
               'create the video yourself with your own camera like I do on YouTube for this '
               'channel.',
       'timestamp': 480,
       'timestamp_label': '[00:08:00]',
       'timestamp_seconds': 480,
       'tip': 'Now once you find a video, you can either be the person in the video. You can '
              'create the video yourself with your own camera like I do on YouTube for this '
              'channel.',
       'title': 'The "Lazy" Way to 1,000,000 Clicks (Free Viral AI Traffic - STEAL THIS!) '
                '(Powerhouse Affiliate)',
       'url': 'https://www.youtube.com/watch?v=hI7Wb7R-89g&t=480s',
       'video_id': 'hI7Wb7R-89g'},
      {'author': 'Vasco Aires',
       'channel': 'Vasco Aires',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:38:37](https://www.youtube.com/watch?v=C2ne_saHpSs&t=2317s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
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
      {'author': 'Ahrefs',
       'channel': 'Ahrefs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:28](https://www.youtube.com/watch?v=tiW6xRYSXmM&t=88s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': "They're researching YouTube, Reddit, forums, review sites, and using all of it "
               'to decide who to recommend. In fact, 86% of the top cited sources are unique '
               'to each AI assistant. Google AI overviews lean heavily on YouTube, Reddit, and '
               'Quora.',
       'timestamp': 88,
       'timestamp_label': '[00:01:28]',
       'timestamp_seconds': 88,
       'tip': "They're researching YouTube, Reddit, forums, review sites, and using all of it "
              'to decide who to recommend. In fact, 86% of the top cited sources are unique to '
              'each AI assistant. Google AI overviews lean heavily on YouTube, Reddit, and '
              'Quora.',
       'title': "SEO in 2026: How I'd Rank in Google in the AI Era (Ahrefs)",
       'url': 'https://www.youtube.com/watch?v=tiW6xRYSXmM&t=88s',
       'video_id': 'tiW6xRYSXmM'},
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
      {'author': 'SparkLoop',
       'channel': 'SparkLoop',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:20:49](https://www.youtube.com/watch?v=KrUPlyUxncE&t=1249s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': 'All of those things are decreasing the number of people that are going to '
               "actually click through the ad because we you know, it's the same way on social "
               'media or anything like you know, or especially websites. Websites is '
               'ridiculous with banner ads and all that stuff.',
       'timestamp': 1249,
       'timestamp_label': '[00:20:49]',
       'timestamp_seconds': 1249,
       'tip': 'All of those things are decreasing the number of people that are going to '
              "actually click through the ad because we you know, it's the same way on social "
              'media or anything like you know, or especially websites. Websites is ridiculous '
              'with banner ads and all that stuff.',
       'title': 'Coaching Session: Tips from a Newsletter Pro — with Josh Spector of For The '
                'Interested (SparkLoop)',
       'url': 'https://www.youtube.com/watch?v=KrUPlyUxncE&t=1249s',
       'video_id': 'KrUPlyUxncE'},
      {'author': 'Marcel Sattler | Leading Native Advertising Expert',
       'channel': 'Marcel Sattler | Leading Native Advertising Expert',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:35](https://www.youtube.com/watch?v=7JPuuysCuKw&t=335s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
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
       'title': 'Affiliate Marketing + Native Ads: Make Money with this Strategy on Taboola '
                'and Outbrain (Marcel Sattler | Leading Native Advertising Expert)',
       'url': 'https://www.youtube.com/watch?v=7JPuuysCuKw&t=335s',
       'video_id': '7JPuuysCuKw'},
      {'author': 'SparkLoop',
       'channel': 'SparkLoop',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:35](https://www.youtube.com/watch?v=q1jLTPNMaCY&t=995s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': 'And nearly everybody has one or two that they can ask. So, at SparkLoop, for '
               "example, we just ask, you know, what's your biggest challenge right now with "
               'your newsletter?',
       'timestamp': 995,
       'timestamp_label': '[00:16:35]',
       'timestamp_seconds': 995,
       'tip': 'And nearly everybody has one or two that they can ask. So, at SparkLoop, for '
              "example, we just ask, you know, what's your biggest challenge right now with "
              'your newsletter?',
       'title': 'Free Newsletter Masterclass: Turn New Readers into Revenue (SparkLoop)',
       'url': 'https://www.youtube.com/watch?v=q1jLTPNMaCY&t=995s',
       'video_id': 'q1jLTPNMaCY'},
      {'author': 'Jackie Strohl',
       'channel': 'Jackie Strohl',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:29](https://www.youtube.com/watch?v=JVbzH2BD68w&t=329s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': 'Thank you guys so much for watching this video I truly appreciate each and '
               'every one of you get out there make it happen and make your dreams come true '
               'bye for now.',
       'timestamp': 329,
       'timestamp_label': '[00:05:29]',
       'timestamp_seconds': 329,
       'tip': 'Thank you guys so much for watching this video I truly appreciate each and '
              'every one of you get out there make it happen and make your dreams come true '
              'bye for now.',
       'title': 'The Most profitable business model  - 4 steps to High ticket commissions '
                '(Jackie Strohl)',
       'url': 'https://www.youtube.com/watch?v=JVbzH2BD68w&t=329s',
       'video_id': 'JVbzH2BD68w'},
      {'author': 'Charlie Chang',
       'channel': 'Charlie Chang',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:29:27](https://www.youtube.com/watch?v=Gj4Zx6Vj7ko&t=1767s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': 'Cover things like building your own online business investing in personal '
               "finance thank you so much for sticking with me for this long and I'll see you "
               'in the next video peace.',
       'timestamp': 1767,
       'timestamp_label': '[00:29:27]',
       'timestamp_seconds': 1767,
       'tip': 'Cover things like building your own online business investing in personal '
              "finance thank you so much for sticking with me for this long and I'll see you "
              'in the next video peace.',
       'title': 'The ONLY Affiliate Marketing Tutorial You Need: Ultimate Step-by-Step for '
                'Beginners (Charlie Chang)',
       'url': 'https://www.youtube.com/watch?v=Gj4Zx6Vj7ko&t=1767s',
       'video_id': 'Gj4Zx6Vj7ko'},
      {'author': 'Wanda Zelaya Real Estate Channel',
       'channel': 'Wanda Zelaya Real Estate Channel',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:50](https://www.youtube.com/watch?v=bHypgQE6iLY&t=530s)',
       'relevance': 'Attributed practitioner commentary on faceless YouTube search capture, '
                    'SparkLoop newsletter co-reg, Reddit/Pinterest SERPs, and paid-to-organic '
                    'loops.',
       'source_type': 'video_pro_tip',
       'text': 'Only one dealing with this am I blowing this completely out of proportion or '
               "have any of you guys had the same issues I'd love to hear from you so please "
               'leave a comment below thanks thanks for watching fellow creator.',
       'timestamp': 530,
       'timestamp_label': '[00:08:50]',
       'timestamp_seconds': 530,
       'tip': 'Only one dealing with this am I blowing this completely out of proportion or '
              "have any of you guys had the same issues I'd love to hear from you so please "
              'leave a comment below thanks thanks for watching fellow creator.',
       'title': 'The DARK SIDE of Paid Recommendations: My Sparkloop & Kit Rejection Story '
                '(Wanda Zelaya Real Estate Channel)',
       'url': 'https://www.youtube.com/watch?v=bHypgQE6iLY&t=530s',
       'video_id': 'bHypgQE6iLY'}],
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
      {'author': 'Ringba',
       'channel': 'Ringba',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:33](https://www.youtube.com/watch?v=a4Aa0kexuh8&t=153s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': 'For example, the buyer may have a concurrency cap that is shared among '
               'multiple affiliates that may not allocate any specific affiliate guaranteed '
               'capacity. This will cause dropped calls to not be paid for and make it almost '
               'impossible to buy paid media.',
       'timestamp': 153,
       'timestamp_label': '[00:02:33]',
       'timestamp_seconds': 153,
       'tip': 'For example, the buyer may have a concurrency cap that is shared among multiple '
              'affiliates that may not allocate any specific affiliate guaranteed capacity. '
              'This will cause dropped calls to not be paid for and make it almost impossible '
              'to buy paid media.',
       'title': 'Why Pay Per Call Affiliates Need Their Own Call Tracking? (Ringba)',
       'url': 'https://www.youtube.com/watch?v=a4Aa0kexuh8&t=153s',
       'video_id': 'a4Aa0kexuh8'},
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
      {'author': 'Luke Pisacane',
       'channel': 'Luke Pisacane',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:09](https://www.youtube.com/watch?v=0mw4i-MSxoc&t=849s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': "'re not having to actually manage this client's inbox and the inbox manager "
               "can solely handle this responsibility so that you're out of the inbox manager "
               "itself. Now, the second hire that you're going to want to make is a tech "
               'manager.',
       'timestamp': 849,
       'timestamp_label': '[00:14:09]',
       'timestamp_seconds': 849,
       'tip': "'re not having to actually manage this client's inbox and the inbox manager can "
              "solely handle this responsibility so that you're out of the inbox manager "
              "itself. Now, the second hire that you're going to want to make is a tech "
              'manager.',
       'title': 'how i made $917,000 with AI Lead Gen working 1-2 hours a day (copy me) (Luke '
                'Pisacane)',
       'url': 'https://www.youtube.com/watch?v=0mw4i-MSxoc&t=849s',
       'video_id': '0mw4i-MSxoc'},
      {'author': 'Jitendra Vaswani',
       'channel': 'Jitendra Vaswani',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:40](https://www.youtube.com/watch?v=E6Nq0auvJ-8&t=220s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': 'We sometimes go to festivals together. And I asked him like, "Hey, you know, '
               'my portfolio is doing better after the helpful content update because we '
               'switched everything to Google Ads." I I want to look for a a good paid ads '
               'agency. We find new affiliate sites.',
       'timestamp': 220,
       'timestamp_label': '[00:03:40]',
       'timestamp_seconds': 220,
       'tip': 'We sometimes go to festivals together. And I asked him like, "Hey, you know, my '
              'portfolio is doing better after the helpful content update because we switched '
              'everything to Google Ads." I I want to look for a a good paid ads agency. We '
              'find new affiliate sites.',
       'title': 'Neils Zee On Making 7 Fig With Google Ads Affiliate Marketing (Jitendra '
                'Vaswani)',
       'url': 'https://www.youtube.com/watch?v=E6Nq0auvJ-8&t=220s',
       'video_id': 'E6Nq0auvJ-8'},
      {'author': 'Digital Niche Agency',
       'channel': 'Digital Niche Agency',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:20:09](https://www.youtube.com/watch?v=ClT7JBQFJGA&t=1209s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': 'Buyer is facilities, finance or sustainability leader The desired conversation '
               'is a portfolio feasibility assessment. Audience signals, sales calls ask about '
               'upfront cost savings.',
       'timestamp': 1209,
       'timestamp_label': '[00:20:09]',
       'timestamp_seconds': 1209,
       'tip': 'Buyer is facilities, finance or sustainability leader The desired conversation '
              'is a portfolio feasibility assessment. Audience signals, sales calls ask about '
              'upfront cost savings.',
       'title': 'How to Rank on ChatGPT and Claude | Generative Engine Optimization (GEO) '
                'Webinar (Digital Niche Agency)',
       'url': 'https://www.youtube.com/watch?v=ClT7JBQFJGA&t=1209s',
       'video_id': 'ClT7JBQFJGA'},
      {'author': 'Ahrefs',
       'channel': 'Ahrefs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:46](https://www.youtube.com/watch?v=SLm9lJnBvyo&t=226s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': "But if you're all caught up, then let's talk about perhaps the most efficient "
               "way to map affiliate topics. And that's by creating product clusters. A "
               'product cluster is a simple content structure that connects a general '
               'comparison post with multiple product review posts.',
       'timestamp': 226,
       'timestamp_label': '[00:03:46]',
       'timestamp_seconds': 226,
       'tip': "But if you're all caught up, then let's talk about perhaps the most efficient "
              "way to map affiliate topics. And that's by creating product clusters. A product "
              'cluster is a simple content structure that connects a general comparison post '
              'with multiple product review posts.',
       'title': 'Content Strategy for Affiliate Marketing Sites [3.3] (Ahrefs)',
       'url': 'https://www.youtube.com/watch?v=SLm9lJnBvyo&t=226s',
       'video_id': 'SLm9lJnBvyo'},
      {'author': 'Matthew Zivkovic',
       'channel': 'Matthew Zivkovic',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:32:47](https://www.youtube.com/watch?v=7lpBAuhtQBY&t=1967s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': 'Working make some money then get then start sourcing some new accounts and '
               "start looking to scale this up so let's go over some questions that came on "
               'from the uh from during the webinar so a couple questions.',
       'timestamp': 1967,
       'timestamp_label': '[00:32:47]',
       'timestamp_seconds': 1967,
       'tip': 'Working make some money then get then start sourcing some new accounts and '
              "start looking to scale this up so let's go over some questions that came on "
              'from the uh from during the webinar so a couple questions.',
       'title': 'Facebook Marketplace Training - Lead Smart - Pay Per Call Affiliate Marketing '
                '(Matthew Zivkovic)',
       'url': 'https://www.youtube.com/watch?v=7lpBAuhtQBY&t=1967s',
       'video_id': '7lpBAuhtQBY'},
      {'author': 'Aldo Gomes',
       'channel': 'Aldo Gomes',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:03](https://www.youtube.com/watch?v=TpcIvpsamnM&t=483s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': 'Running these campaigns will tell you if there is potential or not thank you '
               'very much for watching consider liking and subscribing if you enjoy content '
               "like this check out more videos like this on the channel and I'll see you next "
               'time.',
       'timestamp': 483,
       'timestamp_label': '[00:08:03]',
       'timestamp_seconds': 483,
       'tip': 'Running these campaigns will tell you if there is potential or not thank you '
              'very much for watching consider liking and subscribing if you enjoy content '
              "like this check out more videos like this on the channel and I'll see you next "
              'time.',
       'title': 'The Best Way to Advertise on Google as an Affiliate (Results in 3 Days) (Aldo '
                'Gomes)',
       'url': 'https://www.youtube.com/watch?v=TpcIvpsamnM&t=483s',
       'video_id': 'TpcIvpsamnM'},
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
      {'author': 'Ecom Chief',
       'channel': 'Ecom Chief',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:56](https://www.youtube.com/watch?v=iVK1QrJwylk&t=176s)',
       'relevance': 'Attributed practitioner commentary on running a 3-to-5 person referral '
                    'portfolio, capping single-merchant concentration, and 3x-4.5x site exits.',
       'source_type': 'video_pro_tip',
       'text': 'AI writing tools review site for $95,000. At the time of purchase, the '
               'starting profit was $2,400 per month. Over the following year, the buyer '
               'launched a YouTube channel, expanded the content to include AI design tools, '
               'and created a lead generation email course.',
       'timestamp': 176,
       'timestamp_label': '[00:02:56]',
       'timestamp_seconds': 176,
       'tip': 'AI writing tools review site for $95,000. At the time of purchase, the starting '
              'profit was $2,400 per month. Over the following year, the buyer launched a '
              'YouTube channel, expanded the content to include AI design tools, and created a '
              'lead generation email course.',
       'title': 'How to Buy and Grow an AI Affiliate Website in 2026 (High-Ticket SaaS '
                'Commissions) (Ecom Chief)',
       'url': 'https://www.youtube.com/watch?v=iVK1QrJwylk&t=176s',
       'video_id': 'iVK1QrJwylk'},
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
       'video_id': 'XKj8PVuNBOs'}],
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
      {'author': 'Powerhouse Affiliate',
       'channel': 'Powerhouse Affiliate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:30](https://www.youtube.com/watch?v=cuIiOD3qJ2o&t=150s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': "I'm going to show you the pages and and how AI was able to do it so quickly. "
               "With this particular offer, the first thing I'm going to be doing is looking "
               'for winning ads.',
       'timestamp': 150,
       'timestamp_label': '[00:02:30]',
       'timestamp_seconds': 150,
       'tip': "I'm going to show you the pages and and how AI was able to do it so quickly. "
              "With this particular offer, the first thing I'm going to be doing is looking "
              'for winning ads.',
       'title': 'The "Lazy" Way to Make $100/Day With Facebook Ads (Affiliate Arbitrage) '
                '(Powerhouse Affiliate)',
       'url': 'https://www.youtube.com/watch?v=cuIiOD3qJ2o&t=150s',
       'video_id': 'cuIiOD3qJ2o'},
      {'author': 'Traffic Systems Affiliate',
       'channel': 'Traffic Systems Affiliate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:01](https://www.youtube.com/watch?v=RgtHvwDuzDs&t=181s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': "That's meaning you can make 24 sales a week with 100 USD commissions, okay? Or "
               "you can make only five sales per week with $500 commissions, you're making "
               '$10,000 every single month passively. Now, all you have to do is install one '
               'affiliate campaign on ClickBank.',
       'timestamp': 181,
       'timestamp_label': '[00:03:01]',
       'timestamp_seconds': 181,
       'tip': "That's meaning you can make 24 sales a week with 100 USD commissions, okay? Or "
              "you can make only five sales per week with $500 commissions, you're making "
              '$10,000 every single month passively. Now, all you have to do is install one '
              'affiliate campaign on ClickBank.',
       'title': 'How I Made $13,531 in 7 Days With Google Ads + ClickBank (Traffic Systems '
                'Affiliate)',
       'url': 'https://www.youtube.com/watch?v=RgtHvwDuzDs&t=181s',
       'video_id': 'RgtHvwDuzDs'},
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
      {'author': 'Alex COLLINSEO',
       'channel': 'Alex COLLINSEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=MzA9HXeEoMA&t=20s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': "SEO strategy, and how to execute it step by step. The first strategy we're "
               "going to do is competitor plus alternative. It's my favorite one because we're "
               'getting traffic from competitors to our website.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': "SEO strategy, and how to execute it step by step. The first strategy we're "
              "going to do is competitor plus alternative. It's my favorite one because we're "
              'getting traffic from competitors to our website.',
       'title': 'How To Outrank Your Competitors Using “Alternative” Keyword Pages (Alex '
                'COLLINSEO)',
       'url': 'https://www.youtube.com/watch?v=MzA9HXeEoMA&t=20s',
       'video_id': 'MzA9HXeEoMA'},
      {'author': 'CXL',
       'channel': 'CXL',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:07](https://www.youtube.com/watch?v=ioLcYsLyaII&t=127s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': 'So basically what we want to do is start targeting the ICP in our comparison '
               'pages and then even take that a step beyond and going towards the uh the um '
               'the specific features.',
       'timestamp': 127,
       'timestamp_label': '[00:02:07]',
       'timestamp_seconds': 127,
       'tip': 'So basically what we want to do is start targeting the ICP in our comparison '
              'pages and then even take that a step beyond and going towards the uh the um the '
              'specific features.',
       'title': 'How to build AEO Comparison Pages For AI Dominance (CXL)',
       'url': 'https://www.youtube.com/watch?v=ioLcYsLyaII&t=127s',
       'video_id': 'ioLcYsLyaII'},
      {'author': 'Cheryl Phan',
       'channel': 'Cheryl Phan',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:07](https://www.youtube.com/watch?v=fnCkagoHXx0&t=247s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': "Federal Trade Commission want to make sure that people aren't abusing this and "
               "that's all that's all about so anyway I hope that was helpful and if you have "
               "any questions please reach out and let me know I'm here to help you and do you "
               'all have a blessed day bye-bye.',
       'timestamp': 247,
       'timestamp_label': '[00:04:07]',
       'timestamp_seconds': 247,
       'tip': "Federal Trade Commission want to make sure that people aren't abusing this and "
              "that's all that's all about so anyway I hope that was helpful and if you have "
              "any questions please reach out and let me know I'm here to help you and do you "
              'all have a blessed day bye-bye.',
       'title': 'Affiliate Link Disclosure Rules for FTC (Cheryl Phan)',
       'url': 'https://www.youtube.com/watch?v=fnCkagoHXx0&t=247s',
       'video_id': 'fnCkagoHXx0'},
      {'author': 'Beginner to 1K a Day Journey',
       'channel': 'Beginner to 1K a Day Journey',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:06](https://www.youtube.com/watch?v=HhGv4y6TrXs&t=66s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': 'Um anyways, we we are 13 hours still to go. I would say this day is going to '
               'be great. And um yeah, I I will not even call this like a bad days or anything '
               "like this. It's it's pretty good days, actually. And um yeah, what else I can "
               'show here?',
       'timestamp': 66,
       'timestamp_label': '[00:01:06]',
       'timestamp_seconds': 66,
       'tip': 'Um anyways, we we are 13 hours still to go. I would say this day is going to be '
              'great. And um yeah, I I will not even call this like a bad days or anything '
              "like this. It's it's pretty good days, actually. And um yeah, what else I can "
              'show here?',
       'title': 'HIT $5,000 EVERY WEEK FOR 24 WEEKS STRAIGHT! MARKETCALL (PAY PER CALL) '
                '(Beginner to 1K a Day Journey)',
       'url': 'https://www.youtube.com/watch?v=HhGv4y6TrXs&t=66s',
       'video_id': 'HhGv4y6TrXs'},
      {'author': 'Kyle',
       'channel': 'Kyle',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:11](https://www.youtube.com/watch?v=YI86pVR46-E&t=311s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': "You'll hit but affiliate marketing is a great place to start and so is uh my "
               'website rental business you should check it out and explore it all right good '
               'luck out there bye.',
       'timestamp': 311,
       'timestamp_label': '[00:05:11]',
       'timestamp_seconds': 311,
       'tip': "You'll hit but affiliate marketing is a great place to start and so is uh my "
              'website rental business you should check it out and explore it all right good '
              'luck out there bye.',
       'title': 'HONEST Review of “Affiliate Arbitrage” by Adam Cherrington (Kyle)',
       'url': 'https://www.youtube.com/watch?v=YI86pVR46-E&t=311s',
       'video_id': 'YI86pVR46-E'},
      {'author': 'Adam Enfroy',
       'channel': 'Adam Enfroy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:03](https://www.youtube.com/watch?v=rv01CKLsaY0&t=783s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': 'Amazon at a 4% commission pretty standard product price. To make $10,000 a '
               'month, you need 12,500 sales. That is over 400 sales every single day, right? '
               "There's people that I want to do like, oh, we do book affiliate stuff and it's "
               'do these different categories.',
       'timestamp': 783,
       'timestamp_label': '[00:13:03]',
       'timestamp_seconds': 783,
       'tip': 'Amazon at a 4% commission pretty standard product price. To make $10,000 a '
              'month, you need 12,500 sales. That is over 400 sales every single day, right? '
              "There's people that I want to do like, oh, we do book affiliate stuff and it's "
              'do these different categories.',
       'title': 'How to ACTUALLY Make Your First $1,000 with High Ticket Affiliate '
                'Marketing... Works in 2026 (Adam Enfroy)',
       'url': 'https://www.youtube.com/watch?v=rv01CKLsaY0&t=783s',
       'video_id': 'rv01CKLsaY0'},
      {'author': 'Local Media HQ',
       'channel': 'Local Media HQ',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:39:48](https://www.youtube.com/watch?v=SFCvA5RqbgU&t=2388s)',
       'relevance': 'Attributed practitioner commentary on a 30-day offer-approval, S2S '
                    'postback wiring, comparison-hub launch, and EPC Kill/Fix/Scale sprint.',
       'source_type': 'video_pro_tip',
       'text': "24 hours, blah, blah, blah. And it's just like a list of eight. Or are you "
               'thinking more what I had in my mind of the assist was like, well, again, that '
               'comes back to the email, but it was like a different offer or two each day.',
       'timestamp': 2388,
       'timestamp_label': '[00:39:48]',
       'timestamp_seconds': 2388,
       'tip': "24 hours, blah, blah, blah. And it's just like a list of eight. Or are you "
              'thinking more what I had in my mind of the assist was like, well, again, that '
              'comes back to the email, but it was like a different offer or two each day.',
       'title': 'How to Monetize Subscribers in the First 7 Days (Local Media HQ)',
       'url': 'https://www.youtube.com/watch?v=SFCvA5RqbgU&t=2388s',
       'video_id': 'SFCvA5RqbgU'}]}
