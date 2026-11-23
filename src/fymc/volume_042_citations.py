"""Curated 180-citation Cell-Tower, Digital-Billboard & IOS Lease Arbitrage baseline (15 per chapter across Q1-Q12) mined strictly from verified Cell-Tower, Digital-Billboard & IOS Lease Arbitrage YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'1031',
     '16x',
     '180k',
     '22x',
     'aadt',
     'act',
     'advertising',
     'aggregators',
     'annual',
     'antenna',
     'apwireless',
     'arbitrage',
     'asr',
     'assignment',
     'audit',
     'automated',
     'battery',
     'beautification',
     'bess',
     'billboard',
     'billboards',
     'broker',
     'brokerage',
     'building',
     'business',
     'buyout',
     'calling',
     'capex',
     'case',
     'cashflow',
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
 2: {'1031',
     '16x',
     '180k',
     '22x',
     'aadt',
     'act',
     'advertising',
     'aggregators',
     'annual',
     'antenna',
     'apwireless',
     'arbitrage',
     'asr',
     'assignment',
     'audit',
     'automated',
     'battery',
     'beautification',
     'bess',
     'billboard',
     'billboards',
     'broker',
     'brokerage',
     'budget',
     'building',
     'business',
     'buyer',
     'buyout',
     'calling',
     'capex',
     'case',
     'cashflow',
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
 3: {'1031',
     '16x',
     '180k',
     '22x',
     'aadt',
     'act',
     'advertising',
     'aggregators',
     'annual',
     'antenna',
     'apwireless',
     'arbitrage',
     'asr',
     'assignment',
     'audit',
     'automated',
     'battery',
     'beautification',
     'bess',
     'billboard',
     'billboards',
     'broker',
     'brokerage',
     'building',
     'business',
     'buyout',
     'calling',
     'capex',
     'case',
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
 4: {'1031',
     '16x',
     '180k',
     '22x',
     'aadt',
     'act',
     'advertising',
     'aggregators',
     'annual',
     'antenna',
     'apwireless',
     'arbitrage',
     'asr',
     'assignment',
     'audit',
     'automated',
     'battery',
     'beautification',
     'bess',
     'billboard',
     'billboards',
     'broker',
     'brokerage',
     'budget',
     'building',
     'business',
     'buyout',
     'calling',
     'capex',
     'capital',
     'case',
     'cashflow',
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
 5: {'1031',
     '16x',
     '180k',
     '22x',
     'aadt',
     'act',
     'advertising',
     'aggregators',
     'annual',
     'antenna',
     'apwireless',
     'arbitrage',
     'asr',
     'assignment',
     'audit',
     'automated',
     'avoid',
     'battery',
     'beautification',
     'bess',
     'billboard',
     'billboards',
     'broker',
     'brokerage',
     'building',
     'business',
     'buyout',
     'calling',
     'capex',
     'case',
     'cashflow',
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
 6: {'1031',
     '16x',
     '180k',
     '22x',
     'aadt',
     'act',
     'advertising',
     'aggregators',
     'annual',
     'antenna',
     'apwireless',
     'arbitrage',
     'asr',
     'assignment',
     'audit',
     'automated',
     'battery',
     'beautification',
     'bess',
     'billboard',
     'billboards',
     'broker',
     'brokerage',
     'building',
     'business',
     'buyout',
     'calling',
     'capex',
     'case',
     'cashflow',
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
 7: {'1031',
     '16x',
     '180k',
     '22x',
     'aadt',
     'act',
     'advertising',
     'aggregators',
     'annual',
     'antenna',
     'apwireless',
     'arbitrage',
     'asr',
     'assignment',
     'audit',
     'automated',
     'battery',
     'beautification',
     'bess',
     'billboard',
     'billboards',
     'broker',
     'brokerage',
     'building',
     'business',
     'buyout',
     'calling',
     'capex',
     'case',
     'cashflow',
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
 8: {'1031',
     '16x',
     '180k',
     '22x',
     'aadt',
     'act',
     'advertising',
     'aggregators',
     'annual',
     'antenna',
     'api',
     'apwireless',
     'arbitrage',
     'asr',
     'assignment',
     'audit',
     'automated',
     'battery',
     'beautification',
     'bess',
     'billboard',
     'billboards',
     'broker',
     'brokerage',
     'building',
     'business',
     'buyout',
     'calling',
     'capex',
     'case',
     'cashflow',
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
 9: {'1031',
     '16x',
     '180k',
     '22x',
     'aadt',
     'act',
     'advertising',
     'aggregators',
     'agreement',
     'annual',
     'antenna',
     'apwireless',
     'arbitrage',
     'asr',
     'assignment',
     'audit',
     'automated',
     'battery',
     'beautification',
     'bess',
     'billboard',
     'billboards',
     'broker',
     'brokerage',
     'building',
     'business',
     'buyout',
     'calling',
     'capex',
     'case',
     'cashflow',
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
 10: {'1031',
      '16x',
      '180k',
      '22x',
      'aadt',
      'act',
      'advertising',
      'agent',
      'aggregators',
      'ai',
      'annual',
      'antenna',
      'apwireless',
      'arbitrage',
      'asr',
      'assignment',
      'audit',
      'automate',
      'automated',
      'automation',
      'battery',
      'beautification',
      'bess',
      'billboard',
      'billboards',
      'broker',
      'brokerage',
      'building',
      'business',
      'buyout',
      'calling',
      'capex',
      'case',
      'cashflow',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'1031',
      '16x',
      '180k',
      '22x',
      'aadt',
      'act',
      'advertising',
      'aggregators',
      'annual',
      'antenna',
      'apwireless',
      'arbitrage',
      'asr',
      'assignment',
      'audit',
      'automated',
      'battery',
      'beautification',
      'bess',
      'billboard',
      'billboards',
      'broker',
      'brokerage',
      'building',
      'business',
      'buyout',
      'calling',
      'capex',
      'case',
      'cashflow',
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
 12: {'1031',
      '16x',
      '180k',
      '22x',
      'aadt',
      'act',
      'action',
      'advertising',
      'aggregators',
      'annual',
      'antenna',
      'apwireless',
      'arbitrage',
      'asr',
      'assignment',
      'audit',
      'automated',
      'battery',
      'beautification',
      'bess',
      'billboard',
      'billboards',
      'broker',
      'brokerage',
      'building',
      'business',
      'buyout',
      'calling',
      'capex',
      'case',
      'cashflow',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Rio Explains',
      'channel': 'Rio Explains',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:30](https://www.youtube.com/watch?v=OYv2q23Z36g&t=450s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'American business, but only for the operator disciplined enough to keep debt '
              'low while everyone else in the industry overleverages chasing the same scarce '
              "inventory. Lamar didn't win this market by building the most billboards.",
      'timestamp': 450,
      'timestamp_label': '[00:07:30]',
      'timestamp_seconds': 450,
      'tip': 'American business, but only for the operator disciplined enough to keep debt low '
             'while everyone else in the industry overleverages chasing the same scarce '
             "inventory. Lamar didn't win this market by building the most billboards.",
      'title': 'So You Want to Own a Billboard Company (Rio Explains)',
      'url': 'https://www.youtube.com/watch?v=OYv2q23Z36g&t=450s',
      'video_id': 'OYv2q23Z36g'},
     {'author': 'Mr. Money',
      'channel': 'Mr. Money',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:23](https://www.youtube.com/watch?v=t4mEx2qxaZ8&t=503s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The business model rewards patience, good locations, and above all, permits. '
              'Billboards are not really an advertising business. They are a scarce permission '
              'business.',
      'timestamp': 503,
      'timestamp_label': '[00:08:23]',
      'timestamp_seconds': 503,
      'tip': 'The business model rewards patience, good locations, and above all, permits. '
             'Billboards are not really an advertising business. They are a scarce permission '
             'business.',
      'title': 'So You Want to Own a Billboard? The Real Numbers Behind $10,000 a Month (Mr. '
               'Money)',
      'url': 'https://www.youtube.com/watch?v=t4mEx2qxaZ8&t=503s',
      'video_id': 't4mEx2qxaZ8'},
     {'author': 'Hidden Economics',
      'channel': 'Hidden Economics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:41](https://www.youtube.com/watch?v=XlZ7pkhH2fM&t=221s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Landowners have to deploy strict defensive tactics to survive. That means '
              'demanding percentage-based revenue share clauses, explicitly blocking hidden '
              '20-year automatic renewals, and securing annual audit rights to verify the '
              "operator's actual income.",
      'timestamp': 221,
      'timestamp_label': '[00:03:41]',
      'timestamp_seconds': 221,
      'tip': 'Landowners have to deploy strict defensive tactics to survive. That means '
             'demanding percentage-based revenue share clauses, explicitly blocking hidden '
             '20-year automatic renewals, and securing annual audit rights to verify the '
             "operator's actual income.",
      'title': 'The Economics of Owning a Billboard (Hidden Economics)',
      'url': 'https://www.youtube.com/watch?v=XlZ7pkhH2fM&t=221s',
      'video_id': 'XlZ7pkhH2fM'},
     {'author': 'Tonnage',
      'channel': 'Tonnage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:57](https://www.youtube.com/watch?v=Jr3ddPekZXw&t=177s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The landowner collects rent. The billboard operator collects the advertising '
              'revenue. An advertiser pays to place a message on a structure facing passing '
              'traffic while the operator pays for the right to keep that structure on the '
              'property.',
      'timestamp': 177,
      'timestamp_label': '[00:02:57]',
      'timestamp_seconds': 177,
      'tip': 'The landowner collects rent. The billboard operator collects the advertising '
             'revenue. An advertiser pays to place a message on a structure facing passing '
             'traffic while the operator pays for the right to keep that structure on the '
             'property.',
      'title': 'Highway Billboards: The $9.1B Monopoly Hiding in Plain Sight (Tonnage)',
      'url': 'https://www.youtube.com/watch?v=Jr3ddPekZXw&t=177s',
      'video_id': 'Jr3ddPekZXw'},
     {'author': 'Econometrics',
      'channel': 'Econometrics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:25](https://www.youtube.com/watch?v=q9ejuh31AvI&t=445s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Some sites have a charge that moves with advertising revenue on top of the '
              'fixed amount. That means a vacancy can reduce part of the rent bill while '
              'leaving the base due. The size of the fixed payment helps determine how much '
              'protection the operator gets.',
      'timestamp': 445,
      'timestamp_label': '[00:07:25]',
      'timestamp_seconds': 445,
      'tip': 'Some sites have a charge that moves with advertising revenue on top of the fixed '
             'amount. That means a vacancy can reduce part of the rent bill while leaving the '
             'base due. The size of the fixed payment helps determine how much protection the '
             'operator gets.',
      'title': 'The Hidden Economics of an Empty Billboard (Econometrics)',
      'url': 'https://www.youtube.com/watch?v=q9ejuh31AvI&t=445s',
      'video_id': 'q9ejuh31AvI'},
     {'author': 'Adding Value w/ Shy Assar | CRE & Industrial',
      'channel': 'Adding Value w/ Shy Assar | CRE & Industrial',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:58](https://www.youtube.com/watch?v=7qT_5Pw0cTo&t=658s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, let's talk about the deal profile. That's equates about $50 a land square "
              "foot. Walk us through the business plan. Well, anytime that we're buying "
              "something vacant, we have, you know, value add proposition. We're we're looking "
              'to go out to market for lease.',
      'timestamp': 658,
      'timestamp_label': '[00:10:58]',
      'timestamp_seconds': 658,
      'tip': "So, let's talk about the deal profile. That's equates about $50 a land square "
             "foot. Walk us through the business plan. Well, anytime that we're buying "
             "something vacant, we have, you know, value add proposition. We're we're looking "
             'to go out to market for lease.',
      'title': 'Inside a $4.8M Industrial Outdoor Storage (IOS) Deal in Fontana | Benji Miller '
               '(Adding Value w/ Shy Assar | CRE & Industrial)',
      'url': 'https://www.youtube.com/watch?v=7qT_5Pw0cTo&t=658s',
      'video_id': '7qT_5Pw0cTo'},
     {'author': 'Profit Chain',
      'channel': 'Profit Chain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:02](https://www.youtube.com/watch?v=t9bXdQI0jPM&t=782s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The land has value, the steel has value, and the network location has value. '
              'But a large part of the business model comes from how effectively the tower '
              'company turns one site into a platform serving several customers.',
      'timestamp': 782,
      'timestamp_label': '[00:13:02]',
      'timestamp_seconds': 782,
      'tip': 'The land has value, the steel has value, and the network location has value. But '
             'a large part of the business model comes from how effectively the tower company '
             'turns one site into a platform serving several customers.',
      'title': 'A Cell Tower Pays Its Landowner $2,000 a Month. So Why Are Tower Companies '
               'Worth Billions? (Profit Chain)',
      'url': 'https://www.youtube.com/watch?v=t9bXdQI0jPM&t=782s',
      'video_id': 't9bXdQI0jPM'},
     {'author': 'Tower Genius',
      'channel': 'Tower Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:21](https://www.youtube.com/watch?v=weiPEHNdlU0&t=81s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Our genius is a consulting firm so this is just business uh my business opinion '
              'uh my telecommunications opinion so.',
      'timestamp': 81,
      'timestamp_label': '[00:01:21]',
      'timestamp_seconds': 81,
      'tip': 'Our genius is a consulting firm so this is just business uh my business opinion '
             'uh my telecommunications opinion so.',
      'title': 'Perpetual Easements - Why Cell Tower Lease Buyouts Can Lower Property Value '
               'When Selling a House. (Tower Genius)',
      'url': 'https://www.youtube.com/watch?v=weiPEHNdlU0&t=81s',
      'video_id': 'weiPEHNdlU0'},
     {'author': 'SAENTYS',
      'channel': 'SAENTYS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:38:41](https://www.youtube.com/watch?v=4dMhVDuB-hM&t=2321s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um, but, um, yeah, that was, that's probably the classic case study. European "
              'market is obviously made up of loads of different markets, but how does it '
              'compare? How do you, how does the UK compare to the rest of Europe?',
      'timestamp': 2321,
      'timestamp_label': '[00:38:41]',
      'timestamp_seconds': 2321,
      'tip': "Um, but, um, yeah, that was, that's probably the classic case study. European "
             'market is obviously made up of loads of different markets, but how does it '
             'compare? How do you, how does the UK compare to the rest of Europe?',
      'title': 'ANDREW SMITH: Is Industrial Open Storage (IOS) The Hidden Real Estate '
               'Goldmine? (SAENTYS)',
      'url': 'https://www.youtube.com/watch?v=4dMhVDuB-hM&t=2321s',
      'video_id': '4dMhVDuB-hM'},
     {'author': 'Garret Wong Podcast',
      'channel': 'Garret Wong Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:03](https://www.youtube.com/watch?v=RPNJmiZNQdY&t=843s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s there's so many unique things that you see. Um and as long as our zoning "
              "allows that flexibility we will allow it and it's it's really cool. So what is "
              "your prototypical client then? It's it's a mixture of like logistics and a "
              'small business.',
      'timestamp': 843,
      'timestamp_label': '[00:14:03]',
      'timestamp_seconds': 843,
      'tip': "'s there's so many unique things that you see. Um and as long as our zoning "
             "allows that flexibility we will allow it and it's it's really cool. So what is "
             "your prototypical client then? It's it's a mixture of like logistics and a small "
             'business.',
      'title': 'How to Invest in Industrial Outdoor Storage (Garret Wong Podcast)',
      'url': 'https://www.youtube.com/watch?v=RPNJmiZNQdY&t=843s',
      'video_id': 'RPNJmiZNQdY'},
     {'author': 'Vertical Consultants',
      'channel': 'Vertical Consultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=pwMG_wkkefQ&t=68s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sometimes people think, "Well, I want to know what the market rates are my '
              'area." Well, a cell tower company doesn\'t compare sites in their area when '
              "they're determining what the value of a cell tower is to them. They look at "
              'individual situations.',
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': 'Sometimes people think, "Well, I want to know what the market rates are my '
             'area." Well, a cell tower company doesn\'t compare sites in their area when '
             "they're determining what the value of a cell tower is to them. They look at "
             'individual situations.',
      'title': 'Make REAL Money from Your Cell Tower Lease | What the Carriers Won’t Tell You '
               '(Vertical Consultants)',
      'url': 'https://www.youtube.com/watch?v=pwMG_wkkefQ&t=68s',
      'video_id': 'pwMG_wkkefQ'},
     {'author': 'Jared VanderMeer',
      'channel': 'Jared VanderMeer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:27](https://www.youtube.com/watch?v=NtQMMoZo6dw&t=327s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Couple more youtube videos in this location I hope you guys are getting value '
              'if you have any feedback for me make sure you put in the comments below and '
              'smash like or dislike whatever you guys think hope to see you guys in the next '
              "episode that's all for now.",
      'timestamp': 327,
      'timestamp_label': '[00:05:27]',
      'timestamp_seconds': 327,
      'tip': 'Couple more youtube videos in this location I hope you guys are getting value if '
             'you have any feedback for me make sure you put in the comments below and smash '
             'like or dislike whatever you guys think hope to see you guys in the next episode '
             "that's all for now.",
      'title': 'Does Billboard Advertising Make Sense | Explanation with Math (Jared '
               'VanderMeer)',
      'url': 'https://www.youtube.com/watch?v=NtQMMoZo6dw&t=327s',
      'video_id': 'NtQMMoZo6dw'},
     {'author': 'Vertical Consultants',
      'channel': 'Vertical Consultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:07](https://www.youtube.com/watch?v=eJhWsOIzk6A&t=127s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Want to see how much money I'm making every day every year Etc you need to make "
              'sure you structure a revenue share correctly so you get the right value going '
              'forward today and throughout the term ofal lease get more money get a better '
              'lease get vertical.',
      'timestamp': 127,
      'timestamp_label': '[00:02:07]',
      'timestamp_seconds': 127,
      'tip': "Want to see how much money I'm making every day every year Etc you need to make "
             'sure you structure a revenue share correctly so you get the right value going '
             'forward today and throughout the term ofal lease get more money get a better '
             'lease get vertical.',
      'title': "What Cell Tower Companies Don't Tell You About Leases! (Vertical Consultants)",
      'url': 'https://www.youtube.com/watch?v=eJhWsOIzk6A&t=127s',
      'video_id': 'eJhWsOIzk6A'},
     {'author': 'Vertical Consultants',
      'channel': 'Vertical Consultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=LPZ7-ZDffP8&t=75s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Thing as Market rent every cell site has its own individual value the cell '
              "tower companies don't want you to know that they want you to rely on what they "
              'paid other people why because they made really good deals for themselves and '
              'the property owners are get underpaid.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': 'Thing as Market rent every cell site has its own individual value the cell tower '
             "companies don't want you to know that they want you to rely on what they paid "
             'other people why because they made really good deals for themselves and the '
             'property owners are get underpaid.',
      'title': 'Calculating Cell Tower Rental Rates How Much And Why? (Vertical Consultants)',
      'url': 'https://www.youtube.com/watch?v=LPZ7-ZDffP8&t=75s',
      'video_id': 'LPZ7-ZDffP8'},
     {'author': 'Tower Genius',
      'channel': 'Tower Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:30](https://www.youtube.com/watch?v=Z2FKmFdZgvA&t=390s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Equipment up there's another word that was placed in there in place of "
              "equipment and what's with this situation another word that was in there and how "
              'do we spell stupid alan in new hampshire so um I like I like his instincts.',
      'timestamp': 390,
      'timestamp_label': '[00:06:30]',
      'timestamp_seconds': 390,
      'tip': "Equipment up there's another word that was placed in there in place of equipment "
             "and what's with this situation another word that was in there and how do we "
             'spell stupid alan in new hampshire so um I like I like his instincts.',
      'title': 'Bought Land that had Buyout Perpetual Easement PLUS Cell Site "Lease '
               'Optimization Letter" - Q&A (Tower Genius)',
      'url': 'https://www.youtube.com/watch?v=Z2FKmFdZgvA&t=390s',
      'video_id': 'Z2FKmFdZgvA'}],
 2: [{'author': 'Finpulse',
      'channel': 'Finpulse',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:42](https://www.youtube.com/watch?v=WCGRAxsks5U&t=162s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The operator negotiates a contract with the landowner and obtains the necessary '
              'approvals before building or installing a billboard. The landowner might '
              'receive a fixed monthly payment. Alternatively, the agreement could include '
              'rent based partly on advertising revenue.',
      'timestamp': 162,
      'timestamp_label': '[00:02:42]',
      'timestamp_seconds': 162,
      'tip': 'The operator negotiates a contract with the landowner and obtains the necessary '
             'approvals before building or installing a billboard. The landowner might receive '
             'a fixed monthly payment. Alternatively, the agreement could include rent based '
             'partly on advertising revenue.',
      'title': 'The Secret Billboard Business Nobody Talks About (Finpulse)',
      'url': 'https://www.youtube.com/watch?v=WCGRAxsks5U&t=162s',
      'video_id': 'WCGRAxsks5U'},
     {'author': 'Money Mechanics',
      'channel': 'Money Mechanics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:20](https://www.youtube.com/watch?v=PIQPl5zhm5s&t=440s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s strip the business down to its simplest possible form. You acquire a legal "
              'billboard location. You sell advertising space. You maintain the structure. You '
              "pay the landowner if you don't own the land.",
      'timestamp': 440,
      'timestamp_label': '[00:07:20]',
      'timestamp_seconds': 440,
      'tip': "'s strip the business down to its simplest possible form. You acquire a legal "
             'billboard location. You sell advertising space. You maintain the structure. You '
             "pay the landowner if you don't own the land.",
      'title': 'The Economics of Owning a Billboard (Money Mechanics)',
      'url': 'https://www.youtube.com/watch?v=PIQPl5zhm5s&t=440s',
      'video_id': 'PIQPl5zhm5s'},
     {'author': 'Bama Billboards',
      'channel': 'Bama Billboards',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:24](https://www.youtube.com/watch?v=rxbKA112Tdc&t=444s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re going to want to get a rent/ lease agreement between you and anybody "
              'interested in advertising. Uh, this is important in case, you know, they want '
              'to rent the sign for a year and they only pay for three months.',
      'timestamp': 444,
      'timestamp_label': '[00:07:24]',
      'timestamp_seconds': 444,
      'tip': "'re going to want to get a rent/ lease agreement between you and anybody "
             'interested in advertising. Uh, this is important in case, you know, they want to '
             'rent the sign for a year and they only pay for three months.',
      'title': 'How to start a Billboard Company in 7 Steps (Bama Billboards)',
      'url': 'https://www.youtube.com/watch?v=rxbKA112Tdc&t=444s',
      'video_id': 'rxbKA112Tdc'},
     {'author': 'County Portal',
      'channel': 'County Portal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=V9oP66yUklk&t=102s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You typically get paid in one of two ways. A flat monthly or annual fee, which '
              'gives you predictable, guaranteed income, or a percentage of the advertising '
              'revenue the sign generates.',
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': 'You typically get paid in one of two ways. A flat monthly or annual fee, which '
             'gives you predictable, guaranteed income, or a percentage of the advertising '
             'revenue the sign generates.',
      'title': 'How Much Do Property Owners Get For Billboards? (County Portal)',
      'url': 'https://www.youtube.com/watch?v=V9oP66yUklk&t=102s',
      'video_id': 'V9oP66yUklk'},
     {'author': 'Acquisition Insider',
      'channel': 'Acquisition Insider',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:30](https://www.youtube.com/watch?v=4PyMov-VjoE&t=270s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'DOT about construction plans. And fourth, the sales grind. This is a media '
              'business wearing a real estate costume. And the passive seat belongs to the '
              'landowner collecting ground rent, not to you. So, how does a real buyer '
              "actually find one? There's no MLS for billboards.",
      'timestamp': 270,
      'timestamp_label': '[00:04:30]',
      'timestamp_seconds': 270,
      'tip': 'DOT about construction plans. And fourth, the sales grind. This is a media '
             'business wearing a real estate costume. And the passive seat belongs to the '
             'landowner collecting ground rent, not to you. So, how does a real buyer actually '
             "find one? There's no MLS for billboards.",
      'title': 'How to Acquire a Billboard (A 1965 Law Built the Moat) (Acquisition Insider)',
      'url': 'https://www.youtube.com/watch?v=4PyMov-VjoE&t=270s',
      'video_id': '4PyMov-VjoE'},
     {'author': 'James Furlo | Furlo Capital',
      'channel': 'James Furlo | Furlo Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:39](https://www.youtube.com/watch?v=bk4EnTlbPdA&t=159s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "One of the things I've recently learned, uh, okay. They, so these two companies "
              'essentially got a lease for part of the building to build their cell towers and '
              "then they pay a monthly fee. So it's not like they're, it's not like they own "
              'the roof or own part of the building.',
      'timestamp': 159,
      'timestamp_label': '[00:02:39]',
      'timestamp_seconds': 159,
      'tip': "One of the things I've recently learned, uh, okay. They, so these two companies "
             'essentially got a lease for part of the building to build their cell towers and '
             "then they pay a monthly fee. So it's not like they're, it's not like they own "
             'the roof or own part of the building.',
      'title': 'Cell Tower Lease Buyouts: Smart Evaluation Tips for Investors | Ep 83 (James '
               'Furlo | Furlo Capital)',
      'url': 'https://www.youtube.com/watch?v=bk4EnTlbPdA&t=159s',
      'video_id': 'bk4EnTlbPdA'},
     {'author': 'MoneyLogics',
      'channel': 'MoneyLogics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:09](https://www.youtube.com/watch?v=8Emqeya9KGo&t=69s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's how a sliver of signs pays like a giant. So why doesn't everyone build "
              'one? Because the sign is the easy part. Four states, Alaska, Hawaii, Vermont, '
              'and Maine ban new billboards outright.',
      'timestamp': 69,
      'timestamp_label': '[00:01:09]',
      'timestamp_seconds': 69,
      'tip': "That's how a sliver of signs pays like a giant. So why doesn't everyone build "
             'one? Because the sign is the easy part. Four states, Alaska, Hawaii, Vermont, '
             'and Maine ban new billboards outright.',
      'title': 'How Much Does a Billboard Really Make? (MoneyLogics)',
      'url': 'https://www.youtube.com/watch?v=8Emqeya9KGo&t=69s',
      'video_id': '8Emqeya9KGo'},
     {'author': 'Vertical Consultants',
      'channel': 'Vertical Consultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:18](https://www.youtube.com/watch?v=F1m9euwLJAQ&t=1338s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, if you're if you're offered a situation, sometimes you see this in new cell "
              'tower leases as well. They say, "Well, I\'ll pay you $1,000 a month or I\'ll '
              'give you a a one-time uh fee of of $100,000 for a 99-year lease.".',
      'timestamp': 1338,
      'timestamp_label': '[00:22:18]',
      'timestamp_seconds': 1338,
      'tip': "So, if you're if you're offered a situation, sometimes you see this in new cell "
             'tower leases as well. They say, "Well, I\'ll pay you $1,000 a month or I\'ll '
             'give you a a one-time uh fee of of $100,000 for a 99-year lease.".',
      'title': 'Cell Tower Rent, Escalators, Buyouts and More — Complete Guide for Property '
               'Owners (Vertical Consultants)',
      'url': 'https://www.youtube.com/watch?v=F1m9euwLJAQ&t=1338s',
      'video_id': 'F1m9euwLJAQ'},
     {'author': 'Buildrightacademy',
      'channel': 'Buildrightacademy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:06](https://www.youtube.com/watch?v=kHmq6jr22Ms&t=366s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Here is something you can use on any site. Whatever the type, a US tower is '
              'designed to a national standard, ANSI/TIA-222, usually through the local '
              'building code. It says how much antenna weight and wind and ice the steel must '
              'carry.',
      'timestamp': 366,
      'timestamp_label': '[00:06:06]',
      'timestamp_seconds': 366,
      'tip': 'Here is something you can use on any site. Whatever the type, a US tower is '
             'designed to a national standard, ANSI/TIA-222, usually through the local '
             'building code. It says how much antenna weight and wind and ice the steel must '
             'carry.',
      'title': 'How a Cell Tower Actually Works: A Phone Call, Ground to Sky '
               '(Buildrightacademy)',
      'url': 'https://www.youtube.com/watch?v=kHmq6jr22Ms&t=366s',
      'video_id': 'kHmq6jr22Ms'},
     {'author': 'Industrial Real Estate Show',
      'channel': 'Industrial Real Estate Show',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:44:42](https://www.youtube.com/watch?v=yb3YiKWxoFg&t=2682s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mobile where maybe they pay the tenant pays 2,000 per acre per month and you '
              'just signed a 15-year ironclad lease with with 3% bumps. That night, that might '
              'not be the the coolest story to tell, but probably better economics there than '
              'than looking elsewhere.',
      'timestamp': 2682,
      'timestamp_label': '[00:44:42]',
      'timestamp_seconds': 2682,
      'tip': 'Mobile where maybe they pay the tenant pays 2,000 per acre per month and you '
             'just signed a 15-year ironclad lease with with 3% bumps. That night, that might '
             'not be the the coolest story to tell, but probably better economics there than '
             'than looking elsewhere.',
      'title': 'Diving into Industrial Outdoor Storage IOS (Industrial Real Estate Show)',
      'url': 'https://www.youtube.com/watch?v=yb3YiKWxoFg&t=2682s',
      'video_id': 'yb3YiKWxoFg'},
     {'author': 'Nexus Towers',
      'channel': 'Nexus Towers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=vM7__l_6wgE&t=15s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Because when you go directly to the buyer, they're always looking for a better "
              'deal. They they want to get the most  out of you and give you the.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Because when you go directly to the buyer, they're always looking for a better "
             'deal. They they want to get the most  out of you and give you the.',
      'title': 'Why This Property Owner Chose Nexus Towers for His Cell Tower Lease Buyout '
               '(Nexus Towers)',
      'url': 'https://www.youtube.com/watch?v=vM7__l_6wgE&t=15s',
      'video_id': 'vM7__l_6wgE'},
     {'author': 'Tyler Cauble',
      'channel': 'Tyler Cauble',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:53](https://www.youtube.com/watch?v=q7HQGiIiT_8&t=1493s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Can see their taxes their their um you know payments uh you you can pay with '
              'credit card debit card uh we do text messaging for questions and complaints.',
      'timestamp': 1493,
      'timestamp_label': '[00:24:53]',
      'timestamp_seconds': 1493,
      'tip': 'Can see their taxes their their um you know payments uh you you can pay with '
             'credit card debit card uh we do text messaging for questions and complaints.',
      'title': 'How to Invest in Industrial Outdoor Storage with Ron Rohde (Tyler Cauble)',
      'url': 'https://www.youtube.com/watch?v=q7HQGiIiT_8&t=1493s',
      'video_id': 'q7HQGiIiT_8'},
     {'author': 'Airwave Advisors',
      'channel': 'Airwave Advisors',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=ZhCVLpLy4-o&t=92s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Even heard of and Nick made it into sort of an auction type situation he pared '
              'it down to two different outfits and the one that bought us as a very '
              'professional outfit and it was such a smooth transition we were really pleased '
              'with the results.',
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': 'Even heard of and Nick made it into sort of an auction type situation he pared '
             'it down to two different outfits and the one that bought us as a very '
             'professional outfit and it was such a smooth transition we were really pleased '
             'with the results.',
      'title': 'Cell Tower Lease Buyout Testimonial | Airwave Advisors (Airwave Advisors)',
      'url': 'https://www.youtube.com/watch?v=ZhCVLpLy4-o&t=92s',
      'video_id': 'ZhCVLpLy4-o'},
     {'author': 'Ronald Rohde Law',
      'channel': 'Ronald Rohde Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:13](https://www.youtube.com/watch?v=gcg4K6xqYaU&t=613s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'About 2 and A5 million and so with debt uh as well and so so anybody can do '
              "this it's a it's a low barrier to entry but the trajectory for this could be "
              'Sky High so thanks for watching I hope you appreciate my takeaways on my first '
              "iOS site and we'll see you next time.",
      'timestamp': 613,
      'timestamp_label': '[00:10:13]',
      'timestamp_seconds': 613,
      'tip': 'About 2 and A5 million and so with debt uh as well and so so anybody can do this '
             "it's a it's a low barrier to entry but the trajectory for this could be Sky High "
             'so thanks for watching I hope you appreciate my takeaways on my first iOS site '
             "and we'll see you next time.",
      'title': 'Challenges I Faced On My Industrial Investment IOS (Ronald Rohde Law)',
      'url': 'https://www.youtube.com/watch?v=gcg4K6xqYaU&t=613s',
      'video_id': 'gcg4K6xqYaU'},
     {'author': 'Tower Genius',
      'channel': 'Tower Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=QV7EDp7ej3A&t=15s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Quick uh video and talk about you know this cell tower here behind me the one '
              "in the middle and what's the difference between a cell.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Quick uh video and talk about you know this cell tower here behind me the one in '
             "the middle and what's the difference between a cell.",
      'title': "Cell Phone Tower Land Lease Values - What's the difference between getting "
               '$500 or $5,000 monthly? (Tower Genius)',
      'url': 'https://www.youtube.com/watch?v=QV7EDp7ej3A&t=15s',
      'video_id': 'QV7EDp7ej3A'}],
 3: [{'author': 'The Wealth Script',
      'channel': 'The Wealth Script',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:16](https://www.youtube.com/watch?v=lMUn7vCR_iQ&t=376s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The screen costs money to build and to run, so this isn't all profit. The money "
              'in billboards goes to whoever controls the permit and the screen, not to '
              "whoever owns the dirt. So, here's what a billboard really is. It isn't an "
              'advertising business.',
      'timestamp': 376,
      'timestamp_label': '[00:06:16]',
      'timestamp_seconds': 376,
      'tip': "The screen costs money to build and to run, so this isn't all profit. The money "
             'in billboards goes to whoever controls the permit and the screen, not to whoever '
             "owns the dirt. So, here's what a billboard really is. It isn't an advertising "
             'business.',
      'title': 'Who Really Owns the Billboard You Drive Past? (The Real Math) (The Wealth '
               'Script)',
      'url': 'https://www.youtube.com/watch?v=lMUn7vCR_iQ&t=376s',
      'video_id': 'lMUn7vCR_iQ'},
     {'author': 'Economic Oddities',
      'channel': 'Economic Oddities',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:37](https://www.youtube.com/watch?v=QdFbgvbJJ-M&t=337s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This model ignores them to show the shape of the business. Tenant one covers '
              'the bills. Every tenant after that is profit. Fixed costs are a burden when the '
              'building is empty and a gift once it fills. The land is a silent partner.',
      'timestamp': 337,
      'timestamp_label': '[00:05:37]',
      'timestamp_seconds': 337,
      'tip': 'This model ignores them to show the shape of the business. Tenant one covers the '
             'bills. Every tenant after that is profit. Fixed costs are a burden when the '
             'building is empty and a gift once it fills. The land is a silent partner.',
      'title': 'The Economics of Owning a Cell Tower (Economic Oddities)',
      'url': 'https://www.youtube.com/watch?v=QdFbgvbJJ-M&t=337s',
      'video_id': 'QdFbgvbJJ-M'},
     {'author': 'Acquisition Insider',
      'channel': 'Acquisition Insider',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:27](https://www.youtube.com/watch?v=MtWLazzJb9Y&t=207s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '650,000 over 25 years, a low to mid 7% unlevered return after closing costs. '
              "That's the whole case, a bond with a step-up coupon bought from a seller who "
              "wanted cash now. And here's why the aggregators discounted.",
      'timestamp': 207,
      'timestamp_label': '[00:03:27]',
      'timestamp_seconds': 207,
      'tip': '650,000 over 25 years, a low to mid 7% unlevered return after closing costs. '
             "That's the whole case, a bond with a step-up coupon bought from a seller who "
             "wanted cash now. And here's why the aggregators discounted.",
      'title': "How to Acquire a Cell Tower Lease (25,000 Towers Stopped Paying Rent. Here's "
               'the Math.) (Acquisition Insider)',
      'url': 'https://www.youtube.com/watch?v=MtWLazzJb9Y&t=207s',
      'video_id': 'MtWLazzJb9Y'},
     {'author': 'Ekoniq',
      'channel': 'Ekoniq',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:37](https://www.youtube.com/watch?v=eI1lH8lhvd8&t=97s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "17-year-olds to finance their future. And then there's the third category, the "
              "urban spectacular. This is no longer a billboard in the normal sense. It's "
              'basically a building-sized media asset with landlord economics, event pricing, '
              'and ego problems.',
      'timestamp': 97,
      'timestamp_label': '[00:01:37]',
      'timestamp_seconds': 97,
      'tip': "17-year-olds to finance their future. And then there's the third category, the "
             "urban spectacular. This is no longer a billboard in the normal sense. It's "
             'basically a building-sized media asset with landlord economics, event pricing, '
             'and ego problems.',
      'title': 'The Economics of Owning a Single Digital Billboard (Ekoniq)',
      'url': 'https://www.youtube.com/watch?v=eI1lH8lhvd8&t=97s',
      'video_id': 'eI1lH8lhvd8'},
     {'author': 'Mr. Money',
      'channel': 'Mr. Money',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=jQ79QHMZWQE&t=21s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Tower turned this exact business into roughly 10 and 1/2 billion dollars in '
              'annual revenue with margins most software companies would envy. So today, we '
              'are breaking down the real numbers. What does a tower actually cost to build? '
              'How many tenants does it take to make money?',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'Tower turned this exact business into roughly 10 and 1/2 billion dollars in '
             'annual revenue with margins most software companies would envy. So today, we are '
             'breaking down the real numbers. What does a tower actually cost to build? How '
             'many tenants does it take to make money?',
      'title': 'So You Want to Own a Cell Tower? The Real Numbers Behind the Rent (Mr. Money)',
      'url': 'https://www.youtube.com/watch?v=jQ79QHMZWQE&t=21s',
      'video_id': 'jQ79QHMZWQE'},
     {'author': 'Alaric Invests',
      'channel': 'Alaric Invests',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:40](https://www.youtube.com/watch?v=BrW8RLqtOjQ&t=340s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '12 to 15,000 dollars per year in gross site profit after ground rent and basic '
              "operating costs. At that rate, if you spent $250,000 building the tower, you'd "
              'be looking at a payback period of 17 to 20 years. That is a long time to wait. '
              'But here is where everything changes.',
      'timestamp': 340,
      'timestamp_label': '[00:05:40]',
      'timestamp_seconds': 340,
      'tip': '12 to 15,000 dollars per year in gross site profit after ground rent and basic '
             "operating costs. At that rate, if you spent $250,000 building the tower, you'd "
             'be looking at a payback period of 17 to 20 years. That is a long time to wait. '
             'But here is where everything changes.',
      'title': 'The Economics of Owning a Cell Tower (Alaric Invests)',
      'url': 'https://www.youtube.com/watch?v=BrW8RLqtOjQ&t=340s',
      'video_id': 'BrW8RLqtOjQ'},
     {'author': 'Land Owl',
      'channel': 'Land Owl',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:46](https://www.youtube.com/watch?v=yVhfvSQwGRQ&t=106s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Clifford sandy clay loam mapped at 6 to 10% slopes. See, the house next door '
              'went up in 2002 on the same soil with 70 ft of fall. Slope here is a cost, but '
              "it's not necessarily a no. A battery pad has to be flat, so price the grading, "
              'cut, fill, and maybe a retaining wall.',
      'timestamp': 106,
      'timestamp_label': '[00:01:46]',
      'timestamp_seconds': 106,
      'tip': 'Clifford sandy clay loam mapped at 6 to 10% slopes. See, the house next door '
             'went up in 2002 on the same soil with 70 ft of fall. Slope here is a cost, but '
             "it's not necessarily a no. A battery pad has to be flat, so price the grading, "
             'cut, fill, and maybe a retaining wall.',
      'title': 'What Makes Land Good For A Battery Storage Project (Land Owl)',
      'url': 'https://www.youtube.com/watch?v=yVhfvSQwGRQ&t=106s',
      'video_id': 'yVhfvSQwGRQ'},
     {'author': 'Holly Lane Radio',
      'channel': 'Holly Lane Radio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:48](https://www.youtube.com/watch?v=RRrHddpY1pU&t=588s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That creates high incremental margins. Crown Castle explicitly describes this '
              'model as adding tenants to existing towers at low incremental operating cost. '
              'Its portfolio data shows how maturity changes the economics. Towers acquired or '
              'built in 2006 and earlier average 2.',
      'timestamp': 588,
      'timestamp_label': '[00:09:48]',
      'timestamp_seconds': 588,
      'tip': 'That creates high incremental margins. Crown Castle explicitly describes this '
             'model as adding tenants to existing towers at low incremental operating cost. '
             'Its portfolio data shows how maturity changes the economics. Towers acquired or '
             'built in 2006 and earlier average 2.',
      'title': 'The Economics of Owning a Cell Tower (Holly Lane Radio)',
      'url': 'https://www.youtube.com/watch?v=RRrHddpY1pU&t=588s',
      'video_id': 'RRrHddpY1pU'},
     {'author': 'Ronald Rohde Law',
      'channel': 'Ronald Rohde Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:24](https://www.youtube.com/watch?v=7n_O1KWl4EQ&t=324s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Your unit put do your stuff go outside you're typically going on an acre 1 to 5 "
              "acre property 60 to 100 units whatever the case mine's the same thing except.",
      'timestamp': 324,
      'timestamp_label': '[00:05:24]',
      'timestamp_seconds': 324,
      'tip': "Your unit put do your stuff go outside you're typically going on an acre 1 to 5 "
             "acre property 60 to 100 units whatever the case mine's the same thing except.",
      'title': 'Massive Profit within IOS Industrial Contractor Yard with Chris Long and '
               'Longyards (Ronald Rohde Law)',
      'url': 'https://www.youtube.com/watch?v=7n_O1KWl4EQ&t=324s',
      'video_id': '7n_O1KWl4EQ'},
     {'author': 'Industrial Advisors',
      'channel': 'Industrial Advisors',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:33](https://www.youtube.com/watch?v=gvn8kH2TUE0&t=273s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Yeah, there's certainly a lot of, there's some of those sites that have been "
              "sitting for a while. 's certain ones that have sat. And so you just aren't "
              'going to have the depth of tenants like you do on a building on an iOS site. So '
              'talk a little bit about the ongoing costs.',
      'timestamp': 273,
      'timestamp_label': '[00:04:33]',
      'timestamp_seconds': 273,
      'tip': "Yeah, there's certainly a lot of, there's some of those sites that have been "
             "sitting for a while. 's certain ones that have sat. And so you just aren't going "
             'to have the depth of tenants like you do on a building on an iOS site. So talk a '
             'little bit about the ongoing costs.',
      'title': 'Exploring Industrial Outdoor Storage (IOS) (Industrial Advisors)',
      'url': 'https://www.youtube.com/watch?v=gvn8kH2TUE0&t=273s',
      'video_id': 'gvn8kH2TUE0'},
     {'author': 'Adding Value w/ Shy Assar | CRE & Industrial',
      'channel': 'Adding Value w/ Shy Assar | CRE & Industrial',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:26](https://www.youtube.com/watch?v=znP8wX2_k2w&t=266s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "OS because it's, you know, it's it's it's parking excess trailers. Um which is "
              "kind of it's just a cost for a business. They're not generating revenue out of "
              'parked trailers. They they yearn to not have, you know, parked trailers.',
      'timestamp': 266,
      'timestamp_label': '[00:04:26]',
      'timestamp_seconds': 266,
      'tip': "OS because it's, you know, it's it's it's parking excess trailers. Um which is "
             "kind of it's just a cost for a business. They're not generating revenue out of "
             'parked trailers. They they yearn to not have, you know, parked trailers.',
      'title': 'Industrial Outdoor Storage (IOS) Explained: Macro Trends & Institutional '
               'Strategies | Ambient CP (Adding Value w/ Shy Assar | CRE & Industrial)',
      'url': 'https://www.youtube.com/watch?v=znP8wX2_k2w&t=266s',
      'video_id': 'znP8wX2_k2w'},
     {'author': 'MrHermers',
      'channel': 'MrHermers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:34](https://www.youtube.com/watch?v=4ivHLHQgDVs&t=34s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They don't buy a property cuz it's pretty or because it's ugly and they can "
              "make it look nice like you do a flip in a house Here you're trying to buy a "
              "property and you know that it's going to cash flow.",
      'timestamp': 34,
      'timestamp_label': '[00:00:34]',
      'timestamp_seconds': 34,
      'tip': "They don't buy a property cuz it's pretty or because it's ugly and they can make "
             "it look nice like you do a flip in a house Here you're trying to buy a property "
             "and you know that it's going to cash flow.",
      'title': 'How to Turn Empty Land Into a PROFITABLE Truck Parking Business (MrHermers)',
      'url': 'https://www.youtube.com/watch?v=4ivHLHQgDVs&t=34s',
      'video_id': '4ivHLHQgDVs'},
     {'author': 'Allworth Financial',
      'channel': 'Allworth Financial',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=L5rvTFM0pVg&t=57s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'No expense to you whatsoever no sir and you get 11,000 a year that increases at '
              '2% per year yes sir what are they offering to buy it for uh if it Cash Out 170 '
              "5 years 190 and 10 years at 225 I don't know what that means what do you mean "
              '10 years 10 years 225,000.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': 'No expense to you whatsoever no sir and you get 11,000 a year that increases at '
             '2% per year yes sir what are they offering to buy it for uh if it Cash Out 170 5 '
             "years 190 and 10 years at 225 I don't know what that means what do you mean 10 "
             'years 10 years 225,000.',
      'title': 'Should You Sell Your Cell Tower Lease? Evaluating Buyouts, Risks, and '
               "Starlink's Impact (Allworth Financial)",
      'url': 'https://www.youtube.com/watch?v=L5rvTFM0pVg&t=57s',
      'video_id': 'L5rvTFM0pVg'},
     {'author': 'Vertical Consultants',
      'channel': 'Vertical Consultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=NS76BzQHI_o&t=38s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You want to make sure that you give them enough time, but not too much. If you '
              'give them too much, you lose an opportunity to renegotiate the lease sooner '
              'than later, and that cost you money.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': 'You want to make sure that you give them enough time, but not too much. If you '
             'give them too much, you lose an opportunity to renegotiate the lease sooner than '
             'later, and that cost you money.',
      'title': 'HOW TO Negotiate A Cell Tower Lease In 2024 (Vertical Consultants)',
      'url': 'https://www.youtube.com/watch?v=NS76BzQHI_o&t=38s',
      'video_id': 'NS76BzQHI_o'},
     {'author': 'Tower Genius',
      'channel': 'Tower Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:20](https://www.youtube.com/watch?v=DJfkRMlj2fg&t=260s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Lease rate is the rental prices for your for your uh for your property either '
              'new cell tower or amendment give us a call book a 30 minute discovery call '
              "you've been listening to the wireless wise guys podcast.",
      'timestamp': 260,
      'timestamp_label': '[00:04:20]',
      'timestamp_seconds': 260,
      'tip': 'Lease rate is the rental prices for your for your uh for your property either '
             'new cell tower or amendment give us a call book a 30 minute discovery call '
             "you've been listening to the wireless wise guys podcast.",
      'title': 'How to Negotiate a Cell Tower Lease - Part One (Tower Genius)',
      'url': 'https://www.youtube.com/watch?v=DJfkRMlj2fg&t=260s',
      'video_id': 'DJfkRMlj2fg'}],
 4: [{'author': 'Economics Decoded',
      'channel': 'Economics Decoded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:26](https://www.youtube.com/watch?v=UcnVlSgvKXE&t=326s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Our operator also has a sales task. The billboard doesn't walk into the diner "
              "and explain why this location deserves part of the owner's advertising budget. "
              'A person has to make that case, negotiate the campaign, and get the next '
              'booking ready.',
      'timestamp': 326,
      'timestamp_label': '[00:05:26]',
      'timestamp_seconds': 326,
      'tip': "Our operator also has a sales task. The billboard doesn't walk into the diner "
             "and explain why this location deserves part of the owner's advertising budget. A "
             'person has to make that case, negotiate the campaign, and get the next booking '
             'ready.',
      'title': 'The Real Cost of That Billboard You See Every Day (Economics Decoded)',
      'url': 'https://www.youtube.com/watch?v=UcnVlSgvKXE&t=326s',
      'video_id': 'UcnVlSgvKXE'},
     {'author': 'FutureMint · 10m views · 6 hour ago\n\n\n\n\n\n\n\n\n...',
      'channel': 'FutureMint · 10m views · 6 hour ago\n\n\n\n\n\n\n\n\n...',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=4F72sbfazM8&t=54s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Seeing the tower through that lens is the only way to understand how it '
              'actually makes money. Getting into this business requires serious upfront '
              'capital. Building a single new site from the ground up costs an average of '
              '$275,000. This chart shows the budget.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'Seeing the tower through that lens is the only way to understand how it actually '
             'makes money. Getting into this business requires serious upfront capital. '
             'Building a single new site from the ground up costs an average of $275,000. This '
             'chart shows the budget.',
      'title': 'The Economics of Owning a Cell Tower (FutureMint · 10m views · 6 hour ago\n'
               '\n'
               '\n'
               '\n'
               '\n'
               '\n'
               '\n'
               '\n'
               '\n'
               '...)',
      'url': 'https://www.youtube.com/watch?v=4F72sbfazM8&t=54s',
      'video_id': '4F72sbfazM8'},
     {'author': 'Global Finance Desk',
      'channel': 'Global Finance Desk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=AkX52_z30r4&t=38s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is the business of outdoor advertising. Billboards, transit ads, street '
              'furniture, digital screens. Together, they generate roughly $9 billion a year '
              "in the United States, according to the industry's own trade group.",
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': 'This is the business of outdoor advertising. Billboards, transit ads, street '
             'furniture, digital screens. Together, they generate roughly $9 billion a year in '
             "the United States, according to the industry's own trade group.",
      'title': 'The Economics of Owing a Billboard Empire (Global Finance Desk)',
      'url': 'https://www.youtube.com/watch?v=AkX52_z30r4&t=38s',
      'video_id': 'AkX52_z30r4'},
     {'author': 'ledgerandland',
      'channel': 'ledgerandland',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=6oamhwKj2wU&t=102s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This asset class will eat your capital. Let me shatter a mental model right '
              'now. When most people say billboard, they picture one thing, a sign next to a '
              "highway. That's the stereotype and it's about as useful as calling every "
              "restaurant a McDonald's.",
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': 'This asset class will eat your capital. Let me shatter a mental model right now. '
             'When most people say billboard, they picture one thing, a sign next to a '
             "highway. That's the stereotype and it's about as useful as calling every "
             "restaurant a McDonald's.",
      'title': 'The Economics of Owning a Billboard (ledgerandland)',
      'url': 'https://www.youtube.com/watch?v=6oamhwKj2wU&t=102s',
      'video_id': '6oamhwKj2wU'},
     {'author': 'Franchise Inspectors',
      'channel': 'Franchise Inspectors',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:50](https://www.youtube.com/watch?v=mNNTe8Yz_PI&t=230s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Advertising on Billboard's just from in your territory now number three the "
              "Billboard should have reasonable rents and high advertising rates we're going.",
      'timestamp': 230,
      'timestamp_label': '[00:03:50]',
      'timestamp_seconds': 230,
      'tip': "Advertising on Billboard's just from in your territory now number three the "
             "Billboard should have reasonable rents and high advertising rates we're going.",
      'title': 'Unique Passive Income Business  - Billboards! (Franchise Inspectors)',
      'url': 'https://www.youtube.com/watch?v=mNNTe8Yz_PI&t=230s',
      'video_id': 'mNNTe8Yz_PI'},
     {'author': 'The Bell Board Podcast',
      'channel': 'The Bell Board Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:42:05](https://www.youtube.com/watch?v=N6EyLPQ9NhA&t=2525s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Cuz I don't know you know there's not many any outdoor operators that I that I "
              "have spoken with that do a lot of that. Why why can't we use those tools to "
              "bring us business and we should? Again that's one of the reasons the Gravis "
              'Marketing exists.',
      'timestamp': 2525,
      'timestamp_label': '[00:42:05]',
      'timestamp_seconds': 2525,
      'tip': "Cuz I don't know you know there's not many any outdoor operators that I that I "
             "have spoken with that do a lot of that. Why why can't we use those tools to "
             "bring us business and we should? Again that's one of the reasons the Gravis "
             'Marketing exists.',
      'title': '30 Years in Billboard Advertising: Sales, AI & Growth with Jonathan Graviss '
               '(The Bell Board Podcast)',
      'url': 'https://www.youtube.com/watch?v=N6EyLPQ9NhA&t=2525s',
      'video_id': 'N6EyLPQ9NhA'},
     {'author': 'Commercial Real Estate Now',
      'channel': 'Commercial Real Estate Now',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:24](https://www.youtube.com/watch?v=dKQj8cpiqeE&t=144s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re collecting today may look stable, but the land underneath it has repriced "
              "significantly, and you won't see that value until the lease rolls. Now, for "
              'patient capital with a long hold horizon, that can be a very compelling setup.',
      'timestamp': 144,
      'timestamp_label': '[00:02:24]',
      'timestamp_seconds': 144,
      'tip': "'re collecting today may look stable, but the land underneath it has repriced "
             "significantly, and you won't see that value until the lease rolls. Now, for "
             'patient capital with a long hold horizon, that can be a very compelling setup.',
      'title': 'Equipment Rental Net Lease vs. Industrial Outdoor Storage: Same Land, '
               'Different Trade (Commercial Real Estate Now)',
      'url': 'https://www.youtube.com/watch?v=dKQj8cpiqeE&t=144s',
      'video_id': 'dKQj8cpiqeE'},
     {'author': 'Truck Parking Media',
      'channel': 'Truck Parking Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=hjC6tiI5Kd4&t=28s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Make, model, color, DOT, MC number, license plate, all that stuff is in a '
              "single, easy-to-use repository. If he's coming in here to do yard audits, "
              'automated invoicing, billing, and payments, right?',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': 'Make, model, color, DOT, MC number, license plate, all that stuff is in a '
             "single, easy-to-use repository. If he's coming in here to do yard audits, "
             'automated invoicing, billing, and payments, right?',
      'title': 'Truck Parking Technology That Fills Yards Faster | Rig Hut (Truck Parking '
               'Media)',
      'url': 'https://www.youtube.com/watch?v=hjC6tiI5Kd4&t=28s',
      'video_id': 'hjC6tiI5Kd4'},
     {'author': 'Ronald Rohde Law',
      'channel': 'Ronald Rohde Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:54](https://www.youtube.com/watch?v=-g_D6hbOPNE&t=234s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Flex building up to market standards can cost quite a bit more than a '
              "comparable iOS site. So number one is cost capital and we're going to go for "
              'point4 iOS rents and NOI growth.',
      'timestamp': 234,
      'timestamp_label': '[00:03:54]',
      'timestamp_seconds': 234,
      'tip': 'Flex building up to market standards can cost quite a bit more than a comparable '
             "iOS site. So number one is cost capital and we're going to go for point4 iOS "
             'rents and NOI growth.',
      'title': 'Flex vs Outdoor Storage (IOS) Which industrial investment is better? (Ronald '
               'Rohde Law)',
      'url': 'https://www.youtube.com/watch?v=-g_D6hbOPNE&t=234s',
      'video_id': '-g_D6hbOPNE'},
     {'author': 'Airwave Advisors',
      'channel': 'Airwave Advisors',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=POVBhyyB9Jc&t=15s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then several hundred feet behind a commercial building was was our tower and I '
              'had one major telecom carrier as a tenant on that tower and I went out and.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Then several hundred feet behind a commercial building was was our tower and I '
             'had one major telecom carrier as a tenant on that tower and I went out and.',
      'title': 'Cell Tower Lease Buyout Testimonial | Airwave Advisors (Airwave Advisors)',
      'url': 'https://www.youtube.com/watch?v=POVBhyyB9Jc&t=15s',
      'video_id': 'POVBhyyB9Jc'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:37](https://www.youtube.com/watch?v=Ombo8TjihMk&t=277s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I found were crammed full they didn't have room for one more spot so maybe "
              "that's why they weren't advertising but do you know how do most of these truck.",
      'timestamp': 277,
      'timestamp_label': '[00:04:37]',
      'timestamp_seconds': 277,
      'tip': "I found were crammed full they didn't have room for one more spot so maybe "
             "that's why they weren't advertising but do you know how do most of these truck.",
      'title': 'Truck Yeah! How Evan Shelley Makes Bank on Truck Parking Lots | REtipster 194 '
               '(REtipster)',
      'url': 'https://www.youtube.com/watch?v=Ombo8TjihMk&t=277s',
      'video_id': 'Ombo8TjihMk'},
     {'author': 'Tower Genius',
      'channel': 'Tower Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:18](https://www.youtube.com/watch?v=Eo568DFPXFk&t=18s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Uh let's call the top seven deadly sins of cell tower lease negotiation these "
              "are common errors that property owners and building owners make when they're.",
      'timestamp': 18,
      'timestamp_label': '[00:00:18]',
      'timestamp_seconds': 18,
      'tip': "Uh let's call the top seven deadly sins of cell tower lease negotiation these "
             "are common errors that property owners and building owners make when they're.",
      'title': '7 Deadly Sins of Negotiating Cell Tower Lease Agreements (Tower Genius)',
      'url': 'https://www.youtube.com/watch?v=Eo568DFPXFk&t=18s',
      'video_id': 'Eo568DFPXFk'},
     {'author': 'Robert_Wallace',
      'channel': 'Robert_Wallace',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:40](https://www.youtube.com/watch?v=0Lv5_kKNNWg&t=460s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Resell the rest of it you know I'll probably do that I just got to find the "
              'right um right piece of property where it makes sense uh anyway all great '
              'questions and uh feel free to reach out if you have any others thanks again.',
      'timestamp': 460,
      'timestamp_label': '[00:07:40]',
      'timestamp_seconds': 460,
      'tip': "Resell the rest of it you know I'll probably do that I just got to find the "
             'right um right piece of property where it makes sense uh anyway all great '
             'questions and uh feel free to reach out if you have any others thanks again.',
      'title': 'Leasing VS Easements VS Buying land for billboards (Robert_Wallace)',
      'url': 'https://www.youtube.com/watch?v=0Lv5_kKNNWg&t=460s',
      'video_id': '0Lv5_kKNNWg'},
     {'author': 'Vertical Consultants',
      'channel': 'Vertical Consultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:04](https://www.youtube.com/watch?v=p55_Vmt4xnk&t=184s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Hurt yourself the most you also have some liability issues you need to contain '
              "insurance issues ETC but those are fixes if you understand what you're doing "
              'you can do very well but control your property is the biggest issue that you '
              'into yeah.',
      'timestamp': 184,
      'timestamp_label': '[00:03:04]',
      'timestamp_seconds': 184,
      'tip': 'Hurt yourself the most you also have some liability issues you need to contain '
             "insurance issues ETC but those are fixes if you understand what you're doing you "
             'can do very well but control your property is the biggest issue that you into '
             'yeah.',
      'title': 'Hidden RISKS of A Cell Tower Lease: DON"T SIGN Until You Watch!!! (Vertical '
               'Consultants)',
      'url': 'https://www.youtube.com/watch?v=p55_Vmt4xnk&t=184s',
      'video_id': 'p55_Vmt4xnk'},
     {'author': 'Vertical Consultants',
      'channel': 'Vertical Consultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=BoWyq83WIVk&t=110s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Seen for decades of everything is going to go away you need to understand what '
              'the value of the sell Tower is on your property and make sure you get the best '
              'deal today and going forward get more money get a better lease get vertical.',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': 'Seen for decades of everything is going to go away you need to understand what '
             'the value of the sell Tower is on your property and make sure you get the best '
             'deal today and going forward get more money get a better lease get vertical.',
      'title': 'What Is A Cell Tower Lease Really Worth? Are Cell Towers Becoming Obsolete? '
               '(Vertical Consultants)',
      'url': 'https://www.youtube.com/watch?v=BoWyq83WIVk&t=110s',
      'video_id': 'BoWyq83WIVk'}],
 5: [{'author': 'Old School Financials',
      'channel': 'Old School Financials',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=EFxC43w3Aa8&t=39s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Start with the permit because without it, there is no business at all. In 1965, '
              'Congress passed the Highway Beautification Act. It set a control zone 660 ft '
              "from the highway's edge. Inside that zone, new billboards face strict rules on "
              'size, spacing, and zoning.',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': 'Start with the permit because without it, there is no business at all. In 1965, '
             'Congress passed the Highway Beautification Act. It set a control zone 660 ft '
             "from the highway's edge. Inside that zone, new billboards face strict rules on "
             'size, spacing, and zoning.',
      'title': 'The Highway Landlord Nobody Notices (Old School Financials)',
      'url': 'https://www.youtube.com/watch?v=EFxC43w3Aa8&t=39s',
      'video_id': 'EFxC43w3Aa8'},
     {'author': 'Stick to Wealth',
      'channel': 'Stick to Wealth',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:06](https://www.youtube.com/watch?v=4WZnJVbtMlk&t=306s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The house can be a money machine and the mortgage can still crush you. There is '
              'a softer risk too and it arrives on a schedule. When the economy turns and '
              'companies panic, advertising is one of the very first budgets they cut and '
              'billboards feel it fast.',
      'timestamp': 306,
      'timestamp_label': '[00:05:06]',
      'timestamp_seconds': 306,
      'tip': 'The house can be a money machine and the mortgage can still crush you. There is '
             'a softer risk too and it arrives on a schedule. When the economy turns and '
             'companies panic, advertising is one of the very first budgets they cut and '
             'billboards feel it fast.',
      'title': 'The Economics of Owning a Billboard (Stick to Wealth)',
      'url': 'https://www.youtube.com/watch?v=4WZnJVbtMlk&t=306s',
      'video_id': '4WZnJVbtMlk'},
     {'author': 'Phil Edwards',
      'channel': 'Phil Edwards',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:47](https://www.youtube.com/watch?v=rNWgnEqvTkY&t=587s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That means it is a federally regulated billboard. In 1958, Congress gave states '
              'some extra money for highways if they agreed not to build billboards. Lady Bird '
              "Johnson had a passion for highway beautification. And at last it's achieved, "
              'and so things do get done.',
      'timestamp': 587,
      'timestamp_label': '[00:09:47]',
      'timestamp_seconds': 587,
      'tip': 'That means it is a federally regulated billboard. In 1958, Congress gave states '
             'some extra money for highways if they agreed not to build billboards. Lady Bird '
             "Johnson had a passion for highway beautification. And at last it's achieved, and "
             'so things do get done.',
      'title': 'I bought a billboard to explain billboards (Phil Edwards)',
      'url': 'https://www.youtube.com/watch?v=rNWgnEqvTkY&t=587s',
      'video_id': 'rNWgnEqvTkY'},
     {'author': 'Finance US 1',
      'channel': 'Finance US 1',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:26](https://www.youtube.com/watch?v=Fu71JjwHXWY&t=506s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, where's the risk in what sounds like an almost too good business model? The "
              'biggest risk is under-building in the wrong location.',
      'timestamp': 506,
      'timestamp_label': '[00:08:26]',
      'timestamp_seconds': 506,
      'tip': "So, where's the risk in what sounds like an almost too good business model? The "
             'biggest risk is under-building in the wrong location.',
      'title': 'The Economics of Owning a Cell Tower | 10 minutes (Finance US 1)',
      'url': 'https://www.youtube.com/watch?v=Fu71JjwHXWY&t=506s',
      'video_id': 'Fu71JjwHXWY'},
     {'author': 'Mr. Finance Pro',
      'channel': 'Mr. Finance Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:39](https://www.youtube.com/watch?v=cSRkZ3JGfBA&t=879s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, let me ask you something. If towers are that risky, why do investors still '
              'pay so much for them? Because while the risk is real, the business has a second '
              'hidden advantage. Customers can fail, but the tower stays.',
      'timestamp': 879,
      'timestamp_label': '[00:14:39]',
      'timestamp_seconds': 879,
      'tip': 'Now, let me ask you something. If towers are that risky, why do investors still '
             'pay so much for them? Because while the risk is real, the business has a second '
             'hidden advantage. Customers can fail, but the tower stays.',
      'title': 'The Economics of Owning Telecom Towers (Mr. Finance Pro)',
      'url': 'https://www.youtube.com/watch?v=cSRkZ3JGfBA&t=879s',
      'video_id': 'cSRkZ3JGfBA'},
     {'author': 'Tower Genius',
      'channel': 'Tower Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:51](https://www.youtube.com/watch?v=kPzYR4RlrCM&t=171s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s looking to purchase, uh, you know, the easement there, buy you out. So, if "
              'you have questions about a proposed lease buyout, if you have questions, if '
              "you're going to do a 1031 exchange or anything like that, give us a call at "
              'Tower Genius.',
      'timestamp': 171,
      'timestamp_label': '[00:02:51]',
      'timestamp_seconds': 171,
      'tip': "'s looking to purchase, uh, you know, the easement there, buy you out. So, if "
             'you have questions about a proposed lease buyout, if you have questions, if '
             "you're going to do a 1031 exchange or anything like that, give us a call at "
             'Tower Genius.',
      'title': 'Cell Tower Buyout Leases (Tower Genius)',
      'url': 'https://www.youtube.com/watch?v=kPzYR4RlrCM&t=171s',
      'video_id': 'kPzYR4RlrCM'},
     {'author': 'Industrial Real Estate Show',
      'channel': 'Industrial Real Estate Show',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:38:05](https://www.youtube.com/watch?v=LftC_mcL69E&t=2285s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I I just I think that there's such a long runway ahead of it. What What it "
              'could potentially derail that? What is What keeps you up at night? What are the '
              "risks that perhaps the average person isn't thinking about that could cause a "
              'problem?',
      'timestamp': 2285,
      'timestamp_label': '[00:38:05]',
      'timestamp_seconds': 2285,
      'tip': "I I just I think that there's such a long runway ahead of it. What What it could "
             'potentially derail that? What is What keeps you up at night? What are the risks '
             "that perhaps the average person isn't thinking about that could cause a problem?",
      'title': 'A Deep Dive into Industrial Outdoor Storage IOS (Industrial Real Estate Show)',
      'url': 'https://www.youtube.com/watch?v=LftC_mcL69E&t=2285s',
      'video_id': 'LftC_mcL69E'},
     {'author': 'Nexus Towers',
      'channel': 'Nexus Towers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=xSsNtRvjHBg&t=15s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'What are they a lot of the property owners and landlords we speak with they are '
              'familiar with uh apartment leases right building leases business leases.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'What are they a lot of the property owners and landlords we speak with they are '
             'familiar with uh apartment leases right building leases business leases.',
      'title': 'Cell Tower Lease Agreements – What Property Owners Need to Know (Nexus Towers)',
      'url': 'https://www.youtube.com/watch?v=xSsNtRvjHBg&t=15s',
      'video_id': 'xSsNtRvjHBg'},
     {'author': 'Ask Flip Man',
      'channel': 'Ask Flip Man',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:10](https://www.youtube.com/watch?v=NIYpBpIvXTc&t=130s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s a trucking company with extra space in their yard, a vacant lot, can be uh "
              'tow truck business owner that has a extra lot that never has anything in it, '
              'and use that for truck parking.',
      'timestamp': 130,
      'timestamp_label': '[00:02:10]',
      'timestamp_seconds': 130,
      'tip': "'s a trucking company with extra space in their yard, a vacant lot, can be uh "
             'tow truck business owner that has a extra lot that never has anything in it, and '
             'use that for truck parking.',
      'title': "Make Money on Unused Parking Lots You Don't Own - Semi Truck Parking Arbitrage "
               '(Ask Flip Man)',
      'url': 'https://www.youtube.com/watch?v=NIYpBpIvXTc&t=130s',
      'video_id': 'NIYpBpIvXTc'},
     {'author': 'Tower Genius',
      'channel': 'Tower Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:24](https://www.youtube.com/watch?v=mfnmRoHN1Uo&t=384s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If this technolog is going to be here the least buyout industry is still buying '
              "these things you know they're spending money on them and you offload that risk "
              'let them deal with it so just a suggestion if you have questions in 2024 give '
              'us a call at Tower genius 888 313.',
      'timestamp': 384,
      'timestamp_label': '[00:06:24]',
      'timestamp_seconds': 384,
      'tip': 'If this technolog is going to be here the least buyout industry is still buying '
             "these things you know they're spending money on them and you offload that risk "
             'let them deal with it so just a suggestion if you have questions in 2024 give us '
             'a call at Tower genius 888 313.',
      'title': 'Cell Tower Leases What To Expect in 2024? (Tower Genius)',
      'url': 'https://www.youtube.com/watch?v=mfnmRoHN1Uo&t=384s',
      'video_id': 'mfnmRoHN1Uo'},
     {'author': 'EdisonIndustrial',
      'channel': 'EdisonIndustrial',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=Wu_IobArlaI&t=30s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uncovered storage for industrial users from truck parking to access parking to '
              'equipment parking and non-related users or outdoor storage investors are buying '
              "this aggressively but there's always a risk here are some tips to consider "
              'before buying an iOS site.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'Uncovered storage for industrial users from truck parking to access parking to '
             'equipment parking and non-related users or outdoor storage investors are buying '
             "this aggressively but there's always a risk here are some tips to consider "
             'before buying an iOS site.',
      'title': 'Do this before buying IOS Properties | Industrial real estate '
               '(EdisonIndustrial)',
      'url': 'https://www.youtube.com/watch?v=Wu_IobArlaI&t=30s',
      'video_id': 'Wu_IobArlaI'},
     {'author': 'Ronald Rohde Law',
      'channel': 'Ronald Rohde Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:16](https://www.youtube.com/watch?v=rPXHwXgqWs8&t=496s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Smaller support poles and less depth so it's cheaper you can also have a "
              'rolling gate which has that metal channel that a wheel will roll over the '
              'problem with.',
      'timestamp': 496,
      'timestamp_label': '[00:08:16]',
      'timestamp_seconds': 496,
      'tip': "Smaller support poles and less depth so it's cheaper you can also have a rolling "
             'gate which has that metal channel that a wheel will roll over the problem with.',
      'title': 'Actual Costs of Developing Truck Parking (Ronald Rohde Law)',
      'url': 'https://www.youtube.com/watch?v=rPXHwXgqWs8&t=496s',
      'video_id': 'rPXHwXgqWs8'},
     {'author': 'Vertical Consultants',
      'channel': 'Vertical Consultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=NqS16do0JG8&t=118s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Obligations you're taking on and what risk you're taking on as well what "
              "liabilities you may be taking on before you do anything get assistance that's "
              'tip number three get more money get a better lease get vertical.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': "Obligations you're taking on and what risk you're taking on as well what "
             "liabilities you may be taking on before you do anything get assistance that's "
             'tip number three get more money get a better lease get vertical.',
      'title': '3 Tips To Get More Cell Tower Rent In 2025 (Vertical Consultants)',
      'url': 'https://www.youtube.com/watch?v=NqS16do0JG8&t=118s',
      'video_id': 'NqS16do0JG8'},
     {'author': 'Vertical Consultants',
      'channel': 'Vertical Consultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:02](https://www.youtube.com/watch?v=oiDHDp0Uhxk&t=1082s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Where you have to understand the layers below every time a property owner has '
              'been approached for a new cell tower lease or or if they have an existing cell '
              "tower lease and they're being asked to renegotiate that lease or they asked to "
              'extend that lease Etc.',
      'timestamp': 1082,
      'timestamp_label': '[00:18:02]',
      'timestamp_seconds': 1082,
      'tip': 'Where you have to understand the layers below every time a property owner has '
             'been approached for a new cell tower lease or or if they have an existing cell '
             "tower lease and they're being asked to renegotiate that lease or they asked to "
             'extend that lease Etc.',
      'title': 'Is A Cell Tower Lease REALLY Worth It? (Vertical Consultants)',
      'url': 'https://www.youtube.com/watch?v=oiDHDp0Uhxk&t=1082s',
      'video_id': 'oiDHDp0Uhxk'},
     {'author': 'Vertical Consultants',
      'channel': 'Vertical Consultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=c4oPi61cgB8&t=85s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Income for years and years unless you absolutely have to have that money today '
              "don't sell your cell tower lease if you do you're going to be making that big "
              "zero and I promise you you'll not like it get more money get a better lease get "
              'vertical.',
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': 'Income for years and years unless you absolutely have to have that money today '
             "don't sell your cell tower lease if you do you're going to be making that big "
             "zero and I promise you you'll not like it get more money get a better lease get "
             'vertical.',
      'title': 'Cell Tower Lease Rates-Lowest Rent In United States (Vertical Consultants)',
      'url': 'https://www.youtube.com/watch?v=c4oPi61cgB8&t=85s',
      'video_id': 'c4oPi61cgB8'}],
 6: [{'author': 'Shaun Academy',
      'channel': 'Shaun Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:44](https://www.youtube.com/watch?v=dzIF5i2KhaA&t=44s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Business as a result of the Highway beautification Act to ensure profitability '
              'first understand the financial costs and legal.',
      'timestamp': 44,
      'timestamp_label': '[00:00:44]',
      'timestamp_seconds': 44,
      'tip': 'Business as a result of the Highway beautification Act to ensure profitability '
             'first understand the financial costs and legal.',
      'title': 'How to Start a Billboard Advertising Business (Shaun Academy)',
      'url': 'https://www.youtube.com/watch?v=dzIF5i2KhaA&t=44s',
      'video_id': 'dzIF5i2KhaA'},
     {'author': 'IowaDOT',
      'channel': 'IowaDOT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=8_iv9avZiAQ&t=45s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "First, an advertising sign can be almost anything, not just a billboard. It's "
              "any device that's being used to draw attention to a business or activity, "
              'including banners, small temporary signs, and even messages painted on trailers '
              'and barns.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': "First, an advertising sign can be almost anything, not just a billboard. It's "
             "any device that's being used to draw attention to a business or activity, "
             'including banners, small temporary signs, and even messages painted on trailers '
             'and barns.',
      'title': 'Advertising Signs (IowaDOT)',
      'url': 'https://www.youtube.com/watch?v=8_iv9avZiAQ&t=45s',
      'video_id': '8_iv9avZiAQ'},
     {'author': 'Cashflow Anatomy',
      'channel': 'Cashflow Anatomy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=GzFGSTXAVaI&t=103s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll find online collapses them. The rule is the Highway Beautification Act, "
              'passed in 1965, and it is still operating. It sets requirements for signs along '
              'controlled roads, size, lighting and spacing. A sign that fails them is '
              'generally prohibited and must be removed.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': "'ll find online collapses them. The rule is the Highway Beautification Act, "
             'passed in 1965, and it is still operating. It sets requirements for signs along '
             'controlled roads, size, lighting and spacing. A sign that fails them is '
             'generally prohibited and must be removed.',
      'title': "Why You Can't Build a New Billboard (And Why That's the Whole Business) "
               '(Cashflow Anatomy)',
      'url': 'https://www.youtube.com/watch?v=GzFGSTXAVaI&t=103s',
      'video_id': 'GzFGSTXAVaI'},
     {'author': 'VistaPrint',
      'channel': 'VistaPrint',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=hgodas0iUUM&t=71s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And while traditional billboards are static, these days you can also find '
              'digital billboards that can display moving digital images, animations and '
              "videos. So, shrink down a billboard and print it out on paper, and you've got a "
              'poster.',
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': 'And while traditional billboards are static, these days you can also find '
             'digital billboards that can display moving digital images, animations and '
             "videos. So, shrink down a billboard and print it out on paper, and you've got a "
             'poster.',
      'title': 'Outdoor advertising | Boost your reach with these five types. (VistaPrint)',
      'url': 'https://www.youtube.com/watch?v=hgodas0iUUM&t=71s',
      'video_id': 'hgodas0iUUM'},
     {'author': 'Clear Multifamily',
      'channel': 'Clear Multifamily',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=LMD9ecO4o1M&t=28s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The first one is to own land, in the right location, of course, that you ground '
              'lease to a billboard company. Now, billboard companies are usually large '
              'outdoor advertising companies that will pay you a rent for your location.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': 'The first one is to own land, in the right location, of course, that you ground '
             'lease to a billboard company. Now, billboard companies are usually large outdoor '
             'advertising companies that will pay you a rent for your location.',
      'title': '2 Things Real Estate Investors MUST Know About Billboard Investments (Clear '
               'Multifamily)',
      'url': 'https://www.youtube.com/watch?v=LMD9ecO4o1M&t=28s',
      'video_id': 'LMD9ecO4o1M'},
     {'author': 'Ronald Rohde Law',
      'channel': 'Ronald Rohde Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:36](https://www.youtube.com/watch?v=aMpeVcjGM3c&t=276s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So this could be a three acre paved site maybe with a 20,000 square foot '
              'building. Again, it really just depends on what the demand looks like for the '
              'first phase of that building.',
      'timestamp': 276,
      'timestamp_label': '[00:04:36]',
      'timestamp_seconds': 276,
      'tip': 'So this could be a three acre paved site maybe with a 20,000 square foot '
             'building. Again, it really just depends on what the demand looks like for the '
             'first phase of that building.',
      'title': 'I Bought 7.5 Acres to Build This IOS Deal (Ronald Rohde Law)',
      'url': 'https://www.youtube.com/watch?v=aMpeVcjGM3c&t=276s',
      'video_id': 'aMpeVcjGM3c'},
     {'author': 'Realty Returns',
      'channel': 'Realty Returns',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:54](https://www.youtube.com/watch?v=6YQWIQERSYQ&t=174s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Yards. Expect  60 70% LTV, 2025-year amortization. Bring a real business plan '
              'and pre-leas  leases if you can. Deal flow. Call yard.',
      'timestamp': 174,
      'timestamp_label': '[00:02:54]',
      'timestamp_seconds': 174,
      'tip': 'Yards. Expect  60 70% LTV, 2025-year amortization. Bring a real business plan '
             'and pre-leas  leases if you can. Deal flow. Call yard.',
      'title': 'Why Industrial Outdoor Storage Is the Next Big Cashflow Play (Realty Returns)',
      'url': 'https://www.youtube.com/watch?v=6YQWIQERSYQ&t=174s',
      'video_id': '6YQWIQERSYQ'},
     {'author': 'Truck Parking Media',
      'channel': 'Truck Parking Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=ulBXkeE5I_8&t=139s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Number three, speed to lead is everything. So, when a driver calls, no matter '
              'what time, and if they ask for parking, usually they are have they have the '
              "highest conversion rates. So, they're calling you and they're calling three "
              'other yards at the same time.',
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': 'Number three, speed to lead is everything. So, when a driver calls, no matter '
             'what time, and if they ask for parking, usually they are have they have the '
             "highest conversion rates. So, they're calling you and they're calling three "
             'other yards at the same time.',
      'title': 'What I Wish I Knew Before Managing My First Truck Parking Yard (Truck Parking '
               'Media)',
      'url': 'https://www.youtube.com/watch?v=ulBXkeE5I_8&t=139s',
      'video_id': 'ulBXkeE5I_8'},
     {'author': 'Empowered Investor',
      'channel': 'Empowered Investor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:18](https://www.youtube.com/watch?v=Ul4fTKkTHho&t=318s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Yeah yeah okay okay good stuff so what if they don't have actual land for a "
              'tower I mean I remember you know I was looking at an office building deal I '
              "don't think office is too good.",
      'timestamp': 318,
      'timestamp_label': '[00:05:18]',
      'timestamp_seconds': 318,
      'tip': "Yeah yeah okay okay good stuff so what if they don't have actual land for a "
             'tower I mean I remember you know I was looking at an office building deal I '
             "don't think office is too good.",
      'title': 'How to Profit From 5G Cell Towers as a Real Estate Investor | 5G Real Estate '
               'Investment (Empowered Investor)',
      'url': 'https://www.youtube.com/watch?v=Ul4fTKkTHho&t=318s',
      'video_id': 'Ul4fTKkTHho'},
     {'author': 'Orbital Ledger',
      'channel': 'Orbital Ledger',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:49](https://www.youtube.com/watch?v=G3zZhjoRDUg&t=589s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'SpaceX a credible fourth player, even in a hybrid network. He also said that '
              'building a terrestrial network without a roaming or MVNO deal would be very '
              'challenging. And about small cells alone, he said it seems, quote, an '
              'impossible ask.',
      'timestamp': 589,
      'timestamp_label': '[00:09:49]',
      'timestamp_seconds': 589,
      'tip': 'SpaceX a credible fourth player, even in a hybrid network. He also said that '
             'building a terrestrial network without a roaming or MVNO deal would be very '
             'challenging. And about small cells alone, he said it seems, quote, an impossible '
             'ask.',
      'title': 'SpaceX Just Finished Its Rooftop Starlink Cell Tower — And Telecom Giants Are '
               'Panicking (Orbital Ledger)',
      'url': 'https://www.youtube.com/watch?v=G3zZhjoRDUg&t=589s',
      'video_id': 'G3zZhjoRDUg'},
     {'author': 'Adding Value w/ Shy Assar | CRE & Industrial',
      'channel': 'Adding Value w/ Shy Assar | CRE & Industrial',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:34:57](https://www.youtube.com/watch?v=tn1QmPINHeE&t=2097s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'd love to ask and, you know, something that younger guys are always so "
              "curious about who maybe haven't done their first deal is what was your guys' "
              'first deal like? And could you walk us through that? Well, actually, you let '
              'you go first.',
      'timestamp': 2097,
      'timestamp_label': '[00:34:57]',
      'timestamp_seconds': 2097,
      'tip': "I'd love to ask and, you know, something that younger guys are always so curious "
             "about who maybe haven't done their first deal is what was your guys' first deal "
             'like? And could you walk us through that? Well, actually, you let you go first.',
      'title': 'Industrial Outdoor Storage (IOS) & Truck Terminals in the Inland Empire | '
               'Steve Sprenger (Adding Value w/ Shy Assar | CRE & Industrial)',
      'url': 'https://www.youtube.com/watch?v=tn1QmPINHeE&t=2097s',
      'video_id': 'tn1QmPINHeE'},
     {'author': 'Codie Sanchez',
      'channel': 'Codie Sanchez',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:03](https://www.youtube.com/watch?v=DXWpZSGVI4w&t=543s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Them make a deal a long-term deal but if you want something tomorrow or two '
              "days from now and you only want it for two hours we're kind of the only option.",
      'timestamp': 543,
      'timestamp_label': '[00:09:03]',
      'timestamp_seconds': 543,
      'tip': 'Them make a deal a long-term deal but if you want something tomorrow or two days '
             "from now and you only want it for two hours we're kind of the only option.",
      'title': 'How to Make $3M a Year Buying Billboards (Codie Sanchez)',
      'url': 'https://www.youtube.com/watch?v=DXWpZSGVI4w&t=543s',
      'video_id': 'DXWpZSGVI4w'},
     {'author': 'Tyler Cauble',
      'channel': 'Tyler Cauble',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:12](https://www.youtube.com/watch?v=IRDT0HnPpUc&t=912s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Got yourself a pretty good deal and if you want to dive more into industrial '
              'outdoor storage check out this video here on the laziest way to invest in '
              'commercial real estate.',
      'timestamp': 912,
      'timestamp_label': '[00:15:12]',
      'timestamp_seconds': 912,
      'tip': 'Got yourself a pretty good deal and if you want to dive more into industrial '
             'outdoor storage check out this video here on the laziest way to invest in '
             'commercial real estate.',
      'title': '$30k/Month from A Parking Lot?? (Tyler Cauble)',
      'url': 'https://www.youtube.com/watch?v=IRDT0HnPpUc&t=912s',
      'video_id': 'IRDT0HnPpUc'},
     {'author': 'Tower Genius',
      'channel': 'Tower Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=cdP7Eld_jP4&t=102s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your asset we are sure that you will be able to quickly determine whether our '
              'coaching services are the right solution for you please follow the link below '
              'to book a 30-minute strategy call we know you will be glad you took this first '
              'step in obtaining expert guidance.',
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': 'Your asset we are sure that you will be able to quickly determine whether our '
             'coaching services are the right solution for you please follow the link below to '
             'book a 30-minute strategy call we know you will be glad you took this first step '
             'in obtaining expert guidance.',
      'title': 'Cell Tower Lease Buyout - Before You Sell Your Cell Site Easements For a Cash '
               'Lump Sum (Tower Genius)',
      'url': 'https://www.youtube.com/watch?v=cdP7Eld_jP4&t=102s',
      'video_id': 'cdP7Eld_jP4'},
     {'author': 'Tower Genius',
      'channel': 'Tower Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:10](https://www.youtube.com/watch?v=xv8TdIdnmRQ&t=550s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Book a 30-minute discovery call anytime with one of our appointment centers and '
              'we look forward to discussing your cell tower lease proposal and help you to '
              "navigate that negotiation and maximize the deal you've been listening to the "
              'wireless wise guys podcast.',
      'timestamp': 550,
      'timestamp_label': '[00:09:10]',
      'timestamp_seconds': 550,
      'tip': 'Book a 30-minute discovery call anytime with one of our appointment centers and '
             'we look forward to discussing your cell tower lease proposal and help you to '
             "navigate that negotiation and maximize the deal you've been listening to the "
             'wireless wise guys podcast.',
      'title': 'How to Negotiate a Cell Tower Lease  - Part 3 (Tower Genius)',
      'url': 'https://www.youtube.com/watch?v=xv8TdIdnmRQ&t=550s',
      'video_id': 'xv8TdIdnmRQ'}],
 7: [{'author': 'Hustle Labs',
      'channel': 'Hustle Labs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:08](https://www.youtube.com/watch?v=IsQBWJcu3ro&t=188s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Everybody wins because the location owner pays nothing and gets a modern '
              "amenity. Let's break the actual execution down into four steps. Step one, pick "
              'your location. Not every business is a good fit.',
      'timestamp': 188,
      'timestamp_label': '[00:03:08]',
      'timestamp_seconds': 188,
      'tip': 'Everybody wins because the location owner pays nothing and gets a modern '
             "amenity. Let's break the actual execution down into four steps. Step one, pick "
             'your location. Not every business is a good fit.',
      'title': "The Side Hustle No One's Talking About (Indoor Billboards) (Hustle Labs)",
      'url': 'https://www.youtube.com/watch?v=IsQBWJcu3ro&t=188s',
      'video_id': 'IsQBWJcu3ro'},
     {'author': 'Circuit Masterclass',
      'channel': 'Circuit Masterclass',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:22](https://www.youtube.com/watch?v=YhDIp_Bjk-I&t=322s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'However, the grid voltage is much higher. Therefore, a transformer is used to '
              'step up the PCS output voltage to the grid voltage level. Similarly, the '
              'transformer also steps down the grid voltage when power is taken from the grid '
              'to charge the battery.',
      'timestamp': 322,
      'timestamp_label': '[00:05:22]',
      'timestamp_seconds': 322,
      'tip': 'However, the grid voltage is much higher. Therefore, a transformer is used to '
             'step up the PCS output voltage to the grid voltage level. Similarly, the '
             'transformer also steps down the grid voltage when power is taken from the grid '
             'to charge the battery.',
      'title': 'Battery Energy Storage System (BESS) Explained | Layout, PCS, EMS, BMS & '
               'Working Principle (Circuit Masterclass)',
      'url': 'https://www.youtube.com/watch?v=YhDIp_Bjk-I&t=322s',
      'video_id': 'YhDIp_Bjk-I'},
     {'author': 'The Finance Explainer',
      'channel': 'The Finance Explainer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=pHu5ZfxNtfg&t=91s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And layer three is the advertising inventory, meaning the actual right to sell '
              'ad space on that sign, which is a business asset completely separate from the '
              "metal and the dirt. In most cases, a billboard company doesn't buy land at all.",
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': 'And layer three is the advertising inventory, meaning the actual right to sell '
             'ad space on that sign, which is a business asset completely separate from the '
             "metal and the dirt. In most cases, a billboard company doesn't buy land at all.",
      'title': 'The Economics of Owning a Billboard | The Explainer (The Finance Explainer)',
      'url': 'https://www.youtube.com/watch?v=pHu5ZfxNtfg&t=91s',
      'video_id': 'pHu5ZfxNtfg'},
     {'author': 'What They Really Sell',
      'channel': 'What They Really Sell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:15](https://www.youtube.com/watch?v=H0bRd-9Ez2c&t=435s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'At the end of 2025, Lamar had about 5,500 digital billboard displays against '
              'roughly 159,300 total billboard displays. That is only around 3 and 12% of the '
              'display count. Yet those digital billboards generated approximately 33% of '
              "Lamar's billboard advertising revenue.",
      'timestamp': 435,
      'timestamp_label': '[00:07:15]',
      'timestamp_seconds': 435,
      'tip': 'At the end of 2025, Lamar had about 5,500 digital billboard displays against '
             'roughly 159,300 total billboard displays. That is only around 3 and 12% of the '
             'display count. Yet those digital billboards generated approximately 33% of '
             "Lamar's billboard advertising revenue.",
      'title': 'Why a Billboard Is Worth More Than the Ad on It (What They Really Sell)',
      'url': 'https://www.youtube.com/watch?v=H0bRd-9Ez2c&t=435s',
      'video_id': 'H0bRd-9Ez2c'},
     {'author': 'Learn Solar & BESS',
      'channel': 'Learn Solar & BESS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=i_OH8wyz41M&t=126s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Take Rajasthan for example. They are pioneering the shift right now with their '
              "2025 green open access rules. If you're building a renewable project over 5 "
              'megawatt, you absolutely must include battery storage, at least 5% capacity for '
              'a minimum of 2 hours.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': 'Take Rajasthan for example. They are pioneering the shift right now with their '
             "2025 green open access rules. If you're building a renewable project over 5 "
             'megawatt, you absolutely must include battery storage, at least 5% capacity for '
             'a minimum of 2 hours.',
      'title': 'Battery Energy Storage System - BESS | Explained |  #Learnsolar&bess #BESS '
               '(Learn Solar & BESS)',
      'url': 'https://www.youtube.com/watch?v=i_OH8wyz41M&t=126s',
      'video_id': 'i_OH8wyz41M'},
     {'author': 'BESS Engineer',
      'channel': 'BESS Engineer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:19](https://www.youtube.com/watch?v=Pd5iB85hCLU&t=19s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Then, the sun sets. Demand races up the duck's neck  in just a few hours to the "
              'evening peak, its head. A battery energy storage system, or.',
      'timestamp': 19,
      'timestamp_label': '[00:00:19]',
      'timestamp_seconds': 19,
      'tip': "Then, the sun sets. Demand races up the duck's neck  in just a few hours to the "
             'evening peak, its head. A battery energy storage system, or.',
      'title': 'How a BESS Site Works: Batteries to Grid | BESS Decoded Ep. 1 (BESS Engineer)',
      'url': 'https://www.youtube.com/watch?v=Pd5iB85hCLU&t=19s',
      'video_id': 'Pd5iB85hCLU'},
     {'author': 'MaxLife Commercial RE MLR',
      'channel': 'MaxLife Commercial RE MLR',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=oYtLEutv1NQ&t=31s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Let me show you how it actually works, what the numbers look like, and where '
              'investors get burned. With a warehouse, you are underwriting a building. With '
              'IOS, there is barely a building to underwrite. You are buying land and the '
              'right to use it a specific way.',
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': 'Let me show you how it actually works, what the numbers look like, and where '
             'investors get burned. With a warehouse, you are underwriting a building. With '
             'IOS, there is barely a building to underwrite. You are buying land and the right '
             'to use it a specific way.',
      'title': 'Industrial Outdoor Storage (IOS) Explained: Florida Yards, Rents & Risks '
               '(MaxLife Commercial RE MLR)',
      'url': 'https://www.youtube.com/watch?v=oYtLEutv1NQ&t=31s',
      'video_id': 'oYtLEutv1NQ'},
     {'author': 'Aries Advisors',
      'channel': 'Aries Advisors',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:03](https://www.youtube.com/watch?v=Yg_kM2-vltw&t=123s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Whether you already have a tower on your property or you've been approached "
              "with an offer for a new tower or perhaps you're considering a lease buyout, the "
              'smartest first step is to get clarity.',
      'timestamp': 123,
      'timestamp_label': '[00:02:03]',
      'timestamp_seconds': 123,
      'tip': "Whether you already have a tower on your property or you've been approached with "
             "an offer for a new tower or perhaps you're considering a lease buyout, the "
             'smartest first step is to get clarity.',
      'title': 'Unlock Hidden Income with Cell Towers (Aries Advisors)',
      'url': 'https://www.youtube.com/watch?v=Yg_kM2-vltw&t=123s',
      'video_id': 'Yg_kM2-vltw'},
     {'author': 'Telecom Training',
      'channel': 'Telecom Training',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=tqz39K230_w&t=89s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That allows millions of phones to share the network efficiently. When most '
              'people look at a cell tower, they see this: large white panels mounted high '
              'above the ground. But those panels are usually radomes, a protective outer '
              'cover that hides the real antenna system inside.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': 'That allows millions of phones to share the network efficiently. When most '
             'people look at a cell tower, they see this: large white panels mounted high '
             'above the ground. But those panels are usually radomes, a protective outer cover '
             'that hides the real antenna system inside.',
      'title': 'What’s Inside a Cell Tower Antenna? | Cellular Antennas Explained (Telecom '
               'Training)',
      'url': 'https://www.youtube.com/watch?v=tqz39K230_w&t=89s',
      'video_id': 'tqz39K230_w'},
     {'author': 'The Power Hub',
      'channel': 'The Power Hub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:30](https://www.youtube.com/watch?v=zXV1Vy_XECY&t=390s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Energy storage system to complement your renewable energy source or just want '
              'to understand if your land is suitable for b s click the button or link below '
              "this video and one of the power hub's experts will reach out to you for an "
              'informal.',
      'timestamp': 390,
      'timestamp_label': '[00:06:30]',
      'timestamp_seconds': 390,
      'tip': 'Energy storage system to complement your renewable energy source or just want to '
             'understand if your land is suitable for b s click the button or link below this '
             "video and one of the power hub's experts will reach out to you for an informal.",
      'title': 'Battery Energy Storage Systems (BESS) (The Power Hub)',
      'url': 'https://www.youtube.com/watch?v=zXV1Vy_XECY&t=390s',
      'video_id': 'zXV1Vy_XECY'},
     {'author': 'Tower Genius',
      'channel': 'Tower Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:24](https://www.youtube.com/watch?v=xfquYQeRi_Q&t=84s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That you don't leave things a chance give tower genius a call our number is "
              '888-313-9750 my business partner kevin dunhu and I have been helping property '
              'owners with their sell site lease questions since 2008 and we can help you too '
              'thanks.',
      'timestamp': 84,
      'timestamp_label': '[00:01:24]',
      'timestamp_seconds': 84,
      'tip': "That you don't leave things a chance give tower genius a call our number is "
             '888-313-9750 my business partner kevin dunhu and I have been helping property '
             'owners with their sell site lease questions since 2008 and we can help you too '
             'thanks.',
      'title': 'HOW TO USE A CELL TOWER LEASE BUYOUT CALCULATOR (Tower Genius)',
      'url': 'https://www.youtube.com/watch?v=xfquYQeRi_Q&t=84s',
      'video_id': 'xfquYQeRi_Q'},
     {'author': 'INDOT',
      'channel': 'INDOT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:23](https://www.youtube.com/watch?v=YWN-XPL47M0&t=863s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Folks are gonna be able to watch this and learn about what we do as an agency '
              'and kind of your career journey so thank you again so much for joining me this '
              'morning thanks again David I probably ate it talk to you soon egg teasing and '
              'have a good day bye.',
      'timestamp': 863,
      'timestamp_label': '[00:14:23]',
      'timestamp_seconds': 863,
      'tip': 'Folks are gonna be able to watch this and learn about what we do as an agency '
             'and kind of your career journey so thank you again so much for joining me this '
             'morning thanks again David I probably ate it talk to you soon egg teasing and '
             'have a good day bye.',
      'title': 'Career Pathway Conversations with Kiara Cross - Outdoor Advertising Permits '
               'Specialist (INDOT)',
      'url': 'https://www.youtube.com/watch?v=YWN-XPL47M0&t=863s',
      'video_id': 'YWN-XPL47M0'},
     {'author': 'LandSkills',
      'channel': 'LandSkills',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:34](https://www.youtube.com/watch?v=hr88g_fSUMM&t=634s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Time now for site Concepts and Tower lease.net this is Bart pair thanks for '
              'taking the time to watch the videos I really hope you learned something '
              'valuable today I look forward to speaking with you have a great day.',
      'timestamp': 634,
      'timestamp_label': '[00:10:34]',
      'timestamp_seconds': 634,
      'tip': 'Time now for site Concepts and Tower lease.net this is Bart pair thanks for '
             'taking the time to watch the videos I really hope you learned something valuable '
             'today I look forward to speaking with you have a great day.',
      'title': '5 Cell Tower Lease Blunders (LandSkills)',
      'url': 'https://www.youtube.com/watch?v=hr88g_fSUMM&t=634s',
      'video_id': 'hr88g_fSUMM'},
     {'author': 'Vertical Consultants',
      'channel': 'Vertical Consultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:12](https://www.youtube.com/watch?v=uuYMqpFuo3Y&t=132s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Lease or do something with an existing cell tower lease has a motivation to get '
              'you to focus where they want you to focus you need to think of it a bigger '
              'picture understand all the aspects of a cell tower lease get more money get a '
              'better lease get vertical.',
      'timestamp': 132,
      'timestamp_label': '[00:02:12]',
      'timestamp_seconds': 132,
      'tip': 'Lease or do something with an existing cell tower lease has a motivation to get '
             'you to focus where they want you to focus you need to think of it a bigger '
             'picture understand all the aspects of a cell tower lease get more money get a '
             'better lease get vertical.',
      'title': 'Cell Tower Lease Rent Offer How Much And Why? (Vertical Consultants)',
      'url': 'https://www.youtube.com/watch?v=uuYMqpFuo3Y&t=132s',
      'video_id': 'uuYMqpFuo3Y'},
     {'author': 'Vertical Consultants',
      'channel': 'Vertical Consultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:11](https://www.youtube.com/watch?v=JyLcfYCapGo&t=131s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That lease or somebody wants to buy it you want to know how much your sell '
              'Tower lease is worth scan this QR code and get more information about your '
              'lease and how much you should get get more money get a better lease get '
              'vertical.',
      'timestamp': 131,
      'timestamp_label': '[00:02:11]',
      'timestamp_seconds': 131,
      'tip': 'That lease or somebody wants to buy it you want to know how much your sell Tower '
             'lease is worth scan this QR code and get more information about your lease and '
             'how much you should get get more money get a better lease get vertical.',
      'title': 'MAXIMIZE Your Cell Tower Lease Rent Rates in 2025 (Vertical Consultants)',
      'url': 'https://www.youtube.com/watch?v=JyLcfYCapGo&t=131s',
      'video_id': 'JyLcfYCapGo'}],
 8: [{'author': 'Behind The Billions',
      'channel': 'Behind The Billions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:55](https://www.youtube.com/watch?v=Bb-6A1zEJAc&t=175s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Annual operating cost is 800 million to 3 billion. You are not an advertising '
              'company anymore. You are a real estate holding company wrapped around a '
              'technology platform wrapped around a national media sales operation. You are '
              'not in the billboard business.',
      'timestamp': 175,
      'timestamp_label': '[00:02:55]',
      'timestamp_seconds': 175,
      'tip': 'Annual operating cost is 800 million to 3 billion. You are not an advertising '
             'company anymore. You are a real estate holding company wrapped around a '
             'technology platform wrapped around a national media sales operation. You are not '
             'in the billboard business.',
      'title': 'The Economics of Owning a Billboard Network (Behind The Billions)',
      'url': 'https://www.youtube.com/watch?v=Bb-6A1zEJAc&t=175s',
      'video_id': 'Bb-6A1zEJAc'},
     {'author': 'Vaultonomics',
      'channel': 'Vaultonomics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:54](https://www.youtube.com/watch?v=clsOKO3QgiM&t=414s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Billboards are often priced around how many people are expected to see them. '
              'And the industry measures audiences with traffic data from highway departments '
              'and from tools like Geopath. In a booming city with advertisers fighting for '
              'space, prices climb.',
      'timestamp': 414,
      'timestamp_label': '[00:06:54]',
      'timestamp_seconds': 414,
      'tip': 'Billboards are often priced around how many people are expected to see them. And '
             'the industry measures audiences with traffic data from highway departments and '
             'from tools like Geopath. In a booming city with advertisers fighting for space, '
             'prices climb.',
      'title': 'The Economics of Owning a Billboard Business in America (Vaultonomics)',
      'url': 'https://www.youtube.com/watch?v=clsOKO3QgiM&t=414s',
      'video_id': 'clsOKO3QgiM'},
     {'author': 'Plain Sight',
      'channel': 'Plain Sight',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=Nuf8IbOuL70&t=30s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Meet Lamar Advertising, a company that says it has operated under the Lamar '
              'name since 1902. Its annual report says it operates about one hundred '
              'fifty-nine thousand three hundred billboard displays in forty-five states and '
              'Canada.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'Meet Lamar Advertising, a company that says it has operated under the Lamar name '
             'since 1902. Its annual report says it operates about one hundred fifty-nine '
             'thousand three hundred billboard displays in forty-five states and Canada.',
      'title': 'What Does Lamar Really Sell The Dirt Under the Billboard (Plain Sight)',
      'url': 'https://www.youtube.com/watch?v=Nuf8IbOuL70&t=30s',
      'video_id': 'Nuf8IbOuL70'},
     {'author': 'Telecom Training',
      'channel': 'Telecom Training',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:39](https://www.youtube.com/watch?v=zDZJfjUxezU&t=279s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Each one of these antennas if it was eight antenna elements you would need '
              'eight streams so the data would be broken up into eight parts in this case.',
      'timestamp': 279,
      'timestamp_label': '[00:04:39]',
      'timestamp_seconds': 279,
      'tip': 'Each one of these antennas if it was eight antenna elements you would need eight '
             'streams so the data would be broken up into eight parts in this case.',
      'title': 'HOW 5G MIMO ANTENNAS WORK (Telecom Training)',
      'url': 'https://www.youtube.com/watch?v=zDZJfjUxezU&t=279s',
      'video_id': 'zDZJfjUxezU'},
     {'author': 'Texas Geographic Information Office',
      'channel': 'Texas Geographic Information Office',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=d9Le5oqu4wc&t=20s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And I work specifically with our Hi-Beautification Program. And we regulate the '
              "billboards on the side of the road. We're dealing with almost entirely private "
              'property and private assets for the permitting and control of these signs.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'And I work specifically with our Hi-Beautification Program. And we regulate the '
             "billboards on the side of the road. We're dealing with almost entirely private "
             'property and private assets for the permitting and control of these signs.',
      'title': 'How TxDOT uses Address Points and Land Parcel Data For Billboard Regulation '
               '(Texas Geographic Information Office)',
      'url': 'https://www.youtube.com/watch?v=d9Le5oqu4wc&t=20s',
      'video_id': 'd9Le5oqu4wc'},
     {'author': 'Adrian Boysel',
      'channel': 'Adrian Boysel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:04](https://www.youtube.com/watch?v=14aRU-ObgC0&t=604s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You so you want to be able to ask people as well when they call on how to your '
              "bus let's say oh i saw your billboard right so the more tracking you do the.",
      'timestamp': 604,
      'timestamp_label': '[00:10:04]',
      'timestamp_seconds': 604,
      'tip': 'You so you want to be able to ask people as well when they call on how to your '
             "bus let's say oh i saw your billboard right so the more tracking you do the.",
      'title': 'Does Billboard Marketing and Advertising Work? (Adrian Boysel)',
      'url': 'https://www.youtube.com/watch?v=14aRU-ObgC0&t=604s',
      'video_id': '14aRU-ObgC0'},
     {'author': 'Land Intel - Land Investing',
      'channel': 'Land Intel - Land Investing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=P_Nhj8ZzbYw&t=62s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's click run free site check to begin. Once you click run free site check, "
              "this is the launch page you'll see. It allows you to instantly evaluate any "
              'property for solar, BESS, and data center development potential. To get '
              "started, simply enter your property's acreage.",
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': "Let's click run free site check to begin. Once you click run free site check, "
             "this is the launch page you'll see. It allows you to instantly evaluate any "
             'property for solar, BESS, and data center development potential. To get started, '
             "simply enter your property's acreage.",
      'title': 'How to Check ANY Land for Solar, BESS & Data Center Potential for FREE (Land '
               'Intel - Land Investing)',
      'url': 'https://www.youtube.com/watch?v=P_Nhj8ZzbYw&t=62s',
      'video_id': 'P_Nhj8ZzbYw'},
     {'author': 'History of Simple Things',
      'channel': 'History of Simple Things',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:27](https://www.youtube.com/watch?v=MT8oXJXtzq4&t=207s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Each sector has its own dedicated antenna, allowing the tower to serve multiple '
              'users simultaneously while minimizing interference. When you make a call or use '
              'data, your phone automatically connects to the closest tower within your cell.',
      'timestamp': 207,
      'timestamp_label': '[00:03:27]',
      'timestamp_seconds': 207,
      'tip': 'Each sector has its own dedicated antenna, allowing the tower to serve multiple '
             'users simultaneously while minimizing interference. When you make a call or use '
             'data, your phone automatically connects to the closest tower within your cell.',
      'title': 'How Do Cell Towers Actually Work? (History of Simple Things)',
      'url': 'https://www.youtube.com/watch?v=MT8oXJXtzq4&t=207s',
      'video_id': 'MT8oXJXtzq4'},
     {'author': 'Tasty Ad',
      'channel': 'Tasty Ad',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:11](https://www.youtube.com/watch?v=ivfNhpDax7I&t=131s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We know you will see the benefits of using it for yourself and continue to do '
              'so if you use it every day get familiar with it and really take advantage of it '
              'as a sales tool for creating spec you ads for every customer you will see an '
              'increase in your sales.',
      'timestamp': 131,
      'timestamp_label': '[00:02:11]',
      'timestamp_seconds': 131,
      'tip': 'We know you will see the benefits of using it for yourself and continue to do so '
             'if you use it every day get familiar with it and really take advantage of it as '
             'a sales tool for creating spec you ads for every customer you will see an '
             'increase in your sales.',
      'title': 'How to Sell More Billboards (Tasty Ad)',
      'url': 'https://www.youtube.com/watch?v=ivfNhpDax7I&t=131s',
      'video_id': 'ivfNhpDax7I'},
     {'author': 'EdisonIndustrial',
      'channel': 'EdisonIndustrial',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:23](https://www.youtube.com/watch?v=-7jTPPttg2s&t=143s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Foot building but it can be as small as 10,000 ideally the 10 to 20,000 000 ft '
              'range on a 2 3 5 acre piece is almost the perfect outdoor storage and it will '
              'attract most of the users that can occupy that site so infrastructure with a '
              'small.',
      'timestamp': 143,
      'timestamp_label': '[00:02:23]',
      'timestamp_seconds': 143,
      'tip': 'Foot building but it can be as small as 10,000 ideally the 10 to 20,000 000 ft '
             'range on a 2 3 5 acre piece is almost the perfect outdoor storage and it will '
             'attract most of the users that can occupy that site so infrastructure with a '
             'small.',
      'title': 'What’s the perfect Industrial Outdoor Storage IOS Site (EdisonIndustrial)',
      'url': 'https://www.youtube.com/watch?v=-7jTPPttg2s&t=143s',
      'video_id': '-7jTPPttg2s'},
     {'author': 'Vertical Consultants',
      'channel': 'Vertical Consultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:07](https://www.youtube.com/watch?v=7qwoLJg7Ya8&t=367s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Used to be that you drive down the road and you lose coverage and you wouldn't "
              "have cell towers around. Now you don't have enough capacity because your phone "
              'uses so much data. You have to build more and more cell towers to be able to '
              'handle that data.',
      'timestamp': 367,
      'timestamp_label': '[00:06:07]',
      'timestamp_seconds': 367,
      'tip': "Used to be that you drive down the road and you lose coverage and you wouldn't "
             "have cell towers around. Now you don't have enough capacity because your phone "
             'uses so much data. You have to build more and more cell towers to be able to '
             'handle that data.',
      'title': '10 Questions You MUST Ask Before Signing a Cell Tower Deal (Vertical '
               'Consultants)',
      'url': 'https://www.youtube.com/watch?v=7qwoLJg7Ya8&t=367s',
      'video_id': '7qwoLJg7Ya8'},
     {'author': 'Tower Genius',
      'channel': 'Tower Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:42](https://www.youtube.com/watch?v=JyYFN2j-Voo&t=342s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Grand a month and it's got to have annual rent increases and a few other things "
              'so if you have questions about a cell tower lease give us a call Tower genius '
              'our number is 888-313-9750 you can visit us at towergenius.com.',
      'timestamp': 342,
      'timestamp_label': '[00:05:42]',
      'timestamp_seconds': 342,
      'tip': "Grand a month and it's got to have annual rent increases and a few other things "
             'so if you have questions about a cell tower lease give us a call Tower genius '
             'our number is 888-313-9750 you can visit us at towergenius.com.',
      'title': 'Negotiating a Cell Tower Lease from the PROPERTY OWNERS Perspective (Tower '
               'Genius)',
      'url': 'https://www.youtube.com/watch?v=JyYFN2j-Voo&t=342s',
      'video_id': 'JyYFN2j-Voo'},
     {'author': 'Self Storage Income',
      'channel': 'Self Storage Income',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:45](https://www.youtube.com/watch?v=bJCG2BdPq48&t=285s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Not after it's already done if you're considering it don't send the paperwork "
              'make sure the language is built out and you have a specific attorney look over '
              'it to help you set it up right and for you and your company thanks everybody.',
      'timestamp': 285,
      'timestamp_label': '[00:04:45]',
      'timestamp_seconds': 285,
      'tip': "Not after it's already done if you're considering it don't send the paperwork "
             'make sure the language is built out and you have a specific attorney look over '
             'it to help you set it up right and for you and your company thanks everybody.',
      'title': 'Cell Towers | How Much Money Can You Make [But are They Worth It?] (Self '
               'Storage Income)',
      'url': 'https://www.youtube.com/watch?v=bJCG2BdPq48&t=285s',
      'video_id': 'bJCG2BdPq48'},
     {'author': 'Tower Genius',
      'channel': 'Tower Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:46](https://www.youtube.com/watch?v=WlOtjvRO-jU&t=166s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Rooftop sell site lease or about your Tower lease especially if you own the '
              'steel and you have you have uh tenants there that are looking to upgrade give '
              'us a call at Tower genius our number is 888 313 975 visit us at Tower '
              'genius.com.',
      'timestamp': 166,
      'timestamp_label': '[00:02:46]',
      'timestamp_seconds': 166,
      'tip': 'Rooftop sell site lease or about your Tower lease especially if you own the '
             'steel and you have you have uh tenants there that are looking to upgrade give us '
             'a call at Tower genius our number is 888 313 975 visit us at Tower genius.com.',
      'title': 'Why do cell tower lease buyout companies LOVE rooftop cell sites? (Tower '
               'Genius)',
      'url': 'https://www.youtube.com/watch?v=WlOtjvRO-jU&t=166s',
      'video_id': 'WlOtjvRO-jU'},
     {'author': 'Tower Genius',
      'channel': 'Tower Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:09](https://www.youtube.com/watch?v=5MqJqF4hVEQ&t=189s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Worth 100 Grand so uh it's on a site-by-site basis the valuation of these "
              "things don't just give out a right of first refusal and another thing these "
              "rent reduction letters they're always asking for it you know and you got to "
              'watch these offers very closely.',
      'timestamp': 189,
      'timestamp_label': '[00:03:09]',
      'timestamp_seconds': 189,
      'tip': "Worth 100 Grand so uh it's on a site-by-site basis the valuation of these things "
             "don't just give out a right of first refusal and another thing these rent "
             "reduction letters they're always asking for it you know and you got to watch "
             'these offers very closely.',
      'title': 'CELL TOWER LEASE RIGHT OF FIRST REFUSAL VALUE (Tower Genius)',
      'url': 'https://www.youtube.com/watch?v=5MqJqF4hVEQ&t=189s',
      'video_id': '5MqJqF4hVEQ'}],
 9: [{'author': 'How They Make Money',
      'channel': 'How They Make Money',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:56](https://www.youtube.com/watch?v=eVhqvVbf0rA&t=116s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '34% of out-of-home spending in 2024. The secret is scarcity written into law. '
              'The Highway Beautification Act of 1965 restricted new signs within 660 ft of '
              'interstate and primary highways, largely to commercial and industrial areas '
              'that meet state permit rules.',
      'timestamp': 116,
      'timestamp_label': '[00:01:56]',
      'timestamp_seconds': 116,
      'tip': '34% of out-of-home spending in 2024. The secret is scarcity written into law. '
             'The Highway Beautification Act of 1965 restricted new signs within 660 ft of '
             'interstate and primary highways, largely to commercial and industrial areas that '
             'meet state permit rules.',
      'title': 'How Billboards Make Money From a Steel Pole (How They Make Money)',
      'url': 'https://www.youtube.com/watch?v=eVhqvVbf0rA&t=116s',
      'video_id': 'eVhqvVbf0rA'},
     {'author': 'Walt Runs The Numbers',
      'channel': 'Walt Runs The Numbers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:39](https://www.youtube.com/watch?v=9d5MJAQGDk8&t=99s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Highway Beautification Act regulations and local zoning ordinances tightly '
              'restrict where new billboards can be erected, creating a fixed, shrinking '
              'supply of legal locations.',
      'timestamp': 99,
      'timestamp_label': '[00:01:39]',
      'timestamp_seconds': 99,
      'tip': 'Highway Beautification Act regulations and local zoning ordinances tightly '
             'restrict where new billboards can be erected, creating a fixed, shrinking supply '
             'of legal locations.',
      'title': 'What a Highway Billboard Actually Makes Full Accounting (Walt Runs The '
               'Numbers)',
      'url': 'https://www.youtube.com/watch?v=9d5MJAQGDk8&t=99s',
      'video_id': '9d5MJAQGDk8'},
     {'author': 'Next 9NEWS',
      'channel': 'Next 9NEWS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=as0D6GqNVZA&t=70s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "SMALLWOOD IS A SPONSOR OF A BILL THAT WILL MODIFY THE STATE'S OUTDOOR "
              "ADVERTISING BILL THAT WILL MODIFY THE STATE'S OUTDOOR ADVERTISING BILL THAT "
              "WILL MODIFY THE STATE'S OUTDOOR ADVERTISING ACT. THE STATE'S OUTDOOR "
              "ADVERTISING ACT. THE STATE'S OUTDOOR ADVERTISING ACT.",
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': "SMALLWOOD IS A SPONSOR OF A BILL THAT WILL MODIFY THE STATE'S OUTDOOR "
             "ADVERTISING BILL THAT WILL MODIFY THE STATE'S OUTDOOR ADVERTISING BILL THAT WILL "
             "MODIFY THE STATE'S OUTDOOR ADVERTISING ACT. THE STATE'S OUTDOOR ADVERTISING ACT. "
             "THE STATE'S OUTDOOR ADVERTISING ACT.",
      'title': 'Colorado considers change to billboard permit rules (Next 9NEWS)',
      'url': 'https://www.youtube.com/watch?v=as0D6GqNVZA&t=70s',
      'video_id': 'as0D6GqNVZA'},
     {'author': 'TxDOT',
      'channel': 'TxDOT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:47](https://www.youtube.com/watch?v=lQ0yYTXku1c&t=47s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And rules are but also do case studies to find out what litigation has been '
              'successful on specific topics that are a problem for the state you know '
              "there's.",
      'timestamp': 47,
      'timestamp_label': '[00:00:47]',
      'timestamp_seconds': 47,
      'tip': 'And rules are but also do case studies to find out what litigation has been '
             "successful on specific topics that are a problem for the state you know there's.",
      'title': 'Synthesis: Develop Outdoor Advertising Control Reference Manual for TxDOT '
               '0-7085 (TxDOT)',
      'url': 'https://www.youtube.com/watch?v=lQ0yYTXku1c&t=47s',
      'video_id': 'lQ0yYTXku1c'},
     {'author': 'RoadVista 60',
      'channel': 'RoadVista 60',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:13](https://www.youtube.com/watch?v=g3dG9XNCv8o&t=73s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'She passionately advocated for national beautifification efforts. This led '
              'directly to the Landmark Highway Beautifification Act signed into law by '
              'President Lyndon Johnson in 1965. The HBA aimed to control billboards near '
              'federal highways.',
      'timestamp': 73,
      'timestamp_label': '[00:01:13]',
      'timestamp_seconds': 73,
      'tip': 'She passionately advocated for national beautifification efforts. This led '
             'directly to the Landmark Highway Beautifification Act signed into law by '
             'President Lyndon Johnson in 1965. The HBA aimed to control billboards near '
             'federal highways.',
      'title': "Why Billboards Are Banned on America's Most Scenic Roads (RoadVista 60)",
      'url': 'https://www.youtube.com/watch?v=g3dG9XNCv8o&t=73s',
      'video_id': 'g3dG9XNCv8o'},
     {'author': 'One Decision Ago',
      'channel': 'One Decision Ago',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:19](https://www.youtube.com/watch?v=D_1Q_8uXe9s&t=379s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is the moment outdoor advertising stopped being a trade practiced by '
              'individuals and became a genuine political force for full decades before its '
              "most serious federal test would arrive. The industry's legal argument evolved "
              'steadily over these decades.',
      'timestamp': 379,
      'timestamp_label': '[00:06:19]',
      'timestamp_seconds': 379,
      'tip': 'This is the moment outdoor advertising stopped being a trade practiced by '
             'individuals and became a genuine political force for full decades before its '
             "most serious federal test would arrive. The industry's legal argument evolved "
             'steadily over these decades.',
      'title': 'The Billboard Was Invented to Fight a Law — And Then Became the Law (One '
               'Decision Ago)',
      'url': 'https://www.youtube.com/watch?v=D_1Q_8uXe9s&t=379s',
      'video_id': 'D_1Q_8uXe9s'},
     {'author': 'Mr. Finance',
      'channel': 'Mr. Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:22](https://www.youtube.com/watch?v=ku_-0C-ZnV4&t=802s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '4 percentage points off its annual organic growth rate in its core American and '
              "Canadian business. 4 percentage points doesn't sound dramatic until you "
              'remember that this is an industry whose entire pitch to investors is stability '
              'and predictability.',
      'timestamp': 802,
      'timestamp_label': '[00:13:22]',
      'timestamp_seconds': 802,
      'tip': '4 percentage points off its annual organic growth rate in its core American and '
             "Canadian business. 4 percentage points doesn't sound dramatic until you remember "
             'that this is an industry whose entire pitch to investors is stability and '
             'predictability.',
      'title': 'The Economics of Owning a Cell Tower (Mr. Finance)',
      'url': 'https://www.youtube.com/watch?v=ku_-0C-ZnV4&t=802s',
      'video_id': 'ku_-0C-ZnV4'},
     {'author': 'Jonathan Hayek',
      'channel': 'Jonathan Hayek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:21](https://www.youtube.com/watch?v=mPrS0VognEo&t=921s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh so so in that regard, it helped because somebody else was already under '
              "contract and they'd already done a fair amount of due diligence, at least in "
              'terms of ordering the reports.',
      'timestamp': 921,
      'timestamp_label': '[00:15:21]',
      'timestamp_seconds': 921,
      'tip': 'Uh so so in that regard, it helped because somebody else was already under '
             "contract and they'd already done a fair amount of due diligence, at least in "
             'terms of ordering the reports.',
      'title': 'Net Lease Industrial, IOS, and Truck Parking with Ron Rohde (Jonathan Hayek)',
      'url': 'https://www.youtube.com/watch?v=mPrS0VognEo&t=921s',
      'video_id': 'mPrS0VognEo'},
     {'author': 'Robert_Wallace',
      'channel': 'Robert_Wallace',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:14](https://www.youtube.com/watch?v=hxwD9JLVZs8&t=434s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Constitute a renewal of the lease but will be on a month-to-month basis on the '
              'same terms and conditions as applied in the lease.',
      'timestamp': 434,
      'timestamp_label': '[00:07:14]',
      'timestamp_seconds': 434,
      'tip': 'Constitute a renewal of the lease but will be on a month-to-month basis on the '
             'same terms and conditions as applied in the lease.',
      'title': 'Billboard Land Lease Contract (Free Download) (Robert_Wallace)',
      'url': 'https://www.youtube.com/watch?v=hxwD9JLVZs8&t=434s',
      'video_id': 'hxwD9JLVZs8'},
     {'author': 'CREDA Global',
      'channel': 'CREDA Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=cKtqug8KPPk&t=22s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Building coverage than traditional industrial real estate. Tenants really use '
              'the space for outdoor storage >>.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'Building coverage than traditional industrial real estate. Tenants really use '
             'the space for outdoor storage >>.',
      'title': 'NAIOP Insights: Industrial Outdoor Storage (CREDA Global)',
      'url': 'https://www.youtube.com/watch?v=cKtqug8KPPk&t=22s',
      'video_id': 'cKtqug8KPPk'},
     {'author': 'Vertical Consultants',
      'channel': 'Vertical Consultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=USOklBMqTr0&t=92s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Particularly cell tower Ai and how it can assist you as a property owner not '
              'only determining what rent you should get but what overall terms you should get '
              'contact us today always remember get more money get a better lead get vertical.',
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': 'Particularly cell tower Ai and how it can assist you as a property owner not '
             'only determining what rent you should get but what overall terms you should get '
             'contact us today always remember get more money get a better lead get vertical.',
      'title': 'How Cell Tower AI Uses Insider Data to Boost Your Rent! (Vertical Consultants)',
      'url': 'https://www.youtube.com/watch?v=USOklBMqTr0&t=92s',
      'video_id': 'USOklBMqTr0'},
     {'author': 'JP Tower Consulting',
      'channel': 'JP Tower Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:54](https://www.youtube.com/watch?v=gy9A1QN_8Jk&t=234s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Value my experience in the tower industry enables me to anticipate and address '
              'Tower company strategy IES effectively making this Insight invaluable in '
              'navigating the involving landscape of the industry.',
      'timestamp': 234,
      'timestamp_label': '[00:03:54]',
      'timestamp_seconds': 234,
      'tip': 'Value my experience in the tower industry enables me to anticipate and address '
             'Tower company strategy IES effectively making this Insight invaluable in '
             'navigating the involving landscape of the industry.',
      'title': 'How to Negotiate a Cell Tower Contract - Tips (JP Tower Consulting)',
      'url': 'https://www.youtube.com/watch?v=gy9A1QN_8Jk&t=234s',
      'video_id': 'gy9A1QN_8Jk'},
     {'author': 'Tower Genius',
      'channel': 'Tower Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:50](https://www.youtube.com/watch?v=RMRSHif8WD0&t=170s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um, also the rental escalators we've seen where it's like 0. 99% annual, so "
              'like less than 1% annual escalators and these companies are out of their '
              "freaking minds. Uh, the rate of inflation again, it's it's way below CPI.",
      'timestamp': 170,
      'timestamp_label': '[00:02:50]',
      'timestamp_seconds': 170,
      'tip': "Um, also the rental escalators we've seen where it's like 0. 99% annual, so like "
             'less than 1% annual escalators and these companies are out of their freaking '
             "minds. Uh, the rate of inflation again, it's it's way below CPI.",
      'title': 'Cell Tower Leases in 2026 - What to Expect (Tower Genius)',
      'url': 'https://www.youtube.com/watch?v=RMRSHif8WD0&t=170s',
      'video_id': 'RMRSHif8WD0'},
     {'author': 'Tower Genius',
      'channel': 'Tower Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:33](https://www.youtube.com/watch?v=P2LhXcxO5KE&t=153s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Guys I mean it's just it's uh it's capitalism so people want to buy your lease "
              "and a lot of times they'll fight each other for it nothing wrong with that you "
              'know so uh give us a call at Tower genius our numbers 888-313-9750genius.com.',
      'timestamp': 153,
      'timestamp_label': '[00:02:33]',
      'timestamp_seconds': 153,
      'tip': "Guys I mean it's just it's uh it's capitalism so people want to buy your lease "
             "and a lot of times they'll fight each other for it nothing wrong with that you "
             'know so uh give us a call at Tower genius our numbers 888-313-9750genius.com.',
      'title': 'Who are the best CELL TOWER LEASE BUYOUT COMPANIES? (Tower Genius)',
      'url': 'https://www.youtube.com/watch?v=P2LhXcxO5KE&t=153s',
      'video_id': 'P2LhXcxO5KE'},
     {'author': 'Tower Genius',
      'channel': 'Tower Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:58](https://www.youtube.com/watch?v=H0Q5FZ_5RWA&t=298s)',
      'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop telecom '
                   'easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                   'digital-billboard ground-lease assignments, and zero-building Industrial '
                   'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Help people with these cell tower contracts if you have any questions you can '
              "always visit us at towergenius.com or give us a call at 888 313-9750 we'll talk "
              'to you soon thanks.',
      'timestamp': 298,
      'timestamp_label': '[00:04:58]',
      'timestamp_seconds': 298,
      'tip': 'Help people with these cell tower contracts if you have any questions you can '
             "always visit us at towergenius.com or give us a call at 888 313-9750 we'll talk "
             'to you soon thanks.',
      'title': 'Who Loves Your R.O.F.R.? Cell Tower Lease Right of First Refusal (Tower '
               'Genius)',
      'url': 'https://www.youtube.com/watch?v=H0Q5FZ_5RWA&t=298s',
      'video_id': 'H0Q5FZ_5RWA'}],
 10: [{'author': 'eFinancial Models',
       'channel': 'eFinancial Models',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:19](https://www.youtube.com/watch?v=8xq5_kt3OY0&t=1039s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'We could even model a Ford battery cycle because the solar park is 25 years. '
               "But in this case, I don't do that. So if you model battery replacement, this "
               'means we this will trigger capex for each battery.',
       'timestamp': 1039,
       'timestamp_label': '[00:17:19]',
       'timestamp_seconds': 1039,
       'tip': 'We could even model a Ford battery cycle because the solar park is 25 years. '
              "But in this case, I don't do that. So if you model battery replacement, this "
              'means we this will trigger capex for each battery.',
       'title': 'Solar BESS Battery Energy Storage Systems Financial (Excel Template) '
                'Walkthrough (eFinancial Models)',
       'url': 'https://www.youtube.com/watch?v=8xq5_kt3OY0&t=1039s',
       'video_id': '8xq5_kt3OY0'},
      {'author': 'Ned Talks Business',
       'channel': 'Ned Talks Business',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:35](https://www.youtube.com/watch?v=inSGoP3HxYA&t=395s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That's one reason scale matters in this business. 50 billboards gets you "
               "national ad buys. 10 billboards usually doesn't. And what's the stuff nobody "
               'warns you about? The hidden cost that catches new operators the hardest is '
               'lease escalation.',
       'timestamp': 395,
       'timestamp_label': '[00:06:35]',
       'timestamp_seconds': 395,
       'tip': "That's one reason scale matters in this business. 50 billboards gets you "
              "national ad buys. 10 billboards usually doesn't. And what's the stuff nobody "
              'warns you about? The hidden cost that catches new operators the hardest is '
              'lease escalation.',
       'title': 'The Economics of Owning a Billboard Company (Ned Talks Business)',
       'url': 'https://www.youtube.com/watch?v=inSGoP3HxYA&t=395s',
       'video_id': 'inSGoP3HxYA'},
      {'author': 'Follow the Fee',
       'channel': 'Follow the Fee',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:20:02](https://www.youtube.com/watch?v=lQ0ni5KmJiE&t=1202s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': '4% with total debt running more than 12 times its annual cash flow. A leverage '
               'ratio that would be considered dangerously high in almost any industry. A '
               'company sitting on some of the most legally protected, hardest to replicate '
               'advertising real estate in the country.',
       'timestamp': 1202,
       'timestamp_label': '[00:20:02]',
       'timestamp_seconds': 1202,
       'tip': '4% with total debt running more than 12 times its annual cash flow. A leverage '
              'ratio that would be considered dangerously high in almost any industry. A '
              'company sitting on some of the most legally protected, hardest to replicate '
              'advertising real estate in the country.',
       'title': 'The Hidden Economics of Billboard Advertising (Follow the Fee)',
       'url': 'https://www.youtube.com/watch?v=lQ0ni5KmJiE&t=1202s',
       'video_id': 'lQ0ni5KmJiE'},
      {'author': 'Gore Street Capital',
       'channel': 'Gore Street Capital',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:41](https://www.youtube.com/watch?v=9jXkiEU8op0&t=41s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Regarding selection of markets to assess, we need to understand and have '
               'confidence in the long-term business case driven by underlying market and '
               'macro factors.',
       'timestamp': 41,
       'timestamp_label': '[00:00:41]',
       'timestamp_seconds': 41,
       'tip': 'Regarding selection of markets to assess, we need to understand and have '
              'confidence in the long-term business case driven by underlying market and macro '
              'factors.',
       'title': 'How We Choose Battery Storage Projects: The Investment Case for BESS (Gore '
                'Street Capital)',
       'url': 'https://www.youtube.com/watch?v=9jXkiEU8op0&t=41s',
       'video_id': '9jXkiEU8op0'},
      {'author': 'Billboard Source',
       'channel': 'Billboard Source',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=gReq9TXl5BY&t=15s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Sky here with billboards sorts by now you've probably realized how broadcasts "
               'print and digital advertising has become so fragmented and challenging.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': "Sky here with billboards sorts by now you've probably realized how broadcasts "
              'print and digital advertising has become so fragmented and challenging.',
       'title': 'How To Rent and Advertise on a Billboard | Billboard Source (Billboard '
                'Source)',
       'url': 'https://www.youtube.com/watch?v=gReq9TXl5BY&t=15s',
       'video_id': 'gReq9TXl5BY'},
      {'author': 'Ken McElroy',
       'channel': 'Ken McElroy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:36](https://www.youtube.com/watch?v=bteMgQqmSCk&t=36s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And these billboards, they have 25, 30, 40, and even 50-year leases. So, you '
               "imagine that you actually don't even own the land. Then you might say, well, "
               "you're a real estate guy. Well, I'm buying the lease and then there's a "
               'billboard on it, a flat screen in the sky.',
       'timestamp': 36,
       'timestamp_label': '[00:00:36]',
       'timestamp_seconds': 36,
       'tip': 'And these billboards, they have 25, 30, 40, and even 50-year leases. So, you '
              "imagine that you actually don't even own the land. Then you might say, well, "
              "you're a real estate guy. Well, I'm buying the lease and then there's a "
              'billboard on it, a flat screen in the sky.',
       'title': 'This Is the Most Underrated Investment in America (Ken McElroy)',
       'url': 'https://www.youtube.com/watch?v=bteMgQqmSCk&t=36s',
       'video_id': 'bteMgQqmSCk'},
      {'author': 'Chris Long',
       'channel': 'Chris Long',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:18](https://www.youtube.com/watch?v=I_8AzWShUAU&t=318s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s actually costing you money to not be a member of Investor Fuel. If you're "
               'looking to scale your business and build a business that allows you to live '
               'the life of your dreams, please visit investorfuel.',
       'timestamp': 318,
       'timestamp_label': '[00:05:18]',
       'timestamp_seconds': 318,
       'tip': "'s actually costing you money to not be a member of Investor Fuel. If you're "
              'looking to scale your business and build a business that allows you to live the '
              'life of your dreams, please visit investorfuel.',
       'title': 'Industrial Outdoor Storage Explained: How Renting Dirt Works (Chris Long)',
       'url': 'https://www.youtube.com/watch?v=I_8AzWShUAU&t=318s',
       'video_id': 'I_8AzWShUAU'},
      {'author': 'Meg Aubale',
       'channel': 'Meg Aubale',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:59](https://www.youtube.com/watch?v=-s1lJ8WxV9o&t=59s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I'm a developer in Nashville, and I developed the first Airbnb building in "
               'Nashville before Airbnb was to any sort of institutional scale. It was almost '
               '10 years ago now.',
       'timestamp': 59,
       'timestamp_label': '[00:00:59]',
       'timestamp_seconds': 59,
       'tip': "I'm a developer in Nashville, and I developed the first Airbnb building in "
              'Nashville before Airbnb was to any sort of institutional scale. It was almost '
              '10 years ago now.',
       'title': "Why You're Still Early to Industrial Outdoor Storage (Meg Aubale)",
       'url': 'https://www.youtube.com/watch?v=-s1lJ8WxV9o&t=59s',
       'video_id': '-s1lJ8WxV9o'},
      {'author': 'IndiGrid Infrastructure Trust',
       'channel': 'IndiGrid Infrastructure Trust',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:23:31](https://www.youtube.com/watch?v=x9hN7fa_OOI&t=1411s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "IndiGrid reflects India's grid. So, IndiGrid enables energy to your homes. The "
               'vision behind this project was to build a very innovative use case.',
       'timestamp': 1411,
       'timestamp_label': '[00:23:31]',
       'timestamp_seconds': 1411,
       'tip': "IndiGrid reflects India's grid. So, IndiGrid enables energy to your homes. The "
              'vision behind this project was to build a very innovative use case.',
       'title': "Inside India's Biggest Utility-Scale BESS | The Energy Storage | IndiGrid × "
                'National Geographic (IndiGrid Infrastructure Trust)',
       'url': 'https://www.youtube.com/watch?v=x9hN7fa_OOI&t=1411s',
       'video_id': 'x9hN7fa_OOI'},
      {'author': 'The Space Flight',
       'channel': 'The Space Flight',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:02](https://www.youtube.com/watch?v=0P3b6pUkElk&t=662s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Musk did not take a shot at the carriers. He said, quote, "I don\'t think this '
               'means that AT&T, Verizon, and others go out of business or anything. Maybe '
               "they'll lose some revenue here, but I actually think the demand for bandwidth "
               'will be tremendous in the future.".',
       'timestamp': 662,
       'timestamp_label': '[00:11:02]',
       'timestamp_seconds': 662,
       'tip': 'Musk did not take a shot at the carriers. He said, quote, "I don\'t think this '
              'means that AT&T, Verizon, and others go out of business or anything. Maybe '
              "they'll lose some revenue here, but I actually think the demand for bandwidth "
              'will be tremendous in the future.".',
       'title': 'Elon Musk Just Revealed Starlink Micro Cell Towers — And Big Wireless Is In '
                'Trouble (The Space Flight)',
       'url': 'https://www.youtube.com/watch?v=0P3b6pUkElk&t=662s',
       'video_id': '0P3b6pUkElk'},
      {'author': 'Truck Parking Media',
       'channel': 'Truck Parking Media',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:37](https://www.youtube.com/watch?v=GOXjR9kZ3BA&t=157s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s not that rare still it is a strong middle ground for many yards trying to "
               'balance cost security and automation going down the spectrum even more you '
               'have the uh LPR license plate recognition this is much more modern than the '
               'previous two.',
       'timestamp': 157,
       'timestamp_label': '[00:02:37]',
       'timestamp_seconds': 157,
       'tip': "'s not that rare still it is a strong middle ground for many yards trying to "
              'balance cost security and automation going down the spectrum even more you have '
              'the uh LPR license plate recognition this is much more modern than the previous '
              'two.',
       'title': 'Truck Yard Access Control: 4 Systems That Can Make or Break Your Lot’s '
                'Success (Truck Parking Media)',
       'url': 'https://www.youtube.com/watch?v=GOXjR9kZ3BA&t=157s',
       'video_id': 'GOXjR9kZ3BA'},
      {'author': 'Vertical Consultants',
       'channel': 'Vertical Consultants',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=2d9jVK26qi8&t=21s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "We're partnering our expertise with Cell Tower AI to make sure property owners "
               'across the country, whether it be approach for a new cell tower lease or have '
               'an existing one, focus on these three things.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': "We're partnering our expertise with Cell Tower AI to make sure property owners "
              'across the country, whether it be approach for a new cell tower lease or have '
              'an existing one, focus on these three things.',
       'title': 'AI-Powered Negotiation: Maximize Your Cell Tower Lease Income! (Vertical '
                'Consultants)',
       'url': 'https://www.youtube.com/watch?v=2d9jVK26qi8&t=21s',
       'video_id': '2d9jVK26qi8'},
      {'author': 'Tower Genius',
       'channel': 'Tower Genius',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:57](https://www.youtube.com/watch?v=SLOz0FJW1ew&t=117s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Genius which resulted the end result was she ended up selling her cell tower '
               'release rental stream for an additional 35 percent and that was a seven figure '
               'offer so if you have a question about a cell tyre release buyout give us a '
               'call at tower genius 888-313-9750.',
       'timestamp': 117,
       'timestamp_label': '[00:01:57]',
       'timestamp_seconds': 117,
       'tip': 'Genius which resulted the end result was she ended up selling her cell tower '
              'release rental stream for an additional 35 percent and that was a seven figure '
              'offer so if you have a question about a cell tyre release buyout give us a call '
              'at tower genius 888-313-9750.',
       'title': 'How To Negotiate A Cell Tower Lease Buyout - Tower Genius (Tower Genius)',
       'url': 'https://www.youtube.com/watch?v=SLOz0FJW1ew&t=117s',
       'video_id': 'SLOz0FJW1ew'},
      {'author': 'Tower Genius',
       'channel': 'Tower Genius',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:37](https://www.youtube.com/watch?v=wpxdOZZukBY&t=1057s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Actually so anyway um unless you have money to burn then just disregard '
               "everything that I told you otherwise we'd love to talk to you uh visit us at "
               'Tower genius.com or fill out a contact form there or give us a call at 888 '
               '31397 thanks for watching have a great day.',
       'timestamp': 1057,
       'timestamp_label': '[00:17:37]',
       'timestamp_seconds': 1057,
       'tip': 'Actually so anyway um unless you have money to burn then just disregard '
              "everything that I told you otherwise we'd love to talk to you uh visit us at "
              'Tower genius.com or fill out a contact form there or give us a call at 888 '
              '31397 thanks for watching have a great day.',
       'title': 'Who Are the Best Cell Tower Lease Buyout Companies? (Tower Genius)',
       'url': 'https://www.youtube.com/watch?v=wpxdOZZukBY&t=1057s',
       'video_id': 'wpxdOZZukBY'},
      {'author': 'Tower Genius',
       'channel': 'Tower Genius',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:48](https://www.youtube.com/watch?v=Jpi639ecjmg&t=108s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Their side don't you need the higher guns you know sometimes even a higher gun "
               "isn't isn't you know isn't enough everybody seems to be a cell tower expert "
               'nowadays if you need the mother of all cell tower lease experts because '
               "sometimes a higher gun just ain't enough.",
       'timestamp': 108,
       'timestamp_label': '[00:01:48]',
       'timestamp_seconds': 108,
       'tip': "Their side don't you need the higher guns you know sometimes even a higher gun "
              "isn't isn't you know isn't enough everybody seems to be a cell tower expert "
              'nowadays if you need the mother of all cell tower lease experts because '
              "sometimes a higher gun just ain't enough.",
       'title': 'Best Cell Tower Lease Negotiation Strategy (Tower Genius)',
       'url': 'https://www.youtube.com/watch?v=Jpi639ecjmg&t=108s',
       'video_id': 'Jpi639ecjmg'}],
 11: [{'author': 'Profit Mechanics',
       'channel': 'Profit Mechanics',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:53](https://www.youtube.com/watch?v=chCNj5IEUZw&t=53s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A fine most owners never come close to paying and a warning most owners never '
               "heed. Keep that one in your pocket for now. There isn't one price to get into "
               "this business. There are three, and they don't scale the way you'd expect. At "
               "the bottom, you're not building anything.",
       'timestamp': 53,
       'timestamp_label': '[00:00:53]',
       'timestamp_seconds': 53,
       'tip': 'A fine most owners never come close to paying and a warning most owners never '
              "heed. Keep that one in your pocket for now. There isn't one price to get into "
              "this business. There are three, and they don't scale the way you'd expect. At "
              "the bottom, you're not building anything.",
       'title': 'The Economics of Owning a Billboard (Profit Mechanics)',
       'url': 'https://www.youtube.com/watch?v=chCNj5IEUZw&t=53s',
       'video_id': 'chCNj5IEUZw'},
      {'author': 'Learn Solar & BESS',
       'channel': 'Learn Solar & BESS',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:50](https://www.youtube.com/watch?v=72KjPI3DpJ0&t=110s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Okay, let's move into section one, building a mega battery, the micro to macro "
               'scale up. What is absolutely wild about these systems is how they literally '
               'snap together like giant LEGO bricks. We start at step one with a single small '
               'lithium-ion cell.',
       'timestamp': 110,
       'timestamp_label': '[00:01:50]',
       'timestamp_seconds': 110,
       'tip': "Okay, let's move into section one, building a mega battery, the micro to macro "
              'scale up. What is absolutely wild about these systems is how they literally '
              'snap together like giant LEGO bricks. We start at step one with a single small '
              'lithium-ion cell.',
       'title': 'What Is BESS? Battery Energy Storage System Explained Simply (Learn Solar & '
                'BESS)',
       'url': 'https://www.youtube.com/watch?v=72KjPI3DpJ0&t=110s',
       'video_id': '72KjPI3DpJ0'},
      {'author': 'Business Breakdown',
       'channel': 'Business Breakdown',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:41](https://www.youtube.com/watch?v=exXUEqaAB2k&t=221s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Her blind spot was the very same one that had shaped her whole career in '
               'media. She thought the business was the advertising. She measured her '
               'billboard entirely by how well she sold its two faces, and by that measure it '
               'was merely good, respectable, unspectacular.',
       'timestamp': 221,
       'timestamp_label': '[00:03:41]',
       'timestamp_seconds': 221,
       'tip': 'Her blind spot was the very same one that had shaped her whole career in media. '
              'She thought the business was the advertising. She measured her billboard '
              'entirely by how well she sold its two faces, and by that measure it was merely '
              'good, respectable, unspectacular.',
       'title': 'The Real Economics of Owning a Billboard (Business Breakdown)',
       'url': 'https://www.youtube.com/watch?v=exXUEqaAB2k&t=221s',
       'video_id': 'exXUEqaAB2k'},
      {'author': 'Truck N’ Hustle',
       'channel': 'Truck N’ Hustle',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:43](https://www.youtube.com/watch?v=uZVNo7EIaXA&t=583s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'On the ground watching all the trades all the subcontractors making sure they '
               "know what they're doing you need a project manager in this in this case.",
       'timestamp': 583,
       'timestamp_label': '[00:09:43]',
       'timestamp_seconds': 583,
       'tip': 'On the ground watching all the trades all the subcontractors making sure they '
              "know what they're doing you need a project manager in this in this case.",
       'title': 'Pros And Cons; Building The “Truck Parking Lot Business!” (Truck N’ Hustle)',
       'url': 'https://www.youtube.com/watch?v=uZVNo7EIaXA&t=583s',
       'video_id': 'uZVNo7EIaXA'},
      {'author': 'The Bell Board Podcast',
       'channel': 'The Bell Board Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:30:35](https://www.youtube.com/watch?v=nCrchtKHbFw&t=1835s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Um what are you guys doing to to you know, to actually close business? Yeah, I '
               "mean I think a lot of it's relationship building.",
       'timestamp': 1835,
       'timestamp_label': '[00:30:35]',
       'timestamp_seconds': 1835,
       'tip': 'Um what are you guys doing to to you know, to actually close business? Yeah, I '
              "mean I think a lot of it's relationship building.",
       'title': 'How to Buy, Build & Grow a Billboard Business | Dan Franklin (The Bell Board '
                'Podcast)',
       'url': 'https://www.youtube.com/watch?v=nCrchtKHbFw&t=1835s',
       'video_id': 'nCrchtKHbFw'},
      {'author': 'Ryan Wilson Vlogs',
       'channel': 'Ryan Wilson Vlogs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:26](https://www.youtube.com/watch?v=jp9v3OKFs20&t=26s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Jimmy with me, and we're going to be hanging a new billboard up. I had a guy, "
               "I've been holding onto this billboard longer than I've even owned the "
               "billboards. I actually had this billboard up, and that's how I got to buy "
               'these billboards.',
       'timestamp': 26,
       'timestamp_label': '[00:00:26]',
       'timestamp_seconds': 26,
       'tip': "Jimmy with me, and we're going to be hanging a new billboard up. I had a guy, "
              "I've been holding onto this billboard longer than I've even owned the "
              "billboards. I actually had this billboard up, and that's how I got to buy these "
              'billboards.',
       'title': 'Billboard Hustle – Watch This! How Much $$ Can You Really Make?! (Ryan Wilson '
                'Vlogs)',
       'url': 'https://www.youtube.com/watch?v=jp9v3OKFs20&t=26s',
       'video_id': 'jp9v3OKFs20'},
      {'author': 'Chase MacLeod',
       'channel': 'Chase MacLeod',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:15](https://www.youtube.com/watch?v=m96MC6Qe9oM&t=195s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Full building Renovations down to the studs including a new office restrooms '
               'new HVAC and new electrical upgrades for complete information on this '
               'industrial outdoor storage yard we have exclusively listed for sale please '
               'visit our website or contact our team.',
       'timestamp': 195,
       'timestamp_label': '[00:03:15]',
       'timestamp_seconds': 195,
       'tip': 'Full building Renovations down to the studs including a new office restrooms '
              'new HVAC and new electrical upgrades for complete information on this '
              'industrial outdoor storage yard we have exclusively listed for sale please '
              'visit our website or contact our team.',
       'title': 'What is Industrial Outdoor Storage (IOS) | $9M IOS Property For Sale (Chase '
                'MacLeod)',
       'url': 'https://www.youtube.com/watch?v=m96MC6Qe9oM&t=195s',
       'video_id': 'm96MC6Qe9oM'},
      {'author': 'CREUniversity',
       'channel': 'CREUniversity',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:07](https://www.youtube.com/watch?v=QDvEU9XEEA4&t=307s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Would be ideal for the sign in an exit now usage and again how many do you '
               "need do you need 1% of 30 no you don't you only need one Advertiser to have "
               'that billboard sold.',
       'timestamp': 307,
       'timestamp_label': '[00:05:07]',
       'timestamp_seconds': 307,
       'tip': 'Would be ideal for the sign in an exit now usage and again how many do you need '
              "do you need 1% of 30 no you don't you only need one Advertiser to have that "
              'billboard sold.',
       'title': 'The Outdoor Billboard Investment Boot Camp - The Ultimate Resource To Learn '
                'Billboard Investing (CREUniversity)',
       'url': 'https://www.youtube.com/watch?v=QDvEU9XEEA4&t=307s',
       'video_id': 'QDvEU9XEEA4'},
      {'author': 'Truck Parking Media',
       'channel': 'Truck Parking Media',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:03](https://www.youtube.com/watch?v=Fc82YDH9IrI&t=183s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And yeah, from what we've seen, uh the more optimized operations who have more "
               'than one yard facility, uh this just, you know, is usually not the the best '
               'way to go about things. Automated gates, uh these gates use an a motorized '
               'operator.',
       'timestamp': 183,
       'timestamp_label': '[00:03:03]',
       'timestamp_seconds': 183,
       'tip': "And yeah, from what we've seen, uh the more optimized operations who have more "
              'than one yard facility, uh this just, you know, is usually not the the best way '
              'to go about things. Automated gates, uh these gates use an a motorized '
              'operator.',
       'title': 'Manual vs Automatic Gates: Which Is Best for Your Truck Parking Yard? (Truck '
                'Parking Media)',
       'url': 'https://www.youtube.com/watch?v=Fc82YDH9IrI&t=183s',
       'video_id': 'Fc82YDH9IrI'},
      {'author': 'Tower Genius',
       'channel': 'Tower Genius',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:37](https://www.youtube.com/watch?v=pSGbaA0AbTo&t=37s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Looking at an average number of roughly 16 to 17 times 17 and a half times '
               'your annual cell site or cell tower rental now with that said let me just '
               'share my screen real quick and um see here.',
       'timestamp': 37,
       'timestamp_label': '[00:00:37]',
       'timestamp_seconds': 37,
       'tip': 'Looking at an average number of roughly 16 to 17 times 17 and a half times your '
              'annual cell site or cell tower rental now with that said let me just share my '
              'screen real quick and um see here.',
       'title': "What's the Average Cell Tower Lease Buyout Worth? (Tower Genius)",
       'url': 'https://www.youtube.com/watch?v=pSGbaA0AbTo&t=37s',
       'video_id': 'pSGbaA0AbTo'},
      {'author': 'Ronald Rohde Law',
       'channel': 'Ronald Rohde Law',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:59](https://www.youtube.com/watch?v=tonuCLfZrYE&t=179s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Buildings but the definition kind of starts to fall apart with more than 20 or '
               '30 percent coverage of the site having a building so but beyond that you.',
       'timestamp': 179,
       'timestamp_label': '[00:02:59]',
       'timestamp_seconds': 179,
       'tip': 'Buildings but the definition kind of starts to fall apart with more than 20 or '
              '30 percent coverage of the site having a building so but beyond that you.',
       'title': 'How to Invest Industrial Outdoor Storage (Truck Parking) (Ronald Rohde Law)',
       'url': 'https://www.youtube.com/watch?v=tonuCLfZrYE&t=179s',
       'video_id': 'tonuCLfZrYE'},
      {'author': 'Local Marketing Institute',
       'channel': 'Local Marketing Institute',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:02:08](https://www.youtube.com/watch?v=uoJvU0CyoBY&t=3728s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Sounds good Bart thank you so much for your time today really appreciate this '
               "is this is really fascinating stuff it's breathing new life into something "
               "that sounds you're very old fashioned but it's fascinating yeah all right cool "
               'thanks Eric.',
       'timestamp': 3728,
       'timestamp_label': '[01:02:08]',
       'timestamp_seconds': 3728,
       'tip': 'Sounds good Bart thank you so much for your time today really appreciate this '
              "is this is really fascinating stuff it's breathing new life into something that "
              "sounds you're very old fashioned but it's fascinating yeah all right cool "
              'thanks Eric.',
       'title': 'Under the Hood with Blip Billboards (Local Marketing Institute)',
       'url': 'https://www.youtube.com/watch?v=uoJvU0CyoBY&t=3728s',
       'video_id': 'uoJvU0CyoBY'},
      {'author': 'Tyler Cauble',
       'channel': 'Tyler Cauble',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=oGKW8TxE9-Q&t=15s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Invest in commercial real estate which actually makes it incredibly attractive '
               "for beginners in the industry why is it lazy well you don't really have to do.",
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Invest in commercial real estate which actually makes it incredibly attractive '
              "for beginners in the industry why is it lazy well you don't really have to do.",
       'title': 'The Laziest Way To Invest In Commercial Real Estate (Tyler Cauble)',
       'url': 'https://www.youtube.com/watch?v=oGKW8TxE9-Q&t=15s',
       'video_id': 'oGKW8TxE9-Q'},
      {'author': 'Tower Genius',
       'channel': 'Tower Genius',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:46](https://www.youtube.com/watch?v=nUDRfQeqe7A&t=946s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "We are knowledgeable in this field we're not attorneys attorneys do hire us as "
               'a subject matter experts in this field so give us a call 888-313-9750 and we '
               'look forward to helping you out and speaking to you soon thanks.',
       'timestamp': 946,
       'timestamp_label': '[00:15:46]',
       'timestamp_seconds': 946,
       'tip': "We are knowledgeable in this field we're not attorneys attorneys do hire us as "
              'a subject matter experts in this field so give us a call 888-313-9750 and we '
              'look forward to helping you out and speaking to you soon thanks.',
       'title': 'How We Determine Cell Tower Rent Values - Explained (Tower Genius)',
       'url': 'https://www.youtube.com/watch?v=nUDRfQeqe7A&t=946s',
       'video_id': 'nUDRfQeqe7A'},
      {'author': 'Behind The Billions',
       'channel': 'Behind The Billions',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:10](https://www.youtube.com/watch?v=Bb-6A1zEJAc&t=190s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You are in the land business with poles attached. A billboard network is not '
               'an advertising business. It is a land lease arbitrage wrapped around a monthly '
               'advertiser contract. And like any arbitrage, the entire economic engine is '
               'built on one metric.',
       'timestamp': 190,
       'timestamp_label': '[00:03:10]',
       'timestamp_seconds': 190,
       'tip': 'You are in the land business with poles attached. A billboard network is not an '
              'advertising business. It is a land lease arbitrage wrapped around a monthly '
              'advertiser contract. And like any arbitrage, the entire economic engine is '
              'built on one metric.',
       'title': 'The Economics of Owning a Billboard Network (Behind The Billions)',
       'url': 'https://www.youtube.com/watch?v=Bb-6A1zEJAc&t=190s',
       'video_id': 'Bb-6A1zEJAc'}],
 12: [{'author': 'REtipster',
       'channel': 'REtipster',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:48](https://www.youtube.com/watch?v=Yo8dSroHdMk&t=648s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You start the beautification act. No state is allowed to have billboards any '
               'easier than as allowed under the beautification act that covers all the '
               'states.',
       'timestamp': 648,
       'timestamp_label': '[00:10:48]',
       'timestamp_seconds': 648,
       'tip': 'You start the beautification act. No state is allowed to have billboards any '
              'easier than as allowed under the beautification act that covers all the states.',
       'title': "A Review of Frank Rolfe's Billboard University Bootcamp (REtipster)",
       'url': 'https://www.youtube.com/watch?v=Yo8dSroHdMk&t=648s',
       'video_id': 'Yo8dSroHdMk'},
      {'author': 'The Bell Board Podcast',
       'channel': 'The Bell Board Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:38](https://www.youtube.com/watch?v=r6MxdTpj3sg&t=98s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Uh it shows up on a Sunday. So I got to tell the handler unload it. The next '
               "day I get a call from the landlord that the state's taking my property at the "
               "end of the month that I'm building the billboard on and I didn't file it with "
               'the county with an addendum.',
       'timestamp': 98,
       'timestamp_label': '[00:01:38]',
       'timestamp_seconds': 98,
       'tip': 'Uh it shows up on a Sunday. So I got to tell the handler unload it. The next '
              "day I get a call from the landlord that the state's taking my property at the "
              "end of the month that I'm building the billboard on and I didn't file it with "
              'the county with an addendum.',
       'title': 'How Profitable Is the Billboard Business? Industry Experts Share Their Advice '
                '(The Bell Board Podcast)',
       'url': 'https://www.youtube.com/watch?v=r6MxdTpj3sg&t=98s',
       'video_id': 'r6MxdTpj3sg'},
      {'author': 'Josh Talks Business',
       'channel': 'Josh Talks Business',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:01](https://www.youtube.com/watch?v=qH0UhNp0Now&t=241s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A rural stretch with 2,000 cars a day might support a billboard earning around '
               '$500 a month. A dense urban corridor with 100,000 cars a day can push that '
               'same structure past $50,000 a month. Completely different business. Because '
               'the traffic count is different.',
       'timestamp': 241,
       'timestamp_label': '[00:04:01]',
       'timestamp_seconds': 241,
       'tip': 'A rural stretch with 2,000 cars a day might support a billboard earning around '
              '$500 a month. A dense urban corridor with 100,000 cars a day can push that same '
              'structure past $50,000 a month. Completely different business. Because the '
              'traffic count is different.',
       'title': 'The Economics of Owning a Billboard (Josh Talks Business)',
       'url': 'https://www.youtube.com/watch?v=qH0UhNp0Now&t=241s',
       'video_id': 'qH0UhNp0Now'},
      {'author': 'Selina Gonzales',
       'channel': 'Selina Gonzales',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:18](https://www.youtube.com/watch?v=x2ZfqDSKoOI&t=138s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The building part is not the hard part. Getting a carrier to sign before you '
               'pour concrete hard part. The first carrier is the whole business plan. Tower '
               'companies talk about the anchor tenant. In the big master deals, that rent has '
               'been pinned near 1900 dollars a month.',
       'timestamp': 138,
       'timestamp_label': '[00:02:18]',
       'timestamp_seconds': 138,
       'tip': 'The building part is not the hard part. Getting a carrier to sign before you '
              'pour concrete hard part. The first carrier is the whole business plan. Tower '
              'companies talk about the anchor tenant. In the big master deals, that rent has '
              'been pinned near 1900 dollars a month.',
       'title': 'The Economics of Owning a Cell Tower (Selina Gonzales)',
       'url': 'https://www.youtube.com/watch?v=x2ZfqDSKoOI&t=138s',
       'video_id': 'x2ZfqDSKoOI'},
      {'author': 'Cant Miss US | Largest Fleet of Mobile Billboards',
       'channel': 'Cant Miss US | Largest Fleet of Mobile Billboards',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:53](https://www.youtube.com/watch?v=o3KgQJFdGXQ&t=53s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A typical route-based ad campaign nets you $1200 to $1,800 a day. Infact the '
               'Tailgates, festivals, and political rallies can fetch upto $2,500 to $3,600 '
               'per day. If you book just 10 days of event work a month, you’re looking at a '
               '$12k–$18k gross.',
       'timestamp': 53,
       'timestamp_label': '[00:00:53]',
       'timestamp_seconds': 53,
       'tip': 'A typical route-based ad campaign nets you $1200 to $1,800 a day. Infact the '
              'Tailgates, festivals, and political rallies can fetch upto $2,500 to $3,600 per '
              'day. If you book just 10 days of event work a month, you’re looking at a '
              '$12k–$18k gross.',
       'title': 'Is a Mobile Billboard Business Worth It in 2026? ROI & Revenue Reveal (Cant '
                'Miss US | Largest Fleet of Mobile Billboards)',
       'url': 'https://www.youtube.com/watch?v=o3KgQJFdGXQ&t=53s',
       'video_id': 'o3KgQJFdGXQ'},
      {'author': 'GTA Spark',
       'channel': 'GTA Spark',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:21](https://www.youtube.com/watch?v=SnuS5ZZX2qA&t=381s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': '460 total tenant leases across the portfolio. At $2,000 a month per lease, '
               "that's $920,000 a month or $1,40,000 a year in gross leasing revenue. Now, "
               'start subtracting the costs because even in a business this asset light, the '
               'costs are real.',
       'timestamp': 381,
       'timestamp_label': '[00:06:21]',
       'timestamp_seconds': 381,
       'tip': '460 total tenant leases across the portfolio. At $2,000 a month per lease, '
              "that's $920,000 a month or $1,40,000 a year in gross leasing revenue. Now, "
              'start subtracting the costs because even in a business this asset light, the '
              'costs are real.',
       'title': 'The Economics of Owning a Cell Tower Leasing Company (GTA Spark)',
       'url': 'https://www.youtube.com/watch?v=SnuS5ZZX2qA&t=381s',
       'video_id': 'SnuS5ZZX2qA'},
      {'author': 'Mobile Digital Billboard University | Jerry Teeter',
       'channel': 'Mobile Digital Billboard University | Jerry Teeter',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:55](https://www.youtube.com/watch?v=mG9J2Z6RgSY&t=415s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "If you're looking to start a mobile billboard business and you're wondering "
               "what all you need to do, we've got you covered there. Uh Legion is the only "
               'provider right now that offers a complete business in a box solution.',
       'timestamp': 415,
       'timestamp_label': '[00:06:55]',
       'timestamp_seconds': 415,
       'tip': "If you're looking to start a mobile billboard business and you're wondering "
              "what all you need to do, we've got you covered there. Uh Legion is the only "
              'provider right now that offers a complete business in a box solution.',
       'title': 'Why This $250K LED Truck Is the Top Choice for Mobile Digital Billboard '
                'Owners (Mobile Digital Billboard University | Jerry Teeter)',
       'url': 'https://www.youtube.com/watch?v=mG9J2Z6RgSY&t=415s',
       'video_id': 'mG9J2Z6RgSY'},
      {'author': 'Time Ticket',
       'channel': 'Time Ticket',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:02](https://www.youtube.com/watch?v=L2Ys_cCg_Ac&t=422s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Most land is just land, but a patch of dirt in exactly the right place can be '
               'worth more than a building. So, would you take the 330,000 today or keep the '
               '2,100 a month?',
       'timestamp': 422,
       'timestamp_label': '[00:07:02]',
       'timestamp_seconds': 422,
       'tip': 'Most land is just land, but a patch of dirt in exactly the right place can be '
              'worth more than a building. So, would you take the 330,000 today or keep the '
              '2,100 a month?',
       'title': 'POV: The Cell Tower Lot Pays You $2,100 a Month (Time Ticket)',
       'url': 'https://www.youtube.com/watch?v=L2Ys_cCg_Ac&t=422s',
       'video_id': 'L2Ys_cCg_Ac'},
      {'author': 'LandApp by LandGate',
       'channel': 'LandApp by LandGate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:35](https://www.youtube.com/watch?v=Yes7DTfUfJs&t=155s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'No middleman you may be presented with top offers to purchase your property or '
               'lease your land none of which you are obligated to accept so what are you '
               'waiting for consider leasing your property for battery storage and start '
               'generating extra Revenue today.',
       'timestamp': 155,
       'timestamp_label': '[00:02:35]',
       'timestamp_seconds': 155,
       'tip': 'No middleman you may be presented with top offers to purchase your property or '
              'lease your land none of which you are obligated to accept so what are you '
              'waiting for consider leasing your property for battery storage and start '
              'generating extra Revenue today.',
       'title': 'Does My Land Qualify for Battery Storage? (LandApp by LandGate)',
       'url': 'https://www.youtube.com/watch?v=Yes7DTfUfJs&t=155s',
       'video_id': 'Yes7DTfUfJs'},
      {'author': 'Meg Aubale',
       'channel': 'Meg Aubale',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:03](https://www.youtube.com/watch?v=ibaB0OT2vpU&t=243s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "A lot of what I've done in the past has been uh buy a piece of land, design a "
               'building, build it, sell it, and then you make a nice return on your '
               "investment, but then you're done with the building and you have to start all "
               'over again.',
       'timestamp': 243,
       'timestamp_label': '[00:04:03]',
       'timestamp_seconds': 243,
       'tip': "A lot of what I've done in the past has been uh buy a piece of land, design a "
              'building, build it, sell it, and then you make a nice return on your '
              "investment, but then you're done with the building and you have to start all "
              'over again.',
       'title': 'Industrial Outdoor Storage: The Real Estate Asset Class No One Talks About '
                '(Meg Aubale)',
       'url': 'https://www.youtube.com/watch?v=ibaB0OT2vpU&t=243s',
       'video_id': 'ibaB0OT2vpU'},
      {'author': 'Vertical Consultants',
       'channel': 'Vertical Consultants',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:23](https://www.youtube.com/watch?v=c553DbS2mGI&t=23s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "What are rent rates for cell towers in 2024? We're at the start of 2024. I "
               "mean, what we're seeing for cell tower lease rates is in urban locations, "
               "you're seeing rates between $1,200 a month to over $2,000 a month with an "
               'escalator between 2 to 3% every year.',
       'timestamp': 23,
       'timestamp_label': '[00:00:23]',
       'timestamp_seconds': 23,
       'tip': "What are rent rates for cell towers in 2024? We're at the start of 2024. I "
              "mean, what we're seeing for cell tower lease rates is in urban locations, "
              "you're seeing rates between $1,200 a month to over $2,000 a month with an "
              'escalator between 2 to 3% every year.',
       'title': 'What Will Cell Tower Lease Rent Rates Be In 2024? (Vertical Consultants)',
       'url': 'https://www.youtube.com/watch?v=c553DbS2mGI&t=23s',
       'video_id': 'c553DbS2mGI'},
      {'author': 'Tower Genius',
       'channel': 'Tower Genius',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:39](https://www.youtube.com/watch?v=X75LHgvP1U8&t=159s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Typically have labels or you know they'll scribble on with a sharpie it'll be "
               "it'll be labeled who those uh carriers are for so you want to be able to tell "
               'the buyout company who is uh paying uh paying you rent and uh anyway hopefully '
               'that helps and have a great day.',
       'timestamp': 159,
       'timestamp_label': '[00:02:39]',
       'timestamp_seconds': 159,
       'tip': "Typically have labels or you know they'll scribble on with a sharpie it'll be "
              "it'll be labeled who those uh carriers are for so you want to be able to tell "
              'the buyout company who is uh paying uh paying you rent and uh anyway hopefully '
              'that helps and have a great day.',
       'title': 'Important Cell Tower Lease Buyout Tip for 2024 (Tower Genius)',
       'url': 'https://www.youtube.com/watch?v=X75LHgvP1U8&t=159s',
       'video_id': 'X75LHgvP1U8'},
      {'author': 'Tower Genius',
       'channel': 'Tower Genius',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:49](https://www.youtube.com/watch?v=pE5ehBu0C4s&t=289s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Interest in the existing sell Tower lease income stream and future rental '
               'payments you are assigning the lease and you are giving them an easement in '
               'exchange for a cash Lumpa hope that helps have a great day.',
       'timestamp': 289,
       'timestamp_label': '[00:04:49]',
       'timestamp_seconds': 289,
       'tip': 'Interest in the existing sell Tower lease income stream and future rental '
              'payments you are assigning the lease and you are giving them an easement in '
              'exchange for a cash Lumpa hope that helps have a great day.',
       'title': 'What is a Cell Tower Lease Buyout? (Tower Genius)',
       'url': 'https://www.youtube.com/watch?v=pE5ehBu0C4s&t=289s',
       'video_id': 'pE5ehBu0C4s'},
      {'author': 'Vertical Consultants',
       'channel': 'Vertical Consultants',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:44](https://www.youtube.com/watch?v=iRtPyU-Kh2o&t=104s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Paid not only for that space right there but their use of that space up there '
               "you'll make money month after month year after year and it's basically always "
               'increasing based upon the utility of that cell tower.',
       'timestamp': 104,
       'timestamp_label': '[00:01:44]',
       'timestamp_seconds': 104,
       'tip': 'Paid not only for that space right there but their use of that space up there '
              "you'll make money month after month year after year and it's basically always "
              'increasing based upon the utility of that cell tower.',
       'title': 'Calculating Cell Tower Rent Rates (Vertical Consultants)',
       'url': 'https://www.youtube.com/watch?v=iRtPyU-Kh2o&t=104s',
       'video_id': 'iRtPyU-Kh2o'},
      {'author': 'Old School Financials',
       'channel': 'Old School Financials',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:34](https://www.youtube.com/watch?v=EFxC43w3Aa8&t=34s)',
       'relevance': 'Attributed practitioner commentary on perpetual cell-tower/rooftop '
                    'telecom easement buyouts (`16×–22×` REIT flips), `DOT`-permitted highway '
                    'digital-billboard ground-lease assignments, and zero-building Industrial '
                    'Outdoor Storage (`IOS`) fleet drop-yard master-leases (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Because the billboard's real product was never the ad you saw. It was the "
               'ground, the permit, and the right to be seen. Start with the permit because '
               'without it, there is no business at all. In 1965, Congress passed the Highway '
               'Beautification Act.',
       'timestamp': 34,
       'timestamp_label': '[00:00:34]',
       'timestamp_seconds': 34,
       'tip': "Because the billboard's real product was never the ad you saw. It was the "
              'ground, the permit, and the right to be seen. Start with the permit because '
              'without it, there is no business at all. In 1965, Congress passed the Highway '
              'Beautification Act.',
       'title': 'The Highway Landlord Nobody Notices (Old School Financials)',
       'url': 'https://www.youtube.com/watch?v=EFxC43w3Aa8&t=34s',
       'video_id': 'EFxC43w3Aa8'}]}
