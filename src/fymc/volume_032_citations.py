"""Curated 180-citation ISO Payment Processing & ATM Arbitrage baseline (15 per chapter across Q1-Q12) mined strictly from verified ISO Payment Processing & ATM Arbitrage YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'30k',
     '36x',
     'account',
     'accounts',
     'ach',
     'agency',
     'agent',
     'agreement',
     'alert',
     'amendment',
     'analysis',
     'appointment',
     'arbitrage',
     'armored',
     'atm',
     'atms',
     'auto',
     'b2b',
     'balancing',
     'bank',
     'barbershop',
     'boarding',
     'bonus',
     'book',
     'broker',
     'brokers',
     'building',
     'business',
     'businesses',
     'buy',
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
 2: {'30k',
     '36x',
     'account',
     'accounts',
     'ach',
     'agency',
     'agent',
     'agreement',
     'alert',
     'amendment',
     'analysis',
     'appointment',
     'arbitrage',
     'armored',
     'atm',
     'atms',
     'auto',
     'b2b',
     'balancing',
     'bank',
     'barbershop',
     'boarding',
     'bonus',
     'book',
     'broker',
     'brokers',
     'budget',
     'building',
     'business',
     'businesses',
     'buy',
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
 3: {'30k',
     '36x',
     'account',
     'accounts',
     'ach',
     'agency',
     'agent',
     'agreement',
     'alert',
     'amendment',
     'analysis',
     'appointment',
     'arbitrage',
     'armored',
     'atm',
     'atms',
     'auto',
     'b2b',
     'balancing',
     'bank',
     'barbershop',
     'boarding',
     'bonus',
     'book',
     'broker',
     'brokers',
     'building',
     'business',
     'businesses',
     'buy',
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
 4: {'30k',
     '36x',
     'account',
     'accounts',
     'ach',
     'agency',
     'agent',
     'agreement',
     'alert',
     'amendment',
     'analysis',
     'appointment',
     'arbitrage',
     'armored',
     'atm',
     'atms',
     'auto',
     'b2b',
     'balancing',
     'bank',
     'barbershop',
     'boarding',
     'bonus',
     'book',
     'broker',
     'brokers',
     'budget',
     'building',
     'business',
     'businesses',
     'buy',
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
 5: {'30k',
     '36x',
     'account',
     'accounts',
     'ach',
     'agency',
     'agent',
     'agreement',
     'alert',
     'amendment',
     'analysis',
     'appointment',
     'arbitrage',
     'armored',
     'atm',
     'atms',
     'audit',
     'auto',
     'avoid',
     'b2b',
     'balancing',
     'bank',
     'barbershop',
     'boarding',
     'bonus',
     'book',
     'broker',
     'brokers',
     'building',
     'business',
     'businesses',
     'buy',
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
 6: {'30k',
     '36x',
     'account',
     'accounts',
     'ach',
     'agency',
     'agent',
     'agreement',
     'alert',
     'amendment',
     'analysis',
     'appointment',
     'arbitrage',
     'armored',
     'atm',
     'atms',
     'auto',
     'b2b',
     'balancing',
     'bank',
     'barbershop',
     'boarding',
     'bonus',
     'book',
     'broker',
     'brokers',
     'building',
     'business',
     'businesses',
     'buy',
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
 7: {'30k',
     '36x',
     'account',
     'accounts',
     'ach',
     'agency',
     'agent',
     'agreement',
     'alert',
     'amendment',
     'analysis',
     'appointment',
     'arbitrage',
     'armored',
     'atm',
     'atms',
     'auto',
     'b2b',
     'balancing',
     'bank',
     'barbershop',
     'boarding',
     'bonus',
     'book',
     'broker',
     'brokers',
     'building',
     'business',
     'businesses',
     'buy',
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
 8: {'30k',
     '36x',
     'account',
     'accounts',
     'ach',
     'agency',
     'agent',
     'agreement',
     'alert',
     'amendment',
     'analysis',
     'api',
     'appointment',
     'arbitrage',
     'armored',
     'atm',
     'atms',
     'auto',
     'b2b',
     'balancing',
     'bank',
     'barbershop',
     'boarding',
     'bonus',
     'book',
     'broker',
     'brokers',
     'building',
     'business',
     'businesses',
     'buy',
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
 9: {'30k',
     '36x',
     'account',
     'accounts',
     'ach',
     'agency',
     'agent',
     'agreement',
     'alert',
     'amendment',
     'analysis',
     'appointment',
     'arbitrage',
     'armored',
     'atm',
     'atms',
     'auto',
     'b2b',
     'balancing',
     'bank',
     'barbershop',
     'boarding',
     'bonus',
     'book',
     'broker',
     'brokers',
     'building',
     'business',
     'businesses',
     'buy',
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
 10: {'30k',
      '36x',
      'account',
      'accounts',
      'ach',
      'agency',
      'agent',
      'agreement',
      'ai',
      'alert',
      'amendment',
      'analysis',
      'appointment',
      'arbitrage',
      'armored',
      'atm',
      'atms',
      'auto',
      'automate',
      'automation',
      'b2b',
      'balancing',
      'bank',
      'barbershop',
      'boarding',
      'bonus',
      'book',
      'broker',
      'brokers',
      'building',
      'business',
      'businesses',
      'buy',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'30k',
      '36x',
      'account',
      'accounts',
      'ach',
      'agency',
      'agent',
      'agreement',
      'alert',
      'amendment',
      'analysis',
      'appointment',
      'arbitrage',
      'armored',
      'atm',
      'atms',
      'auto',
      'b2b',
      'balancing',
      'bank',
      'barbershop',
      'boarding',
      'bonus',
      'book',
      'broker',
      'brokers',
      'building',
      'business',
      'businesses',
      'buy',
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
 12: {'30k',
      '36x',
      'account',
      'accounts',
      'ach',
      'action',
      'agency',
      'agent',
      'agreement',
      'alert',
      'amendment',
      'analysis',
      'appointment',
      'arbitrage',
      'armored',
      'atm',
      'atms',
      'auto',
      'b2b',
      'balancing',
      'bank',
      'barbershop',
      'boarding',
      'bonus',
      'book',
      'broker',
      'brokers',
      'building',
      'business',
      'businesses',
      'buy',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Juan Jeronimo',
      'channel': 'Juan Jeronimo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:24](https://www.youtube.com/watch?v=eSIQwH_sArI&t=504s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '"Oh, an ATM business, I could set it up." But no, one thing I will recommend '
              'you guys to do is when you open up a business bank account, always try to open '
              'up two accounts. One for your surcharge and one for your bulk cash.',
      'timestamp': 504,
      'timestamp_label': '[00:08:24]',
      'timestamp_seconds': 504,
      'tip': '"Oh, an ATM business, I could set it up." But no, one thing I will recommend you '
             'guys to do is when you open up a business bank account, always try to open up '
             'two accounts. One for your surcharge and one for your bulk cash.',
      'title': '6 Years of ATM Business Knowledge in 25 Mins ($15,000 Per Month) (Juan '
               'Jeronimo)',
      'url': 'https://www.youtube.com/watch?v=eSIQwH_sArI&t=504s',
      'video_id': 'eSIQwH_sArI'},
     {'author': 'Mr.Money2.0',
      'channel': 'Mr.Money2.0',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:46](https://www.youtube.com/watch?v=ipAviL3RhFM&t=1666s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But even then, the ceiling is not infinite. Every market has a finite number of '
              'highquality locations. Competitors are searching for the same places. Bank '
              'branches can offer free withdrawals. Businesses can decide to stop hosting '
              'third-party ATMs.',
      'timestamp': 1666,
      'timestamp_label': '[00:27:46]',
      'timestamp_seconds': 1666,
      'tip': 'But even then, the ceiling is not infinite. Every market has a finite number of '
             'highquality locations. Competitors are searching for the same places. Bank '
             'branches can offer free withdrawals. Businesses can decide to stop hosting '
             'third-party ATMs.',
      'title': 'How Independent ATM Operators ACTUALLY Make Millions (Hint: It’s Not Banking '
               'Fees) (Mr.Money2.0)',
      'url': 'https://www.youtube.com/watch?v=ipAviL3RhFM&t=1666s',
      'video_id': 'ipAviL3RhFM'},
     {'author': 'Residual Builders',
      'channel': 'Residual Builders',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:49](https://www.youtube.com/watch?v=lubvPaxm55o&t=289s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "224 per month for as long as John's in business. I truly want to emphasize that "
              'this is residual income. You did the work once and now every single month, $224 '
              "hits your bank account. That's $2,688 per year in passive income. That's "
              '$26,880 over the next 10 years.',
      'timestamp': 289,
      'timestamp_label': '[00:04:49]',
      'timestamp_seconds': 289,
      'tip': "224 per month for as long as John's in business. I truly want to emphasize that "
             'this is residual income. You did the work once and now every single month, $224 '
             "hits your bank account. That's $2,688 per year in passive income. That's $26,880 "
             'over the next 10 years.',
      'title': 'Merchant Services Business Model Explained (How to Get Clients in 2026) '
               '(Residual Builders)',
      'url': 'https://www.youtube.com/watch?v=lubvPaxm55o&t=289s',
      'video_id': 'lubvPaxm55o'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:32:26](https://www.youtube.com/watch?v=gBwNpKmRuWY&t=1946s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I know you have a lot of direct contact with the agent channel the agents that '
              "are selling the card not present maybe it's B2B maybe it's service providers.",
      'timestamp': 1946,
      'timestamp_label': '[00:32:26]',
      'timestamp_seconds': 1946,
      'tip': 'I know you have a lot of direct contact with the agent channel the agents that '
             "are selling the card not present maybe it's B2B maybe it's service providers.",
      'title': 'Selling Card Not Present Merchants on Dual Pricing and Surcharging '
               '(CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=gBwNpKmRuWY&t=1946s',
      'video_id': 'gBwNpKmRuWY'},
     {'author': 'ABC News (Australia)',
      'channel': 'ABC News (Australia)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:39](https://www.youtube.com/watch?v=mlRKCgDApCY&t=159s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um obviously, banks are now trying to get a little bit more business from '
              'clients by offering a good rate. But, at the end of the day, we have to see '
              "it's not a win for the consumer. It's not a win for small businesses at all.",
      'timestamp': 159,
      'timestamp_label': '[00:02:39]',
      'timestamp_seconds': 159,
      'tip': 'Um obviously, banks are now trying to get a little bit more business from '
             "clients by offering a good rate. But, at the end of the day, we have to see it's "
             "not a win for the consumer. It's not a win for small businesses at all.",
      'title': 'Businesses may be forced to increase prices as card surcharge ban begins | ABC '
               'NEWS (ABC News (Australia))',
      'url': 'https://www.youtube.com/watch?v=mlRKCgDApCY&t=159s',
      'video_id': 'mlRKCgDApCY'},
     {'author': 'Electronic Money Company',
      'channel': 'Electronic Money Company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=Fc87Q5Igrbc&t=126s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It will be deducted from your residuals. Some reps use this to close a sale. '
              'Some reps sell it for their cost. Others choose to market up. It is your '
              'business, so you decide how to best close a merchant services account. The real '
              'money is in the residual income.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': 'It will be deducted from your residuals. Some reps use this to close a sale. '
             'Some reps sell it for their cost. Others choose to market up. It is your '
             'business, so you decide how to best close a merchant services account. The real '
             'money is in the residual income.',
      'title': 'Merchant Services Residuals: How Does Your Processor Compare? (Part 2) '
               '(Electronic Money Company)',
      'url': 'https://www.youtube.com/watch?v=Fc87Q5Igrbc&t=126s',
      'video_id': 'Fc87Q5Igrbc'},
     {'author': 'Joe Wagner | Merchant Services & Passive Income',
      'channel': 'Joe Wagner | Merchant Services & Passive Income',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:24](https://www.youtube.com/watch?v=6Gf0BTz5h5E&t=24s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sign a merchant account there are departments that help you manage and service '
              'those accounts even if you were to disappear if they had an issue they have a '
              'phone number to call that that account.',
      'timestamp': 24,
      'timestamp_label': '[00:00:24]',
      'timestamp_seconds': 24,
      'tip': 'Sign a merchant account there are departments that help you manage and service '
             'those accounts even if you were to disappear if they had an issue they have a '
             'phone number to call that that account.',
      'title': 'The #1 Residual Income Vehicle for Salespeople | 20 Reasons Why (Joe Wagner | '
               'Merchant Services & Passive Income)',
      'url': 'https://www.youtube.com/watch?v=6Gf0BTz5h5E&t=24s',
      'video_id': '6Gf0BTz5h5E'},
     {'author': 'Helcim',
      'channel': 'Helcim',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:29](https://www.youtube.com/watch?v=cZ2DaswdAqo&t=329s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But first, are you finding value in having payments explained to you in an '
              "open, honest, and detailed way? Well, we've made a free ebook called "
              'Understanding Payments that can serve as a go-to resource for any business '
              'owner curious about payments.',
      'timestamp': 329,
      'timestamp_label': '[00:05:29]',
      'timestamp_seconds': 329,
      'tip': 'But first, are you finding value in having payments explained to you in an open, '
             "honest, and detailed way? Well, we've made a free ebook called Understanding "
             'Payments that can serve as a go-to resource for any business owner curious about '
             'payments.',
      'title': 'Interchange Plus: The "Secret" Pricing Model That Saves Your Business '
               'Thousands (Helcim)',
      'url': 'https://www.youtube.com/watch?v=cZ2DaswdAqo&t=329s',
      'video_id': 'cZ2DaswdAqo'},
     {'author': 'Electronic Payments Coalition',
      'channel': 'Electronic Payments Coalition',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=MXBPDGL9Iss&t=45s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Market-based approach all businesses end up being charged the same capped rate '
              'thanks to durbin your favorite shop on the corner ends up paying the same.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': 'Market-based approach all businesses end up being charged the same capped rate '
             'thanks to durbin your favorite shop on the corner ends up paying the same.',
      'title': 'Repeal the Durbin Amendment - Stop the Merchant Markup (Electronic Payments '
               'Coalition)',
      'url': 'https://www.youtube.com/watch?v=MXBPDGL9Iss&t=45s',
      'video_id': 'MXBPDGL9Iss'},
     {'author': 'Electronic Money Company',
      'channel': 'Electronic Money Company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=HlgVERn_rhY&t=134s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Okay they they want to keep their favorite small businesses in business to '
              "service them but there's a new way coming out now it's called dual.",
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': 'Okay they they want to keep their favorite small businesses in business to '
             "service them but there's a new way coming out now it's called dual.",
      'title': 'Eliminate Your Merchant Services Fees with Dual Pricing! #dualpricing '
               '#merchantservices (Electronic Money Company)',
      'url': 'https://www.youtube.com/watch?v=HlgVERn_rhY&t=134s',
      'video_id': 'HlgVERn_rhY'},
     {'author': 'Philip Webb',
      'channel': 'Philip Webb',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:21](https://www.youtube.com/watch?v=r5NRe-C_aM0&t=201s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So what i'll do is if i'm not going to give a commission we'll probably price "
              'it under the market value and.',
      'timestamp': 201,
      'timestamp_label': '[00:03:21]',
      'timestamp_seconds': 201,
      'tip': "So what i'll do is if i'm not going to give a commission we'll probably price it "
             'under the market value and.',
      'title': 'What Should I Set The Surcharge To - ATM Business 2021 (Philip Webb)',
      'url': 'https://www.youtube.com/watch?v=r5NRe-C_aM0&t=201s',
      'video_id': 'r5NRe-C_aM0'},
     {'author': 'Philip Webb',
      'channel': 'Philip Webb',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=zHPWp60QbG4&t=85s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Because an armored car service they're just putting in the money and then every "
              "time if there's a service issue what happens is the merchant would call us we.",
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': "Because an armored car service they're just putting in the money and then every "
             "time if there's a service issue what happens is the merchant would call us we.",
      'title': 'Top 5 ATM Vault Cash questions answered in detail (ATM Business 2021) (Philip '
               'Webb)',
      'url': 'https://www.youtube.com/watch?v=zHPWp60QbG4&t=85s',
      'video_id': 'zHPWp60QbG4'},
     {'author': 'Merchant Doctor',
      'channel': 'Merchant Doctor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:44](https://www.youtube.com/watch?v=Hx-TboJVDyo&t=224s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Have any comments or questions please leave them below and we'll be happy to "
              'answer them for you right away otherwise jump on over to Facebook and give the '
              'merchant doctor a like so that you can be a part of the merchant doctor '
              'Revolution.',
      'timestamp': 224,
      'timestamp_label': '[00:03:44]',
      'timestamp_seconds': 224,
      'tip': "Have any comments or questions please leave them below and we'll be happy to "
             'answer them for you right away otherwise jump on over to Facebook and give the '
             'merchant doctor a like so that you can be a part of the merchant doctor '
             'Revolution.',
      'title': 'What is the Durbin Amendment & Will Your Credit Card Processor Let you '
               'benefit? (Merchant Doctor)',
      'url': 'https://www.youtube.com/watch?v=Hx-TboJVDyo&t=224s',
      'video_id': 'Hx-TboJVDyo'},
     {'author': 'Sean Jones Revolution Payments',
      'channel': 'Sean Jones Revolution Payments',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:48](https://www.youtube.com/watch?v=EQEdEkxVIXU&t=48s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s been a game Cher because it does doesn't matter how you're processing cards "
              "we're able to do that behind the scenes you can see how these cards are "
              'clearing 2.',
      'timestamp': 48,
      'timestamp_label': '[00:00:48]',
      'timestamp_seconds': 48,
      'tip': "'s been a game Cher because it does doesn't matter how you're processing cards "
             "we're able to do that behind the scenes you can see how these cards are clearing "
             '2.',
      'title': 'How I saved this client over $35,000 in interchange fees with level 3 credit '
               'card processing (Sean Jones Revolution Payments)',
      'url': 'https://www.youtube.com/watch?v=EQEdEkxVIXU&t=48s',
      'video_id': 'EQEdEkxVIXU'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:02](https://www.youtube.com/watch?v=bdumFSr4sA8&t=422s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Importantly learn this industry if you understand it if you're an expert it's "
              "going to help you make more sales it's going to help you build your business my "
              'name is James Shepard thanks for watching this edition of The Merchant sales '
              'insight foreign.',
      'timestamp': 422,
      'timestamp_label': '[00:07:02]',
      'timestamp_seconds': 422,
      'tip': "Importantly learn this industry if you understand it if you're an expert it's "
             "going to help you make more sales it's going to help you build your business my "
             'name is James Shepard thanks for watching this edition of The Merchant sales '
             'insight foreign.',
      'title': 'Understanding Merchant Statements and Fees (CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=bdumFSr4sA8&t=422s',
      'video_id': 'bdumFSr4sA8'}],
 2: [{'author': 'High-Risk Merchant Accounts | Adaptiv Payments',
      'channel': 'High-Risk Merchant Accounts | Adaptiv Payments',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:10](https://www.youtube.com/watch?v=D7Ea5oEHwpM&t=130s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ask for every fee in writing before you sign, and check the contract length and '
              'any early termination fee. Many gateways also take Apple Pay and Google Pay, '
              'and ACH payments straight from a bank account. Online debits need the '
              "customer's account validated first.",
      'timestamp': 130,
      'timestamp_label': '[00:02:10]',
      'timestamp_seconds': 130,
      'tip': 'Ask for every fee in writing before you sign, and check the contract length and '
             'any early termination fee. Many gateways also take Apple Pay and Google Pay, and '
             "ACH payments straight from a bank account. Online debits need the customer's "
             'account validated first.',
      'title': 'High-Risk Payment Gateway: What It Is and How to Get One (2026) (High-Risk '
               'Merchant Accounts | Adaptiv Payments)',
      'url': 'https://www.youtube.com/watch?v=D7Ea5oEHwpM&t=130s',
      'video_id': 'D7Ea5oEHwpM'},
     {'author': 'PaymentProcessorCom',
      'channel': 'PaymentProcessorCom',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:38](https://www.youtube.com/watch?v=q9nKd4oVwnw&t=158s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Fourth, look beyond the advertised rate. Ask for a written breakdown of the '
              'charges that would apply to your business. What do you pay per card payment? '
              'What happens when a customer asks for a refund or disputes a charge? Are there '
              'fees for closing your account?',
      'timestamp': 158,
      'timestamp_label': '[00:02:38]',
      'timestamp_seconds': 158,
      'tip': 'Fourth, look beyond the advertised rate. Ask for a written breakdown of the '
             'charges that would apply to your business. What do you pay per card payment? '
             'What happens when a customer asks for a refund or disputes a charge? Are there '
             'fees for closing your account?',
      'title': 'How to Get a High Risk Merchant Account (PaymentProcessorCom)',
      'url': 'https://www.youtube.com/watch?v=q9nKd4oVwnw&t=158s',
      'video_id': 'q9nKd4oVwnw'},
     {'author': 'Payment Alliance',
      'channel': 'Payment Alliance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=DJ6yGG_L6uI&t=33s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Business cards it's like waving a magic wand and poof more money stays into "
              'your bank account but hold up what makes pay trce the superhero of the payment '
              'world.',
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': "Business cards it's like waving a magic wand and poof more money stays into your "
             'bank account but hold up what makes pay trce the superhero of the payment world.',
      'title': 'Lower Interchange Rates B2B | Interchange Optimization for Level 2 and Level 3 '
               'Cards" (Payment Alliance)',
      'url': 'https://www.youtube.com/watch?v=DJ6yGG_L6uI&t=33s',
      'video_id': 'DJ6yGG_L6uI'},
     {'author': 'Chad The POS Guy',
      'channel': 'Chad The POS Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=pNxf7ZuEt5w&t=45s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Not every point of sale system can do this. For example, Toast and Square do '
              'not have the ability to actually pass the fees off to their customer. So, if '
              "you're using Toast or Square, you as the business owner are forced to pay for "
              'that credit card processing fee.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': 'Not every point of sale system can do this. For example, Toast and Square do not '
             "have the ability to actually pass the fees off to their customer. So, if you're "
             'using Toast or Square, you as the business owner are forced to pay for that '
             'credit card processing fee.',
      'title': 'what is DUAL PRICING / CASH DISCOUNT with a POS? (Chad The POS Guy)',
      'url': 'https://www.youtube.com/watch?v=pNxf7ZuEt5w&t=45s',
      'video_id': 'pNxf7ZuEt5w'},
     {'author': 'Electronic Money Company',
      'channel': 'Electronic Money Company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=QxwC71KUT-g&t=63s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The customer sees both prices and chooses how they want to pay. This method '
              'eliminates the burden of processing fees for the business while giving '
              'customers a transparent choice. Public perception has shifted. 5 years ago, '
              'businesses were hesitant to implement this model.',
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': 'The customer sees both prices and chooses how they want to pay. This method '
             'eliminates the burden of processing fees for the business while giving customers '
             'a transparent choice. Public perception has shifted. 5 years ago, businesses '
             'were hesitant to implement this model.',
      'title': 'How Dual Pricing Helps Merchants Eliminate Credit Card Fees (Electronic Money '
               'Company)',
      'url': 'https://www.youtube.com/watch?v=QxwC71KUT-g&t=63s',
      'video_id': 'QxwC71KUT-g'},
     {'author': 'SwipeNow Payments',
      'channel': 'SwipeNow Payments',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=9ldQhQgiuEY&t=21s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t pay any credit card processing fees. So, stick around as we explore the "
              'benefits, the pros and cons, and how you can choose the right payment processor '
              "for your business. I'm at one of my favorite local restaurants savoring a "
              'delicious meal.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "'t pay any credit card processing fees. So, stick around as we explore the "
             'benefits, the pros and cons, and how you can choose the right payment processor '
             "for your business. I'm at one of my favorite local restaurants savoring a "
             'delicious meal.',
      'title': 'ZERO Fee Processing: No Fee Credit Card Processing | What You Need To Know '
               '(SwipeNow Payments)',
      'url': 'https://www.youtube.com/watch?v=9ldQhQgiuEY&t=21s',
      'video_id': '9ldQhQgiuEY'},
     {'author': 'Scott Shaw',
      'channel': 'Scott Shaw',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=hdPpKRl1Bhk&t=91s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If an item costs ten dollars a cash paying customer will simply pay ten dollars '
              'however if the customer pays with a credit card the total amount will.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': 'If an item costs ten dollars a cash paying customer will simply pay ten dollars '
             'however if the customer pays with a credit card the total amount will.',
      'title': 'Dual Pricing - Cash Discounting Program - Eliminate Payment Processing Fees - '
               'Merchant Services (Scott Shaw)',
      'url': 'https://www.youtube.com/watch?v=hdPpKRl1Bhk&t=91s',
      'video_id': 'hdPpKRl1Bhk'},
     {'author': 'GoDaddy',
      'channel': 'GoDaddy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=bBK7nzs3_mQ&t=15s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'More from every sale than they should. Credit card processing fees  are the '
              'charges a business pays to accept card payments.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'More from every sale than they should. Credit card processing fees  are the '
             'charges a business pays to accept card payments.',
      'title': 'How to Lower Credit Card Processing Fees for Small Businesses - GoDaddy '
               '(GoDaddy)',
      'url': 'https://www.youtube.com/watch?v=bBK7nzs3_mQ&t=15s',
      'video_id': 'bBK7nzs3_mQ'},
     {'author': 'NMI',
      'channel': 'NMI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:41](https://www.youtube.com/watch?v=-APdyXeqh6o&t=461s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So this will throw an error if the merchant tries to add a customer to the '
              'vault if their card or bank account are.',
      'timestamp': 461,
      'timestamp_label': '[00:07:41]',
      'timestamp_seconds': 461,
      'tip': 'So this will throw an error if the merchant tries to add a customer to the vault '
             'if their card or bank account are.',
      'title': 'Advanced Payment Gateway Features (Merchant Configuration Guide) (NMI)',
      'url': 'https://www.youtube.com/watch?v=-APdyXeqh6o&t=461s',
      'video_id': '-APdyXeqh6o'},
     {'author': 'LawLens',
      'channel': 'LawLens',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:11](https://www.youtube.com/watch?v=M4iOZn_3wng&t=131s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Not the bank's overall expenses, not the average cost across millions of "
              'swipes. Here is the example the court used. Suppose a bank buys fraud detection '
              'software for one fixed upfront fee. It pays that fee whether it processes one '
              'transaction or millions.',
      'timestamp': 131,
      'timestamp_label': '[00:02:11]',
      'timestamp_seconds': 131,
      'tip': "Not the bank's overall expenses, not the average cost across millions of swipes. "
             'Here is the example the court used. Suppose a bank buys fraud detection software '
             'for one fixed upfront fee. It pays that fee whether it processes one transaction '
             'or millions.',
      'title': "A Truck Stop Just Killed the Fed's Debit-Card Fee Cap — But Your Checkout "
               "Won't Change Yet (LawLens)",
      'url': 'https://www.youtube.com/watch?v=M4iOZn_3wng&t=131s',
      'video_id': 'M4iOZn_3wng'},
     {'author': 'Merchant Maverick',
      'channel': 'Merchant Maverick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:11](https://www.youtube.com/watch?v=h72ua8pD9cU&t=551s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "150 to 350 is probably something you're going to have to pay to buy a terminal. "
              "It's a reasonable cost and it's fine. Next up is a terminal lease fee.",
      'timestamp': 551,
      'timestamp_label': '[00:09:11]',
      'timestamp_seconds': 551,
      'tip': "150 to 350 is probably something you're going to have to pay to buy a terminal. "
             "It's a reasonable cost and it's fine. Next up is a terminal lease fee.",
      'title': 'Credit Card Processing Fees and Rates Explained (Merchant Maverick)',
      'url': 'https://www.youtube.com/watch?v=h72ua8pD9cU&t=551s',
      'video_id': 'h72ua8pD9cU'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=mqEQN-xgAAk&t=15s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Charged by the issuing bank so the bank that issues the card they have a fee '
              'that they charge and these are called interchange fees now most of you.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Charged by the issuing bank so the bank that issues the card they have a fee '
             'that they charge and these are called interchange fees now most of you.',
      'title': 'What is Interchange Optimization? | Payment Insights (CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=mqEQN-xgAAk&t=15s',
      'video_id': 'mqEQN-xgAAk'},
     {'author': 'Valor PayTech',
      'channel': 'Valor PayTech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=8r3qQJlNz-E&t=88s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'When we hit Process Payment, you’ll see the product details, totals, and a '
              'prompt to proceed appear on the terminal screen. On the terminal, tap Proceed, '
              'confirm Yes, enter the customer’s last name for QuickBooks, and present the '
              'card.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'When we hit Process Payment, you’ll see the product details, totals, and a '
             'prompt to proceed appear on the terminal screen. On the terminal, tap Proceed, '
             'confirm Yes, enter the customer’s last name for QuickBooks, and present the '
             'card.',
      'title': 'How to Use Valor Connect to Complete Online Transactions on POS? (Valor '
               'PayTech)',
      'url': 'https://www.youtube.com/watch?v=8r3qQJlNz-E&t=88s',
      'video_id': '8r3qQJlNz-E'},
     {'author': 'Joe Wagner | Merchant Services & Passive Income',
      'channel': 'Joe Wagner | Merchant Services & Passive Income',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:39](https://www.youtube.com/watch?v=9ImWZ__BWMs&t=99s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Will stay forever because you're happy and not because you're locked into us we "
              'look forward to helping your business and want to say thank you ahead of time '
              'for giving us opportunity to be your payments provider contact easy pay today '
              "and let's get started foreign.",
      'timestamp': 99,
      'timestamp_label': '[00:01:39]',
      'timestamp_seconds': 99,
      'tip': "Will stay forever because you're happy and not because you're locked into us we "
             'look forward to helping your business and want to say thank you ahead of time '
             'for giving us opportunity to be your payments provider contact easy pay today '
             "and let's get started foreign.",
      'title': 'What Is Dual Pricing? | Merchant Services Explained (Joe Wagner | Merchant '
               'Services & Passive Income)',
      'url': 'https://www.youtube.com/watch?v=9ImWZ__BWMs&t=99s',
      'video_id': '9ImWZ__BWMs'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:13](https://www.youtube.com/watch?v=XEaaN73nJ6Q&t=193s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Well somebody has to pay for those rewards and those and that that cash back '
              "you're getting usually it's the merchant that pays for that because.",
      'timestamp': 193,
      'timestamp_label': '[00:03:13]',
      'timestamp_seconds': 193,
      'tip': 'Well somebody has to pay for those rewards and those and that that cash back '
             "you're getting usually it's the merchant that pays for that because.",
      'title': 'What is Tiered Pricing? | Payments Insights (CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=XEaaN73nJ6Q&t=193s',
      'video_id': 'XEaaN73nJ6Q'}],
 3: [{'author': 'Revenue Stacks',
      'channel': 'Revenue Stacks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:41](https://www.youtube.com/watch?v=qJ7rTUZZ68c&t=221s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Prove the unit economics on one machine before you scale. The winner is the ATM '
              'route operator, recurring, scalable, sellable. The verdict is buy the route, '
              "but don't start there. Put it in a good location, a bar, a barbershop, heavy "
              'cash retail, and run it for 6 months.',
      'timestamp': 221,
      'timestamp_label': '[00:03:41]',
      'timestamp_seconds': 221,
      'tip': 'Prove the unit economics on one machine before you scale. The winner is the ATM '
             'route operator, recurring, scalable, sellable. The verdict is buy the route, but '
             "don't start there. Put it in a good location, a bar, a barbershop, heavy cash "
             'retail, and run it for 6 months.',
      'title': "Start an ATM Machine Business. Here's the Real Math + How to do it (Revenue "
               'Stacks)',
      'url': 'https://www.youtube.com/watch?v=qJ7rTUZZ68c&t=221s',
      'video_id': 'qJ7rTUZZ68c'},
     {'author': 'The Business Vault\nYT',
      'channel': 'The Business Vault\nYT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:37](https://www.youtube.com/watch?v=7OKwcgW5-rw&t=397s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "300 transactions could generate $900. But remember, that's revenue, not profit. "
              'First, subtract the processing and network-related costs. Next, account for the '
              "store owner's commission. Then estimate cash handling and replenishment "
              'expenses.',
      'timestamp': 397,
      'timestamp_label': '[00:06:37]',
      'timestamp_seconds': 397,
      'tip': "300 transactions could generate $900. But remember, that's revenue, not profit. "
             'First, subtract the processing and network-related costs. Next, account for the '
             "store owner's commission. Then estimate cash handling and replenishment "
             'expenses.',
      'title': 'How Much Money Does an ATM Business REALLY Make? (The Business Vault\nYT)',
      'url': 'https://www.youtube.com/watch?v=7OKwcgW5-rw&t=397s',
      'video_id': '7OKwcgW5-rw'},
     {'author': 'Side Hustle Culture',
      'channel': 'Side Hustle Culture',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:46](https://www.youtube.com/watch?v=gIHRHcpHBPY&t=226s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Can quickly scale your business with additional machines to produce even more '
              "monthly income or if cash doesn't entice you check out our video on setting up "
              'a bitcoin atm business for even wider profit margins in the booming crypto '
              "space we'll see in the next video.",
      'timestamp': 226,
      'timestamp_label': '[00:03:46]',
      'timestamp_seconds': 226,
      'tip': 'Can quickly scale your business with additional machines to produce even more '
             "monthly income or if cash doesn't entice you check out our video on setting up a "
             'bitcoin atm business for even wider profit margins in the booming crypto space '
             "we'll see in the next video.",
      'title': 'How to Start an ATM Business (Step-by-Step) (Side Hustle Culture)',
      'url': 'https://www.youtube.com/watch?v=gIHRHcpHBPY&t=226s',
      'video_id': 'gIHRHcpHBPY'},
     {'author': 'PaymentCloud',
      'channel': 'PaymentCloud',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=xRGCXR9kPug&t=163s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The advantages of dual pricing are number one lower processing costs. Dual '
              'pricing allows businesses to pass credit card or debit card processing fees to '
              'customers paying with cards, preserving profit margin.',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': 'The advantages of dual pricing are number one lower processing costs. Dual '
             'pricing allows businesses to pass credit card or debit card processing fees to '
             'customers paying with cards, preserving profit margin.',
      'title': 'Save Money With Dual Pricing: Why Merchants Switch to Dual Pricing | Pros, '
               'Cons, and an Example (PaymentCloud)',
      'url': 'https://www.youtube.com/watch?v=xRGCXR9kPug&t=163s',
      'video_id': 'xRGCXR9kPug'},
     {'author': 'Residual Builders',
      'channel': 'Residual Builders',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:37](https://www.youtube.com/watch?v=r78HBt5LE9U&t=517s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And so, we can tell business owners, "Listen, we\'re just going to charge you '
              "the cost of the card, and I'm going to add 0. 60% as my own profit margin on "
              'top of that cost." Then you have another pricing model called tiered pricing.',
      'timestamp': 517,
      'timestamp_label': '[00:08:37]',
      'timestamp_seconds': 517,
      'tip': 'And so, we can tell business owners, "Listen, we\'re just going to charge you '
             "the cost of the card, and I'm going to add 0. 60% as my own profit margin on top "
             'of that cost." Then you have another pricing model called tiered pricing.',
      'title': 'Merchant Services Explained (How Payment Processing Actually Works) (Residual '
               'Builders)',
      'url': 'https://www.youtube.com/watch?v=r78HBt5LE9U&t=517s',
      'video_id': 'r78HBt5LE9U'},
     {'author': 'Merchant Maverick',
      'channel': 'Merchant Maverick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=CTTa8diTsTU&t=31s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Essentially, it’s a way for businesses to pass the cost of transaction fees '
              'onto the customer instead of absorbing them. Some businesses may also offer '
              'cash discounting, which offers customers a slightly lower price if they pay '
              'with cash or a debit card.',
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': 'Essentially, it’s a way for businesses to pass the cost of transaction fees onto '
             'the customer instead of absorbing them. Some businesses may also offer cash '
             'discounting, which offers customers a slightly lower price if they pay with cash '
             'or a debit card.',
      'title': 'Credit Card Surcharging: What You Need to Know (Merchant Maverick)',
      'url': 'https://www.youtube.com/watch?v=CTTa8diTsTU&t=31s',
      'video_id': 'CTTa8diTsTU'},
     {'author': 'Philip Webb',
      'channel': 'Philip Webb',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:15](https://www.youtube.com/watch?v=2-Udo9XtHqM&t=315s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But sometimes we profit because we put a little sign in the barbershop that '
              'says cash inside atm inside and we get a lot of street traffic people walking '
              'in to.',
      'timestamp': 315,
      'timestamp_label': '[00:05:15]',
      'timestamp_seconds': 315,
      'tip': 'But sometimes we profit because we put a little sign in the barbershop that says '
             'cash inside atm inside and we get a lot of street traffic people walking in to.',
      'title': 'The top 5 secrets when placing an ATM in a Barbershop (ATM business tips) '
               '(Philip Webb)',
      'url': 'https://www.youtube.com/watch?v=2-Udo9XtHqM&t=315s',
      'video_id': '2-Udo9XtHqM'},
     {'author': 'Joe Wagner | Merchant Services & Passive Income',
      'channel': 'Joe Wagner | Merchant Services & Passive Income',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=81tAw0Al6N0&t=51s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And don't forget those annual fees, too. Across America, businesses are taking "
              "advantage of the law, but many small business owners don't even know about this "
              'option. Have you ever been to a gas station where they offer a cash price and '
              'credit price per gallon?',
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': "And don't forget those annual fees, too. Across America, businesses are taking "
             "advantage of the law, but many small business owners don't even know about this "
             'option. Have you ever been to a gas station where they offer a cash price and '
             'credit price per gallon?',
      'title': 'How the Cash Discount Program & Dual Pricing Actually Work (Full Explanation) '
               '(Joe Wagner | Merchant Services & Passive Income)',
      'url': 'https://www.youtube.com/watch?v=81tAw0Al6N0&t=51s',
      'video_id': '81tAw0Al6N0'},
     {'author': 'Titan Merchant Services',
      'channel': 'Titan Merchant Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=lsC_M7zjTjY&t=72s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Or pay with cash at a reduced price this helps offset the cost of processing '
              'payments and history has proven that card paying customers will still pay for.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': 'Or pay with cash at a reduced price this helps offset the cost of processing '
             'payments and history has proven that card paying customers will still pay for.',
      'title': 'Best Payment Processing Solutions: Cash Discount & Dual Pricing (Titan '
               'Merchant Services)',
      'url': 'https://www.youtube.com/watch?v=lsC_M7zjTjY&t=72s',
      'video_id': 'lsC_M7zjTjY'},
     {'author': 'Ryan Anthony',
      'channel': 'Ryan Anthony',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:26](https://www.youtube.com/watch?v=KsqD8Ch93YI&t=566s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll do is they will uh raise the price of everything, raise the price and then "
              "discount the cash. So what this is is in effect doing is it's giving you a way "
              'to recoup the cost and then discounting the cash.',
      'timestamp': 566,
      'timestamp_label': '[00:09:26]',
      'timestamp_seconds': 566,
      'tip': "'ll do is they will uh raise the price of everything, raise the price and then "
             "discount the cash. So what this is is in effect doing is it's giving you a way "
             'to recoup the cost and then discounting the cash.',
      'title': 'How to Legally Offset Credit Card Processing Fees (Ryan Anthony)',
      'url': 'https://www.youtube.com/watch?v=KsqD8Ch93YI&t=566s',
      'video_id': 'KsqD8Ch93YI'},
     {'author': 'BancardSales',
      'channel': 'BancardSales',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:30](https://www.youtube.com/watch?v=5jk-0XxkiR0&t=330s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Overall rates and overall costs that you'll end up paying for merchant services "
              'flat rate pricing is offered by both merchant account providers and by.',
      'timestamp': 330,
      'timestamp_label': '[00:05:30]',
      'timestamp_seconds': 330,
      'tip': "Overall rates and overall costs that you'll end up paying for merchant services "
             'flat rate pricing is offered by both merchant account providers and by.',
      'title': 'Merchant Account Rates & Pricing - Interchange Plus, Tier Based & Flat Rate '
               'Comparison (BancardSales)',
      'url': 'https://www.youtube.com/watch?v=5jk-0XxkiR0&t=330s',
      'video_id': '5jk-0XxkiR0'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:58](https://www.youtube.com/watch?v=AnhJYbY3ptw&t=58s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You have to understand how this works. When you are doing interchange plus '
              'pricing for instance, what you are doing is you are passing the cost of '
              'interchange and the bank fees and the dues and assessments and all that through '
              'to the merchant.',
      'timestamp': 58,
      'timestamp_label': '[00:00:58]',
      'timestamp_seconds': 58,
      'tip': 'You have to understand how this works. When you are doing interchange plus '
             'pricing for instance, what you are doing is you are passing the cost of '
             'interchange and the bank fees and the dues and assessments and all that through '
             'to the merchant.',
      'title': 'Cash Discounting Residuals – The Most Important Variable (CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=AnhJYbY3ptw&t=58s',
      'video_id': 'AnhJYbY3ptw'},
     {'author': 'Electronic Money Company',
      'channel': 'Electronic Money Company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:18](https://www.youtube.com/watch?v=AdPAOJ52cvk&t=138s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They understand that the more you earn, the more they earn. The wrong processor '
              'uses confusing statements, changing pricing behind the scenes, changing the '
              'rates that you have to sell at, changing bonus programs.',
      'timestamp': 138,
      'timestamp_label': '[00:02:18]',
      'timestamp_seconds': 138,
      'tip': 'They understand that the more you earn, the more they earn. The wrong processor '
             'uses confusing statements, changing pricing behind the scenes, changing the '
             'rates that you have to sell at, changing bonus programs.',
      'title': 'How to Build Six-Figure Residuals in Merchant Services (It’s Not Just Closing '
               'Deals) (Electronic Money Company)',
      'url': 'https://www.youtube.com/watch?v=AdPAOJ52cvk&t=138s',
      'video_id': 'AdPAOJ52cvk'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=qBBgFNiTDYg&t=115s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you paid $5, you would price it at six. So, the idea of you just mark it up '
              "20% no matter how much it cost you, you mark it up 20%. Now, there's there's "
              'benefits and drawbacks to that pricing structure, right? The benefit would be '
              "you know you're going to make money.",
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': 'If you paid $5, you would price it at six. So, the idea of you just mark it up '
             "20% no matter how much it cost you, you mark it up 20%. Now, there's there's "
             'benefits and drawbacks to that pricing structure, right? The benefit would be '
             "you know you're going to make money.",
      'title': 'What is Interchange Plus Pricing? | Payments Insights (CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=qBBgFNiTDYg&t=115s',
      'video_id': 'qBBgFNiTDYg'},
     {'author': 'Joe Wagner | Merchant Services & Passive Income',
      'channel': 'Joe Wagner | Merchant Services & Passive Income',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=XXH81AbZQcg&t=25s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Merchants are never shown how transactions are routed into these tiers, which '
              "means there's no way to know what the processor is actually earning. This lack "
              'of transparency almost always results in higher cost than interchange plus '
              'pricing. Tiered pricing is old school.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': 'Merchants are never shown how transactions are routed into these tiers, which '
             "means there's no way to know what the processor is actually earning. This lack "
             'of transparency almost always results in higher cost than interchange plus '
             'pricing. Tiered pricing is old school.',
      'title': 'What Is Tiered Pricing? Merchant Services Pricing Explained (Joe Wagner | '
               'Merchant Services & Passive Income)',
      'url': 'https://www.youtube.com/watch?v=XXH81AbZQcg&t=25s',
      'video_id': 'XXH81AbZQcg'}],
 4: [{'author': 'Philip Webb',
      'channel': 'Philip Webb',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:37](https://www.youtube.com/watch?v=nAL1HBqHAl8&t=37s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then he was shocked by discovering additional expenses. Some of these expenses '
              'are business registration or corporate setup, monthly bank account fees, '
              'transportation costs, and working capital for the day-to-day business.',
      'timestamp': 37,
      'timestamp_label': '[00:00:37]',
      'timestamp_seconds': 37,
      'tip': 'Then he was shocked by discovering additional expenses. Some of these expenses '
             'are business registration or corporate setup, monthly bank account fees, '
             'transportation costs, and working capital for the day-to-day business.',
      'title': 'Everything You Need to Know About Starting an ATM Business (Philip Webb)',
      'url': 'https://www.youtube.com/watch?v=nAL1HBqHAl8&t=37s',
      'video_id': 'nAL1HBqHAl8'},
     {'author': 'ATMDepot - Make Money with ATM Machines',
      'channel': 'ATMDepot - Make Money with ATM Machines',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=Cb9qwLOH7y0&t=98s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's low effort, but not zero effort. Con two, upfront costs and risks. Like "
              "any business, you'll have some startup costs. You'll need to buy your ATM, "
              "maybe pay rent if it's in a mall or busy spot, and get insurance if you want "
              'extra protection.',
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': "It's low effort, but not zero effort. Con two, upfront costs and risks. Like any "
             "business, you'll have some startup costs. You'll need to buy your ATM, maybe pay "
             "rent if it's in a mall or busy spot, and get insurance if you want extra "
             'protection.',
      'title': 'ATM Business Pros and Cons 2025 | Is It Still Worth Starting an ATM Business '
               'Today? (ATMDepot - Make Money with ATM Machines)',
      'url': 'https://www.youtube.com/watch?v=Cb9qwLOH7y0&t=98s',
      'video_id': 'Cb9qwLOH7y0'},
     {'author': 'Merchant Maverick',
      'channel': 'Merchant Maverick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:19](https://www.youtube.com/watch?v=2E0M95jxJpU&t=199s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Reach out to them directly for a custom quote, but PaymentCloud does not charge '
              'any account setup fees. To round out our list is our top pick, Payment Nerds. '
              'Payment Nerds serves businesses and industries such as CBD, crypto trading, '
              'online dating, and nutraceuticals.',
      'timestamp': 199,
      'timestamp_label': '[00:03:19]',
      'timestamp_seconds': 199,
      'tip': 'Reach out to them directly for a custom quote, but PaymentCloud does not charge '
             'any account setup fees. To round out our list is our top pick, Payment Nerds. '
             'Payment Nerds serves businesses and industries such as CBD, crypto trading, '
             'online dating, and nutraceuticals.',
      'title': 'The Best High-Risk Merchant Accounts (Merchant Maverick)',
      'url': 'https://www.youtube.com/watch?v=2E0M95jxJpU&t=199s',
      'video_id': '2E0M95jxJpU'},
     {'author': 'The Digital Merchant',
      'channel': 'The Digital Merchant',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:37](https://www.youtube.com/watch?v=kpo2g7o_Ylg&t=577s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They take on a lot of the liability, so they really mitigate risk. Um their '
              "drawback though is their tech stack is a mix of stuff that they've acquired as "
              'of recent third party tools and then their own software. So it can be a little '
              'disjointed from what I understand.',
      'timestamp': 577,
      'timestamp_label': '[00:09:37]',
      'timestamp_seconds': 577,
      'tip': 'They take on a lot of the liability, so they really mitigate risk. Um their '
             "drawback though is their tech stack is a mix of stuff that they've acquired as "
             'of recent third party tools and then their own software. So it can be a little '
             'disjointed from what I understand.',
      'title': 'Best Payment Processors for ISOs and Agents: A CPA’s 2026 Guide (The Digital '
               'Merchant)',
      'url': 'https://www.youtube.com/watch?v=kpo2g7o_Ylg&t=577s',
      'video_id': 'kpo2g7o_Ylg'},
     {'author': 'Finance Blueprint',
      'channel': 'Finance Blueprint',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:27](https://www.youtube.com/watch?v=_wQk1Avcku8&t=987s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'APIs, security architecture and PCI readiness, underwriting and compliance '
              'setup, test terminals, recruitment, training, marketing, insurance, working '
              'capital and contingency.',
      'timestamp': 987,
      'timestamp_label': '[00:16:27]',
      'timestamp_seconds': 987,
      'tip': 'APIs, security architecture and PCI readiness, underwriting and compliance '
             'setup, test terminals, recruitment, training, marketing, insurance, working '
             'capital and contingency.',
      'title': 'The Economics of Owning a Payment Processing Company Explained (Finance '
               'Blueprint)',
      'url': 'https://www.youtube.com/watch?v=_wQk1Avcku8&t=987s',
      'video_id': '_wQk1Avcku8'},
     {'author': 'Residual Builders',
      'channel': 'Residual Builders',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:01](https://www.youtube.com/watch?v=nqxmsddQ2LU&t=961s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And so, another pain point. Now, think about that for a second. These are '
              'people who run real businesses, have revenue, but need capital for emergency. '
              'And they just got told no by the bank.',
      'timestamp': 961,
      'timestamp_label': '[00:16:01]',
      'timestamp_seconds': 961,
      'tip': 'And so, another pain point. Now, think about that for a second. These are people '
             'who run real businesses, have revenue, but need capital for emergency. And they '
             'just got told no by the bank.',
      'title': 'How to Sell Merchant Services in 2026 (What Actually Works Now) (Residual '
               'Builders)',
      'url': 'https://www.youtube.com/watch?v=nqxmsddQ2LU&t=961s',
      'video_id': 'nqxmsddQ2LU'},
     {'author': 'Scott Shaw',
      'channel': 'Scott Shaw',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:07](https://www.youtube.com/watch?v=tjdQFiCG9xo&t=127s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'American bank card from unparalleled Merchant benefits unrivaled income '
              'generation potential to novel sales tools partnering with us is the smartest '
              "move you'll make for more information or to partner with us please visit our "
              'website at North americanbank card. proo.',
      'timestamp': 127,
      'timestamp_label': '[00:02:07]',
      'timestamp_seconds': 127,
      'tip': 'American bank card from unparalleled Merchant benefits unrivaled income '
             'generation potential to novel sales tools partnering with us is the smartest '
             "move you'll make for more information or to partner with us please visit our "
             'website at North americanbank card. proo.',
      'title': 'North American Bancard - ISO Agent Program - Become a Payment Processor - '
               'Selling Merchant Services (Scott Shaw)',
      'url': 'https://www.youtube.com/watch?v=tjdQFiCG9xo&t=127s',
      'video_id': 'tjdQFiCG9xo'},
     {'author': 'TODAY',
      'channel': 'TODAY',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:05](https://www.youtube.com/watch?v=ahGJLcVvtj0&t=125s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'ANGRY ABOUT SURCHARGES OR FEES THAT ARE DISCLOSED AT THE VERY BEGINNING. '
              'Reporter: FOR MANY BUSINESSES A SMALL SURCHARGE HELPS KEEPS PRICES STABLE LIKE '
              'AT LAVERY BREWERY COMPANY IN DOWNTOWN ERIE, PENNSYLVANIA. INSURANCE COSTS ARE '
              'GOING UP. I DID NOT WANT TO RAISE OUR PRICES.',
      'timestamp': 125,
      'timestamp_label': '[00:02:05]',
      'timestamp_seconds': 125,
      'tip': 'ANGRY ABOUT SURCHARGES OR FEES THAT ARE DISCLOSED AT THE VERY BEGINNING. '
             'Reporter: FOR MANY BUSINESSES A SMALL SURCHARGE HELPS KEEPS PRICES STABLE LIKE '
             'AT LAVERY BREWERY COMPANY IN DOWNTOWN ERIE, PENNSYLVANIA. INSURANCE COSTS ARE '
             'GOING UP. I DID NOT WANT TO RAISE OUR PRICES.',
      'title': 'How to Avoid Credit Card Surcharges and Convenience Fees (TODAY)',
      'url': 'https://www.youtube.com/watch?v=ahGJLcVvtj0&t=125s',
      'video_id': 'ahGJLcVvtj0'},
     {'author': 'Paygent AI',
      'channel': 'Paygent AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:15](https://www.youtube.com/watch?v=xTWy5shtdSk&t=435s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It can be businesses that do ACH heavy. So big businesses who do a lot of like '
              'high ticket dollar values, uh they would make up that would make a lot of sense '
              'for those organizations as well.',
      'timestamp': 435,
      'timestamp_label': '[00:07:15]',
      'timestamp_seconds': 435,
      'tip': 'It can be businesses that do ACH heavy. So big businesses who do a lot of like '
             'high ticket dollar values, uh they would make up that would make a lot of sense '
             'for those organizations as well.',
      'title': 'Flat Rate vs Interchange Plus vs Tiered Pricing — What Merchants Need to Know '
               '(Paygent AI)',
      'url': 'https://www.youtube.com/watch?v=xTWy5shtdSk&t=435s',
      'video_id': 'xTWy5shtdSk'},
     {'author': 'Sean Jones Revolution Payments',
      'channel': 'Sean Jones Revolution Payments',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=QBl05xxHst0&t=15s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Provider can set up a merchant account to accept business to business and '
              'business to government purchases however level 3 processing can reduce your.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Provider can set up a merchant account to accept business to business and '
             'business to government purchases however level 3 processing can reduce your.',
      'title': 'Level 3 Processing Interchange Rates | Revolution Payments (Sean Jones '
               'Revolution Payments)',
      'url': 'https://www.youtube.com/watch?v=QBl05xxHst0&t=15s',
      'video_id': 'QBl05xxHst0'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:15](https://www.youtube.com/watch?v=AKvayIEwefA&t=315s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The b2b space so business to business business to government have some unique '
              'requirements and you know our CEO wants to make merchants happy and we '
              'realized.',
      'timestamp': 315,
      'timestamp_label': '[00:05:15]',
      'timestamp_seconds': 315,
      'tip': 'The b2b space so business to business business to government have some unique '
             'requirements and you know our CEO wants to make merchants happy and we realized.',
      'title': 'Interchange Optimization Made Easy - Live Event Replay (CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=AKvayIEwefA&t=315s',
      'video_id': 'AKvayIEwefA'},
     {'author': 'Electronic Money Company',
      'channel': 'Electronic Money Company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=J2MM1Nbrie8&t=43s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Want one example of residual income is selling Merchants Services we get a '
              'split of every transaction that goes through our Merchants accounts and as.',
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': 'Want one example of residual income is selling Merchants Services we get a split '
             'of every transaction that goes through our Merchants accounts and as.',
      'title': 'Merchant Service Sales - Residual Income Opportunity Business! | Sell Merchant '
               'Services (Electronic Money Company)',
      'url': 'https://www.youtube.com/watch?v=J2MM1Nbrie8&t=43s',
      'video_id': 'J2MM1Nbrie8'},
     {'author': 'Joe Wagner | Merchant Services & Passive Income',
      'channel': 'Joe Wagner | Merchant Services & Passive Income',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=j2tVhd1OiOw&t=15s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "To you growing your business and helping people so let's jump right in here  to "
              'kick this off right let me share this.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "To you growing your business and helping people so let's jump right in here  to "
             'kick this off right let me share this.',
      'title': 'Activating Merchant Accounts Makes the Residual Income (Joe Wagner | Merchant '
               'Services & Passive Income)',
      'url': 'https://www.youtube.com/watch?v=j2tVhd1OiOw&t=15s',
      'video_id': 'j2tVhd1OiOw'},
     {'author': 'Scott Shaw',
      'channel': 'Scott Shaw',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:15](https://www.youtube.com/watch?v=CyITyguICWc&t=135s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Unparalleled Merchant benefits unrivaled income generation potential to novel '
              'sales tools partnering with us is the smartest move you will make for more '
              'information or to partner with us please visit our website at '
              'charmerchantgroup.com foreign.',
      'timestamp': 135,
      'timestamp_label': '[00:02:15]',
      'timestamp_seconds': 135,
      'tip': 'Unparalleled Merchant benefits unrivaled income generation potential to novel '
             'sales tools partnering with us is the smartest move you will make for more '
             'information or to partner with us please visit our website at '
             'charmerchantgroup.com foreign.',
      'title': 'Become a Payment Service Provider - Becoming a Payment Processor Company - '
               'Become a Merchant ISO/MSP (Scott Shaw)',
      'url': 'https://www.youtube.com/watch?v=CyITyguICWc&t=135s',
      'video_id': 'CyITyguICWc'},
     {'author': 'Electronic Money Company',
      'channel': 'Electronic Money Company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:07](https://www.youtube.com/watch?v=CGOJATo9AMI&t=127s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Gay at 505 296 2847 let's take the skills you've gained from James Shepard's "
              "videos and turn them into Real Results don't settle for less join electronic "
              "money company and build a career you're proud of call today talk to you soon "
              'bye.',
      'timestamp': 127,
      'timestamp_label': '[00:02:07]',
      'timestamp_seconds': 127,
      'tip': "Gay at 505 296 2847 let's take the skills you've gained from James Shepard's "
             "videos and turn them into Real Results don't settle for less join electronic "
             "money company and build a career you're proud of call today talk to you soon "
             'bye.',
      'title': 'How to Boost Merchant Services Sales Rep Income! (Electronic Money Company)',
      'url': 'https://www.youtube.com/watch?v=CGOJATo9AMI&t=127s',
      'video_id': 'CGOJATo9AMI'}],
 5: [{'author': 'The Business Guy | Asset Protection Planners',
      'channel': 'The Business Guy | Asset Protection Planners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:26](https://www.youtube.com/watch?v=qUuX7pVlywk&t=986s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'ATMs in their branches, you know, all around town. Wells Fargo, Chase, US Bank, '
              'PNC, Centrust, you know, every every grocery store has an ATM, but not every '
              'new business has an ATM, right? Because new businesses are popping up every '
              'day.',
      'timestamp': 986,
      'timestamp_label': '[00:16:26]',
      'timestamp_seconds': 986,
      'tip': 'ATMs in their branches, you know, all around town. Wells Fargo, Chase, US Bank, '
             'PNC, Centrust, you know, every every grocery store has an ATM, but not every new '
             'business has an ATM, right? Because new businesses are popping up every day.',
      'title': 'How to Start an ATM Business - $2,182 Profit/Mo. Per Machine (The Business Guy '
               '| Asset Protection Planners)',
      'url': 'https://www.youtube.com/watch?v=qUuX7pVlywk&t=986s',
      'video_id': 'qUuX7pVlywk'},
     {'author': 'Philip Webb',
      'channel': 'Philip Webb',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:49](https://www.youtube.com/watch?v=y2XZeV3G0YU&t=49s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Second, what real ATM performance actually looks like. And third, the most '
              'common early mistakes and how to avoid them. Question number one, how long does '
              'it take for an ATM to work? This is almost always the first question. ATMs do '
              'not work on timelines.',
      'timestamp': 49,
      'timestamp_label': '[00:00:49]',
      'timestamp_seconds': 49,
      'tip': 'Second, what real ATM performance actually looks like. And third, the most '
             'common early mistakes and how to avoid them. Question number one, how long does '
             'it take for an ATM to work? This is almost always the first question. ATMs do '
             'not work on timelines.',
      'title': 'Before You Start an ATM Business, Watch This (Philip Webb)',
      'url': 'https://www.youtube.com/watch?v=y2XZeV3G0YU&t=49s',
      'video_id': 'y2XZeV3G0YU'},
     {'author': 'Electronic Money Company',
      'channel': 'Electronic Money Company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:15](https://www.youtube.com/watch?v=MTRmzsfsHTs&t=135s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Their Hardware a way to make to lower the risk and lower the rate on B2B and '
              'b2g cards businesses to business and business to government for each.',
      'timestamp': 135,
      'timestamp_label': '[00:02:15]',
      'timestamp_seconds': 135,
      'tip': 'Their Hardware a way to make to lower the risk and lower the rate on B2B and b2g '
             'cards businesses to business and business to government for each.',
      'title': 'Saving Money on Credit Card Processing Fees | Merchant Services | Credit Card '
               'Terminal (Electronic Money Company)',
      'url': 'https://www.youtube.com/watch?v=MTRmzsfsHTs&t=135s',
      'video_id': 'MTRmzsfsHTs'},
     {'author': 'Future Investor',
      'channel': 'Future Investor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:05](https://www.youtube.com/watch?v=l2IVnP9Bnwk&t=425s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'An ATM business has a deceptively physical problem. Machines break, screens '
              'fail, card readers malfunction, cash dispensers jam, and communication links go '
              'down.',
      'timestamp': 425,
      'timestamp_label': '[00:07:05]',
      'timestamp_seconds': 425,
      'tip': 'An ATM business has a deceptively physical problem. Machines break, screens '
             'fail, card readers malfunction, cash dispensers jam, and communication links go '
             'down.',
      'title': 'Where Does Your $5 ATM Fee Actually Go? (Future Investor)',
      'url': 'https://www.youtube.com/watch?v=l2IVnP9Bnwk&t=425s',
      'video_id': 'l2IVnP9Bnwk'},
     {'author': 'Funnelish',
      'channel': 'Funnelish',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:14](https://www.youtube.com/watch?v=-G2UpQAf8L0&t=434s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'NMI, which is connected to a second merchant account. If I have a temporary '
              "decline, or there's a problem with one of my accounts, I don't have to lose "
              'that sale. Once this strategy is set up, rules get checked top to bottom.',
      'timestamp': 434,
      'timestamp_label': '[00:07:14]',
      'timestamp_seconds': 434,
      'tip': 'NMI, which is connected to a second merchant account. If I have a temporary '
             "decline, or there's a problem with one of my accounts, I don't have to lose that "
             'sale. Once this strategy is set up, rules get checked top to bottom.',
      'title': 'Do All Supplement Brands Need a High Risk Merchant Account? (+ Payment '
               'Routing) (Funnelish)',
      'url': 'https://www.youtube.com/watch?v=-G2UpQAf8L0&t=434s',
      'video_id': '-G2UpQAf8L0'},
     {'author': 'Megalith',
      'channel': 'Megalith',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:55](https://www.youtube.com/watch?v=lnoavHYKfcI&t=295s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your server shows the invoice, checks that it was paid, and approves the order. '
              'The agent wires that up for you. So, if card processors call you high risk, for '
              'cards, look at a high-risk merchant account like Sorpay or Durango.',
      'timestamp': 295,
      'timestamp_label': '[00:04:55]',
      'timestamp_seconds': 295,
      'tip': 'Your server shows the invoice, checks that it was paid, and approves the order. '
             'The agent wires that up for you. So, if card processors call you high risk, for '
             'cards, look at a high-risk merchant account like Sorpay or Durango.',
      'title': 'High-Risk Payment Processing: Get Paid Without a Merchant Account (Megalith)',
      'url': 'https://www.youtube.com/watch?v=lnoavHYKfcI&t=295s',
      'video_id': 'lnoavHYKfcI'},
     {'author': 'The Reach Network',
      'channel': 'The Reach Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:07](https://www.youtube.com/watch?v=fO958wEcK8A&t=67s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If there is a chargeback that's being filed and the chargeback meets the "
              'criteria Ethoca was set up with for for that specific account, then the '
              "merchant will receive an alert saying somebody's filing a chargeback on the "
              'following payment.',
      'timestamp': 67,
      'timestamp_label': '[00:01:07]',
      'timestamp_seconds': 67,
      'tip': "If there is a chargeback that's being filed and the chargeback meets the "
             'criteria Ethoca was set up with for for that specific account, then the merchant '
             "will receive an alert saying somebody's filing a chargeback on the following "
             'payment.',
      'title': 'True Fraud #8 - Avoid Chargeback Blind Spots With Ethoca and Verifi (The Reach '
               'Network)',
      'url': 'https://www.youtube.com/watch?v=fO958wEcK8A&t=67s',
      'video_id': 'fO958wEcK8A'},
     {'author': 'Philip Webb',
      'channel': 'Philip Webb',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:44](https://www.youtube.com/watch?v=OHndNgTdq3Y&t=284s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This business especially on our site because we do have risk out there point '
              'number four is the auto renewal you always want to.',
      'timestamp': 284,
      'timestamp_label': '[00:04:44]',
      'timestamp_seconds': 284,
      'tip': 'This business especially on our site because we do have risk out there point '
             'number four is the auto renewal you always want to.',
      'title': 'ATM location agreement - Top 5 things you needed in your ATM location '
               'agreement  (ATM Business 2021) (Philip Webb)',
      'url': 'https://www.youtube.com/watch?v=OHndNgTdq3Y&t=284s',
      'video_id': 'OHndNgTdq3Y'},
     {'author': 'Verifi, A Visa Solution',
      'channel': 'Verifi, A Visa Solution',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:58](https://www.youtube.com/watch?v=KktmiaWBVe8&t=58s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Notification to the participating seller seller has 72 hours to decide if they '
              'want to proactively refund the pre-dispute to avoid a chargeback and.',
      'timestamp': 58,
      'timestamp_label': '[00:00:58]',
      'timestamp_seconds': 58,
      'tip': 'Notification to the participating seller seller has 72 hours to decide if they '
             'want to proactively refund the pre-dispute to avoid a chargeback and.',
      'title': 'Verifi Explainer Series | RESOLVE for Merchants (Verifi, A Visa Solution)',
      'url': 'https://www.youtube.com/watch?v=KktmiaWBVe8&t=58s',
      'video_id': 'KktmiaWBVe8'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:04](https://www.youtube.com/watch?v=Aqf6gQvEgnw&t=244s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Oh, I’ve got to have a buy out. I got to get this money right now. Take an '
              'extra week to make sure you are getting the right deal, because if you don’t '
              'get the right deal long term, it’s a big problem.',
      'timestamp': 244,
      'timestamp_label': '[00:04:04]',
      'timestamp_seconds': 244,
      'tip': 'Oh, I’ve got to have a buy out. I got to get this money right now. Take an extra '
             'week to make sure you are getting the right deal, because if you don’t get the '
             'right deal long term, it’s a big problem.',
      'title': 'Residual Buyouts - Don’t make this mistake (CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=Aqf6gQvEgnw&t=244s',
      'video_id': 'Aqf6gQvEgnw'},
     {'author': 'Rocket ATM',
      'channel': 'Rocket ATM',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:27](https://www.youtube.com/watch?v=gS2sjD2NYOU&t=1167s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mistake there clear clear clear I need to make a space here so one one one one '
              "one on one there's the space right there I just made a space so welcome - there "
              "you go and I need another space so one one one there's the space right there "
              'welcome to rocket.',
      'timestamp': 1167,
      'timestamp_label': '[00:19:27]',
      'timestamp_seconds': 1167,
      'tip': 'Mistake there clear clear clear I need to make a space here so one one one one '
             "one on one there's the space right there I just made a space so welcome - there "
             "you go and I need another space so one one one there's the space right there "
             'welcome to rocket.',
      'title': 'Genmega Hantle ATM Setup Step By Step Guide - CDS (Rocket ATM)',
      'url': 'https://www.youtube.com/watch?v=gS2sjD2NYOU&t=1167s',
      'video_id': 'gS2sjD2NYOU'},
     {'author': 'Chargeflow',
      'channel': 'Chargeflow',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:07](https://www.youtube.com/watch?v=sBnXe7LYFO8&t=127s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Chargeback notification is a somber note that arrives after a dispute has been '
              'filed bearing the unfortunate news of a customer grievance already causing.',
      'timestamp': 127,
      'timestamp_label': '[00:02:07]',
      'timestamp_seconds': 127,
      'tip': 'Chargeback notification is a somber note that arrives after a dispute has been '
             'filed bearing the unfortunate news of a customer grievance already causing.',
      'title': 'How Chargeback Alerts Work: Verifi RDR, Ethoca & CDRN Explained for Merchants '
               '(Chargeflow)',
      'url': 'https://www.youtube.com/watch?v=sBnXe7LYFO8&t=127s',
      'video_id': 'sBnXe7LYFO8'},
     {'author': 'Scott E. Adams | Chargeback Expert',
      'channel': 'Scott E. Adams | Chargeback Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:04](https://www.youtube.com/watch?v=5mi35dvcRrA&t=364s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Those categories of products um you know the coming days we'll have some more "
              'around other products in there and also some ideas um better or not products on '
              'how to learn your fraud to in your chargebacks so thanks a lot.',
      'timestamp': 364,
      'timestamp_label': '[00:06:04]',
      'timestamp_seconds': 364,
      'tip': "Those categories of products um you know the coming days we'll have some more "
             'around other products in there and also some ideas um better or not products on '
             'how to learn your fraud to in your chargebacks so thanks a lot.',
      'title': "Rapid Dispute Resolution (RDR) vs Verifi CDRN and Ethoca Alerts - What's the "
               'Difference? (Scott E. Adams | Chargeback Expert)',
      'url': 'https://www.youtube.com/watch?v=5mi35dvcRrA&t=364s',
      'video_id': '5mi35dvcRrA'},
     {'author': 'Joe Wagner | Merchant Services & Passive Income',
      'channel': 'Joe Wagner | Merchant Services & Passive Income',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:52](https://www.youtube.com/watch?v=BzCJ4NGRI54&t=412s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Guys are at then from targets we're converting them over to deals and then "
              'folks obviously very very very important but this business is not about deals '
              'this business and put this one in green.',
      'timestamp': 412,
      'timestamp_label': '[00:06:52]',
      'timestamp_seconds': 412,
      'tip': "Guys are at then from targets we're converting them over to deals and then folks "
             'obviously very very very important but this business is not about deals this '
             'business and put this one in green.',
      'title': 'How to Succeed in Merchant Services Sales | 10-Minute Guide (Joe Wagner | '
               'Merchant Services & Passive Income)',
      'url': 'https://www.youtube.com/watch?v=BzCJ4NGRI54&t=412s',
      'video_id': 'BzCJ4NGRI54'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:58](https://www.youtube.com/watch?v=RMbvSJJrPMQ&t=178s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Eventually sell that in a buy out right awesome so Cece sales procom slash '
              "buyout and that's the definitive guide I think you'll really find it helpful "
              'awesome thanks everybody have a great day.',
      'timestamp': 178,
      'timestamp_label': '[00:02:58]',
      'timestamp_seconds': 178,
      'tip': 'Eventually sell that in a buy out right awesome so Cece sales procom slash '
             "buyout and that's the definitive guide I think you'll really find it helpful "
             'awesome thanks everybody have a great day.',
      'title': 'Introduction to Selling Merchant Residuals (CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=RMbvSJJrPMQ&t=178s',
      'video_id': 'RMbvSJJrPMQ'}],
 6: [{'author': 'Joe Wagner | Merchant Services & Passive Income',
      'channel': 'Joe Wagner | Merchant Services & Passive Income',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:09](https://www.youtube.com/watch?v=3FBYq-eEJOk&t=129s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Pillar number four is AI and automation. Business owners don't need more "
              'reports, they need better decisions. Artificial intelligence and auto- mation '
              'are changing how businesses take the data and decide what to do with it all '
              'together.',
      'timestamp': 129,
      'timestamp_label': '[00:02:09]',
      'timestamp_seconds': 129,
      'tip': "Pillar number four is AI and automation. Business owners don't need more "
             'reports, they need better decisions. Artificial intelligence and auto- mation '
             'are changing how businesses take the data and decide what to do with it all '
             'together.',
      'title': 'The Future of Merchant Services: 7 Things Every Payments Sales Agent Must '
               'Understand (Joe Wagner | Merchant Services & Passive Income)',
      'url': 'https://www.youtube.com/watch?v=3FBYq-eEJOk&t=129s',
      'video_id': '3FBYq-eEJOk'},
     {'author': 'PayTrace',
      'channel': 'PayTrace',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:52](https://www.youtube.com/watch?v=5z1bCzU6Luw&t=1792s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "See if I can get my password correct first try. That usually doesn't happen. On "
              'our accounts now, you will see under this account dropdown menu this link that '
              'says enhanced data.',
      'timestamp': 1792,
      'timestamp_label': '[00:29:52]',
      'timestamp_seconds': 1792,
      'tip': "See if I can get my password correct first try. That usually doesn't happen. On "
             'our accounts now, you will see under this account dropdown menu this link that '
             'says enhanced data.',
      'title': 'How to Reduce Your B2B Credit Card Processing Fees with PayTrace Interchange '
               'Optimization and CEDP (PayTrace)',
      'url': 'https://www.youtube.com/watch?v=5z1bCzU6Luw&t=1792s',
      'video_id': '5z1bCzU6Luw'},
     {'author': 'TouchSuite',
      'channel': 'TouchSuite',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:27](https://www.youtube.com/watch?v=mFDxx7C-_EA&t=27s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Second, the lower Product 3 rates, which replaced the old Level 3 rates, only '
              "apply when Visa's checks find your line-item data is real. In mid-April 2026, "
              'Visa retired its Level 2 interchange programs for Business, Corporate, and '
              'Purchasing cards.',
      'timestamp': 27,
      'timestamp_label': '[00:00:27]',
      'timestamp_seconds': 27,
      'tip': 'Second, the lower Product 3 rates, which replaced the old Level 3 rates, only '
             "apply when Visa's checks find your line-item data is real. In mid-April 2026, "
             'Visa retired its Level 2 interchange programs for Business, Corporate, and '
             'Purchasing cards.',
      'title': 'Visa CEDP Explained: Why Level 2 Data No Longer Lowers B2B Card Rates '
               '(TouchSuite)',
      'url': 'https://www.youtube.com/watch?v=mFDxx7C-_EA&t=27s',
      'video_id': 'mFDxx7C-_EA'},
     {'author': 'Austin Zaback',
      'channel': 'Austin Zaback',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=DFSahEAw3uY&t=15s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The ATM business now as you can tell we have a couple of ATMs here ok so we '
              'have 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'The ATM business now as you can tell we have a couple of ATMs here ok so we have '
             '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17.',
      'title': 'How To Find And Secure ATM Contracts/Locations (Step By Step) (Austin Zaback)',
      'url': 'https://www.youtube.com/watch?v=DFSahEAw3uY&t=15s',
      'video_id': 'DFSahEAw3uY'},
     {'author': 'NMI',
      'channel': 'NMI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=WxBDVPgeUYI&t=33s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re actively being billed, everything's in good standing with the account. Now, "
              'at the top, we want to put accounts that are in a status that you may want to '
              'know about, that you may want to notice first and foremost.',
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': "'re actively being billed, everything's in good standing with the account. Now, "
             'at the top, we want to put accounts that are in a status that you may want to '
             'know about, that you may want to notice first and foremost.',
      'title': 'Merchant Account Statuses Explained | NMI Payment Gateway Guide (NMI)',
      'url': 'https://www.youtube.com/watch?v=WxBDVPgeUYI&t=33s',
      'video_id': 'WxBDVPgeUYI'},
     {'author': 'Juan Jeronimo',
      'channel': 'Juan Jeronimo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:00](https://www.youtube.com/watch?v=2iQEC3gV3oo&t=300s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "In the next video, I'm going to show you guys exactly how to find profitable "
              "ATM locations step-by-step, because that's the part that actually makes or "
              'breaks your business.',
      'timestamp': 300,
      'timestamp_label': '[00:05:00]',
      'timestamp_seconds': 300,
      'tip': "In the next video, I'm going to show you guys exactly how to find profitable ATM "
             "locations step-by-step, because that's the part that actually makes or breaks "
             'your business.',
      'title': 'How Much Does It Cost to Start an ATM Business (Full Breakdown) (Juan '
               'Jeronimo)',
      'url': 'https://www.youtube.com/watch?v=2iQEC3gV3oo&t=300s',
      'video_id': '2iQEC3gV3oo'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:34:26](https://www.youtube.com/watch?v=KlaksrooZhw&t=2066s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And the beauty of this, too, also, by the way, is the first 30 days will double '
              'that initial qualified bonus, qualified lead bonus. So, you can make a a good '
              "chunk of change. Well, that's just one Those are the two ways. Well, the third "
              "way is there's a rev share.",
      'timestamp': 2066,
      'timestamp_label': '[00:34:26]',
      'timestamp_seconds': 2066,
      'tip': 'And the beauty of this, too, also, by the way, is the first 30 days will double '
             'that initial qualified bonus, qualified lead bonus. So, you can make a a good '
             "chunk of change. Well, that's just one Those are the two ways. Well, the third "
             "way is there's a rev share.",
      'title': 'The Future of Interchange Optimization (CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=KlaksrooZhw&t=2066s',
      'video_id': 'KlaksrooZhw'},
     {'author': 'Electronic Money Company',
      'channel': 'Electronic Money Company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=kIPaI-A_dCM&t=78s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We do not want to surprise our merchants when they get their first statement '
              'with some hidden fees showing up. This is not the right way to treat anyone, '
              'much less keep a client for the lifetime of their business.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'We do not want to surprise our merchants when they get their first statement '
             'with some hidden fees showing up. This is not the right way to treat anyone, '
             'much less keep a client for the lifetime of their business.',
      'title': 'How to Build Lifetime Residual Income Selling Merchant Services — No Hard '
               'Closing Required (Electronic Money Company)',
      'url': 'https://www.youtube.com/watch?v=kIPaI-A_dCM&t=78s',
      'video_id': 'kIPaI-A_dCM'},
     {'author': 'Philip Webb',
      'channel': 'Philip Webb',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:50](https://www.youtube.com/watch?v=c9guz0-WUZQ&t=170s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's get back to the video Point number three a contract the SLA the agreement "
              'this is where you guys in ATM world you got to cut your best deal right off '
              'the.',
      'timestamp': 170,
      'timestamp_label': '[00:02:50]',
      'timestamp_seconds': 170,
      'tip': "Let's get back to the video Point number three a contract the SLA the agreement "
             'this is where you guys in ATM world you got to cut your best deal right off the.',
      'title': 'The 5 best ways on how to handle your ATM contracts in a location (Philip '
               'Webb)',
      'url': 'https://www.youtube.com/watch?v=c9guz0-WUZQ&t=170s',
      'video_id': 'c9guz0-WUZQ'},
     {'author': 'O3 Merchant Services',
      'channel': 'O3 Merchant Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:27](https://www.youtube.com/watch?v=y6h2-zKFtQ0&t=27s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Traditional credit card pricing model versus the new dual pricing model so the '
              'first thing I want to get into is traditional credit card pricing models.',
      'timestamp': 27,
      'timestamp_label': '[00:00:27]',
      'timestamp_seconds': 27,
      'tip': 'Traditional credit card pricing model versus the new dual pricing model so the '
             'first thing I want to get into is traditional credit card pricing models.',
      'title': 'Traditional Credit Card Pricing vs. Dual Pricing: Which One to Choose For Your '
               'Business (O3 Merchant Services)',
      'url': 'https://www.youtube.com/watch?v=y6h2-zKFtQ0&t=27s',
      'video_id': 'y6h2-zKFtQ0'},
     {'author': 'Taxes & Side Hustles',
      'channel': 'Taxes & Side Hustles',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=SEPDFZSU8Ps&t=111s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Then the first of the month because that's when people are getting their checks "
              "so Friday's hurry first of the month or around tax season time.",
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': "Then the first of the month because that's when people are getting their checks "
             "so Friday's hurry first of the month or around tax season time.",
      'title': 'How to Negotiate an ATM Contract (Taxes & Side Hustles)',
      'url': 'https://www.youtube.com/watch?v=SEPDFZSU8Ps&t=111s',
      'video_id': 'SEPDFZSU8Ps'},
     {'author': 'Practical Ecommerce',
      'channel': 'Practical Ecommerce',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:59](https://www.youtube.com/watch?v=LjfmC9EATic&t=779s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I I find that fascinating and I I talk to some of the big gateways and what's "
              'happening right now is the providers of online pin debit are going directly to '
              "Merchants you are correct and they're bypassing gateways like authorized.",
      'timestamp': 779,
      'timestamp_label': '[00:12:59]',
      'timestamp_seconds': 779,
      'tip': "I I find that fascinating and I I talk to some of the big gateways and what's "
             'happening right now is the providers of online pin debit are going directly to '
             "Merchants you are correct and they're bypassing gateways like authorized.",
      'title': 'Credit Card Exec On Durbin Amendment, New Debit Card Rates (Practical '
               'Ecommerce)',
      'url': 'https://www.youtube.com/watch?v=LjfmC9EATic&t=779s',
      'video_id': 'LjfmC9EATic'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=ruAqtp4NcPA&t=103s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In the last video, we talked about there is two important things in determining '
              'how profitable an account is going to be. The first one is what size account '
              'are you going after? We didn’t talk about the second one. The second one is '
              'what about your cost structure?',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': 'In the last video, we talked about there is two important things in determining '
             'how profitable an account is going to be. The first one is what size account are '
             'you going after? We didn’t talk about the second one. The second one is what '
             'about your cost structure?',
      'title': 'How Much Residual Can You Make Selling Merchant Services? (CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=ruAqtp4NcPA&t=103s',
      'video_id': 'ruAqtp4NcPA'},
     {'author': 'Scott E. Adams | Chargeback Expert',
      'channel': 'Scott E. Adams | Chargeback Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:34](https://www.youtube.com/watch?v=gJ_2exzq6FA&t=214s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Did we get a charge back and or a fraud flag transaction so this tells us but '
              "yeah so we think it's great it's something that most Merchants should use it's "
              'generally inexpensive um so hopefully that helps let us know if you have '
              'questions and thanks a lot.',
      'timestamp': 214,
      'timestamp_label': '[00:03:34]',
      'timestamp_seconds': 214,
      'tip': 'Did we get a charge back and or a fraud flag transaction so this tells us but '
             "yeah so we think it's great it's something that most Merchants should use it's "
             'generally inexpensive um so hopefully that helps let us know if you have '
             'questions and thanks a lot.',
      'title': 'Verifi Inform - Visa TC40, Visa TC15, Visa Fraud and Chargeback Data all in '
               'Real Time (Scott E. Adams | Chargeback Expert)',
      'url': 'https://www.youtube.com/watch?v=gJ_2exzq6FA&t=214s',
      'video_id': 'gJ_2exzq6FA'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:10](https://www.youtube.com/watch?v=KFKUpD0sDxk&t=370s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Background basically yep exactly so long story short if you already have a '
              'company fantastic you know go try them out if not go to ccsalespro.com click on '
              "find a processor and you know I'll help you out there all right perfect.",
      'timestamp': 370,
      'timestamp_label': '[00:06:10]',
      'timestamp_seconds': 370,
      'tip': 'Background basically yep exactly so long story short if you already have a '
             'company fantastic you know go try them out if not go to ccsalespro.com click on '
             "find a processor and you know I'll help you out there all right perfect.",
      'title': 'How Do I Become My Own ISO? (CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=KFKUpD0sDxk&t=370s',
      'video_id': 'KFKUpD0sDxk'}],
 7: [{'author': 'ATMDepot - Make Money with ATM Machines',
      'channel': 'ATMDepot - Make Money with ATM Machines',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:20](https://www.youtube.com/watch?v=ETBd5FI2JHY&t=200s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Triton 9600, Gene Mega G1900, Hyioong 1800 CE, Tranax, most old bank ATMs. '
              "These might be too old, too bulky, or not upgradeable. If you're serious about "
              'starting an ATM business, take your time and make informed decisions.',
      'timestamp': 200,
      'timestamp_label': '[00:03:20]',
      'timestamp_seconds': 200,
      'tip': 'Triton 9600, Gene Mega G1900, Hyioong 1800 CE, Tranax, most old bank ATMs. These '
             "might be too old, too bulky, or not upgradeable. If you're serious about "
             'starting an ATM business, take your time and make informed decisions.',
      'title': 'Where to Buy an ATM Machine (Without Getting Scammed) (ATMDepot - Make Money '
               'with ATM Machines)',
      'url': 'https://www.youtube.com/watch?v=ETBd5FI2JHY&t=200s',
      'video_id': 'ETBd5FI2JHY'},
     {'author': 'ATM Connect',
      'channel': 'ATM Connect',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:40](https://www.youtube.com/watch?v=kXEFZM-F90k&t=460s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Portal a video showing a step-by-step process of how to start the ATM business '
              "you should ask yourself if their ATM business was so profitable why they're.",
      'timestamp': 460,
      'timestamp_label': '[00:07:40]',
      'timestamp_seconds': 460,
      'tip': 'Portal a video showing a step-by-step process of how to start the ATM business '
             "you should ask yourself if their ATM business was so profitable why they're.",
      'title': 'Avoid ATM Automation Packages!!! (ATM Connect)',
      'url': 'https://www.youtube.com/watch?v=kXEFZM-F90k&t=460s',
      'video_id': 'kXEFZM-F90k'},
     {'author': 'Philip Webb',
      'channel': 'Philip Webb',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:50](https://www.youtube.com/watch?v=6k0qIHsvs0M&t=470s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Business and don't forget pdq merch enterprises we sell atms we process "
              "transactions and we sell parts so we can help you in your atm journey and don't "
              'forget I will see you over at the atm mastermind group page.',
      'timestamp': 470,
      'timestamp_label': '[00:07:50]',
      'timestamp_seconds': 470,
      'tip': "Business and don't forget pdq merch enterprises we sell atms we process "
             "transactions and we sell parts so we can help you in your atm journey and don't "
             'forget I will see you over at the atm mastermind group page.',
      'title': 'Atm Cash Vault Services -  Top 5 things you should know before you get a '
               'vaulter for your ATM (Philip Webb)',
      'url': 'https://www.youtube.com/watch?v=6k0qIHsvs0M&t=470s',
      'video_id': '6k0qIHsvs0M'},
     {'author': 'Velocity Merchant Services - VMS',
      'channel': 'Velocity Merchant Services - VMS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:02](https://www.youtube.com/watch?v=uBEewd90EL8&t=122s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Whatever they were buying since the cashless ATM is integrated straight with '
              'your POS system the actual money is still going straight to the business.',
      'timestamp': 122,
      'timestamp_label': '[00:02:02]',
      'timestamp_seconds': 122,
      'tip': 'Whatever they were buying since the cashless ATM is integrated straight with '
             'your POS system the actual money is still going straight to the business.',
      'title': 'Cannabis dispensary owners guide to Cashless ATMs and Point of Banking '
               '(Velocity Merchant Services - VMS)',
      'url': 'https://www.youtube.com/watch?v=uBEewd90EL8&t=122s',
      'video_id': 'uBEewd90EL8'},
     {'author': 'Chad Otsuji ATM Business',
      'channel': 'Chad Otsuji ATM Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:06](https://www.youtube.com/watch?v=6zaxeyp07Zg&t=186s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Your atm business and you haven't yet make sure you go ahead and click on this "
              "video right here because I'm going to explain all of the steps to starting your "
              "atm business that's all for this video guys I'll see you in the next one peace.",
      'timestamp': 186,
      'timestamp_label': '[00:03:06]',
      'timestamp_seconds': 186,
      'tip': "Your atm business and you haven't yet make sure you go ahead and click on this "
             "video right here because I'm going to explain all of the steps to starting your "
             "atm business that's all for this video guys I'll see you in the next one peace.",
      'title': 'Buy this ATM machine NOW! (Chad Otsuji ATM Business)',
      'url': 'https://www.youtube.com/watch?v=6zaxeyp07Zg&t=186s',
      'video_id': '6zaxeyp07Zg'},
     {'author': 'Joe Wagner | Merchant Services & Passive Income',
      'channel': 'Joe Wagner | Merchant Services & Passive Income',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=6dCPtuCCcvw&t=50s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Available for their business independent sales organizations isos offer '
              'personalized Services they manage Merchant accounts providing tailored '
              'Solutions without process in payments themselves.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': 'Available for their business independent sales organizations isos offer '
             'personalized Services they manage Merchant accounts providing tailored Solutions '
             'without process in payments themselves.',
      'title': 'The Merchant Services Industry Explained (Agents, ISOs, & Income) (Joe Wagner '
               '| Merchant Services & Passive Income)',
      'url': 'https://www.youtube.com/watch?v=6dCPtuCCcvw&t=50s',
      'video_id': '6dCPtuCCcvw'},
     {'author': 'Ryan Anthony',
      'channel': 'Ryan Anthony',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=RF6l5ilPKQ0&t=75s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Math now the reason I put do the math is the first step in the process is '
              'because it takes some figuring in your brain before you decide to stop trading '
              'your.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': 'Math now the reason I put do the math is the first step in the process is '
             'because it takes some figuring in your brain before you decide to stop trading '
             'your.',
      'title': 'How to Start a Credit Card Processing Business | Residual Income with Merchant '
               'Services (Ryan Anthony)',
      'url': 'https://www.youtube.com/watch?v=RF6l5ilPKQ0&t=75s',
      'video_id': 'RF6l5ilPKQ0'},
     {'author': 'News24',
      'channel': 'News24',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=AE1F8LcgZ98&t=71s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The tax officer saying no, a different set of rules apply to us. Now, tenants, '
              "too, are facing a squeeze. Macquarie Bank's deft payment system, which "
              'processes more than a million rent payments a month, has also blocked credit '
              'card payments.',
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': 'The tax officer saying no, a different set of rules apply to us. Now, tenants, '
             "too, are facing a squeeze. Macquarie Bank's deft payment system, which processes "
             'more than a million rent payments a month, has also blocked credit card '
             'payments.',
      'title': '‘Unintended consequences’: Labor’s credit card surcharge ban sparks backlash '
               '(News24)',
      'url': 'https://www.youtube.com/watch?v=AE1F8LcgZ98&t=71s',
      'video_id': 'AE1F8LcgZ98'},
     {'author': 'nexio',
      'channel': 'nexio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:04](https://www.youtube.com/watch?v=wCnscoBFCKc&t=184s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So next let's cover the registration process number one you're going to need to "
              'choose a payment processor the first step is to identify a suitable payment.',
      'timestamp': 184,
      'timestamp_label': '[00:03:04]',
      'timestamp_seconds': 184,
      'tip': "So next let's cover the registration process number one you're going to need to "
             'choose a payment processor the first step is to identify a suitable payment.',
      'title': 'Integrated Payments: Wholesale ISO Overview for Vertical Software Companies '
               '(nexio)',
      'url': 'https://www.youtube.com/watch?v=wCnscoBFCKc&t=184s',
      'video_id': 'wCnscoBFCKc'},
     {'author': 'Scott Shaw',
      'channel': 'Scott Shaw',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:20](https://www.youtube.com/watch?v=wOJ4s_5GRDY&t=140s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Support to deployment underwriting and risk we will even mask our call centers '
              'to support the building of your individual.',
      'timestamp': 140,
      'timestamp_label': '[00:02:20]',
      'timestamp_seconds': 140,
      'tip': 'Support to deployment underwriting and risk we will even mask our call centers '
             'to support the building of your individual.',
      'title': 'Become a Registered ISO for Merchant Services - How to Start Your Own Payment '
               'Processing Company (Scott Shaw)',
      'url': 'https://www.youtube.com/watch?v=wOJ4s_5GRDY&t=140s',
      'video_id': 'wOJ4s_5GRDY'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:47](https://www.youtube.com/watch?v=2Sn4XMqpW4I&t=347s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The same goes for the processor. They may be marking up and keeping some of '
              'that money to pay for their building rent, to pay for their support system etc. '
              'Okay, now we’re going to do the same thing with the mark-up that we did with '
              'the interchange.',
      'timestamp': 347,
      'timestamp_label': '[00:05:47]',
      'timestamp_seconds': 347,
      'tip': 'The same goes for the processor. They may be marking up and keeping some of that '
             'money to pay for their building rent, to pay for their support system etc. Okay, '
             'now we’re going to do the same thing with the mark-up that we did with the '
             'interchange.',
      'title': 'What is Interchange Plus or Cost Plus Pricing - Merchant Services (CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=2Sn4XMqpW4I&t=347s',
      'video_id': '2Sn4XMqpW4I'},
     {'author': 'Verifi, A Visa Solution',
      'channel': 'Verifi, A Visa Solution',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=0mvbNuyEem8&t=115s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Record their action and verify one indicating the outcome reason and simply hit '
              'submit Merchants can gain control of disputes using verifies car diagnostic '
              'cdrn solution offering pre-dispute resolution Services all in a single easy to '
              'ous online portal.',
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': 'Record their action and verify one indicating the outcome reason and simply hit '
             'submit Merchants can gain control of disputes using verifies car diagnostic cdrn '
             'solution offering pre-dispute resolution Services all in a single easy to ous '
             'online portal.',
      'title': 'Verifi Explainer | RESOLVE Solution: CDRN Walkthrough (Verifi, A Visa '
               'Solution)',
      'url': 'https://www.youtube.com/watch?v=0mvbNuyEem8&t=115s',
      'video_id': '0mvbNuyEem8'},
     {'author': 'Joe Wagner | Merchant Services & Passive Income',
      'channel': 'Joe Wagner | Merchant Services & Passive Income',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:44](https://www.youtube.com/watch?v=KRZuPsngOLw&t=284s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Three show them that's basically how easy this is you've been seeing it for "
              'years now we want to implement it in your business step four here let me show '
              "you now if they're at the same point.",
      'timestamp': 284,
      'timestamp_label': '[00:04:44]',
      'timestamp_seconds': 284,
      'tip': "Three show them that's basically how easy this is you've been seeing it for "
             'years now we want to implement it in your business step four here let me show '
             "you now if they're at the same point.",
      'title': 'How to Present Cash Discounting Without Confusing the Merchant (Joe Wagner | '
               'Merchant Services & Passive Income)',
      'url': 'https://www.youtube.com/watch?v=KRZuPsngOLw&t=284s',
      'video_id': 'KRZuPsngOLw'},
     {'author': 'Electronic Money Company',
      'channel': 'Electronic Money Company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=4LJj9o_IDnQ&t=118s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They have never heard from their salesperson since they signed up, and they '
              'want a relationship with someone to assist them should their system go down. '
              "They're unhappy with Clover support.",
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': 'They have never heard from their salesperson since they signed up, and they want '
             "a relationship with someone to assist them should their system go down. They're "
             'unhappy with Clover support.',
      'title': 'Merchant Services Sales Training The Real Reasons Businesses Switch Processors '
               '(Electronic Money Company)',
      'url': 'https://www.youtube.com/watch?v=4LJj9o_IDnQ&t=118s',
      'video_id': '4LJj9o_IDnQ'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:24](https://www.youtube.com/watch?v=tG2nIK3Th4Q&t=1524s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're not james all you're doing is selling price and again there are some "
              'players out there in the b2b space that you know believe that.',
      'timestamp': 1524,
      'timestamp_label': '[00:25:24]',
      'timestamp_seconds': 1524,
      'tip': "You're not james all you're doing is selling price and again there are some "
             'players out there in the b2b space that you know believe that.',
      'title': 'Get the Inside Scoop on Level 2 & 3 Interchange Optimization (CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=tG2nIK3Th4Q&t=1524s',
      'video_id': 'tG2nIK3Th4Q'}],
 8: [{'author': 'Lines & Gains',
      'channel': 'Lines & Gains',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:35](https://www.youtube.com/watch?v=-6VRYcYBnSA&t=455s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '15,000 in crisp $20 bills every Thursday morning. Their automated anti-money '
              'laundering software will flag your account as a high-risk money services '
              'business and close your accounts without warning.',
      'timestamp': 455,
      'timestamp_label': '[00:07:35]',
      'timestamp_seconds': 455,
      'tip': '15,000 in crisp $20 bills every Thursday morning. Their automated anti-money '
             'laundering software will flag your account as a high-risk money services '
             'business and close your accounts without warning.',
      'title': 'I Analyzed the Real Math of Owning 10 ATMs in America (2026 Profit Breakdown) '
               '(Lines & Gains)',
      'url': 'https://www.youtube.com/watch?v=-6VRYcYBnSA&t=455s',
      'video_id': '-6VRYcYBnSA'},
     {'author': 'All Things Money',
      'channel': 'All Things Money',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=F87ku5Df-mA&t=120s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'US bank card acceptance market. They claim that the amendment has saved '
              'consumers money, created jobs, and increased the availability of free checking '
              'accounts.',
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': 'US bank card acceptance market. They claim that the amendment has saved '
             'consumers money, created jobs, and increased the availability of free checking '
             'accounts.',
      'title': 'The Debit Card Battle Over the Durbin Amendment: How It Affects Consumers and '
               'Businesses (All Things Money)',
      'url': 'https://www.youtube.com/watch?v=F87ku5Df-mA&t=120s',
      'video_id': 'F87ku5Df-mA'},
     {'author': 'High-Risk Merchant Accounts | Adaptiv Payments',
      'channel': 'High-Risk Merchant Accounts | Adaptiv Payments',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:38](https://www.youtube.com/watch?v=NdTgGwtE_N4&t=278s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "A falling ratio with a clear plan behind it shows a bank you're in control. "
              'Adaptiv Payments sets up high-risk merchant accounts with chargeback alerts, '
              'RDR and fraud tools, and helps you answer the disputes worth fighting. The '
              "link's in the description.",
      'timestamp': 278,
      'timestamp_label': '[00:04:38]',
      'timestamp_seconds': 278,
      'tip': "A falling ratio with a clear plan behind it shows a bank you're in control. "
             'Adaptiv Payments sets up high-risk merchant accounts with chargeback alerts, RDR '
             "and fraud tools, and helps you answer the disputes worth fighting. The link's in "
             'the description.',
      'title': 'Chargeback Prevention: How to Stop Chargebacks and Keep Your Merchant Account '
               '(2026) (High-Risk Merchant Accounts | Adaptiv Payments)',
      'url': 'https://www.youtube.com/watch?v=NdTgGwtE_N4&t=278s',
      'video_id': 'NdTgGwtE_N4'},
     {'author': 'money guy 2.0',
      'channel': 'money guy 2.0',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:36](https://www.youtube.com/watch?v=hulU30cthAs&t=456s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, now let's talk about something even more dangerous, The scams hiding inside "
              'this industry. Because this business has become a magnet for shady investment '
              "schemes. You've probably seen the ads. Buy an ATM, place it, and earn passive "
              'income for life.',
      'timestamp': 456,
      'timestamp_label': '[00:07:36]',
      'timestamp_seconds': 456,
      'tip': "So, now let's talk about something even more dangerous, The scams hiding inside "
             'this industry. Because this business has become a magnet for shady investment '
             "schemes. You've probably seen the ads. Buy an ATM, place it, and earn passive "
             'income for life.',
      'title': 'The Economics of Owning ATM Machines | Costs, Surcharge Profits & ROI (money '
               'guy 2.0)',
      'url': 'https://www.youtube.com/watch?v=hulU30cthAs&t=456s',
      'video_id': 'hulU30cthAs'},
     {'author': 'Philip Webb',
      'channel': 'Philip Webb',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=kbluVa_rgsM&t=15s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "What to look for when you buy an atm location agreement hi i'm phil from pdq "
              'merch enterprises and the atm mastermind group page and we help hundreds of.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "What to look for when you buy an atm location agreement hi i'm phil from pdq "
             'merch enterprises and the atm mastermind group page and we help hundreds of.',
      'title': 'What To Look For When Buying An ATM Location Agreement - ATM Business 2021 '
               '(Philip Webb)',
      'url': 'https://www.youtube.com/watch?v=kbluVa_rgsM&t=15s',
      'video_id': 'kbluVa_rgsM'},
     {'author': 'BancardSales',
      'channel': 'BancardSales',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:56](https://www.youtube.com/watch?v=AseZioaNb5s&t=116s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Credit card data is when it's sent from the processor or the point-of-sale "
              'device over to the bank for approval and back again the top level security for.',
      'timestamp': 116,
      'timestamp_label': '[00:01:56]',
      'timestamp_seconds': 116,
      'tip': "Credit card data is when it's sent from the processor or the point-of-sale "
             'device over to the bank for approval and back again the top level security for.',
      'title': "Merchant Account Pricing -  What Is Interchange - Fees, Rates and Why it's "
               'important to you! (BancardSales)',
      'url': 'https://www.youtube.com/watch?v=AseZioaNb5s&t=116s',
      'video_id': 'AseZioaNb5s'},
     {'author': 'TouchSuite',
      'channel': 'TouchSuite',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=60QTYm0QFZU&t=64s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sometimes the fields exist in your software but are optional, turned off by '
              'default, or not mapped in the integration. Here is a hypothetical business, and '
              'these numbers are made up for illustration.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': 'Sometimes the fields exist in your software but are optional, turned off by '
             'default, or not mapped in the integration. Here is a hypothetical business, and '
             'these numbers are made up for illustration.',
      'title': 'Level 2 and Level 3 Card Data: Estimate the Business Card Impact (TouchSuite)',
      'url': 'https://www.youtube.com/watch?v=60QTYm0QFZU&t=64s',
      'video_id': '60QTYm0QFZU'},
     {'author': 'Nuvei',
      'channel': 'Nuvei',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:01](https://www.youtube.com/watch?v=bBQUixWA9qA&t=121s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Misunderstandings sear chargings can be a useful tool for merchants but it's "
              'important to use it responsibly and transparently by understanding the ins and '
              'outs of sear charging you can make informed decisions that benefit both your '
              'business and your customers.',
      'timestamp': 121,
      'timestamp_label': '[00:02:01]',
      'timestamp_seconds': 121,
      'tip': "Misunderstandings sear chargings can be a useful tool for merchants but it's "
             'important to use it responsibly and transparently by understanding the ins and '
             'outs of sear charging you can make informed decisions that benefit both your '
             'business and your customers.',
      'title': 'What is surcharging? Credit card surcharge rules explained (Nuvei)',
      'url': 'https://www.youtube.com/watch?v=bBQUixWA9qA&t=121s',
      'video_id': 'bBQUixWA9qA'},
     {'author': 'Transaction Expert',
      'channel': 'Transaction Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:00](https://www.youtube.com/watch?v=cL-wn0WX_PA&t=360s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In your area come out and present a cost analysis to you help you understand '
              'your statement better and show you how we can save you money because of the '
              'Duran Amendment.',
      'timestamp': 360,
      'timestamp_label': '[00:06:00]',
      'timestamp_seconds': 360,
      'tip': 'In your area come out and present a cost analysis to you help you understand '
             'your statement better and show you how we can save you money because of the '
             'Duran Amendment.',
      'title': 'What is the Durbin Amendment? (Transaction Expert)',
      'url': 'https://www.youtube.com/watch?v=cL-wn0WX_PA&t=360s',
      'video_id': 'cL-wn0WX_PA'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:52](https://www.youtube.com/watch?v=RxgrRsVThx4&t=172s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Well, there is a couple ways. The easiest way is this: If you’re a physical '
              'location business, you know you’re a retailor, restaurant, auto repair shop, '
              'really you should see 70%, 60 to 70% of your transactions should be qualified.',
      'timestamp': 172,
      'timestamp_label': '[00:02:52]',
      'timestamp_seconds': 172,
      'tip': 'Well, there is a couple ways. The easiest way is this: If you’re a physical '
             'location business, you know you’re a retailor, restaurant, auto repair shop, '
             'really you should see 70%, 60 to 70% of your transactions should be qualified.',
      'title': 'How to Read a Merchant Statement   Tier Pricing (CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=RxgrRsVThx4&t=172s',
      'video_id': 'RxgrRsVThx4'},
     {'author': 'ATM Connect',
      'channel': 'ATM Connect',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=ujDLOkqXvfg&t=120s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'What the denomination that cassette has so this is useful to in case you need '
              "you need it so these these keys are for the cassette which I'm going to open "
              'and show you and these these keys are for the chest storm for the top part of '
              "the ATM which I'm going to open.",
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': 'What the denomination that cassette has so this is useful to in case you need '
             "you need it so these these keys are for the cassette which I'm going to open and "
             'show you and these these keys are for the chest storm for the top part of the '
             "ATM which I'm going to open.",
      'title': 'How to unbox a new ATM (Genmega) | ATM Business (ATM Connect)',
      'url': 'https://www.youtube.com/watch?v=ujDLOkqXvfg&t=120s',
      'video_id': 'ujDLOkqXvfg'},
     {'author': 'Scott Shaw',
      'channel': 'Scott Shaw',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:15](https://www.youtube.com/watch?v=dvdrcApxBHo&t=135s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Unparalleled Merchant benefits unrivaled income generation potential to novel '
              'sales tools partnering with us is the smartest move you will make for more '
              'information or to partner with us please visit our website at Sharp '
              'merchantgroup.com foreign.',
      'timestamp': 135,
      'timestamp_label': '[00:02:15]',
      'timestamp_seconds': 135,
      'tip': 'Unparalleled Merchant benefits unrivaled income generation potential to novel '
             'sales tools partnering with us is the smartest move you will make for more '
             'information or to partner with us please visit our website at Sharp '
             'merchantgroup.com foreign.',
      'title': 'Merchant Services ISO Agent - Selling Payment Processing - Become a Credit '
               'Card Processing Agent (Scott Shaw)',
      'url': 'https://www.youtube.com/watch?v=dvdrcApxBHo&t=135s',
      'video_id': 'dvdrcApxBHo'},
     {'author': 'Verifi, A Visa Solution',
      'channel': 'Verifi, A Visa Solution',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:37](https://www.youtube.com/watch?v=84OsVYhwoxY&t=97s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Built in-house every tool that we have we've created on our own with our "
              'sellers as our customers and their voice contributing to the design and the '
              "conception of each of our solutions but we've built them all we are the "
              'innovator in the space.',
      'timestamp': 97,
      'timestamp_label': '[00:01:37]',
      'timestamp_seconds': 97,
      'tip': "Built in-house every tool that we have we've created on our own with our sellers "
             'as our customers and their voice contributing to the design and the conception '
             "of each of our solutions but we've built them all we are the innovator in the "
             'space.',
      'title': 'Verifi Explainer Series | RECOVER Solution: Managed Chargeback Representment '
               'for Sellers (Verifi, A Visa Solution)',
      'url': 'https://www.youtube.com/watch?v=84OsVYhwoxY&t=97s',
      'video_id': '84OsVYhwoxY'},
     {'author': 'Philip Webb',
      'channel': 'Philip Webb',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:30](https://www.youtube.com/watch?v=YgQxm2IWnKw&t=330s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Not what we want to do point number two is we got an ATM business for financial '
              "freedom what does that mean it's just a little extra money a little side "
              'hustle.',
      'timestamp': 330,
      'timestamp_label': '[00:05:30]',
      'timestamp_seconds': 330,
      'tip': 'Not what we want to do point number two is we got an ATM business for financial '
             "freedom what does that mean it's just a little extra money a little side hustle.",
      'title': 'Should you Become A Vault Casher? - ATM Business 2020 (Philip Webb)',
      'url': 'https://www.youtube.com/watch?v=YgQxm2IWnKw&t=330s',
      'video_id': 'YgQxm2IWnKw'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=fb0PHmE8aCc&t=15s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Okay so i wanted to ask you the question about the um what pricing type i can '
              'make more money um being independent foreigner because i.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Okay so i wanted to ask you the question about the um what pricing type i can '
             'make more money um being independent foreigner because i.',
      'title': 'Choosing The Right Pricing Structure: Tiered Pricing VS. Interchange Plus '
               '(CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=fb0PHmE8aCc&t=15s',
      'video_id': 'fb0PHmE8aCc'}],
 9: [{'author': 'Georges Rayess',
      'channel': 'Georges Rayess',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=gH8-LQ4srZY&t=118s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The trade-off, RDR auto refunds disputes you might have won in representment, '
              'so you calibrate the rules to your reason mix. ETHA has no fully equivalent '
              "automatic product yet. Mastercard has said it's building one, but today Ethica "
              'is still alert and respond.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': 'The trade-off, RDR auto refunds disputes you might have won in representment, so '
             'you calibrate the rules to your reason mix. ETHA has no fully equivalent '
             "automatic product yet. Mastercard has said it's building one, but today Ethica "
             'is still alert and respond.',
      'title': 'Ethoca vs Verifi: The Two Dispute-Interception Networks Every Subscription App '
               'Needs (Georges Rayess)',
      'url': 'https://www.youtube.com/watch?v=gH8-LQ4srZY&t=118s',
      'video_id': 'gH8-LQ4srZY'},
     {'author': 'Chad Otsuji ATM Business',
      'channel': 'Chad Otsuji ATM Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:09](https://www.youtube.com/watch?v=pxCV1SkPnK4&t=429s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So I could sell this contract for possibly $10,000 you know I could sell it '
              'next month and get 10k right to my bank account now that you cannot do if.',
      'timestamp': 429,
      'timestamp_label': '[00:07:09]',
      'timestamp_seconds': 429,
      'tip': 'So I could sell this contract for possibly $10,000 you know I could sell it next '
             'month and get 10k right to my bank account now that you cannot do if.',
      'title': 'How To Find Locations For ATM Business (Passive Income) (Chad Otsuji ATM '
               'Business)',
      'url': 'https://www.youtube.com/watch?v=pxCV1SkPnK4&t=429s',
      'video_id': 'pxCV1SkPnK4'},
     {'author': 'POS Nexus',
      'channel': 'POS Nexus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=ZAtYPaS2xkA&t=104s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So who does dual pricing suit? Businesses with a manageable number of prices, a '
              "capable POS, and customers who still pay cash. It's a poor fit for large or "
              'fast-changing catalogs, or where almost nobody pays cash. And state rules vary '
              'and change often.',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': 'So who does dual pricing suit? Businesses with a manageable number of prices, a '
             "capable POS, and customers who still pay cash. It's a poor fit for large or "
             'fast-changing catalogs, or where almost nobody pays cash. And state rules vary '
             'and change often.',
      'title': 'Dual Pricing vs Cash Discount: Is "Zero-Fee" Processing Legal? (POS Nexus)',
      'url': 'https://www.youtube.com/watch?v=ZAtYPaS2xkA&t=104s',
      'video_id': 'ZAtYPaS2xkA'},
     {'author': 'WKYC Channel 3',
      'channel': 'WKYC Channel 3',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=AGTRnXUImOw&t=38s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Visa and Mastercard set limits on these fees, capping. Them at 3 or 4% of the '
              'sale. Those card company limits are rules that businesses agree to in order to '
              "be able to take those cards, but they're not the law.",
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': 'Visa and Mastercard set limits on these fees, capping. Them at 3 or 4% of the '
             'sale. Those card company limits are rules that businesses agree to in order to '
             "be able to take those cards, but they're not the law.",
      'title': 'Are surcharges and convenience charges legal on debit card transactions? (WKYC '
               'Channel 3)',
      'url': 'https://www.youtube.com/watch?v=AGTRnXUImOw&t=38s',
      'video_id': 'AGTRnXUImOw'},
     {'author': 'durbinamendment',
      'channel': 'durbinamendment',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:44](https://www.youtube.com/watch?v=_5A2a4Vu7A8&t=464s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Though the bank is required by law to pass those savings on the processor okay '
              'so what does that mean for you as a business it means that if you were on.',
      'timestamp': 464,
      'timestamp_label': '[00:07:44]',
      'timestamp_seconds': 464,
      'tip': 'Though the bank is required by law to pass those savings on the processor okay '
             'so what does that mean for you as a business it means that if you were on.',
      'title': 'What is the Durbin Amendment and how does it effect small business? '
               '(durbinamendment)',
      'url': 'https://www.youtube.com/watch?v=_5A2a4Vu7A8&t=464s',
      'video_id': '_5A2a4Vu7A8'},
     {'author': 'PaymentCloud',
      'channel': 'PaymentCloud',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=xfBalp9Zzio&t=52s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So now let's break down the key components of a merchant state. Is your "
              'merchant ID number or mid for short and contact information? Your Mid is your '
              "business's unique identifier. Think of it as your merchant account's lifeline.",
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': "So now let's break down the key components of a merchant state. Is your merchant "
             "ID number or mid for short and contact information? Your Mid is your business's "
             "unique identifier. Think of it as your merchant account's lifeline.",
      'title': 'Understanding Your Merchant Statement: Everything They Don’t Want You To Know '
               '(PaymentCloud)',
      'url': 'https://www.youtube.com/watch?v=xfBalp9Zzio&t=52s',
      'video_id': 'xfBalp9Zzio'},
     {'author': 'Joe Wagner | Merchant Services & Passive Income',
      'channel': 'Joe Wagner | Merchant Services & Passive Income',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:53](https://www.youtube.com/watch?v=Em1hM53SuTA&t=233s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, after more than 16 years in merchant services, this is one lesson I wish '
              "every new agent understood before signing their first agreement. Don't fall in "
              'love with the compensation plan before you read the contract.',
      'timestamp': 233,
      'timestamp_label': '[00:03:53]',
      'timestamp_seconds': 233,
      'tip': 'So, after more than 16 years in merchant services, this is one lesson I wish '
             "every new agent understood before signing their first agreement. Don't fall in "
             'love with the compensation plan before you read the contract.',
      'title': 'Merchant Services ISO Agreements Explained | Vesting, Termination & Residual '
               'Rights (Joe Wagner | Merchant Services & Passive Income)',
      'url': 'https://www.youtube.com/watch?v=Em1hM53SuTA&t=233s',
      'video_id': 'Em1hM53SuTA'},
     {'author': 'Global Legal Law Firm',
      'channel': 'Global Legal Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:18](https://www.youtube.com/watch?v=rj9tjHr1nNo&t=1218s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Clark Cramer from National ePayment. Go find Clark over at nationale-payment. '
              'And as always, James Huber joining us in the studio, managing partner of Global '
              "Legal Law Firm. Thank you, and we'll see you on the next one.",
      'timestamp': 1218,
      'timestamp_label': '[00:20:18]',
      'timestamp_seconds': 1218,
      'tip': 'Clark Cramer from National ePayment. Go find Clark over at nationale-payment. '
             'And as always, James Huber joining us in the studio, managing partner of Global '
             "Legal Law Firm. Thank you, and we'll see you on the next one.",
      'title': 'Dual Pricing Done Right: 2026 Practical Guide To Cash Discount And Surcharging '
               'Compliance | PEP106 (Global Legal Law Firm)',
      'url': 'https://www.youtube.com/watch?v=rj9tjHr1nNo&t=1218s',
      'video_id': 'rj9tjHr1nNo'},
     {'author': 'Austin Lewis',
      'channel': 'Austin Lewis',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:38](https://www.youtube.com/watch?v=bnXrdKgeSvY&t=158s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Next six to twelve months but in our contract it also says you cannot go with a '
              'new vendor if you move from this shop inside that one year so if he moves in '
              "the shop within six months then we've check out our ATM and put it inside his "
              'new shop closing deals.',
      'timestamp': 158,
      'timestamp_label': '[00:02:38]',
      'timestamp_seconds': 158,
      'tip': 'Next six to twelve months but in our contract it also says you cannot go with a '
             'new vendor if you move from this shop inside that one year so if he moves in the '
             "shop within six months then we've check out our ATM and put it inside his new "
             'shop closing deals.',
      'title': 'LIVE ATM business negotiation | ATM contracts signed (Austin Lewis)',
      'url': 'https://www.youtube.com/watch?v=bnXrdKgeSvY&t=158s',
      'video_id': 'bnXrdKgeSvY'},
     {'author': 'Valor PayTech',
      'channel': 'Valor PayTech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=MVL80SKYNYs&t=25s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Can see let's view the full board this is where you will add contact "
              'information enter the DBA name to the business which will autop poate the legal '
              'name a username can be an email address that has never been used before or you '
              'will be prompted to enter a unique.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': "Can see let's view the full board this is where you will add contact information "
             'enter the DBA name to the business which will autop poate the legal name a '
             'username can be an email address that has never been used before or you will be '
             'prompted to enter a unique.',
      'title': 'How to deploy merchants on the Valor Portal | Valor PayTech (Valor PayTech)',
      'url': 'https://www.youtube.com/watch?v=MVL80SKYNYs&t=25s',
      'video_id': 'MVL80SKYNYs'},
     {'author': 'nexio',
      'channel': 'nexio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:47](https://www.youtube.com/watch?v=JCe-IWhyJIk&t=227s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The payment processor in sponsor Bank outlining the terms and conditions of '
              'your partnership so what are the responsibilities of operating as a.',
      'timestamp': 227,
      'timestamp_label': '[00:03:47]',
      'timestamp_seconds': 227,
      'tip': 'The payment processor in sponsor Bank outlining the terms and conditions of your '
             'partnership so what are the responsibilities of operating as a.',
      'title': 'Integrated Payments: Retail ISO Overview for Vertical SaaS #paymentprocessing '
               '#integratedpayments (nexio)',
      'url': 'https://www.youtube.com/watch?v=JCe-IWhyJIk&t=227s',
      'video_id': 'JCe-IWhyJIk'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:27](https://www.youtube.com/watch?v=ZRmKamGyTPc&t=27s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Where we're you know, the the business owner is increasing their pricing when "
              "someone uses a certain method of payment, a card for instance, by let's say 4%, "
              "okay? Now, I'm not talking about compliance and all that in this video.",
      'timestamp': 27,
      'timestamp_label': '[00:00:27]',
      'timestamp_seconds': 27,
      'tip': "Where we're you know, the the business owner is increasing their pricing when "
             "someone uses a certain method of payment, a card for instance, by let's say 4%, "
             "okay? Now, I'm not talking about compliance and all that in this video.",
      'title': 'What is Dual Pricing? | Payment Insights (CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=ZRmKamGyTPc&t=27s',
      'video_id': 'ZRmKamGyTPc'},
     {'author': 'Philip Webb',
      'channel': 'Philip Webb',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=ZN0dj7u6nmo&t=42s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And not in the atm business maybe i'm in the atm business i'm thinking about "
              'getting an atm business i hear dispensaries are a hot spot i.',
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': "And not in the atm business maybe i'm in the atm business i'm thinking about "
             'getting an atm business i hear dispensaries are a hot spot i.',
      'title': 'ATM machine in dispensaries (Placing ATM in Dispensaries Explained) (Philip '
               'Webb)',
      'url': 'https://www.youtube.com/watch?v=ZN0dj7u6nmo&t=42s',
      'video_id': 'ZN0dj7u6nmo'},
     {'author': 'Philip Webb',
      'channel': 'Philip Webb',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:23](https://www.youtube.com/watch?v=oIqtdUU2Qtg&t=143s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And you're building relationships with those customers when you're doing that "
              "you're asking them hey do you know any other new store.",
      'timestamp': 143,
      'timestamp_label': '[00:02:23]',
      'timestamp_seconds': 143,
      'tip': "And you're building relationships with those customers when you're doing that "
             "you're asking them hey do you know any other new store.",
      'title': "Why You Shouldn't Become A Vault Casher, But We DID! - ATM Business 2020 "
               '(Philip Webb)',
      'url': 'https://www.youtube.com/watch?v=oIqtdUU2Qtg&t=143s',
      'video_id': 'oIqtdUU2Qtg'},
     {'author': 'CCSalesPro',
      'channel': 'CCSalesPro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:14](https://www.youtube.com/watch?v=bAuRUu51g3c&t=374s)',
      'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                   'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                   'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "94434 4635 I'm in the beautiful state of Florida or you can email me at payrock "
              "p a y ooc Rich Norton gmail.com if I don't answer text me leave me a message I "
              'look forward to speaking with you awesome thanks Rich.',
      'timestamp': 374,
      'timestamp_label': '[00:06:14]',
      'timestamp_seconds': 374,
      'tip': "94434 4635 I'm in the beautiful state of Florida or you can email me at payrock "
             "p a y ooc Rich Norton gmail.com if I don't answer text me leave me a message I "
             'look forward to speaking with you awesome thanks Rich.',
      'title': 'How Much Can You Make Selling Payment Processing? (2024 Update) (CCSalesPro)',
      'url': 'https://www.youtube.com/watch?v=bAuRUu51g3c&t=374s',
      'video_id': 'bAuRUu51g3c'}],
 10: [{'author': 'PaymentCloud',
       'channel': 'PaymentCloud',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:30](https://www.youtube.com/watch?v=XwCDjPAfKtY&t=150s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Plus, you'll have a dedicated account manager who will provide you with "
               'personalized one on one support. High risk merchant accounts are basically '
               'traditional merchant accounts, just with the ability to meet the challenges of '
               'high risk businesses.',
       'timestamp': 150,
       'timestamp_label': '[00:02:30]',
       'timestamp_seconds': 150,
       'tip': "Plus, you'll have a dedicated account manager who will provide you with "
              'personalized one on one support. High risk merchant accounts are basically '
              'traditional merchant accounts, just with the ability to meet the challenges of '
              'high risk businesses.',
       'title': 'High-Risk Merchant Accounts EXPLAINED: What to Do If Your Business Is '
                'Considered High-Risk (PaymentCloud)',
       'url': 'https://www.youtube.com/watch?v=XwCDjPAfKtY&t=150s',
       'video_id': 'XwCDjPAfKtY'},
      {'author': 'CenturyPaymentsInc',
       'channel': 'CenturyPaymentsInc',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:37](https://www.youtube.com/watch?v=Jn1CXq7YPYs&t=97s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Amendment and for unique ways to leverage your payment processing while '
               'enjoying excellent customer service visit our website let us show you why we '
               'are in the top 15 of the fastest growing businesses on the inc 500 list two '
               'years in a row.',
       'timestamp': 97,
       'timestamp_label': '[00:01:37]',
       'timestamp_seconds': 97,
       'tip': 'Amendment and for unique ways to leverage your payment processing while '
              'enjoying excellent customer service visit our website let us show you why we '
              'are in the top 15 of the fastest growing businesses on the inc 500 list two '
              'years in a row.',
       'title': 'The Durbin Amendment: How Does it Affect My Business? (CenturyPaymentsInc)',
       'url': 'https://www.youtube.com/watch?v=Jn1CXq7YPYs&t=97s',
       'video_id': 'Jn1CXq7YPYs'},
      {'author': 'Payment Talks',
       'channel': 'Payment Talks',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:19](https://www.youtube.com/watch?v=6aCyowxoMCk&t=139s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "The Debtor Agent is the bank that actually holds the Debtor's account, and the "
               "Creditor Agent is the bank that holds the Creditor's account. Agent is the "
               'word to hold onto here. It means the bank, not the customer. It can be '
               'individual or corporate.',
       'timestamp': 139,
       'timestamp_label': '[00:02:19]',
       'timestamp_seconds': 139,
       'tip': "The Debtor Agent is the bank that actually holds the Debtor's account, and the "
              "Creditor Agent is the bank that holds the Creditor's account. Agent is the word "
              'to hold onto here. It means the bank, not the customer. It can be individual or '
              'corporate.',
       'title': 'ISO 20022 Payment Lifecycle — Part 1: Foundations + STP Backbone (Payment '
                'Talks)',
       'url': 'https://www.youtube.com/watch?v=6aCyowxoMCk&t=139s',
       'video_id': '6aCyowxoMCk'},
      {'author': 'NateCity',
       'channel': 'NateCity',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:00](https://www.youtube.com/watch?v=d2GxgAYdUig&t=240s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I said that don't treat it like a full-time gig, I know there is plenty of "
               'owners out there, ATM business owners, that have well over 100 or 100 or 200 '
               'ATMs and this is their full thing.',
       'timestamp': 240,
       'timestamp_label': '[00:04:00]',
       'timestamp_seconds': 240,
       'tip': "I said that don't treat it like a full-time gig, I know there is plenty of "
              'owners out there, ATM business owners, that have well over 100 or 100 or 200 '
              'ATMs and this is their full thing.',
       'title': 'Is the ATM Business Still Worth It in 2026? My Honest Breakdown (NateCity)',
       'url': 'https://www.youtube.com/watch?v=d2GxgAYdUig&t=240s',
       'video_id': 'd2GxgAYdUig'},
      {'author': 'Joe Wagner | Merchant Services & Passive Income',
       'channel': 'Joe Wagner | Merchant Services & Passive Income',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:50](https://www.youtube.com/watch?v=N58l9UMrKHY&t=50s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Now, there's acquiring banks. These are the banks that receive the money on "
               "the business's side. Once a transaction is approved, the acquiring bank "
               "deposits the funds into the merchants's account minus a few fees.",
       'timestamp': 50,
       'timestamp_label': '[00:00:50]',
       'timestamp_seconds': 50,
       'tip': "Now, there's acquiring banks. These are the banks that receive the money on the "
              "business's side. Once a transaction is approved, the acquiring bank deposits "
              "the funds into the merchants's account minus a few fees.",
       'title': 'Merchant Services Explained: Banks, ISOs, ISVs & Sales Agents (Joe Wagner | '
                'Merchant Services & Passive Income)',
       'url': 'https://www.youtube.com/watch?v=N58l9UMrKHY&t=50s',
       'video_id': 'N58l9UMrKHY'},
      {'author': 'Philip Webb',
       'channel': 'Philip Webb',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:56](https://www.youtube.com/watch?v=cH26OWh_YDI&t=476s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Today again this is Phil from the ATMs my group page where we buy your freedom '
               'with one transaction at a time thank you guys for making us number one on '
               "YouTube and I'll see you over at the next ATM Mastermind video.",
       'timestamp': 476,
       'timestamp_label': '[00:07:56]',
       'timestamp_seconds': 476,
       'tip': 'Today again this is Phil from the ATMs my group page where we buy your freedom '
              'with one transaction at a time thank you guys for making us number one on '
              "YouTube and I'll see you over at the next ATM Mastermind video.",
       'title': 'Mastering Location Agreements: 5 Vital Steps to Secure ATM Spots (Philip '
                'Webb)',
       'url': 'https://www.youtube.com/watch?v=cH26OWh_YDI&t=476s',
       'video_id': 'cH26OWh_YDI'},
      {'author': 'MASTER FINANCE TV',
       'channel': 'MASTER FINANCE TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:01](https://www.youtube.com/watch?v=pxfdlwdIz2E&t=121s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But, high-volume locations come with a severe catch. Business owners in busy '
               'spaces know exactly what their foot traffic is worth, and they will leverage '
               'that volume to demand a much larger percentage of the revenue share.',
       'timestamp': 121,
       'timestamp_label': '[00:02:01]',
       'timestamp_seconds': 121,
       'tip': 'But, high-volume locations come with a severe catch. Business owners in busy '
              'spaces know exactly what their foot traffic is worth, and they will leverage '
              'that volume to demand a much larger percentage of the revenue share.',
       'title': 'How Much Money Does Owning an ATM Really Make? (MASTER FINANCE TV)',
       'url': 'https://www.youtube.com/watch?v=pxfdlwdIz2E&t=121s',
       'video_id': 'pxfdlwdIz2E'},
      {'author': 'Chargeback',
       'channel': 'Chargeback',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:44](https://www.youtube.com/watch?v=sH9CslJpDeA&t=44s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The fastest taking up to 12 business hours to get going while RDR requires up '
               'to 72 business hours when it comes to payment gateways all alert providers '
               'can.',
       'timestamp': 44,
       'timestamp_label': '[00:00:44]',
       'timestamp_seconds': 44,
       'tip': 'The fastest taking up to 12 business hours to get going while RDR requires up '
              'to 72 business hours when it comes to payment gateways all alert providers can.',
       'title': 'Chargeback.io - Ethoca, RDR & CDRN Enrollment Explained (Chargeback)',
       'url': 'https://www.youtube.com/watch?v=sH9CslJpDeA&t=44s',
       'video_id': 'sH9CslJpDeA'},
      {'author': 'Sean Jones Revolution Payments',
       'channel': 'Sean Jones Revolution Payments',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=vVvGM8Rlor8&t=15s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Responsible for 75 to 90 percent of the fees that businesses pay to take '
               "credit cards and get this that speed doesn't even go to your process or it "
               'actually.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Responsible for 75 to 90 percent of the fees that businesses pay to take credit '
              "cards and get this that speed doesn't even go to your process or it actually.",
       'title': 'Interchange Audit & Level-3 Processing (Sean Jones Revolution Payments)',
       'url': 'https://www.youtube.com/watch?v=vVvGM8Rlor8&t=15s',
       'video_id': 'vVvGM8Rlor8'},
      {'author': 'CCSalesPro',
       'channel': 'CCSalesPro',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:13](https://www.youtube.com/watch?v=wqM5pwZDSBQ&t=133s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Right but if you're trying to grow your business right the best thing to do "
               'one of the best things to do think about this so many other businesses have to '
               'go.',
       'timestamp': 133,
       'timestamp_label': '[00:02:13]',
       'timestamp_seconds': 133,
       'tip': "Right but if you're trying to grow your business right the best thing to do one "
              'of the best things to do think about this so many other businesses have to go.',
       'title': 'Why Should You Sell Your Merchant Services Residual? (CCSalesPro)',
       'url': 'https://www.youtube.com/watch?v=wqM5pwZDSBQ&t=133s',
       'video_id': 'wqM5pwZDSBQ'},
      {'author': 'Scott E. Adams | Chargeback Expert',
       'channel': 'Scott E. Adams | Chargeback Expert',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=Ghanuu5dNMk&t=15s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Another of the alert Services out there and you know most people think of the '
               'one from verifi we talked about yesterday CD are in as the Visa side and.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Another of the alert Services out there and you know most people think of the '
              'one from verifi we talked about yesterday CD are in as the Visa side and.',
       'title': 'Ethoca Alerts and Chargeback Prevention (Scott E. Adams | Chargeback Expert)',
       'url': 'https://www.youtube.com/watch?v=Ghanuu5dNMk&t=15s',
       'video_id': 'Ghanuu5dNMk'},
      {'author': 'Philip Webb',
       'channel': 'Philip Webb',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:23](https://www.youtube.com/watch?v=FhOgcbeefS0&t=323s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Charge for this training but I'm going to give it to you absolutely free for a "
               'limited time offer so click the link below and register today always remember '
               'here at pdq merch enterprises in the atm mastermind group page we buy your '
               'freedom back one transaction at a time.',
       'timestamp': 323,
       'timestamp_label': '[00:05:23]',
       'timestamp_seconds': 323,
       'tip': "Charge for this training but I'm going to give it to you absolutely free for a "
              'limited time offer so click the link below and register today always remember '
              'here at pdq merch enterprises in the atm mastermind group page we buy your '
              'freedom back one transaction at a time.',
       'title': 'Top 5 tips on how to increase you atm surcharge fee (ATM business 2021) '
                '(Philip Webb)',
       'url': 'https://www.youtube.com/watch?v=FhOgcbeefS0&t=323s',
       'video_id': 'FhOgcbeefS0'},
      {'author': 'Electronic Money Company',
       'channel': 'Electronic Money Company',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:16](https://www.youtube.com/watch?v=HAEcBxhwNkI&t=256s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'B2B processing, integrations to QuickBooks, invoicing, email, and text to pay. '
               'You can sell solutions instead of just how cheap can we do it. Value instead '
               'of discounts and the value allows you to sell at higher rates.',
       'timestamp': 256,
       'timestamp_label': '[00:04:16]',
       'timestamp_seconds': 256,
       'tip': 'B2B processing, integrations to QuickBooks, invoicing, email, and text to pay. '
              'You can sell solutions instead of just how cheap can we do it. Value instead of '
              'discounts and the value allows you to sell at higher rates.',
       'title': 'Merchant Services Sales How to Pick a Processor That Builds and Protects Long '
                'Term Residuals (Electronic Money Company)',
       'url': 'https://www.youtube.com/watch?v=HAEcBxhwNkI&t=256s',
       'video_id': 'HAEcBxhwNkI'},
      {'author': 'CCSalesPro',
       'channel': 'CCSalesPro',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:06](https://www.youtube.com/watch?v=iouhW_rMFI0&t=66s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'To just walk in yep and say hey I can do this for you right and then you lose '
               "that account okay fine I'll sign on yours so then you use that account and.",
       'timestamp': 66,
       'timestamp_label': '[00:01:06]',
       'timestamp_seconds': 66,
       'tip': 'To just walk in yep and say hey I can do this for you right and then you lose '
              "that account okay fine I'll sign on yours so then you use that account and.",
       'title': 'How Does Pricing and Service Affect a Merchant Residual Buyout? (CCSalesPro)',
       'url': 'https://www.youtube.com/watch?v=iouhW_rMFI0&t=66s',
       'video_id': 'iouhW_rMFI0'},
      {'author': 'CCSalesPro',
       'channel': 'CCSalesPro',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:52](https://www.youtube.com/watch?v=qaQA_RMy-_c&t=232s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Slash buyout and once you do that we'll take you right over to a page where "
               'you can actually put just a little bit of information in there about your '
               'portfolio send it directly to a partner we trust and get you that that third '
               "party offer that you're looking for great.",
       'timestamp': 232,
       'timestamp_label': '[00:03:52]',
       'timestamp_seconds': 232,
       'tip': "Slash buyout and once you do that we'll take you right over to a page where you "
              'can actually put just a little bit of information in there about your portfolio '
              'send it directly to a partner we trust and get you that that third party offer '
              "that you're looking for great.",
       'title': 'Should I Sell My Merchant Residual Portfolio Back to My ISO? (CCSalesPro)',
       'url': 'https://www.youtube.com/watch?v=qaQA_RMy-_c&t=232s',
       'video_id': 'qaQA_RMy-_c'}],
 11: [{'author': 'The Payout',
       'channel': 'The Payout',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:22](https://www.youtube.com/watch?v=Q4wB_IBk6ik&t=202s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Each one earning a few hundred dollars a month. At that scale, you're looking "
               'at a business that can bring in 10 to 20,000 dollars monthly with far fewer '
               'employees and far less overhead than most small businesses.',
       'timestamp': 202,
       'timestamp_label': '[00:03:22]',
       'timestamp_seconds': 202,
       'tip': "Each one earning a few hundred dollars a month. At that scale, you're looking "
              'at a business that can bring in 10 to 20,000 dollars monthly with far fewer '
              'employees and far less overhead than most small businesses.',
       'title': 'The ATM Business Nobody Talks About 💵 (Explained In 4 Minutes) (The Payout)',
       'url': 'https://www.youtube.com/watch?v=Q4wB_IBk6ik&t=202s',
       'video_id': 'Q4wB_IBk6ik'},
      {'author': 'Austin Zaback',
       'channel': 'Austin Zaback',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:44](https://www.youtube.com/watch?v=gvvB3u1AMMI&t=284s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Prius in order to, you know, drive around and fill up ATMs. Now, in the ATM '
               'industry, you can hire what they call somebody to fill your ATM, okay? And '
               "they're what we used to call like a cash loader, okay?",
       'timestamp': 284,
       'timestamp_label': '[00:04:44]',
       'timestamp_seconds': 284,
       'tip': 'Prius in order to, you know, drive around and fill up ATMs. Now, in the ATM '
              'industry, you can hire what they call somebody to fill your ATM, okay? And '
              "they're what we used to call like a cash loader, okay?",
       'title': 'Why I SOLD MY ATM BUSINESS | The Future of ATM’s in 2023 (Austin Zaback)',
       'url': 'https://www.youtube.com/watch?v=gvvB3u1AMMI&t=284s',
       'video_id': 'gvvB3u1AMMI'},
      {'author': 'County Portal',
       'channel': 'County Portal',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:13](https://www.youtube.com/watch?v=QZSSbXV33jg&t=73s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Identification number, EIN, from the IRS, and open a dedicated business bank '
               'account. This is non-negotiable for professionalism and liability.',
       'timestamp': 73,
       'timestamp_label': '[00:01:13]',
       'timestamp_seconds': 73,
       'tip': 'Identification number, EIN, from the IRS, and open a dedicated business bank '
              'account. This is non-negotiable for professionalism and liability.',
       'title': 'How To Start A Credit Card Processing Company? (County Portal)',
       'url': 'https://www.youtube.com/watch?v=QZSSbXV33jg&t=73s',
       'video_id': 'QZSSbXV33jg'},
      {'author': 'Residual Income for Beginners',
       'channel': 'Residual Income for Beginners',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:24:54](https://www.youtube.com/watch?v=uV3SWzHlom0&t=1494s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "300,000 to get started, and they're like, man, it's going to take me a while "
               'to recoup that. I could use an extra 50,000 right now. Um and then another '
               'thing, guys, for a lot of small businesses and business owners, they may '
               'already have a loan from the bank.',
       'timestamp': 1494,
       'timestamp_label': '[00:24:54]',
       'timestamp_seconds': 1494,
       'tip': "300,000 to get started, and they're like, man, it's going to take me a while to "
              'recoup that. I could use an extra 50,000 right now. Um and then another thing, '
              'guys, for a lot of small businesses and business owners, they may already have '
              'a loan from the bank.',
       'title': 'How I Went from Riding the Bus to $190,000,000 in Merchant Services! '
                '(Residual Income for Beginners)',
       'url': 'https://www.youtube.com/watch?v=uV3SWzHlom0&t=1494s',
       'video_id': 'uV3SWzHlom0'},
      {'author': 'Joe Wagner | Merchant Services & Passive Income',
       'channel': 'Joe Wagner | Merchant Services & Passive Income',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:21](https://www.youtube.com/watch?v=6fKRmYMx0m8&t=141s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': '10,000 per month in passive income. One of the most exciting parts about being '
               'a 1099 in this industry is you never have to stop building. You can scale far '
               'beyond that and evolve into the five levels of mastery and just keep growing '
               'and growing in this business.',
       'timestamp': 141,
       'timestamp_label': '[00:02:21]',
       'timestamp_seconds': 141,
       'tip': '10,000 per month in passive income. One of the most exciting parts about being '
              'a 1099 in this industry is you never have to stop building. You can scale far '
              'beyond that and evolve into the five levels of mastery and just keep growing '
              'and growing in this business.',
       'title': 'Merchant Services for Beginners: How to Get Started the Right Way (Joe Wagner '
                '| Merchant Services & Passive Income)',
       'url': 'https://www.youtube.com/watch?v=6fKRmYMx0m8&t=141s',
       'video_id': '6fKRmYMx0m8'},
      {'author': 'ABC News (Australia)',
       'channel': 'ABC News (Australia)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:56](https://www.youtube.com/watch?v=COwQpax5fxU&t=56s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'These changes will help take some of the pressures off consumers and '
               'businesses and help with the cost of living. These changes could cost the '
               'banks around $660 million per year. Each bank will have to make its own '
               'decision.',
       'timestamp': 56,
       'timestamp_label': '[00:00:56]',
       'timestamp_seconds': 56,
       'tip': 'These changes will help take some of the pressures off consumers and businesses '
              'and help with the cost of living. These changes could cost the banks around '
              '$660 million per year. Each bank will have to make its own decision.',
       'title': 'Ban on debit and credit card surcharges | The Business | ABC NEWS (ABC News '
                '(Australia))',
       'url': 'https://www.youtube.com/watch?v=COwQpax5fxU&t=56s',
       'video_id': 'COwQpax5fxU'},
      {'author': 'Next Generation Payments',
       'channel': 'Next Generation Payments',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:56](https://www.youtube.com/watch?v=b0H2H7FAjPA&t=56s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Our trusted service supports over 2,000 restaurants using our systems. Our '
               'free POS package includes everything from installation to ongoing support. '
               'Imagine increasing sales, improving operations, and building your brand '
               'without spending a dime on POS systems.',
       'timestamp': 56,
       'timestamp_label': '[00:00:56]',
       'timestamp_seconds': 56,
       'tip': 'Our trusted service supports over 2,000 restaurants using our systems. Our free '
              'POS package includes everything from installation to ongoing support. Imagine '
              'increasing sales, improving operations, and building your brand without '
              'spending a dime on POS systems.',
       'title': 'Dual Pricing Explained: Clear Cash and Card Prices (Next Generation Payments)',
       'url': 'https://www.youtube.com/watch?v=b0H2H7FAjPA&t=56s',
       'video_id': 'b0H2H7FAjPA'},
      {'author': 'WKRN News 2',
       'channel': 'WKRN News 2',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=DzLysrdcerg&t=20s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'THANKS TO SOME GOOD OL FASHIONED BRUTE FORCE. 15 FRIDAY MORNING FOR ATM '
               'BANDITS SWOOP IN TO THE RELIANT BANK PARKING LOT IN P GROOM. 3 MEN IMMEDIATELY '
               'JUMP OUT WITH HEAVY CROWBARS WHILE THESE 3 BIG IN PRYING OPEN THE MACHINES '
               'OUTER LAYER.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'THANKS TO SOME GOOD OL FASHIONED BRUTE FORCE. 15 FRIDAY MORNING FOR ATM BANDITS '
              'SWOOP IN TO THE RELIANT BANK PARKING LOT IN P GROOM. 3 MEN IMMEDIATELY JUMP OUT '
              'WITH HEAVY CROWBARS WHILE THESE 3 BIG IN PRYING OPEN THE MACHINES OUTER LAYER.',
       'title': 'Suspects open ATM in 30 seconds (WKRN News 2)',
       'url': 'https://www.youtube.com/watch?v=DzLysrdcerg&t=20s',
       'video_id': 'DzLysrdcerg'},
      {'author': 'SwipeNow Payments',
       'channel': 'SwipeNow Payments',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:57](https://www.youtube.com/watch?v=QbpUZX5GSzA&t=117s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Entities includes the merchant which is the business the customer the '
               'acquiring bank which is the Merchants Bank the issuing bank which is the '
               'customers bank.',
       'timestamp': 117,
       'timestamp_label': '[00:01:57]',
       'timestamp_seconds': 117,
       'tip': 'Entities includes the merchant which is the business the customer the acquiring '
              'bank which is the Merchants Bank the issuing bank which is the customers bank.',
       'title': 'Selling Payment Processing: How to Make Money Selling Merchant Services '
                '(SwipeNow Payments)',
       'url': 'https://www.youtube.com/watch?v=QbpUZX5GSzA&t=117s',
       'video_id': 'QbpUZX5GSzA'},
      {'author': 'Philip Webb',
       'channel': 'Philip Webb',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:50](https://www.youtube.com/watch?v=9QGfLH_pm0o&t=410s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Prices and the ATMs my group page we buy Freedom back one transaction at a '
               "time thank you guys for making us number one on YouTube and we're also on "
               'Rumble so check us out foreign.',
       'timestamp': 410,
       'timestamp_label': '[00:06:50]',
       'timestamp_seconds': 410,
       'tip': 'Prices and the ATMs my group page we buy Freedom back one transaction at a time '
              "thank you guys for making us number one on YouTube and we're also on Rumble so "
              'check us out foreign.',
       'title': 'ATM location agreement tips  (The top 5 must have things in your SLA) (Philip '
                'Webb)',
       'url': 'https://www.youtube.com/watch?v=9QGfLH_pm0o&t=410s',
       'video_id': '9QGfLH_pm0o'},
      {'author': 'MerchantAccounts.ca',
       'channel': 'MerchantAccounts.ca',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:53](https://www.youtube.com/watch?v=btemhvIers4&t=53s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Country level so I'm Canadian we are Canadian based business every payment "
               "processor in Canada incurs the same interchange cost structure so it doesn't.",
       'timestamp': 53,
       'timestamp_label': '[00:00:53]',
       'timestamp_seconds': 53,
       'tip': "Country level so I'm Canadian we are Canadian based business every payment "
              "processor in Canada incurs the same interchange cost structure so it doesn't.",
       'title': 'What is Interchange Plus Pricing? (MerchantAccounts.ca)',
       'url': 'https://www.youtube.com/watch?v=btemhvIers4&t=53s',
       'video_id': 'btemhvIers4'},
      {'author': 'Cornerstone Advisors',
       'channel': 'Cornerstone Advisors',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:25](https://www.youtube.com/watch?v=FwB1KshUr5A&t=205s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Cautiously optimistic it could be a little bit more than 14.4 but it's not "
               "going to be 21 so if you're close or you're on the verge or even if you're "
               "over definitely make sure you've got that sized up correctly and you've "
               'understand that impact.',
       'timestamp': 205,
       'timestamp_label': '[00:03:25]',
       'timestamp_seconds': 205,
       'tip': "Cautiously optimistic it could be a little bit more than 14.4 but it's not "
              "going to be 21 so if you're close or you're on the verge or even if you're over "
              "definitely make sure you've got that sized up correctly and you've understand "
              'that impact.',
       'title': 'Hot Takes | Durbin Amendment Changes with Kevin Von Holten (Cornerstone '
                'Advisors)',
       'url': 'https://www.youtube.com/watch?v=FwB1KshUr5A&t=205s',
       'video_id': 'FwB1KshUr5A'},
      {'author': "Michael O'Hare",
       'channel': "Michael O'Hare",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=ZbMb1ETKWMI&t=21s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Which greatly reduces your card processing rates in fact This is the biggest '
               'cost reduction In The history of the payments industry.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'Which greatly reduces your card processing rates in fact This is the biggest '
              'cost reduction In The history of the payments industry.',
       'title': "How to lower your card processing fees thru Durbin Act (Michael O'Hare)",
       'url': 'https://www.youtube.com/watch?v=ZbMb1ETKWMI&t=21s',
       'video_id': 'ZbMb1ETKWMI'},
      {'author': 'CCSalesPro',
       'channel': 'CCSalesPro',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:32](https://www.youtube.com/watch?v=3bPRCy508Lc&t=212s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Paytech terminal is going to automatically calculate that difference so '
               'somebody comes to the store they pay they buy something for a hundred dollars.',
       'timestamp': 212,
       'timestamp_label': '[00:03:32]',
       'timestamp_seconds': 212,
       'tip': 'Paytech terminal is going to automatically calculate that difference so '
              'somebody comes to the store they pay they buy something for a hundred dollars.',
       'title': 'How to Sell Dual Pricing (CCSalesPro)',
       'url': 'https://www.youtube.com/watch?v=3bPRCy508Lc&t=212s',
       'video_id': '3bPRCy508Lc'},
      {'author': 'Lines & Gains',
       'channel': 'Lines & Gains',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:59](https://www.youtube.com/watch?v=-6VRYcYBnSA&t=479s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'ISO affiliate through your ATM processor and open a dedicated ATM vault cash '
               'account with an ATM-friendly regional commercial bank or use armored vault '
               'cash provisioning once you pass 15 machines.',
       'timestamp': 479,
       'timestamp_label': '[00:07:59]',
       'timestamp_seconds': 479,
       'tip': 'ISO affiliate through your ATM processor and open a dedicated ATM vault cash '
              'account with an ATM-friendly regional commercial bank or use armored vault cash '
              'provisioning once you pass 15 machines.',
       'title': 'I Analyzed the Real Math of Owning 10 ATMs in America (2026 Profit Breakdown) '
                '(Lines & Gains)',
       'url': 'https://www.youtube.com/watch?v=-6VRYcYBnSA&t=479s',
       'video_id': '-6VRYcYBnSA'}],
 12: [{'author': 'Residual Builders',
       'channel': 'Residual Builders',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:30](https://www.youtube.com/watch?v=4z4EyZ1Rkbk&t=450s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And that's why the payments industry is so powerful. You're not just closing "
               "deals and earning a one-time commission. You're building a portfolio, a book "
               "of business of recurring revenue. And so, in step five, let's go ahead and "
               'create our 90-day target.',
       'timestamp': 450,
       'timestamp_label': '[00:07:30]',
       'timestamp_seconds': 450,
       'tip': "And that's why the payments industry is so powerful. You're not just closing "
              "deals and earning a one-time commission. You're building a portfolio, a book of "
              "business of recurring revenue. And so, in step five, let's go ahead and create "
              'our 90-day target.',
       'title': 'How to Hit $10K/Month in Merchant Services (How Many Clients You Need) '
                '(Residual Builders)',
       'url': 'https://www.youtube.com/watch?v=4z4EyZ1Rkbk&t=450s',
       'video_id': '4z4EyZ1Rkbk'},
      {'author': 'The Business Guy | Asset Protection Planners',
       'channel': 'The Business Guy | Asset Protection Planners',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:13](https://www.youtube.com/watch?v=gaNeKJoK-74&t=553s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'People will buy it then you have to stand there all day hoping somebody walks '
               "in what a drag right with the ATM business you don't even have to show up.",
       'timestamp': 553,
       'timestamp_label': '[00:09:13]',
       'timestamp_seconds': 553,
       'tip': 'People will buy it then you have to stand there all day hoping somebody walks '
              "in what a drag right with the ATM business you don't even have to show up.",
       'title': 'How to Start an ATM Business | How Much Can You MAKE? (The Business Guy | '
                'Asset Protection Planners)',
       'url': 'https://www.youtube.com/watch?v=gaNeKJoK-74&t=553s',
       'video_id': 'gaNeKJoK-74'},
      {'author': 'CAPITAL COACH',
       'channel': 'CAPITAL COACH',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:59](https://www.youtube.com/watch?v=R1wscXZLkbw&t=59s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "This is So, you want to own an ATM business. Let's start with the basics, "
               "because most people don't understand what an ATM actually is. When you walk up "
               "to a machine at a gas station and pull out cash, you're probably not using a "
               "bank's machine.",
       'timestamp': 59,
       'timestamp_label': '[00:00:59]',
       'timestamp_seconds': 59,
       'tip': "This is So, you want to own an ATM business. Let's start with the basics, "
              "because most people don't understand what an ATM actually is. When you walk up "
              "to a machine at a gas station and pull out cash, you're probably not using a "
              "bank's machine.",
       'title': 'The Hidden Costs of Owning an ATM 🏧 (CAPITAL COACH)',
       'url': 'https://www.youtube.com/watch?v=R1wscXZLkbw&t=59s',
       'video_id': 'R1wscXZLkbw'},
      {'author': 'Joe Wagner | Merchant Services & Passive Income',
       'channel': 'Joe Wagner | Merchant Services & Passive Income',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:55](https://www.youtube.com/watch?v=ogeyMD07VYc&t=115s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And this is where merchant services becomes really powerful. Don't think about "
               'one $1,000 transaction, think about businesses processing transactions all day '
               'long. And then again tomorrow, and then they do it again next week, and then '
               'next month, and next year.',
       'timestamp': 115,
       'timestamp_label': '[00:01:55]',
       'timestamp_seconds': 115,
       'tip': "And this is where merchant services becomes really powerful. Don't think about "
              'one $1,000 transaction, think about businesses processing transactions all day '
              'long. And then again tomorrow, and then they do it again next week, and then '
              'next month, and next year.',
       'title': 'Merchant Services Residuals Explained | How Agents Get Paid Monthly (Joe '
                'Wagner | Merchant Services & Passive Income)',
       'url': 'https://www.youtube.com/watch?v=ogeyMD07VYc&t=115s',
       'video_id': 'ogeyMD07VYc'},
      {'author': 'High-Risk Merchant Accounts | Adaptiv Payments',
       'channel': 'High-Risk Merchant Accounts | Adaptiv Payments',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:26](https://www.youtube.com/watch?v=7jkV0JkaEZA&t=26s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'With your own merchant account, the bank reviews your store before you start, '
               'so you know where you stand from day one. Banks look at what you sell and how '
               'you sell it. Products like CBD, supplements, vapes or firearms. Pre-orders and '
               'long shipping times.',
       'timestamp': 26,
       'timestamp_label': '[00:00:26]',
       'timestamp_seconds': 26,
       'tip': 'With your own merchant account, the bank reviews your store before you start, '
              'so you know where you stand from day one. Banks look at what you sell and how '
              'you sell it. Products like CBD, supplements, vapes or firearms. Pre-orders and '
              'long shipping times.',
       'title': 'Ecommerce Merchant Account: What Banks Check Before They Approve Your Store '
                '(2026) (High-Risk Merchant Accounts | Adaptiv Payments)',
       'url': 'https://www.youtube.com/watch?v=7jkV0JkaEZA&t=26s',
       'video_id': '7jkV0JkaEZA'},
      {'author': 'POS Nexus',
       'channel': 'POS Nexus',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:36](https://www.youtube.com/watch?v=m1nRWuyd4rI&t=36s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Debit and prepaid cards can't be surcharged, even debit run as credit. The fee "
               "can't be more than your cost of accepting that card, and never more than three "
               'percent. Give your acquirer thirty days notice before you start. Put a sign at '
               'the door, and another at the till.',
       'timestamp': 36,
       'timestamp_label': '[00:00:36]',
       'timestamp_seconds': 36,
       'tip': "Debit and prepaid cards can't be surcharged, even debit run as credit. The fee "
              "can't be more than your cost of accepting that card, and never more than three "
              'percent. Give your acquirer thirty days notice before you start. Put a sign at '
              'the door, and another at the till.',
       'title': 'Can You Charge a Credit Card Fee? Surcharge Rules + the Visa/Mastercard '
                'Settlement (POS Nexus)',
       'url': 'https://www.youtube.com/watch?v=m1nRWuyd4rI&t=36s',
       'video_id': 'm1nRWuyd4rI'},
      {'author': 'BestCardProcessing',
       'channel': 'BestCardProcessing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:17](https://www.youtube.com/watch?v=UMy8ceQ1bm4&t=797s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Business is searching for the solution is to have an independent third party '
               'card processing professional provide a free no obligation audit of your recent '
               'processing statement a typical audit only takes three days good news.',
       'timestamp': 797,
       'timestamp_label': '[00:13:17]',
       'timestamp_seconds': 797,
       'tip': 'Business is searching for the solution is to have an independent third party '
              'card processing professional provide a free no obligation audit of your recent '
              'processing statement a typical audit only takes three days good news.',
       'title': 'What The Durbin Amendment means to Small Business Credit/Debit Card '
                'Processing (BestCardProcessing)',
       'url': 'https://www.youtube.com/watch?v=UMy8ceQ1bm4&t=797s',
       'video_id': 'UMy8ceQ1bm4'},
      {'author': 'CCSalesPro',
       'channel': 'CCSalesPro',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:49](https://www.youtube.com/watch?v=-sMJDgFoiSM&t=289s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'About building your iso out go to ccsalespro.com insights you can download the '
               'full pdf there you can listen to the audiobook version of it as well thanks so '
               'much for taking time to watch and listen have a great day.',
       'timestamp': 289,
       'timestamp_label': '[00:04:49]',
       'timestamp_seconds': 289,
       'tip': 'About building your iso out go to ccsalespro.com insights you can download the '
              'full pdf there you can listen to the audiobook version of it as well thanks so '
              'much for taking time to watch and listen have a great day.',
       'title': 'Building a Payment Processing Business and Promoting Your Brand (CCSalesPro)',
       'url': 'https://www.youtube.com/watch?v=-sMJDgFoiSM&t=289s',
       'video_id': '-sMJDgFoiSM'},
      {'author': 'Merchant Maverick',
       'channel': 'Merchant Maverick',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:05](https://www.youtube.com/watch?v=dUz90pAXTm0&t=245s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "But for now, you're done with the headaches! And if you're ready to dive into "
               'numbers, go click the link below and see you next week! Check our playlist for '
               'more credit card processing and small business tips!',
       'timestamp': 245,
       'timestamp_label': '[00:04:05]',
       'timestamp_seconds': 245,
       'tip': "But for now, you're done with the headaches! And if you're ready to dive into "
              'numbers, go click the link below and see you next week! Check our playlist for '
              'more credit card processing and small business tips!',
       'title': 'Merchant Account Pricing: Interchange Fees Explained (Merchant Maverick)',
       'url': 'https://www.youtube.com/watch?v=dUz90pAXTm0&t=245s',
       'video_id': 'dUz90pAXTm0'},
      {'author': 'Philip Webb',
       'channel': 'Philip Webb',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:44](https://www.youtube.com/watch?v=cKH1jOBKB_w&t=224s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Seven fifteen days every week and so it'll take some time to change their "
               "their pattern in their habits so now they won't necessarily happen cash when.",
       'timestamp': 224,
       'timestamp_label': '[00:03:44]',
       'timestamp_seconds': 224,
       'tip': "Seven fifteen days every week and so it'll take some time to change their their "
              "pattern in their habits so now they won't necessarily happen cash when.",
       'title': 'How to put an ATM in a Barbershop [ATM business tips] (Philip Webb)',
       'url': 'https://www.youtube.com/watch?v=cKH1jOBKB_w&t=224s',
       'video_id': 'cKH1jOBKB_w'},
      {'author': 'Electronic Money Company',
       'channel': 'Electronic Money Company',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:15](https://www.youtube.com/watch?v=NlqhCjnpL6c&t=135s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Ginger and having three brickandmortar businesses. That is the power of '
               'residual income is that it frees up your time and you can flexibly do many '
               "other things because you're not at a singular place from 9 to5 every day.",
       'timestamp': 135,
       'timestamp_label': '[00:02:15]',
       'timestamp_seconds': 135,
       'tip': 'Ginger and having three brickandmortar businesses. That is the power of '
              'residual income is that it frees up your time and you can flexibly do many '
              "other things because you're not at a singular place from 9 to5 every day.",
       'title': 'The Power of Residual Income from Merchant Services Sales! (Electronic Money '
                'Company)',
       'url': 'https://www.youtube.com/watch?v=NlqhCjnpL6c&t=135s',
       'video_id': 'NlqhCjnpL6c'},
      {'author': 'Scott E. Adams | Chargeback Expert',
       'channel': 'Scott E. Adams | Chargeback Expert',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:11](https://www.youtube.com/watch?v=gROmfVmEsYs&t=191s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'In cdrn and Etha to get quick coverage and start lowering those charge backs '
               "and then get into RDR and go from there there's a lot more you can do but "
               "that's a good start so let us know if you need help I hope that helps thanks a "
               'lot.',
       'timestamp': 191,
       'timestamp_label': '[00:03:11]',
       'timestamp_seconds': 191,
       'tip': 'In cdrn and Etha to get quick coverage and start lowering those charge backs '
              "and then get into RDR and go from there there's a lot more you can do but "
              "that's a good start so let us know if you need help I hope that helps thanks a "
              'lot.',
       'title': 'How long does it take to setup Verifi CDRN and Ethoca Alerts (Scott E. Adams '
                '| Chargeback Expert)',
       'url': 'https://www.youtube.com/watch?v=gROmfVmEsYs&t=191s',
       'video_id': 'gROmfVmEsYs'},
      {'author': 'CCSalesPro',
       'channel': 'CCSalesPro',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:02](https://www.youtube.com/watch?v=VNId5AUIElE&t=362s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Going to make an average of about $30 per month in residual per account that '
               "you get going so how quick will your residual build up well let's think.",
       'timestamp': 362,
       'timestamp_label': '[00:06:02]',
       'timestamp_seconds': 362,
       'tip': 'Going to make an average of about $30 per month in residual per account that '
              "you get going so how quick will your residual build up well let's think.",
       'title': 'How Much Can I Make Selling Merchant Services? - Understanding Residual and '
                'Up Front Commission (CCSalesPro)',
       'url': 'https://www.youtube.com/watch?v=VNId5AUIElE&t=362s',
       'video_id': 'VNId5AUIElE'},
      {'author': 'Philip Webb',
       'channel': 'Philip Webb',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:15](https://www.youtube.com/watch?v=4StHjKKuzds&t=255s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Can get that all day long 350 to 5 and point number five is split what does a '
               "split look like how much money i'm gonna have to give the.",
       'timestamp': 255,
       'timestamp_label': '[00:04:15]',
       'timestamp_seconds': 255,
       'tip': 'Can get that all day long 350 to 5 and point number five is split what does a '
              "split look like how much money i'm gonna have to give the.",
       'title': 'What Should I Set My ATMs Surcharge At - ATM Business 2020 (Philip Webb)',
       'url': 'https://www.youtube.com/watch?v=4StHjKKuzds&t=255s',
       'video_id': '4StHjKKuzds'},
      {'author': 'Revenue Stacks',
       'channel': 'Revenue Stacks',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:46](https://www.youtube.com/watch?v=qJ7rTUZZ68c&t=226s)',
       'relevance': 'Attributed practitioner commentary on wholesale ISO Schedule A '
                    'interchange-to-dual-pricing merchant residual spreads, high-risk MID '
                    'orchestration, and exclusive venue ATM surcharge portfolios (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The winner is the ATM route operator, recurring, scalable, sellable. The '
               "verdict is buy the route, but don't start there. Put it in a good location, a "
               'bar, a barbershop, heavy cash retail, and run it for 6 months.',
       'timestamp': 226,
       'timestamp_label': '[00:03:46]',
       'timestamp_seconds': 226,
       'tip': 'The winner is the ATM route operator, recurring, scalable, sellable. The '
              "verdict is buy the route, but don't start there. Put it in a good location, a "
              'bar, a barbershop, heavy cash retail, and run it for 6 months.',
       'title': "Start an ATM Machine Business. Here's the Real Math + How to do it (Revenue "
                'Stacks)',
       'url': 'https://www.youtube.com/watch?v=qJ7rTUZZ68c&t=226s',
       'video_id': 'qJ7rTUZZ68c'}]}
