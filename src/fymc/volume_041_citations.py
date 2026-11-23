"""Curated 180-citation Buying Group, Card-Float & Ticket Allocation Arbitrage baseline (15 per chapter across Q1-Q12) mined strictly from verified Buying Group, Card-Float & Ticket Allocation Arbitrage YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'1099',
     '150k',
     '45c',
     'account',
     'accounting',
     'ach',
     'act',
     'alerts',
     'algorithms',
     'all',
     'allocation',
     'amex',
     'annual',
     'arbitrage',
     'artist',
     'auto',
     'automation',
     'automatiq',
     'avoiding',
     'axs',
     'bank',
     'barcode',
     'below',
     'bonus',
     'bonuses',
     'bots',
     'break',
     'breakdown',
     'bricks',
     'broker',
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
 2: {'1099',
     '150k',
     '45c',
     'account',
     'accounting',
     'ach',
     'act',
     'alerts',
     'algorithms',
     'all',
     'allocation',
     'amex',
     'annual',
     'arbitrage',
     'artist',
     'auto',
     'automation',
     'automatiq',
     'avoiding',
     'axs',
     'bank',
     'barcode',
     'below',
     'bonus',
     'bonuses',
     'bots',
     'break',
     'breakdown',
     'bricks',
     'broker',
     'budget',
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
 3: {'1099',
     '150k',
     '45c',
     'account',
     'accounting',
     'ach',
     'act',
     'alerts',
     'algorithms',
     'all',
     'allocation',
     'amex',
     'annual',
     'arbitrage',
     'artist',
     'auto',
     'automation',
     'automatiq',
     'avoiding',
     'axs',
     'bank',
     'barcode',
     'below',
     'bonus',
     'bonuses',
     'bots',
     'break',
     'breakdown',
     'bricks',
     'broker',
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
 4: {'1099',
     '150k',
     '45c',
     'account',
     'accounting',
     'ach',
     'act',
     'alerts',
     'algorithms',
     'all',
     'allocation',
     'amex',
     'annual',
     'arbitrage',
     'artist',
     'auto',
     'automation',
     'automatiq',
     'avoiding',
     'axs',
     'bank',
     'barcode',
     'below',
     'bonus',
     'bonuses',
     'bots',
     'break',
     'breakdown',
     'bricks',
     'broker',
     'budget',
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
 5: {'1099',
     '150k',
     '45c',
     'account',
     'accounting',
     'ach',
     'act',
     'alerts',
     'algorithms',
     'all',
     'allocation',
     'amex',
     'annual',
     'arbitrage',
     'artist',
     'audit',
     'auto',
     'automation',
     'automatiq',
     'avoid',
     'avoiding',
     'axs',
     'bank',
     'barcode',
     'below',
     'bonus',
     'bonuses',
     'bots',
     'break',
     'breakdown',
     'bricks',
     'broker',
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
 6: {'1099',
     '150k',
     '45c',
     'account',
     'accounting',
     'ach',
     'act',
     'alerts',
     'algorithms',
     'all',
     'allocation',
     'amex',
     'annual',
     'arbitrage',
     'artist',
     'auto',
     'automation',
     'automatiq',
     'avoiding',
     'axs',
     'bank',
     'barcode',
     'below',
     'bonus',
     'bonuses',
     'bots',
     'break',
     'breakdown',
     'bricks',
     'broker',
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
 7: {'1099',
     '150k',
     '45c',
     'account',
     'accounting',
     'ach',
     'act',
     'alerts',
     'algorithms',
     'all',
     'allocation',
     'amex',
     'annual',
     'arbitrage',
     'artist',
     'auto',
     'automation',
     'automatiq',
     'avoiding',
     'axs',
     'bank',
     'barcode',
     'below',
     'bonus',
     'bonuses',
     'bots',
     'break',
     'breakdown',
     'bricks',
     'broker',
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
 8: {'1099',
     '150k',
     '45c',
     'account',
     'accounting',
     'ach',
     'act',
     'alerts',
     'algorithms',
     'all',
     'allocation',
     'amex',
     'annual',
     'api',
     'arbitrage',
     'artist',
     'auto',
     'automation',
     'automatiq',
     'avoiding',
     'axs',
     'bank',
     'barcode',
     'below',
     'bonus',
     'bonuses',
     'bots',
     'break',
     'breakdown',
     'bricks',
     'broker',
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
 9: {'1099',
     '150k',
     '45c',
     'account',
     'accounting',
     'ach',
     'act',
     'agreement',
     'alerts',
     'algorithms',
     'all',
     'allocation',
     'amex',
     'annual',
     'arbitrage',
     'artist',
     'auto',
     'automation',
     'automatiq',
     'avoiding',
     'axs',
     'bank',
     'barcode',
     'below',
     'bonus',
     'bonuses',
     'bots',
     'break',
     'breakdown',
     'bricks',
     'broker',
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
 10: {'1099',
      '150k',
      '45c',
      'account',
      'accounting',
      'ach',
      'act',
      'agent',
      'ai',
      'alerts',
      'algorithms',
      'all',
      'allocation',
      'amex',
      'annual',
      'arbitrage',
      'artist',
      'auto',
      'automate',
      'automation',
      'automatiq',
      'avoiding',
      'axs',
      'bank',
      'barcode',
      'below',
      'bonus',
      'bonuses',
      'bots',
      'break',
      'breakdown',
      'bricks',
      'broker',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'1099',
      '150k',
      '45c',
      'account',
      'accounting',
      'ach',
      'act',
      'alerts',
      'algorithms',
      'all',
      'allocation',
      'amex',
      'annual',
      'arbitrage',
      'artist',
      'auto',
      'automation',
      'automatiq',
      'avoiding',
      'axs',
      'bank',
      'barcode',
      'below',
      'bonus',
      'bonuses',
      'bots',
      'break',
      'breakdown',
      'bricks',
      'broker',
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
 12: {'1099',
      '150k',
      '45c',
      'account',
      'accounting',
      'ach',
      'act',
      'action',
      'alerts',
      'algorithms',
      'all',
      'allocation',
      'amex',
      'annual',
      'arbitrage',
      'artist',
      'auto',
      'automation',
      'automatiq',
      'avoiding',
      'axs',
      'bank',
      'barcode',
      'below',
      'bonus',
      'bonuses',
      'bots',
      'break',
      'breakdown',
      'bricks',
      'broker',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'CREDNCARD',
      'channel': 'CREDNCARD',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:40](https://www.youtube.com/watch?v=9HLY-5lw8uA&t=520s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Before applying, take your previous 12 months of business transactions and '
              'model them against the current earning rules, annual fees, credits, payment '
              'requirements, and redemption options of both cards. Then, calculate the '
              'expected net value after fees.',
      'timestamp': 520,
      'timestamp_label': '[00:08:40]',
      'timestamp_seconds': 520,
      'tip': 'Before applying, take your previous 12 months of business transactions and model '
             'them against the current earning rules, annual fees, credits, payment '
             'requirements, and redemption options of both cards. Then, calculate the expected '
             'net value after fees.',
      'title': 'Capital One Venture X Business vs. Amex Business Platinum: Spending Tier '
               'Strategy (CREDNCARD)',
      'url': 'https://www.youtube.com/watch?v=9HLY-5lw8uA&t=520s',
      'video_id': '9HLY-5lw8uA'},
     {'author': 'Law & Business',
      'channel': 'Law & Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=VTeJfmUSPYg&t=51s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The concert seat ticket master's implementation often branded as official "
              'platinum ensures that the primary market captures the arbitrage value. The '
              'algorithm continuously forecasts the demand curve setting the price point where '
              'marginal revenue equals marginal cost.',
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': "The concert seat ticket master's implementation often branded as official "
             'platinum ensures that the primary market captures the arbitrage value. The '
             'algorithm continuously forecasts the demand curve setting the price point where '
             'marginal revenue equals marginal cost.',
      'title': 'Ticketmaster Dynamic Pricing Algorithms (Law & Business)',
      'url': 'https://www.youtube.com/watch?v=VTeJfmUSPYg&t=51s',
      'video_id': 'VTeJfmUSPYg'},
     {'author': "Jake's Tech Lab",
      'channel': "Jake's Tech Lab",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:14](https://www.youtube.com/watch?v=jSUO2McsAa8&t=194s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Business Cash is the clear winner. We all like keeping more money, right? '
              'Business Cash can net you up to $1,250 every year from category bonuses without '
              "an annual fee? That's pretty awesome for small businesses.",
      'timestamp': 194,
      'timestamp_label': '[00:03:14]',
      'timestamp_seconds': 194,
      'tip': 'Business Cash is the clear winner. We all like keeping more money, right? '
             'Business Cash can net you up to $1,250 every year from category bonuses without '
             "an annual fee? That's pretty awesome for small businesses.",
      'title': 'Ink Business Cash vs Capital One Spark Cash Plus Comparison 2026 | Best '
               "Business Credit Card? (Jake's Tech Lab)",
      'url': 'https://www.youtube.com/watch?v=jSUO2McsAa8&t=194s',
      'video_id': 'jSUO2McsAa8'},
     {'author': 'Joe Barreto',
      'channel': 'Joe Barreto',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:05](https://www.youtube.com/watch?v=xgsxM7jSJ8U&t=725s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm giving you the warning today on Friday, October 24th. Keep your personal "
              'stuff personal. Keep your business stuff on the business side. Try not to mix '
              'both worlds together. Pay your accounts with your own bank accounts, not '
              "somebody else's account.",
      'timestamp': 725,
      'timestamp_label': '[00:12:05]',
      'timestamp_seconds': 725,
      'tip': "I'm giving you the warning today on Friday, October 24th. Keep your personal "
             'stuff personal. Keep your business stuff on the business side. Try not to mix '
             'both worlds together. Pay your accounts with your own bank accounts, not '
             "somebody else's account.",
      'title': 'The REAL Reason Amex Is Closing Customer Accounts Suddenly (Joe Barreto)',
      'url': 'https://www.youtube.com/watch?v=xgsxM7jSJ8U&t=725s',
      'video_id': 'xgsxM7jSJ8U'},
     {'author': 'Daily Drop',
      'channel': 'Daily Drop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:57](https://www.youtube.com/watch?v=aO-QS7hMLE0&t=297s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Obviously, if you don't have a business or don't travel at all for business, "
              "then you're not going to get the value out of the travel credits or lounge "
              'perks.',
      'timestamp': 297,
      'timestamp_label': '[00:04:57]',
      'timestamp_seconds': 297,
      'tip': "Obviously, if you don't have a business or don't travel at all for business, "
             "then you're not going to get the value out of the travel credits or lounge "
             'perks.',
      'title': 'Capital One Venture X Business Review | #1 Business Card? (Daily Drop)',
      'url': 'https://www.youtube.com/watch?v=aO-QS7hMLE0&t=297s',
      'video_id': 'aO-QS7hMLE0'},
     {'author': 'KC_Watermark',
      'channel': 'KC_Watermark',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:48](https://www.youtube.com/watch?v=Ze2ODb4Bm6g&t=288s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Flag one: this business is shrinking. Eventbrite's annual revenue has come down "
              'from about three hundred twenty-six million dollars to about two hundred '
              'ninety-two million. That is the wrong direction, and it is the main reason the '
              'stock is four dollars and fifty-one cents.',
      'timestamp': 288,
      'timestamp_label': '[00:04:48]',
      'timestamp_seconds': 288,
      'tip': "Flag one: this business is shrinking. Eventbrite's annual revenue has come down "
             'from about three hundred twenty-six million dollars to about two hundred '
             'ninety-two million. That is the wrong direction, and it is the main reason the '
             'stock is four dollars and fifty-one cents.',
      'title': 'The Next Vivid Seats Costs $4.83 — The Ticketing Stock Growing 7% With No '
               'Rescue Deal (KC_Watermark)',
      'url': 'https://www.youtube.com/watch?v=Ze2ODb4Bm6g&t=288s',
      'video_id': 'Ze2ODb4Bm6g'},
     {'author': 'Anthony Venture 2',
      'channel': 'Anthony Venture 2',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=ZSZN6BW7_m0&t=80s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I think that actually might have happened to me, too, with my business platinum '
              "cuz I don't I haven't paid an annual fee on that card. And now that you mention "
              "it I don't I think I paid like a pro rated thing for my Amex business gold, was "
              'not a full 895.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': 'I think that actually might have happened to me, too, with my business platinum '
             "cuz I don't I haven't paid an annual fee on that card. And now that you mention "
             "it I don't I think I paid like a pro rated thing for my Amex business gold, was "
             'not a full 895.',
      'title': 'This Amex Card Upgrade Strategy Nobody Told You Existed (Anthony Venture 2)',
      'url': 'https://www.youtube.com/watch?v=ZSZN6BW7_m0&t=80s',
      'video_id': 'ZSZN6BW7_m0'},
     {'author': 'Pricefx',
      'channel': 'Pricefx',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=mly_b1uoMoM&t=89s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "While there isn't a pure formula for calculating the true market value of a "
              'product or service or a set of conditions that warrant such drastic price '
              "hikes, it's worth exploring the data sources that Ticketmaster uses and its own "
              'pricing to adjust prices.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': "While there isn't a pure formula for calculating the true market value of a "
             'product or service or a set of conditions that warrant such drastic price hikes, '
             "it's worth exploring the data sources that Ticketmaster uses and its own pricing "
             'to adjust prices.',
      'title': "Ticketmaster's Dynamic Pricing (Pricefx)",
      'url': 'https://www.youtube.com/watch?v=mly_b1uoMoM&t=89s',
      'video_id': 'mly_b1uoMoM'},
     {'author': 'Bytes Media',
      'channel': 'Bytes Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:09](https://www.youtube.com/watch?v=_if3NsHr3Lg&t=129s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you rarely use travel portals, carry balances, or run a very small operation '
              'with low monthly spend, the long-term value narrows, and a no fee lower '
              "threshold business card might make more sense. Well, that's all for this video.",
      'timestamp': 129,
      'timestamp_label': '[00:02:09]',
      'timestamp_seconds': 129,
      'tip': 'If you rarely use travel portals, carry balances, or run a very small operation '
             'with low monthly spend, the long-term value narrows, and a no fee lower '
             "threshold business card might make more sense. Well, that's all for this video.",
      'title': 'Capital One Spark Cash Credit Card Review 2026 | Unlimited Business Cash Back, '
               'Rewards & Benefits (Bytes Media)',
      'url': 'https://www.youtube.com/watch?v=_if3NsHr3Lg&t=129s',
      'video_id': '_if3NsHr3Lg'},
     {'author': 'BBC News',
      'channel': 'BBC News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=znwdKE6xlwA&t=62s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re planning to ban any resale for profit. That means whatever you paid for it "
              'will be all you can sell it for. And that should apply to sporting events, too. '
              'Resale websites will still charge service fees, but those could be capped.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': "'re planning to ban any resale for profit. That means whatever you paid for it "
             'will be all you can sell it for. And that should apply to sporting events, too. '
             'Resale websites will still charge service fees, but those could be capped.',
      'title': 'Reselling tickets above face value set to be banned by UK government | BBC '
               'News (BBC News)',
      'url': 'https://www.youtube.com/watch?v=znwdKE6xlwA&t=62s',
      'video_id': 'znwdKE6xlwA'},
     {'author': 'Intuit',
      'channel': 'Intuit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=i-mOkvN7iNE&t=54s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "A business line of credit works differently. It's like having a pool of funds "
              "waiting for you. You don't get a card, instead you transfer money from that "
              'pool into your business account when you need it. Maybe for inventory, '
              'equipment, or covering payroll.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': "A business line of credit works differently. It's like having a pool of funds "
             "waiting for you. You don't get a card, instead you transfer money from that pool "
             'into your business account when you need it. Maybe for inventory, equipment, or '
             'covering payroll.',
      'title': "Business credit cards vs. lines of credit: What's the difference? (2026) "
               '(Intuit)',
      'url': 'https://www.youtube.com/watch?v=i-mOkvN7iNE&t=54s',
      'video_id': 'i-mOkvN7iNE'},
     {'author': 'Marie&leki',
      'channel': 'Marie&leki',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=ZA0a7zheQjQ&t=79s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm not going to say I don't sell my tickets. Whenever I sell sell my tickets "
              "face value and most of the time the tickets I'm definitely selling are the "
              'evening games because all the way from where I live all the way to Seattle and '
              "they usually don't provide transportation.",
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': "I'm not going to say I don't sell my tickets. Whenever I sell sell my tickets "
             "face value and most of the time the tickets I'm definitely selling are the "
             'evening games because all the way from where I live all the way to Seattle and '
             "they usually don't provide transportation.",
      'title': 'seahawks playoff tickets (Marie&leki)',
      'url': 'https://www.youtube.com/watch?v=ZA0a7zheQjQ&t=79s',
      'video_id': 'ZA0a7zheQjQ'},
     {'author': 'StartUp101',
      'channel': 'StartUp101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:23](https://www.youtube.com/watch?v=2N5t8bm1dpA&t=23s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "It's important to note that some states also require a business to obtain a "
              'sales tax permit, even if they are physically operating there and not selling a '
              'taxable product or service.',
      'timestamp': 23,
      'timestamp_label': '[00:00:23]',
      'timestamp_seconds': 23,
      'tip': "It's important to note that some states also require a business to obtain a "
             'sales tax permit, even if they are physically operating there and not selling a '
             'taxable product or service.',
      'title': "Sellers Permit vs Resale Certificate - What's the Difference? (StartUp101)",
      'url': 'https://www.youtube.com/watch?v=2N5t8bm1dpA&t=23s',
      'video_id': '2N5t8bm1dpA'},
     {'author': 'TECH GIANT',
      'channel': 'TECH GIANT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:39](https://www.youtube.com/watch?v=m8toWc8c4lM&t=519s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Spark is a great option but if you want maximum rewards in specific areas or '
              'categories Chase business cards are the way to go let me know in the comments '
              "Which business card you prefer and why thank you for watching and I'll see you "
              'next time.',
      'timestamp': 519,
      'timestamp_label': '[00:08:39]',
      'timestamp_seconds': 519,
      'tip': 'Spark is a great option but if you want maximum rewards in specific areas or '
             'categories Chase business cards are the way to go let me know in the comments '
             "Which business card you prefer and why thank you for watching and I'll see you "
             'next time.',
      'title': 'Capital One Spark Business vs  Chase Business Credit Card | Full Review (2025) '
               '(TECH GIANT)',
      'url': 'https://www.youtube.com/watch?v=m8toWc8c4lM&t=519s',
      'video_id': 'm8toWc8c4lM'},
     {'author': 'Dave Chung',
      'channel': 'Dave Chung',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=HvWd7QRjIEk&t=21s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'At least for us here in Denver, we also have the option to buy two additional '
              'tickets for the first two rounds of the playoffs before the general public had '
              "access. But, I think that's going to be more of a supply and demand thing "
              "that's going to vary a lot by market.",
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'At least for us here in Denver, we also have the option to buy two additional '
             'tickets for the first two rounds of the playoffs before the general public had '
             "access. But, I think that's going to be more of a supply and demand thing that's "
             'going to vary a lot by market.',
      'title': 'How NBA Season Tickets Actually Work (From a 7-Year Holder) (Dave Chung)',
      'url': 'https://www.youtube.com/watch?v=HvWd7QRjIEk&t=21s',
      'video_id': 'HvWd7QRjIEk'}],
 2: [{'author': "Jake's Tech Lab",
      'channel': "Jake's Tech Lab",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=QI-FUFyJsUU&t=33s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Think annual fees, reward structure, welcome bonus, simplicity and redemption, '
              'international use, perks and features, and of course, how flexible they '
              'actually are for your business. All right, first up, annual fee. Honestly, this '
              'is one of its absolute killer perks.',
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': 'Think annual fees, reward structure, welcome bonus, simplicity and redemption, '
             'international use, perks and features, and of course, how flexible they actually '
             'are for your business. All right, first up, annual fee. Honestly, this is one of '
             'its absolute killer perks.',
      'title': 'Ink Business Unlimited vs Capital One Spark Cash Plus | Best Business Credit '
               "Card 2026 (Jake's Tech Lab)",
      'url': 'https://www.youtube.com/watch?v=QI-FUFyJsUU&t=33s',
      'video_id': 'QI-FUFyJsUU'},
     {'author': 'Dutcher Capital',
      'channel': 'Dutcher Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=1e8-M6z0R7c&t=39s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Everyday has no annual fee. Preferred advertises a first year fee waiver, then '
              "$95 a year. We're testing an ongoing year without welcome bonuses and assuming "
              'Alex pays the statement balance in full.',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': 'Everyday has no annual fee. Preferred advertises a first year fee waiver, then '
             "$95 a year. We're testing an ongoing year without welcome bonuses and assuming "
             'Alex pays the statement balance in full.',
      'title': 'Amex Blue Cash: Is 6% Worth the Fee? (Dutcher Capital)',
      'url': 'https://www.youtube.com/watch?v=1e8-M6z0R7c&t=39s',
      'video_id': '1e8-M6z0R7c'},
     {'author': '無國界的Aiden',
      'channel': '無國界的Aiden',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:08](https://www.youtube.com/watch?v=OMnojnDJZ_w&t=428s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '但他忘記了取消系統預設的auto pay 也就是自動扣款 結果就是美國運通的系統照常發起扣款 但他銀行帳戶裡面根本沒有足夠多的錢去付這筆多出來的帳單 '
              '於是就產生了一個最致命的return payment的記錄 這又是美國落後的ACH系統給他帶來的意外的 並且是毫無必要的麻煩 稍後我也會解釋 第二 '
              '就在發生退票的同一天.',
      'timestamp': 428,
      'timestamp_label': '[00:07:08]',
      'timestamp_seconds': 428,
      'tip': '但他忘記了取消系統預設的auto pay 也就是自動扣款 結果就是美國運通的系統照常發起扣款 但他銀行帳戶裡面根本沒有足夠多的錢去付這筆多出來的帳單 '
             '於是就產生了一個最致命的return payment的記錄 這又是美國落後的ACH系統給他帶來的意外的 並且是毫無必要的麻煩 稍後我也會解釋 第二 '
             '就在發生退票的同一天.',
      'title': '刷卡刷到被關戶？Amex Financial Review 真實案例解析：踩雷原因與避免FR方法全解 (無國界的Aiden)',
      'url': 'https://www.youtube.com/watch?v=OMnojnDJZ_w&t=428s',
      'video_id': 'OMnojnDJZ_w'},
     {'author': 'Cash Dissected',
      'channel': 'Cash Dissected',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:33](https://www.youtube.com/watch?v=482heVOfiQg&t=213s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The rest goes back to the venue. The venue isn't on your side in the fight "
              'against fees. The bigger the fee, the bigger its cut. Ticketmaster can even pay '
              'a venue money upfront to win its contract, then earn it back from the fees fans '
              "pay. Here's the second surprise.",
      'timestamp': 213,
      'timestamp_label': '[00:03:33]',
      'timestamp_seconds': 213,
      'tip': "The rest goes back to the venue. The venue isn't on your side in the fight "
             'against fees. The bigger the fee, the bigger its cut. Ticketmaster can even pay '
             'a venue money upfront to win its contract, then earn it back from the fees fans '
             "pay. Here's the second surprise.",
      'title': 'How Ticketmaster Makes Money From Tickets It Already Sold (Taylor Swift Fans '
               'Know) (Cash Dissected)',
      'url': 'https://www.youtube.com/watch?v=482heVOfiQg&t=213s',
      'video_id': '482heVOfiQg'},
     {'author': 'Ticket Flipping',
      'channel': 'Ticket Flipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:00](https://www.youtube.com/watch?v=v5vdJTQKlhU&t=300s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "They get the ticket, you'll get that payment uh in a couple weeks in your bank "
              "account. And how much does Ticket Master charge to sell tickets? 's going to be "
              'around a 15% fee out of your listing price. Pretty straightforwards for selling '
              'tickets on Ticketmaster.',
      'timestamp': 300,
      'timestamp_label': '[00:05:00]',
      'timestamp_seconds': 300,
      'tip': "They get the ticket, you'll get that payment uh in a couple weeks in your bank "
             "account. And how much does Ticket Master charge to sell tickets? 's going to be "
             'around a 15% fee out of your listing price. Pretty straightforwards for selling '
             'tickets on Ticketmaster.',
      'title': 'How To Sell Tickets On Ticketmaster (Beginner Guide) (Ticket Flipping)',
      'url': 'https://www.youtube.com/watch?v=v5vdJTQKlhU&t=300s',
      'video_id': 'v5vdJTQKlhU'},
     {'author': 'Mogulnomics',
      'channel': 'Mogulnomics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=nzZ8nwy2xSY&t=120s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'She loses about 3% on every card payment. No cards, no fees, no tricks. Gary '
              'pays the same $5 as Dave. But Gary gets no points, no cashback, nothing. Gary '
              "is quietly chipping in for Dave's rewards.",
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': 'She loses about 3% on every card payment. No cards, no fees, no tricks. Gary '
             'pays the same $5 as Dave. But Gary gets no points, no cashback, nothing. Gary is '
             "quietly chipping in for Dave's rewards.",
      'title': 'How Credit Card Companies Make Money From You (Even If You Pay in Full) '
               '(Mogulnomics)',
      'url': 'https://www.youtube.com/watch?v=nzZ8nwy2xSY&t=120s',
      'video_id': 'nzZ8nwy2xSY'},
     {'author': 'Stephen Smith',
      'channel': 'Stephen Smith',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:10](https://www.youtube.com/watch?v=zOrHXaEEgxk&t=310s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'To pay that balance off all I have to do is make the minimum payment and I can '
              'carry it over that is amazing because if you think about it realistically you '
              'get.',
      'timestamp': 310,
      'timestamp_label': '[00:05:10]',
      'timestamp_seconds': 310,
      'tip': 'To pay that balance off all I have to do is make the minimum payment and I can '
             'carry it over that is amazing because if you think about it realistically you '
             'get.',
      'title': '$50,000 American Express Plum Card | AMEX Business Card 60 Day 0% APR! (NO '
               'DOCS) (Stephen Smith)',
      'url': 'https://www.youtube.com/watch?v=zOrHXaEEgxk&t=310s',
      'video_id': 'zOrHXaEEgxk'},
     {'author': 'Traveling Teacher Personal Finance',
      'channel': 'Traveling Teacher Personal Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:13](https://www.youtube.com/watch?v=PjJySGf3Swg&t=193s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Um, so that's basically the big deal that you get from this. There is no annual "
              "fee for it, which is kind of good, I guess, because I don't really like paying "
              "annual fees unless it's worth it in the long run. Um, and that's basically a "
              'quick overview of the card itself.',
      'timestamp': 193,
      'timestamp_label': '[00:03:13]',
      'timestamp_seconds': 193,
      'tip': "Um, so that's basically the big deal that you get from this. There is no annual "
             "fee for it, which is kind of good, I guess, because I don't really like paying "
             "annual fees unless it's worth it in the long run. Um, and that's basically a "
             'quick overview of the card itself.',
      'title': 'Can You Buy a Car with Credit Card Points? GM Rewards Card Review and the '
               'Math! (Traveling Teacher Personal Finance)',
      'url': 'https://www.youtube.com/watch?v=PjJySGf3Swg&t=193s',
      'video_id': 'PjJySGf3Swg'},
     {'author': 'Checkout Math',
      'channel': 'Checkout Math',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=T8QUSDg7mnc&t=56s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Some resale sites charged more than 40%. Some websites showed the fees only '
              'after the buyer had typed in payment information. The auditors said their '
              "sample wasn't designed to represent every event, so treat those numbers as a "
              'snapshot.',
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': 'Some resale sites charged more than 40%. Some websites showed the fees only '
             'after the buyer had typed in payment information. The auditors said their sample '
             "wasn't designed to represent every event, so treat those numbers as a snapshot.",
      'title': 'Where Your Ticket Fees Actually Go (Checkout Math)',
      'url': 'https://www.youtube.com/watch?v=T8QUSDg7mnc&t=56s',
      'video_id': 'T8QUSDg7mnc'},
     {'author': 'Elevate Business Consulting, LLC',
      'channel': 'Elevate Business Consulting, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:45](https://www.youtube.com/watch?v=EgyPkxlxqpI&t=225s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Even my mortgage payments are paid with credit cards, right? So make sure that '
              "you're doing organic spending and you're using your credit cards uh to uh buy "
              "things, right? Just set up auto pay for the minimum so you don't miss a "
              'payment.',
      'timestamp': 225,
      'timestamp_label': '[00:03:45]',
      'timestamp_seconds': 225,
      'tip': 'Even my mortgage payments are paid with credit cards, right? So make sure that '
             "you're doing organic spending and you're using your credit cards uh to uh buy "
             "things, right? Just set up auto pay for the minimum so you don't miss a payment.",
      'title': 'The MANUFACTURED SPENDING Strategy That Changed Everything | Elevate Business '
               'Consulting, LLC (Elevate Business Consulting, LLC)',
      'url': 'https://www.youtube.com/watch?v=EgyPkxlxqpI&t=225s',
      'video_id': 'EgyPkxlxqpI'},
     {'author': 'Cal Barton',
      'channel': 'Cal Barton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:15](https://www.youtube.com/watch?v=0pnnp262mLg&t=195s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Years of tax returns and 66% of people were asked to submit either two months '
              "of bank statements or two pay stubs and the third thing that's going to happen.",
      'timestamp': 195,
      'timestamp_label': '[00:03:15]',
      'timestamp_seconds': 195,
      'tip': 'Years of tax returns and 66% of people were asked to submit either two months of '
             "bank statements or two pay stubs and the third thing that's going to happen.",
      'title': 'How To Avoid Amex Financial Review (Cal Barton)',
      'url': 'https://www.youtube.com/watch?v=0pnnp262mLg&t=195s',
      'video_id': '0pnnp262mLg'},
     {'author': 'FULL STRENGTH PODCAST',
      'channel': 'FULL STRENGTH PODCAST',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:30](https://www.youtube.com/watch?v=sfHBAevLV8k&t=270s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Some tickets dropped all the way down to like 200 bucks cuz people were like, '
              '"Yeah, nobody\'s going to pay this." But, you know, people were paying it. I '
              "You guys know I've paid some pretty absurd prices for tickets in the past.",
      'timestamp': 270,
      'timestamp_label': '[00:04:30]',
      'timestamp_seconds': 270,
      'tip': 'Some tickets dropped all the way down to like 200 bucks cuz people were like, '
             '"Yeah, nobody\'s going to pay this." But, you know, people were paying it. I You '
             "guys know I've paid some pretty absurd prices for tickets in the past.",
      'title': 'Episode 15 - NHL Playoff Ticket Prices (FULL STRENGTH PODCAST)',
      'url': 'https://www.youtube.com/watch?v=sfHBAevLV8k&t=270s',
      'video_id': 'sfHBAevLV8k'},
     {'author': 'Three Step Guide',
      'channel': 'Three Step Guide',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=xaHNRvePjBQ&t=110s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'It can also help to have your payment details and account login ready ahead of '
              "time so you can complete the purchase more efficiently. And that's how to use a "
              'presale code on Ticketmaster.',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': 'It can also help to have your payment details and account login ready ahead of '
             "time so you can complete the purchase more efficiently. And that's how to use a "
             'presale code on Ticketmaster.',
      'title': 'How To Use Presale Code On Ticketmaster (2026) (Complete Guide) (Three Step '
               'Guide)',
      'url': 'https://www.youtube.com/watch?v=xaHNRvePjBQ&t=110s',
      'video_id': 'xaHNRvePjBQ'},
     {'author': 'ClarityVenturesVideo',
      'channel': 'ClarityVenturesVideo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:58](https://www.youtube.com/watch?v=lPhNLTTiENE&t=298s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Return or invoice you can reorder any single item or reordering everything with '
              'a single click by clicking reorder all makes it really easy to reorder '
              "especially if you've got a repeat order with a lot of items and quantities.",
      'timestamp': 298,
      'timestamp_label': '[00:04:58]',
      'timestamp_seconds': 298,
      'tip': 'Return or invoice you can reorder any single item or reordering everything with '
             'a single click by clicking reorder all makes it really easy to reorder '
             "especially if you've got a repeat order with a lot of items and quantities.",
      'title': 'Buying Groups Webinar - Increased Sales with Shopping Lists & Easier '
               'Re-ordering (ClarityVenturesVideo)',
      'url': 'https://www.youtube.com/watch?v=lPhNLTTiENE&t=298s',
      'video_id': 'lPhNLTTiENE'},
     {'author': 'Kevin - Financial Tutor 💰',
      'channel': 'Kevin - Financial Tutor 💰',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:16](https://www.youtube.com/watch?v=nQfbn0jqVCk&t=256s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So then I could sell mine after really really struggling and after paying fees '
              'I ended up losing $160 so in total I ended up losing.',
      'timestamp': 256,
      'timestamp_label': '[00:04:16]',
      'timestamp_seconds': 256,
      'tip': 'So then I could sell mine after really really struggling and after paying fees I '
             'ended up losing $160 so in total I ended up losing.',
      'title': 'Flipping Concert Tickets for Profit: Side Hustle Review (Kevin - Financial '
               'Tutor 💰)',
      'url': 'https://www.youtube.com/watch?v=nQfbn0jqVCk&t=256s',
      'video_id': 'nQfbn0jqVCk'}],
 3: [{'author': 'CardsChooser',
      'channel': 'CardsChooser',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=pie5mBLwycU&t=126s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '5% becomes the 5 X transferable points. So now this is something I want to kind '
              "of like share with you. Now the next one that we're going to find here number "
              'two is a US Bank Triple Cash. It got also no annual fee and 750 bonus after '
              '6,180 days.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': '5% becomes the 5 X transferable points. So now this is something I want to kind '
             "of like share with you. Now the next one that we're going to find here number "
             'two is a US Bank Triple Cash. It got also no annual fee and 750 bonus after '
             '6,180 days.',
      'title': 'Best Business Card Bonuses in November 2026  - Ink Cash vs Triple Cash vs Ink '
               'Unlimited (CardsChooser)',
      'url': 'https://www.youtube.com/watch?v=pie5mBLwycU&t=126s',
      'video_id': 'pie5mBLwycU'},
     {'author': 'The Rewards Master',
      'channel': 'The Rewards Master',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:16](https://www.youtube.com/watch?v=qjuRrg-ROGg&t=556s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I don't have the personal Gold Card. This one I use all the time. If you have "
              "an interest in this card, I do have a referral down below. It'll give you the "
              "same opportunity to get the elevated sign-up bonus. It doesn't cost you "
              'anything.',
      'timestamp': 556,
      'timestamp_label': '[00:09:16]',
      'timestamp_seconds': 556,
      'tip': "I don't have the personal Gold Card. This one I use all the time. If you have an "
             "interest in this card, I do have a referral down below. It'll give you the same "
             "opportunity to get the elevated sign-up bonus. It doesn't cost you anything.",
      'title': 'American Express Business Gold Review: 200K Bonus, 4X Rewards... Is It Worth '
               'the $375 Fee? (The Rewards Master)',
      'url': 'https://www.youtube.com/watch?v=qjuRrg-ROGg&t=556s',
      'video_id': 'qjuRrg-ROGg'},
     {'author': 'The Money Advantage',
      'channel': 'The Money Advantage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:25](https://www.youtube.com/watch?v=eckGlyqGUBs&t=325s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Because there is no annual cost to maintain the account, this card becomes a '
              'permanent fixture in your financial portfolio.',
      'timestamp': 325,
      'timestamp_label': '[00:05:25]',
      'timestamp_seconds': 325,
      'tip': 'Because there is no annual cost to maintain the account, this card becomes a '
             'permanent fixture in your financial portfolio.',
      'title': 'Credit Cards For Beginners cash back vs travels. No annual fee (The Money '
               'Advantage)',
      'url': 'https://www.youtube.com/watch?v=eckGlyqGUBs&t=325s',
      'video_id': 'eckGlyqGUBs'},
     {'author': 'Marketing Business Network',
      'channel': 'Marketing Business Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=_lyxCWYwwJA&t=68s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The actual ordering system matters. A supplier may offer a lower unit price, '
              'more useful payment terms or a better delivery arrangement. That is a '
              'possibility, not a guaranteed result. The supplier still has production, '
              'delivery and administrative costs.',
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': 'The actual ordering system matters. A supplier may offer a lower unit price, '
             'more useful payment terms or a better delivery arrangement. That is a '
             'possibility, not a guaranteed result. The supplier still has production, '
             'delivery and administrative costs.',
      'title': 'What is a buying group? (Marketing Business Network)',
      'url': 'https://www.youtube.com/watch?v=_lyxCWYwwJA&t=68s',
      'video_id': '_lyxCWYwwJA'},
     {'author': 'Geobreeze Travel',
      'channel': 'Geobreeze Travel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:04](https://www.youtube.com/watch?v=638DPuaWt9s&t=124s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You've got like for example someone who does all the accounting, cash flow "
              'projections, that sort of thing and the accounts payable. So any outgoing '
              'payments we have to send to our suppliers, the one person handles all that '
              'stuff.',
      'timestamp': 124,
      'timestamp_label': '[00:02:04]',
      'timestamp_seconds': 124,
      'tip': "You've got like for example someone who does all the accounting, cash flow "
             'projections, that sort of thing and the accounts payable. So any outgoing '
             'payments we have to send to our suppliers, the one person handles all that '
             'stuff.',
      'title': 'Earn Credit Card Points by Buying Giftcards (2026) with Taylor from qcgc.io | '
               'Ep 280 (Geobreeze Travel)',
      'url': 'https://www.youtube.com/watch?v=638DPuaWt9s&t=124s',
      'video_id': '638DPuaWt9s'},
     {'author': 'Ben Karabotsis',
      'channel': 'Ben Karabotsis',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:26](https://www.youtube.com/watch?v=jYPli5rcID4&t=1586s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'ve already copped these tickets. If you want a quick sale, you can price them "
              'slightly below the market. And if you want to maximize your profit, you can '
              'price them a bit slightly higher and wait for the demand to increase over time.',
      'timestamp': 1586,
      'timestamp_label': '[00:26:26]',
      'timestamp_seconds': 1586,
      'tip': "'ve already copped these tickets. If you want a quick sale, you can price them "
             'slightly below the market. And if you want to maximize your profit, you can '
             'price them a bit slightly higher and wait for the demand to increase over time.',
      'title': 'Beginners ULTIMATE Guide to Event Ticket Reselling (30 MIN COURSE) (Ben '
               'Karabotsis)',
      'url': 'https://www.youtube.com/watch?v=jYPli5rcID4&t=1586s',
      'video_id': 'jYPli5rcID4'},
     {'author': 'Alex Barajas',
      'channel': 'Alex Barajas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:11](https://www.youtube.com/watch?v=MrvMwsC_ZOg&t=431s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And now, this is one way to have cash liquid in your bank account to do what '
              "you need to do. Now, obviously, this one, the pros is no fees. There's "
              'literally no fees to do this. You just got to have friends that you trust. The '
              'cons is going to be time.',
      'timestamp': 431,
      'timestamp_label': '[00:07:11]',
      'timestamp_seconds': 431,
      'tip': 'And now, this is one way to have cash liquid in your bank account to do what you '
             "need to do. Now, obviously, this one, the pros is no fees. There's literally no "
             'fees to do this. You just got to have friends that you trust. The cons is going '
             'to be time.',
      'title': 'How I Turned Credit Into $100K Cash (0% Interest Hack) (Alex Barajas)',
      'url': 'https://www.youtube.com/watch?v=MrvMwsC_ZOg&t=431s',
      'video_id': 'MrvMwsC_ZOg'},
     {'author': 'UUELTE',
      'channel': 'UUELTE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=1CBYyv8lqgo&t=56s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '433.28 cost we ended up returning 5 thousand five hundred fifty two dollars in '
              'all of the Ticketmaster and otherwise sales that we did that gives us an end of '
              'year end of experiment end of season one total profit.',
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': '433.28 cost we ended up returning 5 thousand five hundred fifty two dollars in '
             'all of the Ticketmaster and otherwise sales that we did that gives us an end of '
             'year end of experiment end of season one total profit.',
      'title': 'I Made $1,000 Flipping NBA Tickets (UUELTE)',
      'url': 'https://www.youtube.com/watch?v=1CBYyv8lqgo&t=56s',
      'video_id': '1CBYyv8lqgo'},
     {'author': 'Ticket Flipping',
      'channel': 'Ticket Flipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:28](https://www.youtube.com/watch?v=ctTMnJPUJk8&t=628s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Some of the recent sales that we've had in this demo account we've had some "
              'sales for Red Hot Chili Peppers here and you can also see a breakdown of the '
              'cost.',
      'timestamp': 628,
      'timestamp_label': '[00:10:28]',
      'timestamp_seconds': 628,
      'tip': "Some of the recent sales that we've had in this demo account we've had some "
             'sales for Red Hot Chili Peppers here and you can also see a breakdown of the '
             'cost.',
      'title': 'The Best Way To Sell Tickets - Lysted Training (Ticket Flipping)',
      'url': 'https://www.youtube.com/watch?v=ctTMnJPUJk8&t=628s',
      'video_id': 'ctTMnJPUJk8'},
     {'author': 'Dave Chung',
      'channel': 'Dave Chung',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:41](https://www.youtube.com/watch?v=CpHB_gOGYSs&t=401s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Tickets below cost for teams that don't have a lot of star power right now so "
              "let's say the Spurs the Raptors those tickets are tougher to sell for sure it.",
      'timestamp': 401,
      'timestamp_label': '[00:06:41]',
      'timestamp_seconds': 401,
      'tip': "Tickets below cost for teams that don't have a lot of star power right now so "
             "let's say the Spurs the Raptors those tickets are tougher to sell for sure it.",
      'title': "What it's REALLY like having NBA season tickets | Should you get season "
               'tickets? (Dave Chung)',
      'url': 'https://www.youtube.com/watch?v=CpHB_gOGYSs&t=401s',
      'video_id': 'CpHB_gOGYSs'},
     {'author': 'NBC4 Washington',
      'channel': 'NBC4 Washington',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=OsZG4eKUfx8&t=36s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Council unanimously voted yes on a bill called the Resale Act. It really is '
              'leveling the playing field for the person who wants to go see a show. The bill '
              'bans bought scalpers, puts a 10% price cap on resale tickets, and forces '
              'resellers to reveal the original price.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': 'Council unanimously voted yes on a bill called the Resale Act. It really is '
             'leveling the playing field for the person who wants to go see a show. The bill '
             'bans bought scalpers, puts a 10% price cap on resale tickets, and forces '
             'resellers to reveal the original price.',
      'title': 'Concert ticket resellers sue over DC law limiting markups | NBC4 Washington '
               '(NBC4 Washington)',
      'url': 'https://www.youtube.com/watch?v=OsZG4eKUfx8&t=36s',
      'video_id': 'OsZG4eKUfx8'},
     {'author': 'ClarityVenturesVideo',
      'channel': 'ClarityVenturesVideo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:32](https://www.youtube.com/watch?v=7kHlVyx4a9E&t=332s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Percent cash back and that calls a loyalty program so that right there is a '
              "very simple tiered pricing there's only one tier member or not and then if you.",
      'timestamp': 332,
      'timestamp_label': '[00:05:32]',
      'timestamp_seconds': 332,
      'tip': 'Percent cash back and that calls a loyalty program so that right there is a very '
             "simple tiered pricing there's only one tier member or not and then if you.",
      'title': 'Buying Groups Webinar - Multi Tiered & Customer-Specific Pricing '
               '(ClarityVenturesVideo)',
      'url': 'https://www.youtube.com/watch?v=7kHlVyx4a9E&t=332s',
      'video_id': '7kHlVyx4a9E'},
     {'author': 'Just Money Ish',
      'channel': 'Just Money Ish',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=u8QBKSzn5K8&t=104s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The reason why a person would even want to do something like this, though, is '
              'because maybe they want to earn cash back, reward points, sign-up bonuses, '
              'airline miles, hotel points, etc.',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': 'The reason why a person would even want to do something like this, though, is '
             'because maybe they want to earn cash back, reward points, sign-up bonuses, '
             'airline miles, hotel points, etc.',
      'title': 'Credit Cycling Explained! (Should You Do it?) (Just Money Ish)',
      'url': 'https://www.youtube.com/watch?v=u8QBKSzn5K8&t=104s',
      'video_id': 'u8QBKSzn5K8'},
     {'author': 'Lysted',
      'channel': 'Lysted',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:41](https://www.youtube.com/watch?v=MJAUFMFXjV8&t=161s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Specific display price on Vivid Seats you can simply continue to adjust your '
              'listing upward or downward once you locate your desired Vivid display price '
              'just press.',
      'timestamp': 161,
      'timestamp_label': '[00:02:41]',
      'timestamp_seconds': 161,
      'tip': 'Specific display price on Vivid Seats you can simply continue to adjust your '
             'listing upward or downward once you locate your desired Vivid display price just '
             'press.',
      'title': 'Inventory Mangement (Lysted)',
      'url': 'https://www.youtube.com/watch?v=MJAUFMFXjV8&t=161s',
      'video_id': 'MJAUFMFXjV8'},
     {'author': "Dani's Tutorials",
      'channel': "Dani's Tutorials",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:26](https://www.youtube.com/watch?v=fCnSbZoDKHU&t=86s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sell tickets on Vivid sits app be sure to use the links down at the description '
              'to get started with vivit sit app if this video was helpful please consider '
              "leaving a like and subscribing to my Channel with that being said I'll see you "
              'in the next video.',
      'timestamp': 86,
      'timestamp_label': '[00:01:26]',
      'timestamp_seconds': 86,
      'tip': 'Sell tickets on Vivid sits app be sure to use the links down at the description '
             'to get started with vivit sit app if this video was helpful please consider '
             "leaving a like and subscribing to my Channel with that being said I'll see you "
             'in the next video.',
      'title': "How To Sell Tickets On Vivid Seats App (2026) (Dani's Tutorials)",
      'url': 'https://www.youtube.com/watch?v=fCnSbZoDKHU&t=86s',
      'video_id': 'fCnSbZoDKHU'}],
 4: [{'author': 'Fundovia',
      'channel': 'Fundovia',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:18](https://www.youtube.com/watch?v=bYLTSIgEHZs&t=198s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'That is why Amex sits in the middle of the stack. Chase history first, then '
              'Amex flexibility. Bank number three, Capital One, and the card is the Spark '
              'Cash Plus. This is also a charge card, also with no preset spending limit. Same '
              'rule as Amex, flexible, never unlimited.',
      'timestamp': 198,
      'timestamp_label': '[00:03:18]',
      'timestamp_seconds': 198,
      'tip': 'That is why Amex sits in the middle of the stack. Chase history first, then Amex '
             'flexibility. Bank number three, Capital One, and the card is the Spark Cash '
             'Plus. This is also a charge card, also with no preset spending limit. Same rule '
             'as Amex, flexible, never unlimited.',
      'title': 'How to Get $150K in Business Credit: Top 3 Banks (Stack Them in This Order) '
               '(Fundovia)',
      'url': 'https://www.youtube.com/watch?v=bYLTSIgEHZs&t=198s',
      'video_id': 'bYLTSIgEHZs'},
     {'author': 'Float - Cash Flow Forecasting',
      'channel': 'Float - Cash Flow Forecasting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=HHf0LK7yPcI&t=70s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'If we put in, say, 3,000, we can see if and when our cash might fall below that '
              'amount in the future. Here, you can see the last sync between Float and your '
              'accounting software, which happens automatically every 24 hours.',
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': 'If we put in, say, 3,000, we can see if and when our cash might fall below that '
             'amount in the future. Here, you can see the last sync between Float and your '
             'accounting software, which happens automatically every 24 hours.',
      'title': 'Bank accounts and Threshold (Float - Cash Flow Forecasting)',
      'url': 'https://www.youtube.com/watch?v=HHf0LK7yPcI&t=70s',
      'video_id': 'HHf0LK7yPcI'},
     {'author': 'Bytes Media',
      'channel': 'Bytes Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=Q12R7gbPW8g&t=55s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The card also includes standard AMX business perks such as purchase protection, '
              'expense management tools, and integration with accounting software. However, '
              'the Plum card is far from perfect.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'The card also includes standard AMX business perks such as purchase protection, '
             'expense management tools, and integration with accounting software. However, the '
             'Plum card is far from perfect.',
      'title': 'American Express Plum Credit Card Review 2026 | Flexible Business Payments, '
               'Benefits & Full Guide (Bytes Media)',
      'url': 'https://www.youtube.com/watch?v=Q12R7gbPW8g&t=55s',
      'video_id': 'Q12R7gbPW8g'},
     {'author': 'Greg Schmidt Official',
      'channel': 'Greg Schmidt Official',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:09](https://www.youtube.com/watch?v=78tbcWA_p0c&t=69s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'With Chase, American Express, Capital One, all the big banks out there. You '
              'find a card, you apply for it, you meet the minimum spending to get the bonus, '
              'and then you determine how long before you want to close that card.',
      'timestamp': 69,
      'timestamp_label': '[00:01:09]',
      'timestamp_seconds': 69,
      'tip': 'With Chase, American Express, Capital One, all the big banks out there. You find '
             'a card, you apply for it, you meet the minimum spending to get the bonus, and '
             'then you determine how long before you want to close that card.',
      'title': "How I Travel for Free: The Beginner's Guide to Credit Card Churning (How I "
               'Earned 3 Million Points) (Greg Schmidt Official)',
      'url': 'https://www.youtube.com/watch?v=78tbcWA_p0c&t=69s',
      'video_id': '78tbcWA_p0c'},
     {'author': 'Just Money Ish',
      'channel': 'Just Money Ish',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:04](https://www.youtube.com/watch?v=Cm-vEtFQnC0&t=244s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And Capital 1 isn't the only financial institution that does this. Most credit "
              'issuers out there have certain algorithms in play that trigger red flags to '
              "your account if they feel that you're being abusive or even fraudulent.",
      'timestamp': 244,
      'timestamp_label': '[00:04:04]',
      'timestamp_seconds': 244,
      'tip': "And Capital 1 isn't the only financial institution that does this. Most credit "
             'issuers out there have certain algorithms in play that trigger red flags to your '
             "account if they feel that you're being abusive or even fraudulent.",
      'title': 'Capital One Will Close Your Credit Card For This One BIG Reason! (CREDIT '
               'CYCLING) (Just Money Ish)',
      'url': 'https://www.youtube.com/watch?v=Cm-vEtFQnC0&t=244s',
      'video_id': 'Cm-vEtFQnC0'},
     {'author': 'Daniel Braun',
      'channel': 'Daniel Braun',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:56](https://www.youtube.com/watch?v=HJuOgHKLiAc&t=236s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Time but then an issuer like Capital One is going to report business credit '
              'card activity at all times on your personal credit so just always do your '
              'research.',
      'timestamp': 236,
      'timestamp_label': '[00:03:56]',
      'timestamp_seconds': 236,
      'tip': 'Time but then an issuer like Capital One is going to report business credit card '
             'activity at all times on your personal credit so just always do your research.',
      'title': 'The EASY Way To Get Business Credit Cards (Full Guide) (Daniel Braun)',
      'url': 'https://www.youtube.com/watch?v=HJuOgHKLiAc&t=236s',
      'video_id': 'HJuOgHKLiAc'},
     {'author': 'MainBotpy',
      'channel': 'MainBotpy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:42](https://www.youtube.com/watch?v=OGtORpGSTL0&t=162s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'My account and I will get back to you okay so I have added uh my account there '
              "and uh let's just run the bottons again event link and uh number of tickets uh "
              'to Max price 0 and auto check.',
      'timestamp': 162,
      'timestamp_label': '[00:02:42]',
      'timestamp_seconds': 162,
      'tip': 'My account and I will get back to you okay so I have added uh my account there '
             "and uh let's just run the bottons again event link and uh number of tickets uh "
             'to Max price 0 and auto check.',
      'title': 'Ticketmaster Bot for Professionals | Presell Tickets | Resell Tickets | Queue '
               'Bypass | Auto Checkout (MainBotpy)',
      'url': 'https://www.youtube.com/watch?v=OGtORpGSTL0&t=162s',
      'video_id': 'OGtORpGSTL0'},
     {'author': 'FlipFlip',
      'channel': 'FlipFlip',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=WvhULoLUeyg&t=35s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ticketmaster and every single ticket that you purchase on your Ticketmaster '
              'account will automatically transfer over to listed by itself so all you need '
              'to.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'Ticketmaster and every single ticket that you purchase on your Ticketmaster '
             'account will automatically transfer over to listed by itself so all you need to.',
      'title': 'How to Use Lysted for Ticket Reselling: Beginner Guide (2023) (FlipFlip)',
      'url': 'https://www.youtube.com/watch?v=WvhULoLUeyg&t=35s',
      'video_id': 'WvhULoLUeyg'},
     {'author': 'thumbsuprun',
      'channel': 'thumbsuprun',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:32](https://www.youtube.com/watch?v=atRV36CcmWc&t=572s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Leave a comment below so I can answer all of them. I will answer every single '
              "one myself, even if there's a million of them. Put a million questions, I will "
              'answer one million times.',
      'timestamp': 572,
      'timestamp_label': '[00:09:32]',
      'timestamp_seconds': 572,
      'tip': 'Leave a comment below so I can answer all of them. I will answer every single '
             "one myself, even if there's a million of them. Put a million questions, I will "
             'answer one million times.',
      'title': 'TICKETMASTER VERIFIED FAN PRESALES | THE FREQUENTLY ASKED QUESTIONS YOU WANTED '
               'ANSWERED (thumbsuprun)',
      'url': 'https://www.youtube.com/watch?v=atRV36CcmWc&t=572s',
      'video_id': 'atRV36CcmWc'},
     {'author': 'Ticket Flipping',
      'channel': 'Ticket Flipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:14](https://www.youtube.com/watch?v=-mFQXqq3hxI&t=254s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'We offer a kind of uh Express sign up for listed and a bunch of other tools '
              "that you might need so if you're interested in flipping tickets online I would "
              "highly recommend you sign up and use the link below if you're interested said.",
      'timestamp': 254,
      'timestamp_label': '[00:04:14]',
      'timestamp_seconds': 254,
      'tip': 'We offer a kind of uh Express sign up for listed and a bunch of other tools that '
             "you might need so if you're interested in flipping tickets online I would highly "
             "recommend you sign up and use the link below if you're interested said.",
      'title': 'How to Sell your Tickets and Get Paid Right Away (Ticket Flipping)',
      'url': 'https://www.youtube.com/watch?v=-mFQXqq3hxI&t=254s',
      'video_id': '-mFQXqq3hxI'},
     {'author': 'Checkmark Tutorial',
      'channel': 'Checkmark Tutorial',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=hglOA-iPzNc&t=80s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So whether you want cash back um travel RSE or no annual phase this is where '
              'you make your decision now once you find the right card now uh submit your.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': 'So whether you want cash back um travel RSE or no annual phase this is where you '
             'make your decision now once you find the right card now uh submit your.',
      'title': 'HOW TO GET APPROVED FOR CAPITAL ONE SPARK BUSINESS CREDIT CARD (Checkmark '
               'Tutorial)',
      'url': 'https://www.youtube.com/watch?v=hglOA-iPzNc&t=80s',
      'video_id': 'hglOA-iPzNc'},
     {'author': 'Just Money Ish',
      'channel': 'Just Money Ish',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:37](https://www.youtube.com/watch?v=Zu5102EGxLc&t=37s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So, that's something you're into, then you're probably going to want to "
              "consider subscribing. But without further ado, let's get to today's video. So, "
              'all of the Capital One Business Spark credit cards are all going to be bogus in '
              'my personal opinion.',
      'timestamp': 37,
      'timestamp_label': '[00:00:37]',
      'timestamp_seconds': 37,
      'tip': "So, that's something you're into, then you're probably going to want to consider "
             "subscribing. But without further ado, let's get to today's video. So, all of the "
             'Capital One Business Spark credit cards are all going to be bogus in my personal '
             'opinion.',
      'title': '5 Reasons Why You Should Stay Away From Capital One Spark Business Credit '
               'Cards (Just Money Ish)',
      'url': 'https://www.youtube.com/watch?v=Zu5102EGxLc&t=37s',
      'video_id': 'Zu5102EGxLc'},
     {'author': 'ProudMoney - Credit Cards & Personal Finance',
      'channel': 'ProudMoney - Credit Cards & Personal Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:42](https://www.youtube.com/watch?v=IrfC1PHQGVQ&t=522s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'As always please go to proud Metacom where we do credit card reviews talk '
              'personal finance we talk deals and all sorts of other fun stuff too thanks for '
              'watching bye.',
      'timestamp': 522,
      'timestamp_label': '[00:08:42]',
      'timestamp_seconds': 522,
      'tip': 'As always please go to proud Metacom where we do credit card reviews talk '
             'personal finance we talk deals and all sorts of other fun stuff too thanks for '
             'watching bye.',
      'title': 'Why Credit Card Limit Increases May Be Bad (And Why Banks Keep Giving Them To '
               'You) (ProudMoney - Credit Cards & Personal Finance)',
      'url': 'https://www.youtube.com/watch?v=IrfC1PHQGVQ&t=522s',
      'video_id': 'IrfC1PHQGVQ'},
     {'author': 'CardRight',
      'channel': 'CardRight',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:18](https://www.youtube.com/watch?v=Nevp4Iee4iw&t=18s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The first and most important thing to know is that when amex hits you with a '
              "financial review they're not looking for you to prove the income that you "
              'wrote.',
      'timestamp': 18,
      'timestamp_label': '[00:00:18]',
      'timestamp_seconds': 18,
      'tip': 'The first and most important thing to know is that when amex hits you with a '
             "financial review they're not looking for you to prove the income that you wrote.",
      'title': 'Hit with a Amex financial review? Here is how to handle it properly '
               '(CardRight)',
      'url': 'https://www.youtube.com/watch?v=Nevp4Iee4iw&t=18s',
      'video_id': 'Nevp4Iee4iw'},
     {'author': 'Ticket Flipping',
      'channel': 'Ticket Flipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:44](https://www.youtube.com/watch?v=uTYlLrxT-xM&t=1484s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Process with some tools so this is a little more advanced you can follow along '
              "or you can kind of skip forward through this well later on I'll cover.",
      'timestamp': 1484,
      'timestamp_label': '[00:24:44]',
      'timestamp_seconds': 1484,
      'tip': 'Process with some tools so this is a little more advanced you can follow along '
             "or you can kind of skip forward through this well later on I'll cover.",
      'title': 'Ticket Broker Introductory Webinar (Ticket Flipping)',
      'url': 'https://www.youtube.com/watch?v=uTYlLrxT-xM&t=1484s',
      'video_id': 'uTYlLrxT-xM'}],
 5: [{'author': 'The Wealth Paradox',
      'channel': 'The Wealth Paradox',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:37](https://www.youtube.com/watch?v=twmhQO3-WGw&t=277s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Here is the mistake to avoid. Do not turn this into an all-or-nothing identity '
              'test. People fail financially when they believe one imperfect month means the '
              'whole plan is broken. A strong money system expects real life.',
      'timestamp': 277,
      'timestamp_label': '[00:04:37]',
      'timestamp_seconds': 277,
      'tip': 'Here is the mistake to avoid. Do not turn this into an all-or-nothing identity '
             'test. People fail financially when they believe one imperfect month means the '
             'whole plan is broken. A strong money system expects real life.',
      'title': "Why Nobody Talks About the Credit Card Float (And How It's Making Some People "
               'Rich) (The Wealth Paradox)',
      'url': 'https://www.youtube.com/watch?v=twmhQO3-WGw&t=277s',
      'video_id': 'twmhQO3-WGw'},
     {'author': 'John Liang',
      'channel': 'John Liang',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=SkbED_I8KzM&t=168s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '100,000 points after you spend $8,000 within the first 4 months. In addition, '
              'both cards offer you 0% APR for the first 12 months. But there is a problem '
              "with both of these signup bonuses, and that's the fact that these are all-time "
              'high bonuses.',
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': '100,000 points after you spend $8,000 within the first 4 months. In addition, '
             'both cards offer you 0% APR for the first 12 months. But there is a problem with '
             "both of these signup bonuses, and that's the fact that these are all-time high "
             'bonuses.',
      'title': 'Chase Ink Unlimited vs Chase Ink Cash - 100,000 Point Bonus! (John Liang)',
      'url': 'https://www.youtube.com/watch?v=SkbED_I8KzM&t=168s',
      'video_id': 'SkbED_I8KzM'},
     {'author': 'HowToCredit',
      'channel': 'HowToCredit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:24](https://www.youtube.com/watch?v=NhkTWTt1RKI&t=144s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And the catch is they all report to your personal credit. Every swipe, every '
              'balance, every single payment, and every single mistake, ladies and gents, all '
              "of these cards report to your personal account. This is why I'm not a fan of "
              "them, okay? Here's what most people miss.",
      'timestamp': 144,
      'timestamp_label': '[00:02:24]',
      'timestamp_seconds': 144,
      'tip': 'And the catch is they all report to your personal credit. Every swipe, every '
             'balance, every single payment, and every single mistake, ladies and gents, all '
             "of these cards report to your personal account. This is why I'm not a fan of "
             "them, okay? Here's what most people miss.",
      'title': 'Capital One Sparks Business Credit Cards Review (2025): Worst Business Credit '
               'Cards Ever (HowToCredit)',
      'url': 'https://www.youtube.com/watch?v=NhkTWTt1RKI&t=144s',
      'video_id': 'NhkTWTt1RKI'},
     {'author': 'Lysted',
      'channel': 'Lysted',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:05](https://www.youtube.com/watch?v=yqoaLjQxJ2w&t=185s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Tickets they're going to charge you 2 000 for that mistake mistakes can be very "
              "expensive very costly so be sure that you're posting accurate information and "
              "that you're staying on top of your fulfillment tab to fulfill all of your sales "
              'in a timely manner.',
      'timestamp': 185,
      'timestamp_label': '[00:03:05]',
      'timestamp_seconds': 185,
      'tip': "Tickets they're going to charge you 2 000 for that mistake mistakes can be very "
             "expensive very costly so be sure that you're posting accurate information and "
             "that you're staying on top of your fulfillment tab to fulfill all of your sales "
             'in a timely manner.',
      'title': 'Order Fulfillment (Lysted)',
      'url': 'https://www.youtube.com/watch?v=yqoaLjQxJ2w&t=185s',
      'video_id': 'yqoaLjQxJ2w'},
     {'author': 'Trip Astute',
      'channel': 'Trip Astute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=hdNIogj_le0&t=120s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'This can also reduce the chance of a fraud alert on your account. Number 4) Be '
              'honest about your income numbers: American Express allows you to request a line '
              'of credit increase by providing your total annual income.',
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': 'This can also reduce the chance of a fraud alert on your account. Number 4) Be '
             'honest about your income numbers: American Express allows you to request a line '
             'of credit increase by providing your total annual income.',
      'title': 'How to Avoid an AMEX Financial Review | Things to Avoid & What To Do If It '
               'Happens to You (Trip Astute)',
      'url': 'https://www.youtube.com/watch?v=hdNIogj_le0&t=120s',
      'video_id': 'hdNIogj_le0'},
     {'author': 'Frequent Miler',
      'channel': 'Frequent Miler',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:11](https://www.youtube.com/watch?v=nMlQUH3s8qY&t=1451s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Next person was able to extend it. No problem at all and went on to tell her '
              "he's going to do her big favor as he can see that she's 18 nights short of "
              'platinum status. My wife only had 32 nights this year. So two actually in a '
              'hotel.',
      'timestamp': 1451,
      'timestamp_label': '[00:24:11]',
      'timestamp_seconds': 1451,
      'tip': 'Next person was able to extend it. No problem at all and went on to tell her '
             "he's going to do her big favor as he can see that she's 18 nights short of "
             'platinum status. My wife only had 32 nights this year. So two actually in a '
             'hotel.',
      'title': 'Buying groups: Big risks / big rewards | Ep223 | 10-7-23 (Frequent Miler)',
      'url': 'https://www.youtube.com/watch?v=nMlQUH3s8qY&t=1451s',
      'video_id': 'nMlQUH3s8qY'},
     {'author': 'Colin Matthew',
      'channel': 'Colin Matthew',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:22](https://www.youtube.com/watch?v=xZwOSYlOyVc&t=142s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And a huge portion of what American Express extends you is unsecured on the '
              "charge card side. There's no preset spending limits at all. That means American "
              "Express is making a live ongoing bet on your ability to pay, so they're taking "
              'more risk.',
      'timestamp': 142,
      'timestamp_label': '[00:02:22]',
      'timestamp_seconds': 142,
      'tip': 'And a huge portion of what American Express extends you is unsecured on the '
             "charge card side. There's no preset spending limits at all. That means American "
             "Express is making a live ongoing bet on your ability to pay, so they're taking "
             'more risk.',
      'title': 'HOW TO AVOID A FINANCIAL REVIEW FROM AMERICAN EXPRESS (2026) (Colin Matthew)',
      'url': 'https://www.youtube.com/watch?v=xZwOSYlOyVc&t=142s',
      'video_id': 'xZwOSYlOyVc'},
     {'author': 'TicketSpice',
      'channel': 'TicketSpice',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:41](https://www.youtube.com/watch?v=xnRbEvUENzI&t=101s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "That is speculative ticketing and it's a huge problem in the event industry, "
              'but not all hope is lost. If you are encountering this or want to help stop and '
              'prevent it, we do have some tricks up our sleeve.',
      'timestamp': 101,
      'timestamp_label': '[00:01:41]',
      'timestamp_seconds': 101,
      'tip': "That is speculative ticketing and it's a huge problem in the event industry, but "
             'not all hope is lost. If you are encountering this or want to help stop and '
             'prevent it, we do have some tricks up our sleeve.',
      'title': 'What Is Speculative Ticketing? Unauthorized Ticket Resale Explained '
               '(TicketSpice)',
      'url': 'https://www.youtube.com/watch?v=xnRbEvUENzI&t=101s',
      'video_id': 'xnRbEvUENzI'},
     {'author': 'Ask Sebby Business',
      'channel': 'Ask Sebby Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:20](https://www.youtube.com/watch?v=x9-GMvg8lPA&t=200s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Of increase that limit to account for that and then the other employees who '
              "maybe don't spend as much you don't really have to have as much at risk on.",
      'timestamp': 200,
      'timestamp_label': '[00:03:20]',
      'timestamp_seconds': 200,
      'tip': 'Of increase that limit to account for that and then the other employees who '
             "maybe don't spend as much you don't really have to have as much at risk on.",
      'title': 'King of Business Cards?! 👑🐐 Capital One Spark Cash Plus (Ask Sebby Business)',
      'url': 'https://www.youtube.com/watch?v=x9-GMvg8lPA&t=200s',
      'video_id': 'x9-GMvg8lPA'},
     {'author': 'Geobreeze Travel',
      'channel': 'Geobreeze Travel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=QTa7eNv00k4&t=15s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Get into that territory and and you're getting closer to being at risk of of "
              'bank shutdowns but I would say in general educate yourself on the.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Get into that territory and and you're getting closer to being at risk of of "
             'bank shutdowns but I would say in general educate yourself on the.',
      'title': 'Rapidly Earning Points Buying and Selling Gift Cards with Taylor from QCGC | '
               'Ep 162 (Geobreeze Travel)',
      'url': 'https://www.youtube.com/watch?v=QTa7eNv00k4&t=15s',
      'video_id': 'QTa7eNv00k4'},
     {'author': 'RJ Financial',
      'channel': 'RJ Financial',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:19](https://www.youtube.com/watch?v=HCkT2XqTvms&t=379s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Thousand dollar credit limit of course they're cycling through it but that's "
              "not really how it works so they'll risk management you know their algorithms.",
      'timestamp': 379,
      'timestamp_label': '[00:06:19]',
      'timestamp_seconds': 379,
      'tip': "Thousand dollar credit limit of course they're cycling through it but that's not "
             "really how it works so they'll risk management you know their algorithms.",
      'title': 'Cycling Credit Card Limits - Spin Class (RJ Financial)',
      'url': 'https://www.youtube.com/watch?v=HCkT2XqTvms&t=379s',
      'video_id': 'HCkT2XqTvms'},
     {'author': 'CardRight',
      'channel': 'CardRight',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=XsemDHBgzWE&t=114s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You haven't already and why don't you leave me a comment let me know how long "
              "you've been with amex and I will see you next time.",
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': "You haven't already and why don't you leave me a comment let me know how long "
             "you've been with amex and I will see you next time.",
      'title': 'Avoid a Amex financial review. 4 things not to do (CardRight)',
      'url': 'https://www.youtube.com/watch?v=XsemDHBgzWE&t=114s',
      'video_id': 'XsemDHBgzWE'},
     {'author': 'u2 credit consulting',
      'channel': 'u2 credit consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:44](https://www.youtube.com/watch?v=UYH3UwJ9oOM&t=344s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Credit card charge card credit card so that's it and just let me know what "
              "videos I want to see tommy if y'all like these videos and uh everything like "
              'that please give me feedback so I see you in the next videos.',
      'timestamp': 344,
      'timestamp_label': '[00:05:44]',
      'timestamp_seconds': 344,
      'tip': "Credit card charge card credit card so that's it and just let me know what "
             "videos I want to see tommy if y'all like these videos and uh everything like "
             'that please give me feedback so I see you in the next videos.',
      'title': 'American Express Plum Business Charge Card (u2 credit consulting)',
      'url': 'https://www.youtube.com/watch?v=UYH3UwJ9oOM&t=344s',
      'video_id': 'UYH3UwJ9oOM'},
     {'author': 'thumbsuprun',
      'channel': 'thumbsuprun',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:36](https://www.youtube.com/watch?v=15eJYcQnVKU&t=1056s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Becoming a problem in terms of whether those events will actually take place '
              "Toronto mle Leafs Ottawa Senators Toronto Raptors they've already.",
      'timestamp': 1056,
      'timestamp_label': '[00:17:36]',
      'timestamp_seconds': 1056,
      'tip': 'Becoming a problem in terms of whether those events will actually take place '
             "Toronto mle Leafs Ottawa Senators Toronto Raptors they've already.",
      'title': 'HOW MUCH I MADE RESELLING $209,953 OF TICKETS IN 2021 | LIFE OF A PART TIME '
               'TICKET BROKER (thumbsuprun)',
      'url': 'https://www.youtube.com/watch?v=15eJYcQnVKU&t=1056s',
      'video_id': '15eJYcQnVKU'},
     {'author': 'Simon Katz - Ideal Media',
      'channel': 'Simon Katz - Ideal Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:32](https://www.youtube.com/watch?v=1AvpfkuaT_Q&t=512s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Recommend people do I do Etc and I'll respond to those comments as well and I'm "
              "sure the audience also appreciates it don't get knocked out like Mike Tyson "
              'hitting you in the face.',
      'timestamp': 512,
      'timestamp_label': '[00:08:32]',
      'timestamp_seconds': 512,
      'tip': "Recommend people do I do Etc and I'll respond to those comments as well and I'm "
             "sure the audience also appreciates it don't get knocked out like Mike Tyson "
             'hitting you in the face.',
      'title': 'How To Avoid A Financial Review From American Express (Simon Katz - Ideal '
               'Media)',
      'url': 'https://www.youtube.com/watch?v=1AvpfkuaT_Q&t=512s',
      'video_id': '1AvpfkuaT_Q'}],
 6: [{'author': 'thumbsuprun',
      'channel': 'thumbsuprun',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:01](https://www.youtube.com/watch?v=hQgsk6D3C_Q&t=61s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "This is the first time they've actually been able to use the BOTS Act. So, "
              "we're going to go into all the details about that case. And lastly, just going "
              "to talk about where we're going to go from here. So, strap in, stay tuned, get "
              'ready.',
      'timestamp': 61,
      'timestamp_label': '[00:01:01]',
      'timestamp_seconds': 61,
      'tip': "This is the first time they've actually been able to use the BOTS Act. So, we're "
             'going to go into all the details about that case. And lastly, just going to talk '
             "about where we're going to go from here. So, strap in, stay tuned, get ready.",
      'title': 'WHAT ARE TICKETING BOTS AND CAN WE FINALLY BEAT THEM?! | THE BOTS ACT 2016 | '
               'BEAT THE BOTS (thumbsuprun)',
      'url': 'https://www.youtube.com/watch?v=hQgsk6D3C_Q&t=61s',
      'video_id': 'hQgsk6D3C_Q'},
     {'author': 'Aleeya34',
      'channel': 'Aleeya34',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=uGTZ3jSLGRg&t=28s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Next, select the event you want. Use the search bar to find the artist, team, '
              'or show, then pick the correct city and date from the results.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': 'Next, select the event you want. Use the search bar to find the artist, team, or '
             'show, then pick the correct city and date from the results.',
      'title': 'How to Use Presale Code on Ticketmaster - Easiest Way (2026 Guide) (Aleeya34)',
      'url': 'https://www.youtube.com/watch?v=uGTZ3jSLGRg&t=28s',
      'video_id': 'uGTZ3jSLGRg'},
     {'author': 'Daniel Shepherd',
      'channel': 'Daniel Shepherd',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=a0APMJagyzA&t=50s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'An annual basis so the amex plum card has no annual fee for the first year but '
              'after this you will be charged 250 each year and one of the best ways to '
              'offset.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': 'An annual basis so the amex plum card has no annual fee for the first year but '
             'after this you will be charged 250 each year and one of the best ways to offset.',
      'title': 'Reviewing The Amex Plum Card - Who Is It For? (Daniel Shepherd)',
      'url': 'https://www.youtube.com/watch?v=a0APMJagyzA&t=50s',
      'video_id': 'a0APMJagyzA'},
     {'author': 'Queue-it',
      'channel': 'Queue-it',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=TG6ufh9T_-8&t=45s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I need to find the event, enter my personal information, enter the payment '
              "details, and then complete the transaction. While, I'm doing all of this. The "
              "bots' checkout looks like this. As you can see, the bot flies through the "
              "checkout while I'm still looking for my wallet.",
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': 'I need to find the event, enter my personal information, enter the payment '
             "details, and then complete the transaction. While, I'm doing all of this. The "
             "bots' checkout looks like this. As you can see, the bot flies through the "
             "checkout while I'm still looking for my wallet.",
      'title': 'What Are Ticket Bots & How Can We Beat Them? | Quick Questions with Queue-it '
               '(Queue-it)',
      'url': 'https://www.youtube.com/watch?v=TG6ufh9T_-8&t=45s',
      'video_id': 'TG6ufh9T_-8'},
     {'author': 'Jack McColl',
      'channel': 'Jack McColl',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=c5MGulNCfZ8&t=110s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And that trust shows up directly on the two new limits you're going to get. For "
              "American Express, AMEX's version is the Blue Business Plus. 0% for 12 months, "
              'no annual fee, and two points per dollar spent on your first $50,000 in annual '
              'spend on the card.',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': "And that trust shows up directly on the two new limits you're going to get. For "
             "American Express, AMEX's version is the Blue Business Plus. 0% for 12 months, no "
             'annual fee, and two points per dollar spent on your first $50,000 in annual '
             'spend on the card.',
      'title': 'The 5 Best Credit Cards Offering 0% Interest (Jack McColl)',
      'url': 'https://www.youtube.com/watch?v=c5MGulNCfZ8&t=110s',
      'video_id': 'c5MGulNCfZ8'},
     {'author': 'John Muscarello',
      'channel': 'John Muscarello',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:36](https://www.youtube.com/watch?v=rpJHRiGfebQ&t=876s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "But, that's what I got for you guys. Getting orders canceled is just part of "
              "the game. But, it's just something you have to deal with. It's just another "
              "obstacle. Again, one of the best ways to overcome this is find sites that don't "
              'care how much you are buying.',
      'timestamp': 876,
      'timestamp_label': '[00:14:36]',
      'timestamp_seconds': 876,
      'tip': "But, that's what I got for you guys. Getting orders canceled is just part of the "
             "game. But, it's just something you have to deal with. It's just another "
             "obstacle. Again, one of the best ways to overcome this is find sites that don't "
             'care how much you are buying.',
      'title': 'How I Avoid Online Arbitrage Order Cancellations for Amazon FBA (John '
               'Muscarello)',
      'url': 'https://www.youtube.com/watch?v=rpJHRiGfebQ&t=876s',
      'video_id': 'rpJHRiGfebQ'},
     {'author': 'Ticket Flipping',
      'channel': 'Ticket Flipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:40](https://www.youtube.com/watch?v=Bs4wpbsiMvY&t=160s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re going to be able to get all the presale passwords. So, right here Justin "
              'Timberlake is going on sale, Madison Square Garden. Get a little bit of more '
              "info like, you know, what's the popularity of this artist, you know, how many "
              'people are listening to him on Spotify.',
      'timestamp': 160,
      'timestamp_label': '[00:02:40]',
      'timestamp_seconds': 160,
      'tip': "'re going to be able to get all the presale passwords. So, right here Justin "
             'Timberlake is going on sale, Madison Square Garden. Get a little bit of more '
             "info like, you know, what's the popularity of this artist, you know, how many "
             'people are listening to him on Spotify.',
      'title': 'Where to find presale passwords and verified fan codes for Ticketmaster '
               '(Ticket Flipping)',
      'url': 'https://www.youtube.com/watch?v=Bs4wpbsiMvY&t=160s',
      'video_id': 'Bs4wpbsiMvY'},
     {'author': 'Lets Get To The Points',
      'channel': 'Lets Get To The Points',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:48:12](https://www.youtube.com/watch?v=mEjNm8zKoQs&t=2892s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "In fact, I think you're getting a lot more with that deal that you propose. So "
              "yeah, I think it's always smart when you can to take advantage of those types "
              'of situations. So before we go, we want to know where can we find you and thank '
              'you for being here today.',
      'timestamp': 2892,
      'timestamp_label': '[00:48:12]',
      'timestamp_seconds': 2892,
      'tip': "In fact, I think you're getting a lot more with that deal that you propose. So "
             "yeah, I think it's always smart when you can to take advantage of those types of "
             'situations. So before we go, we want to know where can we find you and thank you '
             'for being here today.',
      'title': '98. Unlock MASSIVE Rewards with Buying Groups! (Lets Get To The Points)',
      'url': 'https://www.youtube.com/watch?v=mEjNm8zKoQs&t=2892s',
      'video_id': 'mEjNm8zKoQs'},
     {'author': 'Carys Mai',
      'channel': 'Carys Mai',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:28](https://www.youtube.com/watch?v=RRK7zpnM8WQ&t=1468s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'There might also be people you know who like like the artist. Message them '
              'saying, do you have any spare tickets? Because sometimes people like over buy. '
              "They're like, oh I'll just get four and ask four of my friends but they can "
              'only find three friends, you know?',
      'timestamp': 1468,
      'timestamp_label': '[00:24:28]',
      'timestamp_seconds': 1468,
      'tip': 'There might also be people you know who like like the artist. Message them '
             'saying, do you have any spare tickets? Because sometimes people like over buy. '
             "They're like, oh I'll just get four and ask four of my friends but they can only "
             'find three friends, you know?',
      'title': 'the ultimate guide to buying concert tickets | VIP, presale, ticketmaster & '
               'resale (Carys Mai)',
      'url': 'https://www.youtube.com/watch?v=RRK7zpnM8WQ&t=1468s',
      'video_id': 'RRK7zpnM8WQ'},
     {'author': 'Ben Hedges',
      'channel': 'Ben Hedges',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:08](https://www.youtube.com/watch?v=Lbu0I0_jyQA&t=188s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Welcome bonuses you can get a huge amount of points or cash back for opening a '
              "card and we're going to give you a few examples but first if you do run a small "
              "business or if you're a freelance Batman Uber driver.",
      'timestamp': 188,
      'timestamp_label': '[00:03:08]',
      'timestamp_seconds': 188,
      'tip': 'Welcome bonuses you can get a huge amount of points or cash back for opening a '
             "card and we're going to give you a few examples but first if you do run a small "
             "business or if you're a freelance Batman Uber driver.",
      'title': 'Personal Credit Cards VS Business VS Corporate: What’s the Difference? (Ben '
               'Hedges)',
      'url': 'https://www.youtube.com/watch?v=Lbu0I0_jyQA&t=188s',
      'video_id': 'Lbu0I0_jyQA'},
     {'author': 'Chief Tuts',
      'channel': 'Chief Tuts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=42SWCuGJuN4&t=114s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So click on the event and then you'll be directed to details page, click "
              'ticket, download it and then you can now manage or transfer them to someone '
              'else. All right, you can either send the tickets on that person or even list '
              'them for resell.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': "So click on the event and then you'll be directed to details page, click ticket, "
             'download it and then you can now manage or transfer them to someone else. All '
             'right, you can either send the tickets on that person or even list them for '
             'resell.',
      'title': 'How To Transfer SeatGeek Tickets on Vivid Seats (Easiest Way) (Chief Tuts)',
      'url': 'https://www.youtube.com/watch?v=42SWCuGJuN4&t=114s',
      'video_id': '42SWCuGJuN4'},
     {'author': 'Pearly Soul',
      'channel': 'Pearly Soul',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=gCYx-X-zn1I&t=51s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um I actually have two accounts ready here just in case you know something '
              'happens. I have a um at least I have a backup. So the first one is here on my '
              'phone. Um this is my ticket master account. And for the second one, um I have '
              "my niece's like ticket master account.",
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': 'Um I actually have two accounts ready here just in case you know something '
             'happens. I have a um at least I have a backup. So the first one is here on my '
             'phone. Um this is my ticket master account. And for the second one, um I have my '
             "niece's like ticket master account.",
      'title': 'WHAT THE ACTUAL TICKETMASTER QUEUE LOOKS LIKE + PRESALE JOURNEY (BLACKPINK) | '
               'SIMPLY PEARLY (Pearly Soul)',
      'url': 'https://www.youtube.com/watch?v=gCYx-X-zn1I&t=51s',
      'video_id': 'gCYx-X-zn1I'},
     {'author': 'UUELTE',
      'channel': 'UUELTE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=nqLwxP2-Wws&t=22s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Was a great experience here's a quick look at that night our first time sitting "
              "in our season ticket seats it's game time first things first I need a hat you "
              "all know I need a hornet's hat most of them are over here.",
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "Was a great experience here's a quick look at that night our first time sitting "
             "in our season ticket seats it's game time first things first I need a hat you "
             "all know I need a hornet's hat most of them are over here.",
      'title': 'NBA Season Tickets as an Investment? (UUELTE)',
      'url': 'https://www.youtube.com/watch?v=nqLwxP2-Wws&t=22s',
      'video_id': 'nqLwxP2-Wws'},
     {'author': 'Benzaiten Media',
      'channel': 'Benzaiten Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:53](https://www.youtube.com/watch?v=CXnQuOOvcuQ&t=113s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Chat feature for this Sub Hub right for example in the seate you can find it '
              "you can just talk to them uh but in the stop H you doesn't which is a very big "
              'difference I hope you found this video very useful and you reach your '
              'conclusion.',
      'timestamp': 113,
      'timestamp_label': '[00:01:53]',
      'timestamp_seconds': 113,
      'tip': 'Chat feature for this Sub Hub right for example in the seate you can find it you '
             "can just talk to them uh but in the stop H you doesn't which is a very big "
             'difference I hope you found this video very useful and you reach your '
             'conclusion.',
      'title': 'SEATGEEK VS STUBHUB WHICH IS BETTER (2024) FULL GUIDE (Benzaiten Media)',
      'url': 'https://www.youtube.com/watch?v=CXnQuOOvcuQ&t=113s',
      'video_id': 'CXnQuOOvcuQ'},
     {'author': 'Behind The Hum',
      'channel': 'Behind The Hum',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=lw83Hqpb-7Y&t=102s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "When it's your turn, you get a token, a pass that lets you shop without being "
              "stopped again. That's one reason a queue can crawl, then lurch forward. Someone "
              'else has a hand on the tap. Why would anyone build a queue that ignores who '
              'came first?',
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': "When it's your turn, you get a token, a pass that lets you shop without being "
             "stopped again. That's one reason a queue can crawl, then lurch forward. Someone "
             'else has a hand on the tap. Why would anyone build a queue that ignores who came '
             'first?',
      'title': "Why You're Always #84,000 in the Ticket Queue (Behind The Hum)",
      'url': 'https://www.youtube.com/watch?v=lw83Hqpb-7Y&t=102s',
      'video_id': 'lw83Hqpb-7Y'}],
 7: [{'author': 'Veridox',
      'channel': 'Veridox',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:00](https://www.youtube.com/watch?v=pyK2CwcPJx0&t=1560s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '2027, what four concrete steps can you take right now as a concert or sports '
              'fan to avoid feeding the broker and fee machine? Step one, never buy '
              'speculative tickets on secondary resale sites before an official artist presale '
              'or general on sale begins.',
      'timestamp': 1560,
      'timestamp_label': '[00:26:00]',
      'timestamp_seconds': 1560,
      'tip': '2027, what four concrete steps can you take right now as a concert or sports fan '
             'to avoid feeding the broker and fee machine? Step one, never buy speculative '
             'tickets on secondary resale sites before an official artist presale or general '
             'on sale begins.',
      'title': 'The $1.3 Billion Ticket Rig: How Ticketmaster & Scalper Bots Harvest Live '
               'Events (Veridox)',
      'url': 'https://www.youtube.com/watch?v=pyK2CwcPJx0&t=1560s',
      'video_id': 'pyK2CwcPJx0'},
     {'author': 'Sygnify Data',
      'channel': 'Sygnify Data',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:51](https://www.youtube.com/watch?v=m_xKoY7Uj74&t=171s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The law, the Better Online Ticket Sales Act, bans getting around a security '
              'measure, access control system, or other technological control a ticket seller '
              'uses to enforce posted ticket limits. In March 2025, AXS added a check.',
      'timestamp': 171,
      'timestamp_label': '[00:02:51]',
      'timestamp_seconds': 171,
      'tip': 'The law, the Better Online Ticket Sales Act, bans getting around a security '
             'measure, access control system, or other technological control a ticket seller '
             'uses to enforce posted ticket limits. In March 2025, AXS added a check.',
      'title': '7,624 tickets to one concert: the REPS ticket broker file (Sygnify Data)',
      'url': 'https://www.youtube.com/watch?v=m_xKoY7Uj74&t=171s',
      'video_id': 'm_xKoY7Uj74'},
     {'author': 'ZEPHRA',
      'channel': 'ZEPHRA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:01](https://www.youtube.com/watch?v=ejjX4X_T2iA&t=121s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Once the transaction is successful, Ticketmaster will send you a confirmation '
              "email and your tickets will appear in your account based on that event's "
              "delivery schedule. That's all it takes to use a presale code on Ticketmaster.",
      'timestamp': 121,
      'timestamp_label': '[00:02:01]',
      'timestamp_seconds': 121,
      'tip': 'Once the transaction is successful, Ticketmaster will send you a confirmation '
             "email and your tickets will appear in your account based on that event's "
             "delivery schedule. That's all it takes to use a presale code on Ticketmaster.",
      'title': 'How To Use Presale Code On Ticketmaster 2026 Step by Step (ZEPHRA)',
      'url': 'https://www.youtube.com/watch?v=ejjX4X_T2iA&t=121s',
      'video_id': 'ejjX4X_T2iA'},
     {'author': 'AskSebby',
      'channel': 'AskSebby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:13](https://www.youtube.com/watch?v=w8CgH2R003g&t=733s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "They'll send you a specific link to upload all your information if you do not "
              "include a cover sheet then they're not going to be able to process it step.",
      'timestamp': 733,
      'timestamp_label': '[00:12:13]',
      'timestamp_seconds': 733,
      'tip': "They'll send you a specific link to upload all your information if you do not "
             "include a cover sheet then they're not going to be able to process it step.",
      'title': 'I Survived an Amex Financial Review AGAIN: Mistakes to AVOID (AskSebby)',
      'url': 'https://www.youtube.com/watch?v=w8CgH2R003g&t=733s',
      'video_id': 'w8CgH2R003g'},
     {'author': 'Three Step Guide',
      'channel': 'Three Step Guide',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:34](https://www.youtube.com/watch?v=QVwMd8_MPyc&t=94s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'From there, follow the on-screen procedure to complete the process. The system '
              'will guide you through the remaining steps, which may include confirming your '
              'ticket selection, reviewing your order, and proceeding through checkout.',
      'timestamp': 94,
      'timestamp_label': '[00:01:34]',
      'timestamp_seconds': 94,
      'tip': 'From there, follow the on-screen procedure to complete the process. The system '
             'will guide you through the remaining steps, which may include confirming your '
             'ticket selection, reviewing your order, and proceeding through checkout.',
      'title': 'How To Buy Presale Tickets On Ticketmaster (2026) (Complete Guide) (Three Step '
               'Guide)',
      'url': 'https://www.youtube.com/watch?v=QVwMd8_MPyc&t=94s',
      'video_id': 'QVwMd8_MPyc'},
     {'author': 'thumbsuprun',
      'channel': 'thumbsuprun',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:47](https://www.youtube.com/watch?v=L6DxT_aO7To&t=347s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Registration process so step one from here is actually going in and signing in '
              'to your ticketmaster account.',
      'timestamp': 347,
      'timestamp_label': '[00:05:47]',
      'timestamp_seconds': 347,
      'tip': 'Registration process so step one from here is actually going in and signing in '
             'to your ticketmaster account.',
      'title': 'HOW TO SIGN UP FOR TICKETMASTER VERIFIED FAN PRESALE CODES + 3 TIPS TO IMPROVE '
               'YOUR ODDS! (thumbsuprun)',
      'url': 'https://www.youtube.com/watch?v=L6DxT_aO7To&t=347s',
      'video_id': 'L6DxT_aO7To'},
     {'author': 'PurpleCircuit',
      'channel': 'PurpleCircuit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=hx8WaOiS13k&t=102s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You should also review any ticket restrictions such as transfer limitations or '
              'delayed ticket delivery policies. If prompted, enter your pre-sale code exactly '
              'as it was provided. Then proceed to check out and make sure you are signed into '
              'your ticket master account.',
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': 'You should also review any ticket restrictions such as transfer limitations or '
             'delayed ticket delivery policies. If prompted, enter your pre-sale code exactly '
             'as it was provided. Then proceed to check out and make sure you are signed into '
             'your ticket master account.',
      'title': 'How To Get Presale Tickets on Ticketmaster 2026 (Step-by-Step Guide) '
               '(PurpleCircuit)',
      'url': 'https://www.youtube.com/watch?v=hx8WaOiS13k&t=102s',
      'video_id': 'hx8WaOiS13k'},
     {'author': 'TutorialsWithJames',
      'channel': 'TutorialsWithJames',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=lj_eATnFmgE&t=15s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is a very quick and simple thing to do so make sure you watch this video '
              "all the way to the end so you don't miss any important steps now the first "
              'thing you.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'This is a very quick and simple thing to do so make sure you watch this video '
             "all the way to the end so you don't miss any important steps now the first thing "
             'you.',
      'title': 'How To Sell Tickets On Vivid Seats (2025 UPDATE!) (TutorialsWithJames)',
      'url': 'https://www.youtube.com/watch?v=lj_eATnFmgE&t=15s',
      'video_id': 'lj_eATnFmgE'},
     {'author': 'Quick and Easy',
      'channel': 'Quick and Easy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=aFPf82J1I4Y&t=15s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "To follow along I'm going to teach you how to do this process over at the Vivid "
              'Seats website when you arrive at the website sign into your account and once.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "To follow along I'm going to teach you how to do this process over at the Vivid "
             'Seats website when you arrive at the website sign into your account and once.',
      'title': 'How To Sell Tickets on Vivid Seats (Quick and Easy!) (Quick and Easy)',
      'url': 'https://www.youtube.com/watch?v=aFPf82J1I4Y&t=15s',
      'video_id': 'aFPf82J1I4Y'},
     {'author': 'Bianca Kyla',
      'channel': 'Bianca Kyla',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=-VwXw8O92zI&t=20s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "It's for friends and family because I always get tickets. So they told me, "
              '"Let\'s just let Kyla do it and I want you to win. Step one, turn off Wi-Fi on '
              "all of the devices in your house that you're not using.",
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "It's for friends and family because I always get tickets. So they told me, "
             '"Let\'s just let Kyla do it and I want you to win. Step one, turn off Wi-Fi on '
             "all of the devices in your house that you're not using.",
      'title': '8 Step Strategy that ACTUALLY works on Ticketmaster | BTS, BigBang, Bruno Mars '
               'Tickets Secured! (Bianca Kyla)',
      'url': 'https://www.youtube.com/watch?v=-VwXw8O92zI&t=20s',
      'video_id': '-VwXw8O92zI'},
     {'author': 'Vivid Seats',
      'channel': 'Vivid Seats',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:46](https://www.youtube.com/watch?v=BfCMyhnCVQY&t=46s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The Vivid Seats app is here for ordering all your tickets, checking your ticket '
              'status, and seeing your estimated delivery date. Rest assured, with our 100% '
              "Buyer Guarantee and our 100 million tickets sold, we're making sure you get "
              'into your event.',
      'timestamp': 46,
      'timestamp_label': '[00:00:46]',
      'timestamp_seconds': 46,
      'tip': 'The Vivid Seats app is here for ordering all your tickets, checking your ticket '
             'status, and seeing your estimated delivery date. Rest assured, with our 100% '
             "Buyer Guarantee and our 100 million tickets sold, we're making sure you get into "
             'your event.',
      'title': 'Vivid Seats | How to Accept Electronic Ticket Transfer from SeatGeek (Vivid '
               'Seats)',
      'url': 'https://www.youtube.com/watch?v=BfCMyhnCVQY&t=46s',
      'video_id': 'BfCMyhnCVQY'},
     {'author': 'Calby Ng',
      'channel': 'Calby Ng',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=KdXCjTDBTqE&t=102s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'If possible would you like to be connected and also get their direct phone '
              "number yes please we'll first need to verify your Visa signature card.",
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': 'If possible would you like to be connected and also get their direct phone '
             "number yes please we'll first need to verify your Visa signature card.",
      'title': 'We Tried All the Credit Card Concierges Here’s What I Learned (Calby Ng)',
      'url': 'https://www.youtube.com/watch?v=KdXCjTDBTqE&t=102s',
      'video_id': 'KdXCjTDBTqE'},
     {'author': 'Mike Biddle',
      'channel': 'Mike Biddle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=J2ZOHuwCo10&t=68s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "System so there's nothing you can really do about it but just click that join "
              "queue and if you're lucky you'll be 400 um low and it'll take you two three.",
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': "System so there's nothing you can really do about it but just click that join "
             "queue and if you're lucky you'll be 400 um low and it'll take you two three.",
      'title': 'Ticketmaster verified fan presale tips mobile desktop NF Pink Madonna '
               'Springstein Taylor Swift Lizzo (Mike Biddle)',
      'url': 'https://www.youtube.com/watch?v=J2ZOHuwCo10&t=68s',
      'video_id': 'J2ZOHuwCo10'},
     {'author': 'Lysted',
      'channel': 'Lysted',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=Tjcjx18COZU&t=54s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Just very user friendly I originally got into listed thanks to recommendations '
              "from my broker ER Community but I've stayed with them thanks to their ease of.",
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'Just very user friendly I originally got into listed thanks to recommendations '
             "from my broker ER Community but I've stayed with them thanks to their ease of.",
      'title': 'Ticket Selling Side Gig with Lysted (Lysted)',
      'url': 'https://www.youtube.com/watch?v=Tjcjx18COZU&t=54s',
      'video_id': 'Tjcjx18COZU'},
     {'author': 'Pack Your Bag With Points',
      'channel': 'Pack Your Bag With Points',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:50](https://www.youtube.com/watch?v=aJ7DjHaD-XU&t=290s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "It's a great site I love it earn a ton of points this way if you have any "
              'questions or want any follow-up just let me know thanks guys.',
      'timestamp': 290,
      'timestamp_label': '[00:04:50]',
      'timestamp_seconds': 290,
      'tip': "It's a great site I love it earn a ton of points this way if you have any "
             'questions or want any follow-up just let me know thanks guys.',
      'title': 'Buy For Me Retail Tutorial (Pack Your Bag With Points)',
      'url': 'https://www.youtube.com/watch?v=aJ7DjHaD-XU&t=290s',
      'video_id': 'aJ7DjHaD-XU'}],
 8: [{'author': 'Ben Farr',
      'channel': 'Ben Farr',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=I75OnHkQrdc&t=22s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'That nearly half of all concert and event tickets are bought up by scalpers '
              'professional resellers who use tools Bots and software to resell their tickets '
              'for insane.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'That nearly half of all concert and event tickets are bought up by scalpers '
             'professional resellers who use tools Bots and software to resell their tickets '
             'for insane.',
      'title': "I Investigated Ticket Scalping (it's worse than I thought) (Ben Farr)",
      'url': 'https://www.youtube.com/watch?v=I75OnHkQrdc&t=22s',
      'video_id': 'I75OnHkQrdc'},
     {'author': '13 ON YOUR SIDE',
      'channel': '13 ON YOUR SIDE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:32](https://www.youtube.com/watch?v=-t2jgsOhnog&t=212s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Yeah, I think, I think the enforcement side becomes a little bit easier. Uh, '
              "you know, tracking down these bad actors that are doing these bots, it's a "
              'tough job anyhow. But when we do get the information, it allows us to act more '
              'swiftly.',
      'timestamp': 212,
      'timestamp_label': '[00:03:32]',
      'timestamp_seconds': 212,
      'tip': 'Yeah, I think, I think the enforcement side becomes a little bit easier. Uh, you '
             "know, tracking down these bad actors that are doing these bots, it's a tough job "
             'anyhow. But when we do get the information, it allows us to act more swiftly.',
      'title': 'Legislation cracks down on ticket-buying bots (13 ON YOUR SIDE)',
      'url': 'https://www.youtube.com/watch?v=-t2jgsOhnog&t=212s',
      'video_id': '-t2jgsOhnog'},
     {'author': 'Ash Automates',
      'channel': 'Ash Automates',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:50](https://www.youtube.com/watch?v=C3cU-UVpLoU&t=170s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "It's one of the biggest differentiators. Because Connect links to each "
              'marketplace through your own seller account and your own API key, your account '
              'history, your standing, and your relationship with each marketplace all stay in '
              'your name. The marketplace pays you directly.',
      'timestamp': 170,
      'timestamp_label': '[00:02:50]',
      'timestamp_seconds': 170,
      'tip': "It's one of the biggest differentiators. Because Connect links to each "
             'marketplace through your own seller account and your own API key, your account '
             'history, your standing, and your relationship with each marketplace all stay in '
             'your name. The marketplace pays you directly.',
      'title': 'How to Sell Tickets on Multiple Sites Without Overselling (Connect Review) '
               '(Ash Automates)',
      'url': 'https://www.youtube.com/watch?v=C3cU-UVpLoU&t=170s',
      'video_id': 'C3cU-UVpLoU'},
     {'author': 'Naam Wynn',
      'channel': 'Naam Wynn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:10](https://www.youtube.com/watch?v=AsYTdszcmx8&t=250s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The easiest way to do this is with the right online business bank account. That '
              "brings us to today's sponsor, Relay. Relay is a business banking platform built "
              'specifically for small business owners and sole proprietors.',
      'timestamp': 250,
      'timestamp_label': '[00:04:10]',
      'timestamp_seconds': 250,
      'tip': 'The easiest way to do this is with the right online business bank account. That '
             "brings us to today's sponsor, Relay. Relay is a business banking platform built "
             'specifically for small business owners and sole proprietors.',
      'title': 'How to Get Cash from Credit Cards at 0% APR (2026) (Naam Wynn)',
      'url': 'https://www.youtube.com/watch?v=AsYTdszcmx8&t=250s',
      'video_id': 'AsYTdszcmx8'},
     {'author': 'Wholesome Financials',
      'channel': 'Wholesome Financials',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:33](https://www.youtube.com/watch?v=IaYI1caam3s&t=573s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'t mean you shouldn't check out regional banks and what products that they "
              'offer, >> right? And so, what would be a major bank that you recommend? Yeah, a '
              "major bank is u Amex. I always get them confused, but >> what's the other one?",
      'timestamp': 573,
      'timestamp_label': '[00:09:33]',
      'timestamp_seconds': 573,
      'tip': "'t mean you shouldn't check out regional banks and what products that they "
             'offer, >> right? And so, what would be a major bank that you recommend? Yeah, a '
             "major bank is u Amex. I always get them confused, but >> what's the other one?",
      'title': 'The SHOCKING Truth About Capital One Spark Business Credit Card (Wholesome '
               'Financials)',
      'url': 'https://www.youtube.com/watch?v=IaYI1caam3s&t=573s',
      'video_id': 'IaYI1caam3s'},
     {'author': 'Vivid Seats',
      'channel': 'Vivid Seats',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:31](https://www.youtube.com/watch?v=RlHOkpE3Cxg&t=211s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "When all else fails, sometimes it's best to wait an hour, and try again later. "
              'Rest assured, with our 100% Buyer Guarantee and our 100 million tickets sold, '
              "we're making sure you get in to your event. What if you accept your tickets, "
              "but you don't see a barcode or a QR code?",
      'timestamp': 211,
      'timestamp_label': '[00:03:31]',
      'timestamp_seconds': 211,
      'tip': "When all else fails, sometimes it's best to wait an hour, and try again later. "
             'Rest assured, with our 100% Buyer Guarantee and our 100 million tickets sold, '
             "we're making sure you get in to your event. What if you accept your tickets, but "
             "you don't see a barcode or a QR code?",
      'title': 'Vivid Seats | How to Accept Electronic Ticket Transfer from Ticketmaster '
               '(Vivid Seats)',
      'url': 'https://www.youtube.com/watch?v=RlHOkpE3Cxg&t=211s',
      'video_id': 'RlHOkpE3Cxg'},
     {'author': 'James Baker CPA',
      'channel': 'James Baker CPA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=w7-zxRnNOSo&t=68s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "$5,000 you're going to get a 1099 K so when you apply for your stripe account "
              "or any other payment processor you're going to be giving them your information.",
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': "$5,000 you're going to get a 1099 K so when you apply for your stripe account or "
             "any other payment processor you're going to be giving them your information.",
      'title': 'CPA Explains: 1099K (Everything You Need To Know - 2025 Update) (James Baker '
               'CPA)',
      'url': 'https://www.youtube.com/watch?v=w7-zxRnNOSo&t=68s',
      'video_id': 'w7-zxRnNOSo'},
     {'author': 'Bytes Media',
      'channel': 'Bytes Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:09](https://www.youtube.com/watch?v=Z-sM6DX4rEM&t=69s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "2026 appropriate perks for remote and travel-heavy teams. With that said, it's "
              'not perfect. The $395 annual fee will be hard to justify if your business does '
              'not actually use the lounge access, travel portal, or the full $300 annual '
              'credit.',
      'timestamp': 69,
      'timestamp_label': '[00:01:09]',
      'timestamp_seconds': 69,
      'tip': "2026 appropriate perks for remote and travel-heavy teams. With that said, it's "
             'not perfect. The $395 annual fee will be hard to justify if your business does '
             'not actually use the lounge access, travel portal, or the full $300 annual '
             'credit.',
      'title': 'Capital One Venture X Business Credit Card Review 2026 | Business Travel '
               'Rewards, Benefits Guide (Bytes Media)',
      'url': 'https://www.youtube.com/watch?v=Z-sM6DX4rEM&t=69s',
      'video_id': 'Z-sM6DX4rEM'},
     {'author': 'Ticket Flipping',
      'channel': 'Ticket Flipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=Cf05ISv9JrQ&t=15s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Toolbox and why it is the most important tool for any ticket broker a lot of '
              "those training that we have is geared towards newer broker's people who are.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Toolbox and why it is the most important tool for any ticket broker a lot of '
             "those training that we have is geared towards newer broker's people who are.",
      'title': 'How to use the Ticketflipping Toolbox: Features and Benefits (Ticket Flipping)',
      'url': 'https://www.youtube.com/watch?v=Cf05ISv9JrQ&t=15s',
      'video_id': 'Cf05ISv9JrQ'},
     {'author': 'CardRight',
      'channel': 'CardRight',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:23](https://www.youtube.com/watch?v=RqEu9gdaauI&t=23s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Short what is a financial review an AMX financial review is basically when AMX '
              'temporarily suspends your account and request to review your tax return people.',
      'timestamp': 23,
      'timestamp_label': '[00:00:23]',
      'timestamp_seconds': 23,
      'tip': 'Short what is a financial review an AMX financial review is basically when AMX '
             'temporarily suspends your account and request to review your tax return people.',
      'title': 'Avoid a Amex financial review. 4 things not to do [2024] (CardRight)',
      'url': 'https://www.youtube.com/watch?v=RqEu9gdaauI&t=23s',
      'video_id': 'RqEu9gdaauI'},
     {'author': 'AskSebby',
      'channel': 'AskSebby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:06](https://www.youtube.com/watch?v=Er1tcSbzC2w&t=66s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Where they don't trust you at all number two is unsecured which is pretty much "
              'the opposite here are the look at your credit score and you can get pretty.',
      'timestamp': 66,
      'timestamp_label': '[00:01:06]',
      'timestamp_seconds': 66,
      'tip': "Where they don't trust you at all number two is unsecured which is pretty much "
             'the opposite here are the look at your credit score and you can get pretty.',
      'title': 'Yikes! Amex Financial Review: How to Avoid in 2023 (AskSebby)',
      'url': 'https://www.youtube.com/watch?v=Er1tcSbzC2w&t=66s',
      'video_id': 'Er1tcSbzC2w'},
     {'author': 'Ticket Flipping Hub',
      'channel': 'Ticket Flipping Hub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:59](https://www.youtube.com/watch?v=kcVkiYOF11Q&t=179s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Below in the description of this video it will also be the pin comment and you '
              'can take a look at our programs and get some more information about what we do '
              'so thank you so much and looking forward to seeing you in the next video take '
              'care for now.',
      'timestamp': 179,
      'timestamp_label': '[00:02:59]',
      'timestamp_seconds': 179,
      'tip': 'Below in the description of this video it will also be the pin comment and you '
             'can take a look at our programs and get some more information about what we do '
             'so thank you so much and looking forward to seeing you in the next video take '
             'care for now.',
      'title': "UNTAPPED Ticket Flipping Strategy | The Secret Ticket Brokers DON'T Want You "
               'to Know About! (Ticket Flipping Hub)',
      'url': 'https://www.youtube.com/watch?v=kcVkiYOF11Q&t=179s',
      'video_id': 'kcVkiYOF11Q'},
     {'author': 'SplitSeasonTickets',
      'channel': 'SplitSeasonTickets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:23](https://www.youtube.com/watch?v=J8HUmBHqM3c&t=143s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Will just have one ticket location but you can have more than one if that's uh "
              "what your group has so we'll just put a name here and this could just be uh you "
              "know bleachers and we'll put in the season ticket account.",
      'timestamp': 143,
      'timestamp_label': '[00:02:23]',
      'timestamp_seconds': 143,
      'tip': "Will just have one ticket location but you can have more than one if that's uh "
             "what your group has so we'll just put a name here and this could just be uh you "
             "know bleachers and we'll put in the season ticket account.",
      'title': 'Getting Started, Create a Ticket Group (SplitSeasonTickets)',
      'url': 'https://www.youtube.com/watch?v=J8HUmBHqM3c&t=143s',
      'video_id': 'J8HUmBHqM3c'},
     {'author': 'thumbsuprun',
      'channel': 'thumbsuprun',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=mRSt597LFCQ&t=15s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Here on thumbs up where we talk about buying tickets selling tickets and making '
              "sure that you have all the fun with your today we're talking all about.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Here on thumbs up where we talk about buying tickets selling tickets and making '
             "sure that you have all the fun with your today we're talking all about.",
      'title': 'HOW TO SELL AND SHIP HARD STOCK TICKETS | STUBHUB VIVID SEATS SEATGEEK '
               '(thumbsuprun)',
      'url': 'https://www.youtube.com/watch?v=mRSt597LFCQ&t=15s',
      'video_id': 'mRSt597LFCQ'},
     {'author': 'Matthew Perry',
      'channel': 'Matthew Perry',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:27](https://www.youtube.com/watch?v=eEtyddAIvq8&t=267s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Your minimum imbalance so that's definitely a good thing to have an extended "
              'period of time to pay with no interest if you pay your minimum balance so '
              "that's definitely a good thing because it's like having zero APR 4 2015.",
      'timestamp': 267,
      'timestamp_label': '[00:04:27]',
      'timestamp_seconds': 267,
      'tip': "Your minimum imbalance so that's definitely a good thing to have an extended "
             "period of time to pay with no interest if you pay your minimum balance so that's "
             "definitely a good thing because it's like having zero APR 4 2015.",
      'title': 'Credit Card Review: The Plum Card from American Express (Matthew Perry)',
      'url': 'https://www.youtube.com/watch?v=eEtyddAIvq8&t=267s',
      'video_id': 'eEtyddAIvq8'}],
 9: [{'author': 'The Empire Files',
      'channel': 'The Empire Files',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=z5bfNAlrPwg&t=83s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Each account bought a few tickets. Together, they bought millions. The idea is '
              'simple, defeat the controls that enforce the limit. In 2016, Congress passed a '
              'law against it, the BOTS Act. It came after bots swept up tickets for hit '
              'shows, and fans were left with nothing.',
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': 'Each account bought a few tickets. Together, they bought millions. The idea is '
             'simple, defeat the controls that enforce the limit. In 2016, Congress passed a '
             'law against it, the BOTS Act. It came after bots swept up tickets for hit shows, '
             'and fans were left with nothing.',
      'title': 'How One Company Bought 18.5 Million Tickets Before You Could (The Empire '
               'Files)',
      'url': 'https://www.youtube.com/watch?v=z5bfNAlrPwg&t=83s',
      'video_id': 'z5bfNAlrPwg'},
     {'author': 'Cameron Gayed',
      'channel': 'Cameron Gayed',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:19](https://www.youtube.com/watch?v=H2F6UOr65H4&t=259s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'But if you can get it, they have great travel and great business benefits. '
              "Truist Bank I give a B tier. Simply because they're not in every state, so it's "
              "not accessible for everybody. You don't need to already have a checking account "
              'with Truist.',
      'timestamp': 259,
      'timestamp_label': '[00:04:19]',
      'timestamp_seconds': 259,
      'tip': 'But if you can get it, they have great travel and great business benefits. '
             "Truist Bank I give a B tier. Simply because they're not in every state, so it's "
             "not accessible for everybody. You don't need to already have a checking account "
             'with Truist.',
      'title': 'I Ranked Every Business Credit Card (2026 Tier List) (Cameron Gayed)',
      'url': 'https://www.youtube.com/watch?v=H2F6UOr65H4&t=259s',
      'video_id': 'H2F6UOr65H4'},
     {'author': 'FOX 5 Washington DC',
      'channel': 'FOX 5 Washington DC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=Fw6FD7wtec0&t=31s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'SUING THE SEATGEEK, VIVIDSEATS, GAME TIME AND TICKPICK ARE ALL SUING THE '
              'DISTRICT TO STOP IT FROM GOING INTO EFFECT. BRIAN BARRY WITH DISTRICT TO STOP '
              'IT FROM GOING INTO EFFECT. BRIAN BARRY WITH THE TICKET POLICY FORUM, SAYS THE '
              'RESALE ACT VIOLATES THE LAW.',
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': 'SUING THE SEATGEEK, VIVIDSEATS, GAME TIME AND TICKPICK ARE ALL SUING THE '
             'DISTRICT TO STOP IT FROM GOING INTO EFFECT. BRIAN BARRY WITH DISTRICT TO STOP IT '
             'FROM GOING INTO EFFECT. BRIAN BARRY WITH THE TICKET POLICY FORUM, SAYS THE '
             'RESALE ACT VIOLATES THE LAW.',
      'title': 'Ticket resale companies sue DC over proposed law (FOX 5 Washington DC)',
      'url': 'https://www.youtube.com/watch?v=Fw6FD7wtec0&t=31s',
      'video_id': 'Fw6FD7wtec0'},
     {'author': 'Phillip Pak',
      'channel': 'Phillip Pak',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:34](https://www.youtube.com/watch?v=uXsekqVFn10&t=154s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "A lot of the times, you're not just limited to one single sign-up bonus in one "
              'lifetime. You can get two, three, or even four of these sign-up bonuses. This '
              'is because when they send you email offers or literally mail-in offers.',
      'timestamp': 154,
      'timestamp_label': '[00:02:34]',
      'timestamp_seconds': 154,
      'tip': "A lot of the times, you're not just limited to one single sign-up bonus in one "
             'lifetime. You can get two, three, or even four of these sign-up bonuses. This is '
             'because when they send you email offers or literally mail-in offers.',
      'title': '5 Reasons Why The AMEX Business Gold Card Is Better Than You Think In 2026 '
               '(Phillip Pak)',
      'url': 'https://www.youtube.com/watch?v=uXsekqVFn10&t=154s',
      'video_id': 'uXsekqVFn10'},
     {'author': 'Eli Facenda',
      'channel': 'Eli Facenda',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=fEjp_gJN8OQ&t=51s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Going to do for your business in terms of end-of-year annual return and compare '
              'that to option b what the benefit would be of earning points and using those '
              'at.',
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': 'Going to do for your business in terms of end-of-year annual return and compare '
             'that to option b what the benefit would be of earning points and using those at.',
      'title': 'Should You Get the AMEX Plum for your Business? (Eli Facenda)',
      'url': 'https://www.youtube.com/watch?v=fEjp_gJN8OQ&t=51s',
      'video_id': 'fEjp_gJN8OQ'},
     {'author': 'WWLP-22News',
      'channel': 'WWLP-22News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=fAVGs0g8--w&t=87s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Consumers League argues this just leads to jacked up prices for out of-state '
              "customers no one at the hearing hosted by the state legislator's consumer "
              'protection committee testified in favor of letting the law stand as is live at '
              'the State House Christine Lee 22 News.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': 'Consumers League argues this just leads to jacked up prices for out of-state '
             "customers no one at the hearing hosted by the state legislator's consumer "
             'protection committee testified in favor of letting the law stand as is live at '
             'the State House Christine Lee 22 News.',
      'title': 'Ticket brokers seek changes to resale law (WWLP-22News)',
      'url': 'https://www.youtube.com/watch?v=fAVGs0g8--w&t=87s',
      'video_id': 'fAVGs0g8--w'},
     {'author': 'CBC News',
      'channel': 'CBC News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=cY2OK7IEAso&t=68s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '" They go on to say, "We remain committed to creating a fair and secure ticket '
              'marketplace for everyone in compliance with all applicable laws and '
              'regulations.".',
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': '" They go on to say, "We remain committed to creating a fair and secure ticket '
             'marketplace for everyone in compliance with all applicable laws and '
             'regulations.".',
      'title': 'Ticketmaster delists resale tickets in Ontario after bill passed (CBC News)',
      'url': 'https://www.youtube.com/watch?v=cY2OK7IEAso&t=68s',
      'video_id': 'cY2OK7IEAso'},
     {'author': 'Hands Off Sales Tax (HOST)',
      'channel': 'Hands Off Sales Tax (HOST)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:08](https://www.youtube.com/watch?v=w-siA5UEWLY&t=128s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And that's how many sellers avoid over-registering while still preventing "
              'unnecessary tax from being charged on their supplier orders. That said, '
              'acceptance rules vary by state and by platform, so this is an area where '
              'details matter.',
      'timestamp': 128,
      'timestamp_label': '[00:02:08]',
      'timestamp_seconds': 128,
      'tip': "And that's how many sellers avoid over-registering while still preventing "
             'unnecessary tax from being charged on their supplier orders. That said, '
             'acceptance rules vary by state and by platform, so this is an area where details '
             'matter.',
      'title': 'The Huge Printful Resale Certificate Mistake (Hands Off Sales Tax (HOST))',
      'url': 'https://www.youtube.com/watch?v=w-siA5UEWLY&t=128s',
      'video_id': 'w-siA5UEWLY'},
     {'author': 'Aleeya34',
      'channel': 'Aleeya34',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:46](https://www.youtube.com/watch?v=XoGnWfnhHao&t=106s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ensure the name matches your payment method to prevent delays. Before you can '
              'finish, click the checkbox to agree to the terms and event policies. This '
              'confirms you understand the rules and prevents order issues. Finally, click '
              'place order.',
      'timestamp': 106,
      'timestamp_label': '[00:01:46]',
      'timestamp_seconds': 106,
      'tip': 'Ensure the name matches your payment method to prevent delays. Before you can '
             'finish, click the checkbox to agree to the terms and event policies. This '
             'confirms you understand the rules and prevents order issues. Finally, click '
             'place order.',
      'title': 'How to Buy Presale Tickets on Ticketmaster (2026 Guide) (Aleeya34)',
      'url': 'https://www.youtube.com/watch?v=XoGnWfnhHao&t=106s',
      'video_id': 'XoGnWfnhHao'},
     {'author': 'thumbsuprun',
      'channel': 'thumbsuprun',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:00](https://www.youtube.com/watch?v=Lv8TASDf0Q4&t=180s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Explicitly state this but what it means is that if you have been flagged your '
              'account will never be able to successfully get a code ever again.',
      'timestamp': 180,
      'timestamp_label': '[00:03:00]',
      'timestamp_seconds': 180,
      'tip': 'Explicitly state this but what it means is that if you have been flagged your '
             'account will never be able to successfully get a code ever again.',
      'title': 'HOW TO SUCCEED AT TICKETMASTER VERIFIED FAN PRESALES (thumbsuprun)',
      'url': 'https://www.youtube.com/watch?v=Lv8TASDf0Q4&t=180s',
      'video_id': 'Lv8TASDf0Q4'},
     {'author': 'Ticket Flipping',
      'channel': 'Ticket Flipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:05](https://www.youtube.com/watch?v=ohPaFrchlzE&t=305s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Really, really, really familiarize yourself with the entire venue. Get familiar '
              'where all the seats are in the arena. Familiarize yourself with the terms. Next '
              'study the primary market.',
      'timestamp': 305,
      'timestamp_label': '[00:05:05]',
      'timestamp_seconds': 305,
      'tip': 'Really, really, really familiarize yourself with the entire venue. Get familiar '
             'where all the seats are in the arena. Familiarize yourself with the terms. Next '
             'study the primary market.',
      'title': 'How To Make Money Reselling Tickets - Flipping Playoff Tickets (Ticket '
               'Flipping)',
      'url': 'https://www.youtube.com/watch?v=ohPaFrchlzE&t=305s',
      'video_id': 'ohPaFrchlzE'},
     {'author': 'Smart Capital',
      'channel': 'Smart Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:03](https://www.youtube.com/watch?v=aE4ci0-ah-k&t=483s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The second is application rules. Some issuers limit how many new cards you can '
              "open, and the best known example is Chase's reported five and 24 rule, under "
              'which many applicants with five or more new cards in the past two years are not '
              'approved.',
      'timestamp': 483,
      'timestamp_label': '[00:08:03]',
      'timestamp_seconds': 483,
      'tip': 'The second is application rules. Some issuers limit how many new cards you can '
             "open, and the best known example is Chase's reported five and 24 rule, under "
             'which many applicants with five or more new cards in the past two years are not '
             'approved.',
      'title': 'Business Credit Card Rewards: How to Travel for Free With Points 2026 (Smart '
               'Capital)',
      'url': 'https://www.youtube.com/watch?v=aE4ci0-ah-k&t=483s',
      'video_id': 'aE4ci0-ah-k'},
     {'author': 'Lysted',
      'channel': 'Lysted',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=Zv0-nTTakh4&t=52s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'At a time if you do so each ticket posted will be added to all the selected '
              'events only use this feature if you have the same ticket location for mult '
              'multiple.',
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': 'At a time if you do so each ticket posted will be added to all the selected '
             'events only use this feature if you have the same ticket location for mult '
             'multiple.',
      'title': 'Listing Tickets (Lysted)',
      'url': 'https://www.youtube.com/watch?v=Zv0-nTTakh4&t=52s',
      'video_id': 'Zv0-nTTakh4'},
     {'author': 'Ahmed’s Voice',
      'channel': 'Ahmed’s Voice',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:23](https://www.youtube.com/watch?v=6H1RUQH71uc&t=23s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, if you're using resale sites such as StubHub, SeatGeek, Vivid Seats, or "
              'any of these other resale thirdparty uh vendors, please be careful. I have tips '
              "at my Substack, I'm edvoice.",
      'timestamp': 23,
      'timestamp_label': '[00:00:23]',
      'timestamp_seconds': 23,
      'tip': "Now, if you're using resale sites such as StubHub, SeatGeek, Vivid Seats, or any "
             'of these other resale thirdparty uh vendors, please be careful. I have tips at '
             "my Substack, I'm edvoice.",
      'title': 'Be careful booking concert #tickets .  #substack #stubhub #seatgeek '
               '#vividseats #concerttickets (Ahmed’s Voice)',
      'url': 'https://www.youtube.com/watch?v=6H1RUQH71uc&t=23s',
      'video_id': '6H1RUQH71uc'},
     {'author': 'CardRight',
      'channel': 'CardRight',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=A8jkRXH6hXc&t=15s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BG`) purchase-order fulfillment stacked with uncapped `2%–4%` commercial '
                   'card float/rebates, and `BOTS Act`-compliant secondary live-event ticket, '
                   '`SSL`, and corporate-suite allocation brokerage (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Want to discuss with you how to handle a financial review if you are already.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Want to discuss with you how to handle a financial review if you are already.',
      'title': 'Hit with a Amex financial review? Here is how to handle it properly [2024] '
               '(CardRight)',
      'url': 'https://www.youtube.com/watch?v=A8jkRXH6hXc&t=15s',
      'video_id': 'A8jkRXH6hXc'}],
 10: [{'author': "Jake's Tech Lab",
       'channel': "Jake's Tech Lab",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:34](https://www.youtube.com/watch?v=NjlljrQidKg&t=34s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s what we all care about, travel perks, how well they scale for large "
               'business spend, and finally, all those nice to have protections and extra '
               "features. Let's roll out the mind map. Let's kick off with annual fees because "
               'honestly, no one likes sticker shock.',
       'timestamp': 34,
       'timestamp_label': '[00:00:34]',
       'timestamp_seconds': 34,
       'tip': "'s what we all care about, travel perks, how well they scale for large business "
              'spend, and finally, all those nice to have protections and extra features. '
              "Let's roll out the mind map. Let's kick off with annual fees because honestly, "
              'no one likes sticker shock.',
       'title': 'Capital One Spark Cash Plus vs Amex Business Gold | Best Business Credit Card '
                "2026 (Jake's Tech Lab)",
       'url': 'https://www.youtube.com/watch?v=NjlljrQidKg&t=34s',
       'video_id': 'NjlljrQidKg'},
      {'author': 'Chris Hutchins',
       'channel': 'Chris Hutchins',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:54:27](https://www.youtube.com/watch?v=Dbhznmaq0Bg&t=3267s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Reserve, it's Amex Platinum, real cards with high annual fees. Um, I know "
               "you've done an episode on a lot of these things. I wanted to, you know, hear "
               'your take on this and and other perks that might apply to people in that '
               "situation. They'll waive it on all personal cards.",
       'timestamp': 3267,
       'timestamp_label': '[00:54:27]',
       'timestamp_seconds': 3267,
       'tip': "Reserve, it's Amex Platinum, real cards with high annual fees. Um, I know "
              "you've done an episode on a lot of these things. I wanted to, you know, hear "
              'your take on this and and other perks that might apply to people in that '
              "situation. They'll waive it on all personal cards.",
       'title': 'Maximize Your Points: Stacking, Buyers Clubs, Redemption Hacks, and More '
                '(Chris Hutchins)',
       'url': 'https://www.youtube.com/watch?v=Dbhznmaq0Bg&t=3267s',
       'video_id': 'Dbhznmaq0Bg'},
      {'author': 'HowToCredit',
       'channel': 'HowToCredit',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:26](https://www.youtube.com/watch?v=1F0G53GBilU&t=746s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Now, for all my people with a 700 credit score or better, and you're looking "
               'to get 50 to $300,000 in business capital to start or scale your business, '
               'then what I want you to do is click that link below to sign up for a capital '
               'consultation.',
       'timestamp': 746,
       'timestamp_label': '[00:12:26]',
       'timestamp_seconds': 746,
       'tip': "Now, for all my people with a 700 credit score or better, and you're looking to "
              'get 50 to $300,000 in business capital to start or scale your business, then '
              'what I want you to do is click that link below to sign up for a capital '
              'consultation.',
       'title': 'How To Get A $10k CREDIT CARD Limit FAST!! | PERSONAL & BUSINESS METHOD 2026 '
                '(HowToCredit)',
       'url': 'https://www.youtube.com/watch?v=1F0G53GBilU&t=746s',
       'video_id': '1F0G53GBilU'},
      {'author': 'Loral Langemeier',
       'channel': 'Loral Langemeier',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:19](https://www.youtube.com/watch?v=OVRY6T42zPA&t=79s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s just about cards, a debit card is linked to your bank. It's money that's "
               'coming out of your bank account right away. So, immediate purchases media '
               "taken out of your bank. Credit cards are different, it's building your credit "
               "it's associated to your credit spending.",
       'timestamp': 79,
       'timestamp_label': '[00:01:19]',
       'timestamp_seconds': 79,
       'tip': "'s just about cards, a debit card is linked to your bank. It's money that's "
              'coming out of your bank account right away. So, immediate purchases media taken '
              "out of your bank. Credit cards are different, it's building your credit it's "
              'associated to your credit spending.',
       'title': 'How To Leverage Credit Cards To Build Wealth (Loral Langemeier)',
       'url': 'https://www.youtube.com/watch?v=OVRY6T42zPA&t=79s',
       'video_id': 'OVRY6T42zPA'},
      {'author': 'Tutorials By David',
       'channel': 'Tutorials By David',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:38](https://www.youtube.com/watch?v=1uLGFbtlWBQ&t=38s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Next is set up your email forwarding. So email forwarding is crucial because '
               'listed automation relies on purchase confirmation emails from ticket master. '
               'So after that is automated account sweep. So with email forwarding in place '
               'and your login added.',
       'timestamp': 38,
       'timestamp_label': '[00:00:38]',
       'timestamp_seconds': 38,
       'tip': 'Next is set up your email forwarding. So email forwarding is crucial because '
              'listed automation relies on purchase confirmation emails from ticket master. So '
              'after that is automated account sweep. So with email forwarding in place and '
              'your login added.',
       'title': 'How to Link Ticketmaster to Lysted (2026 GUIDE) (Tutorials By David)',
       'url': 'https://www.youtube.com/watch?v=1uLGFbtlWBQ&t=38s',
       'video_id': '1uLGFbtlWBQ'},
      {'author': 'VANNtastic!',
       'channel': 'VANNtastic!',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:55](https://www.youtube.com/watch?v=CO5ahnL4ijI&t=55s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'ll be talking about what this looks like using the credit cards instead of "
               'the line of credit. Now, remember, credit cards, unless you are with a credit '
               'union, a bank that will allow you to transfer funds from your checking account '
               'into your credit card, okay?',
       'timestamp': 55,
       'timestamp_label': '[00:00:55]',
       'timestamp_seconds': 55,
       'tip': "'ll be talking about what this looks like using the credit cards instead of the "
              'line of credit. Now, remember, credit cards, unless you are with a credit '
              'union, a bank that will allow you to transfer funds from your checking account '
              'into your credit card, okay?',
       'title': 'How to Create More Cash Flow Using Credit Cards (VANNtastic!)',
       'url': 'https://www.youtube.com/watch?v=CO5ahnL4ijI&t=55s',
       'video_id': 'CO5ahnL4ijI'},
      {'author': 'Fine Print',
       'channel': 'Fine Print',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:18](https://www.youtube.com/watch?v=Pv_ogmKsubk&t=798s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, they chose not to enforce. The FTC lawsuit filed in September 2025 alleges '
               'that ticket masters employees turn a blind eye as a matter of policy to ticket '
               'broker misbehavior. One broker flagged for large-scale violations was '
               'described internally as not slowing down.',
       'timestamp': 798,
       'timestamp_label': '[00:13:18]',
       'timestamp_seconds': 798,
       'tip': 'So, they chose not to enforce. The FTC lawsuit filed in September 2025 alleges '
              'that ticket masters employees turn a blind eye as a matter of policy to ticket '
              'broker misbehavior. One broker flagged for large-scale violations was described '
              'internally as not slowing down.',
       'title': 'Ticketmaster Just Got Caught Scalping Their Own Tickets (Fine Print)',
       'url': 'https://www.youtube.com/watch?v=Pv_ogmKsubk&t=798s',
       'video_id': 'Pv_ogmKsubk'},
      {'author': 'Trip Astute',
       'channel': 'Trip Astute',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:16](https://www.youtube.com/watch?v=ThfeGmFtkZk&t=496s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Have you tried using your credit card’s concierge? If so, what has been your '
               'experience? Let me know in the comment section below. I’m curious to hear '
               'whether you all are using this benefit.',
       'timestamp': 496,
       'timestamp_label': '[00:08:16]',
       'timestamp_seconds': 496,
       'tip': 'Have you tried using your credit card’s concierge? If so, what has been your '
              'experience? Let me know in the comment section below. I’m curious to hear '
              'whether you all are using this benefit.',
       'title': "Credit Card Concierge Service | Underrated Benefit That's Useful for Both "
                'Travel & Daily Life (Trip Astute)',
       'url': 'https://www.youtube.com/watch?v=ThfeGmFtkZk&t=496s',
       'video_id': 'ThfeGmFtkZk'},
      {'author': 'Colin Matthew',
       'channel': 'Colin Matthew',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:11](https://www.youtube.com/watch?v=QVqw68pTohQ&t=191s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And you'll end up paying over 13K in interest. You end up paying the bank more "
               'than your original debt without reducing principal significantly when you make '
               'minimum payments. You could play their game and stay broke, or you can use a '
               'simple strategy to flip the script.',
       'timestamp': 191,
       'timestamp_label': '[00:03:11]',
       'timestamp_seconds': 191,
       'tip': "And you'll end up paying over 13K in interest. You end up paying the bank more "
              'than your original debt without reducing principal significantly when you make '
              'minimum payments. You could play their game and stay broke, or you can use a '
              'simple strategy to flip the script.',
       'title': 'How to Pay Off Your Maxed Out Credit Cards with ZERO Cashflow! (Colin '
                'Matthew)',
       'url': 'https://www.youtube.com/watch?v=QVqw68pTohQ&t=191s',
       'video_id': 'QVqw68pTohQ'},
      {'author': 'Jack McColl',
       'channel': 'Jack McColl',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:45](https://www.youtube.com/watch?v=SNCeMDvlJsQ&t=585s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "150,000 of personal annual income, those people I've seen to maximize the "
               'limits on the cards. And the same principle as always, the income should be as '
               "high enough to justify a real limit so you don't trigger the documentation "
               'request of proof of income.',
       'timestamp': 585,
       'timestamp_label': '[00:09:45]',
       'timestamp_seconds': 585,
       'tip': "150,000 of personal annual income, those people I've seen to maximize the "
              'limits on the cards. And the same principle as always, the income should be as '
              "high enough to justify a real limit so you don't trigger the documentation "
              'request of proof of income.',
       'title': 'Do THIS Before Applying for an Amex Business Credit Card (Jack McColl)',
       'url': 'https://www.youtube.com/watch?v=SNCeMDvlJsQ&t=585s',
       'video_id': 'SNCeMDvlJsQ'},
      {'author': 'The Hockey Guy',
       'channel': 'The Hockey Guy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:30](https://www.youtube.com/watch?v=nWMK3vxC4WE&t=570s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Generate more income so we will see how this all turns out uh but again you '
               'know just just personally i totally understand why people would.',
       'timestamp': 570,
       'timestamp_label': '[00:09:30]',
       'timestamp_seconds': 570,
       'tip': 'Generate more income so we will see how this all turns out uh but again you '
              'know just just personally i totally understand why people would.',
       'title': 'NHL Execs Concerned with Season Ticket Sales and the Effect on the Cap (The '
                'Hockey Guy)',
       'url': 'https://www.youtube.com/watch?v=nWMK3vxC4WE&t=570s',
       'video_id': 'nWMK3vxC4WE'},
      {'author': 'Fairlyne',
       'channel': 'Fairlyne',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=rzhKnvAoXZo&t=21s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "France et j'ai même envie de dire en Europe puisque le modèle WIGO est en "
               "train de s'exporter notamment en Espagne et puis aussi sur Paris-Bruxelles.",
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': "France et j'ai même envie de dire en Europe puisque le modèle WIGO est en train "
              "de s'exporter notamment en Espagne et puis aussi sur Paris-Bruxelles.",
       'title': 'Fairlyne Case Study: OUIGOSWAP, on 3 years of ticket resale from SeatResale '
                'to full marketplace (Fairlyne)',
       'url': 'https://www.youtube.com/watch?v=rzhKnvAoXZo&t=21s',
       'video_id': 'rzhKnvAoXZo'},
      {'author': 'Calby Ng',
       'channel': 'Calby Ng',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:45](https://www.youtube.com/watch?v=pgK3SEONYmE&t=885s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Frog definitely make sure you go and do that and I guess we'll see you later "
               "take care everybody I me you can distinguish it by the annual fe uh that's "
               "true mastercard's free man free baby true true free.",
       'timestamp': 885,
       'timestamp_label': '[00:14:45]',
       'timestamp_seconds': 885,
       'tip': "Frog definitely make sure you go and do that and I guess we'll see you later "
              "take care everybody I me you can distinguish it by the annual fe uh that's true "
              "mastercard's free man free baby true true free.",
       'title': 'Luxury Credit Card Concierges Are They Worth Your Time (Here’s What’s Best) '
                '(Calby Ng)',
       'url': 'https://www.youtube.com/watch?v=pgK3SEONYmE&t=885s',
       'video_id': 'pgK3SEONYmE'},
      {'author': 'thumbsuprun',
       'channel': 'thumbsuprun',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:55](https://www.youtube.com/watch?v=sBvNovp3-P0&t=475s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Bit late you might just forget about it all together so again make sure you '
               'get that sleep very.',
       'timestamp': 475,
       'timestamp_label': '[00:07:55]',
       'timestamp_seconds': 475,
       'tip': 'Bit late you might just forget about it all together so again make sure you get '
              'that sleep very.',
       'title': 'HOW TO PREPARE FOR A TICKETMASTER VERIFIED FAN PRESALE | BUY PRESALE TICKETS '
                'WAITLISTED VS SELECTED (thumbsuprun)',
       'url': 'https://www.youtube.com/watch?v=sBvNovp3-P0&t=475s',
       'video_id': 'sBvNovp3-P0'},
      {'author': 'Ticket Flipping',
       'channel': 'Ticket Flipping',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:03](https://www.youtube.com/watch?v=M7PkhZcLJys&t=63s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Money flipping tickets visit ticketflipping.com and we'll show you how to "
               'really do it go into a lot more depth there and you get access to our training '
               'course video guides and a bunch of tools that are really going to take your '
               'resale to the next level.',
       'timestamp': 63,
       'timestamp_label': '[00:01:03]',
       'timestamp_seconds': 63,
       'tip': "Money flipping tickets visit ticketflipping.com and we'll show you how to "
              'really do it go into a lot more depth there and you get access to our training '
              'course video guides and a bunch of tools that are really going to take your '
              'resale to the next level.',
       'title': 'How to get paid right away for your tickets (Ticket Flipping)',
       'url': 'https://www.youtube.com/watch?v=M7PkhZcLJys&t=63s',
       'video_id': 'M7PkhZcLJys'}],
 11: [{'author': 'Cal Barton',
       'channel': 'Cal Barton',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:59](https://www.youtube.com/watch?v=sVToTQaS_Dw&t=179s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'They had personal cards, business cards, 11 Amex cards total. He also '
               "participated in Amex's small business working capital program, eventually "
               'scaling his line of credit from 75K to 150K as his business grew.',
       'timestamp': 179,
       'timestamp_label': '[00:02:59]',
       'timestamp_seconds': 179,
       'tip': 'They had personal cards, business cards, 11 Amex cards total. He also '
              "participated in Amex's small business working capital program, eventually "
              'scaling his line of credit from 75K to 150K as his business grew.',
       'title': 'Amex Account Shutdowns Are Out of Control! (Cal Barton)',
       'url': 'https://www.youtube.com/watch?v=sVToTQaS_Dw&t=179s',
       'video_id': 'sVToTQaS_Dw'},
      {'author': 'Colin Matthew',
       'channel': 'Colin Matthew',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:38](https://www.youtube.com/watch?v=gTpUtrhQsnM&t=878s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Banks have a total exposure limit. Most banks, especially Chase, have a '
               'maximum exposure. They will only lend about 50% of your total annual income '
               'across all of your cards with that bank combined.',
       'timestamp': 878,
       'timestamp_label': '[00:14:38]',
       'timestamp_seconds': 878,
       'tip': 'Banks have a total exposure limit. Most banks, especially Chase, have a maximum '
              'exposure. They will only lend about 50% of your total annual income across all '
              'of your cards with that bank combined.',
       'title': 'Do THIS To Get MASSIVE SOFT PULL Credit Limit Increases (FAST) (Colin '
                'Matthew)',
       'url': 'https://www.youtube.com/watch?v=gTpUtrhQsnM&t=878s',
       'video_id': 'gTpUtrhQsnM'},
      {'author': 'Joey | Amazon FBA',
       'channel': 'Joey | Amazon FBA',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:26](https://www.youtube.com/watch?v=tKw8SljNcPE&t=446s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re expecting to scale or you already are scaling just because it allows you "
               'more access to funding without a massive obligation to have that same cash on '
               'hand right?',
       'timestamp': 446,
       'timestamp_label': '[00:07:26]',
       'timestamp_seconds': 446,
       'tip': "'re expecting to scale or you already are scaling just because it allows you "
              'more access to funding without a massive obligation to have that same cash on '
              'hand right?',
       'title': 'The BEST Way to Leverage Business Credit as an Amazon Online Arbitrage Seller '
                '[2026 Full Guide] (Joey | Amazon FBA)',
       'url': 'https://www.youtube.com/watch?v=tKw8SljNcPE&t=446s',
       'video_id': 'tKw8SljNcPE'},
      {'author': 'TackleIMS',
       'channel': 'TackleIMS',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:21](https://www.youtube.com/watch?v=WLaBGRjvR2M&t=201s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Invite someone by email, give them a role, change it later, or take them off '
               'the team. And their past records keep their name. An administrator can do all '
               'of this, too, everything but granting ownership for a partner or '
               'second-in-command.',
       'timestamp': 201,
       'timestamp_label': '[00:03:21]',
       'timestamp_seconds': 201,
       'tip': 'Invite someone by email, give them a role, change it later, or take them off '
              'the team. And their past records keep their name. An administrator can do all '
              'of this, too, everything but granting ownership for a partner or '
              'second-in-command.',
       'title': 'Tackle shop POS roles: counter, manager, bookkeeper, owner | TackleIMS '
                '(TackleIMS)',
       'url': 'https://www.youtube.com/watch?v=WLaBGRjvR2M&t=201s',
       'video_id': 'WLaBGRjvR2M'},
      {'author': 'JA The Panther Guy',
       'channel': 'JA The Panther Guy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:22](https://www.youtube.com/watch?v=59o6u0b6Kz0&t=502s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That's how the price you pay. And those are the sources on the right side. You "
               'got marketplace as sources as well for the NHL. All those sources there is in '
               'the corner right of each team.',
       'timestamp': 502,
       'timestamp_label': '[00:08:22]',
       'timestamp_seconds': 502,
       'tip': "That's how the price you pay. And those are the sources on the right side. You "
              'got marketplace as sources as well for the NHL. All those sources there is in '
              'the corner right of each team.',
       'title': 'NHL every outdoor game avg resell tickets prices highest to lowers #nhl (JA '
                'The Panther Guy)',
       'url': 'https://www.youtube.com/watch?v=59o6u0b6Kz0&t=502s',
       'video_id': '59o6u0b6Kz0'},
      {'author': 'ABC10',
       'channel': 'ABC10',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=je9hw5gRKNA&t=21s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You know, the big, big 2000 team and that was grea. Season ticket holders like '
               'Robin Cleary have been through it all for her. The UPS and mostly downs of the '
               'last 24 years. I knew that we were going to win the championship every year.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'You know, the big, big 2000 team and that was grea. Season ticket holders like '
              'Robin Cleary have been through it all for her. The UPS and mostly downs of the '
              'last 24 years. I knew that we were going to win the championship every year.',
       'title': 'What you need to know about Kings v. Warriors playoff tickets (ABC10)',
       'url': 'https://www.youtube.com/watch?v=je9hw5gRKNA&t=21s',
       'video_id': 'je9hw5gRKNA'},
      {'author': 'ClarityVenturesVideo',
       'channel': 'ClarityVenturesVideo',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:44](https://www.youtube.com/watch?v=qcQs8Xq3hPg&t=344s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Or does it allow them to purchase up to five hundred dollars a month on '
               'account but anything larger than that gets forward to a procurement manager '
               'for.',
       'timestamp': 344,
       'timestamp_label': '[00:05:44]',
       'timestamp_seconds': 344,
       'tip': 'Or does it allow them to purchase up to five hundred dollars a month on account '
              'but anything larger than that gets forward to a procurement manager for.',
       'title': 'Buying Groups Webinar - What is a Buying Group? (ClarityVenturesVideo)',
       'url': 'https://www.youtube.com/watch?v=qcQs8Xq3hPg&t=344s',
       'video_id': 'qcQs8Xq3hPg'},
      {'author': 'Greg B',
       'channel': 'Greg B',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:19](https://www.youtube.com/watch?v=xAStH-KBkrs&t=79s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Here's what most people don't know about fees. StubHub charges a 20 to 25% "
               'service fee on top of the ticket price. But, some platforms like SeatGeek have '
               "lower fees, and the official team sites often have no fees at all. Now, here's "
               "the thing most people don't know.",
       'timestamp': 79,
       'timestamp_label': '[00:01:19]',
       'timestamp_seconds': 79,
       'tip': "Here's what most people don't know about fees. StubHub charges a 20 to 25% "
              'service fee on top of the ticket price. But, some platforms like SeatGeek have '
              "lower fees, and the official team sites often have no fees at all. Now, here's "
              "the thing most people don't know.",
       'title': '🎟️ DO NOT Buy StubHub Tickets Before You Hear This 😱 This strategy saved me '
                'hundreds on sports (Greg B)',
       'url': 'https://www.youtube.com/watch?v=xAStH-KBkrs&t=79s',
       'video_id': 'xAStH-KBkrs'},
      {'author': 'Just Money Ish',
       'channel': 'Just Money Ish',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:16](https://www.youtube.com/watch?v=04bDgAQcsYs&t=376s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Chase branch and applying for the credit card there with a relationship '
               'manager and letting him know why you need a specific amount of funds for your '
               'business, so that way he could justify it to the underwriter. But, not all of '
               'them are willing to do this for you guys.',
       'timestamp': 376,
       'timestamp_label': '[00:06:16]',
       'timestamp_seconds': 376,
       'tip': 'Chase branch and applying for the credit card there with a relationship manager '
              'and letting him know why you need a specific amount of funds for your business, '
              'so that way he could justify it to the underwriter. But, not all of them are '
              'willing to do this for you guys.',
       'title': '5 Reasons Why You Should Get the Chase Ink Business Unlimited Credit Card! '
                '(Just Money Ish)',
       'url': 'https://www.youtube.com/watch?v=04bDgAQcsYs&t=376s',
       'video_id': '04bDgAQcsYs'},
      {'author': 'John Muscarello',
       'channel': 'John Muscarello',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:19](https://www.youtube.com/watch?v=ThO9ard-k8E&t=559s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Was fraud um so you really want this yes I do okay let me rerun it or place '
               "the order again and we'll make sure your account doesn't get flagged had this.",
       'timestamp': 559,
       'timestamp_label': '[00:09:19]',
       'timestamp_seconds': 559,
       'tip': 'Was fraud um so you really want this yes I do okay let me rerun it or place the '
              "order again and we'll make sure your account doesn't get flagged had this.",
       'title': 'How to Avoid Order Cancellations When Doing Online Arbitrage - Amazon FBA Pro '
                'Tips (John Muscarello)',
       'url': 'https://www.youtube.com/watch?v=ThO9ard-k8E&t=559s',
       'video_id': 'ThO9ard-k8E'},
      {'author': 'Tickets 101',
       'channel': 'Tickets 101',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:19](https://www.youtube.com/watch?v=1ZNkmoIj-S8&t=19s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Tickets from a secondary website is to make sure that they transfer the '
               "tickets to your account through the primary website so let's say the primary "
               'website.',
       'timestamp': 19,
       'timestamp_label': '[00:00:19]',
       'timestamp_seconds': 19,
       'tip': 'Tickets from a secondary website is to make sure that they transfer the tickets '
              "to your account through the primary website so let's say the primary website.",
       'title': 'Are My BTS Tickets Real?? Vivid Seats. StubHub. SeatGeek. (Tickets 101)',
       'url': 'https://www.youtube.com/watch?v=1ZNkmoIj-S8&t=19s',
       'video_id': '1ZNkmoIj-S8'},
      {'author': 'Mr. Will Roundtree',
       'channel': 'Mr. Will Roundtree',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:10](https://www.youtube.com/watch?v=a1MwAkYtYBE&t=670s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Position of having great credit to even put these strategies into play you can '
               'reach out to my team or see the link in the bio to get more information about '
               'improving and going through our credit optimization program but until then '
               "I'll see you at the top peace.",
       'timestamp': 670,
       'timestamp_label': '[00:11:10]',
       'timestamp_seconds': 670,
       'tip': 'Position of having great credit to even put these strategies into play you can '
              'reach out to my team or see the link in the bio to get more information about '
              "improving and going through our credit optimization program but until then I'll "
              'see you at the top peace.',
       'title': 'How I Use Credit Cards To Make Money With No Money (Mr. Will Roundtree)',
       'url': 'https://www.youtube.com/watch?v=a1MwAkYtYBE&t=670s',
       'video_id': 'a1MwAkYtYBE'},
      {'author': 'TiqAssist',
       'channel': 'TiqAssist',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:55](https://www.youtube.com/watch?v=7xoI46m2EG8&t=55s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Affect your resale value as the season progresses it's the competitive "
               'competitiveness of your team and the health of your starting quarterback if.',
       'timestamp': 55,
       'timestamp_label': '[00:00:55]',
       'timestamp_seconds': 55,
       'tip': "Affect your resale value as the season progresses it's the competitive "
              'competitiveness of your team and the health of your starting quarterback if.',
       'title': 'Best Way To Sell NFL and NBA Tickets - TiqAssist Season Ticket Talk - Episode '
                '1 (TiqAssist)',
       'url': 'https://www.youtube.com/watch?v=7xoI46m2EG8&t=55s',
       'video_id': '7xoI46m2EG8'},
      {'author': 'thumbsuprun',
       'channel': 'thumbsuprun',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:40](https://www.youtube.com/watch?v=5yZoObwVnRk&t=40s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Everybody else this is all about how to get first in line in the ticketmaster '
               'smart queue every single time this is the big one.',
       'timestamp': 40,
       'timestamp_label': '[00:00:40]',
       'timestamp_seconds': 40,
       'tip': 'Everybody else this is all about how to get first in line in the ticketmaster '
              'smart queue every single time this is the big one.',
       'title': 'THE SECRET TO ALWAYS GETTING FIRST IN LINE FOR TICKETMASTER SMART QUEUE! '
                '(thumbsuprun)',
       'url': 'https://www.youtube.com/watch?v=5yZoObwVnRk&t=40s',
       'video_id': '5yZoObwVnRk'},
      {'author': 'Fundovia',
       'channel': 'Fundovia',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:55](https://www.youtube.com/watch?v=bYLTSIgEHZs&t=115s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '150,000 of that spending each year. The current offer is 100,000 bonus points '
               'after $8,000 of spending in the first 3 months. Employee cards are free with '
               'the Ink Preferred. Your team spends on the same account and you keep the '
               'points.',
       'timestamp': 115,
       'timestamp_label': '[00:01:55]',
       'timestamp_seconds': 115,
       'tip': '150,000 of that spending each year. The current offer is 100,000 bonus points '
              'after $8,000 of spending in the first 3 months. Employee cards are free with '
              'the Ink Preferred. Your team spends on the same account and you keep the '
              'points.',
       'title': 'How to Get $150K in Business Credit: Top 3 Banks (Stack Them in This Order) '
                '(Fundovia)',
       'url': 'https://www.youtube.com/watch?v=bYLTSIgEHZs&t=115s',
       'video_id': 'bYLTSIgEHZs'}],
 12: [{'author': 'Czech It Out: Money Hacks',
       'channel': 'Czech It Out: Money Hacks',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:44](https://www.youtube.com/watch?v=HNO_8rnhPeE&t=44s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And they will ask you to buy the product for them. As soon as they receive it, '
               'they will send you AC transfer back to your bank account. So technically, you '
               'can start this with no money down because you use your credit card.',
       'timestamp': 44,
       'timestamp_label': '[00:00:44]',
       'timestamp_seconds': 44,
       'tip': 'And they will ask you to buy the product for them. As soon as they receive it, '
              'they will send you AC transfer back to your bank account. So technically, you '
              'can start this with no money down because you use your credit card.',
       'title': 'How I Made $X,XXX in My First Month with BuyForMeRetail (BFMR Review) | '
                'Online Side Hustle (Czech It Out: Money Hacks)',
       'url': 'https://www.youtube.com/watch?v=HNO_8rnhPeE&t=44s',
       'video_id': 'HNO_8rnhPeE'},
      {'author': 'Chase Yokoyama',
       'channel': 'Chase Yokoyama',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:30](https://www.youtube.com/watch?v=-tJAC79lKi8&t=690s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Apple TV and Apple Music for 12 months, which Chase values at $324, a free '
               'DashPass membership plus up to $420 a year on DoorDash promos, $10 a month for '
               "Lyft, and $10 a month for Peloton. Add it all up, and that's about $2,500 in "
               'credits on a $795 annual fee card.',
       'timestamp': 690,
       'timestamp_label': '[00:11:30]',
       'timestamp_seconds': 690,
       'tip': 'Apple TV and Apple Music for 12 months, which Chase values at $324, a free '
              'DashPass membership plus up to $420 a year on DoorDash promos, $10 a month for '
              "Lyft, and $10 a month for Peloton. Add it all up, and that's about $2,500 in "
              'credits on a $795 annual fee card.',
       'title': 'Amex Platinum vs Chase Reserve vs Capital One Venture X (Which to Get) (Chase '
                'Yokoyama)',
       'url': 'https://www.youtube.com/watch?v=-tJAC79lKi8&t=690s',
       'video_id': '-tJAC79lKi8'},
      {'author': 'Christopher Grant',
       'channel': 'Christopher Grant',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:20](https://www.youtube.com/watch?v=GFmuZ9Z3Drg&t=80s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Not sure exactly where the line is, but one seller was blocked after placing '
               'plus or minus 10 consecutive orders for about five days a week over the period '
               'of a month. So, Target is actually pretty hard to get banned.',
       'timestamp': 80,
       'timestamp_label': '[00:01:20]',
       'timestamp_seconds': 80,
       'tip': 'Not sure exactly where the line is, but one seller was blocked after placing '
              'plus or minus 10 consecutive orders for about five days a week over the period '
              'of a month. So, Target is actually pretty hard to get banned.',
       'title': 'Online Arbitrage Orders Keep Getting Canceled? 👎 [Here is a Solution] | OA '
                'Buddy (Christopher Grant)',
       'url': 'https://www.youtube.com/watch?v=GFmuZ9Z3Drg&t=80s',
       'video_id': 'GFmuZ9Z3Drg'},
      {'author': 'Walker Deibel',
       'channel': 'Walker Deibel',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:14](https://www.youtube.com/watch?v=PGcp5CLCmWs&t=254s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And I want you to on big orders, I want you to add deposits and milestone '
               'payments. I want you to quantify all of these dollars. And when you go to the '
               'meeting at the bank to get the bank financing, bring them, okay?',
       'timestamp': 254,
       'timestamp_label': '[00:04:14]',
       'timestamp_seconds': 254,
       'tip': 'And I want you to on big orders, I want you to add deposits and milestone '
              'payments. I want you to quantify all of these dollars. And when you go to the '
              'meeting at the bank to get the bank financing, bring them, okay?',
       'title': 'Buying the Float: The Hidden Cash Flow Trap in Every Deal (Walker Deibel)',
       'url': 'https://www.youtube.com/watch?v=PGcp5CLCmWs&t=254s',
       'video_id': 'PGcp5CLCmWs'},
      {'author': 'Stephen Smith',
       'channel': 'Stephen Smith',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:02](https://www.youtube.com/watch?v=RY2Q9yq3v3E&t=302s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s good side really fast, you want to start putting money into their accounts. "
               "When you open a new checking account with a bank or a credit union, you don't "
               'want to just deposit the minimum required amount.',
       'timestamp': 302,
       'timestamp_label': '[00:05:02]',
       'timestamp_seconds': 302,
       'tip': "'s good side really fast, you want to start putting money into their accounts. "
              "When you open a new checking account with a bank or a credit union, you don't "
              'want to just deposit the minimum required amount.',
       'title': "The Only Credit Limit Increase Video You'll Ever Need (2026) (Stephen Smith)",
       'url': 'https://www.youtube.com/watch?v=RY2Q9yq3v3E&t=302s',
       'video_id': 'RY2Q9yq3v3E'},
      {'author': 'RJ Financial',
       'channel': 'RJ Financial',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:32](https://www.youtube.com/watch?v=vfXgcEGNVuM&t=512s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Down they take all your points right other issue or sometimes they allow you '
               "30 days to move out basically amex doesn't do that you'll lose like all.",
       'timestamp': 512,
       'timestamp_label': '[00:08:32]',
       'timestamp_seconds': 512,
       'tip': 'Down they take all your points right other issue or sometimes they allow you 30 '
              "days to move out basically amex doesn't do that you'll lose like all.",
       'title': 'Amex Financial Reviews - Honesty Counts! (RJ Financial)',
       'url': 'https://www.youtube.com/watch?v=vfXgcEGNVuM&t=512s',
       'video_id': 'vfXgcEGNVuM'},
      {'author': 'Emmanuel Ak',
       'channel': 'Emmanuel Ak',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=YTBKTfhq9bg&t=20s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, Hardwell NYC released tickets this week. You can see here all the '
               'information was given in the discord analysis risk price and we all made money '
               'off it. Well, those who bought the tickets made money and let me show you how '
               'this works.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'So, Hardwell NYC released tickets this week. You can see here all the '
              'information was given in the discord analysis risk price and we all made money '
              'off it. Well, those who bought the tickets made money and let me show you how '
              'this works.',
       'title': 'i made this much in a day from concert tickets (copy me lol) (Emmanuel Ak)',
       'url': 'https://www.youtube.com/watch?v=YTBKTfhq9bg&t=20s',
       'video_id': 'YTBKTfhq9bg'},
      {'author': 'Points Panda',
       'channel': 'Points Panda',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:32](https://www.youtube.com/watch?v=rUdn6piNvLA&t=212s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Entire four-hour course where we show you absolutely everything you need to '
               'know to be a travel happy professional with all that being said thanks so much '
               'for watching the video have an awesome day.',
       'timestamp': 212,
       'timestamp_label': '[00:03:32]',
       'timestamp_seconds': 212,
       'tip': 'Entire four-hour course where we show you absolutely everything you need to '
              'know to be a travel happy professional with all that being said thanks so much '
              'for watching the video have an awesome day.',
       'title': 'Amex Plum Card Review - Net 60 Payment Credit Card for Business Owners '
                '(Points Panda)',
       'url': 'https://www.youtube.com/watch?v=rUdn6piNvLA&t=212s',
       'video_id': 'rUdn6piNvLA'},
      {'author': 'Dick “Lens Flare Transitions” Nixon',
       'channel': 'Dick “Lens Flare Transitions” Nixon',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:12](https://www.youtube.com/watch?v=K8GzDJBkdwQ&t=492s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Dropping the price um yeah scarcity people pay for a premium uh can you change '
               'pricing regularly okay okay so yes the day of the week is very.',
       'timestamp': 492,
       'timestamp_label': '[00:08:12]',
       'timestamp_seconds': 492,
       'tip': 'Dropping the price um yeah scarcity people pay for a premium uh can you change '
              'pricing regularly okay okay so yes the day of the week is very.',
       'title': 'How to make money online selling / reselling tickets on Stubhub and '
                'Ticketmaster (Dick “Lens Flare Transitions” Nixon)',
       'url': 'https://www.youtube.com/watch?v=K8GzDJBkdwQ&t=492s',
       'video_id': 'K8GzDJBkdwQ'},
      {'author': 'makazo!',
       'channel': 'makazo!',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:30](https://www.youtube.com/watch?v=IMb7_xt0ZW4&t=510s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I'm still in Q for the other day, but it's okay. It's probably all sold out. "
               "It's time for Met Life to Okay, it turned 1:00 a. 's still not letting me in "
               'the queue yet.',
       'timestamp': 510,
       'timestamp_label': '[00:08:30]',
       'timestamp_seconds': 510,
       'tip': "I'm still in Q for the other day, but it's okay. It's probably all sold out. "
              "It's time for Met Life to Okay, it turned 1:00 a. 's still not letting me in "
              'the queue yet.',
       'title': 'FIGHTING THE BTS TICKETMASTER WAR 😭😭😭😭 (I got some of the worst queue numbers '
                'I’ve ever seen 😭) (makazo!)',
       'url': 'https://www.youtube.com/watch?v=IMb7_xt0ZW4&t=510s',
       'video_id': 'IMb7_xt0ZW4'},
      {'author': 'ZEPHRA',
       'channel': 'ZEPHRA',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:22](https://www.youtube.com/watch?v=wqsrNbgFdtg&t=22s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'StubHub so your payment can move forward. Start by going to StubHub and '
               "signing into your account. Once you're in, list your SeatGeek tickets for sale "
               'on StubHub.',
       'timestamp': 22,
       'timestamp_label': '[00:00:22]',
       'timestamp_seconds': 22,
       'tip': 'StubHub so your payment can move forward. Start by going to StubHub and signing '
              "into your account. Once you're in, list your SeatGeek tickets for sale on "
              'StubHub.',
       'title': 'How To Transfer Seatgeek Tickets To Stubhub (ZEPHRA)',
       'url': 'https://www.youtube.com/watch?v=wqsrNbgFdtg&t=22s',
       'video_id': 'wqsrNbgFdtg'},
      {'author': 'Bytes Media',
       'channel': 'Bytes Media',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:49](https://www.youtube.com/watch?v=AEyd6uOijzg&t=49s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'QuickBooks or Excel, virtual card numbers for safer online payments, and $0 '
               'fraud liability, which are all genuinely helpful day-to-day features. With '
               "that said, it's not perfect.",
       'timestamp': 49,
       'timestamp_label': '[00:00:49]',
       'timestamp_seconds': 49,
       'tip': 'QuickBooks or Excel, virtual card numbers for safer online payments, and $0 '
              'fraud liability, which are all genuinely helpful day-to-day features. With that '
              "said, it's not perfect.",
       'title': 'Capital One Spark Classic Credit Card Review 2026 | Business Credit Building '
                'Card Explained (Bytes Media)',
       'url': 'https://www.youtube.com/watch?v=AEyd6uOijzg&t=49s',
       'video_id': 'AEyd6uOijzg'},
      {'author': 'Stephen Smith',
       'channel': 'Stephen Smith',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:01](https://www.youtube.com/watch?v=bYSi0VFWtpg&t=121s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Instead of looking at your balance only at the end of the month, the issuer '
               'calculates interest by adding up your balance every day of the billing cycle, '
               'averaging those numbers and then applying the interest rate to that average.',
       'timestamp': 121,
       'timestamp_label': '[00:02:01]',
       'timestamp_seconds': 121,
       'tip': 'Instead of looking at your balance only at the end of the month, the issuer '
              'calculates interest by adding up your balance every day of the billing cycle, '
              'averaging those numbers and then applying the interest rate to that average.',
       'title': 'Velocity Banking Explained: If Your Credit Cards Are Maxed Out Then DO THIS '
                '(Stephen Smith)',
       'url': 'https://www.youtube.com/watch?v=bYSi0VFWtpg&t=121s',
       'video_id': 'bYSi0VFWtpg'},
      {'author': 'Line Item',
       'channel': 'Line Item',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:22](https://www.youtube.com/watch?v=4PXlRtr3IyQ&t=562s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Live Nation says it will appeal. A remedies trial, where states want '
               'Ticketmaster split from Live Nation, is not expected to start before February. '
               "The Justice Department deal is waiting on court approval. The FTC's own case "
               'about fees is in discovery.',
       'timestamp': 562,
       'timestamp_label': '[00:09:22]',
       'timestamp_seconds': 562,
       'tip': 'Live Nation says it will appeal. A remedies trial, where states want '
              'Ticketmaster split from Live Nation, is not expected to start before February. '
              "The Justice Department deal is waiting on court approval. The FTC's own case "
              'about fees is in discovery.',
       'title': 'Why a $20 Concert Ticket Comes With $23 in Fees (Line Item)',
       'url': 'https://www.youtube.com/watch?v=4PXlRtr3IyQ&t=562s',
       'video_id': '4PXlRtr3IyQ'},
      {'author': 'CardsChooser',
       'channel': 'CardsChooser',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:14](https://www.youtube.com/watch?v=pie5mBLwycU&t=134s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BG`) purchase-order fulfillment stacked with uncapped '
                    '`2%–4%` commercial card float/rebates, and `BOTS Act`-compliant secondary '
                    'live-event ticket, `SSL`, and corporate-suite allocation brokerage '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Now the next one that we're going to find here number two is a US Bank Triple "
               'Cash. It got also no annual fee and 750 bonus after 6,180 days. There you '
               'going to have 3% foreign fee and 0% on the purchases and transfers for 12 '
               'billing cycles.',
       'timestamp': 134,
       'timestamp_label': '[00:02:14]',
       'timestamp_seconds': 134,
       'tip': "Now the next one that we're going to find here number two is a US Bank Triple "
              'Cash. It got also no annual fee and 750 bonus after 6,180 days. There you going '
              'to have 3% foreign fee and 0% on the purchases and transfers for 12 billing '
              'cycles.',
       'title': 'Best Business Card Bonuses in November 2026  - Ink Cash vs Triple Cash vs Ink '
                'Unlimited (CardsChooser)',
       'url': 'https://www.youtube.com/watch?v=pie5mBLwycU&t=134s',
       'video_id': 'pie5mBLwycU'}]}
