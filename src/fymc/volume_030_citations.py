"""Curated 180-citation Lending & Flash-Funding Arbitrage baseline (15 per chapter across Q1-Q12) mined strictly from verified Lending & Flash-Funding Arbitrage YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'100',
     'aged',
     'agent',
     'agreement',
     'alta',
     'annualized',
     'approved',
     'apr',
     'arbitrage',
     'assignment',
     'automated',
     'avoiding',
     'b2b',
     'bank',
     'before',
     'bridge',
     'building',
     'business',
     'buyer',
     'callback',
     'cancellation',
     'capital',
     'card',
     'charging',
     'checklists',
     'clearing',
     'client',
     'clients',
     'close',
     'closing',
     'commercial',
     'company',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'100',
     'aged',
     'agent',
     'agreement',
     'alta',
     'annualized',
     'approved',
     'apr',
     'arbitrage',
     'assignment',
     'automated',
     'avoiding',
     'b2b',
     'bank',
     'before',
     'bridge',
     'budget',
     'building',
     'business',
     'buyer',
     'callback',
     'cancellation',
     'capital',
     'card',
     'charging',
     'checklists',
     'clearing',
     'close',
     'closing',
     'commercial',
     'company',
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
 3: {'100',
     'aged',
     'agent',
     'agreement',
     'alta',
     'annualized',
     'approved',
     'apr',
     'arbitrage',
     'assignment',
     'automated',
     'avoiding',
     'b2b',
     'bank',
     'before',
     'bridge',
     'building',
     'business',
     'buyer',
     'callback',
     'cancellation',
     'capital',
     'card',
     'cash',
     'cashflow',
     'charging',
     'checklists',
     'clearing',
     'close',
     'closing',
     'commercial',
     'commission',
     'company',
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
 4: {'100',
     'aged',
     'agent',
     'agreement',
     'alta',
     'annualized',
     'approved',
     'apr',
     'arbitrage',
     'assignment',
     'automated',
     'avoiding',
     'b2b',
     'bank',
     'before',
     'bridge',
     'budget',
     'building',
     'business',
     'buyer',
     'callback',
     'cancellation',
     'capital',
     'card',
     'charging',
     'checklists',
     'clearing',
     'close',
     'closing',
     'commercial',
     'company',
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
 5: {'100',
     'aged',
     'agent',
     'agreement',
     'alta',
     'annualized',
     'approved',
     'apr',
     'arbitrage',
     'assignment',
     'audit',
     'automated',
     'avoid',
     'avoiding',
     'b2b',
     'bank',
     'before',
     'bridge',
     'building',
     'business',
     'buyer',
     'callback',
     'cancellation',
     'capital',
     'card',
     'charging',
     'checklists',
     'clawback',
     'clearing',
     'close',
     'closing',
     'commercial',
     'company',
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
 6: {'100',
     'aged',
     'agent',
     'agreement',
     'alta',
     'annualized',
     'approved',
     'apr',
     'arbitrage',
     'assignment',
     'automated',
     'avoiding',
     'b2b',
     'bank',
     'before',
     'bridge',
     'building',
     'business',
     'buyer',
     'callback',
     'cancellation',
     'capital',
     'card',
     'charging',
     'checklists',
     'clearing',
     'client',
     'close',
     'closing',
     'commercial',
     'company',
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
 7: {'100',
     'aged',
     'agent',
     'agreement',
     'alta',
     'annualized',
     'approved',
     'apr',
     'arbitrage',
     'assignment',
     'automated',
     'avoiding',
     'b2b',
     'bank',
     'before',
     'bridge',
     'building',
     'business',
     'buyer',
     'callback',
     'cancellation',
     'capital',
     'card',
     'charging',
     'checklist',
     'checklists',
     'clearing',
     'close',
     'closing',
     'commercial',
     'company',
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
 8: {'100',
     'aged',
     'agent',
     'agreement',
     'alta',
     'annualized',
     'api',
     'approved',
     'apr',
     'arbitrage',
     'assignment',
     'automated',
     'avoiding',
     'b2b',
     'bank',
     'before',
     'bridge',
     'building',
     'business',
     'buyer',
     'callback',
     'cancellation',
     'capital',
     'card',
     'charging',
     'checklists',
     'clearing',
     'close',
     'closing',
     'commercial',
     'company',
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
 9: {'100',
     'aged',
     'agent',
     'agreement',
     'alta',
     'annualized',
     'approved',
     'apr',
     'arbitrage',
     'assignment',
     'automated',
     'avoiding',
     'b2b',
     'bank',
     'before',
     'bridge',
     'building',
     'business',
     'buyer',
     'callback',
     'cancellation',
     'capital',
     'card',
     'charging',
     'checklists',
     'clearing',
     'close',
     'closing',
     'commercial',
     'company',
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
 10: {'100',
      'aged',
      'agent',
      'agreement',
      'ai',
      'alta',
      'annualized',
      'approved',
      'apr',
      'arbitrage',
      'assignment',
      'automate',
      'automated',
      'automation',
      'avoiding',
      'b2b',
      'bank',
      'before',
      'bridge',
      'building',
      'business',
      'buyer',
      'callback',
      'cancellation',
      'capital',
      'card',
      'charging',
      'checklists',
      'clearing',
      'close',
      'closing',
      'commercial',
      'company',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'100',
      'aged',
      'agent',
      'agreement',
      'alta',
      'annualized',
      'approved',
      'apr',
      'arbitrage',
      'assignment',
      'automated',
      'avoiding',
      'b2b',
      'bank',
      'before',
      'bridge',
      'building',
      'business',
      'buyer',
      'callback',
      'cancellation',
      'capital',
      'card',
      'charging',
      'checklists',
      'clearing',
      'close',
      'closing',
      'commercial',
      'company',
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
 12: {'100',
      'action',
      'aged',
      'agent',
      'agreement',
      'alta',
      'annualized',
      'approved',
      'apr',
      'arbitrage',
      'assignment',
      'automated',
      'avoiding',
      'b2b',
      'bank',
      'before',
      'bridge',
      'building',
      'business',
      'buyer',
      'callback',
      'cancellation',
      'capital',
      'card',
      'charging',
      'checklists',
      'clearing',
      'close',
      'closing',
      'commercial',
      'company',
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
      'markdown': '[00:06:57](https://www.youtube.com/watch?v=LktXzMB-Sis&t=417s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That means that you got to go with Chase first before you touch any other bank '
              'while your Experian report is still completely clean. Apply for the Chase Ink '
              'Unlimited first. So, get approved and activate it. Then a few days later, you '
              'want to apply for a second card.',
      'timestamp': 417,
      'timestamp_label': '[00:06:57]',
      'timestamp_seconds': 417,
      'tip': 'That means that you got to go with Chase first before you touch any other bank '
             'while your Experian report is still completely clean. Apply for the Chase Ink '
             'Unlimited first. So, get approved and activate it. Then a few days later, you '
             'want to apply for a second card.',
      'title': 'The $100,000 Business Credit LOOPHOLE That Feels ILLEGAL (But Works) (Naam '
               'Wynn)',
      'url': 'https://www.youtube.com/watch?v=LktXzMB-Sis&t=417s',
      'video_id': 'LktXzMB-Sis'},
     {'author': 'Lex Levinrad Real Estate Training and Coaching',
      'channel': 'Lex Levinrad Real Estate Training and Coaching',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:27](https://www.youtube.com/watch?v=ogZEBPqsJc4&t=147s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now another big reason why you want to consider double closing and we double '
              'close almost all of our deals. And this is because right now, towards the end '
              "of 2021 you're going to be seeing an abundance of foreclosure, short sales bank "
              'on properties coming around the market.',
      'timestamp': 147,
      'timestamp_label': '[00:02:27]',
      'timestamp_seconds': 147,
      'tip': 'Now another big reason why you want to consider double closing and we double '
             'close almost all of our deals. And this is because right now, towards the end of '
             "2021 you're going to be seeing an abundance of foreclosure, short sales bank on "
             'properties coming around the market.',
      'title': 'Assignment of Contract Or Double Closing For Wholesaling (Lex Levinrad Real '
               'Estate Training and Coaching)',
      'url': 'https://www.youtube.com/watch?v=ogZEBPqsJc4&t=147s',
      'video_id': 'ogZEBPqsJc4'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:55](https://www.youtube.com/watch?v=aIHVhFGaNAw&t=1735s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Those are your three clients. So, Scott\'s asking, "Well, why doesn\'t your '
              'buyer, your client, just go to a bank?" Well, first off, nobody in real estate '
              'goes to banks. Well, because they go through an arduous, tedious process and '
              'their timing is atrocious.',
      'timestamp': 1735,
      'timestamp_label': '[00:28:55]',
      'timestamp_seconds': 1735,
      'tip': 'Those are your three clients. So, Scott\'s asking, "Well, why doesn\'t your '
             'buyer, your client, just go to a bank?" Well, first off, nobody in real estate '
             'goes to banks. Well, because they go through an arduous, tedious process and '
             'their timing is atrocious.',
      'title': 'The Easiest Way to Make Money in Real Estate (That No One Talks About) (Pace '
               'Morby)',
      'url': 'https://www.youtube.com/watch?v=aIHVhFGaNAw&t=1735s',
      'video_id': 'aIHVhFGaNAw'},
     {'author': 'The Mortgage Man - Steve Ferguson',
      'channel': 'The Mortgage Man - Steve Ferguson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:12](https://www.youtube.com/watch?v=AGFnuSOGL68&t=192s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re enjoying your time, your home will get listed with a listing agent and "
              "you'll market it. Hopefully, it will get sold in four months or less. But if "
              'for some reason it has not sold in four months or less, the bridge loan program '
              'will take ownership of your property.',
      'timestamp': 192,
      'timestamp_label': '[00:03:12]',
      'timestamp_seconds': 192,
      'tip': "'re enjoying your time, your home will get listed with a listing agent and "
             "you'll market it. Hopefully, it will get sold in four months or less. But if for "
             'some reason it has not sold in four months or less, the bridge loan program will '
             'take ownership of your property.',
      'title': 'Bridge Loans Explained: How to Buy Your Next Home Before Selling Your Current '
               'One (The Mortgage Man - Steve Ferguson)',
      'url': 'https://www.youtube.com/watch?v=AGFnuSOGL68&t=192s',
      'video_id': 'AGFnuSOGL68'},
     {'author': 'Stephen Smith',
      'channel': 'Stephen Smith',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:24](https://www.youtube.com/watch?v=UuM0MLm-2DU&t=864s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Currently, we are on firsthorizon. 're looking at the Visa small business "
              'credit card. Now, with this one, you can get credit lines up to $50,000. You '
              'also get 0% APR on purchases for the first 6 months following account opening.',
      'timestamp': 864,
      'timestamp_label': '[00:14:24]',
      'timestamp_seconds': 864,
      'tip': "Currently, we are on firsthorizon. 're looking at the Visa small business credit "
             'card. Now, with this one, you can get credit lines up to $50,000. You also get '
             '0% APR on purchases for the first 6 months following account opening.',
      'title': 'How to Get 40 Business Credit Cards for a Startup | 0% APR (1M+ in Credit) '
               '(Stephen Smith)',
      'url': 'https://www.youtube.com/watch?v=UuM0MLm-2DU&t=864s',
      'video_id': 'UuM0MLm-2DU'},
     {'author': 'Velocity Advantage Capital',
      'channel': 'Velocity Advantage Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=HGfRd2Z2i24&t=43s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Uh sometimes they were available, sometimes they didn't have the capital "
              'available. So that was a huge uh roadblock bottleneck to our business uh real '
              'estate or wholesaling business. And then the other side of it was the actual uh '
              'fees and charges for double closing.',
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': "Uh sometimes they were available, sometimes they didn't have the capital "
             'available. So that was a huge uh roadblock bottleneck to our business uh real '
             'estate or wholesaling business. And then the other side of it was the actual uh '
             'fees and charges for double closing.',
      'title': 'Transactional Funding And Double Closings—What You Need To Know (Velocity '
               'Advantage Capital)',
      'url': 'https://www.youtube.com/watch?v=HGfRd2Z2i24&t=43s',
      'video_id': 'HGfRd2Z2i24'},
     {'author': 'Sure Flow Capital Partners',
      'channel': 'Sure Flow Capital Partners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=9HWpfZS4eQM&t=42s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Money that often never even leaves escrow. So, a transaction can close with '
              'little to none of your own cash. You are the operator running the deal. They do '
              'their job inside the closing and the deal gets done. Now, notice what I just '
              'said. The money often never leaves escrow.',
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': 'Money that often never even leaves escrow. So, a transaction can close with '
             'little to none of your own cash. You are the operator running the deal. They do '
             'their job inside the closing and the deal gets done. Now, notice what I just '
             'said. The money often never leaves escrow.',
      'title': 'How to Fund Seller Carryback Deals with Transactional Funding (Sure Flow '
               'Capital Partners)',
      'url': 'https://www.youtube.com/watch?v=9HWpfZS4eQM&t=42s',
      'video_id': '9HWpfZS4eQM'},
     {'author': 'Hard Money Mastermind',
      'channel': 'Hard Money Mastermind',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:32](https://www.youtube.com/watch?v=9ISIUnJvomU&t=392s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Business model and hopefully everyone you know in the audience watch watching '
              'or listening like knows the power of it but like for the amount of hours that '
              'go.',
      'timestamp': 392,
      'timestamp_label': '[00:06:32]',
      'timestamp_seconds': 392,
      'tip': 'Business model and hopefully everyone you know in the audience watch watching or '
             'listening like knows the power of it but like for the amount of hours that go.',
      'title': 'Scaling A Private Lending Company with Daniel Paloscio from SEP Capital in '
               'Tampa, FL #realestate (Hard Money Mastermind)',
      'url': 'https://www.youtube.com/watch?v=9ISIUnJvomU&t=392s',
      'video_id': '9ISIUnJvomU'},
     {'author': 'The Conversation Capital',
      'channel': 'The Conversation Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:51:44](https://www.youtube.com/watch?v=nU-tvSUTP8g&t=3104s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re putting their rents and cents in to say if they can save a 100 rand towards "
              'another service, how then do we help them save that but get actually the '
              "ultimate benefit or whatever they're looking for. So those are some of the "
              "things that we're doing through Flexi.",
      'timestamp': 3104,
      'timestamp_label': '[00:51:44]',
      'timestamp_seconds': 3104,
      'tip': "'re putting their rents and cents in to say if they can save a 100 rand towards "
             'another service, how then do we help them save that but get actually the '
             "ultimate benefit or whatever they're looking for. So those are some of the "
             "things that we're doing through Flexi.",
      'title': 'Scaling Small Businesses: The Secret To Closing The Funding Gap (The '
               'Conversation Capital)',
      'url': 'https://www.youtube.com/watch?v=nU-tvSUTP8g&t=3104s',
      'video_id': 'nU-tvSUTP8g'},
     {'author': 'Investor Army',
      'channel': 'Investor Army',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:53](https://www.youtube.com/watch?v=ltZrMvVSfdw&t=53s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "$100,000 so once you've fixed up the house and it's all shiny and new it could "
              "sell for $100,000 as far as appraised value it's going to take.",
      'timestamp': 53,
      'timestamp_label': '[00:00:53]',
      'timestamp_seconds': 53,
      'tip': "$100,000 so once you've fixed up the house and it's all shiny and new it could "
             "sell for $100,000 as far as appraised value it's going to take.",
      'title': 'Promissory Note, Deed Of Trust, and Deed Explained (Investor Army)',
      'url': 'https://www.youtube.com/watch?v=ltZrMvVSfdw&t=53s',
      'video_id': 'ltZrMvVSfdw'},
     {'author': 'Hard Money Mike',
      'channel': 'Hard Money Mike',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:06](https://www.youtube.com/watch?v=QMbtBhGx9os&t=66s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Number four is loan to value how much will they lend you hard money lenders in '
              'this market at the end of 2022 will lend you up to 90 percent of the purchase '
              'and.',
      'timestamp': 66,
      'timestamp_label': '[00:01:06]',
      'timestamp_seconds': 66,
      'tip': 'Number four is loan to value how much will they lend you hard money lenders in '
             'this market at the end of 2022 will lend you up to 90 percent of the purchase '
             'and.',
      'title': 'COMPARE: Hard Money vs DSCR - Which is the Better Option for You? (Hard Money '
               'Mike)',
      'url': 'https://www.youtube.com/watch?v=QMbtBhGx9os&t=66s',
      'video_id': 'QMbtBhGx9os'},
     {'author': 'Julee Felsman | Workshop Team | Guaranteed Rate',
      'channel': 'Julee Felsman | Workshop Team | Guaranteed Rate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:10](https://www.youtube.com/watch?v=faIlHE0Vtco&t=1150s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Oregon check out the other videos in this playlist and if you're in the market "
              'for a lender my contact information is in the description below I would love to '
              'talk.',
      'timestamp': 1150,
      'timestamp_label': '[00:19:10]',
      'timestamp_seconds': 1150,
      'tip': "Oregon check out the other videos in this playlist and if you're in the market "
             'for a lender my contact information is in the description below I would love to '
             'talk.',
      'title': 'Property Taxes at Closing in Oregon | What are Prorations, Escrow Deposits, '
               'Hold & Pay? (Julee Felsman | Workshop Team | Guaranteed Rate)',
      'url': 'https://www.youtube.com/watch?v=faIlHE0Vtco&t=1150s',
      'video_id': 'faIlHE0Vtco'},
     {'author': 'Andrew Finney Team',
      'channel': 'Andrew Finney Team',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:54](https://www.youtube.com/watch?v=ND7J57hzroE&t=294s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'To the appraised value or to either cut it in half and you come up five they go '
              'down five whatever have you whatever the circumstances are that would make '
              'sense.',
      'timestamp': 294,
      'timestamp_label': '[00:04:54]',
      'timestamp_seconds': 294,
      'tip': 'To the appraised value or to either cut it in half and you come up five they go '
             'down five whatever have you whatever the circumstances are that would make '
             'sense.',
      'title': 'How To Protect Your Earnest Money Deposit! (Andrew Finney Team)',
      'url': 'https://www.youtube.com/watch?v=ND7J57hzroE&t=294s',
      'video_id': 'ND7J57hzroE'},
     {'author': 'LearnREInvesting',
      'channel': 'LearnREInvesting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=l-l8leRQ_KE&t=89s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Besttransactionalfunding.com for all your same day double closing needs '
              'including a list of investor friendly closing agents in various States we have '
              'more five-star Google ratings than all the other transactional funders '
              'combined.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': 'Besttransactionalfunding.com for all your same day double closing needs '
             'including a list of investor friendly closing agents in various States we have '
             'more five-star Google ratings than all the other transactional funders combined.',
      'title': 'Real Estate Investing - What Upfront Fees are there for Transactional Funding? '
               '(LearnREInvesting)',
      'url': 'https://www.youtube.com/watch?v=l-l8leRQ_KE&t=89s',
      'video_id': 'l-l8leRQ_KE'},
     {'author': 'FlipThisWholesaler',
      'channel': 'FlipThisWholesaler',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:08](https://www.youtube.com/watch?v=FOfp5iWKVkc&t=368s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Gets too confusing for me to go back and forth from Facebook to YouTube to my '
              "blog answering questions so if you're on YouTube and you have a question or "
              'comment you can go to my blog it is flip this wholesaler.com.',
      'timestamp': 368,
      'timestamp_label': '[00:06:08]',
      'timestamp_seconds': 368,
      'tip': 'Gets too confusing for me to go back and forth from Facebook to YouTube to my '
             "blog answering questions so if you're on YouTube and you have a question or "
             'comment you can go to my blog it is flip this wholesaler.com.',
      'title': 'Wholesaling Real Estate: How to Get a Proof of Funds Letter '
               '(FlipThisWholesaler)',
      'url': 'https://www.youtube.com/watch?v=FOfp5iWKVkc&t=368s',
      'video_id': 'FOfp5iWKVkc'}],
 2: [{'author': 'Suzanne & Chad Team: CPA + Realtors',
      'channel': 'Suzanne & Chad Team: CPA + Realtors',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:42](https://www.youtube.com/watch?v=ImGiAjG57s0&t=282s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "One of the last fees that is paid for by the seller is for the title company's "
              'fee for providing their services. Now, this is a good segue into buyers closing '
              'costs because the buyer typically also has a fee that they pay to the title '
              'company for their title services.',
      'timestamp': 282,
      'timestamp_label': '[00:04:42]',
      'timestamp_seconds': 282,
      'tip': "One of the last fees that is paid for by the seller is for the title company's "
             'fee for providing their services. Now, this is a good segue into buyers closing '
             'costs because the buyer typically also has a fee that they pay to the title '
             'company for their title services.',
      'title': 'Who Pays Closing Costs in Florida? Buyer vs Seller Breakdown (Full Guide) '
               '(Suzanne & Chad Team: CPA + Realtors)',
      'url': 'https://www.youtube.com/watch?v=ImGiAjG57s0&t=282s',
      'video_id': 'ImGiAjG57s0'},
     {'author': 'Fuel My Deal',
      'channel': 'Fuel My Deal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:46](https://www.youtube.com/watch?v=y5I0Ma11ptA&t=46s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t see exactly what you're making. And third, when you need to show credibility "
              'at the closing table by being the actual buyer of record. Let me give you a '
              'quick example. You contract a property for $100,000 with the seller. You find '
              'an end buyer willing to pay $115,000.',
      'timestamp': 46,
      'timestamp_label': '[00:00:46]',
      'timestamp_seconds': 46,
      'tip': "'t see exactly what you're making. And third, when you need to show credibility "
             'at the closing table by being the actual buyer of record. Let me give you a '
             'quick example. You contract a property for $100,000 with the seller. You find an '
             'end buyer willing to pay $115,000.',
      'title': 'What Is Transactional Funding? Double Close Explained for Real Estate '
               'Investors (Fuel My Deal)',
      'url': 'https://www.youtube.com/watch?v=y5I0Ma11ptA&t=46s',
      'video_id': 'y5I0Ma11ptA'},
     {'author': 'Sure Flow Capital Partners',
      'channel': 'Sure Flow Capital Partners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:03](https://www.youtube.com/watch?v=AsVTF7HImUo&t=123s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, let's go over how a double close would work. Let's go through a simple "
              'example. You contract a property from a seller for 100,000. You find the end '
              "buyer who's willing to pay that 120,000. In a double close, there's two "
              'transactions.',
      'timestamp': 123,
      'timestamp_label': '[00:02:03]',
      'timestamp_seconds': 123,
      'tip': "So, let's go over how a double close would work. Let's go through a simple "
             'example. You contract a property from a seller for 100,000. You find the end '
             "buyer who's willing to pay that 120,000. In a double close, there's two "
             'transactions.',
      'title': '🚀 What Is Transactional Funding? How to Close Deals When Your Cash Is Tied Up '
               '(Sure Flow Capital Partners)',
      'url': 'https://www.youtube.com/watch?v=AsVTF7HImUo&t=123s',
      'video_id': 'AsVTF7HImUo'},
     {'author': 'Escrow Escapes',
      'channel': 'Escrow Escapes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:03](https://www.youtube.com/watch?v=kfe6mMfaivM&t=423s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your agent gets the contract question, who agreed to pay this? And where does '
              'the contract address it? If there is a special assessment, ask when it was '
              'approved, whether it was disclosed, what it funds, and whether responsibility '
              'was assigned in writing.',
      'timestamp': 423,
      'timestamp_label': '[00:07:03]',
      'timestamp_seconds': 423,
      'tip': 'Your agent gets the contract question, who agreed to pay this? And where does '
             'the contract address it? If there is a special assessment, ask when it was '
             'approved, whether it was disclosed, what it funds, and whether responsibility '
             'was assigned in writing.',
      'title': 'The Proration Surprise: When Property Taxes and HOA Fees Change the Closing '
               'Math (Escrow Escapes)',
      'url': 'https://www.youtube.com/watch?v=kfe6mMfaivM&t=423s',
      'video_id': 'kfe6mMfaivM'},
     {'author': 'Kristie Dimarakis',
      'channel': 'Kristie Dimarakis',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=NwZ7Oa8GUXQ&t=92s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'These contingency help protect your deposit if something unexpectedly happens '
              'and you need to back out of the contract. Also, it is always best to work with '
              'your agent and the escrow officer to see what your best options are for '
              'payment.',
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': 'These contingency help protect your deposit if something unexpectedly happens '
             'and you need to back out of the contract. Also, it is always best to work with '
             'your agent and the escrow officer to see what your best options are for payment.',
      'title': 'How to Protect Your Earnest Money Deposit When Buying a Home 🛑💸 (Kristie '
               'Dimarakis)',
      'url': 'https://www.youtube.com/watch?v=NwZ7Oa8GUXQ&t=92s',
      'video_id': 'NwZ7Oa8GUXQ'},
     {'author': 'James Brinkman',
      'channel': 'James Brinkman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:13](https://www.youtube.com/watch?v=NqrtD90l6pk&t=73s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'These contingencies help protect your deposit if something unexpected happens '
              'and you need to back out of the contract. Also, it is always best to work with '
              'your agent and escrow officer to see what are your best options for payment.',
      'timestamp': 73,
      'timestamp_label': '[00:01:13]',
      'timestamp_seconds': 73,
      'tip': 'These contingencies help protect your deposit if something unexpected happens '
             'and you need to back out of the contract. Also, it is always best to work with '
             'your agent and escrow officer to see what are your best options for payment.',
      'title': "Don't Lose Your Deposit! Protect Your Earnest Money When Buying a Home (James "
               'Brinkman)',
      'url': 'https://www.youtube.com/watch?v=NqrtD90l6pk&t=73s',
      'video_id': 'NqrtD90l6pk'},
     {'author': "Scott Horne's Owner Finance Network",
      'channel': "Scott Horne's Owner Finance Network",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:44](https://www.youtube.com/watch?v=XdrwPF-D1FI&t=224s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A survey that is required by the lender is going to be a a a fee for the loan '
              "cuz in other words you can't get the loan without having these things done "
              'along the way. Closing costs at a title company are not lender fees.',
      'timestamp': 224,
      'timestamp_label': '[00:03:44]',
      'timestamp_seconds': 224,
      'tip': 'A survey that is required by the lender is going to be a a a fee for the loan '
             "cuz in other words you can't get the loan without having these things done along "
             'the way. Closing costs at a title company are not lender fees.',
      'title': 'Usury Laws Explained (Avoid Illegal Interest Rates + Fee Traps) | Scott Horne '
               "(Scott Horne's Owner Finance Network)",
      'url': 'https://www.youtube.com/watch?v=XdrwPF-D1FI&t=224s',
      'video_id': 'XdrwPF-D1FI'},
     {'author': 'Real Estate Wealth Network',
      'channel': 'Real Estate Wealth Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=m77TLPPF8KA&t=87s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '50,000 on the assignment fee and she flipped out and she decided, "No, they\'re '
              'making 50,000. " And I said, "See, that\'s why I just rather do, you know, the '
              'double closing, the concurrent.".',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': '50,000 on the assignment fee and she flipped out and she decided, "No, they\'re '
             'making 50,000. " And I said, "See, that\'s why I just rather do, you know, the '
             'double closing, the concurrent.".',
      'title': 'Transactional Funding for Wholesalers | Funding for ZERO Fees! (Real Estate '
               'Wealth Network)',
      'url': 'https://www.youtube.com/watch?v=m77TLPPF8KA&t=87s',
      'video_id': 'm77TLPPF8KA'},
     {'author': 'Think Escrow!',
      'channel': 'Think Escrow!',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:24](https://www.youtube.com/watch?v=f-7Rw_JAZOA&t=204s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Proceeds Wired from the sale the title company and the settlement agent collect '
              'these monies and so they pay them according to the escro process it is a.',
      'timestamp': 204,
      'timestamp_label': '[00:03:24]',
      'timestamp_seconds': 204,
      'tip': 'Proceeds Wired from the sale the title company and the settlement agent collect '
             'these monies and so they pay them according to the escro process it is a.',
      'title': 'Threats to Escrow! Part 1 - Wire Fraud! The most prevalent threat to your '
               'escrow transaction (Think Escrow!)',
      'url': 'https://www.youtube.com/watch?v=f-7Rw_JAZOA&t=204s',
      'video_id': 'f-7Rw_JAZOA'},
     {'author': 'Beyond the Address',
      'channel': 'Beyond the Address',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:49](https://www.youtube.com/watch?v=1ysRoNF77u8&t=49s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If everything goes smoothly, it gets applied towards your down payment or '
              'closing costs. But if you back out without a valid reason, like a contingency '
              'in your contract, you could lose that money. The seller could have the right to '
              'your deposit for the breach in contract.',
      'timestamp': 49,
      'timestamp_label': '[00:00:49]',
      'timestamp_seconds': 49,
      'tip': 'If everything goes smoothly, it gets applied towards your down payment or '
             'closing costs. But if you back out without a valid reason, like a contingency in '
             'your contract, you could lose that money. The seller could have the right to '
             'your deposit for the breach in contract.',
      'title': 'What Is an Earnest Money Deposit? (And How to Protect It) (Beyond the Address)',
      'url': 'https://www.youtube.com/watch?v=1ysRoNF77u8&t=49s',
      'video_id': '1ysRoNF77u8'},
     {'author': 'Real Estate Finance Academy with Trevor Calton',
      'channel': 'Real Estate Finance Academy with Trevor Calton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:27](https://www.youtube.com/watch?v=Z-MpltBp8qA&t=207s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Default is when the terms of the note have been violated by either non-payment '
              "or what we call technical default. When say the borrower doesn't maintain the "
              'property to the appropriate levels or fails to pay their property taxes.',
      'timestamp': 207,
      'timestamp_label': '[00:03:27]',
      'timestamp_seconds': 207,
      'tip': 'Default is when the terms of the note have been violated by either non-payment '
             "or what we call technical default. When say the borrower doesn't maintain the "
             'property to the appropriate levels or fails to pay their property taxes.',
      'title': 'Promissory Notes Explained: What Borrowers Actually Sign (And Why It Matters) '
               '(Real Estate Finance Academy with Trevor Calton)',
      'url': 'https://www.youtube.com/watch?v=Z-MpltBp8qA&t=207s',
      'video_id': 'Z-MpltBp8qA'},
     {'author': 'Inland Professional Title LLC',
      'channel': 'Inland Professional Title LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:53](https://www.youtube.com/watch?v=JExnsYGsNd8&t=293s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Basics of that and then we'll go into escrow collection so please tune in again "
              'next thursday to hear about the real estate contract thank you for using ipt '
              'and I look forward to seeing you next week.',
      'timestamp': 293,
      'timestamp_label': '[00:04:53]',
      'timestamp_seconds': 293,
      'tip': "Basics of that and then we'll go into escrow collection so please tune in again "
             'next thursday to hear about the real estate contract thank you for using ipt and '
             'I look forward to seeing you next week.',
      'title': 'Seller Financing: Note and Deed of Trust (Inland Professional Title LLC)',
      'url': 'https://www.youtube.com/watch?v=JExnsYGsNd8&t=293s',
      'video_id': 'JExnsYGsNd8'},
     {'author': 'LearnREInvesting',
      'channel': 'LearnREInvesting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:26](https://www.youtube.com/watch?v=BbugvWp8qsA&t=26s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Minimum fee no processing fee virtually instant approval a simple one-page '
              'funding agreement same day double closings only one day rate is 1% of the.',
      'timestamp': 26,
      'timestamp_label': '[00:00:26]',
      'timestamp_seconds': 26,
      'tip': 'Minimum fee no processing fee virtually instant approval a simple one-page '
             'funding agreement same day double closings only one day rate is 1% of the.',
      'title': 'Transactional Funding In Tennessee Net Profit $30,070.71 No Money Deal '
               '(LearnREInvesting)',
      'url': 'https://www.youtube.com/watch?v=BbugvWp8qsA&t=26s',
      'video_id': 'BbugvWp8qsA'},
     {'author': 'Kaminsky Real Estate Group',
      'channel': 'Kaminsky Real Estate Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:03](https://www.youtube.com/watch?v=p5RGCN-UQL8&t=123s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Purchase price the reason is most commonly three percent of the purchase price '
              'is because of the liquidated damages clause I will give you some tips on '
              'liquidated damages and another episode of ed gives you tips on the real estate '
              'purchase contract thanks for watching.',
      'timestamp': 123,
      'timestamp_label': '[00:02:03]',
      'timestamp_seconds': 123,
      'tip': 'Purchase price the reason is most commonly three percent of the purchase price '
             'is because of the liquidated damages clause I will give you some tips on '
             'liquidated damages and another episode of ed gives you tips on the real estate '
             'purchase contract thanks for watching.',
      'title': 'How To Protect Your Earnest Money Deposit When Buying a Home | Homebuyer '
               'Questions (Kaminsky Real Estate Group)',
      'url': 'https://www.youtube.com/watch?v=p5RGCN-UQL8&t=123s',
      'video_id': 'p5RGCN-UQL8'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:30](https://www.youtube.com/watch?v=qbBAO0ozP-0&t=750s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That urgency little tricks hi Kelly my name is Pace morby how are you doing I'm "
              "so good hey we're opening up escrow with you guys on a sub 2 deal with Carolyn "
              "Myron I'm not sure if you saw the contract already.",
      'timestamp': 750,
      'timestamp_label': '[00:12:30]',
      'timestamp_seconds': 750,
      'tip': "That urgency little tricks hi Kelly my name is Pace morby how are you doing I'm "
             "so good hey we're opening up escrow with you guys on a sub 2 deal with Carolyn "
             "Myron I'm not sure if you saw the contract already.",
      'title': 'Contracts for Earnest Money Deposits | Gator Method (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=qbBAO0ozP-0&t=750s',
      'video_id': 'qbBAO0ozP-0'}],
 3: [{'author': 'Brett Flory',
      'channel': 'Brett Flory',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=QQEovor5ZiA&t=68s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re not using your own cash, just leverage and timing. So, why use "
              "transactional funding? It allows you to close deals where assignment isn't "
              'allowed. It protects your profit margins by keeping the original purchase price '
              'private. And it gives you credibility.',
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': "'re not using your own cash, just leverage and timing. So, why use transactional "
             "funding? It allows you to close deals where assignment isn't allowed. It "
             'protects your profit margins by keeping the original purchase price private. And '
             'it gives you credibility.',
      'title': 'How to Use Transactional Funding to Close Wholesale Real Estate Deals! (Brett '
               'Flory)',
      'url': 'https://www.youtube.com/watch?v=QQEovor5ZiA&t=68s',
      'video_id': 'QQEovor5ZiA'},
     {'author': 'Katie Anderson | PENSACOLA AREA REALTOR ',
      'channel': 'Katie Anderson | PENSACOLA AREA REALTOR ',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=NMjK2yG_6ys&t=56s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Either we cancel the contract, and that's the unfortunate case sometimes, or we "
              'close on the contract. On closing day, that earnest money goes right back '
              "towards that purchase price and towards your closing costs if you're the buyer.",
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': "Either we cancel the contract, and that's the unfortunate case sometimes, or we "
             'close on the contract. On closing day, that earnest money goes right back '
             "towards that purchase price and towards your closing costs if you're the buyer.",
      'title': 'Earnest Money Deposit (EMD): Where It Goes and What Happens If You Cancel '
               '(Katie Anderson | PENSACOLA AREA REALTOR )',
      'url': 'https://www.youtube.com/watch?v=NMjK2yG_6ys&t=56s',
      'video_id': 'NMjK2yG_6ys'},
     {'author': 'Easy Lending USA',
      'channel': 'Easy Lending USA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=GcefOZxHIAg&t=163s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "A conventional loan can't close that fast. So the investor uses a bridge loan. "
              'At seventy-five percent of value, the bridge loan is three hundred thousand '
              "dollars. That leaves about one hundred thousand of the investor's own cash, "
              'plus closing costs.',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': "A conventional loan can't close that fast. So the investor uses a bridge loan. "
             'At seventy-five percent of value, the bridge loan is three hundred thousand '
             "dollars. That leaves about one hundred thousand of the investor's own cash, plus "
             'closing costs.',
      'title': "Hard Money vs Bridge Loans (2026): What's the Difference? (Easy Lending USA)",
      'url': 'https://www.youtube.com/watch?v=GcefOZxHIAg&t=163s',
      'video_id': 'GcefOZxHIAg'},
     {'author': 'David Olds REI',
      'channel': 'David Olds REI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=oXZTulq2Qx0&t=117s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Another ,000 or $2,000 so now you're up to 106,000 right 100 plus 6,000 in "
              "closing costs 120us 106 your profit is only 14,000 so what's the difference.",
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': "Another ,000 or $2,000 so now you're up to 106,000 right 100 plus 6,000 in "
             "closing costs 120us 106 your profit is only 14,000 so what's the difference.",
      'title': 'Demystifying Wholesaling: Assignment vs Double Close | Real Estate Insights '
               'with David Olds 🏡💰 (David Olds REI)',
      'url': 'https://www.youtube.com/watch?v=oXZTulq2Qx0&t=117s',
      'video_id': 'oXZTulq2Qx0'},
     {'author': 'Fast Business Lending',
      'channel': 'Fast Business Lending',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=-EPbq7NKBZY&t=126s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Holding that remaining $30,000 in reserve costs you absolutely nothing. If you '
              'take this $20,000 draw from a traditional bank and pay it back over a 6-month '
              'term, the bank uses a prime rate plus a margin formula. That keeps your total '
              'interest cost to roughly $583.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': 'Holding that remaining $30,000 in reserve costs you absolutely nothing. If you '
             'take this $20,000 draw from a traditional bank and pay it back over a 6-month '
             'term, the bank uses a prime rate plus a margin formula. That keeps your total '
             'interest cost to roughly $583.',
      'title': 'Best Business Lines of Credit in 2027 (A Loan Officer Ranks 7) (Fast Business '
               'Lending)',
      'url': 'https://www.youtube.com/watch?v=-EPbq7NKBZY&t=126s',
      'video_id': '-EPbq7NKBZY'},
     {'author': 'Fund My Real Estate Deal',
      'channel': 'Fund My Real Estate Deal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:02](https://www.youtube.com/watch?v=yWKbp0xDuE8&t=1142s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Paying for all these sites you need to get your rental business up and running. '
              'That profit margin that they receive off of these stack method deals, that can '
              'go towards that at a much smaller cost. And by the way, this is debt.',
      'timestamp': 1142,
      'timestamp_label': '[00:19:02]',
      'timestamp_seconds': 1142,
      'tip': 'Paying for all these sites you need to get your rental business up and running. '
             'That profit margin that they receive off of these stack method deals, that can '
             'go towards that at a much smaller cost. And by the way, this is debt.',
      'title': 'Transactional Lender Reveals How to Close Deals Fast (Fund My Real Estate '
               'Deal)',
      'url': 'https://www.youtube.com/watch?v=yWKbp0xDuE8&t=1142s',
      'video_id': 'yWKbp0xDuE8'},
     {'author': 'Vertical Capital',
      'channel': 'Vertical Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:31](https://www.youtube.com/watch?v=5a6OhvT6Dcw&t=511s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This EMD goes towards the purchase price or the sales price. For example, today '
              'you write a check to the title company for 123 Magazine Street, any amount of '
              '$1,000. On the date of the closing, the $1,000 is subtracted from the final '
              'closing cost.',
      'timestamp': 511,
      'timestamp_label': '[00:08:31]',
      'timestamp_seconds': 511,
      'tip': 'This EMD goes towards the purchase price or the sales price. For example, today '
             'you write a check to the title company for 123 Magazine Street, any amount of '
             '$1,000. On the date of the closing, the $1,000 is subtracted from the final '
             'closing cost.',
      'title': 'What Is Transactional Funding and How Does It Work? (Vertical Capital)',
      'url': 'https://www.youtube.com/watch?v=5a6OhvT6Dcw&t=511s',
      'video_id': '5a6OhvT6Dcw'},
     {'author': 'RJ Baxter - NEO Home Loans',
      'channel': 'RJ Baxter - NEO Home Loans',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=XH6IkQFi_8M&t=118s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Some banks don't like that. However, some banks are fine with it. You need to "
              "ask them if there's a prepayment penalty. But in a lot of cases, the prepayment "
              "penalty plus the home equity line closing costs are a lot less than you're "
              'going to pay on a traditional bridge loan.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': "Some banks don't like that. However, some banks are fine with it. You need to "
             "ask them if there's a prepayment penalty. But in a lot of cases, the prepayment "
             "penalty plus the home equity line closing costs are a lot less than you're going "
             'to pay on a traditional bridge loan.',
      'title': 'Don’t Use a Bridge Loan Until You Watch This (RJ Baxter - NEO Home Loans)',
      'url': 'https://www.youtube.com/watch?v=XH6IkQFi_8M&t=118s',
      'video_id': 'XH6IkQFi_8M'},
     {'author': 'Adam Dobrinich | East Bay Realtor',
      'channel': 'Adam Dobrinich | East Bay Realtor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=SmGAUIMTEyI&t=126s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Don't have time to wipe things down I can refer you to a cleaning company "
              'usually cost about a couple hundred to uh get the place cleaned up and so if.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': "Don't have time to wipe things down I can refer you to a cleaning company "
             'usually cost about a couple hundred to uh get the place cleaned up and so if.',
      'title': 'Seller Escrow Process Step Ten | Loan Funded/ Closing (Adam Dobrinich | East '
               'Bay Realtor)',
      'url': 'https://www.youtube.com/watch?v=SmGAUIMTEyI&t=126s',
      'video_id': 'SmGAUIMTEyI'},
     {'author': 'Clicks Geek',
      'channel': 'Clicks Geek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=cgY-PRTdUB4&t=65s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The coaching and sales programs that they're sold right takes no money which is "
              "true you can come to people like me and we'll put up a 100% of the cash and.",
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': "The coaching and sales programs that they're sold right takes no money which is "
             "true you can come to people like me and we'll put up a 100% of the cash and.",
      'title': 'Transactional Funding For Wholesaling (Clicks Geek)',
      'url': 'https://www.youtube.com/watch?v=cgY-PRTdUB4&t=65s',
      'video_id': 'cgY-PRTdUB4'},
     {'author': 'FlipThisWholesaler',
      'channel': 'FlipThisWholesaler',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:44](https://www.youtube.com/watch?v=FUjDeT5p55I&t=44s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Agent told me I need a proof of funds letter to submit with my offer if I'm "
              'making a cash offer will a letter from a transactional funding source work '
              "I've.",
      'timestamp': 44,
      'timestamp_label': '[00:00:44]',
      'timestamp_seconds': 44,
      'tip': "Agent told me I need a proof of funds letter to submit with my offer if I'm "
             "making a cash offer will a letter from a transactional funding source work I've.",
      'title': 'How to Wholesale Real Estate: Where to Get a Proof of Funds Letter '
               '(FlipThisWholesaler)',
      'url': 'https://www.youtube.com/watch?v=FUjDeT5p55I&t=44s',
      'video_id': 'FUjDeT5p55I'},
     {'author': 'Lex Levinrad Real Estate Training and Coaching',
      'channel': 'Lex Levinrad Real Estate Training and Coaching',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:33](https://www.youtube.com/watch?v=aX6Stxr8SfM&t=93s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Buyer Joe let's call him cash buyer Joe he comes in he looks at his property "
              "for 90 and he says I'd like to buy that.",
      'timestamp': 93,
      'timestamp_label': '[00:01:33]',
      'timestamp_seconds': 93,
      'tip': "Buyer Joe let's call him cash buyer Joe he comes in he looks at his property for "
             "90 and he says I'd like to buy that.",
      'title': 'Transactional Funding and Double Closings - How It Works And How We Fund Our '
               'Students (Lex Levinrad Real Estate Training and Coaching)',
      'url': 'https://www.youtube.com/watch?v=aX6Stxr8SfM&t=93s',
      'video_id': 'aX6Stxr8SfM'},
     {'author': 'Ryan Schrope',
      'channel': 'Ryan Schrope',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=wpikXXbAYnE&t=15s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Months with no promise of profit buying rentals is the long-term play no quick '
              'cash and wholesaling will set you back a few thousand bucks just to get '
              'started.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Months with no promise of profit buying rentals is the long-term play no quick '
             'cash and wholesaling will set you back a few thousand bucks just to get started.',
      'title': 'What Is Transactional Funding? (How I Made $31,000 in 1 Day) (Ryan Schrope)',
      'url': 'https://www.youtube.com/watch?v=wpikXXbAYnE&t=15s',
      'video_id': 'wpikXXbAYnE'},
     {'author': 'Flipping Mastery TV',
      'channel': 'Flipping Mastery TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:47](https://www.youtube.com/watch?v=R83ectOeUdU&t=707s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Those all-cash offers so that you've got a really strong offer when you go out "
              "there in the marketplace all right Gerry Norton and I'll see you soon.",
      'timestamp': 707,
      'timestamp_label': '[00:11:47]',
      'timestamp_seconds': 707,
      'tip': "Those all-cash offers so that you've got a really strong offer when you go out "
             "there in the marketplace all right Gerry Norton and I'll see you soon.",
      'title': 'How To Get A Proof Of Funds Letter And Use It For Making Cash Offers (Flipping '
               'Mastery TV)',
      'url': 'https://www.youtube.com/watch?v=R83ectOeUdU&t=707s',
      'video_id': 'R83ectOeUdU'},
     {'author': 'Foreclosure University',
      'channel': 'Foreclosure University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=rNJDrR6nTIk&t=79s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Forward to providing you some proof of funds letters so anytime you need them '
              "go ahead and fill out this form you can click on this link here and it'll take "
              "you to a funding request form where you guys can fill that out and uh we'll "
              'send you a proof of funds letter.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': 'Forward to providing you some proof of funds letters so anytime you need them go '
             "ahead and fill out this form you can click on this link here and it'll take you "
             "to a funding request form where you guys can fill that out and uh we'll send you "
             'a proof of funds letter.',
      'title': 'Proof of Funds - Transactional Funding - Proof  of funds letter (Foreclosure '
               'University)',
      'url': 'https://www.youtube.com/watch?v=rNJDrR6nTIk&t=79s',
      'video_id': 'rNJDrR6nTIk'}],
 4: [{'author': 'Cal Barton',
      'channel': 'Cal Barton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=Eh5z4F-toEI&t=21s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t ask millions of questions. And yes, I'll walk you through a ninecard stack "
              'strategy that can unlock a h 100 plus thousand in 0% APR business funding even '
              "if you're just getting started. But I need to let you know I launched my 0% APR "
              'business card database.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "'t ask millions of questions. And yes, I'll walk you through a ninecard stack "
             'strategy that can unlock a h 100 plus thousand in 0% APR business funding even '
             "if you're just getting started. But I need to let you know I launched my 0% APR "
             'business card database.',
      'title': '0% APR Business Credit Stacking for New LLCs (20 Cards) (Cal Barton)',
      'url': 'https://www.youtube.com/watch?v=Eh5z4F-toEI&t=21s',
      'video_id': 'Eh5z4F-toEI'},
     {'author': 'Tim Talks Real Estate',
      'channel': 'Tim Talks Real Estate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:13](https://www.youtube.com/watch?v=AkHsQo6uSuU&t=133s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, let's talk about the bank versus you angle, because I want you clear-eyed "
              "here. I've been in this business since 2007, before loan officers even needed a "
              "license. And I'll tell you straight, a bridge loan is a real product that "
              'genuinely helps in the right situation.',
      'timestamp': 133,
      'timestamp_label': '[00:02:13]',
      'timestamp_seconds': 133,
      'tip': "Now, let's talk about the bank versus you angle, because I want you clear-eyed "
             "here. I've been in this business since 2007, before loan officers even needed a "
             "license. And I'll tell you straight, a bridge loan is a real product that "
             'genuinely helps in the right situation.',
      'title': 'Bridge Loans Explained How to Buy Before You Sell and the Free Alternative '
               '(Tim Talks Real Estate)',
      'url': 'https://www.youtube.com/watch?v=AkHsQo6uSuU&t=133s',
      'video_id': 'AkHsQo6uSuU'},
     {'author': 'Fund My Real Estate Deal',
      'channel': 'Fund My Real Estate Deal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:26](https://www.youtube.com/watch?v=a--96aHg5xs&t=266s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '400k, not a lot of us have that kind of money sitting in the bank. And going '
              'back running the stack method and need short-term bridge capital, which is '
              'again goes back from bridging that gap for the the down payment from the senior '
              'loan.',
      'timestamp': 266,
      'timestamp_label': '[00:04:26]',
      'timestamp_seconds': 266,
      'tip': '400k, not a lot of us have that kind of money sitting in the bank. And going '
             'back running the stack method and need short-term bridge capital, which is again '
             'goes back from bridging that gap for the the down payment from the senior loan.',
      'title': 'Transactional Funding Explained: Close More Deals in 2026 (Fund My Real Estate '
               'Deal)',
      'url': 'https://www.youtube.com/watch?v=a--96aHg5xs&t=266s',
      'video_id': 'a--96aHg5xs'},
     {'author': 'Damen Capital Fund',
      'channel': 'Damen Capital Fund',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:58](https://www.youtube.com/watch?v=mrt2bJ7XfNU&t=418s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re more excited about the transaction. Six, no ongoing liability for you. Once "
              "you close and the property deeds to the buyer, you're done with the property "
              "ownership. You hold a lean, but you're not the owner. You don't need liability "
              'insurance.',
      'timestamp': 418,
      'timestamp_label': '[00:06:58]',
      'timestamp_seconds': 418,
      'tip': "'re more excited about the transaction. Six, no ongoing liability for you. Once "
             "you close and the property deeds to the buyer, you're done with the property "
             "ownership. You hold a lean, but you're not the owner. You don't need liability "
             'insurance.',
      'title': 'Promissory Note vs Land Contract — Which to Use for Land | Module 6 of 14 '
               '(Damen Capital Fund)',
      'url': 'https://www.youtube.com/watch?v=mrt2bJ7XfNU&t=418s',
      'video_id': 'mrt2bJ7XfNU'},
     {'author': 'Venus Venture',
      'channel': 'Venus Venture',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=qHujP7kjj4Y&t=87s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Require lender's title insurance to protect against hidden claims or recording "
              'errors. This step ensures that your lean is truly first in line. Record the '
              'lean immediately. The lean must be recorded at or before closing to guarantee '
              'priority.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': "Require lender's title insurance to protect against hidden claims or recording "
             'errors. This step ensures that your lean is truly first in line. Record the lean '
             'immediately. The lean must be recorded at or before closing to guarantee '
             'priority.',
      'title': 'Unlock Real Estate Security: First-Lien Loans Explained! (Venus Venture)',
      'url': 'https://www.youtube.com/watch?v=qHujP7kjj4Y&t=87s',
      'video_id': 'qHujP7kjj4Y'},
     {'author': 'Ron LeGrand',
      'channel': 'Ron LeGrand',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=Rrp7i7rV1lo&t=71s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Permission to do that in your offer we're building it into our offers we're "
              'putting them right in there that we have the right to assign this to another '
              "entity that we want to use the close with and we're not having any trouble "
              'getting that accepted okay all.',
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': "Permission to do that in your offer we're building it into our offers we're "
             'putting them right in there that we have the right to assign this to another '
             "entity that we want to use the close with and we're not having any trouble "
             'getting that accepted okay all.',
      'title': 'Ask Ron - Frank C. - Simultaneous Closings (Ron LeGrand)',
      'url': 'https://www.youtube.com/watch?v=Rrp7i7rV1lo&t=71s',
      'video_id': 'Rrp7i7rV1lo'},
     {'author': 'Forefront Enterprises',
      'channel': 'Forefront Enterprises',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:41](https://www.youtube.com/watch?v=Qe97wvpylvo&t=41s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Dollars and i have a buyer at 25 000 and i'm going to closing so i schedule my "
              'closing to buy the property from the seller.',
      'timestamp': 41,
      'timestamp_label': '[00:00:41]',
      'timestamp_seconds': 41,
      'tip': "Dollars and i have a buyer at 25 000 and i'm going to closing so i schedule my "
             'closing to buy the property from the seller.',
      'title': "Wholesaling Real Estate: Simultaneous Closings and REO's (Forefront "
               'Enterprises)',
      'url': 'https://www.youtube.com/watch?v=Qe97wvpylvo&t=41s',
      'video_id': 'Qe97wvpylvo'},
     {'author': 'Foreclosure University',
      'channel': 'Foreclosure University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=38RXOgdabuQ&t=87s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Transaction from A to B and then once that's done now you can actually flip "
              'this house to your in buyer and close on the deal and everything works well so.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': "Transaction from A to B and then once that's done now you can actually flip this "
             'house to your in buyer and close on the deal and everything works well so.',
      'title': 'Transactional Funding - Proof of Funds Letters (Foreclosure University)',
      'url': 'https://www.youtube.com/watch?v=38RXOgdabuQ&t=87s',
      'video_id': '38RXOgdabuQ'},
     {'author': 'Esquire Advice',
      'channel': 'Esquire Advice',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:11](https://www.youtube.com/watch?v=hy-UeKXcTUA&t=191s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Generally affected with a pledge agreement possession of the stock or llc '
              'certificate if the interest are.',
      'timestamp': 191,
      'timestamp_label': '[00:03:11]',
      'timestamp_seconds': 191,
      'tip': 'Generally affected with a pledge agreement possession of the stock or llc '
             'certificate if the interest are.',
      'title': 'Securing a Promissory Note - Real Estate, Stock, LLC Interests, and More - '
               'Mortgages and Pledges (Esquire Advice)',
      'url': 'https://www.youtube.com/watch?v=hy-UeKXcTUA&t=191s',
      'video_id': 'hy-UeKXcTUA'},
     {'author': 'Lender Link',
      'channel': 'Lender Link',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:27](https://www.youtube.com/watch?v=W1fiiFnsFhE&t=507s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So that the rule is one, they could do one loan per year. And they are okay '
              "without a license. And it's, it's fairly nuanced, but the best rule I could "
              'probably implement here is you can make one business purpose loan in a calendar '
              'year without being licensed.',
      'timestamp': 507,
      'timestamp_label': '[00:08:27]',
      'timestamp_seconds': 507,
      'tip': 'So that the rule is one, they could do one loan per year. And they are okay '
             "without a license. And it's, it's fairly nuanced, but the best rule I could "
             'probably implement here is you can make one business purpose loan in a calendar '
             'year without being licensed.',
      'title': 'California Usury Laws for Private Mortgage Lending (Lender Link)',
      'url': 'https://www.youtube.com/watch?v=W1fiiFnsFhE&t=507s',
      'video_id': 'W1fiiFnsFhE'},
     {'author': 'Tom McKay - FlipAnythingUSA',
      'channel': 'Tom McKay - FlipAnythingUSA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:00](https://www.youtube.com/watch?v=cvQX0jcvIFc&t=360s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So you could watch all of his free content and and he'll he'll say the same "
              "exact thing I won't do business with you if you I if you don't have an LLC "
              'from.',
      'timestamp': 360,
      'timestamp_label': '[00:06:00]',
      'timestamp_seconds': 360,
      'tip': "So you could watch all of his free content and and he'll he'll say the same "
             "exact thing I won't do business with you if you I if you don't have an LLC from.",
      'title': 'Is Pace Morby Gator Lending an Upselling Scam? (Tom McKay - FlipAnythingUSA)',
      'url': 'https://www.youtube.com/watch?v=cvQX0jcvIFc&t=360s',
      'video_id': 'cvQX0jcvIFc'},
     {'author': 'William Bronchick',
      'channel': 'William Bronchick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:16](https://www.youtube.com/watch?v=Z9NzpNmbuu8&t=196s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The parcels are parts and pieces are complete then we finish the closing '
              'back-to-back so it really is to actual closings that are done either '
              'simultaneously or in pieces in parts to make the whole thing complete everybody '
              "follow that that's our that's our double.",
      'timestamp': 196,
      'timestamp_label': '[00:03:16]',
      'timestamp_seconds': 196,
      'tip': 'The parcels are parts and pieces are complete then we finish the closing '
             'back-to-back so it really is to actual closings that are done either '
             'simultaneously or in pieces in parts to make the whole thing complete everybody '
             "follow that that's our that's our double.",
      'title': 'William "Bill" Bronchick  - Double Closings (William Bronchick)',
      'url': 'https://www.youtube.com/watch?v=Z9NzpNmbuu8&t=196s',
      'video_id': 'Z9NzpNmbuu8'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:32](https://www.youtube.com/watch?v=7yVZPbb03bc&t=812s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Dollars on let's say a credit card or a line of credit how much money would i "
              "make at 10 at 10 percent i'd make 500 for the year.",
      'timestamp': 812,
      'timestamp_label': '[00:13:32]',
      'timestamp_seconds': 812,
      'tip': "Dollars on let's say a credit card or a line of credit how much money would i "
             "make at 10 at 10 percent i'd make 500 for the year.",
      'title': 'The Gator Method | Beginner Strategy For Real Estate Investing (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=7yVZPbb03bc&t=812s',
      'video_id': '7yVZPbb03bc'},
     {'author': 'Oakwood Lending',
      'channel': 'Oakwood Lending',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:07](https://www.youtube.com/watch?v=VxkBvKoeA38&t=187s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Wholesaler and you're wondering how it works and you have questions let us know "
              'put your questions or your comment or your feedback on our youtube site or send '
              "me an e-mail at Adam 800 quid lending calm and I'll walk you through all of "
              'this thanks for listening.',
      'timestamp': 187,
      'timestamp_label': '[00:03:07]',
      'timestamp_seconds': 187,
      'tip': "Wholesaler and you're wondering how it works and you have questions let us know "
             'put your questions or your comment or your feedback on our youtube site or send '
             "me an e-mail at Adam 800 quid lending calm and I'll walk you through all of this "
             'thanks for listening.',
      'title': 'Transactional Funding (SDDC Same Day Double Close) (Oakwood Lending)',
      'url': 'https://www.youtube.com/watch?v=VxkBvKoeA38&t=187s',
      'video_id': 'VxkBvKoeA38'},
     {'author': 'LearnREInvesting',
      'channel': 'LearnREInvesting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:30](https://www.youtube.com/watch?v=PlXZzAIYwfI&t=150s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Title companies or even closing attorneys I suggest you get referrals for '
              'investor friendly closing agents and deal with the N buyers attorney as the '
              'issue presents itself thanks for joining us for this continuing series of '
              'transactional funding question and answers.',
      'timestamp': 150,
      'timestamp_label': '[00:02:30]',
      'timestamp_seconds': 150,
      'tip': 'Title companies or even closing attorneys I suggest you get referrals for '
             'investor friendly closing agents and deal with the N buyers attorney as the '
             'issue presents itself thanks for joining us for this continuing series of '
             'transactional funding question and answers.',
      'title': 'Transactional Funding Hated By Some Closing Agents! Transactional Funding '
               'Information (LearnREInvesting)',
      'url': 'https://www.youtube.com/watch?v=PlXZzAIYwfI&t=150s',
      'video_id': 'PlXZzAIYwfI'}],
 5: [{'author': 'Zach Siegel',
      'channel': 'Zach Siegel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:41](https://www.youtube.com/watch?v=Fs38E_kSwxE&t=641s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'At our company Small Biz Heroes, we help business owners create complete '
              'funding road maps that start with immediate capital needs and end with bank '
              "level financing. We've guided hundreds of businesses through this exact "
              'transition.',
      'timestamp': 641,
      'timestamp_label': '[00:10:41]',
      'timestamp_seconds': 641,
      'tip': 'At our company Small Biz Heroes, we help business owners create complete funding '
             'road maps that start with immediate capital needs and end with bank level '
             "financing. We've guided hundreds of businesses through this exact transition.",
      'title': 'Best 0% APR Business Credit Cards 2026 (Unlock Up to $100K in Interest-Free '
               'Capital) (Zach Siegel)',
      'url': 'https://www.youtube.com/watch?v=Fs38E_kSwxE&t=641s',
      'video_id': 'Fs38E_kSwxE'},
     {'author': 'Propy',
      'channel': 'Propy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=hn4wyDTnTXc&t=98s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The lender's policy protects the lender's loan. The owner's policy protects "
              'you, the buyer, if a covered problem from before you bought the home shows up '
              "later. And it's a one-time payment at closing, not a monthly bill.",
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': "The lender's policy protects the lender's loan. The owner's policy protects you, "
             'the buyer, if a covered problem from before you bought the home shows up later. '
             "And it's a one-time payment at closing, not a monthly bill.",
      'title': "Title vs Escrow: What's the Difference? (Explained Simply) (Propy)",
      'url': 'https://www.youtube.com/watch?v=hn4wyDTnTXc&t=98s',
      'video_id': 'hn4wyDTnTXc'},
     {'author': 'Flip Lab',
      'channel': 'Flip Lab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:01](https://www.youtube.com/watch?v=Qk7hhsytc9Y&t=421s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Of closing meaning me as a transactional funder i am only going to fund on your '
              "deal once i confirm with the title company that the end buyer's funds are.",
      'timestamp': 421,
      'timestamp_label': '[00:07:01]',
      'timestamp_seconds': 421,
      'tip': 'Of closing meaning me as a transactional funder i am only going to fund on your '
             "deal once i confirm with the title company that the end buyer's funds are.",
      'title': 'Transactional Funding | Same Day Double Close Wholesale Deals! Real Estate '
               'Investing (Flip Lab)',
      'url': 'https://www.youtube.com/watch?v=Qk7hhsytc9Y&t=421s',
      'video_id': 'Qk7hhsytc9Y'},
     {'author': 'MKK Capital Commercial Hard Money Lenders',
      'channel': 'MKK Capital Commercial Hard Money Lenders',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=k0m3lOvAU7U&t=88s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Or is the plan to improve the asset's value and sell it for a profit? A "
              'realistic plan shows the lender that this is a true bridge, not a long-term '
              'risk. Finally, timing and communication determine who gets to the closing table '
              'first.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': "Or is the plan to improve the asset's value and sell it for a profit? A "
             'realistic plan shows the lender that this is a true bridge, not a long-term '
             'risk. Finally, timing and communication determine who gets to the closing table '
             'first.',
      'title': 'What is Commercial Bridge Financing and Loan Exit Plans Explained (MKK Capital '
               'Commercial Hard Money Lenders)',
      'url': 'https://www.youtube.com/watch?v=k0m3lOvAU7U&t=88s',
      'video_id': 'k0m3lOvAU7U'},
     {'author': 'Ryan Schrope',
      'channel': 'Ryan Schrope',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:29](https://www.youtube.com/watch?v=xdTSPoFABEY&t=269s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "When I started building this business, I didn't know anybody that had actually "
              "uh scaled this kind of a business, right? Now it's continuing to grow. If you "
              "want to be a part of it, don't make this mistake, okay?",
      'timestamp': 269,
      'timestamp_label': '[00:04:29]',
      'timestamp_seconds': 269,
      'tip': "When I started building this business, I didn't know anybody that had actually "
             "uh scaled this kind of a business, right? Now it's continuing to grow. If you "
             "want to be a part of it, don't make this mistake, okay?",
      'title': 'The 3 reasons 99% of transactional funding businesses fail (Ryan Schrope)',
      'url': 'https://www.youtube.com/watch?v=xdTSPoFABEY&t=269s',
      'video_id': 'xdTSPoFABEY'},
     {'author': 'LearnREInvesting',
      'channel': 'LearnREInvesting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:34](https://www.youtube.com/watch?v=1ZAn99Atwe8&t=34s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Example of actually a triple closing this was done with no money no credit and '
              'no risk and as I always say the investor still profits if the end buyer.',
      'timestamp': 34,
      'timestamp_label': '[00:00:34]',
      'timestamp_seconds': 34,
      'tip': 'Example of actually a triple closing this was done with no money no credit and '
             'no risk and as I always say the investor still profits if the end buyer.',
      'title': 'Real Estate Investing| Double Closing | Transactional funding| Flipping '
               'Houses| Triple closing (LearnREInvesting)',
      'url': 'https://www.youtube.com/watch?v=1ZAn99Atwe8&t=34s',
      'video_id': '1ZAn99Atwe8'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=T5jtdYhM6tQ&t=79s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, here's the challenge with transactional lending. Sometimes transactional "
              'lending Alpha Gator will have different parameters for transactional lending. '
              'This is double closing, right? Alpha Gator also does DSCR loans and hard money '
              'loans and commercial loans, right?',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': "Now, here's the challenge with transactional lending. Sometimes transactional "
             'lending Alpha Gator will have different parameters for transactional lending. '
             'This is double closing, right? Alpha Gator also does DSCR loans and hard money '
             'loans and commercial loans, right?',
      'title': "There's Almost NO Risk | Gator Method (Pace Morby)",
      'url': 'https://www.youtube.com/watch?v=T5jtdYhM6tQ&t=79s',
      'video_id': 'T5jtdYhM6tQ'},
     {'author': 'Clint Coons Esq. | Real Estate Asset Protection',
      'channel': 'Clint Coons Esq. | Real Estate Asset Protection',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:35](https://www.youtube.com/watch?v=6bibMzU1L3U&t=155s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Perspective so what I suggest we do is we avoid the joint venture agreement '
              'garbage altogether my preferred methodology for.',
      'timestamp': 155,
      'timestamp_label': '[00:02:35]',
      'timestamp_seconds': 155,
      'tip': 'Perspective so what I suggest we do is we avoid the joint venture agreement '
             'garbage altogether my preferred methodology for.',
      'title': 'Setting up a Real Estate Joint Venture (Clint Coons Esq. | Real Estate Asset '
               'Protection)',
      'url': 'https://www.youtube.com/watch?v=6bibMzU1L3U&t=155s',
      'video_id': '6bibMzU1L3U'},
     {'author': 'Brent Daniels - Wholesaling Inc',
      'channel': 'Brent Daniels - Wholesaling Inc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:41](https://www.youtube.com/watch?v=HB5dJx0VOrA&t=161s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "There's a lot of There's a lot of nice houses out here. Why don't you fix your "
              "home up and sell it with an agent? Why don't you keep it and be a landlord? Why "
              "should I give you my money? What is the problem I'm solving for you? Are you "
              'sure you even want to sell this house?',
      'timestamp': 161,
      'timestamp_label': '[00:02:41]',
      'timestamp_seconds': 161,
      'tip': "There's a lot of There's a lot of nice houses out here. Why don't you fix your "
             "home up and sell it with an agent? Why don't you keep it and be a landlord? Why "
             "should I give you my money? What is the problem I'm solving for you? Are you "
             'sure you even want to sell this house?',
      'title': 'How Do I Get A Proof Of Funds? | Wholesale Real Estate (Brent Daniels - '
               'Wholesaling Inc)',
      'url': 'https://www.youtube.com/watch?v=HB5dJx0VOrA&t=161s',
      'video_id': 'HB5dJx0VOrA'},
     {'author': 'True Title',
      'channel': 'True Title',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:09](https://www.youtube.com/watch?v=qsZtsUB4AFM&t=189s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'On all of the amounts shown in the above section are then subtotal in the debit '
              'and credit columns and the next line will include an amount due from meaning '
              'you must pay it for closing after your review please sign and date on the '
              'signature page.',
      'timestamp': 189,
      'timestamp_label': '[00:03:09]',
      'timestamp_seconds': 189,
      'tip': 'On all of the amounts shown in the above section are then subtotal in the debit '
             'and credit columns and the next line will include an amount due from meaning you '
             'must pay it for closing after your review please sign and date on the signature '
             'page.',
      'title': "Buyer's Guide to Closing Documents - ALTA Settlement Statement - Section 1 "
               '(True Title)',
      'url': 'https://www.youtube.com/watch?v=qsZtsUB4AFM&t=189s',
      'video_id': 'qsZtsUB4AFM'},
     {'author': 'Jason Gaston',
      'channel': 'Jason Gaston',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:11](https://www.youtube.com/watch?v=JbOkaP42JKo&t=551s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Transactional funding one closing second closing all involving the same '
              "property the same house thanks for watching we'll see you next video.",
      'timestamp': 551,
      'timestamp_label': '[00:09:11]',
      'timestamp_seconds': 551,
      'tip': 'Transactional funding one closing second closing all involving the same property '
             "the same house thanks for watching we'll see you next video.",
      'title': 'Wholesaling Real Estate 101 - The Double Close (Jason Gaston)',
      'url': 'https://www.youtube.com/watch?v=JbOkaP42JKo&t=551s',
      'video_id': 'JbOkaP42JKo'},
     {'author': 'Win-Win Realtors TV',
      'channel': 'Win-Win Realtors TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:06](https://www.youtube.com/watch?v=y9awo1XfRU4&t=186s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If the disclosures and or reports revealed something that the buyer disapproves '
              'of and if the buyer does discover something they disapprove of the buyer can '
              'back out of that transaction and receive your deposit money back.',
      'timestamp': 186,
      'timestamp_label': '[00:03:06]',
      'timestamp_seconds': 186,
      'tip': 'If the disclosures and or reports revealed something that the buyer disapproves '
             'of and if the buyer does discover something they disapprove of the buyer can '
             'back out of that transaction and receive your deposit money back.',
      'title': 'HOW NOT TO LOOSE YOUR EARNEST MONEY DEPOSIT? UNDERSTAND CONTENGENCIES. '
               '(Win-Win Realtors TV)',
      'url': 'https://www.youtube.com/watch?v=y9awo1XfRU4&t=186s',
      'video_id': 'y9awo1XfRU4'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:41:50](https://www.youtube.com/watch?v=S9WonQBbHG8&t=2510s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Gap before the money comes back in and I go no problem I can do I can do that '
              "kind of loan it's really risky because I'm it's not necessarily RIS real "
              'estate.',
      'timestamp': 2510,
      'timestamp_label': '[00:41:50]',
      'timestamp_seconds': 2510,
      'tip': 'Gap before the money comes back in and I go no problem I can do I can do that '
             "kind of loan it's really risky because I'm it's not necessarily RIS real estate.",
      'title': 'From Teacher to Investor: $230K/Year with Gator Lending (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=S9WonQBbHG8&t=2510s',
      'video_id': 'S9WonQBbHG8'},
     {'author': 'Jamil Damji',
      'channel': 'Jamil Damji',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:41](https://www.youtube.com/watch?v=_4J_JXkaaMg&t=761s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That you can do in the investment space of real estate and also leave me a '
              'comment because it lets me know who you are I can respond to you and we can '
              "actually be friends I'll see you in the next.",
      'timestamp': 761,
      'timestamp_label': '[00:12:41]',
      'timestamp_seconds': 761,
      'tip': 'That you can do in the investment space of real estate and also leave me a '
             'comment because it lets me know who you are I can respond to you and we can '
             "actually be friends I'll see you in the next.",
      'title': 'How to work with a Closing Attorney, Escrow companies, and title companies '
               '(Jamil Damji)',
      'url': 'https://www.youtube.com/watch?v=_4J_JXkaaMg&t=761s',
      'video_id': '_4J_JXkaaMg'},
     {'author': 'Flipping Mastery TV',
      'channel': 'Flipping Mastery TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:43](https://www.youtube.com/watch?v=qWrqNQvtTO8&t=403s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The time and freedom to have me do and give everything you want in life that's "
              "what it's all about and I'll see you on the next video.",
      'timestamp': 403,
      'timestamp_label': '[00:06:43]',
      'timestamp_seconds': 403,
      'tip': "The time and freedom to have me do and give everything you want in life that's "
             "what it's all about and I'll see you on the next video.",
      'title': 'How To Finance A Wholesale Deal - Transactional Funding EXPLAINED (Flipping '
               'Mastery TV)',
      'url': 'https://www.youtube.com/watch?v=qWrqNQvtTO8&t=403s',
      'video_id': 'qWrqNQvtTO8'}],
 6: [{'author': 'Naam Wynn',
      'channel': 'Naam Wynn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:15](https://www.youtube.com/watch?v=bdodeCpS6JI&t=495s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'B2B services are viewed as lower risk. You can find a full list linked down '
              "below. Now, when you're first starting out, your NACS code may not seem like a "
              "big deal. In fact, you probably won't get asked about it until you start "
              'applying.',
      'timestamp': 495,
      'timestamp_label': '[00:08:15]',
      'timestamp_seconds': 495,
      'tip': 'B2B services are viewed as lower risk. You can find a full list linked down '
             "below. Now, when you're first starting out, your NACS code may not seem like a "
             "big deal. In fact, you probably won't get asked about it until you start "
             'applying.',
      'title': 'How to Get $100,000+ in Business Credit at 0% APR (New LLCs) (Naam Wynn)',
      'url': 'https://www.youtube.com/watch?v=bdodeCpS6JI&t=495s',
      'video_id': 'bdodeCpS6JI'},
     {'author': 'Velocity Advantage Capital',
      'channel': 'Velocity Advantage Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=Fb1_zsDd4XE&t=100s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Close that first contract with the seller turn around and close it with a '
              'second contract with the end buyer and on that second closing we get our our '
              'money back that we put up to fund the deal in our fee and then the investor '
              'gets their profit.',
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': 'Close that first contract with the seller turn around and close it with a second '
             'contract with the end buyer and on that second closing we get our our money back '
             'that we put up to fund the deal in our fee and then the investor gets their '
             'profit.',
      'title': 'How to Use TRANSACTIONAL Funding for Double Closings (Velocity Advantage '
               'Capital)',
      'url': 'https://www.youtube.com/watch?v=Fb1_zsDd4XE&t=100s',
      'video_id': 'Fb1_zsDd4XE'},
     {'author': 'HowToCredit',
      'channel': 'HowToCredit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:23](https://www.youtube.com/watch?v=0jZD4_NoCTs&t=383s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We're going to stay with US Bank right now then we're going to go with number "
              'two, which is the Shield Visa Business Credit Card. Now this one is a little '
              "different because it's the first card on the list that solves the balance "
              'transfer problems, okay?',
      'timestamp': 383,
      'timestamp_label': '[00:06:23]',
      'timestamp_seconds': 383,
      'tip': "We're going to stay with US Bank right now then we're going to go with number "
             'two, which is the Shield Visa Business Credit Card. Now this one is a little '
             "different because it's the first card on the list that solves the balance "
             'transfer problems, okay?',
      'title': 'If You Need $50,000 Or More In Business Funding 0% Interest , Use These 5 '
               'Cards ASAP (HowToCredit)',
      'url': 'https://www.youtube.com/watch?v=0jZD4_NoCTs&t=383s',
      'video_id': '0jZD4_NoCTs'},
     {'author': 'Game Changer Real Estate Insights',
      'channel': 'Game Changer Real Estate Insights',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=lLbfcHAX30o&t=60s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I talk about in several other of our videos, is how do you handle the closing? '
              'You need to make sure they close independently of each other. So, in other '
              "words, we're not using the end buyer's money to fund the first closing.",
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': 'I talk about in several other of our videos, is how do you handle the closing? '
             'You need to make sure they close independently of each other. So, in other '
             "words, we're not using the end buyer's money to fund the first closing.",
      'title': 'Double Closings Transactional Funding Real Estate Investing [E-101] (Game '
               'Changer Real Estate Insights)',
      'url': 'https://www.youtube.com/watch?v=lLbfcHAX30o&t=60s',
      'video_id': 'lLbfcHAX30o'},
     {'author': 'Jamil Damji',
      'channel': 'Jamil Damji',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=KMD0dZIIYwc&t=59s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Would inherently ly double close that deal why because I have seen sellers walk '
              'up from a closing table and walk right out of the title company and.',
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': 'Would inherently ly double close that deal why because I have seen sellers walk '
             'up from a closing table and walk right out of the title company and.',
      'title': 'When To Double Close & When to Assign | Wholesale Real Estate (Jamil Damji)',
      'url': 'https://www.youtube.com/watch?v=KMD0dZIIYwc&t=59s',
      'video_id': 'KMD0dZIIYwc'},
     {'author': 'Luigi Ontiveros',
      'channel': 'Luigi Ontiveros',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:46](https://www.youtube.com/watch?v=UpxkrBIxTtQ&t=226s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Made between your company known as a seller and your buyers name as the buyer '
              'for property located at your new profitable deal it.',
      'timestamp': 226,
      'timestamp_label': '[00:03:46]',
      'timestamp_seconds': 226,
      'tip': 'Made between your company known as a seller and your buyers name as the buyer '
             'for property located at your new profitable deal it.',
      'title': 'How a Double Closing Works in Real Estate Wholesaling (Luigi Ontiveros)',
      'url': 'https://www.youtube.com/watch?v=UpxkrBIxTtQ&t=226s',
      'video_id': 'UpxkrBIxTtQ'},
     {'author': 'Fuel My Deal',
      'channel': 'Fuel My Deal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:23](https://www.youtube.com/watch?v=cqT1jSeQWKo&t=23s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is generally used for double closes in wholesaling. You contract a '
              'property with the seller, then resell to your end buyer, often the same day. A '
              'transactional funding partner covers the first closing and is repaid '
              'immediately at the second closing.',
      'timestamp': 23,
      'timestamp_label': '[00:00:23]',
      'timestamp_seconds': 23,
      'tip': 'This is generally used for double closes in wholesaling. You contract a property '
             'with the seller, then resell to your end buyer, often the same day. A '
             'transactional funding partner covers the first closing and is repaid immediately '
             'at the second closing.',
      'title': 'How to Pick the Right Loan for Your Deal (Transactional vs Hard Money vs DSCR) '
               '(Fuel My Deal)',
      'url': 'https://www.youtube.com/watch?v=cqT1jSeQWKo&t=23s',
      'video_id': 'cqT1jSeQWKo'},
     {'author': 'Flipping Mastery TV',
      'channel': 'Flipping Mastery TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:13](https://www.youtube.com/watch?v=9NXVYf_SZCA&t=73s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Clauses and ways out of the contract and the reason is if they can't find a "
              'buyer for that deal they want to be able to get out of the contract without '
              'any.',
      'timestamp': 73,
      'timestamp_label': '[00:01:13]',
      'timestamp_seconds': 73,
      'tip': "Clauses and ways out of the contract and the reason is if they can't find a "
             'buyer for that deal they want to be able to get out of the contract without any.',
      'title': 'How To Handle Proof of Funds When Making Cash Offers (Flipping Mastery TV)',
      'url': 'https://www.youtube.com/watch?v=9NXVYf_SZCA&t=73s',
      'video_id': '9NXVYf_SZCA'},
     {'author': 'Ryan Schrope',
      'channel': 'Ryan Schrope',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:35](https://www.youtube.com/watch?v=wjyrMCdmO9g&t=335s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t have any payroll on these people. And the promise to these referrals is "
              "simply, hey, you go find the deal, right? 'll partner and they'll bring the "
              "deal and I'll bring the systems. So that's the capital and you know the TC's, "
              'the contracts, all of that good stuff.',
      'timestamp': 335,
      'timestamp_label': '[00:05:35]',
      'timestamp_seconds': 335,
      'tip': "'t have any payroll on these people. And the promise to these referrals is "
             "simply, hey, you go find the deal, right? 'll partner and they'll bring the deal "
             "and I'll bring the systems. So that's the capital and you know the TC's, the "
             'contracts, all of that good stuff.',
      'title': 'How I closed 138 transactional funding deals in 1 year (full blueprint) (Ryan '
               'Schrope)',
      'url': 'https://www.youtube.com/watch?v=wjyrMCdmO9g&t=335s',
      'video_id': 'wjyrMCdmO9g'},
     {'author': 'Gerald Harris',
      'channel': 'Gerald Harris',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=0Nli9p7r9jI&t=110s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Double closing on a deal okay um that's when so let me give you an example of a "
              "double closing and another term we're going to talk about is transactional "
              'funding okay so let me give you an example so basically.',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': "Double closing on a deal okay um that's when so let me give you an example of a "
             "double closing and another term we're going to talk about is transactional "
             'funding okay so let me give you an example so basically.',
      'title': 'How to Wholesale Real Estate as a Realtor using Transactional Funding (Gerald '
               'Harris)',
      'url': 'https://www.youtube.com/watch?v=0Nli9p7r9jI&t=110s',
      'video_id': '0Nli9p7r9jI'},
     {'author': 'Beyond The Deals Podcast',
      'channel': 'Beyond The Deals Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:45](https://www.youtube.com/watch?v=tbL4i7Pr1EM&t=1245s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And there's several other companies I know of that will not uh they won't work "
              'with first-time flippers. Why why do you think it is that you guys are willing '
              'to do that? I >> think we just understand the numbers really well. We just have '
              'a lot of data.',
      'timestamp': 1245,
      'timestamp_label': '[00:20:45]',
      'timestamp_seconds': 1245,
      'tip': "And there's several other companies I know of that will not uh they won't work "
             'with first-time flippers. Why why do you think it is that you guys are willing '
             'to do that? I >> think we just understand the numbers really well. We just have '
             'a lot of data.',
      'title': 'Hard Money Secrets: Scaling Your Real Estate Portfolio with Gabrial Carter '
               '(Beyond The Deals Podcast)',
      'url': 'https://www.youtube.com/watch?v=tbL4i7Pr1EM&t=1245s',
      'video_id': 'tbL4i7Pr1EM'},
     {'author': 'Brent Daniels - Wholesaling Inc',
      'channel': 'Brent Daniels - Wholesaling Inc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:30](https://www.youtube.com/watch?v=AcL3tusr27o&t=210s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Want to work with you so that you want to be best friends with a hard money '
              'lender the first step in building the relationship with the hard money lender.',
      'timestamp': 210,
      'timestamp_label': '[00:03:30]',
      'timestamp_seconds': 210,
      'tip': 'Want to work with you so that you want to be best friends with a hard money '
             'lender the first step in building the relationship with the hard money lender.',
      'title': 'How To Get A Proof of Funds Letter For Wholesaling (3 Free Ways) (Brent '
               'Daniels - Wholesaling Inc)',
      'url': 'https://www.youtube.com/watch?v=AcL3tusr27o&t=210s',
      'video_id': 'AcL3tusr27o'},
     {'author': 'LearnREInvesting',
      'channel': 'LearnREInvesting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=AvFYUxl4Gx8&t=114s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Be sure to check out besttransactionalfunding.com for all your same day double '
              'closing needs including a list of investor friendly closing agents in various '
              'States we have more five-star Google ratings than all the other transactional '
              'funders combined.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': 'Be sure to check out besttransactionalfunding.com for all your same day double '
             'closing needs including a list of investor friendly closing agents in various '
             'States we have more five-star Google ratings than all the other transactional '
             'funders combined.',
      'title': 'Real Estate Investing - What is a Transaction Fee in Transactional Funding? '
               '(LearnREInvesting)',
      'url': 'https://www.youtube.com/watch?v=AvFYUxl4Gx8&t=114s',
      'video_id': 'AvFYUxl4Gx8'},
     {'author': 'Crushing REI',
      'channel': 'Crushing REI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=jDAbeOWsBX4&t=54s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Transaction many wholesalers need earnest money to secure a wholesale deal into '
              'lockup contracts essentially what uh Pace has come up with is um a lot of these '
              "wholesalers they don't have the earnest.",
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'Transaction many wholesalers need earnest money to secure a wholesale deal into '
             'lockup contracts essentially what uh Pace has come up with is um a lot of these '
             "wholesalers they don't have the earnest.",
      'title': "Honest Gator Method Review: Is Pace Morby's Gator Lender Course Worth It? "
               '(Crushing REI)',
      'url': 'https://www.youtube.com/watch?v=jDAbeOWsBX4&t=54s',
      'video_id': 'jDAbeOWsBX4'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=A3l3Dg0cJLk&t=120s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You put in so if you're putting down that and then I just keep giving you 3 000 "
              "or I mean for the first deal we can start off and we can do because we're.",
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': "You put in so if you're putting down that and then I just keep giving you 3 000 "
             "or I mean for the first deal we can start off and we can do because we're.",
      'title': 'Double Your Money with the Gator Method | Live Call (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=A3l3Dg0cJLk&t=120s',
      'video_id': 'A3l3Dg0cJLk'}],
 7: [{'author': 'Jed Bratt - Living in San Diego',
      'channel': 'Jed Bratt - Living in San Diego',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:46](https://www.youtube.com/watch?v=gtM_ZElxYdA&t=106s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Watch these other lectures check out the supplementals on the next steps '
              'following close of escrow and other things you want to know as a homeowner but '
              'this is the final step before you actually get your keys congratulations and '
              "I'll see you in the other videos.",
      'timestamp': 106,
      'timestamp_label': '[00:01:46]',
      'timestamp_seconds': 106,
      'tip': 'Watch these other lectures check out the supplementals on the next steps '
             'following close of escrow and other things you want to know as a homeowner but '
             'this is the final step before you actually get your keys congratulations and '
             "I'll see you in the other videos.",
      'title': 'ESCROW PROCESS: Funding & Recording | Buying Real Estate (Jed Bratt - Living '
               'in San Diego)',
      'url': 'https://www.youtube.com/watch?v=gtM_ZElxYdA&t=106s',
      'video_id': 'gtM_ZElxYdA'},
     {'author': 'Katherine Brough',
      'channel': 'Katherine Brough',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:40](https://www.youtube.com/watch?v=h1TnczbK_bE&t=280s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Don't wait until the next business day to begin reporting it. Before sending "
              'money for a home purchase, remember these three steps. Establish a trusted '
              'contact number early. Verify the wiring instructions directly before sending.',
      'timestamp': 280,
      'timestamp_label': '[00:04:40]',
      'timestamp_seconds': 280,
      'tip': "Don't wait until the next business day to begin reporting it. Before sending "
             'money for a home purchase, remember these three steps. Establish a trusted '
             'contact number early. Verify the wiring instructions directly before sending.',
      'title': 'Real Estate Wire Fraud: How to Protect Your Down Payment Before Closing '
               '(Katherine Brough)',
      'url': 'https://www.youtube.com/watch?v=h1TnczbK_bE&t=280s',
      'video_id': 'h1TnczbK_bE'},
     {'author': 'Flip With Rick',
      'channel': 'Flip With Rick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=itXS_PDnxa8&t=15s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Company what they actually do then I'm going to walk you through the 10 closing "
              'steps that all titles take to complete a real estate transaction but before I '
              'get.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Company what they actually do then I'm going to walk you through the 10 closing "
             'steps that all titles take to complete a real estate transaction but before I '
             'get.',
      'title': 'Title Companies & Closings Explained for Beginners in Wholesaling Real Estate '
               '(Day#4) (Flip With Rick)',
      'url': 'https://www.youtube.com/watch?v=itXS_PDnxa8&t=15s',
      'video_id': 'itXS_PDnxa8'},
     {'author': 'Tom Olsewski - Team Olsewski',
      'channel': 'Tom Olsewski - Team Olsewski',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=haXXzqITogY&t=102s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Make sure that it's a wire not an ACH trans transfer it has to be a wire so "
              "that's step one in the escrow process let's get that squared away and if you "
              "have any questions reach out to your agent or our transaction team we're happy "
              'to help foreign.',
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': "Make sure that it's a wire not an ACH trans transfer it has to be a wire so "
             "that's step one in the escrow process let's get that squared away and if you "
             "have any questions reach out to your agent or our transaction team we're happy "
             'to help foreign.',
      'title': 'Buyer Escrow Process Step One    Send Initial Deposit AKA EMD to Escrow (Tom '
               'Olsewski - Team Olsewski)',
      'url': 'https://www.youtube.com/watch?v=haXXzqITogY&t=102s',
      'video_id': 'haXXzqITogY'},
     {'author': 'BetterWealth',
      'channel': 'BetterWealth',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:56](https://www.youtube.com/watch?v=ojWjbXNf-HI&t=476s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Had 50 or 100,000 and I put that money from this business credit card into this '
              'business opportunity or investment that I can most likely make x amount return.',
      'timestamp': 476,
      'timestamp_label': '[00:07:56]',
      'timestamp_seconds': 476,
      'tip': 'Had 50 or 100,000 and I put that money from this business credit card into this '
             'business opportunity or investment that I can most likely make x amount return.',
      'title': 'How To Get $200,000 in Business Credit at 0% Interest (With No Business '
               'History) | Jack McColl (BetterWealth)',
      'url': 'https://www.youtube.com/watch?v=ojWjbXNf-HI&t=476s',
      'video_id': 'ojWjbXNf-HI'},
     {'author': 'The Real Estate Lender',
      'channel': 'The Real Estate Lender',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:46](https://www.youtube.com/watch?v=Bp3FsnPecRY&t=466s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I also built the fix and flip funding blueprint $47 linked below. It walks the '
              'funding timeline, the draws and the cash float step by step. And for the full '
              'library, every course, every track, my deal up close, school premiums founding '
              '100 is $97 a month.',
      'timestamp': 466,
      'timestamp_label': '[00:07:46]',
      'timestamp_seconds': 466,
      'tip': 'I also built the fix and flip funding blueprint $47 linked below. It walks the '
             'funding timeline, the draws and the cash float step by step. And for the full '
             'library, every course, every track, my deal up close, school premiums founding '
             '100 is $97 a month.',
      'title': 'How Private Lenders Protect Their Money: Notes, Liens & Insurance (The Real '
               'Estate Lender)',
      'url': 'https://www.youtube.com/watch?v=Bp3FsnPecRY&t=466s',
      'video_id': 'Bp3FsnPecRY'},
     {'author': 'Ayala Law PA',
      'channel': 'Ayala Law PA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=0cBnXayz9w4&t=98s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, what happens at the end is like a lot of business owners, when it comes to '
              "the end of the life of these loans, they sometimes don't have the capital and "
              'then that refinancing. And in that refinancing process, there is delay.',
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': 'Now, what happens at the end is like a lot of business owners, when it comes to '
             "the end of the life of these loans, they sometimes don't have the capital and "
             'then that refinancing. And in that refinancing process, there is delay.',
      'title': 'Business Loan Agreements: What Every Business Owner Should Review (Ayala Law '
               'PA)',
      'url': 'https://www.youtube.com/watch?v=0cBnXayz9w4&t=98s',
      'video_id': '0cBnXayz9w4'},
     {'author': 'Toño Flores',
      'channel': 'Toño Flores',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:49](https://www.youtube.com/watch?v=fv1IoI6DQn8&t=349s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I mean option number two we can do deals together. You learn how I do things '
              'handson. We run a few deals side by side and then you take the process and you '
              'run your own transactional funding business. Once you learn from me you learn '
              'the steps that I follow.',
      'timestamp': 349,
      'timestamp_label': '[00:05:49]',
      'timestamp_seconds': 349,
      'tip': 'I mean option number two we can do deals together. You learn how I do things '
             'handson. We run a few deals side by side and then you take the process and you '
             'run your own transactional funding business. Once you learn from me you learn '
             'the steps that I follow.',
      'title': 'Private Money Lending vs Transactional Funding: The Truth They Are Not Telling '
               'You (Toño Flores)',
      'url': 'https://www.youtube.com/watch?v=fv1IoI6DQn8&t=349s',
      'video_id': 'fv1IoI6DQn8'},
     {'author': 'Flipping Mastery TV',
      'channel': 'Flipping Mastery TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:33](https://www.youtube.com/watch?v=Jfl-5LgDTaM&t=813s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Next video where I explain in detail the steps to follow after you get a '
              "contract with a motivated seller now you're gonna love the detailed "
              "step-by-step breakdown watch it now and I'll see you on the next video.",
      'timestamp': 813,
      'timestamp_label': '[00:13:33]',
      'timestamp_seconds': 813,
      'tip': 'Next video where I explain in detail the steps to follow after you get a '
             "contract with a motivated seller now you're gonna love the detailed step-by-step "
             "breakdown watch it now and I'll see you on the next video.",
      'title': 'The Right Way To Do A Double Closing Real Estate Deal (Flipping Mastery TV)',
      'url': 'https://www.youtube.com/watch?v=Jfl-5LgDTaM&t=813s',
      'video_id': 'Jfl-5LgDTaM'},
     {'author': 'Real Estate Explainer',
      'channel': 'Real Estate Explainer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:14](https://www.youtube.com/watch?v=1UWrNExO1Ak&t=254s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "There's underwriting happening somewhere else, out of state, and they kick it "
              "back cuz there's one little thing on that checklist they don't like, and they "
              'kill otherwise good deals. And so, I had just left a 15-year career as a '
              'computer engineer at that time.',
      'timestamp': 254,
      'timestamp_label': '[00:04:14]',
      'timestamp_seconds': 254,
      'tip': "There's underwriting happening somewhere else, out of state, and they kick it "
             "back cuz there's one little thing on that checklist they don't like, and they "
             'kill otherwise good deals. And so, I had just left a 15-year career as a '
             'computer engineer at that time.',
      'title': 'Private Money Lending Explained: Fast Fix-and-Flip Loans, 75% ARV, and SDIRA '
               'Co-Lending with Inve... (Real Estate Explainer)',
      'url': 'https://www.youtube.com/watch?v=1UWrNExO1Ak&t=254s',
      'video_id': '1UWrNExO1Ak'},
     {'author': 'Charles Nedder | Greenwich CT Real Estate',
      'channel': 'Charles Nedder | Greenwich CT Real Estate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:15](https://www.youtube.com/watch?v=xyiyeiBkCqQ&t=255s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That is why having an experienced attorney and an agent who understands how '
              'these contracts work in Greenwich is not optional. It is the single most '
              'important thing you can do to protect your money in this process.',
      'timestamp': 255,
      'timestamp_label': '[00:04:15]',
      'timestamp_seconds': 255,
      'tip': 'That is why having an experienced attorney and an agent who understands how '
             'these contracts work in Greenwich is not optional. It is the single most '
             'important thing you can do to protect your money in this process.',
      'title': 'Earnest Money in Greenwich, CT with Charles Nedder (Charles Nedder | Greenwich '
               'CT Real Estate)',
      'url': 'https://www.youtube.com/watch?v=xyiyeiBkCqQ&t=255s',
      'video_id': 'xyiyeiBkCqQ'},
     {'author': 'Ryan Schrope',
      'channel': 'Ryan Schrope',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:43](https://www.youtube.com/watch?v=j30R1Cef6PE&t=1063s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Statement that means I know how much money to send and they have now signed '
              'that they know how much money to send back to me so then what needs to happen '
              "well once that's confirmed the last step of my process is wait.",
      'timestamp': 1063,
      'timestamp_label': '[00:17:43]',
      'timestamp_seconds': 1063,
      'tip': 'Statement that means I know how much money to send and they have now signed that '
             'they know how much money to send back to me so then what needs to happen well '
             "once that's confirmed the last step of my process is wait.",
      'title': 'The Entire Double Closing Process (step-by-step) (Ryan Schrope)',
      'url': 'https://www.youtube.com/watch?v=j30R1Cef6PE&t=1063s',
      'video_id': 'j30R1Cef6PE'},
     {'author': 'Diana Cifuentes',
      'channel': 'Diana Cifuentes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:02](https://www.youtube.com/watch?v=eMR8CmhQHhk&t=362s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Has a right to give you your keys so the 30th is when the property is actually '
              "yours congratulations yay so guys that's a 30-day escrow process if there's "
              'anything that you did not understand please let me know we will love to answer '
              'talk to you soon goodbye.',
      'timestamp': 362,
      'timestamp_label': '[00:06:02]',
      'timestamp_seconds': 362,
      'tip': 'Has a right to give you your keys so the 30th is when the property is actually '
             "yours congratulations yay so guys that's a 30-day escrow process if there's "
             'anything that you did not understand please let me know we will love to answer '
             'talk to you soon goodbye.',
      'title': 'What Is Escrow? Escrow Process Explained - Step by Step (Diana Cifuentes)',
      'url': 'https://www.youtube.com/watch?v=eMR8CmhQHhk&t=362s',
      'video_id': 'eMR8CmhQHhk'},
     {'author': 'LearnREInvesting',
      'channel': 'LearnREInvesting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=6muHPduCEtc&t=134s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your same day double closing needs including a list of investor friendly '
              'closing agents in various States we have more five-star Google ratings than all '
              'the other transactional funders combined.',
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': 'Your same day double closing needs including a list of investor friendly closing '
             'agents in various States we have more five-star Google ratings than all the '
             'other transactional funders combined.',
      'title': 'Real Estate Investing - Transactional Funding Costs (LearnREInvesting)',
      'url': 'https://www.youtube.com/watch?v=6muHPduCEtc&t=134s',
      'video_id': '6muHPduCEtc'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=UtlUmrdNU8Y&t=104s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I needed a lender that I'd used in the past um it was like two days before "
              'Christmas and most of my other lenders were out of town and I go hey I need.',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': "I needed a lender that I'd used in the past um it was like two days before "
             'Christmas and most of my other lenders were out of town and I go hey I need.',
      'title': 'When To Pay Off Private Money Lenders In Real Estate Deals | The 3 TYPES Of '
               'Lenders (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=UtlUmrdNU8Y&t=104s',
      'video_id': 'UtlUmrdNU8Y'}],
 8: [{'author': 'EZ Real Estate Platform',
      'channel': 'EZ Real Estate Platform',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:37](https://www.youtube.com/watch?v=KDMCbsw9VKs&t=1657s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're walking away cost of business to protect your profit, you're spending "
              '$3,000. So with that, with putting it on the platform, you can now say Pete '
              "will double close for you and you walk away with the 80 K. 'cause my fees "
              "covered by the buyer's premium.",
      'timestamp': 1657,
      'timestamp_label': '[00:27:37]',
      'timestamp_seconds': 1657,
      'tip': "You're walking away cost of business to protect your profit, you're spending "
             '$3,000. So with that, with putting it on the platform, you can now say Pete will '
             "double close for you and you walk away with the 80 K. 'cause my fees covered by "
             "the buyer's premium.",
      'title': 'A Game-Changer for Agent and Wholesaler Collabs: Transactional Funding & Buyer '
               'Premiums (EZ Real Estate Platform)',
      'url': 'https://www.youtube.com/watch?v=KDMCbsw9VKs&t=1657s',
      'video_id': 'KDMCbsw9VKs'},
     {'author': 'Rene Nelson',
      'channel': 'Rene Nelson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:47](https://www.youtube.com/watch?v=VIt86OFRY3Y&t=647s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Maybe they have some financial reporting that isn't done yet or or maybe "
              "there's a time constraint with the closing and the bank can't close fast "
              'enough. Any, you know, wide number of reasons that somebody could need a bridge '
              'loan.',
      'timestamp': 647,
      'timestamp_label': '[00:10:47]',
      'timestamp_seconds': 647,
      'tip': "Maybe they have some financial reporting that isn't done yet or or maybe there's "
             "a time constraint with the closing and the bank can't close fast enough. Any, "
             'you know, wide number of reasons that somebody could need a bridge loan.',
      'title': 'Bridge Loans Explained: When Private Money Works and When It Can Wreck a Deal '
               '(Rene Nelson)',
      'url': 'https://www.youtube.com/watch?v=VIt86OFRY3Y&t=647s',
      'video_id': 'VIt86OFRY3Y'},
     {'author': 'Andrew Kraft',
      'channel': 'Andrew Kraft',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:59](https://www.youtube.com/watch?v=S_u_YpirRNM&t=479s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So deployment, you're going to take your money, you're going to deploy it into "
              'real estate, business expansion, high ROI flips, and always structure to pay '
              'back um those companies before your 0% APR ends, right?',
      'timestamp': 479,
      'timestamp_label': '[00:07:59]',
      'timestamp_seconds': 479,
      'tip': "So deployment, you're going to take your money, you're going to deploy it into "
             'real estate, business expansion, high ROI flips, and always structure to pay '
             'back um those companies before your 0% APR ends, right?',
      'title': '🚀 How to Get $50K–$250K in 0% Interest Business Credit Using Credit Card '
               'Stacking (Andrew Kraft)',
      'url': 'https://www.youtube.com/watch?v=S_u_YpirRNM&t=479s',
      'video_id': 'S_u_YpirRNM'},
     {'author': 'Closer Control',
      'channel': 'Closer Control',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:59](https://www.youtube.com/watch?v=qtTEzFSMqJg&t=779s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I do on all my deals is I say, "Hey, if I was going to do an assignment on '
              "this, like we're double closing it, right? But an assignment, you were going to "
              'have to pay all the closing costs anyways." So I put the BC closing costs still '
              'on my in buyer.',
      'timestamp': 779,
      'timestamp_label': '[00:12:59]',
      'timestamp_seconds': 779,
      'tip': 'I do on all my deals is I say, "Hey, if I was going to do an assignment on this, '
             "like we're double closing it, right? But an assignment, you were going to have "
             'to pay all the closing costs anyways." So I put the BC closing costs still on my '
             'in buyer.',
      'title': 'Wholesaling In 2026: Double Closing, Transactional Funding & Protecting Your '
               'Spread | EP1 (Closer Control)',
      'url': 'https://www.youtube.com/watch?v=qtTEzFSMqJg&t=779s',
      'video_id': 'qtTEzFSMqJg'},
     {'author': 'Michael Daniel Investments',
      'channel': 'Michael Daniel Investments',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=0EcBhBq5U08&t=40s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Before a bank will look at it. The seller won't wait around for that. A bridge "
              "lender can often move  quickly because the question it's asking.",
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': "Before a bank will look at it. The seller won't wait around for that. A bridge "
             "lender can often move  quickly because the question it's asking.",
      'title': 'How a Real Estate Bridge Loan Works (and What Goes Wrong) (Michael Daniel '
               'Investments)',
      'url': 'https://www.youtube.com/watch?v=0EcBhBq5U08&t=40s',
      'video_id': '0EcBhBq5U08'},
     {'author': 'Adam Dobrinich | East Bay Realtor',
      'channel': 'Adam Dobrinich | East Bay Realtor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=FLFrQtywQ5g&t=42s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Wire into the esro company which would be the remainder of your down payment '
              "and any closing costs now again we're going to take a real quick pause here.",
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': 'Wire into the esro company which would be the remainder of your down payment and '
             "any closing costs now again we're going to take a real quick pause here.",
      'title': 'Buyer Escrow Process Step Ten | Fund Loan & Close (Adam Dobrinich | East Bay '
               'Realtor)',
      'url': 'https://www.youtube.com/watch?v=FLFrQtywQ5g&t=42s',
      'video_id': 'FLFrQtywQ5g'},
     {'author': 'Chris Bounds | AI Deal Flow for Real Estate',
      'channel': 'Chris Bounds | AI Deal Flow for Real Estate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:48](https://www.youtube.com/watch?v=FG5mYU_-AVQ&t=228s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Multi-family where you've got to raise five million maybe race four but you "
              "need the other million to close and you'll finish raising it post closing.",
      'timestamp': 228,
      'timestamp_label': '[00:03:48]',
      'timestamp_seconds': 228,
      'tip': "Multi-family where you've got to raise five million maybe race four but you need "
             "the other million to close and you'll finish raising it post closing.",
      'title': 'How To Finance A Wholesale Deal | Transactional Funding In Real Estate '
               'Explained (Chris Bounds | AI Deal Flow for Real Estate)',
      'url': 'https://www.youtube.com/watch?v=FG5mYU_-AVQ&t=228s',
      'video_id': 'FG5mYU_-AVQ'},
     {'author': 'Velocity Channel',
      'channel': 'Velocity Channel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:42](https://www.youtube.com/watch?v=5IAt1l4ev5w&t=282s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Just opened the business bank account yesterday then your business started when '
              "it started yesterday we're going to go ahead and hammer on this in the next "
              'lesson I want to see you over there Pronto okay thank you so much for watching '
              "we'll see you in the next lesson.",
      'timestamp': 282,
      'timestamp_label': '[00:04:42]',
      'timestamp_seconds': 282,
      'tip': 'Just opened the business bank account yesterday then your business started when '
             "it started yesterday we're going to go ahead and hammer on this in the next "
             'lesson I want to see you over there Pronto okay thank you so much for watching '
             "we'll see you in the next lesson.",
      'title': 'How To Get At Least $50,000 In Business Lines Of Credit In Just 6 Months... '
               'Part 2 (Velocity Channel)',
      'url': 'https://www.youtube.com/watch?v=5IAt1l4ev5w&t=282s',
      'video_id': '5IAt1l4ev5w'},
     {'author': 'Beth Pinkley Johnson - Private Money Lending Coach',
      'channel': 'Beth Pinkley Johnson - Private Money Lending Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:02](https://www.youtube.com/watch?v=qCwj0Q01AJY&t=182s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So choose whether or not location of investment and if that matters to you or '
              'not. This will be important consideration before choosing which path to go '
              "down. So there's really four different ways in which you can be the bank and be "
              'a private money lender.',
      'timestamp': 182,
      'timestamp_label': '[00:03:02]',
      'timestamp_seconds': 182,
      'tip': 'So choose whether or not location of investment and if that matters to you or '
             'not. This will be important consideration before choosing which path to go down. '
             "So there's really four different ways in which you can be the bank and be a "
             'private money lender.',
      'title': 'Why YOU Should Become a Private Money Lender in 2025 | Top 5 Reasons (Beth '
               'Pinkley Johnson - Private Money Lending Coach)',
      'url': 'https://www.youtube.com/watch?v=qCwj0Q01AJY&t=182s',
      'video_id': 'qCwj0Q01AJY'},
     {'author': 'Ryan Schrope',
      'channel': 'Ryan Schrope',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:56](https://www.youtube.com/watch?v=KQxDCgfJ6VA&t=476s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Every time you use the word EMD double close stack method, people can search '
              'that. And then when they do search that, the way that it will pop up at the top '
              'is if what you made, whatever post you made garnered more attention than the '
              "others. That's what posted at the top.",
      'timestamp': 476,
      'timestamp_label': '[00:07:56]',
      'timestamp_seconds': 476,
      'tip': 'Every time you use the word EMD double close stack method, people can search '
             'that. And then when they do search that, the way that it will pop up at the top '
             'is if what you made, whatever post you made garnered more attention than the '
             "others. That's what posted at the top.",
      'title': "His transactional funding business needs better leads. Here's the simple fix "
               '(Ryan Schrope)',
      'url': 'https://www.youtube.com/watch?v=KQxDCgfJ6VA&t=476s',
      'video_id': 'KQxDCgfJ6VA'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:41](https://www.youtube.com/watch?v=_WfyIRKBE8o&t=161s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I use to make money, but the shovel is the tool I use to dig that ditch. 0 is '
              'lending money to people who are fixing and flipping, doing BRRR loans, '
              "commercial loans, all sorts of loans. Go back and watch the training, it'll "
              'tell you all the ditches that you can dig.',
      'timestamp': 161,
      'timestamp_label': '[00:02:41]',
      'timestamp_seconds': 161,
      'tip': 'I use to make money, but the shovel is the tool I use to dig that ditch. 0 is '
             'lending money to people who are fixing and flipping, doing BRRR loans, '
             "commercial loans, all sorts of loans. Go back and watch the training, it'll tell "
             'you all the ditches that you can dig.',
      'title': 'NEW Gator Lending Strategies And Tools | Gator Method (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=_WfyIRKBE8o&t=161s',
      'video_id': '_WfyIRKBE8o'},
     {'author': 'Investor Fuel - Real Estate Mastermind',
      'channel': 'Investor Fuel - Real Estate Mastermind',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:25](https://www.youtube.com/watch?v=RyQUnNc92YU&t=385s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Leaders across the real estate investing industry they're available affluent "
              'calm / shows for simply search for flip nerd in the iTunes Store.',
      'timestamp': 385,
      'timestamp_label': '[00:06:25]',
      'timestamp_seconds': 385,
      'tip': "Leaders across the real estate investing industry they're available affluent "
             'calm / shows for simply search for flip nerd in the iTunes Store.',
      'title': 'Transactional Funding for Wholesaling with Lex Levinrad (Investor Fuel - Real '
               'Estate Mastermind)',
      'url': 'https://www.youtube.com/watch?v=RyQUnNc92YU&t=385s',
      'video_id': 'RyQUnNc92YU'},
     {'author': 'Flipping Mastery TV',
      'channel': 'Flipping Mastery TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:16](https://www.youtube.com/watch?v=0A2TpKfV1Os&t=556s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So yeah okay um yeah so but but I do that as I I find it seldom a good idea to '
              "let buyers no yeah yeah penny's done this a long time spencer.",
      'timestamp': 556,
      'timestamp_label': '[00:09:16]',
      'timestamp_seconds': 556,
      'tip': 'So yeah okay um yeah so but but I do that as I I find it seldom a good idea to '
             "let buyers no yeah yeah penny's done this a long time spencer.",
      'title': 'Watch Me Get The Title Company To Close My Wholesale Deal (Flipping Mastery '
               'TV)',
      'url': 'https://www.youtube.com/watch?v=0A2TpKfV1Os&t=556s',
      'video_id': '0A2TpKfV1Os'},
     {'author': 'Robert Greenblatt | South Jersey Real Estate',
      'channel': 'Robert Greenblatt | South Jersey Real Estate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:08](https://www.youtube.com/watch?v=CCWuS-x3COc&t=128s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Scenario plays out and you just don't want the house well you can't just walk "
              "away that way sometimes that becomes a negotiation but it doesn't automatically "
              "revert to either party in the transaction that's a really big piece of escrow.",
      'timestamp': 128,
      'timestamp_label': '[00:02:08]',
      'timestamp_seconds': 128,
      'tip': "Scenario plays out and you just don't want the house well you can't just walk "
             "away that way sometimes that becomes a negotiation but it doesn't automatically "
             "revert to either party in the transaction that's a really big piece of escrow.",
      'title': 'What Is ESCROW DEPOSIT? (Earnest Money) | Real Estate In 3 Minutes (Robert '
               'Greenblatt | South Jersey Real Estate)',
      'url': 'https://www.youtube.com/watch?v=CCWuS-x3COc&t=128s',
      'video_id': 'CCWuS-x3COc'},
     {'author': 'LearnREInvesting',
      'channel': 'LearnREInvesting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:28](https://www.youtube.com/watch?v=2MOHSWLCCqc&t=388s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Video are average 3 to eight times larger than what some wholesalers expect '
              "from a deal don't fall into believing that you can't make serious money on your "
              'deals and then you go and accept tips from your end.',
      'timestamp': 388,
      'timestamp_label': '[00:06:28]',
      'timestamp_seconds': 388,
      'tip': 'Video are average 3 to eight times larger than what some wholesalers expect from '
             "a deal don't fall into believing that you can't make serious money on your deals "
             'and then you go and accept tips from your end.',
      'title': '20 Deals Using Transactional Funding With No Upfront Fees (LearnREInvesting)',
      'url': 'https://www.youtube.com/watch?v=2MOHSWLCCqc&t=388s',
      'video_id': '2MOHSWLCCqc'}],
 9: [{'author': 'LearnREInvesting',
      'channel': 'LearnREInvesting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=0u7L7Q7CE5o&t=168s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Compare operational requirements as well as price, state coverage, title '
              'company rules, and buyer verification, timing, and maximum deal size. Get the '
              'final fee and funding conditions in writing before the closing package is '
              'finalized.',
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': 'Compare operational requirements as well as price, state coverage, title company '
             'rules, and buyer verification, timing, and maximum deal size. Get the final fee '
             'and funding conditions in writing before the closing package is finalized.',
      'title': 'Comparison of Transactional Funding Rates (Avoid Overpaying!) '
               '(LearnREInvesting)',
      'url': 'https://www.youtube.com/watch?v=0u7L7Q7CE5o&t=168s',
      'video_id': '0u7L7Q7CE5o'},
     {'author': 'The Full Deal REI',
      'channel': 'The Full Deal REI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:29](https://www.youtube.com/watch?v=H-3pmQVYvCI&t=509s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t see each other's numbers. But deeds are public record, so a motivated person "
              "could piece it together. Follow your state's disclosure rules. What contract do "
              'I use with the end buyer? A regular purchase agreement, with you as the seller.',
      'timestamp': 509,
      'timestamp_label': '[00:08:29]',
      'timestamp_seconds': 509,
      'tip': "'t see each other's numbers. But deeds are public record, so a motivated person "
             "could piece it together. Follow your state's disclosure rules. What contract do "
             'I use with the end buyer? A regular purchase agreement, with you as the seller.',
      'title': 'How Much Does Transactional Funding Cost (Real Example + What Lenders Require) '
               '(The Full Deal REI)',
      'url': 'https://www.youtube.com/watch?v=H-3pmQVYvCI&t=509s',
      'video_id': 'H-3pmQVYvCI'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=9-Vzu27aIq0&t=120s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you're a real estate agent, how many times does your state contract satisfy "
              'exactly what your agreement with the buyer, the seller is? How many times do '
              'you have to do addendums to your contracts? What percent of the time do when '
              'you do a deal?',
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': "If you're a real estate agent, how many times does your state contract satisfy "
             'exactly what your agreement with the buyer, the seller is? How many times do you '
             'have to do addendums to your contracts? What percent of the time do when you do '
             'a deal?',
      'title': 'When Do You Need A JV Agreement? (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=9-Vzu27aIq0&t=120s',
      'video_id': '9-Vzu27aIq0'},
     {'author': 'The Treasure Valley Home Show',
      'channel': 'The Treasure Valley Home Show',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:45](https://www.youtube.com/watch?v=5lKK7iczAKk&t=765s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It has to be agreed by um and approved by both brokerages, right? The the the '
              "listing office and the the selling or the buyer's agent office are going to "
              "have to mutually agree on that. And it's it's it's referenced specifically in "
              'the contract.',
      'timestamp': 765,
      'timestamp_label': '[00:12:45]',
      'timestamp_seconds': 765,
      'tip': 'It has to be agreed by um and approved by both brokerages, right? The the the '
             "listing office and the the selling or the buyer's agent office are going to have "
             "to mutually agree on that. And it's it's it's referenced specifically in the "
             'contract.',
      'title': 'How to Protect Your Earnest Money | Home Buying Ep. 6 (The Treasure Valley '
               'Home Show)',
      'url': 'https://www.youtube.com/watch?v=5lKK7iczAKk&t=765s',
      'video_id': '5lKK7iczAKk'},
     {'author': 'Tony Zowd',
      'channel': 'Tony Zowd',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=KmNl8nlbUxw&t=28s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now have a new document a CD also a closing disclosure that's typically only "
              'going to have the buyer information on one and the sellers information on one.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': "Now have a new document a CD also a closing disclosure that's typically only "
             'going to have the buyer information on one and the sellers information on one.',
      'title': "What's the difference between a ALTA, HUD-1 & CD (Tony Zowd)",
      'url': 'https://www.youtube.com/watch?v=KmNl8nlbUxw&t=28s',
      'video_id': 'KmNl8nlbUxw'},
     {'author': 'Yanowitz Law Firm, PLLC │ Will & Trust Lawyers',
      'channel': 'Yanowitz Law Firm, PLLC │ Will & Trust Lawyers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=D8jafo21-34&t=59s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But here's where it gets tricky and potentially expensive. If the deal falls "
              'apart, who gets the earnest money? That generally depends entirely on the '
              'purchase agreement and your contingencies. Contingencies are legal escape '
              'clauses in the contract.',
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': "But here's where it gets tricky and potentially expensive. If the deal falls "
             'apart, who gets the earnest money? That generally depends entirely on the '
             'purchase agreement and your contingencies. Contingencies are legal escape '
             'clauses in the contract.',
      'title': 'What Is Earnest Money in Real Estate  And How to Avoid Losing It (Yanowitz Law '
               'Firm, PLLC │ Will & Trust Lawyers)',
      'url': 'https://www.youtube.com/watch?v=D8jafo21-34&t=59s',
      'video_id': 'D8jafo21-34'},
     {'author': 'House Math',
      'channel': 'House Math',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:57](https://www.youtube.com/watch?v=IDV1BO2CYmg&t=237s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Not to the bank, but to unpaid property taxes. Sam's house is safe, but his "
              'neighbor Frank still owes on his mortgage, and he never wrote a will. So, what '
              "happens to Frank's house if he dies? Rules on taxes, liens, and tax sales are "
              'different in every state and county.',
      'timestamp': 237,
      'timestamp_label': '[00:03:57]',
      'timestamp_seconds': 237,
      'tip': "Not to the bank, but to unpaid property taxes. Sam's house is safe, but his "
             'neighbor Frank still owes on his mortgage, and he never wrote a will. So, what '
             "happens to Frank's house if he dies? Rules on taxes, liens, and tax sales are "
             'different in every state and county.',
      'title': "What Happens If You Don't Pay Property Taxes on a Paid-Off House? (House Math)",
      'url': 'https://www.youtube.com/watch?v=IDV1BO2CYmg&t=237s',
      'video_id': 'IDV1BO2CYmg'},
     {'author': 'Hard Money Mastermind',
      'channel': 'Hard Money Mastermind',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:51](https://www.youtube.com/watch?v=bNJYDcDSFxU&t=711s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um, we obviously have commercial purpose language in there that the title '
              "company has to state as well that yes, as far as they're concerned, this is a "
              'commercial purpose transaction.',
      'timestamp': 711,
      'timestamp_label': '[00:11:51]',
      'timestamp_seconds': 711,
      'tip': 'Um, we obviously have commercial purpose language in there that the title '
             "company has to state as well that yes, as far as they're concerned, this is a "
             'commercial purpose transaction.',
      'title': 'The Exact Loan Documents We Use as Private Lenders (Hard Money Mastermind)',
      'url': 'https://www.youtube.com/watch?v=bNJYDcDSFxU&t=711s',
      'video_id': 'bNJYDcDSFxU'},
     {'author': 'AmericanHomeland',
      'channel': 'AmericanHomeland',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:54](https://www.youtube.com/watch?v=go0zT3tGaQo&t=174s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Hud-1 settlement statement so guys that pretty much sums it up if you have any '
              'more questions about how to read a closing disclosure or a hud-1 settlement '
              'statement reach out to us at American homeland title.',
      'timestamp': 174,
      'timestamp_label': '[00:02:54]',
      'timestamp_seconds': 174,
      'tip': 'Hud-1 settlement statement so guys that pretty much sums it up if you have any '
             'more questions about how to read a closing disclosure or a hud-1 settlement '
             'statement reach out to us at American homeland title.',
      'title': 'Reading a Closing Disclosure and an ALTA HUD 1 Settlement Statement '
               '(AmericanHomeland)',
      'url': 'https://www.youtube.com/watch?v=go0zT3tGaQo&t=174s',
      'video_id': 'go0zT3tGaQo'},
     {'author': 'Brandy Battres',
      'channel': 'Brandy Battres',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:41](https://www.youtube.com/watch?v=mgqTnWybcW8&t=41s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But here’s the key: this deposit isn’t just free money that you get back. If '
              'everything goes smoothly, it gets applied toward your down payment or closing '
              'costs. But if you back out without a valid reason, like a contingency in your '
              'contract, you could lose that money!',
      'timestamp': 41,
      'timestamp_label': '[00:00:41]',
      'timestamp_seconds': 41,
      'tip': 'But here’s the key: this deposit isn’t just free money that you get back. If '
             'everything goes smoothly, it gets applied toward your down payment or closing '
             'costs. But if you back out without a valid reason, like a contingency in your '
             'contract, you could lose that money!',
      'title': 'BUYERS: Don’t Lose Your Earnest Money Deposit! (Brandy Battres)',
      'url': 'https://www.youtube.com/watch?v=mgqTnWybcW8&t=41s',
      'video_id': 'mgqTnWybcW8'},
     {'author': 'Kai Lu',
      'channel': 'Kai Lu',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:59](https://www.youtube.com/watch?v=pqyNMc1tJj4&t=119s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The terms and conditions it's time for you to instruct your lawyer to start the "
              "legal work that's your step number three so as promised earlier i'm going to.",
      'timestamp': 119,
      'timestamp_label': '[00:01:59]',
      'timestamp_seconds': 119,
      'tip': "The terms and conditions it's time for you to instruct your lawyer to start the "
             "legal work that's your step number three so as promised earlier i'm going to.",
      'title': 'How to Become a Private Lender in 3 Steps (Kai Lu)',
      'url': 'https://www.youtube.com/watch?v=pqyNMc1tJj4&t=119s',
      'video_id': 'pqyNMc1tJj4'},
     {'author': 'Realtypath',
      'channel': 'Realtypath',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:33](https://www.youtube.com/watch?v=XlKk96ekJTE&t=573s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Do in order to give you the information that is against a property and to know '
              "our road mapap for what we need to do to ensure that you're getting clear title "
              "awesome all right now we got a bunch of those terms out of the way let's figure "
              'out why do we need Title.',
      'timestamp': 573,
      'timestamp_label': '[00:09:33]',
      'timestamp_seconds': 573,
      'tip': 'Do in order to give you the information that is against a property and to know '
             "our road mapap for what we need to do to ensure that you're getting clear title "
             "awesome all right now we got a bunch of those terms out of the way let's figure "
             'out why do we need Title.',
      'title': 'JumpStart - Contract to Close - Understanding Title & Escrow (Realtypath)',
      'url': 'https://www.youtube.com/watch?v=XlKk96ekJTE&t=573s',
      'video_id': 'XlKk96ekJTE'},
     {'author': 'The Secret TLC 777',
      'channel': 'The Secret TLC 777',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:20](https://www.youtube.com/watch?v=eFyovu8iZIA&t=980s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Payment 15 USC 1681 a and we're going to look at d 2 a 1. so let's go to 15 USC "
              "1681a definitions and rules of construction we're talking about late payments "
              "all right so we're going to go to D2 talking about Consumer Report.",
      'timestamp': 980,
      'timestamp_label': '[00:16:20]',
      'timestamp_seconds': 980,
      'tip': "Payment 15 USC 1681 a and we're going to look at d 2 a 1. so let's go to 15 USC "
             "1681a definitions and rules of construction we're talking about late payments "
             "all right so we're going to go to D2 talking about Consumer Report.",
      'title': 'High Interest Rates #Usury Law #Predatory Lending (The Secret TLC 777)',
      'url': 'https://www.youtube.com/watch?v=eFyovu8iZIA&t=980s',
      'video_id': 'eFyovu8iZIA'},
     {'author': 'TownCenter Partners Litigation Finance',
      'channel': 'TownCenter Partners Litigation Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:32](https://www.youtube.com/watch?v=YahUsg3anlA&t=152s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Litigation funding conformed to uninformed preconceptions where the law '
              'establishes that alone is a transaction involving an absolute duty to repay '
              'litigation funding should not be characterized as alone if you need help with '
              'litigation funding call or email me today.',
      'timestamp': 152,
      'timestamp_label': '[00:02:32]',
      'timestamp_seconds': 152,
      'tip': 'Litigation funding conformed to uninformed preconceptions where the law '
             'establishes that alone is a transaction involving an absolute duty to repay '
             'litigation funding should not be characterized as alone if you need help with '
             'litigation funding call or email me today.',
      'title': 'How Usury & Other Consumer Lending Regulations Can Affect Litigation Finance '
               'Agreements (TownCenter Partners Litigation Finance)',
      'url': 'https://www.youtube.com/watch?v=YahUsg3anlA&t=152s',
      'video_id': 'YahUsg3anlA'},
     {'author': 'LearnREInvesting',
      'channel': 'LearnREInvesting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:14](https://www.youtube.com/watch?v=VGIfE33jspg&t=194s)',
      'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                   "transactional double-close funding, earnest-money ('Gator') lending, and "
                   '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Requirement on two of the sites as I mentioned shortfunding.com '
              'transactionalfunding.com thanks for joining me for this overview of '
              'transactional funders and I wish you unlimited success in your real estate '
              'investing career.',
      'timestamp': 194,
      'timestamp_label': '[00:03:14]',
      'timestamp_seconds': 194,
      'tip': 'Requirement on two of the sites as I mentioned shortfunding.com '
             'transactionalfunding.com thanks for joining me for this overview of '
             'transactional funders and I wish you unlimited success in your real estate '
             'investing career.',
      'title': 'Transactional Funding| Warning Transactional Lenders Not The Same '
               '(LearnREInvesting)',
      'url': 'https://www.youtube.com/watch?v=VGIfE33jspg&t=194s',
      'video_id': 'VGIfE33jspg'}],
 10: [{'author': 'David Olds REI',
       'channel': 'David Olds REI',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:36](https://www.youtube.com/watch?v=KG3yn1b1Yr4&t=756s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So the way that we fund it is once all the closing docs are signed, and the '
               'closing company will show us, and once your end buyer is fully committed and '
               "they put their money in escrow, >> Mhm. 'll wire over that money that you need "
               'to close the first transaction.',
       'timestamp': 756,
       'timestamp_label': '[00:12:36]',
       'timestamp_seconds': 756,
       'tip': 'So the way that we fund it is once all the closing docs are signed, and the '
              'closing company will show us, and once your end buyer is fully committed and '
              "they put their money in escrow, >> Mhm. 'll wire over that money that you need "
              'to close the first transaction.',
       'title': 'Why Smart Wholesalers Are Utilizing Double Closings (David Olds REI)',
       'url': 'https://www.youtube.com/watch?v=KG3yn1b1Yr4&t=756s',
       'video_id': 'KG3yn1b1Yr4'},
      {'author': 'LearnREInvesting',
       'channel': 'LearnREInvesting',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:04](https://www.youtube.com/watch?v=sZe_QRsB_NE&t=64s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Between then and the time the end buyer signs his required documents, the HUD '
               'one closing statement, hold harmless agreement, or other documents is required '
               "by the closing agent. They're transactional funding lenders who advertise 30, "
               '60, or even 90day transactional funding.',
       'timestamp': 64,
       'timestamp_label': '[00:01:04]',
       'timestamp_seconds': 64,
       'tip': 'Between then and the time the end buyer signs his required documents, the HUD '
              'one closing statement, hold harmless agreement, or other documents is required '
              "by the closing agent. They're transactional funding lenders who advertise 30, "
              '60, or even 90day transactional funding.',
       'title': 'Transactional Funding How Long Can You Use It?|Real Estate '
                'Investing|Best|Lending|lender|Fl (LearnREInvesting)',
       'url': 'https://www.youtube.com/watch?v=sZe_QRsB_NE&t=64s',
       'video_id': 'sZe_QRsB_NE'},
      {'author': 'Ryan Schrope',
       'channel': 'Ryan Schrope',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:09](https://www.youtube.com/watch?v=2a2qJD8P3gI&t=969s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'John, my this double close is closing tomorrow. And so what needs to happen '
               'for this double close, which is way different again than a stack method, is '
               'that John could wire the money directly to the title company >> Uh-huh. It '
               "doesn't have to come from yours.",
       'timestamp': 969,
       'timestamp_label': '[00:16:09]',
       'timestamp_seconds': 969,
       'tip': 'John, my this double close is closing tomorrow. And so what needs to happen for '
              'this double close, which is way different again than a stack method, is that '
              "John could wire the money directly to the title company >> Uh-huh. It doesn't "
              'have to come from yours.',
       'title': 'His transactional funding business is targeting the wrong people, watch me '
                'fix it (Ryan Schrope)',
       'url': 'https://www.youtube.com/watch?v=2a2qJD8P3gI&t=969s',
       'video_id': '2a2qJD8P3gI'},
      {'author': 'Jasper Cool',
       'channel': 'Jasper Cool',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:16](https://www.youtube.com/watch?v=EUE6UWl2qBA&t=76s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Closing date, just whatever date you have scheduled to close, you can put that '
               "right here. If you click on this little thing, it'll open up the calendar and "
               'you can pick the date. Next, closing attorney or title company. This just '
               'means who is actually closing your deal.',
       'timestamp': 76,
       'timestamp_label': '[00:01:16]',
       'timestamp_seconds': 76,
       'tip': 'Closing date, just whatever date you have scheduled to close, you can put that '
              "right here. If you click on this little thing, it'll open up the calendar and "
              'you can pick the date. Next, closing attorney or title company. This just means '
              'who is actually closing your deal.',
       'title': 'How to Get Double Close Funding for Your Wholesale Deals (FAST!) (Jasper '
                'Cool)',
       'url': 'https://www.youtube.com/watch?v=EUE6UWl2qBA&t=76s',
       'video_id': 'EUE6UWl2qBA'},
      {'author': 'One Percent | Wholesaling Real Estate',
       'channel': 'One Percent | Wholesaling Real Estate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:44](https://www.youtube.com/watch?v=YO8RBYT_lQ0&t=164s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Escro agent whether it be the title company or title attorney they are liable '
               'to give that deposit back to you no questions asked it says if buyer.',
       'timestamp': 164,
       'timestamp_label': '[00:02:44]',
       'timestamp_seconds': 164,
       'tip': 'Escro agent whether it be the title company or title attorney they are liable '
              'to give that deposit back to you no questions asked it says if buyer.',
       'title': 'Earnest Money Deposit & Inspection Period EXPLAINED | Real Estate Wholesaling '
                '(One Percent | Wholesaling Real Estate)',
       'url': 'https://www.youtube.com/watch?v=YO8RBYT_lQ0&t=164s',
       'video_id': 'YO8RBYT_lQ0'},
      {'author': 'Christopher Grant',
       'channel': 'Christopher Grant',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:36:49](https://www.youtube.com/watch?v=-M4ZoYEoh3k&t=2209s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You got another card 20% or 20K 0% APR the other Chase Ink Unlimited and then '
               'you can take that available balance combine it over and now you have 40K. And '
               'then you can still start the 12 months all over again.',
       'timestamp': 2209,
       'timestamp_label': '[00:36:49]',
       'timestamp_seconds': 2209,
       'tip': 'You got another card 20% or 20K 0% APR the other Chase Ink Unlimited and then '
              'you can take that available balance combine it over and now you have 40K. And '
              'then you can still start the 12 months all over again.',
       'title': 'How He Built $385K in 0% Credit Lines to Scale Amazon Online Arbitrage '
                '(Christopher Grant)',
       'url': 'https://www.youtube.com/watch?v=-M4ZoYEoh3k&t=2209s',
       'video_id': '-M4ZoYEoh3k'},
      {'author': 'Marvin Francois',
       'channel': 'Marvin Francois',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:57:25](https://www.youtube.com/watch?v=Ksec0I8vpLQ&t=3445s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s all kind of the same thing. So, I kind of >> walk me through it. Walk me "
               'through So when we get to sales, remember guys, this is one of the highest '
               'leverage things you can have in the business, right?',
       'timestamp': 3445,
       'timestamp_label': '[00:57:25]',
       'timestamp_seconds': 3445,
       'tip': "'s all kind of the same thing. So, I kind of >> walk me through it. Walk me "
              'through So when we get to sales, remember guys, this is one of the highest '
              'leverage things you can have in the business, right?',
       'title': 'The $100K Funding Masterclass: 0% Credit Stacking, CDFIs, and Funding '
                'Businesses Explained (Marvin Francois)',
       'url': 'https://www.youtube.com/watch?v=Ksec0I8vpLQ&t=3445s',
       'video_id': 'Ksec0I8vpLQ'},
      {'author': 'Jack McColl',
       'channel': 'Jack McColl',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:17](https://www.youtube.com/watch?v=gUK5DvwuWnQ&t=497s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Like little building blocks um in real estate getting getting  some you know '
               'learning learning the lessons on a smaller scale gang getting some.',
       'timestamp': 497,
       'timestamp_label': '[00:08:17]',
       'timestamp_seconds': 497,
       'tip': 'Like little building blocks um in real estate getting getting  some you know '
              'learning learning the lessons on a smaller scale gang getting some.',
       'title': 'How He Got $170K in 0% Credit and Built 6 Airbnb Listings (Jack McColl)',
       'url': 'https://www.youtube.com/watch?v=gUK5DvwuWnQ&t=497s',
       'video_id': 'gUK5DvwuWnQ'},
      {'author': 'Pace Morby',
       'channel': 'Pace Morby',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:16](https://www.youtube.com/watch?v=iVg9EsSij2c&t=136s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Because the National Association of Realtors doesn't like wholesalers. They "
               'want to get rid of wholesalers. And the best way to not be a wholesaler is to '
               'actually buy the property and then sell it to your buyer. This wholesaler '
               'needs double close money.',
       'timestamp': 136,
       'timestamp_label': '[00:02:16]',
       'timestamp_seconds': 136,
       'tip': "Because the National Association of Realtors doesn't like wholesalers. They "
              'want to get rid of wholesalers. And the best way to not be a wholesaler is to '
              'actually buy the property and then sell it to your buyer. This wholesaler needs '
              'double close money.',
       'title': 'Why the Gator Method Is a Great Way to Get Started in Real Estate (Pace '
                'Morby)',
       'url': 'https://www.youtube.com/watch?v=iVg9EsSij2c&t=136s',
       'video_id': 'iVg9EsSij2c'},
      {'author': 'Radikal Marketer',
       'channel': 'Radikal Marketer',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:33](https://www.youtube.com/watch?v=Oa3bugxGPHE&t=693s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Down on one to two things like it's not just about the score and it's not just "
               "about the bank that can give you the money it's about all the other things "
               "that make up a big picture we have to think big picture with credit or we're "
               'not going to win in the game yep.',
       'timestamp': 693,
       'timestamp_label': '[00:11:33]',
       'timestamp_seconds': 693,
       'tip': "Down on one to two things like it's not just about the score and it's not just "
              "about the bank that can give you the money it's about all the other things that "
              "make up a big picture we have to think big picture with credit or we're not "
              'going to win in the game yep.',
       'title': 'CREDIT CARD STACKING EXPOSED 🔥 | TRUTH BEHIND 0% BUSINESS CREDIT CARD '
                'FUNDING! (Radikal Marketer)',
       'url': 'https://www.youtube.com/watch?v=Oa3bugxGPHE&t=693s',
       'video_id': 'Oa3bugxGPHE'},
      {'author': 'Molly Tennant',
       'channel': 'Molly Tennant',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:51](https://www.youtube.com/watch?v=TTA8OtC6qJs&t=51s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Of different ways that you can put this together for a couple of different '
               "types of transactions but usually it's like hey I want to bring $20,000 to "
               'close on.',
       'timestamp': 51,
       'timestamp_label': '[00:00:51]',
       'timestamp_seconds': 51,
       'tip': 'Of different ways that you can put this together for a couple of different '
              "types of transactions but usually it's like hey I want to bring $20,000 to "
              'close on.',
       'title': 'Real Estate Joint Venture Agreement Explained by Molly Tennant (Molly '
                'Tennant)',
       'url': 'https://www.youtube.com/watch?v=TTA8OtC6qJs&t=51s',
       'video_id': 'TTA8OtC6qJs'},
      {'author': 'Korean Atlanta Mentorship',
       'channel': 'Korean Atlanta Mentorship',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=NgkU4dL1_sU&t=20s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Got lots of lines of credit. In fact, I have 26 lines of credit that equal up '
               'to $494,000 in limits. Let me go ahead and zoom in there. Business credit '
               'cards, personal credit cards, personal lines of credit, personal lines of '
               'credit.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'Got lots of lines of credit. In fact, I have 26 lines of credit that equal up '
              'to $494,000 in limits. Let me go ahead and zoom in there. Business credit '
              'cards, personal credit cards, personal lines of credit, personal lines of '
              'credit.',
       'title': 'The SECRET to Getting LINES OF CREDIT - Velocity Banking Explained (Korean '
                'Atlanta Mentorship)',
       'url': 'https://www.youtube.com/watch?v=NgkU4dL1_sU&t=20s',
       'video_id': 'NgkU4dL1_sU'},
      {'author': 'Jeb Smith',
       'channel': 'Jeb Smith',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:53](https://www.youtube.com/watch?v=xOBdb3zZB9Y&t=353s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Contact me directly I'm happy to help as always I appreciate you taking the "
               "time to watch and we'll see you again soon bye-bye.",
       'timestamp': 353,
       'timestamp_label': '[00:05:53]',
       'timestamp_seconds': 353,
       'tip': "Contact me directly I'm happy to help as always I appreciate you taking the "
              "time to watch and we'll see you again soon bye-bye.",
       'title': 'What is a bridge loan - How do bridge loans work? (Jeb Smith)',
       'url': 'https://www.youtube.com/watch?v=xOBdb3zZB9Y&t=353s',
       'video_id': 'xOBdb3zZB9Y'},
      {'author': 'Gary Pryde',
       'channel': 'Gary Pryde',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:31](https://www.youtube.com/watch?v=nKwv-ImRqjo&t=391s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Notifications to be notified anytime I upload another podcast remember this '
               'content is for informational purposes see you next time for more insights and '
               'strategies to help you crush your real estate goals.',
       'timestamp': 391,
       'timestamp_label': '[00:06:31]',
       'timestamp_seconds': 391,
       'tip': 'Notifications to be notified anytime I upload another podcast remember this '
              'content is for informational purposes see you next time for more insights and '
              'strategies to help you crush your real estate goals.',
       'title': '"Master the Basics: What You MUST Know About Promissory Notes Secured by '
                'Deeds of Trust!" (Gary Pryde)',
       'url': 'https://www.youtube.com/watch?v=nKwv-ImRqjo&t=391s',
       'video_id': 'nKwv-ImRqjo'},
      {'author': 'Pace Morby',
       'channel': 'Pace Morby',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:33:05](https://www.youtube.com/watch?v=z2rCv8gn1cE&t=1985s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "We'll put a link down in the Instagram uh Down Below guys and thank you so "
               'much for tuning in to another episode of get creative thanks PE.',
       'timestamp': 1985,
       'timestamp_label': '[00:33:05]',
       'timestamp_seconds': 1985,
       'tip': "We'll put a link down in the Instagram uh Down Below guys and thank you so much "
              'for tuning in to another episode of get creative thanks PE.',
       'title': 'How He Made $300K in Real Estate with NO Money: Gator Method Revealed (Pace '
                'Morby)',
       'url': 'https://www.youtube.com/watch?v=z2rCv8gn1cE&t=1985s',
       'video_id': 'z2rCv8gn1cE'}],
 11: [{'author': 'Sure Flow Capital Partners',
       'channel': 'Sure Flow Capital Partners',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:20](https://www.youtube.com/watch?v=2OXgeuq7LZU&t=80s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Even though your buyer is paying you minutes later, the order of operations '
               'requires real money to fund that A2B purchase before the BTOC sale funds to '
               "you. That's exactly what transactional funding does. It funds the first close "
               'so the second close can happen.',
       'timestamp': 80,
       'timestamp_label': '[00:01:20]',
       'timestamp_seconds': 80,
       'tip': 'Even though your buyer is paying you minutes later, the order of operations '
              'requires real money to fund that A2B purchase before the BTOC sale funds to '
              "you. That's exactly what transactional funding does. It funds the first close "
              'so the second close can happen.',
       'title': "Don't Lose Your Deal! How Transactional Funding Saves Double Closings (Sure "
                'Flow Capital Partners)',
       'url': 'https://www.youtube.com/watch?v=2OXgeuq7LZU&t=80s',
       'video_id': '2OXgeuq7LZU'},
      {'author': 'Odardo LLC',
       'channel': 'Odardo LLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:18](https://www.youtube.com/watch?v=aHsBrb_hBYw&t=78s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A is the seller, B is you, and C is your end buyer. Each leg has its own '
               'contract, its own closing statement, and its own deed. The two closings are '
               'often on the same day, sometimes back-to-back at the same title company. For a '
               'short time, you are the owner of record.',
       'timestamp': 78,
       'timestamp_label': '[00:01:18]',
       'timestamp_seconds': 78,
       'tip': 'A is the seller, B is you, and C is your end buyer. Each leg has its own '
              'contract, its own closing statement, and its own deed. The two closings are '
              'often on the same day, sometimes back-to-back at the same title company. For a '
              'short time, you are the owner of record.',
       'title': 'Assignment vs. Double Close: How Wholesalers Close Deals (Costs, Funding, '
                'Michigan Rules) | ORES 101 (Odardo LLC)',
       'url': 'https://www.youtube.com/watch?v=aHsBrb_hBYw&t=78s',
       'video_id': 'aHsBrb_hBYw'},
      {'author': 'Sure Flow Capital Partners',
       'channel': 'Sure Flow Capital Partners',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:42](https://www.youtube.com/watch?v=sXh1jFRArig&t=102s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Even though your buyer is paying you minutes later. The order of operations '
               'requires real money to fund that A to B purchase before the B to C sale leg '
               "funds to you. That's exactly what transactional funding does. It funds the "
               'first close so the second close can happen.',
       'timestamp': 102,
       'timestamp_label': '[00:01:42]',
       'timestamp_seconds': 102,
       'tip': 'Even though your buyer is paying you minutes later. The order of operations '
              'requires real money to fund that A to B purchase before the B to C sale leg '
              "funds to you. That's exactly what transactional funding does. It funds the "
              'first close so the second close can happen.',
       'title': 'How Wholesalers Use Transactional Funding to Double Close Deals (Without '
                'Using Their Own Money) (Sure Flow Capital Partners)',
       'url': 'https://www.youtube.com/watch?v=sXh1jFRArig&t=102s',
       'video_id': 'sXh1jFRArig'},
      {'author': 'Hard Money Mastermind',
       'channel': 'Hard Money Mastermind',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:00](https://www.youtube.com/watch?v=9g6lYN-Aei0&t=720s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Building a business is a very different skill set. No, I can relate to some of '
               "that based on early HMBB years. What like we didn't hire crazy. We just Jason "
               'and I just did everything ourselves to the point where it was really '
               'miserable.',
       'timestamp': 720,
       'timestamp_label': '[00:12:00]',
       'timestamp_seconds': 720,
       'tip': 'Building a business is a very different skill set. No, I can relate to some of '
              "that based on early HMBB years. What like we didn't hire crazy. We just Jason "
              'and I just did everything ourselves to the point where it was really miserable.',
       'title': "Tiffany High's Playbook for Scaling Flipping and Private Lending (Hard Money "
                'Mastermind)',
       'url': 'https://www.youtube.com/watch?v=9g6lYN-Aei0&t=720s',
       'video_id': '9g6lYN-Aei0'},
      {'author': 'Larry Mastropieri',
       'channel': 'Larry Mastropieri',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:11](https://www.youtube.com/watch?v=CSHBzTZo3Yc&t=71s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But what what are your thoughts on that? Yeah, I mean like the your first line '
               "of defense is obviously yourself and understanding what you're doing. The "
               "second is the person you hire to represent you, which is the buyer's agent as "
               'an example, right?',
       'timestamp': 71,
       'timestamp_label': '[00:01:11]',
       'timestamp_seconds': 71,
       'tip': 'But what what are your thoughts on that? Yeah, I mean like the your first line '
              "of defense is obviously yourself and understanding what you're doing. The "
              "second is the person you hire to represent you, which is the buyer's agent as "
              'an example, right?',
       'title': 'How can buyers protect their earnest money deposit in Florida? (Larry '
                'Mastropieri)',
       'url': 'https://www.youtube.com/watch?v=CSHBzTZo3Yc&t=71s',
       'video_id': 'CSHBzTZo3Yc'},
      {'author': 'ShortFunding',
       'channel': 'ShortFunding',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:30](https://www.youtube.com/watch?v=YWoKsJsQWbU&t=150s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Fundings company mission is to help you keep more of your flip profits by '
               'providing easier access to Capital at lower rates and with the highest level '
               "of professionalism I'm here to help you with that also I'll see you in the "
               'next video training segment goodbye for now.',
       'timestamp': 150,
       'timestamp_label': '[00:02:30]',
       'timestamp_seconds': 150,
       'tip': 'Fundings company mission is to help you keep more of your flip profits by '
              'providing easier access to Capital at lower rates and with the highest level of '
              "professionalism I'm here to help you with that also I'll see you in the next "
              'video training segment goodbye for now.',
       'title': 'What is Flash Cash  - How to Double Close Legally (ShortFunding)',
       'url': 'https://www.youtube.com/watch?v=YWoKsJsQWbU&t=150s',
       'video_id': 'YWoKsJsQWbU'},
      {'author': 'SEI Mortgage - Ryan Marks',
       'channel': 'SEI Mortgage - Ryan Marks',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:56](https://www.youtube.com/watch?v=d8gbJrywXFE&t=236s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': '6 to 12 months, so you want to make sure that you have an exit strategy as '
               'soon as you sell your departing residence in order to pay off that bridge loan '
               'and go into whatever your long-term financing is for the remaining house that '
               'you now own.',
       'timestamp': 236,
       'timestamp_label': '[00:03:56]',
       'timestamp_seconds': 236,
       'tip': '6 to 12 months, so you want to make sure that you have an exit strategy as soon '
              'as you sell your departing residence in order to pay off that bridge loan and '
              'go into whatever your long-term financing is for the remaining house that you '
              'now own.',
       'title': 'Ex-Big-Bank Lender Explains Bridge Loan Secrets in 6 Minutes (SEI Mortgage - '
                'Ryan Marks)',
       'url': 'https://www.youtube.com/watch?v=d8gbJrywXFE&t=236s',
       'video_id': 'd8gbJrywXFE'},
      {'author': 'LendingWise',
       'channel': 'LendingWise',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:49](https://www.youtube.com/watch?v=uVDb80-WSkw&t=169s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I think that the way the the dashboard and the loan files are organized makes '
               'it really easy for us to to close as many loans as we do. And I think that you '
               'know, Chris and team have really done a nice job staying on the front foot of '
               'the innovation.',
       'timestamp': 169,
       'timestamp_label': '[00:02:49]',
       'timestamp_seconds': 169,
       'tip': 'I think that the way the the dashboard and the loan files are organized makes '
              'it really easy for us to to close as many loans as we do. And I think that you '
              'know, Chris and team have really done a nice job staying on the front foot of '
              'the innovation.',
       'title': 'HouseMax CEO Jeff Fechter on Scaling Private Lending with LendingWise | '
                'Customer Testimonial (LendingWise)',
       'url': 'https://www.youtube.com/watch?v=uVDb80-WSkw&t=169s',
       'video_id': 'uVDb80-WSkw'},
      {'author': 'PropLogix',
       'channel': 'PropLogix',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:22](https://www.youtube.com/watch?v=k03c-6thJPg&t=142s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s not the end of the world. I know we live in a very busy you know time, but "
               'picking up the phone and calling your closer, your processor, the manager at '
               'the title company you know, your realtor, your lender just to verify.',
       'timestamp': 142,
       'timestamp_label': '[00:02:22]',
       'timestamp_seconds': 142,
       'tip': "'s not the end of the world. I know we live in a very busy you know time, but "
              'picking up the phone and calling your closer, your processor, the manager at '
              'the title company you know, your realtor, your lender just to verify.',
       'title': 'Title Expert Talks: Fending Off Wire Fraud in a Title Company (PropLogix)',
       'url': 'https://www.youtube.com/watch?v=k03c-6thJPg&t=142s',
       'video_id': 'k03c-6thJPg'},
      {'author': 'Ryan Schrope',
       'channel': 'Ryan Schrope',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:21](https://www.youtube.com/watch?v=N4o948Y1Q-U&t=501s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'There are some variables that could come up like for example sometimes people '
               'might close at one title company and then do the second transaction at a.',
       'timestamp': 501,
       'timestamp_label': '[00:08:21]',
       'timestamp_seconds': 501,
       'tip': 'There are some variables that could come up like for example sometimes people '
              'might close at one title company and then do the second transaction at a.',
       'title': 'Transactional Funding 101: Getting Started (Ryan Schrope)',
       'url': 'https://www.youtube.com/watch?v=N4o948Y1Q-U&t=501s',
       'video_id': 'N4o948Y1Q-U'},
      {'author': 'Toby Mathis Esq | Tax Planning & Asset Protection',
       'channel': 'Toby Mathis Esq | Tax Planning & Asset Protection',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=FiBdpAVfzMo&t=15s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "How to complete our real estate joint venture agreement you know it's pretty "
               "straight forwards if you've been doing it for a while and I can appreciate "
               'the.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': "How to complete our real estate joint venture agreement you know it's pretty "
              "straight forwards if you've been doing it for a while and I can appreciate the.",
       'title': 'Real Estate Joint Venture Agreement Walkthrough (Toby Mathis Esq | Tax '
                'Planning & Asset Protection)',
       'url': 'https://www.youtube.com/watch?v=FiBdpAVfzMo&t=15s',
       'video_id': 'FiBdpAVfzMo'},
      {'author': 'Sunny Fedorenko',
       'channel': 'Sunny Fedorenko',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:25](https://www.youtube.com/watch?v=j0SpK9C7lHs&t=205s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'It must be done only through secure portals. I repeat, never ever ever even if '
               'it looks real. Rule number two, call the escro company directly, but call them '
               'using the number you were given in person, not the number in the email, not '
               'the number in the attachment.',
       'timestamp': 205,
       'timestamp_label': '[00:03:25]',
       'timestamp_seconds': 205,
       'tip': 'It must be done only through secure portals. I repeat, never ever ever even if '
              'it looks real. Rule number two, call the escro company directly, but call them '
              'using the number you were given in person, not the number in the email, not the '
              'number in the attachment.',
       'title': 'Wire Fraud in Escrow Is Getting Worse — Here’s How to Protect Yourself (Sunny '
                'Fedorenko)',
       'url': 'https://www.youtube.com/watch?v=j0SpK9C7lHs&t=205s',
       'video_id': 'j0SpK9C7lHs'},
      {'author': 'Pace Morby',
       'channel': 'Pace Morby',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:11](https://www.youtube.com/watch?v=x24Yz464jLE&t=71s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Finding them how i manage them what my team is doing i got i showed you guys '
               'my slack channel yesterday and showed you how my team is making decisions on '
               'every.',
       'timestamp': 71,
       'timestamp_label': '[00:01:11]',
       'timestamp_seconds': 71,
       'tip': 'Finding them how i manage them what my team is doing i got i showed you guys my '
              'slack channel yesterday and showed you how my team is making decisions on '
              'every.',
       'title': 'What is the Gator Method | Close Deals For $0 With Transactional Funding '
                '(Pace Morby)',
       'url': 'https://www.youtube.com/watch?v=x24Yz464jLE&t=71s',
       'video_id': 'x24Yz464jLE'},
      {'author': 'LearnREInvesting',
       'channel': 'LearnREInvesting',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:56](https://www.youtube.com/watch?v=a0yQnepWIA4&t=176s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The Deferred amount of time between the A to B and B to C CL closings this '
               'extended transactional financing is suitable for double closings that require '
               'a holding period before the title to the property can be deed to an end '
               'purchaser.',
       'timestamp': 176,
       'timestamp_label': '[00:02:56]',
       'timestamp_seconds': 176,
       'tip': 'The Deferred amount of time between the A to B and B to C CL closings this '
              'extended transactional financing is suitable for double closings that require a '
              'holding period before the title to the property can be deed to an end '
              'purchaser.',
       'title': 'What Is Extended Transactional Funding? (LearnREInvesting)',
       'url': 'https://www.youtube.com/watch?v=a0yQnepWIA4&t=176s',
       'video_id': 'a0yQnepWIA4'},
      {'author': 'Naam Wynn',
       'channel': 'Naam Wynn',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:07](https://www.youtube.com/watch?v=bdodeCpS6JI&t=787s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'They help you turn your business credit into working capital, but liquidating '
               'your card at a fee. So, the fee is usually around 6%. So, if you have $100,000 '
               'available in credit, you can liquidate up to 90% of that and walk away with '
               '$90,000 cash minus the fee.',
       'timestamp': 787,
       'timestamp_label': '[00:13:07]',
       'timestamp_seconds': 787,
       'tip': 'They help you turn your business credit into working capital, but liquidating '
              'your card at a fee. So, the fee is usually around 6%. So, if you have $100,000 '
              'available in credit, you can liquidate up to 90% of that and walk away with '
              '$90,000 cash minus the fee.',
       'title': 'How to Get $100,000+ in Business Credit at 0% APR (New LLCs) (Naam Wynn)',
       'url': 'https://www.youtube.com/watch?v=bdodeCpS6JI&t=787s',
       'video_id': 'bdodeCpS6JI'}],
 12: [{'author': 'Gap Funding | 100% Real Estate Financing',
       'channel': 'Gap Funding | 100% Real Estate Financing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:32](https://www.youtube.com/watch?v=ItOMPgJwT_4&t=212s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Long-term, this actually builds your credit. Now, turning credit into actual '
               'cash. This is a question I get every single day of the week. A title company '
               "or contractor doesn't take a swipe of your business card. You need the funds "
               'to move.',
       'timestamp': 212,
       'timestamp_label': '[00:03:32]',
       'timestamp_seconds': 212,
       'tip': 'Long-term, this actually builds your credit. Now, turning credit into actual '
              'cash. This is a question I get every single day of the week. A title company or '
              "contractor doesn't take a swipe of your business card. You need the funds to "
              'move.',
       'title': 'Credit Card Stacking for Real Estate Investors: The Same-Day Stack Nobody '
                'Explains Right (Gap Funding | 100% Real Estate Financing)',
       'url': 'https://www.youtube.com/watch?v=ItOMPgJwT_4&t=212s',
       'video_id': 'ItOMPgJwT_4'},
      {'author': 'Hard Money Mike',
       'channel': 'Hard Money Mike',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:43](https://www.youtube.com/watch?v=i2EHd_tEf1w&t=163s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'This as a lender we send the documents just like any other closing and the '
               'wire the same day we inform the title company that we will not close or fund '
               'our loan.',
       'timestamp': 163,
       'timestamp_label': '[00:02:43]',
       'timestamp_seconds': 163,
       'tip': 'This as a lender we send the documents just like any other closing and the wire '
              'the same day we inform the title company that we will not close or fund our '
              'loan.',
       'title': 'Transactional Funding: What It Is and How to Use It (Hard Money Mike)',
       'url': 'https://www.youtube.com/watch?v=i2EHd_tEf1w&t=163s',
       'video_id': 'i2EHd_tEf1w'},
      {'author': 'The Virtual Investor',
       'channel': 'The Virtual Investor',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:37](https://www.youtube.com/watch?v=kCbwtS3VKw4&t=217s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A is the end seller, B is the wholesaler. When the wholesaler finds an end '
               'buyer, they will then sign a new purchase agreement, also known as a BTOC '
               'transaction, to purchase the property at a higher price and close on the same '
               'day as the A to B transaction.',
       'timestamp': 217,
       'timestamp_label': '[00:03:37]',
       'timestamp_seconds': 217,
       'tip': 'A is the end seller, B is the wholesaler. When the wholesaler finds an end '
              'buyer, they will then sign a new purchase agreement, also known as a BTOC '
              'transaction, to purchase the property at a higher price and close on the same '
              'day as the A to B transaction.',
       'title': 'What is Transactional Funding for Real Estate Wholesalers? (The Virtual '
                'Investor)',
       'url': 'https://www.youtube.com/watch?v=kCbwtS3VKw4&t=217s',
       'video_id': 'kCbwtS3VKw4'},
      {'author': 'JAG Real Estate Lifestyle',
       'channel': 'JAG Real Estate Lifestyle',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:42](https://www.youtube.com/watch?v=E9HjXJUTsZc&t=282s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re moving into another property or they want to put the cash in the bank and "
               "let it sit for a little while before they buy something. There's a lot of "
               "reasons why people don't want to wait 30 days to close a transaction anymore, "
               'especially in California.',
       'timestamp': 282,
       'timestamp_label': '[00:04:42]',
       'timestamp_seconds': 282,
       'tip': "'re moving into another property or they want to put the cash in the bank and "
              "let it sit for a little while before they buy something. There's a lot of "
              "reasons why people don't want to wait 30 days to close a transaction anymore, "
              'especially in California.',
       'title': 'Earnest Money Explained: How Buyers Avoid Losing Their Deposit (JAG Real '
                'Estate Lifestyle)',
       'url': 'https://www.youtube.com/watch?v=E9HjXJUTsZc&t=282s',
       'video_id': 'E9HjXJUTsZc'},
      {'author': 'OrotonEquities',
       'channel': 'OrotonEquities',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:24](https://www.youtube.com/watch?v=vtoojcHUwHU&t=84s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Some transactional finance financing companies only give you 24 hours. Um, '
               "that third day really does u make a difference when you're trying to taunt a "
               'short sale, backto-back closing with the second lender, with your attorney, '
               "the buyer's attorney, and title company.",
       'timestamp': 84,
       'timestamp_label': '[00:01:24]',
       'timestamp_seconds': 84,
       'tip': 'Some transactional finance financing companies only give you 24 hours. Um, that '
              "third day really does u make a difference when you're trying to taunt a short "
              'sale, backto-back closing with the second lender, with your attorney, the '
              "buyer's attorney, and title company.",
       'title': "3-Day Transactional Funding - Oroton's STF Program (OrotonEquities)",
       'url': 'https://www.youtube.com/watch?v=vtoojcHUwHU&t=84s',
       'video_id': 'vtoojcHUwHU'},
      {'author': 'Aravision Funding',
       'channel': 'Aravision Funding',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:18](https://www.youtube.com/watch?v=4jdvXuchjXo&t=138s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Airvision Funding gives you access to capital from trusted private lenders. '
               "Visit our website for more information. And if you're ready to see what we can "
               'offer, fill out and send in the preliminary questions form and we will get '
               'back to you within one business day.',
       'timestamp': 138,
       'timestamp_label': '[00:02:18]',
       'timestamp_seconds': 138,
       'tip': 'Airvision Funding gives you access to capital from trusted private lenders. '
              "Visit our website for more information. And if you're ready to see what we can "
              'offer, fill out and send in the preliminary questions form and we will get back '
              'to you within one business day.',
       'title': 'Short-Term Bridge Loans for Real Estate Investors (Aravision Funding)',
       'url': 'https://www.youtube.com/watch?v=4jdvXuchjXo&t=138s',
       'video_id': '4jdvXuchjXo'},
      {'author': 'Biz Matthew',
       'channel': 'Biz Matthew',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:51](https://www.youtube.com/watch?v=ntGitnGf_xo&t=231s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Do is you close on the property yourself and you probably wait a week or two '
               'weeks in order to sell that property just so you can get the right buyer for.',
       'timestamp': 231,
       'timestamp_label': '[00:03:51]',
       'timestamp_seconds': 231,
       'tip': 'Do is you close on the property yourself and you probably wait a week or two '
              'weeks in order to sell that property just so you can get the right buyer for.',
       'title': 'Should You Double Closes or do Assignments in Wholesaling Real Estate (Biz '
                'Matthew)',
       'url': 'https://www.youtube.com/watch?v=ntGitnGf_xo&t=231s',
       'video_id': 'ntGitnGf_xo'},
      {'author': 'LearnREInvesting',
       'channel': 'LearnREInvesting',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:23](https://www.youtube.com/watch?v=gCae6AF4TSo&t=143s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Will be funded with the end buyer's money all within a few moments lastly the "
               'transactional funders money will be wired back to his bank account usually the '
               'same day thanks for joining us for the Real Estate Investors series on '
               'transactional funding.',
       'timestamp': 143,
       'timestamp_label': '[00:02:23]',
       'timestamp_seconds': 143,
       'tip': "Will be funded with the end buyer's money all within a few moments lastly the "
              'transactional funders money will be wired back to his bank account usually the '
              'same day thanks for joining us for the Real Estate Investors series on '
              'transactional funding.',
       'title': 'What Is Transactional Funding?| Best|Lending|Lenders|Florida '
                '(LearnREInvesting)',
       'url': 'https://www.youtube.com/watch?v=gCae6AF4TSo&t=143s',
       'video_id': 'gCae6AF4TSo'},
      {'author': 'Abdiel Garcia Rodriguez',
       'channel': 'Abdiel Garcia Rodriguez',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:12](https://www.youtube.com/watch?v=min0RpX32uc&t=252s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "The gator the fee is always based on calendar days and it's no more than 60 "
               "days for compensation it'll be at the close of escrow and it'll either be a.",
       'timestamp': 252,
       'timestamp_label': '[00:04:12]',
       'timestamp_seconds': 252,
       'tip': "The gator the fee is always based on calendar days and it's no more than 60 "
              "days for compensation it'll be at the close of escrow and it'll either be a.",
       'title': 'EMD & Transactional Funding Criteria | Gator Method 🐊 (Abdiel Garcia '
                'Rodriguez)',
       'url': 'https://www.youtube.com/watch?v=min0RpX32uc&t=252s',
       'video_id': 'min0RpX32uc'},
      {'author': 'Ryan Dossey',
       'channel': 'Ryan Dossey',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:51](https://www.youtube.com/watch?v=UlOFHwYtg7E&t=291s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Like 45 60 days left to get this particular project sold now I was on a '
               'meeting earlier this week of like what are we going to do about it.',
       'timestamp': 291,
       'timestamp_label': '[00:04:51]',
       'timestamp_seconds': 291,
       'tip': 'Like 45 60 days left to get this particular project sold now I was on a meeting '
              'earlier this week of like what are we going to do about it.',
       'title': 'Private Lender REVEALS How to Get Funding (Real Estate Insider Tips) (Ryan '
                'Dossey)',
       'url': 'https://www.youtube.com/watch?v=UlOFHwYtg7E&t=291s',
       'video_id': 'UlOFHwYtg7E'},
      {'author': 'Kelsie Toole',
       'channel': 'Kelsie Toole',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:33](https://www.youtube.com/watch?v=-9IO2PFhhdE&t=393s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That's okay that's okay because this is your home and this is your life "
               "savings and we want to make sure that it's spent correctly don't you so close "
               "with Chicago title and join me next week for Tuesday's title tip thanks guys "
               'bye.',
       'timestamp': 393,
       'timestamp_label': '[00:06:33]',
       'timestamp_seconds': 393,
       'tip': "That's okay that's okay because this is your home and this is your life savings "
              "and we want to make sure that it's spent correctly don't you so close with "
              "Chicago title and join me next week for Tuesday's title tip thanks guys bye.",
       'title': 'Tuesdays Title Tip - How to avoid wire fraud - Chicago Title (Kelsie Toole)',
       'url': 'https://www.youtube.com/watch?v=-9IO2PFhhdE&t=393s',
       'video_id': '-9IO2PFhhdE'},
      {'author': 'Velocity Channel',
       'channel': 'Velocity Channel',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:16](https://www.youtube.com/watch?v=J25bp-FJXOA&t=796s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Zero down payment using business credit we have case studies right to go from '
               'zero to one hundred thousand dollars unsecured credit in seven days.',
       'timestamp': 796,
       'timestamp_label': '[00:13:16]',
       'timestamp_seconds': 796,
       'tip': 'Zero down payment using business credit we have case studies right to go from '
              'zero to one hundred thousand dollars unsecured credit in seven days.',
       'title': "Velocity Banking and Business Credit: It's Better To Borrow $1,000,000 Than "
                'Earn It (Velocity Channel)',
       'url': 'https://www.youtube.com/watch?v=J25bp-FJXOA&t=796s',
       'video_id': 'J25bp-FJXOA'},
      {'author': 'Pace Morby',
       'channel': 'Pace Morby',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:18](https://www.youtube.com/watch?v=ho2GajBX7V8&t=18s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Week for 50 grand i'll get my money back benjamin says yes i'm familiar with "
               "gator lending are you i just invented it 20 days ago and i've done one "
               'training.',
       'timestamp': 18,
       'timestamp_label': '[00:00:18]',
       'timestamp_seconds': 18,
       'tip': "Week for 50 grand i'll get my money back benjamin says yes i'm familiar with "
              "gator lending are you i just invented it 20 days ago and i've done one "
              'training.',
       'title': 'Transactional Lending VS GATOR METHOD | Pace Morby Breakdown (Pace Morby)',
       'url': 'https://www.youtube.com/watch?v=ho2GajBX7V8&t=18s',
       'video_id': 'ho2GajBX7V8'},
      {'author': 'Flipping Mastery TV',
       'channel': 'Flipping Mastery TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:03](https://www.youtube.com/watch?v=3aAzZildhKk&t=723s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Confirm that if not her then it'll be someone else no good yeah we'll get you "
               "taken care of okay thank you you're welcome have a great day you too bye all "
               'right bye.',
       'timestamp': 723,
       'timestamp_label': '[00:12:03]',
       'timestamp_seconds': 723,
       'tip': "Confirm that if not her then it'll be someone else no good yeah we'll get you "
              "taken care of okay thank you you're welcome have a great day you too bye all "
              'right bye.',
       'title': 'Title & Closing Process EXPLAINED | Wholesale Real Estate (Flipping Mastery '
                'TV)',
       'url': 'https://www.youtube.com/watch?v=3aAzZildhKk&t=723s',
       'video_id': '3aAzZildhKk'},
      {'author': 'The Full Deal REI',
       'channel': 'The Full Deal REI',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:41](https://www.youtube.com/watch?v=H-3pmQVYvCI&t=521s)',
       'relevance': 'Attributed practitioner commentary on 24-to-72-hour escrow-locked '
                    "transactional double-close funding, earnest-money ('Gator') lending, and "
                    '0%-APR corporate credit-to-escrow liquidity velocity (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'It depends on state law and the title company. What if the buyer backs out on '
               "closing day? That's exactly why the non-refundable deposit and escrow release "
               'clause matter. Since you took title, the tax treatment may be different from '
               'an assignment.',
       'timestamp': 521,
       'timestamp_label': '[00:08:41]',
       'timestamp_seconds': 521,
       'tip': 'It depends on state law and the title company. What if the buyer backs out on '
              "closing day? That's exactly why the non-refundable deposit and escrow release "
              'clause matter. Since you took title, the tax treatment may be different from an '
              'assignment.',
       'title': 'How Much Does Transactional Funding Cost (Real Example + What Lenders '
                'Require) (The Full Deal REI)',
       'url': 'https://www.youtube.com/watch?v=H-3pmQVYvCI&t=521s',
       'video_id': 'H-3pmQVYvCI'}]}
