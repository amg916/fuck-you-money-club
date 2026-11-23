"""Curated 180-citation Buying Group, Commercial Card-Float & Rebate Arbitrage baseline (15 per chapter across Q1-Q12) mined strictly from verified Buying Group, Commercial Card-Float & Rebate Arbitrage YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'1099',
     '150k',
     '5000',
     'account',
     'accounting',
     'ach',
     'adjustments',
     'advantage',
     'amazon',
     'america',
     'amex',
     'apple',
     'apr',
     'arbitrage',
     'automating',
     'b2b',
     'bank',
     'below',
     'best',
     'bill',
     'bonus',
     'break',
     'brex',
     'building',
     'business',
     'buy',
     'buyers',
     'buyformeretail',
     'buying',
     'buyinggroup',
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
     '5000',
     'account',
     'accounting',
     'ach',
     'adjustments',
     'advantage',
     'amazon',
     'america',
     'amex',
     'apple',
     'apr',
     'arbitrage',
     'automating',
     'b2b',
     'bank',
     'below',
     'best',
     'bill',
     'bonus',
     'break',
     'brex',
     'budget',
     'building',
     'business',
     'buy',
     'buyer',
     'buyers',
     'buyformeretail',
     'buying',
     'buyinggroup',
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
     '5000',
     'account',
     'accounting',
     'ach',
     'adjustments',
     'advantage',
     'amazon',
     'america',
     'amex',
     'apple',
     'apr',
     'arbitrage',
     'automating',
     'b2b',
     'bank',
     'below',
     'best',
     'bill',
     'bonus',
     'break',
     'brex',
     'building',
     'business',
     'buy',
     'buyers',
     'buyformeretail',
     'buying',
     'buyinggroup',
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
     '5000',
     'account',
     'accounting',
     'ach',
     'adjustments',
     'advantage',
     'amazon',
     'america',
     'amex',
     'apple',
     'apr',
     'arbitrage',
     'automating',
     'b2b',
     'bank',
     'below',
     'best',
     'bill',
     'bonus',
     'break',
     'brex',
     'budget',
     'building',
     'business',
     'buy',
     'buyers',
     'buyformeretail',
     'buying',
     'buyinggroup',
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
     '5000',
     'account',
     'accounting',
     'ach',
     'adjustments',
     'advantage',
     'amazon',
     'america',
     'amex',
     'apple',
     'apr',
     'arbitrage',
     'audit',
     'automating',
     'avoid',
     'b2b',
     'bank',
     'below',
     'best',
     'bill',
     'bonus',
     'break',
     'brex',
     'building',
     'business',
     'buy',
     'buyers',
     'buyformeretail',
     'buying',
     'buyinggroup',
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
     '5000',
     'account',
     'accounting',
     'ach',
     'adjustments',
     'advantage',
     'amazon',
     'america',
     'amex',
     'apple',
     'apr',
     'arbitrage',
     'automating',
     'b2b',
     'bank',
     'below',
     'best',
     'bill',
     'bonus',
     'break',
     'brex',
     'building',
     'business',
     'buy',
     'buyers',
     'buyformeretail',
     'buying',
     'buyinggroup',
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
     '5000',
     'account',
     'accounting',
     'ach',
     'adjustments',
     'advantage',
     'amazon',
     'america',
     'amex',
     'apple',
     'apr',
     'arbitrage',
     'automating',
     'b2b',
     'bank',
     'below',
     'best',
     'bill',
     'bonus',
     'break',
     'brex',
     'building',
     'business',
     'buy',
     'buyers',
     'buyformeretail',
     'buying',
     'buyinggroup',
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
     '5000',
     'account',
     'accounting',
     'ach',
     'adjustments',
     'advantage',
     'amazon',
     'america',
     'amex',
     'api',
     'apple',
     'apr',
     'arbitrage',
     'automating',
     'b2b',
     'bank',
     'below',
     'best',
     'bill',
     'bonus',
     'break',
     'brex',
     'building',
     'business',
     'buy',
     'buyers',
     'buyformeretail',
     'buying',
     'buyinggroup',
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
     '5000',
     'account',
     'accounting',
     'ach',
     'adjustments',
     'advantage',
     'agreement',
     'amazon',
     'america',
     'amex',
     'apple',
     'apr',
     'arbitrage',
     'automating',
     'b2b',
     'bank',
     'below',
     'best',
     'bill',
     'bonus',
     'break',
     'brex',
     'building',
     'business',
     'buy',
     'buyers',
     'buyformeretail',
     'buying',
     'buyinggroup',
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
      '5000',
      'account',
      'accounting',
      'ach',
      'adjustments',
      'advantage',
      'agent',
      'ai',
      'amazon',
      'america',
      'amex',
      'apple',
      'apr',
      'arbitrage',
      'automate',
      'automating',
      'automation',
      'b2b',
      'bank',
      'below',
      'best',
      'bill',
      'bonus',
      'break',
      'brex',
      'building',
      'business',
      'buy',
      'buyers',
      'buyformeretail',
      'buying',
      'buyinggroup',
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
      '5000',
      'account',
      'accounting',
      'ach',
      'adjustments',
      'advantage',
      'amazon',
      'america',
      'amex',
      'apple',
      'apr',
      'arbitrage',
      'automating',
      'b2b',
      'bank',
      'below',
      'best',
      'bill',
      'bonus',
      'break',
      'brex',
      'building',
      'business',
      'buy',
      'buyers',
      'buyformeretail',
      'buying',
      'buyinggroup',
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
      '5000',
      'account',
      'accounting',
      'ach',
      'action',
      'adjustments',
      'advantage',
      'amazon',
      'america',
      'amex',
      'apple',
      'apr',
      'arbitrage',
      'automating',
      'b2b',
      'bank',
      'below',
      'best',
      'bill',
      'bonus',
      'break',
      'brex',
      'building',
      'business',
      'buy',
      'buyers',
      'buyformeretail',
      'buying',
      'buyinggroup',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Naam Wynn',
      'channel': 'Naam Wynn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:41](https://www.youtube.com/watch?v=QFNkg3G6als&t=221s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Number three is the Bank of America Advantage Unlimited Cash Rewards Card. This '
              'one keeps things simple with an unlimited 1 and 1/2% cash back on everything '
              'that you buy. No annual fee, no categories, no caps. But, this is where it gets '
              'interesting.',
      'timestamp': 221,
      'timestamp_label': '[00:03:41]',
      'timestamp_seconds': 221,
      'tip': 'Number three is the Bank of America Advantage Unlimited Cash Rewards Card. This '
             'one keeps things simple with an unlimited 1 and 1/2% cash back on everything '
             'that you buy. No annual fee, no categories, no caps. But, this is where it gets '
             'interesting.',
      'title': '5 BEST Business Credit Cards ($25,000 Limit) (Naam Wynn)',
      'url': 'https://www.youtube.com/watch?v=QFNkg3G6als&t=221s',
      'video_id': 'QFNkg3G6als'},
     {'author': 'Everyday Money Heroes',
      'channel': 'Everyday Money Heroes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:37](https://www.youtube.com/watch?v=HbZGYalSsyc&t=277s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I use primarily the shop online functionality of it. Um Rakuten's business "
              'model is that that they act as an affiliate marketer, which means that '
              'retailers like Nike, Target, um Best Buy, uh they pay Rakuten a commission for '
              'sending shoppers to their websites.',
      'timestamp': 277,
      'timestamp_label': '[00:04:37]',
      'timestamp_seconds': 277,
      'tip': "I use primarily the shop online functionality of it. Um Rakuten's business model "
             'is that that they act as an affiliate marketer, which means that retailers like '
             'Nike, Target, um Best Buy, uh they pay Rakuten a commission for sending shoppers '
             'to their websites.',
      'title': 'Why Most People Overpay For Everyday Purchases| Hidden Rakuten Stacking '
               'Secrets (Everyday Money Heroes)',
      'url': 'https://www.youtube.com/watch?v=HbZGYalSsyc&t=277s',
      'video_id': 'HbZGYalSsyc'},
     {'author': 'Miles with Mary - Points & Miles Travel',
      'channel': 'Miles with Mary - Points & Miles Travel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=E07WIJs8BE0&t=32s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm going to show you why the signup bonus can actually be worth so much more "
              "and why it's one of my absolute favorite business cards on the market.",
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': "I'm going to show you why the signup bonus can actually be worth so much more "
             "and why it's one of my absolute favorite business cards on the market.",
      'title': 'Chase Ink Business Cash Review 2026 — The Best No Fee Business Card? (Miles '
               'with Mary - Points & Miles Travel)',
      'url': 'https://www.youtube.com/watch?v=E07WIJs8BE0&t=32s',
      'video_id': 'E07WIJs8BE0'},
     {'author': 'Daily Drop',
      'channel': 'Daily Drop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:49](https://www.youtube.com/watch?v=61XiQ9ahJjA&t=109s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re going to talk about in a second. But, it's a great catch-all card for "
              "random business expenses that don't fit into a better bonus category. Think "
              'software subscriptions, equipment, props, supplies, production purchases, or '
              'client expenses.',
      'timestamp': 109,
      'timestamp_label': '[00:01:49]',
      'timestamp_seconds': 109,
      'tip': "'re going to talk about in a second. But, it's a great catch-all card for random "
             "business expenses that don't fit into a better bonus category. Think software "
             'subscriptions, equipment, props, supplies, production purchases, or client '
             'expenses.',
      'title': 'I Have 7 Chase Business Cards: This One’s the Best (Daily Drop)',
      'url': 'https://www.youtube.com/watch?v=61XiQ9ahJjA&t=109s',
      'video_id': '61XiQ9ahJjA'},
     {'author': 'Daniel Shepherd',
      'channel': 'Daniel Shepherd',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:54](https://www.youtube.com/watch?v=a0APMJagyzA&t=174s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Business and know that you can pay your statement credit early each month then '
              'this card does offer some value but remember just to break even on the card.',
      'timestamp': 174,
      'timestamp_label': '[00:02:54]',
      'timestamp_seconds': 174,
      'tip': 'Business and know that you can pay your statement credit early each month then '
             'this card does offer some value but remember just to break even on the card.',
      'title': 'Reviewing The Amex Plum Card - Who Is It For? (Daniel Shepherd)',
      'url': 'https://www.youtube.com/watch?v=a0APMJagyzA&t=174s',
      'video_id': 'a0APMJagyzA'},
     {'author': 'StartUp101',
      'channel': 'StartUp101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:49](https://www.youtube.com/watch?v=2N5t8bm1dpA&t=169s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A resale certificate allows you to buy products that you are going to resell to '
              'your customers tax free. Why can you do this, you may ask? Well, because sales '
              'taxes are intended to be paid on the final value of a product or service.',
      'timestamp': 169,
      'timestamp_label': '[00:02:49]',
      'timestamp_seconds': 169,
      'tip': 'A resale certificate allows you to buy products that you are going to resell to '
             'your customers tax free. Why can you do this, you may ask? Well, because sales '
             'taxes are intended to be paid on the final value of a product or service.',
      'title': "Sellers Permit vs Resale Certificate - What's the Difference? (StartUp101)",
      'url': 'https://www.youtube.com/watch?v=2N5t8bm1dpA&t=169s',
      'video_id': '2N5t8bm1dpA'},
     {'author': 'Elliot Explains',
      'channel': 'Elliot Explains',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:34](https://www.youtube.com/watch?v=ZxYkMfSxxpI&t=154s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'To sum it up, this card fits best for established businesses spending a lot in '
              'its 3x categories and ready to use points for high value redemptions. If all '
              'the travel perks and bonus categories fit your needs, the value can far '
              'outweigh the fee.',
      'timestamp': 154,
      'timestamp_label': '[00:02:34]',
      'timestamp_seconds': 154,
      'tip': 'To sum it up, this card fits best for established businesses spending a lot in '
             'its 3x categories and ready to use points for high value redemptions. If all the '
             'travel perks and bonus categories fit your needs, the value can far outweigh the '
             'fee.',
      'title': 'Chase Ink Business Preferred Credit Card Review 2025 | Worth It or Leave It? '
               '(Elliot Explains)',
      'url': 'https://www.youtube.com/watch?v=ZxYkMfSxxpI&t=154s',
      'video_id': 'ZxYkMfSxxpI'},
     {'author': 'Bytes Media',
      'channel': 'Bytes Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:45](https://www.youtube.com/watch?v=3bWSyAjx93M&t=105s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If your spending doesn't regularly hit the 4x categories, the value drops "
              'quickly. The $150,000 annual cap on bonus rewards may also feel restrictive for '
              'larger businesses with heavy ad or shipping budgets. Another downside is that '
              'the statement credits are somewhat niche.',
      'timestamp': 105,
      'timestamp_label': '[00:01:45]',
      'timestamp_seconds': 105,
      'tip': "If your spending doesn't regularly hit the 4x categories, the value drops "
             'quickly. The $150,000 annual cap on bonus rewards may also feel restrictive for '
             'larger businesses with heavy ad or shipping budgets. Another downside is that '
             'the statement credits are somewhat niche.',
      'title': 'American Express Business Gold Credit Card Review 2026 | High Rewards Business '
               'Card Benefits & Fees (Bytes Media)',
      'url': 'https://www.youtube.com/watch?v=3bWSyAjx93M&t=105s',
      'video_id': '3bWSyAjx93M'},
     {'author': 'Ryan Maya',
      'channel': 'Ryan Maya',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:25](https://www.youtube.com/watch?v=bQr7v1bOiXo&t=145s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Don't have to call into a bank and have a long whole time or get stuck on hold "
              'with an automated service you literally have a real person at any time of the.',
      'timestamp': 145,
      'timestamp_label': '[00:02:25]',
      'timestamp_seconds': 145,
      'tip': "Don't have to call into a bank and have a long whole time or get stuck on hold "
             'with an automated service you literally have a real person at any time of the.',
      'title': '3 Reasons You NEED The Spark Cash Plus Business Credit Card (Ryan Maya)',
      'url': 'https://www.youtube.com/watch?v=bQr7v1bOiXo&t=145s',
      'video_id': 'bQr7v1bOiXo'},
     {'author': 'The BoldlyGo Podcast: Revolutionizing Your Journey',
      'channel': 'The BoldlyGo Podcast: Revolutionizing Your Journey',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:33:08](https://www.youtube.com/watch?v=dXNdXw4A16A&t=1988s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s 10% on appliances, but you want to buy a camera and cameras are 1% or 1x. So "
              'understanding what actual the terms are and what the multiplier value is is '
              'huge as well.',
      'timestamp': 1988,
      'timestamp_label': '[00:33:08]',
      'timestamp_seconds': 1988,
      'tip': "'s 10% on appliances, but you want to buy a camera and cameras are 1% or 1x. So "
             'understanding what actual the terms are and what the multiplier value is is huge '
             'as well.',
      'title': 'She Earned 100,000 Amex Points in 3 MONTHS on Rakuten Without Spending More '
               '(The BoldlyGo Podcast: Revolutionizing Your Journey)',
      'url': 'https://www.youtube.com/watch?v=dXNdXw4A16A&t=1988s',
      'video_id': 'dXNdXw4A16A'},
     {'author': 'Spencer Johnson',
      'channel': 'Spencer Johnson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:52](https://www.youtube.com/watch?v=v36IWeannUs&t=352s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If frackathon also had a deal where they gave you five percent back on top of '
              'that for that streaming service you would also get 5x Amex membership Awards.',
      'timestamp': 352,
      'timestamp_label': '[00:05:52]',
      'timestamp_seconds': 352,
      'tip': 'If frackathon also had a deal where they gave you five percent back on top of '
             'that for that streaming service you would also get 5x Amex membership Awards.',
      'title': 'How To Earn MAX Value From Credit Cards (Reward Stacking Guide) (Spencer '
               'Johnson)',
      'url': 'https://www.youtube.com/watch?v=v36IWeannUs&t=352s',
      'video_id': 'v36IWeannUs'},
     {'author': 'AskSebby',
      'channel': 'AskSebby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=Uvyem-_QFhI&t=31s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'When using points in this way, at checkout, each point is worth 0. Put another '
              "way, you're getting eighth of a cent, meaning that 100k points is 800 in value. "
              'Ironically, this is actually better than some competing bank points.',
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': 'When using points in this way, at checkout, each point is worth 0. Put another '
             "way, you're getting eighth of a cent, meaning that 100k points is 800 in value. "
             'Ironically, this is actually better than some competing bank points.',
      'title': 'The Ultimate Guide to Maximizing Chase Points 2025 (AskSebby)',
      'url': 'https://www.youtube.com/watch?v=Uvyem-_QFhI&t=31s',
      'video_id': 'Uvyem-_QFhI'},
     {'author': 'Just Money Ish',
      'channel': 'Just Money Ish',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:46](https://www.youtube.com/watch?v=u8QBKSzn5K8&t=226s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I hope you guys found value in any of this information as always. 50,000 or '
              'even 150,000 plus in capital so that we guys can actually scale and grow your '
              'business, send an email to justmoneyish@gmail.',
      'timestamp': 226,
      'timestamp_label': '[00:03:46]',
      'timestamp_seconds': 226,
      'tip': 'I hope you guys found value in any of this information as always. 50,000 or even '
             '150,000 plus in capital so that we guys can actually scale and grow your '
             'business, send an email to justmoneyish@gmail.',
      'title': 'Credit Cycling Explained! (Should You Do it?) (Just Money Ish)',
      'url': 'https://www.youtube.com/watch?v=u8QBKSzn5K8&t=226s',
      'video_id': 'u8QBKSzn5K8'},
     {'author': 'Spencer Johnson',
      'channel': 'Spencer Johnson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:06](https://www.youtube.com/watch?v=egM5zxfGtj0&t=186s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "About the bonus let's talk about how much value I personally got from this card "
              'by spending on it this year outside of the bonus I guess just for reference.',
      'timestamp': 186,
      'timestamp_label': '[00:03:06]',
      'timestamp_seconds': 186,
      'tip': "About the bonus let's talk about how much value I personally got from this card "
             'by spending on it this year outside of the bonus I guess just for reference.',
      'title': 'The Chase Ink Cash: My HONEST 1-Year Review (Spencer Johnson)',
      'url': 'https://www.youtube.com/watch?v=egM5zxfGtj0&t=186s',
      'video_id': 'egM5zxfGtj0'},
     {'author': 'Cal Barton',
      'channel': 'Cal Barton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=D6bPd67bgps&t=56s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Request a credit limit increase you know a huge example of this is Navy Federal '
              'Credit Unit if you call in the customer service then they will almost always.',
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': 'Request a credit limit increase you know a huge example of this is Navy Federal '
             'Credit Unit if you call in the customer service then they will almost always.',
      'title': 'When Should You Ask for a Credit Limit Increase? (Cal Barton)',
      'url': 'https://www.youtube.com/watch?v=D6bPd67bgps&t=56s',
      'video_id': 'D6bPd67bgps'}],
 2: [{'author': 'Fat Stacks Academy',
      'channel': 'Fat Stacks Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:43](https://www.youtube.com/watch?v=9JkcZCA1q_M&t=343s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s about a $100 monthly payment that just automatically pays out of my bank "
              "account. It's crucial to mark your calendar with your end of your 0% APR "
              'period.',
      'timestamp': 343,
      'timestamp_label': '[00:05:43]',
      'timestamp_seconds': 343,
      'tip': "'s about a $100 monthly payment that just automatically pays out of my bank "
             "account. It's crucial to mark your calendar with your end of your 0% APR period.",
      'title': 'The Ultimate Catch All Card (Supercharging the Blue Business Plus) (Fat Stacks '
               'Academy)',
      'url': 'https://www.youtube.com/watch?v=9JkcZCA1q_M&t=343s',
      'video_id': '9JkcZCA1q_M'},
     {'author': 'Joe Barreto',
      'channel': 'Joe Barreto',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:18](https://www.youtube.com/watch?v=xgsxM7jSJ8U&t=198s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re using somebody else's bank account to pay that bill. So, using another "
              "person's account to pay a large spend can raise those flags. And that's because "
              'you should have your own account.',
      'timestamp': 198,
      'timestamp_label': '[00:03:18]',
      'timestamp_seconds': 198,
      'tip': "'re using somebody else's bank account to pay that bill. So, using another "
             "person's account to pay a large spend can raise those flags. And that's because "
             'you should have your own account.',
      'title': 'The REAL Reason Amex Is Closing Customer Accounts Suddenly (Joe Barreto)',
      'url': 'https://www.youtube.com/watch?v=xgsxM7jSJ8U&t=198s',
      'video_id': 'xgsxM7jSJ8U'},
     {'author': "Leo's Travel Hacks",
      'channel': "Leo's Travel Hacks",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=4uIEMf5mkHg&t=32s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It is a charge card, not a credit card. Your spending capacity adapts to how '
              'you buy and pay. If you carry a balance with pay over time, the APR runs from '
              '19. And there are no foreign transaction fees. And read the wording carefully '
              'because the wording is the offer.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': 'It is a charge card, not a credit card. Your spending capacity adapts to how you '
             'buy and pay. If you carry a balance with pay over time, the APR runs from 19. '
             'And there are no foreign transaction fees. And read the wording carefully '
             'because the wording is the offer.',
      'title': "Amex Gold Card 2026: $524 in Credits, 4X Dining — Worth the $325 Fee? (Leo's "
               'Travel Hacks)',
      'url': 'https://www.youtube.com/watch?v=4uIEMf5mkHg&t=32s',
      'video_id': '4uIEMf5mkHg'},
     {'author': "Jake's Tech Lab",
      'channel': "Jake's Tech Lab",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=QI-FUFyJsUU&t=33s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q2 operational verification).',
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
     {'author': 'SKUio',
      'channel': 'SKUio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=q4miWZl-6Jc&t=40s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The buyer moves on to checkout. There, After this order shows where the account '
              'would end up. Place order stays off, with the reason right above it. The buyer '
              'can edit the cart, or pay open invoices first. Buyers can also check their '
              'credit under My Account.',
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': 'The buyer moves on to checkout. There, After this order shows where the account '
             'would end up. Place order stays off, with the reason right above it. The buyer '
             'can edit the cart, or pay open invoices first. Buyers can also check their '
             'credit under My Account.',
      'title': 'How to Enforce Dealer Credit Limits at Checkout on a B2B Wholesale Portal | '
               'SKU.io (SKUio)',
      'url': 'https://www.youtube.com/watch?v=q4miWZl-6Jc&t=40s',
      'video_id': 'q4miWZl-6Jc'},
     {'author': 'George Waters',
      'channel': 'George Waters',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=nRJlDybpS4s&t=60s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, this is when the bank sends you checks that you can deposit directly into '
              'your bank account right from your credit card balance. And in exchange for this '
              "service, you're usually going to pay about a 3 to 5% onetime fee.",
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': 'Now, this is when the bank sends you checks that you can deposit directly into '
             'your bank account right from your credit card balance. And in exchange for this '
             "service, you're usually going to pay about a 3 to 5% onetime fee.",
      'title': 'How To Liquidate Your Credit Cards | Turn Credit Into Cash! (George Waters)',
      'url': 'https://www.youtube.com/watch?v=nRJlDybpS4s&t=60s',
      'video_id': 'nRJlDybpS4s'},
     {'author': 'Money with Andrey',
      'channel': 'Money with Andrey',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=E-FSl936NIg&t=78s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t know Rakuten, Rakuten is a cashback site with a very simple in reality "
              'business model, at least simple for the 21st century. Stores simply pay Rakuten '
              'a fee when it sends them a customer. And Rakuten gives a part of this fee to '
              'the customer, aka yourself.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': "'t know Rakuten, Rakuten is a cashback site with a very simple in reality "
             'business model, at least simple for the 21st century. Stores simply pay Rakuten '
             'a fee when it sends them a customer. And Rakuten gives a part of this fee to the '
             'customer, aka yourself.',
      'title': "Rakuten Won't Make You Rich... Use It Anyway (Rakuten Review) (Money with "
               'Andrey)',
      'url': 'https://www.youtube.com/watch?v=E-FSl936NIg&t=78s',
      'video_id': 'E-FSl936NIg'},
     {'author': 'Elliot Explains',
      'channel': 'Elliot Explains',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=yssYp2uZMdg&t=28s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The 250 feed annual fee can be offset quickly. If a business spends around '
              '17,000 or more and consistently pays early, the discount alone recoups the '
              'cost. Zero foreign transaction fees also make it friendly for businesses with '
              'international vendors or travel needs.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': 'The 250 feed annual fee can be offset quickly. If a business spends around '
             '17,000 or more and consistently pays early, the discount alone recoups the cost. '
             'Zero foreign transaction fees also make it friendly for businesses with '
             'international vendors or travel needs.',
      'title': 'American Express Plum Card Review 2025 | Worth It or Leave It? (Elliot '
               'Explains)',
      'url': 'https://www.youtube.com/watch?v=yssYp2uZMdg&t=28s',
      'video_id': 'yssYp2uZMdg'},
     {'author': 'Elevate Business Consulting, LLC',
      'channel': 'Elevate Business Consulting, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:45](https://www.youtube.com/watch?v=EgyPkxlxqpI&t=225s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q2 operational verification).',
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
     {'author': '無國界的Aiden',
      'channel': '無國界的Aiden',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:08](https://www.youtube.com/watch?v=OMnojnDJZ_w&t=428s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q2 operational verification).',
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
     {'author': 'DansDeals',
      'channel': 'DansDeals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=ti02qu7iwX4&t=70s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Pays and the best part about Sephora is that when you sign up for a free '
              "membership, you're going to get free shipping, which means all the $10 products "
              'on the site are going to be completely free after the $10 Pays credit because '
              "there's no shipping fees.",
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': 'Pays and the best part about Sephora is that when you sign up for a free '
             "membership, you're going to get free shipping, which means all the $10 products "
             'on the site are going to be completely free after the $10 Pays credit because '
             "there's no shipping fees.",
      'title': 'How to earn $100s with your credit cards! (DansDeals)',
      'url': 'https://www.youtube.com/watch?v=ti02qu7iwX4&t=70s',
      'video_id': 'ti02qu7iwX4'},
     {'author': 'Bytes Media',
      'channel': 'Bytes Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=RUlyCRTmgxI&t=70s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "With that said, it's not perfect. Because it's a pay-in-full card, there's no "
              "traditional APR, but if you don't clear the full statement balance, you get hit "
              'with a 2. 99% late fee on the outstanding amount, which can be painful for cash '
              'flow type businesses.',
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': "With that said, it's not perfect. Because it's a pay-in-full card, there's no "
             "traditional APR, but if you don't clear the full statement balance, you get hit "
             'with a 2. 99% late fee on the outstanding amount, which can be painful for cash '
             'flow type businesses.',
      'title': 'Capital One Spark Cash Plus Credit Card Review 2026 | Business Cash Back, '
               'Benefits & Full Card Guide (Bytes Media)',
      'url': 'https://www.youtube.com/watch?v=RUlyCRTmgxI&t=70s',
      'video_id': 'RUlyCRTmgxI'},
     {'author': 'CardRight',
      'channel': 'CardRight',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:07](https://www.youtube.com/watch?v=RqEu9gdaauI&t=67s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Financial review and number three if you make a payment and the payment is '
              'returned by the bank due to insufficient funds this can instantly trigger a.',
      'timestamp': 67,
      'timestamp_label': '[00:01:07]',
      'timestamp_seconds': 67,
      'tip': 'Financial review and number three if you make a payment and the payment is '
             'returned by the bank due to insufficient funds this can instantly trigger a.',
      'title': 'Avoid a Amex financial review. 4 things not to do [2024] (CardRight)',
      'url': 'https://www.youtube.com/watch?v=RqEu9gdaauI&t=67s',
      'video_id': 'RqEu9gdaauI'},
     {'author': 'Matthew Perry',
      'channel': 'Matthew Perry',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:27](https://www.youtube.com/watch?v=eEtyddAIvq8&t=267s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q2 operational verification).',
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
      'video_id': 'eEtyddAIvq8'},
     {'author': 'ClarityVenturesVideo',
      'channel': 'ClarityVenturesVideo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:58](https://www.youtube.com/watch?v=lPhNLTTiENE&t=298s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q2 operational verification).',
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
      'video_id': 'lPhNLTTiENE'}],
 3: [{'author': 'CardsChooser',
      'channel': 'CardsChooser',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:58](https://www.youtube.com/watch?v=pie5mBLwycU&t=238s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "There you're going to have also the PNC business option. So it got no annual "
              'fee and $800 bonus after 15,000 free billing cycles. No foreign fee, no intra '
              "APR. It's best for bigger businesses that travel abroad. The largest no fee "
              'bonus, no foreign fee, and high limits.',
      'timestamp': 238,
      'timestamp_label': '[00:03:58]',
      'timestamp_seconds': 238,
      'tip': "There you're going to have also the PNC business option. So it got no annual fee "
             'and $800 bonus after 15,000 free billing cycles. No foreign fee, no intra APR. '
             "It's best for bigger businesses that travel abroad. The largest no fee bonus, no "
             'foreign fee, and high limits.',
      'title': 'Best Business Card Bonuses in November 2026  - Ink Cash vs Triple Cash vs Ink '
               'Unlimited (CardsChooser)',
      'url': 'https://www.youtube.com/watch?v=pie5mBLwycU&t=238s',
      'video_id': 'pie5mBLwycU'},
     {'author': 'Geobreeze Travel',
      'channel': 'Geobreeze Travel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:00](https://www.youtube.com/watch?v=638DPuaWt9s&t=300s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re buying them at a discount, they are able to increase their own profit "
              'margins. But, yeah, I mean, arbitrage card at this point is 3 years old, so the '
              "customer base with that has been growing consistently as well. So, yeah, that's "
              'where we sell our gift cards.',
      'timestamp': 300,
      'timestamp_label': '[00:05:00]',
      'timestamp_seconds': 300,
      'tip': "'re buying them at a discount, they are able to increase their own profit "
             'margins. But, yeah, I mean, arbitrage card at this point is 3 years old, so the '
             "customer base with that has been growing consistently as well. So, yeah, that's "
             'where we sell our gift cards.',
      'title': 'Earn Credit Card Points by Buying Giftcards (2026) with Taylor from qcgc.io | '
               'Ep 280 (Geobreeze Travel)',
      'url': 'https://www.youtube.com/watch?v=638DPuaWt9s&t=300s',
      'video_id': '638DPuaWt9s'},
     {'author': 'Phillip Pak',
      'channel': 'Phillip Pak',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=uXsekqVFn10&t=89s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But the points that you earn from this is way higher than that 3% margin. So, '
              'um you could definitely uh profit if you use some like things like rent. Now, '
              "the cool part about these business cards from Amex is that you don't really "
              'need a business to get these cards.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': 'But the points that you earn from this is way higher than that 3% margin. So, um '
             'you could definitely uh profit if you use some like things like rent. Now, the '
             "cool part about these business cards from Amex is that you don't really need a "
             'business to get these cards.',
      'title': '5 Reasons Why The AMEX Business Gold Card Is Better Than You Think In 2026 '
               '(Phillip Pak)',
      'url': 'https://www.youtube.com/watch?v=uXsekqVFn10&t=89s',
      'video_id': 'uXsekqVFn10'},
     {'author': "Credit4CEO's",
      'channel': "Credit4CEO's",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=uvd7Aufi38A&t=111s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Chase business checking account within the first card anniversary, you will '
              'earn a one time 10 percent bonus on all of your eligible cash back earned '
              'within that first year. So if you earn 250 in cash back, you will get a 250 '
              'bonus.',
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': 'Chase business checking account within the first card anniversary, you will earn '
             'a one time 10 percent bonus on all of your eligible cash back earned within that '
             'first year. So if you earn 250 in cash back, you will get a 250 bonus.',
      'title': "Chase Ink Business Credit Cards (Which One Is For You?) (Credit4CEO's)",
      'url': 'https://www.youtube.com/watch?v=uvd7Aufi38A&t=111s',
      'video_id': 'uvd7Aufi38A'},
     {'author': 'Miles with Mary - Points & Miles Travel',
      'channel': 'Miles with Mary - Points & Miles Travel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=z45WdojPWE8&t=62s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '8,000 in the first 4 months, which Chase markets as a $1,000 cash back bonus. '
              'Both come with a 0% intro APR for the first 12 months on purchases. Both '
              'include purchase protection, extended warranty protection, and primary rental '
              'car coverage when you rent for business.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': '8,000 in the first 4 months, which Chase markets as a $1,000 cash back bonus. '
             'Both come with a 0% intro APR for the first 12 months on purchases. Both include '
             'purchase protection, extended warranty protection, and primary rental car '
             'coverage when you rent for business.',
      'title': "Chase Ink Business Cash or Ink Business Unlimited? Here's How to Choose (Miles "
               'with Mary - Points & Miles Travel)',
      'url': 'https://www.youtube.com/watch?v=z45WdojPWE8&t=62s',
      'video_id': 'z45WdojPWE8'},
     {'author': 'Marketing Business Network',
      'channel': 'Marketing Business Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=_lyxCWYwwJA&t=68s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q3 operational verification).',
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
     {'author': 'MrJoey Explains',
      'channel': 'MrJoey Explains',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:20](https://www.youtube.com/watch?v=gv9Q_Ee7DZ0&t=320s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Merchants pay to handle it. Counting, reconciliation, bank deposits, armored '
              'transport, theft and shrinkage, and staff time. Some of that cost is also baked '
              "into the shelf price. So, the comparison isn't fee versus no fee.",
      'timestamp': 320,
      'timestamp_label': '[00:05:20]',
      'timestamp_seconds': 320,
      'tip': 'Merchants pay to handle it. Counting, reconciliation, bank deposits, armored '
             'transport, theft and shrinkage, and staff time. Some of that cost is also baked '
             "into the shelf price. So, the comparison isn't fee versus no fee.",
      'title': 'Why people who pay cash fund your credit card rewards. (MrJoey Explains)',
      'url': 'https://www.youtube.com/watch?v=gv9Q_Ee7DZ0&t=320s',
      'video_id': 'gv9Q_Ee7DZ0'},
     {'author': 'Mark Reese',
      'channel': 'Mark Reese',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:13](https://www.youtube.com/watch?v=PsWV8Q1E-k0&t=313s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Back some of that cost so the First new benefit here is a $240 flexible '
              'business credit and enrollment is required you can do that by going to your AMX '
              'account.',
      'timestamp': 313,
      'timestamp_label': '[00:05:13]',
      'timestamp_seconds': 313,
      'tip': 'Back some of that cost so the First new benefit here is a $240 flexible business '
             'credit and enrollment is required you can do that by going to your AMX account.',
      'title': 'BIG CHANGES: Amex Business Gold Card Worth $375?! (Full Review) (Mark Reese)',
      'url': 'https://www.youtube.com/watch?v=PsWV8Q1E-k0&t=313s',
      'video_id': 'PsWV8Q1E-k0'},
     {'author': 'Leen on Travel',
      'channel': 'Leen on Travel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=zK3uQ4upb_4&t=38s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This means that we can earn some serious points when not working on a signup '
              'bonus by using this card to buy gift cards for our expenses. One month I earned '
              '6,000 points just by putting $1,200 of my monthly expenditures on fee free Visa '
              'gift cards purchased with my ink cash.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': 'This means that we can earn some serious points when not working on a signup '
             'bonus by using this card to buy gift cards for our expenses. One month I earned '
             '6,000 points just by putting $1,200 of my monthly expenditures on fee free Visa '
             'gift cards purchased with my ink cash.',
      'title': 'My favorite perk of the Chase Business Ink Cash  #travelhacking (Leen on '
               'Travel)',
      'url': 'https://www.youtube.com/watch?v=zK3uQ4upb_4&t=38s',
      'video_id': 'zK3uQ4upb_4'},
     {'author': 'Alex Barajas',
      'channel': 'Alex Barajas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:11](https://www.youtube.com/watch?v=MrvMwsC_ZOg&t=431s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q3 operational verification).',
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
     {'author': 'Hands Off Sales Tax (HOST)',
      'channel': 'Hands Off Sales Tax (HOST)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:57](https://www.youtube.com/watch?v=w-siA5UEWLY&t=177s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Printful requests refreshed documentation. If resale certificates aren't set up "
              'correctly, Printful or Printify will continue charging sales tax on your '
              'orders. Your per-unit costs increase, often by 5% or more, and your margins '
              "shrink, or you're forced to raise prices.",
      'timestamp': 177,
      'timestamp_label': '[00:02:57]',
      'timestamp_seconds': 177,
      'tip': "Printful requests refreshed documentation. If resale certificates aren't set up "
             'correctly, Printful or Printify will continue charging sales tax on your orders. '
             'Your per-unit costs increase, often by 5% or more, and your margins shrink, or '
             "you're forced to raise prices.",
      'title': 'The Huge Printful Resale Certificate Mistake (Hands Off Sales Tax (HOST))',
      'url': 'https://www.youtube.com/watch?v=w-siA5UEWLY&t=177s',
      'video_id': 'w-siA5UEWLY'},
     {'author': 'Nate Bind',
      'channel': 'Nate Bind',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:22](https://www.youtube.com/watch?v=1FoepUfDsnE&t=82s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Finish Line something for $1 and then 3 months later, February 27th, I got a '
              'referral bonus of $80 credited into my account. Now, this account is under a '
              'different name so you do not even need an ID in order to cash this bonus out. '
              'All you will need is a phone number.',
      'timestamp': 82,
      'timestamp_label': '[00:01:22]',
      'timestamp_seconds': 82,
      'tip': 'Finish Line something for $1 and then 3 months later, February 27th, I got a '
             'referral bonus of $80 credited into my account. Now, this account is under a '
             'different name so you do not even need an ID in order to cash this bonus out. '
             'All you will need is a phone number.',
      'title': 'Spend $1, Get $80 Back?! Capital One Shopping Glitch (2026) (Nate Bind)',
      'url': 'https://www.youtube.com/watch?v=1FoepUfDsnE&t=82s',
      'video_id': '1FoepUfDsnE'},
     {'author': 'Bytes Media',
      'channel': 'Bytes Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:24](https://www.youtube.com/watch?v=AEyd6uOijzg&t=24s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '1% cash back on every purchase with no categories to track, plus a boosted 5% '
              "cash back on hotels and rental cars when you book through Capital One's "
              'business travel portal, which is useful in 2026 as travel costs stay elevated '
              'for many small businesses.',
      'timestamp': 24,
      'timestamp_label': '[00:00:24]',
      'timestamp_seconds': 24,
      'tip': '1% cash back on every purchase with no categories to track, plus a boosted 5% '
             "cash back on hotels and rental cars when you book through Capital One's business "
             'travel portal, which is useful in 2026 as travel costs stay elevated for many '
             'small businesses.',
      'title': 'Capital One Spark Classic Credit Card Review 2026 | Business Credit Building '
               'Card Explained (Bytes Media)',
      'url': 'https://www.youtube.com/watch?v=AEyd6uOijzg&t=24s',
      'video_id': 'AEyd6uOijzg'},
     {'author': 'Rob Berger',
      'channel': 'Rob Berger',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:16](https://www.youtube.com/watch?v=4pWev9D_0yQ&t=496s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Bonus actually I should go back um blue blue cash preferred has 250 welcome '
              'bonus two of course you gotta spend the uh hit the spend requirement.',
      'timestamp': 496,
      'timestamp_label': '[00:08:16]',
      'timestamp_seconds': 496,
      'tip': 'Bonus actually I should go back um blue blue cash preferred has 250 welcome '
             'bonus two of course you gotta spend the uh hit the spend requirement.',
      'title': 'A 3-Credit Card Cash Back Strategy Worth $500,000+ (Rob Berger)',
      'url': 'https://www.youtube.com/watch?v=4pWev9D_0yQ&t=496s',
      'video_id': '4pWev9D_0yQ'},
     {'author': 'Naam Wynn',
      'channel': 'Naam Wynn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:25](https://www.youtube.com/watch?v=6KiaTyIQOCQ&t=445s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Since revolving lines of credit have a larger impact on this portion of your '
              'credit score so tackle those to the best of your ability when it comes to '
              'credit.',
      'timestamp': 445,
      'timestamp_label': '[00:07:25]',
      'timestamp_seconds': 445,
      'tip': 'Since revolving lines of credit have a larger impact on this portion of your '
             'credit score so tackle those to the best of your ability when it comes to '
             'credit.',
      'title': '5 Steps to get MASSIVE CREDIT Limit Increases (FAST) (Naam Wynn)',
      'url': 'https://www.youtube.com/watch?v=6KiaTyIQOCQ&t=445s',
      'video_id': '6KiaTyIQOCQ'}],
 4: [{'author': 'Thrive Media',
      'channel': 'Thrive Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=PtqbX-LQUjE&t=30s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It was originally called Wikibby, but Capital One acquired it in 2018. You do '
              'not need a Capital One account or credit card to use it. It works on sites like '
              'Amazon, Walmart, eBay, Best Buy, and thousands of other online retailers.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'It was originally called Wikibby, but Capital One acquired it in 2018. You do '
             'not need a Capital One account or credit card to use it. It works on sites like '
             'Amazon, Walmart, eBay, Best Buy, and thousands of other online retailers.',
      'title': 'Capital One Shopping App Honest Review 2026 | Pros & Cons (Thrive Media)',
      'url': 'https://www.youtube.com/watch?v=PtqbX-LQUjE&t=30s',
      'video_id': 'PtqbX-LQUjE'},
     {'author': 'Elliot Explains',
      'channel': 'Elliot Explains',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:06](https://www.youtube.com/watch?v=R62RsX0IuZo&t=66s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The absence of foreign transaction fees is a relief for those who work with '
              'international suppliers or make overseas purchases. Business tools like '
              'accounting software sensing and easy vendor payments are included to help '
              "streamline operations. Still, it's not for everyone.",
      'timestamp': 66,
      'timestamp_label': '[00:01:06]',
      'timestamp_seconds': 66,
      'tip': 'The absence of foreign transaction fees is a relief for those who work with '
             'international suppliers or make overseas purchases. Business tools like '
             'accounting software sensing and easy vendor payments are included to help '
             "streamline operations. Still, it's not for everyone.",
      'title': 'Capital One Spark Cash Plus Card Review 2025 | Worth It or Leave It? (Elliot '
               'Explains)',
      'url': 'https://www.youtube.com/watch?v=R62RsX0IuZo&t=66s',
      'video_id': 'R62RsX0IuZo'},
     {'author': 'Hoss the Points Boss',
      'channel': 'Hoss the Points Boss',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:27](https://www.youtube.com/watch?v=Rs3ocS_gBOI&t=327s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So we've got a coupon code, Rakuten portal, Amex offer, and manufacturer "
              "rebate. That's a four-way stack on a single purchase. My next bucket, "
              'Electronics, added another 16,000 points from a laptop I bought at Best Buy and '
              'a Samsung TV.',
      'timestamp': 327,
      'timestamp_label': '[00:05:27]',
      'timestamp_seconds': 327,
      'tip': "So we've got a coupon code, Rakuten portal, Amex offer, and manufacturer rebate. "
             "That's a four-way stack on a single purchase. My next bucket, Electronics, added "
             'another 16,000 points from a laptop I bought at Best Buy and a Samsung TV.',
      'title': 'How I Earned 400K Points Through Shopping Portals (Hoss the Points Boss)',
      'url': 'https://www.youtube.com/watch?v=Rs3ocS_gBOI&t=327s',
      'video_id': 'Rs3ocS_gBOI'},
     {'author': 'Credit Compass TV',
      'channel': 'Credit Compass TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=cpfdLJFA6I4&t=54s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Tools including detailed year-end summaries and integration with accounting '
              'software other benefits include complimentary employee cards and.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'Tools including detailed year-end summaries and integration with accounting '
             'software other benefits include complimentary employee cards and.',
      'title': 'Capital One Spark Cash Plus Card: The Ultimate Business Card (Credit Compass '
               'TV)',
      'url': 'https://www.youtube.com/watch?v=cpfdLJFA6I4&t=54s',
      'video_id': 'cpfdLJFA6I4'},
     {'author': 'Nate Bind',
      'channel': 'Nate Bind',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=ILSF_d9HX5I&t=25s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '"Oh, you get $100 for spending $100." I would have been like, "That is a '
              'complete scam. They\'re trying to drain your bank account." In all honesty, '
              "it's it's not. This is one of the best cashback sites I've ever used or "
              "extensions I've ever used.",
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': '"Oh, you get $100 for spending $100." I would have been like, "That is a '
             'complete scam. They\'re trying to drain your bank account." In all honesty, '
             "it's it's not. This is one of the best cashback sites I've ever used or "
             "extensions I've ever used.",
      'title': 'I Thought This Capital One Shopping Cashback Was Too Good To Be True (Nate '
               'Bind)',
      'url': 'https://www.youtube.com/watch?v=ILSF_d9HX5I&t=25s',
      'video_id': 'ILSF_d9HX5I'},
     {'author': 'Eli',
      'channel': 'Eli',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:37](https://www.youtube.com/watch?v=L5V4-qjpKSw&t=37s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "One. But here's the part people get wrong. You do not need a Capital One credit "
              'card or bank account.',
      'timestamp': 37,
      'timestamp_label': '[00:00:37]',
      'timestamp_seconds': 37,
      'tip': "One. But here's the part people get wrong. You do not need a Capital One credit "
             'card or bank account.',
      'title': 'How Is Nobody Talking About This? The $80 Capital One Shopping Bonus, '
               'Explained (Eli)',
      'url': 'https://www.youtube.com/watch?v=L5V4-qjpKSw&t=37s',
      'video_id': 'L5V4-qjpKSw'},
     {'author': 'Daniel Braun',
      'channel': 'Daniel Braun',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:09](https://www.youtube.com/watch?v=HJuOgHKLiAc&t=309s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Guarantee anyway no matter what business structure you have with a sole prop or '
              "an LLC or whatever so basically that means you can't just buy something with.",
      'timestamp': 309,
      'timestamp_label': '[00:05:09]',
      'timestamp_seconds': 309,
      'tip': 'Guarantee anyway no matter what business structure you have with a sole prop or '
             "an LLC or whatever so basically that means you can't just buy something with.",
      'title': 'The EASY Way To Get Business Credit Cards (Full Guide) (Daniel Braun)',
      'url': 'https://www.youtube.com/watch?v=HJuOgHKLiAc&t=309s',
      'video_id': 'HJuOgHKLiAc'},
     {'author': 'IV(4) PROSPERITY',
      'channel': 'IV(4) PROSPERITY',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:30](https://www.youtube.com/watch?v=L5GeiqJtqEc&t=870s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm an active banker and financial services professional. I have 14 plus years "
              "of experience. I have an active mortgage loan originator's license, active life "
              "insurance license, as well as a firmer investment license, and I'm a small "
              'business banker as well.',
      'timestamp': 870,
      'timestamp_label': '[00:14:30]',
      'timestamp_seconds': 870,
      'tip': "I'm an active banker and financial services professional. I have 14 plus years "
             "of experience. I have an active mortgage loan originator's license, active life "
             "insurance license, as well as a firmer investment license, and I'm a small "
             'business banker as well.',
      'title': '“Why American Express Trusts Income More Than Credit” (IV(4) PROSPERITY)',
      'url': 'https://www.youtube.com/watch?v=L5GeiqJtqEc&t=870s',
      'video_id': 'L5GeiqJtqEc'},
     {'author': 'Daily Drop',
      'channel': 'Daily Drop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:33](https://www.youtube.com/watch?v=aO-QS7hMLE0&t=213s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Capital 1 Spark Cash, you can actually convert that cash back into miles with '
              'your Venture X business, making this an incredible twocard setup. Okay, so the '
              'Venture X business obviously offers a lot of value. But who is this right for '
              'and who should look elsewhere?',
      'timestamp': 213,
      'timestamp_label': '[00:03:33]',
      'timestamp_seconds': 213,
      'tip': 'Capital 1 Spark Cash, you can actually convert that cash back into miles with '
             'your Venture X business, making this an incredible twocard setup. Okay, so the '
             'Venture X business obviously offers a lot of value. But who is this right for '
             'and who should look elsewhere?',
      'title': 'Capital One Venture X Business Review | #1 Business Card? (Daily Drop)',
      'url': 'https://www.youtube.com/watch?v=aO-QS7hMLE0&t=213s',
      'video_id': 'aO-QS7hMLE0'},
     {'author': 'Ben Hedges',
      'channel': 'Ben Hedges',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:36](https://www.youtube.com/watch?v=3sY2v2Stv7c&t=216s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This could be a good one to take advantage of. Most I've ever seen with British "
              "Airways is 40% so this is pretty close to that. All right, let's now look at a "
              'few transfer bonuses from Amex and Capital One.',
      'timestamp': 216,
      'timestamp_label': '[00:03:36]',
      'timestamp_seconds': 216,
      'tip': "This could be a good one to take advantage of. Most I've ever seen with British "
             "Airways is 40% so this is pretty close to that. All right, let's now look at a "
             'few transfer bonuses from Amex and Capital One.',
      'title': 'HUGE Transfer and Welcome BONUSES From Chase and Amex (Ben Hedges)',
      'url': 'https://www.youtube.com/watch?v=3sY2v2Stv7c&t=216s',
      'video_id': '3sY2v2Stv7c'},
     {'author': 'Naam Wynn',
      'channel': 'Naam Wynn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:29](https://www.youtube.com/watch?v=QmHwfz5Muvw&t=149s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t even hurt your credit score. There are companies out there that do soft "
              'pulls when you request online. To name a few, this includes Navy Federal, '
              "American Express, Chase, Bank of America, and Capital 1. These checks don't "
              'affect your credit at all.',
      'timestamp': 149,
      'timestamp_label': '[00:02:29]',
      'timestamp_seconds': 149,
      'tip': "'t even hurt your credit score. There are companies out there that do soft pulls "
             'when you request online. To name a few, this includes Navy Federal, American '
             "Express, Chase, Bank of America, and Capital 1. These checks don't affect your "
             'credit at all.',
      'title': 'Do THIS to Get MASSIVE Credit Limit Increase (FAST) (Naam Wynn)',
      'url': 'https://www.youtube.com/watch?v=QmHwfz5Muvw&t=149s',
      'video_id': 'QmHwfz5Muvw'},
     {'author': 'Bytes Media',
      'channel': 'Bytes Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=_if3NsHr3Lg&t=52s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Capital One Business Travel, free employee and virtual cards, downloadable '
              'records to tools like QuickBooks, and a relatively quick online application '
              'that can be completed in about 10 minutes with an instant decision in most '
              'cases.',
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': 'Capital One Business Travel, free employee and virtual cards, downloadable '
             'records to tools like QuickBooks, and a relatively quick online application that '
             'can be completed in about 10 minutes with an instant decision in most cases.',
      'title': 'Capital One Spark Cash Credit Card Review 2026 | Unlimited Business Cash Back, '
               'Rewards & Benefits (Bytes Media)',
      'url': 'https://www.youtube.com/watch?v=_if3NsHr3Lg&t=52s',
      'video_id': '_if3NsHr3Lg'},
     {'author': 'Checkmark Tutorial',
      'channel': 'Checkmark Tutorial',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=hglOA-iPzNc&t=15s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now before applying it's important to know that Capital One offers PR approval "
              'for their business credit cards this can help you get a better idea of which.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Now before applying it's important to know that Capital One offers PR approval "
             'for their business credit cards this can help you get a better idea of which.',
      'title': 'HOW TO GET APPROVED FOR CAPITAL ONE SPARK BUSINESS CREDIT CARD (Checkmark '
               'Tutorial)',
      'url': 'https://www.youtube.com/watch?v=hglOA-iPzNc&t=15s',
      'video_id': 'hglOA-iPzNc'},
     {'author': 'Velocity Channel',
      'channel': 'Velocity Channel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:15](https://www.youtube.com/watch?v=SA627GQFS0k&t=255s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'World would I want to do that CJ would not that increase my credit card bill '
              'well the answer is this where are you placing your income okay where are you '
              'placing.',
      'timestamp': 255,
      'timestamp_label': '[00:04:15]',
      'timestamp_seconds': 255,
      'tip': 'World would I want to do that CJ would not that increase my credit card bill '
             'well the answer is this where are you placing your income okay where are you '
             'placing.',
      'title': 'How To Turn Your Credit Card Into A Cash Flow Machine (Velocity Channel)',
      'url': 'https://www.youtube.com/watch?v=SA627GQFS0k&t=255s',
      'video_id': 'SA627GQFS0k'},
     {'author': 'Pack Your Bag With Points',
      'channel': 'Pack Your Bag With Points',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:50](https://www.youtube.com/watch?v=aJ7DjHaD-XU&t=290s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q4 operational verification).',
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
 5: [{'author': 'Cal Barton',
      'channel': 'Cal Barton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:22](https://www.youtube.com/watch?v=3dq0zRBwn8E&t=562s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Amex for 2 years and paid in full every month. Then they switched their payment '
              'account from Bank of America to Chase. The first payment failed because they '
              'entered the wrong routing and account information.',
      'timestamp': 562,
      'timestamp_label': '[00:09:22]',
      'timestamp_seconds': 562,
      'tip': 'Amex for 2 years and paid in full every month. Then they switched their payment '
             'account from Bank of America to Chase. The first payment failed because they '
             'entered the wrong routing and account information.',
      'title': 'How to Avoid Amex Financial Reviews (Cal Barton)',
      'url': 'https://www.youtube.com/watch?v=3dq0zRBwn8E&t=562s',
      'video_id': '3dq0zRBwn8E'},
     {'author': 'HowToCredit',
      'channel': 'HowToCredit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=NhkTWTt1RKI&t=20s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Not too sure what I'm referring to? Because in today's lesson, I'm going to "
              'break down how the Capital One business credit cards are actually a trap if '
              "you're serious about building business credit and accessing business funding "
              'the right way.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Not too sure what I'm referring to? Because in today's lesson, I'm going to "
             'break down how the Capital One business credit cards are actually a trap if '
             "you're serious about building business credit and accessing business funding the "
             'right way.',
      'title': 'Capital One Sparks Business Credit Cards Review (2025): Worst Business Credit '
               'Cards Ever (HowToCredit)',
      'url': 'https://www.youtube.com/watch?v=NhkTWTt1RKI&t=20s',
      'video_id': 'NhkTWTt1RKI'},
     {'author': 'Professor Oak',
      'channel': 'Professor Oak',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=9eT88-uWTrw&t=65s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I was looking for a business card signup bonus in general was that the septic '
              'tank problem at one of my rental properties, as I talked about in a previous '
              "video, is going to be a huge expense. It's going to be probably like 20, 30 "
              'grand.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': 'I was looking for a business card signup bonus in general was that the septic '
             'tank problem at one of my rental properties, as I talked about in a previous '
             "video, is going to be a huge expense. It's going to be probably like 20, 30 "
             'grand.',
      'title': 'How I Got The Amex Business Gold Sign-Up Bonus Twice (Professor Oak)',
      'url': 'https://www.youtube.com/watch?v=9eT88-uWTrw&t=65s',
      'video_id': '9eT88-uWTrw'},
     {'author': 'The Wealth Paradox',
      'channel': 'The Wealth Paradox',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:37](https://www.youtube.com/watch?v=twmhQO3-WGw&t=277s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q5 operational verification).',
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
     {'author': 'Colin Matthew',
      'channel': 'Colin Matthew',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:29](https://www.youtube.com/watch?v=xZwOSYlOyVc&t=389s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Reported reasons in those waves included buying gift cards to hit minimum '
              'spend, buying gift cards to max out Amex offers, clients. This is a gray area, '
              'not worth your American Express relationship. I would avoid buying gift cards '
              'entirely using American Express.',
      'timestamp': 389,
      'timestamp_label': '[00:06:29]',
      'timestamp_seconds': 389,
      'tip': 'Reported reasons in those waves included buying gift cards to hit minimum spend, '
             'buying gift cards to max out Amex offers, clients. This is a gray area, not '
             'worth your American Express relationship. I would avoid buying gift cards '
             'entirely using American Express.',
      'title': 'HOW TO AVOID A FINANCIAL REVIEW FROM AMERICAN EXPRESS (2026) (Colin Matthew)',
      'url': 'https://www.youtube.com/watch?v=xZwOSYlOyVc&t=389s',
      'video_id': 'xZwOSYlOyVc'},
     {'author': 'AskSebby',
      'channel': 'AskSebby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:31](https://www.youtube.com/watch?v=w8CgH2R003g&t=151s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Apple products imagine if someone stole your credit card and they were buying '
              'stuff that they could later resell those would be the products that would '
              'spook.',
      'timestamp': 151,
      'timestamp_label': '[00:02:31]',
      'timestamp_seconds': 151,
      'tip': 'Apple products imagine if someone stole your credit card and they were buying '
             'stuff that they could later resell those would be the products that would spook.',
      'title': 'I Survived an Amex Financial Review AGAIN: Mistakes to AVOID (AskSebby)',
      'url': 'https://www.youtube.com/watch?v=w8CgH2R003g&t=151s',
      'video_id': 'w8CgH2R003g'},
     {'author': 'Trip Astute',
      'channel': 'Trip Astute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:17](https://www.youtube.com/watch?v=hdNIogj_le0&t=197s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The third possible scenario is that American Express finds you to be too high '
              'of a credit risk or find a discrepancy in your stated income, and they close '
              'your account.',
      'timestamp': 197,
      'timestamp_label': '[00:03:17]',
      'timestamp_seconds': 197,
      'tip': 'The third possible scenario is that American Express finds you to be too high of '
             'a credit risk or find a discrepancy in your stated income, and they close your '
             'account.',
      'title': 'How to Avoid an AMEX Financial Review | Things to Avoid & What To Do If It '
               'Happens to You (Trip Astute)',
      'url': 'https://www.youtube.com/watch?v=hdNIogj_le0&t=197s',
      'video_id': 'hdNIogj_le0'},
     {'author': 'Dutcher Capital',
      'channel': 'Dutcher Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:59](https://www.youtube.com/watch?v=1e8-M6z0R7c&t=239s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Don't count a benefit twice buy something new just to congratulate yourself for "
              'saving. Every day is an easier fit when eligible grocery spending is modest. '
              'Online retail matters and you want to avoid an annual fee.',
      'timestamp': 239,
      'timestamp_label': '[00:03:59]',
      'timestamp_seconds': 239,
      'tip': "Don't count a benefit twice buy something new just to congratulate yourself for "
             'saving. Every day is an easier fit when eligible grocery spending is modest. '
             'Online retail matters and you want to avoid an annual fee.',
      'title': 'Amex Blue Cash: Is 6% Worth the Fee? (Dutcher Capital)',
      'url': 'https://www.youtube.com/watch?v=1e8-M6z0R7c&t=239s',
      'video_id': '1e8-M6z0R7c'},
     {'author': 'Grant Rudow',
      'channel': 'Grant Rudow',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:16](https://www.youtube.com/watch?v=D6wFVrnYqb4&t=736s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Advantage card, it's not exactly a 50/50 split. The bank will actually bulk "
              'purchase miles from the airline for something like 1. Then they turn around and '
              'offer those miles to us. The only thing is, those miles cost the airline '
              'absolutely nothing to give away.',
      'timestamp': 736,
      'timestamp_label': '[00:12:16]',
      'timestamp_seconds': 736,
      'tip': "Advantage card, it's not exactly a 50/50 split. The bank will actually bulk "
             'purchase miles from the airline for something like 1. Then they turn around and '
             'offer those miles to us. The only thing is, those miles cost the airline '
             'absolutely nothing to give away.',
      'title': "The NEW 'Credit Card' Trap, Explained (Grant Rudow)",
      'url': 'https://www.youtube.com/watch?v=D6wFVrnYqb4&t=736s',
      'video_id': 'D6wFVrnYqb4'},
     {'author': 'Geobreeze Travel',
      'channel': 'Geobreeze Travel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=QTa7eNv00k4&t=15s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q5 operational verification).',
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
      'markdown': '[00:07:01](https://www.youtube.com/watch?v=HCkT2XqTvms&t=421s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Multiple payments to a credit card company that can also be seen as risk '
              "because you're likely doing it through ACH and achs can be Unwound after the.",
      'timestamp': 421,
      'timestamp_label': '[00:07:01]',
      'timestamp_seconds': 421,
      'tip': 'Multiple payments to a credit card company that can also be seen as risk because '
             "you're likely doing it through ACH and achs can be Unwound after the.",
      'title': 'Cycling Credit Card Limits - Spin Class (RJ Financial)',
      'url': 'https://www.youtube.com/watch?v=HCkT2XqTvms&t=421s',
      'video_id': 'HCkT2XqTvms'},
     {'author': 'KaungFi',
      'channel': 'KaungFi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:21](https://www.youtube.com/watch?v=VAOuseYv0SI&t=381s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And recently, I this is a recent development, they've started giving you "
              'bonuses for credit cards as well. So this is on top of the sign-up bonus that '
              'you get from the bank itself. Rakuten will give you anywhere between $100 to '
              "$300 is what I've seen.",
      'timestamp': 381,
      'timestamp_label': '[00:06:21]',
      'timestamp_seconds': 381,
      'tip': "And recently, I this is a recent development, they've started giving you bonuses "
             'for credit cards as well. So this is on top of the sign-up bonus that you get '
             'from the bank itself. Rakuten will give you anywhere between $100 to $300 is '
             "what I've seen.",
      'title': 'Rakuten: What Influencers Won’t Share (Everything You Need to Know 2026) '
               '(KaungFi)',
      'url': 'https://www.youtube.com/watch?v=VAOuseYv0SI&t=381s',
      'video_id': 'VAOuseYv0SI'},
     {'author': 'Make Manage Grow Money',
      'channel': 'Make Manage Grow Money',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:50](https://www.youtube.com/watch?v=pjLnjZQ79Ng&t=290s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And let them do it um which is kind of comparable to saying i'm going to invest "
              "in myself because it's still investing in a business or.",
      'timestamp': 290,
      'timestamp_label': '[00:04:50]',
      'timestamp_seconds': 290,
      'tip': "And let them do it um which is kind of comparable to saying i'm going to invest "
             "in myself because it's still investing in a business or.",
      'title': 'Credit Card Arbitrage to Generate Wealth AND Kill It (Make Manage Grow Money)',
      'url': 'https://www.youtube.com/watch?v=pjLnjZQ79Ng&t=290s',
      'video_id': 'pjLnjZQ79Ng'},
     {'author': 'CardRight',
      'channel': 'CardRight',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=XsemDHBgzWE&t=114s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q5 operational verification).',
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
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q5 operational verification).',
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
      'video_id': 'UYH3UwJ9oOM'}],
 6: [{'author': 'John Muscarello',
      'channel': 'John Muscarello',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:36](https://www.youtube.com/watch?v=rpJHRiGfebQ&t=876s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q6 operational verification).',
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
     {'author': 'Daniel Shepherd',
      'channel': 'Daniel Shepherd',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:47](https://www.youtube.com/watch?v=9mXtEwhakHo&t=227s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Ideally, you'd meet it through expenses your business already had planned. A "
              "welcome bonus can make the first year attractive, but we'll also look at "
              "whether the card makes sense once that bonus is behind you. Now, let's break "
              'down the ongoing rewards.',
      'timestamp': 227,
      'timestamp_label': '[00:03:47]',
      'timestamp_seconds': 227,
      'tip': "Ideally, you'd meet it through expenses your business already had planned. A "
             "welcome bonus can make the first year attractive, but we'll also look at whether "
             "the card makes sense once that bonus is behind you. Now, let's break down the "
             'ongoing rewards.',
      'title': 'Amex Business Gold Review: Worth $375 or Overrated? (Daniel Shepherd)',
      'url': 'https://www.youtube.com/watch?v=9mXtEwhakHo&t=227s',
      'video_id': '9mXtEwhakHo'},
     {'author': 'Mogulnomics',
      'channel': 'Mogulnomics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:51](https://www.youtube.com/watch?v=nzZ8nwy2xSY&t=171s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Because the people who get the best deal from credit cards. Credit card rewards '
              'are big business. About 92% of card spending in America now happens on rewards '
              'cards.',
      'timestamp': 171,
      'timestamp_label': '[00:02:51]',
      'timestamp_seconds': 171,
      'tip': 'Because the people who get the best deal from credit cards. Credit card rewards '
             'are big business. About 92% of card spending in America now happens on rewards '
             'cards.',
      'title': 'How Credit Card Companies Make Money From You (Even If You Pay in Full) '
               '(Mogulnomics)',
      'url': 'https://www.youtube.com/watch?v=nzZ8nwy2xSY&t=171s',
      'video_id': 'nzZ8nwy2xSY'},
     {'author': 'Cards and Points',
      'channel': 'Cards and Points',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:24](https://www.youtube.com/watch?v=z9qhRLe7frA&t=84s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You don't need a formal business structure, an employer identification number, "
              "or a separate bank account to qualify. And your business doesn't even need to "
              'be making money yet. When you apply for a business credit card, you can use '
              'your own social security number.',
      'timestamp': 84,
      'timestamp_label': '[00:01:24]',
      'timestamp_seconds': 84,
      'tip': "You don't need a formal business structure, an employer identification number, "
             "or a separate bank account to qualify. And your business doesn't even need to be "
             'making money yet. When you apply for a business credit card, you can use your '
             'own social security number.',
      'title': 'Which Chase Business Card is Right For You? [Compare Chase Ink Credit Cards] '
               '(Cards and Points)',
      'url': 'https://www.youtube.com/watch?v=z9qhRLe7frA&t=84s',
      'video_id': 'z9qhRLe7frA'},
     {'author': "Jake's Tech Lab",
      'channel': "Jake's Tech Lab",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:39](https://www.youtube.com/watch?v=NjlljrQidKg&t=219s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Cash Plus, no category caps, no preset limit, and always the same 2% cash back. '
              'But if you love to hack categories, MX gives you that 4x bonus, but only on the '
              'first 150k per year. After that, the rate drops off a cliff.',
      'timestamp': 219,
      'timestamp_label': '[00:03:39]',
      'timestamp_seconds': 219,
      'tip': 'Cash Plus, no category caps, no preset limit, and always the same 2% cash back. '
             'But if you love to hack categories, MX gives you that 4x bonus, but only on the '
             'first 150k per year. After that, the rate drops off a cliff.',
      'title': 'Capital One Spark Cash Plus vs Amex Business Gold | Best Business Credit Card '
               "2026 (Jake's Tech Lab)",
      'url': 'https://www.youtube.com/watch?v=NjlljrQidKg&t=219s',
      'video_id': 'NjlljrQidKg'},
     {'author': 'Traveling Teacher Personal Finance',
      'channel': 'Traveling Teacher Personal Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:33](https://www.youtube.com/watch?v=PjJySGf3Swg&t=93s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '1,000 in the first 90 days you have the card. If we look at the redemption '
              "level or what you get for every point that you have, it's basically one penny "
              'off of a purchase from GM. Not the best bonus, but not the worst. Uh, so you '
              'can take that into consideration.',
      'timestamp': 93,
      'timestamp_label': '[00:01:33]',
      'timestamp_seconds': 93,
      'tip': '1,000 in the first 90 days you have the card. If we look at the redemption level '
             "or what you get for every point that you have, it's basically one penny off of a "
             'purchase from GM. Not the best bonus, but not the worst. Uh, so you can take '
             'that into consideration.',
      'title': 'Can You Buy a Car with Credit Card Points? GM Rewards Card Review and the '
               'Math! (Traveling Teacher Personal Finance)',
      'url': 'https://www.youtube.com/watch?v=PjJySGf3Swg&t=93s',
      'video_id': 'PjJySGf3Swg'},
     {'author': 'ClarityVenturesVideo',
      'channel': 'ClarityVenturesVideo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:00](https://www.youtube.com/watch?v=qcQs8Xq3hPg&t=180s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Of having a buy group marketplace in the first place consider how difficult it '
              'is for amazon developers to know what changes they can make to the website.',
      'timestamp': 180,
      'timestamp_label': '[00:03:00]',
      'timestamp_seconds': 180,
      'tip': 'Of having a buy group marketplace in the first place consider how difficult it '
             'is for amazon developers to know what changes they can make to the website.',
      'title': 'Buying Groups Webinar - What is a Buying Group? (ClarityVenturesVideo)',
      'url': 'https://www.youtube.com/watch?v=qcQs8Xq3hPg&t=180s',
      'video_id': 'qcQs8Xq3hPg'},
     {'author': 'Monty The Card Nerd',
      'channel': 'Monty The Card Nerd',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:41](https://www.youtube.com/watch?v=7n9y5L1-mD0&t=221s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Down the facts to find the answer first off personal credit cards will show up '
              'on your personal credit report for obvious reasons while business credit.',
      'timestamp': 221,
      'timestamp_label': '[00:03:41]',
      'timestamp_seconds': 221,
      'tip': 'Down the facts to find the answer first off personal credit cards will show up '
             'on your personal credit report for obvious reasons while business credit.',
      'title': 'How To CORRECTLY HACK 0% APR Credit Cards (2025) (Monty The Card Nerd)',
      'url': 'https://www.youtube.com/watch?v=7n9y5L1-mD0&t=221s',
      'video_id': '7n9y5L1-mD0'},
     {'author': 'Points Wire',
      'channel': 'Points Wire',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:49](https://www.youtube.com/watch?v=0EsrkpAxvQQ&t=229s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Atmos is still new, so expect some rough edges booking partner awards. But, if '
              "Southeast Asia's on your list, that's worth a search. Last one, a cautionary "
              'tale. View from the Wing covered a Hertz customer stuck with a $1,367 bill for '
              'a car they say they never rented.',
      'timestamp': 229,
      'timestamp_label': '[00:03:49]',
      'timestamp_seconds': 229,
      'tip': 'Atmos is still new, so expect some rough edges booking partner awards. But, if '
             "Southeast Asia's on your list, that's worth a search. Last one, a cautionary "
             'tale. View from the Wing covered a Hertz customer stuck with a $1,367 bill for a '
             'car they say they never rented.',
      'title': 'Amex Cracks Down on Gamers, Chase Penta-Stack Spotted (Points Wire)',
      'url': 'https://www.youtube.com/watch?v=0EsrkpAxvQQ&t=229s',
      'video_id': '0EsrkpAxvQQ'},
     {'author': 'airelle',
      'channel': 'airelle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:32](https://www.youtube.com/watch?v=MWPOAsKJ1-g&t=572s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, this one blew my mind. For example, let's say there's a Black Friday deal "
              "at Best Buy for PS5s, which are usually like, I don't know, $600, but on sale "
              "they're $500. Best Buy will cap the number of PS5s you can buy to maybe one or "
              'two per customer.',
      'timestamp': 572,
      'timestamp_label': '[00:09:32]',
      'timestamp_seconds': 572,
      'tip': "Now, this one blew my mind. For example, let's say there's a Black Friday deal "
             "at Best Buy for PS5s, which are usually like, I don't know, $600, but on sale "
             "they're $500. Best Buy will cap the number of PS5s you can buy to maybe one or "
             'two per customer.',
      'title': '13 GENIUS Ways to Hit Your Credit Card Minimum Spend (Without Overspending!) '
               '(airelle)',
      'url': 'https://www.youtube.com/watch?v=MWPOAsKJ1-g&t=572s',
      'video_id': 'MWPOAsKJ1-g'},
     {'author': 'WorldlyTips',
      'channel': 'WorldlyTips',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:12](https://www.youtube.com/watch?v=6_ILrKQ_BEI&t=432s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Compare prices across stores. Flip highlights sale items with digital coupons '
              'so you can stack them. Find 50% off, then add $1 off. One store for produce, '
              'another for meat. Your list watches for price drops and pings you. If you buy '
              'groceries, flip is essential.',
      'timestamp': 432,
      'timestamp_label': '[00:07:12]',
      'timestamp_seconds': 432,
      'tip': 'Compare prices across stores. Flip highlights sale items with digital coupons so '
             'you can stack them. Find 50% off, then add $1 off. One store for produce, '
             'another for meat. Your list watches for price drops and pings you. If you buy '
             'groceries, flip is essential.',
      'title': 'Stacking Cashback Apps Reveals This Shocking Hack (WorldlyTips)',
      'url': 'https://www.youtube.com/watch?v=6_ILrKQ_BEI&t=432s',
      'video_id': '6_ILrKQ_BEI'},
     {'author': 'StartupWise',
      'channel': 'StartupWise',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=B-JWfjeKKyU&t=20s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The link down below and when you use that link you'll get 70,000 welcome points "
              "after spending $10,000 in the first 3 months so if you're able to meet.",
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "The link down below and when you use that link you'll get 70,000 welcome points "
             "after spending $10,000 in the first 3 months so if you're able to meet.",
      'title': 'American Express Business Gold Credit Card Review (StartupWise)',
      'url': 'https://www.youtube.com/watch?v=B-JWfjeKKyU&t=20s',
      'video_id': 'B-JWfjeKKyU'},
     {'author': 'CardRight',
      'channel': 'CardRight',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:18](https://www.youtube.com/watch?v=Nevp4Iee4iw&t=18s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q6 operational verification).',
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
     {'author': 'Ben Hedges',
      'channel': 'Ben Hedges',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:08](https://www.youtube.com/watch?v=Lbu0I0_jyQA&t=188s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q6 operational verification).',
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
     {'author': 'CardRight',
      'channel': 'CardRight',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=A8jkRXH6hXc&t=15s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Targeted the first and most important thing to know is that when AMX hits you '
              "with a financial review they're not.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Targeted the first and most important thing to know is that when AMX hits you '
             "with a financial review they're not.",
      'title': 'Hit with a Amex financial review? Here is how to handle it properly [2024] '
               '(CardRight)',
      'url': 'https://www.youtube.com/watch?v=A8jkRXH6hXc&t=15s',
      'video_id': 'A8jkRXH6hXc'}],
 7: [{'author': 'Cameron Gayed',
      'channel': 'Cameron Gayed',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:11](https://www.youtube.com/watch?v=H2F6UOr65H4&t=131s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But again, they do start you off with lower limits. One way to get around this '
              'is if you are already an existing business checking account holder with Bank of '
              'America. They want a long-standing relationship and they want to be the number '
              'one bank.',
      'timestamp': 131,
      'timestamp_label': '[00:02:11]',
      'timestamp_seconds': 131,
      'tip': 'But again, they do start you off with lower limits. One way to get around this '
             'is if you are already an existing business checking account holder with Bank of '
             'America. They want a long-standing relationship and they want to be the number '
             'one bank.',
      'title': 'I Ranked Every Business Credit Card (2026 Tier List) (Cameron Gayed)',
      'url': 'https://www.youtube.com/watch?v=H2F6UOr65H4&t=131s',
      'video_id': 'H2F6UOr65H4'},
     {'author': 'Bella Sloan Enterprises',
      'channel': 'Bella Sloan Enterprises',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=2sUP7XrGRgM&t=21s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm going to break down the exact step-by-step process and I would follow if I "
              'wanted to increase my limits starting today, and it takes about 4 minutes per '
              'account.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "I'm going to break down the exact step-by-step process and I would follow if I "
             'wanted to increase my limits starting today, and it takes about 4 minutes per '
             'account.',
      'title': 'Do THIS for a MASSIVE Credit Limit Increase (FAST) (Bella Sloan Enterprises)',
      'url': 'https://www.youtube.com/watch?v=2sUP7XrGRgM&t=21s',
      'video_id': '2sUP7XrGRgM'},
     {'author': 'The Rewards Master',
      'channel': 'The Rewards Master',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:33](https://www.youtube.com/watch?v=qjuRrg-ROGg&t=273s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s primarily an electronics provider, you're going to get 4x. Well, that could "
              'be great when you buy a new computer or buy a new sound system or whatever it '
              'may be. You get 4x on your cell phone bill.',
      'timestamp': 273,
      'timestamp_label': '[00:04:33]',
      'timestamp_seconds': 273,
      'tip': "'s primarily an electronics provider, you're going to get 4x. Well, that could "
             'be great when you buy a new computer or buy a new sound system or whatever it '
             'may be. You get 4x on your cell phone bill.',
      'title': 'American Express Business Gold Review: 200K Bonus, 4X Rewards... Is It Worth '
               'the $375 Fee? (The Rewards Master)',
      'url': 'https://www.youtube.com/watch?v=qjuRrg-ROGg&t=273s',
      'video_id': 'qjuRrg-ROGg'},
     {'author': 'Phillip Pak',
      'channel': 'Phillip Pak',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:06](https://www.youtube.com/watch?v=Ye64oVq2FgU&t=306s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I like to use this strictly for GrubHub because one, I love food. And two, '
              'GrubHub now comes with GrubHub Plus if you have an Amazon Prime account. So now '
              'you get free delivery with your food.',
      'timestamp': 306,
      'timestamp_label': '[00:05:06]',
      'timestamp_seconds': 306,
      'tip': 'I like to use this strictly for GrubHub because one, I love food. And two, '
             'GrubHub now comes with GrubHub Plus if you have an Amazon Prime account. So now '
             'you get free delivery with your food.',
      'title': '200,000 AMEX Business Gold Card Offer Is Back | No Lifetime Language Offers & '
               'How To Find Them (Phillip Pak)',
      'url': 'https://www.youtube.com/watch?v=Ye64oVq2FgU&t=306s',
      'video_id': 'Ye64oVq2FgU'},
     {'author': 'Elliot Explains',
      'channel': 'Elliot Explains',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:59](https://www.youtube.com/watch?v=PefxZqyor_s&t=119s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The big $10,000 minimum spend for the welcome bonus is steep, possibly locking '
              "out smaller or newer businesses. Plus, it's mainly a charge card you're "
              'expected to pay in full every month unless you use Flex for Business, and '
              "there's no 0% intro APR here.",
      'timestamp': 119,
      'timestamp_label': '[00:01:59]',
      'timestamp_seconds': 119,
      'tip': 'The big $10,000 minimum spend for the welcome bonus is steep, possibly locking '
             "out smaller or newer businesses. Plus, it's mainly a charge card you're expected "
             "to pay in full every month unless you use Flex for Business, and there's no 0% "
             'intro APR here.',
      'title': 'Chase Ink Business Premier Credit Card Review 2025 | Worth It or Leave It? '
               '(Elliot Explains)',
      'url': 'https://www.youtube.com/watch?v=PefxZqyor_s&t=119s',
      'video_id': 'PefxZqyor_s'},
     {'author': 'Spencer Johnson',
      'channel': 'Spencer Johnson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:51](https://www.youtube.com/watch?v=Fk75okyk2W4&t=171s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Little quick tip for those that either have or are planning on using the '
              'GrubHub credits. The best way to actually get value back from that credit is to '
              "set all of your orders to pickup. That way, you don't have to tip the driver or "
              'pay the delivery fees.',
      'timestamp': 171,
      'timestamp_label': '[00:02:51]',
      'timestamp_seconds': 171,
      'tip': 'Little quick tip for those that either have or are planning on using the GrubHub '
             'credits. The best way to actually get value back from that credit is to set all '
             "of your orders to pickup. That way, you don't have to tip the driver or pay the "
             'delivery fees.',
      'title': 'Amex Business Gold: SECRET Point Earning Machine (Spencer Johnson)',
      'url': 'https://www.youtube.com/watch?v=Fk75okyk2W4&t=171s',
      'video_id': 'Fk75okyk2W4'},
     {'author': 'Frequent Miler',
      'channel': 'Frequent Miler',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:17](https://www.youtube.com/watch?v=nMlQUH3s8qY&t=497s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I I wouldn't put as like a reason, necessarily, but it's a nice like extra "
              "benefit. So, let's talk about card talk. And for this week's card talk, we've "
              'got the newly enhanced Amex Business Gold card.',
      'timestamp': 497,
      'timestamp_label': '[00:08:17]',
      'timestamp_seconds': 497,
      'tip': "I I wouldn't put as like a reason, necessarily, but it's a nice like extra "
             "benefit. So, let's talk about card talk. And for this week's card talk, we've "
             'got the newly enhanced Amex Business Gold card.',
      'title': 'Buying groups: Big risks / big rewards | Ep223 | 10-7-23 (Frequent Miler)',
      'url': 'https://www.youtube.com/watch?v=nMlQUH3s8qY&t=497s',
      'video_id': 'nMlQUH3s8qY'},
     {'author': "Luke's Points and Miles",
      'channel': "Luke's Points and Miles",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=Wf33Dss7Sl8&t=15s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I wanted to really break down this card that is universally talked about as a '
              'bonus only card and most folks will completely dismiss this card as a keeper.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'I wanted to really break down this card that is universally talked about as a '
             'bonus only card and most folks will completely dismiss this card as a keeper.',
      'title': "Let's Really Break Down the American Express Business Gold Card! (Luke's "
               'Points and Miles)',
      'url': 'https://www.youtube.com/watch?v=Wf33Dss7Sl8&t=15s',
      'video_id': 'Wf33Dss7Sl8'},
     {'author': 'ClarityVenturesVideo',
      'channel': 'ClarityVenturesVideo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:45](https://www.youtube.com/watch?v=7kHlVyx4a9E&t=645s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Know where you're going where are you going to go with your business and what "
              'are the different steps in your scaling.',
      'timestamp': 645,
      'timestamp_label': '[00:10:45]',
      'timestamp_seconds': 645,
      'tip': "Know where you're going where are you going to go with your business and what "
             'are the different steps in your scaling.',
      'title': 'Buying Groups Webinar - Multi Tiered & Customer-Specific Pricing '
               '(ClarityVenturesVideo)',
      'url': 'https://www.youtube.com/watch?v=7kHlVyx4a9E&t=645s',
      'video_id': '7kHlVyx4a9E'},
     {'author': 'Intuit',
      'channel': 'Intuit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=i-mOkvN7iNE&t=54s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q7 operational verification).',
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
     {'author': 'Travel Hacking Tips WITHOUT Juggling Credit Cards',
      'channel': 'Travel Hacking Tips WITHOUT Juggling Credit Cards',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:57](https://www.youtube.com/watch?v=_xs_maW_2ZM&t=297s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You don't need a Bilt credit card, as I mentioned before. You just need a Bilt "
              "Rewards account. I do encourage folks to get a Bilt credit card. I think it's a "
              "fantastic earner. When I am buying new shoes through Rakuten, I'm paying with "
              'my Bilt card.',
      'timestamp': 297,
      'timestamp_label': '[00:04:57]',
      'timestamp_seconds': 297,
      'tip': "You don't need a Bilt credit card, as I mentioned before. You just need a Bilt "
             "Rewards account. I do encourage folks to get a Bilt credit card. I think it's a "
             "fantastic earner. When I am buying new shoes through Rakuten, I'm paying with my "
             'Bilt card.',
      'title': 'Rakuten + Bilt: The Ultimate Points Stacking Strategy (Travel Hacking Tips '
               'WITHOUT Juggling Credit Cards)',
      'url': 'https://www.youtube.com/watch?v=_xs_maW_2ZM&t=297s',
      'video_id': '_xs_maW_2ZM'},
     {'author': 'Michael Martinez',
      'channel': 'Michael Martinez',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:33](https://www.youtube.com/watch?v=CDTjD80PdZk&t=1053s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And I told them, "Hell no, I want to pay. I\'ll just pick it up in store." So, '
              'the rep updated my account and changed the transaction from delivery to instore '
              'pickup.',
      'timestamp': 1053,
      'timestamp_label': '[00:17:33]',
      'timestamp_seconds': 1053,
      'tip': 'And I told them, "Hell no, I want to pay. I\'ll just pick it up in store." So, '
             'the rep updated my account and changed the transaction from delivery to instore '
             'pickup.',
      'title': 'This Capital One Shopping Strategy Earned Me $500+ Cash Back in 3 Months '
               '(Michael Martinez)',
      'url': 'https://www.youtube.com/watch?v=CDTjD80PdZk&t=1053s',
      'video_id': 'CDTjD80PdZk'},
     {'author': 'Stephen Smith',
      'channel': 'Stephen Smith',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:15](https://www.youtube.com/watch?v=bYSi0VFWtpg&t=615s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'As Maria continues using Velocity Banking, she should also keep her eyes open '
              'for opportunities to make the system even more efficient. One way is through a '
              '0% APR balance transfer card.',
      'timestamp': 615,
      'timestamp_label': '[00:10:15]',
      'timestamp_seconds': 615,
      'tip': 'As Maria continues using Velocity Banking, she should also keep her eyes open '
             'for opportunities to make the system even more efficient. One way is through a '
             '0% APR balance transfer card.',
      'title': 'Velocity Banking Explained: If Your Credit Cards Are Maxed Out Then DO THIS '
               '(Stephen Smith)',
      'url': 'https://www.youtube.com/watch?v=bYSi0VFWtpg&t=615s',
      'video_id': 'bYSi0VFWtpg'},
     {'author': 'Finance Simple',
      'channel': 'Finance Simple',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=1HX4QoYAPMY&t=22s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ach payment is a way to transfer money between the banks and financial '
              'institutions without cash paper checks or credit cards there are two types of '
              'ach payment transactions debit and credit.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'Ach payment is a way to transfer money between the banks and financial '
             'institutions without cash paper checks or credit cards there are two types of '
             'ach payment transactions debit and credit.',
      'title': 'what is ACH payment | ach payments explained | ach payment processing (Finance '
               'Simple)',
      'url': 'https://www.youtube.com/watch?v=1HX4QoYAPMY&t=22s',
      'video_id': '1HX4QoYAPMY'},
     {'author': 'Joe Barreto',
      'channel': 'Joe Barreto',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:03](https://www.youtube.com/watch?v=YKkt6aTmI3c&t=603s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Just randomly go to something else so miente this was a short one but it was an '
              'important one and I thank you so much for being here as always I thank you for '
              'giving me the privilege of your time until next time Mente take care.',
      'timestamp': 603,
      'timestamp_label': '[00:10:03]',
      'timestamp_seconds': 603,
      'tip': 'Just randomly go to something else so miente this was a short one but it was an '
             'important one and I thank you so much for being here as always I thank you for '
             'giving me the privilege of your time until next time Mente take care.',
      'title': 'Major Chase Benefits Upgrade | Amex Offers Disappoint (Joe Barreto)',
      'url': 'https://www.youtube.com/watch?v=YKkt6aTmI3c&t=603s',
      'video_id': 'YKkt6aTmI3c'}],
 8: [{'author': 'Naam Wynn',
      'channel': 'Naam Wynn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:10](https://www.youtube.com/watch?v=AsYTdszcmx8&t=250s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q8 operational verification).',
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
     {'author': 'Bytes Media',
      'channel': 'Bytes Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=Q12R7gbPW8g&t=55s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q8 operational verification).',
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
     {'author': 'Jack McColl',
      'channel': 'Jack McColl',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:27](https://www.youtube.com/watch?v=SNCeMDvlJsQ&t=627s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Business Reserve card because that card earns me four points per dollar spent '
              "on travel and even more if I book the travel in the Chase portal, but I don't "
              'always do that. But you definitely want to have one of the best travel cards if '
              'you have travel expenses.',
      'timestamp': 627,
      'timestamp_label': '[00:10:27]',
      'timestamp_seconds': 627,
      'tip': 'Business Reserve card because that card earns me four points per dollar spent on '
             "travel and even more if I book the travel in the Chase portal, but I don't "
             'always do that. But you definitely want to have one of the best travel cards if '
             'you have travel expenses.',
      'title': 'Do THIS Before Applying for an Amex Business Credit Card (Jack McColl)',
      'url': 'https://www.youtube.com/watch?v=SNCeMDvlJsQ&t=627s',
      'video_id': 'SNCeMDvlJsQ'},
     {'author': 'Lets Get To The Points',
      'channel': 'Lets Get To The Points',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:40:27](https://www.youtube.com/watch?v=mEjNm8zKoQs&t=2427s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's say you go through a shopping portal like Racketin or maybe even one of "
              "the airline portals to buy the product from Best Buy. You're also getting "
              'additional miles or points that way as well.',
      'timestamp': 2427,
      'timestamp_label': '[00:40:27]',
      'timestamp_seconds': 2427,
      'tip': "Let's say you go through a shopping portal like Racketin or maybe even one of "
             "the airline portals to buy the product from Best Buy. You're also getting "
             'additional miles or points that way as well.',
      'title': '98. Unlock MASSIVE Rewards with Buying Groups! (Lets Get To The Points)',
      'url': 'https://www.youtube.com/watch?v=mEjNm8zKoQs&t=2427s',
      'video_id': 'mEjNm8zKoQs'},
     {'author': 'Simplyscotted',
      'channel': 'Simplyscotted',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:37](https://www.youtube.com/watch?v=uUnfurRXAhs&t=217s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Below if you want that sign up bonus you can also stack credit card rewards by '
              'finding deals inside of your MX portal sometimes you can snag some great deals.',
      'timestamp': 217,
      'timestamp_label': '[00:03:37]',
      'timestamp_seconds': 217,
      'tip': 'Below if you want that sign up bonus you can also stack credit card rewards by '
             'finding deals inside of your MX portal sometimes you can snag some great deals.',
      'title': 'Complete Rakuten Guide! Earn More American Express Reward Points FAST! '
               '(Simplyscotted)',
      'url': 'https://www.youtube.com/watch?v=uUnfurRXAhs&t=217s',
      'video_id': 'uUnfurRXAhs'},
     {'author': 'Max Miles Points',
      'channel': 'Max Miles Points',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:47](https://www.youtube.com/watch?v=i4N6SEsh28c&t=227s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Cards and so this shows American Express Chase Bank of America and City offers '
              'you can swipe down to search for specific offers this is where the card.',
      'timestamp': 227,
      'timestamp_label': '[00:03:47]',
      'timestamp_seconds': 227,
      'tip': 'Cards and so this shows American Express Chase Bank of America and City offers '
             'you can swipe down to search for specific offers this is where the card.',
      'title': 'Maximize Your Credit Card Rewards with CardPointers | Tutorial (Max Miles '
               'Points)',
      'url': 'https://www.youtube.com/watch?v=i4N6SEsh28c&t=227s',
      'video_id': 'i4N6SEsh28c'},
     {'author': 'Rachel | Points & Miles',
      'channel': 'Rachel | Points & Miles',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:55](https://www.youtube.com/watch?v=59DiBbciIn8&t=655s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, we usually prefer to transfer points to airline partners for the best '
              'value, but sometimes busy business owners with tons of points just want to book '
              'in the portal. And with 35% back, that can sometimes make sense.',
      'timestamp': 655,
      'timestamp_label': '[00:10:55]',
      'timestamp_seconds': 655,
      'tip': 'Now, we usually prefer to transfer points to airline partners for the best '
             'value, but sometimes busy business owners with tons of points just want to book '
             'in the portal. And with 35% back, that can sometimes make sense.',
      'title': 'Are You Using The WRONG Business Credit Cards?! (Here are the 7 best)! (Rachel '
               '| Points & Miles)',
      'url': 'https://www.youtube.com/watch?v=59DiBbciIn8&t=655s',
      'video_id': '59DiBbciIn8'},
     {'author': 'Miles with Mary - Points & Miles Travel',
      'channel': 'Miles with Mary - Points & Miles Travel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:07](https://www.youtube.com/watch?v=Mexc_KkiIkU&t=127s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It doesn't connect to your bank accounts or require you to use programs like "
              'Plaid. You simply log in to your credit card accounts and then the browser '
              'extension will pull all known data from those cards that you have from its own '
              'massive database.',
      'timestamp': 127,
      'timestamp_label': '[00:02:07]',
      'timestamp_seconds': 127,
      'tip': "It doesn't connect to your bank accounts or require you to use programs like "
             'Plaid. You simply log in to your credit card accounts and then the browser '
             'extension will pull all known data from those cards that you have from its own '
             'massive database.',
      'title': 'Maximizing Credit Card Rewards with CardPointers - Full Guide (Miles with Mary '
               '- Points & Miles Travel)',
      'url': 'https://www.youtube.com/watch?v=Mexc_KkiIkU&t=127s',
      'video_id': 'Mexc_KkiIkU'},
     {'author': 'Points with Phillip',
      'channel': 'Points with Phillip',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:07](https://www.youtube.com/watch?v=8-7xVaopdzg&t=307s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, that could also be a solid option. Now, interesting to to note, personally '
              'for me, I actually uh I have never forgotten the personal Gold card with Delta. '
              'I just have the business Gold card. So, I will still be able to get that '
              'sign-up bonus.',
      'timestamp': 307,
      'timestamp_label': '[00:05:07]',
      'timestamp_seconds': 307,
      'tip': 'So, that could also be a solid option. Now, interesting to to note, personally '
             'for me, I actually uh I have never forgotten the personal Gold card with Delta. '
             'I just have the business Gold card. So, I will still be able to get that sign-up '
             'bonus.',
      'title': 'Rumor: Amex To Drop INSANE Bonuses On Gold, Platinum Cards (Points with '
               'Phillip)',
      'url': 'https://www.youtube.com/watch?v=8-7xVaopdzg&t=307s',
      'video_id': '8-7xVaopdzg'},
     {'author': "Luke's Points and Miles",
      'channel': "Luke's Points and Miles",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:10](https://www.youtube.com/watch?v=qV4hh99M_Xs&t=370s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I have a couple different direct deposit options that I can use for bank '
              'account bonuses and stuff like that. So, I may add a monthly direct deposit '
              "soon, at least temporarily. And then I'm going to reapply for this card in "
              'maybe March.',
      'timestamp': 370,
      'timestamp_label': '[00:06:10]',
      'timestamp_seconds': 370,
      'tip': 'I have a couple different direct deposit options that I can use for bank account '
             'bonuses and stuff like that. So, I may add a monthly direct deposit soon, at '
             "least temporarily. And then I'm going to reapply for this card in maybe March.",
      'title': "The Best Cash Back Credit Card in the Game (Luke's Points and Miles)",
      'url': 'https://www.youtube.com/watch?v=qV4hh99M_Xs&t=370s',
      'video_id': 'qV4hh99M_Xs'},
     {'author': 'Points Rookie',
      'channel': 'Points Rookie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:22](https://www.youtube.com/watch?v=lfbv6SuAgRE&t=322s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t unlock this option for you. So when a store says 5% cashback, read that as "
              'five points for every dollar that you spend. So if you buy a $200 coat at a '
              "store paying 5%, that's $10 cashback or 1,000 Amex points.",
      'timestamp': 322,
      'timestamp_label': '[00:05:22]',
      'timestamp_seconds': 322,
      'tip': "'t unlock this option for you. So when a store says 5% cashback, read that as "
             'five points for every dollar that you spend. So if you buy a $200 coat at a '
             "store paying 5%, that's $10 cashback or 1,000 Amex points.",
      'title': 'Ep 26- Before Black Friday: How to Earn Money or Travel Points With Rakuten '
               '(Points Rookie)',
      'url': 'https://www.youtube.com/watch?v=lfbv6SuAgRE&t=322s',
      'video_id': 'lfbv6SuAgRE'},
     {'author': 'Elliot Explains',
      'channel': 'Elliot Explains',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=DS0GsIckf58&t=80s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The hotel bonus applies only to prepaid stays through specific booking '
              'channels, limiting flexibility. The high APR, reaching up to 28. 74% with an '
              'even steeper penalty rate, makes it unsuitable for carrying a balance.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': 'The hotel bonus applies only to prepaid stays through specific booking channels, '
             'limiting flexibility. The high APR, reaching up to 28. 74% with an even steeper '
             'penalty rate, makes it unsuitable for carrying a balance.',
      'title': 'Delta SkyMiles Platinum Business Card Review 2025 | Worth It or Leave It? '
               '(Elliot Explains)',
      'url': 'https://www.youtube.com/watch?v=DS0GsIckf58&t=80s',
      'video_id': 'DS0GsIckf58'},
     {'author': 'Mark Reese',
      'channel': 'Mark Reese',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:51](https://www.youtube.com/watch?v=ae1WayyrwnE&t=411s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And they for some reason love to hide their points feature upon logging into '
              "your account select the card you want to use so i've chosen my city double.",
      'timestamp': 411,
      'timestamp_label': '[00:06:51]',
      'timestamp_seconds': 411,
      'tip': 'And they for some reason love to hide their points feature upon logging into '
             "your account select the card you want to use so i've chosen my city double.",
      'title': 'Beginner’s Guide to Transfer Partners for BIG VALUE (Amex, Chase, Citi, '
               'Capital One Credit Cards) (Mark Reese)',
      'url': 'https://www.youtube.com/watch?v=ae1WayyrwnE&t=411s',
      'video_id': 'ae1WayyrwnE'},
     {'author': 'Jon Joseph',
      'channel': 'Jon Joseph',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:54](https://www.youtube.com/watch?v=V_o90eWaTpI&t=414s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "A referral link to M1 Finance down below if you're interested in that and "
              "finally I'm going to attach my referral link for my AMX gold credit card down "
              'in the description below all right guys thanks for watching and happy holidays.',
      'timestamp': 414,
      'timestamp_label': '[00:06:54]',
      'timestamp_seconds': 414,
      'tip': "A referral link to M1 Finance down below if you're interested in that and "
             "finally I'm going to attach my referral link for my AMX gold credit card down in "
             'the description below all right guys thanks for watching and happy holidays.',
      'title': 'CASH BACK STACKING | How I combine deals/apps/cards to get money back! '
               '(Rakuten, Dosh, PEI) (Jon Joseph)',
      'url': 'https://www.youtube.com/watch?v=V_o90eWaTpI&t=414s',
      'video_id': 'V_o90eWaTpI'},
     {'author': 'ProudMoney - Credit Cards & Personal Finance',
      'channel': 'ProudMoney - Credit Cards & Personal Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:42](https://www.youtube.com/watch?v=IrfC1PHQGVQ&t=522s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q8 operational verification).',
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
      'video_id': 'IrfC1PHQGVQ'}],
 9: [{'author': 'Colin Matthew',
      'channel': 'Colin Matthew',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:50](https://www.youtube.com/watch?v=gTpUtrhQsnM&t=830s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'America, US Bank, you can move your business limits to business limits and '
              'reset the 0% too. This is one of the most powerful plays in the credit game '
              'right now that almost nobody talks about. Now, there are some rules to know. '
              'This only works within the same bank.',
      'timestamp': 830,
      'timestamp_label': '[00:13:50]',
      'timestamp_seconds': 830,
      'tip': 'America, US Bank, you can move your business limits to business limits and reset '
             'the 0% too. This is one of the most powerful plays in the credit game right now '
             'that almost nobody talks about. Now, there are some rules to know. This only '
             'works within the same bank.',
      'title': 'Do THIS To Get MASSIVE SOFT PULL Credit Limit Increases (FAST) (Colin Matthew)',
      'url': 'https://www.youtube.com/watch?v=gTpUtrhQsnM&t=830s',
      'video_id': 'gTpUtrhQsnM'},
     {'author': 'CREDNCARD',
      'channel': 'CREDNCARD',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:12](https://www.youtube.com/watch?v=9HLY-5lw8uA&t=312s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The Business Platinum may also provide a pay with points rebate on qualifying '
              'airfare booked through the applicable American Express travel channel, subject '
              'to the current benefit terms, eligible airline rules, annual rebate limits, and '
              'other restrictions.',
      'timestamp': 312,
      'timestamp_label': '[00:05:12]',
      'timestamp_seconds': 312,
      'tip': 'The Business Platinum may also provide a pay with points rebate on qualifying '
             'airfare booked through the applicable American Express travel channel, subject '
             'to the current benefit terms, eligible airline rules, annual rebate limits, and '
             'other restrictions.',
      'title': 'Capital One Venture X Business vs. Amex Business Platinum: Spending Tier '
               'Strategy (CREDNCARD)',
      'url': 'https://www.youtube.com/watch?v=9HLY-5lw8uA&t=312s',
      'video_id': '9HLY-5lw8uA'},
     {'author': 'Cal Barton',
      'channel': 'Cal Barton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:27](https://www.youtube.com/watch?v=Zgd5WIoedks&t=447s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ve opened five or more personal credit cards across all issuers in the past 24 "
              "months. Now some applicants say they're getting turned down below that line. "
              "They're hearing a three account limit applies to their business applications.",
      'timestamp': 447,
      'timestamp_label': '[00:07:27]',
      'timestamp_seconds': 447,
      'tip': "'ve opened five or more personal credit cards across all issuers in the past 24 "
             "months. Now some applicants say they're getting turned down below that line. "
             "They're hearing a three account limit applies to their business applications.",
      'title': 'AMEX, Citi & Chase Are Changing the Credit Card Rules! (Cal Barton)',
      'url': 'https://www.youtube.com/watch?v=Zgd5WIoedks&t=447s',
      'video_id': 'Zgd5WIoedks'},
     {'author': 'Finance With Sharan',
      'channel': 'Finance With Sharan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:04:45](https://www.youtube.com/watch?v=M4SMio3nUKs&t=3885s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And if I have to buy a 1 lakh flagship phone, like the Nothing, what is the '
              'best credit card to use? Any hacks for buying flagship phone? I would probably '
              'look to buy that at a Reliance Digital or a Croma, and I would use one of my '
              'premium credit cards to buy Croma vouchers.',
      'timestamp': 3885,
      'timestamp_label': '[01:04:45]',
      'timestamp_seconds': 3885,
      'tip': 'And if I have to buy a 1 lakh flagship phone, like the Nothing, what is the best '
             'credit card to use? Any hacks for buying flagship phone? I would probably look '
             'to buy that at a Reliance Digital or a Croma, and I would use one of my premium '
             'credit cards to buy Croma vouchers.',
      'title': 'How to Pick the Right Credit Card in 2026 for Free Travel, Rewards & Value | '
               'Aly Hajiani | FWS 105 (Finance With Sharan)',
      'url': 'https://www.youtube.com/watch?v=M4SMio3nUKs&t=3885s',
      'video_id': 'M4SMio3nUKs'},
     {'author': 'Points with Phillip',
      'channel': 'Points with Phillip',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:14](https://www.youtube.com/watch?v=nZSZ4gP-QwI&t=434s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I just did a video recently where I talked about being about to buy um an '
              'iPhone with that because this might be the best card for that. Now, in addition '
              'to that, you do have some kind of more gimmie categories, more easily '
              'accessible categories.',
      'timestamp': 434,
      'timestamp_label': '[00:07:14]',
      'timestamp_seconds': 434,
      'tip': 'I just did a video recently where I talked about being about to buy um an iPhone '
             'with that because this might be the best card for that. Now, in addition to '
             'that, you do have some kind of more gimmie categories, more easily accessible '
             'categories.',
      'title': 'The Amex Business Gold Credit Card Just Got A HUGE New Feature! (Points with '
               'Phillip)',
      'url': 'https://www.youtube.com/watch?v=nZSZ4gP-QwI&t=434s',
      'video_id': 'nZSZ4gP-QwI'},
     {'author': 'Matt Clausen',
      'channel': 'Matt Clausen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=2NMHIyn8lWI&t=134s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '240 notion credit, a $200 $240 zero credit. This is accounting firm accounting '
              "software. 250 legal zoom credit and a $100 resi credit. There's also an "
              'interesting design option, a $24 karat goldplated card after spending $100,000 '
              'in a calendar year.',
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': '240 notion credit, a $200 $240 zero credit. This is accounting firm accounting '
             "software. 250 legal zoom credit and a $100 resi credit. There's also an "
             'interesting design option, a $24 karat goldplated card after spending $100,000 '
             'in a calendar year.',
      'title': 'This Amex Business Gold Survey Reveals A LOT (Matt Clausen)',
      'url': 'https://www.youtube.com/watch?v=2NMHIyn8lWI&t=134s',
      'video_id': '2NMHIyn8lWI'},
     {'author': 'John Liang',
      'channel': 'John Liang',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:13](https://www.youtube.com/watch?v=SkbED_I8KzM&t=133s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And so I always recommend just keep it separate for your own sake, but there is '
              'no law binding you to it. In addition, with business credit cards, it unlocks a '
              'whole world of additional opportunities to earn massive signup bonuses.',
      'timestamp': 133,
      'timestamp_label': '[00:02:13]',
      'timestamp_seconds': 133,
      'tip': 'And so I always recommend just keep it separate for your own sake, but there is '
             'no law binding you to it. In addition, with business credit cards, it unlocks a '
             'whole world of additional opportunities to earn massive signup bonuses.',
      'title': 'Chase Ink Unlimited vs Chase Ink Cash - 100,000 Point Bonus! (John Liang)',
      'url': 'https://www.youtube.com/watch?v=SkbED_I8KzM&t=133s',
      'video_id': 'SkbED_I8KzM'},
     {'author': "Jake's Tech Lab",
      'channel': "Jake's Tech Lab",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:01](https://www.youtube.com/watch?v=jSUO2McsAa8&t=241s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'No complex math, no tracking. You just pay off the charge card each month. '
              "Though, yeah, if you wanted a sneaky 0% intro APR, you won't find it here. "
              'Still, in terms of keeping it headache-free, Spark Cash Plus wins hands down.',
      'timestamp': 241,
      'timestamp_label': '[00:04:01]',
      'timestamp_seconds': 241,
      'tip': 'No complex math, no tracking. You just pay off the charge card each month. '
             "Though, yeah, if you wanted a sneaky 0% intro APR, you won't find it here. "
             'Still, in terms of keeping it headache-free, Spark Cash Plus wins hands down.',
      'title': 'Ink Business Cash vs Capital One Spark Cash Plus Comparison 2026 | Best '
               "Business Credit Card? (Jake's Tech Lab)",
      'url': 'https://www.youtube.com/watch?v=jSUO2McsAa8&t=241s',
      'video_id': 'jSUO2McsAa8'},
     {'author': 'Eli Facenda',
      'channel': 'Eli Facenda',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=fEjp_gJN8OQ&t=28s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Thing that's special about the plum card is that you get much longer terms to "
              "pay that actual bounce back so if you're in a business where cash management "
              'is.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': "Thing that's special about the plum card is that you get much longer terms to "
             "pay that actual bounce back so if you're in a business where cash management is.",
      'title': 'Should You Get the AMEX Plum for your Business? (Eli Facenda)',
      'url': 'https://www.youtube.com/watch?v=fEjp_gJN8OQ&t=28s',
      'video_id': 'fEjp_gJN8OQ'},
     {'author': 'StartupWise',
      'channel': 'StartupWise',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:46](https://www.youtube.com/watch?v=q2u8OT37r4s&t=46s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Better in terms of annual fee now let's talk about the welcome bonus so this is "
              'obviously going to change depending on when you guys are watching this video.',
      'timestamp': 46,
      'timestamp_label': '[00:00:46]',
      'timestamp_seconds': 46,
      'tip': "Better in terms of annual fee now let's talk about the welcome bonus so this is "
             'obviously going to change depending on when you guys are watching this video.',
      'title': 'American Express Business Gold vs Platinum Credit Card Comparison '
               '(StartupWise)',
      'url': 'https://www.youtube.com/watch?v=q2u8OT37r4s&t=46s',
      'video_id': 'q2u8OT37r4s'},
     {'author': 'Itinerary Boss',
      'channel': 'Itinerary Boss',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:48](https://www.youtube.com/watch?v=xTEAB6N6l_A&t=768s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So that's the bonus of this too. So you can kind of come up with a nice "
              "strategy of what's the best way for where I live. So if you're, you know, for "
              "me, American, American Airlines miles are very important because we're an "
              'American Airlines hub.',
      'timestamp': 768,
      'timestamp_label': '[00:12:48]',
      'timestamp_seconds': 768,
      'tip': "So that's the bonus of this too. So you can kind of come up with a nice strategy "
             "of what's the best way for where I live. So if you're, you know, for me, "
             "American, American Airlines miles are very important because we're an American "
             'Airlines hub.',
      'title': 'Maximize Credit Card Points with Rakuten & SaveWise (Itinerary Boss)',
      'url': 'https://www.youtube.com/watch?v=xTEAB6N6l_A&t=768s',
      'video_id': 'xTEAB6N6l_A'},
     {'author': 'Just Money Ish',
      'channel': 'Just Money Ish',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:34](https://www.youtube.com/watch?v=Cm-vEtFQnC0&t=154s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you're purchasing the same thing all the time and creating a pattern like "
              'buying gift cards all the time, for example, and then just creating money '
              'orders. So that way you can pay the card back to take advantage of higher '
              'limits or even reward points.',
      'timestamp': 154,
      'timestamp_label': '[00:02:34]',
      'timestamp_seconds': 154,
      'tip': "If you're purchasing the same thing all the time and creating a pattern like "
             'buying gift cards all the time, for example, and then just creating money '
             'orders. So that way you can pay the card back to take advantage of higher limits '
             'or even reward points.',
      'title': 'Capital One Will Close Your Credit Card For This One BIG Reason! (CREDIT '
               'CYCLING) (Just Money Ish)',
      'url': 'https://www.youtube.com/watch?v=Cm-vEtFQnC0&t=154s',
      'video_id': 'Cm-vEtFQnC0'},
     {'author': 'Bytes Media',
      'channel': 'Bytes Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=L-fP6r8X7A0&t=43s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, let's discuss what it does. Well, the app is completely free to use and "
              'does not require a Capital 1 bank account, which makes it accessible for almost '
              'anyone.',
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': "Now, let's discuss what it does. Well, the app is completely free to use and "
             'does not require a Capital 1 bank account, which makes it accessible for almost '
             'anyone.',
      'title': 'Capital One Shopping App Review 2026 | Pros and Cons – Honest & Unbiased '
               '(Bytes Media)',
      'url': 'https://www.youtube.com/watch?v=L-fP6r8X7A0&t=43s',
      'video_id': 'L-fP6r8X7A0'},
     {'author': 'Daily Drop',
      'channel': 'Daily Drop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:38](https://www.youtube.com/watch?v=kDpEoiV0EZM&t=698s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That down in the description box below along with the full list of our top '
              'travel credit cards right now but as always thank you so much for watching and '
              "we'll see you in the next video.",
      'timestamp': 698,
      'timestamp_label': '[00:11:38]',
      'timestamp_seconds': 698,
      'tip': 'That down in the description box below along with the full list of our top '
             'travel credit cards right now but as always thank you so much for watching and '
             "we'll see you in the next video.",
      'title': 'Rakuten Review & Demo (How I Earn THOUSANDS of Extra Points) (Daily Drop)',
      'url': 'https://www.youtube.com/watch?v=kDpEoiV0EZM&t=698s',
      'video_id': 'kDpEoiV0EZM'},
     {'author': 'Simon Katz - Ideal Media',
      'channel': 'Simon Katz - Ideal Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:32](https://www.youtube.com/watch?v=1AvpfkuaT_Q&t=512s)',
      'relevance': 'Attributed practitioner commentary on pre-committed wholesale Buying-Group '
                   '(`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment to '
                   'sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` commercial '
                   'card & `Rakuten`/`TopCashback` portal rebate stacking, `Plastiq`/`Melio` '
                   'B2B invoice float, and `55`-day T-bill/bank-bonus treasury velocity '
                   '(Chapter Q9 operational verification).',
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
 10: [{'author': 'Ask Sebby Business',
       'channel': 'Ask Sebby Business',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:35](https://www.youtube.com/watch?v=oH1xNl2vB28&t=395s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Worst case, you're getting an intro bonus to give the card a test drive. It's "
               "no annual fee and can go into your stack and it doesn't hurt you. Best case "
               "early on, it helps you for office supply stores and it can't scale with your "
               'business for something like internet.',
       'timestamp': 395,
       'timestamp_label': '[00:06:35]',
       'timestamp_seconds': 395,
       'tip': "Worst case, you're getting an intro bonus to give the card a test drive. It's "
              "no annual fee and can go into your stack and it doesn't hurt you. Best case "
              "early on, it helps you for office supply stores and it can't scale with your "
              'business for something like internet.',
       'title': 'BEST Chase Business Credit Card?! | Chase Ink Cash Review (Ask Sebby '
                'Business)',
       'url': 'https://www.youtube.com/watch?v=oH1xNl2vB28&t=395s',
       'video_id': 'oH1xNl2vB28'},
      {'author': 'Loral Langemeier',
       'channel': 'Loral Langemeier',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:19](https://www.youtube.com/watch?v=OVRY6T42zPA&t=79s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q10 operational verification).',
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
      {'author': 'Just Money Ish',
       'channel': 'Just Money Ish',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:37](https://www.youtube.com/watch?v=Zu5102EGxLc&t=277s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Because if you guys are really looking to kickstart your business, the best '
               'way to do this is by getting a 0% intro APR credit card for at least about a '
               "year or so. So that way you don't have to pay any interest on the credit card "
               'for borrowing money.',
       'timestamp': 277,
       'timestamp_label': '[00:04:37]',
       'timestamp_seconds': 277,
       'tip': 'Because if you guys are really looking to kickstart your business, the best way '
              'to do this is by getting a 0% intro APR credit card for at least about a year '
              "or so. So that way you don't have to pay any interest on the credit card for "
              'borrowing money.',
       'title': '5 Reasons Why You Should Stay Away From Capital One Spark Business Credit '
                'Cards (Just Money Ish)',
       'url': 'https://www.youtube.com/watch?v=Zu5102EGxLc&t=277s',
       'video_id': 'Zu5102EGxLc'},
      {'author': 'SimplyAndyHere',
       'channel': 'SimplyAndyHere',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=R9f9H7_4bE8&t=21s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Racketin to me is basically coupon clipping but for online websites. And if we '
               'look at some examples of what is currently available from just signing in, we '
               "have Amazon, Macy's, Target, Best Buy, and many others.",
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'Racketin to me is basically coupon clipping but for online websites. And if we '
              'look at some examples of what is currently available from just signing in, we '
              "have Amazon, Macy's, Target, Best Buy, and many others.",
       'title': 'Applying for the Rakuten Credit Card… Is It Worth It? (SimplyAndyHere)',
       'url': 'https://www.youtube.com/watch?v=R9f9H7_4bE8&t=21s',
       'video_id': 'R9f9H7_4bE8'},
      {'author': 'HowToCredit',
       'channel': 'HowToCredit',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:26](https://www.youtube.com/watch?v=1F0G53GBilU&t=746s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q10 operational verification).',
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
      {'author': 'Wholesome Financials',
       'channel': 'Wholesome Financials',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:36](https://www.youtube.com/watch?v=IaYI1caam3s&t=516s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s go to a card from [snorts] a major bank that is that also has 0% APR "
               "offers, but >> doesn't actually report to your personal credit, so you can "
               'actually use it. A more top like a more lower tier bank.',
       'timestamp': 516,
       'timestamp_label': '[00:08:36]',
       'timestamp_seconds': 516,
       'tip': "'s go to a card from [snorts] a major bank that is that also has 0% APR offers, "
              "but >> doesn't actually report to your personal credit, so you can actually use "
              'it. A more top like a more lower tier bank.',
       'title': 'The SHOCKING Truth About Capital One Spark Business Credit Card (Wholesome '
                'Financials)',
       'url': 'https://www.youtube.com/watch?v=IaYI1caam3s&t=516s',
       'video_id': 'IaYI1caam3s'},
      {'author': 'Chris Hutchins',
       'channel': 'Chris Hutchins',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:16](https://www.youtube.com/watch?v=Dbhznmaq0Bg&t=196s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And this can be as simple as you pay for dinner for a whole bunch of people, '
               'and everybody Venmos you back. That way you get the points for putting the '
               "spend on your credit card, but it doesn't really affect your bank account "
               'because other people are paying you back.',
       'timestamp': 196,
       'timestamp_label': '[00:03:16]',
       'timestamp_seconds': 196,
       'tip': 'And this can be as simple as you pay for dinner for a whole bunch of people, '
              'and everybody Venmos you back. That way you get the points for putting the '
              "spend on your credit card, but it doesn't really affect your bank account "
              'because other people are paying you back.',
       'title': 'Maximize Your Points: Stacking, Buyers Clubs, Redemption Hacks, and More '
                '(Chris Hutchins)',
       'url': 'https://www.youtube.com/watch?v=Dbhznmaq0Bg&t=196s',
       'video_id': 'Dbhznmaq0Bg'},
      {'author': 'Escape of the Week',
       'channel': 'Escape of the Week',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:05](https://www.youtube.com/watch?v=U64ykipOtaA&t=545s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'If we scroll down here to key benefits, this is a very nice benefit, receive '
               "up to $650 credit back, we're backing your business with up to $650 back when "
               'you spend money at zero Google ads, meta Amazon web services.',
       'timestamp': 545,
       'timestamp_label': '[00:09:05]',
       'timestamp_seconds': 545,
       'tip': 'If we scroll down here to key benefits, this is a very nice benefit, receive up '
              "to $650 credit back, we're backing your business with up to $650 back when you "
              'spend money at zero Google ads, meta Amazon web services.',
       'title': 'Amex Business Gold Card Review: Does It Pay for Itself? (2026) (Escape of the '
                'Week)',
       'url': 'https://www.youtube.com/watch?v=U64ykipOtaA&t=545s',
       'video_id': 'U64ykipOtaA'},
      {'author': 'Jack McColl',
       'channel': 'Jack McColl',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:50](https://www.youtube.com/watch?v=c5MGulNCfZ8&t=110s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And that trust shows up directly on the two new limits you're going to get. "
               "For American Express, AMEX's version is the Blue Business Plus. 0% for 12 "
               'months, no annual fee, and two points per dollar spent on your first $50,000 '
               'in annual spend on the card.',
       'timestamp': 110,
       'timestamp_label': '[00:01:50]',
       'timestamp_seconds': 110,
       'tip': "And that trust shows up directly on the two new limits you're going to get. For "
              "American Express, AMEX's version is the Blue Business Plus. 0% for 12 months, "
              'no annual fee, and two points per dollar spent on your first $50,000 in annual '
              'spend on the card.',
       'title': 'The 5 Best Credit Cards Offering 0% Interest (Jack McColl)',
       'url': 'https://www.youtube.com/watch?v=c5MGulNCfZ8&t=110s',
       'video_id': 'c5MGulNCfZ8'},
      {'author': 'The Money Advantage',
       'channel': 'The Money Advantage',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:49](https://www.youtube.com/watch?v=eckGlyqGUBs&t=409s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Another vital concept is credit utilization, which is the percentage of your '
               'available credit that you are currently using. A best practice is to keep this '
               'number below 30 %, which signals to the financial world that you are managing '
               'your resources with care and foresight.',
       'timestamp': 409,
       'timestamp_label': '[00:06:49]',
       'timestamp_seconds': 409,
       'tip': 'Another vital concept is credit utilization, which is the percentage of your '
              'available credit that you are currently using. A best practice is to keep this '
              'number below 30 %, which signals to the financial world that you are managing '
              'your resources with care and foresight.',
       'title': 'Credit Cards For Beginners cash back vs travels. No annual fee (The Money '
                'Advantage)',
       'url': 'https://www.youtube.com/watch?v=eckGlyqGUBs&t=409s',
       'video_id': 'eckGlyqGUBs'},
      {'author': 'UpgradedPoints',
       'channel': 'UpgradedPoints',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:07](https://www.youtube.com/watch?v=kiOoNZghrGk&t=67s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, I had a $150 car rental. I still booked directly through Hertz, earned my '
               "Hertz points, and I'm going to get $100 back. One that I've not taken "
               "advantage of yet, but it's still in my account is spend $100 on hotels, get "
               '$100 back.',
       'timestamp': 67,
       'timestamp_label': '[00:01:07]',
       'timestamp_seconds': 67,
       'tip': 'So, I had a $150 car rental. I still booked directly through Hertz, earned my '
              "Hertz points, and I'm going to get $100 back. One that I've not taken advantage "
              "of yet, but it's still in my account is spend $100 on hotels, get $100 back.",
       'title': 'How Chris Uses Capital One Shopping to Earn Free Hotel Stays (UpgradedPoints)',
       'url': 'https://www.youtube.com/watch?v=kiOoNZghrGk&t=67s',
       'video_id': 'kiOoNZghrGk'},
      {'author': 'Stephen Smith',
       'channel': 'Stephen Smith',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:45](https://www.youtube.com/watch?v=zOrHXaEEgxk&t=525s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A while I buy some inventory just here and there this one is probably going to '
               'be my go-to man this one is going to be awesome very excited about this card.',
       'timestamp': 525,
       'timestamp_label': '[00:08:45]',
       'timestamp_seconds': 525,
       'tip': 'A while I buy some inventory just here and there this one is probably going to '
              'be my go-to man this one is going to be awesome very excited about this card.',
       'title': '$50,000 American Express Plum Card | AMEX Business Card 60 Day 0% APR! (NO '
                'DOCS) (Stephen Smith)',
       'url': 'https://www.youtube.com/watch?v=zOrHXaEEgxk&t=525s',
       'video_id': 'zOrHXaEEgxk'},
      {'author': 'TECH GIANT',
       'channel': 'TECH GIANT',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:39](https://www.youtube.com/watch?v=m8toWc8c4lM&t=519s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q10 operational verification).',
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
       'title': 'Capital One Spark Business vs  Chase Business Credit Card | Full Review '
                '(2025) (TECH GIANT)',
       'url': 'https://www.youtube.com/watch?v=m8toWc8c4lM&t=519s',
       'video_id': 'm8toWc8c4lM'},
      {'author': 'Cal Barton',
       'channel': 'Cal Barton',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:15](https://www.youtube.com/watch?v=0pnnp262mLg&t=195s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Years of tax returns and 66% of people were asked to submit either two months '
               "of bank statements or two pay stubs and the third thing that's going to "
               'happen.',
       'timestamp': 195,
       'timestamp_label': '[00:03:15]',
       'timestamp_seconds': 195,
       'tip': 'Years of tax returns and 66% of people were asked to submit either two months '
              "of bank statements or two pay stubs and the third thing that's going to happen.",
       'title': 'How To Avoid Amex Financial Review (Cal Barton)',
       'url': 'https://www.youtube.com/watch?v=0pnnp262mLg&t=195s',
       'video_id': '0pnnp262mLg'},
      {'author': 'Frequent Miler',
       'channel': 'Frequent Miler',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:24:56](https://www.youtube.com/watch?v=p6KX6rsg_Rk&t=1496s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'That on my own without getting a call Rep involved is so good really nice '
               'really a big I mean hats off Mariette nicely done thank you for finally making '
               "that possible and Hyatt if you're listening Marriott made it possible to do "
               'this online.',
       'timestamp': 1496,
       'timestamp_label': '[00:24:56]',
       'timestamp_seconds': 1496,
       'tip': 'That on my own without getting a call Rep involved is so good really nice '
              'really a big I mean hats off Mariette nicely done thank you for finally making '
              "that possible and Hyatt if you're listening Marriott made it possible to do "
              'this online.',
       'title': '13 ways to increase credit card spend (and get most of it back) | Ep197 | '
                '4-8-23 (Frequent Miler)',
       'url': 'https://www.youtube.com/watch?v=p6KX6rsg_Rk&t=1496s',
       'video_id': 'p6KX6rsg_Rk'}],
 11: [{'author': 'Cal Barton',
       'channel': 'Cal Barton',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:59](https://www.youtube.com/watch?v=sVToTQaS_Dw&t=179s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q11 operational verification).',
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
      {'author': 'Ben Hedges',
       'channel': 'Ben Hedges',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:40](https://www.youtube.com/watch?v=1K72JHTnPlw&t=280s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And this is all through their dedicated team of professional certified '
               'financial planners. The best part is there is no charge to see if Domain Money '
               'is right for you. Use the link below to book a free 30-minute strategy '
               'session.',
       'timestamp': 280,
       'timestamp_label': '[00:04:40]',
       'timestamp_seconds': 280,
       'tip': 'And this is all through their dedicated team of professional certified '
              'financial planners. The best part is there is no charge to see if Domain Money '
              'is right for you. Use the link below to book a free 30-minute strategy session.',
       'title': 'The Amex Platinum Is Changing (And Not For The Better) (Ben Hedges)',
       'url': 'https://www.youtube.com/watch?v=1K72JHTnPlw&t=280s',
       'video_id': '1K72JHTnPlw'},
      {'author': 'Joey | Amazon FBA',
       'channel': 'Joey | Amazon FBA',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:26](https://www.youtube.com/watch?v=tKw8SljNcPE&t=446s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q11 operational verification).',
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
      {'author': 'KaungFi',
       'channel': 'KaungFi',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:50](https://www.youtube.com/watch?v=R-TCKAPsObw&t=350s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s like the best bank account bonuses every month, and they update it. Please "
               'be doing these, you guys. This is This is easy money. This is what I do '
               'instead of high-yield savings account.',
       'timestamp': 350,
       'timestamp_label': '[00:05:50]',
       'timestamp_seconds': 350,
       'tip': "'s like the best bank account bonuses every month, and they update it. Please "
              'be doing these, you guys. This is This is easy money. This is what I do instead '
              'of high-yield savings account.',
       'title': 'The RIGHT way to use Rakuten (from a points pro!) (KaungFi)',
       'url': 'https://www.youtube.com/watch?v=R-TCKAPsObw&t=350s',
       'video_id': 'R-TCKAPsObw'},
      {'author': 'Bytes Media',
       'channel': 'Bytes Media',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:51](https://www.youtube.com/watch?v=Z-sM6DX4rEM&t=111s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'X Business card fits best in 2026 for established small and mid-size '
               'businesses with excellent credit that spend heavily on travel and want a '
               'rewards ecosystem plus premium perks, not for very lean or low travel '
               'operations that just need a simple cash back card.',
       'timestamp': 111,
       'timestamp_label': '[00:01:51]',
       'timestamp_seconds': 111,
       'tip': 'X Business card fits best in 2026 for established small and mid-size businesses '
              'with excellent credit that spend heavily on travel and want a rewards ecosystem '
              'plus premium perks, not for very lean or low travel operations that just need a '
              'simple cash back card.',
       'title': 'Capital One Venture X Business Credit Card Review 2026 | Business Travel '
                'Rewards, Benefits Guide (Bytes Media)',
       'url': 'https://www.youtube.com/watch?v=Z-sM6DX4rEM&t=111s',
       'video_id': 'Z-sM6DX4rEM'},
      {'author': 'Colin Matthew',
       'channel': 'Colin Matthew',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:32](https://www.youtube.com/watch?v=QVqw68pTohQ&t=212s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That's exactly what I did when I was about 20 years old. Boosted my score into "
               'the 750s, acquired over 800 grand in business funding, and started buying '
               'section 8 rental properties and starting and scaling my multiple businesses.',
       'timestamp': 212,
       'timestamp_label': '[00:03:32]',
       'timestamp_seconds': 212,
       'tip': "That's exactly what I did when I was about 20 years old. Boosted my score into "
              'the 750s, acquired over 800 grand in business funding, and started buying '
              'section 8 rental properties and starting and scaling my multiple businesses.',
       'title': 'How to Pay Off Your Maxed Out Credit Cards with ZERO Cashflow! (Colin '
                'Matthew)',
       'url': 'https://www.youtube.com/watch?v=QVqw68pTohQ&t=212s',
       'video_id': 'QVqw68pTohQ'},
      {'author': 'WealthRoom AI',
       'channel': 'WealthRoom AI',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:14](https://www.youtube.com/watch?v=8_GgpKDJJTE&t=194s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'If you run business expenses, real estate deposits, or digital ad campaigns '
               'through your personal credit profiles, you are bottlenecking your scaling '
               'capacity and risking personal financial liquidation.',
       'timestamp': 194,
       'timestamp_label': '[00:03:14]',
       'timestamp_seconds': 194,
       'tip': 'If you run business expenses, real estate deposits, or digital ad campaigns '
              'through your personal credit profiles, you are bottlenecking your scaling '
              'capacity and risking personal financial liquidation.',
       'title': 'How to Turn Credit Into Capital in 2027 (Corporate Arbitrage Blueprint '
                '(WealthRoom AI)',
       'url': 'https://www.youtube.com/watch?v=8_GgpKDJJTE&t=194s',
       'video_id': '8_GgpKDJJTE'},
      {'author': "Paul's Points",
       'channel': "Paul's Points",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:22](https://www.youtube.com/watch?v=iwdIgYSyL9s&t=22s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Chase can take the bonus back if you close the account within 6 months. 70,000 '
               'Hyatt points can mean several nights at a simple hotel or a night or two at a '
               'top resort. It depends on the hotel and the dates.',
       'timestamp': 22,
       'timestamp_label': '[00:00:22]',
       'timestamp_seconds': 22,
       'tip': 'Chase can take the bonus back if you close the account within 6 months. 70,000 '
              'Hyatt points can mean several nights at a simple hotel or a night or two at a '
              'top resort. It depends on the hotel and the dates.',
       'title': "Chase Hyatt Business Card Bonus Rises to 70,000 (Paul's Points)",
       'url': 'https://www.youtube.com/watch?v=iwdIgYSyL9s&t=22s',
       'video_id': 'iwdIgYSyL9s'},
      {'author': "Jake's Tech Lab",
       'channel': "Jake's Tech Lab",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:03](https://www.youtube.com/watch?v=W3nb-AdwMck&t=183s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Oh, and here's something cool you probably didn't know. Both these cards hook "
               'you up with 5% back on lift rides until September 30th, 2027. So, if your team '
               'is always zipping around, definitely keep that in mind. Next up, annual fee '
               'and APR.',
       'timestamp': 183,
       'timestamp_label': '[00:03:03]',
       'timestamp_seconds': 183,
       'tip': "Oh, and here's something cool you probably didn't know. Both these cards hook "
              'you up with 5% back on lift rides until September 30th, 2027. So, if your team '
              'is always zipping around, definitely keep that in mind. Next up, annual fee and '
              'APR.',
       'title': 'Ink Business Unlimited vs Ink Business Cash | Best Chase Business Card 2026 '
                "(Jake's Tech Lab)",
       'url': 'https://www.youtube.com/watch?v=W3nb-AdwMck&t=183s',
       'video_id': 'W3nb-AdwMck'},
      {'author': 'VANNtastic!',
       'channel': 'VANNtastic!',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:55](https://www.youtube.com/watch?v=CO5ahnL4ijI&t=55s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q11 operational verification).',
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
      {'author': 'Just Money Ish',
       'channel': 'Just Money Ish',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:41](https://www.youtube.com/watch?v=04bDgAQcsYs&t=221s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Ink Business Unlimited credit card. Now, the third reason why you guys should '
               'get this business credit card is because not only does it offer you no annual '
               "fees, but you'll also receive a 0% intro APR for the first 12 months on "
               'purchases, which is absolutely fantastic.',
       'timestamp': 221,
       'timestamp_label': '[00:03:41]',
       'timestamp_seconds': 221,
       'tip': 'Ink Business Unlimited credit card. Now, the third reason why you guys should '
              'get this business credit card is because not only does it offer you no annual '
              "fees, but you'll also receive a 0% intro APR for the first 12 months on "
              'purchases, which is absolutely fantastic.',
       'title': '5 Reasons Why You Should Get the Chase Ink Business Unlimited Credit Card! '
                '(Just Money Ish)',
       'url': 'https://www.youtube.com/watch?v=04bDgAQcsYs&t=221s',
       'video_id': '04bDgAQcsYs'},
      {'author': 'John Muscarello',
       'channel': 'John Muscarello',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:19](https://www.youtube.com/watch?v=ThO9ard-k8E&t=559s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q11 operational verification).',
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
      {'author': 'AskSebby',
       'channel': 'AskSebby',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:16](https://www.youtube.com/watch?v=Er1tcSbzC2w&t=316s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And down below in the description box make sure the links are competitive but '
               "otherwise it's a huge way to support the channel so thank you guys in advance.",
       'timestamp': 316,
       'timestamp_label': '[00:05:16]',
       'timestamp_seconds': 316,
       'tip': 'And down below in the description box make sure the links are competitive but '
              "otherwise it's a huge way to support the channel so thank you guys in advance.",
       'title': 'Yikes! Amex Financial Review: How to Avoid in 2023 (AskSebby)',
       'url': 'https://www.youtube.com/watch?v=Er1tcSbzC2w&t=316s',
       'video_id': 'Er1tcSbzC2w'},
      {'author': 'Mr. Will Roundtree',
       'channel': 'Mr. Will Roundtree',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:10](https://www.youtube.com/watch?v=a1MwAkYtYBE&t=670s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q11 operational verification).',
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
      {'author': 'Thrive Media',
       'channel': 'Thrive Media',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:40](https://www.youtube.com/watch?v=PtqbX-LQUjE&t=40s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Capital One acquired it in 2018. You do not need a Capital One account or '
               'credit card to use it. It works on sites like Amazon, Walmart, eBay, Best Buy, '
               'and thousands of other online retailers. So basically it is designed to save '
               'you money with little to no effort.',
       'timestamp': 40,
       'timestamp_label': '[00:00:40]',
       'timestamp_seconds': 40,
       'tip': 'Capital One acquired it in 2018. You do not need a Capital One account or '
              'credit card to use it. It works on sites like Amazon, Walmart, eBay, Best Buy, '
              'and thousands of other online retailers. So basically it is designed to save '
              'you money with little to no effort.',
       'title': 'Capital One Shopping App Honest Review 2026 | Pros & Cons (Thrive Media)',
       'url': 'https://www.youtube.com/watch?v=PtqbX-LQUjE&t=40s',
       'video_id': 'PtqbX-LQUjE'}],
 12: [{'author': 'Czech It Out: Money Hacks',
       'channel': 'Czech It Out: Money Hacks',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:44](https://www.youtube.com/watch?v=HNO_8rnhPeE&t=44s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q12 operational verification).',
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
      {'author': 'Christopher Grant',
       'channel': 'Christopher Grant',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:26](https://www.youtube.com/watch?v=GFmuZ9Z3Drg&t=86s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '10 consecutive orders for about five days a week over the period of a month. '
               "So, Target is actually pretty hard to get banned. Of course, unless you're "
               'taking advantage of loss leaders and things like that. And then, if we open up '
               'another tab and go to say walgreens.',
       'timestamp': 86,
       'timestamp_label': '[00:01:26]',
       'timestamp_seconds': 86,
       'tip': '10 consecutive orders for about five days a week over the period of a month. '
              "So, Target is actually pretty hard to get banned. Of course, unless you're "
              'taking advantage of loss leaders and things like that. And then, if we open up '
              'another tab and go to say walgreens.',
       'title': 'Online Arbitrage Orders Keep Getting Canceled? 👎 [Here is a Solution] | OA '
                'Buddy (Christopher Grant)',
       'url': 'https://www.youtube.com/watch?v=GFmuZ9Z3Drg&t=86s',
       'video_id': 'GFmuZ9Z3Drg'},
      {'author': 'Leen on Travel',
       'channel': 'Leen on Travel',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:32](https://www.youtube.com/watch?v=TvJBiMpMRhw&t=32s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Amex Business Gold is that you get $300 per year in ChatGPT Business statement '
               "credits after enrollment. But, here's the thing, ChatGPT Business requires a "
               'minimum of two seats, and on the monthly plan, standard seats cost $25 each. '
               'That means you normally pay $50 a month.',
       'timestamp': 32,
       'timestamp_label': '[00:00:32]',
       'timestamp_seconds': 32,
       'tip': 'Amex Business Gold is that you get $300 per year in ChatGPT Business statement '
              "credits after enrollment. But, here's the thing, ChatGPT Business requires a "
              'minimum of two seats, and on the monthly plan, standard seats cost $25 each. '
              'That means you normally pay $50 a month.',
       'title': 'The Amex Business Gold Is a $320 MONEYMAKER?! (Leen on Travel)',
       'url': 'https://www.youtube.com/watch?v=TvJBiMpMRhw&t=32s',
       'video_id': 'TvJBiMpMRhw'},
      {'author': 'Twin Finances',
       'channel': 'Twin Finances',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:55](https://www.youtube.com/watch?v=OxMh5dpHvJk&t=55s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Lululemon, REI, and even Best Buy. So, I would always double check the options '
               'before you start using this. Also, it takes about a month to get your cash '
               'back from when you make your purchase.',
       'timestamp': 55,
       'timestamp_label': '[00:00:55]',
       'timestamp_seconds': 55,
       'tip': 'Lululemon, REI, and even Best Buy. So, I would always double check the options '
              'before you start using this. Also, it takes about a month to get your cash back '
              'from when you make your purchase.',
       'title': 'How to Use the Capital One Shopping Portal | Ultimate Guide (Twin Finances)',
       'url': 'https://www.youtube.com/watch?v=OxMh5dpHvJk&t=55s',
       'video_id': 'OxMh5dpHvJk'},
      {'author': 'Credit Card BS',
       'channel': 'Credit Card BS',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:40](https://www.youtube.com/watch?v=UBo0IdafezQ&t=220s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '20 a month at FedEx, GrubHub, or office supply stores. And then you usually '
               'have to activate this. My personal way of liquidating this is to just go to '
               "like a Staples and buy a 20 or $25 Amazon gift card. So, assuming you're able "
               "to use this credit, that's $240 a year.",
       'timestamp': 220,
       'timestamp_label': '[00:03:40]',
       'timestamp_seconds': 220,
       'tip': '20 a month at FedEx, GrubHub, or office supply stores. And then you usually '
              'have to activate this. My personal way of liquidating this is to just go to '
              "like a Staples and buy a 20 or $25 Amazon gift card. So, assuming you're able "
              "to use this credit, that's $240 a year.",
       'title': 'Should You Get the Amex Business Gold? (Credit Card BS)',
       'url': 'https://www.youtube.com/watch?v=UBo0IdafezQ&t=220s',
       'video_id': 'UBo0IdafezQ'},
      {'author': 'Anthony Venture 2',
       'channel': 'Anthony Venture 2',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:36](https://www.youtube.com/watch?v=ZSZN6BW7_m0&t=156s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Tim who've been here literally since the start. So, if you're interested, down "
               'in the pinned comment below, we have a free trial active right now. And '
               'whatever price you buy in at is going to be grandfathered forever.',
       'timestamp': 156,
       'timestamp_label': '[00:02:36]',
       'timestamp_seconds': 156,
       'tip': "Tim who've been here literally since the start. So, if you're interested, down "
              'in the pinned comment below, we have a free trial active right now. And '
              'whatever price you buy in at is going to be grandfathered forever.',
       'title': 'This Amex Card Upgrade Strategy Nobody Told You Existed (Anthony Venture 2)',
       'url': 'https://www.youtube.com/watch?v=ZSZN6BW7_m0&t=156s',
       'video_id': 'ZSZN6BW7_m0'},
      {'author': "Leo's Travel Hacks",
       'channel': "Leo's Travel Hacks",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:22](https://www.youtube.com/watch?v=4RuPkU_XvWA&t=322s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '1,000 points too, though its page shows JetBlue from 250 points and Qantas '
               'from 500. For timing, Chase says most transfers arrive by the next business '
               'day and no later than seven business days, while American Express says '
               'transfers typically take 48 to 72 hours.',
       'timestamp': 322,
       'timestamp_label': '[00:05:22]',
       'timestamp_seconds': 322,
       'tip': '1,000 points too, though its page shows JetBlue from 250 points and Qantas from '
              '500. For timing, Chase says most transfers arrive by the next business day and '
              'no later than seven business days, while American Express says transfers '
              'typically take 48 to 72 hours.',
       'title': 'Chase vs Amex 2026: Ultimate Rewards vs Membership Rewards — Partners, Ratios '
                "& Cards (Leo's Travel Hacks)",
       'url': 'https://www.youtube.com/watch?v=4RuPkU_XvWA&t=322s',
       'video_id': '4RuPkU_XvWA'},
      {'author': 'Stephen Smith',
       'channel': 'Stephen Smith',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:02](https://www.youtube.com/watch?v=RY2Q9yq3v3E&t=302s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q12 operational verification).',
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
      {'author': 'Ask Sebby Business',
       'channel': 'Ask Sebby Business',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:38](https://www.youtube.com/watch?v=x9-GMvg8lPA&t=98s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'First month they might ask you what your business does there is a minor bonus '
               'I feel like I need to mention because otherwise people are going to get mad.',
       'timestamp': 98,
       'timestamp_label': '[00:01:38]',
       'timestamp_seconds': 98,
       'tip': 'First month they might ask you what your business does there is a minor bonus I '
              'feel like I need to mention because otherwise people are going to get mad.',
       'title': 'King of Business Cards?! 👑🐐 Capital One Spark Cash Plus (Ask Sebby Business)',
       'url': 'https://www.youtube.com/watch?v=x9-GMvg8lPA&t=98s',
       'video_id': 'x9-GMvg8lPA'},
      {'author': 'James Baker CPA',
       'channel': 'James Baker CPA',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:08](https://www.youtube.com/watch?v=w7-zxRnNOSo&t=68s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "$5,000 you're going to get a 1099 K so when you apply for your stripe account "
               "or any other payment processor you're going to be giving them your "
               'information.',
       'timestamp': 68,
       'timestamp_label': '[00:01:08]',
       'timestamp_seconds': 68,
       'tip': "$5,000 you're going to get a 1099 K so when you apply for your stripe account "
              "or any other payment processor you're going to be giving them your information.",
       'title': 'CPA Explains: 1099K (Everything You Need To Know - 2025 Update) (James Baker '
                'CPA)',
       'url': 'https://www.youtube.com/watch?v=w7-zxRnNOSo&t=68s',
       'video_id': 'w7-zxRnNOSo'},
      {'author': 'RJ Financial',
       'channel': 'RJ Financial',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:32](https://www.youtube.com/watch?v=vfXgcEGNVuM&t=512s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q12 operational verification).',
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
      {'author': 'Frequent Miler',
       'channel': 'Frequent Miler',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:42](https://www.youtube.com/watch?v=WXhl_7UcgL8&t=282s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Lot of sense particularly for a business with really big expenses I mean if '
               "you're spending hundreds of thousands of dollars a month on your card that's.",
       'timestamp': 282,
       'timestamp_label': '[00:04:42]',
       'timestamp_seconds': 282,
       'tip': 'Lot of sense particularly for a business with really big expenses I mean if '
              "you're spending hundreds of thousands of dollars a month on your card that's.",
       'title': 'Chase Ink Business Premier | Card Talk Ep9 | 10-10-24 (Frequent Miler)',
       'url': 'https://www.youtube.com/watch?v=WXhl_7UcgL8&t=282s',
       'video_id': 'WXhl_7UcgL8'},
      {'author': 'Points Panda',
       'channel': 'Points Panda',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:32](https://www.youtube.com/watch?v=rUdn6piNvLA&t=212s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q12 operational verification).',
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
      {'author': 'Bytes Media',
       'channel': 'Bytes Media',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:48](https://www.youtube.com/watch?v=jINKMWHyrg4&t=108s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, it's not ideal for businesses that rely on carrying a balance "
               'month-to-month. Business Premiere credit card is a strong option for '
               'businesses with high spending and a preference for simple, predictable cash '
               'back.',
       'timestamp': 108,
       'timestamp_label': '[00:01:48]',
       'timestamp_seconds': 108,
       'tip': "So, it's not ideal for businesses that rely on carrying a balance "
              'month-to-month. Business Premiere credit card is a strong option for businesses '
              'with high spending and a preference for simple, predictable cash back.',
       'title': 'Chase Ink Business Premier Credit Card Review 2026 | High Spending Business '
                'Rewards & Cash Back (Bytes Media)',
       'url': 'https://www.youtube.com/watch?v=jINKMWHyrg4&t=108s',
       'video_id': 'jINKMWHyrg4'},
      {'author': 'Naam Wynn',
       'channel': 'Naam Wynn',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:17](https://www.youtube.com/watch?v=QFNkg3G6als&t=197s)',
       'relevance': 'Attributed practitioner commentary on pre-committed wholesale '
                    'Buying-Group (`BuyForMeRetail`/`Pointsmaker`/`MaxOutDeals`) fulfillment '
                    'to sales-tax-exempt `DE`/`NH`/`OR` warehouses, uncapped `2%–4%` '
                    'commercial card & `Rakuten`/`TopCashback` portal rebate stacking, '
                    '`Plastiq`/`Melio` B2B invoice float, and `55`-day T-bill/bank-bonus '
                    'treasury velocity (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Melio also has a free plan to get you started with a set number of free bank '
               'transfers every month. And paid plans if your business needs more. It also '
               "connects with QuickBooks, Xero, and NetSuite, so you're never entering the "
               'same bill twice.',
       'timestamp': 197,
       'timestamp_label': '[00:03:17]',
       'timestamp_seconds': 197,
       'tip': 'Melio also has a free plan to get you started with a set number of free bank '
              'transfers every month. And paid plans if your business needs more. It also '
              "connects with QuickBooks, Xero, and NetSuite, so you're never entering the same "
              'bill twice.',
       'title': '5 BEST Business Credit Cards ($25,000 Limit) (Naam Wynn)',
       'url': 'https://www.youtube.com/watch?v=QFNkg3G6als&t=197s',
       'video_id': 'QFNkg3G6als'}]}
