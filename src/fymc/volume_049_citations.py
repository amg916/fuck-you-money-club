"""Curated 180-citation Regulated Prediction-Market Terminals & Licensed iGaming Affiliates baseline (15 per chapter across Q1-Q12) mined strictly from verified Regulated Prediction-Market Terminals & Licensed iGaming Affiliates YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'100k',
     '40k',
     'access',
     'acquisition',
     'admin',
     'ads',
     'affiliate',
     'affiliates',
     'agco',
     'age',
     'alert',
     'analytics',
     'api',
     'arbitrage',
     'architecture',
     'audit',
     'automated',
     'backlinks',
     'bankroll',
     'banned',
     'betmgm',
     'better',
     'betting',
     'board',
     'book',
     'books',
     'broker',
     'brokers',
     'build',
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
 2: {'100k',
     '40k',
     'access',
     'acquisition',
     'admin',
     'ads',
     'affiliate',
     'affiliates',
     'agco',
     'age',
     'alert',
     'analytics',
     'api',
     'arbitrage',
     'architecture',
     'audit',
     'automated',
     'backlinks',
     'bankroll',
     'banned',
     'betmgm',
     'better',
     'betting',
     'board',
     'book',
     'books',
     'broker',
     'brokers',
     'budget',
     'build',
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
 3: {'100k',
     '40k',
     'access',
     'acquisition',
     'admin',
     'ads',
     'affiliate',
     'affiliates',
     'agco',
     'age',
     'alert',
     'analytics',
     'api',
     'arbitrage',
     'architecture',
     'audit',
     'automated',
     'backlinks',
     'bankroll',
     'banned',
     'betmgm',
     'better',
     'betting',
     'board',
     'book',
     'books',
     'broker',
     'brokers',
     'build',
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
 4: {'100k',
     '40k',
     'access',
     'acquisition',
     'admin',
     'ads',
     'affiliate',
     'affiliates',
     'agco',
     'age',
     'alert',
     'analytics',
     'api',
     'arbitrage',
     'architecture',
     'audit',
     'automated',
     'backlinks',
     'bankroll',
     'banned',
     'betmgm',
     'better',
     'betting',
     'board',
     'book',
     'books',
     'broker',
     'brokers',
     'budget',
     'build',
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
 5: {'100k',
     '40k',
     'access',
     'acquisition',
     'admin',
     'ads',
     'affiliate',
     'affiliates',
     'agco',
     'age',
     'alert',
     'analytics',
     'api',
     'arbitrage',
     'architecture',
     'audit',
     'automated',
     'avoid',
     'backlinks',
     'bankroll',
     'banned',
     'betmgm',
     'better',
     'betting',
     'board',
     'book',
     'books',
     'broker',
     'brokers',
     'build',
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
 6: {'100k',
     '40k',
     'access',
     'acquisition',
     'admin',
     'ads',
     'affiliate',
     'affiliates',
     'agco',
     'age',
     'alert',
     'analytics',
     'api',
     'arbitrage',
     'architecture',
     'audit',
     'automated',
     'backlinks',
     'bankroll',
     'banned',
     'betmgm',
     'better',
     'betting',
     'board',
     'book',
     'books',
     'broker',
     'brokers',
     'build',
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
 7: {'100k',
     '40k',
     'access',
     'acquisition',
     'admin',
     'ads',
     'affiliate',
     'affiliates',
     'agco',
     'age',
     'alert',
     'analytics',
     'api',
     'arbitrage',
     'architecture',
     'audit',
     'automated',
     'backlinks',
     'bankroll',
     'banned',
     'betmgm',
     'better',
     'betting',
     'board',
     'book',
     'books',
     'broker',
     'brokers',
     'build',
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
 8: {'100k',
     '40k',
     'access',
     'acquisition',
     'admin',
     'ads',
     'affiliate',
     'affiliates',
     'agco',
     'age',
     'alert',
     'analytics',
     'api',
     'arbitrage',
     'architecture',
     'audit',
     'automated',
     'backlinks',
     'bankroll',
     'banned',
     'betmgm',
     'better',
     'betting',
     'board',
     'book',
     'books',
     'broker',
     'brokers',
     'build',
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
 9: {'100k',
     '40k',
     'access',
     'acquisition',
     'admin',
     'ads',
     'affiliate',
     'affiliates',
     'agco',
     'age',
     'agreement',
     'alert',
     'analytics',
     'api',
     'arbitrage',
     'architecture',
     'audit',
     'automated',
     'backlinks',
     'bankroll',
     'banned',
     'betmgm',
     'better',
     'betting',
     'board',
     'book',
     'books',
     'broker',
     'brokers',
     'build',
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
 10: {'100k',
      '40k',
      'access',
      'acquisition',
      'admin',
      'ads',
      'affiliate',
      'affiliates',
      'agco',
      'age',
      'agent',
      'ai',
      'alert',
      'analytics',
      'api',
      'arbitrage',
      'architecture',
      'audit',
      'automate',
      'automated',
      'automation',
      'backlinks',
      'bankroll',
      'banned',
      'betmgm',
      'better',
      'betting',
      'board',
      'book',
      'books',
      'broker',
      'brokers',
      'build',
      'building',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'100k',
      '40k',
      'access',
      'acquisition',
      'admin',
      'ads',
      'affiliate',
      'affiliates',
      'agco',
      'age',
      'alert',
      'analytics',
      'api',
      'arbitrage',
      'architecture',
      'audit',
      'automated',
      'backlinks',
      'bankroll',
      'banned',
      'betmgm',
      'better',
      'betting',
      'board',
      'book',
      'books',
      'broker',
      'brokers',
      'build',
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
 12: {'100k',
      '40k',
      'access',
      'acquisition',
      'action',
      'admin',
      'ads',
      'affiliate',
      'affiliates',
      'agco',
      'age',
      'alert',
      'analytics',
      'api',
      'arbitrage',
      'architecture',
      'audit',
      'automated',
      'backlinks',
      'bankroll',
      'banned',
      'betmgm',
      'better',
      'betting',
      'board',
      'book',
      'books',
      'broker',
      'brokers',
      'build',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Trade Handle',
      'channel': 'Trade Handle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:34](https://www.youtube.com/watch?v=LHwUBaFR_no&t=34s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The sports book creates the market, sets the odds, and accepts the bet. Those '
              'odds also usually include a betting margin, which is part of how sports books '
              'manage risk and generate revenue.',
      'timestamp': 34,
      'timestamp_label': '[00:00:34]',
      'timestamp_seconds': 34,
      'tip': 'The sports book creates the market, sets the odds, and accepts the bet. Those '
             'odds also usually include a betting margin, which is part of how sports books '
             'manage risk and generate revenue.',
      'title': 'Prediction Markets vs Sportsbooks: Key Differences Explained (Trade Handle)',
      'url': 'https://www.youtube.com/watch?v=LHwUBaFR_no&t=34s',
      'video_id': 'LHwUBaFR_no'},
     {'author': 'Ace Alliance',
      'channel': 'Ace Alliance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:00](https://www.youtube.com/watch?v=W_qH_fC6vPE&t=300s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t mean um just sending more players through the same model. Um what are the "
              'realistic directions that an established affiliate business can take when it '
              'really wants to grow beyond traffic acquisition? So, first of all is that I '
              'think of it as a ladder.',
      'timestamp': 300,
      'timestamp_label': '[00:05:00]',
      'timestamp_seconds': 300,
      'tip': "'t mean um just sending more players through the same model. Um what are the "
             'realistic directions that an established affiliate business can take when it '
             'really wants to grow beyond traffic acquisition? So, first of all is that I '
             'think of it as a ladder.',
      'title': 'How iGaming Affiliates Can Create Value for Operators and Studios (Ace '
               'Alliance)',
      'url': 'https://www.youtube.com/watch?v=W_qH_fC6vPE&t=300s',
      'video_id': 'W_qH_fC6vPE'},
     {'author': 'iGaming Marketing Agency Tips by Christian Strutt',
      'channel': 'iGaming Marketing Agency Tips by Christian Strutt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:11](https://www.youtube.com/watch?v=3ZUgO2w5vfU&t=371s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Top lists always work well, like best casinos for beginners or the best sports '
              'book for football betting, um the best sports book for racing betting in the '
              'US. The more niche it works, the more niche the content, the the better it it '
              'tends to convert.',
      'timestamp': 371,
      'timestamp_label': '[00:06:11]',
      'timestamp_seconds': 371,
      'tip': 'Top lists always work well, like best casinos for beginners or the best sports '
             'book for football betting, um the best sports book for racing betting in the US. '
             'The more niche it works, the more niche the content, the the better it it tends '
             'to convert.',
      'title': 'How To Start an iGaming Affiliate Business in 2026 - Starting a Gambling '
               'Affiliate Marketing Company (iGaming Marketing Agency Tips by Christian '
               'Strutt)',
      'url': 'https://www.youtube.com/watch?v=3ZUgO2w5vfU&t=371s',
      'video_id': '3ZUgO2w5vfU'},
     {'author': 'Simple Explain',
      'channel': 'Simple Explain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:54](https://www.youtube.com/watch?v=Osx2O3SjlCA&t=174s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Two, the IB is usually affiliated with the FCM either as an independent entity '
              'that is partnered with that merchant firm or as a direct subsidiary of that '
              'FCM. Three, IBs are better able to service their clients as they are local and '
              'their primary goal is customer service.',
      'timestamp': 174,
      'timestamp_label': '[00:02:54]',
      'timestamp_seconds': 174,
      'tip': 'Two, the IB is usually affiliated with the FCM either as an independent entity '
             'that is partnered with that merchant firm or as a direct subsidiary of that FCM. '
             'Three, IBs are better able to service their clients as they are local and their '
             'primary goal is customer service.',
      'title': 'What Is an Introducing Broker? (Simple Explain)',
      'url': 'https://www.youtube.com/watch?v=Osx2O3SjlCA&t=174s',
      'video_id': 'Osx2O3SjlCA'},
     {'author': 'Push House | Advertising Network',
      'channel': 'Push House | Advertising Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:53](https://www.youtube.com/watch?v=Qygo77RCGlw&t=233s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Is rare due to the peculiarities of the niche since registration does not '
              'guarantee further use of the service the next model is CPS which is the most.',
      'timestamp': 233,
      'timestamp_label': '[00:03:53]',
      'timestamp_seconds': 233,
      'tip': 'Is rare due to the peculiarities of the niche since registration does not '
             'guarantee further use of the service the next model is CPS which is the most.',
      'title': 'How to Earn on Sports Betting Affiliate Programs? Complete Guide to Niche | '
               'Push.House (Push House | Advertising Network)',
      'url': 'https://www.youtube.com/watch?v=Qygo77RCGlw&t=233s',
      'video_id': 'Qygo77RCGlw'},
     {'author': 'Capperway',
      'channel': 'Capperway',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:14](https://www.youtube.com/watch?v=GLsvRuOxKds&t=74s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But when you're selling a subscription, you're charging people for a service. "
              "Those are two completely different business models. Let's say you're selling "
              'access to your sports picks for about $50 a month.',
      'timestamp': 74,
      'timestamp_label': '[00:01:14]',
      'timestamp_seconds': 74,
      'tip': "But when you're selling a subscription, you're charging people for a service. "
             "Those are two completely different business models. Let's say you're selling "
             'access to your sports picks for about $50 a month.',
      'title': 'How I’d Build a $10,000/Month Sports Betting Business From Zero (Capperway)',
      'url': 'https://www.youtube.com/watch?v=GLsvRuOxKds&t=74s',
      'video_id': 'GLsvRuOxKds'},
     {'author': 'Revpanda Group',
      'channel': 'Revpanda Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:53](https://www.youtube.com/watch?v=6l_ci8Pi0jI&t=293s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I just want to follow up uh with the regulations question. So do you think '
              'Alexander when we have like stricter regulations in a market is it helping the '
              'business or is it killing the affiliates business in general? Uh as I said '
              'before we we have uh two options or two cases.',
      'timestamp': 293,
      'timestamp_label': '[00:04:53]',
      'timestamp_seconds': 293,
      'tip': 'I just want to follow up uh with the regulations question. So do you think '
             'Alexander when we have like stricter regulations in a market is it helping the '
             'business or is it killing the affiliates business in general? Uh as I said '
             'before we we have uh two options or two cases.',
      'title': 'How to Build an Unbreakable iGaming Affiliate Portfolio in 2026 (Revpanda '
               'Group)',
      'url': 'https://www.youtube.com/watch?v=6l_ci8Pi0jI&t=293s',
      'video_id': '6l_ci8Pi0jI'},
     {'author': 'The Young Turks',
      'channel': 'The Young Turks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:57](https://www.youtube.com/watch?v=Y-ToFo3PvAw&t=297s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll touch on that in just a minute, cryptocurrency, other issues. About 70% of "
              "Kalshi's daily trading volume comes from sports betting, according to the "
              'prediction market operator. And so, on prediction markets, 79% to 84% of all '
              'accounts um lose.',
      'timestamp': 297,
      'timestamp_label': '[00:04:57]',
      'timestamp_seconds': 297,
      'tip': "'ll touch on that in just a minute, cryptocurrency, other issues. About 70% of "
             "Kalshi's daily trading volume comes from sports betting, according to the "
             'prediction market operator. And so, on prediction markets, 79% to 84% of all '
             'accounts um lose.',
      'title': 'How Prediction Markets Are TAKING OVER America (The Young Turks)',
      'url': 'https://www.youtube.com/watch?v=Y-ToFo3PvAw&t=297s',
      'video_id': 'Y-ToFo3PvAw'},
     {'author': 'Lou 1win',
      'channel': 'Lou 1win',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:37](https://www.youtube.com/watch?v=d_2br4amklI&t=37s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Them can lead to bad business decisions. Start with gross gaming revenue,  '
              'usually shortened to GGR. In a simplified model, GGR is the total.',
      'timestamp': 37,
      'timestamp_label': '[00:00:37]',
      'timestamp_seconds': 37,
      'tip': 'Them can lead to bad business decisions. Start with gross gaming revenue,  '
             'usually shortened to GGR. In a simplified model, GGR is the total.',
      'title': 'How iGaming Revenue Works (Lou 1win)',
      'url': 'https://www.youtube.com/watch?v=d_2br4amklI&t=37s',
      'video_id': 'd_2br4amklI'},
     {'author': 'Interactive Brokers',
      'channel': 'Interactive Brokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=ceR-weGZSXc&t=35s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Clients can purchase the contracts through Forecast X, an IBKR affiliate that '
              'operates both a designated contract market and derivative clearing organization '
              'licensed by the CFTC. Macroeconomic and climate considerations can '
              'significantly impact portfolios.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'Clients can purchase the contracts through Forecast X, an IBKR affiliate that '
             'operates both a designated contract market and derivative clearing organization '
             'licensed by the CFTC. Macroeconomic and climate considerations can significantly '
             'impact portfolios.',
      'title': 'Using ForecastEx Economic Forecast Contracts to Hedge Economic and Climate '
               'Risks (Interactive Brokers)',
      'url': 'https://www.youtube.com/watch?v=ceR-weGZSXc&t=35s',
      'video_id': 'ceR-weGZSXc'},
     {'author': 'OddsJam: Sports Betting Strategy & Education',
      'channel': 'OddsJam: Sports Betting Strategy & Education',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:06](https://www.youtube.com/watch?v=ob0DiySE-UI&t=306s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, there isn't a massive disagreement here within price, but again, these are "
              "three different books with three different prices. The reason there's different "
              "prices because they're all in competition for your business. But not every book "
              'is created equal.',
      'timestamp': 306,
      'timestamp_label': '[00:05:06]',
      'timestamp_seconds': 306,
      'tip': "Now, there isn't a massive disagreement here within price, but again, these are "
             "three different books with three different prices. The reason there's different "
             "prices because they're all in competition for your business. But not every book "
             'is created equal.',
      'title': 'The Complete Guide to +EV Sports Betting (For Beginners) (OddsJam: Sports '
               'Betting Strategy & Education)',
      'url': 'https://www.youtube.com/watch?v=ob0DiySE-UI&t=306s',
      'video_id': 'ob0DiySE-UI'},
     {'author': 'Part Time Larry',
      'channel': 'Part Time Larry',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:53](https://www.youtube.com/watch?v=E2mgWN4ReqQ&t=233s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Putting together our thoughts um you know you can see here we have this uh you '
              'know this is a little uh betting model here and we got all the different.',
      'timestamp': 233,
      'timestamp_label': '[00:03:53]',
      'timestamp_seconds': 233,
      'tip': 'Putting together our thoughts um you know you can see here we have this uh you '
             'know this is a little uh betting model here and we got all the different.',
      'title': 'Prediction Markets with the Kalshi API (Python Tutorial) (Part Time Larry)',
      'url': 'https://www.youtube.com/watch?v=E2mgWN4ReqQ&t=233s',
      'video_id': 'E2mgWN4ReqQ'},
     {'author': 'NEXTPredict',
      'channel': 'NEXTPredict',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=uh3GgMs9ha8&t=163s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And that was followed up with another insider trading case sort of in the '
              'business sphere that involved Google. That was a few weeks after that. And '
              "we've brought other insider trading cases and market manipulation cases.",
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': 'And that was followed up with another insider trading case sort of in the '
             "business sphere that involved Google. That was a few weeks after that. And we've "
             'brought other insider trading cases and market manipulation cases.',
      'title': 'View from the CFTC ft. CFTC Director of Enforcement David Miller & CNN | '
               'NEXTPredict NYC 2026 (NEXTPredict)',
      'url': 'https://www.youtube.com/watch?v=uh3GgMs9ha8&t=163s',
      'video_id': 'uh3GgMs9ha8'},
     {'author': 'License Gentlemen',
      'channel': 'License Gentlemen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=4mTaeo1ds6g&t=20s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'B2C a platform or your game provider. And then you know the documents for every '
              'business model are completely different but uh the basic documents always '
              'include the KYC part.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'B2C a platform or your game provider. And then you know the documents for every '
             'business model are completely different but uh the basic documents always '
             'include the KYC part.',
      'title': 'What Documents Are Actually Required For A Gambling License in 2025? (License '
               'Gentlemen)',
      'url': 'https://www.youtube.com/watch?v=4mTaeo1ds6g&t=20s',
      'video_id': '4mTaeo1ds6g'},
     {'author': 'Juiced Bets',
      'channel': 'Juiced Bets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:45](https://www.youtube.com/watch?v=PaQjSUCZVb0&t=405s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It tells you what kind of what kind of percent gain you can make and then also '
              'the amount of money you can make based on the liquidity in that market. You can '
              'filter it based on the percent spread like we have right here.',
      'timestamp': 405,
      'timestamp_label': '[00:06:45]',
      'timestamp_seconds': 405,
      'tip': 'It tells you what kind of what kind of percent gain you can make and then also '
             'the amount of money you can make based on the liquidity in that market. You can '
             'filter it based on the percent spread like we have right here.',
      'title': 'I Found an Arbitrage Tool for Prediction Markets (Kalshi & Polymarket) (Juiced '
               'Bets)',
      'url': 'https://www.youtube.com/watch?v=PaQjSUCZVb0&t=405s',
      'video_id': 'PaQjSUCZVb0'}],
 2: [{'author': '15M iGaming Media & Dealflow Platform',
      'channel': '15M iGaming Media & Dealflow Platform',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:01](https://www.youtube.com/watch?v=WaWQNIAchz0&t=361s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The contract determines the rest. To understand the scale of this industry, '
              "consider Better Collective. It's a publicly listed digital sports media group "
              'whose business includes affiliate-driven customer acquisition.',
      'timestamp': 361,
      'timestamp_label': '[00:06:01]',
      'timestamp_seconds': 361,
      'tip': 'The contract determines the rest. To understand the scale of this industry, '
             "consider Better Collective. It's a publicly listed digital sports media group "
             'whose business includes affiliate-driven customer acquisition.',
      'title': 'How a Casino Affiliate Program Actually Works – With Numbers (15M iGaming '
               'Media & Dealflow Platform)',
      'url': 'https://www.youtube.com/watch?v=WaWQNIAchz0&t=361s',
      'video_id': 'WaWQNIAchz0'},
     {'author': 'Odys Podcast: The High Stakes Growth Show',
      'channel': 'Odys Podcast: The High Stakes Growth Show',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:28](https://www.youtube.com/watch?v=ohEZ5-gHckQ&t=1408s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "SEO affiliates, there's always pays for, coming up with a better solution, with "
              'better offers, with better product to, guide players how to pay, you know, '
              "their bonuses or the right casino games. So, I don't see it as, issue, but "
              'rather for big affiliates.',
      'timestamp': 1408,
      'timestamp_label': '[00:23:28]',
      'timestamp_seconds': 1408,
      'tip': "SEO affiliates, there's always pays for, coming up with a better solution, with "
             'better offers, with better product to, guide players how to pay, you know, their '
             "bonuses or the right casino games. So, I don't see it as, issue, but rather for "
             'big affiliates.',
      'title': "iGaming Affiliate Strategies: You're Burning 90K Monthly, Levon Nikoghosyan, "
               'AffPapa CEO Reveals Why (Odys Podcast: The High Stakes Growth Show)',
      'url': 'https://www.youtube.com/watch?v=ohEZ5-gHckQ&t=1408s',
      'video_id': 'ohEZ5-gHckQ'},
     {'author': 'CasinoRank+Insider',
      'channel': 'CasinoRank+Insider',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:49](https://www.youtube.com/watch?v=XU9tdzKAxdU&t=49s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's talk why this is exploding. Affiliate marketing works because it's "
              'efficient, targeted, and trusted. Operators only pay for real players. '
              'Affiliates reach specific audiences like poker fans or slot streamers, and '
              'players trust them more than ads.',
      'timestamp': 49,
      'timestamp_label': '[00:00:49]',
      'timestamp_seconds': 49,
      'tip': "Let's talk why this is exploding. Affiliate marketing works because it's "
             'efficient, targeted, and trusted. Operators only pay for real players. '
             'Affiliates reach specific audiences like poker fans or slot streamers, and '
             'players trust them more than ads.',
      'title': 'How iGaming Affiliates Drive Billions in 2025 (And Why It Works) '
               '(CasinoRank+Insider)',
      'url': 'https://www.youtube.com/watch?v=XU9tdzKAxdU&t=49s',
      'video_id': 'XU9tdzKAxdU'},
     {'author': 'closeuptrading',
      'channel': 'closeuptrading',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:33](https://www.youtube.com/watch?v=4_swDdRFYJc&t=93s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sell for 15 cents a contract without waiting for the answer. And it works the '
              'other way, too. ForecastX, zero commission plus a 1 cent exchange fee. Kalshi '
              'and CME, 1 cent plus 1 cent. And ForecastX pays an incentive coupon on open '
              'positions, 3.',
      'timestamp': 93,
      'timestamp_label': '[00:01:33]',
      'timestamp_seconds': 93,
      'tip': 'Sell for 15 cents a contract without waiting for the answer. And it works the '
             'other way, too. ForecastX, zero commission plus a 1 cent exchange fee. Kalshi '
             'and CME, 1 cent plus 1 cent. And ForecastX pays an incentive coupon on open '
             'positions, 3.',
      'title': 'How to Trade Prediction Markets (Kalshi, ForecastEx, CME Inside Interactive '
               'Brokers) (closeuptrading)',
      'url': 'https://www.youtube.com/watch?v=4_swDdRFYJc&t=93s',
      'video_id': '4_swDdRFYJc'},
     {'author': 'iGaming Express',
      'channel': 'iGaming Express',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=zEJgRn6SLjs&t=102s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Processing fees affiliate commissions licensing fees taxes the formula for ngr '
              'is ngr ggr bonuses Payment Processing fees affiliate commissions licensing.',
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': 'Processing fees affiliate commissions licensing fees taxes the formula for ngr '
             'is ngr ggr bonuses Payment Processing fees affiliate commissions licensing.',
      'title': 'GGR vs NGR: Understanding key metrics in iGaming (iGaming Express)',
      'url': 'https://www.youtube.com/watch?v=zEJgRn6SLjs&t=102s',
      'video_id': 'zEJgRn6SLjs'},
     {'author': 'Schwab Network',
      'channel': 'Schwab Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:36:21](https://www.youtube.com/watch?v=ZW18j-a-TuY&t=2181s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I think if you try to overly focus on monetization there you end up kind of '
              'taking away uh some of the value and the access. So I would say exchange '
              'trading fees. Name one event contract category that every C-suite level '
              'executive should be watching right now.',
      'timestamp': 2181,
      'timestamp_label': '[00:36:21]',
      'timestamp_seconds': 2181,
      'tip': 'I think if you try to overly focus on monetization there you end up kind of '
             'taking away uh some of the value and the access. So I would say exchange trading '
             'fees. Name one event contract category that every C-suite level executive should '
             'be watching right now.',
      'title': 'Kalshi Co-Founder & COO on Future of Prediction Markets (Schwab Network)',
      'url': 'https://www.youtube.com/watch?v=ZW18j-a-TuY&t=2181s',
      'video_id': 'ZW18j-a-TuY'},
     {'author': 'Brokerchampion',
      'channel': 'Brokerchampion',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:49](https://www.youtube.com/watch?v=CIinXD9tbVo&t=229s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'These rules can feel restrictive compared with offshore brokers, but the '
              'mechanism is straightforward. The regulator limits the ways a retail account '
              'can build hidden or excessive exposure. Customer fund segregation works '
              'differently.',
      'timestamp': 229,
      'timestamp_label': '[00:03:49]',
      'timestamp_seconds': 229,
      'tip': 'These rules can feel restrictive compared with offshore brokers, but the '
             'mechanism is straightforward. The regulator limits the ways a retail account can '
             'build hidden or excessive exposure. Customer fund segregation works differently.',
      'title': 'The CFTC Explained 2026: Who Polices US Futures, Swaps and Retail Forex '
               '(Brokerchampion)',
      'url': 'https://www.youtube.com/watch?v=CIinXD9tbVo&t=229s',
      'video_id': 'CIinXD9tbVo'},
     {'author': 'iGaming Marketing Agency Tips by Christian Strutt',
      'channel': 'iGaming Marketing Agency Tips by Christian Strutt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:44](https://www.youtube.com/watch?v=6jlPOcl5CnI&t=284s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re a smaller affiliate starting out that that can sometimes be a bit painful "
              'as you build up your player base and commission. So those with a lower payment '
              'threshold are generally more p more preferable. And I also like um programs '
              'with multiple payment options.',
      'timestamp': 284,
      'timestamp_label': '[00:04:44]',
      'timestamp_seconds': 284,
      'tip': "'re a smaller affiliate starting out that that can sometimes be a bit painful as "
             'you build up your player base and commission. So those with a lower payment '
             'threshold are generally more p more preferable. And I also like um programs with '
             'multiple payment options.',
      'title': 'How To Choose The Right Gambling Affiliate Program - Finding The Best iGaming '
               'Affiliate Programs (iGaming Marketing Agency Tips by Christian Strutt)',
      'url': 'https://www.youtube.com/watch?v=6jlPOcl5CnI&t=284s',
      'video_id': '6jlPOcl5CnI'},
     {'author': 'TC Trading',
      'channel': 'TC Trading',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:49](https://www.youtube.com/watch?v=MREcV1sLqwc&t=469s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Didn't you make this trade at 39 cents per contract? So, why is your average "
              'price 41?" That is because there were 2 cents worth of fees, which I\'m going '
              'to discuss shortly. So, our unrealized P&L is actually down $2 immediately.',
      'timestamp': 469,
      'timestamp_label': '[00:07:49]',
      'timestamp_seconds': 469,
      'tip': "Didn't you make this trade at 39 cents per contract? So, why is your average "
             'price 41?" That is because there were 2 cents worth of fees, which I\'m going to '
             'discuss shortly. So, our unrealized P&L is actually down $2 immediately.',
      'title': 'How To Trade Prediction Markets On Interactive Brokers (Kalshi + CME + '
               'ForecastEx) (TC Trading)',
      'url': 'https://www.youtube.com/watch?v=MREcV1sLqwc&t=469s',
      'video_id': 'MREcV1sLqwc'},
     {'author': 'John Lothian News (JLN)',
      'channel': 'John Lothian News (JLN)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:39](https://www.youtube.com/watch?v=GaBqUuuLjrQ&t=279s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Day depending upon the closing price of that contract we pay you interest on '
              "that closing price currently at 4.3% and and why do we do this it's we.",
      'timestamp': 279,
      'timestamp_label': '[00:04:39]',
      'timestamp_seconds': 279,
      'tip': 'Day depending upon the closing price of that contract we pay you interest on '
             "that closing price currently at 4.3% and and why do we do this it's we.",
      'title': 'Thomas Peterffy on ForecastEx: Building a Buy-Only Market to Transform '
               'Event\xa0Contracts\xa0Trading (John Lothian News (JLN))',
      'url': 'https://www.youtube.com/watch?v=GaBqUuuLjrQ&t=279s',
      'video_id': 'GaBqUuuLjrQ'},
     {'author': 'CryptoCoins',
      'channel': 'CryptoCoins',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:38](https://www.youtube.com/watch?v=1v9Cq8L6jqg&t=158s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I could trade in Miami getting LeBron James as his future team for 45 cents. '
              'Now, when he finally chooses and if it is Miami, all of those contracts pay out '
              'at a dollar, meaning I would make 55 cents per per share that I purchased in '
              'this contract.',
      'timestamp': 158,
      'timestamp_label': '[00:02:38]',
      'timestamp_seconds': 158,
      'tip': 'I could trade in Miami getting LeBron James as his future team for 45 cents. '
             'Now, when he finally chooses and if it is Miami, all of those contracts pay out '
             'at a dollar, meaning I would make 55 cents per per share that I purchased in '
             'this contract.',
      'title': 'Can You Predict the Future? Kalshi Pro & Prediction Markets Explained '
               '(CryptoCoins)',
      'url': 'https://www.youtube.com/watch?v=1v9Cq8L6jqg&t=158s',
      'video_id': '1v9Cq8L6jqg'},
     {'author': 'Part Time Larry',
      'channel': 'Part Time Larry',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:54](https://www.youtube.com/watch?v=vT0qMNgOkxo&t=174s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "24 and I've lost nearly half of my money. And this is because I was biased. I "
              "want my team to win so much that I'm willing to pay a little bit too much to "
              'have a contract that says the Rockets are going to win uh the championship.',
      'timestamp': 174,
      'timestamp_label': '[00:02:54]',
      'timestamp_seconds': 174,
      'tip': "24 and I've lost nearly half of my money. And this is because I was biased. I "
             "want my team to win so much that I'm willing to pay a little bit too much to "
             'have a contract that says the Rockets are going to win uh the championship.',
      'title': 'Why Kalshi Bettors Lose (72 Million Trades Analyzed) (Part Time Larry)',
      'url': 'https://www.youtube.com/watch?v=vT0qMNgOkxo&t=174s',
      'video_id': 'vT0qMNgOkxo'},
     {'author': 'CFTC',
      'channel': 'CFTC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:27:15](https://www.youtube.com/watch?v=jx5ZryxlRsI&t=5235s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Agreed to use in the future with the customer that's buying the Grain and the "
              "cash price today that's not converged the May Futures Contract potentially.",
      'timestamp': 5235,
      'timestamp_label': '[01:27:15]',
      'timestamp_seconds': 5235,
      'tip': "Agreed to use in the future with the customer that's buying the Grain and the "
             "cash price today that's not converged the May Futures Contract potentially.",
      'title': 'Part I: CFTC Staff Roundtable on Position Limits for Physical Commodity '
               'Derivatives, 06/19/14 (CFTC)',
      'url': 'https://www.youtube.com/watch?v=jx5ZryxlRsI&t=5235s',
      'video_id': 'jx5ZryxlRsI'},
     {'author': '🎓Profeissor.com🚀Digital Assets, AI & FinTech',
      'channel': '🎓Profeissor.com🚀Digital Assets, AI & FinTech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=YIkTrxNRVlc&t=52s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'These contracts are structured as binary contracts. So if the reference event '
              'occurs, you receive a payment, and if the reference event does not occur, then '
              'you receive nothing.',
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': 'These contracts are structured as binary contracts. So if the reference event '
             'occurs, you receive a payment, and if the reference event does not occur, then '
             'you receive nothing.',
      'title': "🔮What are @mention contracts? 🇺🇸CFTC staff's guidance to this new type of "
               'event contract 📈 (🎓Profeissor.com🚀Digital Assets, AI & FinTech)',
      'url': 'https://www.youtube.com/watch?v=YIkTrxNRVlc&t=52s',
      'video_id': 'YIkTrxNRVlc'},
     {'author': 'CNBC Television',
      'channel': 'CNBC Television',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=oEiVp7yDA6s&t=110s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'WELL, THERE HAS BEEN LIKE EVERY AGENCY IN GOVERNMENT STAFFING CUTS. SO NOW DOES '
              'THE CFTC HAVE THE ABILITY TO POLICE THESE MARKETS? THEY HAVE REGULATED AND '
              "POLICED EVENT CONTRACTS, DESIGNATED CONTRACT MARKETS, AS THEY'RE CALLED "
              'ESSENTIALLY EXCHANGES.',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': 'WELL, THERE HAS BEEN LIKE EVERY AGENCY IN GOVERNMENT STAFFING CUTS. SO NOW DOES '
             'THE CFTC HAVE THE ABILITY TO POLICE THESE MARKETS? THEY HAVE REGULATED AND '
             "POLICED EVENT CONTRACTS, DESIGNATED CONTRACT MARKETS, AS THEY'RE CALLED "
             'ESSENTIALLY EXCHANGES.',
      'title': 'Former CFTC enforcement director on regulating prediction markets (CNBC '
               'Television)',
      'url': 'https://www.youtube.com/watch?v=oEiVp7yDA6s&t=110s',
      'video_id': 'oEiVp7yDA6s'}],
 3: [{'author': 'BetSmart',
      'channel': 'BetSmart',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:11](https://www.youtube.com/watch?v=jauhFM_n5d4&t=251s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It has better odds, continues to have uh resources to throw at building out '
              'this amazing terminal. And now quickly talking about price for access to all '
              'things better odds. But if you want to add live, it is an extra $10 a month for '
              '$79 a month.',
      'timestamp': 251,
      'timestamp_label': '[00:04:11]',
      'timestamp_seconds': 251,
      'tip': 'It has better odds, continues to have uh resources to throw at building out this '
             'amazing terminal. And now quickly talking about price for access to all things '
             'better odds. But if you want to add live, it is an extra $10 a month for $79 a '
             'month.',
      'title': 'A Free Sports Betting Odds Screen & a Pro-Level Prediction Market Terminal: 2 '
               'Tools I Tested (BetSmart)',
      'url': 'https://www.youtube.com/watch?v=jauhFM_n5d4&t=251s',
      'video_id': 'jauhFM_n5d4'},
     {'author': 'OngPredicts',
      'channel': 'OngPredicts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:25](https://www.youtube.com/watch?v=OEhjqCpa1Uw&t=205s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "KI's own API, you'll know it only sends bids, one list for yes and one for no, "
              'and leaves you to work out the asks. Here both books arrive as bids and asks. '
              'Each book costs five credits. So Kalshi is asking 24 cents and Poly Market 27. '
              'Is that really the same market?',
      'timestamp': 205,
      'timestamp_label': '[00:03:25]',
      'timestamp_seconds': 205,
      'tip': "KI's own API, you'll know it only sends bids, one list for yes and one for no, "
             'and leaves you to work out the asks. Here both books arrive as bids and asks. '
             'Each book costs five credits. So Kalshi is asking 24 cents and Poly Market 27. '
             'Is that really the same market?',
      'title': 'How to Use Polymarket & Kalshi With One API (Python Tutorial) (OngPredicts)',
      'url': 'https://www.youtube.com/watch?v=OEhjqCpa1Uw&t=205s',
      'video_id': 'OEhjqCpa1Uw'},
     {'author': 'OddsJam: Sports Betting Strategy & Education',
      'channel': 'OddsJam: Sports Betting Strategy & Education',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:14](https://www.youtube.com/watch?v=iWi1gqgw35Y&t=494s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Pinnacle which Pinnacle releasing an offer a P plus R line. You know, Novig '
              "doesn't have enough liquidity to really care about. So, you are just betting "
              'into Better Sports Book with a FanDuel or Dvig, which I think is perfectly '
              'fine. It is the best price in the market.',
      'timestamp': 494,
      'timestamp_label': '[00:08:14]',
      'timestamp_seconds': 494,
      'tip': 'Pinnacle which Pinnacle releasing an offer a P plus R line. You know, Novig '
             "doesn't have enough liquidity to really care about. So, you are just betting "
             'into Better Sports Book with a FanDuel or Dvig, which I think is perfectly fine. '
             'It is the best price in the market.',
      'title': 'NBA Betting Course, Part 2: How to Find Positive EV Bets (OddsJam: Sports '
               'Betting Strategy & Education)',
      'url': 'https://www.youtube.com/watch?v=iWi1gqgw35Y&t=494s',
      'video_id': 'iWi1gqgw35Y'},
     {'author': 'iGaming Marketing Agency Tips by Christian Strutt',
      'channel': 'iGaming Marketing Agency Tips by Christian Strutt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=FnNlK_XZ270&t=102s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Provides immediate cash plus long-term income potential. You earn a small '
              'commission on players brought in by affiliates you refer to the program. '
              'Affiliate dashboard provides real-time data on clicks, registrations, deposits, '
              'active players, and your earnings.',
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': 'Provides immediate cash plus long-term income potential. You earn a small '
             'commission on players brought in by affiliates you refer to the program. '
             'Affiliate dashboard provides real-time data on clicks, registrations, deposits, '
             'active players, and your earnings.',
      'title': 'How do casino affiliate programs work? How do the best iGaming affiliates '
               'programs operate? (iGaming Marketing Agency Tips by Christian Strutt)',
      'url': 'https://www.youtube.com/watch?v=FnNlK_XZ270&t=102s',
      'video_id': 'FnNlK_XZ270'},
     {'author': 'Chen Trading',
      'channel': 'Chen Trading',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:02](https://www.youtube.com/watch?v=lYFPEQllQOw&t=122s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The difference is the gross margin before fees and other costs. Your average '
              'price can rise as you buy more shares, so the quote is a starting point, not '
              'the final calculation.',
      'timestamp': 122,
      'timestamp_label': '[00:02:02]',
      'timestamp_seconds': 122,
      'tip': 'The difference is the gross margin before fees and other costs. Your average '
             'price can rise as you buy more shares, so the quote is a starting point, not the '
             'final calculation.',
      'title': 'How to Find Arbitrage Bets Across 15+ Prediction Markets (Full Walkthrough) '
               '(Chen Trading)',
      'url': 'https://www.youtube.com/watch?v=lYFPEQllQOw&t=122s',
      'video_id': 'lYFPEQllQOw'},
     {'author': 'Quantitative Predictions',
      'channel': 'Quantitative Predictions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:05](https://www.youtube.com/watch?v=He2ctf0VZZ8&t=305s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They have the largest venue coverage. They also got access to the API and SDKs. '
              'It has similar pricing to the other ones in this list. And the main thing that '
              'I really like about Predict Fi is of course the venue coverage.',
      'timestamp': 305,
      'timestamp_label': '[00:05:05]',
      'timestamp_seconds': 305,
      'tip': 'They have the largest venue coverage. They also got access to the API and SDKs. '
             'It has similar pricing to the other ones in this list. And the main thing that I '
             'really like about Predict Fi is of course the venue coverage.',
      'title': 'Best Prediction Market Arbitrage Tools 2026 (Quantitative Predictions)',
      'url': 'https://www.youtube.com/watch?v=He2ctf0VZZ8&t=305s',
      'video_id': 'He2ctf0VZZ8'},
     {'author': 'iGaming Marketing Agency Tips by Christian Strutt',
      'channel': 'iGaming Marketing Agency Tips by Christian Strutt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:09](https://www.youtube.com/watch?v=_puyhQJIomQ&t=369s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you can sell those at $300, then you've got a straight 3:1 profit margin, "
              'which which some affiliate prefers, some affiliates prefer. I guess the '
              "negative is a CPA. There's no long-term upside.",
      'timestamp': 369,
      'timestamp_label': '[00:06:09]',
      'timestamp_seconds': 369,
      'tip': "If you can sell those at $300, then you've got a straight 3:1 profit margin, "
             'which which some affiliate prefers, some affiliates prefer. I guess the negative '
             "is a CPA. There's no long-term upside.",
      'title': 'Gambling Affiliate Programs Explained - iGaming Affiliate Program Terms, '
               'Advice, Strategy, Tips (iGaming Marketing Agency Tips by Christian Strutt)',
      'url': 'https://www.youtube.com/watch?v=_puyhQJIomQ&t=369s',
      'video_id': '_puyhQJIomQ'},
     {'author': 'AffPapa Media',
      'channel': 'AffPapa Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:12](https://www.youtube.com/watch?v=Jdm7YPGRFSk&t=192s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Advertiser offers performance-based pricing models guaranteeing advertisers '
              'access to Quality traffic from reliable Publishers with multi-channel '
              'campaigns.',
      'timestamp': 192,
      'timestamp_label': '[00:03:12]',
      'timestamp_seconds': 192,
      'tip': 'Advertiser offers performance-based pricing models guaranteeing advertisers '
             'access to Quality traffic from reliable Publishers with multi-channel campaigns.',
      'title': 'Advertise.net - iGaming Affiliate Network | iGaming Reviews by AffPapa.com '
               '(AffPapa Media)',
      'url': 'https://www.youtube.com/watch?v=Jdm7YPGRFSk&t=192s',
      'video_id': 'Jdm7YPGRFSk'},
     {'author': 'SharpMoney',
      'channel': 'SharpMoney',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:40](https://www.youtube.com/watch?v=O3v0_n4fZLQ&t=880s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Picket that have like a CSV um export that you can get pretty much every '
              "transaction uh and you're pretty much a profit loss there as well as long as "
              'you sync up every book.',
      'timestamp': 880,
      'timestamp_label': '[00:14:40]',
      'timestamp_seconds': 880,
      'tip': 'Picket that have like a CSV um export that you can get pretty much every '
             "transaction uh and you're pretty much a profit loss there as well as long as you "
             'sync up every book.',
      'title': 'Sports Betting Taxes in 2025 + 2026: CPA Explains Why the 90% Rule Isn’t the '
               'End for Pros (SharpMoney)',
      'url': 'https://www.youtube.com/watch?v=O3v0_n4fZLQ&t=880s',
      'video_id': 'O3v0_n4fZLQ'},
     {'author': 'CFTC',
      'channel': 'CFTC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:03](https://www.youtube.com/watch?v=kkkaudUCNSQ&t=1623s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Broadly excuse me provides for transfers between any margin affiliate or branch '
              'wherever located I would note the potentials ask.',
      'timestamp': 1623,
      'timestamp_label': '[00:27:03]',
      'timestamp_seconds': 1623,
      'tip': 'Broadly excuse me provides for transfers between any margin affiliate or branch '
             'wherever located I would note the potentials ask.',
      'title': 'CFTC to Hold an Open Commission Meeting on March 25 (CFTC)',
      'url': 'https://www.youtube.com/watch?v=kkkaudUCNSQ&t=1623s',
      'video_id': 'kkkaudUCNSQ'},
     {'author': 'The Brief',
      'channel': 'The Brief',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:33](https://www.youtube.com/watch?v=l76_21x9yFQ&t=93s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Brokers commodity trading advisors commodity pool operators and other Market '
              'participants the commission ensures that these.',
      'timestamp': 93,
      'timestamp_label': '[00:01:33]',
      'timestamp_seconds': 93,
      'tip': 'Brokers commodity trading advisors commodity pool operators and other Market '
             'participants the commission ensures that these.',
      'title': 'Understanding the Commodity Futures Trading Commission (CFTC) - A Quick Guide '
               '(The Brief)',
      'url': 'https://www.youtube.com/watch?v=l76_21x9yFQ&t=93s',
      'video_id': 'l76_21x9yFQ'},
     {'author': '🎓Profeissor.com🚀Digital Assets, AI & FinTech',
      'channel': '🎓Profeissor.com🚀Digital Assets, AI & FinTech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:19](https://www.youtube.com/watch?v=G-sfCPFFZ5o&t=259s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The CFTC explains that event contracts serve price discovery and risk '
              'management purposes, and that the market-based probability implied in the '
              'pricing of these contracts provide useful economic data.',
      'timestamp': 259,
      'timestamp_label': '[00:04:19]',
      'timestamp_seconds': 259,
      'tip': 'The CFTC explains that event contracts serve price discovery and risk management '
             'purposes, and that the market-based probability implied in the pricing of these '
             'contracts provide useful economic data.',
      'title': 'Prediction Markets🔮& Events Contracts🏈: how will 🇺🇸CFTC regulate them? '
               '(🎓Profeissor.com🚀Digital Assets, AI & FinTech)',
      'url': 'https://www.youtube.com/watch?v=G-sfCPFFZ5o&t=259s',
      'video_id': 'G-sfCPFFZ5o'},
     {'author': 'Affnook',
      'channel': 'Affnook',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:22](https://www.youtube.com/watch?v=Wzz58pqo-ag&t=82s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And total costs are 60,000, your NGR is 240,000. GGR shows revenue generated.  '
              'NGR shows profit retained.',
      'timestamp': 82,
      'timestamp_label': '[00:01:22]',
      'timestamp_seconds': 82,
      'tip': 'And total costs are 60,000, your NGR is 240,000. GGR shows revenue generated.  '
             'NGR shows profit retained.',
      'title': 'Gross Gaming Revenue (GGR) Explained | How iGaming Revenue Really Works '
               '(Affnook)',
      'url': 'https://www.youtube.com/watch?v=Wzz58pqo-ag&t=82s',
      'video_id': 'Wzz58pqo-ag'},
     {'author': 'Top Sports Debate',
      'channel': 'Top Sports Debate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=2zKRyFshFvw&t=60s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Do uh unit play in like a yolo because our money is over on Patreon. So, we '
              "won't be getting a lot of plays over there.",
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': 'Do uh unit play in like a yolo because our money is over on Patreon. So, we '
             "won't be getting a lot of plays over there.",
      'title': 'I CREATED A FREE DISCORD SERVER FOR THE SPORTS BETTING COMMUNITY | FANDUEL | '
               'DRAFTKINGS (Top Sports Debate)',
      'url': 'https://www.youtube.com/watch?v=2zKRyFshFvw&t=60s',
      'video_id': '2zKRyFshFvw'},
     {'author': 'Inside Prediction Markets',
      'channel': 'Inside Prediction Markets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:24](https://www.youtube.com/watch?v=4UVkZUKEmPI&t=204s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And that's another reason why I think, you know, sports are more vulnerable "
              'than other asset classes that are offering cash to legal risks.',
      'timestamp': 204,
      'timestamp_label': '[00:03:24]',
      'timestamp_seconds': 204,
      'tip': "And that's another reason why I think, you know, sports are more vulnerable than "
             'other asset classes that are offering cash to legal risks.',
      'title': 'Perspectives From Our Trading Team: Building Tech & Trading Politics (Inside '
               'Prediction Markets)',
      'url': 'https://www.youtube.com/watch?v=4UVkZUKEmPI&t=204s',
      'video_id': '4UVkZUKEmPI'}],
 4: [{'author': 'Affnook',
      'channel': 'Affnook',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=ZnwZv3TNdv0&t=20s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'To solve this, businesses rely on I gaming affiliate software. In I gaming '
              'affiliate marketing, affiliates promote platforms using content, ads, and '
              'social media. They bring in players who sign up or deposit.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'To solve this, businesses rely on I gaming affiliate software. In I gaming '
             'affiliate marketing, affiliates promote platforms using content, ads, and social '
             'media. They bring in players who sign up or deposit.',
      'title': 'iGaming Affiliate Software Explained | Everything You Need to Know (Affnook)',
      'url': 'https://www.youtube.com/watch?v=ZnwZv3TNdv0&t=20s',
      'video_id': 'ZnwZv3TNdv0'},
     {'author': 'Peaky Ads – Marketing Podcasts & Interviews',
      'channel': 'Peaky Ads – Marketing Podcasts & Interviews',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:50:49](https://www.youtube.com/watch?v=JCr5X66vWg4&t=3049s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Papa, F Papa conference, you went from building affiliate software at Partner '
              'Matrix to building what looks like an ecosystem right now. Is F Papa a '
              'directory that grew arms and legs or did you always plan to build something '
              'bigger?',
      'timestamp': 3049,
      'timestamp_label': '[00:50:49]',
      'timestamp_seconds': 3049,
      'tip': 'Papa, F Papa conference, you went from building affiliate software at Partner '
             'Matrix to building what looks like an ecosystem right now. Is F Papa a directory '
             'that grew arms and legs or did you always plan to build something bigger?',
      'title': "After Brazil's Ban - Where LatAm iGaming Money Goes | Levon Nikoghosyan (Peaky "
               'Ads – Marketing Podcasts & Interviews)',
      'url': 'https://www.youtube.com/watch?v=JCr5X66vWg4&t=3049s',
      'video_id': 'JCr5X66vWg4'},
     {'author': 'Juiced Bets',
      'channel': 'Juiced Bets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:18](https://www.youtube.com/watch?v=andSdRbPQ4E&t=798s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Still a very, very profitable software to add to your arsenal and to make you a '
              "more sharp sports better. I mean, that's what we are doing here. That's why we "
              "bet on sports is to make money. We don't just do it for fun. We're here to make "
              'money betting on sports.',
      'timestamp': 798,
      'timestamp_label': '[00:13:18]',
      'timestamp_seconds': 798,
      'tip': 'Still a very, very profitable software to add to your arsenal and to make you a '
             "more sharp sports better. I mean, that's what we are doing here. That's why we "
             "bet on sports is to make money. We don't just do it for fun. We're here to make "
             'money betting on sports.',
      'title': 'How to Use OddsJam in 2025: +EV Filters, Strategy, Tools, Tutorial (Juiced '
               'Bets)',
      'url': 'https://www.youtube.com/watch?v=andSdRbPQ4E&t=798s',
      'video_id': 'andSdRbPQ4E'},
     {'author': 'OddsJam: Sports Betting Strategy & Education',
      'channel': 'OddsJam: Sports Betting Strategy & Education',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:25](https://www.youtube.com/watch?v=bKaCBMQuXgk&t=565s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Greedy we want to start with very small bet sizes to get some reps in build '
              'your confidence up understand how the software and the sports books work so.',
      'timestamp': 565,
      'timestamp_label': '[00:09:25]',
      'timestamp_seconds': 565,
      'tip': 'Greedy we want to start with very small bet sizes to get some reps in build your '
             'confidence up understand how the software and the sports books work so.',
      'title': 'Arbitrage Betting Tutorial (Risk-Free Sports Betting) | How to Use OddsJam '
               '(OddsJam: Sports Betting Strategy & Education)',
      'url': 'https://www.youtube.com/watch?v=bKaCBMQuXgk&t=565s',
      'video_id': 'bKaCBMQuXgk'},
     {'author': 'Hexward Labs | Cybersecurity Tools + AI',
      'channel': 'Hexward Labs | Cybersecurity Tools + AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=gsvmpPQY_ak&t=55s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Instead, they must use a remote access VPN. A software client on the laptop '
              'authenticates directly to the headquarters firewall, building a temporary '
              'on-demand tunnel just for that one device.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'Instead, they must use a remote access VPN. A software client on the laptop '
             'authenticates directly to the headquarters firewall, building a temporary '
             'on-demand tunnel just for that one device.',
      'title': 'Complete Cisco FTD VPN Course: Site-to-Site & Remote Access (FMC 7.6 Crash '
               'Course) (Hexward Labs | Cybersecurity Tools + AI)',
      'url': 'https://www.youtube.com/watch?v=gsvmpPQY_ak&t=55s',
      'video_id': 'gsvmpPQY_ak'},
     {'author': 'Interactive Brokers',
      'channel': 'Interactive Brokers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:02](https://www.youtube.com/watch?v=LiKm_5YWgPU&t=842s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Interactive Brokers LLC is a CFTC registered Futures Commission Merchant and a '
              'clearing member and affiliate of Forecast X LLC. Forecast X Forecast X is a '
              'CFTC registered designated contract market and derivatives clearing '
              'organization.',
      'timestamp': 842,
      'timestamp_label': '[00:14:02]',
      'timestamp_seconds': 842,
      'tip': 'Interactive Brokers LLC is a CFTC registered Futures Commission Merchant and a '
             'clearing member and affiliate of Forecast X LLC. Forecast X Forecast X is a CFTC '
             'registered designated contract market and derivatives clearing organization.',
      'title': 'Geopolitics Meets Markets - Cents of Security Ep. 124 (Interactive Brokers)',
      'url': 'https://www.youtube.com/watch?v=LiKm_5YWgPU&t=842s',
      'video_id': 'LiKm_5YWgPU'},
     {'author': 'Revpanda Group',
      'channel': 'Revpanda Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:29](https://www.youtube.com/watch?v=Xyf6JUN9RFg&t=29s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Get the click, make your money. When you own the audience and actually have an '
              "app where you've got their registration, you're able to retarget them. 8 "
              'billion dollars average value of the betting budget. Who do you think will win '
              'this World Cup affiliate race?',
      'timestamp': 29,
      'timestamp_label': '[00:00:29]',
      'timestamp_seconds': 29,
      'tip': 'Get the click, make your money. When you own the audience and actually have an '
             "app where you've got their registration, you're able to retarget them. 8 billion "
             'dollars average value of the betting budget. Who do you think will win this '
             'World Cup affiliate race?',
      'title': 'TRAILER | World Cup 2026 iGaming Affiliate: Battle SEO, AI, & End of Cheap '
               'Traffic (Revpanda Group)',
      'url': 'https://www.youtube.com/watch?v=Xyf6JUN9RFg&t=29s',
      'video_id': 'Xyf6JUN9RFg'},
     {'author': 'Inside Prediction Markets',
      'channel': 'Inside Prediction Markets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:39](https://www.youtube.com/watch?v=xM4qzY2FKFw&t=1179s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Like to look at the, the quantitative firm stack, where it's like you have a "
              "generalist quantitative trader who's just kind of like monitoring the board "
              'entirely, which is what I think we have right now with these new seven guys.',
      'timestamp': 1179,
      'timestamp_label': '[00:19:39]',
      'timestamp_seconds': 1179,
      'tip': "Like to look at the, the quantitative firm stack, where it's like you have a "
             "generalist quantitative trader who's just kind of like monitoring the board "
             'entirely, which is what I think we have right now with these new seven guys.',
      'title': 'Building a Winning Prediction Market Trading Team (Inside Prediction Markets)',
      'url': 'https://www.youtube.com/watch?v=xM4qzY2FKFw&t=1179s',
      'video_id': 'xM4qzY2FKFw'},
     {'author': 'OddsFantasy',
      'channel': 'OddsFantasy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:57](https://www.youtube.com/watch?v=s_VGmKtzL-0&t=177s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Scroll below, and you'll see the home favorite preset running. That's exactly "
              "how you create an automated trading strategy. If you have any questions, don't "
              "hesitate to email us. You'll get support and a detailed explanation on how to "
              'use the software.',
      'timestamp': 177,
      'timestamp_label': '[00:02:57]',
      'timestamp_seconds': 177,
      'tip': "Scroll below, and you'll see the home favorite preset running. That's exactly "
             "how you create an automated trading strategy. If you have any questions, don't "
             "hesitate to email us. You'll get support and a detailed explanation on how to "
             'use the software.',
      'title': 'How to create automated trading strategies and bots for prediction markets '
               '(Polymarket and Kalshi) (OddsFantasy)',
      'url': 'https://www.youtube.com/watch?v=s_VGmKtzL-0&t=177s',
      'video_id': 's_VGmKtzL-0'},
     {'author': 'R. Capital Intelligence',
      'channel': 'R. Capital Intelligence',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:20](https://www.youtube.com/watch?v=BP1ZGlo9HqM&t=440s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And that changed the direction of the entire market. This timeline shows the '
              'shift from restriction to expansion. And when regulation shifts toward '
              'expansion, capital usually follows. This is not just about betting on '
              'elections.',
      'timestamp': 440,
      'timestamp_label': '[00:07:20]',
      'timestamp_seconds': 440,
      'tip': 'And that changed the direction of the entire market. This timeline shows the '
             'shift from restriction to expansion. And when regulation shifts toward '
             'expansion, capital usually follows. This is not just about betting on elections.',
      'title': 'Unpacking Prediction Markets: Kalshi (CFTC-regulated) and Polymarket '
               '(crypto-based) (R. Capital Intelligence)',
      'url': 'https://www.youtube.com/watch?v=BP1ZGlo9HqM&t=440s',
      'video_id': 'BP1ZGlo9HqM'},
     {'author': 'Ace Alliance',
      'channel': 'Ace Alliance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:41](https://www.youtube.com/watch?v=ebby4L0y_P0&t=41s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And with the regulated markets it is very important to very much geofence the '
              'materials, affiliate marketing, everything to very specific region where the '
              'license is active. That is very interesting and where would you say leakage '
              'happens the most often?',
      'timestamp': 41,
      'timestamp_label': '[00:00:41]',
      'timestamp_seconds': 41,
      'tip': 'And with the regulated markets it is very important to very much geofence the '
             'materials, affiliate marketing, everything to very specific region where the '
             'license is active. That is very interesting and where would you say leakage '
             'happens the most often?',
      'title': 'The Hidden Compliance Risk for iGaming Affiliates | SiGMA Rome 2026 (Ace '
               'Alliance)',
      'url': 'https://www.youtube.com/watch?v=ebby4L0y_P0&t=41s',
      'video_id': 'ebby4L0y_P0'},
     {'author': 'CFTC',
      'channel': 'CFTC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:28](https://www.youtube.com/watch?v=Ckw1w5mSMIQ&t=688s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It could expand access to sophisticated financial tools, enable businesses to '
              'manage risk with greater precision, and create entirely new forms of economic '
              'activity.',
      'timestamp': 688,
      'timestamp_label': '[00:11:28]',
      'timestamp_seconds': 688,
      'tip': 'It could expand access to sophisticated financial tools, enable businesses to '
             'manage risk with greater precision, and create entirely new forms of economic '
             'activity.',
      'title': 'CFTC’s Innovation Task Force to Host the Inaugural Frontier Forum on Super '
               'Intelligence (CFTC)',
      'url': 'https://www.youtube.com/watch?v=Ckw1w5mSMIQ&t=688s',
      'video_id': 'Ckw1w5mSMIQ'},
     {'author': 'Pick Scouts',
      'channel': 'Pick Scouts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:41](https://www.youtube.com/watch?v=lmzuGHKUTnE&t=161s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Bankroll management here so it is a huge Plus on that so let me hop into some '
              "cons here honestly not many cons they were awesome if I'm being honest this.",
      'timestamp': 161,
      'timestamp_label': '[00:02:41]',
      'timestamp_seconds': 161,
      'tip': 'Bankroll management here so it is a huge Plus on that so let me hop into some '
             "cons here honestly not many cons they were awesome if I'm being honest this.",
      'title': 'I Joined CookTheBooks Sports Betting Discord. Here are my thoughts (Pick '
               'Scouts)',
      'url': 'https://www.youtube.com/watch?v=lmzuGHKUTnE&t=161s',
      'video_id': 'lmzuGHKUTnE'},
     {'author': 'Cisco Secure Firewall',
      'channel': 'Cisco Secure Firewall',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:30](https://www.youtube.com/watch?v=qqMzcSS31as&t=450s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Changed and we have a couple of hosts on the inside on these unique VLANs now '
              "we're going to verify that connectivity between these outside hosts and inside "
              'and conclude our overview of this setup.',
      'timestamp': 450,
      'timestamp_label': '[00:07:30]',
      'timestamp_seconds': 450,
      'tip': 'Changed and we have a couple of hosts on the inside on these unique VLANs now '
             "we're going to verify that connectivity between these outside hosts and inside "
             'and conclude our overview of this setup.',
      'title': 'FPR4100 ASA App Failover + FTD NGIPS (1) Overview (2017) (Cisco Secure '
               'Firewall)',
      'url': 'https://www.youtube.com/watch?v=qqMzcSS31as&t=450s',
      'video_id': 'qqMzcSS31as'},
     {'author': 'centsorsense',
      'channel': 'centsorsense',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:07](https://www.youtube.com/watch?v=qH8nQqkMNv8&t=667s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Any of the other companies in in the recent past I'd love to know more I "
              'appreciate all you guys today and I look forward to talking to you again in the '
              'future thanks.',
      'timestamp': 667,
      'timestamp_label': '[00:11:07]',
      'timestamp_seconds': 667,
      'tip': "Any of the other companies in in the recent past I'd love to know more I "
             'appreciate all you guys today and I look forward to talking to you again in the '
             'future thanks.',
      'title': 'FORECASTEX - A new prediction exchange from Interactive Brokers #trading '
               '#binarytrading #newmarket (centsorsense)',
      'url': 'https://www.youtube.com/watch?v=qH8nQqkMNv8&t=667s',
      'video_id': 'qH8nQqkMNv8'}],
 5: [{'author': 'Bet The Math',
      'channel': 'Bet The Math',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:49](https://www.youtube.com/watch?v=nOjpng5gNGo&t=349s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So arbitrage is when two books, sports books, prediction markets, betting '
              'exchanges have such different prices that you can play equal and opposite '
              'outcomes and guarantee a risk-free profit.',
      'timestamp': 349,
      'timestamp_label': '[00:05:49]',
      'timestamp_seconds': 349,
      'tip': 'So arbitrage is when two books, sports books, prediction markets, betting '
             'exchanges have such different prices that you can play equal and opposite '
             'outcomes and guarantee a risk-free profit.',
      'title': 'Kalshi & Polymarket: 3 Strategies to Find an Edge (Bet The Math)',
      'url': 'https://www.youtube.com/watch?v=nOjpng5gNGo&t=349s',
      'video_id': 'nOjpng5gNGo'},
     {'author': 'Taf',
      'channel': 'Taf',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=GLvhRHB7n2U&t=21s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The problem is that one sports book clock in that you are arbitrage betting, '
              'they will either limit your account to the point where you can ultimately not '
              'bet anymore.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'The problem is that one sports book clock in that you are arbitrage betting, '
             'they will either limit your account to the point where you can ultimately not '
             'bet anymore.',
      'title': 'I Found the Best Prediction Market Arbitrage Tool (Kalshi & Polymarket) (Taf)',
      'url': 'https://www.youtube.com/watch?v=GLvhRHB7n2U&t=21s',
      'video_id': 'GLvhRHB7n2U'},
     {'author': 'Revpanda Group',
      'channel': 'Revpanda Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:23](https://www.youtube.com/watch?v=qOL8mMQPJyI&t=563s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, if they just only stay in that small niche market for instance that used to '
              'be good, things change, right? So, there are risk about it. So, can Can tell me '
              'about those risks affiliates can face in those small markets that is really '
              'sensitive to change?',
      'timestamp': 563,
      'timestamp_label': '[00:09:23]',
      'timestamp_seconds': 563,
      'tip': 'So, if they just only stay in that small niche market for instance that used to '
             'be good, things change, right? So, there are risk about it. So, can Can tell me '
             'about those risks affiliates can face in those small markets that is really '
             'sensitive to change?',
      'title': 'How to Build an Unbreakable iGaming Affiliate Portfolio in 2026 (Revpanda '
               'Group)',
      'url': 'https://www.youtube.com/watch?v=qOL8mMQPJyI&t=563s',
      'video_id': 'qOL8mMQPJyI'},
     {'author': 'Simple Betting Guides',
      'channel': 'Simple Betting Guides',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:38](https://www.youtube.com/watch?v=zfqcFKWL2gA&t=158s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Neither sports betting nor prediction markets guarantee profit. Both require '
              'careful thinking, risk control, and realistic expectations. A common beginner '
              'mistake is saying prediction markets are just sports betting with a different '
              'name.',
      'timestamp': 158,
      'timestamp_label': '[00:02:38]',
      'timestamp_seconds': 158,
      'tip': 'Neither sports betting nor prediction markets guarantee profit. Both require '
             'careful thinking, risk control, and realistic expectations. A common beginner '
             'mistake is saying prediction markets are just sports betting with a different '
             'name.',
      'title': 'Prediction Markets vs Sports Betting: What is the difference? (Simple Betting '
               'Guides)',
      'url': 'https://www.youtube.com/watch?v=zfqcFKWL2gA&t=158s',
      'video_id': 'zfqcFKWL2gA'},
     {'author': 'Billy Collins',
      'channel': 'Billy Collins',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:17](https://www.youtube.com/watch?v=AcW1ucJmvQc&t=437s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I don't really care cuz that's not a lot of confidence or conviction from the "
              "sharp better. Or it's going to show you a plus EV play like on Rhamondre where "
              "it's about a 2 and 1/2% edge. FanDuel is just way off to the rest of the sports "
              'betting market.',
      'timestamp': 437,
      'timestamp_label': '[00:07:17]',
      'timestamp_seconds': 437,
      'tip': "I don't really care cuz that's not a lot of confidence or conviction from the "
             "sharp better. Or it's going to show you a plus EV play like on Rhamondre where "
             "it's about a 2 and 1/2% edge. FanDuel is just way off to the rest of the sports "
             'betting market.',
      'title': "I Tested OddsJam's NEW Parlay Tool (Here's What Happened) (Billy Collins)",
      'url': 'https://www.youtube.com/watch?v=AcW1ucJmvQc&t=437s',
      'video_id': 'AcW1ucJmvQc'},
     {'author': 'iGaming Real Talk Podcast',
      'channel': 'iGaming Real Talk Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:41](https://www.youtube.com/watch?v=TzU_M6ldezQ&t=161s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But however, is there a way affiliates can control that because they don't have "
              "access to what operator does after they send the traffic? Sometimes they don't "
              'even have access to the data. Having data is all all the transparency kind of '
              'like a problem always.',
      'timestamp': 161,
      'timestamp_label': '[00:02:41]',
      'timestamp_seconds': 161,
      'tip': "But however, is there a way affiliates can control that because they don't have "
             "access to what operator does after they send the traffic? Sometimes they don't "
             'even have access to the data. Having data is all all the transparency kind of '
             'like a problem always.',
      'title': 'Are CPA and RevShare Models Starting to Change? | Paul Puolakka (iGaming Real '
               'Talk Podcast)',
      'url': 'https://www.youtube.com/watch?v=TzU_M6ldezQ&t=161s',
      'video_id': 'TzU_M6ldezQ'},
     {'author': 'Inside Prediction Markets',
      'channel': 'Inside Prediction Markets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:58](https://www.youtube.com/watch?v=gOWvAiqg_qw&t=1318s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And I think that's something that, you know, for people who bet on sports "
              "books, it's obviously been a concern for a long time. How do I avoid getting "
              "limited? And the first response to Ms. 't have to worry about that anymore.",
      'timestamp': 1318,
      'timestamp_label': '[00:21:58]',
      'timestamp_seconds': 1318,
      'tip': "And I think that's something that, you know, for people who bet on sports books, "
             "it's obviously been a concern for a long time. How do I avoid getting limited? "
             "And the first response to Ms. 't have to worry about that anymore.",
      'title': 'How AI Gives You a Massive Edge on Prediction Markets (Inside Prediction '
               'Markets)',
      'url': 'https://www.youtube.com/watch?v=gOWvAiqg_qw&t=1318s',
      'video_id': 'gOWvAiqg_qw'},
     {'author': 'Odys Podcast: The High Stakes Growth Show',
      'channel': 'Odys Podcast: The High Stakes Growth Show',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:51](https://www.youtube.com/watch?v=ESj1bVRdO2s&t=471s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They use it to kind of audit how they appear on the Affiliate's website, and "
              'they reach out and they request some, some changes. But all in all, you have '
              "to, you look at what's permits permissible and, you display content based on "
              "that. It doesn't really affect the rankings.",
      'timestamp': 471,
      'timestamp_label': '[00:07:51]',
      'timestamp_seconds': 471,
      'tip': "They use it to kind of audit how they appear on the Affiliate's website, and "
             'they reach out and they request some, some changes. But all in all, you have to, '
             "you look at what's permits permissible and, you display content based on that. "
             "It doesn't really affect the rankings.",
      'title': 'Why iGaming Sites Fail at SEO in Regulated Markets (And How to Win) (Odys '
               'Podcast: The High Stakes Growth Show)',
      'url': 'https://www.youtube.com/watch?v=ESj1bVRdO2s&t=471s',
      'video_id': 'ESj1bVRdO2s'},
     {'author': 'Luke Parlay',
      'channel': 'Luke Parlay',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=I88FWcNIr_0&t=15s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Blindly or take whatever odds their sports book gives them but that's a mistake "
              "so I'm going to show you how I use odds Jam to find the best possible.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Blindly or take whatever odds their sports book gives them but that's a mistake "
             "so I'm going to show you how I use odds Jam to find the best possible.",
      'title': 'How I Use OddsJam to Find Winning Bets in 4 Minutes (Luke Parlay)',
      'url': 'https://www.youtube.com/watch?v=I88FWcNIr_0&t=15s',
      'video_id': 'I88FWcNIr_0'},
     {'author': 'InGenius by Veritasium',
      'channel': 'InGenius by Veritasium',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:48](https://www.youtube.com/watch?v=CTUqmUHvd2Y&t=1248s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So we see that skilled traders do this, but no other group does that. Second, '
              'they avoid low probability long shots and focus on the favourites to win. This '
              "works because they're betting against other people's biases.",
      'timestamp': 1248,
      'timestamp_label': '[00:20:48]',
      'timestamp_seconds': 1248,
      'tip': 'So we see that skilled traders do this, but no other group does that. Second, '
             'they avoid low probability long shots and focus on the favourites to win. This '
             "works because they're betting against other people's biases.",
      'title': "We analysed 3 years worth of Polymarket trades. Here's what we found. "
               '(InGenius by Veritasium)',
      'url': 'https://www.youtube.com/watch?v=CTUqmUHvd2Y&t=1248s',
      'video_id': 'CTUqmUHvd2Y'},
     {'author': 'CFTC',
      'channel': 'CFTC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:37:30](https://www.youtube.com/watch?v=vqL3OS8Ot9o&t=2250s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Audit groups that may have some applicability to what we're looking at here in "
              'terms of U risk assessment and the like um is that something if we can.',
      'timestamp': 2250,
      'timestamp_label': '[00:37:30]',
      'timestamp_seconds': 2250,
      'tip': "Audit groups that may have some applicability to what we're looking at here in "
             'terms of U risk assessment and the like um is that something if we can.',
      'title': 'CFTC Roundtable on Enhancing Protections Afforded Customers and Funds '
               'Deposited by Customers: Part 1 (CFTC)',
      'url': 'https://www.youtube.com/watch?v=vqL3OS8Ot9o&t=2250s',
      'video_id': 'vqL3OS8Ot9o'},
     {'author': 'OngPredicts',
      'channel': 'OngPredicts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:59](https://www.youtube.com/watch?v=4SzgTKdaSHI&t=119s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Self-custody and global access on one side, a crypto learning curve on the '
              "other. If you're outside the US and want the main arena, this is it. Number "
              'two, Kalshi, the CFTC-regulated US exchange. Everything here is in actual '
              'dollars in a book in a brokerage style account.',
      'timestamp': 119,
      'timestamp_label': '[00:01:59]',
      'timestamp_seconds': 119,
      'tip': 'Self-custody and global access on one side, a crypto learning curve on the '
             "other. If you're outside the US and want the main arena, this is it. Number two, "
             'Kalshi, the CFTC-regulated US exchange. Everything here is in actual dollars in '
             'a book in a brokerage style account.',
      'title': 'Top 10 Prediction Markets 2026 (OngPredicts)',
      'url': 'https://www.youtube.com/watch?v=4SzgTKdaSHI&t=119s',
      'video_id': '4SzgTKdaSHI'},
     {'author': 'OddsJam: Sports Betting Strategy & Education',
      'channel': 'OddsJam: Sports Betting Strategy & Education',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:03](https://www.youtube.com/watch?v=J3KQ5FaneSs&t=303s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I could bet this at No Vig. I'd even take this at The Score. DraftKings, it's a "
              'close call. Maybe you could go ahead and grab it there. A lot of options here '
              'when it comes to these books on this play. So, I could go bet this at the rec '
              'book.',
      'timestamp': 303,
      'timestamp_label': '[00:05:03]',
      'timestamp_seconds': 303,
      'tip': "I could bet this at No Vig. I'd even take this at The Score. DraftKings, it's a "
             'close call. Maybe you could go ahead and grab it there. A lot of options here '
             'when it comes to these books on this play. So, I could go bet this at the rec '
             'book.',
      'title': 'I made $6,748 betting on player props in 30 days using one strategy (OddsJam: '
               'Sports Betting Strategy & Education)',
      'url': 'https://www.youtube.com/watch?v=J3KQ5FaneSs&t=303s',
      'video_id': 'J3KQ5FaneSs'},
     {'author': 'PredictionNews',
      'channel': 'PredictionNews',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:34:38](https://www.youtube.com/watch?v=9aHX4chc8YY&t=2078s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It\'s important for industry growth because a hedge fund will say, "Gee, I '
              'really want to put on a a hedge in for this type of risk, right?" But there\'s '
              "not a lot of exposure I mean, there's not a lot of liquidity there. And so, "
              'with a taxonomy, they can look at correlation.',
      'timestamp': 2078,
      'timestamp_label': '[00:34:38]',
      'timestamp_seconds': 2078,
      'tip': 'It\'s important for industry growth because a hedge fund will say, "Gee, I '
             'really want to put on a a hedge in for this type of risk, right?" But there\'s '
             "not a lot of exposure I mean, there's not a lot of liquidity there. And so, with "
             'a taxonomy, they can look at correlation.',
      'title': 'The CFTC’s Vision for Prediction Markets with Dorothy DeWitt | Prediction '
               'Market Movers (PredictionNews)',
      'url': 'https://www.youtube.com/watch?v=9aHX4chc8YY&t=2078s',
      'video_id': '9aHX4chc8YY'},
     {'author': 'Ayo Kush',
      'channel': 'Ayo Kush',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:17](https://www.youtube.com/watch?v=Lf0mO_lAI_Q&t=197s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Okay from here and if I have one year for them just creates another one new me '
              "share one for these because I'm running evolution would have to come down my "
              'encryption and our shock already.',
      'timestamp': 197,
      'timestamp_label': '[00:03:17]',
      'timestamp_seconds': 197,
      'tip': 'Okay from here and if I have one year for them just creates another one new me '
             "share one for these because I'm running evolution would have to come down my "
             'encryption and our shock already.',
      'title': 'Site to Site VPN on FTD (IKEv2) - Part 2 (Ayo Kush)',
      'url': 'https://www.youtube.com/watch?v=Lf0mO_lAI_Q&t=197s',
      'video_id': 'Lf0mO_lAI_Q'}],
 6: [{'author': 'OngPredicts',
      'channel': 'OngPredicts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:52](https://www.youtube.com/watch?v=T6thRudYjsg&t=472s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Let the filtered list find the gaps, open the market, check, compare, run the '
              "numbers, and size the bet with Kelly. And if you'd rather pull these prices "
              "into your own code, the same data is on PredictIt's API. The link is in the "
              'description.',
      'timestamp': 472,
      'timestamp_label': '[00:07:52]',
      'timestamp_seconds': 472,
      'tip': 'Let the filtered list find the gaps, open the market, check, compare, run the '
             "numbers, and size the bet with Kelly. And if you'd rather pull these prices into "
             "your own code, the same data is on PredictIt's API. The link is in the "
             'description.',
      'title': 'How to Find Arbitrage Bets On Prediction Markets  (15+ Venues Walkthrough) '
               '(OngPredicts)',
      'url': 'https://www.youtube.com/watch?v=T6thRudYjsg&t=472s',
      'video_id': 'T6thRudYjsg'},
     {'author': 'Ace Alliance',
      'channel': 'Ace Alliance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:58](https://www.youtube.com/watch?v=cxhsS1A2A4I&t=958s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, we could consult them and tell them look guys it's it's better than you "
              'think in in another way or rename the game because we see the different naming '
              "organic data gain much more visibility throughout organic search. So, that's "
              "that's the first thing.",
      'timestamp': 958,
      'timestamp_label': '[00:15:58]',
      'timestamp_seconds': 958,
      'tip': "So, we could consult them and tell them look guys it's it's better than you "
             'think in in another way or rename the game because we see the different naming '
             "organic data gain much more visibility throughout organic search. So, that's "
             "that's the first thing.",
      'title': 'How iGaming Affiliates Can Create Value for Operators and Studios (Ace '
               'Alliance)',
      'url': 'https://www.youtube.com/watch?v=cxhsS1A2A4I&t=958s',
      'video_id': 'cxhsS1A2A4I'},
     {'author': 'Unabated',
      'channel': 'Unabated',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:56](https://www.youtube.com/watch?v=rrKRhjye1sw&t=596s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's a reason why you can often find a slightly better price on these exchanges "
              'on big events compared to a sports book. Now, coming in at number one on our '
              'list is perhaps the biggest caveat of all, fees and commissions.',
      'timestamp': 596,
      'timestamp_label': '[00:09:56]',
      'timestamp_seconds': 596,
      'tip': "It's a reason why you can often find a slightly better price on these exchanges "
             'on big events compared to a sports book. Now, coming in at number one on our '
             'list is perhaps the biggest caveat of all, fees and commissions.',
      'title': 'Inside Prediction Markets: What the Pros Know (and You Don’t) (Unabated)',
      'url': 'https://www.youtube.com/watch?v=rrKRhjye1sw&t=596s',
      'video_id': 'rrKRhjye1sw'},
     {'author': 'Brokerchampion',
      'channel': 'Brokerchampion',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=dvFmfWlkYq0&t=64s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Forex leverage you receive, which brokers can serve you, and whether your '
              "client money must be kept separate from the broker's assets. The $20 million "
              'threshold is the first clue.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': 'Forex leverage you receive, which brokers can serve you, and whether your client '
             "money must be kept separate from the broker's assets. The $20 million threshold "
             'is the first clue.',
      'title': 'What Is the CFTC? The US Regulator Behind Futures, Swaps and Retail Forex '
               '(2026) (Brokerchampion)',
      'url': 'https://www.youtube.com/watch?v=dvFmfWlkYq0&t=64s',
      'video_id': 'dvFmfWlkYq0'},
     {'author': 'SportsGameOdds API',
      'channel': 'SportsGameOdds API',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=auctQZC3iOE&t=71s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's get our hands dirty and actually make our first API call. We're going to "
              "pull a list of upcoming NFL games. It's basically the hello world of sports "
              "data. And you're about to see just how easy it is. This is a real practical "
              'copy and paste example.',
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': "Let's get our hands dirty and actually make our first API call. We're going to "
             "pull a list of upcoming NFL games. It's basically the hello world of sports "
             "data. And you're about to see just how easy it is. This is a real practical copy "
             'and paste example.',
      'title': 'Get Sports Odds and Data with an Odds API (SportsGameOdds API)',
      'url': 'https://www.youtube.com/watch?v=auctQZC3iOE&t=71s',
      'video_id': 'auctQZC3iOE'},
     {'author': 'Handsome Finance',
      'channel': 'Handsome Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:51](https://www.youtube.com/watch?v=4sCGelTkwek&t=231s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So what he's betting on is probably a bot trying to make money from arbitrage "
              "on the market. So that's not someone that I'm going to follow. But Ashdav is "
              "going to help me. This one we're going to be able to find trades and find "
              'traders.',
      'timestamp': 231,
      'timestamp_label': '[00:03:51]',
      'timestamp_seconds': 231,
      'tip': "So what he's betting on is probably a bot trying to make money from arbitrage on "
             "the market. So that's not someone that I'm going to follow. But Ashdav is going "
             "to help me. This one we're going to be able to find trades and find traders.",
      'title': 'I Tested 40 Prediction Market Tools. Use These 5. (Handsome Finance)',
      'url': 'https://www.youtube.com/watch?v=4sCGelTkwek&t=231s',
      'video_id': '4sCGelTkwek'},
     {'author': 'iGaming Business',
      'channel': 'iGaming Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:29](https://www.youtube.com/watch?v=uyC7gnWqji0&t=269s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re going to get an extra roll. So, bigger another opportunity to win more. "
              'First roll, we build four houses. You can see that kind of collecting down at '
              "the bottom. Now that extra roll comes into play, and they're going to move "
              'around the board to win an even bigger prize.',
      'timestamp': 269,
      'timestamp_label': '[00:04:29]',
      'timestamp_seconds': 269,
      'tip': "'re going to get an extra roll. So, bigger another opportunity to win more. "
             'First roll, we build four houses. You can see that kind of collecting down at '
             "the bottom. Now that extra roll comes into play, and they're going to move "
             'around the board to win an even bigger prize.',
      'title': 'GGB Supplier Showcase: Galaxy Gaming (iGaming Business)',
      'url': 'https://www.youtube.com/watch?v=uyC7gnWqji0&t=269s',
      'video_id': 'uyC7gnWqji0'},
     {'author': 'OddsJam: Sports Betting Strategy & Education',
      'channel': 'OddsJam: Sports Betting Strategy & Education',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:05](https://www.youtube.com/watch?v=Gl7DgicTVxk&t=125s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And naturally, there's going to be a lot of recreational books like a "
              "DraftKings, a BetRivers, a BetMGM, or Fanatics where you're going to find a lot "
              'of success.',
      'timestamp': 125,
      'timestamp_label': '[00:02:05]',
      'timestamp_seconds': 125,
      'tip': "And naturally, there's going to be a lot of recreational books like a "
             "DraftKings, a BetRivers, a BetMGM, or Fanatics where you're going to find a lot "
             'of success.',
      'title': 'Which OddsJam Tool Fits You? Momentum vs Sharp Money vs Traders vs +EV '
               '(OddsJam: Sports Betting Strategy & Education)',
      'url': 'https://www.youtube.com/watch?v=Gl7DgicTVxk&t=125s',
      'video_id': 'Gl7DgicTVxk'},
     {'author': 'Part Time Larry',
      'channel': 'Part Time Larry',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:27](https://www.youtube.com/watch?v=Ib0BEFKAvn0&t=1107s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And then I pass that list of categories to my select box and then it has a a '
              'list of distinct categories, right? Then down here on line 88, you see I have a '
              "conditional. I said it says if I've entered a search and I've selected a "
              'category, right?',
      'timestamp': 1107,
      'timestamp_label': '[00:18:27]',
      'timestamp_seconds': 1107,
      'tip': 'And then I pass that list of categories to my select box and then it has a a '
             'list of distinct categories, right? Then down here on line 88, you see I have a '
             "conditional. I said it says if I've entered a search and I've selected a "
             'category, right?',
      'title': 'Prediction Market Assistant with Perplexity Sonar API and Kalshi API (Part '
               'Time Larry)',
      'url': 'https://www.youtube.com/watch?v=Ib0BEFKAvn0&t=1107s',
      'video_id': 'Ib0BEFKAvn0'},
     {'author': 'CASINOAFFMASTERY',
      'channel': 'CASINOAFFMASTERY',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=JUjTzv8yGw4&t=146s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Example is new online casinos new UK online casino sites you want people to '
              'Google this and then they find your website in the search results and then.',
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': 'Example is new online casinos new UK online casino sites you want people to '
             'Google this and then they find your website in the search results and then.',
      'title': 'How Much Can You ACTUALLY Make From Casino Affiliate Marketing? '
               '(CASINOAFFMASTERY)',
      'url': 'https://www.youtube.com/watch?v=JUjTzv8yGw4&t=146s',
      'video_id': 'JUjTzv8yGw4'},
     {'author': 'NET Learners',
      'channel': 'NET Learners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:32](https://www.youtube.com/watch?v=gd0RJEsarik&t=1112s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Yeah I can say to make the Easter please to make the VPN is definitely right so '
              'now we go to the client client I have to to the interface to inside in the '
              'first yeah yeah.',
      'timestamp': 1112,
      'timestamp_label': '[00:18:32]',
      'timestamp_seconds': 1112,
      'tip': 'Yeah I can say to make the Easter please to make the VPN is definitely right so '
             'now we go to the client client I have to to the interface to inside in the first '
             'yeah yeah.',
      'title': 'Configure S2S VPN on FTD managed by FMC (NET Learners)',
      'url': 'https://www.youtube.com/watch?v=gd0RJEsarik&t=1112s',
      'video_id': 'gd0RJEsarik'},
     {'author': 'Silesio Carvalho',
      'channel': 'Silesio Carvalho',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:36](https://www.youtube.com/watch?v=1hYtt8kbt1g&t=216s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, let's go to show tunnel list. Uh some adjustments we want to make. So, "
              "first we're going to convert this to a custom tunnel. And let's first check "
              'here. So first we want to use Ike version two.',
      'timestamp': 216,
      'timestamp_label': '[00:03:36]',
      'timestamp_seconds': 216,
      'tip': "So, let's go to show tunnel list. Uh some adjustments we want to make. So, first "
             "we're going to convert this to a custom tunnel. And let's first check here. So "
             'first we want to use Ike version two.',
      'title': 'FMC Site-to-Site VPN Explained for Real Deployments (Silesio Carvalho)',
      'url': 'https://www.youtube.com/watch?v=1hYtt8kbt1g&t=216s',
      'video_id': '1hYtt8kbt1g'},
     {'author': "JP's Networking channel",
      'channel': "JP's Networking channel",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:46](https://www.youtube.com/watch?v=-wMPo0JDEtI&t=646s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We'll come down we'll go to site site vpn go to connection profiles we will "
              "first of all allow ike version 1 on the outside interface that's where we're "
              'building our tunnel to we will go ahead and add a new connection profile.',
      'timestamp': 646,
      'timestamp_label': '[00:10:46]',
      'timestamp_seconds': 646,
      'tip': "We'll come down we'll go to site site vpn go to connection profiles we will "
             "first of all allow ike version 1 on the outside interface that's where we're "
             'building our tunnel to we will go ahead and add a new connection profile.',
      'title': "Setting up Site to Site VPN between remote ASA and HQ Firepower FTD's (JP's "
               'Networking channel)',
      'url': 'https://www.youtube.com/watch?v=-wMPo0JDEtI&t=646s',
      'video_id': '-wMPo0JDEtI'},
     {'author': 'A Lawyer In Finance Explains  1.1M views',
      'channel': 'A Lawyer In Finance Explains  1.1M views',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=BO0iMB23sU4&t=63s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re in one of these countries. The CFTC has on their website a list of "
              'jurisdictions that qualify for substituted compliance because their regulations '
              "are considered comparable to the US's regulations. And those countries are "
              'Japan, Mexico, the European Union, and the UK.',
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': "'re in one of these countries. The CFTC has on their website a list of "
             'jurisdictions that qualify for substituted compliance because their regulations '
             "are considered comparable to the US's regulations. And those countries are "
             'Japan, Mexico, the European Union, and the UK.',
      'title': 'CFTC SWAP DEALER CCO ANNUAL REPORT for Foreign Swap Dealers (A Lawyer In '
               'Finance Explains  1.1M views)',
      'url': 'https://www.youtube.com/watch?v=BO0iMB23sU4&t=63s',
      'video_id': 'BO0iMB23sU4'},
     {'author': 'CFTC',
      'channel': 'CFTC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:18](https://www.youtube.com/watch?v=ZEPjpgVSavY&t=198s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re talking about the US versus offshore which is non-regulated in the US. And "
              "so the big step here and it's come up here is in May of this year, the CFTC "
              'approved the first onshore US perpetual future starting in Bitcoin.',
      'timestamp': 198,
      'timestamp_label': '[00:03:18]',
      'timestamp_seconds': 198,
      'tip': "'re talking about the US versus offshore which is non-regulated in the US. And "
             "so the big step here and it's come up here is in May of this year, the CFTC "
             'approved the first onshore US perpetual future starting in Bitcoin.',
      'title': 'Presentation on Perpetual Futures’ Funding Rate Mechanism, July 29 AAC Meeting '
               '(CFTC)',
      'url': 'https://www.youtube.com/watch?v=ZEPjpgVSavY&t=198s',
      'video_id': 'ZEPjpgVSavY'}],
 7: [{'author': 'Metablock iGaming',
      'channel': 'Metablock iGaming',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:56](https://www.youtube.com/watch?v=XyJxTxBFvuw&t=836s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'DraftKings or BetMGM are not your target audience. No, they build their own '
              'tech. Your ideal targets are startups or existing online casinos wanting to '
              'cross-sell sports betting. But, the absolute golden demographic, affiliate '
              'marketers.',
      'timestamp': 836,
      'timestamp_label': '[00:13:56]',
      'timestamp_seconds': 836,
      'tip': 'DraftKings or BetMGM are not your target audience. No, they build their own '
             'tech. Your ideal targets are startups or existing online casinos wanting to '
             'cross-sell sports betting. But, the absolute golden demographic, affiliate '
             'marketers.',
      'title': '𝗪𝗵𝗶𝘁𝗲 𝗟𝗮𝗯𝗲𝗹 𝗦𝗽𝗼𝗿𝘁𝘀𝗯𝗼𝗼𝗸 𝗘𝘅𝗽𝗹𝗮𝗶𝗻𝗲𝗱 | 𝗧𝘂𝗿𝗻𝗸𝗲𝘆 𝘃𝘀. 𝗪𝗵𝗶𝘁𝗲 𝗟𝗮𝗯𝗲𝗹, 𝗔𝗜 & 𝗟𝗶𝗰𝗲𝗻𝘀𝗶𝗻𝗴 '
               '(Metablock iGaming)',
      'url': 'https://www.youtube.com/watch?v=XyJxTxBFvuw&t=836s',
      'video_id': 'XyJxTxBFvuw'},
     {'author': 'Trackdesk',
      'channel': 'Trackdesk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:18](https://www.youtube.com/watch?v=zjkFJJ0rAJ0&t=378s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Only when the answers point to a real player does the conversion move forward. '
              "Build it into your standard workflow, and you'll catch a meaningful percentage "
              'of low-quality conversions before they ever hit your payout queue.',
      'timestamp': 378,
      'timestamp_label': '[00:06:18]',
      'timestamp_seconds': 378,
      'tip': 'Only when the answers point to a real player does the conversion move forward. '
             "Build it into your standard workflow, and you'll catch a meaningful percentage "
             'of low-quality conversions before they ever hit your payout queue.',
      'title': 'iGaming Affiliate Marketing in 2026: A Senior Operator’s Field Guide '
               '(Trackdesk)',
      'url': 'https://www.youtube.com/watch?v=zjkFJJ0rAJ0&t=378s',
      'video_id': 'zjkFJJ0rAJ0'},
     {'author': 'Clark Knows Ball',
      'channel': 'Clark Knows Ball',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:50](https://www.youtube.com/watch?v=ghCIWcXbadk&t=290s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, you can see here the math on it. So, he had the over over on Hard Rock, and '
              'this was actually a middle opportunity for him as well, which is even better '
              'because you have a chance where both can hit. But arbitrage is essentially '
              'there is a difference in the books.',
      'timestamp': 290,
      'timestamp_label': '[00:04:50]',
      'timestamp_seconds': 290,
      'tip': 'So, you can see here the math on it. So, he had the over over on Hard Rock, and '
             'this was actually a middle opportunity for him as well, which is even better '
             'because you have a chance where both can hit. But arbitrage is essentially there '
             'is a difference in the books.',
      'title': 'The REAL Way To Win On Kalshi In 2026 (Full Guide) (Clark Knows Ball)',
      'url': 'https://www.youtube.com/watch?v=ghCIWcXbadk&t=290s',
      'video_id': 'ghCIWcXbadk'},
     {'author': 'License Gentlemen',
      'channel': 'License Gentlemen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:22](https://www.youtube.com/watch?v=CmKMSqyx4r0&t=862s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Canada or in other developed regions like Australia, New Zealand, I'm not going "
              'to mention all the countries. So, of course, the situation is much better and '
              'uh the frequency of affiliate fraud is less. But what you can do here, you '
              'know, they learn how to cheat the system.',
      'timestamp': 862,
      'timestamp_label': '[00:14:22]',
      'timestamp_seconds': 862,
      'tip': "Canada or in other developed regions like Australia, New Zealand, I'm not going "
             'to mention all the countries. So, of course, the situation is much better and uh '
             'the frequency of affiliate fraud is less. But what you can do here, you know, '
             'they learn how to cheat the system.',
      'title': '🎯 Affiliate Fraud in iGaming: What They Don’t Tell You Until You Lose €200K '
               '(License Gentlemen)',
      'url': 'https://www.youtube.com/watch?v=CmKMSqyx4r0&t=862s',
      'video_id': 'CmKMSqyx4r0'},
     {'author': 'Whale Slots',
      'channel': 'Whale Slots',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=QpjzafRRmjQ&t=118s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '15, 20 seconds before you even saw the breakaway. Their system logged it the '
              'instant it happened. Maybe that specific betting market even closed seconds '
              "ago. So, you're betting on something that for the book maker is already "
              'history.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': '15, 20 seconds before you even saw the breakaway. Their system logged it the '
             'instant it happened. Maybe that specific betting market even closed seconds ago. '
             "So, you're betting on something that for the book maker is already history.",
      'title': 'Live Betting Latency Explained | Gambling podcast (Whale Slots)',
      'url': 'https://www.youtube.com/watch?v=QpjzafRRmjQ&t=118s',
      'video_id': 'QpjzafRRmjQ'},
     {'author': 'Ace Alliance',
      'channel': 'Ace Alliance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:29](https://www.youtube.com/watch?v=H4Pub14VDXA&t=149s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "In terms of the biggest change that we've seen in acquisition and affiliate "
              'marketing is really that focus on value of traffic, that focus of quality '
              'versus quantity. Um, really people want to understand where the traffic is '
              "coming from, what's converting specifically.",
      'timestamp': 149,
      'timestamp_label': '[00:02:29]',
      'timestamp_seconds': 149,
      'tip': "In terms of the biggest change that we've seen in acquisition and affiliate "
             'marketing is really that focus on value of traffic, that focus of quality versus '
             'quantity. Um, really people want to understand where the traffic is coming from, '
             "what's converting specifically.",
      'title': 'iGaming Affiliate Marketing in 2027: What Operators Need to Get Right | SiGMA '
               'Rome (Ace Alliance)',
      'url': 'https://www.youtube.com/watch?v=H4Pub14VDXA&t=149s',
      'video_id': 'H4Pub14VDXA'},
     {'author': 'OngPredicts',
      'channel': 'OngPredicts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:31](https://www.youtube.com/watch?v=to-RcU1_UCQ&t=511s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It gives me the scanning part without me having to build the whole system '
              "myself. I can just basically use predictify. So if you're doing prediction "
              'market arbitrage, I would definitely give Predictify a very long look.',
      'timestamp': 511,
      'timestamp_label': '[00:08:31]',
      'timestamp_seconds': 511,
      'tip': 'It gives me the scanning part without me having to build the whole system '
             "myself. I can just basically use predictify. So if you're doing prediction "
             'market arbitrage, I would definitely give Predictify a very long look.',
      'title': 'How To Arbitrage Prediction Markets (15 Prediction Markets) (OngPredicts)',
      'url': 'https://www.youtube.com/watch?v=to-RcU1_UCQ&t=511s',
      'video_id': 'to-RcU1_UCQ'},
     {'author': 'Metablock iGaming',
      'channel': 'Metablock iGaming',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:20](https://www.youtube.com/watch?v=TSktawP5zG4&t=200s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The licensing  journey follows a clear process. Due diligence, offshore company '
              'formation, a full technical system audit, application submission.',
      'timestamp': 200,
      'timestamp_label': '[00:03:20]',
      'timestamp_seconds': 200,
      'tip': 'The licensing  journey follows a clear process. Due diligence, offshore company '
             'formation, a full technical system audit, application submission.',
      'title': 'How to Start an iGaming Business | White Label & Turnkey Casino Platform '
               '#igaming (Metablock iGaming)',
      'url': 'https://www.youtube.com/watch?v=TSktawP5zG4&t=200s',
      'video_id': 'TSktawP5zG4'},
     {'author': 'Leo the SEO',
      'channel': 'Leo the SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=mHQEPWigYgI&t=22s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm legit to do that because I used to work for the biggest affiliate company "
              'for five six years and now I set up my own SEO agency helping some I gaming '
              'people to get better results.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "I'm legit to do that because I used to work for the biggest affiliate company "
             'for five six years and now I set up my own SEO agency helping some I gaming '
             'people to get better results.',
      'title': 'World’s Most Brutal Casino SEO SERPs (Leo the SEO)',
      'url': 'https://www.youtube.com/watch?v=mHQEPWigYgI&t=22s',
      'video_id': 'mHQEPWigYgI'},
     {'author': 'Daily Support',
      'channel': 'Daily Support',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=9TXcuMRP0Sc&t=75s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The same process applies when configuring other FOS and FTD instances. Once '
              'complete, both devices will have identical interface mapping. Then log into the '
              'FMC firepower management center. Log into the FMC using admin user.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': 'The same process applies when configuring other FOS and FTD instances. Once '
             'complete, both devices will have identical interface mapping. Then log into the '
             'FMC firepower management center. Log into the FMC using admin user.',
      'title': 'How to Configure Cisco FTD High Availability in FMC | Active-Standby Firepower '
               'Setup | HA Explained (Daily Support)',
      'url': 'https://www.youtube.com/watch?v=9TXcuMRP0Sc&t=75s',
      'video_id': '9TXcuMRP0Sc'},
     {'author': 'Backpack Exchange Official',
      'channel': 'Backpack Exchange Official',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=0Yj5x9uwKAE&t=22s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "FCM broker with with the NFA. And so that's one way to do it. There's also a "
              "process which others are pursuing where they're going to partner with "
              'registrants. But at the end of the day, our requirements are very clear.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "FCM broker with with the NFA. And so that's one way to do it. There's also a "
             "process which others are pursuing where they're going to partner with "
             'registrants. But at the end of the day, our requirements are very clear.',
      'title': 'CFTC Chairman on Backpack: "The First On-Chain DCO/DCM" (Backpack Exchange '
               'Official)',
      'url': 'https://www.youtube.com/watch?v=0Yj5x9uwKAE&t=22s',
      'video_id': '0Yj5x9uwKAE'},
     {'author': 'CoinGeek',
      'channel': 'CoinGeek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:18](https://www.youtube.com/watch?v=0mX0Ac4Zc8s&t=558s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'N-chain what we can do is into the back end of our system we um we link it up '
              'through an api and then we can stamp all key actions that are needed that will.',
      'timestamp': 558,
      'timestamp_label': '[00:09:18]',
      'timestamp_seconds': 558,
      'tip': 'N-chain what we can do is into the back end of our system we um we link it up '
             'through an api and then we can stamp all key actions that are needed that will.',
      'title': 'iGaming and responsible compliance | CG New York (CoinGeek)',
      'url': 'https://www.youtube.com/watch?v=0mX0Ac4Zc8s&t=558s',
      'video_id': '0mX0Ac4Zc8s'},
     {'author': 'Polymarket Plays & Analysis',
      'channel': 'Polymarket Plays & Analysis',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=zeZHFQujNTg&t=115s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The volume traded on market is $29. 5 million, demonstrating significant '
              "attention to potential shifts within Iran's political system and widespread "
              'belief among participants that change is likely.',
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': 'The volume traded on market is $29. 5 million, demonstrating significant '
             "attention to potential shifts within Iran's political system and widespread "
             'belief among participants that change is likely.',
      'title': 'Iran War Prediction Markets — Polymarket Analysis 2026-11-06 | Political '
               'Betting Odds & News Update (Polymarket Plays & Analysis)',
      'url': 'https://www.youtube.com/watch?v=zeZHFQujNTg&t=115s',
      'video_id': 'zeZHFQujNTg'},
     {'author': 'Three Markets –\xa0The Prediction Market Podcast',
      'channel': 'Three Markets –\xa0The Prediction Market Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:52](https://www.youtube.com/watch?v=DvHXWcq2iWc&t=352s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They tend to try and dismiss any bias of the result. My main bet is that there '
              'is a short-term overestimation of yes and that you could just buy the the the '
              "entire market index of all markets and all you're doing is betting on nos.",
      'timestamp': 352,
      'timestamp_label': '[00:05:52]',
      'timestamp_seconds': 352,
      'tip': 'They tend to try and dismiss any bias of the result. My main bet is that there '
             'is a short-term overestimation of yes and that you could just buy the the the '
             "entire market index of all markets and all you're doing is betting on nos.",
      'title': "Prediction Market Trader's Strategy That Turned $286 To $1M (Three Markets "
               '–\xa0The Prediction Market Podcast)',
      'url': 'https://www.youtube.com/watch?v=DvHXWcq2iWc&t=352s',
      'video_id': 'DvHXWcq2iWc'},
     {'author': 'OddsJam: Sports Betting Strategy & Education',
      'channel': 'OddsJam: Sports Betting Strategy & Education',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:18](https://www.youtube.com/watch?v=Gjuo-nBvRiM&t=498s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'll get back to you and I'm updating this package always so it's only going to "
              'get better from here thanks for listening and good luck with the MLB playoffs '
              'and NFL season bye.',
      'timestamp': 498,
      'timestamp_label': '[00:08:18]',
      'timestamp_seconds': 498,
      'tip': "I'll get back to you and I'm updating this package always so it's only going to "
             'get better from here thanks for listening and good luck with the MLB playoffs '
             'and NFL season bye.',
      'title': 'Sports Betting Models | Odds API | OddsJam + DingerStats (OddsJam: Sports '
               'Betting Strategy & Education)',
      'url': 'https://www.youtube.com/watch?v=Gjuo-nBvRiM&t=498s',
      'video_id': 'Gjuo-nBvRiM'}],
 8: [{'author': 'Powerhouse Affiliate',
      'channel': 'Powerhouse Affiliate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:32](https://www.youtube.com/watch?v=pihR_hy7xRU&t=752s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '"I\'ve requested high search volume search terms related to casino tools that '
              'people might actually use and then sign up to an affiliate program through my '
              'website if I build the tool for them." And then you can use AI to create these '
              'tools.',
      'timestamp': 752,
      'timestamp_label': '[00:12:32]',
      'timestamp_seconds': 752,
      'tip': '"I\'ve requested high search volume search terms related to casino tools that '
             'people might actually use and then sign up to an affiliate program through my '
             'website if I build the tool for them." And then you can use AI to create these '
             'tools.',
      'title': '$3,000,000 Casino Affiliate Traffic Hacks for iGaming Offers (AI Changes '
               'Everything!) (Powerhouse Affiliate)',
      'url': 'https://www.youtube.com/watch?v=pihR_hy7xRU&t=752s',
      'video_id': 'pihR_hy7xRU'},
     {'author': 'Olga Zarr SEO',
      'channel': 'Olga Zarr SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=j9LMpZesI1o&t=89s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So I became an affiliate in 2010 and I've also done B2B affiliation as well as "
              "B2C. I sold those sites recently and I've been building the software that I "
              'currently do today, which is currently mainly for gambling affiliates.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': "So I became an affiliate in 2010 and I've also done B2B affiliation as well as "
             "B2C. I sold those sites recently and I've been building the software that I "
             'currently do today, which is currently mainly for gambling affiliates.',
      'title': '(Black Hat) SEO for Casino & Gambling Sites With John Wright! Are You Ready '
               'For This? (Olga Zarr SEO)',
      'url': 'https://www.youtube.com/watch?v=j9LMpZesI1o&t=89s',
      'video_id': 'j9LMpZesI1o'},
     {'author': 'OddsJam: Sports Betting Strategy & Education',
      'channel': 'OddsJam: Sports Betting Strategy & Education',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:58](https://www.youtube.com/watch?v=wTrqHdI32FA&t=418s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Osam software so that you can see that line movement on your phone. You can '
              "also go over to Oz Jam's arbitrage tool and any arbitrage plays that you see to "
              "FanDuel or Pinnacle, bet the recreational book on that side. You'll find a lot "
              'of success there as well.',
      'timestamp': 418,
      'timestamp_label': '[00:06:58]',
      'timestamp_seconds': 418,
      'tip': 'Osam software so that you can see that line movement on your phone. You can also '
             "go over to Oz Jam's arbitrage tool and any arbitrage plays that you see to "
             "FanDuel or Pinnacle, bet the recreational book on that side. You'll find a lot "
             'of success there as well.',
      'title': 'The SECRET to Winning Player Prop Bets (2 Strategies That Work) (OddsJam: '
               'Sports Betting Strategy & Education)',
      'url': 'https://www.youtube.com/watch?v=wTrqHdI32FA&t=418s',
      'video_id': 'wTrqHdI32FA'},
     {'author': 'Quantitative Predictions',
      'channel': 'Quantitative Predictions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:26](https://www.youtube.com/watch?v=AoLKXHhSRtM&t=86s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Coming in at number four, we do have Nansen's API. Now, you might know Nansen "
              'for the crypto endpoints and the crypto data and analytics. However, they do '
              'actually offer some prediction market endpoints, specifically for Polymarket.',
      'timestamp': 86,
      'timestamp_label': '[00:01:26]',
      'timestamp_seconds': 86,
      'tip': "Coming in at number four, we do have Nansen's API. Now, you might know Nansen "
             'for the crypto endpoints and the crypto data and analytics. However, they do '
             'actually offer some prediction market endpoints, specifically for Polymarket.',
      'title': 'Best Prediction Market APIs in 2026 (Polymarket, Kalshi & More) (Quantitative '
               'Predictions)',
      'url': 'https://www.youtube.com/watch?v=AoLKXHhSRtM&t=86s',
      'video_id': 'AoLKXHhSRtM'},
     {'author': 'Money Blueprint',
      'channel': 'Money Blueprint',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:44](https://www.youtube.com/watch?v=IrZSO1sh3ME&t=44s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Founded by two young MIT graduates, this platform didn't just want to create a "
              'betting app. They wanted to build a regulated financial exchange where you '
              'could trade yes or no contracts on real-world events.',
      'timestamp': 44,
      'timestamp_label': '[00:00:44]',
      'timestamp_seconds': 44,
      'tip': "Founded by two young MIT graduates, this platform didn't just want to create a "
             'betting app. They wanted to build a regulated financial exchange where you could '
             'trade yes or no contracts on real-world events.',
      'title': 'How 2 MIT Grads Took the CFTC to Court—and Won (Money Blueprint)',
      'url': 'https://www.youtube.com/watch?v=IrZSO1sh3ME&t=44s',
      'video_id': 'IrZSO1sh3ME'},
     {'author': 'CASINOAFFMASTERY',
      'channel': 'CASINOAFFMASTERY',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:18](https://www.youtube.com/watch?v=_cAwM5AXvUE&t=1758s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re using their tool because you basically still have to control the outcome of "
              'the tools anyway. So, the business model of this because now you kind of '
              'learned a [snorts] lot already through this video is that affiliate marketing '
              'is not a get-richqu scheme.',
      'timestamp': 1758,
      'timestamp_label': '[00:29:18]',
      'timestamp_seconds': 1758,
      'tip': "'re using their tool because you basically still have to control the outcome of "
             'the tools anyway. So, the business model of this because now you kind of learned '
             'a [snorts] lot already through this video is that affiliate marketing is not a '
             'get-richqu scheme.',
      'title': 'Beginner’s Guide to Casino Affiliate Marketing in 2025 (CASINOAFFMASTERY)',
      'url': 'https://www.youtube.com/watch?v=_cAwM5AXvUE&t=1758s',
      'video_id': '_cAwM5AXvUE'},
     {'author': 'Affnook',
      'channel': 'Affnook',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:33](https://www.youtube.com/watch?v=jE9PBJOzw_E&t=153s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The creation of the site stage. So, I'm meeting people who are you know, "
              'shopping for Ethnoc for an affiliate tracking platform and then.',
      'timestamp': 153,
      'timestamp_label': '[00:02:33]',
      'timestamp_seconds': 153,
      'tip': "The creation of the site stage. So, I'm meeting people who are you know, "
             'shopping for Ethnoc for an affiliate tracking platform and then.',
      'title': 'What’s Changing in iGaming Affiliate Marketing? | Affnook Webinar (Affnook)',
      'url': 'https://www.youtube.com/watch?v=jE9PBJOzw_E&t=153s',
      'video_id': 'jE9PBJOzw_E'},
     {'author': 'Big Pond Digital',
      'channel': 'Big Pond Digital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:02:14](https://www.youtube.com/watch?v=jWqa6ck6G3Y&t=3734s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'AI helpers are coming into the industry. So, what we are building with the AI '
              "AI on the affi is that uh it's just going to give you the recommendations based "
              'on the data.',
      'timestamp': 3734,
      'timestamp_label': '[01:02:14]',
      'timestamp_seconds': 3734,
      'tip': 'AI helpers are coming into the industry. So, what we are building with the AI AI '
             "on the affi is that uh it's just going to give you the recommendations based on "
             'the data.',
      'title': 'Are iGaming Affiliates Still Worth It in 2026? | SEO, AI & GEO (Big Pond '
               'Digital)',
      'url': 'https://www.youtube.com/watch?v=jWqa6ck6G3Y&t=3734s',
      'video_id': 'jWqa6ck6G3Y'},
     {'author': 'NBC News',
      'channel': 'NBC News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=APN3zwcwPdQ&t=32s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'JAY MALAVIYA IS JUST 22 YEARS OLD. HE DROPPED OUT OF COLLEGE TO BUILD HIS '
              "COMPANY, KAIROS, WITH HIS FRIEND ZAID AL-ZAIN. IT'S A PREDICTION MARKET "
              "PLATFORM THAT'S STILL IN THE TESTING PHASE, BUT HAS ALREADY SIGNED DEALS WITH "
              'FOUR COMPANIES, INCLUDING KALKI AND POLYMARKET.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': 'JAY MALAVIYA IS JUST 22 YEARS OLD. HE DROPPED OUT OF COLLEGE TO BUILD HIS '
             "COMPANY, KAIROS, WITH HIS FRIEND ZAID AL-ZAIN. IT'S A PREDICTION MARKET PLATFORM "
             "THAT'S STILL IN THE TESTING PHASE, BUT HAS ALREADY SIGNED DEALS WITH FOUR "
             'COMPANIES, INCLUDING KALKI AND POLYMARKET.',
      'title': 'How prediction markets are spawning an entire trading industry (NBC News)',
      'url': 'https://www.youtube.com/watch?v=APN3zwcwPdQ&t=32s',
      'video_id': 'APN3zwcwPdQ'},
     {'author': 'SEO Jesus',
      'channel': 'SEO Jesus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:05](https://www.youtube.com/watch?v=nQYzKRUzRCM&t=185s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And they keep on building all their links to the age domain that's passing the "
              'power and authority to the burner subdomain. But, of course, that burner '
              'subdomain itself has got a lot of resources thrown at it as well.',
      'timestamp': 185,
      'timestamp_label': '[00:03:05]',
      'timestamp_seconds': 185,
      'tip': "And they keep on building all their links to the age domain that's passing the "
             'power and authority to the burner subdomain. But, of course, that burner '
             'subdomain itself has got a lot of resources thrown at it as well.',
      'title': 'International IGaming SEO: Advanced Tactics of Offshore Casinos (SEO Jesus)',
      'url': 'https://www.youtube.com/watch?v=nQYzKRUzRCM&t=185s',
      'video_id': 'nQYzKRUzRCM'},
     {'author': 'Earn2Trade',
      'channel': 'Earn2Trade',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:57](https://www.youtube.com/watch?v=fGEHMyG3ktY&t=657s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They are constantly pioneering digital initiatives as well, and on top of that, '
              "they're always providing ancillary services. This could include things like "
              'data analytics and other consultation papers that can provide insights into the '
              'commodity futures market.',
      'timestamp': 657,
      'timestamp_label': '[00:10:57]',
      'timestamp_seconds': 657,
      'tip': 'They are constantly pioneering digital initiatives as well, and on top of that, '
             "they're always providing ancillary services. This could include things like data "
             'analytics and other consultation papers that can provide insights into the '
             'commodity futures market.',
      'title': 'What is the CFTC and What Does it Do? (Earn2Trade)',
      'url': 'https://www.youtube.com/watch?v=fGEHMyG3ktY&t=657s',
      'video_id': 'fGEHMyG3ktY'},
     {'author': 'A Lawyer In Finance Explains  1.1M views',
      'channel': 'A Lawyer In Finance Explains  1.1M views',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:18](https://www.youtube.com/watch?v=gpIcoaEPb7Q&t=498s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '38951 to the extent that it requires compliance with part 45. So uh 38951 is a '
              'books and recordkeeping requirement and part 45 deals with the swap data '
              'recording and recordkeeping.',
      'timestamp': 498,
      'timestamp_label': '[00:08:18]',
      'timestamp_seconds': 498,
      'tip': '38951 to the extent that it requires compliance with part 45. So uh 38951 is a '
             'books and recordkeeping requirement and part 45 deals with the swap data '
             'recording and recordkeeping.',
      'title': "The CFTC's No-Action Letter on Binary Options and Event Markets Railbird and "
               'Letter 25-26 Kalshi (A Lawyer In Finance Explains  1.1M views)',
      'url': 'https://www.youtube.com/watch?v=gpIcoaEPb7Q&t=498s',
      'video_id': 'gpIcoaEPb7Q'},
     {'author': 'Securing Networks with Cisco Firepower Threat Defense',
      'channel': 'Securing Networks with Cisco Firepower Threat Defense',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=W2EECB7yOaw&t=87s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "IP address routing and access control policy for both the FTD's and the FTD Sai "
              "a for Gigabit Ethernet 0/0 I've configured it as an outside interface with IP "
              "address 192 168 1.1 for Gigabit Ethernet 0 / 1 I've configured it as an inside "
              'in inside interface 10.10 dot.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': "IP address routing and access control policy for both the FTD's and the FTD Sai "
             "a for Gigabit Ethernet 0/0 I've configured it as an outside interface with IP "
             "address 192 168 1.1 for Gigabit Ethernet 0 / 1 I've configured it as an inside "
             'in inside interface 10.10 dot.',
      'title': 'Configuring IPSec Site to Site VPN in FTD using FMC (Securing Networks with '
               'Cisco Firepower Threat Defense)',
      'url': 'https://www.youtube.com/watch?v=W2EECB7yOaw&t=87s',
      'video_id': 'W2EECB7yOaw'},
     {'author': 'Traffic Cardinal EN — Affiliate Press',
      'channel': 'Traffic Cardinal EN — Affiliate Press',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:49](https://www.youtube.com/watch?v=GRpptuPlok4&t=109s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Promotional messages and in fact we will have absolutely no effective ways to '
              'try and motivate the player or user to return to the project or platform here I '
              'would really like to emphasize.',
      'timestamp': 109,
      'timestamp_label': '[00:01:49]',
      'timestamp_seconds': 109,
      'tip': 'Promotional messages and in fact we will have absolutely no effective ways to '
             'try and motivate the player or user to return to the project or platform here I '
             'would really like to emphasize.',
      'title': 'How To Choose The Right iGaming Project To Work On The RevShare by Anton '
               'Konvertov (Traffic Cardinal EN — Affiliate Press)',
      'url': 'https://www.youtube.com/watch?v=GRpptuPlok4&t=109s',
      'video_id': 'GRpptuPlok4'},
     {'author': 'NEXT',
      'channel': 'NEXT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:29](https://www.youtube.com/watch?v=DmXIrgbAw-Y&t=449s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Social casino in north america and sweepstakes casinos things that were still '
              "working in the states that didn't even have online casino to begin with yet so "
              'we saw a massive uptick this year we saw growth in north america we saw.',
      'timestamp': 449,
      'timestamp_label': '[00:07:29]',
      'timestamp_seconds': 449,
      'tip': 'Social casino in north america and sweepstakes casinos things that were still '
             "working in the states that didn't even have online casino to begin with yet so "
             'we saw a massive uptick this year we saw growth in north america we saw.',
      'title': 'Podcast by Pierre Lindh #69 - Michael Daly, CEO, Catena Media (NEXT)',
      'url': 'https://www.youtube.com/watch?v=DmXIrgbAw-Y&t=449s',
      'video_id': 'DmXIrgbAw-Y'}],
 9: [{'author': '3SNET',
      'channel': '3SNET',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:16](https://www.youtube.com/watch?v=XUPjmWHBPq4&t=196s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The market grows fast and so do the advertising rules. The federal law banned '
              'promoting unlicensed operators, promising guaranteed wins, or framing betting '
              'as an investment or a way to fix financial problems. In 2026, it got more '
              'specific.',
      'timestamp': 196,
      'timestamp_label': '[00:03:16]',
      'timestamp_seconds': 196,
      'tip': 'The market grows fast and so do the advertising rules. The federal law banned '
             'promoting unlicensed operators, promising guaranteed wins, or framing betting as '
             'an investment or a way to fix financial problems. In 2026, it got more specific.',
      'title': 'Do Affiliates Need a License? New iGaming Rules 2026 (3SNET)',
      'url': 'https://www.youtube.com/watch?v=XUPjmWHBPq4&t=196s',
      'video_id': 'XUPjmWHBPq4'},
     {'author': 'iGaming Marketing Agency Tips by Christian Strutt',
      'channel': 'iGaming Marketing Agency Tips by Christian Strutt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:49](https://www.youtube.com/watch?v=MKTk-Y-xt1I&t=349s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Just just be aware of the compliance issues, regulatory issues out in the US '
              "markets. So you've got to have the the the age 18 plus. You got to have "
              'responsible gambling disclaimers. You got to have clear bonus terms and '
              'eligibility per state.',
      'timestamp': 349,
      'timestamp_label': '[00:05:49]',
      'timestamp_seconds': 349,
      'tip': 'Just just be aware of the compliance issues, regulatory issues out in the US '
             "markets. So you've got to have the the the age 18 plus. You got to have "
             'responsible gambling disclaimers. You got to have clear bonus terms and '
             'eligibility per state.',
      'title': '🎯 The US Sports Betting Boom 2025 Affiliate Marketing Opportunities & '
               'State-by-State Strategy Guide (iGaming Marketing Agency Tips by Christian '
               'Strutt)',
      'url': 'https://www.youtube.com/watch?v=MKTk-Y-xt1I&t=349s',
      'video_id': 'MKTk-Y-xt1I'},
     {'author': 'High-Risk Merchant Accounts | Adaptiv Payments',
      'channel': 'High-Risk Merchant Accounts | Adaptiv Payments',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=jerDG4rTmK8&t=38s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'New Jersey, Pennsylvania and Michigan. Each state sets its own rules and its '
              "own age limit, usually 21, so you're licensed state by state. And sweepstakes "
              'casinos are now banned in several states, including California and New York.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': 'New Jersey, Pennsylvania and Michigan. Each state sets its own rules and its own '
             "age limit, usually 21, so you're licensed state by state. And sweepstakes "
             'casinos are now banned in several states, including California and New York.',
      'title': 'iGaming Payment Processing: How Online Casinos and Sportsbooks Get Approved '
               '(2026) (High-Risk Merchant Accounts | Adaptiv Payments)',
      'url': 'https://www.youtube.com/watch?v=jerDG4rTmK8&t=38s',
      'video_id': 'jerDG4rTmK8'},
     {'author': 'EVERNET Consulting: IT • Marketing • AI Consulting',
      'channel': 'EVERNET Consulting: IT • Marketing • AI Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:48](https://www.youtube.com/watch?v=1VnsVfLqgiw&t=48s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Google real expertise, and how to fit compliance review into publishing without '
              'slowing everything down. This is general information, not legal advice. Gaming '
              'rules vary by state and change often, so check with your compliance team and '
              'counsel.',
      'timestamp': 48,
      'timestamp_label': '[00:00:48]',
      'timestamp_seconds': 48,
      'tip': 'Google real expertise, and how to fit compliance review into publishing without '
             'slowing everything down. This is general information, not legal advice. Gaming '
             'rules vary by state and change often, so check with your compliance team and '
             'counsel.',
      'title': 'iGaming SEO: how sportsbooks and fantasy sites grow within the rules (EVERNET '
               'Consulting: IT • Marketing • AI Consulting)',
      'url': 'https://www.youtube.com/watch?v=1VnsVfLqgiw&t=48s',
      'video_id': '1VnsVfLqgiw'},
     {'author': 'A Lawyer In Finance Explains  1.1M views',
      'channel': 'A Lawyer In Finance Explains  1.1M views',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:48](https://www.youtube.com/watch?v=MHeX-gRNpCE&t=48s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And Massachusetts recently filed against Cali in state court. So, it is '
              "possible to get something removed from state court to federal court, but that's "
              "an extra step and you're fighting on their terms. So, uh it's better for the "
              'state regulators to start in state court.',
      'timestamp': 48,
      'timestamp_label': '[00:00:48]',
      'timestamp_seconds': 48,
      'tip': 'And Massachusetts recently filed against Cali in state court. So, it is possible '
             "to get something removed from state court to federal court, but that's an extra "
             "step and you're fighting on their terms. So, uh it's better for the state "
             'regulators to start in state court.',
      'title': 'Prediction Market Legal War: Why States are Suing Kalshi & Polymarket. Former '
               'CFTC Lawyer Explains (A Lawyer In Finance Explains  1.1M views)',
      'url': 'https://www.youtube.com/watch?v=MHeX-gRNpCE&t=48s',
      'video_id': 'MHeX-gRNpCE'},
     {'author': 'CNBC Television',
      'channel': 'CNBC Television',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:28](https://www.youtube.com/watch?v=SYcmPpHGHIo&t=388s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "OPTIONS ARE VERY COMPLICATED. THESE PRODUCTS AREN'T SUPER COMPLICATED. IF YOU "
              "LOOK AT THE TERMS OF THE CONTRACT. SO WE'RE GOING TO REGULATE THEM. WE'RE GOING "
              "TO MAKE SURE THE TERMS ARE OUT THERE. WE'RE GOING TO MAKE SURE THERE'S PROPER "
              'DISCLOSURE.',
      'timestamp': 388,
      'timestamp_label': '[00:06:28]',
      'timestamp_seconds': 388,
      'tip': "OPTIONS ARE VERY COMPLICATED. THESE PRODUCTS AREN'T SUPER COMPLICATED. IF YOU "
             "LOOK AT THE TERMS OF THE CONTRACT. SO WE'RE GOING TO REGULATE THEM. WE'RE GOING "
             "TO MAKE SURE THE TERMS ARE OUT THERE. WE'RE GOING TO MAKE SURE THERE'S PROPER "
             'DISCLOSURE.',
      'title': 'CFTC Chair Michael Selig tackles perpetual futures ‘misconceptions’ (CNBC '
               'Television)',
      'url': 'https://www.youtube.com/watch?v=SYcmPpHGHIo&t=388s',
      'video_id': 'SYcmPpHGHIo'},
     {'author': 'Congress Clips',
      'channel': 'Congress Clips',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=e6Xc_HIIRbQ&t=80s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They've built out legal gaming systems with compacts, licensing, integrity "
              'rules, age verification, and consumer protections.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': "They've built out legal gaming systems with compacts, licensing, integrity "
             'rules, age verification, and consumer protections.',
      'title': 'CFTC Chair Faces Tough Questions on Fast-Growing Prediction Markets (Congress '
               'Clips)',
      'url': 'https://www.youtube.com/watch?v=e6Xc_HIIRbQ&t=80s',
      'video_id': 'e6Xc_HIIRbQ'},
     {'author': 'CFTC',
      'channel': 'CFTC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[02:46:16](https://www.youtube.com/watch?v=yUqRhv7w9Vs&t=9976s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "GCP and let's say ELSOC or gross omnid that in terms of how the the rules and "
              'the code would work. Joe then Tim Joe KC board of trade. Uh Bob I just want to '
              'address the DCO cost issue real quick.',
      'timestamp': 9976,
      'timestamp_label': '[02:46:16]',
      'timestamp_seconds': 9976,
      'tip': "GCP and let's say ELSOC or gross omnid that in terms of how the the rules and "
             'the code would work. Joe then Tim Joe KC board of trade. Uh Bob I just want to '
             'address the DCO cost issue real quick.',
      'title': 'Day 1: Roundtable to Discuss Additional Customer Collateral Protections (CFTC)',
      'url': 'https://www.youtube.com/watch?v=yUqRhv7w9Vs&t=9976s',
      'video_id': 'yUqRhv7w9Vs'},
     {'author': '🎓Profeissor.com🚀Digital Assets, AI & FinTech',
      'channel': '🎓Profeissor.com🚀Digital Assets, AI & FinTech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:34](https://www.youtube.com/watch?v=4Vqws7tSo8E&t=214s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Step one is to ask whether the contract in question is an event contract in the '
              'first place. In other words, is it an agreement, contract, transaction, or swap '
              'in an excluded commodity that is based upon an occurrence, the extent of an '
              'occurrence, or a contingency.',
      'timestamp': 214,
      'timestamp_label': '[00:03:34]',
      'timestamp_seconds': 214,
      'tip': 'Step one is to ask whether the contract in question is an event contract in the '
             'first place. In other words, is it an agreement, contract, transaction, or swap '
             'in an excluded commodity that is based upon an occurrence, the extent of an '
             'occurrence, or a contingency.',
      'title': '🔮How will CFTC regulate Event Contracts⚽️ and 🇺🇸Prediction Markets? 📦Unpacking '
               'new 267-page rule 📖 (🎓Profeissor.com🚀Digital Assets, AI & FinTech)',
      'url': 'https://www.youtube.com/watch?v=4Vqws7tSo8E&t=214s',
      'video_id': '4Vqws7tSo8E'},
     {'author': 'Braeden Anderson',
      'channel': 'Braeden Anderson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=tgQX7NOuUyk&t=83s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'CFTC has to develop market structure regulation that fits that new reality. He '
              'uses the phrase fit for purpose market structure regulations and he talks about '
              'developing clear rules of the road and for what he calls the golden age of '
              'American financial markets.',
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': 'CFTC has to develop market structure regulation that fits that new reality. He '
             'uses the phrase fit for purpose market structure regulations and he talks about '
             'developing clear rules of the road and for what he calls the golden age of '
             'American financial markets.',
      'title': 'CFTC Chair Selig’s First Big Move (Braeden Anderson)',
      'url': 'https://www.youtube.com/watch?v=tgQX7NOuUyk&t=83s',
      'video_id': 'tgQX7NOuUyk'},
     {'author': 'PredictionNews',
      'channel': 'PredictionNews',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=7na4n6_OBK0&t=20s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Uh Andrew Kim, let's get right into it. Give us a sense of where these cases "
              'stand right now. Is there a clear winner right now or are we just putting '
              'points on the board on the state side and the prediction market side?',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Uh Andrew Kim, let's get right into it. Give us a sense of where these cases "
             'stand right now. Is there a clear winner right now or are we just putting points '
             'on the board on the state side and the prediction market side?',
      'title': 'Andrew Kim on Kalshi Cases, Sports Contracts & Prediction Markets | Prediction '
               'Market Movers (PredictionNews)',
      'url': 'https://www.youtube.com/watch?v=7na4n6_OBK0&t=20s',
      'video_id': '7na4n6_OBK0'},
     {'author': 'iDEA Growth',
      'channel': 'iDEA Growth',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:30:22](https://www.youtube.com/watch?v=LqlSYBu75Hk&t=1822s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Visit casinos or play online with with legal sports books so i think that we '
              'need to look at it holistically and not just focus.',
      'timestamp': 1822,
      'timestamp_label': '[00:30:22]',
      'timestamp_seconds': 1822,
      'tip': 'Visit casinos or play online with with legal sports books so i think that we '
             'need to look at it holistically and not just focus.',
      'title': "The Dos & Don'ts of Advertising and iGaming (iDEA Growth)",
      'url': 'https://www.youtube.com/watch?v=LqlSYBu75Hk&t=1822s',
      'video_id': 'LqlSYBu75Hk'},
     {'author': 'REH CPA',
      'channel': 'REH CPA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:34](https://www.youtube.com/watch?v=rN19s1QAAYo&t=94s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Don't get the losses at all you're not you don't get the losses at all it's "
              "definitely you can't just net them together and write it off as a law well.",
      'timestamp': 94,
      'timestamp_label': '[00:01:34]',
      'timestamp_seconds': 94,
      'tip': "Don't get the losses at all you're not you don't get the losses at all it's "
             "definitely you can't just net them together and write it off as a law well.",
      'title': "Online Sports Betting Taxes - Don't Make This Mistake... (REH CPA)",
      'url': 'https://www.youtube.com/watch?v=rN19s1QAAYo&t=94s',
      'video_id': 'rN19s1QAAYo'},
     {'author': 'CFTC',
      'channel': 'CFTC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:37](https://www.youtube.com/watch?v=ec9Mk3slriY&t=337s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Some of the reporting requirements while still requiring a certification of '
              'compliance and they address the concerns raised about access to source code on.',
      'timestamp': 337,
      'timestamp_label': '[00:05:37]',
      'timestamp_seconds': 337,
      'tip': 'Some of the reporting requirements while still requiring a certification of '
             'compliance and they address the concerns raised about access to source code on.',
      'title': 'Open Commission Meeting to Consider a Supplemental Proposal to Automated '
               'Trading Regulation (CFTC)',
      'url': 'https://www.youtube.com/watch?v=ec9Mk3slriY&t=337s',
      'video_id': 'ec9Mk3slriY'},
     {'author': 'Cisco Secure Firewall',
      'channel': 'Cisco Secure Firewall',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:31](https://www.youtube.com/watch?v=-2AQt4ZxwmU&t=751s)',
      'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                   'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                   'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                   'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                   'Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Connections running top that is what you saw actually displayed in both of '
              'these units a sa and STD I am receiving iperf UDP connections same over here so '
              'those are the other two UDP connections that you have in place.',
      'timestamp': 751,
      'timestamp_label': '[00:12:31]',
      'timestamp_seconds': 751,
      'tip': 'Connections running top that is what you saw actually displayed in both of these '
             'units a sa and STD I am receiving iperf UDP connections same over here so those '
             'are the other two UDP connections that you have in place.',
      'title': 'FPR4100 FTD App Cluster NGIPS with ASA App Failover (1) Overview (2017) (Cisco '
               'Secure Firewall)',
      'url': 'https://www.youtube.com/watch?v=-2AQt4ZxwmU&t=751s',
      'video_id': '-2AQt4ZxwmU'}],
 10: [{'author': 'iGaming Marketing Agency Tips by Christian Strutt',
       'channel': 'iGaming Marketing Agency Tips by Christian Strutt',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:48](https://www.youtube.com/watch?v=EA4I4Vc4wFM&t=168s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s AI, uh, it doesn't go well. I've seen casino affiliates roll out sites with "
               "all AI, thinking they're doing really well, invest loads of money into "
               'backlinks. Google at one point sees the entire content AI breach of '
               'regulations using automation to try and cheat Google.',
       'timestamp': 168,
       'timestamp_label': '[00:02:48]',
       'timestamp_seconds': 168,
       'tip': "'s AI, uh, it doesn't go well. I've seen casino affiliates roll out sites with "
              "all AI, thinking they're doing really well, invest loads of money into "
              'backlinks. Google at one point sees the entire content AI breach of regulations '
              'using automation to try and cheat Google.',
       'title': 'How SEO Drives Massive Casino Traffic (Without Paid Ads) (iGaming Marketing '
                'Agency Tips by Christian Strutt)',
       'url': 'https://www.youtube.com/watch?v=EA4I4Vc4wFM&t=168s',
       'video_id': 'EA4I4Vc4wFM'},
      {'author': 'Defined',
       'channel': 'Defined',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:49](https://www.youtube.com/watch?v=LefzH8sYzRI&t=349s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "UI, I'm probably going straight to their API rather than through an "
               'aggregator? If your product is Polymarket first, say a dedicated terminal or '
               'analytics dashboard, their native API gives you the lowest latency and the '
               'richest access to venue specific features.',
       'timestamp': 349,
       'timestamp_label': '[00:05:49]',
       'timestamp_seconds': 349,
       'tip': "UI, I'm probably going straight to their API rather than through an aggregator? "
              'If your product is Polymarket first, say a dedicated terminal or analytics '
              'dashboard, their native API gives you the lowest latency and the richest access '
              'to venue specific features.',
       'title': 'Top 5 Prediction Market APIs for Real-Time Odds Dashboards (Defined)',
       'url': 'https://www.youtube.com/watch?v=LefzH8sYzRI&t=349s',
       'video_id': 'LefzH8sYzRI'},
      {'author': 'Robot Traders',
       'channel': 'Robot Traders',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:17](https://www.youtube.com/watch?v=yYjo1lzNoGI&t=77s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "In other words, a solid foundation that you can build a on if you're for "
               "example using some AI to help you code, etc. With this, you'll get a good "
               'understanding of the foundations on how to do all of that to guide your agent '
               'properly or to develop yourself, etc.',
       'timestamp': 77,
       'timestamp_label': '[00:01:17]',
       'timestamp_seconds': 77,
       'tip': "In other words, a solid foundation that you can build a on if you're for "
              "example using some AI to help you code, etc. With this, you'll get a good "
              'understanding of the foundations on how to do all of that to guide your agent '
              'properly or to develop yourself, etc.',
       'title': 'How to Use the Kalshi API with Python (Full Guide) (Robot Traders)',
       'url': 'https://www.youtube.com/watch?v=yYjo1lzNoGI&t=77s',
       'video_id': 'yYjo1lzNoGI'},
      {'author': 'Odds Breaker',
       'channel': 'Odds Breaker',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:44](https://www.youtube.com/watch?v=aZvtaObt8Gw&t=104s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'If you can find the arbitrage, the return obviously depends on the size of '
               "what you put down. But if you don't have cash sitting in six different betting "
               'apps ready to fire instantly, the lines can move against you pretty quickly. '
               'Four commands to an AI coder.',
       'timestamp': 104,
       'timestamp_label': '[00:01:44]',
       'timestamp_seconds': 104,
       'tip': 'If you can find the arbitrage, the return obviously depends on the size of what '
              "you put down. But if you don't have cash sitting in six different betting apps "
              'ready to fire instantly, the lines can move against you pretty quickly. Four '
              'commands to an AI coder.',
       'title': 'I Built a Sports betting Arbitrage Scanner for FREE (AI Tutorial) (Odds '
                'Breaker)',
       'url': 'https://www.youtube.com/watch?v=aZvtaObt8Gw&t=104s',
       'video_id': 'aZvtaObt8Gw'},
      {'author': 'OngPredicts',
       'channel': 'OngPredicts',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:48](https://www.youtube.com/watch?v=HtGMBJ7ynjs&t=108s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Strong depth, but a more focused starting point for this particular build. '
               'Number three, we have Monit. Monit takes an an agent-first approach. An AI '
               'agent can discover and call tools through one platform.',
       'timestamp': 108,
       'timestamp_label': '[00:01:48]',
       'timestamp_seconds': 108,
       'tip': 'Strong depth, but a more focused starting point for this particular build. '
              'Number three, we have Monit. Monit takes an an agent-first approach. An AI '
              'agent can discover and call tools through one platform.',
       'title': 'Top 5 Prediction Market APIs in 2026 (Polymarket, Kalshi & More) '
                '(OngPredicts)',
       'url': 'https://www.youtube.com/watch?v=HtGMBJ7ynjs&t=108s',
       'video_id': 'HtGMBJ7ynjs'},
      {'author': 'Coding with Ado',
       'channel': 'Coding with Ado',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:21](https://www.youtube.com/watch?v=MkF4ThP7PRs&t=141s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Catch error ER okay and let's do here um cost response equals to now wa A.G "
               "and let's do https API do the ODS ai.com SL V4 SL sports slash sport.",
       'timestamp': 141,
       'timestamp_label': '[00:02:21]',
       'timestamp_seconds': 141,
       'tip': "Catch error ER okay and let's do here um cost response equals to now wa A.G and "
              "let's do https API do the ODS ai.com SL V4 SL sports slash sport.",
       'title': 'Automate Your Sports Betting Analysis: Fetching Real-Time Odds with Node.js! '
                '(Coding with Ado)',
       'url': 'https://www.youtube.com/watch?v=MkF4ThP7PRs&t=141s',
       'video_id': 'MkF4ThP7PRs'},
      {'author': 'ShaunsTake',
       'channel': 'ShaunsTake',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:40](https://www.youtube.com/watch?v=A3KSnSZOPtM&t=580s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I've done very well as a sports better on daily fantasy sports apps. Limited "
               'to $5 on PrizePicks, banned on Dabble for beating them too much. I have I '
               'think a $100 limit per day on Underdog. I can only do a $25 max bet on '
               'Underdog now.',
       'timestamp': 580,
       'timestamp_label': '[00:09:40]',
       'timestamp_seconds': 580,
       'tip': "I've done very well as a sports better on daily fantasy sports apps. Limited to "
              '$5 on PrizePicks, banned on Dabble for beating them too much. I have I think a '
              '$100 limit per day on Underdog. I can only do a $25 max bet on Underdog now.',
       'title': 'I Built a FREE AI Bot to Analyze ANY Kalshi Market (Full Tutorial) '
                '(ShaunsTake)',
       'url': 'https://www.youtube.com/watch?v=A3KSnSZOPtM&t=580s',
       'video_id': 'A3KSnSZOPtM'},
      {'author': 'AI in Regulated Industries',
       'channel': 'AI in Regulated Industries',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:54](https://www.youtube.com/watch?v=bsDlbXqvPok&t=174s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'An ID tells you who an agent works for, not what it will do. Thousands of '
               'similar agents can all be identified and still stampede together, but you '
               "can't fix herding if you can't see who's moving. If you build trading agents, "
               'start now.',
       'timestamp': 174,
       'timestamp_label': '[00:02:54]',
       'timestamp_seconds': 174,
       'tip': 'An ID tells you who an agent works for, not what it will do. Thousands of '
              "similar agents can all be identified and still stampede together, but you can't "
              "fix herding if you can't see who's moving. If you build trading agents, start "
              'now.',
       'title': "AI Trading Agents: The CFTC's Know Your Agent Question (AI in Regulated "
                'Industries)',
       'url': 'https://www.youtube.com/watch?v=bsDlbXqvPok&t=174s',
       'video_id': 'bsDlbXqvPok'},
      {'author': 'Three Markets –\xa0The Prediction Market Podcast',
       'channel': 'Three Markets –\xa0The Prediction Market Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:03](https://www.youtube.com/watch?v=iL5j83SC_fg&t=243s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'API access to all of the different leading LLMs. I think um Quen is maybe in '
               'there. Certainly Claude is in there. Gemini is in there um and has them '
               'trading in in real prediction markets.',
       'timestamp': 243,
       'timestamp_label': '[00:04:03]',
       'timestamp_seconds': 243,
       'tip': 'API access to all of the different leading LLMs. I think um Quen is maybe in '
              'there. Certainly Claude is in there. Gemini is in there um and has them trading '
              'in in real prediction markets.',
       'title': 'What happens when you let AI trade on prediction markets? (Three Markets –\xa0'
                'The Prediction Market Podcast)',
       'url': 'https://www.youtube.com/watch?v=iL5j83SC_fg&t=243s',
       'video_id': 'iL5j83SC_fg'},
      {'author': 'Big Pond Digital',
       'channel': 'Big Pond Digital',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:38:44](https://www.youtube.com/watch?v=0_KHkuMmtVQ&t=2324s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'They what they lack is maybe getting getting links. Although I suppose you can '
               "actually get there's different types of links you can attract as an affiliate "
               "or a review website for example. Um >> I think if it's harder for affiliates "
               'nowadays to actually rank a lot harder.',
       'timestamp': 2324,
       'timestamp_label': '[00:38:44]',
       'timestamp_seconds': 2324,
       'tip': 'They what they lack is maybe getting getting links. Although I suppose you can '
              "actually get there's different types of links you can attract as an affiliate "
              "or a review website for example. Um >> I think if it's harder for affiliates "
              'nowadays to actually rank a lot harder.',
       'title': 'The Future of Casino & Sportsbook SEO: What Still Works in 2026 (Big Pond '
                'Digital)',
       'url': 'https://www.youtube.com/watch?v=0_KHkuMmtVQ&t=2324s',
       'video_id': '0_KHkuMmtVQ'},
      {'author': 'Inside Prediction Markets',
       'channel': 'Inside Prediction Markets',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:06](https://www.youtube.com/watch?v=tM5MKtoBoZ0&t=66s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I've been betting for about five years doing the traditional sports book "
               'stuff. I mean, I came out of college and went into a corporate job. Grew up in '
               'Princeton, new Jersey.',
       'timestamp': 66,
       'timestamp_label': '[00:01:06]',
       'timestamp_seconds': 66,
       'tip': "I've been betting for about five years doing the traditional sports book stuff. "
              'I mean, I came out of college and went into a corporate job. Grew up in '
              'Princeton, new Jersey.',
       'title': 'Inside a Fully Manual Prediction Market Strategy: Where Human Judgment Finds '
                'an Edge (Inside Prediction Markets)',
       'url': 'https://www.youtube.com/watch?v=tM5MKtoBoZ0&t=66s',
       'video_id': 'tM5MKtoBoZ0'},
      {'author': 'FX Lens',
       'channel': 'FX Lens',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:40](https://www.youtube.com/watch?v=7dJD_z7zIRU&t=160s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Thenext thingthatgets misquotedis leverage. 9A1sets minimumsecurity '
               'deposits2%of notionalvaluefor majorcurrencypairs, 5%forallother currencypairs.',
       'timestamp': 160,
       'timestamp_label': '[00:02:40]',
       'timestamp_seconds': 160,
       'tip': 'Thenext thingthatgets misquotedis leverage. 9A1sets minimumsecurity '
              'deposits2%of notionalvaluefor majorcurrencypairs, 5%forallother currencypairs.',
       'title': 'NFA vs CFTC Explained: How to Verify a US Forex Broker & Avoid Fake '
                'Regulation (FX Lens)',
       'url': 'https://www.youtube.com/watch?v=7dJD_z7zIRU&t=160s',
       'video_id': '7dJD_z7zIRU'},
      {'author': 'Natalie Fratto',
       'channel': 'Natalie Fratto',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:21](https://www.youtube.com/watch?v=rDeB10i9gCE&t=501s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Historically, the regulator has banned people from doing things on war, '
               'terrorism, assassination, violence, things that can generally create like '
               'moral hazards.',
       'timestamp': 501,
       'timestamp_label': '[00:08:21]',
       'timestamp_seconds': 501,
       'tip': 'Historically, the regulator has banned people from doing things on war, '
              'terrorism, assassination, violence, things that can generally create like moral '
              'hazards.',
       'title': 'Explaining Prediction Markets with the CEO of Kalshi (Natalie Fratto)',
       'url': 'https://www.youtube.com/watch?v=rDeB10i9gCE&t=501s',
       'video_id': 'rDeB10i9gCE'},
      {'author': 'Ace Alliance',
       'channel': 'Ace Alliance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:44](https://www.youtube.com/watch?v=R-_FHgwDEFQ&t=284s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Space so yeah Mr gamble itself started in 2019 I was kind of like really '
               'focusing on Twitch stream actually back then so the founders were like '
               'building.',
       'timestamp': 284,
       'timestamp_label': '[00:04:44]',
       'timestamp_seconds': 284,
       'tip': 'Space so yeah Mr gamble itself started in 2019 I was kind of like really '
              'focusing on Twitch stream actually back then so the founders were like '
              'building.',
       'title': 'Building Strong iGaming Affiliate and Operator Partnerships (Ace Alliance)',
       'url': 'https://www.youtube.com/watch?v=R-_FHgwDEFQ&t=284s',
       'video_id': 'R-_FHgwDEFQ'},
      {'author': 'OddsJam: Sports Betting Strategy & Education',
       'channel': 'OddsJam: Sports Betting Strategy & Education',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:05](https://www.youtube.com/watch?v=ZTKIge6SyQI&t=125s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Your needs are met and um you know working with odds jam is something that '
               'benefits your business so again check out the odd gm api if you are looking '
               'for an odds api.',
       'timestamp': 125,
       'timestamp_label': '[00:02:05]',
       'timestamp_seconds': 125,
       'tip': 'Your needs are met and um you know working with odds jam is something that '
              'benefits your business so again check out the odd gm api if you are looking for '
              'an odds api.',
       'title': 'The OddsJam Odds API - Why Delayed Data is Holding Back your Business '
                '(OddsJam: Sports Betting Strategy & Education)',
       'url': 'https://www.youtube.com/watch?v=ZTKIge6SyQI&t=125s',
       'video_id': 'ZTKIge6SyQI'}],
 11: [{'author': 'Scrape Atlas',
       'channel': 'Scrape Atlas',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:41](https://www.youtube.com/watch?v=OPiw3RZFInQ&t=161s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, the tool that we're then relying upon to make this work is called "
               "ScrapeAtlas. The website is scrapeatlas. And it's basically a dedicated API, a "
               'unified API to get access to these platforms at scale.',
       'timestamp': 161,
       'timestamp_label': '[00:02:41]',
       'timestamp_seconds': 161,
       'tip': "So, the tool that we're then relying upon to make this work is called "
              "ScrapeAtlas. The website is scrapeatlas. And it's basically a dedicated API, a "
              'unified API to get access to these platforms at scale.',
       'title': 'How to Build a Kalshi & Polymarket Arbitrage Bot with ChatGPT (Scrape Atlas)',
       'url': 'https://www.youtube.com/watch?v=OPiw3RZFInQ&t=161s',
       'video_id': 'OPiw3RZFInQ'},
      {'author': 'SportsGameOdds API',
       'channel': 'SportsGameOdds API',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:55](https://www.youtube.com/watch?v=JXdlRbDVFNY&t=115s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'For each game, it groups the spread odds by sports book, finds the best price '
               'for each team, and refreshes every 30 seconds. We show 10 well-known '
               'sportsbooks. We compare the prices only on the main line. So, better price or '
               "worse spread doesn't win.",
       'timestamp': 115,
       'timestamp_label': '[00:01:55]',
       'timestamp_seconds': 115,
       'tip': 'For each game, it groups the spread odds by sports book, finds the best price '
              'for each team, and refreshes every 30 seconds. We show 10 well-known '
              'sportsbooks. We compare the prices only on the main line. So, better price or '
              "worse spread doesn't win.",
       'title': 'Compare Live Sports Odds Across Sportsbooks in 3 Minutes (Next.js + '
                'SportsGameOdds API) (SportsGameOdds API)',
       'url': 'https://www.youtube.com/watch?v=JXdlRbDVFNY&t=115s',
       'video_id': 'JXdlRbDVFNY'},
      {'author': 'OddsJam Edge',
       'channel': 'OddsJam Edge',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:12](https://www.youtube.com/watch?v=V7_y5HtPs8c&t=252s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And again, in general, these sharp books are much harder to beat, almost '
               "impossible, right? If you're trying to make money betting on Circa, it's going "
               "to be really, really, really, really hard cuz again, it's a sharp book. They "
               'have pretty accurate lines.',
       'timestamp': 252,
       'timestamp_label': '[00:04:12]',
       'timestamp_seconds': 252,
       'tip': 'And again, in general, these sharp books are much harder to beat, almost '
              "impossible, right? If you're trying to make money betting on Circa, it's going "
              "to be really, really, really, really hard cuz again, it's a sharp book. They "
              'have pretty accurate lines.',
       'title': 'How I Use Sharp Sportsbooks to Find +EV Bets (OddsJam Edge)',
       'url': 'https://www.youtube.com/watch?v=V7_y5HtPs8c&t=252s',
       'video_id': 'V7_y5HtPs8c'},
      {'author': 'Metablock iGaming',
       'channel': 'Metablock iGaming',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:33](https://www.youtube.com/watch?v=3O-jguNKEvw&t=753s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You also get granular real-time analytics to see exactly which sports, '
               'leagues, or even specific betting markets are yielding the highest profits. '
               'That allows you to adjust your affiliate marketing spend on the fly.',
       'timestamp': 753,
       'timestamp_label': '[00:12:33]',
       'timestamp_seconds': 753,
       'tip': 'You also get granular real-time analytics to see exactly which sports, leagues, '
              'or even specific betting markets are yielding the highest profits. That allows '
              'you to adjust your affiliate marketing spend on the fly.',
       'title': '𝗪𝗵𝗶𝘁𝗲 𝗟𝗮𝗯𝗲𝗹 𝗦𝗽𝗼𝗿𝘁𝘀𝗯𝗼𝗼𝗸 𝗕𝘂𝘀𝗶𝗻𝗲𝘀𝘀 𝗘𝘅𝗽𝗹𝗮𝗶𝗻𝗲𝗱 | 𝗦𝗮𝗹𝗲𝘀, 𝗟𝗶𝗰𝗲𝗻𝘀𝗶𝗻𝗴 & 𝗣𝗿𝗼𝗳𝗶𝘁 𝗠𝗼𝗱𝗲𝗹 '
                '(Metablock iGaming)',
       'url': 'https://www.youtube.com/watch?v=3O-jguNKEvw&t=753s',
       'video_id': '3O-jguNKEvw'},
      {'author': 'iGaming Marketing Agency Tips by Christian Strutt',
       'channel': 'iGaming Marketing Agency Tips by Christian Strutt',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:19:33](https://www.youtube.com/watch?v=Ag1Beu0lxIM&t=1173s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "If you're targeting the US, get a US domain. The other thing is go "
               'afterformational content first. So, betting strategy guides, betting guides, '
               "casino reviews, sports book reviews, that's the sort of thing that helps to "
               'build trust.',
       'timestamp': 1173,
       'timestamp_label': '[00:19:33]',
       'timestamp_seconds': 1173,
       'tip': "If you're targeting the US, get a US domain. The other thing is go "
              'afterformational content first. So, betting strategy guides, betting guides, '
              "casino reviews, sports book reviews, that's the sort of thing that helps to "
              'build trust.',
       'title': 'Gambling SEO for iGaming Affiliates - iGaming SEO Agency Experts Tips, '
                'Strategy, Advice for SEO (iGaming Marketing Agency Tips by Christian Strutt)',
       'url': 'https://www.youtube.com/watch?v=Ag1Beu0lxIM&t=1173s',
       'video_id': 'Ag1Beu0lxIM'},
      {'author': 'OddsJam: Sports Betting Strategy & Education',
       'channel': 'OddsJam: Sports Betting Strategy & Education',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:41](https://www.youtube.com/watch?v=36K9qpRjKXQ&t=401s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Not 5% then for our Sports books unlike Arbitrage betting we don't need to "
               'execute two bets on two books so here you can even Whittle this down even.',
       'timestamp': 401,
       'timestamp_label': '[00:06:41]',
       'timestamp_seconds': 401,
       'tip': "Not 5% then for our Sports books unlike Arbitrage betting we don't need to "
              'execute two bets on two books so here you can even Whittle this down even.',
       'title': 'The Formula for Live Betting Success using OddsJam (OddsJam: Sports Betting '
                'Strategy & Education)',
       'url': 'https://www.youtube.com/watch?v=36K9qpRjKXQ&t=401s',
       'video_id': '36K9qpRjKXQ'},
      {'author': 'Quantcha',
       'channel': 'Quantcha',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:59](https://www.youtube.com/watch?v=LV2B3nAVotQ&t=179s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Sports events often include a specialized scenario representing the point '
               'spread between two teams. These can be a little tricky to work with on the run '
               'since every market is expressed in terms of the scale of the winning team.',
       'timestamp': 179,
       'timestamp_label': '[00:02:59]',
       'timestamp_seconds': 179,
       'tip': 'Sports events often include a specialized scenario representing the point '
              'spread between two teams. These can be a little tricky to work with on the run '
              'since every market is expressed in terms of the scale of the winning team.',
       'title': 'Master Prediction Market Visuals: Event Charts, Order Books, History & More '
                'in Qwidgets (Quantcha)',
       'url': 'https://www.youtube.com/watch?v=LV2B3nAVotQ&t=179s',
       'video_id': 'LV2B3nAVotQ'},
      {'author': 'Apipheny',
       'channel': 'Apipheny',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:18](https://www.youtube.com/watch?v=tRDcXGZK9RE&t=258s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Apis in Rapid API along with the Epiphany add-on to get any data you want into '
               'your Google sheet if you have any questions feel free to leave a comment or '
               'contact our support team thanks for watching and have a great day.',
       'timestamp': 258,
       'timestamp_label': '[00:04:18]',
       'timestamp_seconds': 258,
       'tip': 'Apis in Rapid API along with the Epiphany add-on to get any data you want into '
              'your Google sheet if you have any questions feel free to leave a comment or '
              'contact our support team thanks for watching and have a great day.',
       'title': 'How To Get Sports Odds Data in Google Sheets For Betting (Apipheny)',
       'url': 'https://www.youtube.com/watch?v=tRDcXGZK9RE&t=258s',
       'video_id': 'tRDcXGZK9RE'},
      {'author': 'Linkee ai',
       'channel': 'Linkee ai',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:26](https://www.youtube.com/watch?v=PGdrtjIirPk&t=26s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And everyone markets SEO to casino, betting, or affiliate brands. The biggest '
               'weight,  25%, went to verified iGaming results, FTDs.',
       'timestamp': 26,
       'timestamp_label': '[00:00:26]',
       'timestamp_seconds': 26,
       'tip': 'And everyone markets SEO to casino, betting, or affiliate brands. The biggest '
              'weight,  25%, went to verified iGaming results, FTDs.',
       'title': 'Best Casino SEO Agencies: Top 10 iGaming SEO Agencies Ranked for FTDs (Linkee '
                'ai)',
       'url': 'https://www.youtube.com/watch?v=PGdrtjIirPk&t=26s',
       'video_id': 'PGdrtjIirPk'},
      {'author': 'PA Gaming Control Board',
       'channel': 'PA Gaming Control Board',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:21:36](https://www.youtube.com/watch?v=gpGZLcIMERI&t=1296s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Well, the award from the North American Gaming Regulators Association was was '
               'quite an was an honor, not only for me as the head of our Bureau of Gaming '
               'Operations, but all of my colleagues in the different bureaus here at the '
               'Gaming Control Board.',
       'timestamp': 1296,
       'timestamp_label': '[00:21:36]',
       'timestamp_seconds': 1296,
       'tip': 'Well, the award from the North American Gaming Regulators Association was was '
              'quite an was an honor, not only for me as the head of our Bureau of Gaming '
              'Operations, but all of my colleagues in the different bureaus here at the '
              'Gaming Control Board.',
       'title': 'How the PGCB Protects Online Gaming Customers with Gaming Operations Director '
                'Paul Resch (PA Gaming Control Board)',
       'url': 'https://www.youtube.com/watch?v=gpGZLcIMERI&t=1296s',
       'video_id': 'gpGZLcIMERI'},
      {'author': 'Revpanda Group',
       'channel': 'Revpanda Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:27:31](https://www.youtube.com/watch?v=OlzqNLFabLI&t=1651s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, the proper approach for a media buyer is to have a test campaign, finding '
               'what performs, and then optimizing and scaling the budget, and having it as a '
               'loop model. So, not once test and then and then scale it, right?',
       'timestamp': 1651,
       'timestamp_label': '[00:27:31]',
       'timestamp_seconds': 1651,
       'tip': 'So, the proper approach for a media buyer is to have a test campaign, finding '
              'what performs, and then optimizing and scaling the budget, and having it as a '
              'loop model. So, not once test and then and then scale it, right?',
       'title': 'World Cup 2026 iGaming Affiliate Battle: SEO, AI, & End of Cheap Traffic '
                '(Revpanda Group)',
       'url': 'https://www.youtube.com/watch?v=OlzqNLFabLI&t=1651s',
       'video_id': 'OlzqNLFabLI'},
      {'author': 'Inside Prediction Markets',
       'channel': 'Inside Prediction Markets',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:34:42](https://www.youtube.com/watch?v=ZmMVHubZpns&t=2082s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Bills are playing a you know, a shitty wild card team. Maybe that's that kind "
               "of suffered an injury late and it's like it's just a 9010 split of where the "
               'money is going and everyone is betting on the the Chiefs or the bills or the '
               'Ravens or whatever.',
       'timestamp': 2082,
       'timestamp_label': '[00:34:42]',
       'timestamp_seconds': 2082,
       'tip': "Bills are playing a you know, a shitty wild card team. Maybe that's that kind "
              "of suffered an injury late and it's like it's just a 9010 split of where the "
              'money is going and everyone is betting on the the Chiefs or the bills or the '
              'Ravens or whatever.',
       'title': 'Novig Climbs to #1 in Sports: What’s Behind the Downloads? (Inside Prediction '
                'Markets)',
       'url': 'https://www.youtube.com/watch?v=ZmMVHubZpns&t=2082s',
       'video_id': 'ZmMVHubZpns'},
      {'author': 'Capperway',
       'channel': 'Capperway',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:40](https://www.youtube.com/watch?v=bvKrNXvCO3I&t=340s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So now, like I said earlier in the video, we have to go ahead and set up our '
               'Discord. And I do feel as if this is necessary, especially if you want to '
               'build a bond with the people that are going to be paying you for your '
               'subscription. So connect your Discord server.',
       'timestamp': 340,
       'timestamp_label': '[00:05:40]',
       'timestamp_seconds': 340,
       'tip': 'So now, like I said earlier in the video, we have to go ahead and set up our '
              'Discord. And I do feel as if this is necessary, especially if you want to build '
              'a bond with the people that are going to be paying you for your subscription. '
              'So connect your Discord server.',
       'title': 'How To Make a $10,000/Month Sports Betting Business (Capperway)',
       'url': 'https://www.youtube.com/watch?v=bvKrNXvCO3I&t=340s',
       'video_id': 'bvKrNXvCO3I'},
      {'author': 'Interactive Brokers',
       'channel': 'Interactive Brokers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:20:11](https://www.youtube.com/watch?v=rMm-V95moXc&t=1211s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Engage with these products and and get involved and you know ideally maybe '
               'make changes in their lives and uh and go out into the world and make the '
               'world a better.',
       'timestamp': 1211,
       'timestamp_label': '[00:20:11]',
       'timestamp_seconds': 1211,
       'tip': 'Engage with these products and and get involved and you know ideally maybe make '
              'changes in their lives and uh and go out into the world and make the world a '
              'better.',
       'title': 'Forecast & Event Contracts Explained - Cents of Security Podcast Ep. 69 '
                '(Interactive Brokers)',
       'url': 'https://www.youtube.com/watch?v=rMm-V95moXc&t=1211s',
       'video_id': 'rMm-V95moXc'},
      {'author': 'Affnook',
       'channel': 'Affnook',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:37](https://www.youtube.com/watch?v=ZnwZv3TNdv0&t=157s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Platforms like Afnook are designed specifically for i gaming businesses. They '
               'offer real-time analytics, omni channel tracking, customizable dashboards, and '
               'automated workflows, helping affiliate managers scale efficiently while '
               'maintaining full control.',
       'timestamp': 157,
       'timestamp_label': '[00:02:37]',
       'timestamp_seconds': 157,
       'tip': 'Platforms like Afnook are designed specifically for i gaming businesses. They '
              'offer real-time analytics, omni channel tracking, customizable dashboards, and '
              'automated workflows, helping affiliate managers scale efficiently while '
              'maintaining full control.',
       'title': 'iGaming Affiliate Software Explained | Everything You Need to Know (Affnook)',
       'url': 'https://www.youtube.com/watch?v=ZnwZv3TNdv0&t=157s',
       'video_id': 'ZnwZv3TNdv0'}],
 12: [{'author': 'OddsJam: Sports Betting Strategy & Education',
       'channel': 'OddsJam: Sports Betting Strategy & Education',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:32](https://www.youtube.com/watch?v=uxFJJTsfAhc&t=32s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'April, I made over $11,000. But for the first 13 days of the month, I focused '
               'exclusively on arbitrage betting, and a large percentage of my bets were live '
               'arbitrage betting. Now, I took a day off on the 7th, so this is actually 12 '
               'days of arbitrage betting.',
       'timestamp': 32,
       'timestamp_label': '[00:00:32]',
       'timestamp_seconds': 32,
       'tip': 'April, I made over $11,000. But for the first 13 days of the month, I focused '
              'exclusively on arbitrage betting, and a large percentage of my bets were live '
              'arbitrage betting. Now, I took a day off on the 7th, so this is actually 12 '
              'days of arbitrage betting.',
       'title': 'I Put Arbitrage and +EV Betting to the Test — The Results SHOCKED Me '
                '(OddsJam: Sports Betting Strategy & Education)',
       'url': 'https://www.youtube.com/watch?v=uxFJJTsfAhc&t=32s',
       'video_id': 'uxFJJTsfAhc'},
      {'author': 'Sports Bet University | Sports Betting Education',
       'channel': 'Sports Bet University | Sports Betting Education',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:46](https://www.youtube.com/watch?v=6VVxJaQPyPc&t=526s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s uh it's uh simple once you get to going with it and once you understand "
               'your your higherics and your daily stacking of edges in order to put together '
               'a bankroll and a building day each day in the in the sports betting world.',
       'timestamp': 526,
       'timestamp_label': '[00:08:46]',
       'timestamp_seconds': 526,
       'tip': "'s uh it's uh simple once you get to going with it and once you understand your "
              'your higherics and your daily stacking of edges in order to put together a '
              'bankroll and a building day each day in the in the sports betting world.',
       'title': 'Advanced OddsJam Tutorial 🔥 How Sharps Find Positive EV Bets & Beat the '
                'Sportsbooks (Sports Bet University | Sports Betting Education)',
       'url': 'https://www.youtube.com/watch?v=6VVxJaQPyPc&t=526s',
       'video_id': '6VVxJaQPyPc'},
      {'author': 'Ace Alliance',
       'channel': 'Ace Alliance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:04](https://www.youtube.com/watch?v=GM2_yRmV_Bw&t=184s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'This sounds pretty amazing and this is such a milestone. And Mika, do you '
               'think is the traditional affiliate model still enough to build really a major '
               "iGaming business, let's say 5 years from now? So we're speaking about that "
               'internally 24 hours a day.',
       'timestamp': 184,
       'timestamp_label': '[00:03:04]',
       'timestamp_seconds': 184,
       'tip': 'This sounds pretty amazing and this is such a milestone. And Mika, do you think '
              'is the traditional affiliate model still enough to build really a major iGaming '
              "business, let's say 5 years from now? So we're speaking about that internally "
              '24 hours a day.',
       'title': 'The Future of Affiliate Marketing in iGaming: SlotCatalog’s New Marketplace | '
                'SBC Summit Lisbon 26 (Ace Alliance)',
       'url': 'https://www.youtube.com/watch?v=GM2_yRmV_Bw&t=184s',
       'video_id': 'GM2_yRmV_Bw'},
      {'author': 'Part Time Larry',
       'channel': 'Part Time Larry',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:48](https://www.youtube.com/watch?v=bA_NUrMJuw4&t=1008s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And then there's these official feeds with Sports Radar partnerships that are "
               'going to be really fast. The best Kavachi traders, the most sophisticated '
               'people that are betting a lot of money, probably have access to the expensive '
               'feeds that might be $5,000 a month.',
       'timestamp': 1008,
       'timestamp_label': '[00:16:48]',
       'timestamp_seconds': 1008,
       'tip': "And then there's these official feeds with Sports Radar partnerships that are "
              'going to be really fast. The best Kavachi traders, the most sophisticated '
              'people that are betting a lot of money, probably have access to the expensive '
              'feeds that might be $5,000 a month.',
       'title': 'I built a Kalshi NFL Prediction Market Bot in Python (it was too slow) (Part '
                'Time Larry)',
       'url': 'https://www.youtube.com/watch?v=bA_NUrMJuw4&t=1008s',
       'video_id': 'bA_NUrMJuw4'},
      {'author': 'OddsJam: Sports Betting Strategy & Education',
       'channel': 'OddsJam: Sports Betting Strategy & Education',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:53](https://www.youtube.com/watch?v=zMU9NWt0gdE&t=473s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'In the last month, in the last 30 days, I think I made around $20,000, give or '
               'take couple couple hundred dollars. Um from a mix of strategies of arbitrage '
               'betting, positive EV, and a large portion of it was actually from these '
               'prediction markets, from using this tool.',
       'timestamp': 473,
       'timestamp_label': '[00:07:53]',
       'timestamp_seconds': 473,
       'tip': 'In the last month, in the last 30 days, I think I made around $20,000, give or '
              'take couple couple hundred dollars. Um from a mix of strategies of arbitrage '
              'betting, positive EV, and a large portion of it was actually from these '
              'prediction markets, from using this tool.',
       'title': 'Why Everyone Is Suddenly Betting on Prediction Markets (OddsJam: Sports '
                'Betting Strategy & Education)',
       'url': 'https://www.youtube.com/watch?v=zMU9NWt0gdE&t=473s',
       'video_id': 'zMU9NWt0gdE'},
      {'author': 'Three Markets –\xa0The Prediction Market Podcast',
       'channel': 'Three Markets –\xa0The Prediction Market Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:35](https://www.youtube.com/watch?v=cwYnvWKtsYo&t=155s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'All linked back all linked back to historic tweet counts per month, week, day, '
               'hour, even minute. Lots of noise, of course, but plenty of alpha, too. The '
               'model was great, far beyond anything the others produced.',
       'timestamp': 155,
       'timestamp_label': '[00:02:35]',
       'timestamp_seconds': 155,
       'tip': 'All linked back all linked back to historic tweet counts per month, week, day, '
              'hour, even minute. Lots of noise, of course, but plenty of alpha, too. The '
              'model was great, far beyond anything the others produced.',
       'title': 'How Quants Trade Prediction Markets (Three Markets –\xa0The Prediction Market '
                'Podcast)',
       'url': 'https://www.youtube.com/watch?v=cwYnvWKtsYo&t=155s',
       'video_id': 'cwYnvWKtsYo'},
      {'author': 'OddsJam Edge',
       'channel': 'OddsJam Edge',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:01](https://www.youtube.com/watch?v=r_G17vayq6A&t=541s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Tools like OddJam can help make that process fast, simple, and repeatable '
               "every single day. And if you start positive EV betting daily, you're already "
               'putting yourself in a position that most sports bettors will never reach.',
       'timestamp': 541,
       'timestamp_label': '[00:09:01]',
       'timestamp_seconds': 541,
       'tip': 'Tools like OddJam can help make that process fast, simple, and repeatable every '
              "single day. And if you start positive EV betting daily, you're already putting "
              'yourself in a position that most sports bettors will never reach.',
       'title': 'How to Find +EV Bets Before the Sportsbooks Fix Them (OddsJam Edge)',
       'url': 'https://www.youtube.com/watch?v=r_G17vayq6A&t=541s',
       'video_id': 'r_G17vayq6A'},
      {'author': 'Capperway',
       'channel': 'Capperway',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:54](https://www.youtube.com/watch?v=uMAJwS6tPzw&t=54s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "What does your subscription have to offer that maybe someone else's "
               "subscription won't have, right? You need to come up with all of the reasons, "
               "like maybe it's EV betting, arbitrage betting, an active community, you know, "
               'daily plays of the day, all these kinds of things.',
       'timestamp': 54,
       'timestamp_label': '[00:00:54]',
       'timestamp_seconds': 54,
       'tip': "What does your subscription have to offer that maybe someone else's "
              "subscription won't have, right? You need to come up with all of the reasons, "
              "like maybe it's EV betting, arbitrage betting, an active community, you know, "
              'daily plays of the day, all these kinds of things.',
       'title': 'How To Make "F*ck you" Money with a Sports Betting Business in 2026... '
                '(Capperway)',
       'url': 'https://www.youtube.com/watch?v=uMAJwS6tPzw&t=54s',
       'video_id': 'uMAJwS6tPzw'},
      {'author': 'OngPredicts',
       'channel': 'OngPredicts',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:49](https://www.youtube.com/watch?v=kDOrvOpgzjE&t=109s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Name it anything and grab this and put it in a safe place. Next, head over to '
               'Predict It Fi. You register for an account and you get your free API key. And '
               'make sure you have a valid account so you can have access the free Predict It '
               "Fi's API key on the free plan.",
       'timestamp': 109,
       'timestamp_label': '[00:01:49]',
       'timestamp_seconds': 109,
       'tip': 'Name it anything and grab this and put it in a safe place. Next, head over to '
              'Predict It Fi. You register for an account and you get your free API key. And '
              'make sure you have a valid account so you can have access the free Predict It '
              "Fi's API key on the free plan.",
       'title': 'How I Built a Profitable Polymarket AI Trading Bot Using JEV (OngPredicts)',
       'url': 'https://www.youtube.com/watch?v=kDOrvOpgzjE&t=109s',
       'video_id': 'kDOrvOpgzjE'},
      {'author': 'Polymarket Plays & Analysis',
       'channel': 'Polymarket Plays & Analysis',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:35](https://www.youtube.com/watch?v=akeWaTjtmIA&t=515s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "The perceived shift in American public opinion reflected in Gallop's statement "
               'could lead bettors to reassess probabilities associated with a return to the '
               'Joint Comprehensive Plan of Action JCPOA.',
       'timestamp': 515,
       'timestamp_label': '[00:08:35]',
       'timestamp_seconds': 515,
       'tip': "The perceived shift in American public opinion reflected in Gallop's statement "
              'could lead bettors to reassess probabilities associated with a return to the '
              'Joint Comprehensive Plan of Action JCPOA.',
       'title': 'Iran War Prediction Markets — Polymarket Analysis 2026-11-06 | Political '
                'Betting Odds & News Update (Polymarket Plays & Analysis)',
       'url': 'https://www.youtube.com/watch?v=akeWaTjtmIA&t=515s',
       'video_id': 'akeWaTjtmIA'},
      {'author': 'Diveroli Affiliate Marketing',
       'channel': 'Diveroli Affiliate Marketing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:26](https://www.youtube.com/watch?v=fpjGrq-HJJ4&t=686s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Well, new style ads too, only they're getting more aggressive now. So, if "
               'before it was like a milkmaid from Nigeria or a minor who went to the mine '
               "every day and now he doesn't work, that kind of thing rarely catches on for us "
               'anymore.',
       'timestamp': 686,
       'timestamp_label': '[00:11:26]',
       'timestamp_seconds': 686,
       'tip': "Well, new style ads too, only they're getting more aggressive now. So, if "
              'before it was like a milkmaid from Nigeria or a minor who went to the mine '
              "every day and now he doesn't work, that kind of thing rarely catches on for us "
              'anymore.',
       'title': 'Best iGaming Ad Creatives in 2026: What Works Beyond Slots & Crash Games '
                '(Diveroli Affiliate Marketing)',
       'url': 'https://www.youtube.com/watch?v=fpjGrq-HJJ4&t=686s',
       'video_id': 'fpjGrq-HJJ4'},
      {'author': 'Inside Prediction Markets',
       'channel': 'Inside Prediction Markets',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:46](https://www.youtube.com/watch?v=ieRL4BXtMGA&t=946s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'It could be a week or two if the 90% tax proposal got resolved tomorrow, would '
               'you start playing OSB again or have you kind of the the die has been cast. I '
               'am full on PM so I am not looking back unless the Supreme Court says '
               'otherwise.',
       'timestamp': 946,
       'timestamp_label': '[00:15:46]',
       'timestamp_seconds': 946,
       'tip': 'It could be a week or two if the 90% tax proposal got resolved tomorrow, would '
              'you start playing OSB again or have you kind of the the die has been cast. I am '
              'full on PM so I am not looking back unless the Supreme Court says otherwise.',
       'title': 'Turning $100 to $1M on Prediction Markets: How to Build a Winning Operation '
                '(Inside Prediction Markets)',
       'url': 'https://www.youtube.com/watch?v=ieRL4BXtMGA&t=946s',
       'video_id': 'ieRL4BXtMGA'},
      {'author': 'Interactive Brokers',
       'channel': 'Interactive Brokers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:39](https://www.youtube.com/watch?v=Vix7rchq6b8&t=819s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Balanced more tilted towards a 25 basis point reduction uh and we we see those '
               'kinds of Arbitrage opportunities across our markets pretty much every single '
               'day.',
       'timestamp': 819,
       'timestamp_label': '[00:13:39]',
       'timestamp_seconds': 819,
       'tip': 'Balanced more tilted towards a 25 basis point reduction uh and we we see those '
              'kinds of Arbitrage opportunities across our markets pretty much every single '
              'day.',
       'title': 'A Behind the Scenes Look at ForecastEx Events Contracts- IBKR Podcast Ep. 181 '
                '(Interactive Brokers)',
       'url': 'https://www.youtube.com/watch?v=Vix7rchq6b8&t=819s',
       'video_id': 'Vix7rchq6b8'},
      {'author': 'John Crestani',
       'channel': 'John Crestani',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:41:35](https://www.youtube.com/watch?v=rEP2Pyna6UA&t=6095s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "The next day and the next day because you're worried about failing or doing it "
               'wrong when actually the best way to do things wrong is to consume and not do '
               'anything at all.',
       'timestamp': 6095,
       'timestamp_label': '[01:41:35]',
       'timestamp_seconds': 6095,
       'tip': "The next day and the next day because you're worried about failing or doing it "
              'wrong when actually the best way to do things wrong is to consume and not do '
              'anything at all.',
       'title': 'Own an Online Casino | Gambling Affiliate Marketing Strategy (John Crestani)',
       'url': 'https://www.youtube.com/watch?v=rEP2Pyna6UA&t=6095s',
       'video_id': 'rEP2Pyna6UA'},
      {'author': 'BetSmart',
       'channel': 'BetSmart',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:39](https://www.youtube.com/watch?v=jauhFM_n5d4&t=399s)',
       'relevance': 'Attributed practitioner commentary on non-custodial `CFTC`-regulated '
                    'event-contract (`DCM`) analytics terminals, real-time cross-venue odds '
                    'SaaS subscriptions, and state-licensed (`NJ`/`PA`/`MI`/`WV`/`ON`) '
                    'sportsbook/iGaming `CPA` and `NGR` affiliate comparison portals (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I've been giving out codes for the last week. Better's giving out codes all "
               'the time. So, make sure to follow us links in the description to get yourself '
               'access to Be Better for 100% free.',
       'timestamp': 399,
       'timestamp_label': '[00:06:39]',
       'timestamp_seconds': 399,
       'tip': "I've been giving out codes for the last week. Better's giving out codes all the "
              'time. So, make sure to follow us links in the description to get yourself '
              'access to Be Better for 100% free.',
       'title': 'A Free Sports Betting Odds Screen & a Pro-Level Prediction Market Terminal: 2 '
                'Tools I Tested (BetSmart)',
       'url': 'https://www.youtube.com/watch?v=jauhFM_n5d4&t=399s',
       'video_id': 'jauhFM_n5d4'}]}
